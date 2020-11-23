// TODO: muted for Python because it was muted for JS. Once Python doesn't piggy-back on JS, investigate if it can be re-enabled for Python.
// IGNORE_BACKEND: PYTHON
// IGNORE_BACKEND_FIR: JVM_IR
// MODULE: lib
// FILE: l1.kt

val <T : CharSequence> T.z
    get() = { x: T -> this }

// FILE: l2.kt

fun test(ok: String, fail: String) = ok.z(fail)

// MODULE: main(lib)
// FILE: main.kt

fun box() = test("OK", "FAIL")