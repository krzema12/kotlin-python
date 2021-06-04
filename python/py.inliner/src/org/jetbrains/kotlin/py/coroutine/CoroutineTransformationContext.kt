/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.coroutine

import org.jetbrains.kotlin.js.backend.ast.JsFunction
import org.jetbrains.kotlin.js.backend.ast.JsName
import org.jetbrains.kotlin.js.backend.ast.JsScope
import org.jetbrains.kotlin.js.backend.ast.metadata.coroutineMetadata

class CoroutineTransformationContext(private val scope: JsScope, function: JsFunction) {
    private val localVariableNameCache = mutableMapOf<JsName, JsName>()
    private val usedLocalVariableIds = mutableSetOf<String>()

    val entryBlock = org.jetbrains.kotlin.py.coroutine.CoroutineBlock()
    val globalCatchBlock = org.jetbrains.kotlin.py.coroutine.CoroutineBlock()
    val metadata = function.coroutineMetadata!!
    val controllerFieldName by lazy { scope.declareName("\$controller") }
    val returnValueFieldName by lazy { scope.declareName("\$returnValue") }
    val receiverFieldName by lazy { scope.declareName("\$this") }

    fun getFieldName(variableName: JsName) = localVariableNameCache.getOrPut(variableName) {
        val baseId = "local\$${variableName.ident}"
        var suggestedId = baseId
        var suffix = 0
        while (!usedLocalVariableIds.add(suggestedId)) {
            suggestedId = "${baseId}_${suffix++}"
        }
        scope.declareName(suggestedId)
    }
}
