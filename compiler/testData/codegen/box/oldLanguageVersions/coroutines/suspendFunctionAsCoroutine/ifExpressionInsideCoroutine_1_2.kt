// TODO: muted for Python because it was muted for JS. Once Python doesn't piggy-back on JS, investigate if it can be re-enabled for Python.
// IGNORE_BACKEND: PYTHON
// !LANGUAGE: -ReleaseCoroutines
// IGNORE_BACKEND: JVM_IR
// IGNORE_BACKEND: JS
// WITH_RUNTIME
// WITH_COROUTINES
// DONT_TARGET_EXACT_BACKEND: JS_IR
// DONT_TARGET_EXACT_BACKEND: JS_IR_ES6

import helpers.*
import kotlin.coroutines.experimental.*

val f = run {
    buildSequence {
        if (true) {
            yield("OK")
        }
    }.toList()
}

fun box(): String {
    return f[0]
}
