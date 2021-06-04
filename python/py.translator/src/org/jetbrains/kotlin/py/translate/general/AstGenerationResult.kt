/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.translate.general

import org.jetbrains.kotlin.descriptors.DeclarationDescriptor
import org.jetbrains.kotlin.descriptors.ModuleDescriptor
import org.jetbrains.kotlin.js.backend.ast.*
import org.jetbrains.kotlin.js.config.JsConfig
import org.jetbrains.kotlin.py.facade.TranslationUnit
import org.jetbrains.kotlin.protobuf.CodedInputStream
import org.jetbrains.kotlin.psi.KtFile
import org.jetbrains.kotlin.serialization.js.ast.JsAstDeserializer
import org.jetbrains.kotlin.serialization.js.ast.JsAstProtoBuf
import java.io.ByteArrayInputStream
import java.io.File
import java.util.HashSet

class AstGenerationResult(
    val units: Collection<TranslationUnit>,
    val translatedSourceFiles: Map<KtFile, SourceFileTranslationResult>,
    val inlineFunctionTagMap: Map<String, TranslationUnit>,
    moduleDescriptor: ModuleDescriptor,
    config: JsConfig
) {

    val newFragments = translatedSourceFiles.values.map { it.fragment }.toSet()

    private val cache = mutableMapOf<TranslationUnit.BinaryAst, DeserializedFileTranslationResult>()

    private val merger = Merger(moduleDescriptor, config.moduleId, config.moduleKind)

    private val sourceRoots = config.sourceMapRoots.map { File(it) }
    private val deserializer = JsAstDeserializer(merger.program, sourceRoots)

    fun getTranslationResult(unit: TranslationUnit): FileTranslationResult =
        when (unit) {
            is TranslationUnit.SourceFile -> translatedSourceFiles[unit.file]!!
            is TranslationUnit.BinaryAst -> cache.getOrPut(unit) {
                // TODO Don't deserialize header twice
                val inlineData = JsAstProtoBuf.InlineData.parseFrom(CodedInputStream.newInstance(unit.inlineData))

                DeserializedFileTranslationResult(
                    deserializer.deserialize(ByteArrayInputStream(unit.data)),
                    HashSet(inlineData.inlineFunctionTagsList)
                )
            }
        }

    fun buildProgram(): Pair<JsProgram, List<String>> {
        val fragments = units.map { getTranslationResult(it).fragment }
        fragments.forEach { merger.addFragment(it) }
        return merger.buildProgram() to merger.importedModules.map { it.externalName }
    }
}

sealed class FileTranslationResult {
    abstract val fragment: JsProgramFragment

    abstract val inlineFunctionTags: Set<String>
}

class SourceFileTranslationResult(
    override val fragment: JsProgramFragment,
    override val inlineFunctionTags: Set<String>,
    val memberScope: List<DeclarationDescriptor>
) : FileTranslationResult()

class DeserializedFileTranslationResult(
    override val fragment: JsProgramFragment,
    override val inlineFunctionTags: Set<String>
) : FileTranslationResult()

