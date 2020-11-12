/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package asdl

import org.junit.Test

class ParsingTest {

    @Test
    fun successfulParsing() {
        // given
        val simpleAsdl = ParsingTest::class.java.getResource("/Simple.asdl").readText()

        // when
        val parsedAsdl = parseAsdl(simpleAsdl)

        // then
        val expectedAsdl = AsdlModule(
            name = "SimpleModule",
            types = listOf(
                AsdlType(
                    name = "mod",
                    constructors = listOf(
                        AsdlConstructor(
                            name = "Module",
                            attributes = listOf(
                                AsdlAttribute(
                                    name = "body",
                                    // Recursive reference to this type - not sure how to tackle this yet.
                                    type = AsdlType("stmt"),
                                    quantity = AsdlQuantity.ZeroOrMore,
                                ),
                            )
                        )
                    )
                ),
                AsdlType(
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
                AsdlType(
                    name = "expr",
                    constructors = listOf(
                        AsdlConstructor(
                            name = "NamedExpr",
                            attributes = listOf(
                                AsdlAttribute(
                                    name = "target",
                                    // Recursive reference to this type - not sure how to tackle this yet.
                                    type = AsdlType("expr"),
                                ),
                                AsdlAttribute(
                                    name = "value",
                                    // Recursive reference to this type - not sure how to tackle this yet.
                                    type = AsdlType("expr"),
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
                AsdlType(
                    name = "expr_constant",
                    constructors = listOf(
                        AsdlConstructor("Load"),
                        AsdlConstructor("Store"),
                        AsdlConstructor("Del"),
                    )
                )
            ),
        )
        // TODO compare expected and parsed once implemented
    }

}
