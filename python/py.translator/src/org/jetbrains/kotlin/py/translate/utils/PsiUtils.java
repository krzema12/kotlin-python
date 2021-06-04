/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.utils;

import com.intellij.openapi.editor.Document;
import com.intellij.psi.PsiElement;
import com.intellij.psi.PsiFile;
import com.intellij.psi.tree.IElementType;
import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;
import org.jetbrains.kotlin.descriptors.CallableDescriptor;
import org.jetbrains.kotlin.js.backend.ast.JsLocation;
import org.jetbrains.kotlin.py.sourceMap.SourceFilePathResolver;
import org.jetbrains.kotlin.lexer.KtToken;
import org.jetbrains.kotlin.lexer.KtTokens;
import org.jetbrains.kotlin.psi.*;
import org.jetbrains.kotlin.resolve.calls.model.ResolvedCall;
import org.jetbrains.kotlin.resolve.calls.model.VariableAsFunctionResolvedCall;

import java.io.File;
import java.io.IOException;
import java.util.Collections;
import java.util.List;

public final class PsiUtils {

    private PsiUtils() {
    }

    @Nullable
    public static KtSimpleNameExpression getSimpleName(@NotNull KtExpression expression) {
        if (expression instanceof KtSimpleNameExpression) {
            return (KtSimpleNameExpression) expression;
        }

        if (expression instanceof KtQualifiedExpression) {
            return getSelectorAsSimpleName((KtQualifiedExpression) expression);
        }

        return null;
    }

    @Nullable
    public static KtSimpleNameExpression getSelectorAsSimpleName(@NotNull KtQualifiedExpression expression) {
        KtExpression selectorExpression = getSelector(expression);
        if (!(selectorExpression instanceof KtSimpleNameExpression)) {
            return null;
        }
        return (KtSimpleNameExpression) selectorExpression;
    }

    @NotNull
    public static KtExpression getSelector(@NotNull KtQualifiedExpression expression) {
        KtExpression selectorExpression = expression.getSelectorExpression();
        assert selectorExpression != null : "Selector should not be null.";
        return selectorExpression;
    }

    @NotNull
    public static KtToken getOperationToken(@NotNull KtOperationExpression expression) {
        KtSimpleNameExpression operationExpression = expression.getOperationReference();
        IElementType elementType = operationExpression.getReferencedNameElementType();
        assert elementType instanceof KtToken : "Expected KtToken type, but " + elementType.getClass() + ", expression: " + expression.getText();
        return (KtToken) elementType;
    }

    @NotNull
    public static KtExpression getBaseExpression(@NotNull KtUnaryExpression expression) {
        KtExpression baseExpression = expression.getBaseExpression();
        assert baseExpression != null;
        return baseExpression;
    }

    public static boolean isPrefix(@NotNull KtUnaryExpression expression) {
        return (expression instanceof KtPrefixExpression);
    }

    public static boolean isAssignment(KtToken token) {
        return (token == KtTokens.EQ);
    }

    public static boolean isNegatedOperation(@NotNull KtBinaryExpression binaryExpression) {
        return (binaryExpression.getOperationToken() == KtTokens.EXCLEQ) || KtPsiUtil.isNotInOperation(binaryExpression);
    }

    @NotNull
    public static List<KtParameter> getPrimaryConstructorParameters(@NotNull KtPureClassOrObject classDeclaration) {
        if (classDeclaration instanceof KtClass) {
            return classDeclaration.getPrimaryConstructorParameters();
        }
        return Collections.emptyList();
    }

    @NotNull
    public static KtExpression getLoopRange(@NotNull KtForExpression expression) {
        KtExpression rangeExpression = expression.getLoopRange();
        assert rangeExpression != null;
        return rangeExpression;
    }

    @NotNull
    public static CallableDescriptor getFunctionDescriptor(ResolvedCall<?> resolvedCall) {
        if (resolvedCall instanceof VariableAsFunctionResolvedCall) {
            return  ((VariableAsFunctionResolvedCall) resolvedCall).getVariableCall().getCandidateDescriptor();
        }

        return resolvedCall.getCandidateDescriptor();
    }

    @NotNull
    public static JsLocation extractLocationFromPsi(@NotNull PsiElement element, @NotNull SourceFilePathResolver pathResolver)
            throws IOException {
        PsiFile psiFile = element.getContainingFile();
        int offset = element.getNode().getStartOffset();
        Document document = psiFile.getViewProvider().getDocument();
        assert document != null;
        int sourceLine = document.getLineNumber(offset);
        int sourceColumn = offset - document.getLineStartOffset(sourceLine);

        File file = new File(psiFile.getViewProvider().getVirtualFile().getPath());
        return new JsLocation(pathResolver.getPathRelativeToSourceRoots(file), sourceLine, sourceColumn);
    }
}
