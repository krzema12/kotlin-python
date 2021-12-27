/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.ir.backend.py.lower

import org.jetbrains.kotlin.backend.common.BodyLoweringPass
import org.jetbrains.kotlin.ir.declarations.*
import org.jetbrains.kotlin.ir.expressions.*

class CallableReferenceLowering : BodyLoweringPass {

    override fun lower(irFile: IrFile) {
        TODO("Left here only because companion object is used. This class will be probably removed soon.")
    }

    override fun lower(irBody: IrBody, container: IrDeclaration) {
        TODO("Left here only because companion object is used. This class will be probably removed soon.")
    }

    companion object {
        object LAMBDA_IMPL : IrDeclarationOriginImpl("LAMBDA_IMPL")

        object CALLABLE_REFERENCE_CREATE : IrStatementOriginImpl("CALLABLE_REFERENCE_CREATE")
        object CALLABLE_REFERENCE_INVOKE : IrStatementOriginImpl("CALLABLE_REFERENCE_INVOKE")
    }

}
