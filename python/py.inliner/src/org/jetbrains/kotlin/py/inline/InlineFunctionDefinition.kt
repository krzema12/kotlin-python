/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.inline

import org.jetbrains.kotlin.py.inline.util.FunctionWithWrapper

class InlineFunctionDefinition(
    val fn: FunctionWithWrapper,
    val tag: String?)
