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
