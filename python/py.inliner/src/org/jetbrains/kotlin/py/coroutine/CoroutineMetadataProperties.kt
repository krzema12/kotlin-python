/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.coroutine

import org.jetbrains.kotlin.js.backend.ast.JsDebugger
import org.jetbrains.kotlin.js.backend.ast.JsExpressionStatement
import org.jetbrains.kotlin.js.backend.ast.metadata.MetadataProperty

var JsDebugger.targetBlock: org.jetbrains.kotlin.py.coroutine.CoroutineBlock? by MetadataProperty(default = null)
var JsDebugger.targetExceptionBlock: org.jetbrains.kotlin.py.coroutine.CoroutineBlock? by MetadataProperty(default = null)
var JsDebugger.finallyPath: List<org.jetbrains.kotlin.py.coroutine.CoroutineBlock>? by MetadataProperty(default = null)

var JsExpressionStatement.targetBlock by MetadataProperty(default = false)
var JsExpressionStatement.targetExceptionBlock by MetadataProperty(default = false)
var JsExpressionStatement.finallyPath by MetadataProperty(default = false)
