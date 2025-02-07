// TODO: muted for Python because it was muted for JS. Once Python doesn't piggy-back on JS, investigate if it can be re-enabled for Python.
// IGNORE_BACKEND: PYTHON
// IGNORE_BACKEND: JS_IR
// IGNORE_BACKEND: JS_IR_ES6
// IGNORE_BACKEND: JS, NATIVE
// !USE_EXPERIMENTAL: kotlin.ExperimentalStdlibApi
// WITH_REFLECT

import kotlin.reflect.full.findAnnotation
import kotlin.reflect.full.findAnnotations
import kotlin.test.assertEquals
import kotlin.test.assertNull

annotation class Yes(val value: String)
annotation class No(val value: String)

@Yes("OK")
@No("Fail")
class Foo

class Bar

fun box(): String {
    assertNull(Bar::class.findAnnotation<Yes>())
    assertNull(Bar::class.findAnnotation<No>())

    assertEquals("OK", Foo::class.findAnnotations<Yes>().single().value)

    return Foo::class.findAnnotation<Yes>()?.value ?: "Fail: no annotation"
}
