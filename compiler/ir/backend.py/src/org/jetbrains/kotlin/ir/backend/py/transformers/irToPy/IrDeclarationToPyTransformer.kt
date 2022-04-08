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
        val fieldName = context.getNameForField(declaration).ident.toValidPythonSymbol()

        if (
            declaration.initializer != null &&
            // todo: the following lines omit initializing of known stdlib fields that are unsupported yet. need to remove them eventually
            declaration.symbol.owner.name.asString().toValidPythonSymbol() !in setOf(
                "UNDEFINED_RESULT",
                "output",
                "INV_2_26",
                "INV_2_53",
                "buf",
                "bufFloat64",
                "bufFloat32",
                "bufInt32",
                "lowIndex",
                "highIndex",
                "propertyRefClassMetadataCache",
                "NAME_TO_ADAPTER",
            )
        ) {
            val initializer = declaration.initializer!!.accept(IrElementToPyExpressionTransformer(), context)
            context.staticContext.initializerBlock += Assign(
                targets = listOf(Name(id = identifier(fieldName), ctx = Store)),
                value = initializer,
                type_comment = null,
            )
        }

        return Assign(
            targets = listOf(Name(id = identifier(fieldName), ctx = Store)),
            value = Constant(value = constant("None"), kind = null),
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
