// TODO: muted for Python because it was muted for JS. Once Python doesn't piggy-back on JS, investigate if it can be re-enabled for Python.
// IGNORE_BACKEND: PYTHON
// MODULE: lib
// FILE: lib.kt
@PublishedApi
internal fun published() = "OK"

inline fun test() = published()

// MODULE: main(lib)
// FILE: main.kt
fun box() = test()
