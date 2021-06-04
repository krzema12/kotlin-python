/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */
package org.jetbrains.kotlin.py.translate.declaration

import org.jetbrains.kotlin.descriptors.FunctionDescriptor
import org.jetbrains.kotlin.descriptors.PropertyDescriptor
import org.jetbrains.kotlin.js.backend.ast.JsExpression
import org.jetbrains.kotlin.py.translate.context.TranslationContext
import org.jetbrains.kotlin.py.translate.utils.BindingUtils
import org.jetbrains.kotlin.py.translate.utils.JsAstUtils
import org.jetbrains.kotlin.py.translate.utils.JsDescriptorUtils
import org.jetbrains.kotlin.py.translate.utils.addFunctionButNotExport
import org.jetbrains.kotlin.psi.KtElement
import org.jetbrains.kotlin.psi.KtProperty
import org.jetbrains.kotlin.resolve.BindingContext

class FileDeclarationVisitor(private val context: TranslationContext) : AbstractDeclarationVisitor() {
    override fun visitProperty(expression: KtProperty, context: TranslationContext) {
        val propertyDescriptor = BindingUtils.getPropertyDescriptor(context.bindingContext(), expression)

        val innerName = context.getInnerNameForDescriptor(propertyDescriptor)
        val backingFieldRequired = context.bindingContext()[BindingContext.BACKING_FIELD_REQUIRED, propertyDescriptor] ?: false
        if (backingFieldRequired || expression.delegateExpression != null) {
            val initializer = context.translateDelegateOrInitializerExpression(expression)
            context.addDeclarationStatement(JsAstUtils.newVar(innerName, null))
            if (initializer != null) {
                context.addTopLevelStatement(JsAstUtils.assignment(innerName.makeRef(), initializer).makeStmt())
            }
        }

        super.visitProperty(expression, context)
    }

    override fun addFunction(descriptor: FunctionDescriptor, expression: JsExpression?, psi: KtElement?) {
        if (expression == null) return
        context.addFunctionButNotExport(descriptor, expression)
        context.export(descriptor)
    }

    override fun addProperty(descriptor: PropertyDescriptor, getter: JsExpression, setter: JsExpression?) {
        if (!JsDescriptorUtils.isSimpleFinalProperty(descriptor)) {
            context.addFunctionButNotExport(descriptor.getter!!, getter)
            if (setter != null) {
                context.addFunctionButNotExport(descriptor.setter!!, setter)
            }
        }
        context.export(descriptor)
    }

    override fun getBackingFieldReference(descriptor: PropertyDescriptor): JsExpression {
        return context.getInnerReference(descriptor)
    }
}
