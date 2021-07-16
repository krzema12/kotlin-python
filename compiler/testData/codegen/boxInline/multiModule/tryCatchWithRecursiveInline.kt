// TODO: muted for Python because it was muted for JS. Once Python doesn't piggy-back on JS, investigate if it can be re-enabled for Python.
// IGNORE_BACKEND: PYTHON
// IGNORE_BACKEND: NATIVE
// FILE: lib.kt
inline fun <T> T.andAlso(block: (T) -> Unit): T {
    block(this)
    return this
}

inline fun <T> tryCatch(block: () -> T, onSuccess: (T) -> Unit) {
    try {
        block()
    } catch (e: Throwable) {
        return
    }.andAlso { onSuccess(it) }
}

// FILE: main.kt
fun box(): String {
    var result = false
    tryCatch(block = { true }) {
        result = it
    }
    return if (result) "OK" else "Fail"
}
