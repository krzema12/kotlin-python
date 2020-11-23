// TODO: muted for Python because it was muted for JS. Once Python doesn't piggy-back on JS, investigate if it can be re-enabled for Python.
// IGNORE_BACKEND: PYTHON
// ERROR_POLICY: SEMANTIC

// MODULE: lib
// FILE: t.kt

fun bar(a: String, b: String): String

fun foo(): String {
    return bar("O", "K")
}

// MODULE: main(lib)
// FILE: b.kt

fun box(): String {
    val r = foo()
    if (r is String) return r
    return "OK"
}