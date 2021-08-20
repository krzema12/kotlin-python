/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.ir.backend.py.transformers.irToPy

import generated.Python.*
import org.jetbrains.kotlin.ir.backend.py.lower.InteropCallableReferenceLowering
import org.jetbrains.kotlin.ir.backend.py.utils.JsGenerationContext
import org.jetbrains.kotlin.ir.backend.py.utils.asString
import org.jetbrains.kotlin.ir.backend.py.utils.isJsNativeInvoke
import org.jetbrains.kotlin.ir.backend.py.utils.realOverrideTarget
import org.jetbrains.kotlin.ir.declarations.IrSimpleFunction
import org.jetbrains.kotlin.ir.declarations.IrValueParameter
import org.jetbrains.kotlin.ir.declarations.IrVariable
import org.jetbrains.kotlin.ir.expressions.*
import org.jetbrains.kotlin.ir.util.isFunctionTypeOrSubtype
import org.jetbrains.kotlin.ir.util.parentAsClass
import org.jetbrains.kotlin.util.OperatorNameConventions

@Suppress("PARAMETER_NAME_CHANGED_ON_OVERRIDE")
class IrElementToPyExpressionTransformer : BaseIrElementToPyNodeTransformer<List<expr>, JsGenerationContext> {

    override fun visitVararg(expression: IrVararg, context: JsGenerationContext): List<expr> {
        return expression.elements.flatMap { it.accept(this, context) }
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
            is IrVararg -> visitVararg(expression, data)
            is IrDynamicOperatorExpression -> visitDynamicOperatorExpression(expression, data)
            is IrDynamicMemberExpression -> visitDynamicMemberExpression(expression, data)
            is IrStringConcatenation -> visitStringConcatenation(expression, data)
            is IrFunctionExpression -> visitFunctionExpression(expression, data)
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
        // TODO: create lowering: if there is one statement, use IrExpressionBody, otherwise, create a _no_name_provided_function_ and call it.
        //       for now, the code doesn't support some cases

        return Lambda(
            args = argumentsImpl(
                posonlyargs = emptyList(),
                args = expression.function.valueParameters.map { argImpl(identifier(it.name.asString().toValidPythonSymbol()), null, null) },
                kwonlyargs = emptyList(),
                kw_defaults = emptyList(),
                defaults = emptyList(),
                vararg = null,
                kwarg = null,
            ),
            body = when (val body = expression.function.body) {
                is IrBlockBody -> {
                    val statements = IrElementToPyStatementTransformer().visitBlockBody(body, context)
                    when (val single = statements.singleOrNull() as? Return) {
                        null -> Name(id = identifier("visitExpressionFunctionBodyStatements x${statements.size} ${statements.map { it::class.simpleName }}".toValidPythonSymbol()), ctx = Load)
                        else -> single.value ?: Name(id = identifier("visitExpressionFunctionBodyStatementsReturn null".toValidPythonSymbol()), ctx = Load)
                    }
                }
                else -> Name(id = identifier("visitExpressionFunctionBody $body".toValidPythonSymbol()), ctx = Load)
            }
        )
            .let(::listOf)
    }

    override fun <T> visitConst(expression: IrConst<T>, context: JsGenerationContext): List<expr> {
        return listOf(when (val kind = expression.kind) {
            is IrConstKind.String -> Constant(
                value = constant(value = "'${kind.valueOf(expression).replace("'", "\\'")}'"),
                kind = null,
            )
            is IrConstKind.Long -> Constant(
                value = constant(value = "${kind.valueOf(expression)}"),
                kind = null,
            )
            is IrConstKind.Int -> Constant(
                value = constant(value = "${kind.valueOf(expression)}"),
                kind = null,
            )
            is IrConstKind.Short -> Constant(
                value = constant(value = "${kind.valueOf(expression)}"),
                kind = null,
            )
            is IrConstKind.Byte -> Constant(
                value = constant(value = "${kind.valueOf(expression)}"),
                kind = null,
            )
            is IrConstKind.Double -> Constant(
                value = constant(value = "${kind.valueOf(expression)}"),
                kind = null,
            )
            is IrConstKind.Float -> Constant(
                value = constant(value = "${kind.valueOf(expression)}"),
                kind = null,
            )
            is IrConstKind.Boolean -> Constant(
                value = constant(value = "${kind.valueOf(expression)}".replaceFirstChar { it.uppercase() }),
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
        return expression
            .arguments
            .map { argument ->
                argument
                    .accept(this, context)
                    .singleOrNull()
                    ?.let { Call(func = Name(id = identifier("str"), ctx = Load), args = listOf(it), keywords = emptyList()) }
                    ?: Name(id = identifier("visitStringConcatenation $argument".toValidPythonSymbol()), ctx = Load)
            }
            .reduce { left, right -> BinOp(left = left, op = Add, right = right) }
            .let(::listOf)
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
        val noOfArguments = expression.valueArgumentsCount

        val arguments = (0 until noOfArguments).mapNotNull { argIndex ->
            val valueArgument: IrExpression? = expression.getValueArgument(argIndex)
            valueArgument?.let {
                IrElementToPyExpressionTransformer().visitExpression(it, context)
            }
        }.flatten()

        return listOf(Call(
            func = Name(id = identifier("super"), ctx = Load),
            args = arguments,
            keywords = emptyList(),
        ))
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
        fun isFunctionTypeInvoke(receiver: expr?, call: IrCall): Boolean {
            if (receiver == null) return false
            val simpleFunction = call.symbol.owner as? IrSimpleFunction ?: return false
            val receiverType = simpleFunction.dispatchReceiverParameter?.type ?: return false

            if (call.origin === InteropCallableReferenceLowering.Companion.EXPLICIT_INVOKE) return false

            return simpleFunction.name == OperatorNameConventions.INVOKE && receiverType.isFunctionTypeOrSubtype()
        }

        val function = expression.symbol.owner.realOverrideTarget

        context.staticContext.intrinsics[function.symbol]?.let {
            return it(expression, context)
        }

        val transformer = IrElementToPyExpressionTransformer()
        val pyDispatchReceiver = expression.dispatchReceiver?.accept(transformer, context)
        val pyExtensionReceiver = expression.extensionReceiver?.accept(transformer, context)
        val arguments = translateCallArguments(expression, context, transformer)

        if (isFunctionTypeInvoke(pyDispatchReceiver?.single(), expression) || expression.symbol.owner.isJsNativeInvoke()) {
            return Call(
                func = pyDispatchReceiver?.single() ?: pyExtensionReceiver!!.single(),
                args = arguments,
                keywords = emptyList(),
            )
                .let(::listOf)
        }

        if (pyDispatchReceiver == null) {
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
                        value = pyDispatchReceiver.single(),
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
        return listOf(
            expression
                .branches
                .map { branch ->
                    IfExp(
                        test = IrElementToPyExpressionTransformer().visitExpression(branch.condition, context).first(),
                        body = IrElementToPyExpressionTransformer().visitExpression(branch.result, context).first(),
                        orelse = Name(id = identifier("dummyBranch"), ctx = Load),
                    )
                }
                .reduceRight { iff, acc ->
                    val accTest = acc.test

                    if (accTest is Constant && accTest.value.value == "True") {
                        // optimization
                        IfExp(
                            test = iff.test,
                            body = iff.body,
                            orelse = acc.body,
                        )
                    } else {
                        IfExp(
                            test = iff.test,
                            body = iff.body,
                            orelse = acc,
                        )
                    }
                }
        )
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
        return listOf(
            Call(
                func = Name(id = identifier(expression.memberName.toValidPythonSymbol()), ctx = Load),
                args = visitExpression(expression.receiver, data),
                keywords = emptyList(),
            )
        )
    }

    override fun visitDynamicOperatorExpression(expression: IrDynamicOperatorExpression, data: JsGenerationContext): List<expr> {
        // TODO
        return listOf(
            Call(
                func = Name(id = identifier(expression.operator.toString().toValidPythonSymbol()), ctx = Load),
                args = visitExpression(expression.receiver, data) + expression.arguments.flatMap { visitExpression(it, data) },
                keywords = emptyList(),
            )
        )
    }

    override fun visitComposite(expression: IrComposite, data: JsGenerationContext): List<expr> {
        // TODO
        return listOf(Name(id = identifier("visitComposite-inToPyExpressionTransformer $expression".toValidPythonSymbol()), ctx = Load))
    }
}
