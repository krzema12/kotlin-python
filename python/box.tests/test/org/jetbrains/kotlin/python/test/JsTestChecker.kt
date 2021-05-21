/*
 * Copyright 2010-2018 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.python.test

import org.jetbrains.kotlin.js.engine.ScriptEngine
import org.jetbrains.kotlin.js.engine.ScriptEngineNashorn
import org.junit.Assert
import java.io.InputStreamReader
import java.nio.file.Paths
import java.util.concurrent.ConcurrentLinkedQueue
import kotlin.concurrent.thread

fun createScriptEngine(): ScriptEngine {
    return ScriptEngineNashorn()
}

fun ScriptEngine.overrideAsserter() {
    evalVoid("this['kotlin-test'].kotlin.test.overrideAsserter_wbnzx$(this['kotlin-test'].kotlin.test.DefaultAsserter);")
}

fun ScriptEngine.runTestFunction(
    testModuleName: String?,
    testPackageName: String?,
    testFunctionName: String,
    withModuleSystem: Boolean
): String? {
    var script = when {
        withModuleSystem -> BasicBoxTest.KOTLIN_TEST_INTERNAL + ".require('" + testModuleName!! + "')"
        testModuleName === null -> "this"
        else -> testModuleName
    }

    if (testPackageName !== null) {
        script += ".$testPackageName"
    }

    val testPackage = eval<Any>(script)
    return callMethod<String?>(testPackage, testFunctionName).also {
        releaseObject(testPackage)
    }
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

class PythonException(override val message: String) : RuntimeException(message)

object PythonTestChecker : AbstractJsTestChecker() {

    // -u: force the stdout and stderr streams to be unbuffered
    // -q: don't print version and copyright messages on interactive startup
    // -i: forces a prompt even if stdin does not appear to be a terminal
    private val process = Runtime.getRuntime().exec("python3.8 -q -u -i").also { process ->
        Runtime.getRuntime().addShutdownHook(thread(start = false) {
            process.destroy()
        })
    }

    private val stdoutReader = process.inputStream.reader()
    private val stderrReader = process.errorStream.reader()
    private val stdinWriter = process.outputStream.writer()

    private fun writeLine(line: String = "") {
        stdinWriter.appendLine(line)
        stdinWriter.flush()
        println("Written line: $line")
    }

    private fun enqueueOutput(reader: InputStreamReader, queue: ConcurrentLinkedQueue<Char>) = thread(isDaemon = true) {
        while (true) {
            val nextChar = reader.read()
            if (nextChar == -1) {
                break
            } else {
                queue.add(nextChar.toChar())
            }
        }
    }

    private val outQueue = ConcurrentLinkedQueue<Char>()  // contains output
        .also { enqueueOutput(stdoutReader, it) }

    private val errQueue = ConcurrentLinkedQueue<Char>()  // contains chevrons
        .also { enqueueOutput(stderrReader, it) }

    private fun ConcurrentLinkedQueue<Char>.getString() = buildString {
        this@getString.forEach {
            this.append(it)
        }
    }

    private fun extractOut() = buildString {
        outQueue.removeAll {
            this.append(it)
            true
        }
        println("Extracted out: '$this'")
    }

    private fun waitForExecution(): String {
        // take one chevron out of the queue and extract output
        println("Taking one chevron out from errQueue...")
        while (true) {
            val indexOfChevron = errQueue.getString().indexOf(chevron)
            if (indexOfChevron == -1) {
                Thread.sleep(1)
            } else {
                println("Taking one chevron out from '${errQueue.getString()}'")
                repeat(indexOfChevron + chevron.length) {
                    errQueue.remove()
                }
                break
            }
        }
        println("Took one chevron out, remaining: '${errQueue.getString()}'")
        return extractOut()
    }

    private val chevron = "CHEVRON>".also {
        // it shouldn't be empty to be able to detect
        // also, it should be quite unique to avoid colisions with other output
        check(it.isNotEmpty())
    }

    init {
        writeLine("""import sys; sys.ps1 = "$chevron"; sys.ps2 = "";""")
        waitForExecution()
    }

    override fun run(files: List<String>, f: ScriptEngine.() -> Any?): Any? {
        assert(files.size == 1) { "For now the test checker supports a single output from the compiler!" }
        val fileToRun = files[0]
        val pathToFileToRun = Paths.get(fileToRun)

        return runPython(pathToFileToRun.toString())
    }

    override fun checkStdout(files: List<String>, expectedResult: String) {
        TODO("Not yet implemented")
    }

    private fun runPython(scriptPath: String): String {
        writeLine("""with open("$scriptPath", "r", encoding="utf-8") as script: exec(script.read())""")
        writeLine()  // end entering the previous command
        waitForExecution()

        // 1. We can't just do writeLine("""print(box())""") because it seems that code that throwing an exception hangs an interpreter
        //    process: no info is output anymore, even no visible error is output.
        //    So let's surround this print with try-except and print the exception text manually

        // 2. To distinguish an exception from a normal result, let's add a prefix to the output.

        val normal = "normal"
        val exception = "exception"

        writeLine("""try: print("$normal", box(), sep="")""")
        writeLine("""except: import traceback; print("$exception", traceback.format_exc(), sep="")""")
        writeLine()  // end entering the previous command

        val stdout = waitForExecution()
        check(stdout.startsWith(normal) || stdout.startsWith(exception)) { "Can't obtain stdout for some reason" }

        if (stdout.startsWith(normal)) {
            return stdout.removePrefix(normal)
        } else {
            throw PythonException(stdout.removePrefix(exception))
        }
    }
}

fun ScriptEngine.runAndRestoreContext(f: ScriptEngine.() -> Any?): Any? {
    return try {
        saveState()
        f()
    } finally {
        restoreState()
    }
}
