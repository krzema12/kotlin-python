// TODO: muted for Python because it was muted for JS. Once Python doesn't piggy-back on JS, investigate if it can be re-enabled for Python.
// IGNORE_BACKEND: PYTHON
// ERROR_POLICY: SEMANTIC

// MODULE: lib
// FILE: t.kt

fun foo(o: Any): Any = o as ErrType

// MODULE: main(lib)
// FILE: b.kt

fun box(): String {
    try {
        foo(Any())
    } catch (e: IllegalStateException) {
        return "OK"
    }
    return "fail"
}