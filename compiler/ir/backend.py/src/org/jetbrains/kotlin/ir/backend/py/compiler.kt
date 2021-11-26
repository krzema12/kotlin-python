/*
 * Copyright 2010-2018 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.ir.backend.py

import org.jetbrains.kotlin.backend.common.phaser.PhaseConfig
import org.jetbrains.kotlin.backend.common.phaser.invokeToplevel
import org.jetbrains.kotlin.ir.backend.js.MainModule
import org.jetbrains.kotlin.ir.backend.js.ModulesStructure
import org.jetbrains.kotlin.ir.backend.js.loadIr
import org.jetbrains.kotlin.ir.backend.py.lower.generateTests
import org.jetbrains.kotlin.ir.backend.py.lower.moveBodilessDeclarationsToSeparatePlace
import org.jetbrains.kotlin.ir.backend.py.transformers.irToPy.IrModuleToPyTransformer
import org.jetbrains.kotlin.ir.declarations.IrFactory
import org.jetbrains.kotlin.ir.declarations.IrModuleFragment
import org.jetbrains.kotlin.ir.declarations.StageController
import org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrFactory
import org.jetbrains.kotlin.ir.util.ExternalDependenciesGenerator
import org.jetbrains.kotlin.ir.util.noUnboundLeft
import org.jetbrains.kotlin.js.config.RuntimeDiagnostic
import org.jetbrains.kotlin.name.FqName

class CompilerResult(
    val pyCode: PyCode?,
    val dcePyCode: PyCode?,
)

class PyCode(val mainModule: String, val dependencies: Iterable<Pair<String, String>> = emptyList())

fun compile(
    depsDescriptors: ModulesStructure,
    phaseConfig: PhaseConfig,
    irFactory: IrFactory,
    exportedDeclarations: Set<FqName> = emptySet(),
    generateFullJs: Boolean = true,
    generateDceJs: Boolean = false,
    dceDriven: Boolean = false,
    dceRuntimeDiagnostic: RuntimeDiagnostic? = null,
    es6mode: Boolean = false,
    multiModule: Boolean = false,
    relativeRequirePath: Boolean = false,
    propertyLazyInitialization: Boolean,
    verifySignatures: Boolean = true,
): CompilerResult {
    val (moduleFragment: IrModuleFragment, dependencyModules, irBuiltIns, symbolTable, deserializer) =
        loadIr(depsDescriptors, irFactory, verifySignatures)
    val mainModule = depsDescriptors.mainModule
    val configuration = depsDescriptors.compilerConfiguration

    val moduleDescriptor = moduleFragment.descriptor

    val allModules = when (mainModule) {
        is MainModule.SourceFiles -> dependencyModules + listOf(moduleFragment)
        is MainModule.Klib -> dependencyModules
    }

    val context = JsIrBackendContext(
        moduleDescriptor,
        irBuiltIns,
        symbolTable,
        allModules.first(),
        exportedDeclarations,
        configuration,
        es6mode = es6mode,
        dceRuntimeDiagnostic = dceRuntimeDiagnostic,
        propertyLazyInitialization = propertyLazyInitialization,
    )

    // Load declarations referenced during `context` initialization
    val irProviders = listOf(deserializer)
    ExternalDependenciesGenerator(symbolTable, irProviders).generateUnboundSymbolsAsDependencies()

    deserializer.postProcess()
    symbolTable.noUnboundLeft("Unbound symbols at the end of linker")

    allModules.forEach { module ->
        moveBodilessDeclarationsToSeparatePlace(context, module)
    }

    // TODO should be done incrementally
    generateTests(context, allModules.last())

    if (dceDriven) {
        val controller = MutableController(context, pirLowerings)

        check(irFactory is PersistentIrFactory)
        irFactory.stageController = controller

        controller.currentStage = controller.lowerings.size + 1

        eliminateDeadDeclarations(allModules, context)

        irFactory.stageController = StageController(controller.currentStage)

        val transformer = IrModuleToPyTransformer(
            context,
            fullJs = true,
            dceJs = false,
            multiModule = multiModule,
            relativeRequirePath = relativeRequirePath
        )
        return transformer.generateModule(allModules)
    } else {
        jsPhases.invokeToplevel(phaseConfig, context, allModules)
        val transformer = IrModuleToPyTransformer(
            context,
            fullJs = generateFullJs,
            dceJs = generateDceJs,
            multiModule = multiModule,
            relativeRequirePath = relativeRequirePath
        )
        return transformer.generateModule(allModules)
    }
}
