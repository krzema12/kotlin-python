/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.context;

import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;
import org.jetbrains.kotlin.js.backend.ast.*;
import org.jetbrains.kotlin.js.backend.ast.metadata.MetadataProperties;

import static org.jetbrains.kotlin.js.backend.ast.JsVars.JsVar;

//TODO: consider renaming to scoping context
public final class DynamicContext {
    @NotNull
    public static DynamicContext rootContext(@NotNull JsScope rootScope, @NotNull JsBlock globalBlock) {
        return new DynamicContext(rootScope, globalBlock);
    }

    @NotNull
    public static DynamicContext newContext(@NotNull JsScope scope, @NotNull JsBlock block) {
        return new DynamicContext(scope, block);
    }

    @NotNull
    private final JsScope currentScope;

    @NotNull
    private final JsBlock currentBlock;

    @Nullable
    private JsVars vars;

    private DynamicContext(@NotNull JsScope scope, @NotNull JsBlock block) {
        this.currentScope = scope;
        this.currentBlock = block;
    }

    @NotNull
    public DynamicContext innerBlock(@NotNull JsBlock block) {
        return new DynamicContext(currentScope, block);
    }

    @NotNull
    public TemporaryVariable declareTemporary(@Nullable JsExpression initExpression, @Nullable Object sourceInfo) {
        if (vars == null) {
            vars = new JsVars();
            MetadataProperties.setSynthetic(vars, true);
            currentBlock.getStatements().add(vars);
            vars.setSource(sourceInfo);
        }

        JsName temporaryName = JsScope.declareTemporary();
        JsVar var = new JsVar(temporaryName, null);
        var.setSource(sourceInfo);
        MetadataProperties.setSynthetic(var, true);
        vars.add(var);
        if (initExpression != null) {
            var.source(initExpression.getSource());
        }
        return TemporaryVariable.create(temporaryName, initExpression);
    }

    void moveVarsFrom(@NotNull DynamicContext dynamicContext) {
        if (dynamicContext.vars != null) {
            if (vars == null) {
                vars = dynamicContext.vars;
                currentBlock.getStatements().add(vars);
            } else {
                vars.addAll(dynamicContext.vars);
            }
            dynamicContext.currentBlock.getStatements().remove(dynamicContext.vars);
            dynamicContext.vars = null;
        }
    }

    @NotNull
    public JsScope getScope() {
        return currentScope;
    }

    @NotNull
    public JsBlock jsBlock() {
        return currentBlock;
    }
}
