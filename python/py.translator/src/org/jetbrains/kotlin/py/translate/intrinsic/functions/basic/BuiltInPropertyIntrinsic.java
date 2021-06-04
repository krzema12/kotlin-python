/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.intrinsic.functions.basic;

import org.jetbrains.kotlin.js.backend.ast.JsExpression;
import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;
import org.jetbrains.kotlin.py.translate.context.TranslationContext;
import org.jetbrains.kotlin.py.translate.utils.JsAstUtils;

import java.util.List;

//TODO: find should be usages
public final class BuiltInPropertyIntrinsic extends FunctionIntrinsicWithReceiverComputed {

    @NotNull
    private final String propertyName;

    public BuiltInPropertyIntrinsic(@NotNull String propertyName) {
        this.propertyName = propertyName;
    }

    @NotNull
    @Override
    public JsExpression apply(@Nullable JsExpression receiver, @NotNull List<? extends JsExpression> arguments,
                              @NotNull TranslationContext context) {
        assert receiver != null;
        assert arguments.isEmpty() : "Properties can't have arguments.";
        return JsAstUtils.pureFqn(propertyName, receiver);
    }
}
