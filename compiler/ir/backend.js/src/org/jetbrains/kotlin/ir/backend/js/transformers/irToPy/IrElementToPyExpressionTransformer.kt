/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.ir.backend.js.transformers.irToPy

import generated.Python.*
import org.jetbrains.kotlin.ir.backend.js.utils.JsGenerationContext
import org.jetbrains.kotlin.ir.declarations.IrValueParameter
import org.jetbrains.kotlin.ir.declarations.IrVariable
import org.jetbrains.kotlin.ir.expressions.*

@Suppress("PARAMETER_NAME_CHANGED_ON_OVERRIDE")
class IrElementToPyExpressionTransformer : BaseIrElementToPyNodeTransformer<expr, JsGenerationContext> {

    override fun visitVararg(expression: IrVararg, context: JsGenerationContext): expr {
        // TODO
        return Name(id = identifier("visitVararg"), ctx = Load)
    }

    override fun visitExpression(expression: IrExpression, data: JsGenerationContext): expr {
        // TODO
//        println("visitExpression: $expression")
        return when (expression) {
            is IrConst<*> -> visitConst(expression, data)
            is IrGetValue -> visitGetValue(expression, data)
            is IrCall -> visitCall(expression, data)
            else -> Name(id = identifier("visitExpression-other $expression"), ctx = Load)
        }
    }

    override fun visitExpressionBody(body: IrExpressionBody, context: JsGenerationContext): expr {
        // TODO
        return Name(id = identifier("visitExpressionBody"), ctx = Load)
    }

    override fun visitFunctionExpression(expression: IrFunctionExpression, context: JsGenerationContext): expr {
        // TODO
        return Name(id = identifier("visitFunctionExpression"), ctx = Load)
    }

    override fun <T> visitConst(expression: IrConst<T>, context: JsGenerationContext): expr {
        return when (val kind = expression.kind) {
            is IrConstKind.String -> Constant(
                value = constant(value = "'${kind.valueOf(expression)}'"),
                kind = null,
            )
            is IrConstKind.Int -> Constant(
                value = constant(value = "${kind.valueOf(expression)}"),
                kind = null,
            )
            // TODO other types
            else -> Name(id = identifier("visitConst-other"), ctx = Load)
        }
    }

    override fun visitStringConcatenation(expression: IrStringConcatenation, context: JsGenerationContext): expr {
        // TODO
        return Name(id = identifier("visitStringConcatenation"), ctx = Load)
    }

    override fun visitGetField(expression: IrGetField, context: JsGenerationContext): expr {
        // TODO
        return Name(id = identifier("visitGetField"), ctx = Load)
    }

    override fun visitGetValue(expression: IrGetValue, context: JsGenerationContext): expr {
        // TODO
        println("visitGetValue")
        println(expression.origin)
        println(expression.symbol)
        println(expression.symbol.owner)

        return when (val owner = expression.symbol.owner) {
            is IrValueParameter, is IrVariable -> Name(id = identifier(if (owner.name.isSpecial) "(special)" else owner.name.identifier), ctx = Load)
            else -> Name(id = identifier("visitGetValue_other $owner"), ctx = Load)
        }
    }

    override fun visitGetObjectValue(expression: IrGetObjectValue, context: JsGenerationContext): expr {
        // TODO
        return Name(id = identifier("visitGetObjectValue"), ctx = Load)
    }

    override fun visitSetField(expression: IrSetField, context: JsGenerationContext): expr {
        // TODO
        return Name(id = identifier("visitSetField"), ctx = Load)
    }

    override fun visitSetValue(expression: IrSetValue, context: JsGenerationContext): expr {
        // TODO
        return Name(id = identifier("visitSetValue"), ctx = Load)
    }

    override fun visitDelegatingConstructorCall(expression: IrDelegatingConstructorCall, context: JsGenerationContext): expr {
        // TODO
        return Name(id = identifier("visitDelegatingConstructorCall"), ctx = Load)
    }

    override fun visitConstructorCall(expression: IrConstructorCall, context: JsGenerationContext): expr {
        // TODO
        return Name(id = identifier("visitConstructorCall"), ctx = Load)
    }

    override fun visitCall(expression: IrCall, context: JsGenerationContext): expr {
        // TODO
//        with(expression) {
//            println("symbol.owner.name: ${symbol.owner.name.identifier}")
//        }
//        println("========")

        val noOfArguments = expression.valueArgumentsCount

        val arguments = (0 until noOfArguments).mapNotNull { argIndex ->
            val valueArgument: IrExpression? = expression.getValueArgument(argIndex)
            valueArgument?.let {
                IrElementToPyExpressionTransformer().visitExpression(it, context)
            }
        }

        return Call(
            func = Name(id = identifier(if (expression.symbol.owner.name.isSpecial) "(special)" else expression.symbol.owner.name.identifier), ctx = Load),
            args = arguments,
            keywords = emptyList(),
        )
    }

    override fun visitWhen(expression: IrWhen, context: JsGenerationContext): expr {
        // TODO
        return Name(id = identifier("visitWhen"), ctx = Load)
    }

    override fun visitTypeOperator(expression: IrTypeOperatorCall, data: JsGenerationContext): expr {
        // TODO
        return Name(id = identifier("visitTypeOperator"), ctx = Load)
    }

    override fun visitDynamicMemberExpression(expression: IrDynamicMemberExpression, data: JsGenerationContext): expr {
        // TODO
        return Name(id = identifier("visitDynamicMemberExpression"), ctx = Load)
    }

    override fun visitDynamicOperatorExpression(expression: IrDynamicOperatorExpression, data: JsGenerationContext): expr {
        // TODO
        return Name(id = identifier("visitVararg"), ctx = Load)
    }
}
