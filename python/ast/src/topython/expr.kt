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
        is BoolOp -> TODO()
        is NamedExpr -> TODO()
        is BinOp -> TODO()
        is UnaryOp -> TODO()
        is Lambda -> TODO()
        is IfExp -> toPython()
        is Dict -> TODO()
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
        is Subscript -> TODO()
        is Starred -> TODO()
        is List -> toPython()
        is Tuple -> TODO()
        is Slice -> TODO()
    }
}

fun Name.toPython() =
    id.name

fun IfExp.toPython() =
    "(${body.toPython()}) if (${test.toPython()}) else (${orelse.toPython()})"

fun List.toPython() =
    elts.joinToString(separator = ", ", prefix = "[", postfix = "]") {
        it.toPython()
    }

fun Constant.toPython() =
    value.value.replace("\n", "\\n")

fun Compare.toPython() =
    "${left.toPython()}${ops.zip(comparators).joinToString("") { (op, c) -> " ${op.toPython()} ${c.toPython()}" }}"

fun Call.toPython() =
    "${func.toPython()}(${args.joinToString(", ") { it.toPython() }})"

fun Attribute.toPython() =
    "${value.toPython()}.${attr.name}"
