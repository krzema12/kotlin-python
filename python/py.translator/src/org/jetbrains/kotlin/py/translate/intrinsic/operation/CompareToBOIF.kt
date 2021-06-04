/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.intrinsic.operation

import org.jetbrains.kotlin.builtins.KotlinBuiltIns
import org.jetbrains.kotlin.builtins.KotlinBuiltIns.isPrimitiveTypeOrNullablePrimitiveType
import org.jetbrains.kotlin.descriptors.FunctionDescriptor
import org.jetbrains.kotlin.js.backend.ast.JsIntLiteral
import org.jetbrains.kotlin.js.patterns.PatternBuilder.pattern
import org.jetbrains.kotlin.py.translate.utils.JsAstUtils.*
import org.jetbrains.kotlin.lexer.KtSingleValueToken
import org.jetbrains.kotlin.resolve.calls.tasks.isDynamic
import org.jetbrains.kotlin.types.KotlinType
import org.jetbrains.kotlin.types.expressions.OperatorConventions
import org.jetbrains.kotlin.utils.identity

object CompareToBOIF : BinaryOperationIntrinsicFactory {
    override fun getSupportTokens(): Set<KtSingleValueToken> = OperatorConventions.COMPARISON_OPERATIONS

    private val patterns = listOf(
        pattern("Int|Short|Byte|Float|Double.compareTo(Long)") to binaryIntrinsic(toRight = { r, _ -> longToNumber(r) }),
        pattern("Long.compareTo(Int|Short|Byte|Float|Double)") to binaryIntrinsic(toLeft = { l, _ -> longToNumber(l) }),
        // L.compareTo(R) OP 0
        pattern("Long.compareTo(Long)") to complexBinaryIntrinsic({ l, r, _ -> compareForObject(l, r) }, { _, _, _-> JsIntLiteral(0) })
    )

    override fun getIntrinsic(descriptor: FunctionDescriptor, leftType: KotlinType?, rightType: KotlinType?): BinaryOperationIntrinsic? {
        if (descriptor.isDynamic()) return binaryIntrinsic()

        if (leftType == null || rightType == null || !KotlinBuiltIns.isBuiltIn(descriptor)) return null

        patterns.forEach { (p, i) -> if (p.test(descriptor)) return i }

        // Types may be nullable if properIeeeComparisons are switched off, e.g. fun foo(a: Double?) = a != null && a < 0.0
        return if (isPrimitiveTypeOrNullablePrimitiveType(leftType) && isPrimitiveTypeOrNullablePrimitiveType(rightType)) {
            binaryIntrinsic(coerceTo(leftType), coerceTo(rightType))
        } else {
            // Kotlin.compareTo(L, R) OP 0
            complexBinaryIntrinsic({ l, r, _ -> compareTo(l, r) }, { _, _, _ -> JsIntLiteral(0) })
        }
    }
}
