fun isPowerOfTwo(n: Short): Boolean = (n.toInt() and (n - 1)) == 0

fun factorial(n: Int): Long = when (n <= 1) {
    true -> 1
    false -> n * factorial(n - 1)
}

fun numberOfCombinations(n: Int, k: Int): Long = factorial(n) / (factorial(k) * factorial(n - k))

fun sumOverflowDemo(a: Int, b: Int): Int = a + b
