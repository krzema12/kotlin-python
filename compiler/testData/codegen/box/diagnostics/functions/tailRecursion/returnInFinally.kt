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

<!NO_TAIL_CALLS_FOUND!>tailrec fun test(counter : Int) : Int<!> {
    if (counter == 0) return 0

    try {
        // do nothing
    } finally {
        return <!TAIL_RECURSION_IN_TRY_IS_NOT_SUPPORTED!>test<!>(counter - 1)
    }
}

fun box() : String = if (test(3) == 0) "OK" else "FAIL"
