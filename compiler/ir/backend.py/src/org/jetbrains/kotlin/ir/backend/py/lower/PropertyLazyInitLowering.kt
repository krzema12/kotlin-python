/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.ir.backend.py.lower

import org.jetbrains.kotlin.backend.common.BodyLoweringPass
import org.jetbrains.kotlin.backend.common.DeclarationTransformer
import org.jetbrains.kotlin.backend.common.ir.isPure
import org.jetbrains.kotlin.backend.common.ir.isTopLevel
import org.jetbrains.kotlin.descriptors.DescriptorVisibilities.INTERNAL
import org.jetbrains.kotlin.ir.IrStatement
import org.jetbrains.kotlin.ir.UNDEFINED_OFFSET
import org.jetbrains.kotlin.ir.backend.py.JsIrBackendContext
import org.jetbrains.kotlin.ir.backend.py.ir.JsIrArithBuilder
import org.jetbrains.kotlin.ir.backend.py.ir.JsIrBuilder
import org.jetbrains.kotlin.ir.backend.py.utils.prependFunctionCall
import org.jetbrains.kotlin.ir.builders.declarations.addFunction
import org.jetbrains.kotlin.ir.builders.declarations.buildField
import org.jetbrains.kotlin.ir.declarations.*
import org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrElementBase
import org.jetbrains.kotlin.ir.expressions.IrBody
import org.jetbrains.kotlin.ir.expressions.IrExpression
import org.jetbrains.kotlin.ir.expressions.IrGetField
import org.jetbrains.kotlin.ir.expressions.IrSetField
import org.jetbrains.kotlin.name.Name
import kotlin.collections.Collection
import kotlin.collections.List
import kotlin.collections.Map
import kotlin.collections.all
import kotlin.collections.asSequence
import kotlin.collections.component1
import kotlin.collections.component2
import kotlin.collections.contains
import kotlin.collections.filterNotNull
import kotlin.collections.forEach
import kotlin.collections.listOf
import kotlin.collections.map
import kotlin.collections.mutableListOf
import kotlin.collections.set
import kotlin.collections.toList
import kotlin.collections.toMap

class PropertyLazyInitLowering(
    private val context: JsIrBackendContext
) : BodyLoweringPass {

    private val irBuiltIns
        get() = context.irBuiltIns

    private val calculator = JsIrArithBuilder(context)

    private val irFactory
        get() = context.irFactory

    private val fileToInitializationFuns
        get() = context.fileToInitializationFuns

    private val fileToInitializerPureness
        get() = context.fileToInitializerPureness

    override fun lower(irBody: IrBody, container: IrDeclaration) {
        if (container !is IrField && container !is IrSimpleFunction && container !is IrProperty)
            return

        if (!container.isCompatibleDeclaration()) return

        val file = container.parent as? IrFile
            ?: return

        val initFun = (when {
            file in fileToInitializationFuns -> fileToInitializationFuns[file]
            fileToInitializerPureness[file] == true -> null
            else -> {
                createInitializationFunction(file).also {
                    fileToInitializationFuns[file] = it
                }
            }
        }) ?: return

        val initializationCall = JsIrBuilder.buildCall(
            target = initFun.symbol,
            type = initFun.returnType
        )

        when (container) {
            is IrSimpleFunction ->
                irBody.prependFunctionCall(initializationCall)
            is IrField -> {
                container
                    .correspondingProperty
                    ?.takeIf { it.isForLazyInit() }
                    ?.takeIf { it.backingField?.initializer != null }
                    ?.let { listOf(it.getter, it.setter) }
                    ?.filterNotNull()
                    ?.forEach {
                        irBody.prependFunctionCall(initializationCall)
                    }
            }
        }
    }

    private fun createInitializationFunction(
        file: IrFile
    ): IrSimpleFunction? {
        val fileName = file.name

        val declarations = file.declarations.toList()

        val fieldToInitializer = calculateFieldToExpression(
            declarations
        )

        if (fieldToInitializer.isEmpty()) return null

        val allFieldsInFilePure = allFieldsInFilePure(fieldToInitializer.values)
        fileToInitializerPureness[file] = allFieldsInFilePure
        if (allFieldsInFilePure) {
            return null
        }

        val initializedField = irFactory.createInitializationField(fileName)
            .apply {
                file.declarations.add(this)
                parent = file
            }
        initializedField.initializer = irFactory.createExpressionBody(JsIrBuilder.buildBoolean(context.irBuiltIns.booleanType, false))

        return irFactory.addFunction(file) {
            name = Name.identifier("init properties $fileName")
            returnType = irBuiltIns.unitType
            visibility = INTERNAL
            origin = JsIrBuilder.SYNTHESIZED_DECLARATION
        }.apply {
            buildPropertiesInitializationBody(
                file,
                fieldToInitializer,
                initializedField
            )
        }
    }

    private fun IrFactory.createInitializationField(fileName: String): IrField =
        buildField {
            name = Name.identifier("properties initialized $fileName")
            type = irBuiltIns.booleanType
            isStatic = true
            isFinal = true
            origin = JsIrBuilder.SYNTHESIZED_DECLARATION
        }

    private fun IrSimpleFunction.buildPropertiesInitializationBody(
        file: IrFile,
        initializers: Map<IrField, IrExpression>,
        initializedField: IrField
    ) {
        body = irFactory.createBlockBody(
            UNDEFINED_OFFSET,
            UNDEFINED_OFFSET,
            buildBodyWithIfGuard(file, initializers, initializedField)
        )
    }

    private fun buildBodyWithIfGuard(
        file: IrFile,
        initializers: Map<IrField, IrExpression>,
        initializedField: IrField
    ): List<IrStatement> {
        val statements = initializers
            .map { (field, expression) ->
                createIrSetField(field, expression)
            }

        val upGuard = createIrSetField(
            initializedField,
            JsIrBuilder.buildBoolean(context.irBuiltIns.booleanType, true)
        )

        // This is a workaround to be able to emit "global ..." Python construct. There's no corresponding IR entity, so we emit a function
        // which then is checked if the name contains some special parts. If yes, it's translated to "Global".
        val dummyFunction = irFactory.addFunction(file) {
            name = Name.identifier("Python workaround set ${initializedField.name.identifier} to global")
            returnType = irBuiltIns.unitType
            visibility = INTERNAL
            origin = JsIrBuilder.SYNTHESIZED_DECLARATION
        }

        val settingToGlobal = JsIrBuilder.buildCall(dummyFunction.symbol)
        val ifStatement = JsIrBuilder.buildIfElse(
            type = irBuiltIns.unitType,
            cond = calculator.not(createIrGetField(initializedField)),
            thenBranch = JsIrBuilder.buildComposite(
                type = irBuiltIns.unitType,
                statements = mutableListOf(upGuard).apply { addAll(statements) }
            )
        )

        return listOf(settingToGlobal, ifStatement)
    }
}

private fun createIrGetField(field: IrField): IrGetField {
    return JsIrBuilder.buildGetField(
        symbol = field.symbol,
        receiver = null
    )
}

private fun createIrSetField(field: IrField, expression: IrExpression): IrSetField {
    return JsIrBuilder.buildSetField(
        symbol = field.symbol,
        receiver = null,
        value = expression,
        type = expression.type
    )
}

private fun allFieldsInFilePure(fieldToInitializer: Collection<IrExpression>) =
    fieldToInitializer.all { it.isPure(anyVariable = true) }

class RemoveInitializersForLazyProperties(
    private val context: JsIrBackendContext
) : DeclarationTransformer {

    private val fileToInitializerPureness
        get() = context.fileToInitializerPureness

    override fun transformFlat(declaration: IrDeclaration): List<IrDeclaration>? {
        if (declaration !is IrField) return null

        if (!declaration.isCompatibleDeclaration()) return null

        val file = declaration.parent as? IrFile ?: return null

        if (fileToInitializerPureness[file] == true) return null

        val allFieldsInFilePure = fileToInitializerPureness[file]
            ?: calculateFileFieldsPureness(file)

        if (allFieldsInFilePure) {
            return null
        }

        declaration.correspondingProperty
            ?.takeIf { it.isForLazyInit() }
            ?.backingField
            ?.let {
                it.initializer = null
            }

        return null
    }

    private fun calculateFileFieldsPureness(file: IrFile): Boolean {
        val declarations = file.declarations.toList()
        val expressions = calculateFieldToExpression(declarations)
            .values

        val allFieldsInFilePure = allFieldsInFilePure(expressions)
        fileToInitializerPureness[file] = allFieldsInFilePure
        return allFieldsInFilePure
    }
}

private fun calculateFieldToExpression(declarations: Collection<IrDeclaration>): Map<IrField, IrExpression> =
    declarations
        .asSequence()
        .filter { it.isCompatibleDeclaration() }
        .map { it.correspondingProperty }
        .filterNotNull()
        .filter { it.isForLazyInit() }
        .distinct()
        .mapNotNull { it.backingField }
        .filter { it.initializer != null }
        .map { it to it.initializer!!.expression }
        .toMap()

private fun IrProperty.isForLazyInit() = isTopLevel && !isConst

private val IrDeclaration.correspondingProperty: IrProperty?
    get() {
        if (this !is IrSimpleFunction && this !is IrField && this !is IrProperty)
            return null

        return when (this) {
            is IrProperty -> this
            is IrSimpleFunction -> propertyWithPersistentSafe {
                correspondingPropertySymbol?.owner
            }
            is IrField -> propertyWithPersistentSafe {
                correspondingPropertySymbol?.owner
            }
            else -> error("Can be only IrProperty, IrSimpleFunction or IrField")
        }
    }

private fun IrDeclaration.propertyWithPersistentSafe(transform: IrDeclaration.() -> IrProperty?): IrProperty? =
    if (this !is PersistentIrElementBase<*> || this.createdOn <= this.factory.stageController.currentStage) {
        transform()
    } else null

private fun IrDeclaration.isCompatibleDeclaration() =
    origin in compatibleOrigins

private val compatibleOrigins = listOf(
    IrDeclarationOrigin.DEFINED,
    IrDeclarationOrigin.DELEGATED_PROPERTY_ACCESSOR,
    IrDeclarationOrigin.PROPERTY_DELEGATE,
    IrDeclarationOrigin.DEFAULT_PROPERTY_ACCESSOR,
    IrDeclarationOrigin.PROPERTY_BACKING_FIELD,
)