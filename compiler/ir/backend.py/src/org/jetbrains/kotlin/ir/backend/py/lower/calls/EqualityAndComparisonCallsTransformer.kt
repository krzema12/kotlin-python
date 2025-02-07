/*
 * Copyright 2010-2018 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.ir.backend.py.lower.calls

import org.jetbrains.kotlin.ir.backend.py.PyIrBackendContext
import org.jetbrains.kotlin.ir.backend.py.ir.JsIrBuilder
import org.jetbrains.kotlin.ir.backend.py.utils.isEqualsInheritedFromAny
import org.jetbrains.kotlin.ir.declarations.IrClass
import org.jetbrains.kotlin.ir.declarations.IrFunction
import org.jetbrains.kotlin.ir.declarations.IrSimpleFunction
import org.jetbrains.kotlin.ir.declarations.isStaticMethodOfClass
import org.jetbrains.kotlin.ir.expressions.IrCall
import org.jetbrains.kotlin.ir.expressions.IrExpression
import org.jetbrains.kotlin.ir.expressions.IrFunctionAccessExpression
import org.jetbrains.kotlin.ir.expressions.impl.IrCallImpl
import org.jetbrains.kotlin.ir.symbols.IrSimpleFunctionSymbol
import org.jetbrains.kotlin.ir.types.IrDynamicType
import org.jetbrains.kotlin.ir.types.isComparable
import org.jetbrains.kotlin.ir.types.isNullable
import org.jetbrains.kotlin.ir.util.*
import org.jetbrains.kotlin.name.Name


class EqualityAndComparisonCallsTransformer(context: PyIrBackendContext) : CallsTransformer {
    private val intrinsics = context.intrinsics
    private val irBuiltIns = context.irBuiltIns

    private val symbolToTransformer: SymbolToTransformer = mutableMapOf()

    init {
        symbolToTransformer.run {
            add(irBuiltIns.eqeqeqSymbol, intrinsics.jsEqeqeq)
            add(irBuiltIns.eqeqSymbol, ::transformEqeqOperator)
            // ieee754equals can only be applied in between statically known Floats, Doubles, null or undefined
            add(irBuiltIns.ieee754equalsFunByOperandType, ::chooseEqualityOperatorForPrimitiveTypes)

            add(irBuiltIns.booleanNotSymbol, intrinsics.jsNot)

            add(irBuiltIns.lessFunByOperandType.filterKeys { it != irBuiltIns.longClass }, intrinsics.jsLt)
            add(irBuiltIns.lessOrEqualFunByOperandType.filterKeys { it != irBuiltIns.longClass }, intrinsics.jsLtEq)
            add(irBuiltIns.greaterFunByOperandType.filterKeys { it != irBuiltIns.longClass }, intrinsics.jsGt)
            add(irBuiltIns.greaterOrEqualFunByOperandType.filterKeys { it != irBuiltIns.longClass }, intrinsics.jsGtEq)

            add(irBuiltIns.lessFunByOperandType[irBuiltIns.longClass]!!, transformLongComparison(intrinsics.jsLt))
            add(irBuiltIns.lessOrEqualFunByOperandType[irBuiltIns.longClass]!!, transformLongComparison(intrinsics.jsLtEq))
            add(irBuiltIns.greaterFunByOperandType[irBuiltIns.longClass]!!, transformLongComparison(intrinsics.jsGt))
            add(irBuiltIns.greaterOrEqualFunByOperandType[irBuiltIns.longClass]!!, transformLongComparison(intrinsics.jsGtEq))
        }
    }

    private fun transformLongComparison(comparator: IrSimpleFunctionSymbol): (IrFunctionAccessExpression) -> IrExpression = { call ->
        IrCallImpl(
            call.startOffset,
            call.endOffset,
            comparator.owner.returnType,
            comparator,
            typeArgumentsCount = 0,
            valueArgumentsCount = 2
        ).apply {
            putValueArgument(0, irCall(call, intrinsics.longCompareToLong, argumentsAsReceivers = true))
            putValueArgument(1, JsIrBuilder.buildInt(irBuiltIns.intType, 0))
        }
    }

    override fun transformFunctionAccess(call: IrFunctionAccessExpression, doNotIntrinsify: Boolean): IrExpression {
        val symbol = call.symbol
        symbolToTransformer[symbol]?.let {
            return it(call)
        }

        return when (symbol.owner.name) {
            Name.identifier("compareTo") -> if (doNotIntrinsify) call else transformCompareToMethodCall(call)
            Name.identifier("equals") -> transformEqualsMethodCall(call as IrCall)
            else -> call
        }
    }

    private fun transformEqeqOperator(call: IrFunctionAccessExpression): IrExpression {
        val lhs = call.getValueArgument(0)!!
        val rhs = call.getValueArgument(1)!!

        return when {
            lhs.type is IrDynamicType ->
                irCall(call, intrinsics.jsEqeq)

            // Special optimization for "<expression> == null"
            lhs.isNullConst() || rhs.isNullConst() ->
                irCall(call, intrinsics.jsEqeq)

            else ->
                chooseEqualityOperatorForPrimitiveTypes(call)  // todo: ensure that __eq__ is used to compile equals everywhere
        }
    }

    private fun chooseEqualityOperatorForPrimitiveTypes(call: IrFunctionAccessExpression): IrExpression = when {
        // todo
        call.allValueArgumentsAreNullable() ->
            irCall(call, intrinsics.jsEqeq)
        else ->
            irCall(call, intrinsics.jsEqeq)
    }

    private fun IrFunctionAccessExpression.allValueArgumentsAreNullable() =
        (0 until valueArgumentsCount).all { getValueArgument(it)!!.type.isNullable() }

    private fun transformCompareToMethodCall(call: IrFunctionAccessExpression): IrExpression {
        val function = call.symbol.owner as IrSimpleFunction
        if (function.parent !is IrClass) return call

        fun IrSimpleFunction.isFakeOverriddenFromComparable(): Boolean = when {
            !isFakeOverride ->
                !isStaticMethodOfClass && parentAsClass.thisReceiver!!.type.isComparable()

            else -> overriddenSymbols.all { it.owner.isFakeOverriddenFromComparable() }
        }

        return when {
            // Use runtime function call in case when receiverType is a primitive JS type that doesn't have `compareTo` method,
            // or has a potential to be primitive type (being fake overridden from `Comparable`)
            function.isMethodOfPrimitiveJSType() || function.isFakeOverriddenFromComparable() ->
                irCall(call, intrinsics.jsCompareTo, receiversAsArguments = true)

            // Valid `compareTo` method must be present at this point
            else ->
                call
        }
    }


    private fun transformEqualsMethodCall(call: IrCall): IrExpression {
        val function = call.symbol.owner
        return when {
            // Nothing special
            !function.isEqualsInheritedFromAny() -> call

            // `Any.equals` works as identity operator
            call.isSuperToAny() ->
                irCall(call, intrinsics.jsEqeqeq, receiversAsArguments = true)

            // Use runtime function call in case when receiverType is a primitive JS type that doesn't have `equals` method,
            // or has a potential to be primitive type (being fake overridden from `Any`)
            function.isMethodOfPotentiallyPrimitiveJSType() ->
                irCall(call, intrinsics.jsEquals, receiversAsArguments = true)

            // Valid `equals` method must be present at this point
            else -> call
        }
    }

    private fun IrFunction.isMethodOfPrimitiveJSType() =
        dispatchReceiverParameter?.let {
            it.type.getPrimitiveType() != PrimitiveType.OTHER
        } ?: false

    private fun IrFunction.isMethodOfPotentiallyPrimitiveJSType() =
        isMethodOfPrimitiveJSType() || isFakeOverriddenFromAny()

}
