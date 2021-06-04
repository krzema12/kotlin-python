/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.context;

import org.jetbrains.kotlin.js.backend.ast.JsExpression;
import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;
import org.jetbrains.kotlin.descriptors.DeclarationDescriptor;
import org.jetbrains.kotlin.psi.KtExpression;

import java.util.Collections;
import java.util.Map;

public class AliasingContext {
    @NotNull
    public static AliasingContext getCleanContext() {
        return new AliasingContext(null, null, null);
    }

    @Nullable
    private final Map<DeclarationDescriptor, JsExpression> aliasesForDescriptors;

    @Nullable
    private final Map<KtExpression, JsExpression> aliasesForExpressions;

    @Nullable
    private final AliasingContext parent;

    private AliasingContext(
            @Nullable AliasingContext parent,
            @Nullable Map<DeclarationDescriptor, JsExpression> aliasesForDescriptors,
            @Nullable Map<KtExpression, JsExpression> aliasesForExpressions
    ) {
        this.parent = parent;
        this.aliasesForDescriptors = aliasesForDescriptors;
        this.aliasesForExpressions = aliasesForExpressions;
    }

    @NotNull
    public AliasingContext inner() {
        return new AliasingContext(this, null, null);
    }

    @NotNull
    public AliasingContext inner(@NotNull DeclarationDescriptor descriptor, @NotNull JsExpression alias) {
        return new AliasingContext(this, Collections.singletonMap(descriptor, alias), null);
    }

    @NotNull
    public AliasingContext withExpressionsAliased(@NotNull Map<KtExpression, JsExpression> aliasesForExpressions) {
        return new AliasingContext(this, null, aliasesForExpressions);
    }

    @NotNull
    public AliasingContext withDescriptorsAliased(@NotNull Map<DeclarationDescriptor, JsExpression> aliases) {
        return new AliasingContext(this, aliases, null);
    }

    @Nullable
    public JsExpression getAliasForDescriptor(@NotNull DeclarationDescriptor descriptor) {
        // these aliases cannot be shared and applicable only in current context
        JsExpression alias = aliasesForDescriptors != null ? aliasesForDescriptors.get(descriptor.getOriginal()) : null;
        JsExpression result = alias != null || parent == null ? alias : parent.getAliasForDescriptor(descriptor);
        return result != null ? result.deepCopy() : null;
    }

    @Nullable
    public JsExpression getAliasForExpression(@NotNull KtExpression element) {
        JsExpression alias = aliasesForExpressions != null ? aliasesForExpressions.get(element) : null;
        JsExpression result = alias != null || parent == null ? alias : parent.getAliasForExpression(element);
        return result != null ? result.deepCopy() : null;
    }
}
