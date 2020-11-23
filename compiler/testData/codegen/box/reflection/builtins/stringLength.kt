// TODO: muted for Python because it was muted for JS. Once Python doesn't piggy-back on JS, investigate if it can be re-enabled for Python.
// IGNORE_BACKEND: PYTHON
// IGNORE_BACKEND: JS_IR, JS, NATIVE
// IGNORE_BACKEND: JS_IR_ES6
// WITH_REFLECT

import kotlin.test.assertEquals

fun box(): String {
    String::class.members
    assertEquals(2, String::length.call("OK"))
    return "OK"
}
