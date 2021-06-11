/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.inline.clean

import org.jetbrains.kotlin.js.backend.ast.*
import org.jetbrains.kotlin.py.coroutine.finallyPath
import org.jetbrains.kotlin.py.coroutine.targetBlock
import org.jetbrains.kotlin.py.coroutine.targetExceptionBlock

class CoroutineStateElimination(private val body: JsBlock) {
    fun apply(): Boolean {
        var changed = false

        body.accept(object : RecursiveJsVisitor() {
            override fun visitBlock(x: JsBlock) {
                visitStatements(x.statements)
                super.visitBlock(x)
            }

            override fun visitCase(x: JsCase) {
                visitStatements(x.statements)
                super.visitCase(x)
            }

            private fun visitStatements(statements: MutableList<JsStatement>) {
                class IndexHolder {
                    var value: Int? = null
                }

                val indexesToRemove = mutableSetOf<Int>()
                val lastTargetBlockIndex = IndexHolder()
                val lastTargetExceptionBlockIndex = IndexHolder()
                val lastFinallyPathIndex = IndexHolder()

                for ((index, statement) in statements.withIndex()) {
                    val indexesToUpdate = mutableListOf<IndexHolder>()
                    if (statement is JsExpressionStatement) {
                        if (statement.targetBlock) {
                            indexesToUpdate += lastTargetBlockIndex
                        }
                        if (statement.targetExceptionBlock) {
                            indexesToUpdate += lastTargetExceptionBlockIndex
                        }
                        if (statement.finallyPath) {
                            indexesToUpdate += lastFinallyPathIndex
                        }
                    }

                    if (indexesToUpdate.isNotEmpty()) {
                        for (indexToUpdate in indexesToUpdate) {
                            indexToUpdate.value?.let { indexesToRemove += it }
                            indexToUpdate.value = index
                        }
                    }
                    else {
                        lastTargetBlockIndex.value = null
                        lastTargetExceptionBlockIndex.value = null
                        lastFinallyPathIndex.value = null
                    }
                }

                for (index in indexesToRemove.sorted().reversed()) {
                    statements.removeAt(index)
                }
                if (indexesToRemove.isNotEmpty()) {
                    changed = true
                }
            }
        })

        return changed
    }
}