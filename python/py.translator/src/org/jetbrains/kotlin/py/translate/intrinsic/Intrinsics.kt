/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.intrinsic

import org.jetbrains.kotlin.descriptors.ClassDescriptor
import org.jetbrains.kotlin.descriptors.FunctionDescriptor
import org.jetbrains.kotlin.py.translate.context.TranslationContext
import org.jetbrains.kotlin.py.translate.intrinsic.functions.FunctionIntrinsics
import org.jetbrains.kotlin.py.translate.intrinsic.functions.basic.FunctionIntrinsic
import org.jetbrains.kotlin.py.translate.intrinsic.objects.ObjectIntrinsic
import org.jetbrains.kotlin.py.translate.intrinsic.objects.ObjectIntrinsics
import org.jetbrains.kotlin.py.translate.intrinsic.operation.BinaryOperationIntrinsic
import org.jetbrains.kotlin.py.translate.intrinsic.operation.BinaryOperationIntrinsics
import org.jetbrains.kotlin.psi.KtBinaryExpression

/**
 * Provides mechanism to substitute method calls /w native constructs directly.
 */
class Intrinsics {
    private val functionIntrinsics = FunctionIntrinsics()
    private val binaryOperationIntrinsics = BinaryOperationIntrinsics()
    private val objectIntrinsics = ObjectIntrinsics()

    fun getBinaryOperationIntrinsic(expression: KtBinaryExpression, context: TranslationContext): BinaryOperationIntrinsic? {
        return binaryOperationIntrinsics.getIntrinsic(expression, context)
    }

    fun getFunctionIntrinsic(descriptor: FunctionDescriptor, context: TranslationContext): FunctionIntrinsic? {
        return functionIntrinsics.getIntrinsic(descriptor, context)
    }

    fun getObjectIntrinsic(classDescriptor: ClassDescriptor): ObjectIntrinsic? {
        return objectIntrinsics.getIntrinsic(classDescriptor)
    }
}