/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.initializer;

import org.jetbrains.annotations.NotNull;
import org.jetbrains.kotlin.builtins.KotlinBuiltIns;
import org.jetbrains.kotlin.descriptors.PropertyDescriptor;
import org.jetbrains.kotlin.js.backend.ast.*;
import org.jetbrains.kotlin.py.translate.context.TranslationContext;
import org.jetbrains.kotlin.py.translate.declaration.PropertyTranslatorKt;
import org.jetbrains.kotlin.py.translate.general.TranslatorVisitor;
import org.jetbrains.kotlin.py.translate.utils.BindingUtils;
import org.jetbrains.kotlin.py.translate.utils.JsAstUtils;
import org.jetbrains.kotlin.py.translate.utils.JsDescriptorUtils;
import org.jetbrains.kotlin.py.translate.utils.TranslationUtils;
import org.jetbrains.kotlin.psi.*;
import org.jetbrains.kotlin.py.translate.context.TranslationContext;
import org.jetbrains.kotlin.py.translate.general.Translation;
import org.jetbrains.kotlin.py.translate.general.TranslatorVisitor;
import org.jetbrains.kotlin.py.translate.utils.BindingUtils;
import org.jetbrains.kotlin.py.translate.utils.JsAstUtils;
import org.jetbrains.kotlin.py.translate.utils.JsDescriptorUtils;
import org.jetbrains.kotlin.py.translate.utils.TranslationUtils;
import org.jetbrains.kotlin.resolve.BindingContext;
import org.jetbrains.kotlin.types.KotlinType;

import static org.jetbrains.kotlin.py.translate.general.Translation.translateAsStatementAndMergeInBlockIfNeeded;
import static org.jetbrains.kotlin.py.translate.initializer.InitializerUtils.generateInitializerForDelegate;
import static org.jetbrains.kotlin.py.translate.initializer.InitializerUtils.generateInitializerForProperty;

public final class InitializerVisitor extends TranslatorVisitor<Void> {
    @Override
    protected Void emptyResult(@NotNull TranslationContext context) {
        return null;
    }

    @Override
    public final Void visitProperty(@NotNull KtProperty property, @NotNull TranslationContext context) {
        PropertyDescriptor descriptor = BindingUtils.getPropertyDescriptor(context.bindingContext(), property);
        JsExpression value = PropertyTranslatorKt.translateDelegateOrInitializerExpression(context, property);
        JsStatement statement = null;

        KtExpression initializer = property.getInitializer();
        KtExpression delegate = property.getDelegateExpression();
        if (initializer != null) {
            assert value != null;
            KotlinType type = TranslationUtils.isReferenceToSyntheticBackingField(descriptor) ?
                              descriptor.getType() :
                              TranslationUtils.getReturnTypeForCoercion(descriptor);
            value = TranslationUtils.coerce(context, value, type);
            statement = InitializerUtils.generateInitializerForProperty(context, descriptor, value);
        }
        else if (delegate != null) {
            assert value != null;
            statement = InitializerUtils.generateInitializerForDelegate(context, descriptor, value);
        }
        else if (Boolean.TRUE.equals(context.bindingContext().get(BindingContext.BACKING_FIELD_REQUIRED, descriptor))) {
            JsNameRef backingFieldReference = TranslationUtils.backingFieldReference(context, descriptor);
            JsExpression defaultValue = generateDefaultValue(descriptor, backingFieldReference);
            statement = TranslationUtils.assignmentToBackingField(context, descriptor, defaultValue).source(property).makeStmt();
        }
        else if (JsDescriptorUtils.isSimpleFinalProperty(descriptor)) {
            JsNameRef propRef = new JsNameRef(context.getNameForDescriptor(descriptor), new JsThisRef());
            JsExpression defaultValue = generateDefaultValue(descriptor, propRef);
            statement = JsAstUtils.assignment(propRef, defaultValue).source(property).makeStmt();
        }

        if (statement != null && !JsAstUtils.isEmptyStatement(statement)) {
            context.addStatementsToCurrentBlock(JsAstUtils.flattenStatement(statement));
        }

        return null;
    }

    @NotNull
    private static JsExpression generateDefaultValue(
            @NotNull PropertyDescriptor property,
            @NotNull JsExpression lateInitDefault
    ) {
        if (property.isLateInit()) return lateInitDefault.deepCopy();

        KotlinType type = property.getType();
        if (KotlinBuiltIns.isInt(type) || KotlinBuiltIns.isFloat(type) || KotlinBuiltIns.isDouble(type) ||
            KotlinBuiltIns.isByte(type) || KotlinBuiltIns.isShort(type)
        ) {
            return new JsIntLiteral(0);
        }
        else if (KotlinBuiltIns.isBoolean(type)) {
            return new JsBooleanLiteral(false);
        }
        else {
            return new JsNullLiteral();
        }
    }

    @Override
    public Void visitAnonymousInitializer(@NotNull KtAnonymousInitializer initializer, @NotNull TranslationContext context) {
        KtExpression initializerBody = initializer.getBody();
        if (initializerBody != null) {
            context.addStatementsToCurrentBlock(JsAstUtils.flattenStatement(
                    Translation.translateAsStatementAndMergeInBlockIfNeeded(initializerBody, context)));
        }
        return null;
    }

    @Override
    // Not interested in other types of declarations, they do not contain initializers.
    public Void visitDeclaration(@NotNull KtDeclaration expression, @NotNull TranslationContext context) {
        return null;
    }

    @Override
    public Void visitSecondaryConstructor(@NotNull KtSecondaryConstructor constructor, TranslationContext data) {
        return null;
    }
}
