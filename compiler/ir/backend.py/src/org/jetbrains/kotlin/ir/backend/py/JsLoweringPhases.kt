/*
 * Copyright 2010-2018 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.ir.backend.py

import org.jetbrains.kotlin.backend.common.*
import org.jetbrains.kotlin.backend.common.lower.*
import org.jetbrains.kotlin.backend.common.lower.inline.FunctionInlining
import org.jetbrains.kotlin.backend.common.lower.inline.LocalClassesExtractionFromInlineFunctionsLowering
import org.jetbrains.kotlin.backend.common.lower.inline.LocalClassesInInlineFunctionsLowering
import org.jetbrains.kotlin.backend.common.lower.inline.LocalClassesInInlineLambdasLowering
import org.jetbrains.kotlin.backend.common.lower.loops.ForLoopsLowering
import org.jetbrains.kotlin.backend.common.lower.optimizations.FoldConstantLowering
import org.jetbrains.kotlin.backend.common.lower.optimizations.PropertyAccessorInlineLowering
import org.jetbrains.kotlin.backend.common.phaser.*
import org.jetbrains.kotlin.ir.IrElement
import org.jetbrains.kotlin.ir.backend.py.lower.*
import org.jetbrains.kotlin.ir.backend.py.lower.calls.CallsLowering
import org.jetbrains.kotlin.ir.backend.py.lower.cleanup.CleanupLowering
import org.jetbrains.kotlin.ir.backend.py.lower.coroutines.PySuspendFunctionsLowering
import org.jetbrains.kotlin.ir.backend.py.lower.inline.CopyInlineFunctionBodyLowering
import org.jetbrains.kotlin.ir.backend.py.lower.inline.RemoveInlineDeclarationsWithReifiedTypeParametersLowering
import org.jetbrains.kotlin.ir.backend.py.lower.inline.pyRecordExtractedLocalClasses
import org.jetbrains.kotlin.ir.declarations.IrModuleFragment

private fun makePyModulePhase(
    lowering: (PyIrBackendContext) -> FileLoweringPass,
    name: String,
    description: String,
    prerequisite: Set<NamedCompilerPhase<PyIrBackendContext, *>> = emptySet()
): NamedCompilerPhase<PyIrBackendContext, Iterable<IrModuleFragment>> = makeCustomPyModulePhase(
    op = { context, modules -> lowering(context).lower(modules) },
    name = name,
    description = description,
    prerequisite = prerequisite
)

private fun makeCustomPyModulePhase(
    op: (PyIrBackendContext, IrModuleFragment) -> Unit,
    description: String,
    name: String,
    prerequisite: Set<NamedCompilerPhase<PyIrBackendContext, *>> = emptySet()
): NamedCompilerPhase<PyIrBackendContext, Iterable<IrModuleFragment>> = NamedCompilerPhase(
    name = name,
    description = description,
    prerequisite = prerequisite,
    lower = object : SameTypeCompilerPhase<PyIrBackendContext, Iterable<IrModuleFragment>> {
        override fun invoke(
            phaseConfig: PhaseConfig,
            phaserState: PhaserState<Iterable<IrModuleFragment>>,
            context: PyIrBackendContext,
            input: Iterable<IrModuleFragment>
        ): Iterable<IrModuleFragment> {
            input.forEach { module ->
                op(context, module)
            }
            return input
        }
    },
    actions = setOf(defaultDumper.toMultiModuleAction(), validationAction.toMultiModuleAction()),
)

private fun <C> Action<IrElement, C>.toMultiModuleAction(): Action<Iterable<IrModuleFragment>, C> {
    return { state, modules, context ->
        modules.forEach { module ->
            this(state, module, context)
        }
    }
}

sealed class Lowering(val name: String) {
    abstract val modulePhase: NamedCompilerPhase<PyIrBackendContext, Iterable<IrModuleFragment>>
}

class DeclarationLowering(
    name: String,
    description: String,
    prerequisite: Set<NamedCompilerPhase<PyIrBackendContext, *>> = emptySet(),
    private val factory: (PyIrBackendContext) -> DeclarationTransformer
) : Lowering(name) {
    fun declarationTransformer(context: PyIrBackendContext): DeclarationTransformer {
        return factory(context)
    }

    override val modulePhase = makePyModulePhase(factory, name, description, prerequisite)
}

class BodyLowering(
    name: String,
    description: String,
    prerequisite: Set<NamedCompilerPhase<PyIrBackendContext, *>> = emptySet(),
    private val factory: (PyIrBackendContext) -> BodyLoweringPass
) : Lowering(name) {
    override val modulePhase = makePyModulePhase(factory, name, description, prerequisite)
}

class ModuleLowering(
    name: String,
    override val modulePhase: NamedCompilerPhase<PyIrBackendContext, Iterable<IrModuleFragment>>
) : Lowering(name)

private fun makeDeclarationTransformerPhase(
    lowering: (PyIrBackendContext) -> DeclarationTransformer,
    name: String,
    description: String,
    prerequisite: Set<Lowering> = emptySet()
) = DeclarationLowering(name, description, prerequisite.map { it.modulePhase }.toSet(), lowering)

private fun makeBodyLoweringPhase(
    lowering: (PyIrBackendContext) -> BodyLoweringPass,
    name: String,
    description: String,
    prerequisite: Set<Lowering> = emptySet()
) = BodyLowering(name, description, prerequisite.map { it.modulePhase }.toSet(), lowering)

fun NamedCompilerPhase<PyIrBackendContext, Iterable<IrModuleFragment>>.toModuleLowering() = ModuleLowering(this.name, this)

private val validateIrBeforeLowering = makeCustomPyModulePhase(
    ::validationCallback,
    name = "ValidateIrBeforeLowering",
    description = "Validate IR before lowering"
).toModuleLowering()

private val validateIrAfterLowering = makeCustomPyModulePhase(
    ::validationCallback,
    name = "ValidateIrAfterLowering",
    description = "Validate IR after lowering"
).toModuleLowering()

val scriptRemoveReceiverLowering = makePyModulePhase(
    ::ScriptRemoveReceiverLowering,
    name = "ScriptRemoveReceiver",
    description = "Remove receivers for declarations in script"
).toModuleLowering()

val createScriptFunctionsPhase = makePyModulePhase(
    ::CreateScriptFunctionsPhase,
    name = "CreateScriptFunctionsPhase",
    description = "Create functions for initialize and evaluate script"
).toModuleLowering()

private val expectDeclarationsRemovingPhase = makeDeclarationTransformerPhase(
    ::ExpectDeclarationsRemoveLowering,
    name = "ExpectDeclarationsRemoving",
    description = "Remove expect declaration from module fragment"
)

private val lateinitNullableFieldsPhase = makeDeclarationTransformerPhase(
    ::NullableFieldsForLateinitCreationLowering,
    name = "LateinitNullableFields",
    description = "Create nullable fields for lateinit properties"
)

private val lateinitDeclarationLoweringPhase = makeDeclarationTransformerPhase(
    ::NullableFieldsDeclarationLowering,
    name = "LateinitDeclarations",
    description = "Reference nullable fields from properties and getters + insert checks"
)

private val lateinitUsageLoweringPhase = makeBodyLoweringPhase(
    ::LateinitUsageLowering,
    name = "LateinitUsage",
    description = "Insert checks for lateinit field references"
)

private val kotlinNothingValueExceptionPhase = makeBodyLoweringPhase(
    ::KotlinNothingValueExceptionLowering,
    name = "KotlinNothingValueException",
    description = "Throw proper exception for calls returning value of type 'kotlin.Nothing'"
)

private val stripTypeAliasDeclarationsPhase = makeDeclarationTransformerPhase(
    { StripTypeAliasDeclarationsLowering() },
    name = "StripTypeAliasDeclarations",
    description = "Strip typealias declarations"
)

private val arrayConstructorPhase = makeBodyLoweringPhase(
    ::ArrayConstructorLowering,
    name = "ArrayConstructor",
    description = "Transform `Array(size) { index -> value }` into a loop"
)

private val sharedVariablesLoweringPhase = makeBodyLoweringPhase(
    ::SharedVariablesLowering,
    name = "SharedVariablesLowering",
    description = "Box captured mutable variables",
    prerequisite = setOf(lateinitDeclarationLoweringPhase, lateinitUsageLoweringPhase)
)

private val localClassesInInlineLambdasPhase = makeBodyLoweringPhase(
    ::LocalClassesInInlineLambdasLowering,
    name = "LocalClassesInInlineLambdasPhase",
    description = "Extract local classes from inline lambdas"
)

private val localClassesInInlineFunctionsPhase = makeBodyLoweringPhase(
    ::LocalClassesInInlineFunctionsLowering,
    name = "LocalClassesInInlineFunctionsPhase",
    description = "Extract local classes from inline functions"
)

private val localClassesExtractionFromInlineFunctionsPhase = makeBodyLoweringPhase(
    { context -> LocalClassesExtractionFromInlineFunctionsLowering(context, BackendContext::pyRecordExtractedLocalClasses) },
    name = "localClassesExtractionFromInlineFunctionsPhase",
    description = "Move local classes from inline functions into nearest declaration container",
    prerequisite = setOf(localClassesInInlineFunctionsPhase)
)

private val functionInliningPhase = makeBodyLoweringPhase(
    ::FunctionInlining,
    name = "FunctionInliningPhase",
    description = "Perform function inlining",
    prerequisite = setOf(
        expectDeclarationsRemovingPhase, sharedVariablesLoweringPhase,
        localClassesInInlineLambdasPhase, localClassesExtractionFromInlineFunctionsPhase
    )
)

private val copyInlineFunctionBodyLoweringPhase = makeDeclarationTransformerPhase(
    ::CopyInlineFunctionBodyLowering,
    name = "CopyInlineFunctionBody",
    description = "Copy inline function body",
    prerequisite = setOf(functionInliningPhase)
)

private val removeInlineDeclarationsWithReifiedTypeParametersLoweringPhase = makeDeclarationTransformerPhase(
    { RemoveInlineDeclarationsWithReifiedTypeParametersLowering() },
    name = "RemoveInlineFunctionsWithReifiedTypeParametersLowering",
    description = "Remove Inline functions with reified parameters from context",
    prerequisite = setOf(functionInliningPhase)
)

private val throwableSuccessorsLoweringPhase = makeBodyLoweringPhase(
    ::ThrowableLowering,
    name = "ThrowableLowering",
    description = "Link kotlin.Throwable and JavaScript Error together to provide proper interop between language and platform exceptions"
)

private val tailrecLoweringPhase = makeBodyLoweringPhase(
    ::TailrecLowering,
    name = "TailrecLowering",
    description = "Replace `tailrec` callsites with equivalent loop"
)

private val enumClassConstructorLoweringPhase = makeDeclarationTransformerPhase(
    ::EnumClassConstructorLowering,
    name = "EnumClassConstructorLowering",
    description = "Transform Enum Class into regular Class"
)

private val enumClassConstructorBodyLoweringPhase = makeBodyLoweringPhase(
    ::EnumClassConstructorBodyTransformer,
    name = "EnumClassConstructorBodyLowering",
    description = "Transform Enum Class into regular Class"
)

private val enumEntryInstancesLoweringPhase = makeDeclarationTransformerPhase(
    ::EnumEntryInstancesLowering,
    name = "EnumEntryInstancesLowering",
    description = "Create instance variable for each enum entry initialized with `null`",
    prerequisite = setOf(enumClassConstructorLoweringPhase)
)

private val enumEntryInstancesBodyLoweringPhase = makeBodyLoweringPhase(
    ::EnumEntryInstancesBodyLowering,
    name = "EnumEntryInstancesBodyLowering",
    description = "Insert enum entry field initialization into correxposnding class constructors",
    prerequisite = setOf(enumEntryInstancesLoweringPhase)
)

private val enumClassCreateInitializerLoweringPhase = makeDeclarationTransformerPhase(
    ::EnumClassCreateInitializerLowering,
    name = "EnumClassCreateInitializerLowering",
    description = "Create initializer for enum entries",
    prerequisite = setOf(enumClassConstructorLoweringPhase)
)

private val enumEntryCreateGetInstancesFunsLoweringPhase = makeDeclarationTransformerPhase(
    ::EnumEntryCreateGetInstancesFunsLowering,
    name = "EnumEntryCreateGetInstancesFunsLowering",
    description = "Create enumEntry_getInstance functions",
    prerequisite = setOf(enumClassConstructorLoweringPhase)
)

private val enumSyntheticFunsLoweringPhase = makeDeclarationTransformerPhase(
    ::EnumSyntheticFunctionsLowering,
    name = "EnumSyntheticFunctionsLowering",
    description = "Implement `valueOf` and `values`",
    prerequisite = setOf(enumClassConstructorLoweringPhase, enumClassCreateInitializerLoweringPhase)
)

private val enumUsageLoweringPhase = makeBodyLoweringPhase(
    ::EnumUsageLowering,
    name = "EnumUsageLowering",
    description = "Replace enum access with invocation of corresponding function",
    prerequisite = setOf(enumEntryCreateGetInstancesFunsLoweringPhase)
)

private val externalEnumUsageLoweringPhase = makeBodyLoweringPhase(
    ::ExternalEnumUsagesLowering,
    name = "ExternalEnumUsagesLowering",
    description = "Replace external enum entry accesses with field accesses"
)

private val enumEntryRemovalLoweringPhase = makeDeclarationTransformerPhase(
    ::EnumClassRemoveEntriesLowering,
    name = "EnumEntryRemovalLowering",
    description = "Replace enum entry with corresponding class",
    prerequisite = setOf(enumUsageLoweringPhase)
)

private val returnableBlockLoweringPhase = makeBodyLoweringPhase(
    ::ReturnableBlockLowering,
    name = "ReturnableBlockLowering",
    description = "Replace returnable block with do-while loop",
    prerequisite = setOf(functionInliningPhase)
)

private val rangeContainsLoweringPhase = makeBodyLoweringPhase(
    ::RangeContainsLowering,
    name = "RangeContainsLowering",
    description = "[Optimization] Optimizes calls to contains() for ClosedRanges"
)

private val forLoopsLoweringPhase = makeBodyLoweringPhase(
    ::ForLoopsLowering,
    name = "ForLoopsLowering",
    description = "[Optimization] For loops lowering"
)

private val propertyAccessorInlinerLoweringPhase = makeBodyLoweringPhase(
    ::PropertyAccessorInlineLowering,
    name = "PropertyAccessorInlineLowering",
    description = "[Optimization] Inline property accessors"
)

private val copyPropertyAccessorBodiesLoweringPass = makeDeclarationTransformerPhase(
    ::CopyAccessorBodyLowerings,
    name = "CopyAccessorBodyLowering",
    description = "Copy accessor bodies so that ist can be safely read in PropertyAccessorInlineLowering",
    prerequisite = setOf(propertyAccessorInlinerLoweringPhase)
)

private val foldConstantLoweringPhase = makeBodyLoweringPhase(
    { FoldConstantLowering(it, true) },
    name = "FoldConstantLowering",
    description = "[Optimization] Constant Folding",
    prerequisite = setOf(propertyAccessorInlinerLoweringPhase)
)

private val localDelegatedPropertiesLoweringPhase = makeBodyLoweringPhase(
    { LocalDelegatedPropertiesLowering() },
    name = "LocalDelegatedPropertiesLowering",
    description = "Transform Local Delegated properties"
)

private val localDeclarationsLoweringPhase = makeBodyLoweringPhase(
    ::LocalDeclarationsLowering,
    name = "LocalDeclarationsLowering",
    description = "Move local declarations into nearest declaration container",
    prerequisite = setOf(sharedVariablesLoweringPhase, localDelegatedPropertiesLoweringPhase)
)

private val localClassExtractionPhase = makeBodyLoweringPhase(
    { context -> LocalClassPopupLowering(context, BackendContext::pyRecordExtractedLocalClasses) },
    name = "LocalClassExtractionPhase",
    description = "Move local declarations into nearest declaration container",
    prerequisite = setOf(localDeclarationsLoweringPhase)
)

private val innerClassesLoweringPhase = makeDeclarationTransformerPhase(
    { context -> InnerClassesLowering(context, context.innerClassesSupport) },
    name = "InnerClassesLowering",
    description = "Capture outer this reference to inner class"
)

private val innerClassesMemberBodyLoweringPhase = makeBodyLoweringPhase(
    { context -> InnerClassesMemberBodyLowering(context, context.innerClassesSupport) },
    name = "InnerClassesMemberBody",
    description = "Replace `this` with 'outer this' field references",
    prerequisite = setOf(innerClassesLoweringPhase)
)

private val innerClassConstructorCallsLoweringPhase = makeBodyLoweringPhase(
    { context -> InnerClassConstructorCallsLowering(context, context.innerClassesSupport) },
    name = "InnerClassConstructorCallsLowering",
    description = "Replace inner class constructor invocation"
)

private val suspendFunctionsLoweringPhase = makeBodyLoweringPhase(
    ::PySuspendFunctionsLowering,
    name = "SuspendFunctionsLowering",
    description = "Transform suspend functions into CoroutineImpl instance and build state machine"
)

private val privateMembersLoweringPhase = makeDeclarationTransformerPhase(
    ::PrivateMembersLowering,
    name = "PrivateMembersLowering",
    description = "Extract private members from classes"
)

private val privateMemberUsagesLoweringPhase = makeBodyLoweringPhase(
    ::PrivateMemberBodiesLowering,
    name = "PrivateMemberUsagesLowering",
    description = "Rewrite the private member usages"
)

private val propertyReferenceLoweringPhase = makeBodyLoweringPhase(
    ::PropertyReferenceLowering,
    name = "PropertyReferenceLowering",
    description = "Transform property references"
)

private val interopCallableReferenceLoweringPhase = makeBodyLoweringPhase(
    ::InteropCallableReferenceLowering,
    name = "InteropCallableReferenceLowering",
    description = "Interop layer for function references and lambdas",
    prerequisite = setOf(
        suspendFunctionsLoweringPhase,
        localDeclarationsLoweringPhase,
        localDelegatedPropertiesLoweringPhase,
    )
)

private val defaultArgumentStubGeneratorPhase = makeDeclarationTransformerPhase(
    ::PyDefaultArgumentStubGenerator,
    name = "DefaultArgumentStubGenerator",
    description = "Generate synthetic stubs for functions with default parameter values"
)

private val defaultArgumentPatchOverridesPhase = makeDeclarationTransformerPhase(
    ::DefaultParameterPatchOverridenSymbolsLowering,
    name = "DefaultArgumentsPatchOverrides",
    description = "Patch overrides for fake override dispatch functions",
    prerequisite = setOf(defaultArgumentStubGeneratorPhase)
)

private val defaultParameterInjectorPhase = makeBodyLoweringPhase(
    { context -> DefaultParameterInjector(context, skipExternalMethods = true, forceSetOverrideSymbols = false) },
    name = "DefaultParameterInjector",
    description = "Replace callsite with default parameters with corresponding stub function",
    prerequisite = setOf(interopCallableReferenceLoweringPhase, innerClassesLoweringPhase)
)

private val defaultParameterCleanerPhase = makeDeclarationTransformerPhase(
    ::DefaultParameterCleaner,
    name = "DefaultParameterCleaner",
    description = "Clean default parameters up"
)


private val exportedDefaultParameterStubPhase = makeDeclarationTransformerPhase(
    ::ExportedDefaultParameterStub,
    name = "ExportedDefaultParameterStub",
    description = "Generates default stub for exported entity and renames the non-default counterpart"
)

private val pyDefaultCallbackGeneratorPhase = makeBodyLoweringPhase(
    ::PyDefaultCallbackGenerator,
    name = "PyDefaultCallbackGenerator",
    description = "Build binding for super calls with default parameters"
)

private val propertiesLoweringPhase = makeDeclarationTransformerPhase(
    { PropertiesLowering() },
    name = "PropertiesLowering",
    description = "Move fields and accessors out from its property"
)

private val primaryConstructorLoweringPhase = makeDeclarationTransformerPhase(
    ::PrimaryConstructorLowering,
    name = "PrimaryConstructorLowering",
    description = "Creates primary constructor if it doesn't exist",
    prerequisite = setOf(enumClassConstructorLoweringPhase)
)

private val delegateToPrimaryConstructorLoweringPhase = makeBodyLoweringPhase(
    ::DelegateToSyntheticPrimaryConstructor,
    name = "DelegateToSyntheticPrimaryConstructor",
    description = "Delegates to synthetic primary constructor",
    prerequisite = setOf(primaryConstructorLoweringPhase)
)

private val annotationConstructorLowering = makeDeclarationTransformerPhase(
    ::AnnotationConstructorLowering,
    name = "AnnotationConstructorLowering",
    description = "Generate annotation constructor body"
)

private val initializersLoweringPhase = makeBodyLoweringPhase(
    ::InitializersLowering,
    name = "InitializersLowering",
    description = "Merge init block and field initializers into [primary] constructor",
    prerequisite = setOf(
        enumClassConstructorLoweringPhase, primaryConstructorLoweringPhase, annotationConstructorLowering, localClassExtractionPhase
    )
)

private val initializersCleanupLoweringPhase = makeDeclarationTransformerPhase(
    ::InitializersCleanupLowering,
    name = "InitializersCleanupLowering",
    description = "Remove non-static anonymous initializers and field init expressions",
    prerequisite = setOf(initializersLoweringPhase)
)

private val multipleCatchesLoweringPhase = makeBodyLoweringPhase(
    ::MultipleCatchesLowering,
    name = "MultipleCatchesLowering",
    description = "Replace multiple catches with single one"
)

private val errorExpressionLoweringPhase = makeBodyLoweringPhase(
    ::PyErrorExpressionLowering,
    name = "errorExpressionLoweringPhase",
    description = "Transform error expressions into simple ir code",
    prerequisite = setOf(multipleCatchesLoweringPhase)
)

private val errorDeclarationLoweringPhase = makeDeclarationTransformerPhase(
    ::PyErrorDeclarationLowering,
    name = "errorDeclarationLoweringPhase",
    description = "Transform error declarations into simple ir code"
)

private val bridgesConstructionPhase = makeDeclarationTransformerPhase(
    ::PyBridgesConstruction,
    name = "BridgesConstruction",
    description = "Generate bridges",
    prerequisite = setOf(suspendFunctionsLoweringPhase)
)

private val singleAbstractMethodPhase = makeBodyLoweringPhase(
    ::PySingleAbstractMethodLowering,
    name = "SingleAbstractMethod",
    description = "Replace SAM conversions with instances of interface-implementing classes"
)

private val typeOperatorLoweringPhase = makeBodyLoweringPhase(
    ::TypeOperatorLowering,
    name = "TypeOperatorLowering",
    description = "Lower IrTypeOperator with corresponding logic",
    prerequisite = setOf(
        bridgesConstructionPhase,
        removeInlineDeclarationsWithReifiedTypeParametersLoweringPhase,
        singleAbstractMethodPhase, errorExpressionLoweringPhase
    )
)

private val secondaryConstructorLoweringPhase = makeDeclarationTransformerPhase(
    ::SecondaryConstructorLowering,
    name = "SecondaryConstructorLoweringPhase",
    description = "Generate static functions for each secondary constructor",
    prerequisite = setOf(innerClassesLoweringPhase)
)

private val secondaryFactoryInjectorLoweringPhase = makeBodyLoweringPhase(
    ::SecondaryFactoryInjectorLowering,
    name = "SecondaryFactoryInjectorLoweringPhase",
    description = "Replace usage of secondary constructor with corresponding static function",
    prerequisite = setOf(innerClassesLoweringPhase)
)

private val constLoweringPhase = makeBodyLoweringPhase(
    ::ConstLowering,
    name = "ConstLowering",
    description = "Wrap Long and Char constants into constructor invocation"
)

private val inlineClassDeclarationLoweringPhase = makeDeclarationTransformerPhase(
    { InlineClassLowering(it).inlineClassDeclarationLowering },
    name = "InlineClassDeclarationLowering",
    description = "Handle inline class declarations"
)

private val inlineClassUsageLoweringPhase = makeBodyLoweringPhase(
    { InlineClassLowering(it).inlineClassUsageLowering },
    name = "InlineClassUsageLowering",
    description = "Handle inline class usages",
    prerequisite = setOf(
        // Const lowering generates inline class constructors for unsigned integers
        // which should be lowered by this lowering
        constLoweringPhase
    )
)

private val autoboxingTransformerPhase = makeBodyLoweringPhase(
    ::AutoboxingTransformer,
    name = "AutoboxingTransformer",
    description = "Insert box/unbox intrinsics"
)

private val blockDecomposerLoweringPhase = makeBodyLoweringPhase(
    ::PyBlockDecomposerLowering,
    name = "BlockDecomposerLowering",
    description = "Transform statement-like-expression nodes into pure-statement to make it easily transform into Py",
    prerequisite = setOf(typeOperatorLoweringPhase, suspendFunctionsLoweringPhase)
)

private val classReferenceLoweringPhase = makeBodyLoweringPhase(
    ::ClassReferenceLowering,
    name = "ClassReferenceLowering",
    description = "Handle class references"
)

private val primitiveCompanionLoweringPhase = makeBodyLoweringPhase(
    ::PrimitiveCompanionLowering,
    name = "PrimitiveCompanionLowering",
    description = "Replace common companion object access with platform one"
)

private val callsLoweringPhase = makeBodyLoweringPhase(
    ::CallsLowering,
    name = "CallsLowering",
    description = "Handle intrinsics"
)

private val objectDeclarationLoweringPhase = makeDeclarationTransformerPhase(
    ::ObjectDeclarationLowering,
    name = "ObjectDeclarationLowering",
    description = "Create lazy object instance generator functions"
)

private val invokeStaticInitializersPhase = makeBodyLoweringPhase(
    ::InvokeStaticInitializersLowering,
    name = "IntroduceStaticInitializersLowering",
    description = "Invoke companion object's initializers from companion object in object constructor",
    prerequisite = setOf(objectDeclarationLoweringPhase)
)

private val objectUsageLoweringPhase = makeBodyLoweringPhase(
    ::ObjectUsageLowering,
    name = "ObjectUsageLowering",
    description = "Transform IrGetObjectValue into instance generator call"
)

private val captureStackTraceInThrowablesPhase = makeBodyLoweringPhase(
    ::CaptureStackTraceInThrowables,
    name = "CaptureStackTraceInThrowables",
    description = "Capture stack trace in Throwable constructors"
)

private val cleanupLoweringPhase = makeBodyLoweringPhase(
    { CleanupLowering() },
    name = "CleanupLowering",
    description = "Clean up IR before codegen"
)

private val loweringList = listOf(
    scriptRemoveReceiverLowering,
    validateIrBeforeLowering,
    expectDeclarationsRemovingPhase,
    stripTypeAliasDeclarationsPhase,
    arrayConstructorPhase,
    lateinitNullableFieldsPhase,
    lateinitDeclarationLoweringPhase,
    lateinitUsageLoweringPhase,
    sharedVariablesLoweringPhase,
    localClassesInInlineLambdasPhase,
    localClassesInInlineFunctionsPhase,
    localClassesExtractionFromInlineFunctionsPhase,
    functionInliningPhase,
    copyInlineFunctionBodyLoweringPhase,
    removeInlineDeclarationsWithReifiedTypeParametersLoweringPhase,
    createScriptFunctionsPhase,
    singleAbstractMethodPhase,
    tailrecLoweringPhase,
    enumClassConstructorLoweringPhase,
    enumClassConstructorBodyLoweringPhase,
    localDelegatedPropertiesLoweringPhase,
    localDeclarationsLoweringPhase,
    localClassExtractionPhase,
    innerClassesLoweringPhase,
    innerClassesMemberBodyLoweringPhase,
    innerClassConstructorCallsLoweringPhase,
    propertiesLoweringPhase,
    primaryConstructorLoweringPhase,
    delegateToPrimaryConstructorLoweringPhase,
    annotationConstructorLowering,
    initializersLoweringPhase,
    initializersCleanupLoweringPhase,
    kotlinNothingValueExceptionPhase,
    // Common prefix ends
    enumEntryInstancesLoweringPhase,
    enumEntryInstancesBodyLoweringPhase,
    enumClassCreateInitializerLoweringPhase,
    enumEntryCreateGetInstancesFunsLoweringPhase,
    enumSyntheticFunsLoweringPhase,
    enumUsageLoweringPhase,
    externalEnumUsageLoweringPhase,
    enumEntryRemovalLoweringPhase,
    suspendFunctionsLoweringPhase,
    propertyReferenceLoweringPhase,
    interopCallableReferenceLoweringPhase,
    returnableBlockLoweringPhase,
    rangeContainsLoweringPhase,
    forLoopsLoweringPhase,
    primitiveCompanionLoweringPhase,
    propertyAccessorInlinerLoweringPhase,
    copyPropertyAccessorBodiesLoweringPass,
    foldConstantLoweringPhase,
    privateMembersLoweringPhase,
    privateMemberUsagesLoweringPhase,
    exportedDefaultParameterStubPhase,
    defaultArgumentStubGeneratorPhase,
    defaultArgumentPatchOverridesPhase,
    defaultParameterInjectorPhase,
    defaultParameterCleanerPhase,
    pyDefaultCallbackGeneratorPhase,
    throwableSuccessorsLoweringPhase,
    multipleCatchesLoweringPhase,
    errorExpressionLoweringPhase,
    errorDeclarationLoweringPhase,
    bridgesConstructionPhase,
    typeOperatorLoweringPhase,
    secondaryConstructorLoweringPhase,
    secondaryFactoryInjectorLoweringPhase,
    classReferenceLoweringPhase,
    constLoweringPhase,
    inlineClassDeclarationLoweringPhase,
    inlineClassUsageLoweringPhase,
    autoboxingTransformerPhase,
    blockDecomposerLoweringPhase,
    objectDeclarationLoweringPhase,
    invokeStaticInitializersPhase,
    objectUsageLoweringPhase,
    captureStackTraceInThrowablesPhase,
    callsLoweringPhase,
    cleanupLoweringPhase,
    validateIrAfterLowering
)

val pyPhases = NamedCompilerPhase(
    name = "IrModuleLowering",
    description = "IR module lowering",
    lower = loweringList.map {
        @Suppress("USELESS_CAST")
        it.modulePhase as CompilerPhase<PyIrBackendContext, Iterable<IrModuleFragment>, Iterable<IrModuleFragment>>
    }.reduce { acc, lowering -> acc.then(lowering) },
    actions = setOf(defaultDumper.toMultiModuleAction(), validationAction.toMultiModuleAction()),
    nlevels = 1
)
