/*
 * Copyright 2010-2018 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.ir.backend.py.utils

import generated.Python.stmt
import org.jetbrains.kotlin.ir.declarations.IrDeclarationWithName
import org.jetbrains.kotlin.ir.declarations.IrFunction
import org.jetbrains.kotlin.js.backend.ast.JsName

class PyGenerationContext(
    val currentFunction: IrFunction?,
    val staticContext: PyStaticContext,
    val localNames: LocalNameGenerator,
    val definedTypes: MutableSet<String> = mutableSetOf(),
): IrNamer by staticContext {

    private val extraStatements = mutableListOf<stmt>()

    val extraStatementsSize get() = extraStatements.size

    fun addStatement(stmt: stmt) {
        extraStatements.add(stmt)
    }

    fun extractStatements(): List<stmt> {
        return extraStatements.toList().also { extraStatements.clear() }
    }

    fun newScope(): PyGenerationContext {
        return PyGenerationContext(
            currentFunction = currentFunction,
            staticContext = staticContext,
            localNames = localNames,
            definedTypes = definedTypes,
        )
    }

    fun newDeclaration(func: IrFunction? = null, localNames: LocalNameGenerator): PyGenerationContext {
        return PyGenerationContext(
            currentFunction = func,
            staticContext = staticContext,
            localNames = localNames,
            definedTypes = definedTypes,
        )
    }

    fun getNameForValueDeclaration(declaration: IrDeclarationWithName): JsName {
        val name = localNames.variableNames.names[declaration] ?: error("Variable name is not found ${declaration.name}")
        return JsName(name)
    }
}