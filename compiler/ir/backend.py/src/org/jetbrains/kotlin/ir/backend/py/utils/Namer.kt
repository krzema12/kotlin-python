/*
 * Copyright 2010-2018 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.ir.backend.py.utils

object Namer {
    val OUTER_NAME = "\$outer"
    val UNREACHABLE_NAME = "\$unreachable"

    val DELEGATE = "\$delegate"

    val IMPLICIT_RECEIVER_NAME = "this"

    val PROTOTYPE_NAME = "prototype"

    val CONTINUATION = "\$cont"

    val KCALLABLE_GET_NAME = "<get-name>"
    val KCALLABLE_NAME = "callableName"
    val KPROPERTY_GET = "get"
    val KPROPERTY_SET = "set"
    const val KCALLABLE_ARITY = "\$arity"

    const val SHARED_BOX_V = "'_v'"
}