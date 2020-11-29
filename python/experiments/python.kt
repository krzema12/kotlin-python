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
