/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

@file:Suppress("NON_MEMBER_FUNCTION_NO_BODY", "UNUSED_PARAMETER", "unused")

package kotlin.python

@RequiresOptIn(message = "Here be dragons! This is a compiler intrinsic, proceed with care!")
@Retention(AnnotationRetention.BINARY)
@Target(AnnotationTarget.FUNCTION)
internal annotation class JsIntrinsic

@JsIntrinsic
internal fun jsEqeq(a: Any?, b: Any?): Boolean

@JsIntrinsic
internal fun jsNotEq(a: Any?, b: Any?): Boolean

@JsIntrinsic
internal fun jsEqeqeq(a: Any?, b: Any?): Boolean

@JsIntrinsic
internal fun jsNotEqeq(a: Any?, b: Any?): Boolean

@JsIntrinsic
internal fun jsGt(a: Any?, b: Any?): Boolean

@JsIntrinsic
internal fun jsGtEq(a: Any?, b: Any?): Boolean

@JsIntrinsic
internal fun jsLt(a: Any?, b: Any?): Boolean

@JsIntrinsic
internal fun jsLtEq(a: Any?, b: Any?): Boolean

@JsIntrinsic
internal fun jsNot(a: Any?): Boolean

@JsIntrinsic
internal fun jsUnaryPlus(a: Any?): Any?

@JsIntrinsic
internal fun jsUnaryMinus(a: Any?): Any?

@JsIntrinsic
internal fun jsPrefixInc(a: Any?): Any?

@JsIntrinsic
internal fun jsPostfixInc(a: Any?): Any?

@JsIntrinsic
internal fun jsPrefixDec(a: Any?): Any?

@JsIntrinsic
internal fun jsPostfixDec(a: Any?): Any?

@JsIntrinsic
internal fun jsPlus(a: Any?, b: Any?): Any?

@JsIntrinsic
internal fun jsMinus(a: Any?, b: Any?): Any?

@JsIntrinsic
internal fun jsMult(a: Any?, b: Any?): Any?

@JsIntrinsic
internal fun jsDiv(a: Any?, b: Any?): Any?

@JsIntrinsic
internal fun jsMod(a: Any?, b: Any?): Any?

@JsIntrinsic
internal fun jsPlusAssign(a: Any?, b: Any?): Any?

@JsIntrinsic
internal fun jsMinusAssign(a: Any?, b: Any?): Any?

@JsIntrinsic
internal fun jsMultAssign(a: Any?, b: Any?): Any?

@JsIntrinsic
internal fun jsDivAssign(a: Any?, b: Any?): Any?

@JsIntrinsic
internal fun jsModAssign(a: Any?, b: Any?): Any?

@JsIntrinsic
internal fun jsAnd(a: Any?, b: Any?): Any?

@JsIntrinsic
internal fun jsOr(a: Any?, b: Any?): Any?

@JsIntrinsic
internal fun jsBitAnd(a: Any?, b: Any?): Int

@JsIntrinsic
internal fun jsBitOr(a: Any?, b: Any?): Int

@JsIntrinsic
internal fun jsBitXor(a: Any?, b: Any?): Int

@JsIntrinsic
internal fun jsBitNot(a: Any?): Int

@JsIntrinsic
internal fun jsBitShiftR(a: Any?, b: Any?): Int

@JsIntrinsic
internal fun jsBitShiftRU(a: Any?, b: Any?): Int

@JsIntrinsic
internal fun jsBitShiftL(a: Any?, b: Any?): Int

@JsIntrinsic
internal fun jsInstanceOfIntrinsic(a: Any?, b: Any?): Boolean

@JsIntrinsic
internal fun jsNewTarget(a: Any?): Any?

@JsIntrinsic
internal fun emptyObject(a: Any?): Any?

@JsIntrinsic
internal fun openInitializerBox(a: Any?, b: Any?): Any?

@JsIntrinsic
internal fun jsArrayLength(a: Any?): Any?

@JsIntrinsic
internal fun jsArrayGet(a: Any?, b: Any?): Any?

@JsIntrinsic
internal fun jsArraySet(a: Any?, b: Any?, c: Any?): Any?

@JsIntrinsic
internal fun arrayLiteral(a: Any?): Any?

@JsIntrinsic
internal fun int8Array(a: Any?): Any?

@JsIntrinsic
internal fun int16Array(a: Any?): Any?

@JsIntrinsic
internal fun int32Array(a: Any?): Any?

@JsIntrinsic
internal fun float32Array(a: Any?): Any?

@JsIntrinsic
internal fun float64Array(a: Any?): Any?

@JsIntrinsic
internal fun int8ArrayOf(a: Any?): Any?

@JsIntrinsic
internal fun int16ArrayOf(a: Any?): Any?

@JsIntrinsic
internal fun int32ArrayOf(a: Any?): Any?

@JsIntrinsic
internal fun float32ArrayOf(a: Any?): Any?

@JsIntrinsic
internal fun float64ArrayOf(a: Any?): Any?

@JsIntrinsic
internal fun <T> objectCreate(): T

@JsIntrinsic
internal fun <T> sharedBoxCreate(v: T?): dynamic

@JsIntrinsic
internal fun <T> sharedBoxRead(box: dynamic): T?

@JsIntrinsic
internal fun <T> sharedBoxWrite(box: dynamic, nv: T?)

@JsIntrinsic
internal fun jsUndefined(): Nothing?

@JsIntrinsic
internal fun <T> DefaultType(): T

@JsIntrinsic
internal fun jsBind(receiver: Any?, target: Any?): Any?

@JsIntrinsic
internal fun <A> slice(a: A): A

@JsIntrinsic
internal fun unreachable(): Nothing

@JsIntrinsic
internal fun jsInIntrinsic(lhs: Any?, rhs: Any): Boolean

@JsIntrinsic
internal fun jsDelete(e: Any?)

@JsIntrinsic
internal fun jsTypeOf(value_hack: Any?): String

@JsIntrinsic
internal fun jsDeleteProperty(obj_hack: Any, property_hack: Any)

@JsIntrinsic
internal fun jsBitwiseOr(lhs_hack: Any?, rhs_hack: Any?): Int

@JsIntrinsic
internal fun jsBitwiseAnd(lhs_hack: Any?, rhs_hack: Any?): Int

@JsIntrinsic
internal fun jsInstanceOf(obj_hack: Any?, jsClass_hack: Any?): Boolean

@JsIntrinsic
internal fun jsIn(lhs_hack: Any?, rhs_hack: Any): Boolean

@JsIntrinsic
internal fun numberToByte(a: dynamic): Byte

@JsIntrinsic
internal fun numberToDouble(@Suppress("UNUSED_PARAMETER") a: dynamic): Double

@JsIntrinsic
internal fun numberToInt(a: dynamic): Int

@JsIntrinsic
internal fun numberToShort(a: dynamic): Short

@JsIntrinsic
internal fun toByte(@Suppress("UNUSED_PARAMETER") a: dynamic): Byte

@JsIntrinsic
internal fun toShort(@Suppress("UNUSED_PARAMETER") a: dynamic): Short

@JsIntrinsic
internal fun numberToLong(a: dynamic): Long

@JsIntrinsic
internal fun toLong(a: dynamic): Long

@JsIntrinsic
internal fun doubleToInt(a: Double): Int

@JsIntrinsic
internal fun numberToChar(a: dynamic)

@JsIntrinsic
internal fun isInterface(obj: dynamic, iface: dynamic): Boolean

@JsIntrinsic
internal fun isArray(): Boolean

@JsIntrinsic
internal fun isObject(): Boolean

@JsIntrinsic
internal fun isSuspendFunction(): Boolean

@JsIntrinsic
internal fun isNumber(): Boolean

@JsIntrinsic
internal fun isComparable(): Boolean

@JsIntrinsic
internal fun isCharSequence(): Boolean

@JsIntrinsic
internal fun isBooleanArray(): Boolean

@JsIntrinsic
internal fun isByteArray(): Boolean

@JsIntrinsic
internal fun isShortArray(): Boolean

@JsIntrinsic
internal fun isCharArray(): Boolean

@JsIntrinsic
internal fun isIntArray(): Boolean

@JsIntrinsic
internal fun isFloatArray(): Boolean

@JsIntrinsic
internal fun isLongArray(): Boolean

@JsIntrinsic
internal fun isDoubleArray(): Boolean

@JsIntrinsic
internal fun enumValueOfIntrinsic(): Boolean

@JsIntrinsic
internal fun enumValuesIntrinsic(): Boolean

@JsIntrinsic
internal fun js(): Boolean

@JsIntrinsic
internal fun hashCode(): Boolean

@JsIntrinsic
internal fun getNumberHashCode(): Boolean

@JsIntrinsic
internal fun getObjectHashCode(): Boolean

@JsIntrinsic
internal fun getStringHashCode(): Boolean

@JsIntrinsic
internal fun toString(): Boolean

@JsIntrinsic
internal fun anyToString(): Boolean

@JsIntrinsic
internal fun compareTo(): Boolean

@JsIntrinsic
internal fun equals(): Boolean

@JsIntrinsic
internal fun construct(): Boolean
