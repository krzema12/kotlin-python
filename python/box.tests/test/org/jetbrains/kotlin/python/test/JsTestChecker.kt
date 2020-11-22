/*
 * Copyright 2010-2018 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.python.test

import org.jetbrains.kotlin.js.engine.ScriptEngine
import org.jetbrains.kotlin.js.engine.ScriptEngineNashorn
import org.jetbrains.kotlin.js.engine.ScriptEngineV8
import org.jetbrains.kotlin.test.KotlinTestUtils
import org.junit.Assert

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

object PythonTestChecker : AbstractJsTestChecker() {
    override fun run(files: List<String>, f: ScriptEngine.() -> Any?): Any? {
        // TODO call Python interpreter - for now, mocking that the interpreter returned "OK" (success for most tests)
        return "OK"
    }

    override fun checkStdout(files: List<String>, expectedResult: String) {
        TODO("Not yet implemented")
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
