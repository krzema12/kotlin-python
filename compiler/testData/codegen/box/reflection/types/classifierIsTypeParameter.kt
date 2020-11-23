// TODO: muted for Python because it was muted for JS. Once Python doesn't piggy-back on JS, investigate if it can be re-enabled for Python.
// IGNORE_BACKEND: PYTHON
// IGNORE_BACKEND: JS_IR
// IGNORE_BACKEND: JS_IR_ES6
// TODO: muted automatically, investigate should it be ran for JS or not
// IGNORE_BACKEND: JS, NATIVE

// WITH_REFLECT

import kotlin.reflect.KTypeParameter
import kotlin.test.*

class A<U> {
    fun <T> foo(): T = null!!
    fun bar(): Array<U>? = null!!
}

fun box(): String {
    val t = A::class.members.single { it.name == "foo" }.returnType
    assertFalse(t.isMarkedNullable)
    val tc = t.classifier
    if (tc !is KTypeParameter) fail(tc.toString())
    assertEquals("T", tc.name)

    val u = A::class.members.single { it.name == "bar" }.returnType
    assertTrue(u.isMarkedNullable)
    assertEquals(Array<Any>::class, u.classifier)

    return "OK"
}
