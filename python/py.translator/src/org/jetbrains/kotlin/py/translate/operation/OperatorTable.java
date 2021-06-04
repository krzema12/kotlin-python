/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.operation;

import com.google.common.collect.ImmutableBiMap;
import org.jetbrains.kotlin.js.backend.ast.JsBinaryOperator;
import org.jetbrains.kotlin.js.backend.ast.JsUnaryOperator;
import org.jetbrains.annotations.NotNull;
import org.jetbrains.kotlin.lexer.KtToken;
import org.jetbrains.kotlin.lexer.KtTokens;

import java.util.Map;

public final class OperatorTable {

    //TODO : not all operators , add and test bit operators
    private static final Map<KtToken, JsBinaryOperator> binaryOperatorsMap = ImmutableBiMap.<KtToken, JsBinaryOperator>builder()
            .put(KtTokens.PLUS, JsBinaryOperator.ADD)
            .put(KtTokens.MINUS, JsBinaryOperator.SUB)
            .put(KtTokens.MUL, JsBinaryOperator.MUL)
            .put(KtTokens.DIV, JsBinaryOperator.DIV)
            .put(KtTokens.EQ, JsBinaryOperator.ASG)
            .put(KtTokens.GT, JsBinaryOperator.GT)
            .put(KtTokens.GTEQ, JsBinaryOperator.GTE)
            .put(KtTokens.LT, JsBinaryOperator.LT)
            .put(KtTokens.LTEQ, JsBinaryOperator.LTE)
            .put(KtTokens.ANDAND, JsBinaryOperator.AND)
            .put(KtTokens.OROR, JsBinaryOperator.OR)
            .put(KtTokens.PERC, JsBinaryOperator.MOD)
            .put(KtTokens.PLUSEQ, JsBinaryOperator.ASG_ADD)
            .put(KtTokens.MINUSEQ, JsBinaryOperator.ASG_SUB)
            .put(KtTokens.DIVEQ, JsBinaryOperator.ASG_DIV)
            .put(KtTokens.MULTEQ, JsBinaryOperator.ASG_MUL)
            .put(KtTokens.PERCEQ, JsBinaryOperator.ASG_MOD)
            .put(KtTokens.IN_KEYWORD, JsBinaryOperator.INOP)
            .put(KtTokens.EQEQEQ, JsBinaryOperator.REF_EQ)
            .put(KtTokens.EXCLEQEQEQ, JsBinaryOperator.REF_NEQ)
            .build();

    private static final ImmutableBiMap<KtToken, JsUnaryOperator> unaryOperatorsMap = ImmutableBiMap.<KtToken, JsUnaryOperator>builder()
            .put(KtTokens.PLUSPLUS, JsUnaryOperator.INC)
            .put(KtTokens.MINUSMINUS, JsUnaryOperator.DEC)
            .put(KtTokens.EXCL, JsUnaryOperator.NOT)
            .put(KtTokens.MINUS, JsUnaryOperator.NEG)
            .put(KtTokens.PLUS, JsUnaryOperator.POS)
            .build();

    private OperatorTable() {
    }

    public static boolean hasCorrespondingOperator(@NotNull KtToken token) {
        return binaryOperatorsMap.containsKey(token) || unaryOperatorsMap.containsKey(token);
    }

    public static boolean hasCorrespondingBinaryOperator(@NotNull KtToken token) {
        return binaryOperatorsMap.containsKey(token);
    }

    @NotNull
    static public JsBinaryOperator getBinaryOperator(@NotNull KtToken token) {
        assert KtTokens.OPERATIONS.contains(token) : "Token should represent an operation!";
        return binaryOperatorsMap.get(token);
    }

    @NotNull
    static public JsUnaryOperator getUnaryOperator(@NotNull KtToken token) {
        assert KtTokens.OPERATIONS.contains(token) : "Token should represent an operation!";
        return unaryOperatorsMap.get(token);
    }
}
