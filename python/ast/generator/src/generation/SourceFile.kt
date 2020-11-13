/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package generation

import java.nio.file.Path

data class SourceFile(
    val name: String,
    val content: String,
)

fun SourceFile.writeToFile(directory: Path) {
    val targetFile = directory.resolve(name).toFile()
    targetFile.parentFile.mkdirs()
    targetFile.writeText(content)
}
