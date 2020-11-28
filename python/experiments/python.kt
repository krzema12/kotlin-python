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

class TestClass {
    fun getSomeString() = "Hello from Kotlin class!"
}

fun returnString() = "Hello from Kotlin!"

fun returnStringFromClass(): String {
    val testClass = TestClass()
    return testClass.getSomeString()
}
