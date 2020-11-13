import asdl.parseAsdl
import generation.generateKotlinFromAsdl
import generation.writeToFile
import java.nio.file.Paths

/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

fun main() {
    val python39AsdlAsText = {}.javaClass.getResource("/Python39.asdl").readText()
    val python39Asdl = parseAsdl(python39AsdlAsText)

    val targetDirectory = Paths.get("python/ast/src/generated")
    targetDirectory.toFile().deleteRecursively()
    python39Asdl.generateKotlinFromAsdl()
        .forEach {
            it.writeToFile(directory = targetDirectory)
        }
}
