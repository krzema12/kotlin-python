// TODO: muted for Python because it was muted for JS. Once Python doesn't piggy-back on JS, investigate if it can be re-enabled for Python.
// IGNORE_BACKEND: PYTHON
// IGNORE_BACKEND: JS_IR
// IGNORE_BACKEND: JS_IR_ES6
// TODO: muted automatically, investigate should it be ran for JS or not
// IGNORE_BACKEND: JS, NATIVE

// WITH_REFLECT

import kotlin.test.assertEquals

fun foo(a: String, b: String = "b", c: String, d: String = "d", e: String) =
        a + b + c + d + e

fun box(): String {
    val p = ::foo.parameters
    assertEquals("abcde", ::foo.callBy(mapOf(
            p[0] to "a",
            p[2] to "c",
            p[4] to "e"
    )))

    return "OK"
}
