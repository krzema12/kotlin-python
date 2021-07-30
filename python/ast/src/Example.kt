import generated.Python.*
import generated.Python.List
import topython.toPython

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
// >>> import ast; print(ast.dump(ast.parse('fruits = ["apple", "banana", "cherry"]\nfor x in fruits:\n    print(x)')))
// Module(
//   body=[
//     Assign(
//       targets=[Name(id='fruits', ctx=Store())],
//       value=List(
//         elts=[
//           Constant(value='apple', kind=None),
//           Constant(value='banana', kind=None),
//           Constant(value='cherry', kind=None)
//         ],
//         ctx=Load()
//       ),
//       type_comment=None
//     ),
//     For(
//       target=Name(id='x', ctx=Store()),
//       iter=Name(id='fruits', ctx=Load()),
//       body=[Expr(
//         value=Call(
//           func=Name(id='print', ctx=Load()),
//           args=[Name(id='x', ctx=Load())],
//           keywords=[]
//         ))
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
            targets = listOf(Name(id = identifier("fruits"), ctx = Store)),
            value = List(
                elts = listOf(
                    Constant(value = constant("\"apple\""), kind = null),
                    Constant(value = constant("\"banana\""), kind = null),
                    Constant(value = constant("\"cherry\""), kind = null),
                ),
                ctx = Load,
            ),
            type_comment = null,
        ),
        For(
            target = Name(id = identifier("x"), ctx = Store),
            iter = Name(id = identifier("fruits"), ctx = Load),
            body = listOf(Expr(
                value = Call(
                    func = Name(id = identifier("print"), ctx = Load),
                    args = listOf(Name(id = identifier("x"), ctx = Load),),
                    keywords = emptyList(),
                ))
            ),
            orelse = emptyList(),
            type_comment = null,
        ),
    ),
    type_ignores = emptyList(),
)

fun main() {
    println(buildString { examplePythonCodeAst.toPython(this) })
    // Produces:
    //
    // fruits = ["apple", "banana", "cherry"]
    // for x in fruits:
    //     print(x)
}
