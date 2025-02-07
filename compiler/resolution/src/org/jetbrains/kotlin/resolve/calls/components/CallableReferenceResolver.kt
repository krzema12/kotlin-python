/*
 * Copyright 2010-2017 JetBrains s.r.o.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.jetbrains.kotlin.resolve.calls.components

import org.jetbrains.kotlin.builtins.KotlinBuiltIns
import org.jetbrains.kotlin.descriptors.ModuleDescriptor
import org.jetbrains.kotlin.resolve.calls.context.CheckArgumentTypesMode
import org.jetbrains.kotlin.resolve.calls.inference.ConstraintSystemBuilder
import org.jetbrains.kotlin.resolve.calls.inference.ConstraintSystemOperation
import org.jetbrains.kotlin.resolve.calls.inference.components.ConstraintInjector
import org.jetbrains.kotlin.resolve.calls.inference.components.NewTypeSubstitutor
import org.jetbrains.kotlin.resolve.calls.model.*
import org.jetbrains.kotlin.resolve.calls.results.*
import org.jetbrains.kotlin.resolve.calls.tower.*
import org.jetbrains.kotlin.types.UnwrappedType
import org.jetbrains.kotlin.types.checker.KotlinTypeRefiner
import org.jetbrains.kotlin.util.CancellationChecker


class CallableReferenceOverloadConflictResolver(
    builtIns: KotlinBuiltIns,
    module: ModuleDescriptor,
    specificityComparator: TypeSpecificityComparator,
    platformOverloadsSpecificityComparator: PlatformOverloadsSpecificityComparator,
    cancellationChecker: CancellationChecker,
    statelessCallbacks: KotlinResolutionStatelessCallbacks,
    constraintInjector: ConstraintInjector,
    kotlinTypeRefiner: KotlinTypeRefiner,
) : OverloadingConflictResolver<CallableReferenceCandidate>(
    builtIns,
    module,
    specificityComparator,
    platformOverloadsSpecificityComparator,
    cancellationChecker,
    { it.candidate },
    { statelessCallbacks.createConstraintSystemForOverloadResolution(constraintInjector, builtIns) },
    Companion::createFlatSignature,
    { null },
    { statelessCallbacks.isDescriptorFromSource(it) },
    null,
    kotlinTypeRefiner,
) {
    companion object {
        private fun createFlatSignature(candidate: CallableReferenceCandidate) =
            FlatSignature.createFromReflectionType(
                candidate, candidate.candidate, candidate.numDefaults, hasBoundExtensionReceiver = candidate.extensionReceiver != null,
                candidate.reflectionCandidateType
            )
    }
}


class CallableReferenceResolver(
    private val towerResolver: TowerResolver,
    private val callableReferenceOverloadConflictResolver: CallableReferenceOverloadConflictResolver,
    private val callComponents: KotlinCallComponents
) {

    fun processCallableReferenceArgument(
        csBuilder: ConstraintSystemBuilder,
        resolvedAtom: ResolvedCallableReferenceAtom,
        diagnosticsHolder: KotlinDiagnosticsHolder,
        resolutionCallbacks: KotlinResolutionCallbacks
    ) {
        val argument = resolvedAtom.atom
        val expectedType = resolvedAtom.expectedType?.let { (csBuilder.buildCurrentSubstitutor() as NewTypeSubstitutor).safeSubstitute(it) }

        val scopeTower = callComponents.statelessCallbacks.getScopeTowerForCallableReferenceArgument(argument)
        val candidates = runRHSResolution(scopeTower, argument, expectedType, csBuilder, resolutionCallbacks) { checkCallableReference ->
            csBuilder.runTransaction { checkCallableReference(this); false }
        }

        if (candidates.size > 1 && resolvedAtom is EagerCallableReferenceAtom) {
            if (candidates.all { it.resultingApplicability.isInapplicable }) {
                diagnosticsHolder.addDiagnostic(CallableReferenceCandidatesAmbiguity(argument, candidates))
            }

            resolvedAtom.setAnalyzedResults(
                candidate = null,
                subResolvedAtoms = listOf(resolvedAtom.transformToPostponed())
            )
            return
        }

        val chosenCandidate = candidates.singleOrNull()
        if (chosenCandidate != null) {
            val (toFreshSubstitutor, diagnostic) = with(chosenCandidate) {
                csBuilder.checkCallableReference(
                    argument, dispatchReceiver, extensionReceiver, candidate,
                    reflectionCandidateType, expectedType, scopeTower.lexicalScope.ownerDescriptor
                )
            }
            (chosenCandidate.diagnostics + diagnostic).filterNotNull().forEach {
                val transformedDiagnostic = when (it) {
                    is CompatibilityWarning -> CompatibilityWarningOnArgument(argument, it.candidate)
                    is VisibilityError -> VisibilityErrorOnArgument(argument, it.invisibleMember)
                    else -> it
                }
                diagnosticsHolder.addDiagnostic(transformedDiagnostic)
            }
            chosenCandidate.freshSubstitutor = toFreshSubstitutor
        } else {
            if (candidates.isEmpty()) {
                diagnosticsHolder.addDiagnostic(NoneCallableReferenceCandidates(argument))
            } else {
                diagnosticsHolder.addDiagnostic(CallableReferenceCandidatesAmbiguity(argument, candidates))
            }
        }

        // todo -- create this inside CallableReferencesCandidateFactory
        val subKtArguments = listOfNotNull(buildResolvedKtArgument(argument.lhsResult))

        resolvedAtom.setAnalyzedResults(chosenCandidate, subKtArguments)
    }

    private fun buildResolvedKtArgument(lhsResult: LHSResult): ResolvedAtom? {
        if (lhsResult !is LHSResult.Expression) return null
        val lshCallArgument = lhsResult.lshCallArgument
        return when (lshCallArgument) {
            is SubKotlinCallArgument -> lshCallArgument.callResult
            is ExpressionKotlinCallArgument -> ResolvedExpressionAtom(lshCallArgument)
            else -> unexpectedArgument(lshCallArgument)
        }
    }

    private fun runRHSResolution(
        scopeTower: ImplicitScopeTower,
        callableReference: CallableReferenceKotlinCallArgument,
        expectedType: UnwrappedType?, // this type can have not fixed type variable inside
        csBuilder: ConstraintSystemBuilder,
        resolutionCallbacks: KotlinResolutionCallbacks,
        compatibilityChecker: ((ConstraintSystemOperation) -> Unit) -> Unit // you can run anything throw this operation and all this operation will be rolled back
    ): Set<CallableReferenceCandidate> {
        val factory = CallableReferencesCandidateFactory(
            callableReference, callComponents, scopeTower, compatibilityChecker, expectedType, csBuilder, resolutionCallbacks
        )
        val processor = createCallableReferenceProcessor(factory)
        val candidates = towerResolver.runResolve(scopeTower, processor, useOrder = true, name = callableReference.rhsName)
        return callableReferenceOverloadConflictResolver.chooseMaximallySpecificCandidates(
            candidates,
            CheckArgumentTypesMode.CHECK_VALUE_ARGUMENTS,
            discriminateGenerics = false // we can't specify generics explicitly for callable references
        )
    }
}

