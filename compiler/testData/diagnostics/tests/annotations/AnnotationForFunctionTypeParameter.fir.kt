annotation class A1
annotation class A2(val some: Int = 12)

fun <<!WRONG_ANNOTATION_TARGET!>@A1<!> <!WRONG_ANNOTATION_TARGET!>@A2(3)<!> <!WRONG_ANNOTATION_TARGET!>@A2<!> <!WRONG_ANNOTATION_TARGET!>@A1(<!TOO_MANY_ARGUMENTS!>12<!>)<!> <!WRONG_ANNOTATION_TARGET!>@A2(<!ARGUMENT_TYPE_MISMATCH!>"Test"<!>)<!>  T> topFun() = 12

class SomeClass {
    fun <<!WRONG_ANNOTATION_TARGET!>@A1<!> <!WRONG_ANNOTATION_TARGET!>@A2(3)<!> <!WRONG_ANNOTATION_TARGET!>@A2<!> <!WRONG_ANNOTATION_TARGET!>@A1(<!TOO_MANY_ARGUMENTS!>12<!>)<!> <!WRONG_ANNOTATION_TARGET!>@A2(<!ARGUMENT_TYPE_MISMATCH!>"Test"<!>)<!> T> method() = 12

    fun foo() {
        fun <<!WRONG_ANNOTATION_TARGET!>@A1<!> <!WRONG_ANNOTATION_TARGET!>@A2(3)<!> <!WRONG_ANNOTATION_TARGET!>@A2<!> <!WRONG_ANNOTATION_TARGET!>@A1(<!TOO_MANY_ARGUMENTS!>12<!>)<!> <!WRONG_ANNOTATION_TARGET!>@A2(<!ARGUMENT_TYPE_MISMATCH!>"Test"<!>)<!>  T> innerFun() = 12
    }
}

@Target(AnnotationTarget.TYPE)
annotation class TA
@Target(AnnotationTarget.TYPE_PARAMETER)
annotation class TPA(val some: Int = 12)

fun <<!WRONG_ANNOTATION_TARGET!>@TA<!> @TPA(3) @TPA <!WRONG_ANNOTATION_TARGET!>@TA(<!TOO_MANY_ARGUMENTS!>12<!>)<!> @TPA(<!ARGUMENT_TYPE_MISMATCH!>"Test"<!>)  T> topFunTPA() = 12

class SomeClassTPA {
    fun <<!WRONG_ANNOTATION_TARGET!>@TA<!> @TPA(3) @TPA <!WRONG_ANNOTATION_TARGET!>@TA(<!TOO_MANY_ARGUMENTS!>12<!>)<!> @TPA(<!ARGUMENT_TYPE_MISMATCH!>"Test"<!>) T> method() = 12

    fun foo() {
        fun <<!WRONG_ANNOTATION_TARGET!>@TA<!> @TPA(3) @TPA <!WRONG_ANNOTATION_TARGET!>@TA(<!TOO_MANY_ARGUMENTS!>12<!>)<!> @TPA(<!ARGUMENT_TYPE_MISMATCH!>"Test"<!>)  T> innerFun() = 12
    }
}

@Target(AnnotationTarget.TYPE)
annotation class TA
@Target(AnnotationTarget.TYPE_PARAMETER)
annotation class TPA(val some: Int = 12)

fun <@TA @TPA(3) @TPA @TA(<!TOO_MANY_ARGUMENTS!>12<!>) @TPA(<!ARGUMENT_TYPE_MISMATCH!>"Test"<!>)  T> topFunTPA() = 12

class SomeClassTPA {
    fun <@TA @TPA(3) @TPA @TA(<!TOO_MANY_ARGUMENTS!>12<!>) @TPA(<!ARGUMENT_TYPE_MISMATCH!>"Test"<!>) T> method() = 12

    fun foo() {
        fun <@TA @TPA(3) @TPA @TA(<!TOO_MANY_ARGUMENTS!>12<!>) @TPA(<!ARGUMENT_TYPE_MISMATCH!>"Test"<!>)  T> innerFun() = 12
    }
}
