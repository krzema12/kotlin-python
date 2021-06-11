/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.inline.util.rewriters

import org.jetbrains.kotlin.js.backend.ast.*
import org.jetbrains.kotlin.js.backend.ast.metadata.*
import org.jetbrains.kotlin.py.coroutine.isStateMachineResult
import org.jetbrains.kotlin.py.translate.context.Namer
import org.jetbrains.kotlin.py.translate.utils.JsAstUtils

class ReturnReplacingVisitor(
        private val resultRef: JsNameRef?,
        private val breakLabel: JsNameRef?,
        private val function: JsFunction,
        private val isSuspend: Boolean
) : JsVisitorWithContextImpl() {

    /**
     * Prevents replacing returns in object literal
     */
    override fun visit(x: JsObjectLiteral, ctx: JsContext<JsNode>): Boolean = false

    /**
     * Prevents replacing returns in inner function
     */
    override fun visit(x: JsFunction, ctx: JsContext<JsNode>): Boolean = false

    override fun endVisit(x: JsReturn, ctx: JsContext<JsNode>) {
        if (x.returnTarget != null && function.functionDescriptor != x.returnTarget) return

        ctx.removeMe()

        val returnReplacement = getReturnReplacement(x.expression)
        if (returnReplacement != null) {
            if (returnReplacement.source == null) {
                returnReplacement.source = x.source
            }
            ctx.addNext(JsExpressionStatement(returnReplacement))
        }

        if (breakLabel != null) {
            ctx.addNext(JsBreak(breakLabel).apply { source = x.source })
        }
    }

    private fun getReturnReplacement(returnExpression: JsExpression?): JsExpression? {
        return if (returnExpression != null) {
            val assignment = resultRef?.let { lhs ->
                val rhs = processCoroutineResult(returnExpression)!!
                JsAstUtils.assignment(lhs, rhs).apply { synthetic = true }
            }
            assignment ?: processCoroutineResult(returnExpression)
        }
        else {
            processCoroutineResult(null)
        }
    }

    private fun processCoroutineResult(expression: JsExpression?): JsExpression? {
        if (!isSuspend || expression.isStateMachineResult()) return expression
        val lhs = JsNameRef("\$\$coroutineResult\$\$", JsAstUtils.stateMachineReceiver()).apply { coroutineResult = true }
        return JsAstUtils.assignment(lhs, expression ?: Namer.getUndefinedExpression())
    }
}