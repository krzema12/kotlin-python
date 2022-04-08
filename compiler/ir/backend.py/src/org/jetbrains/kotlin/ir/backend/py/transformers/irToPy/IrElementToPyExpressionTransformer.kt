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
import org.jetbrains.kotlin.ir.types.*
import org.jetbrains.kotlin.ir.util.isEffectivelyExternal
import org.jetbrains.kotlin.ir.util.isFunctionTypeOrSubtype
import org.jetbrains.kotlin.ir.util.parentAsClass
import org.jetbrains.kotlin.util.OperatorNameConventions

@Suppress("PARAMETER_NAME_CHANGED_ON_OVERRIDE")
class IrElementToPyExpressionTransformer : BaseIrElementToPyNodeTransformer<expr, PyGenerationContext> {

    override fun visitVararg(expression: IrVararg, context: PyGenerationContext): expr {
        return Tuple(elts = expression.elements.map { it.accept(this, context) }, ctx = Load)
    }

    override fun visitExpression(expression: IrExpression, data: PyGenerationContext): expr {
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
            is IrVararg -> visitVararg(expression, data)
            is IrDynamicOperatorExpression -> visitDynamicOperatorExpression(expression, data)
            is IrDynamicMemberExpression -> visitDynamicMemberExpression(expression, data)
            is IrStringConcatenation -> visitStringConcatenation(expression, data)
            is IrFunctionExpression -> visitFunctionExpression(expression, data)
            is IrRawFunctionReference -> visitRawFunctionReference(expression, data)
            is IrFunctionReference -> visitFunctionReference(expression, data)
            else -> Name(id = identifier("visitExpression-other $expression".toValidPythonSymbol()), ctx = Load)
        }
    }

    override fun visitExpressionBody(body: IrExpressionBody, context: PyGenerationContext): expr = body.expression.accept(this, context)

    override fun visitFunctionExpression(expression: IrFunctionExpression, context: PyGenerationContext): expr {
        // TODO: create lowering: if there is one statement, use IrExpressionBody, otherwise, create a _no_name_provided_function_ and call it.
        //       for now, the code doesn't support some cases

        val parameters = listOfNotNull(expression.function.dispatchReceiverParameter, expression.function.extensionReceiverParameter) +
                expression.function.valueParameters
        val args = argumentsImpl(
            args = parameters.map { argImpl(identifier(it.name.asString().toValidPythonSymbol()), null, null) },
            posonlyargs = emptyList(),
            vararg = null,
            kwonlyargs = emptyList(),
            kw_defaults = emptyList(),
            kwarg = null,
            defaults = emptyList(),
        )

        return Lambda(
            args = args,
            body = when (val body = expression.function.body) {
                is IrBlockBody -> {
                    val statements = IrElementToPyStatementTransformer().visitBlockBody(body, context)
                    when (val single = statements.singleOrNull() as? Return) {
                        null -> {
                            val complexFunctionName = identifier("complexFunction x${statements.size} ${statements.map { it::class.simpleName }} ${context.extraStatementsSize}".toValidPythonSymbol())

                            val complexFunction = FunctionDef(
                                name = complexFunctionName,
                                args = args,
                                body = statements,
                                decorator_list = emptyList(),
                                returns = null,
                                type_comment = null,
                            )

                            context.addStatement(complexFunction)

                            return Name(id = complexFunctionName, ctx = Load)
                        }
                        else -> single.value ?: Name(id = identifier("visitExpressionFunctionBodyStatementsReturn null".toValidPythonSymbol()), ctx = Load)
                    }
                }
                else -> Name(id = identifier("visitExpressionFunctionBody $body".toValidPythonSymbol()), ctx = Load)
            }
        )
    }

    override fun <T> visitConst(expression: IrConst<T>, context: PyGenerationContext): expr {
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

    override fun visitStringConcatenation(expression: IrStringConcatenation, context: PyGenerationContext): expr {
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

    override fun visitGetField(expression: IrGetField, context: PyGenerationContext): expr {
        // TODO
        val field = expression.symbol.owner
        val receiverExpression = expression.receiver?.accept(this, context)

        return if (receiverExpression != null) {
            Attribute(value = receiverExpression, attr = identifier(field.name.asString().toValidPythonSymbol()), ctx = Store)
        } else {
            Name(id = identifier(context.getNameForField(field).ident.toValidPythonSymbol()), ctx = Load)
        }
    }

    override fun visitGetValue(expression: IrGetValue, context: PyGenerationContext): expr {
        // TODO
        return when (val owner = expression.symbol.owner) {
            is IrVariable -> Name(id = identifier(context.getNameForValueDeclaration(owner).ident.toValidPythonSymbol()), ctx = Load)
            is IrValueParameter -> Name(id = identifier(owner.name.asString().toValidPythonSymbol().toPythonSpecific()), ctx = Load)
            else -> Name(id = identifier("visitGetValue_other $owner".toValidPythonSymbol()), ctx = Load)
        }
    }

    override fun visitGetObjectValue(expression: IrGetObjectValue, context: PyGenerationContext): expr {
        val field = expression.symbol.owner
        return Name(id = identifier(field.name.asString().toValidPythonSymbol()), ctx = Load)
    }

    override fun visitSetField(expression: IrSetField, context: PyGenerationContext): expr {
        // TODO
        return Name(id = identifier("visitSetField_expression $expression".toValidPythonSymbol()), ctx = Load)
    }

    override fun visitSetValue(expression: IrSetValue, context: PyGenerationContext): expr {
        // TODO
        return Name(id = identifier("visitSetValue-inToPyExpressionTransformer $expression".toValidPythonSymbol()), ctx = Load)
    }

    override fun visitDelegatingConstructorCall(expression: IrDelegatingConstructorCall, context: PyGenerationContext): expr {
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

    override fun visitConstructorCall(expression: IrConstructorCall, context: PyGenerationContext): expr {
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

    override fun visitCall(expression: IrCall, context: PyGenerationContext): expr {
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

    override fun visitWhen(expression: IrWhen, context: PyGenerationContext): expr {
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

    override fun visitTypeOperator(expression: IrTypeOperatorCall, data: PyGenerationContext): expr {
        // TODO: take a look how JS performs here: much easier, looks like in most cases call is just omitted and just the argument is used
        val type = expression.typeOperand
        val funcName = when {
            type.isDouble() || type.isFloat() -> "float"
            type.isString() -> "str"
            type.isAny() || type.isNullableAny() -> ""  // todo: get rid of this hack
            else -> type.asString().toValidPythonSymbol()
        }

        return when (expression.operator) {
            IrTypeOperator.REINTERPRET_CAST -> Call(
                func = Name(id = identifier(funcName), ctx = Load),
                args = listOf(visitExpression(expression.argument, data)),
                keywords = emptyList(),
            )
            else -> Name(id = identifier("visitTypeOperator $funcName".toValidPythonSymbol()), ctx = Load)
        }
    }

    override fun visitDynamicMemberExpression(expression: IrDynamicMemberExpression, data: PyGenerationContext): expr {
        return Attribute(
            expression.receiver.accept(this, data),
            identifier(expression.memberName.toValidPythonSymbol()),
            Load,
        )
    }

    override fun visitDynamicOperatorExpression(expression: IrDynamicOperatorExpression, data: PyGenerationContext): expr {
        fun prefixOperation(op: unaryop, expression: IrDynamicOperatorExpression, data: PyGenerationContext) =
            UnaryOp(op, expression.receiver.accept(this, data))

        fun binaryOperation(op: operator, expression: IrDynamicOperatorExpression, data: PyGenerationContext) =
            BinOp(expression.left.accept(this, data), op, expression.right.accept(this, data))

        fun binaryOperation(op: cmpop, expression: IrDynamicOperatorExpression, data: PyGenerationContext) =
            Compare(expression.left.accept(this, data), listOf(op), listOf(expression.right.accept(this, data)))

        fun binaryOperation(op: boolop, expression: IrDynamicOperatorExpression, data: PyGenerationContext) =
            BoolOp(op, listOf(expression.left.accept(this, data), expression.right.accept(this, data)))

        return when (expression.operator) {
            IrDynamicOperator.UNARY_PLUS -> prefixOperation(UAdd, expression, data)
            IrDynamicOperator.UNARY_MINUS -> prefixOperation(USub, expression, data)

            IrDynamicOperator.EXCL -> prefixOperation(Not, expression, data)

            IrDynamicOperator.BINARY_PLUS -> binaryOperation(Add, expression, data)
            IrDynamicOperator.BINARY_MINUS -> binaryOperation(Sub, expression, data)
            IrDynamicOperator.MUL -> binaryOperation(Mult, expression, data)
            IrDynamicOperator.DIV -> binaryOperation(Div, expression, data)
            IrDynamicOperator.MOD -> binaryOperation(Mod, expression, data)

            IrDynamicOperator.GT -> binaryOperation(Gt, expression, data)
            IrDynamicOperator.LT -> binaryOperation(Lt, expression, data)
            IrDynamicOperator.GE -> binaryOperation(GtE, expression, data)
            IrDynamicOperator.LE -> binaryOperation(LtE, expression, data)

            IrDynamicOperator.EQEQ -> binaryOperation(Eq, expression, data)
            IrDynamicOperator.EXCLEQ -> binaryOperation(NotEq, expression, data)

            IrDynamicOperator.EQEQEQ -> binaryOperation(Is, expression, data)
            IrDynamicOperator.EXCLEQEQ -> binaryOperation(IsNot, expression, data)

            IrDynamicOperator.ANDAND -> binaryOperation(And, expression, data)
            IrDynamicOperator.OROR -> binaryOperation(Or, expression, data)

            IrDynamicOperator.ARRAY_ACCESS -> Subscript(
                value = expression.left.accept(this, data),
                slice = expression.right.accept(this, data),
                ctx = Load,
            )

            IrDynamicOperator.INVOKE -> Call(
                func = expression.receiver.accept(this, data),
                args = expression.arguments.map { it.accept(this, data) },
                keywords = emptyList(),
            )

            else -> Call(
                func = Name(id = identifier("Unexpected operator ${expression.operator}".toValidPythonSymbol()), ctx = Load),
                args = listOf(visitExpression(expression.receiver, data)) + expression.arguments.map { visitExpression(it, data) },
                keywords = emptyList(),
            )
        }
    }

    override fun visitComposite(expression: IrComposite, data: PyGenerationContext): expr {
        // TODO
        return Name(id = identifier("visitComposite-inToPyExpressionTransformer $expression".toValidPythonSymbol()), ctx = Load)
    }

    override fun visitRawFunctionReference(expression: IrRawFunctionReference, data: PyGenerationContext): expr {
        return Name(id = identifier(expression.symbol.owner.name.asString().toValidPythonSymbol()), ctx = Load)
    }

    override fun visitFunctionReference(expression: IrFunctionReference, data: PyGenerationContext): expr {
        return Name(id = identifier(expression.referencedName.asString().toValidPythonSymbol()), ctx = Load)
    }
}
