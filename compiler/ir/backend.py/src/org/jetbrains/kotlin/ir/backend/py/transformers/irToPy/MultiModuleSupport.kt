/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.ir.backend.py.transformers.irToPy

import org.jetbrains.kotlin.ir.backend.py.utils.IrNamer
import org.jetbrains.kotlin.ir.declarations.IrModuleFragment

interface CrossModuleReferenceInfo {
    fun exports(module: IrModuleFragment): List<String>

    fun withReferenceTracking(namer: IrNamer, excludedModules: Iterable<IrModuleFragment>): IrNamerWithImports
}

interface IrNamerWithImports : IrNamer {
    fun imports(): List<Pair<IrModuleFragment, List<String>>>
}

object EmptyCrossModuleReferenceInfo : CrossModuleReferenceInfo {
    override fun exports(module: IrModuleFragment): List<String> = emptyList()

    override fun withReferenceTracking(namer: IrNamer, excludedModules: Iterable<IrModuleFragment>): IrNamerWithImports =
        object : IrNamerWithImports, IrNamer by namer {
            override fun imports() = emptyList<Pair<IrModuleFragment, List<String>>>()
        }
}
