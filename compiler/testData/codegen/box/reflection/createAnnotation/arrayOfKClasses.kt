// TODO: muted for Python because it was muted for JS. Once Python doesn't piggy-back on JS, investigate if it can be re-enabled for Python.
// IGNORE_BACKEND: PYTHON
// IGNORE_BACKEND: JS_IR
// IGNORE_BACKEND: JS_IR_ES6
// TODO: muted automatically, investigate should it be ran for JS or not
// IGNORE_BACKEND: JS, NATIVE

// WITH_REFLECT
package test

import kotlin.reflect.KClass
import kotlin.test.assertEquals

annotation class Anno(val klasses: Array<KClass<*>> = arrayOf(String::class, Int::class))

fun box(): String {
    val anno = Anno::class.constructors.single().callBy(emptyMap())
    assertEquals(listOf(String::class, Int::class), anno.klasses.toList())
    assertEquals("@test.Anno(klasses=[class java.lang.String, int])", anno.toString())
    return "OK"
}
