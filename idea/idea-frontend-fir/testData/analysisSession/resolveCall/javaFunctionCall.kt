// FILE: call.kt
fun call() {
    val javaClass = JavaClass()
    javaClass.<expr>javaMethod()</expr>
}

// FILE: JavaClass.java
class JavaClass {
    void javaMethod() {}
}

// CALL: KtFunctionCall: targetFunction = /JavaClass.javaMethod(): kotlin.Unit