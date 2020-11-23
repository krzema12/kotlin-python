// TODO: muted for Python because it was muted for JS. Once Python doesn't piggy-back on JS, investigate if it can be re-enabled for Python.
// IGNORE_BACKEND: PYTHON
// ERROR_POLICY: SEMANTIC

// MODULE: lib
// FILE: t.kt

fun <reified T> bar(t: T) = t

fun <reified T> qux() = T::class

fun foo(): String {
    return bar<String>("OK")
}

fun dec() { qux() }

// MODULE: main(lib)
// FILE: b.kt

fun box(): String {
    try {
        dec()
    } catch (e: Throwable /*js ReferenceError*/) {
        return foo()
    }
}