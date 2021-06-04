/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.operation;

import org.jetbrains.kotlin.js.backend.ast.JsExpression;
import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;
import org.jetbrains.kotlin.descriptors.CallableDescriptor;
import org.jetbrains.kotlin.descriptors.FunctionDescriptor;
import org.jetbrains.kotlin.js.patterns.DescriptorPredicate;
import org.jetbrains.kotlin.js.patterns.PatternBuilder;
import org.jetbrains.kotlin.py.translate.callTranslator.CallTranslator;
import org.jetbrains.kotlin.py.translate.context.TranslationContext;
import org.jetbrains.kotlin.py.translate.general.AbstractTranslator;
import org.jetbrains.kotlin.py.translate.general.Translation;
import org.jetbrains.kotlin.py.translate.utils.JsAstUtils;
import org.jetbrains.kotlin.psi.*;
import org.jetbrains.kotlin.psi.psiUtil.PsiUtilsKt;
import org.jetbrains.kotlin.py.translate.context.TranslationContext;
import org.jetbrains.kotlin.py.translate.general.AbstractTranslator;
import org.jetbrains.kotlin.py.translate.general.Translation;
import org.jetbrains.kotlin.resolve.calls.callUtil.CallUtilKt;
import org.jetbrains.kotlin.resolve.calls.model.ResolvedCall;
import org.jetbrains.kotlin.resolve.scopes.receivers.ExpressionReceiver;

/**
 * Translates 'A in B' expression applying specialization if possible
 */
public class InOperationTranslator extends AbstractTranslator {
    private static final DescriptorPredicate INT_SPECIALIZATION_TEST = PatternBuilder.pattern("ranges.IntRange.contains");
    private static final DescriptorPredicate INT_RANGE_TEST = PatternBuilder.pattern("Int.rangeTo");
    private final JsExpression left;
    private final KtExpression right;
    private final KtSimpleNameExpression operation;
    private final boolean negated;

    public InOperationTranslator(@NotNull TranslationContext context, @NotNull JsExpression left, @NotNull KtExpression right,
            @NotNull KtSimpleNameExpression operation, boolean negated) {
        super(context);
        this.left = left;
        this.right = right;
        this.operation = operation;
        this.negated = negated;
    }

    @NotNull
    public JsExpression translate() {
        ResolvedCall<? extends FunctionDescriptor> call = CallUtilKt.getFunctionResolvedCallWithAssert(operation, bindingContext());
        if (INT_SPECIALIZATION_TEST.test(call.getResultingDescriptor())) {
            JsExpression candidate = translateInt();
            if (candidate != null) {
                return candidate;
            }
        }
        JsExpression rightTranslated = Translation.translateAsExpression(right, context());
        return translateGeneral(call, rightTranslated);
    }

    @NotNull
    private JsExpression translateGeneral(@NotNull ResolvedCall<? extends FunctionDescriptor> call, @NotNull JsExpression rightTranslated) {
        JsExpression result = CallTranslator.translate(context(), call, rightTranslated);
        if (negated) {
            result = JsAstUtils.not(result);
        }
        return result;
    }

    @Nullable
    private JsExpression translateInt() {
        ResolvedCall<? extends CallableDescriptor> rightCall = CallUtilKt.getResolvedCallWithAssert(right, bindingContext());
        if (!(rightCall.getResultingDescriptor() instanceof FunctionDescriptor)) {
            return null;
        }
        FunctionDescriptor callDescriptor = (FunctionDescriptor) rightCall.getResultingDescriptor();
        if (!INT_RANGE_TEST.test(callDescriptor)) {
            return null;
        }
        if (!(rightCall.getDispatchReceiver() instanceof ExpressionReceiver)) {
            return null;
        }

        KtExpression lower = ((ExpressionReceiver) rightCall.getDispatchReceiver()).getExpression();
        KtExpression upper = rightCall.getCall().getValueArguments().get(0).getArgumentExpression();
        assert upper != null : "Parse error occurred: " + PsiUtilsKt.getTextWithLocation(right);
        return translateInt(lower, upper);
    }

    @NotNull
    private JsExpression translateInt(@NotNull KtExpression lowerExpression, @NotNull KtExpression upperExpression) {
        JsExpression lower = Translation.translateAsExpression(lowerExpression, context());
        JsExpression upper = Translation.translateAsExpression(upperExpression, context());
        if (!negated) {
            JsExpression first = JsAstUtils.greaterThanEq(left, lower);
            JsExpression second = JsAstUtils.lessThanEq(left, upper);
            return JsAstUtils.and(first, second);
        }
        else {
            JsExpression first = JsAstUtils.lessThan(left, lower);
            JsExpression second = JsAstUtils.greaterThan(left, upper);
            return JsAstUtils.or(first, second);
        }
    }
}
