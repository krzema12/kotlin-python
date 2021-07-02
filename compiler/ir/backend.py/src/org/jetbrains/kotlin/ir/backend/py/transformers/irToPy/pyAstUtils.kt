/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.ir.backend.py.transformers.irToPy

import generated.Python.*
import org.jetbrains.kotlin.ir.backend.py.utils.JsGenerationContext
import org.jetbrains.kotlin.ir.declarations.IrConstructor
import org.jetbrains.kotlin.ir.declarations.IrFunction
import org.jetbrains.kotlin.ir.expressions.IrMemberAccessExpression
import org.jetbrains.kotlin.ir.util.isVararg

fun translateFunction(declaration: IrFunction, context: JsGenerationContext): FunctionDef {
    val isClassMethod = declaration.dispatchReceiverParameter != null
    val isConstructor = declaration is IrConstructor
    val body = declaration.body?.accept(IrElementToPyStatementTransformer(), context) ?: listOf(Pass)
    val args = declaration.valueParameters
        .filter { !it.isVararg }
        .map { valueParameter ->
            argImpl(
                arg = identifier(valueParameter.name.asString().toValidPythonSymbol()),
                annotation = null,
                type_comment = null,
            )
        }
    val selfArg = argImpl(
        arg = identifier("self"),
        annotation = null,
        type_comment = null,
    )

    return FunctionDef(
        name = identifier(if (isConstructor) "__init__" else declaration.name.asString().toValidPythonSymbol()),
        args = argumentsImpl(
            posonlyargs = emptyList(),
            args = if (isClassMethod || isConstructor) {
                listOf(selfArg) + args
            } else args,
            vararg = declaration.valueParameters.firstOrNull { it.isVararg }?.let {
                argImpl(
                    arg = identifier(it.name.asString().toValidPythonSymbol()),
                    annotation = null,
                    type_comment = null,
                )
            },
            kwonlyargs = emptyList(),
            kw_defaults = emptyList(),
            kwarg = null,
            defaults = emptyList(),
        ),
        body = body,
        decorator_list = emptyList(),
        returns = null,
        type_comment = null,
    )
}

fun translateCallArguments(expression: IrMemberAccessExpression<*>, context: JsGenerationContext, transformer: IrElementToPyExpressionTransformer): List<expr> {
    val size = expression.valueArgumentsCount

    val arguments = (0 until size).mapTo(ArrayList(size)) { index ->
        val argument = expression.getValueArgument(index)
        val result = argument?.accept(transformer, context)
        if (result == null) {
            emptyList()  // todo
//            if (context.staticContext.backendContext.es6mode) return@mapTo JsPrefixOperation(JsUnaryOperator.VOID, JsIntLiteral(2))
//
//            assert(expression is IrFunctionAccessExpression && expression.symbol.owner.isExternalOrInheritedFromExternal())
//            JsPrefixOperation(JsUnaryOperator.VOID, JsIntLiteral(1))
        } else
            result
    }

//    return if (expression.symbol.isSuspend) {
//        arguments + context.continuation
//    } else arguments
    return arguments.flatten()  // todo
}
