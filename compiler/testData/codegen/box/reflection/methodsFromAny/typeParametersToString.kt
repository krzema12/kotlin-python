// TODO: muted for Python because it was muted for JS. Once Python doesn't piggy-back on JS, investigate if it can be re-enabled for Python.
// IGNORE_BACKEND: PYTHON
// IGNORE_BACKEND: JS_IR
// IGNORE_BACKEND: JS_IR_ES6
// TODO: muted automatically, investigate should it be ran for JS or not
// IGNORE_BACKEND: JS, NATIVE

// WITH_REFLECT

import kotlin.test.assertEquals

interface Variance<A, in B, out C, D>
class OneBound<T : Enum<T>>
class SeveralBounds<T : Cloneable> where T : Enum<T>, T : Variance<String, Int?, Double?, Number>

fun box(): String {
    assertEquals("[A, in B, out C, D]", Variance::class.typeParameters.toString())
    assertEquals("[T]", OneBound::class.typeParameters.toString())
    assertEquals("[T]", SeveralBounds::class.typeParameters.toString())

    return "OK"
}
