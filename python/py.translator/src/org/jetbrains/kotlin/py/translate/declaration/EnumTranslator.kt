/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.declaration

import com.intellij.psi.PsiElement
import org.jetbrains.kotlin.builtins.StandardNames
import org.jetbrains.kotlin.descriptors.ClassDescriptor
import org.jetbrains.kotlin.descriptors.FunctionDescriptor
import org.jetbrains.kotlin.js.backend.ast.*
import org.jetbrains.kotlin.py.translate.context.Namer
import org.jetbrains.kotlin.py.translate.context.TranslationContext
import org.jetbrains.kotlin.py.translate.general.AbstractTranslator
import org.jetbrains.kotlin.py.translate.utils.JsAstUtils
import org.jetbrains.kotlin.resolve.DescriptorUtils
import org.jetbrains.kotlin.resolve.descriptorUtil.fqNameSafe

class EnumTranslator(
    context: TranslationContext,
    val descriptor: ClassDescriptor,
    val entries: List<ClassDescriptor>,
    private val psi: PsiElement
) : AbstractTranslator(context) {
    fun generateStandardMethods() {
        generateValuesFunction()
        generateValueOfFunction()
    }

    private fun generateValuesFunction() {
        val function = createFunction(DescriptorUtils.getFunctionByName(descriptor.staticScope, StandardNames.ENUM_VALUES))

        val values = entries.map {
            JsInvocation(JsAstUtils.pureFqn(context().getNameForObjectInstance(it), null)).source(psi)
        }
        function.body.statements += JsReturn(JsArrayLiteral(values).source(psi)).apply { source = psi }
    }

    private fun generateValueOfFunction() {
        val function = createFunction(DescriptorUtils.getFunctionByName(descriptor.staticScope, StandardNames.ENUM_VALUE_OF))

        val nameParam = JsScope.declareTemporaryName("name")
        function.parameters += JsParameter(nameParam)

        val clauses = entries.map { entry ->
            JsCase().apply {
                caseExpression = JsStringLiteral(entry.name.asString()).source(psi)
                statements += JsReturn(JsInvocation(JsAstUtils.pureFqn(context().getNameForObjectInstance(entry), null)).source(psi))
                        .apply { source = psi }
                source = psi
            }
        }

        val message = JsBinaryOperation(JsBinaryOperator.ADD,
                                        JsStringLiteral("No enum constant ${descriptor.fqNameSafe}."),
                                        nameParam.makeRef())
        val throwFunction = context().getReferenceToIntrinsic(Namer.THROW_ILLEGAL_STATE_EXCEPTION_FUN_NAME)
        val throwStatement = JsExpressionStatement(JsInvocation(throwFunction, message).source(psi))

        if (clauses.isNotEmpty()) {
            val defaultCase = JsDefault().apply {
                statements += throwStatement
                source = psi
            }
            function.body.statements += JsSwitch(nameParam.makeRef().source(psi), clauses + defaultCase).apply { source = psi }
        }
        else {
            function.body.statements += throwStatement
        }
    }

    private fun createFunction(functionDescriptor: FunctionDescriptor): JsFunction {
        val function = context().getFunctionObject(functionDescriptor)
        function.name = context().getInnerNameForDescriptor(functionDescriptor)
        function.source = psi
        context().addDeclarationStatement(function.makeStmt())

        val classRef = context().getInnerReference(descriptor)
        val functionRef = function.name.makeRef()
        val assignment = JsAstUtils.assignment(JsNameRef(context().getNameForDescriptor(functionDescriptor), classRef), functionRef)
        context().addDeclarationStatement(assignment.makeStmt())

        return function
    }
}
