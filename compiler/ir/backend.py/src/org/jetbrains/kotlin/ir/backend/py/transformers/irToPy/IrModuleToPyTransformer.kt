/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.ir.backend.py.transformers.irToPy

import generated.Python.*
import org.jetbrains.kotlin.ir.backend.py.CompilerResult
import org.jetbrains.kotlin.ir.backend.py.PyCode
import org.jetbrains.kotlin.ir.backend.py.PyIrBackendContext
import org.jetbrains.kotlin.ir.backend.py.lower.StaticMembersLowering
import org.jetbrains.kotlin.ir.backend.py.utils.*
import org.jetbrains.kotlin.ir.declarations.IrModuleFragment
import org.jetbrains.kotlin.ir.declarations.IrSimpleFunction
import topython.toPython

// TODO
class IrModuleToPyTransformer(
    private val backendContext: PyIrBackendContext,
    private val mainArguments: List<String>?,
    var namer: NameTables = NameTables(emptyList()),
) {
    fun generateModule(modules: Iterable<IrModuleFragment>): CompilerResult {
        val additionalPackages = with(backendContext) {
            externalPackageFragment.values + listOf(
                bodilessBuiltInsPackageFragment,
            ) + packageLevelJsModules
        }

        modules.forEach { module ->
            module.files.forEach { StaticMembersLowering(backendContext).lower(it) }
        }

        modules.forEach { module ->
            namer.merge(module.files, additionalPackages)
        }

        return CompilerResult(generateWrappedModuleBody(modules, namer))
    }

    private fun generateWrappedModuleBody(modules: Iterable<IrModuleFragment>, namer: NameTables): PyCode {
        return PyCode(
            generateWrappedModuleBody2(
                modules,
                namer,
                EmptyCrossModuleReferenceInfo
            )
        )
    }

    private fun generateWrappedModuleBody2(
        modules: Iterable<IrModuleFragment>,
        namer: NameTables,
        refInfo: CrossModuleReferenceInfo
    ): String {

        val nameGenerator = refInfo.withReferenceTracking(
            IrNamerImpl(newNameTables = namer, backendContext),
            modules
        )
        val staticContext = PyStaticContext(
            backendContext = backendContext,
            irNamer = nameGenerator,
        )
        val rootContext = PyGenerationContext(
            currentFunction = null,
            staticContext = staticContext,
            localNames = LocalNameGenerator(NameScope.EmptyScope)
        )

        val callToMain = generateCallToMain(modules)
        val imports = generateImports()

        val moduleBody = generateModuleBody(modules, rootContext)
        val program = Module(
            body = moduleBody,
            type_ignores = emptyList(),
        ).let {
            it.copy(body = imports + it.body + callToMain)
        }

        return program.toPython()
    }

    private fun generateImports() =
        listOf(
            // Needed to support passing arguments for 'main' function.
            Import(names = listOf(aliasImpl(name = identifier("sys"), asname = null))),
        )

    private fun generateModuleBody(modules: Iterable<IrModuleFragment>, context: PyGenerationContext): List<stmt> {
        // todo: supporting inserting splitting comments as in JS would be handy

        val statements = mutableListOf<stmt>()

        modules.forEach { module: IrModuleFragment ->
            module.files.forEach {
                statements += it.accept(IrFileToPyTransformer(), context)
            }
        }

        statements += context.staticContext.initializerBlock

        return statements
    }

    private fun generateMainArguments(mainFunction: IrSimpleFunction): List<expr> {
        val retrieveArgumentsFromSystem = if (mainFunction.valueParameters.isNotEmpty()) {
            Subscript(
                value = Attribute(
                    value = Name(identifier("sys"), ctx = Load),
                    attr = identifier("argv"),
                    ctx = Load,
                ),
                slice = Slice(
                    lower = Constant(value = constant("1"), kind = null),
                    upper = null,
                    step = null,
                ),
                ctx = Load,
            )
        } else null
        return listOfNotNull(retrieveArgumentsFromSystem)
    }

    private fun generateCallToMain(modules: Iterable<IrModuleFragment>): List<stmt> {
        if (mainArguments == null) return emptyList() // in case `NO_MAIN` and `main(..)` exists
        val mainFunction = JsMainFunctionDetector.getMainFunctionOrNull(modules.last())
        return mainFunction?.let {
            // TODO handle arguments
            listOf(
                If(
                    test = Compare(
                        left = Name(id = identifier("__name__"), ctx = Load),
                        ops = listOf(Eq),
                        comparators = listOf(Constant(value = constant("\"__main__\""), kind = null)),
                    ),
                    body = listOf(
                        Call(
                            func = Name(id = identifier("main"), ctx = Load),
                            args = generateMainArguments(it),
                            keywords = emptyList(),
                        ).makeStmt(),
                    ),
                    orelse = emptyList(),
                ),
            )
        } ?: emptyList()
    }
}
