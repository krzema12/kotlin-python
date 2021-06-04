/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.inline.clean

import org.jetbrains.kotlin.js.backend.ast.*
import org.jetbrains.kotlin.js.backend.ast.metadata.coroutineMetadata
import org.jetbrains.kotlin.js.backend.ast.metadata.imported


fun removeUnusedImports(fragment: JsProgramFragment, code: JsBlock) {
    val usedImports = mutableSetOf<JsName>()

    collectUsedImports(code, usedImports)

    fragment.nameBindings.retainAll { !it.name.imported || it.name in usedImports }

    val existingTags = fragment.nameBindings.map { it.key }.toSet()

    fragment.imports.entries.retainAll { (k, _) -> k in existingTags }
}

private fun collectUsedImports(root: JsNode, to: MutableSet<JsName>): Set<JsName> {
    val collector = UsedImportsCollector(to)
    root.accept(collector)

    // See StaticContext.getVariableForPropertyMetadata
    // TODO Find a better way
    val removedPseudoImports = mutableSetOf<JsName>()
    NodeRemover(JsVars::class.java) { statement ->
        if (statement.vars.size == 1) {
            val name = statement.vars[0].name
            (name.imported && name !in collector.usedImports).also {
                if (it) removedPseudoImports += name
            }
        } else {
            false
        }
    }.accept(root)
    collector.pseudoImports.forEach {
        if (it.name !in removedPseudoImports) {
            it.initExpression.accept(collector)
        }
    }

    return collector.usedImports
}

private class UsedImportsCollector(val usedImports: MutableSet<JsName>) : RecursiveJsVisitor() {

    val pseudoImports = mutableListOf<JsVars.JsVar>()

    override fun visit(x: JsVars.JsVar) {
        if (x.name.imported) {
            pseudoImports += x
        } else {
            super.visit(x)
        }
    }

    override fun visitNameRef(nameRef: JsNameRef) {
        val name = nameRef.name
        if (name != null && name.imported) {
            usedImports += name
        }
        super.visitNameRef(nameRef)
    }

    override fun visitFunction(x: JsFunction) {
        x.coroutineMetadata?.apply {
            accept(suspendObjectRef)
            accept(baseClassRef)
        }
        super.visitFunction(x)
    }
}
