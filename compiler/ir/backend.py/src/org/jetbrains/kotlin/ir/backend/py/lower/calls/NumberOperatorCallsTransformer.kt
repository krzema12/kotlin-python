/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.ir.backend.py.lower.calls

import org.jetbrains.kotlin.ir.backend.py.PyIrBackendContext
import org.jetbrains.kotlin.ir.backend.py.ir.JsIrBuilder
import org.jetbrains.kotlin.ir.backend.py.utils.OperatorNames
import org.jetbrains.kotlin.ir.expressions.IrExpression
import org.jetbrains.kotlin.ir.expressions.IrFunctionAccessExpression
import org.jetbrains.kotlin.ir.expressions.impl.IrCallImpl
import org.jetbrains.kotlin.ir.symbols.IrSimpleFunctionSymbol
import org.jetbrains.kotlin.ir.types.*
import org.jetbrains.kotlin.ir.util.irCall
import org.jetbrains.kotlin.name.Name

private val HASH_CODE_NAME = Name.identifier("hashCode")

class NumberOperatorCallsTransformer(context: PyIrBackendContext) : CallsTransformer {
    private val intrinsics = context.intrinsics
    private val irBuiltIns = context.irBuiltIns

    private fun buildInt(v: Int) = JsIrBuilder.buildInt(irBuiltIns.intType, v)

    private val memberToTransformer = MemberToTransformer().apply {

        val primitiveNumbers =
            irBuiltIns.run { listOf(longType, intType, shortType, byteType, floatType, doubleType) }

        for (type in primitiveNumbers) {
            add(type, OperatorNames.UNARY_PLUS, intrinsics.jsUnaryPlus)
            add(type, OperatorNames.UNARY_MINUS, ::transformUnaryMinus)
        }

        add(irBuiltIns.stringType, OperatorNames.ADD, intrinsics.jsPlus)

        irBuiltIns.intType.let {
            add(it, OperatorNames.SHL, intrinsics.jsBitShiftL)
            add(it, OperatorNames.SHR, intrinsics.jsBitShiftR)
            add(it, OperatorNames.SHRU, intrinsics.jsBitShiftRU)
            add(it, OperatorNames.AND, intrinsics.jsBitAnd)
            add(it, OperatorNames.OR, intrinsics.jsBitOr)
            add(it, OperatorNames.XOR, intrinsics.jsBitXor)
            add(it, OperatorNames.INV, intrinsics.jsBitNot)
        }

        irBuiltIns.booleanType.let {
            // These operators are not short-circuit -- using bitwise operators '&', '|', '^' followed by coercion to boolean
            add(it, OperatorNames.AND) { call -> toBoolean(irCall(call, intrinsics.jsBitAnd, receiversAsArguments = true)) }
            add(it, OperatorNames.OR) { call -> toBoolean(irCall(call, intrinsics.jsBitOr, receiversAsArguments = true)) }
            add(it, OperatorNames.XOR) { call -> toBoolean(irCall(call, intrinsics.jsBitXor, receiversAsArguments = true)) }

            add(it, OperatorNames.NOT, intrinsics.jsNot)

            add(it, HASH_CODE_NAME) { call -> intrinsics.jsNumberToInt.call(call.dispatchReceiver!!) }
        }

        for (type in primitiveNumbers) {
            add(type, Name.identifier("rangeTo"), ::transformRangeTo)
            add(type, HASH_CODE_NAME, ::transformHashCode)
        }

        for (type in primitiveNumbers) {
            add(type, OperatorNames.INC, ::transformIncrement)
            add(type, OperatorNames.DEC, ::transformDecrement)
        }

        for (type in primitiveNumbers) {
            add(type, OperatorNames.ADD, withLongCoercion(::transformAdd))
            add(type, OperatorNames.SUB, withLongCoercion(::transformSub))
            add(type, OperatorNames.MUL, withLongCoercion(::transformMul))
            add(type, OperatorNames.DIV, withLongCoercion(::transformDiv))
            add(type, OperatorNames.MOD, withLongCoercion(::transformRem))
            add(type, OperatorNames.REM, withLongCoercion(::transformRem))
        }
    }

    override fun transformFunctionAccess(call: IrFunctionAccessExpression, doNotIntrinsify: Boolean): IrExpression {
        val function = call.symbol.owner
        function.dispatchReceiverParameter?.also {
            val key = SimpleMemberKey(it.type, function.name)
            memberToTransformer[key]?.also {
                return it(call)
            }
        }
        return call
    }

    private fun transformRangeTo(call: IrFunctionAccessExpression): IrExpression {
        if (call.valueArgumentsCount != 1) return call
        return with(call.symbol.owner.valueParameters[0].type) {
            when {
                isByte() || isShort() || isInt() ->
                    irCall(call, intrinsics.jsNumberRangeToNumber, receiversAsArguments = true)
                isLong() ->
                    irCall(call, intrinsics.jsNumberRangeToLong, receiversAsArguments = true)
                else -> call
            }
        }
    }

    private fun transformHashCode(call: IrFunctionAccessExpression): IrExpression {
        return with(call.symbol.owner.dispatchReceiverParameter!!.type) {
            when {
                isByte() || isShort() || isInt() ->
                    call.dispatchReceiver!!
                isFloat() || isDouble() ->
                    // TODO introduce doubleToHashCode?
                    irCall(call, intrinsics.jsGetNumberHashCode, receiversAsArguments = true)
                else -> call
            }
        }
    }

    private fun irBinaryOp(
        call: IrFunctionAccessExpression,
        intrinsic: IrSimpleFunctionSymbol,
        toInt32: Boolean = false
    ): IrExpression {
        val newCall = irCall(call, intrinsic, receiversAsArguments = true)
        if (toInt32)
            return intrinsics.jsNumberToInt.call(newCall)
        return newCall
    }

    class BinaryOp(call: IrFunctionAccessExpression) {
        val function = call.symbol.owner
        val name = function.name
        val lhs = function.dispatchReceiverParameter!!.type
        val rhs = function.valueParameters[0].type
        val result = function.returnType

        fun canAddOrSubOverflow() =
            result.isInt() && (lhs.isInt() || rhs.isInt())
    }

    private fun transformAdd(call: IrFunctionAccessExpression) =
        irBinaryOp(call, intrinsics.jsPlus, toInt32 = BinaryOp(call).canAddOrSubOverflow())

    private fun transformSub(call: IrFunctionAccessExpression) =
        irBinaryOp(call, intrinsics.jsMinus, toInt32 = BinaryOp(call).canAddOrSubOverflow())

    private fun transformMul(call: IrFunctionAccessExpression) =
        irBinaryOp(call, intrinsics.jsMult, toInt32 = BinaryOp(call).result.isInt())

    private fun transformDiv(call: IrFunctionAccessExpression) =
        irBinaryOp(call, intrinsics.jsDiv, toInt32 = BinaryOp(call).result.isInt())

    private fun transformRem(call: IrFunctionAccessExpression) =
        irBinaryOp(call, intrinsics.jsMod)

    private fun transformIncrement(call: IrFunctionAccessExpression) =
        transformCrement(call, intrinsics.jsPlus)

    private fun transformDecrement(call: IrFunctionAccessExpression) =
        transformCrement(call, intrinsics.jsMinus)

    private fun transformCrement(call: IrFunctionAccessExpression, correspondingBinaryOp: IrSimpleFunctionSymbol): IrExpression {
        val operation = irCall(call, correspondingBinaryOp, receiversAsArguments = true).apply {
            putValueArgument(1, buildInt(1))
        }

        return convertResultToPrimitiveType(operation, call.type)
    }

    private fun transformUnaryMinus(call: IrFunctionAccessExpression) =
        convertResultToPrimitiveType(
            irCall(call, intrinsics.jsUnaryMinus, receiversAsArguments = true),
            call.type
        )

    private fun convertResultToPrimitiveType(e: IrExpression, type: IrType) = when {
        type.isByte() -> intrinsics.jsNumberToByte.call(e)
        type.isShort() -> intrinsics.jsNumberToShort.call(e)
        type.isInt() -> intrinsics.jsNumberToInt.call(e)
        type.isLong() -> intrinsics.jsNumberToLong.call(e)
        else -> e
    }

    private fun withLongCoercion(default: (IrFunctionAccessExpression) -> IrExpression): (IrFunctionAccessExpression) -> IrExpression =
        { call ->
            assert(call.valueArgumentsCount == 1)
            val arg = call.getValueArgument(0)!!

            if (arg.type.isLong()) {
                val receiverType = call.dispatchReceiver!!.type

                when {
                    // Double OP Long => Double OP Long.toDouble()
                    receiverType.isDouble() -> {
                        call.putValueArgument(0, IrCallImpl(
                            call.startOffset,
                            call.endOffset,
                            intrinsics.longToDouble.owner.returnType,
                            intrinsics.longToDouble,
                            typeArgumentsCount = 0,
                            valueArgumentsCount = 0
                        ).apply {
                            dispatchReceiver = arg
                        })
                    }
                    // Float OP Long => Float OP Long.toFloat()
                    receiverType.isFloat() -> {
                        call.putValueArgument(0, IrCallImpl(
                            call.startOffset,
                            call.endOffset,
                            intrinsics.longToFloat.owner.returnType,
                            intrinsics.longToFloat,
                            typeArgumentsCount = 0,
                            valueArgumentsCount = 0
                        ).apply {
                            dispatchReceiver = arg
                        })
                    }
                }
            }

            if (call.dispatchReceiver!!.type.isLong()) {
                call
            } else {
                default(call)
            }
        }

    fun IrSimpleFunctionSymbol.call(vararg arguments: IrExpression) =
        JsIrBuilder.buildCall(this, owner.returnType).apply {
            for ((idx, arg) in arguments.withIndex()) {
                putValueArgument(idx, arg)
            }
        }

    private fun booleanNegate(e: IrExpression) =
        JsIrBuilder.buildCall(intrinsics.jsNot, irBuiltIns.booleanType).apply {
            putValueArgument(0, e)
        }

    private fun toBoolean(e: IrExpression) =
        booleanNegate(booleanNegate(e))
}
