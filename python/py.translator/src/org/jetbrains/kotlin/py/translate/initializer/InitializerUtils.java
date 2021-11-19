/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.initializer;

import org.jetbrains.annotations.NotNull;
import org.jetbrains.kotlin.descriptors.PropertyDescriptor;
import org.jetbrains.kotlin.js.backend.ast.JsExpression;
import org.jetbrains.kotlin.js.backend.ast.JsStatement;
import org.jetbrains.kotlin.py.translate.context.TranslationContext;
import org.jetbrains.kotlin.py.translate.utils.JsAstUtils;
import org.jetbrains.kotlin.resolve.source.PsiSourceElementKt;

import static org.jetbrains.kotlin.py.translate.utils.TranslationUtils.assignmentToBackingField;

public final class InitializerUtils {
    private InitializerUtils() {
    }

    @NotNull
    public static JsStatement generateInitializerForProperty(
            @NotNull TranslationContext context,
            @NotNull PropertyDescriptor descriptor,
            @NotNull JsExpression value
    ) {
        JsExpression assignment = assignmentToBackingField(context, descriptor, value);
        assignment.setSource(PsiSourceElementKt.getPsi(descriptor.getSource()));
        return assignment.makeStmt();
    }

    @NotNull
    public static JsStatement generateInitializerForDelegate(
            @NotNull TranslationContext context,
            @NotNull PropertyDescriptor descriptor,
            @NotNull JsExpression value
    ) {
        return JsAstUtils.defineSimpleProperty(context.getNameForBackingField(descriptor), value, descriptor.getSource());
    }
}
