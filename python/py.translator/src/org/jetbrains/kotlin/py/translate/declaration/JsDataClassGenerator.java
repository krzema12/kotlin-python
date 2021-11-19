/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.declaration;

import org.jetbrains.annotations.NotNull;
import org.jetbrains.kotlin.descriptors.*;
import org.jetbrains.kotlin.js.backend.ast.*;
import org.jetbrains.kotlin.psi.KtClassOrObject;
import org.jetbrains.kotlin.psi.KtParameter;
import org.jetbrains.kotlin.py.translate.context.Namer;
import org.jetbrains.kotlin.py.translate.context.TranslationContext;
import org.jetbrains.kotlin.py.translate.utils.JsAstUtils;
import org.jetbrains.kotlin.resolve.BindingContext;
import org.jetbrains.kotlin.resolve.BindingContextUtils;
import org.jetbrains.kotlin.resolve.calls.components.ArgumentsUtilsKt;
import org.jetbrains.kotlin.resolve.source.PsiSourceElementKt;

import java.util.ArrayList;
import java.util.List;

class JsDataClassGenerator extends JsEqualsHashcodeToStringGenerator {

    JsDataClassGenerator(KtClassOrObject klass, TranslationContext context) {
        super(klass, context);
    }

    @Override
    public void generateComponentFunction(@NotNull FunctionDescriptor function, @NotNull ValueParameterDescriptor parameter) {
        PropertyDescriptor propertyDescriptor = context.bindingContext().get(BindingContext.VALUE_PARAMETER_AS_PROPERTY, parameter);
        assert propertyDescriptor != null : "Property descriptor is expected to be non-null";

        JsFunction functionObject = generateJsMethod(function);
        JsExpression returnExpression = JsAstUtils.pureFqn(context.getNameForDescriptor(propertyDescriptor), new JsThisRef());
        JsReturn returnStatement = new JsReturn(returnExpression);
        returnStatement.setSource(PsiSourceElementKt.getPsi(parameter.getSource()));
        functionObject.getBody().getStatements().add(returnStatement);
    }

    @Override
    public void generateCopyFunction(@NotNull FunctionDescriptor function, @NotNull List<? extends KtParameter> constructorParameters) {
        JsFunction functionObj = generateJsMethod(function);

        assert function.getValueParameters().size() == constructorParameters.size();

        List<JsExpression> constructorArguments = new ArrayList<>(constructorParameters.size());

        for (int i = 0; i < constructorParameters.size(); i++) {
            KtParameter constructorParam = constructorParameters.get(i);

            ValueParameterDescriptor parameterDescriptor = (ValueParameterDescriptor) BindingContextUtils.getNotNull(
                    context.bindingContext(), BindingContext.VALUE_PARAMETER, constructorParam);

            PropertyDescriptor propertyDescriptor = BindingContextUtils.getNotNull(
                    context.bindingContext(), BindingContext.VALUE_PARAMETER_AS_PROPERTY, parameterDescriptor);

            JsName fieldName = context.getNameForDescriptor(propertyDescriptor);
            JsName paramName = JsScope.declareTemporaryName(context.getNameForDescriptor(parameterDescriptor).getIdent());

            functionObj.getParameters().add(new JsParameter(paramName));

            JsExpression argumentValue;
            JsExpression parameterValue = new JsNameRef(paramName);
            if (!constructorParam.hasValOrVar()) {
                assert !ArgumentsUtilsKt.hasDefaultValue(function.getValueParameters().get(i));
                // Caller cannot rely on default value and pass undefined here.
                argumentValue = parameterValue;
            }
            else {
                JsExpression defaultCondition = JsAstUtils.equality(new JsNameRef(paramName), Namer.getUndefinedExpression());
                argumentValue = new JsConditional(defaultCondition, new JsNameRef(fieldName, new JsThisRef()), parameterValue);
            }
            constructorArguments.add(argumentValue.source(constructorParam));
        }

        ClassDescriptor classDescriptor = (ClassDescriptor) function.getContainingDeclaration();
        ClassConstructorDescriptor constructor = classDescriptor.getUnsubstitutedPrimaryConstructor();
        assert constructor != null : "Data class should have primary constructor: " + classDescriptor;

        JsExpression constructorRef = context.getInnerReference(constructor);

        JsNew returnExpression = new JsNew(constructorRef, constructorArguments);
        if (context.shouldBeDeferred(constructor)) {
            context.deferConstructorCall(constructor, returnExpression.getArguments());
        }
        returnExpression.setSource(getDeclaration());

        JsReturn returnStatement = new JsReturn(returnExpression);
        returnStatement.setSource(getDeclaration());
        functionObj.getBody().getStatements().add(returnStatement);
    }
}
