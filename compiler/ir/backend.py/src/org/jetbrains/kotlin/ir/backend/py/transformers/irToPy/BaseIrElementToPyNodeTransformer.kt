/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.ir.backend.py.transformers.irToPy

import org.jetbrains.kotlin.ir.IrElement
import org.jetbrains.kotlin.ir.backend.py.utils.TODO
import org.jetbrains.kotlin.ir.visitors.IrElementVisitor

interface BaseIrElementToPyNodeTransformer<out R, in D> : IrElementVisitor<R, D> {
    override fun visitElement(element: IrElement, data: D): R {
        TODO(element)
    }
}
