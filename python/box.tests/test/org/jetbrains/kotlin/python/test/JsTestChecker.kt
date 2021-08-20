/*
 * Copyright 2010-2018 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.python.test

import org.jetbrains.kotlin.js.engine.ScriptEngine
import org.jetbrains.kotlin.js.engine.ScriptEngineNashorn
import org.junit.Assert
import java.io.BufferedReader
import java.io.InputStreamReader
import java.nio.file.Files
import java.nio.file.Paths
import java.util.concurrent.TimeUnit
import kotlin.system.measureTimeMillis

fun createScriptEngine(): ScriptEngine {
    return ScriptEngineNashorn()
}

fun ScriptEngine.overrideAsserter() {
    eval("this['kotlin-test'].kotlin.test.overrideAsserter_wbnzx$(this['kotlin-test'].kotlin.test.DefaultAsserter);")
}

fun ScriptEngine.runTestFunction(
    testModuleName: String?,
    testPackageName: String?,
    testFunctionName: String,
    withModuleSystem: Boolean
): String {
    var script = when {
        withModuleSystem -> BasicBoxTest.KOTLIN_TEST_INTERNAL + ".require('" + testModuleName!! + "')"
        testModuleName === null -> "this"
        else -> testModuleName
    }

    if (testPackageName !== null) {
        script += ".$testPackageName"
    }

    script += ".$testFunctionName()"

    return eval(script)
}

abstract class AbstractJsTestChecker {
    fun check(
        files: List<String>,
        testModuleName: String?,
        testPackageName: String?,
        testFunctionName: String,
        expectedResult: String,
        withModuleSystem: Boolean
    ) {
        val actualResult = run(files, testModuleName, testPackageName, testFunctionName, withModuleSystem)
        Assert.assertEquals(expectedResult, actualResult)
    }

    private fun run(
        files: List<String>,
        testModuleName: String?,
        testPackageName: String?,
        testFunctionName: String,
        withModuleSystem: Boolean
    ) = run(files) {
        runTestFunction(testModuleName, testPackageName, testFunctionName, withModuleSystem)
    }


    fun run(files: List<String>) {
        run(files) { null }
    }

    abstract fun checkStdout(files: List<String>, expectedResult: String)

    protected abstract fun run(files: List<String>, f: ScriptEngine.() -> Any?): Any?
}

class PythonExecutionException(override val message: String) : RuntimeException(message)

object PythonTestChecker : AbstractJsTestChecker() {
    override fun run(files: List<String>, f: ScriptEngine.() -> Any?): Any? {
        assert(files.size == 1) { "For now the test checker supports a single output from the compiler!" }
        val fileToRun = files[0]
        val pathToFileToRun = Paths.get(fileToRun)

        val temporaryDirectory = Files.createTempDirectory(pathToFileToRun.parent, pathToFileToRun.fileName.toString())
        Files.copy(pathToFileToRun, temporaryDirectory.resolve("compiled_module.py"))
        val consumerScriptPath = temporaryDirectory.resolve("consumer.py")
        consumerScriptPath.toFile().writeText("""
            from compiled_module import box

            print(box())
        """.trimIndent())

        val pythonOutput = runPython(consumerScriptPath.toString())
        temporaryDirectory.toFile().deleteRecursively()
        return pythonOutput
    }

    override fun checkStdout(files: List<String>, expectedResult: String) {
        TODO("Not yet implemented")
    }

    private fun runPython(scriptPath: String): String {
        val process = Runtime.getRuntime().exec("python3.8 $scriptPath")
        val runningTime = measureTimeMillis {
            process.waitFor(10, TimeUnit.SECONDS)
        }
        val runningTimeMessage = "Python running time: $runningTime ms"
        val exitValue = try {
            process.exitValue()
        } catch (e: IllegalThreadStateException) {
            // If the process hasn't finished yet.
            process.destroyForcibly()
            123 // Some non-zero value, doesn't matter what.
        }

        if (exitValue != 0) {
            val stderrReader = BufferedReader(InputStreamReader(process.errorStream))
            val stderr = stderrReader.lineSequence().toList().takeLast(10).joinToString("\n")
            throw PythonExecutionException("$runningTimeMessage\n$stderr")
        } else {
            val stdoutReader = BufferedReader(InputStreamReader(process.inputStream))
            return stdoutReader.lineSequence().joinToString("\n")
        }
    }
}

fun ScriptEngine.runAndRestoreContext(f: ScriptEngine.() -> Any?): Any? {
    return try {
        saveGlobalState()
        f()
    } finally {
        restoreGlobalState()
    }
}
