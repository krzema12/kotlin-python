/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.intrinsic.functions.basic

import org.jetbrains.kotlin.js.backend.ast.JsExpression
import org.jetbrains.kotlin.js.backend.ast.JsNew
import org.jetbrains.kotlin.descriptors.ClassDescriptor
import org.jetbrains.kotlin.descriptors.FunctionDescriptor
import org.jetbrains.kotlin.descriptors.PackageFragmentDescriptor
import org.jetbrains.kotlin.py.translate.context.TranslationContext
import org.jetbrains.kotlin.py.translate.reference.ReferenceTranslator
import org.jetbrains.kotlin.resolve.scopes.DescriptorKindFilter

class RangeToIntrinsic(function: FunctionDescriptor) : FunctionIntrinsicWithReceiverComputed() {
    val rangeTypeDescriptor = function.returnType!!.constructor.declarationDescriptor as ClassDescriptor

    override fun apply(receiver: JsExpression?, arguments: List<JsExpression>, context: TranslationContext): JsExpression {
        val packageName = (rangeTypeDescriptor.containingDeclaration as PackageFragmentDescriptor).fqName
        val packageDescriptor = context.currentModule.getPackage(packageName)
        val existingClasses = packageDescriptor.memberScope.getContributedDescriptors(DescriptorKindFilter.CLASSIFIERS) {
            it == rangeTypeDescriptor.name
        }
        val finalClass = (existingClasses.firstOrNull() as? ClassDescriptor) ?: rangeTypeDescriptor
        val constructor = ReferenceTranslator.translateAsTypeReference(finalClass, context)
        return JsNew(constructor, listOfNotNull(receiver) + arguments)
    }
}