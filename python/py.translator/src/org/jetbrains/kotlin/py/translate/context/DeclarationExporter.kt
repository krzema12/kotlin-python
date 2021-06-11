/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.context

import org.jetbrains.kotlin.descriptors.*
import org.jetbrains.kotlin.js.backend.ast.*
import org.jetbrains.kotlin.js.backend.ast.metadata.exportedTag
import org.jetbrains.kotlin.js.backend.ast.metadata.staticRef
import org.jetbrains.kotlin.js.descriptorUtils.shouldBeExported
import org.jetbrains.kotlin.js.translate.utils.AnnotationsUtils.isLibraryObject
import org.jetbrains.kotlin.js.translate.utils.AnnotationsUtils.isNativeObject
import org.jetbrains.kotlin.py.translate.utils.JsAstUtils
import org.jetbrains.kotlin.py.translate.utils.JsAstUtils.assignment
import org.jetbrains.kotlin.py.translate.utils.JsDescriptorUtils
import org.jetbrains.kotlin.py.translate.utils.TranslationUtils
import org.jetbrains.kotlin.py.translate.utils.definePackageAlias
import org.jetbrains.kotlin.name.FqName
import org.jetbrains.kotlin.resolve.DescriptorUtils
import org.jetbrains.kotlin.resolve.inline.isEffectivelyInlineOnly
import org.jetbrains.kotlin.resolve.source.getPsi

internal class DeclarationExporter(val context: StaticContext) {
    private val objectLikeKinds = setOf(ClassKind.OBJECT, ClassKind.ENUM_ENTRY)
    private val exportedDeclarations = mutableSetOf<MemberDescriptor>()
    private val localPackageNames = mutableMapOf<FqName, JsName>()
    private val statements: MutableList<JsStatement>
        get() = context.fragment.exportBlock.statements

    fun export(descriptor: MemberDescriptor, force: Boolean) {
        if (exportedDeclarations.contains(descriptor)) return
        if (descriptor is ConstructorDescriptor && descriptor.isPrimary) return
        if (isNativeObject(descriptor) || isLibraryObject(descriptor)) return
        if (descriptor.isEffectivelyInlineOnly()) return

        val suggestedName = context.nameSuggestion.suggest(descriptor, context.bindingContext) ?: return

        val container = suggestedName.scope
        if (!descriptor.shouldBeExported(force)) return
        exportedDeclarations.add(descriptor)

        val qualifier = when {
            container is PackageFragmentDescriptor -> {
                getLocalPackageName(container.fqName).makeRef()
            }
            DescriptorUtils.isObject(container) -> {
                JsAstUtils.prototypeOf(context.getInnerNameForDescriptor(container).makeRef())
            }
            else -> {
                context.getInnerNameForDescriptor(container).makeRef()
            }
        }

        when {
            descriptor is ClassDescriptor && descriptor.kind in objectLikeKinds -> {
                exportObject(descriptor, qualifier)
            }
            descriptor is PropertyDescriptor && container is PackageFragmentDescriptor -> {
                exportProperty(descriptor, qualifier)
            }
            else -> {
                assign(descriptor, qualifier)
            }
        }
    }

    private fun assign(descriptor: DeclarationDescriptor, qualifier: JsExpression) {
        val exportedName = context.getInnerNameForDescriptor(descriptor)
        val expression = exportedName.makeRef()
        val propertyName = context.getNameForDescriptor(descriptor)
        if (propertyName.staticRef == null && exportedName != propertyName) {
            propertyName.staticRef = expression
        }
        statements += assignment(JsNameRef(propertyName, qualifier), expression).exportStatement(descriptor)
    }

    private fun exportObject(declaration: ClassDescriptor, qualifier: JsExpression) {
        val name = context.getNameForDescriptor(declaration)
        val expression = JsAstUtils.defineGetter(qualifier, name.ident,
                                                 context.getNameForObjectInstance(declaration).makeRef())
        statements += expression.exportStatement(declaration)
    }

    private fun exportProperty(declaration: PropertyDescriptor, qualifier: JsExpression) {
        val propertyLiteral = JsObjectLiteral(true)

        val name = context.getNameForDescriptor(declaration).ident
        val simpleProperty = JsDescriptorUtils.isSimpleFinalProperty(declaration) &&
                             !TranslationUtils.shouldAccessViaFunctions(declaration)

        val exportedName: JsName
        val getterBody: JsExpression = if (simpleProperty) {
            exportedName = context.getInnerNameForDescriptor(declaration)
            val accessToField = JsReturn(exportedName.makeRef())
            JsFunction(context.fragment.scope, JsBlock(accessToField), "$declaration getter")
        }
        else {
            exportedName = context.getInnerNameForDescriptor(declaration.getter!!)
            exportedName.makeRef()
        }
        propertyLiteral.propertyInitializers += JsPropertyInitializer(JsNameRef("get"), getterBody)

        if (declaration.isVar) {
            val setterBody: JsExpression = if (simpleProperty) {
                val statements = mutableListOf<JsStatement>()
                val function = JsFunction(context.fragment.scope, JsBlock(statements), "$declaration setter")
                function.source = declaration.source.getPsi()
                val valueName = JsScope.declareTemporaryName("value")
                function.parameters += JsParameter(valueName)
                statements += assignment(context.getInnerNameForDescriptor(declaration).makeRef(), valueName.makeRef()).makeStmt()
                function
            }
            else {
                context.getInnerNameForDescriptor(declaration.setter!!).makeRef()
            }
            propertyLiteral.propertyInitializers += JsPropertyInitializer(JsNameRef("set"), setterBody)
        }

        statements += JsAstUtils.defineProperty(qualifier, name, propertyLiteral).exportStatement(declaration)
    }

    fun getLocalPackageName(packageName: FqName): JsName {
        if (packageName.isRoot) {
            return context.fragment.scope.declareName(Namer.getRootPackageName())
        }
        var name = localPackageNames[packageName]
        if (name == null) {
            name = JsScope.declareTemporaryName("package$" + packageName.shortName().asString())
            localPackageNames[packageName] = name
            statements += definePackageAlias(packageName.shortName().asString(), name, packageName.asString(),
                                             getLocalPackageName(packageName.parent()).makeRef())
        }
        return name
    }

    private fun JsExpression.exportStatement(declaration: DeclarationDescriptor) = JsExpressionStatement(this).also {
        it.exportedTag = context.getTag(declaration)
    }

    private fun MemberDescriptor.shouldBeExported(force: Boolean) = force || shouldBeExported(context.config)
}

