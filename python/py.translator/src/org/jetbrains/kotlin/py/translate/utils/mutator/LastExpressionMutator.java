/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.utils.mutator;

import org.jetbrains.annotations.NotNull;
import org.jetbrains.kotlin.js.backend.ast.*;
import org.jetbrains.kotlin.py.translate.utils.JsAstUtils;

import java.util.List;

import static org.jetbrains.kotlin.py.translate.utils.JsAstUtils.convertToStatement;

public final class LastExpressionMutator {
    public static JsStatement mutateLastExpression(@NotNull JsNode node, @NotNull Mutator mutator) {
        return JsAstUtils.convertToStatement(new LastExpressionMutator(mutator).apply(node));
    }

    @NotNull
    private final Mutator mutator;

    private LastExpressionMutator(@NotNull Mutator mutator) {
        this.mutator = mutator;
    }

    //TODO: visitor?
    //TODO: when expression?
    @NotNull
    private JsNode apply(@NotNull JsNode node) {
        if (node instanceof JsBlock) {
            return applyToBlock((JsBlock) node);
        }
        if (node instanceof JsIf) {
            return applyToIf((JsIf) node);
        }
        if (node instanceof JsTry) {
            return applyToTry((JsTry) node);
        }
        if (node instanceof JsExpressionStatement) {
            return applyToStatement((JsExpressionStatement) node);
        }
        if (node instanceof JsSwitch) {
            return applyToSwitch((JsSwitch) node);
        }
        return mutator.mutate(node);
    }

    @NotNull
    private JsNode applyToStatement(@NotNull JsExpressionStatement node) {
        return JsAstUtils.convertToStatement(apply(node.getExpression()));
    }

    @NotNull
    private JsNode applyToIf(@NotNull JsIf node) {
        node.setThenStatement(JsAstUtils.convertToStatement(apply(node.getThenStatement())));
        JsStatement elseStmt = node.getElseStatement();
        if (elseStmt != null) {
            node.setElseStatement(JsAstUtils.convertToStatement(apply(elseStmt)));
        }
        return node;
    }

    @NotNull
    private JsNode applyToTry(@NotNull JsTry node) {
        applyToBlock(node.getTryBlock());
        for(JsCatch jsCatch: node.getCatches()) {
            applyToBlock(jsCatch.getBody());
        }
        return node;
    }

    @NotNull
    private JsNode applyToBlock(@NotNull JsBlock node) {
        List<JsStatement> statements = node.getStatements();

        if (statements.isEmpty()) return node;

        int size = statements.size();
        statements.set(size - 1, JsAstUtils.convertToStatement(apply(statements.get(size - 1))));
        return node;
    }

    @NotNull
    private JsNode applyToSwitch(@NotNull JsSwitch node) {
        for (JsSwitchMember member : node.getCases()) {
            int size = member.getStatements().size();
            if (size < 2) continue;

            JsNode lastStatement = apply(member.getStatements().get(size - 1));
            if (!(lastStatement instanceof JsBreak)) continue;

            member.getStatements().set(size - 2, JsAstUtils.convertToStatement(apply(member.getStatements().get(size - 2))));
        }

        return node;
    }
}
