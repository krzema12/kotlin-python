/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.intrinsic.functions.factories

import org.jetbrains.kotlin.descriptors.ClassDescriptor
import org.jetbrains.kotlin.descriptors.FunctionDescriptor
import org.jetbrains.kotlin.descriptors.PropertyDescriptor
import org.jetbrains.kotlin.descriptors.PropertyGetterDescriptor
import org.jetbrains.kotlin.js.backend.ast.JsExpression
import org.jetbrains.kotlin.js.backend.ast.JsNameRef
import org.jetbrains.kotlin.py.translate.callTranslator.CallInfo
import org.jetbrains.kotlin.py.translate.context.TranslationContext
import org.jetbrains.kotlin.py.translate.intrinsic.functions.basic.FunctionIntrinsic
import org.jetbrains.kotlin.py.translate.utils.JsAstUtils
import org.jetbrains.kotlin.resolve.scopes.DescriptorKindFilter
import org.jetbrains.kotlin.resolve.scopes.receivers.SuperCallReceiverValue
import org.jetbrains.kotlin.types.typeUtil.isNotNullThrowable

object ExceptionPropertyIntrinsicFactory : FunctionIntrinsicFactory {
    override fun getIntrinsic(descriptor: FunctionDescriptor, context: TranslationContext): FunctionIntrinsic? {
        if (descriptor !is PropertyGetterDescriptor) return null
        val classDescriptor = descriptor.correspondingProperty.containingDeclaration as? ClassDescriptor ?: return null
        if (!classDescriptor.defaultType.isNotNullThrowable()) return null

        return Intrinsic
    }

    object Intrinsic : FunctionIntrinsic() {
        override fun apply(callInfo: CallInfo, arguments: List<JsExpression>, context: TranslationContext): JsExpression {
            val property = callInfo.resolvedCall.resultingDescriptor as PropertyDescriptor
            if (callInfo.resolvedCall.call.explicitReceiver !is SuperCallReceiverValue) {
                val name = context.getNameForDescriptor(property)
                return JsNameRef(name, callInfo.dispatchReceiver!!)
            }

            val currentClassProperty = context.classDescriptor!!.unsubstitutedMemberScope
                    .getContributedDescriptors(DescriptorKindFilter.CALLABLES)
                    .filterIsInstance<PropertyDescriptor>()
                    .first { it.overriddenDescriptors.any { it == property } }
            return JsAstUtils.pureFqn(context.getNameForBackingField(currentClassProperty), callInfo.dispatchReceiver!!)
        }
    }
}