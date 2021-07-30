/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package topython

import generated.Python.*

fun mod.toPython(acc: StringBuilder) = when (this) {
    is Module -> toPython(acc)
    is Interactive -> TODO()
    is Expression -> TODO()
    is FunctionType -> TODO()
}

fun Module.toPython(acc: StringBuilder) {
    body.toPython("", acc)
}
