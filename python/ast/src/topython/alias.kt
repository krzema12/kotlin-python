/*
 * Copyright 2010-2022 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package topython

import generated.Python.alias
import generated.Python.aliasImpl

fun alias.toPython() =
    when (this) {
        is aliasImpl -> toPython()
    }

fun aliasImpl.toPython() =
    name.name
