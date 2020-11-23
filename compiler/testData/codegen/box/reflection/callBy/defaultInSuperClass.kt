// TODO: muted for Python because it was muted for JS. Once Python doesn't piggy-back on JS, investigate if it can be re-enabled for Python.
// IGNORE_BACKEND: PYTHON
// IGNORE_BACKEND: JS_IR, JS, NATIVE
// IGNORE_BACKEND: JS_IR_ES6
// WITH_REFLECT

open class A {
    open fun foo(a: String, b: String = "b") = b + a
}

class B : A() {
    override fun foo(a: String, b: String) = a + b
}

fun box(): String {
    val f = B::foo

    assert("ab" == f.callBy(mapOf(
        f.parameters.first() to B(),
        f.parameters.single { it.name == "a" } to "a"
    )))

    return "OK"
}
