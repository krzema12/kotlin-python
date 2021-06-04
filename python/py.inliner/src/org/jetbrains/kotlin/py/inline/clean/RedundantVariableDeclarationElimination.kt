/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.inline.clean

import org.jetbrains.kotlin.js.backend.ast.*
import org.jetbrains.kotlin.js.backend.ast.metadata.synthetic
import org.jetbrains.kotlin.py.inline.util.collectFreeVariables

internal class RedundantVariableDeclarationElimination(private val root: JsStatement) {
    private val usages = mutableSetOf<JsName>()
    private var hasChanges = false

    fun apply(): Boolean {
        analyze()
        perform()
        return hasChanges
    }

    private fun analyze() {
        object : JsVisitorWithContextImpl() {
            override fun visit(x: JsNameRef, ctx: JsContext<*>): Boolean {
                val name = x.name
                if (name != null && x.qualifier == null) {
                    usages += name
                }
                return super.visit(x, ctx)
            }

            override fun visit(x: JsBreak, ctx: JsContext<*>) = false

            override fun visit(x: JsContinue, ctx: JsContext<*>) = false

            override fun visit(x: JsFunction, ctx: JsContext<*>): Boolean {
                usages += x.collectFreeVariables()
                return false
            }
        }.accept(root)
    }

    private fun perform() {
        object : JsVisitorWithContextImpl() {
            override fun endVisit(x: JsVars, ctx: JsContext<*>) {
                if (x.synthetic) {
                    if (x.vars.removeAll { it.initExpression == null && it.name !in usages }) {
                        hasChanges = true
                    }
                    if (x.vars.isEmpty()) {
                        ctx.removeMe()
                    }
                }
                super.endVisit(x, ctx)
            }

            override fun visit(x: JsFunction, ctx: JsContext<*>) = false
        }.accept(root)
    }
}
