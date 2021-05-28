/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.ir.backend.js.transformers.irToPy

// The below utils are needed temporarily, to make an incomplete Python output at least valid Python.
// Thanks to this, the interpreter can run the file and we can start with implementing simpler pieces.

fun String.toValidPythonSymbol() =
    replace(Regex("[^a-zA-Z0-9_]"), "_")
        .replace(Regex("^and$"), "_and")
        .replace(Regex("^or$"), "_or")
        .replace(Regex("^with$"), "_with")
        .replace(Regex("^lambda$"), "_lambda")
        .replace(Regex("^from$"), "_from")
        .replace(Regex("^assert$"), "_assert")
        .replace(Regex("^yield$"), "_yield")

fun String.toPythonSpecific() =
    replace(Regex("^_this_$"), "self")
