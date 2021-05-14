/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package topython

import generated.Python.arguments
import generated.Python.argumentsImpl

fun arguments.toPython(): String {
    return when (this) {
        is argumentsImpl -> toPython()
    }
}

fun argumentsImpl.toPython() =
    (args.map { it.toPython() } + vararg?.let { listOf("*${it.toPython()}") }.orEmpty())
        .joinToString(", ")
