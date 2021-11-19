/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.intrinsic.functions

import org.jetbrains.kotlin.descriptors.FunctionDescriptor
import org.jetbrains.kotlin.py.translate.context.TranslationContext
import org.jetbrains.kotlin.py.translate.intrinsic.functions.basic.FunctionIntrinsic
import org.jetbrains.kotlin.py.translate.intrinsic.functions.factories.*

class FunctionIntrinsics {

    private val intrinsicCache = mutableMapOf<FunctionDescriptor, FunctionIntrinsic?>()

    private val factories = listOf(
        LongOperationFIF,
        PrimitiveUnaryOperationFIF.INSTANCE,
        StringPlusCharFIF,
        PrimitiveBinaryOperationFIF.INSTANCE,
        ArrayFIF,
        TopLevelFIF.INSTANCE,
        NumberAndCharConversionFIF,
        ThrowableConstructorIntrinsicFactory,
        ExceptionPropertyIntrinsicFactory,
        AsDynamicFIF,
        CoroutineContextFIF,
        SuspendCoroutineUninterceptedOrReturnFIF,
        TypeOfFIF
    )

    fun getIntrinsic(descriptor: FunctionDescriptor, context: TranslationContext): FunctionIntrinsic? {
        if (descriptor in intrinsicCache) return intrinsicCache[descriptor]

        return factories.firstNotNullOfOrNull { it.getIntrinsic(descriptor, context) }.also {
            intrinsicCache[descriptor] = it
        }
    }
}
