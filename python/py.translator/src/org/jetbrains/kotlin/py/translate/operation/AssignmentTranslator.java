/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.operation;

import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;
import org.jetbrains.kotlin.descriptors.*;
import org.jetbrains.kotlin.js.backend.ast.JsExpression;
import org.jetbrains.kotlin.py.translate.context.TranslationContext;
import org.jetbrains.kotlin.py.translate.general.AbstractTranslator;
import org.jetbrains.kotlin.py.translate.reference.AccessTranslationUtils;
import org.jetbrains.kotlin.py.translate.reference.AccessTranslator;
import org.jetbrains.kotlin.py.translate.reference.BackingFieldAccessTranslator;
import org.jetbrains.kotlin.lexer.KtToken;
import org.jetbrains.kotlin.psi.*;
import org.jetbrains.kotlin.py.translate.context.TranslationContext;
import org.jetbrains.kotlin.py.translate.general.AbstractTranslator;
import org.jetbrains.kotlin.types.expressions.OperatorConventions;

import static org.jetbrains.kotlin.py.translate.utils.BindingUtils.*;
import static org.jetbrains.kotlin.py.translate.utils.PsiUtils.getSimpleName;
import static org.jetbrains.kotlin.py.translate.utils.PsiUtils.isAssignment;
import static org.jetbrains.kotlin.py.translate.utils.TranslationUtils.hasCorrespondingFunctionIntrinsic;

public abstract class AssignmentTranslator extends AbstractTranslator {

    public static boolean isAssignmentOperator(KtToken operationToken) {
        return (OperatorConventions.ASSIGNMENT_OPERATIONS.keySet().contains(operationToken) || isAssignment(operationToken));
    }

    @NotNull
    public static JsExpression translate(@NotNull KtBinaryExpression expression, @NotNull TranslationContext context) {
        if (hasCorrespondingFunctionIntrinsic(context, expression)) {
            // This is a hack. This code is conceptually wrong, refactoring required here.
            // The right implementation is: get assignment via OverloadedAssignmentTranslator and see at the result.
            // If it's an expression like `a = a + b` then represent it as `a += b`
            // Another right implementation is: enumerate explicitly which descriptors are OK to intrinsify like this.
            CallableDescriptor operationDescriptor = getCallableDescriptorForOperationExpression(context.bindingContext(), expression);
            if (operationDescriptor == null || operationDescriptor.getExtensionReceiverParameter() == null) {
                return IntrinsicAssignmentTranslator.doTranslate(expression, context);
            }
        }
        return OverloadedAssignmentTranslator.doTranslate(expression, context);
    }

    @NotNull
    protected final KtBinaryExpression expression;
    protected final boolean isVariableReassignment;

    protected AssignmentTranslator(@NotNull KtBinaryExpression expression, @NotNull TranslationContext context) {
        super(context);
        this.expression = expression;
        this.isVariableReassignment = isVariableReassignment(context.bindingContext(), expression);
        assert expression.getLeft() != null : "No left-hand side: " + expression.getText();
    }

    protected final AccessTranslator createAccessTranslator(@NotNull KtExpression left, boolean forceOrderOfEvaluation) {
        if (isValProperty(left, context())) {
            KtSimpleNameExpression simpleName = getSimpleName(left);
            assert simpleName != null;
            return BackingFieldAccessTranslator.newInstance(simpleName, context());
        }
        else {
            return AccessTranslationUtils.getAccessTranslator(left, context(), forceOrderOfEvaluation);
        }
    }

    private static boolean isValProperty(
            @NotNull KtExpression expression,
            @NotNull TranslationContext context
    ) {
        KtSimpleNameExpression simpleNameExpression = getSimpleName(expression);

        if (simpleNameExpression != null) {
            DeclarationDescriptor descriptor = getDescriptorForReferenceExpression(context.bindingContext(), simpleNameExpression);
            return descriptor instanceof PropertyDescriptor && !((PropertyDescriptor) descriptor).isVar();
        }

        return false;
    }
}
