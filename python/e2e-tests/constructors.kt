/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

var s = "abc"

class MultiConstructors1(a: Int) {

    init {
        s = "body 11"
    }

    constructor(b: String) : this(2) {
        s = "body 12"
    }
}

fun multi11() {
    MultiConstructors1(1)
}

fun multi12() {
    MultiConstructors1("a")
}

class MultiConstructors2 {

    constructor(a: Int) {
        s = "body 21"
    }

    constructor(b: String) {
        s = "body 22"
    }
}

fun multi21() {
    MultiConstructors2(1)
}

fun multi22() {
    MultiConstructors2("a")
}

class MultiConstructors3 {

    constructor(a: Int) {
        s = "body 31"
    }

    constructor(b: String) : this(3) {
        s = "body 32"
    }

    constructor(b: Boolean) : this("c") {
        s = "body 33"
    }
}

fun multi31() {
    MultiConstructors3(1)
}

fun multi32() {
    MultiConstructors3("a")
}

fun multi33() {
    MultiConstructors3(true)
}

abstract class BaseClass {

    constructor(i: Int) {
        s = "body base"
    }
}

class ChildClass : BaseClass {

    constructor(a: Int) : super(4) {
        s = "body child"
    }
}

fun child() {
    ChildClass(123)
}
