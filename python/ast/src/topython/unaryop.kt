/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package topython

import generated.Python.*

fun unaryop.toPython(): String = when (this) {
    Invert -> "~"
    Not -> "not "
    UAdd -> "+"
    USub -> "-"
}
