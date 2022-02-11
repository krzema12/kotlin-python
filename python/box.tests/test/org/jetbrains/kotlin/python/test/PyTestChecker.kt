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
import kotlin.io.path.copyTo
import kotlin.io.path.writeText
import kotlin.system.measureTimeMillis

class PythonExecutionException(override val message: String) : RuntimeException(message)

object PythonTestChecker {

    const val EXPECTED_RESULT = "OK"

    fun check(generatedPyFilePath: String) {
        val actualResult = run(generatedPyFilePath)
        assertEquals(EXPECTED_RESULT, actualResult)
    }

    private fun run(generatedPyFilePath: String): Any {
        val generatedPyFile = Paths.get(generatedPyFilePath)

        val temporaryDirectory = Files.createTempDirectory(generatedPyFile.parent, generatedPyFile.fileName.toString())
        try {
            generatedPyFile.copyTo(temporaryDirectory.resolve("compiled_module.py"))
            val consumerScriptPath = temporaryDirectory.resolve("consumer.py")
            consumerScriptPath.writeText(
                """
                    from compiled_module import box
        
                    print(box())
                """.trimIndent()
            )

            return runPython(consumerScriptPath.toString())
        } finally {
            temporaryDirectory.toFile().deleteRecursively()
        }
    }

    private fun runPython(scriptPath: String): String {
        val interpreterBinary = requireNotNull(System.getProperty("kotlin.py.interpreter.binary")) {
            "Python interpreter binary is not set! It should be set by the build logic."
        }
        val process = Runtime.getRuntime().exec("$interpreterBinary $scriptPath")
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
