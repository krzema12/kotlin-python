/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.expression

import org.jetbrains.kotlin.descriptors.FunctionDescriptor
import org.jetbrains.kotlin.py.translate.utils.BindingUtils
import org.jetbrains.kotlin.psi.*
import org.jetbrains.kotlin.resolve.BindingContext

class LocalFunctionCollector(val bindingContext: BindingContext) : KtVisitorVoid() {
    val functions = mutableSetOf<FunctionDescriptor>()

    override fun visitExpression(expression: KtExpression) {
        if (expression is KtDeclarationWithBody) {
            functions += BindingUtils.getFunctionDescriptor(bindingContext, expression)
        }
        else {
            expression.acceptChildren(this, null)
        }
    }

    override fun visitClassOrObject(classOrObject: KtClassOrObject) {
        // skip
    }
}
