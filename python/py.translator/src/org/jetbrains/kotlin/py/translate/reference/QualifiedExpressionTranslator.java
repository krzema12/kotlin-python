/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.reference;

import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;
import org.jetbrains.kotlin.descriptors.DeclarationDescriptor;
import org.jetbrains.kotlin.descriptors.PackageViewDescriptor;
import org.jetbrains.kotlin.js.backend.ast.JsExpression;
import org.jetbrains.kotlin.js.backend.ast.JsNode;
import org.jetbrains.kotlin.py.translate.context.TranslationContext;
import org.jetbrains.kotlin.py.translate.utils.ErrorReportingUtils;
import org.jetbrains.kotlin.psi.*;
import org.jetbrains.kotlin.py.translate.context.TranslationContext;
import org.jetbrains.kotlin.py.translate.general.Translation;
import org.jetbrains.kotlin.py.translate.utils.BindingUtils;
import org.jetbrains.kotlin.py.translate.utils.ErrorReportingUtils;
import org.jetbrains.kotlin.py.translate.utils.PsiUtils;
import org.jetbrains.kotlin.resolve.calls.callUtil.CallUtilKt;
import org.jetbrains.kotlin.resolve.calls.model.ResolvedCall;

import static org.jetbrains.kotlin.py.translate.general.Translation.translateAsExpression;
import static org.jetbrains.kotlin.py.translate.utils.BindingUtils.getDescriptorForReferenceExpression;
import static org.jetbrains.kotlin.py.translate.utils.PsiUtils.getSelector;

public final class QualifiedExpressionTranslator {

    private QualifiedExpressionTranslator() {
    }

    @NotNull
    public static AccessTranslator getAccessTranslator(@NotNull KtQualifiedExpression expression,
                                                       @NotNull TranslationContext context, boolean forceOrderOfEvaluation) {
        JsExpression receiver = translateReceiver(expression, context);
        if (forceOrderOfEvaluation && receiver != null) {
            receiver = context.defineTemporary(receiver);
        }

        KtExpression selector = PsiUtils.getSelector(expression);
        if (selector instanceof KtSimpleNameExpression) {
            return VariableAccessTranslator.newInstance(context, (KtSimpleNameExpression) selector, receiver);
        }
        if (selector instanceof KtCallExpression) {
            return new QualifiedExpressionWithCallSelectorAccessTranslator((KtCallExpression) selector, receiver, context);
        }

        throw new AssertionError("Unexpected qualified expression: " + expression.getText());
    }

    @NotNull
    public static JsNode translateQualifiedExpression(
            @NotNull KtQualifiedExpression expression,
            @NotNull TranslationContext context
    ) {
        ResolvedCall<?> call = CallUtilKt.getResolvedCall(expression, context.bindingContext());
        JsExpression receiver = null;
        if (call != null) {
            receiver = translateReceiver(expression, context);
        }
        KtExpression selector = PsiUtils.getSelector(expression);
        return dispatchToCorrectTranslator(receiver, selector, context);
    }

    @NotNull
    private static JsNode dispatchToCorrectTranslator(
            @Nullable JsExpression receiver,
            @NotNull KtExpression selector,
            @NotNull TranslationContext context
    ) {
        if (ReferenceTranslator.canBePropertyAccess(selector, context)) {
            assert selector instanceof KtSimpleNameExpression : "Selectors for properties must be simple names.";
            return VariableAccessTranslator.newInstance(context, (KtSimpleNameExpression)selector, receiver).translateAsGet();
        }
        if (selector instanceof KtCallExpression) {
            return invokeCallExpressionTranslator(receiver, (KtCallExpression) selector, context);
        }
        //TODO: never get there
        if (selector instanceof KtSimpleNameExpression) {
            return ReferenceTranslator.translateSimpleName((KtSimpleNameExpression) selector, context);
        }
        throw new AssertionError("Unexpected qualified expression: " + selector.getText());
    }

    @NotNull
    static JsNode invokeCallExpressionTranslator(
            @Nullable JsExpression receiver,
            @NotNull KtCallExpression selector,
            @NotNull TranslationContext context
    ) {
        try {
            return CallExpressionTranslator.translate(selector, receiver, context);
        } catch (RuntimeException e) {
            throw  ErrorReportingUtils.reportErrorWithLocation(selector, e);
        }
    }

    @Nullable
    private static JsExpression translateReceiver(@NotNull KtQualifiedExpression expression,
                                                  @NotNull TranslationContext context) {
        KtExpression receiverExpression = expression.getReceiverExpression();
        if (isFullQualifierForExpression(receiverExpression, context)) {
            return null;
        }
        return Translation.translateAsExpression(receiverExpression, context);
    }

    //TODO: prove correctness
    private static boolean isFullQualifierForExpression(@Nullable KtExpression receiverExpression, @NotNull TranslationContext context) {
        if (receiverExpression == null) {
            return false;
        }
        if (receiverExpression instanceof KtReferenceExpression) {
            DeclarationDescriptor descriptorForReferenceExpression =
                BindingUtils.getDescriptorForReferenceExpression(context.bindingContext(), (KtReferenceExpression)receiverExpression);
            if (descriptorForReferenceExpression instanceof PackageViewDescriptor) {
                return true;
            }
        }
        if (receiverExpression instanceof KtQualifiedExpression) {
            return isFullQualifierForExpression(((KtQualifiedExpression)receiverExpression).getSelectorExpression(), context);
        }
        return false;
    }
}
