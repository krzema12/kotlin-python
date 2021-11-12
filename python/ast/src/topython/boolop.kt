/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package topython

import generated.Python.And
import generated.Python.Or
import generated.Python.boolop

fun boolop.toPython(): String = when (this) {
    And -> "and"
    Or -> "or"
}
