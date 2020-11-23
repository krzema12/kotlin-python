// TODO: muted for Python because it was muted for JS. Once Python doesn't piggy-back on JS, investigate if it can be re-enabled for Python.
// IGNORE_BACKEND: PYTHON
// IGNORE_BACKEND: JS_IR
// IGNORE_BACKEND: JS_IR_ES6
// TODO: muted automatically, investigate should it be ran for JS or not
// IGNORE_BACKEND: JS, NATIVE

// WITH_REFLECT

@Retention(AnnotationRetention.RUNTIME)
annotation class Simple(val value: String)

fun test(@Simple("OK") x: Int) {}

fun box(): String {
    return (::test.parameters.single().annotations.single() as Simple).value
}
