/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.ir.backend.py

import org.jetbrains.kotlin.backend.common.CommonBackendContext
import org.jetbrains.kotlin.backend.common.ir.isOverridableOrOverrides
import org.jetbrains.kotlin.ir.backend.py.utils.isDispatchReceiver
import org.jetbrains.kotlin.ir.declarations.IrClass
import org.jetbrains.kotlin.ir.declarations.IrSimpleFunction
import org.jetbrains.kotlin.ir.declarations.IrValueParameter
import org.jetbrains.kotlin.ir.symbols.IrSimpleFunctionSymbol
import org.jetbrains.kotlin.ir.types.IrType

interface PyCommonBackendContext : CommonBackendContext {
    override val mapping: PyMapping

    val inlineClassesUtils: InlineClassesUtils
}

interface InlineClassesUtils {
    fun isTypeInlined(type: IrType): Boolean

    fun shouldValueParameterBeBoxed(parameter: IrValueParameter): Boolean {
        val function = parameter.parent as? IrSimpleFunction ?: return false
        val klass = function.parent as? IrClass ?: return false
        if (!isClassInlineLike(klass)) return false
        return parameter.isDispatchReceiver && function.isOverridableOrOverrides
    }

    fun getInlinedClass(type: IrType): IrClass?

    fun isClassInlineLike(klass: IrClass): Boolean

    val boxIntrinsic: IrSimpleFunctionSymbol
    val unboxIntrinsic: IrSimpleFunctionSymbol
}
