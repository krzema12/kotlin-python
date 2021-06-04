/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.reference;

import org.jetbrains.kotlin.js.backend.ast.JsExpression;
import org.jetbrains.annotations.NotNull;
import org.jetbrains.kotlin.py.translate.context.TranslationContext;
import org.jetbrains.kotlin.py.translate.general.Translation;
import org.jetbrains.kotlin.psi.KtExpression;
import org.jetbrains.kotlin.py.translate.context.TranslationContext;
import org.jetbrains.kotlin.py.translate.general.Translation;

public class DefaultAccessTranslator implements AccessTranslator {
    private final KtExpression expression;
    private final TranslationContext context;

    public DefaultAccessTranslator(@NotNull KtExpression expression, @NotNull TranslationContext context) {
        this.expression = expression;
        this.context = context;
    }

    @NotNull
    @Override
    public JsExpression translateAsGet() {
        return Translation.translateAsExpression(expression, context);
    }

    @NotNull
    @Override
    public JsExpression translateAsSet(@NotNull JsExpression setTo) {
        throw new UnsupportedOperationException("This method is not meant to be supported in in DefaultAccessTranslator");
    }

    @NotNull
    @Override
    public AccessTranslator getCached() {
        throw new UnsupportedOperationException("This method is not meant to be supported in in DefaultAccessTranslator");
    }
}
