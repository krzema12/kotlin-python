// TODO: muted for Python because it was muted for JS. Once Python doesn't piggy-back on JS, investigate if it can be re-enabled for Python.
// IGNORE_BACKEND: PYTHON


// MODULE: lib
// FILE: lib.kt


class C<T> {
    fun foo(): String = "OK"

    companion object {
        fun bar(): C<*> = C<String>()
    }
}



// MODULE: main(lib)
// FILE: main.kt

fun box(): String {
    return C.bar().foo()
}