// TODO: muted for Python because it was muted for JS. Once Python doesn't piggy-back on JS, investigate if it can be re-enabled for Python.
// IGNORE_BACKEND: PYTHON
// WITH_REFLECT
// IGNORE_BACKEND: JS_IR, JS, NATIVE
// IGNORE_BACKEND: JS_IR_ES6

// different annotation order
// IGNORE_BACKEND: ANDROID

package test

import kotlin.test.assertEquals

annotation class Ann1
annotation class Ann2

class Foo {
    @setparam:Ann1
    var delegate = " "
        set(@Ann2 value) {}
}

fun box(): String {
    val setterParameters = Foo::delegate.setter.parameters
    assertEquals(2, setterParameters.size)
    assertEquals("[]", setterParameters.first().annotations.toString())
    assertEquals("[@test.Ann2(), @test.Ann1()]", setterParameters.last().annotations.toString())
    return "OK"
}
