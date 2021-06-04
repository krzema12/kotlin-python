/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.intrinsic.functions.basic

import org.jetbrains.kotlin.js.backend.ast.JsExpression
import org.jetbrains.kotlin.py.translate.callTranslator.CallInfo
import org.jetbrains.kotlin.py.translate.context.TranslationContext

/**
 * Base for intrinsics that substitute standard function calls like Int#plus, Float#minus ... etc
 */
abstract class FunctionIntrinsic {
    abstract fun apply(callInfo: CallInfo, arguments: List<JsExpression>, context: TranslationContext): JsExpression
}
