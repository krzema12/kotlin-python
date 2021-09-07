/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.ir.backend.py.transformers.irToPy

import generated.Python.*
import org.jetbrains.kotlin.ir.IrStatement
import org.jetbrains.kotlin.ir.backend.py.utils.JsGenerationContext
import org.jetbrains.kotlin.ir.declarations.IrFunction
import org.jetbrains.kotlin.ir.declarations.IrVariable
import org.jetbrains.kotlin.ir.expressions.*
import org.jetbrains.kotlin.ir.types.isAny
import org.jetbrains.kotlin.ir.util.constructedClassType

private fun List<IrStatement>.translate(context: JsGenerationContext): List<stmt> {
    val globals = this
        .filterIsInstance<IrSetField>()
        .filter { it.symbol.owner.isStatic }
        .map { it.symbol.owner.name.asString().toValidPythonSymbol().let(::identifier) }
        .let { globals ->
            when (globals.isEmpty()) {
                true -> emptyList()
                else -> Global(globals).let(::listOf)
            }
        }
    val body = this.flatMap { it.accept(IrElementToPyStatementTransformer(), context) }

    return globals + body
}

@Suppress("PARAMETER_NAME_CHANGED_ON_OVERRIDE")
class IrElementToPyStatementTransformer : BaseIrElementToPyNodeTransformer<List<stmt>, JsGenerationContext> {

    override fun visitFunction(declaration: IrFunction, data: JsGenerationContext): List<stmt> {
        // TODO
        return listOf(Expr(value = Name(id = identifier("visitFunction $declaration".toValidPythonSymbol()), ctx = Load)))
    }

    override fun visitBlockBody(body: IrBlockBody, context: JsGenerationContext): List<stmt> {
        return body.statements.translate(context)
    }

    override fun visitBlock(expression: IrBlock, context: JsGenerationContext): List<stmt> {
        return expression.statements.translate(context)
    }

    override fun visitComposite(expression: IrComposite, context: JsGenerationContext): List<stmt> {
        return expression.statements.translate(context)
    }

    override fun visitExpression(expression: IrExpression, context: JsGenerationContext): List<stmt> {
        return when (expression) {
            is IrBlock -> visitBlock(expression, context)
            is IrReturn -> visitReturn(expression, context)
            is IrComposite -> visitComposite(expression, context)
            is IrBreak -> visitBreak(expression, context)
            is IrDoWhileLoop -> visitDoWhileLoop(expression, context)
            is IrContinue -> visitContinue(expression, context)
            is IrConstructorCall -> visitConstructorCall(expression, context)
            is IrThrow -> visitThrow(expression, context)
            is IrSetValue -> visitSetValue(expression, context)
            else -> listOf(Expr(value = Name(id = identifier("visitExpression-other--inToPyStatementTransformer $expression".toValidPythonSymbol()), ctx = Load)))
        }
    }

    override fun visitBreak(jump: IrBreak, context: JsGenerationContext): List<stmt> {
        // todo (support label)
        return listOf(Break)
    }

    override fun visitContinue(jump: IrContinue, context: JsGenerationContext): List<stmt> {
        // todo (support label)
        return listOf(Continue)
    }

    override fun visitSetField(expression: IrSetField, context: JsGenerationContext): List<stmt> {
        // TODO
        val receiverAsExpressions = expression.receiver?.accept(IrElementToPyExpressionTransformer(), context)
        return listOf(
            Assign(
                targets = if (receiverAsExpressions != null) {
                    listOf(Attribute(value = receiverAsExpressions, attr = identifier(expression.symbol.owner.name.asString().toValidPythonSymbol()), ctx = Store))
                } else {
                    listOf(Name(id = identifier(expression.symbol.owner.name.identifier.toValidPythonSymbol()), ctx = Store))
                },
                value = IrElementToPyExpressionTransformer().visitExpression(expression.value, context),
                type_comment = null,
            )
        )
    }

    override fun visitSetValue(expression: IrSetValue, context: JsGenerationContext): List<stmt> {
        return listOf(
            Assign(
                targets = listOf(Name(id = identifier(expression.symbol.owner.name.identifier.toValidPythonSymbol()), ctx = Store)),
                value = IrElementToPyExpressionTransformer().visitExpression(expression.value, context),
                type_comment = null,
            )
        )
    }

    override fun visitReturn(expression: IrReturn, context: JsGenerationContext): List<stmt> {
        return listOf(Return(
            value = IrElementToPyExpressionTransformer().visitExpression(expression.value, context),
        ))
    }

    override fun visitThrow(expression: IrThrow, context: JsGenerationContext): List<stmt> {
        return listOf(Raise(
            exc = IrElementToPyExpressionTransformer().visitExpression(expression.value, context),
            cause = null,
        ))
    }

    override fun visitVariable(declaration: IrVariable, context: JsGenerationContext): List<stmt> {
        // TODO
        return declaration.initializer?.let { initializer ->
            Assign(
                targets = listOf(Name(id = identifier(declaration.name.identifier.toValidPythonSymbol()), ctx = Store)),
                value = IrElementToPyExpressionTransformer().visitExpression(initializer, context),
                type_comment = null,
            )
        }
            ?.let(::listOf)
            ?: emptyList()
    }

    override fun visitDelegatingConstructorCall(expression: IrDelegatingConstructorCall, context: JsGenerationContext): List<stmt> {
        // TODO
        if (expression.symbol.owner.constructedClassType.isAny()) {
            return listOf()
        }
        return expression.accept(IrElementToPyExpressionTransformer(), context).makeStmt().let(::listOf)
    }

    override fun visitCall(expression: IrCall, data: JsGenerationContext): List<stmt> {
        // TODO
        return IrElementToPyExpressionTransformer().visitCall(expression, data).makeStmt().let(::listOf)
    }

    override fun visitConstructorCall(expression: IrConstructorCall, context: JsGenerationContext): List<stmt> {
        return IrElementToPyExpressionTransformer().visitConstructorCall(expression, context).makeStmt().let(::listOf)
    }

    override fun visitInstanceInitializerCall(expression: IrInstanceInitializerCall, context: JsGenerationContext): List<stmt> {
        // TODO
        return listOf(Expr(value = Name(id = identifier("visitInstanceInitializerCall $expression".toValidPythonSymbol()), ctx = Load)))
    }

    override fun visitTry(aTry: IrTry, context: JsGenerationContext): List<stmt> {
        // TODO
        return listOf(Expr(value = Name(id = identifier("visitTry $aTry".toValidPythonSymbol()), ctx = Load)))
    }

    override fun visitWhen(expression: IrWhen, context: JsGenerationContext): List<stmt> {
        return listOf(
            expression
                .branches
                .map { branch ->
                    If(
                        test = IrElementToPyExpressionTransformer().visitExpression(branch.condition, context),
                        body = IrElementToPyStatementTransformer().visitExpression(branch.result, context),
                        orelse = emptyList(),
                    )
                }
                .reduceRight { iff, acc ->
                    val accTest = acc.test

                    if (accTest is Constant && accTest.value.value == "True") {
                        // optimization
                        If(
                            test = iff.test,
                            body = iff.body,
                            orelse = acc.body,
                        )
                    } else {
                        If(
                            test = iff.test,
                            body = iff.body,
                            orelse = listOf(acc),
                        )
                    }
                }
        )
    }

    override fun visitWhileLoop(loop: IrWhileLoop, context: JsGenerationContext): List<stmt> {
        // TODO
        return listOf(While(
            test = IrElementToPyExpressionTransformer().visitExpression(loop.condition, context),
            body = loop.body?.accept(this, context) ?: emptyList(),
            orelse = emptyList(),
        ))
    }

    override fun visitDoWhileLoop(loop: IrDoWhileLoop, context: JsGenerationContext): List<stmt> {
        // transform like:
        //
        // while True:
        //     <body>
        //     if <condition>:
        //         break
        val body = loop.body?.accept(this, context).orEmpty()
        val condition = If(
            test = IrElementToPyExpressionTransformer().visitExpression(loop.condition, context),
            body = listOf(Break),
            orelse = emptyList(),
        )

        return While(
            test = Constant(value = constant("True"), kind = null),
            body = body + condition,
            orelse = emptyList(),
        )
            .let(::listOf)
    }
}
