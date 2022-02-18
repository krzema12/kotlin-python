/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package topython

import generated.Python.*
import generated.Python.List
import generated.Python.Set

fun expr.toPython(): String {
    return when (this) {
        is Name -> toPython()
        is BoolOp -> toPython()
        is NamedExpr -> TODO()
        is BinOp -> toPython()
        is UnaryOp -> toPython()
        is Lambda -> toPython()
        is IfExp -> toPython()
        is Dict -> toPython()
        is Set -> TODO()
        is ListComp -> TODO()
        is SetComp -> TODO()
        is DictComp -> TODO()
        is GeneratorExp -> TODO()
        is Await -> TODO()
        is Yield -> TODO()
        is YieldFrom -> TODO()
        is Compare -> toPython()
        is Call -> toPython()
        is FormattedValue -> TODO()
        is JoinedStr -> TODO()
        is Constant -> toPython()
        is Attribute -> toPython()
        is Subscript -> toPython()
        is Starred -> toPython()
        is List -> toPython()
        is Tuple -> toPython()
        is Slice -> toPython()
    }
}

private fun expr.needsParentheses(forceEvaluate: Boolean) = when (this) {
    is Name -> false
    is UnaryOp -> forceEvaluate
    is List -> false
    is Constant -> forceEvaluate
    is Call -> false
    is Attribute -> false
    is Subscript -> false
    else -> true
}

private fun expr.surroundIfNeeded(forceEvaluate: Boolean = false) = when (needsParentheses(forceEvaluate)) {
    true -> "(${this.toPython()})"
    false -> this.toPython()
}

fun Name.toPython() =
    id.name

fun BoolOp.toPython() =
    values.joinToString(" ${op.toPython()} ") { it.surroundIfNeeded() }

fun BinOp.toPython() =
    "${left.surroundIfNeeded()} ${op.toPython()} ${right.surroundIfNeeded()}"

fun UnaryOp.toPython() =
    "${op.toPython()}${operand.surroundIfNeeded()}"

fun Lambda.toPython() =
    "lambda ${args.toPython()}: ${body.toPython()}"

fun IfExp.toPython() =
    "(${body.toPython()}) if (${test.toPython()}) else (${orelse.toPython()})"

fun Dict.toPython() =
    keys.zip(values).joinToString(prefix = "{", postfix = "}") { (k, v) -> "${k.toPython()}: ${v.toPython()}" }

fun List.toPython() =
    elts.joinToString(separator = ", ", prefix = "[", postfix = "]") {
        it.toPython()
    }

fun Tuple.toPython() =
    when (val single = elts.singleOrNull()) {
        null -> elts.joinToString(separator = ", ", prefix = "(", postfix = ")") { it.toPython() }
        else -> "(${single.toPython()},)"
    }

fun Constant.toPython() =
    value.value.replace("\n", "\\n")

fun Compare.toPython() =
    "${left.toPython()}${ops.zip(comparators).joinToString("") { (op, c) -> " ${op.toPython()} ${c.toPython()}" }}"

fun Call.toPython() =
    "${func.surroundIfNeeded(forceEvaluate = true)}(${args.joinToString(", ") { it.toPython() }})"

fun Attribute.toPython() =
    "${value.surroundIfNeeded(forceEvaluate = true)}.${attr.name}"

fun Subscript.toPython() =
    "${value.surroundIfNeeded(forceEvaluate = true)}[${slice.toPython()}]"

fun Starred.toPython() =
    "*${value.toPython()}"

fun Slice.toPython() =
    "${lower?.toPython() ?: ""}:${upper?.toPython() ?: ""}"