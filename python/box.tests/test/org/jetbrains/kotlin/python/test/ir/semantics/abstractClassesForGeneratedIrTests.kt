/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.python.test.ir.semantics

import org.jetbrains.kotlin.python.test.BasicIrBoxTest

abstract class AbstractIrPythonCodegenBoxTest : BasicIrBoxTest(
    "compiler/testData/codegen/box/",
    "codegen/irBox/"
)

abstract class AbstractIrPythonCodegenBoxErrorTest : BasicIrBoxTest(
    "compiler/testData/codegen/boxError/",
    "codegen/irBoxError/"
)

abstract class AbstractIrPythonCodegenInlineTest : BasicIrBoxTest(
    "compiler/testData/codegen/boxInline/",
    "codegen/irBoxInline/"
)
