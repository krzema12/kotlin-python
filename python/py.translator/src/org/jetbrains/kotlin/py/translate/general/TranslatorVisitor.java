/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.general;

import org.jetbrains.annotations.NotNull;
import org.jetbrains.kotlin.js.resolve.diagnostics.ErrorsJs;
import org.jetbrains.kotlin.py.translate.context.TranslationContext;
import org.jetbrains.kotlin.psi.KtDeclaration;
import org.jetbrains.kotlin.psi.KtDeclarationContainer;
import org.jetbrains.kotlin.psi.KtElement;
import org.jetbrains.kotlin.psi.KtVisitor;

/**
 * This class is a base class for all visitors.
 */
public abstract class TranslatorVisitor<T> extends KtVisitor<T, TranslationContext> {

    protected abstract T emptyResult(@NotNull TranslationContext context);

    @Override
    public T visitKtElement(@NotNull KtElement expression, TranslationContext context) {
        context.bindingTrace().report(ErrorsJs.NOT_SUPPORTED.on(expression, expression));
        return emptyResult(context);
    }

    public final void traverseContainer(@NotNull KtDeclarationContainer jetClass,
            @NotNull TranslationContext context) {
        for (KtDeclaration declaration : jetClass.getDeclarations()) {
            declaration.accept(this, context);
        }
    }
}
