// TODO: muted for Python because it was muted for JS. Once Python doesn't piggy-back on JS, investigate if it can be re-enabled for Python.
// IGNORE_BACKEND: PYTHON
// DONT_TARGET_EXACT_BACKEND: WASM
// WASM_MUTE_REASON: SAM_CONVERSIONS
// IGNORE_BACKEND: JS, JS_IR
// IGNORE_BACKEND: JS_IR_ES6

fun interface KRunnable {
    fun invoke()
}

fun interface KBoolean {
    fun invoke(b: Boolean)
}

fun useFunInterface(fn: KRunnable) {
    fn.invoke()
}
fun useFunInterfacePredicate(fn: KBoolean) {
    fn.invoke(true)
}

fun <T> testIntersection(x: T) where T : () -> Unit, T : (Boolean) -> Unit {
    useFunInterface(x)
    useFunInterfacePredicate(x)
}

var result = ""

object Test : () -> Unit, (Boolean) -> Unit {
    override fun invoke() {
        result += "O"
    }

    override fun invoke(p1: Boolean) {
        if (p1) result += "K"
    }
}

fun box(): String {
    testIntersection(Test)
    return result
}