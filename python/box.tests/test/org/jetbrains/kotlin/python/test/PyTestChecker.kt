/*
 * Copyright 2010-2018 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.python.test

import org.junit.Assert.assertEquals
import java.io.BufferedReader
import java.io.InputStreamReader
import java.nio.file.Files
import java.nio.file.Paths
import java.util.concurrent.TimeUnit
import kotlin.system.measureTimeMillis

abstract class AbstractPyTestChecker {
    fun check(files: List<String>, expectedResult: String) {
        val actualResult = run(files)
        assertEquals(expectedResult, actualResult)
    }

    protected abstract fun run(files: List<String>): Any
}

class PythonExecutionException(override val message: String) : RuntimeException(message)

object PythonTestChecker : AbstractPyTestChecker() {
    override fun run(files: List<String>): Any {
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
            val stderr = try {
                val stderrReader = BufferedReader(InputStreamReader(process.errorStream))
                stderrReader.lineSequence().toList().takeLast(10).joinToString("\n")
            } catch (e: Exception) {
                "There was a problem when extracting the contents of STDERR. Details: $e"
            }
            throw PythonExecutionException("$runningTimeMessage\n$stderr")
        } else {
            val stdoutReader = BufferedReader(InputStreamReader(process.inputStream))
            return stdoutReader.lineSequence().joinToString("\n")
        }
    }
}
