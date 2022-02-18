fun pythonTest() {
    println("Hello world")
}

fun exampleFromAstTest() {
    // fruits = ["apple", "banana", "cherry"]
    // for x in fruits:
    //   print(x)
    val fruits = listOf("apple", "banana", "cherry")
    for (x in fruits) {
        println(x)
    }
}

fun isPowerOfTwo(n: Short): Boolean = (n.toInt() and (n - 1)) == 0

fun factorial(n: Int): Long = when (n <= 1) {
    true -> 1
    false -> n * factorial(n - 1)
}

fun numberOfCombinations(n: Int, k: Int): Long = factorial(n) / (factorial(k) * factorial(n - k))

fun sumOverflowDemo(a: Int, b: Int): Int = a + b

fun execute20(f: (Int) -> Int): Int = f(20)

fun execute20Doubled() = execute20 { it + it }

fun lambdaAndCapturing(): Int {
    var capt = 0
    val l = { ++capt }
    return l()
}

fun a(a1: Int, vararg a2: Int) {

}

fun b() {
    a(1, 2, 3)
}

fun newCode() {
    listOf("apple", "banana", "cherry")
        .map { it.toUpperCase() }
        .forEach { x ->
        println(x)
    }
}

class TestClass(val classParameter: String) {
    fun getSomeString() = "Hello from Kotlin class!"

    fun functionReturningClassParameter() = classParameter
}

fun returnString() = "Hello from Kotlin!"

fun returnStringFromClass(): String {
    val testClass = TestClass("paramVal")
    return testClass.getSomeString()
}

fun returnParameterFromClass(): String {
    return TestClass("paramVal").functionReturningClassParameter()
}

fun main(args: Array<String>) {
    println("This is main with arguments!")
}
