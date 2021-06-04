/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.utils.mutator;

import org.jetbrains.annotations.NotNull;
import org.jetbrains.kotlin.js.backend.ast.JsExpression;
import org.jetbrains.kotlin.js.backend.ast.JsNode;
import org.jetbrains.kotlin.py.translate.context.TranslationContext;
import org.jetbrains.kotlin.py.translate.utils.TranslationUtils;
import org.jetbrains.kotlin.py.translate.context.TranslationContext;
import org.jetbrains.kotlin.py.translate.utils.TranslationUtils;
import org.jetbrains.kotlin.types.KotlinType;

public class CoercionMutator implements Mutator {
    private final KotlinType targetType;
    private final TranslationContext context;

    public CoercionMutator(@NotNull KotlinType targetType, @NotNull TranslationContext context) {
        this.targetType = targetType;
        this.context = context;
    }

    @NotNull
    @Override
    public JsNode mutate(@NotNull JsNode node) {
        if (node instanceof JsExpression) {
            return TranslationUtils.coerce(context, (JsExpression) node, targetType);
        }

        return node;
    }
}
