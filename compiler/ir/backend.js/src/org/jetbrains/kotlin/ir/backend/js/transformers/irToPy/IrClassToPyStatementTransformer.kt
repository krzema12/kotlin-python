/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.ir.backend.js.transformers.irToPy

import generated.Python.*
import org.jetbrains.kotlin.ir.backend.js.utils.JsGenerationContext
import org.jetbrains.kotlin.ir.declarations.IrClass
import org.jetbrains.kotlin.ir.declarations.IrConstructor
import org.jetbrains.kotlin.ir.declarations.IrField
import org.jetbrains.kotlin.ir.declarations.IrSimpleFunction
import org.jetbrains.kotlin.ir.util.render

fun IrClass.toPythonStatement(context: JsGenerationContext): stmt {
    return ClassDef(
        name = identifier(name.asString().toValidPythonSymbol()),
        bases = emptyList(),
        keywords = emptyList(),
        body = declarations.map { declaration ->
            when (declaration) {
                is IrConstructor -> IrDeclarationToPyTransformer().visitConstructor(declaration, context)
                is IrSimpleFunction -> IrDeclarationToPyTransformer().visitSimpleFunction(declaration, context)
                is IrClass -> Expr(value = Name(id = identifier("visitClassDeclaration_IrClass ${declaration.render()}".toValidPythonSymbol()), ctx = Load))
                is IrField -> Expr(value = Name(id = identifier("visitClassDeclaration_IrField ${declaration.render()}".toValidPythonSymbol()), ctx = Load))
                else -> throw IllegalArgumentException("Unknown declaration type: ${declaration.render()}")
            }
        },
        decorator_list = emptyList(),
    )
}
