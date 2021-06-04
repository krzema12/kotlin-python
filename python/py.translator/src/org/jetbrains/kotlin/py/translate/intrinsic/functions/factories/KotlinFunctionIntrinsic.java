/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.intrinsic.functions.factories;

import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;
import org.jetbrains.kotlin.js.backend.ast.JsExpression;
import org.jetbrains.kotlin.js.backend.ast.JsInvocation;
import org.jetbrains.kotlin.py.translate.context.Namer;
import org.jetbrains.kotlin.py.translate.context.TranslationContext;
import org.jetbrains.kotlin.py.translate.intrinsic.functions.basic.FunctionIntrinsicWithReceiverComputed;
import org.jetbrains.kotlin.py.translate.utils.JsAstUtils;
import org.jetbrains.kotlin.py.translate.utils.TranslationUtils;
import org.jetbrains.kotlin.py.translate.context.Namer;
import org.jetbrains.kotlin.py.translate.context.TranslationContext;
import org.jetbrains.kotlin.py.translate.intrinsic.functions.basic.FunctionIntrinsicWithReceiverComputed;

import java.util.ArrayList;
import java.util.List;

public class KotlinFunctionIntrinsic extends FunctionIntrinsicWithReceiverComputed {
    @NotNull
    private final String functionName;
    private final JsExpression[] additionalArguments;

    public KotlinFunctionIntrinsic(@NotNull String functionName, JsExpression... additionalArguments) {
        this.functionName = functionName;
        this.additionalArguments = additionalArguments;
    }

    @NotNull
    @Override
    public JsExpression apply(
            @Nullable JsExpression receiver,
            @NotNull List<? extends JsExpression> arguments,
            @NotNull TranslationContext context
    ) {
        JsExpression function = JsAstUtils.pureFqn(functionName, Namer.kotlinObject());
        if (additionalArguments.length > 0) {
            List<JsExpression> newArguments = new ArrayList<>(arguments);
            for (JsExpression e : additionalArguments) {
                newArguments.add(e.deepCopy());
            }
            arguments = newArguments;
        }
        return new JsInvocation(function, receiver == null ? arguments : TranslationUtils.generateInvocationArguments(receiver, arguments));
    }
}
