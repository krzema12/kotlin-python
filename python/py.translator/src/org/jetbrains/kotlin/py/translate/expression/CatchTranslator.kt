/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.expression

import com.intellij.psi.PsiElement
import org.jetbrains.kotlin.js.backend.ast.*
import org.jetbrains.kotlin.py.translate.context.TranslationContext
import org.jetbrains.kotlin.py.translate.general.AbstractTranslator
import org.jetbrains.kotlin.py.translate.general.Translation.patternTranslator
import org.jetbrains.kotlin.py.translate.general.Translation.translateAsStatementAndMergeInBlockIfNeeded
import org.jetbrains.kotlin.py.translate.utils.BindingUtils
import org.jetbrains.kotlin.py.translate.utils.JsAstUtils
import org.jetbrains.kotlin.py.translate.utils.JsAstUtils.convertToBlock
import org.jetbrains.kotlin.psi.KtCatchClause
import org.jetbrains.kotlin.psi.KtTypeReference
import org.jetbrains.kotlin.resolve.BindingContext
import org.jetbrains.kotlin.resolve.BindingContextUtils.getNotNull
import org.jetbrains.kotlin.types.isDynamic

class CatchTranslator(
        val catches: List<KtCatchClause>,
        val psi: PsiElement,
        context: TranslationContext
) : AbstractTranslator(context) {

    /**
     * In JavaScript there is no multiple catches, so we translate
     * multiple catch to single catch with instanceof checks for
     * every catch clause.
     *
     * For example this code:
     *  try {
     *      ...
     *  } catch(e: NullPointerException) {
     *      ...
     *  } catch(e: RuntimeException) {
     *      ...
     *  }
     *
     *  is translated to the following JsCode
     *
     *  try {
     *      ...
     *  } catch(e) {
     *      if (e instanceof NullPointerException) {
     *          ...
     *      } else {
     *          if (e instanceof RuntimeException) {
     *              ...
     *          } else throw e;
     *      }
     *  }
     */
    fun translate(): JsCatch? {
        if (catches.isEmpty()) return null

        val firstCatch = catches.first()
        val catchParameter = firstCatch.catchParameter
        val parameterDescriptor = BindingUtils.getDescriptorForElement(bindingContext(), catchParameter!!)
        val parameterName = context().getNameForDescriptor(parameterDescriptor).ident

        val jsCatch = JsCatch(context().scope(), parameterName)
        val parameterRef = jsCatch.parameter.name.makeRef()
        val catchContext = context().innerContextWithAliased(parameterDescriptor, parameterRef)

        jsCatch.body = JsBlock(translateCatches(catchContext, parameterRef, catches.iterator()))

        return jsCatch
    }

    private fun translateCatches(
        context: TranslationContext,
        initialCatchParameterRef: JsNameRef,
        catches: Iterator<KtCatchClause>
    ): JsStatement {
        if (!catches.hasNext()) {
            return JsThrow(initialCatchParameterRef).apply { source = psi }
        }

        var nextContext = context

        val catch = catches.next()
        val param = catch.catchParameter!!
        val parameterDescriptor = BindingUtils.getDescriptorForElement(bindingContext(), catch.catchParameter!!)
        val parameterName = context().getNameForDescriptor(parameterDescriptor)
        val paramType = param.typeReference!!

        val additionalStatements = mutableListOf<JsStatement>()
        val parameterRef = if (parameterName.ident != initialCatchParameterRef.ident) {
            val parameterAlias = JsScope.declareTemporaryName(parameterName.ident)
            additionalStatements += JsAstUtils.newVar(parameterAlias, initialCatchParameterRef)
            val ref = JsAstUtils.pureFqn(parameterAlias, null)
            ref
        }
        else {
            initialCatchParameterRef
        }
        nextContext = nextContext.innerContextWithAliased(parameterDescriptor, parameterRef)
        val thenBlock = translateCatchBody(nextContext, catch)
        thenBlock.statements.addAll(0, additionalStatements)

        if (paramType.isDynamic) return thenBlock

        // translateIsCheck won't ever return `null` if its second argument is `null`
        val typeCheck = with (patternTranslator(nextContext)) {
            translateIsCheck(initialCatchParameterRef, paramType)
        }!!

        val elseBlock = translateCatches(context, initialCatchParameterRef, catches)
        return JsIf(typeCheck.source(catch), thenBlock, elseBlock).apply { source = catch }
    }

    private fun translateCatchBody(context: TranslationContext, catchClause: KtCatchClause): JsBlock {
        val catchBody = catchClause.catchBody
        val jsCatchBody = if (catchBody != null) {
            translateAsStatementAndMergeInBlockIfNeeded(catchBody, context)
        }
        else {
            JsAstUtils.asSyntheticStatement(JsNullLiteral())
        }

        return convertToBlock(jsCatchBody)
    }

    private val KtTypeReference.isDynamic: Boolean
        get() = getNotNull(bindingContext(), BindingContext.TYPE, this).isDynamic()
}
