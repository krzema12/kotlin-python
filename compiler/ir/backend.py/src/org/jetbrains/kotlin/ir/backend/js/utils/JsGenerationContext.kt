/*
 * Copyright 2010-2018 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.ir.backend.js.utils

import org.jetbrains.kotlin.ir.declarations.IrFunction
import org.jetbrains.kotlin.ir.symbols.IrFunctionSymbol
import org.jetbrains.kotlin.ir.util.isSuspend
import org.jetbrains.kotlin.js.backend.ast.JsName
import org.jetbrains.kotlin.js.backend.ast.JsNameRef
import org.jetbrains.kotlin.js.backend.ast.JsScope
import org.jetbrains.kotlin.js.backend.ast.JsThisRef

val emptyScope: JsScope
    get() = object : JsScope("nil") {
        override fun doCreateName(ident: String): JsName {
            error("Trying to create name in empty scope")
        }
    }

class JsGenerationContext(
    val currentFunction: IrFunction?,
    private val irNamer: IrNamer,
) : IrNamer by irNamer {
    fun newDeclaration(func: IrFunction? = null): JsGenerationContext {
        return JsGenerationContext(
            currentFunction = func,
            irNamer = irNamer,
        )
    }

    val continuation
        get() = if (isCoroutineDoResume()) {
            JsThisRef()
        } else {
            if (currentFunction!!.isSuspend) {
                JsNameRef(Namer.CONTINUATION)
            } else {
                getNameForValueDeclaration(currentFunction.valueParameters.last()).makeRef()
            }
        }

    private fun isCoroutineDoResume(): Boolean {
        return false
//        val overriddenSymbols = (currentFunction as? IrSimpleFunction)?.overriddenSymbols ?: return false
//        return overriddenSymbols.any {
//            it.owner.name.asString() == "doResume" && it.owner.parent == staticContext.coroutineImplDeclaration
//        }
    }

    fun checkIfJsCode(symbol: IrFunctionSymbol): Boolean = false //symbol == staticContext.backendContext.intrinsics.jsCode
}
