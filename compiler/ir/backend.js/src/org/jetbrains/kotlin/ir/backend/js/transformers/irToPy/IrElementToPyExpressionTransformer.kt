/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.ir.backend.js.transformers.irToPy

import generated.Python.*
import org.jetbrains.kotlin.ir.backend.js.utils.JsGenerationContext
import org.jetbrains.kotlin.ir.backend.js.utils.asString
import org.jetbrains.kotlin.ir.declarations.IrValueParameter
import org.jetbrains.kotlin.ir.declarations.IrVariable
import org.jetbrains.kotlin.ir.expressions.*
import org.jetbrains.kotlin.ir.util.parentAsClass

@Suppress("PARAMETER_NAME_CHANGED_ON_OVERRIDE")
class IrElementToPyExpressionTransformer : BaseIrElementToPyNodeTransformer<List<expr>, JsGenerationContext> {

    override fun visitVararg(expression: IrVararg, context: JsGenerationContext): List<expr> {
        // TODO
        return listOf(Name(id = identifier("visitVararg"), ctx = Load))
    }

    override fun visitExpression(expression: IrExpression, data: JsGenerationContext): List<expr> {
        // TODO
        return when (expression) {
            is IrConst<*> -> visitConst(expression, data)
            is IrGetValue -> visitGetValue(expression, data)
            is IrGetField -> visitGetField(expression, data)
            is IrCall -> visitCall(expression, data)
            is IrComposite -> visitComposite(expression, data)
            is IrSetValue -> visitSetValue(expression, data)
            is IrWhen -> visitWhen(expression, data)
            is IrConstructorCall -> visitConstructorCall(expression, data)
            is IrTypeOperatorCall -> visitTypeOperator(expression, data)
//            is IrBlock -> visitBlock(expression, data)
            else -> listOf(Name(id = identifier("visitExpression-other $expression".toValidPythonSymbol()), ctx = Load))
        }
    }

//    override fun visitBlock(expression: IrBlock, data: JsGenerationContext): List<expr> {
//        // TODO
//        return listOf(Name(id = identifier("visitBlock $expression"), ctx = Load))
//    }

    override fun visitExpressionBody(body: IrExpressionBody, context: JsGenerationContext): List<expr> {
        // TODO
        return listOf(Name(id = identifier("visitExpressionBody $body".toValidPythonSymbol()), ctx = Load))
    }

    override fun visitFunctionExpression(expression: IrFunctionExpression, context: JsGenerationContext): List<expr> {
        // TODO
        return listOf(Name(id = identifier("visitFunctionExpression $expression".toValidPythonSymbol()), ctx = Load))
    }

    override fun <T> visitConst(expression: IrConst<T>, context: JsGenerationContext): List<expr> {
        return listOf(when (val kind = expression.kind) {
            is IrConstKind.String -> Constant(
                value = constant(value = "'${kind.valueOf(expression).replace("'", "\\'")}'"),
                kind = null,
            )
            is IrConstKind.Int -> Constant(
                value = constant(value = "${kind.valueOf(expression)}"),
                kind = null,
            )
            is IrConstKind.Double -> Constant(
                value = constant(value = "${kind.valueOf(expression)}"),
                kind = null,
            )
            is IrConstKind.Boolean -> Constant(
                value = constant(value = "${kind.valueOf(expression)}".capitalize()),
                kind = null,
            )
            is IrConstKind.Null -> Constant(
                value = constant(value = "None"),
                kind = null,
            )
            // TODO other types
            else -> Name(id = identifier("visitConst-other $kind".toValidPythonSymbol()), ctx = Load)
        })
    }

    override fun visitStringConcatenation(expression: IrStringConcatenation, context: JsGenerationContext): List<expr> {
        // TODO
        return listOf(Name(id = identifier("visitStringConcatenation $expression".toValidPythonSymbol()), ctx = Load))
    }

    override fun visitGetField(expression: IrGetField, context: JsGenerationContext): List<expr> {
        // TODO
        val field = expression.symbol.owner
        val receiverExpression = expression.receiver?.accept(this, context)?.get(0)

        return listOf(if (receiverExpression != null) {
            Attribute(value = receiverExpression, attr = identifier(expression.symbol.owner.name.asString().toValidPythonSymbol()), ctx = Store)
        } else {
            Name(id = identifier(field.name.asString().toValidPythonSymbol()), ctx = Load)
        })
    }

    override fun visitGetValue(expression: IrGetValue, context: JsGenerationContext): List<expr> {
        // TODO
        return listOf(when (val owner = expression.symbol.owner) {
            is IrValueParameter, is IrVariable -> Name(id = identifier(owner.name.asString().toValidPythonSymbol().toPythonSpecific()), ctx = Load)
            else -> Name(id = identifier("visitGetValue_other $owner".toValidPythonSymbol()), ctx = Load)
        })
    }

    override fun visitGetObjectValue(expression: IrGetObjectValue, context: JsGenerationContext): List<expr> {
        // TODO
        return listOf(Name(id = identifier("visitGetObjectValue $expression".toValidPythonSymbol()), ctx = Load))
    }

    override fun visitSetField(expression: IrSetField, context: JsGenerationContext): List<expr> {
        // TODO
        return listOf(Name(id = identifier("visitSetField_expression $expression".toValidPythonSymbol()), ctx = Load))
    }

    override fun visitSetValue(expression: IrSetValue, context: JsGenerationContext): List<expr> {
        // TODO
        return listOf(Name(id = identifier("visitSetValue-inToPyExpressionTransformer $expression".toValidPythonSymbol()), ctx = Load))
    }

    override fun visitDelegatingConstructorCall(expression: IrDelegatingConstructorCall, context: JsGenerationContext): List<expr> {
        // TODO
        return listOf(Name(id = identifier("visitDelegatingConstructorCall $expression".toValidPythonSymbol()), ctx = Load))
    }

    override fun visitConstructorCall(expression: IrConstructorCall, context: JsGenerationContext): List<expr> {
        val noOfArguments = expression.valueArgumentsCount

        val arguments = (0 until noOfArguments).mapNotNull { argIndex ->
            val valueArgument: IrExpression? = expression.getValueArgument(argIndex)
            valueArgument?.let {
                IrElementToPyExpressionTransformer().visitExpression(it, context)
            }
        }.flatten()

        val className = expression.symbol.owner.parentAsClass.name.asString().toValidPythonSymbol()
        return listOf(Call(
            func = Name(id = identifier(className), ctx = Load),
            args = arguments,
            keywords = emptyList(),
        ))
    }

    override fun visitCall(expression: IrCall, context: JsGenerationContext): List<expr> {
        // TODO
        val noOfArguments = expression.valueArgumentsCount

        val arguments = (0 until noOfArguments).mapNotNull { argIndex ->
            val valueArgument: IrExpression? = expression.getValueArgument(argIndex)
            valueArgument?.let {
                IrElementToPyExpressionTransformer().visitExpression(it, context)
            }
        }.flatten()

        val test: List<expr>? = expression.dispatchReceiver?.accept(this, context)

        if (test == null) {
            return listOf(
                Call(
                    func = Name(id = identifier(expression.symbol.owner.name.asString().toValidPythonSymbol()), ctx = Load),
                    args = arguments,
                    keywords = emptyList(),
                )
            )
        } else {
            return listOf(
                Call(
                    func = Attribute(
                        value = test[0],
                        attr = identifier(expression.symbol.owner.name.asString().toValidPythonSymbol()),
                        ctx = Load,
                    ),
                    args = arguments,
                    keywords = emptyList(),
                )
            )
        }
    }

    override fun visitWhen(expression: IrWhen, context: JsGenerationContext): List<expr> {
        // TODO
        return listOf(Name(id = identifier("visitWhen-inToByExpressionTransformer $expression".toValidPythonSymbol()), ctx = Load))
    }

    override fun visitTypeOperator(expression: IrTypeOperatorCall, data: JsGenerationContext): List<expr> {
        // TODO
        return listOf(when (expression.operator) {
            IrTypeOperator.REINTERPRET_CAST -> Call(
                func = Name(id = identifier(expression.typeOperand.asString().toValidPythonSymbol()), ctx = Load),
                args = visitExpression(expression.argument, data),
                keywords = emptyList(),
            )
            else -> Name(id = identifier("visitTypeOperator ${expression.operator}".toValidPythonSymbol()), ctx = Load)
        })
    }

    override fun visitDynamicMemberExpression(expression: IrDynamicMemberExpression, data: JsGenerationContext): List<expr> {
        // TODO
        return listOf(Name(id = identifier("visitDynamicMemberExpression $expression".toValidPythonSymbol()), ctx = Load))
    }

    override fun visitDynamicOperatorExpression(expression: IrDynamicOperatorExpression, data: JsGenerationContext): List<expr> {
        // TODO
        return listOf(Name(id = identifier("visitVararg $expression".toValidPythonSymbol()), ctx = Load))
    }

    override fun visitComposite(expression: IrComposite, data: JsGenerationContext): List<expr> {
        // TODO
        return listOf(Name(id = identifier("visitComposite-inToPyExpressionTransformer $expression".toValidPythonSymbol()), ctx = Load))
    }
}
