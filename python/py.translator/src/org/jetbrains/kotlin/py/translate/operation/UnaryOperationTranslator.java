/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.operation;

import org.jetbrains.kotlin.js.backend.ast.JsBinaryOperation;
import org.jetbrains.kotlin.js.backend.ast.JsExpression;
import com.intellij.psi.tree.IElementType;
import org.jetbrains.annotations.NotNull;
import org.jetbrains.kotlin.descriptors.FunctionDescriptor;
import org.jetbrains.kotlin.py.translate.callTranslator.CallTranslator;
import org.jetbrains.kotlin.py.translate.context.TranslationContext;
import org.jetbrains.kotlin.py.translate.utils.JsAstUtils;
import org.jetbrains.kotlin.py.translate.utils.TranslationUtils;
import org.jetbrains.kotlin.lexer.KtTokens;
import org.jetbrains.kotlin.psi.KtConstantExpression;
import org.jetbrains.kotlin.psi.KtExpression;
import org.jetbrains.kotlin.psi.KtUnaryExpression;
import org.jetbrains.kotlin.py.translate.context.TranslationContext;
import org.jetbrains.kotlin.py.translate.general.Translation;
import org.jetbrains.kotlin.resolve.calls.callUtil.CallUtilKt;
import org.jetbrains.kotlin.resolve.calls.model.ResolvedCall;
import org.jetbrains.kotlin.resolve.constants.CompileTimeConstant;
import org.jetbrains.kotlin.resolve.constants.evaluate.ConstantExpressionEvaluator;

import static org.jetbrains.kotlin.py.translate.general.Translation.translateAsExpression;
import static org.jetbrains.kotlin.py.translate.utils.BindingUtils.getCompileTimeValue;
import static org.jetbrains.kotlin.py.translate.utils.ErrorReportingUtils.message;
import static org.jetbrains.kotlin.py.translate.utils.PsiUtils.getBaseExpression;
import static org.jetbrains.kotlin.py.translate.utils.PsiUtils.getOperationToken;
import static org.jetbrains.kotlin.py.translate.utils.TranslationUtils.*;

public final class UnaryOperationTranslator {
    private UnaryOperationTranslator() {
    }

    @NotNull
    public static JsExpression translate(
            @NotNull KtUnaryExpression expression,
            @NotNull TranslationContext context
    ) {
        IElementType operationToken = expression.getOperationReference().getReferencedNameElementType();
        if (operationToken == KtTokens.EXCLEXCL) {
            KtExpression baseExpression = getBaseExpression(expression);
            JsExpression translatedExpression = translateAsExpression(baseExpression, context);
            return sure(baseExpression, translatedExpression, context);
        }

        if (operationToken == KtTokens.MINUS) {
            KtExpression baseExpression = getBaseExpression(expression);
            if (baseExpression instanceof KtConstantExpression) {
                CompileTimeConstant<?> compileTimeValue = ConstantExpressionEvaluator.getConstant(expression, context.bindingContext());
                assert compileTimeValue != null : message(expression, "Expression is not compile time value: " + expression.getText() + " ");
                Object value = getCompileTimeValue(context.bindingContext(), expression, compileTimeValue);
                if (value instanceof Long) {
                    return JsAstUtils.newLong((Long) value);
                }
            }
        }

        if (IncrementTranslator.isIncrement(operationToken)) {
            return IncrementTranslator.translate(expression, context);
        }

        JsExpression baseExpression = TranslationUtils.translateBaseExpression(context, expression);
        if (isExclForBinaryEqualLikeExpr(expression, baseExpression)) {
            return translateExclForBinaryEqualLikeExpr((JsBinaryOperation) baseExpression);
        }

        ResolvedCall<? extends FunctionDescriptor> resolvedCall = CallUtilKt.getFunctionResolvedCallWithAssert(expression, context.bindingContext());
        return CallTranslator.translate(context, resolvedCall, baseExpression);
    }

    private static boolean isExclForBinaryEqualLikeExpr(@NotNull KtUnaryExpression expression, @NotNull JsExpression baseExpression) {
        if (getOperationToken(expression).equals(KtTokens.EXCL)) {
            if (baseExpression instanceof JsBinaryOperation) {
                return isEqualLikeOperator(((JsBinaryOperation) baseExpression).getOperator());
            }
        }
        return false;
    }
}
