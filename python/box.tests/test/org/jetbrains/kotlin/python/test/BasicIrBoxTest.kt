/*
 * Copyright 2010-2018 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.python.test

import org.jetbrains.kotlin.backend.common.phaser.PhaseConfig
import org.jetbrains.kotlin.backend.common.phaser.toPhaseMap
import org.jetbrains.kotlin.cli.common.messages.AnalyzerWithCompilerReport
import org.jetbrains.kotlin.cli.common.messages.MessageCollector
import org.jetbrains.kotlin.cli.js.messageCollectorLogger
import org.jetbrains.kotlin.ir.backend.js.MainModule
import org.jetbrains.kotlin.ir.backend.js.generateKLib
import org.jetbrains.kotlin.ir.backend.js.jsResolveLibraries
import org.jetbrains.kotlin.ir.backend.py.CompilerResult
import org.jetbrains.kotlin.ir.backend.py.JsCode
import org.jetbrains.kotlin.ir.backend.py.compile
import org.jetbrains.kotlin.ir.backend.py.jsPhases
import org.jetbrains.kotlin.ir.declarations.impl.IrFactoryImpl
import org.jetbrains.kotlin.js.config.JSConfigurationKeys
import org.jetbrains.kotlin.js.config.JsConfig
import org.jetbrains.kotlin.name.FqName
import org.jetbrains.kotlin.py.facade.MainCallParameters
import org.jetbrains.kotlin.py.facade.TranslationUnit
import org.jetbrains.kotlin.utils.addToStdlib.measureTimeMillisWithResult
import java.io.File
import java.lang.Boolean.getBoolean

private val fullRuntimeKlib: String = System.getProperty("kotlin.js.full.stdlib.path")
private val defaultRuntimeKlib = System.getProperty("kotlin.js.reduced.stdlib.path")
private val kotlinTestKLib = System.getProperty("kotlin.js.kotlin.test.path")

class KotlinCompilationException(override val message: String, override val cause: Throwable) : RuntimeException(message, cause)

abstract class BasicIrBoxTest(
    pathToTestDir: String,
    testGroupOutputDirPrefix: String,
    pathToRootOutputDir: String = TEST_DATA_DIR_PATH,
) : BasicBoxTest(
    pathToTestDir,
    testGroupOutputDirPrefix,
    pathToRootOutputDir = pathToRootOutputDir,
) {
    private val compilationCache = mutableMapOf<String, String>()

    private val cachedDependencies = mutableMapOf<String, Collection<String>>()

    override fun doTest(filePath: String, expectedResult: String, mainCallParameters: MainCallParameters) {
        compilationCache.clear()
        cachedDependencies.clear()
        super.doTest(filePath, expectedResult, mainCallParameters)
    }

    override fun translateFiles(
        units: List<TranslationUnit>,
        outputFile: File,
        config: JsConfig,
        mainCallParameters: MainCallParameters,
        remap: Boolean,
        testPackage: String?,
        testFunction: String,
        needsFullIrRuntime: Boolean,
        isMainModule: Boolean,
        splitPerModule: Boolean,
        propertyLazyInitialization: Boolean,
    ) {
        val filesToCompile = units.map { (it as TranslationUnit.SourceFile).file }

        val runtimeKlibs = if (needsFullIrRuntime) listOf(fullRuntimeKlib, kotlinTestKLib) else listOf(defaultRuntimeKlib)

        val transitiveLibraries = config.configuration[JSConfigurationKeys.TRANSITIVE_LIBRARIES]!!.map { File(it).name }

        val allKlibPaths = (runtimeKlibs + transitiveLibraries.map {
            compilationCache[it] ?: error("Can't find compiled module for dependency $it")
        }).map { File(it).absolutePath }

        val resolvedLibraries = jsResolveLibraries(allKlibPaths, emptyList(), messageCollectorLogger(MessageCollector.NONE))

        val actualOutputFile = outputFile.absolutePath.let {
            if (!isMainModule) it.replace("_v5.js", "/") else it
        }

        if (isMainModule) {
            val debugMode = getBoolean("kotlin.py.debugMode")

            val phaseConfig = if (debugMode) {
                val allPhasesSet = jsPhases.toPhaseMap().values.toSet()
                val dumpOutputDir = File(outputFile.parent, outputFile.nameWithoutExtension + "-irdump")
                println("\n ------ Dumping phases to file://$dumpOutputDir")
                PhaseConfig(
                    jsPhases,
                    dumpToDirectory = dumpOutputDir.path,
                    toDumpStateAfter = allPhasesSet,
                    toValidateStateAfter = allPhasesSet,
                    dumpOnlyFqName = null
                )
            } else {
                PhaseConfig(jsPhases)
            }

            var compilationException: Throwable? = null
            val compiledModuleWithDuration: Pair<Long, CompilerResult?> = measureTimeMillisWithResult {
                try {
                    compile(
                        project = config.project,
                        mainModule = MainModule.SourceFiles(filesToCompile),
                        analyzer = AnalyzerWithCompilerReport(config.configuration),
                        configuration = config.configuration,
                        phaseConfig = phaseConfig,
                        irFactory = IrFactoryImpl,
                        allDependencies = resolvedLibraries,
                        friendDependencies = emptyList(),
                        mainArguments = mainCallParameters.run { if (shouldBeGenerated()) arguments() else null },
                        exportedDeclarations = setOf(FqName.fromSegments(listOfNotNull(testPackage, testFunction))),
                        generateFullJs = true,
                        multiModule = splitPerModule,
                        propertyLazyInitialization = propertyLazyInitialization,
                    )
                } catch (e: Throwable) {
                    compilationException = e
                    null
                }
            }
            val compilationTimeMessage = "Kotlin compilation time: ${compiledModuleWithDuration.first} ms"

            compilationException?.let {
                throw KotlinCompilationException(compilationTimeMessage, it)
            }
            val compiledModule = compiledModuleWithDuration.second!!

            compiledModule.jsCode!!.writeTo(outputFile, config)
        } else {
            generateKLib(
                project = config.project,
                files = filesToCompile,
                analyzer = AnalyzerWithCompilerReport(config.configuration),
                configuration = config.configuration,
                allDependencies = resolvedLibraries,
                friendDependencies = emptyList(),
                irFactory = IrFactoryImpl,
                outputKlibPath = actualOutputFile,
                nopack = true
            )

            compilationCache[outputFile.name.replace(".js", ".meta.js")] = actualOutputFile
        }
    }

    private fun JsCode.writeTo(outputFile: File, config: JsConfig) {
        val wrappedCode = wrapWithModuleEmulationMarkers(mainModule, moduleId = config.moduleId, moduleKind = config.moduleKind)
        outputFile.write(wrappedCode)

        val dependencyPaths = mutableListOf<String>()

        dependencies.forEach { (moduleId, code) ->
            val wrappedCode2 = wrapWithModuleEmulationMarkers(code, config.moduleKind, moduleId)
            val dependencyPath = outputFile.absolutePath.replace("_v5.js", "-${moduleId}_v5.js")
            dependencyPaths += dependencyPath
            File(dependencyPath).write(wrappedCode2)
        }

        cachedDependencies[outputFile.absolutePath] = dependencyPaths
    }

    private fun File.write(text: String) {
        parentFile.mkdirs()
        writeText(text)
    }

    override fun runGeneratedCode(
        jsFiles: List<String>,
        testModuleName: String?,
        testPackage: String?,
        testFunction: String,
        expectedResult: String,
        withModuleSystem: Boolean
    ) {
        // TODO: should we do anything special for module systems?
        // TODO: return list of js from translateFiles and provide then to this function with other js files

        val allFiles = jsFiles.flatMap { file -> cachedDependencies[File(file).absolutePath]?.let { deps -> deps + file } ?: listOf(file) }
        testChecker.check(allFiles, expectedResult)
    }
}
