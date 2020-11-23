// TODO: muted for Python because it was muted for JS. Once Python doesn't piggy-back on JS, investigate if it can be re-enabled for Python.
// IGNORE_BACKEND: PYTHON
// IGNORE_BACKEND: JS_IR
// IGNORE_BACKEND: JS_IR_ES6
// TODO: muted automatically, investigate should it be ran for JS or not
// IGNORE_BACKEND: JS, NATIVE

// WITH_RUNTIME

import kotlin.reflect.KClass

val <T : KClass<*>> T.myjava1: Class<*>
    get() = java

val <E : Any, T : KClass<E>> T.myjava2: Class<E>
    get() = java

class O
class K

fun box(): String =
        O::class.myjava1.getSimpleName() + K::class.myjava2.getSimpleName()

