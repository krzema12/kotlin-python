// TODO: muted for Python because it was muted for JS. Once Python doesn't piggy-back on JS, investigate if it can be re-enabled for Python.
// IGNORE_BACKEND: PYTHON
// IGNORE_BACKEND: JS_IR, JS, NATIVE
// IGNORE_BACKEND: JS_IR_ES6
// WITH_REFLECT

import kotlin.test.assertEquals
import kotlin.test.assertTrue

enum class E { X, Y, Z }

fun box(): String {
    assertTrue(E::class.members.size in 11..12, "" + E::class.members.size)
    assertEquals("Y", E::name.call(E.Y))
    assertEquals(2, E::ordinal.call(E.Z))
    return "OK"
}
