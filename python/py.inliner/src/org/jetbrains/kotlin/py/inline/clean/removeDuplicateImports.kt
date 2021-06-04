/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.inline.clean

import org.jetbrains.kotlin.js.backend.ast.*
import org.jetbrains.kotlin.py.inline.util.getImportTag
import org.jetbrains.kotlin.py.inline.util.replaceNames

fun removeDuplicateImports(node: JsNode) {
    node.accept(object : RecursiveJsVisitor() {
        override fun visitBlock(x: JsBlock) {
            super.visitBlock(x)
            removeDuplicateImports(x.statements)
        }
    })
}

private fun removeDuplicateImports(statements: MutableList<JsStatement>) {
    val existingImports = mutableMapOf<String, JsName>()
    val replacements = mutableMapOf<JsName, JsExpression>()
    removeDuplicateImports(statements, existingImports, replacements)

    for (statement in statements) {
        replaceNames(statement, replacements)
    }
}

private fun removeDuplicateImports(
    statements: MutableList<JsStatement>,
    existingImports: MutableMap<String, JsName>,
    replacements: MutableMap<JsName, JsExpression>
) {
    var index = 0
    while (index < statements.size) {
        val statement = statements[index]
        if (statement is JsVars) {
            val importTag = getImportTag(statement)
            if (importTag != null) {
                val name = statement.vars[0].name
                val existingName = existingImports[importTag]
                if (existingName != null) {
                    replacements[name] = existingName.makeRef()
                    statements.removeAt(index)
                    continue
                }
                else {
                    existingImports[importTag] = name
                }
            }
        }
        else if (statement is JsBlock) {
            removeDuplicateImports(statement.statements, existingImports, replacements)
        }

        index++
    }
}
