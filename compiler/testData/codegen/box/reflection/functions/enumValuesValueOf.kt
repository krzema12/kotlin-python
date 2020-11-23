// TODO: muted for Python because it was muted for JS. Once Python doesn't piggy-back on JS, investigate if it can be re-enabled for Python.
// IGNORE_BACKEND: PYTHON
// IGNORE_BACKEND: JS_IR, JS, NATIVE
// IGNORE_BACKEND: JS_IR_ES6
// WITH_REFLECT

package test

import kotlin.test.assertEquals

enum class E { X, Y, Z }

fun box(): String {
    assertEquals("fun values(): kotlin.Array<test.E>", E::values.toString())
    assertEquals(listOf(E.X, E.Y, E.Z), E::values.call().toList())
    assertEquals("fun valueOf(kotlin.String): test.E", E::valueOf.toString())
    assertEquals(E.Y, E::valueOf.call("Y"))

    return "OK"
}
