/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package asdl

// Based on https://www.usenix.org/legacy/publications/library/proceedings/dsl97/full_papers/wang/wang.pdf

data class AsdlModule(
    val name: String,
    val types: List<AsdlType>,
)

data class AsdlType(
    val name: String,
    val constructors: List<AsdlConstructor> = emptyList(),
    val attributes: List<AsdlAttribute> = emptyList(),
)

data class AsdlConstructor(
    val name: String,
    val attributes: List<AsdlAttribute> = emptyList(),
)

data class AsdlAttribute(
    val name: String,
    val type: AsdlType,
    val quantity: AsdlQuantity = AsdlQuantity.Single,
)

enum class AsdlQuantity {
    Single,
    Optional,
    ZeroOrMore,
}
