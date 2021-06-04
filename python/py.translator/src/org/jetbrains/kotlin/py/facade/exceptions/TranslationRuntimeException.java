/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.facade.exceptions;

import com.intellij.psi.PsiElement;
import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;
import org.jetbrains.kotlin.psi.psiUtil.PsiUtilsKt;

public class TranslationRuntimeException extends RuntimeException {
    public TranslationRuntimeException(@NotNull PsiElement element, @Nullable Throwable cause) {
        super("Unexpected error occurred compiling the following fragment: " + PsiUtilsKt.getTextWithLocation(element), cause);
    }
}
