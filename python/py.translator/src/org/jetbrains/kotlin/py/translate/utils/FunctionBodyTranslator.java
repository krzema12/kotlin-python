/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.utils;

import com.intellij.psi.PsiElement;
import org.jetbrains.annotations.NotNull;
import org.jetbrains.kotlin.backend.common.CodegenUtil;
import org.jetbrains.kotlin.builtins.KotlinBuiltIns;
import org.jetbrains.kotlin.descriptors.ClassDescriptor;
import org.jetbrains.kotlin.descriptors.DeclarationDescriptor;
import org.jetbrains.kotlin.descriptors.FunctionDescriptor;
import org.jetbrains.kotlin.descriptors.ValueParameterDescriptor;
import org.jetbrains.kotlin.js.backend.ast.*;
import org.jetbrains.kotlin.js.backend.ast.metadata.MetadataProperties;
import org.jetbrains.kotlin.js.naming.NameSuggestion;
import org.jetbrains.kotlin.psi.KtBlockExpression;
import org.jetbrains.kotlin.psi.KtDeclarationWithBody;
import org.jetbrains.kotlin.psi.KtExpression;
import org.jetbrains.kotlin.py.translate.context.Namer;
import org.jetbrains.kotlin.py.translate.context.TranslationContext;
import org.jetbrains.kotlin.py.translate.expression.LocalFunctionCollector;
import org.jetbrains.kotlin.py.translate.general.AbstractTranslator;
import org.jetbrains.kotlin.py.translate.general.Translation;
import org.jetbrains.kotlin.py.translate.reference.ReferenceTranslator;
import org.jetbrains.kotlin.resolve.source.PsiSourceElementKt;
import org.jetbrains.kotlin.types.KotlinType;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import static org.jetbrains.kotlin.py.translate.utils.JsAstUtils.*;
import static org.jetbrains.kotlin.py.translate.utils.mutator.LastExpressionMutator.mutateLastExpression;

public final class FunctionBodyTranslator extends AbstractTranslator {

    @NotNull
    public static JsBlock translateFunctionBody(
            @NotNull FunctionDescriptor descriptor,
            @NotNull KtDeclarationWithBody declarationWithBody,
            @NotNull TranslationContext functionBodyContext
    ) {
        Map<DeclarationDescriptor, JsExpression> aliases = new HashMap<>();
        LocalFunctionCollector functionCollector = new LocalFunctionCollector(functionBodyContext.bindingContext());
        declarationWithBody.acceptChildren(functionCollector, null);

        for (FunctionDescriptor localFunction : functionCollector.getFunctions()) {
            String localIdent = localFunction.getName().isSpecial() ? "lambda" : localFunction.getName().asString();
            JsName localName = JsScope.declareTemporaryName(NameSuggestion.sanitizeName(localIdent));
            MetadataProperties.setDescriptor(localName, localFunction);
            JsExpression alias = JsAstUtils.pureFqn(localName, null);
            aliases.put(localFunction, alias);
        }

        if (!aliases.isEmpty()) {
            functionBodyContext = functionBodyContext.innerContextWithDescriptorsAliased(aliases);
        }

        return (new FunctionBodyTranslator(descriptor, declarationWithBody, functionBodyContext)).translate();
    }

    @NotNull
    public static List<JsStatement> setDefaultValueForArguments(
            @NotNull FunctionDescriptor descriptor,
            @NotNull TranslationContext context
    ) {
        List<ValueParameterDescriptor> valueParameters = descriptor.getValueParameters();
        List<ValueParameterDescriptor> valueParametersForDefaultValue =
                CodegenUtil.getFunctionParametersForDefaultValueGeneration(descriptor, context.bindingTrace());

        List<JsStatement> result = new ArrayList<>(valueParameters.size());
        for (int i = 0; i < valueParameters.size(); i++) {
            ValueParameterDescriptor valueParameter = valueParameters.get(i);
            ValueParameterDescriptor valueParameterForDefaultValue = valueParametersForDefaultValue.get(i);

            if (!valueParameterForDefaultValue.declaresDefaultValue()) continue;

            JsExpression jsNameRef = ReferenceTranslator.translateAsValueReference(valueParameter, context);

            KtExpression defaultArgument = BindingUtils.getDefaultArgument(valueParameterForDefaultValue);
            JsBlock defaultArgBlock = new JsBlock();
            JsExpression defaultValue = Translation.translateAsExpression(defaultArgument, context, defaultArgBlock);

            // parameterName = defaultValue
            PsiElement psi = PsiSourceElementKt.getPsi(valueParameter.getSource());
            JsStatement assignStatement = assignment(jsNameRef, defaultValue).source(psi).makeStmt();

            JsStatement thenStatement = JsAstUtils.mergeStatementInBlockIfNeeded(assignStatement, defaultArgBlock);

            // parameterName === undefined
            JsBinaryOperation checkArgIsUndefined = equality(jsNameRef, Namer.getUndefinedExpression());
            checkArgIsUndefined.source(psi);

            // if (parameterName === undefined) {
            //     parameterName = defaultValue
            // }
            JsIf jsIf = JsAstUtils.newJsIf(checkArgIsUndefined, thenStatement);
            jsIf.setSource(checkArgIsUndefined.getSource());
            result.add(jsIf);
        }

        return result;
    }

    @NotNull
    private final FunctionDescriptor descriptor;
    @NotNull
    private final KtDeclarationWithBody declaration;

    private FunctionBodyTranslator(@NotNull FunctionDescriptor descriptor,
                                   @NotNull KtDeclarationWithBody declaration,
                                   @NotNull TranslationContext context) {
        super(context);
        this.descriptor = descriptor;
        this.declaration = declaration;
    }

    @NotNull
    private JsBlock translate() {
        KtExpression jetBodyExpression = declaration.getBodyExpression();
        assert jetBodyExpression != null : "Cannot translate a body of an abstract function.";
        JsBlock jsBlock = new JsBlock();


        JsNode jsBody = Translation.translateExpression(jetBodyExpression, context(), jsBlock);
        jsBlock.getStatements().addAll(mayBeWrapWithReturn(jsBody).getStatements());

        if (jetBodyExpression instanceof KtBlockExpression &&
            descriptor.getReturnType() != null && KotlinBuiltIns.isUnit(descriptor.getReturnType()) &&
            !KotlinBuiltIns.isUnit(TranslationUtils.getReturnTypeForCoercion(descriptor))) {
            ClassDescriptor unit = context().getCurrentModule().getBuiltIns().getUnit();
            JsReturn jsReturn = new JsReturn(ReferenceTranslator.translateAsValueReference(unit, context()));
            jsReturn.setSource(UtilsKt.getFinalElement(declaration));
            jsBlock.getStatements().add(jsReturn);
        }

        return jsBlock;
    }

    @NotNull
    private JsBlock mayBeWrapWithReturn(@NotNull JsNode body) {
        if (!mustAddReturnToGeneratedFunctionBody()) {
            return convertToBlock(body);
        }
        return convertToBlock(lastExpressionReturned(body));
    }

    private boolean mustAddReturnToGeneratedFunctionBody() {
        KotlinType functionReturnType = descriptor.getReturnType();
        assert functionReturnType != null : "Function return typed type must be resolved.";
        return (!declaration.hasBlockBody()) && !(KotlinBuiltIns.isUnit(functionReturnType) && !descriptor.isSuspend());
    }

    @NotNull
    private JsNode lastExpressionReturned(@NotNull JsNode body) {
        return mutateLastExpression(body, node -> {
            if (!(node instanceof JsExpression)) {
                return node;
            }

            assert declaration.getBodyExpression() != null;
            KotlinType returnType = TranslationUtils.getReturnTypeForCoercion(descriptor);
            node = TranslationUtils.coerce(context(), (JsExpression) node, returnType);

            JsReturn jsReturn = new JsReturn((JsExpression) node);
            jsReturn.setSource(declaration.getBodyExpression());
            MetadataProperties.setReturnTarget(jsReturn, descriptor);
            return jsReturn;
        });
    }
}
