/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.operation;

import org.jetbrains.annotations.NotNull;
import org.jetbrains.kotlin.js.backend.ast.*;
import org.jetbrains.kotlin.py.translate.context.TranslationContext;
import org.jetbrains.kotlin.lexer.KtToken;
import org.jetbrains.kotlin.lexer.KtTokens;
import org.jetbrains.kotlin.psi.KtUnaryExpression;
import org.jetbrains.kotlin.py.translate.context.TranslationContext;

import static org.jetbrains.kotlin.py.translate.utils.PsiUtils.getOperationToken;
import static org.jetbrains.kotlin.py.translate.utils.PsiUtils.isPrefix;
import static org.jetbrains.kotlin.py.translate.utils.TranslationUtils.isSimpleNameExpressionNotDelegatedLocalVar;

public class DynamicIncrementTranslator extends IncrementTranslator {

    @NotNull
    public static JsExpression doTranslate(@NotNull KtUnaryExpression expression,
            @NotNull TranslationContext context) {
        return (new DynamicIncrementTranslator(expression, context))
                .translate();
    }

    private DynamicIncrementTranslator(@NotNull KtUnaryExpression expression,
            @NotNull TranslationContext context) {
        super(expression, context);
    }

    @NotNull
    private JsExpression translate() {
        if (isSimpleNameExpressionNotDelegatedLocalVar(expression.getBaseExpression(), context())) {
            return primitiveExpressionIncrement();
        }
        return translateIncrementExpression();
    }

    @NotNull
    private JsExpression primitiveExpressionIncrement() {
        JsUnaryOperator operator = OperatorTable.getUnaryOperator(getOperationToken(expression));
        JsExpression getExpression = accessTranslator.translateAsGet();
        if (isPrefix(expression)) {
            return new JsPrefixOperation(operator, getExpression);
        }
        else {
            return new JsPostfixOperation(operator, getExpression);
        }
    }

    @Override
    @NotNull
    protected JsExpression operationExpression(@NotNull TranslationContext context, @NotNull JsExpression receiver) {
        return unaryAsBinary(receiver);
    }

    @NotNull
    private JsBinaryOperation unaryAsBinary(@NotNull JsExpression leftExpression) {
        JsNumberLiteral oneLiteral = new JsIntLiteral(1);
        KtToken token = getOperationToken(expression);
        if (token.equals(KtTokens.PLUSPLUS)) {
            return new JsBinaryOperation(JsBinaryOperator.ADD, leftExpression, oneLiteral);
        }
        if (token.equals(KtTokens.MINUSMINUS)) {
            return new JsBinaryOperation(JsBinaryOperator.SUB, leftExpression, oneLiteral);
        }
        throw new AssertionError("This method should be called only for increment and decrement operators");
    }

}
