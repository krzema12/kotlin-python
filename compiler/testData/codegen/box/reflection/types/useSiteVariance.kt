// TODO: muted for Python because it was muted for JS. Once Python doesn't piggy-back on JS, investigate if it can be re-enabled for Python.
// IGNORE_BACKEND: PYTHON
// IGNORE_BACKEND: JS_IR
// IGNORE_BACKEND: JS_IR_ES6
// TODO: muted automatically, investigate should it be ran for JS or not
// IGNORE_BACKEND: JS, NATIVE

// WITH_REFLECT

import kotlin.reflect.KVariance
import kotlin.test.assertEquals

class Fourple<A, B, C, D>
fun foo(): Fourple<String, in String, out String, *> = null!!

fun listOfStrings(): List<String> = null!!

fun box(): String {
    assertEquals(
            listOf(
                    KVariance.INVARIANT,
                    KVariance.IN,
                    KVariance.OUT,
                    null
            ),
            ::foo.returnType.arguments.map { it.variance }
    )

    // Declaration-site variance should have no effect on the variance of the type projection:
    assertEquals(KVariance.INVARIANT, ::listOfStrings.returnType.arguments.first().variance)

    return "OK"
}
