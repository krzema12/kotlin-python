// TODO: muted for Python because it was muted for JS. Once Python doesn't piggy-back on JS, investigate if it can be re-enabled for Python.
// IGNORE_BACKEND: PYTHON

// MODULE: lib
// FILE: lib.kt
enum class A {
    X {
        val x = "OK"

        inner class Inner {
            val y = x
        }

        val z = Inner()

        override val test: String
            get() = z.y
    };

    abstract val test: String
}

// MODULE: main(lib)
// FILE: main.kt
fun box() = A.X.test
