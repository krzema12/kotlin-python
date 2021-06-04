/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.facade;

import org.jetbrains.annotations.NotNull;

import java.util.Collections;
import java.util.List;

public abstract class MainCallParameters {
    @NotNull
    public static MainCallParameters noCall() {
        return new MainCallParameters() {

            @NotNull
            @Override
            public List<String> arguments() {
                throw new UnsupportedOperationException("#arguments");
            }

            @Override
            public boolean shouldBeGenerated() {
                return false;
            }
        };
    }


    @NotNull
    public static MainCallParameters mainWithoutArguments() {
        return new MainCallParameters() {

            @NotNull
            @Override
            public List<String> arguments() {
                return Collections.emptyList();
            }

            @Override
            public boolean shouldBeGenerated() {
                return true;
            }
        };
    }

    @NotNull
    public static MainCallParameters mainWithArguments(@NotNull List<String> parameters) {
        return new MainCallParameters() {

            @NotNull
            @Override
            public List<String> arguments() {
                return parameters;
            }

            @Override
            public boolean shouldBeGenerated() {
                return true;
            }
        };
    }

    public abstract boolean shouldBeGenerated();

    @NotNull
    public abstract List<String> arguments();
}
