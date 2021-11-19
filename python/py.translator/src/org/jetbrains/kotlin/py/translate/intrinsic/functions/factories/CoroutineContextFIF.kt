/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.intrinsic.functions.factories

import org.jetbrains.kotlin.descriptors.ClassDescriptor
import org.jetbrains.kotlin.descriptors.FunctionDescriptor
import org.jetbrains.kotlin.js.backend.ast.JsExpression
import org.jetbrains.kotlin.js.backend.ast.JsNameRef
import org.jetbrains.kotlin.js.backend.ast.metadata.isInline
import org.jetbrains.kotlin.js.descriptorUtils.isCoroutineLambda
import org.jetbrains.kotlin.name.Name
import org.jetbrains.kotlin.py.translate.callTranslator.CallInfo
import org.jetbrains.kotlin.py.translate.context.TranslationContext
import org.jetbrains.kotlin.py.translate.intrinsic.functions.basic.FunctionIntrinsic
import org.jetbrains.kotlin.py.translate.utils.JsAstUtils
import org.jetbrains.kotlin.py.translate.utils.TranslationUtils
import org.jetbrains.kotlin.resolve.DescriptorUtils
import org.jetbrains.kotlin.resolve.calls.checkers.isBuiltInCoroutineContext

object CoroutineContextFIF : FunctionIntrinsicFactory {
    override fun getIntrinsic(descriptor: FunctionDescriptor, context: TranslationContext): FunctionIntrinsic? {
        if (!descriptor.isBuiltInCoroutineContext()) return null
        return Intrinsic
    }

    object Intrinsic : FunctionIntrinsic() {
        override fun apply(callInfo: CallInfo, arguments: List<JsExpression>, context: TranslationContext): JsExpression {
            val continuation = TranslationUtils.getEnclosingContinuationParameter(context)
            val continuationDescriptor = continuation.type.constructor.declarationDescriptor as? ClassDescriptor ?: error("Continuation is not a class")
            val contContext = DescriptorUtils.getPropertyByName(continuationDescriptor.unsubstitutedMemberScope, Name.identifier("context"))
            val res = JsNameRef(
                context.getNameForDescriptor(contContext),
                if (context.declarationDescriptor?.isCoroutineLambda == true) JsAstUtils.stateMachineReceiver()
                else TranslationUtils.translateContinuationArgument(context)
            )
            res.isInline = false
            return res
        }
    }
}
