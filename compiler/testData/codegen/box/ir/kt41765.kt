// TODO: muted for Python because it was muted for JS. Once Python doesn't piggy-back on JS, investigate if it can be re-enabled for Python.
// IGNORE_BACKEND: PYTHON
// MODULE: lib
// FILE: lib.kt

// KT-41765

interface X {
    override fun toString() :String
}

interface Y

abstract class A: Y, X

// MODULE: main(lib)
// FILE: main.kt

class B: A() {
    override fun toString() = "BBB"
}

fun box(): String {
    if (B().toString() == "BBB") return "OK"
    return "FAIL"
}

