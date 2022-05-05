/*
 * Copyright 2010-2022 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.ir.backend.py.lower

import org.jetbrains.kotlin.backend.common.BodyLoweringPass
import org.jetbrains.kotlin.backend.common.lower.createIrBuilder
import org.jetbrains.kotlin.ir.backend.py.PyIrBackendContext
import org.jetbrains.kotlin.ir.backend.py.ir.JsIrArithBuilder
import org.jetbrains.kotlin.ir.backend.py.ir.JsIrBuilder
import org.jetbrains.kotlin.ir.builders.createTmpVariable
import org.jetbrains.kotlin.ir.builders.irComposite
import org.jetbrains.kotlin.ir.builders.irGet
import org.jetbrains.kotlin.ir.builders.irSet
import org.jetbrains.kotlin.ir.declarations.IrDeclaration
import org.jetbrains.kotlin.ir.expressions.IrBody
import org.jetbrains.kotlin.ir.expressions.IrDoWhileLoop
import org.jetbrains.kotlin.ir.expressions.IrExpression
import org.jetbrains.kotlin.ir.expressions.impl.IrWhileLoopImpl
import org.jetbrains.kotlin.ir.symbols.IrSymbol
import org.jetbrains.kotlin.ir.visitors.IrElementTransformerVoid
import org.jetbrains.kotlin.ir.visitors.transformChildrenVoid

class DoWhileTransformer(private val context: PyIrBackendContext, private val irSymbol: IrSymbol) : IrElementTransformerVoid() {

    private val calculator = JsIrArithBuilder(context)
    private val constTrue get() = JsIrBuilder.buildBoolean(context.irBuiltIns.booleanType, true)
    private val constFalse get() = JsIrBuilder.buildBoolean(context.irBuiltIns.booleanType, false)

    /*
        Transform:

        do:
            <body>
        while (<condition>)

        To:

        firstIterationLoopName = true
        while firstIterationLoopName or (<condition>):
            firstIterationLoopName = false
            <body>
    */
    override fun visitDoWhileLoop(loop: IrDoWhileLoop): IrExpression {
        return context.createIrBuilder(irSymbol).irComposite {
            val tmp = createTmpVariable(constTrue, nameHint = "firstIteration")
            val newCondition = calculator.oror(irGet(tmp), loop.condition)
            val newBody = irComposite {
                +irSet(tmp, constFalse)
                loop.body?.unaryPlus()
            }

            +IrWhileLoopImpl(loop.startOffset, loop.endOffset, loop.type, loop.origin).apply {
                condition = newCondition
                body = newBody
                label = loop.label
            }
        }
    }
}

class DoWhileRemover(private val context: PyIrBackendContext) : BodyLoweringPass {
    override fun lower(irBody: IrBody, container: IrDeclaration) {
        irBody.transformChildrenVoid(DoWhileTransformer(context, container.symbol))
    }
}
