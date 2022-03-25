/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.ir.backend.py.transformers.irToPy

import generated.Python.*
import org.jetbrains.kotlin.ir.backend.py.utils.LocalNameGenerator
import org.jetbrains.kotlin.ir.backend.py.utils.NameScope
import org.jetbrains.kotlin.ir.backend.py.utils.PyGenerationContext
import org.jetbrains.kotlin.ir.declarations.*

@Suppress("PARAMETER_NAME_CHANGED_ON_OVERRIDE")
class IrDeclarationToPyTransformer : BaseIrElementToPyNodeTransformer<List<stmt>, PyGenerationContext> {

    override fun visitSimpleFunction(declaration: IrSimpleFunction, context: PyGenerationContext): List<stmt> {
        require(!declaration.isExpect)
        return declaration.accept(IrFunctionToPyTransformer(), context).let(::listOf)
    }

    override fun visitConstructor(declaration: IrConstructor, context: PyGenerationContext): List<stmt> {
        // TODO
        return declaration.accept(IrFunctionToPyTransformer(), context).let(::listOf)
    }

    override fun visitClass(declaration: IrClass, context: PyGenerationContext): List<stmt> {
        return declaration.toPythonStatement(context.newDeclaration(localNames = LocalNameGenerator(NameScope.EmptyScope)))  // todo: use proper (parent/global) name scope
    }

    override fun visitErrorDeclaration(declaration: IrErrorDeclaration, data: PyGenerationContext): List<stmt> {
        // TODO
        return Expr(value = Name(id = identifier("visitErrorDeclaration $declaration".toValidPythonSymbol()), ctx = Load)).let(::listOf)
    }

    override fun visitField(declaration: IrField, context: PyGenerationContext): List<stmt> {
        return Assign(
            targets = listOf(Name(id = identifier(declaration.symbol.owner.name.asString().toValidPythonSymbol()), ctx = Store)),
            value = Constant(value = constant("None"), kind = null),  // todo: move the field to the bottom of the file and use actual initializer
            type_comment = null,
        ).let(::listOf)
    }

    override fun visitVariable(declaration: IrVariable, context: PyGenerationContext): List<stmt> {
        // TODO
        return Expr(value = Name(id = identifier("visitVariable_irDeclarationToPyTransformer $declaration".toValidPythonSymbol()), ctx = Load)).let(::listOf)
    }

    override fun visitScript(irScript: IrScript, context: PyGenerationContext): List<stmt> {
        // TODO
        return Expr(value = Name(id = identifier("visitScript $irScript".toValidPythonSymbol()), ctx = Load)).let(::listOf)
    }
}
