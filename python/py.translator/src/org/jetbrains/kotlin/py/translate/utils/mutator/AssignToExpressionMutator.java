/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.utils.mutator;

import org.jetbrains.kotlin.js.backend.ast.JsExpression;
import org.jetbrains.kotlin.js.backend.ast.JsNode;
import org.jetbrains.annotations.NotNull;
import org.jetbrains.kotlin.py.translate.utils.JsAstUtils;

import static org.jetbrains.kotlin.py.translate.utils.JsAstUtils.assignment;

public final class AssignToExpressionMutator implements Mutator {

    @NotNull
    private final JsExpression toAssign;

    public AssignToExpressionMutator(@NotNull JsExpression toAssign) {
        this.toAssign = toAssign;
    }

    @NotNull
    @Override
    public JsNode mutate(@NotNull JsNode node) {
        if (!(node instanceof JsExpression)) {
            return node;
        }
        JsExpression result = JsAstUtils.assignment(toAssign, (JsExpression) node);
        result.setSource(node.getSource());
        return result;
    }
}
