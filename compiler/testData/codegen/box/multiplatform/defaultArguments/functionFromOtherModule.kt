// TODO: muted for Python because it was muted for JS. Once Python doesn't piggy-back on JS, investigate if it can be re-enabled for Python.
// IGNORE_BACKEND: PYTHON
// !LANGUAGE: +MultiPlatformProjects
// IGNORE_BACKEND_FIR: JVM_IR
// WITH_RUNTIME
// MODULE: lib
// FILE: common.kt

expect fun foo(a: String, b: String = "O"): String

// FILE: platform.kt

actual fun foo(a: String, b: String) = a + b

// MODULE: main(lib)
// FILE: main.kt

fun box(): String {
    return foo("") + foo("K", "")
}