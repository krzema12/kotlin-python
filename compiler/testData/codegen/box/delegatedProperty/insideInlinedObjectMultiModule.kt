// TODO: muted for Python because it was muted for JS. Once Python doesn't piggy-back on JS, investigate if it can be re-enabled for Python.
// IGNORE_BACKEND: PYTHON
// MODULE: lib
// FILE: lib.kt

import kotlin.reflect.*

class Delegate {
    var inner = "OK"
    operator fun getValue(t: Any?, p: KProperty<*>): String = inner
}

inline fun <T> foo(b: () -> T): T {
    return b()
}

fun del() = Delegate()

// MODULE: lib2(lib)
// FILE: lib2.kt

fun qux() = foo {
    val f = object {
        val a by del()
    }

    f.a
}

// MODULE: main(lib2)
// FILE: main.kt

fun box(): String {
    return qux()
}