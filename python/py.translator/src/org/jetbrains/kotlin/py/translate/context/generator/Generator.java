/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.context.generator;

import com.google.common.collect.Lists;
import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;
import org.jetbrains.kotlin.descriptors.DeclarationDescriptor;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Generator<V> {
    @NotNull
    private final Map<DeclarationDescriptor, V> values = new HashMap<>();
    @NotNull
    private final List<Rule<V>> rules = Lists.newArrayList();

    protected final void addRule(@NotNull Rule<V> rule) {
        rules.add(rule);
    }

    @Nullable
    public V get(@NotNull DeclarationDescriptor descriptor) {
        V result = values.get(descriptor);
        if (result != null) {
            return result;
        }
        result = generate(descriptor);
        values.put(descriptor, result);
        return result;
    }

    @Nullable
    private V generate(@NotNull DeclarationDescriptor descriptor) {
        for (Rule<V> rule : rules) {
            V result = rule.apply(descriptor);
            if (result != null) {
                return result;
            }
        }
        return null;
    }
}
