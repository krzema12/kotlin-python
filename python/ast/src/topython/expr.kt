/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package topython

import generated.Python.*
import generated.Python.List
import generated.Python.Set

fun expr.toPython(acc: StringBuilder) = when (this) {
    is Name -> toPython(acc)
    is BoolOp -> TODO()
    is NamedExpr -> TODO()
    is BinOp -> toPython(acc)
    is UnaryOp -> toPython(acc)
    is Lambda -> TODO()
    is IfExp -> toPython(acc)
    is Dict -> TODO()
    is Set -> TODO()
    is ListComp -> TODO()
    is SetComp -> TODO()
    is DictComp -> TODO()
    is GeneratorExp -> TODO()
    is Await -> TODO()
    is Yield -> TODO()
    is YieldFrom -> TODO()
    is Compare -> toPython(acc)
    is Call -> toPython(acc)
    is FormattedValue -> TODO()
    is JoinedStr -> TODO()
    is Constant -> toPython(acc)
    is Attribute -> toPython(acc)
    is Subscript -> toPython(acc)
    is Starred -> TODO()
    is List -> toPython(acc)
    is Tuple -> TODO()
    is Slice -> TODO()
}

fun Name.toPython(acc: StringBuilder) {
    acc.append(id.name)
}

fun BinOp.toPython(acc: StringBuilder) {
    acc.append('(')
    left.toPython(acc)
    acc.append(") ")
    acc.append(op.toPython())
    acc.append(" (")
    right.toPython(acc)
    acc.append(')')
}

fun UnaryOp.toPython(acc: StringBuilder) {
    acc.append(op.toPython())
    acc.append('(')
    operand.toPython(acc)
    acc.append(')')
}

fun IfExp.toPython(acc: StringBuilder) {
    acc.append('(')
    body.toPython(acc)
    acc.append(") if (")
    test.toPython(acc)
    acc.append(") else (")
    orelse.toPython(acc)
    acc.append(')')
}

fun List.toPython(acc: StringBuilder) {
    acc.append('[')
    elts.forEachIndexed { i, it ->
        if (i != 0) {
            acc.append(", ")
        }
        it.toPython(acc)
    }
    acc.append(']')
}

fun Constant.toPython(acc: StringBuilder) {
    acc.append(value.value.replace("\n", "\\n"))
}

fun Compare.toPython(acc: StringBuilder) {
    left.toPython(acc)
    ops.zip(comparators).forEach { (op, c) ->
        acc.append(' ')
        acc.append(op.toPython())
        acc.append(' ')
        c.toPython(acc)
    }
}

fun Call.toPython(acc: StringBuilder) {
    func.toPython(acc)
    acc.append('(')
    args.forEachIndexed { i, it ->
        if (i != 0) {
            acc.append(", ")
        }
        it.toPython(acc)
    }
    acc.append(')')
}

fun Attribute.toPython(acc: StringBuilder) {
    value.toPython(acc)
    acc.append('.')
    acc.append(attr.name)
}

fun Subscript.toPython(acc: StringBuilder) {
    value.toPython(acc)
    acc.append('[')
    slice.toPython(acc)
    acc.append(']')
}
