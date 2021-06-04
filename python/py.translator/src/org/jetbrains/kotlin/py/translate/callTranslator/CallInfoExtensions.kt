/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.callTranslator

import org.jetbrains.kotlin.js.backend.ast.JsExpression
import org.jetbrains.kotlin.js.backend.ast.JsName
import org.jetbrains.kotlin.js.backend.ast.metadata.SideEffectKind
import org.jetbrains.kotlin.js.backend.ast.metadata.sideEffects
import org.jetbrains.kotlin.descriptors.CallableDescriptor
import org.jetbrains.kotlin.descriptors.PropertyAccessorDescriptor
import org.jetbrains.kotlin.descriptors.PropertyDescriptor
import org.jetbrains.kotlin.descriptors.VariableDescriptor
import org.jetbrains.kotlin.descriptors.impl.TypeAliasConstructorDescriptor
import org.jetbrains.kotlin.py.translate.reference.ReferenceTranslator
import org.jetbrains.kotlin.js.translate.utils.AnnotationsUtils
import org.jetbrains.kotlin.py.translate.utils.JsAstUtils
import org.jetbrains.kotlin.py.translate.utils.TranslationUtils
import org.jetbrains.kotlin.psi.KtSuperExpression
import org.jetbrains.kotlin.resolve.descriptorUtil.isExtension
import org.jetbrains.kotlin.resolve.scopes.receivers.ExpressionReceiver


val CallInfo.callableDescriptor: CallableDescriptor
    get() {
        val result = resolvedCall.resultingDescriptor.original
        return if (result is TypeAliasConstructorDescriptor) result.underlyingConstructorDescriptor else result
    }

fun CallInfo.isNative(): Boolean = AnnotationsUtils.isNativeObject(callableDescriptor)

fun CallInfo.isSuperInvocation(): Boolean {
    val dispatchReceiver = resolvedCall.dispatchReceiver
    return dispatchReceiver is ExpressionReceiver && dispatchReceiver.expression is KtSuperExpression
}

val CallInfo.calleeOwner: JsExpression
    get() {
        val calleeOwner = resolvedCall.resultingDescriptor.containingDeclaration
        return ReferenceTranslator.translateAsValueReference(calleeOwner, context)
    }

val VariableAccessInfo.variableDescriptor: VariableDescriptor
    get() = callableDescriptor as VariableDescriptor

val VariableAccessInfo.variableName: JsName
    get() = context.getNameForDescriptor(variableDescriptor)

fun VariableAccessInfo.isGetAccess(): Boolean = value == null

fun VariableAccessInfo.getAccessDescriptor(): PropertyAccessorDescriptor {
    val property = variableDescriptor as PropertyDescriptor
    return if (isGetAccess()) property.getter!! else property.setter!!
}

fun VariableAccessInfo.getAccessDescriptorIfNeeded(): CallableDescriptor {
    return if (variableDescriptor is PropertyDescriptor &&
               (variableDescriptor.isExtension || TranslationUtils.shouldAccessViaFunctions(variableDescriptor))
                   ) {
        getAccessDescriptor()
    }
    else {
        variableDescriptor
    }
}

fun VariableAccessInfo.constructAccessExpression(ref: JsExpression): JsExpression {
    return if (isGetAccess()) {
        ref
    }
    else {
        // This is useful when passing AST to TemporaryAssignmentElimination. It can bring
        // property assignment like `obj.propertyName = $tmp` to places where `$tmp` gets its value,
        // but only when it's sure that no side effects possible.
        ref.sideEffects = SideEffectKind.PURE
        JsAstUtils.assignment(ref, value!!)
    }
}

val FunctionCallInfo.functionName: JsName
    get() = context.getNameForDescriptor(callableDescriptor)

fun FunctionCallInfo.hasSpreadOperator(): Boolean = argumentsInfo.hasSpreadOperator
