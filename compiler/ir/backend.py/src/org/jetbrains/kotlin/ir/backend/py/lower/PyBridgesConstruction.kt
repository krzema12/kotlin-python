/*
 * Copyright 2010-2019 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.ir.backend.py.lower

import org.jetbrains.kotlin.ir.backend.py.PyIrBackendContext
import org.jetbrains.kotlin.ir.backend.py.PyLoweredDeclarationOrigin
import org.jetbrains.kotlin.ir.backend.py.utils.hasStableJsName
import org.jetbrains.kotlin.ir.backend.py.utils.jsFunctionSignature
import org.jetbrains.kotlin.ir.declarations.IrDeclarationOrigin
import org.jetbrains.kotlin.ir.declarations.IrSimpleFunction

class PyBridgesConstruction(context: PyIrBackendContext) : BridgesConstruction<PyIrBackendContext>(context) {
    override fun getFunctionSignature(function: IrSimpleFunction): String =
        jsFunctionSignature(function, context)

    override fun getBridgeOrigin(bridge: IrSimpleFunction): IrDeclarationOrigin =
        if (bridge.hasStableJsName(context))
            PyLoweredDeclarationOrigin.BRIDGE_WITH_STABLE_NAME
        else
            PyLoweredDeclarationOrigin.BRIDGE_WITHOUT_STABLE_NAME
}
