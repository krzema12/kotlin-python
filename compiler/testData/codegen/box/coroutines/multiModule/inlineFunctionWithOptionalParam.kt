// TODO: muted for Python because it was muted for JS. Once Python doesn't piggy-back on JS, investigate if it can be re-enabled for Python.
// IGNORE_BACKEND: PYTHON
// MODULE: lib
// FILE: lib.kt
inline fun foo(x: String = "OK"): String {
    return x + x
}

// MODULE: main(lib, support)
// FILE: main.kt
// WITH_RUNTIME
// WITH_COROUTINES
// COMMON_COROUTINES_TEST
import helpers.*
import COROUTINES_PACKAGE.*
import COROUTINES_PACKAGE.intrinsics.*

var result = ""

fun builder(c: suspend () -> Unit) {
    c.startCoroutine(EmptyContinuation)
}

fun box(): String {
    builder {
        result = foo()
    }
    if (result != "OKOK") return "fail: $result"
    return "OK"
}
