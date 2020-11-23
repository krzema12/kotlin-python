// TODO: muted for Python because it was muted for JS. Once Python doesn't piggy-back on JS, investigate if it can be re-enabled for Python.
// IGNORE_BACKEND: PYTHON
// ERROR_POLICY: SEMANTIC

// MODULE: lib
// FILE: t.kt

class A
class B

fun bar(): B = B()
fun foo(): A {
    return bar()
}

// MODULE: main(lib)
// FILE: b.kt

fun box(): String {
    try {
        foo()
    } catch (e: ClassCastException) {
        return "OK"
    }
    return "FAIL"
}