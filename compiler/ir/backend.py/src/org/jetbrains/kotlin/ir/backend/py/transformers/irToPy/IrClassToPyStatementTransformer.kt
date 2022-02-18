/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.ir.backend.py.transformers.irToPy

import generated.Python.*
import org.jetbrains.kotlin.ir.backend.py.utils.PyGenerationContext
import org.jetbrains.kotlin.ir.backend.py.utils.asString
import org.jetbrains.kotlin.ir.declarations.IrClass
import org.jetbrains.kotlin.ir.declarations.IrConstructor
import org.jetbrains.kotlin.ir.declarations.IrField
import org.jetbrains.kotlin.ir.declarations.IrSimpleFunction
import org.jetbrains.kotlin.ir.types.IrType
import org.jetbrains.kotlin.ir.types.getClass
import org.jetbrains.kotlin.ir.util.isInterface
import org.jetbrains.kotlin.ir.util.render
import org.jetbrains.kotlin.ir.util.superTypes

private fun IrType.deepSuperTypes(): List<IrType> {
    val supers = this.superTypes()
    return when (supers.isEmpty()) {
        true -> emptyList()
        false -> supers + supers.flatMap { it.deepSuperTypes() }
    }
}

private fun List<IrType>.sortTopologically(): List<IrType> {  // todo: there turns out to be DFS.topologicalOrder, maybe use it?
    // logic: in Python, a topological ordering of superclasses declarations is needed. Consider the following classes and interfaces:
    //
    //  interface I0
    //  interface I1 : I0
    //  open class C0 : I0
    //  class Our : I0, I1, C0()
    //
    // In Python, we can't declare `class Our(I0, I1, C0)` as it will give "Cannot create a consistent method resolution order (MRO)" runtime error.
    // We need to declare it like this: `class Our(C0, I1, I0)`. So the topological sorting below helps.
    // See `org.jetbrains.kotlin.python.test.ir.semantics.IrPythonCodegenBoxTestGenerated$FakeOverride.testFunction` test that checks all the possible orderings.
    val superClass = this.filter { !it.isInterface() }
    assert(superClass.size in 0..1) { "Found more than 1 super class: all $this, super classes: $superClass" }

    val interfacesTopologicalGraph = (this - superClass).associateWithTo(mutableMapOf()) { it.deepSuperTypes() }

    val sortedInterfaces = mutableListOf<IrType>()

    while (interfacesTopologicalGraph.isNotEmpty()) {
        val mostBaseTypes = interfacesTopologicalGraph
            .keys
            .filter { type -> interfacesTopologicalGraph.values.all { superTypes -> type !in superTypes } }
            .sortedBy {
                // interfaces should go last as they are "less base" and "more super"
                when (it.isInterface()) {
                    true -> 1
                    false -> 0
                }
            }

        sortedInterfaces.addAll(mostBaseTypes)
        mostBaseTypes.forEach(interfacesTopologicalGraph::remove)
    }

    return superClass + sortedInterfaces
}

private fun IrType.calculateName(context: PyGenerationContext): String = try {
    this.getClass()?.let { clazz -> context.getNameForClass(clazz).ident }
} catch (e: IllegalStateException) {
    null
} ?: this.asString().toValidPythonSymbol()

fun IrClass.toPythonStatement(context: PyGenerationContext): List<stmt> {
    val superTypes = superTypes
        .sortTopologically()  // prevent the "Cannot create a consistent method resolution order (MRO)" runtime error
        .map { it.calculateName(context) }
        .filterNot { it.startsWith("kotlin_") }  // todo: Temporarily!

    val forwardDeclarations = superTypes
        .filter { it !in context.definedTypes }
        .map {
            ClassDef(
                name = identifier(it),
                bases = emptyList(),
                keywords = emptyList(),
                body = emptyList(),
                decorator_list = emptyList(),
            )
        }

    val thisClassName = context.getNameForClass(this).ident.toValidPythonSymbol()
    val thisClass = ClassDef(
        name = identifier(thisClassName),
        bases = superTypes.map { Name(id = identifier(it), ctx = Load) },
        keywords = emptyList(),
        body = declarations.mapNotNull { declaration ->
            when (declaration) {
                is IrConstructor -> IrDeclarationToPyTransformer().visitConstructor(declaration, context)
                is IrSimpleFunction -> IrDeclarationToPyTransformer().visitSimpleFunction(declaration, context)
                is IrClass -> Expr(value = Name(id = identifier("visitClassDeclaration_IrClass ${declaration.render()}".toValidPythonSymbol()), ctx = Load)).let(::listOf)
                is IrField -> null
                else -> throw IllegalArgumentException("Unknown declaration type: ${declaration.render()}")
            }
        }.flatten(),
        decorator_list = emptyList(),
    )

    context.definedTypes.addAll(superTypes)
    context.definedTypes.add(thisClassName)

    return forwardDeclarations + listOf(thisClass)
}
