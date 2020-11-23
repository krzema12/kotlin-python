// TODO: muted for Python because it was muted for JS. Once Python doesn't piggy-back on JS, investigate if it can be re-enabled for Python.
// IGNORE_BACKEND: PYTHON
// ERROR_POLICY: SEMANTIC

// MODULE: lib
// FILE: t.kt

fun bar() { throw Exception("..") }

fun foo(): String {
    try {
        bar()
    } catch (e: ErrType) {
        throw Expception(e)
    }
}

// MODULE: main(lib)
// FILE: b.kt

fun box(): String {
    try {
        foo()
    } catch (e: IllegalStateException) {
        return "OK"
    }
    return "fail"
}