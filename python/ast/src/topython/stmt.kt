/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package topython

import generated.Python.*

fun stmt.toPython(indent: String, acc: StringBuilder) = when (this) {
    is Assign -> toPython(indent, acc)
    is FunctionDef -> toPython(indent, acc)
    is AsyncFunctionDef -> TODO()
    is ClassDef -> toPython(indent, acc)
    is Return -> toPython(indent, acc)
    is Delete -> TODO()
    is AugAssign -> TODO()
    is AnnAssign -> TODO()
    is For -> toPython(indent, acc)
    is AsyncFor -> TODO()
    is While -> toPython(indent, acc)
    is If -> toPython(indent, acc)
    is With -> TODO()
    is AsyncWith -> TODO()
    is Raise -> TODO()
    is Try -> TODO()
    is Assert -> TODO()
    is Import -> TODO()
    is ImportFrom -> TODO()
    is Global -> TODO()
    is Nonlocal -> TODO()
    is Expr -> toPython(indent, acc)
    Pass -> passToPython(indent, acc)
    Break -> breakToPython(indent, acc)
    Continue -> continueToPython(indent, acc)
}

fun Assign.toPython(indent: String, acc: StringBuilder) {
    acc.append(indent)
    targets.singleOrNull()?.toPython(acc) ?: run {
        acc.append(targets.joinToString(separator = ", ", prefix = "[", postfix = "]"))  // todo: fix this
    }
    acc.append(" = ")
    value.toPython(acc)
}

fun For.toPython(indent: String, acc: StringBuilder) {
    acc.append(indent)
    acc.append("for ")
    target.toPython(acc)
    acc.append(" in ")
    iter.toPython(acc)
    acc.append(":\n")
    body.toPython(indent + oneLineIndent, acc)
}

fun Expr.toPython(indent: String, acc: StringBuilder) {
    acc.append(indent)
    value.toPython(acc)
}

fun FunctionDef.toPython(indent: String, acc: StringBuilder) {
    acc.append(indent)
    acc.append("def ")
    acc.append(name.name)
    acc.append('(')
    args.toPython(acc)
    acc.append("):\n")
    if (body.isNotEmpty()) {
        body.toPython(indent + oneLineIndent, acc)
    } else {
        Pass.toPython(indent + oneLineIndent, acc)
    }
    acc.append('\n')
}

fun List<stmt>.toPython(indent: String, acc: StringBuilder) {
    forEachIndexed { i, it ->
        if (i != 0) {
            acc.append('\n')
        }
        it.toPython(indent, acc)
    }
}

fun Return.toPython(indent: String, acc: StringBuilder) {
    acc.append(indent)
    value?.let {
        acc.append("return ")
        it.toPython(acc)
    } ?: run {
        acc.append("return")
    }
}

fun While.toPython(indent: String, acc: StringBuilder) {
    acc.append(indent)
    acc.append("while ")
    test.toPython(acc)
    acc.append(":\n")
    body.toPython(indent + oneLineIndent, acc)
    acc.append('\n')
}

fun If.toPythonWithoutFirstIndent(indent: String, acc: StringBuilder) {
    acc.append("if ")
    test.toPython(acc)
    acc.append(":\n")
    if (body.isNotEmpty()) {
        body.toPython(indent + oneLineIndent, acc)
    } else {
        Pass.toPython(indent + oneLineIndent, acc)
    }
    acc.append('\n')
    if (orelse.isEmpty()) {
        return
    }
    acc.append(indent)
    (orelse.singleOrNull() as? If)?.let {
        acc.append("el")
        it.toPythonWithoutFirstIndent(indent, acc)
    } ?: run {
        acc.append("else:\n")
        orelse.toPython(indent + oneLineIndent, acc)
        acc.append('\n')
    }
}

fun If.toPython(indent: String, acc: StringBuilder) {
    acc.append(indent)
    toPythonWithoutFirstIndent(indent, acc)
}

fun ClassDef.toPython(indent: String, acc: StringBuilder) {
    bases.forEach {
        acc.append(indent)
        acc.append("class ")
        it.toPython(acc)
        acc.append(":\n")
        Pass.toPython(indent + oneLineIndent, acc)
        acc.append("\n\n")
    }
    acc.append(indent)
    acc.append("class ")
    acc.append(name.name)
    if (bases.isNotEmpty()) {
        acc.append('(')
        bases.forEachIndexed { i, it ->
            if (i != 0) {
                acc.append(", ")
            }
            it.toPython(acc)
        }
        acc.append(')')
    }
    acc.append(":\n")
    if (body.isNotEmpty()) {
        body.toPython(indent + oneLineIndent, acc)
    } else {
        Pass.toPython(indent + oneLineIndent, acc)
    }
    acc.append('\n')
}

fun passToPython(indent: String, acc: StringBuilder) {
    acc.append(indent)
    acc.append("pass")
}

fun breakToPython(indent: String, acc: StringBuilder) {
    acc.append(indent)
    acc.append("break")
}

fun continueToPython(indent: String, acc: StringBuilder) {
    acc.append(indent)
    acc.append("continue")
}
