/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.reference;

import org.jetbrains.kotlin.js.backend.ast.JsExpression;
import org.jetbrains.annotations.NotNull;
import org.jetbrains.kotlin.descriptors.PropertyDescriptor;
import org.jetbrains.kotlin.descriptors.impl.SyntheticFieldDescriptorKt;
import org.jetbrains.kotlin.py.translate.context.TranslationContext;
import org.jetbrains.kotlin.py.translate.general.AbstractTranslator;
import org.jetbrains.kotlin.psi.KtSimpleNameExpression;
import org.jetbrains.kotlin.py.translate.context.TranslationContext;
import org.jetbrains.kotlin.py.translate.general.AbstractTranslator;
import org.jetbrains.kotlin.py.translate.utils.BindingUtils;
import org.jetbrains.kotlin.py.translate.utils.TranslationUtils;

import static org.jetbrains.kotlin.py.translate.utils.BindingUtils.getDescriptorForReferenceExpression;
import static org.jetbrains.kotlin.py.translate.utils.TranslationUtils.assignmentToBackingField;
import static org.jetbrains.kotlin.py.translate.utils.TranslationUtils.backingFieldReference;

public final class BackingFieldAccessTranslator extends AbstractTranslator implements AccessTranslator {

    @NotNull
    private final PropertyDescriptor descriptor;

    /*package*/
    public static BackingFieldAccessTranslator newInstance(@NotNull KtSimpleNameExpression expression,
                                                    @NotNull TranslationContext context) {
        PropertyDescriptor referencedProperty = SyntheticFieldDescriptorKt.getReferencedProperty(
                getDescriptorForReferenceExpression(context.bindingContext(), expression)
        );
        assert referencedProperty != null;
        return new BackingFieldAccessTranslator(referencedProperty, context);
    }

    private BackingFieldAccessTranslator(@NotNull PropertyDescriptor descriptor, @NotNull TranslationContext context) {
        super(context);
        this.descriptor = descriptor;
    }

    @NotNull
    @Override
    public JsExpression translateAsGet() {
        return backingFieldReference(context(), descriptor);
    }

    @NotNull
    @Override
    public JsExpression translateAsSet(@NotNull JsExpression setTo) {
        return assignmentToBackingField(context(), descriptor, setTo);
    }

    @NotNull
    @Override
    public AccessTranslator getCached() {
        return this;
    }
}
