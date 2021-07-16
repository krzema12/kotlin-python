// TODO: muted for Python because it was muted for JS. Once Python doesn't piggy-back on JS, investigate if it can be re-enabled for Python.
// IGNORE_BACKEND: PYTHON
// !LANGUAGE: +MultiPlatformProjects
// IGNORE_BACKEND: JS
// IGNORE_BACKEND: JS_IR
// IGNORE_BACKEND: JS_IR_ES6
// IGNORE_BACKEND: NATIVE

// MODULE: lib-common
// FILE: common.kt

package test

expect enum class E

// MODULE: lib-jvm(lib-common)
// FILE: jvm.kt

package test

actual typealias E = F

enum class F {
    OK;
}

// MODULE: main(lib-jvm)
// FILE: jvm2.kt

import test.E.*

fun box(): String {
    return OK.name
}
