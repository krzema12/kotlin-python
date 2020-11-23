// TODO: muted for Python because it was muted for JS. Once Python doesn't piggy-back on JS, investigate if it can be re-enabled for Python.
// IGNORE_BACKEND: PYTHON
// IGNORE_BACKEND: JS_IR
// IGNORE_BACKEND: JS_IR_ES6
// TODO: muted automatically, investigate should it be ran for JS or not
// IGNORE_BACKEND: JS, NATIVE

// WITH_REFLECT

class A(val result: String = "OK") {
    fun foo(x: Int = 42): String {
        assert(x == 42) { x }
        return result
    }
}

fun box(): String = A::foo.callBy(mapOf(A::foo.parameters.first() to A()))
