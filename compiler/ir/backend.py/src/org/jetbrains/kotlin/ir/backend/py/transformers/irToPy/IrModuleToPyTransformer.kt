/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.ir.backend.py.transformers.irToPy

import generated.Python.Module
import generated.Python.stmt
import org.jetbrains.kotlin.ir.backend.py.CompilerResult
import org.jetbrains.kotlin.ir.backend.py.JsIrBackendContext
import org.jetbrains.kotlin.ir.backend.py.PyCode
import org.jetbrains.kotlin.ir.backend.py.lower.StaticMembersLowering
import org.jetbrains.kotlin.ir.backend.py.utils.*
import org.jetbrains.kotlin.ir.declarations.IrModuleFragment
import topython.toPython

// TODO
class IrModuleToPyTransformer(
    private val backendContext: JsIrBackendContext,
    private val generateScriptModule: Boolean = false,
    var namer: NameTables = NameTables(emptyList()),
    private val fullJs: Boolean = true,
    private val dceJs: Boolean = false,
    private val relativeRequirePath: Boolean = false
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

        val jsCode = if (fullJs) generateWrappedModuleBody(modules, namer) else null

        val dceJsCode = null
        return CompilerResult(jsCode, dceJsCode)
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
        val staticContext = JsStaticContext(
            backendContext = backendContext,
            irNamer = nameGenerator,
            globalNameScope = namer.globalNames
        )
        val rootContext = JsGenerationContext(
            currentFunction = null,
            staticContext = staticContext,
            localNames = LocalNameGenerator(NameScope.EmptyScope)
        )

        val moduleBody = generateModuleBody(modules, rootContext)
        val program = Module(
            body = moduleBody,
            type_ignores = emptyList(),
        )

        return program.toPython()
    }

    private fun generateModuleBody(modules: Iterable<IrModuleFragment>, context: JsGenerationContext): List<stmt> {
        return modules.flatMap { module: IrModuleFragment ->
            module.files.flatMap {
                it.accept(IrFileToPyTransformer(), context)
            }
        }
    }
}
