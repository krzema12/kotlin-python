// TODO: muted for Python because it was muted for JS. Once Python doesn't piggy-back on JS, investigate if it can be re-enabled for Python.
// IGNORE_BACKEND: PYTHON
// WITH_RUNTIME
// MODULE: lib
// FILE: common.kt

enum class FooEnum(val s: String) {
    O("O"),
    FAIL("FAIL"),
    K("K");
}


// MODULE: bar(lib)
// FILE: second.kt

fun bar(): String = FooEnum.valueOf("O").s + FooEnum.values()[2].s

// MODULE: main(bar)
// FILE: main.kt

fun box(): String {
    return bar()
}