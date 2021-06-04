/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.inline.clean

import org.jetbrains.kotlin.js.backend.ast.*
import org.jetbrains.kotlin.js.backend.ast.metadata.isLocal
import org.jetbrains.kotlin.js.backend.ast.metadata.staticRef
import org.jetbrains.kotlin.py.inline.util.IdentitySet
import org.jetbrains.kotlin.py.inline.util.collectReferencedNames

/**
 * Removes unused function definitions:
 *  f: function() { return 10 }
 *
 * At now, it only removes unused local functions and function literals,
 * because named functions can be referenced from another module.
 */
fun removeUnusedFunctionDefinitions(root: JsNode, functions: Map<JsName, JsFunction>) {
    val removable = with(UnusedLocalFunctionsCollector(functions)) {
        process()
        accept(root)
        removableFunctions
    }.toSet()

    val remover = NodeRemover(JsStatement::class.java) { statement ->
        val expression = when (statement) {
            is JsExpressionStatement -> statement.expression
            is JsVars -> if (statement.vars.size == 1) statement.vars[0].initExpression else null
            else -> null
        }
        expression is JsFunction && expression in removable
    }

    remover.accept(root)
}

private class UnusedLocalFunctionsCollector(private val functions: Map<JsName, JsFunction>) : JsVisitorWithContextImpl() {
    private val tracker = ReferenceTracker<JsName, JsFunction>()
    private val processed = IdentitySet<JsFunction>()

    val removableFunctions: List<JsFunction>
        get() = tracker.removable

    fun process() {
        functions.filter { it.value.isLocal }
                 .forEach { tracker.addCandidateForRemoval(it.key, it.value) }

        for ((name, function) in functions) {
            if (function.isLocal) {
                processLocalFunction(name, function)
            } else {
                processNonLocalFunction(function)
            }

            processed.add(function)
        }
    }

    override fun visit(x: JsPropertyInitializer, ctx: JsContext<*>): Boolean {
        val value = x.valueExpr

        return when (value) {
            is JsFunction -> !wasProcessed(value)
            else -> super.visit(x, ctx)
        }
    }

    override fun visit(x: JsFunction, ctx: JsContext<*>): Boolean = !wasProcessed(x)

    override fun endVisit(x: JsFunction, ctx: JsContext<*>) {
        processed.add(x)
    }

    override fun endVisit(x: JsNameRef, ctx: JsContext<*>) {
        val name = x.name
        if (isFunctionReference(x) && name != null) {
            tracker.markReachable(name)
        }
    }

    private fun processLocalFunction(name: JsName, function: JsFunction) {
        for (referenced in collectReferencedNames(function)) {
            tracker.addRemovableReference(name, referenced)
        }
    }

    private fun processNonLocalFunction(function: JsFunction) {
        for (referenced in collectReferencedNames(function)) {
            tracker.markReachable(referenced)
        }
    }

    private fun isFunctionReference(nameRef: HasName?): Boolean {
        return nameRef?.name?.staticRef is JsFunction
    }

    private fun wasProcessed(function: JsFunction?): Boolean = function != null && function in processed
}

