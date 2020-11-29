/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.ir.backend.js.transformers.irToPy

import generated.Python.*
import org.jetbrains.kotlin.ir.backend.js.utils.JsGenerationContext
import org.jetbrains.kotlin.ir.declarations.IrFunction
import org.jetbrains.kotlin.ir.declarations.IrVariable
import org.jetbrains.kotlin.ir.expressions.*

@Suppress("PARAMETER_NAME_CHANGED_ON_OVERRIDE")
class IrElementToPyStatementTransformer : BaseIrElementToPyNodeTransformer<List<stmt>, JsGenerationContext> {

    override fun visitFunction(declaration: IrFunction, data: JsGenerationContext): List<stmt> {
        // TODO
        return listOf(Expr(value = Name(id = identifier("visitFunction $declaration".toValidPythonSymbol()), ctx = Load)))
    }

    override fun visitBlockBody(body: IrBlockBody, context: JsGenerationContext): List<stmt> {
        // TODO
        return body.statements.flatMap { it.accept(this, context) }
    }

    override fun visitBlock(expression: IrBlock, context: JsGenerationContext): List<stmt> {
        // TODO
        return expression.statements.flatMap {
            it.accept(this, context)
        }
    }

    override fun visitComposite(expression: IrComposite, context: JsGenerationContext): List<stmt> {
        // TODO
        return expression.statements.flatMap {
            it.accept(this, context)
        }
    }

    override fun visitExpression(expression: IrExpression, context: JsGenerationContext): List<stmt> {
        return when (expression) {
            is IrBlock -> visitBlock(expression, context)
            else -> listOf(Expr(value = Name(id = identifier("visitExpression-other--inToPyStatementTransformer $expression".toValidPythonSymbol()), ctx = Load)))
        }
    }

    override fun visitBreak(jump: IrBreak, context: JsGenerationContext): List<stmt> {
        // TODO
        return listOf(Expr(value = Name(id = identifier("visitBreak $jump".toValidPythonSymbol()), ctx = Load)))
    }

    override fun visitContinue(jump: IrContinue, context: JsGenerationContext): List<stmt> {
        // TODO
        return listOf(Expr(value = Name(id = identifier("visitContinue $jump".toValidPythonSymbol()), ctx = Load)))
    }

    override fun visitSetField(expression: IrSetField, context: JsGenerationContext): List<stmt> {
        // TODO
        val receiverAsExpressions = expression.receiver?.accept(IrElementToPyExpressionTransformer(), context)?.get(0)
        return listOf(
            Assign(
                targets = if (receiverAsExpressions != null) {
                    listOf(Attribute(value = receiverAsExpressions, attr = identifier(expression.symbol.owner.name.asString().toValidPythonSymbol()), ctx = Store))
                } else {
                    listOf(Name(id = identifier(expression.symbol.owner.name.identifier.toValidPythonSymbol()), ctx = Store))
                },
                value = IrElementToPyExpressionTransformer().visitExpression(expression.value, context).first(),
                type_comment = null,
            )
        )
    }

    override fun visitSetValue(expression: IrSetValue, context: JsGenerationContext): List<stmt> {
        return listOf(
            Assign(
                targets = listOf(Name(id = identifier(expression.symbol.owner.name.identifier.toValidPythonSymbol()), ctx = Store)),
                value = IrElementToPyExpressionTransformer().visitExpression(expression.value, context).first(),
                type_comment = null,
            )
        )
    }

    override fun visitReturn(expression: IrReturn, context: JsGenerationContext): List<stmt> {
        return listOf(Return(
            value = IrElementToPyExpressionTransformer().visitExpression(expression.value, context).first(),
        ))
    }

    override fun visitThrow(expression: IrThrow, context: JsGenerationContext): List<stmt> {
        // TODO
        return listOf(Expr(value = Name(id = identifier("visitThrow $expression".toValidPythonSymbol()), ctx = Load)))
    }

    override fun visitVariable(declaration: IrVariable, context: JsGenerationContext): List<stmt> {
        // TODO
        return listOf(declaration.initializer?.let { initializer ->
            Assign(
                targets = listOf(Name(id = identifier(declaration.name.identifier.toValidPythonSymbol()), ctx = Store)),
                value = IrElementToPyExpressionTransformer().visitExpression(initializer, context).first(),
                type_comment = null,
            )
        } ?: Expr(
            value = Name(
                id = identifier(declaration.name.identifier.toValidPythonSymbol()),
                ctx = Load,
            ),
        ))
    }

    override fun visitDelegatingConstructorCall(expression: IrDelegatingConstructorCall, context: JsGenerationContext): List<stmt> {
        // TODO
        return listOf(Assign(
            targets = listOf(Name(id = identifier("visitDelegatingCOnstructorCall $expression".toValidPythonSymbol()), ctx = Store)),
            value = Constant(value = constant("0"), kind = null),
            type_comment = null,
        ))
    }

    override fun visitCall(expression: IrCall, data: JsGenerationContext): List<stmt> {
        // TODO
        return IrElementToPyExpressionTransformer().visitCall(expression, data)
            .map { Expr(value = it) }
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
        return expression.branches.map { branch ->
            If(
                test = IrElementToPyExpressionTransformer().visitExpression(branch.condition, context).first(),
                body = IrElementToPyStatementTransformer().visitExpression(branch.result, context),
                orelse = emptyList(), // TODO
            )
        }
        // TODO
//        return listOf(Expr(value = Name(id = identifier("visitWhen-inToPyStatementTransformer $expression"), ctx = Load)))
    }

    override fun visitWhileLoop(loop: IrWhileLoop, context: JsGenerationContext): List<stmt> {
        // TODO
        return listOf(While(
            test = IrElementToPyExpressionTransformer().visitExpression(loop.condition, context).first(),
            body = loop.body?.accept(this, context) ?: emptyList(),
            orelse = emptyList(),
        ))
    }

    override fun visitDoWhileLoop(loop: IrDoWhileLoop, context: JsGenerationContext): List<stmt> {
        // TODO
        return listOf(Expr(value = Name(id = identifier("visitDoWhileLoop $loop".toValidPythonSymbol()), ctx = Load)))
    }
}
