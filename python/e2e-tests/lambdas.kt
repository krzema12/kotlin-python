fun execute20(f: (Int) -> Int): Int = f(20)

fun execute20Doubled() = execute20 { it + it }
