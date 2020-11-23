// TODO: muted for Python because it was muted for JS. Once Python doesn't piggy-back on JS, investigate if it can be re-enabled for Python.
// IGNORE_BACKEND: PYTHON
// IGNORE_BACKEND: JS_IR
// IGNORE_BACKEND: JS_IR_ES6
// TODO: muted automatically, investigate should it be ran for JS or not
// IGNORE_BACKEND: JS, NATIVE

// WITH_REFLECT

import kotlin.reflect.full.createType
import kotlin.test.assertEquals

class Foo<T> {
    fun nonNull(): T = null!!
    fun nullable(): T? = null
}

fun box(): String {
    val tp = Foo::class.typeParameters.single()
    assertEquals(
            Foo::class.members.single { it.name == "nonNull" }.returnType,
            tp.createType()
    )
    assertEquals(
            Foo::class.members.single { it.name == "nullable" }.returnType,
            tp.createType(nullable = true)
    )

    assertEquals(tp.createType(), tp.createType())
    assertEquals(tp.createType(nullable = true), tp.createType(nullable = true))

    assertEquals("T", tp.createType().toString())
    assertEquals("T?", tp.createType(nullable = true).toString())

    return "OK"
}
