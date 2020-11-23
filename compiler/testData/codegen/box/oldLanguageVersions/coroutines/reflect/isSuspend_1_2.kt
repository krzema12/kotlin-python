// TODO: muted for Python because it was muted for JS. Once Python doesn't piggy-back on JS, investigate if it can be re-enabled for Python.
// IGNORE_BACKEND: PYTHON
// !LANGUAGE: -ReleaseCoroutines
// WITH_COROUTINES
// WITH_REFLECT
// DONT_TARGET_EXACT_BACKEND: JS_IR
// DONT_TARGET_EXACT_BACKEND: JS_IR_ES6

// IGNORE_BACKEND: NATIVE
// IGNORE_BACKEND: JS

import helpers.*
import kotlin.coroutines.experimental.*

class A {
    fun noArgs() = "OK"
}

fun box(): String {
    if (A::noArgs.isSuspend) return "FAIL"
    return "OK"
}
