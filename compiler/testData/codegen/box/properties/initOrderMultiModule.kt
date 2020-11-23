// TODO: muted for Python because it was muted for JS. Once Python doesn't piggy-back on JS, investigate if it can be re-enabled for Python.
// IGNORE_BACKEND: PYTHON
// MODULE: lib
// FILE: lib.kt

// KT-34273

class Foo(val str: String)

private val foo1 = Foo("OK")

val foo2 = foo1

// MODULE: main(lib)
// FILE: main.kt

fun box(): String = foo2.str
