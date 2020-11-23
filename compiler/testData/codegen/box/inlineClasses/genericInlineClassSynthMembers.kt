// TODO: muted for Python because it was muted for JS. Once Python doesn't piggy-back on JS, investigate if it can be re-enabled for Python.
// IGNORE_BACKEND: PYTHON
// IGNORE_BACKEND: JS
// MODULE: lib1
// FILE: lib1.kt

class C<T>(val t: T) {
    override fun hashCode(): Int = t as Int
}

// MODULE: lib2(lib1)
// FILE: lib2.kt

inline class IC<TT>(val c: C<TT>) {
    fun foo(): Int = c.hashCode()
}


// MODULE: main(lib2)
// FILE: main.kt


fun box(): String {
    val ic = IC<Int>(C(42))

    if (ic.foo() != 42) return "FAIL"
    return "OK"
}