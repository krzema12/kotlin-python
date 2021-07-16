// TODO: muted for Python because it was muted for JS. Once Python doesn't piggy-back on JS, investigate if it can be re-enabled for Python.
// IGNORE_BACKEND: PYTHON
// DONT_TARGET_EXACT_BACKEND: WASM
// WASM_MUTE_REASON: STDLIB_COLLECTIONS
// !LANGUAGE: +NewInference
// !DIAGNOSTICS: -EXPERIMENTAL_API_USAGE_ERROR -UNUSED_EXPRESSION
// WITH_RUNTIME

@OptIn(ExperimentalStdlibApi::class)
fun test(s: String?): Int {
    val list = buildList {
        s?.let(::add)
    }
    return list.size
}

fun box(): String {
    return when (test("hello")) {
        1 -> "OK"
        else -> "Error"
    }
}
