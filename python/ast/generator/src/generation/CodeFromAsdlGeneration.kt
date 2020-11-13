/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package generation

import asdl.AsdlAttribute
import asdl.AsdlConstructor
import asdl.AsdlModule
import asdl.AsdlTypeDefinition

fun AsdlModule.generateKotlinFromAsdl(): List<SourceFile> {
    return types.map { it.toKotlinSourceFile(name) } + listOf(getBuiltInTypesFile(name))
}

fun getBuiltInTypesFile(moduleName: String): SourceFile {
    return SourceFile(
        name = "generated/$moduleName/builtIns.kt",
        content = """
            package generated.$moduleName
            
            object identifier 
            object int
            object string
            object constant
        """,
    )
}

private fun AsdlTypeDefinition.toKotlinSourceFile(moduleName: String): SourceFile {
    val fileName = "generated/$moduleName/$name.kt"
    val content = """
        package generated.$moduleName
        
        sealed class $name(${attributes.toKotlinClassArguments(open = true) ?: ""})
        
        ${constructors.toKotlinSourceFile(this)}
    """

    return SourceFile(fileName, content)
}

private fun List<AsdlConstructor>.toKotlinSourceFile(parentSealedClass: AsdlTypeDefinition): String {
    return joinToString("\n") {
        it.toKotlinSourceFile(parentSealedClass)
    }
}

private fun AsdlConstructor.toKotlinSourceFile(parentSealedClass: AsdlTypeDefinition): String {
    val constructorName = name ?: "${parentSealedClass.name}Impl"
    return if ((attributes + parentSealedClass.attributes).isEmpty()) {
        """
            object $constructorName : ${parentSealedClass.name}() 
        """
    } else {
        """
        data class $constructorName(${listOf(attributes.toKotlinClassArguments(), parentSealedClass.attributes.toKotlinClassArguments(override = true)).filterNotNull().joinToString(", ")}) 
            : ${parentSealedClass.name}(${parentSealedClass.attributes.joinToString(", ") { it.name }}) 
        """
    }
}

private fun List<AsdlAttribute>.toKotlinClassArguments(open: Boolean = false, override: Boolean = false): String? {
    return if (isEmpty())
        return null
    else joinToString(", ") {
        "${if (open) "open " else if (override) "override " else ""}val ${it.name}: ${it.type.name}"
    }
}
