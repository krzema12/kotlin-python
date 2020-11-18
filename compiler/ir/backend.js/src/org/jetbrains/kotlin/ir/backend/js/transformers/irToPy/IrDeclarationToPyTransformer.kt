/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.ir.backend.js.transformers.irToPy

import generated.Python.*
import org.jetbrains.kotlin.ir.backend.js.utils.JsGenerationContext
import org.jetbrains.kotlin.ir.declarations.*

@Suppress("PARAMETER_NAME_CHANGED_ON_OVERRIDE")
class IrDeclarationToPyTransformer : BaseIrElementToPyNodeTransformer<stmt, JsGenerationContext> {

    override fun visitSimpleFunction(declaration: IrSimpleFunction, context: JsGenerationContext): stmt {
        require(!declaration.isExpect)
        return declaration.accept(IrFunctionToPyTransformer(), context)
    }

    override fun visitConstructor(declaration: IrConstructor, context: JsGenerationContext): stmt {
        // TODO
        return Expr(value = Name(id = identifier("visitConstructor $declaration"), ctx = Load))
    }

    override fun visitClass(declaration: IrClass, context: JsGenerationContext): stmt {
        // TODO
        return ClassDef(
            name = identifier(declaration.name.asString()),
            bases = emptyList(),
            keywords = emptyList(),
            body = emptyList(),
            decorator_list = emptyList(),
        )
    }

    override fun visitErrorDeclaration(declaration: IrErrorDeclaration, data: JsGenerationContext): stmt {
        // TODO
        return Expr(value = Name(id = identifier("visitErrorDeclaration $declaration"), ctx = Load))
    }

    override fun visitField(declaration: IrField, context: JsGenerationContext): stmt {
        // TODO
        return Expr(value = Name(id = identifier("visitField $declaration"), ctx = Load))
    }

    override fun visitVariable(declaration: IrVariable, context: JsGenerationContext): stmt {
        // TODO
        return Expr(value = Name(id = identifier("visitVariable_irDeclarationToPyTransformer $declaration"), ctx = Load))
    }

    override fun visitScript(irScript: IrScript, context: JsGenerationContext): stmt {
        // TODO
        return Expr(value = Name(id = identifier("visitScript $irScript"), ctx = Load))
    }
}
