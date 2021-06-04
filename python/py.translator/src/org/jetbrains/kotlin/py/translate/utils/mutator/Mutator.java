/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.utils.mutator;

import org.jetbrains.kotlin.js.backend.ast.JsNode;
import org.jetbrains.annotations.NotNull;

public interface Mutator {
    @NotNull
    JsNode mutate(@NotNull JsNode node);
}
