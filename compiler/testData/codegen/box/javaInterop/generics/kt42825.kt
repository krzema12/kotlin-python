// TODO: muted for Python because it was muted for JS. Once Python doesn't piggy-back on JS, investigate if it can be re-enabled for Python.
// IGNORE_BACKEND: PYTHON
// FILE: Processor.java

public interface Processor<T> {
    boolean process(T t);
}

// FILE: test.kt
// DONT_TARGET_EXACT_BACKEND: WASM
// IGNORE_BACKEND: JS
// IGNORE_BACKEND: JS_IR

interface PsiModifierListOwner
interface KtClassOrObject {
    fun toLightClass(): PsiModifierListOwner?
}

fun execute(declaration: Any, consumer: Processor<in PsiModifierListOwner>) {
    when (declaration) {
        is KtClassOrObject -> {
            val lightClass = declaration.toLightClass()
            consumer.process(lightClass)
        }
    }
}

fun box(): String = "OK"