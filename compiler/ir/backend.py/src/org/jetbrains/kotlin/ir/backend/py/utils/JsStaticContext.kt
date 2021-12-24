/*
 * Copyright 2010-2018 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.ir.backend.py.utils

import org.jetbrains.kotlin.ir.backend.py.JsIrBackendContext
import org.jetbrains.kotlin.ir.backend.py.transformers.irToPy.PyIntrinsicTransformers
import org.jetbrains.kotlin.js.backend.ast.JsGlobalBlock


class JsStaticContext(
    val backendContext: JsIrBackendContext,
    private val irNamer: IrNamer,
    val globalNameScope: NameScope
) : IrNamer by irNamer {
    val intrinsics = PyIntrinsicTransformers(backendContext)
    val coroutineImplDeclaration = backendContext.ir.symbols.coroutineImpl.owner

    val initializerBlock = JsGlobalBlock()
}