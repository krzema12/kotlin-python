/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package topython

import generated.Python.arguments
import generated.Python.argumentsImpl

fun arguments.toPython(acc: StringBuilder) = when (this) {
    is argumentsImpl -> toPython(acc)
}

fun argumentsImpl.toPython(acc: StringBuilder) {
    args.forEachIndexed { i, arg ->
        if (i != 0) {
            acc.append(", ")
        }
        arg.toPython(acc)
    }
    vararg?.let {
        if (args.isNotEmpty()) {
            acc.append(", ")
        }
        acc.append('*')
        it.toPython(acc)
    }
}
