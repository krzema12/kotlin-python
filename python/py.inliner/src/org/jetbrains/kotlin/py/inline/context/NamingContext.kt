/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.inline.context

import org.jetbrains.kotlin.js.backend.ast.*
import org.jetbrains.kotlin.js.backend.ast.metadata.synthetic
import org.jetbrains.kotlin.py.inline.util.replaceNames
import org.jetbrains.kotlin.py.translate.utils.JsAstUtils

class NamingContext(private val previousStatements: MutableList<JsStatement>) {
    private val renamings = mutableMapOf<JsName, JsNameRef>()
    private val declarations = mutableListOf<JsVars>()
    private var addedDeclarations = false

    fun applyRenameTo(target: JsNode): JsNode {
        if (!addedDeclarations) {
            previousStatements.addAll(declarations)
            addedDeclarations = true
        }

        return replaceNames(target, renamings)
    }

    fun replaceName(name: JsName, replacement: JsNameRef) {
        assert(!renamings.containsKey(name)) { "$name has been renamed already" }

        renamings.put(name, replacement)
    }

    fun newVar(name: JsName, value: JsExpression? = null, source: Any?) {
        val vars = JsAstUtils.newVar(name, value)
        vars.synthetic = true
        vars.source = source
        declarations.add(vars)
    }
}
