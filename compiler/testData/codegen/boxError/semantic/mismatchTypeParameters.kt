// TODO: muted for Python because it was muted for JS. Once Python doesn't piggy-back on JS, investigate if it can be re-enabled for Python.
// IGNORE_BACKEND: PYTHON
// ERROR_POLICY: SEMANTIC

// MODULE: lib
// FILE: t.kt

fun bar<T>(a: T): T = a

var storage = ""

fun foo() {
    storage += bar("O")
    storage += bar<Any, String, Number>("K")
}

// MODULE: main(lib)
// FILE: b.kt

fun box(): String {
    foo()
    return storage
}