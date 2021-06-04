/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.ir.backend.py.transformers.irToPy

import generated.Python.*
import org.jetbrains.kotlin.ir.backend.py.CompilerResult
import org.jetbrains.kotlin.ir.backend.py.JsCode
import org.jetbrains.kotlin.ir.backend.py.JsIrBackendContext
import org.jetbrains.kotlin.ir.backend.py.eliminateDeadDeclarations
import org.jetbrains.kotlin.ir.backend.py.export.ExportModelGenerator
import org.jetbrains.kotlin.ir.backend.py.export.ExportedModule
import org.jetbrains.kotlin.ir.backend.py.export.toTypeScript
import org.jetbrains.kotlin.ir.backend.py.lower.StaticMembersLowering
import org.jetbrains.kotlin.ir.backend.py.utils.*
import org.jetbrains.kotlin.ir.declarations.*
import topython.toPython

// TODO
class IrModuleToPyTransformer(
    private val backendContext: JsIrBackendContext,
    private val mainArguments: List<String>?,
    private val generateScriptModule: Boolean = false,
    var namer: NameTables = NameTables(emptyList()),
    private val fullJs: Boolean = true,
    private val dceJs: Boolean = false,
    private val multiModule: Boolean = false,
    private val relativeRequirePath: Boolean = false
) {
    fun generateModule(modules: Iterable<IrModuleFragment>): CompilerResult {
        val additionalPackages = with(backendContext) {
            externalPackageFragment.values + listOf(
                bodilessBuiltInsPackageFragment,
                intrinsics.externalPackageFragment
            ) + packageLevelJsModules
        }

        val exportedModule = ExportModelGenerator(backendContext).generateExport(modules)
        val dts = exportedModule.toTypeScript()

        modules.forEach { module ->
            module.files.forEach { StaticMembersLowering(backendContext).lower(it) }
        }

        if (multiModule) {
            breakCrossModuleFieldAccess(backendContext, modules)
        }

        modules.forEach { module ->
            namer.merge(module.files, additionalPackages)
        }

        val jsCode = if (fullJs) generateWrappedModuleBody(modules, exportedModule, namer) else null

        val dceJsCode = if (dceJs) {
            eliminateDeadDeclarations(modules, backendContext)
            // Use a fresh namer for DCE so that we could compare the result with DCE-driven
            // TODO: is this mode relevant for scripting? If yes, refactor so that the external name tables are used here when needed.
            val namer = NameTables(emptyList())
            namer.merge(modules.flatMap { it.files }, additionalPackages)
            generateWrappedModuleBody(modules, exportedModule, namer)
        } else null

        return CompilerResult(jsCode, dceJsCode, dts)
    }

    private fun generateWrappedModuleBody(modules: Iterable<IrModuleFragment>, exportedModule: ExportedModule, namer: NameTables): JsCode {
        if (multiModule) {

            val refInfo = buildCrossModuleReferenceInfo(modules)

            val rM = modules.reversed()

            val main = rM.first()
            val others = rM.drop(1)

            val mainModule = generateWrappedModuleBody2(
                listOf(main),
                others,
                exportedModule,
                namer,
                refInfo
            )

            val dependencies = others.mapIndexed { index, module ->
                val moduleName = sanitizeName(module.safeName)

                val exportedDeclarations = ExportModelGenerator(backendContext).let { module.files.flatMap { file -> it.generateExport(file) } }

                moduleName to generateWrappedModuleBody2(
                    listOf(module),
                    others.drop(index + 1),
                    ExportedModule(moduleName, exportedModule.moduleKind, exportedDeclarations),
                    namer,
                    refInfo
                )
            }.reversed()

            return JsCode(mainModule, dependencies)
        } else {
            return JsCode(
                generateWrappedModuleBody2(
                    modules,
                    emptyList(),
                    exportedModule,
                    namer,
                    EmptyCrossModuleReferenceInfo
                )
            )
        }
    }

    private fun generateWrappedModuleBody2(
        modules: Iterable<IrModuleFragment>,
        dependencies: Iterable<IrModuleFragment>,
        exportedModule: ExportedModule,
        namer: NameTables,
        refInfo: CrossModuleReferenceInfo
    ): String {

        val nameGenerator = refInfo.withReferenceTracking(
            IrNamerImpl(newNameTables = namer),
            modules
        )
        val rootContext = JsGenerationContext(
            currentFunction = null,
            irNamer = nameGenerator,
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
