/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.inline.clean

import org.jetbrains.kotlin.js.backend.ast.*
import org.jetbrains.kotlin.py.inline.util.extractFunction

fun simplifyWrappedFunctions(root: JsNode) {
    val visitor = object : JsVisitorWithContextImpl() {
        override fun endVisit(x: JsInvocation, ctx: JsContext<in JsNode>) {
            extractFunction(x)?.let { (function, wrapper) ->
                if (wrapper != null && wrapper.statements.size == 1) {
                    ctx.replaceMe(function)
                }
            }
        }

        override fun endVisit(x: JsVars, ctx: JsContext<in JsStatement>) {
            x.vars.singleOrNull()?.let { jsVar ->
                (jsVar.initExpression as? JsFunction)?.let { function ->
                    if (function.name == null) {
                        function.name = jsVar.name
                        ctx.replaceMe(function.makeStmt())
                    }
                }
            }
        }
    }
    visitor.accept(root)
}
