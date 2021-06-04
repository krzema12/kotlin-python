/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.operation;

import org.jetbrains.kotlin.builtins.KotlinBuiltIns;
import org.jetbrains.kotlin.js.backend.ast.JsBinaryOperation;
import org.jetbrains.kotlin.js.backend.ast.JsBinaryOperator;
import org.jetbrains.kotlin.js.backend.ast.JsBlock;
import org.jetbrains.kotlin.js.backend.ast.JsExpression;
import org.jetbrains.annotations.NotNull;
import org.jetbrains.kotlin.py.translate.context.TranslationContext;
import org.jetbrains.kotlin.py.translate.reference.AccessTranslator;
import org.jetbrains.kotlin.py.translate.utils.JsAstUtils;
import org.jetbrains.kotlin.py.translate.utils.TranslationUtils;
import org.jetbrains.kotlin.lexer.KtSingleValueToken;
import org.jetbrains.kotlin.lexer.KtToken;
import org.jetbrains.kotlin.psi.KtBinaryExpression;
import org.jetbrains.kotlin.psi.KtExpression;
import org.jetbrains.kotlin.py.translate.context.TranslationContext;
import org.jetbrains.kotlin.py.translate.reference.AccessTranslator;
import org.jetbrains.kotlin.py.translate.utils.JsAstUtils;
import org.jetbrains.kotlin.py.translate.utils.PsiUtils;
import org.jetbrains.kotlin.py.translate.utils.TranslationUtils;
import org.jetbrains.kotlin.types.KotlinType;
import org.jetbrains.kotlin.types.expressions.OperatorConventions;

import static org.jetbrains.kotlin.py.translate.utils.PsiUtils.getOperationToken;
import static org.jetbrains.kotlin.py.translate.utils.PsiUtils.isAssignment;
import static org.jetbrains.kotlin.py.translate.utils.TranslationUtils.isSimpleNameExpressionNotDelegatedLocalVar;

public final class IntrinsicAssignmentTranslator extends AssignmentTranslator {
    private final JsExpression right;
    private final AccessTranslator accessTranslator;
    private final boolean rightExpressionTrivial;
    private final JsBlock rightBlock = new JsBlock();

    @NotNull
    public static JsExpression doTranslate(@NotNull KtBinaryExpression expression, @NotNull TranslationContext context) {
        return (new IntrinsicAssignmentTranslator(expression, context)).translate();
    }

    private IntrinsicAssignmentTranslator(@NotNull KtBinaryExpression expression, @NotNull TranslationContext context) {
        super(expression, context);

        right = translateRightExpression(context, expression);
        rightExpressionTrivial = rightBlock.isEmpty();
        KtExpression left = expression.getLeft();
        assert left != null;
        accessTranslator = createAccessTranslator(left, !rightExpressionTrivial);
    }

    private JsExpression translateRightExpression(TranslationContext context, KtBinaryExpression expression) {
        JsExpression result = TranslationUtils.translateRightExpression(context, expression, rightBlock);
        KotlinType leftType = context.bindingContext().getType(expression.getLeft());
        KotlinType rightType = context.bindingContext().getType(expression.getRight());
        if (rightType != null && KotlinBuiltIns.isCharOrNullableChar(rightType)) {
            if (leftType != null && KotlinBuiltIns.isStringOrNullableString(leftType)) {
                result = JsAstUtils.charToString(result);
            }
            else if (leftType != null && !KotlinBuiltIns.isCharOrNullableChar(leftType)) {
                result = TranslationUtils.charToBoxedChar(context, result);
            }
        }
        return result;
    }

    @NotNull
    private JsExpression translate() {
        if (PsiUtils.isAssignment(PsiUtils.getOperationToken(expression))) {
            return translateAsPlainAssignment();
        }
        return translateAsAssignmentOperation();
    }

    @NotNull
    private JsExpression translateAsAssignmentOperation() {
        if (TranslationUtils.isSimpleNameExpressionNotDelegatedLocalVar(expression.getLeft(), context()) && rightExpressionTrivial) {
            return translateAsPlainAssignmentOperation();
        }
        return translateAsAssignToCounterpart();
    }

    @NotNull
    private JsExpression translateAsAssignToCounterpart() {
        JsBinaryOperator operator = getCounterpartOperator();
        JsExpression oldValue = accessTranslator.translateAsGet();
        if (!rightExpressionTrivial) {
            oldValue = context().defineTemporary(oldValue);
        }
        JsBinaryOperation counterpartOperation = new JsBinaryOperation(operator, oldValue, right);
        context().addStatementsToCurrentBlockFrom(rightBlock);
        return accessTranslator.translateAsSet(counterpartOperation);
    }

    @NotNull
    private JsBinaryOperator getCounterpartOperator() {
        KtToken assignmentOperationToken = PsiUtils.getOperationToken(expression);
        assert assignmentOperationToken instanceof KtSingleValueToken;
        assert OperatorConventions.ASSIGNMENT_OPERATIONS.containsKey(assignmentOperationToken);
        KtToken counterpartToken = OperatorConventions.ASSIGNMENT_OPERATION_COUNTERPARTS.get(assignmentOperationToken);
        assert OperatorTable.hasCorrespondingBinaryOperator(counterpartToken) :
                "Unsupported token encountered: " + counterpartToken.toString();
        return OperatorTable.getBinaryOperator(counterpartToken);
    }

    @NotNull
    private JsExpression translateAsPlainAssignmentOperation() {
        context().addStatementsToCurrentBlockFrom(rightBlock);
        JsBinaryOperator operator = getAssignmentOperator();
        return new JsBinaryOperation(operator, accessTranslator.translateAsGet(), right);
    }

    @NotNull
    private JsBinaryOperator getAssignmentOperator() {
        KtToken token = PsiUtils.getOperationToken(expression);
        assert token instanceof KtSingleValueToken;
        assert OperatorConventions.ASSIGNMENT_OPERATIONS.containsKey(token);
        assert OperatorTable.hasCorrespondingBinaryOperator(token) :
                "Unsupported token encountered: " + token.toString();
        return OperatorTable.getBinaryOperator(token);
    }

    @NotNull
    private JsExpression translateAsPlainAssignment() {
        context().addStatementsToCurrentBlockFrom(rightBlock);
        return accessTranslator.translateAsSet(right);
    }
}
