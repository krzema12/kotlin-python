// TODO: muted for Python because it was muted for JS. Once Python doesn't piggy-back on JS, investigate if it can be re-enabled for Python.
// IGNORE_BACKEND: PYTHON
// DONT_TARGET_EXACT_BACKEND: WASM
// WASM_MUTE_REASON: IGNORED_IN_JS
// IGNORE_BACKEND: JS_IR
// IGNORE_BACKEND: JS_IR_ES6
// TODO: muted automatically, investigate should it be ran for JS or not
// DONT_RUN_GENERATED_CODE: JS
// IGNORE_BACKEND: JS
// IGNORE_FIR_DIAGNOSTICS_DIFF

<!NO_TAIL_CALLS_FOUND!>tailrec fun test(go: Boolean) : Unit<!> {
    if (!go) return
    try {
        <!TAIL_RECURSION_IN_TRY_IS_NOT_SUPPORTED!>test<!>(false)
    } catch (any : Exception) {
        <!TAIL_RECURSION_IN_TRY_IS_NOT_SUPPORTED!>test<!>(false)
    } finally {
        <!TAIL_RECURSION_IN_TRY_IS_NOT_SUPPORTED!>test<!>(false)
    }
}

fun box(): String {
    test(true)
    return "OK"
}
