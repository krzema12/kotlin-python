/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.inline.util

import org.jetbrains.kotlin.js.backend.ast.*

fun JsNode.fixForwardNameReferences() {
    accept(object : RecursiveJsVisitor() {
        val currentScope = mutableMapOf<String, JsName>()

        init {
            currentScope += collectDefinedNames(this@fixForwardNameReferences, skipLabelsAndCatches = true).associateBy { it.ident }
        }

        private fun restore(ident: String, oldName: JsName?) {
            if (oldName == null) {
                currentScope -= ident
            } else {
                currentScope[ident] = oldName
            }
        }

        override fun visitFunction(x: JsFunction) {
            val localVars = x.collectLocalVariables(skipLabelsAndCatches = true).toList()
            val backup = arrayOfNulls<JsName>(localVars.size)

            localVars.forEachIndexed { index, localVar ->
                backup[index] = currentScope[localVar.ident]
                currentScope[localVar.ident] = localVar
            }

            super.visitFunction(x)

            for (index in localVars.indices.reversed()) {
                restore(localVars[index].ident, backup[index])
            }
        }

        override fun visitCatch(x: JsCatch) {
            val name = x.parameter.name
            val oldName = currentScope[name.ident]
            currentScope[name.ident] = name

            super.visitCatch(x)

            restore(name.ident, oldName)
        }

        override fun visitNameRef(nameRef: JsNameRef) {
            super.visitNameRef(nameRef)
            if (nameRef.qualifier == null) {
                val ident = nameRef.ident
                val name = currentScope[ident]
                if (name != null) {
                    nameRef.name = name
                }
            }
        }

        override fun visitBreak(x: JsBreak) {}

        override fun visitContinue(x: JsContinue) {}
    })
}