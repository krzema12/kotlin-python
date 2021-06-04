/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.utils;

import com.intellij.psi.PsiElement;
import org.jetbrains.annotations.NotNull;
import org.jetbrains.kotlin.descriptors.DeclarationDescriptor;
import org.jetbrains.kotlin.diagnostics.DiagnosticUtils;
import org.jetbrains.kotlin.diagnostics.PsiDiagnosticUtils;
import org.jetbrains.kotlin.psi.KtExpression;

public final class ErrorReportingUtils {
    private ErrorReportingUtils() {
    }

    @NotNull
    public static RuntimeException reportErrorWithLocation(@NotNull KtExpression selector, @NotNull RuntimeException e) {
        return reportErrorWithLocation(e, PsiDiagnosticUtils.atLocation(selector));
    }

    @NotNull
    private static RuntimeException reportErrorWithLocation(@NotNull RuntimeException e, @NotNull String location) {
        throw new RuntimeException(e.getMessage() + " at " + location, e);
    }

    @NotNull
    public static String message(@NotNull PsiElement expression, @NotNull String messageText) {
        return messageText + " at " + PsiDiagnosticUtils.atLocation(expression) + ".";
    }

    @NotNull
    public static String message(@NotNull DeclarationDescriptor descriptor, @NotNull String explainingMessage) {
        return explainingMessage + " at " + DiagnosticUtils.atLocation(descriptor) + ".";
    }

    @NotNull
    public static String message(@NotNull PsiElement element) {
        return "Error at " + PsiDiagnosticUtils.atLocation(element) + ".";
    }
}
