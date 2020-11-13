import generated.Python.*
import generated.Python.List

/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

// For such Python code:
//
// fruits = ["apple", "banana", "cherry"]
// for x in fruits:
//   print(x)
//
// Python generates such AST:
// >>> print(ast.dump(ast.parse('fruits = ["apple", "banana", "cherry"]\nfor x in fruits:\n    print(x)')))
// Module(
//   body=[
//     Assign(
//       targets=[
//         Name(
//           id='fruits',
//           ctx=Store()
//         )
//       ],
//       value=List(
//         elts=[
//           Constant(
//             value='apple',
//             kind=None
//           ),
//           Constant(
//             value='banana',
//             kind=None
//           ),
//           Constant(
//             value='cherry',
//             kind=None
//           )
//         ],
//         ctx=Load()
//       ),
//       type_comment=None
//     ),
//     For(
//       target=Name(
//         id='x',
//         ctx=Store()
//       ),
//       iter=Name(
//         id='fruits',
//         ctx=Load()
//       ),
//       body=[
//         Expr(
//           value=Call(
//             func=Name(
//               id='print',
//               ctx=Load()
//             ),
//             args=[
//               Name(
//                 id='x',
//                 ctx=Load()
//               )
//             ],
//             keywords=[]
//           )
//         )
//       ],
//       orelse=[],
//       type_comment=None
//     )
//   ],
//   type_ignores=[]
// )
//
// Recreating it below using generated Kotlin entities:

val examplePythonCodeAst: mod = Module(
    body = listOf(
        Assign(
            targets = listOf(
                Name(
                    id = identifier("fruits"),
                    ctx = Store,
                    lineno = int(0), // irrelevant, TODO make optional or remove
                    col_offset = int(0), // irrelevant, TODO make optional or remove
                    end_lineno = null, // irrelevant, TODO make optional or remove
                    end_col_offset = null, // irrelevant, TODO make optional or remove
                ),
            ),
            value = List(
                elts = listOf(
                    Constant(
                        value = constant("'apple'"),
                        kind = null,
                        lineno = int(0), // irrelevant, TODO make optional or remove
                        col_offset = int(0), // irrelevant, TODO make optional or remove
                        end_lineno = null, // irrelevant, TODO make optional or remove
                        end_col_offset = null, // irrelevant, TODO make optional or remove
                    ),
                    Constant(
                        value = constant("'banana'"),
                        kind = null,
                        lineno = int(0), // irrelevant, TODO make optional or remove
                        col_offset = int(0), // irrelevant, TODO make optional or remove
                        end_lineno = null, // irrelevant, TODO make optional or remove
                        end_col_offset = null, // irrelevant, TODO make optional or remove
                    ),
                    Constant(
                        value = constant("'cherry'"),
                        kind = null,
                        lineno = int(0), // irrelevant, TODO make optional or remove
                        col_offset = int(0), // irrelevant, TODO make optional or remove
                        end_lineno = null, // irrelevant, TODO make optional or remove
                        end_col_offset = null, // irrelevant, TODO make optional or remove
                    ),
                ),
                ctx = Load,
                lineno = int(0), // irrelevant, TODO make optional or remove
                col_offset = int(0), // irrelevant, TODO make optional or remove
                end_lineno = null, // irrelevant, TODO make optional or remove
                end_col_offset = null, // irrelevant, TODO make optional or remove
            ),
            type_comment = null,
            lineno = int(0), // irrelevant, TODO make optional or remove
            col_offset = int(0), // irrelevant, TODO make optional or remove
            end_lineno = null, // irrelevant, TODO make optional or remove
            end_col_offset = null, // irrelevant, TODO make optional or remove
        ),
        For(
            target = Name(
                id = identifier("x"),
                ctx = Store,
                lineno = int(0), // irrelevant, TODO make optional or remove
                col_offset = int(0), // irrelevant, TODO make optional or remove
                end_lineno = null, // irrelevant, TODO make optional or remove
                end_col_offset = null, // irrelevant, TODO make optional or remove
            ),
            iter = Name(
                id = identifier("fruits"),
                ctx = Load,
                lineno = int(0), // irrelevant, TODO make optional or remove
                col_offset = int(0), // irrelevant, TODO make optional or remove
                end_lineno = null, // irrelevant, TODO make optional or remove
                end_col_offset = null, // irrelevant, TODO make optional or remove
            ),
            body = listOf(
                Expr(
                    value = Call(
                        func = Name(
                            id = identifier("print"),
                            ctx = Load,
                            lineno = int(0), // irrelevant, TODO make optional or remove
                            col_offset = int(0), // irrelevant, TODO make optional or remove
                            end_lineno = null, // irrelevant, TODO make optional or remove
                            end_col_offset = null, // irrelevant, TODO make optional or remove
                        ),
                        args = listOf(
                            Name(
                                id = identifier("x"),
                                ctx = Load,
                                lineno = int(0), // irrelevant, TODO make optional or remove
                                col_offset = int(0), // irrelevant, TODO make optional or remove
                                end_lineno = null, // irrelevant, TODO make optional or remove
                                end_col_offset = null, // irrelevant, TODO make optional or remove
                            ),
                        ),
                        keywords = emptyList(),
                        lineno = int(0), // irrelevant, TODO make optional or remove
                        col_offset = int(0), // irrelevant, TODO make optional or remove
                        end_lineno = null, // irrelevant, TODO make optional or remove
                        end_col_offset = null, // irrelevant, TODO make optional or remove
                    ),
                    lineno = int(0), // irrelevant, TODO make optional or remove
                    col_offset = int(0), // irrelevant, TODO make optional or remove
                    end_lineno = null, // irrelevant, TODO make optional or remove
                    end_col_offset = null, // irrelevant, TODO make optional or remove
                ),
            ),
            orelse = emptyList(),
            type_comment = null,
            lineno = int(0), // irrelevant, TODO make optional or remove
            col_offset = int(0), // irrelevant, TODO make optional or remove
            end_lineno = null, // irrelevant, TODO make optional or remove
            end_col_offset = null, // irrelevant, TODO make optional or remove
        ),
    ),
    type_ignores = emptyList(),
)
