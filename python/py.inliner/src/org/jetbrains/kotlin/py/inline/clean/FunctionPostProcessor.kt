/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.inline.clean

import org.jetbrains.kotlin.js.backend.ast.JsFunction

class FunctionPostProcessor(val root: JsFunction) {
    val optimizations = listOf(
        //{ TemporaryAssignmentElimination(root.body).apply() },
        { RedundantLabelRemoval(root.body).apply() },
        { EmptyStatementElimination(root.body).apply() },
        { WhileConditionFolding(root.body).apply() },
        { DoWhileGuardElimination(root.body).apply() },
        { TemporaryVariableElimination(root).apply() },
        { RedundantCallElimination(root.body).apply() },
        { IfStatementReduction(root.body).apply() },
        { DeadCodeElimination(root.body).apply() },
        { RedundantVariableDeclarationElimination(root.body).apply() },
        { RedundantStatementElimination(root).apply() },
        { CoroutineStateElimination(root.body).apply() }
    )
    // TODO: reduce to A || B, A && B if possible

    fun apply() {
        do {
            var hasChanges = false
            for (opt in optimizations) {
                hasChanges = hasChanges or opt()
            }
        } while (hasChanges)
    }
}
