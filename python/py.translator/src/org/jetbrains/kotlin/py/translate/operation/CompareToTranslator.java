/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.operation;

import org.jetbrains.kotlin.js.backend.ast.JsBinaryOperation;
import org.jetbrains.kotlin.js.backend.ast.JsBinaryOperator;
import org.jetbrains.kotlin.js.backend.ast.JsExpression;
import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;
import org.jetbrains.kotlin.descriptors.CallableDescriptor;
import org.jetbrains.kotlin.js.backend.ast.JsIntLiteral;
import org.jetbrains.kotlin.py.translate.context.TranslationContext;
import org.jetbrains.kotlin.py.translate.general.AbstractTranslator;
import org.jetbrains.kotlin.lexer.KtToken;
import org.jetbrains.kotlin.psi.KtBinaryExpression;
import org.jetbrains.kotlin.py.translate.context.TranslationContext;
import org.jetbrains.kotlin.py.translate.general.AbstractTranslator;
import org.jetbrains.kotlin.types.expressions.OperatorConventions;

import static org.jetbrains.kotlin.py.translate.utils.BindingUtils.getCallableDescriptorForOperationExpression;
import static org.jetbrains.kotlin.py.translate.utils.ErrorReportingUtils.message;
import static org.jetbrains.kotlin.py.translate.utils.JsDescriptorUtils.isCompareTo;
import static org.jetbrains.kotlin.py.translate.utils.PsiUtils.getOperationToken;

public final class CompareToTranslator extends AbstractTranslator {

    public static boolean isCompareToCall(
            @NotNull KtToken operationToken,
            @Nullable CallableDescriptor operationDescriptor
    ) {
        if (!OperatorConventions.COMPARISON_OPERATIONS.contains(operationToken) || operationDescriptor == null) return false;

        return isCompareTo(operationDescriptor);
    }

    @NotNull
    public static JsExpression translate(@NotNull KtBinaryExpression expression,
            @NotNull TranslationContext context) {
        return (new CompareToTranslator(expression, context)).translate();
    }

    @NotNull
    private final KtBinaryExpression expression;

    private CompareToTranslator(
            @NotNull KtBinaryExpression expression,
            @NotNull TranslationContext context
    ) {
        super(context);
        this.expression = expression;
        CallableDescriptor descriptor = getCallableDescriptorForOperationExpression(context.bindingContext(), expression);
        assert descriptor != null : "CompareTo should always have a descriptor";
        assert (OperatorConventions.COMPARISON_OPERATIONS.contains(getOperationToken(expression))) :
                message(expression, "CompareToTranslator supported only expressions with operation token from COMPARISON_OPERATIONS, " +
                                    "expression: " + expression.getText());
    }

    @NotNull
    private JsExpression translate() {
        JsBinaryOperator correspondingOperator = OperatorTable.getBinaryOperator(getOperationToken(expression));
        JsExpression methodCall = BinaryOperationTranslator.translateAsOverloadedCall(expression, context());
        return new JsBinaryOperation(correspondingOperator, methodCall, new JsIntLiteral(0));
    }
}
