/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.inline.util

import org.jetbrains.kotlin.js.backend.ast.*
import org.jetbrains.kotlin.js.backend.ast.metadata.staticRef

import org.jetbrains.kotlin.py.inline.context.NamingContext
import org.jetbrains.kotlin.py.inline.util.rewriters.LabelNameRefreshingVisitor
import org.jetbrains.kotlin.py.translate.utils.JsAstUtils

fun aliasArgumentsIfNeeded(
        context: NamingContext,
        arguments: List<JsExpression>,
        parameters: List<JsParameter>,
        source: Any?
) {
    require(arguments.size <= parameters.size) { "arguments.size (${arguments.size}) should be less or equal to parameters.size (${parameters.size})" }

    val defaultParams = mutableListOf<JsParameter>()
    for ((arg, param) in arguments.zip(parameters)) {
        if (JsAstUtils.isUndefinedExpression(arg)) {
            defaultParams += param
            continue
        }
        val paramName = param.name

        val replacement = JsScope.declareTemporaryName(paramName.ident).apply {
            staticRef = arg
            context.newVar(this, arg.deepCopy(), source = source)
        }.makeRef()

        replacement.source = arg.source
        context.replaceName(paramName, replacement)
    }

    defaultParams += parameters.subList(arguments.size, parameters.size)
    for (defaultParam in defaultParams) {
        val paramName = defaultParam.name
        val freshName = JsScope.declareTemporaryName(paramName.ident)
        freshName.copyMetadataFrom(paramName)
        context.newVar(freshName, source = source)

        context.replaceName(paramName, freshName.makeRef())
    }
}

/**
 * Makes function local names fresh in context
 */
fun renameLocalNames(
        context: NamingContext,
        function: JsFunction
) {
    for (name in collectDefinedNames(function.body)) {
        val temporaryName = JsScope.declareTemporaryName(name.ident).apply { staticRef = name.staticRef }
        context.replaceName(name, temporaryName.makeRef())
    }
}

fun refreshLabelNames(
        node: JsNode,
        scope: JsScope
): JsNode {
    if (scope !is JsFunctionScope) throw AssertionError("JsFunction is expected to have JsFunctionScope")

    val visitor = LabelNameRefreshingVisitor(scope)
    return visitor.accept(node)
}
