/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package topython

import generated.Python.*

fun stmt.toPython(): String {
    return when (this) {
        is Assign -> toPython()
        is FunctionDef -> toPython()
        is AsyncFunctionDef -> TODO()
        is ClassDef -> toPython()
        is Return -> toPython()
        is Delete -> TODO()
        is AugAssign -> TODO()
        is AnnAssign -> TODO()
        is For -> toPython()
        is AsyncFor -> TODO()
        is While -> toPython()
        is If -> toPython()
        is With -> TODO()
        is AsyncWith -> TODO()
        is Raise -> TODO()
        is Try -> TODO()
        is Assert -> TODO()
        is Import -> TODO()
        is ImportFrom -> TODO()
        is Global -> TODO()
        is Nonlocal -> TODO()
        is Expr -> toPython()
        Pass -> "pass"
        Break -> TODO()
        Continue -> TODO()
    }
}

fun Assign.toPython() =
    "${if (targets.size == 1) targets[0].toPython() else targets.joinToString(separator = ", ", prefix = "[", postfix = "]")} = ${value.toPython()}"

fun For.toPython() =
    "for ${target.toPython()} in ${iter.toPython()}:\n${body.toPython().indent()}"

fun Expr.toPython() =
    value.toPython()

fun FunctionDef.toPython() =
    "def ${name.name}(${args.toPython()}):\n${(if (body.isNotEmpty()) body.toPython() else "pass").indent()}\n"

fun List<stmt>.toPython() =
    joinToString("\n") { it.toPython() }

fun Return.toPython() =
    value?.let { "return ${it.toPython()}" } ?: "return"

fun While.toPython() =
    "while ${test.toPython()}:\n${body.toPython().indent()}\n"

fun If.toPython() =
    "if ${test.toPython()}:\n${(if (body.isNotEmpty()) body.toPython() else "pass").indent()}\n${if (orelse.isNotEmpty()) "else:\n${orelse.toPython().indent()}\n" else ""}"

fun ClassDef.toPython() =
    "${if (bases.isNotEmpty()) bases.joinToString("") { "class ${it.toPython()}:\n${"pass".indent()}\n\n" } else ""}class ${name.name}${if (bases.isNotEmpty()) "(${bases.joinToString(", ") { it.toPython() }})" else ""}:\n${(if (body.isNotEmpty()) body.toPython() else "pass").indent()}\n"
