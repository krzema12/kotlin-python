/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.cli.py

import com.intellij.openapi.Disposable
import com.intellij.openapi.util.io.FileUtil
import org.jetbrains.kotlin.backend.common.serialization.metadata.KlibMetadataVersion
import org.jetbrains.kotlin.cli.common.*
import org.jetbrains.kotlin.cli.common.ExitCode.COMPILATION_ERROR
import org.jetbrains.kotlin.cli.common.ExitCode.OK
import org.jetbrains.kotlin.cli.common.arguments.K2JsArgumentConstants
import org.jetbrains.kotlin.cli.common.arguments.K2PyCompilerArguments
import org.jetbrains.kotlin.cli.common.config.addKotlinSourceRoot
import org.jetbrains.kotlin.cli.common.messages.AnalyzerWithCompilerReport
import org.jetbrains.kotlin.cli.common.messages.CompilerMessageSeverity.ERROR
import org.jetbrains.kotlin.cli.common.messages.CompilerMessageSeverity.LOGGING
import org.jetbrains.kotlin.cli.common.messages.MessageCollector
import org.jetbrains.kotlin.cli.common.messages.MessageUtil
import org.jetbrains.kotlin.cli.jvm.compiler.EnvironmentConfigFiles
import org.jetbrains.kotlin.cli.jvm.compiler.KotlinCoreEnvironment
import org.jetbrains.kotlin.config.CommonConfigurationKeys
import org.jetbrains.kotlin.config.CompilerConfiguration
import org.jetbrains.kotlin.config.IncrementalCompilation
import org.jetbrains.kotlin.config.Services
import org.jetbrains.kotlin.incremental.components.ExpectActualTracker
import org.jetbrains.kotlin.incremental.components.LookupTracker
import org.jetbrains.kotlin.incremental.js.IncrementalDataProvider
import org.jetbrains.kotlin.incremental.js.IncrementalNextRoundChecker
import org.jetbrains.kotlin.incremental.js.IncrementalResultsConsumer
import org.jetbrains.kotlin.ir.backend.js.MainModule
import org.jetbrains.kotlin.ir.backend.js.ModulesStructure
import org.jetbrains.kotlin.ir.backend.js.generateKLib
import org.jetbrains.kotlin.ir.backend.js.ic.checkCaches
import org.jetbrains.kotlin.ir.backend.js.prepareAnalyzedSourceModule
import org.jetbrains.kotlin.ir.backend.py.compile
import org.jetbrains.kotlin.ir.backend.py.pyPhases
import org.jetbrains.kotlin.ir.declarations.impl.IrFactoryImpl
import org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrFactory
import org.jetbrains.kotlin.js.analyzer.JsAnalysisResult
import org.jetbrains.kotlin.js.config.ErrorTolerancePolicy
import org.jetbrains.kotlin.js.config.JSConfigurationKeys
import org.jetbrains.kotlin.js.config.JsConfig
import org.jetbrains.kotlin.library.KLIB_FILE_EXTENSION
import org.jetbrains.kotlin.metadata.deserialization.BinaryVersion
import org.jetbrains.kotlin.psi.KtFile
import org.jetbrains.kotlin.resolve.CompilerEnvironment
import org.jetbrains.kotlin.utils.KotlinPaths
import org.jetbrains.kotlin.utils.join
import java.io.File
import java.io.IOException

class K2PyCompiler : CLICompiler<K2PyCompilerArguments>() {

    override val defaultPerformanceManager: CommonCompilerPerformanceManager =
        object : CommonCompilerPerformanceManager("Kotlin to Python (IR) Compiler") {}

    override fun createArguments(): K2PyCompilerArguments {
        return K2PyCompilerArguments()
    }

    override fun doExecute(
        arguments: K2PyCompilerArguments,
        configuration: CompilerConfiguration,
        rootDisposable: Disposable,
        paths: KotlinPaths?
    ): ExitCode {
        val messageCollector = configuration.getNotNull(CLIConfigurationKeys.MESSAGE_COLLECTOR_KEY)

        val pluginLoadResult = loadPlugins(paths, arguments, configuration)
        if (pluginLoadResult != OK) return pluginLoadResult

        if (arguments.freeArgs.isEmpty() && !IncrementalCompilation.isEnabledForJs()) {
            if (arguments.version) {
                return OK
            }
            if (arguments.includes.isNullOrEmpty()) {
                messageCollector.report(ERROR, "Specify at least one source file or directory", null)
                return COMPILATION_ERROR
            }
        }

        val libraries: List<String> = configureLibraries(arguments.libraries) + listOfNotNull(arguments.includes)
        val friendLibraries: List<String> = configureLibraries(arguments.friendModules)
        val repositories: List<String> = configureLibraries(arguments.repositries)

        configuration.put(JSConfigurationKeys.LIBRARIES, libraries)
        configuration.put(JSConfigurationKeys.TRANSITIVE_LIBRARIES, libraries)
        configuration.put(JSConfigurationKeys.REPOSITORIES, repositories)

        val commonSourcesArray = arguments.commonSources
        val commonSources = commonSourcesArray?.toSet() ?: emptySet()
        for (arg in arguments.freeArgs) {
            configuration.addKotlinSourceRoot(arg, commonSources.contains(arg))
        }

        val environmentForJS =
            KotlinCoreEnvironment.createForProduction(rootDisposable, configuration, EnvironmentConfigFiles.JS_CONFIG_FILES)
        val projectJs = environmentForJS.project
        val configurationJs = environmentForJS.configuration
        val sourcesFiles = environmentForJS.getSourceFiles()

        configurationJs.put(CLIConfigurationKeys.ALLOW_KOTLIN_PACKAGE, arguments.allowKotlinPackage)

        if (!checkKotlinPackageUsage(environmentForJS.configuration, sourcesFiles)) return COMPILATION_ERROR

        val outputFilePath = arguments.outputFile
        if (outputFilePath == null) {
            messageCollector.report(ERROR, "IR: Specify output file via -output", null)
            return COMPILATION_ERROR
        }

        if (messageCollector.hasErrors()) {
            return COMPILATION_ERROR
        }

        if (sourcesFiles.isEmpty() && !IncrementalCompilation.isEnabledForJs() && arguments.includes.isNullOrEmpty()) {
            messageCollector.report(ERROR, "No source files", null)
            return COMPILATION_ERROR
        }

        if (arguments.verbose) {
            reportCompiledSourcesList(messageCollector, sourcesFiles)
        }

        val outputFile = File(outputFilePath)

        configurationJs.put(CommonConfigurationKeys.MODULE_NAME, FileUtil.getNameWithoutExtension(outputFile))

        // TODO: in this method at least 3 different compiler configurations are used (original, env.configuration, jsConfig.configuration)
        // Such situation seems a bit buggy...
        val config = JsConfig(projectJs, configurationJs, CompilerEnvironment)
        val outputDir: File = outputFile.parentFile ?: outputFile.absoluteFile.parentFile!!
        try {
            config.configuration.put(JSConfigurationKeys.OUTPUT_DIR, outputDir.canonicalFile)
        } catch (e: IOException) {
            messageCollector.report(ERROR, "Could not resolve output directory", null)
            return COMPILATION_ERROR
        }

        val icCaches = configureLibraries(arguments.cacheDirectories)

        // Run analysis if main module is sources
        lateinit var sourceModule: ModulesStructure
        if (arguments.includes == null) {
            do {
                sourceModule = prepareAnalyzedSourceModule(
                    projectJs,
                    environmentForJS.getSourceFiles(),
                    configurationJs,
                    libraries,
                    friendLibraries,
                    AnalyzerWithCompilerReport(config.configuration),
                    icUseGlobalSignatures = icCaches.isNotEmpty(),
                    icUseStdlibCache = icCaches.isNotEmpty(),
                    icCache = if (icCaches.isNotEmpty()) checkCaches(libraries, icCaches, skipLib = arguments.includes).data else emptyMap()
                )
                val result = sourceModule.jsFrontEndResult.jsAnalysisResult
                if (result is JsAnalysisResult.RetryWithAdditionalRoots) {
                    environmentForJS.addKotlinSourceRoots(result.additionalKotlinRoots)
                }
            } while (result is JsAnalysisResult.RetryWithAdditionalRoots)
            if (!sourceModule.jsFrontEndResult.jsAnalysisResult.shouldGenerateCode)
                return OK
        }

        if (arguments.irProduceKlibDir || arguments.irProduceKlibFile) {
            if (arguments.irProduceKlibFile) {
                require(outputFile.extension == KLIB_FILE_EXTENSION) { "Please set up .klib file as output" }
            }

            generateKLib(
                sourceModule,
                irFactory = PersistentIrFactory(), // TODO IrFactoryImpl?
                outputKlibPath = outputFile.path,
                nopack = arguments.irProduceKlibDir,
                jsOutputName = null,
            )
        }

        if (arguments.irProducePy) {
            val phaseConfig = createPhaseConfig(pyPhases, arguments, messageCollector)

            val includes = arguments.includes

            val module = if (includes != null) {
                if (sourcesFiles.isNotEmpty()) {
                    messageCollector.report(ERROR, "Source files are not supported when -Xinclude is present")
                }
                val includesPath = File(includes).canonicalPath
                val mainLibPath = libraries.find { File(it).canonicalPath == includesPath }
                    ?: error("No library with name $includes ($includesPath) found")
                val kLib = MainModule.Klib(mainLibPath)
                ModulesStructure(
                    projectJs,
                    kLib,
                    configurationJs,
                    libraries,
                    friendLibraries,
                    icUseGlobalSignatures = icCaches.isNotEmpty(),
                    icUseStdlibCache = icCaches.isNotEmpty(),
                    icCache = if (icCaches.isNotEmpty()) checkCaches(libraries, icCaches, skipLib = includes).data else emptyMap()
                )
            } else {
                sourceModule
            }

            val mainCallArguments = if (K2JsArgumentConstants.NO_CALL == arguments.main) null else emptyList<String>()

            val compiledModule = compile(
                module,
                phaseConfig,
                IrFactoryImpl,
                mainCallArguments,
            )

            outputFile.writeText(compiledModule.pyCode!!.mainModule)
        }

        return OK
    }

    override fun setupPlatformSpecificArgumentsAndServices(
        configuration: CompilerConfiguration,
        arguments: K2PyCompilerArguments,
        services: Services
    ) {
        configuration.put(JSConfigurationKeys.FRIEND_PATHS_DISABLED, arguments.friendModulesDisabled)

        val friendModules = arguments.friendModules
        if (!arguments.friendModulesDisabled && friendModules != null) {
            val friendPaths = friendModules
                .split(File.pathSeparator.toRegex())
                .dropLastWhile { it.isEmpty() }
                .filterNot { it.isEmpty() }

            configuration.put(JSConfigurationKeys.FRIEND_PATHS, friendPaths)
        }

        configuration.putIfNotNull(JSConfigurationKeys.INCREMENTAL_DATA_PROVIDER, services[IncrementalDataProvider::class.java])
        configuration.putIfNotNull(JSConfigurationKeys.INCREMENTAL_RESULTS_CONSUMER, services[IncrementalResultsConsumer::class.java])
        configuration.putIfNotNull(JSConfigurationKeys.INCREMENTAL_NEXT_ROUND_CHECKER, services[IncrementalNextRoundChecker::class.java])
        configuration.putIfNotNull(CommonConfigurationKeys.LOOKUP_TRACKER, services[LookupTracker::class.java])
        configuration.putIfNotNull(CommonConfigurationKeys.EXPECT_ACTUAL_TRACKER, services[ExpectActualTracker::class.java])

        val errorTolerancePolicy = arguments.errorTolerancePolicy?.let { ErrorTolerancePolicy.resolvePolicy(it) }
        configuration.putIfNotNull(JSConfigurationKeys.ERROR_TOLERANCE_POLICY, errorTolerancePolicy)

        if (errorTolerancePolicy?.allowErrors == true) {
            configuration.put(JSConfigurationKeys.DEVELOPER_MODE, true)
        }

        configuration.put(JSConfigurationKeys.FAKE_OVERRIDE_VALIDATOR, arguments.fakeOverrideValidator)
    }

    override fun executableScriptFileName(): String {
        TODO("Provide a proper way to run the compiler with IR BE")
    }

    override fun createMetadataVersion(versionArray: IntArray): BinaryVersion {
        return KlibMetadataVersion(*versionArray)
    }

    override fun MutableList<String>.addPlatformOptions(arguments: K2PyCompilerArguments) {}

    companion object {
        @JvmStatic
        fun main(args: Array<String>) {
            doMain(K2PyCompiler(), args)
        }

        private fun reportCompiledSourcesList(messageCollector: MessageCollector, sourceFiles: List<KtFile>) {
            val fileNames = sourceFiles.map { file ->
                val virtualFile = file.virtualFile
                if (virtualFile != null) {
                    MessageUtil.virtualFileToPath(virtualFile)
                } else {
                    file.name + " (no virtual file)"
                }
            }
            messageCollector.report(LOGGING, "Compiling source files: " + join(fileNames, ", "), null)
        }

        private fun configureLibraries(libraryString: String?): List<String> =
            libraryString?.splitByPathSeparator() ?: emptyList()

        private fun String.splitByPathSeparator(): List<String> {
            return this.split(File.pathSeparator.toRegex())
                .dropLastWhile { it.isEmpty() }
                .toTypedArray()
                .filterNot { it.isEmpty() }
        }
    }
}
