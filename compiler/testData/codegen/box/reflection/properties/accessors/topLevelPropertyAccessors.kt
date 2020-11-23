// TODO: muted for Python because it was muted for JS. Once Python doesn't piggy-back on JS, investigate if it can be re-enabled for Python.
// IGNORE_BACKEND: PYTHON
// IGNORE_BACKEND: JS_IR
// IGNORE_BACKEND: JS_IR_ES6
// TODO: muted automatically, investigate should it be ran for JS or not
// IGNORE_BACKEND: JS, NATIVE

// WITH_REFLECT

import kotlin.test.assertEquals

var state: String = ""

fun box(): String {
    val prop = ::state

    assertEquals("", prop.getter.invoke())
    assertEquals("", prop.getter())

    prop.setter("OK")

    return prop.get()
}
