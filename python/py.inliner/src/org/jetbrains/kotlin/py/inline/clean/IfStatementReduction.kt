/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.inline.clean

import org.jetbrains.kotlin.js.backend.ast.*
import org.jetbrains.kotlin.js.backend.ast.metadata.synthetic
import org.jetbrains.kotlin.py.translate.utils.JsAstUtils

class IfStatementReduction(private val root: JsStatement) {
    private var hasChanges = false

    fun apply(): Boolean {
        visitor.accept(root)

        return hasChanges
    }

    val visitor = object : JsVisitorWithContextImpl() {
        override fun visit(x: JsIf, ctx: JsContext<JsNode>): Boolean {
            val thenStatementRaw = x.thenStatement
            val elseStatementRaw = x.elseStatement
            if (x.synthetic && elseStatementRaw != null) {
                val thenStatement = extractSingleStatement(thenStatementRaw)
                val elseStatement = extractSingleStatement(elseStatementRaw)

                if (thenStatement is JsExpressionStatement && elseStatement is JsExpressionStatement) {
                    val thenAssignment = JsAstUtils.decomposeAssignment(thenStatement.expression)
                    val elseAssignment = JsAstUtils.decomposeAssignment(elseStatement.expression)
                    if (thenAssignment != null && elseAssignment != null) {
                        val (thenTarget, thenValue) = thenAssignment
                        val (elseTarget, elseValue) = elseAssignment
                        if (lhsEqual(thenTarget, elseTarget)) {
                            hasChanges = true
                            val ternary = JsConditional(x.ifExpression, thenValue, elseValue)
                            val replacement = JsExpressionStatement(JsAstUtils.assignment(thenTarget, ternary))
                            replacement.synthetic = thenStatement.synthetic && elseStatement.synthetic
                            ctx.replaceMe(replacement)
                            accept(replacement)
                            return false
                        }
                    }
                }
                else if (thenStatement is JsVars && elseStatement is JsVars) {
                    if (thenStatement.vars.size == 1 && elseStatement.vars.size == 1) {
                        val thenVar = thenStatement.vars[0]
                        val elseVar = elseStatement.vars[0]
                        val thenValue = thenVar.initExpression
                        val elseValue = elseVar.initExpression
                        if (thenVar.name == elseVar.name && thenValue != null && elseValue != null) {
                            hasChanges = true
                            val ternary = JsConditional(x.ifExpression, thenValue, elseValue)
                            val replacement = JsAstUtils.newVar(thenVar.name, ternary)
                            replacement.synthetic = thenStatement.synthetic && elseStatement.synthetic
                            ctx.replaceMe(replacement)
                            accept(replacement)
                            return false
                        }
                    }
                }
                else if (thenStatement is JsReturn && elseStatement is JsReturn) {
                    val thenValue = thenStatement.expression
                    val elseValue = elseStatement.expression
                    if (thenValue != null && elseValue != null) {
                        hasChanges = true
                        val ternary = JsConditional(x.ifExpression, thenValue, elseValue)
                        val replacement = JsReturn(ternary)
                        accept(replacement)
                        ctx.replaceMe(replacement)
                        return false
                    }
                }
            }
            return super.visit(x, ctx)
        }
    }

    private fun extractSingleStatement(statement: JsStatement): JsStatement {
        var result = statement
        while (result is JsBlock && result.statements.size == 1) {
            result = result.statements[0]
        }

        return result
    }

    private fun lhsEqual(a: JsExpression?, b: JsExpression?): Boolean = when {
        a == null && b == null -> true
        a is JsNameRef && b is JsNameRef -> a.name == b.name && lhsEqual(a.qualifier, b.qualifier)
        a is JsArrayAccess && b is JsArrayAccess -> lhsEqual(a.arrayExpression, b.arrayExpression) &&
                                                    lhsEqual(a.indexExpression, b.indexExpression)
        else -> false
    }
}