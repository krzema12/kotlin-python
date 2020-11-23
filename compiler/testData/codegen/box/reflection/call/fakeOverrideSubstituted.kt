// TODO: muted for Python because it was muted for JS. Once Python doesn't piggy-back on JS, investigate if it can be re-enabled for Python.
// IGNORE_BACKEND: PYTHON
// IGNORE_BACKEND: JS_IR
// IGNORE_BACKEND: JS_IR_ES6
// TODO: muted automatically, investigate should it be ran for JS or not
// IGNORE_BACKEND: JS, NATIVE

// WITH_REFLECT

open class A<T>(val t: T) {
    fun foo() = t
}

class B(s: String) : A<String>(s)

fun box(): String {
    val foo = B::class.members.single { it.name == "foo" }
    return foo.call(B("OK")) as String
}
