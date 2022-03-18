/*
 * Copyright 2010-2019 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package kotlin

actual open class Error : Throwable {
    actual constructor() : super()
    actual constructor(message: String?) : super(message)
    actual constructor(message: String?, cause: Throwable?) : super(message, cause)
    actual constructor(cause: Throwable?) : super(cause)
}

actual open class Exception : Throwable {
    actual constructor() : super()
    actual constructor(message: String?) : super(message)
    actual constructor(message: String?, cause: Throwable?) : super(message, cause)
    actual constructor(cause: Throwable?) : super(cause)
}

actual open class RuntimeException : Exception {
    actual constructor() : super()
    actual constructor(message: String?) : super(message)
    actual constructor(message: String?, cause: Throwable?) : super(message, cause)
    actual constructor(cause: Throwable?) : super(cause)
}

actual open class IllegalArgumentException : RuntimeException {
    actual constructor() : super()
    actual constructor(message: String?) : super(message)
    actual constructor(message: String?, cause: Throwable?) : super(message, cause)
    actual constructor(cause: Throwable?) : super(cause)
}

actual open class IllegalStateException : RuntimeException {
    actual constructor() : super()
    actual constructor(message: String?) : super(message)
    actual constructor(message: String?, cause: Throwable?) : super(message, cause)
    actual constructor(cause: Throwable?) : super(cause)
}

actual open class IndexOutOfBoundsException : RuntimeException {
    actual constructor() : super()
    actual constructor(message: String?) : super(message)
}

actual open class ConcurrentModificationException : RuntimeException {
    actual constructor() : super()
    actual constructor(message: String?) : super(message)
    actual constructor(message: String?, cause: Throwable?) : super(message, cause)
    actual constructor(cause: Throwable?) : super(cause)
}

actual open class UnsupportedOperationException : RuntimeException {
    actual constructor() : super()
    actual constructor(message: String?) : super(message)
    actual constructor(message: String?, cause: Throwable?) : super(message, cause)
    actual constructor(cause: Throwable?) : super(cause)
}


actual open class NumberFormatException : IllegalArgumentException {
    actual constructor() : super()
    actual constructor(message: String?) : super(message)
}


actual open class NullPointerException : RuntimeException {
    actual constructor() : super()
    actual constructor(message: String?) : super(message)
}

actual open class ClassCastException : RuntimeException {
    actual constructor() : super()
    actual constructor(message: String?) : super(message)
}

actual open class AssertionError : Error {
    actual constructor() : super()
    constructor(message: String?) : super(message)
    actual constructor(message: Any?) : super(message?.toString(), message as? Throwable)
    @SinceKotlin("1.4")
    constructor(message: String?, cause: Throwable?) : super(message, cause)
}

actual open class NoSuchElementException : RuntimeException {
    actual constructor() : super()
    actual constructor(message: String?) : super(message)
}

@SinceKotlin("1.3")
actual open class ArithmeticException : RuntimeException {
    actual constructor() : super()
    actual constructor(message: String?) : super(message)
}

actual open class NoWhenBranchMatchedException : RuntimeException {
    actual constructor() : super()
    actual constructor(message: String?) : super(message)
    actual constructor(message: String?, cause: Throwable?) : super(message, cause)
    actual constructor(cause: Throwable?) : super(cause)
}

actual open class UninitializedPropertyAccessException : RuntimeException {
    actual constructor() : super()
    actual constructor(message: String?) : super(message)
    actual constructor(message: String?, cause: Throwable?) : super(message, cause)
    actual constructor(cause: Throwable?) : super(cause)
}
