/*
 * Copyright 2010-2018 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.ir.backend.py.transformers.irToPy

import generated.Python.*
import org.jetbrains.kotlin.ir.backend.py.PyIrBackendContext
import org.jetbrains.kotlin.ir.backend.py.utils.Namer
import org.jetbrains.kotlin.ir.backend.py.utils.PyGenerationContext
import org.jetbrains.kotlin.ir.declarations.IrClass
import org.jetbrains.kotlin.ir.declarations.IrDeclarationWithName
import org.jetbrains.kotlin.ir.declarations.IrSimpleFunction
import org.jetbrains.kotlin.ir.expressions.IrCall
import org.jetbrains.kotlin.ir.symbols.IrClassifierSymbol
import org.jetbrains.kotlin.ir.symbols.IrSimpleFunctionSymbol
import org.jetbrains.kotlin.ir.symbols.IrSymbol
import org.jetbrains.kotlin.ir.types.*
import org.jetbrains.kotlin.ir.util.isEffectivelyExternal

typealias IrCallTransformer = (IrCall, context: PyGenerationContext) -> expr

class PyIntrinsicTransformers(backendContext: PyIrBackendContext) {
    private val transformers: Map<IrSymbol, IrCallTransformer>
    val icUtils = backendContext.inlineClassesUtils

    init {
        val intrinsics = backendContext.intrinsics

        transformers = mutableMapOf()

        transformers.apply {
            compareOp(intrinsics.jsEqeqeq, Is)
            compareOp(intrinsics.jsNotEqeq, IsNot)
            compareOp(intrinsics.jsEqeq, Eq)
            compareOp(intrinsics.jsNotEq, NotEq)

            compareOp(intrinsics.jsGt, Gt)
            compareOp(intrinsics.jsGtEq, GtE)
            compareOp(intrinsics.jsLt, Lt)
            compareOp(intrinsics.jsLtEq, LtE)

            unaryOp(intrinsics.jsNot, Not)

            unaryOp(intrinsics.jsUnaryPlus, UAdd)
            unaryOp(intrinsics.jsUnaryMinus, USub)

            binOp(intrinsics.jsPlus, Add)
            binOp(intrinsics.jsMinus, Sub)
            binOp(intrinsics.jsMult, Mult)
            binOp(intrinsics.jsDiv, Div)  // todo: need to switch to FloorDiv in some cases
            binOp(intrinsics.jsMod, Mod)  // todo: ensure that Python's Mod gives the same results as Kotlin's

            binOp(intrinsics.jsBitAnd, BitAnd)
            binOp(intrinsics.jsBitOr, BitOr)
            binOp(intrinsics.jsBitXor, BitXor)
            unaryOp(intrinsics.jsBitNot, Invert)

            binOp(intrinsics.jsBitShiftR, RShift)

            fun simulateOverflow(expr: expr, overSigned: String, maxUnsigned: String): expr = BinOp(
                left = BinOp(
                    left = BinOp(
                        left = expr,
                        op = Add,
                        right = Constant(constant(overSigned), null),
                    ),
                    op = BitAnd,
                    right = Constant(constant(maxUnsigned), null),
                ),
                op = Sub,
                right = Constant(constant(overSigned), null),
            )

            fun String.hex() = "0x${this.reversed().chunked(4).joinToString("_").reversed()}"

            fun overSignedMaxUnsigned(type: IrType): Pair<String, String> = when {
                type.isLong() -> Long.MAX_VALUE.toULong().plus(1u).toString(16).hex() to ULong.MAX_VALUE.toString(16).hex()
                type.isInt() -> Int.MAX_VALUE.toUInt().plus(1u).toString(16).hex() to UInt.MAX_VALUE.toString(16).hex()
                type.isShort() -> Short.MAX_VALUE.toUShort().plus(1u).toString(16).hex() to UShort.MAX_VALUE.toString(16).hex()
                type.isByte() -> Byte.MAX_VALUE.toUByte().plus(1u).toString(16).hex() to UByte.MAX_VALUE.toString(16).hex()
                else -> throw IllegalArgumentException("Not an integer: $type")
            }

            fun simulateUshr(maxUnsigned: String): (expr, expr) -> expr = { left, right ->
                // compile `val >>> n` as `(val && MAX_UNSIGNED) >> n`
                BinOp(
                    left = BinOp(
                        left = left,
                        op = BitAnd,
                        right = Constant(constant(maxUnsigned), null),
                    ),
                    op = RShift,
                    right = right,
                )
            }

            add(intrinsics.jsBitShiftRU) { call, context ->
                val (_, maxUnsigned) = overSignedMaxUnsigned(call.symbol.owner.returnType)
                val (left, right) = translateCallArguments(call, context)
                simulateUshr(maxUnsigned)(left, right)
            }
            add(intrinsics.jsBitShiftL) { call, context ->
                // compile `val << n` as `(val << n).simulateOverflow()`
                val (overSigned, maxUnsigned) = overSignedMaxUnsigned(call.symbol.owner.returnType)
                val (left, right) = translateCallArguments(call, context)
                simulateOverflow(BinOp(left = left, op = LShift, right = right), overSigned = overSigned, maxUnsigned = maxUnsigned)
            }

            // Simulation of overflow for integer numbers:
            // (number).__add__(HALF_UNSIGNED).__and__(MAX_UNSIGNED).__sub__(HALF_UNSIGNED): From Hacker's Delight (Sign Extension)
            // Example:
            // Overflow of a Byte:
            // (128).__add__(0x80).__and__(0xFF).__sub__(0x80) => -128
            listOf(
                intrinsics.jsNumberToLong,
                intrinsics.jsNumberToInt,
                intrinsics.jsNumberToShort,
                intrinsics.jsNumberToByte,
            ).forEach { f ->
                val (overSigned, maxUnsigned) = overSignedMaxUnsigned(f.owner.returnType)
                add(f) { call, context ->
                    val arg = translateCallArguments(call, context).single()
                    simulateOverflow(arg, overSigned = overSigned, maxUnsigned = maxUnsigned)
                }
            }

            // don't do anything when converting a small type to a bigger or equal one
            listOf(
                intrinsics.byteToByte,
                intrinsics.byteToShort,
                intrinsics.byteToInt,
                intrinsics.byteToLong,
                intrinsics.shortToShort,
                intrinsics.shortToInt,
                intrinsics.shortToLong,
                intrinsics.intToInt,
                intrinsics.intToLong,
                intrinsics.longToLong,
            ).forEach { f ->
                add(f) { call, context -> IrElementToPyExpressionTransformer().visitExpression(call.dispatchReceiver!!, context) }
            }

            // drop bits when converting a big type to a smaller one
            listOf(
                intrinsics.shortToByte,
                intrinsics.intToByte,
                intrinsics.intToShort,
                intrinsics.longToByte,
                intrinsics.longToShort,
                intrinsics.longToInt,
            ).forEach { f ->
                val (overSigned, maxUnsigned) = overSignedMaxUnsigned(f.owner.returnType)
                add(f) { call, context ->
                    val arg = IrElementToPyExpressionTransformer().visitExpression(call.dispatchReceiver!!, context)
                    simulateOverflow(arg, overSigned = overSigned, maxUnsigned = maxUnsigned)
                }
            }

            fun replaceLongMethodWithOperator(method: IrSimpleFunctionSymbol, op: (expr, expr) -> expr) {
                val returnType = method.owner.returnType
                if (!returnType.isByte() && !returnType.isShort() && !returnType.isInt() && !returnType.isLong()) {
                    return  // unsupported method
                }

                val (overSigned, maxUnsigned) = overSignedMaxUnsigned(method.owner.returnType)
                add(method) { call, context ->
                    val left = IrElementToPyExpressionTransformer().visitExpression(call.dispatchReceiver!!, context)
                    val right = translateCallArguments(call, context).single()
                    val binOp = op(left, right)
                    simulateOverflow(binOp, overSigned = overSigned, maxUnsigned = maxUnsigned)
                }
            }

            fun binOp(op: operator): (expr, expr) -> expr = { left, right -> BinOp(left = left, op = op, right = right) }
            fun cmpOp(op: cmpop): (expr, expr) -> expr = { left, right ->
                Compare(left = left, ops = listOf(op), comparators = listOf(right))
            }

            intrinsics.longPlus.forEach { replaceLongMethodWithOperator(it, binOp(Add)) }
            intrinsics.longMinus.forEach { replaceLongMethodWithOperator(it, binOp(Sub)) }
            intrinsics.longMult.forEach { replaceLongMethodWithOperator(it, binOp(Mult)) }
            intrinsics.longDiv.forEach { replaceLongMethodWithOperator(it, binOp(FloorDiv)) }
            intrinsics.longMod.forEach { replaceLongMethodWithOperator(it, binOp(Mod)) }
            intrinsics.longAnd.forEach { replaceLongMethodWithOperator(it, binOp(BitAnd)) }
            intrinsics.longOr.forEach { replaceLongMethodWithOperator(it, binOp(BitOr)) }
            intrinsics.longXor.forEach { replaceLongMethodWithOperator(it, binOp(BitXor)) }
            add(intrinsics.longInv) { call, context ->
                val arg = IrElementToPyExpressionTransformer().visitExpression(call.dispatchReceiver!!, context)
                UnaryOp(Invert, arg)
            }
            intrinsics.longShl.forEach { replaceLongMethodWithOperator(it, binOp(LShift)) }
            intrinsics.longShr.forEach { replaceLongMethodWithOperator(it, binOp(RShift)) }
            intrinsics.longUshr.forEach { replaceLongMethodWithOperator(it, simulateUshr(ULong.MAX_VALUE.toString(16).hex())) }
            intrinsics.longEquals.forEach { replaceLongMethodWithOperator(it, cmpOp(Eq)) }

            add(intrinsics.jsInstanceOf) { call, context ->
                val args = translateCallArguments(call, context)
                Call(
                    func = Name(identifier("isinstance"), Load),
                    args = args,
                    keywords = emptyList(),
                )
            }

            add(intrinsics.jsObjectCreate) { call, context ->
                val classToCreate = call.getTypeArgument(0)!!.classifierOrFail.owner as IrClass
                val className = context.getNameForClass(classToCreate).ident.toValidPythonSymbol()
                val pythonName = Name(identifier(className), Load)

                Call(
                    func = Attribute(pythonName, identifier("__new__"), Load),
                    args = listOf(pythonName),
                    keywords = emptyList(),
                )
            }

            add(intrinsics.jsClass) { call, context ->
                val classifier: IrClassifierSymbol = call.getTypeArgument(0)!!.classifierOrFail
                val owner = classifier.owner

                when {
                    owner is IrClass && owner.isEffectivelyExternal() ->
                        Name(identifier(context.getRefForExternalClass(owner).ident), Load)

                    else ->
                        Name(identifier(context.getNameForStaticDeclaration(owner as IrDeclarationWithName).makeRef().ident), Load)
                }
            }

            add(intrinsics.jsArrayLength) { call, context ->
                val args = translateCallArguments(call, context)

                Call(
                    func = Name(identifier("len"), Load),
                    args = args,
                    keywords = emptyList(),
                )
            }

            add(intrinsics.jsArrayGet) { call, context ->
                val args = translateCallArguments(call, context)
                val array = args[0]
                val index = args[1]
                Subscript(value = array, slice = index, ctx = Load)
            }

            add(intrinsics.jsArraySet) { call, context ->
                val args = translateCallArguments(call, context)
                val array = args[0]
                val index = args[1]
                val value = args[2]
                // todo: this is a statement but an expression is required, so using __setitem__ call below for now
                Call(
                    func = Attribute(
                        value = array,
                        attr = identifier("__setitem__"),
                        ctx = Load,
                    ),
                    args = listOf(index, value),
                    keywords = emptyList(),
                )
            }

            add(intrinsics.createSharedBox) { call, context: PyGenerationContext ->
                val arg = translateCallArguments(call, context).single()
                Dict(
                    keys = listOf(Constant(constant(Namer.SHARED_BOX_V), null)),
                    values = listOf(arg),
                )
            }

            add(intrinsics.readSharedBox) { call, context: PyGenerationContext ->
                val box = translateCallArguments(call, context).single()

                Subscript(
                    value = box,
                    slice = Constant(constant(Namer.SHARED_BOX_V), null),
                    ctx = Load,
                )
            }

            add(intrinsics.writeSharedBox) { call, context: PyGenerationContext ->
                val args = translateCallArguments(call, context)
                val box = args[0]
                val value = args[1]

                // todo: this is a statement but an expression is required, so using __setitem__ call below for now
                Call(
                    func = Attribute(
                        value = box,
                        attr = identifier("__setitem__"),
                        ctx = Load,
                    ),
                    args = listOf(Constant(constant(Namer.SHARED_BOX_V), null), value),
                    keywords = emptyList(),
                )
            }
            add(intrinsics.jsUndefined) { _, _ ->
                Name(identifier("None"), Load)
            }
        }
    }

    operator fun get(symbol: IrSymbol): IrCallTransformer? = transformers[symbol]
}

private fun translateCallArguments(expression: IrCall, context: PyGenerationContext): List<expr> {
    return translateCallArguments(expression, context, IrElementToPyExpressionTransformer())
}

private fun MutableMap<IrSymbol, IrCallTransformer>.add(functionSymbol: IrSymbol, t: IrCallTransformer) {
    put(functionSymbol, t)
}

private fun MutableMap<IrSymbol, IrCallTransformer>.add(function: IrSimpleFunction, t: IrCallTransformer) {
    put(function.symbol, t)
}

private fun MutableMap<IrSymbol, IrCallTransformer>.compareOp(function: IrSimpleFunctionSymbol, op: cmpop) {
    withTranslatedArgs(function) { Compare(left = it[0], ops = listOf(op), comparators = listOf(it[1])) }
}

private fun MutableMap<IrSymbol, IrCallTransformer>.unaryOp(function: IrSimpleFunctionSymbol, op: unaryop) {
    withTranslatedArgs(function) { UnaryOp(op = op, operand = it[0]) }
}

private fun MutableMap<IrSymbol, IrCallTransformer>.binOp(function: IrSimpleFunctionSymbol, op: operator) {
    withTranslatedArgs(function) { BinOp(left = it[0], op = op, right = it[1]) }
}

private inline fun MutableMap<IrSymbol, IrCallTransformer>.withTranslatedArgs(
    function: IrSimpleFunctionSymbol,
    crossinline t: (List<expr>) -> expr
) {
    put(function) { call, context -> t(translateCallArguments(call, context)) }
}
