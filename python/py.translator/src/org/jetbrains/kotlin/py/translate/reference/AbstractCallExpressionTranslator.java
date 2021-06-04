/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.reference;

import org.jetbrains.kotlin.js.backend.ast.JsExpression;
import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;
import org.jetbrains.kotlin.descriptors.FunctionDescriptor;
import org.jetbrains.kotlin.py.translate.context.TranslationContext;
import org.jetbrains.kotlin.py.translate.general.AbstractTranslator;
import org.jetbrains.kotlin.psi.KtCallExpression;
import org.jetbrains.kotlin.py.translate.context.TranslationContext;
import org.jetbrains.kotlin.py.translate.general.AbstractTranslator;
import org.jetbrains.kotlin.resolve.calls.callUtil.CallUtilKt;
import org.jetbrains.kotlin.resolve.calls.model.ResolvedCall;

public abstract class AbstractCallExpressionTranslator extends AbstractTranslator {

    @NotNull
    protected final KtCallExpression expression;
    @NotNull
    protected final ResolvedCall<? extends FunctionDescriptor> resolvedCall;
    @Nullable
    protected final JsExpression receiver;

    protected AbstractCallExpressionTranslator(
            @NotNull KtCallExpression expression,
            @Nullable JsExpression receiver,
            @NotNull TranslationContext context
    ) {
        super(context);
        this.expression = expression;
        this.resolvedCall = CallUtilKt.getFunctionResolvedCallWithAssert(expression, bindingContext());
        this.receiver = receiver;
    }

}
