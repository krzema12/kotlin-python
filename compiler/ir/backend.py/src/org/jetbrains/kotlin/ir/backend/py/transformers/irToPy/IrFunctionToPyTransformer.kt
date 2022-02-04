/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.ir.backend.py.transformers.irToPy

import generated.Python.FunctionDef
import org.jetbrains.kotlin.ir.backend.py.utils.PyGenerationContext
import org.jetbrains.kotlin.ir.declarations.IrConstructor
import org.jetbrains.kotlin.ir.declarations.IrFunction
import org.jetbrains.kotlin.ir.declarations.IrSimpleFunction

@Suppress("PARAMETER_NAME_CHANGED_ON_OVERRIDE")
class IrFunctionToPyTransformer : BaseIrElementToPyNodeTransformer<FunctionDef, PyGenerationContext> {
    override fun visitSimpleFunction(declaration: IrSimpleFunction, context: PyGenerationContext): FunctionDef {
        val funcName = if (declaration.dispatchReceiverParameter == null) {
            if (declaration.parent is IrFunction) {
                context.getNameForValueDeclaration(declaration)
            } else {
                context.getNameForStaticFunction(declaration)
            }
        } else {
            context.getNameForMemberFunction(declaration)
        }
        return translateFunction(declaration, funcName, context)
    }

    override fun visitConstructor(declaration: IrConstructor, context: PyGenerationContext): FunctionDef {
        val funcName = context.getNameForConstructor(declaration)
        return translateFunction(declaration, funcName, context)
    }
}
