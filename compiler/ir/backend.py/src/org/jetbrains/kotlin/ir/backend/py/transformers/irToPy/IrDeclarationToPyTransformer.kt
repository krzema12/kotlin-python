/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.ir.backend.py.transformers.irToPy

import generated.Python.*
import org.jetbrains.kotlin.ir.backend.py.utils.JsGenerationContext
import org.jetbrains.kotlin.ir.declarations.*

@Suppress("PARAMETER_NAME_CHANGED_ON_OVERRIDE")
class IrDeclarationToPyTransformer : BaseIrElementToPyNodeTransformer<List<stmt>, JsGenerationContext> {

    override fun visitSimpleFunction(declaration: IrSimpleFunction, context: JsGenerationContext): List<stmt> {
        require(!declaration.isExpect)
        return declaration.accept(IrFunctionToPyTransformer(), context).let(::listOf)
    }

    override fun visitConstructor(declaration: IrConstructor, context: JsGenerationContext): List<stmt> {
        // TODO
        return declaration.accept(IrFunctionToPyTransformer(), context).let(::listOf)
    }

    override fun visitClass(declaration: IrClass, context: JsGenerationContext): List<stmt> {
        return declaration.toPythonStatement(context)
    }

    override fun visitErrorDeclaration(declaration: IrErrorDeclaration, data: JsGenerationContext): List<stmt> {
        // TODO
        return Expr(value = Name(id = identifier("visitErrorDeclaration $declaration".toValidPythonSymbol()), ctx = Load)).let(::listOf)
    }

    override fun visitField(declaration: IrField, context: JsGenerationContext): List<stmt> {
        return Assign(
            targets = listOf(Name(id = identifier(declaration.symbol.owner.name.asString().toValidPythonSymbol()), ctx = Store)),
            value = Constant(value = constant("None"), kind = null),  // todo: move the field to the bottom of the file and use actual initializer
            type_comment = null,
        ).let(::listOf)
    }

    override fun visitVariable(declaration: IrVariable, context: JsGenerationContext): List<stmt> {
        // TODO
        return Expr(value = Name(id = identifier("visitVariable_irDeclarationToPyTransformer $declaration".toValidPythonSymbol()), ctx = Load)).let(::listOf)
    }

    override fun visitScript(irScript: IrScript, context: JsGenerationContext): List<stmt> {
        // TODO
        return Expr(value = Name(id = identifier("visitScript $irScript".toValidPythonSymbol()), ctx = Load)).let(::listOf)
    }
}
