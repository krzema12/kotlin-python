/*
 * Copyright 2010-2018 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.ir.backend.py.ir

import org.jetbrains.kotlin.ir.backend.py.PyIrBackendContext
import org.jetbrains.kotlin.ir.backend.py.utils.OperatorNames
import org.jetbrains.kotlin.ir.expressions.IrExpression
import org.jetbrains.kotlin.ir.types.IrSimpleType
import org.jetbrains.kotlin.name.Name

class JsIrArithBuilder(val context: PyIrBackendContext) {

    val symbols = context.ir.symbols

    private fun buildBinaryOperator(name: Name, l: IrExpression, r: IrExpression): IrExpression {
        val symbol = context.getOperatorByName(name, l.type as IrSimpleType)
        return JsIrBuilder.buildCall(symbol!!).apply {
            dispatchReceiver = l
            putValueArgument(0, r)
        }
    }

    private fun buildUnaryOperator(name: Name, v: IrExpression): IrExpression {
        val symbol = context.getOperatorByName(name, v.type as IrSimpleType)!!
        return JsIrBuilder.buildCall(symbol).apply { dispatchReceiver = v }
    }

    fun add(l: IrExpression, r: IrExpression) = buildBinaryOperator(OperatorNames.ADD, l, r)
    fun div(l: IrExpression, r: IrExpression) = buildBinaryOperator(OperatorNames.DIV, l, r)
    fun mod(l: IrExpression, r: IrExpression) = buildBinaryOperator(OperatorNames.MOD, l, r)
    fun and(l: IrExpression, r: IrExpression) = buildBinaryOperator(OperatorNames.AND, l, r)
    fun or(l: IrExpression, r: IrExpression) = buildBinaryOperator(OperatorNames.OR, l, r)
    fun shl(l: IrExpression, r: IrExpression) = buildBinaryOperator(OperatorNames.SHL, l, r)
    fun shr(l: IrExpression, r: IrExpression) = buildBinaryOperator(OperatorNames.SHR, l, r)
    fun not(v: IrExpression): IrExpression = buildUnaryOperator(OperatorNames.NOT, v)
    fun inv(v: IrExpression): IrExpression = buildUnaryOperator(OperatorNames.INV, v)

    fun andand(l: IrExpression, r: IrExpression) =
        JsIrBuilder.buildIfElse(context.irBuiltIns.booleanType, l, r, JsIrBuilder.buildBoolean(context.irBuiltIns.booleanType, false))
    fun oror(l: IrExpression, r: IrExpression) =
        JsIrBuilder.buildIfElse(context.irBuiltIns.booleanType, l, JsIrBuilder.buildBoolean(context.irBuiltIns.booleanType, true), r)
}