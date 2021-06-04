/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.intrinsic.functions.factories;

import com.google.common.collect.Lists;
import com.intellij.openapi.util.Pair;
import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;
import org.jetbrains.kotlin.descriptors.FunctionDescriptor;
import org.jetbrains.kotlin.py.translate.context.TranslationContext;
import org.jetbrains.kotlin.py.translate.intrinsic.functions.basic.FunctionIntrinsic;
import org.jetbrains.kotlin.py.translate.context.TranslationContext;
import org.jetbrains.kotlin.py.translate.intrinsic.functions.basic.FunctionIntrinsic;

import java.util.List;
import java.util.function.Predicate;

public abstract class CompositeFIF implements FunctionIntrinsicFactory {
    @NotNull
    private final List<Pair<Predicate<FunctionDescriptor>, FunctionIntrinsic>> patternsAndIntrinsics = Lists.newArrayList();

    protected CompositeFIF() {
    }

    @Nullable
    @Override
    public FunctionIntrinsic getIntrinsic(@NotNull FunctionDescriptor descriptor, @NotNull TranslationContext context) {
        for (Pair<Predicate<FunctionDescriptor>, FunctionIntrinsic> entry : patternsAndIntrinsics) {
            if (entry.first.test(descriptor)) {
                return entry.second;
            }
        }
        return null;
    }

    protected void add(@NotNull Predicate<FunctionDescriptor> pattern, @NotNull FunctionIntrinsic intrinsic) {
        patternsAndIntrinsics.add(Pair.create(pattern, intrinsic));
    }
}
