/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

@file:Suppress(
    "NON_ABSTRACT_FUNCTION_WITH_NO_BODY",
    "MUST_BE_INITIALIZED_OR_BE_ABSTRACT",
    "EXTERNAL_TYPE_EXTENDS_NON_EXTERNAL_TYPE",
    "PRIMARY_CONSTRUCTOR_DELEGATION_CALL_EXPECTED",
    "WRONG_MODIFIER_TARGET",
    "UNUSED_PARAMETER"
)

package kotlin

/**
 * An array of bytes. When targeting the JVM, instances of this class are represented as `byte[]`.
 * @constructor Creates a new array of the specified [size], with all elements initialized to zero.
 */
class ByteArray(size: Int) {
    /**
     * Creates a new array of the specified [size], where each element is calculated by calling the specified
     * [init] function.
     *
     * The function [init] is called for each array element sequentially starting from the first one.
     * It should return the value for an array element given its index.
     */
    inline constructor(size: Int, init: (Int) -> Byte)

    /** Returns the array element at the given [index]. This method can be called using the index operator. */
    operator fun get(index: Int): Byte
    /** Sets the element at the given [index] to the given [value]. This method can be called using the index operator. */
    operator fun set(index: Int, value: Byte): Unit

    /** Returns the number of elements in the array. */
    val size: Int

    /** Creates an iterator over the elements of the array. */
    operator fun iterator(): ByteIterator
}

/**
 * An array of chars. When targeting the JVM, instances of this class are represented as `char[]`.
 * @constructor Creates a new array of the specified [size], with all elements initialized to null char (`\u0000').
 */
class CharArray(size: Int) {
    /**
     * Creates a new array of the specified [size], where each element is calculated by calling the specified
     * [init] function.
     *
     * The function [init] is called for each array element sequentially starting from the first one.
     * It should return the value for an array element given its index.
     */
    inline constructor(size: Int, init: (Int) -> Char)

    /** Returns the array element at the given [index]. This method can be called using the index operator. */
    operator fun get(index: Int): Char
    /** Sets the element at the given [index] to the given [value]. This method can be called using the index operator. */
    operator fun set(index: Int, value: Char): Unit

    /** Returns the number of elements in the array. */
    val size: Int

    /** Creates an iterator over the elements of the array. */
    operator fun iterator(): CharIterator
}

/**
 * An array of shorts. When targeting the JVM, instances of this class are represented as `short[]`.
 * @constructor Creates a new array of the specified [size], with all elements initialized to zero.
 */
class ShortArray(size: Int) {
    /**
     * Creates a new array of the specified [size], where each element is calculated by calling the specified
     * [init] function.
     *
     * The function [init] is called for each array element sequentially starting from the first one.
     * It should return the value for an array element given its index.
     */
    inline constructor(size: Int, init: (Int) -> Short)

    /** Returns the array element at the given [index]. This method can be called using the index operator. */
    operator fun get(index: Int): Short
    /** Sets the element at the given [index] to the given [value]. This method can be called using the index operator. */
    operator fun set(index: Int, value: Short): Unit

    /** Returns the number of elements in the array. */
    val size: Int

    /** Creates an iterator over the elements of the array. */
    operator fun iterator(): ShortIterator
}

/**
 * An array of ints. When targeting the JVM, instances of this class are represented as `int[]`.
 * @constructor Creates a new array of the specified [size], with all elements initialized to zero.
 */
class IntArray(size: Int) {
    /**
     * Creates a new array of the specified [size], where each element is calculated by calling the specified
     * [init] function.
     *
     * The function [init] is called for each array element sequentially starting from the first one.
     * It should return the value for an array element given its index.
     */
    inline constructor(size: Int, init: (Int) -> Int)

    /** Returns the array element at the given [index]. This method can be called using the index operator. */
    operator fun get(index: Int): Int
    /** Sets the element at the given [index] to the given [value]. This method can be called using the index operator. */
    operator fun set(index: Int, value: Int): Unit

    /** Returns the number of elements in the array. */
    val size: Int

    /** Creates an iterator over the elements of the array. */
    operator fun iterator(): IntIterator
}

/**
 * An array of longs. When targeting the JVM, instances of this class are represented as `long[]`.
 * @constructor Creates a new array of the specified [size], with all elements initialized to zero.
 */
class LongArray(size: Int) {
    /**
     * Creates a new array of the specified [size], where each element is calculated by calling the specified
     * [init] function.
     *
     * The function [init] is called for each array element sequentially starting from the first one.
     * It should return the value for an array element given its index.
     */
    inline constructor(size: Int, init: (Int) -> Long)

    /** Returns the array element at the given [index]. This method can be called using the index operator. */
    operator fun get(index: Int): Long
    /** Sets the element at the given [index] to the given [value]. This method can be called using the index operator. */
    operator fun set(index: Int, value: Long): Unit

    /** Returns the number of elements in the array. */
    val size: Int

    /** Creates an iterator over the elements of the array. */
    operator fun iterator(): LongIterator
}

/**
 * An array of floats. When targeting the JVM, instances of this class are represented as `float[]`.
 * @constructor Creates a new array of the specified [size], with all elements initialized to zero.
 */
class FloatArray(size: Int) {
    /**
     * Creates a new array of the specified [size], where each element is calculated by calling the specified
     * [init] function.
     *
     * The function [init] is called for each array element sequentially starting from the first one.
     * It should return the value for an array element given its index.
     */
    inline constructor(size: Int, init: (Int) -> Float)

    /** Returns the array element at the given [index]. This method can be called using the index operator. */
    operator fun get(index: Int): Float
    /** Sets the element at the given [index] to the given [value]. This method can be called using the index operator. */
    operator fun set(index: Int, value: Float): Unit

    /** Returns the number of elements in the array. */
    val size: Int

    /** Creates an iterator over the elements of the array. */
    operator fun iterator(): FloatIterator
}

/**
 * An array of doubles. When targeting the JVM, instances of this class are represented as `double[]`.
 * @constructor Creates a new array of the specified [size], with all elements initialized to zero.
 */
class DoubleArray(size: Int) {
    /**
     * Creates a new array of the specified [size], where each element is calculated by calling the specified
     * [init] function.
     *
     * The function [init] is called for each array element sequentially starting from the first one.
     * It should return the value for an array element given its index.
     */
    inline constructor(size: Int, init: (Int) -> Double)

    /** Returns the array element at the given [index]. This method can be called using the index operator. */
    operator fun get(index: Int): Double
    /** Sets the element at the given [index] to the given [value]. This method can be called using the index operator. */
    operator fun set(index: Int, value: Double): Unit

    /** Returns the number of elements in the array. */
    val size: Int

    /** Creates an iterator over the elements of the array. */
    operator fun iterator(): DoubleIterator
}

/**
 * An array of booleans. When targeting the JVM, instances of this class are represented as `boolean[]`.
 * @constructor Creates a new array of the specified [size], with all elements initialized to `false`.
 */
class BooleanArray(size: Int) {
    /**
     * Creates a new array of the specified [size], where each element is calculated by calling the specified
     * [init] function.
     *
     * The function [init] is called for each array element sequentially starting from the first one.
     * It should return the value for an array element given its index.
     */
    inline constructor(size: Int, init: (Int) -> Boolean)

    /** Returns the array element at the given [index]. This method can be called using the index operator. */
    operator fun get(index: Int): Boolean
    /** Sets the element at the given [index] to the given [value]. This method can be called using the index operator. */
    operator fun set(index: Int, value: Boolean): Unit

    /** Returns the number of elements in the array. */
    val size: Int

    /** Creates an iterator over the elements of the array. */
    operator fun iterator(): BooleanIterator
}

