/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.reference;

import org.jetbrains.kotlin.js.backend.ast.JsExpression;
import org.jetbrains.annotations.NotNull;
import org.jetbrains.kotlin.py.translate.context.TranslationContext;
import org.jetbrains.kotlin.py.translate.general.Translation;
import org.jetbrains.kotlin.psi.*;
import org.jetbrains.kotlin.py.translate.context.TranslationContext;
import org.jetbrains.kotlin.py.translate.general.Translation;

import java.util.LinkedHashMap;
import java.util.Map;

public final class AccessTranslationUtils {
    private AccessTranslationUtils() {
    }

    @NotNull
    public static AccessTranslator getAccessTranslator(@NotNull KtExpression referenceExpression, @NotNull TranslationContext context) {
        return getAccessTranslator(referenceExpression, context, false);
    }

    @NotNull
    public static AccessTranslator getAccessTranslator(@NotNull KtExpression referenceExpression,
            @NotNull TranslationContext context, boolean forceOrderOfEvaluation) {
        referenceExpression = KtPsiUtil.deparenthesize(referenceExpression);
        assert referenceExpression != null;
        if (referenceExpression instanceof KtQualifiedExpression) {
            return QualifiedExpressionTranslator.getAccessTranslator((KtQualifiedExpression) referenceExpression, context, forceOrderOfEvaluation);
        }
        if (referenceExpression instanceof KtSimpleNameExpression) {
            return ReferenceTranslator.getAccessTranslator((KtSimpleNameExpression) referenceExpression, context);
        }
        if (referenceExpression instanceof KtArrayAccessExpression) {
            return getArrayAccessTranslator((KtArrayAccessExpression) referenceExpression, context, forceOrderOfEvaluation);
        }
        return new DefaultAccessTranslator(referenceExpression, context);
    }

    @NotNull
    private static AccessTranslator getArrayAccessTranslator(
            @NotNull KtArrayAccessExpression expression,
            @NotNull TranslationContext context,
            boolean forceOrderOfEvaluation
    ) {
        TranslationContext accessArrayContext;
        if (forceOrderOfEvaluation) {
            Map<KtExpression, JsExpression> indexesMap = new LinkedHashMap<>();
            for(KtExpression indexExpression : expression.getIndexExpressions()) {
                JsExpression jsIndexExpression = context.cacheExpressionIfNeeded(
                        Translation.translateAsExpression(indexExpression, context));
                indexesMap.put(indexExpression, jsIndexExpression);
            }
            accessArrayContext = context.innerContextWithAliasesForExpressions(indexesMap);
        } else {
            accessArrayContext = context;
        }

        return ArrayAccessTranslator.newInstance(expression, accessArrayContext);
    }

    @NotNull
    public static JsExpression translateAsGet(@NotNull KtExpression expression, @NotNull TranslationContext context) {
        return (getAccessTranslator(expression, context)).translateAsGet();
    }
}
