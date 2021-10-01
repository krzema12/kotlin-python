/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.generators.tests

import org.jetbrains.kotlin.python.test.ir.semantics.AbstractIrPythonCodegenBoxErrorTest
import org.jetbrains.kotlin.python.test.ir.semantics.AbstractIrPythonCodegenBoxTest
import org.jetbrains.kotlin.python.test.ir.semantics.AbstractIrPythonCodegenInlineTest
import org.jetbrains.kotlin.test.TargetBackend
import org.jetbrains.kotlin.test.generators.generateTestGroupSuiteWithJUnit5

fun main(args: Array<String>) {
    System.setProperty("java.awt.headless", "true")

    generateTestGroupSuiteWithJUnit5(args) {
        testGroup("python/box.tests/test", "compiler/testData") {
            testClass<AbstractIrPythonCodegenBoxTest> {
                model("codegen/box", targetBackend = TargetBackend.PYTHON)
            }

            testClass<AbstractIrPythonCodegenBoxErrorTest> {
                model("codegen/boxError", targetBackend = TargetBackend.PYTHON)
            }

            testClass<AbstractIrPythonCodegenInlineTest> {
                model("codegen/boxInline/", targetBackend = TargetBackend.PYTHON)
            }
        }
    }
}
