/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package topython

import generated.Python.*

fun mod.toPython(): String {
    return when (this) {
        is Module -> toPython()
        is Interactive -> TODO()
        is Expression -> TODO()
        is FunctionType -> TODO()
    }
}

fun Module.toPython() =
    body.joinToString("\n") { it.toPython() }
