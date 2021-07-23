/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package python.ast

import examplePythonCodeAst
import generated.Python.*
import org.junit.Assert.assertEquals
import org.junit.Test
import topython.toPython

class PythonAstTest {

    @Test
    fun testToPython() {
        val expected = """
            fruits = ["apple", "banana", "cherry"]
            for x in fruits:
                print(x)
        """.trimIndent()

        assertEquals(expected, examplePythonCodeAst.toPython())
    }

    @Test
    fun testCompareToPython() {
        val expected = "1 <= a < 10"
        val initial = Compare(
            left = Constant(constant("1"), null),
            ops = listOf(LtE, Lt),
            comparators = listOf(
                Name(identifier("a"), Load),
                Constant(constant("10"), null),
            ),
        )
        val actual = initial.toPython()

        assertEquals(expected, actual)
    }

    @Test
    fun testElifToPython() {
        val expected = """
            |if a <= 5:
            |    branch1
            |elif a <= 10:
            |    branch2
            |else:
            |    branch3
            |
        """.trimMargin()
        val initial = If(
            test = Compare(
                left = Name(identifier("a"), Load),
                ops = listOf(LtE),
                comparators = listOf(Constant(constant("5"), null)),
            ),
            body = listOf(Expr(Name(identifier("branch1"), Load))),
            orelse = listOf(
                If(
                    test = Compare(
                        left = Name(identifier("a"), Load),
                        ops = listOf(LtE),
                        comparators = listOf(Constant(constant("10"), null)),
                    ),
                    body = listOf(Expr(Name(identifier("branch2"), Load))),
                    orelse = listOf(Expr(Name(identifier("branch3"), Load))),
                )
            ),
        )
        val actual = initial.toPython()

        assertEquals(expected, actual)
    }
}
