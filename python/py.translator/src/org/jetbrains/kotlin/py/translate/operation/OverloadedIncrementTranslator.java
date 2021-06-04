/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.operation;

import org.jetbrains.kotlin.js.backend.ast.JsExpression;
import org.jetbrains.annotations.NotNull;
import org.jetbrains.kotlin.descriptors.FunctionDescriptor;
import org.jetbrains.kotlin.py.translate.callTranslator.CallTranslator;
import org.jetbrains.kotlin.py.translate.context.TranslationContext;
import org.jetbrains.kotlin.psi.KtUnaryExpression;
import org.jetbrains.kotlin.py.translate.context.TranslationContext;
import org.jetbrains.kotlin.resolve.calls.callUtil.CallUtilKt;
import org.jetbrains.kotlin.resolve.calls.model.ResolvedCall;

public final class OverloadedIncrementTranslator extends IncrementTranslator {

    @NotNull
    private final ResolvedCall<? extends FunctionDescriptor> resolvedCall;

    /*package*/ OverloadedIncrementTranslator(
            @NotNull KtUnaryExpression expression,
            @NotNull TranslationContext context
    ) {
        super(expression, context);
        this.resolvedCall = CallUtilKt.getFunctionResolvedCallWithAssert(expression, context.bindingContext());
    }

    @Override
    @NotNull
    protected JsExpression operationExpression(@NotNull TranslationContext context, @NotNull JsExpression receiver) {
        return CallTranslator.translate(context, resolvedCall, receiver);
    }
}
