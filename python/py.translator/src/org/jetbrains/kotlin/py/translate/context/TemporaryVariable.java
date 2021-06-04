/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.context;

import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;
import org.jetbrains.kotlin.js.backend.ast.*;
import org.jetbrains.kotlin.js.backend.ast.metadata.MetadataProperties;
import org.jetbrains.kotlin.py.translate.utils.JsAstUtils;
import org.jetbrains.kotlin.types.KotlinType;

public class TemporaryVariable {

    /*package*/ static TemporaryVariable create(@NotNull JsName temporaryName, @Nullable JsExpression initExpression) {
        JsBinaryOperation rhs = null;
        KotlinType type = null;
        if (initExpression != null) {
            rhs = JsAstUtils.assignment(temporaryName.makeRef(), initExpression);
            rhs.source(initExpression.getSource());
            MetadataProperties.setSynthetic(rhs, true);
            type = MetadataProperties.getType(initExpression);
        }
        return new TemporaryVariable(temporaryName, rhs, type);
    }

    @Nullable
    private final JsExpression assignmentExpression;
    @NotNull
    private final JsName variableName;
    @Nullable
    private final KotlinType type;

    protected TemporaryVariable(@NotNull JsName temporaryName, @Nullable JsExpression assignmentExpression, @Nullable KotlinType type) {
        this.variableName = temporaryName;
        this.assignmentExpression = assignmentExpression;
        this.type = type;
    }

    @NotNull
    public JsNameRef reference() {
        JsNameRef result = variableName.makeRef();
        MetadataProperties.setSynthetic(result, true);
        MetadataProperties.setType(result, type);
        return result;
    }

    @NotNull
    public JsName name() {
        return variableName;
    }

    @NotNull
    public JsExpression assignmentExpression() {
        assert assignmentExpression != null;
        return assignmentExpression;
    }

    @NotNull
    public JsStatement assignmentStatement() {
        return JsAstUtils.asSyntheticStatement(assignmentExpression());
    }
}
