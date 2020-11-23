// TODO: muted for Python because it was muted for JS. Once Python doesn't piggy-back on JS, investigate if it can be re-enabled for Python.
// IGNORE_BACKEND: PYTHON
// IGNORE_BACKEND: JS_IR
// IGNORE_BACKEND: JS_IR_ES6
// TODO: muted automatically, investigate should it be ran for JS or not
// IGNORE_BACKEND: JS

// WITH_RUNTIME

inline fun<reified T> isinstance(x: Any?): Boolean {
    return x is T
}

fun box(): String {
    assert(isinstance<String>("abc"))
    assert(isinstance<Int>(1))
    assert(!isinstance<Int>("abc"))

    return "OK"
}
