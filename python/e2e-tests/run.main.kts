#!/usr/bin/env kotlin

@file:DependsOn("com.lordcodes.turtle:turtle:0.6.0")

import com.lordcodes.turtle.ShellLocation
import com.lordcodes.turtle.shellRun
import java.io.File
import java.nio.file.Path
import java.nio.file.Paths

val endToEndRootDir: Path = Paths.get("python/e2e-tests")
val outDir: Path = endToEndRootDir.resolve("out")

outDir.toFile().mkdirs()

println("Starting end-to-end tests")

endToEndRootDir.resolve("testcases").toFile().walk()
    .filter { it.isFile && it.path.endsWith(".kt.py.txt") }
    .forEach { execute(it) }

fun execute(testcaseFile: File) {
    val testName = testcaseFile.name.substringBefore('.')
    println("===== Executing '$testName' =====")

    testcaseFile.extractTestcasePartsToSeparateFiles()
    compileToPython()

    println("===== Finished with '$testName' =====")
}

fun File.extractTestcasePartsToSeparateFiles() {
    outDir.resolve("kotlin-code.kt").toFile()
        .writeText(extractLinesBetween("--- Kotlin code ---", "--- Python consumer ---"))
    outDir.resolve("python-consumer.py").toFile()
        .writeText(extractLinesBetween("--- Python consumer ---", "--- Expected output ---"))
    outDir.resolve("expected-output.txt").toFile()
        .writeText(extractLinesBetween("--- Expected output ---", null))
}

fun File.extractLinesBetween(startLine: String, endLine: String?) =
    readLines()
        .dropWhile { it != startLine }
        .drop(1)
        .takeWhile { it != endLine }
        .joinToString("\n")

fun compileToPython() {
    println("  Compiling to Python...")
    // Running Kotlin-to-Python compiler doesn't work, it looks like calling Java.
    shellRun(
        "dist/kotlinc/bin/kotlinc-py",
        listOf(
//            "-libraries", "dist/kotlinc/lib/kotlin-stdlib-js.jar",
//            "-Xir-produce-py",
//            "-output", "python/e2e-tests/out/compiled.py",
//            "python/e2e-tests/out/kotlin-code.kt",
        )
    )
}

println("All done")

