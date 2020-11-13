/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package asdl

import org.junit.Assert.assertEquals
import org.junit.Test

class ParsingTest {

    @Test
    fun correctParsingOfSimpleAsdl() {
        // given
        val simpleAsdl = ParsingTest::class.java.getResource("/Simple.asdl").readText()

        // when
        val parsedAsdl = parseAsdl(simpleAsdl)

        // then
        val expectedAsdl = AsdlModule(
            name = "SimpleModule",
            types = listOf(
                AsdlTypeDefinition(
                    name = "mod",
                    constructors = listOf(
                        AsdlConstructor(
                            name = "Module",
                            attributes = listOf(
                                AsdlAttribute(
                                    name = "body",
                                    type = AsdlTypeReference("stmt"),
                                    quantity = AsdlQuantity.ZeroOrMore,
                                ),
                            )
                        )
                    )
                ),
                AsdlTypeDefinition(
                    name = "stmt",
                    constructors = listOf(
                        AsdlConstructor(
                            name = "FunctionDef",
                            attributes = listOf(
                                AsdlAttribute(
                                    name = "name",
                                    type = identifier,
                                ),
                                AsdlAttribute(
                                    name = "type_comment",
                                    type = string,
                                    quantity = AsdlQuantity.Optional,
                                )
                            )
                        )
                    ),
                    attributes = listOf(
                        AsdlAttribute(
                            name = "lineno",
                            type = int,
                        ),
                        AsdlAttribute(
                            name = "col_offset",
                            type = int,
                        ),
                    )
                ),
                AsdlTypeDefinition(
                    name = "expr",
                    constructors = listOf(
                        AsdlConstructor(
                            name = "NamedExpr",
                            attributes = listOf(
                                AsdlAttribute(
                                    name = "target",
                                    type = AsdlTypeReference("expr"),
                                ),
                                AsdlAttribute(
                                    name = "value",
                                    type = AsdlTypeReference("expr"),
                                ),
                            )
                        ),
                        AsdlConstructor(
                            name = "Constant",
                            attributes = listOf(
                                AsdlAttribute(
                                    name = "value",
                                    type = constant,
                                ),
                                AsdlAttribute(
                                    name = "kind",
                                    type = string,
                                    quantity = AsdlQuantity.Optional,
                                ),
                            )
                        )
                    )
                ),
                AsdlTypeDefinition(
                    name = "expr_context",
                    constructors = listOf(
                        AsdlConstructor("Load"),
                        AsdlConstructor("Store"),
                        AsdlConstructor("Del"),
                    )
                ),
                AsdlTypeDefinition(
                    name = "comprehension",
                    constructors = listOf(
                        AsdlConstructor(
                            name = null,
                            attributes = listOf(
                                AsdlAttribute(
                                    name = "target",
                                    type = AsdlTypeReference("expr"),
                                ),
                            ),
                        ),
                    ),
                ),
                AsdlTypeDefinition(
                    name = "arg",
                    constructors = listOf(
                        AsdlConstructor(
                            name = null,
                            attributes = listOf(
                                AsdlAttribute(
                                    name = "arg",
                                    type = identifier,
                                ),
                            ),
                        ),
                    ),
                    attributes = listOf(
                        AsdlAttribute(
                            name = "lineno",
                            type = int,
                        ),
                    ),
                )
            ),
        )
        assertEquals(expectedAsdl, parsedAsdl)
    }

    @Test
    fun parsingOfExamplePythonAsdlDoesNotFail() {
        // given
        val simpleAsdl = ParsingTest::class.java.getResource("/Python39.asdl").readText()

        // when
        val parsedAsdl = parseAsdl(simpleAsdl)

        // then
        assertEquals("Python", parsedAsdl.name)
    }

}
