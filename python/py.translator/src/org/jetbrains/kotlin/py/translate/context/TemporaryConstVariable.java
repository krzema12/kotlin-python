/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.context;

import org.jetbrains.kotlin.js.backend.ast.JsExpression;
import org.jetbrains.kotlin.js.backend.ast.JsName;
import org.jetbrains.annotations.NotNull;

public final class TemporaryConstVariable extends TemporaryVariable{
    private boolean initialized = false;

    public TemporaryConstVariable(@NotNull JsName variableName, @NotNull JsExpression assignmentExpression) {
        super(variableName, assignmentExpression, null);
    }

    @NotNull
    public JsExpression value() {
        if (initialized) {
            return reference();
        }
        initialized = true;
        return assignmentExpression();
    }
}
