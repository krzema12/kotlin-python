/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.ir.backend.py.lower

import org.jetbrains.kotlin.backend.common.BodyLoweringPass
import org.jetbrains.kotlin.backend.common.IrElementTransformerVoidWithContext
import org.jetbrains.kotlin.backend.common.pop
import org.jetbrains.kotlin.backend.common.push
import org.jetbrains.kotlin.ir.IrElement
import org.jetbrains.kotlin.ir.IrStatement
import org.jetbrains.kotlin.ir.backend.py.JsIrBackendContext
import org.jetbrains.kotlin.ir.declarations.*
import org.jetbrains.kotlin.ir.expressions.IrBody
import org.jetbrains.kotlin.ir.expressions.IrCall
import org.jetbrains.kotlin.ir.expressions.IrContainerExpression
import org.jetbrains.kotlin.ir.expressions.IrExpression
import org.jetbrains.kotlin.ir.symbols.IrFunctionSymbol
import org.jetbrains.kotlin.ir.visitors.IrElementVisitorVoid
import org.jetbrains.kotlin.ir.visitors.acceptChildrenVoid
import org.jetbrains.kotlin.ir.visitors.transformChildrenVoid

// Outlines `kotlin.js.js(code: String)` calls where JS code references Kotlin locals.
// Makes locals usages explicit.
class JsCodeOutliningLowering(val backendContext: JsIrBackendContext) : BodyLoweringPass {
    override fun lower(irBody: IrBody, container: IrDeclaration) {
        // Fast path to avoid tracking locals scopes for bodies without js() calls
        if (!irBody.containsCallsTo(backendContext.intrinsics.jsCode))
            return

        val replacer = JsCodeOutlineTransformer(backendContext, container)
        irBody.transformChildrenVoid(replacer)
    }
}

private fun IrElement.containsCallsTo(symbol: IrFunctionSymbol): Boolean {
    var result = false
    acceptChildrenVoid(object : IrElementVisitorVoid {
        override fun visitElement(element: IrElement) {
            element.acceptChildrenVoid(this)
        }

        override fun visitCall(expression: IrCall) {
            if (expression.symbol == symbol) {
                result = true
            }
            super.visitCall(expression)
        }
    })

    return result
}

private class JsCodeOutlineTransformer(
    val backendContext: JsIrBackendContext,
    val container: IrDeclaration,
) : IrElementTransformerVoidWithContext() {
    val localScopes: MutableList<MutableMap<String, IrValueDeclaration>> =
        mutableListOf(mutableMapOf())

    init {
        if (container is IrFunction) {
            container.valueParameters.forEach {
                registerValueDeclaration(it)
            }
        }
    }

    inline fun <T> withLocalScope(body: () -> T): T {
        localScopes.push(mutableMapOf())
        val res = body()
        localScopes.pop()
        return res
    }

    fun registerValueDeclaration(irValueDeclaration: IrValueDeclaration) {
        val name = irValueDeclaration.name
        if (!name.isSpecial) {
            val identifier = name.identifier
            val currentScope = localScopes.lastOrNull() ?: error("Expecting a scope")
            currentScope[identifier] = irValueDeclaration
        }
    }

    fun findValueDeclarationWithName(name: String): IrValueDeclaration? {
        for (i in (localScopes.size - 1) downTo 0) {
            val scope = localScopes[i]
            return scope[name] ?: continue
        }
        return null
    }

    override fun visitContainerExpression(expression: IrContainerExpression): IrExpression {
        return withLocalScope { super.visitContainerExpression(expression) }
    }

    override fun visitDeclaration(declaration: IrDeclarationBase): IrStatement {
        return withLocalScope { super.visitDeclaration(declaration) }
    }

    override fun visitValueParameterNew(declaration: IrValueParameter): IrStatement {
        return super.visitValueParameterNew(declaration).also { registerValueDeclaration(declaration) }
    }

    override fun visitVariable(declaration: IrVariable): IrStatement {
        return super.visitVariable(declaration).also { registerValueDeclaration(declaration) }
    }

    override fun visitCall(expression: IrCall): IrExpression {
        return outlineJsCodeIfNeeded(expression) ?: super.visitCall(expression)
    }

    fun outlineJsCodeIfNeeded(expression: IrCall): IrExpression? {
        if (expression.symbol != backendContext.intrinsics.jsCode)
            return null

        TODO()
    }

    companion object {
        object OUTLINED_ORIGIN : IrDeclarationOriginImpl("OUTLINED_ORIGIN")
    }
}