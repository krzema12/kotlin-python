//KT-1293 Compiler doesn't show error when element of Array<Int?> is assigned to Int

package kt1293

fun main() {
    val intArray = arrayOfNulls<Int>(10)
    val i : Int = <!TYPE_MISMATCH!>intArray[0]<!>
    requiresInt(<!TYPE_MISMATCH!>intArray[0]<!>)
}

fun requiresInt(i: Int) {}
