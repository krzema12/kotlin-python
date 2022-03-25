/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.ir.backend.py.transformers.irToPy

import generated.Python.*
import org.jetbrains.kotlin.ir.backend.py.utils.LocalNameGenerator
import org.jetbrains.kotlin.ir.backend.py.utils.PyGenerationContext
import org.jetbrains.kotlin.ir.declarations.IrConstructor
import org.jetbrains.kotlin.ir.declarations.IrFunction
import org.jetbrains.kotlin.ir.expressions.IrMemberAccessExpression
import org.jetbrains.kotlin.ir.expressions.IrVararg
import org.jetbrains.kotlin.ir.util.isVararg
import org.jetbrains.kotlin.ir.util.parentClassOrNull
import org.jetbrains.kotlin.ir.visitors.acceptChildrenVoid
import org.jetbrains.kotlin.ir.visitors.acceptVoid
import org.jetbrains.kotlin.js.backend.ast.JsName

fun expr.makeStmt(): stmt = Expr(value = this)

fun translateFunction(declaration: IrFunction, funcName: JsName, context: PyGenerationContext): FunctionDef {
    val localNameGenerator = LocalNameGenerator(context.localNames.variableNames).also {
        declaration.acceptChildrenVoid(it)
        declaration.parentClassOrNull?.thisReceiver?.acceptVoid(it)
    }
    val functionContext = context.newDeclaration(declaration, localNameGenerator)

    val isClassMethod = declaration.dispatchReceiverParameter != null
    val isConstructor = declaration is IrConstructor
    val extensionReceiverParameter = declaration.extensionReceiverParameter
    val body = declaration.body?.accept(IrElementToPyStatementTransformer(), functionContext) ?: listOf(Pass)
    val args = declaration.valueParameters
        .filter { !it.isVararg }
        .map { valueParameter ->
            argImpl(
                arg = identifier(valueParameter.name.asString().toValidPythonSymbol()),
                annotation = null,
                type_comment = null,
            )
        }

    val selfArg = when {
        isClassMethod || isConstructor -> "self"
        extensionReceiverParameter != null -> extensionReceiverParameter.name.asString().toValidPythonSymbol()
        else -> null
    }?.let {
        val corrected = when (it) {
            "_this_" -> "self"
            else -> it
        }

        argImpl(
            arg = identifier(corrected),
            annotation = null,
            type_comment = null,
        )
    }

    return FunctionDef(
        name = identifier(if (isConstructor) "__init__" else funcName.ident.toValidPythonSymbol()),
        args = argumentsImpl(
            posonlyargs = emptyList(),
            args = listOfNotNull(selfArg) + args,
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

fun translateCallArguments(expression: IrMemberAccessExpression<*>, context: PyGenerationContext, transformer: IrElementToPyExpressionTransformer): List<expr> {
    val size = expression.valueArgumentsCount

    val arguments = (0 until size).mapTo(ArrayList(size)) { index ->
        val argument = expression.getValueArgument(index)
        val result = argument?.accept(transformer, context)
        if (result == null) {
            Name(id = identifier("translateCallArguments $index".toValidPythonSymbol()), ctx = Load)  // todo
        } else if (argument is IrVararg) {
            Starred(value = result, ctx = Load)  // todo: it's not pretty to have *(1, 2, 3) -- we can flatten vararg here
        } else {
            result
        }
    }

    return arguments  // todo
}
