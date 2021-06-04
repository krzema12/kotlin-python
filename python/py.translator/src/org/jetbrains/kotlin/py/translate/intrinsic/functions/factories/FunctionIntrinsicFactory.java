/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.intrinsic.functions.factories;

import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;
import org.jetbrains.kotlin.descriptors.FunctionDescriptor;
import org.jetbrains.kotlin.py.translate.context.TranslationContext;
import org.jetbrains.kotlin.py.translate.intrinsic.functions.basic.FunctionIntrinsic;
import org.jetbrains.kotlin.py.translate.context.TranslationContext;
import org.jetbrains.kotlin.py.translate.intrinsic.functions.basic.FunctionIntrinsic;

public interface FunctionIntrinsicFactory {
    @Nullable
    FunctionIntrinsic getIntrinsic(@NotNull FunctionDescriptor descriptor, @NotNull TranslationContext context);
}
