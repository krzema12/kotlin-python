/*
 * Copyright 2010-2018 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.python.test

import com.intellij.openapi.util.io.FileUtil
import com.intellij.openapi.vfs.StandardFileSystems
import com.intellij.openapi.vfs.VirtualFileManager
import com.intellij.psi.PsiManager
import org.jetbrains.kotlin.backend.common.phaser.PhaseConfig
import org.jetbrains.kotlin.checkers.CompilerTestLanguageVersionSettings
import org.jetbrains.kotlin.checkers.parseLanguageVersionSettings
import org.jetbrains.kotlin.cli.common.messages.AnalyzerWithCompilerReport
import org.jetbrains.kotlin.cli.jvm.compiler.EnvironmentConfigFiles
import org.jetbrains.kotlin.cli.jvm.compiler.KotlinCoreEnvironment
import org.jetbrains.kotlin.config.*
import org.jetbrains.kotlin.idea.KotlinFileType
import org.jetbrains.kotlin.ir.backend.js.prepareAnalyzedSourceModule
import org.jetbrains.kotlin.ir.backend.py.PyCode
import org.jetbrains.kotlin.ir.backend.py.compile
import org.jetbrains.kotlin.ir.backend.py.pyPhases
import org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrFactory
import org.jetbrains.kotlin.js.config.JSConfigurationKeys
import org.jetbrains.kotlin.js.config.JsConfig
import org.jetbrains.kotlin.name.FqName
import org.jetbrains.kotlin.psi.KtFile
import org.jetbrains.kotlin.psi.KtNamedFunction
import org.jetbrains.kotlin.psi.KtPsiFactory
import org.jetbrains.kotlin.py.facade.TranslationUnit
import org.jetbrains.kotlin.python.test.utils.PyTestUtils
import org.jetbrains.kotlin.resolve.CompilerEnvironment
import org.jetbrains.kotlin.serialization.js.JsModuleDescriptor
import org.jetbrains.kotlin.serialization.js.KotlinJavascriptSerializationUtil
import org.jetbrains.kotlin.test.*
import org.jetbrains.kotlin.test.util.KtTestUtil
import org.jetbrains.kotlin.utils.DFS
import org.jetbrains.kotlin.utils.KotlinJavascriptMetadataUtils
import org.jetbrains.kotlin.utils.addToStdlib.measureTimeMillisWithResult
import java.io.Closeable
import java.io.File
import java.util.regex.Pattern

private val fullRuntimeKlib: String = System.getProperty("kotlin.js.full.stdlib.path")
private val defaultRuntimeKlib = System.getProperty("kotlin.js.reduced.stdlib.path")
private val kotlinTestKLib = System.getProperty("kotlin.js.kotlin.test.path")

class KotlinCompilationException(override val message: String, override val cause: Throwable) : RuntimeException(message, cause)

abstract class BasicIrBoxTest(
    private val pathToTestDir: String,
    testGroupOutputDirPrefix: String,
) : KotlinTestWithEnvironment() {
    private val testGroupOutputDirForCompilation = File(TEST_DATA_DIR_PATH + "out/" + testGroupOutputDirPrefix)

    protected fun doTest(filePath: String) {
        val file = File(filePath)
        val outputDir = getOutputDir(file)
        val fileContent = KtTestUtil.doLoadFile(file)

        val needsFullIrRuntime = KJS_WITH_FULL_RUNTIME.matcher(fileContent).find()

        TestFileFactoryImpl().use { testFactory ->
            val inputFiles = TestFiles.createTestFiles(
                file.name,
                fileContent,
                testFactory,
                true
            )
            val modules = inputFiles.map { it.module }.distinct().associateBy { it.name }

            fun TestModule.allTransitiveDependencies(): Set<String> {
                return dependenciesSymbols.toSet() + dependenciesSymbols.flatMap { modules[it]!!.allTransitiveDependencies() }
            }

            val orderedModules = DFS.topologicalOrder(modules.values) { module -> module.dependenciesSymbols.mapNotNull { modules[it] } }

            val testPackage = testFactory.testPackage
            val mainModuleName = DEFAULT_MODULE

            val generatedPyFiles = orderedModules.asReversed().mapNotNull { module ->
                val dependencies = module.dependenciesSymbols.map { outputFileName(outputDir) + ".meta.py" }
                val allDependencies = module.allTransitiveDependencies().map { outputFileName(outputDir) + ".meta.py" }
                val friends = module.friendsSymbols.map { outputFileName(outputDir) + ".meta.py" }

                val outputFileName = outputFileName(outputDir) + ".py"
                val isMainModule = mainModuleName == module.name
                generateJavaScriptFile(
                    testFactory.tmpDir,
                    file.parent,
                    module,
                    outputFileName,
                    dependencies,
                    allDependencies,
                    friends,
                    modules.size > 1,
                    testPackage,
                    needsFullIrRuntime,
                    isMainModule,
                )

                when {
                    // PY_IR generates single js file for all modules (apart from runtime)
                    !isMainModule -> null
                    else -> outputFileName
                }
            }

            val generatedPyFilePath = checkNotNull(generatedPyFiles.singleOrNull()) {
                "More than one generated python file is unsupported yet"
            }

            runGeneratedCode(generatedPyFilePath)
        }
    }

    private fun getOutputDir(file: File): File {
        val stopFile = File(pathToTestDir)
        return generateSequence(file.parentFile) { it.parentFile }
            .takeWhile { it != stopFile }
            .map { it.name }
            .toList().asReversed()
            .fold(testGroupOutputDirForCompilation, ::File)
    }

    private fun outputFileSimpleName(): String {
        return getTestName(true)
    }

    private fun outputFileName(directory: File) = directory.absolutePath + "/" + outputFileSimpleName()

    private fun generateJavaScriptFile(
        tmpDir: File,
        directory: String,
        module: TestModule,
        outputFileName: String,
        dependencies: List<String>,
        allDependencies: List<String>,
        friends: List<String>,
        multiModule: Boolean,
        testPackage: String?,
        needsFullIrRuntime: Boolean,
        isMainModule: Boolean,
    ) {
        val kotlinFiles = module.files.filter { it.fileName.endsWith(".kt") }
        val testFiles = kotlinFiles.map { it.fileName }
        val globalCommonFiles = PyTestUtils.getFilesInDirectoryByExtension(COMMON_FILES_DIR_PATH, KotlinFileType.EXTENSION)
        val localCommonFile = "$directory/$COMMON_FILES_NAME.${KotlinFileType.EXTENSION}"
        val localCommonFiles = if (File(localCommonFile).exists()) listOf(localCommonFile) else emptyList()
        val additionalFiles = globalCommonFiles + localCommonFiles
        val allSourceFiles = (testFiles + additionalFiles).map(::File)
        val psiFiles = createPsiFiles(allSourceFiles.sortedBy { it.canonicalPath }.map { it.canonicalPath })

        val config = createConfig(
            module,
            dependencies,
            allDependencies,
            friends,
            multiModule,
            tmpDir,
        )
        val outputFile = File(outputFileName)

        translateFiles(
            psiFiles.map(TranslationUnit::SourceFile), outputFile, config,
            testPackage, needsFullIrRuntime, isMainModule,
        )
    }

    private fun createPsiFile(fileName: String): KtFile {
        val psiManager = PsiManager.getInstance(project)
        val fileSystem = VirtualFileManager.getInstance().getFileSystem(StandardFileSystems.FILE_PROTOCOL)

        val file = fileSystem.findFileByPath(fileName) ?: error("File not found: $fileName")

        return psiManager.findFile(file) as KtFile
    }

    private fun createPsiFiles(fileNames: List<String>): List<KtFile> = fileNames.map(this::createPsiFile)

    private fun createConfig(
        module: TestModule, dependencies: List<String>, allDependencies: List<String>, friends: List<String>, multiModule: Boolean,
        tmpDir: File,
    ): JsConfig {
        val configuration = environment.configuration.copy()

        configuration.put(CommonConfigurationKeys.DISABLE_INLINE, module.inliningDisabled)
        module.languageVersionSettings?.let { languageVersionSettings ->
            configuration.languageVersionSettings = languageVersionSettings
        }

        val libraries = JsConfig.JS_STDLIB + JsConfig.JS_KOTLIN_TEST + dependencies

        configuration.put(JSConfigurationKeys.LIBRARIES, libraries)
        configuration.put(JSConfigurationKeys.TRANSITIVE_LIBRARIES, allDependencies)
        configuration.put(JSConfigurationKeys.FRIEND_PATHS, friends)

        configuration.put(CommonConfigurationKeys.MODULE_NAME, module.name)

        configuration.put(JSConfigurationKeys.META_INFO, multiModule)

        configuration.put(JSConfigurationKeys.GENERATE_REGION_COMMENTS, true)

        configuration.put(
            JSConfigurationKeys.FILE_PATHS_PREFIX_MAP,
            mapOf(
                tmpDir.absolutePath to "<TMP>",
                File(".").absolutePath.removeSuffix(".") to ""
            )
        )

        return JsConfig(project, configuration, CompilerEnvironment, METADATA_CACHE, (JsConfig.JS_STDLIB + JsConfig.JS_KOTLIN_TEST).toSet())
    }

    private inner class TestFileFactoryImpl : TestFiles.TestFileFactory<TestModule, TestFile>, Closeable {
        var testPackage: String? = null
        val tmpDir = KtTestUtil.tmpDir("js-tests")
        val defaultModule = TestModule(DEFAULT_MODULE, emptyList(), emptyList())
        var languageVersionSettings: LanguageVersionSettings? = null

        override fun createFile(module: TestModule?, fileName: String, text: String, directives: Directives): TestFile {
            val currentModule = module ?: defaultModule

            val ktFile = KtPsiFactory(project).createFile(text)
            val boxFunction = ktFile.declarations.find { it is KtNamedFunction && it.name == TEST_FUNCTION }
            if (boxFunction != null) {
                testPackage = ktFile.packageFqName.asString()
                if (testPackage?.isEmpty() == true) {
                    testPackage = null
                }
            }

            val temporaryFile = File(tmpDir, "${currentModule.name}/$fileName")
            KtTestUtil.mkdirs(temporaryFile.parentFile)
            temporaryFile.writeText(text, Charsets.UTF_8)

            // TODO Deduplicate logic copied from CodegenTestCase.updateConfigurationByDirectivesInTestFiles
            fun LanguageVersion.toSettings() = CompilerTestLanguageVersionSettings(
                emptyMap(),
                ApiVersion.createByLanguageVersion(this),
                this,
                emptyMap()
            )

            fun LanguageVersionSettings.trySet() {
                val old = languageVersionSettings
                assert(old == null || old == this) { "Should not specify language version settings twice:\n$old\n$this" }
                languageVersionSettings = this
            }
            InTextDirectivesUtils.findStringWithPrefixes(text, "// LANGUAGE_VERSION:")?.let {
                LanguageVersion.fromVersionString(it)?.toSettings()?.trySet()
            }

            parseLanguageVersionSettings(directives)?.trySet()

            // Relies on the order of module creation
            // TODO is that ok?
            currentModule.languageVersionSettings = languageVersionSettings

            return TestFile(
                temporaryFile.absolutePath,
                currentModule,
            )
        }

        override fun createModule(name: String, dependencies: List<String>, friends: List<String>, abiVersions: List<Int>): TestModule {
            return TestModule(name, dependencies, friends)
        }

        override fun close() {
            FileUtil.delete(tmpDir)
        }
    }

    private class TestFile(val fileName: String, val module: TestModule) {
        init {
            module.files += this
        }
    }

    private class TestModule(
        name: String,
        dependencies: List<String>,
        friends: List<String>,
    ) : KotlinBaseTest.TestModule(name, dependencies, friends) {
        var inliningDisabled = false
        val files = mutableListOf<TestFile>()
        var languageVersionSettings: LanguageVersionSettings? = null
    }

    override fun createEnvironment() =
        KotlinCoreEnvironment.createForTests(testRootDisposable, CompilerConfiguration(), EnvironmentConfigFiles.JS_CONFIG_FILES)

    private fun translateFiles(
        units: List<TranslationUnit>,
        outputFile: File,
        config: JsConfig,
        testPackage: String?,
        needsFullIrRuntime: Boolean,
        isMainModule: Boolean,
    ) {
        val filesToCompile = units.map { (it as TranslationUnit.SourceFile).file }
        val allKlibPaths = if (needsFullIrRuntime) listOf(fullRuntimeKlib, kotlinTestKLib) else listOf(defaultRuntimeKlib)

        if (isMainModule) {
            val phaseConfig = PhaseConfig(pyPhases)

            val module = prepareAnalyzedSourceModule(
                config.project,
                filesToCompile,
                config.configuration,
                allKlibPaths,
                emptyList(),
                AnalyzerWithCompilerReport(config.configuration),
            )

            var compilationException: Throwable? = null
            val (duration, compiledModule) = measureTimeMillisWithResult {
                try {
                    compile(
                        module,
                        phaseConfig = phaseConfig,
                        irFactory = PersistentIrFactory(),
                        exportedDeclarations = setOf(FqName.fromSegments(listOfNotNull(testPackage, TEST_FUNCTION))),
                        verifySignatures = true,
                    )
                } catch (e: Throwable) {
                    compilationException = e
                    null
                }
            }

            compilationException?.let {
                val compilationTimeMessage = "Kotlin compilation time: $duration ms"
                throw KotlinCompilationException(compilationTimeMessage, it)
            }

            compiledModule!!.pyCode!!.writeTo(outputFile)
        } else {
            TODO()
        }
    }

    private fun PyCode.writeTo(outputFile: File) {
        val wrappedCode = mainModule
        outputFile.write(wrappedCode)

        val dependencyPaths = mutableListOf<String>()

        dependencies.forEach { (moduleId, code) ->
            val dependencyPath = outputFile.absolutePath.replace(".py", "-${moduleId}.py")
            dependencyPaths += dependencyPath
            File(dependencyPath).write(code)
        }
    }

    private fun File.write(text: String) {
        parentFile.mkdirs()
        writeText(text)
    }

    private fun runGeneratedCode(generatedPyFilePath: String) {
        PythonTestChecker.check(generatedPyFilePath)
    }

    companion object {
        val METADATA_CACHE = (JsConfig.JS_STDLIB + JsConfig.JS_KOTLIN_TEST).flatMap { path ->
            KotlinJavascriptMetadataUtils.loadMetadata(path).map { metadata ->
                val parts = KotlinJavascriptSerializationUtil.readModuleAsProto(metadata.body, metadata.version)
                JsModuleDescriptor(metadata.moduleName, parts.kind, parts.importedModules, parts)
            }
        }

        const val TEST_DATA_DIR_PATH = "python/py.translator/testData/"

        private const val COMMON_FILES_NAME = "_common"
        private const val COMMON_FILES_DIR = "_commonFiles/"
        const val COMMON_FILES_DIR_PATH = TEST_DATA_DIR_PATH + COMMON_FILES_DIR

        private val KJS_WITH_FULL_RUNTIME = Pattern.compile("^// *KJS_WITH_FULL_RUNTIME *\$", Pattern.MULTILINE)

        private const val DEFAULT_MODULE = "main"
        private const val TEST_FUNCTION = "box"
    }
}
