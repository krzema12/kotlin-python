/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.context

import org.jetbrains.kotlin.descriptors.CallableDescriptor
import org.jetbrains.kotlin.js.backend.ast.JsGlobalBlock
import org.jetbrains.kotlin.js.backend.ast.JsName

class InlineFunctionContext(val descriptor: CallableDescriptor) {
    val imports = mutableMapOf<String, JsName>()
    val importBlock = JsGlobalBlock()
    val prototypeBlock = JsGlobalBlock()
    val declarationsBlock = JsGlobalBlock()
}