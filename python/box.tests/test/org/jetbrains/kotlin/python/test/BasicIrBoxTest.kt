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
import org.jetbrains.kotlin.js.facade.MainCallParameters
import org.jetbrains.kotlin.name.FqName
import org.jetbrains.kotlin.psi.KtFile
import org.jetbrains.kotlin.psi.KtNamedFunction
import org.jetbrains.kotlin.psi.KtPsiFactory
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

private val fullRuntimeKlib: String get() = System.getProperty("kotlin.js.full.stdlib.path")
private val defaultRuntimeKlib: String get() = System.getProperty("kotlin.js.reduced.stdlib.path")
private val kotlinTestKLib: String get() = System.getProperty("kotlin.js.kotlin.test.path")

class KotlinCompilationException(override val message: String, override val cause: Throwable) : RuntimeException(message, cause)

abstract class BasicIrBoxTest(
    pathToTestDir: String,
    testGroupOutputDirPrefix: String,
) : KotlinTestWithEnvironment() {

    private val testDir = File(pathToTestDir)
    private val compilationGroupDir = File("python/py.translator/testData/out/$testGroupOutputDirPrefix")

    protected fun doTest(testFilePath: String) {
        val testFile = File(testFilePath)
        val fileContent = KtTestUtil.doLoadFile(testFile)

        val generatedPyFiles = TestFileFactoryImpl().use { testFactory ->
            val splitTestFiles = TestFiles.createTestFiles(
                testFile.name,
                fileContent,
                testFactory,
                true,
            )
            val modules = splitTestFiles.map { it.module }.distinct().associateBy { it.name }
            val orderedModules = DFS.topologicalOrder(modules.values) { module -> module.dependenciesSymbols.mapNotNull { modules[it] } }

            val outputDir = getOutputDir(testFile = testFile, stopDir = testDir, compilationGroupDir = compilationGroupDir)
            val needsFullIrRuntime = KJS_WITH_FULL_RUNTIME.matcher(fileContent).find()

            orderedModules.asReversed().mapNotNull { module ->
                val outputFilePath = "${outputDir.absolutePath}/${getTestName(true)}.py"
                val isMainModule = DEFAULT_MODULE == module.name

                generatePythonFile(
                    tmpDir = testFactory.tmpDir,
                    testDir = testFile.parent,
                    module = module,
                    outputFilePath = outputFilePath,
                    multiModule = modules.size > 1,
                    testPackage = testFactory.testPackage,
                    needsFullIrRuntime = needsFullIrRuntime,
                    isMainModule = isMainModule,
                )

                when {
                    // PY_IR generates single js file for all modules (apart from runtime)
                    !isMainModule -> null
                    else -> outputFilePath
                }
            }
        }

        val generatedPyFilePath = checkNotNull(generatedPyFiles.singleOrNull()) {
            "More than one generated python file is unsupported yet"
        }

        PythonTestChecker.check(generatedPyFilePath)
    }

    private fun generatePythonFile(
        tmpDir: File,
        testDir: String,
        module: TestModule,
        outputFilePath: String,
        multiModule: Boolean,
        testPackage: String?,
        needsFullIrRuntime: Boolean,
        isMainModule: Boolean,
    ) {
        val kotlinFiles = module.files.filter { it.filePath.endsWith(".${KotlinFileType.EXTENSION}") }
        val kotlinFilePaths = kotlinFiles.map { it.filePath }
        val localCommonFilePath = "$testDir/_common.${KotlinFileType.EXTENSION}"
        val existingLocalCommonFilePath = localCommonFilePath.takeIf { File(it).exists() }
        val allSourceFiles = (kotlinFilePaths + listOfNotNull(existingLocalCommonFilePath)).map(::File)
        val sortedFileNames = allSourceFiles.map(File::getCanonicalPath).sorted()
        val psiFiles = sortedFileNames.map(::createPsiFile)

        val config = createConfig(
            module = module,
            multiModule = multiModule,
            tmpDir = tmpDir,
        )
        val outputFile = File(outputFilePath)

        translateFiles(
            psiFiles = psiFiles,
            outputFile = outputFile,
            config = config,
            testPackage = testPackage,
            needsFullIrRuntime = needsFullIrRuntime,
            isMainModule = isMainModule,
        )
    }

    private fun createPsiFile(fileName: String): KtFile {
        val psiManager = PsiManager.getInstance(project)
        val fileSystem = VirtualFileManager.getInstance().getFileSystem(StandardFileSystems.FILE_PROTOCOL)

        val file = fileSystem.findFileByPath(fileName) ?: error("File not found: $fileName")

        return psiManager.findFile(file) as KtFile
    }

    private fun createConfig(
        module: TestModule,
        multiModule: Boolean,
        tmpDir: File,
    ): JsConfig {
        val configuration = environment.configuration.copy()

        module.languageVersionSettings?.let { configuration.languageVersionSettings = it }

        val libraries = JsConfig.JS_STDLIB + JsConfig.JS_KOTLIN_TEST

        configuration.put(JSConfigurationKeys.LIBRARIES, libraries)

        configuration.put(CommonConfigurationKeys.MODULE_NAME, module.name)

        configuration.put(JSConfigurationKeys.META_INFO, multiModule)

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
        val tmpDir = KtTestUtil.tmpDir("py-tests")
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

            val temporaryFile = tmpDir.resolve("${currentModule.name}/$fileName")
            temporaryFile.writeSafe(text)

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

    private class TestFile(val filePath: String, val module: TestModule) {
        init {
            module.files += this
        }
    }

    private class TestModule(
        name: String,
        dependencies: List<String>,
        friends: List<String>,
    ) : KotlinBaseTest.TestModule(name, dependencies, friends) {
        val files = mutableListOf<TestFile>()
        var languageVersionSettings: LanguageVersionSettings? = null
    }

    override fun createEnvironment() =
        KotlinCoreEnvironment.createForTests(testRootDisposable, CompilerConfiguration(), EnvironmentConfigFiles.JS_CONFIG_FILES)

    private fun translateFiles(
        psiFiles: List<KtFile>,
        outputFile: File,
        config: JsConfig,
        testPackage: String?,
        needsFullIrRuntime: Boolean,
        isMainModule: Boolean,
    ) {
        val allKlibPaths = if (needsFullIrRuntime) listOf(fullRuntimeKlib, kotlinTestKLib) else listOf(defaultRuntimeKlib)

        if (isMainModule) {
            val phaseConfig = PhaseConfig(pyPhases)

            val module = prepareAnalyzedSourceModule(
                config.project,
                psiFiles,
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
                        mainArguments = null,
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
            TODO()  // todo: specify a message here to make the problem distinguishable in reports
        }
    }

    companion object {
        val METADATA_CACHE = (JsConfig.JS_STDLIB + JsConfig.JS_KOTLIN_TEST).flatMap { path ->
            KotlinJavascriptMetadataUtils.loadMetadata(path).map { metadata ->
                val parts = KotlinJavascriptSerializationUtil.readModuleAsProto(metadata.body, metadata.version)
                JsModuleDescriptor(metadata.moduleName, parts.kind, parts.importedModules, parts)
            }
        }

        private val KJS_WITH_FULL_RUNTIME = Pattern.compile("^// *KJS_WITH_FULL_RUNTIME *\$", Pattern.MULTILINE)

        private const val DEFAULT_MODULE = "main"
        private const val TEST_FUNCTION = "box"

        private fun getOutputDir(testFile: File, stopDir: File, compilationGroupDir: File): File {
            return generateSequence(testFile.parentFile) { it.parentFile }
                .takeWhile { it != stopDir }
                .map { it.name }
                .toList().asReversed()
                .fold(compilationGroupDir, ::File)
        }

        private fun File.writeSafe(text: String) {
            parentFile.mkdirs()
            writeText(text)
        }

        private fun PyCode.writeTo(outputFile: File) {
            val wrappedCode = mainModule
            outputFile.writeSafe(wrappedCode)

            val dependencyPaths = mutableListOf<String>()

            dependencies.forEach { (moduleId, code) ->
                val dependencyPath = outputFile.absolutePath.replace(".py", "-${moduleId}.py")
                dependencyPaths += dependencyPath
                File(dependencyPath).writeSafe(code)
            }
        }
    }
}
