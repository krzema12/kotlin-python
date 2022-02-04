/*
 * Copyright 2010-2018 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.ir.backend.py.utils

import org.jetbrains.kotlin.backend.common.ir.isMethodOfAny
import org.jetbrains.kotlin.ir.IrElement
import org.jetbrains.kotlin.ir.UNDEFINED_OFFSET
import org.jetbrains.kotlin.ir.backend.py.PyIrBackendContext
import org.jetbrains.kotlin.ir.backend.py.PyLoweredDeclarationOrigin
import org.jetbrains.kotlin.ir.backend.py.ir.JsIrBuilder
import org.jetbrains.kotlin.ir.declarations.*
import org.jetbrains.kotlin.ir.expressions.*
import org.jetbrains.kotlin.ir.expressions.impl.IrCallImpl
import org.jetbrains.kotlin.ir.expressions.impl.IrVarargImpl
import org.jetbrains.kotlin.ir.types.IrType
import org.jetbrains.kotlin.ir.types.isNullableAny
import org.jetbrains.kotlin.ir.util.isEffectivelyExternal
import org.jetbrains.kotlin.ir.util.isTopLevelDeclaration
import org.jetbrains.kotlin.name.Name

fun TODO(element: IrElement): Nothing = TODO(element::class.java.simpleName + " is not supported yet here")

@Suppress("UNUSED_PARAMETER")  // todo: ensure the parameter is not needed and remove
fun IrFunction.hasStableJsName(context: PyIrBackendContext?): Boolean {
    if (
        origin == PyLoweredDeclarationOrigin.BRIDGE_WITH_STABLE_NAME ||
        (this as? IrSimpleFunction)?.isMethodOfAny() == true // Handle names for special functions
    ) {
        return true
    }

    if (
        origin == PyLoweredDeclarationOrigin.JS_SHADOWED_EXPORT ||
        origin == IrDeclarationOrigin.FUNCTION_FOR_DEFAULT_PARAMETER ||
        origin == PyLoweredDeclarationOrigin.BRIDGE_WITHOUT_STABLE_NAME
    ) {
        return false
    }

    val namedOrMissingGetter = when (this) {
        is IrSimpleFunction -> {
            val owner = correspondingPropertySymbol?.owner
            if (owner == null) {
                true
            } else {
                owner.getter?.getJsName() != null
            }
        }
        else -> true
    }

    return (isEffectivelyExternal() || getJsName() != null) && namedOrMissingGetter
}

fun IrFunction.isEqualsInheritedFromAny() =
    name == Name.identifier("equals") &&
            dispatchReceiverParameter != null &&
            valueParameters.size == 1 &&
            valueParameters[0].type.isNullableAny()

fun IrDeclaration.hasStaticDispatch() = when (this) {
    is IrSimpleFunction -> dispatchReceiverParameter == null
    is IrProperty -> isTopLevelDeclaration
    is IrField -> isStatic
    else -> true
}

fun List<IrExpression>.toJsArrayLiteral(context: PyIrBackendContext, arrayType: IrType, elementType: IrType): IrExpression {
    val irVararg = IrVarargImpl(UNDEFINED_OFFSET, UNDEFINED_OFFSET, arrayType, elementType, this)

    return IrCallImpl(
        UNDEFINED_OFFSET, UNDEFINED_OFFSET, arrayType,
        context.intrinsics.arrayLiteral,
        valueArgumentsCount = 1,
        typeArgumentsCount = 0
    ).apply {
        putValueArgument(0, irVararg)
    }
}

val IrValueDeclaration.isDispatchReceiver: Boolean
    get() {
        val parent = this.parent
        if (parent is IrClass)
            return true
        if (parent is IrFunction && parent.dispatchReceiverParameter == this)
            return true
        return false
    }

fun IrBody.prependFunctionCall(
    call: IrCall
) {
    when (this) {
        is IrExpressionBody -> {
            expression = JsIrBuilder.buildComposite(
                type = expression.type,
                statements = listOf(
                    call,
                    expression
                )
            )
        }
        is IrBlockBody -> {
            statements.add(
                0,
                call
            )
        }
    }
}