// TODO: muted for Python because it was muted for JS. Once Python doesn't piggy-back on JS, investigate if it can be re-enabled for Python.
// IGNORE_BACKEND: PYTHON
// IGNORE_BACKEND: JS_IR
// IGNORE_BACKEND: JS_IR_ES6
// IGNORE_BACKEND: JS, NATIVE

// WITH_REFLECT

import kotlin.test.assertEquals

fun join(vararg strings: String) = strings.toList().joinToString("")

fun sum(vararg bytes: Byte) = bytes.toList().fold(0) { acc, el -> acc + el }

fun box(): String {
    val j = ::join
    val s = ::sum
    assertEquals("", j.callBy(emptyMap()))
    assertEquals(0, s.callBy(emptyMap()))
    return "OK"
}
