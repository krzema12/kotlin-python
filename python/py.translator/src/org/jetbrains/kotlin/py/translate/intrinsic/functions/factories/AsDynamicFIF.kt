/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.intrinsic.functions.factories

import org.jetbrains.kotlin.js.backend.ast.JsExpression
import org.jetbrains.kotlin.js.patterns.PatternBuilder
import org.jetbrains.kotlin.py.translate.callTranslator.CallInfo
import org.jetbrains.kotlin.py.translate.context.TranslationContext
import org.jetbrains.kotlin.py.translate.intrinsic.functions.basic.FunctionIntrinsic
import org.jetbrains.kotlin.py.translate.utils.TranslationUtils

object AsDynamicFIF : CompositeFIF() {
    init {
        add(PatternBuilder.pattern("kotlin.js.asDynamic()"), object : FunctionIntrinsic() {
            override fun apply(callInfo: CallInfo, arguments: List<JsExpression>, context: TranslationContext): JsExpression =
                    TranslationUtils.coerce(context, callInfo.extensionReceiver!!, callInfo.resolvedCall.extensionReceiver!!.type)
        })
    }
}
