/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.reference;

import org.jetbrains.annotations.NotNull;
import org.jetbrains.kotlin.descriptors.ClassDescriptor;
import org.jetbrains.kotlin.descriptors.DeclarationDescriptor;
import org.jetbrains.kotlin.js.backend.ast.JsExpression;
import org.jetbrains.kotlin.py.translate.context.TranslationContext;
import org.jetbrains.kotlin.py.translate.general.AbstractTranslator;
import org.jetbrains.kotlin.py.translate.intrinsic.objects.ObjectIntrinsic;
import org.jetbrains.kotlin.psi.KtReferenceExpression;
import org.jetbrains.kotlin.psi.KtSimpleNameExpression;
import org.jetbrains.kotlin.py.translate.context.TranslationContext;
import org.jetbrains.kotlin.py.translate.general.AbstractTranslator;
import org.jetbrains.kotlin.py.translate.intrinsic.objects.ObjectIntrinsic;
import org.jetbrains.kotlin.py.translate.utils.BindingUtils;

import static org.jetbrains.kotlin.py.translate.utils.BindingUtils.getDescriptorForReferenceExpression;

public class CompanionObjectIntrinsicAccessTranslator extends AbstractTranslator implements AccessTranslator {
    @NotNull
    /*package*/ static CompanionObjectIntrinsicAccessTranslator newInstance(
            @NotNull KtSimpleNameExpression expression,
            @NotNull TranslationContext context
    ) {
        DeclarationDescriptor referenceDescriptor = getDescriptorForReferenceExpression(context.bindingContext(), expression);
        assert referenceDescriptor != null : "JetSimpleName expression must reference a descriptor " + expression.getText();
        return new CompanionObjectIntrinsicAccessTranslator(referenceDescriptor, context);
    }

    /*package*/ static boolean isCompanionObjectReference(
            @NotNull KtReferenceExpression expression,
            @NotNull TranslationContext context
    ) {
        DeclarationDescriptor descriptor = getDescriptorForReferenceExpression(context.bindingContext(), expression);
        return descriptor instanceof ClassDescriptor && context.intrinsics().getObjectIntrinsic((ClassDescriptor) descriptor) != null;
    }

    @NotNull
    private final JsExpression referenceToCompanionObject;

    private CompanionObjectIntrinsicAccessTranslator(@NotNull DeclarationDescriptor descriptor, @NotNull TranslationContext context) {
        super(context);
        this.referenceToCompanionObject = generateReferenceToCompanionObject(descriptor, context);
    }

    @NotNull
    private static JsExpression generateReferenceToCompanionObject(
            @NotNull DeclarationDescriptor descriptor,
            @NotNull TranslationContext context
    ) {
        ObjectIntrinsic objectIntrinsic = context.intrinsics().getObjectIntrinsic((ClassDescriptor) descriptor);
        return objectIntrinsic.apply(context);
    }

    @Override
    @NotNull
    public JsExpression translateAsGet() {
        return referenceToCompanionObject;
    }

    @Override
    @NotNull
    public JsExpression translateAsSet(@NotNull JsExpression toSetTo) {
        throw new IllegalStateException("companion object can't be set");
    }

    @NotNull
    @Override
    public AccessTranslator getCached() {
        return this;
    }
}
