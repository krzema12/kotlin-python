/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.ir.backend.js.transformers.irToPy

import generated.Python.*
import org.jetbrains.kotlin.ir.backend.js.utils.JsGenerationContext
import org.jetbrains.kotlin.ir.declarations.IrFile

class IrFileToPyTransformer : BaseIrElementToPyNodeTransformer<List<stmt>, JsGenerationContext> {
    override fun visitFile(declaration: IrFile, data: JsGenerationContext): List<stmt> {
        return declaration.declarations.map {
            it.accept(IrDeclarationToPyTransformer(), data)
        }
    }
}