/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.ir.backend.py.transformers.irToPy

import generated.Python.*
import org.jetbrains.kotlin.ir.backend.py.lower.InteropCallableReferenceLowering
import org.jetbrains.kotlin.ir.backend.py.utils.*
import org.jetbrains.kotlin.ir.declarations.IrConstructor
import org.jetbrains.kotlin.ir.declarations.IrSimpleFunction
import org.jetbrains.kotlin.ir.declarations.IrValueParameter
import org.jetbrains.kotlin.ir.declarations.IrVariable
import org.jetbrains.kotlin.ir.expressions.*
import org.jetbrains.kotlin.ir.util.isEffectivelyExternal
import org.jetbrains.kotlin.ir.util.isFunctionTypeOrSubtype
import org.jetbrains.kotlin.ir.util.parentAsClass
import org.jetbrains.kotlin.util.OperatorNameConventions

@Suppress("PARAMETER_NAME_CHANGED_ON_OVERRIDE")
class IrElementToPyExpressionTransformer : BaseIrElementToPyNodeTransformer<expr, JsGenerationContext> {

    override fun visitVararg(expression: IrVararg, context: JsGenerationContext): expr {
        return Tuple(elts = expression.elements.map { it.accept(this, context) }, ctx = Load)
    }

    override fun visitExpression(expression: IrExpression, data: JsGenerationContext): expr {
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
            is IrRawFunctionReference -> visitRawFunctionReference(expression, data)
            else -> Name(id = identifier("visitExpression-other $expression".toValidPythonSymbol()), ctx = Load)
        }
    }

//    override fun visitBlock(expression: IrBlock, data: JsGenerationContext): expr {
//        // TODO
//        return Name(id = identifier("visitBlock $expression"), ctx = Load)
//    }

    override fun visitExpressionBody(body: IrExpressionBody, context: JsGenerationContext): expr {
        // TODO
        return Name(id = identifier("visitExpressionBody $body".toValidPythonSymbol()), ctx = Load)
    }

    override fun visitFunctionExpression(expression: IrFunctionExpression, context: JsGenerationContext): expr {
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
    }

    override fun <T> visitConst(expression: IrConst<T>, context: JsGenerationContext): expr {
        return when (val kind = expression.kind) {
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
        }
    }

    override fun visitStringConcatenation(expression: IrStringConcatenation, context: JsGenerationContext): expr {
        return expression
            .arguments
            .map { argument ->
                @Suppress("USELESS_CAST")  // doesn't work without `as expr`
                argument
                    .accept(this, context)
                    .let { Call(func = Name(id = identifier("str"), ctx = Load), args = listOf(it), keywords = emptyList()) as expr }
            }
            .reduce { left, right -> BinOp(left = left, op = Add, right = right) }
    }

    override fun visitGetField(expression: IrGetField, context: JsGenerationContext): expr {
        // TODO
        val field = expression.symbol.owner
        val receiverExpression = expression.receiver?.accept(this, context)

        return if (receiverExpression != null) {
            Attribute(value = receiverExpression, attr = identifier(expression.symbol.owner.name.asString().toValidPythonSymbol()), ctx = Store)
        } else {
            Name(id = identifier(field.name.asString().toValidPythonSymbol()), ctx = Load)
        }
    }

    override fun visitGetValue(expression: IrGetValue, context: JsGenerationContext): expr {
        // TODO
        return when (val owner = expression.symbol.owner) {
            is IrValueParameter, is IrVariable -> Name(id = identifier(owner.name.asString().toValidPythonSymbol().toPythonSpecific()), ctx = Load)
            else -> Name(id = identifier("visitGetValue_other $owner".toValidPythonSymbol()), ctx = Load)
        }
    }

    override fun visitGetObjectValue(expression: IrGetObjectValue, context: JsGenerationContext): expr {
        val field = expression.symbol.owner
        return Name(id = identifier(field.name.asString().toValidPythonSymbol()), ctx = Load)
    }

    override fun visitSetField(expression: IrSetField, context: JsGenerationContext): expr {
        // TODO
        return Name(id = identifier("visitSetField_expression $expression".toValidPythonSymbol()), ctx = Load)
    }

    override fun visitSetValue(expression: IrSetValue, context: JsGenerationContext): expr {
        // TODO
        return Name(id = identifier("visitSetValue-inToPyExpressionTransformer $expression".toValidPythonSymbol()), ctx = Load)
    }

    override fun visitDelegatingConstructorCall(expression: IrDelegatingConstructorCall, context: JsGenerationContext): expr {
        // compile `super(arg1, arg2, arg...)` as `SuperClassName.__init__(self, arg1, arg2, arg...)`
        val function = expression.symbol.owner
        val arguments = translateCallArguments(expression, context, this)
        val klass = function.parentAsClass
        val fromPrimary = context.currentFunction is IrConstructor
        val receiver = when (fromPrimary) {
            true -> "self"
            false -> context.currentFunction!!.valueParameters.last().name.asString().toValidPythonSymbol()
        }

        val className = context.getNameForClass(klass).ident.toValidPythonSymbol()
        return Call(
            func = Attribute(
                value = Name(identifier(className), Load),
                attr = identifier("__init__"),
                ctx = Load,
            ),
            args = listOf(Name(identifier(receiver), Load)) + arguments,
            keywords = emptyList(),
        )
    }

    override fun visitConstructorCall(expression: IrConstructorCall, context: JsGenerationContext): expr {
        val function = expression.symbol.owner
        val arguments = translateCallArguments(expression, context, this)
        val klass = function.parentAsClass

        require(!klass.isInline) {
            "All inline class constructor calls must be lowered to static function calls"
        }

        val className = context.getNameForClass(klass).ident.toValidPythonSymbol()
        return Call(
            func = Name(id = identifier(className), ctx = Load),
            args = arguments,
            keywords = emptyList(),
        )
    }

    override fun visitCall(expression: IrCall, context: JsGenerationContext): expr {
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

        // Transform external property accessor call
        // @JsName-annotated external property accessors are translated as function calls
        if (function.getJsName() == null) {
            val property = function.correspondingPropertySymbol?.owner
            if (property != null && property.isEffectivelyExternal()) {
                val name = Name(id = identifier(context.getNameForProperty(property).ident.toValidPythonSymbol()), ctx = Load)
                return when (function) {
                    property.getter -> name
//                    property.setter -> Assign(targets = listOf(name), value = arguments.single(), type_comment = null)
                    // todo: this is a statement but an expression is required
                    property.setter -> Name(id = identifier("visitCall set ${context.getNameForProperty(property).ident.toValidPythonSymbol()}"), ctx = Load)
                    else -> error("Function must be an accessor of corresponding property")
                }
            }
        }

        if (isFunctionTypeInvoke(pyDispatchReceiver, expression) || expression.symbol.owner.isJsNativeInvoke()) {
            return Call(
                func = pyDispatchReceiver ?: pyExtensionReceiver!!,
                args = arguments,
                keywords = emptyList(),
            )
        }

        if (pyDispatchReceiver == null) {
            return try {
                Call(
                    func = Name(id = identifier(context.getNameForStaticFunction(function).ident.toValidPythonSymbol()), ctx = Load),
                    args = listOfNotNull(pyExtensionReceiver) + arguments,
                    keywords = emptyList(),
                )
            } catch (e: IllegalStateException) {
                Name(id = identifier("visitCall getNameForStaticFunction ${e.message}".toValidPythonSymbol()), ctx = Load)  // todo
            }
        } else {
            return Call(
                func = Attribute(
                    value = pyDispatchReceiver,
                    attr = identifier(context.getNameForMemberFunction(function).ident.toValidPythonSymbol()),
                    ctx = Load,
                ),
                args = arguments,
                keywords = emptyList(),
            )
        }
    }

    override fun visitWhen(expression: IrWhen, context: JsGenerationContext): expr {
        return expression
            .branches
            .map { branch ->
                IfExp(
                    test = IrElementToPyExpressionTransformer().visitExpression(branch.condition, context),
                    body = IrElementToPyExpressionTransformer().visitExpression(branch.result, context),
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
    }

    override fun visitTypeOperator(expression: IrTypeOperatorCall, data: JsGenerationContext): expr {
        // TODO
        return when (expression.operator) {
            IrTypeOperator.REINTERPRET_CAST -> Call(
                func = Name(id = identifier(expression.typeOperand.asString().toValidPythonSymbol()), ctx = Load),
                args = listOf(visitExpression(expression.argument, data)),
                keywords = emptyList(),
            )
            else -> Name(id = identifier("visitTypeOperator ${expression.operator}".toValidPythonSymbol()), ctx = Load)
        }
    }

    override fun visitDynamicMemberExpression(expression: IrDynamicMemberExpression, data: JsGenerationContext): expr {
        // TODO
        return Call(
            func = Name(id = identifier(expression.memberName.toValidPythonSymbol()), ctx = Load),
            args = listOf(visitExpression(expression.receiver, data)),
            keywords = emptyList(),
        )
    }

    override fun visitDynamicOperatorExpression(expression: IrDynamicOperatorExpression, data: JsGenerationContext): expr {
        // TODO
        return Call(
            func = Name(id = identifier(expression.operator.toString().toValidPythonSymbol()), ctx = Load),
            args = listOf(visitExpression(expression.receiver, data)) + expression.arguments.map { visitExpression(it, data) },
            keywords = emptyList(),
        )
    }

    override fun visitComposite(expression: IrComposite, data: JsGenerationContext): expr {
        // TODO
        return Name(id = identifier("visitComposite-inToPyExpressionTransformer $expression".toValidPythonSymbol()), ctx = Load)
    }

    override fun visitRawFunctionReference(expression: IrRawFunctionReference, data: JsGenerationContext): expr {
        return Name(id = identifier(expression.symbol.owner.name.asString().toValidPythonSymbol()), ctx = Load)
    }
}
