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

open class A {
    open fun foo(s: String = "OK") = s
}

class B : A() {
    <!NO_TAIL_CALLS_FOUND!>override tailrec fun foo(s: String): String<!> {
        return if (s == "OK") s else foo()
    }
}

fun box() = B().foo("FAIL")
