/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.extensions

import org.jetbrains.kotlin.descriptors.ClassDescriptor
import org.jetbrains.kotlin.extensions.ProjectExtensionDescriptor
import org.jetbrains.kotlin.py.translate.context.TranslationContext
import org.jetbrains.kotlin.py.translate.declaration.DeclarationBodyVisitor
import org.jetbrains.kotlin.psi.KtPureClassOrObject

interface JsSyntheticTranslateExtension {
    companion object : ProjectExtensionDescriptor<JsSyntheticTranslateExtension>(
            "org.jetbrains.kotlin.jsSyntheticTranslateExtension", JsSyntheticTranslateExtension::class.java)

    fun generateClassSyntheticParts(declaration: KtPureClassOrObject, descriptor: ClassDescriptor, translator: DeclarationBodyVisitor, context: TranslationContext)
}