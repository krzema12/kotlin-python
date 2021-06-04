/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.inline.clean

import org.jetbrains.kotlin.js.backend.ast.JsBlock
import org.jetbrains.kotlin.js.backend.ast.JsInvocation
import org.jetbrains.kotlin.js.backend.ast.JsNameRef
import org.jetbrains.kotlin.js.backend.ast.RecursiveJsVisitor
import org.jetbrains.kotlin.js.backend.ast.metadata.isJsCall
import org.jetbrains.kotlin.py.inline.util.isCallInvocation

// Replaces a.foo.call(a, b) with a.foo(b)
class RedundantCallElimination(private val root: JsBlock) {
    private var changed = false

    fun apply(): Boolean {
        root.accept(object : RecursiveJsVisitor() {
            override fun visitInvocation(invocation: JsInvocation) {
                tryEliminate(invocation)
                super.visitInvocation(invocation)
            }

            private fun tryEliminate(invocation: JsInvocation) {
                if (!isCallInvocation(invocation)) return

                val call = invocation.qualifier as? JsNameRef ?: return

                if (!call.isJsCall) return

                val qualifier = call.qualifier as? JsNameRef ?: return

                val receiver = qualifier.qualifier as? JsNameRef ?: return
                val firstArg = invocation.arguments.firstOrNull() as? JsNameRef ?: return

                if (receiver.qualifier == null && receiver.name != null && firstArg.qualifier == null && receiver.name == firstArg.name) {
                    invocation.arguments.removeAt(0)
                    invocation.qualifier = qualifier
                    changed = true
                }
            }
        })

        return changed
    }
}
