// TODO: muted for Python because it was muted for JS. Once Python doesn't piggy-back on JS, investigate if it can be re-enabled for Python.
// IGNORE_BACKEND: PYTHON
// IGNORE_BACKEND: JS_IR, JS, NATIVE
// IGNORE_BACKEND: JS_IR_ES6
// WITH_REFLECT

import kotlin.test.assertNotEquals

open class A<T> {
    fun foo(t: T) {}
}

open class B<U> : A<U>()

class C : B<String>()

fun box(): String {
    val afoo = A::class.members.single { it.name == "foo" }
    val bfoo = B::class.members.single { it.name == "foo" }
    val cfoo = C::class.members.single { it.name == "foo" }

    assertNotEquals(afoo, bfoo)
    assertNotEquals(afoo.hashCode(), bfoo.hashCode())
    assertNotEquals(bfoo, cfoo)
    assertNotEquals(bfoo.hashCode(), cfoo.hashCode())

    return "OK"
}
