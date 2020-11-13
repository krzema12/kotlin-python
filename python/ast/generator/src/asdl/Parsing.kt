/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */
package asdl

fun parseAsdl(asdlText: String): AsdlModule {
    val withoutComments = asdlText.removeComments()
    val normalized = withoutComments.normalize()
    val (moduleName, typeDefinitions) = normalized.parseAndLeaveOutModule()

    return AsdlModule(
        name = moduleName,
        types = typeDefinitions.parseTypeDefinitions(),
    )
}

private fun String.removeComments() =
    lines()
        .filterNot { it.trimStart().startsWith("--") }
        .joinToString(separator = "\n")

/**
 * Remove formatting, leave spaces only where they are needed (plus where it's easier to leave them for the sake of easier implementation).
 * The goal is to make any further code as simple as possible, so that it doesn't have to take into account different formatting.
 */
private fun String.normalize() =
    replace('\n', ' ')
        .replace(Regex("\\s+"), " ")
        .trim()
        .replace(Regex("\\s*=\\s*"), "=")
        .replace(Regex("\\s*,\\s*"), ",")
        .replace(Regex("\\s*\\|\\s*"), "|")
        .replace(Regex("\\s*\\{\\s*"), "{")
        .replace(Regex("\\s*}\\s*"), "}")
        .replace(Regex("\\s*attributes\\s*"), "attributes")

private fun String.parseAndLeaveOutModule(): Pair<String, String> {
    val regex = Regex("module (?<moduleName>\\w+)\\{(?<remainingCode>.*)}")
    val matcher = regex.toPattern().matcher(this)
    matcher.find()

    return Pair(matcher.group("moduleName"), matcher.group("remainingCode"))
}

private fun String.parseTypeDefinitions(): List<AsdlTypeDefinition> {
    val typeDefinitions = Regex("\\w+=").findAll(this).toList()
    val characterBoundaries = typeDefinitions.map { it.range.start } + length
    val separatedTypeDefinitions = characterBoundaries.zipWithNext()
        .map { (boundaryStart, boundaryEnd) ->
            this.substring(IntRange(boundaryStart, boundaryEnd - 1)).trim()
        }

    return separatedTypeDefinitions.map { it.parseSingleTypeDefinition() }
}

private fun String.parseSingleTypeDefinition(): AsdlTypeDefinition {
    val (name, definition) = split("=")
    val constructorsAndOptionalAttributes = definition.split("attributes")
    val constructors = constructorsAndOptionalAttributes[0]
    val attributes = if (constructorsAndOptionalAttributes.size > 1)
        constructorsAndOptionalAttributes[1]
            .removeSurrounding("(", ")")
    else
        null
    return AsdlTypeDefinition(
        name,
        constructors = constructors.parseConstructors(),
        attributes = attributes?.parseAttributes() ?: emptyList(),
    )
}

private fun String.parseConstructors(): List<AsdlConstructor> {
    return split("|")
        .map { it.parseSingleConstructor() }
}

private fun String.parseSingleConstructor(): AsdlConstructor {
    val nameAndOptionalAttributes = split("(", ")")
    val name = nameAndOptionalAttributes[0]
    val attributes = if (nameAndOptionalAttributes.size > 1)
        nameAndOptionalAttributes[1]
    else
        null
    return AsdlConstructor(
        name,
        attributes = attributes?.parseAttributes() ?: emptyList())
}

private fun String.parseAttributes(): List<AsdlAttribute> {
    return split(",")
        .map { it.parseSingleAttribute() }
}

private fun String.parseSingleAttribute(): AsdlAttribute {
    val (type, name) = split(" ")
    val quantity = when (type.last()) {
        '?' -> AsdlQuantity.Optional
        '*' -> AsdlQuantity.ZeroOrMore
        else -> AsdlQuantity.Single
    }
    return AsdlAttribute(
        name,
        type = type.parseType(),
        quantity = quantity
    )
}

private fun String.parseType(): AsdlTypeReference {
    return AsdlTypeReference(
        name = this.removeSuffix("?").removeSuffix("*"),
    )
}
