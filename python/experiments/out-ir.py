def fold(initial, operation):
    accumulator = initial
    indexedObject = (special)
    inductionVariable = 0
    last = jsArrayLength(indexedObject)
    while jsLt(inductionVariable, last):
        element = jsArrayGet(indexedObject, inductionVariable)
        inductionVariable = jsBitOr(jsPlus(inductionVariable, 1), 0)
        accumulator = invoke(accumulator, element)
    
    return accumulator

def contains(element):
    return jsGtEq(indexOf(element), 0)

def indexOf(element):
    inductionVariable = 0
    last = jsBitOr(jsMinus(jsArrayLength((special)), 1), 0)
    visitWhen
    return -1

def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@55e4dd68

def special():
    return jsBitOr(jsMinus(jsArrayLength((special)), 1), 0)

def contains(element):
    return jsGtEq(indexOf(element), 0)

def indexOf(element):
    inductionVariable = 0
    last = jsBitOr(jsMinus(jsArrayLength((special)), 1), 0)
    visitWhen
    return -1

def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@21ab919c

def special():
    return jsBitOr(jsMinus(jsArrayLength((special)), 1), 0)

def contains(element):
    return jsGtEq(indexOf(element), 0)

def indexOf(element):
    inductionVariable = 0
    last = jsBitOr(jsMinus(jsArrayLength((special)), 1), 0)
    visitWhen
    return -1

def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@484876a1

def special():
    return jsBitOr(jsMinus(jsArrayLength((special)), 1), 0)

def contains(element):
    return jsGtEq(indexOf(element), 0)

def indexOf(element):
    inductionVariable = 0
    last = jsBitOr(jsMinus(jsArrayLength((special)), 1), 0)
    visitWhen
    return -1

def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5977bdea

def special():
    return jsBitOr(jsMinus(jsArrayLength((special)), 1), 0)

def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@41581c3f

def indexOf(element):
    visitWhen
    return -1

def lastIndexOf(element):
    visitWhen
    return -1

def special():
    return jsBitOr(jsMinus(jsArrayLength((special)), 1), 0)

def joinToString(separator, prefix, postfix, limit, truncated, transform):
    return toString()

def joinToString$default(separator, prefix, postfix, limit, truncated, transform, $mask0, $handler):
    visitWhen
    visitWhen
    visitWhen
    visitWhen
    visitWhen
    visitWhen
    return joinToString(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@1a8b7423, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@55607e6d, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@695dc0e6, limit, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@1e68d8f, transform)

def joinTo(buffer, separator, prefix, postfix, limit, truncated, transform):
    append(prefix)
    Unit_getInstance()
    count = 0
    indexedObject = (special)
    inductionVariable = 0
    last = jsArrayLength(indexedObject)
    while jsLt(inductionVariable, last):
        element = jsArrayGet(indexedObject, inductionVariable)
        inductionVariable = jsBitOr(jsPlus(inductionVariable, 1), 0)
        count = jsBitOr(jsPlus(count, 1), 0)
        visitWhen
        visitWhen
    
    visitWhen
    append(postfix)
    Unit_getInstance()
    return buffer

def joinTo$default(buffer, separator, prefix, postfix, limit, truncated, transform, $mask0, $handler):
    visitWhen
    visitWhen
    visitWhen
    visitWhen
    visitWhen
    visitWhen
    return joinTo(buffer, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@cd19d0a, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@4df0eb55, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@6212695e, limit, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@54c77b89, transform)

def all(predicate):
    tmp
    visitWhen
    visitWhen
    tmp0_iterator = iterator()
    while hasNext():
        element = next()
        visitWhen
    
    return visitConst-other

def joinToString(separator, prefix, postfix, limit, truncated, transform):
    return toString()

def joinToString$default(separator, prefix, postfix, limit, truncated, transform, $mask0, $handler):
    visitWhen
    visitWhen
    visitWhen
    visitWhen
    visitWhen
    visitWhen
    return joinToString(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@7546033d, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@d86a616, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@79a4f733, limit, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@add99a4, transform)

def joinTo(buffer, separator, prefix, postfix, limit, truncated, transform):
    append(prefix)
    Unit_getInstance()
    count = 0
    tmp0_iterator = iterator()
    while hasNext():
        element = next()
        count = jsBitOr(jsPlus(count, 1), 0)
        visitWhen
        visitWhen
    
    visitWhen
    append(postfix)
    Unit_getInstance()
    return buffer

def joinTo$default(buffer, separator, prefix, postfix, limit, truncated, transform, $mask0, $handler):
    visitWhen
    visitWhen
    visitWhen
    visitWhen
    visitWhen
    visitWhen
    return joinTo(buffer, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@196cfaed, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@78e52e87, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@2d7157b0, limit, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@1c9c7f1e, transform)

def indexOfFirst(predicate):
    index = 0
    tmp0_iterator = iterator()
    while hasNext():
        item = next()
        visitWhen
        tmp1 = index
        index = jsBitOr(jsPlus(tmp1, 1), 0)
        Unit_getInstance()
    
    return -1

def indexOfLast(predicate):
    iterator = listIterator((special)())
    while hasPrevious():
        visitWhen
    
    return -1

def any(predicate):
    tmp
    visitWhen
    visitWhen
    tmp0_iterator = iterator()
    while hasNext():
        element = next()
        visitWhen
    
    return visitConst-other

def until(to):
    visitWhen
    return numberRangeToNumber((special), visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@71ef979e)

def downTo(to):
    return fromClosedRange((special), to, -1)

def reversed():
    return fromClosedRange(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@4236d55, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@c7eb2a9, jsBitOr(jsUnaryMinus(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@15dbd88e), 0))

def getOrElse(index, defaultValue):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@6cfd4d4d

def KotlinNothingValueException_init_$Init$($this):
    RuntimeException_init_$Init$($this)
    visitDelegatingCOnstructorCall
    return $this

def KotlinNothingValueException_init_$Create$():
    tmp = KotlinNothingValueException_init_$Init$(Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@4795def)
    return tmp

def KotlinNothingValueException_init_$Init$(message, $this):
    RuntimeException_init_$Init$(message, $this)
    visitDelegatingCOnstructorCall
    return $this

def KotlinNothingValueException_init_$Create$(message):
    tmp = KotlinNothingValueException_init_$Init$(message, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@52599443)
    return tmp

def KotlinNothingValueException_init_$Init$(message, cause, $this):
    RuntimeException_init_$Init$(message, cause, $this)
    visitDelegatingCOnstructorCall
    return $this

def KotlinNothingValueException_init_$Create$(message, cause):
    tmp = KotlinNothingValueException_init_$Init$(message, cause, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@28f74096)
    return tmp

def KotlinNothingValueException_init_$Init$(cause, $this):
    RuntimeException_init_$Init$(cause, $this)
    visitDelegatingCOnstructorCall
    return $this

def KotlinNothingValueException_init_$Create$(cause):
    tmp = KotlinNothingValueException_init_$Init$(cause, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@4c9a3ae)
    return tmp

visitClass
visitField
visitField
def values():
    return arrayLiteral(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrVarargImpl@e80fc9d)

def valueOf(value):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@37d85eec

visitField
def Level_initEntries():
    visitWhen
    visitSetField
    visitSetField
    visitSetField

def Experimental_init_$Init$(level, $mask0, $marker, $this):
    visitWhen
    visitDelegatingCOnstructorCall
    return $this

def Experimental_init_$Create$(level, $mask0, $marker):
    return Experimental_init_$Init$(level, $mask0, $marker, Object$create())

visitClass
def Level_WARNING_getInstance():
    Level_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@4bd47b75

def Level_ERROR_getInstance():
    Level_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@47a1b2f7

visitClass
visitClass
visitClass
visitClass
visitClass
visitField
visitField
def values():
    return arrayLiteral(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrVarargImpl@311d2611)

def valueOf(value):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@2bd9722

visitField
def Level_initEntries():
    visitWhen
    visitSetField
    visitSetField
    visitSetField

def RequiresOptIn_init_$Init$(message, level, $mask0, $marker, $this):
    visitWhen
    visitWhen
    visitDelegatingCOnstructorCall
    return $this

def RequiresOptIn_init_$Create$(message, level, $mask0, $marker):
    return RequiresOptIn_init_$Init$(message, level, $mask0, $marker, Object$create())

visitClass
def Level_WARNING_getInstance():
    Level_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@4e02800b

def Level_ERROR_getInstance():
    Level_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@77e03d01

visitClass
visitClass
visitClass
visitClass
def <no name provided>$factory(this$0):
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@22272bac
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@9af804b

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@18c9291e

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@8179cad

def special($this, specialArg):
    visitSetField

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@2168ed92

visitClass
visitClass
visitClass
visitClass
visitField
def Companion_getInstance():
    visitWhen
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@7bf96c4e

visitClass
def special():
    return jsBitOr(jsMinus((special)(), 1), 0)

def emptyList():
    return EmptyList_getInstance()

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@2e7e9897

def readResolve($this):
    return EmptyList_getInstance()

visitClass
visitField
def EmptyList_getInstance():
    visitWhen
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@347c6044

visitClass
visitField
def EmptyIterator_getInstance():
    visitWhen
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@3dd916d9

def removeAll(predicate):
    return filterInPlace(predicate, visitConst-other)

def removeAll(predicate):
    return filterInPlace(predicate, visitConst-other)

def filterInPlace(predicate, predicateResultToRemove):
    visitWhen
    writeIndex = 0
    inductionVariable = 0
    last = (special)()
    visitWhen
    visitWhen

def filterInPlace(predicate, predicateResultToRemove):
    result = visitConst-other
    tmp0_with_0 = iterator()
    while hasNext():
        visitWhen
    
    return result

visitClass
def contract(builder):
    

visitClass
visitField
visitField
visitField
visitField
def values():
    return arrayLiteral(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrVarargImpl@4f2a0651)

def valueOf(value):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@bf3fe88

visitField
def InvocationKind_initEntries():
    visitWhen
    visitSetField
    visitSetField
    visitSetField
    visitSetField
    visitSetField

visitClass
visitClass
def InvocationKind_AT_MOST_ONCE_getInstance():
    InvocationKind_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@7c698549

def InvocationKind_AT_LEAST_ONCE_getInstance():
    InvocationKind_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@75a45ce

def InvocationKind_EXACTLY_ONCE_getInstance():
    InvocationKind_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@6910e725

def InvocationKind_UNKNOWN_getInstance():
    InvocationKind_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@4c721f6b

visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
def Continuation(context, resumeWith):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@65a03e98

def resumeWithException(exception):
    tmp0_failure_0 = Companion_getInstance()
    return resumeWith(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@194ff162)

def resume(value):
    tmp0_success_0 = Companion_getInstance()
    return resumeWith(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@599bda7e)

def special():
    visitThrow

visitClass
visitClass
visitField
def Key_getInstance():
    visitWhen
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@389b2c60

visitClass
visitClass
visitClass
visitClass
visitClass
def <no name provided>$factory():
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@7b301349
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@6b1be058

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@7aa146e5

def readResolve($this):
    return EmptyCoroutineContext_getInstance()

visitClass
visitField
def EmptyCoroutineContext_getInstance():
    visitWhen
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@145f22cf

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@6a35f9fd

visitClass
visitField
def Companion_getInstance():
    visitWhen
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@435ec7f5

def readResolve($this):
    tmp0_fold_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@1a4ccb7b
    tmp1_fold_0 = EmptyCoroutineContext_getInstance()
    accumulator_1 = tmp1_fold_0
    indexedObject = tmp0_fold_0
    inductionVariable = 0
    last = jsArrayLength(indexedObject)
    while jsLt(inductionVariable, last):
        element_3 = jsArrayGet(indexedObject, inductionVariable)
        inductionVariable = jsBitOr(jsPlus(inductionVariable, 1), 0)
        accumulator_1 = plus(element_3)
    
    return accumulator_1

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@16e2a7be

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@1e6f7127

def size($this):
    cur = $this
    size = 2
    while visitConst-other:
        tmp = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@1603d1fb
        tmp0_elvis_lhs = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@2d3f6e6
        tmp
        visitWhen
        cur = tmp
        tmp1 = size
        size = jsBitOr(jsPlus(tmp1, 1), 0)
        Unit_getInstance()
    

def contains($this, element):
    return equals(get((special)()), element)

def containsAll($this, context):
    cur = context
    while visitConst-other:
        visitWhen
        next = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@685a8158
        visitWhen
    

def writeReplace($this):
    n = size($this)
    elements = fillArrayVal(Array(n), visitConst-other)
    index = $sharedBox$create(0)
    fold(Unit_getInstance(), <no name provided>$factory(elements, index))
    tmp0_check_0 = jsEqeqeq($sharedBox$read(index), n)
    visitWhen
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@464c18c8

visitClass
visitClass
visitClass
visitClass
def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@415b83fa

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@18870976

visitClass
def <no name provided>$factory():
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@7a8ea
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@2f193a75

def <no name provided>$factory($elements, $index):
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@9129682
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@4c44ed49

def special():
    return CoroutineSingletons_COROUTINE_SUSPENDED_getInstance()

visitField
visitField
visitField
def values():
    return arrayLiteral(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrVarargImpl@1235abb2)

def valueOf(value):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@4a9d481b

visitField
def CoroutineSingletons_initEntries():
    visitWhen
    visitSetField
    visitSetField
    visitSetField
    visitSetField

visitClass
def CoroutineSingletons_COROUTINE_SUSPENDED_getInstance():
    CoroutineSingletons_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@529e1192

def CoroutineSingletons_UNDECIDED_getInstance():
    CoroutineSingletons_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@7e83251e

def CoroutineSingletons_RESUMED_getInstance():
    CoroutineSingletons_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@400ed209

def and(other):
    return toByte(jsBitAnd(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@245b6b85, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@1da9b95d))

def or(other):
    return toByte(jsBitOr(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@76fabd1, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@4e6fb132))

def xor(other):
    return toByte(jsBitXor(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@4b8816f7, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@56a2599a))

def inv():
    return toByte(jsBitNot(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@66c9f7))

def and(other):
    return toShort(jsBitAnd(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@19f31c85, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@553f3655))

def or(other):
    return toShort(jsBitOr(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@6b4499f1, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@4fa8389b))

def xor(other):
    return toShort(jsBitXor(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@30c716ce, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@2a8953aa))

def inv():
    return toShort(jsBitNot(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@66f73411))

visitClass
def RequireKotlin_init_$Init$(version, message, level, versionKind, errorCode, $mask0, $marker, $this):
    visitWhen
    visitWhen
    visitWhen
    visitWhen
    visitDelegatingCOnstructorCall
    return $this

def RequireKotlin_init_$Create$(version, message, level, versionKind, errorCode, $mask0, $marker):
    return RequireKotlin_init_$Init$(version, message, level, versionKind, errorCode, $mask0, $marker, Object$create())

visitClass
visitField
visitField
visitField
def values():
    return arrayLiteral(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrVarargImpl@4eb870be)

def valueOf(value):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@63dd100c

visitField
def RequireKotlinVersionKind_initEntries():
    visitWhen
    visitSetField
    visitSetField
    visitSetField
    visitSetField

visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
def RequireKotlinVersionKind_LANGUAGE_VERSION_getInstance():
    RequireKotlinVersionKind_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@2cc76912

def RequireKotlinVersionKind_COMPILER_VERSION_getInstance():
    RequireKotlinVersionKind_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@769c4312

def RequireKotlinVersionKind_API_VERSION_getInstance():
    RequireKotlinVersionKind_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@56c92651

visitClass
visitClass
visitClass
visitField
def Companion_getInstance():
    visitWhen
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@127b9bed

visitClass
visitField
visitField
visitField
def values():
    return arrayLiteral(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrVarargImpl@4bf4cd2e)

def valueOf(value):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@7efceb57

visitField
def KVariance_initEntries():
    visitWhen
    visitSetField
    visitSetField
    visitSetField
    visitSetField

visitClass
def KVariance_INVARIANT_getInstance():
    KVariance_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@2839ac4c

def KVariance_IN_getInstance():
    KVariance_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@5b9b7370

def KVariance_OUT_getInstance():
    KVariance_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@1b3b95e8

def appendElement(element, transform):
    visitWhen

def isEmpty():
    return jsEqeqeq(charSequenceLength((special)), 0)

def special():
    return jsBitOr(jsMinus(charSequenceLength((special)), 1), 0)

def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@1a06b95

visitField
def UNDEFINED_RESULT$init$():
    tmp0_success_0 = Companion_getInstance()
    tmp1_success_0 = (special)()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@28cd26de

def check(value):
    visitWhen

def check(value, lazyMessage):
    visitWhen

def error(message):
    visitThrow

def require(value, lazyMessage):
    visitWhen

def special(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@12aa2cca

def special(this):
    tmp = (special)(this)
    return jsNot(jsInstanceOf(tmp, jsClass()))

def special(this):
    tmp = (special)(this)
    return jsInstanceOf(tmp, jsClass())

def Result__getOrNull-impl(this):
    tmp
    visitWhen
    return tmp

def Result__exceptionOrNull-impl(this):
    tmp0_subject = (special)(this)
    tmp
    visitWhen
    return tmp

def Result__toString-impl(this):
    tmp0_subject = (special)(this)
    tmp
    visitWhen
    return tmp

visitClass
visitField
def Companion_getInstance():
    visitWhen
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@b11d2ad

visitClass
def Result__hashCode-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@3fe9caee

def Result__equals-impl(this, other):
    visitWhen
    tmp0_other_with_cast = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@5d489be4
    visitWhen
    return visitConst-other

visitClass
def createFailure(exception):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@7eb94590

def getOrThrow():
    throwOnFailure()
    tmp = (special)((special))
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@6cb2e94

def throwOnFailure():
    tmp = (special)((special))
    visitWhen

def run(block):
    return invoke()

def TODO():
    visitThrow

def NotImplementedError_init_$Init$(message, $mask0, $marker, $this):
    visitWhen
    visitDelegatingCOnstructorCall
    return $this

def NotImplementedError_init_$Create$(message, $mask0, $marker):
    tmp = NotImplementedError_init_$Init$(message, $mask0, $marker, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@1d2414a1)
    return tmp

visitClass
def let(block):
    return invoke((special))

def also(block):
    invoke((special))
    return (special)

def with(receiver, block):
    return invoke(receiver)

def run(block):
    return invoke((special))

def apply(block):
    invoke((special))
    return (special)

def repeat(times, action):
    inductionVariable = 0
    visitWhen

def special(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@143900a6

visitClass
visitField
def Companion_getInstance():
    visitWhen
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@3a0f0552

def UByte__compareTo-impl(this, other):
    tmp = jsBitAnd(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@2e259c54, 255)
    return compareTo(tmp, jsBitAnd(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@3ff4ed56, 255))

def UByte__compareTo-impl(this, other):
    tmp = unboxIntrinsic(this)
    return UByte__compareTo-impl(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@5bff7f13)

def UByte__compareTo-impl(this, other):
    tmp = jsBitAnd(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@79849cab, 255)
    return compareTo(tmp, jsBitAnd(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@725645f4, 65535))

def UByte__compareTo-impl(this, other):
    tmp0_compareTo_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@53a95744
    return uintCompare((special)(tmp0_compareTo_0), (special)(other))

def UByte__compareTo-impl(this, other):
    tmp0_compareTo_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@37e6ecd3
    return ulongCompare((special)(tmp0_compareTo_0), (special)(other))

def UByte__plus-impl(this, other):
    tmp0_plus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@1b8354aa
    tmp1_plus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@1eecc98c
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@75bd7c4a

def UByte__plus-impl(this, other):
    tmp0_plus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@54fe40e0
    tmp1_plus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@51867eab
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@441ccfd7

def UByte__plus-impl(this, other):
    tmp0_plus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4cd6143c
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@b956293

def UByte__plus-impl(this, other):
    tmp0_plus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@17163282
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@f406ea2

def UByte__minus-impl(this, other):
    tmp0_minus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5e81d985
    tmp1_minus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@74c2edc
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@475414c0

def UByte__minus-impl(this, other):
    tmp0_minus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@2d7956fb
    tmp1_minus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@11f2ef6a
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@1bf596f8

def UByte__minus-impl(this, other):
    tmp0_minus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@ffc9278
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@10e88abc

def UByte__minus-impl(this, other):
    tmp0_minus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5e454172
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@3e1c58c9

def UByte__times-impl(this, other):
    tmp0_times_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4f401aac
    tmp1_times_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@a04462d
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@609047a6

def UByte__times-impl(this, other):
    tmp0_times_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@467c77b2
    tmp1_times_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5ed76e4f
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@11972f4a

def UByte__times-impl(this, other):
    tmp0_times_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@16a58368
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5e409078

def UByte__times-impl(this, other):
    tmp0_times_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@1531ec6
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@3248b221

def UByte__div-impl(this, other):
    tmp0_div_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@60eabf53
    tmp1_div_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@f60910d
    return uintDivide(tmp0_div_0, tmp1_div_0)

def UByte__div-impl(this, other):
    tmp0_div_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@16c5974d
    tmp1_div_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@62832e24
    return uintDivide(tmp0_div_0, tmp1_div_0)

def UByte__div-impl(this, other):
    tmp0_div_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@699a53d4
    return uintDivide(tmp0_div_0, other)

def UByte__div-impl(this, other):
    tmp0_div_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@73344756
    return ulongDivide(tmp0_div_0, other)

def UByte__rem-impl(this, other):
    tmp0_rem_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@766f7bb1
    tmp1_rem_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@3f341562
    return uintRemainder(tmp0_rem_0, tmp1_rem_0)

def UByte__rem-impl(this, other):
    tmp0_rem_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@58f252fe
    tmp1_rem_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@49c50140
    return uintRemainder(tmp0_rem_0, tmp1_rem_0)

def UByte__rem-impl(this, other):
    tmp0_rem_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@581242e1
    return uintRemainder(tmp0_rem_0, other)

def UByte__rem-impl(this, other):
    tmp0_rem_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@2ffb6cf6
    return ulongRemainder(tmp0_rem_0, other)

def UByte__inc-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4064daeb

def UByte__dec-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@d750a

def UByte__rangeTo-impl(this, other):
    tmp = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@7522ea53
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@3d426638

def UByte__and-impl(this, other):
    tmp0_and_0 = (special)(this)
    tmp1_and_0 = (special)(other)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@11db4d00

def UByte__or-impl(this, other):
    tmp0_or_0 = (special)(this)
    tmp1_or_0 = (special)(other)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@614220b8

def UByte__xor-impl(this, other):
    tmp0_xor_0 = (special)(this)
    tmp1_xor_0 = (special)(other)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@44c74781

def UByte__inv-impl(this):
    tmp0_inv_0 = (special)(this)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5233b9e0

def UByte__toByte-impl(this):
    return (special)(this)

def UByte__toShort-impl(this):
    tmp0_and_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@66e33cea
    tmp1_and_0 = visitConst-other
    return toShort(jsBitAnd(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@625b9f43, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@467686b2))

def UByte__toInt-impl(this):
    return jsBitAnd(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@3426ce80, 255)

def UByte__toLong-impl(this):
    return and(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@18ca3125)

def UByte__toUByte-impl(this):
    return this

def UByte__toUShort-impl(this):
    tmp0_and_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@23b34af8
    tmp1_and_0 = visitConst-other
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@3df17e4b

def UByte__toUInt-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@b280053

def UByte__toULong-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@1a5cb2b3

def UByte__toFloat-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@4b495ce7

def UByte__toDouble-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@d367d7d

def UByte__toString-impl(this):
    return toString()

def UByte__hashCode-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@50e4d8cd

def UByte__equals-impl(this, other):
    visitWhen
    tmp0_other_with_cast = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@6fb68c4
    visitWhen
    return visitConst-other

visitClass
def toUByte():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@236ec69

def toUByte():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@31373fc1

def toUByte():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@243dc57b

def toUByte():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4caca1

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@61c98b6c

def special($this, specialArg):
    visitSetField

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@1b406bc2

def special(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@63614cdd

def special(size):
    tmp = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@6371c6ee
    return tmp

def UByteArray__get-impl(this, index):
    tmp0_toUByte_0 = jsArrayGet((special)(this), index)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5c486c5a

def UByteArray__set-impl(this, index, value):
    tmp = (special)(this)
    jsArraySet(tmp, index, (special)(value))

def special(this):
    return jsArrayLength((special)(this))

def UByteArray__iterator-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@526f8cb0

visitClass
def UByteArray__contains-impl(this, element):
    tmp = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@198fb504
    visitWhen
    tmp = (special)(this)
    return contains((special)(element))

def UByteArray__contains-impl(this, element):
    visitWhen
    tmp = unboxIntrinsic(this)
    return UByteArray__contains-impl(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@77e86a53)

def UByteArray__containsAll-impl(this, elements):
    tmp$ret$0
    visitDoWhileLoop
    return tmp$ret$0

def UByteArray__containsAll-impl(this, elements):
    return UByteArray__containsAll-impl(unboxIntrinsic(this), elements)

def UByteArray__isEmpty-impl(this):
    return jsEqeqeq(jsArrayLength((special)(this)), 0)

def UByteArray__toString-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrStringConcatenationImpl@45b97486

def UByteArray__hashCode-impl(this):
    return hashCode(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@136a4800)

def UByteArray__equals-impl(this, other):
    visitWhen
    tmp0_other_with_cast = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@c18ee56
    visitWhen
    return visitConst-other

visitClass
def special(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@5b3c11ce

visitClass
visitField
def Companion_getInstance():
    visitWhen
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@6ffbae2e

def UInt__compareTo-impl(this, other):
    tmp0_compareTo_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5590d10f
    return uintCompare((special)(this), (special)(tmp0_compareTo_0))

def UInt__compareTo-impl(this, other):
    tmp0_compareTo_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@f6bcac8
    return uintCompare((special)(this), (special)(tmp0_compareTo_0))

def UInt__compareTo-impl(this, other):
    return uintCompare((special)(this), (special)(other))

def UInt__compareTo-impl(this, other):
    tmp = unboxIntrinsic(this)
    return UInt__compareTo-impl(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@481beb8b)

def UInt__compareTo-impl(this, other):
    tmp0_compareTo_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@68e3c94
    return ulongCompare((special)(tmp0_compareTo_0), (special)(other))

def UInt__plus-impl(this, other):
    tmp0_plus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@6b6eaa73
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@1cdb0d7b

def UInt__plus-impl(this, other):
    tmp0_plus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@6281326f
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@29457ad2

def UInt__plus-impl(this, other):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4643d88c

def UInt__plus-impl(this, other):
    tmp0_plus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@31ec9703
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@b8be217

def UInt__minus-impl(this, other):
    tmp0_minus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@361c008
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@2f5185ec

def UInt__minus-impl(this, other):
    tmp0_minus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4ba97a4
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@715ab10f

def UInt__minus-impl(this, other):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@3325afbc

def UInt__minus-impl(this, other):
    tmp0_minus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4ba5272e
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@7fb7be26

def UInt__times-impl(this, other):
    tmp0_times_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@2571d0c
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@2d87ac2b

def UInt__times-impl(this, other):
    tmp0_times_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4c1c9116
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4a57cec1

def UInt__times-impl(this, other):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@1ebbb581

def UInt__times-impl(this, other):
    tmp0_times_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5eb20abb
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@7590b28f

def UInt__div-impl(this, other):
    tmp0_div_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@44f6c323
    return uintDivide(this, tmp0_div_0)

def UInt__div-impl(this, other):
    tmp0_div_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@7191c18b
    return uintDivide(this, tmp0_div_0)

def UInt__div-impl(this, other):
    return uintDivide(this, other)

def UInt__div-impl(this, other):
    tmp0_div_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@14cc127b
    return ulongDivide(tmp0_div_0, other)

def UInt__rem-impl(this, other):
    tmp0_rem_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@40d6d07c
    return uintRemainder(this, tmp0_rem_0)

def UInt__rem-impl(this, other):
    tmp0_rem_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@988f4d5
    return uintRemainder(this, tmp0_rem_0)

def UInt__rem-impl(this, other):
    return uintRemainder(this, other)

def UInt__rem-impl(this, other):
    tmp0_rem_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@57cf5515
    return ulongRemainder(tmp0_rem_0, other)

def UInt__inc-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@66837d7b

def UInt__dec-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@47bdfc41

def UInt__rangeTo-impl(this, other):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@10a55edc

def UInt__shl-impl(this, bitCount):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@27e9ac69

def UInt__shr-impl(this, bitCount):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@482f1b64

def UInt__and-impl(this, other):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@22ccf63d

def UInt__or-impl(this, other):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@16e557d4

def UInt__xor-impl(this, other):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@1640a06f

def UInt__inv-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@58c4d427

def UInt__toByte-impl(this):
    return toByte((special)(this))

def UInt__toShort-impl(this):
    return toShort((special)(this))

def UInt__toInt-impl(this):
    return (special)(this)

def UInt__toLong-impl(this):
    return and(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@77dd1899)

def UInt__toUByte-impl(this):
    tmp0_toUByte_0 = (special)(this)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@45bd83de

def UInt__toUShort-impl(this):
    tmp0_toUShort_0 = (special)(this)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@54932357

def UInt__toUInt-impl(this):
    return this

def UInt__toULong-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@1878815a

def UInt__toFloat-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@2d21dca2

def UInt__toDouble-impl(this):
    return uintToDouble((special)(this))

def UInt__toString-impl(this):
    return toString()

def UInt__hashCode-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@62c1259f

def UInt__equals-impl(this, other):
    visitWhen
    tmp0_other_with_cast = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@13a47638
    visitWhen
    return visitConst-other

visitClass
def toUInt():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@16819885

def toUInt():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@559b4958

def toUInt():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@7ec6cb51

def toUInt():
    return doubleToUInt((special))

def toUInt():
    return doubleToUInt(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@6d7453ad)

def toUInt():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@58ae7e50

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@2fab6393

def special($this, specialArg):
    visitSetField

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@6b869242

def special(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@3724ab90

def special(size):
    tmp = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@501dd0b4
    return tmp

def UIntArray__get-impl(this, index):
    tmp0_toUInt_0 = jsArrayGet((special)(this), index)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@3023a901

def UIntArray__set-impl(this, index, value):
    tmp = (special)(this)
    jsArraySet(tmp, index, (special)(value))

def special(this):
    return jsArrayLength((special)(this))

def UIntArray__iterator-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4e0139

visitClass
def UIntArray__contains-impl(this, element):
    tmp = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@fc3fd5b
    visitWhen
    tmp = (special)(this)
    return contains((special)(element))

def UIntArray__contains-impl(this, element):
    visitWhen
    tmp = unboxIntrinsic(this)
    return UIntArray__contains-impl(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@1d1daaa3)

def UIntArray__containsAll-impl(this, elements):
    tmp$ret$0
    visitDoWhileLoop
    return tmp$ret$0

def UIntArray__containsAll-impl(this, elements):
    return UIntArray__containsAll-impl(unboxIntrinsic(this), elements)

def UIntArray__isEmpty-impl(this):
    return jsEqeqeq(jsArrayLength((special)(this)), 0)

def UIntArray__toString-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrStringConcatenationImpl@521090f1

def UIntArray__hashCode-impl(this):
    return hashCode(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@39a1e1e6)

def UIntArray__equals-impl(this, other):
    visitWhen
    tmp0_other_with_cast = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@5c98b98
    visitWhen
    return visitConst-other

visitClass
visitClass
visitField
def Companion_getInstance():
    visitWhen
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@19f7179

visitClass
visitClass
visitField
def Companion_getInstance():
    visitWhen
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@357a3cb9

visitClass
def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@4ed5c276

def special($this, specialArg):
    visitSetField

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@329b6556

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@5c35a03b

def special($this, specialArg):
    visitSetField

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@1642ef89

visitClass
visitClass
visitClass
visitClass
visitClass
def special(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@2c485b3a

visitClass
visitField
def Companion_getInstance():
    visitWhen
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@1543b936

def ULong__compareTo-impl(this, other):
    tmp0_compareTo_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@2c04e8e7
    return ulongCompare((special)(this), (special)(tmp0_compareTo_0))

def ULong__compareTo-impl(this, other):
    tmp0_compareTo_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@51e9f462
    return ulongCompare((special)(this), (special)(tmp0_compareTo_0))

def ULong__compareTo-impl(this, other):
    tmp0_compareTo_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4b71aee1
    return ulongCompare((special)(this), (special)(tmp0_compareTo_0))

def ULong__compareTo-impl(this, other):
    return ulongCompare((special)(this), (special)(other))

def ULong__compareTo-impl(this, other):
    tmp = unboxIntrinsic(this)
    return ULong__compareTo-impl(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@6689f455)

def ULong__plus-impl(this, other):
    tmp0_plus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@7c3341c9
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@65a5cc92

def ULong__plus-impl(this, other):
    tmp0_plus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5a5c0f56
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@390c96a1

def ULong__plus-impl(this, other):
    tmp0_plus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@460dc324
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@1ea555d

def ULong__plus-impl(this, other):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@1771700b

def ULong__minus-impl(this, other):
    tmp0_minus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@25db0f54
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@2691ebbe

def ULong__minus-impl(this, other):
    tmp0_minus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@24dbdfa0
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@2d64757a

def ULong__minus-impl(this, other):
    tmp0_minus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4968eb3f
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@418a5228

def ULong__minus-impl(this, other):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5e8f7cf4

def ULong__times-impl(this, other):
    tmp0_times_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@19121e33
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@7584b20d

def ULong__times-impl(this, other):
    tmp0_times_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@95a02c0
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@40e43e10

def ULong__times-impl(this, other):
    tmp0_times_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@60600939
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4e6eb11d

def ULong__times-impl(this, other):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@61650e2d

def ULong__div-impl(this, other):
    tmp0_div_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@55a690be
    return ulongDivide(this, tmp0_div_0)

def ULong__div-impl(this, other):
    tmp0_div_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@482e1d45
    return ulongDivide(this, tmp0_div_0)

def ULong__div-impl(this, other):
    tmp0_div_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@67c8ca0f
    return ulongDivide(this, tmp0_div_0)

def ULong__div-impl(this, other):
    return ulongDivide(this, other)

def ULong__rem-impl(this, other):
    tmp0_rem_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@220f319a
    return ulongRemainder(this, tmp0_rem_0)

def ULong__rem-impl(this, other):
    tmp0_rem_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@21e896f6
    return ulongRemainder(this, tmp0_rem_0)

def ULong__rem-impl(this, other):
    tmp0_rem_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@7430d369
    return ulongRemainder(this, tmp0_rem_0)

def ULong__rem-impl(this, other):
    return ulongRemainder(this, other)

def ULong__inc-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@641ce448

def ULong__dec-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@2c4bee34

def ULong__rangeTo-impl(this, other):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@697699cb

def ULong__shl-impl(this, bitCount):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@2818d9d7

def ULong__shr-impl(this, bitCount):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@2e92c6f3

def ULong__and-impl(this, other):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@50e4e803

def ULong__or-impl(this, other):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@21fd75f2

def ULong__xor-impl(this, other):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@74e17634

def ULong__inv-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@50a0404b

def ULong__toByte-impl(this):
    return toByte()

def ULong__toShort-impl(this):
    return toShort()

def ULong__toInt-impl(this):
    return toInt()

def ULong__toLong-impl(this):
    return (special)(this)

def ULong__toUByte-impl(this):
    tmp0_toUByte_0 = (special)(this)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@58b4f4a

def ULong__toUShort-impl(this):
    tmp0_toUShort_0 = (special)(this)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@7aef5ab9

def ULong__toUInt-impl(this):
    tmp0_toUInt_0 = (special)(this)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@14e79d6

def ULong__toULong-impl(this):
    return this

def ULong__toFloat-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@4b5954bf

def ULong__toDouble-impl(this):
    return ulongToDouble((special)(this))

def ULong__toString-impl(this):
    return ulongToString((special)(this))

def ULong__hashCode-impl(this):
    return hashCode()

def ULong__equals-impl(this, other):
    visitWhen
    tmp0_other_with_cast = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@71498a88
    visitWhen
    return visitConst-other

visitClass
def toULong():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@33bbedab

def toULong():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4483da9

def toULong():
    return doubleToULong((special))

def toULong():
    return doubleToULong(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@4f62767c)

def toULong():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@39b7e568

def toULong():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5a9886c7

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@3770938d

def special($this, specialArg):
    visitSetField

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@7419c8e2

def special(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@46baac0d

def special(size):
    tmp = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5b8fa102
    return tmp

def ULongArray__get-impl(this, index):
    tmp0_toULong_0 = jsArrayGet((special)(this), index)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@46fd6d87

def ULongArray__set-impl(this, index, value):
    tmp = (special)(this)
    jsArraySet(tmp, index, (special)(value))

def special(this):
    return jsArrayLength((special)(this))

def ULongArray__iterator-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@237b54bc

visitClass
def ULongArray__contains-impl(this, element):
    tmp = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@6b5b5f94
    visitWhen
    tmp = (special)(this)
    return contains((special)(element))

def ULongArray__contains-impl(this, element):
    visitWhen
    tmp = unboxIntrinsic(this)
    return ULongArray__contains-impl(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@26ceca00)

def ULongArray__containsAll-impl(this, elements):
    tmp$ret$0
    visitDoWhileLoop
    return tmp$ret$0

def ULongArray__containsAll-impl(this, elements):
    return ULongArray__containsAll-impl(unboxIntrinsic(this), elements)

def ULongArray__isEmpty-impl(this):
    return jsEqeqeq(jsArrayLength((special)(this)), 0)

def ULongArray__toString-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrStringConcatenationImpl@59919f37

def ULongArray__hashCode-impl(this):
    return hashCode(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@27a23d87)

def ULongArray__equals-impl(this, other):
    visitWhen
    tmp0_other_with_cast = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@32f17e62
    visitWhen
    return visitConst-other

visitClass
visitClass
visitField
def Companion_getInstance():
    visitWhen
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@107852a

visitClass
visitClass
visitField
def Companion_getInstance():
    visitWhen
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@2c193600

visitClass
def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@65669fbb

def special($this, specialArg):
    visitSetField

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@4f405fa7

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@64deb236

def special($this, specialArg):
    visitSetField

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@506e35b9

visitClass
def getProgressionLastElement(start, end, step):
    tmp
    visitWhen
    return tmp

def getProgressionLastElement(start, end, step):
    tmp
    visitWhen
    return tmp

def differenceModulo(a, b, c):
    ac = uintRemainder(a, c)
    bc = uintRemainder(b, c)
    tmp
    visitWhen
    return tmp

def differenceModulo(a, b, c):
    ac = ulongRemainder(a, c)
    bc = ulongRemainder(b, c)
    tmp
    visitWhen
    return tmp

def special(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@455cb6d9

visitClass
visitField
def Companion_getInstance():
    visitWhen
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@6608c8d5

def UShort__compareTo-impl(this, other):
    tmp = jsBitAnd(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@7ae8a6eb, 65535)
    return compareTo(tmp, jsBitAnd(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@5cb41e93, 255))

def UShort__compareTo-impl(this, other):
    tmp = jsBitAnd(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@30f139f, 65535)
    return compareTo(tmp, jsBitAnd(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@6c65578d, 65535))

def UShort__compareTo-impl(this, other):
    tmp = unboxIntrinsic(this)
    return UShort__compareTo-impl(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@21d1f97f)

def UShort__compareTo-impl(this, other):
    tmp0_compareTo_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@7fc9253c
    return uintCompare((special)(tmp0_compareTo_0), (special)(other))

def UShort__compareTo-impl(this, other):
    tmp0_compareTo_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@15944e4e
    return ulongCompare((special)(tmp0_compareTo_0), (special)(other))

def UShort__plus-impl(this, other):
    tmp0_plus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@43fd117c
    tmp1_plus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@50bdd956
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@6d445c91

def UShort__plus-impl(this, other):
    tmp0_plus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@2fbdc8e
    tmp1_plus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@407e7434
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@8d902f

def UShort__plus-impl(this, other):
    tmp0_plus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@3a784248
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4daaad61

def UShort__plus-impl(this, other):
    tmp0_plus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@636aef2e
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@63306e58

def UShort__minus-impl(this, other):
    tmp0_minus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@7a832964
    tmp1_minus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5ccf13a9
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@49fdc88e

def UShort__minus-impl(this, other):
    tmp0_minus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@400fcb68
    tmp1_minus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@8a99989
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@1aff6f46

def UShort__minus-impl(this, other):
    tmp0_minus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@570cf9d5
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@3848c63

def UShort__minus-impl(this, other):
    tmp0_minus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@30ad845d
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@27504ed3

def UShort__times-impl(this, other):
    tmp0_times_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@598c23ad
    tmp1_times_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@1d215a52
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@205fc00e

def UShort__times-impl(this, other):
    tmp0_times_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@2b4f1b37
    tmp1_times_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@61be6b03
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@23f7ed9d

def UShort__times-impl(this, other):
    tmp0_times_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@27d74f45
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@2421fd62

def UShort__times-impl(this, other):
    tmp0_times_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@387051e3
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@1a6bcdf9

def UShort__div-impl(this, other):
    tmp0_div_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@29b8a9a9
    tmp1_div_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@514111ca
    return uintDivide(tmp0_div_0, tmp1_div_0)

def UShort__div-impl(this, other):
    tmp0_div_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5a405492
    tmp1_div_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@70602f49
    return uintDivide(tmp0_div_0, tmp1_div_0)

def UShort__div-impl(this, other):
    tmp0_div_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@9bd2d60
    return uintDivide(tmp0_div_0, other)

def UShort__div-impl(this, other):
    tmp0_div_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@74e37ad3
    return ulongDivide(tmp0_div_0, other)

def UShort__rem-impl(this, other):
    tmp0_rem_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@7ef2f14e
    tmp1_rem_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@3bf27b93
    return uintRemainder(tmp0_rem_0, tmp1_rem_0)

def UShort__rem-impl(this, other):
    tmp0_rem_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@3b8c9157
    tmp1_rem_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@561f276a
    return uintRemainder(tmp0_rem_0, tmp1_rem_0)

def UShort__rem-impl(this, other):
    tmp0_rem_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@49692c4f
    return uintRemainder(tmp0_rem_0, other)

def UShort__rem-impl(this, other):
    tmp0_rem_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@450a6a51
    return ulongRemainder(tmp0_rem_0, other)

def UShort__inc-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5d4493cc

def UShort__dec-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@361b682b

def UShort__rangeTo-impl(this, other):
    tmp = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@a2dc92d
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@41d280cf

def UShort__and-impl(this, other):
    tmp0_and_0 = (special)(this)
    tmp1_and_0 = (special)(other)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@513f965e

def UShort__or-impl(this, other):
    tmp0_or_0 = (special)(this)
    tmp1_or_0 = (special)(other)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@c9ec20e

def UShort__xor-impl(this, other):
    tmp0_xor_0 = (special)(this)
    tmp1_xor_0 = (special)(other)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@528a7eea

def UShort__inv-impl(this):
    tmp0_inv_0 = (special)(this)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@48f1968e

def UShort__toByte-impl(this):
    return toByte((special)(this))

def UShort__toShort-impl(this):
    return (special)(this)

def UShort__toInt-impl(this):
    return jsBitAnd(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@ef76bed, 65535)

def UShort__toLong-impl(this):
    return and(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@218cf600)

def UShort__toUByte-impl(this):
    tmp0_toUByte_0 = (special)(this)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@7a0d71d4

def UShort__toUShort-impl(this):
    return this

def UShort__toUInt-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@3b1bf4bf

def UShort__toULong-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@36c1b50d

def UShort__toFloat-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@36840e6c

def UShort__toDouble-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@7553d28b

def UShort__toString-impl(this):
    return toString()

def UShort__hashCode-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@2a9fd482

def UShort__equals-impl(this, other):
    visitWhen
    tmp0_other_with_cast = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@6d24d173
    visitWhen
    return visitConst-other

visitClass
def toUShort():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@1f041bad

def toUShort():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@1bb425e4

def toUShort():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@42122f28

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@2e3622a6

def special($this, specialArg):
    visitSetField

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@7c465f15

def special(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@2fda92e0

def special(size):
    tmp = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@7e06727f
    return tmp

def UShortArray__get-impl(this, index):
    tmp0_toUShort_0 = jsArrayGet((special)(this), index)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5614c340

def UShortArray__set-impl(this, index, value):
    tmp = (special)(this)
    jsArraySet(tmp, index, (special)(value))

def special(this):
    return jsArrayLength((special)(this))

def UShortArray__iterator-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@37c49a55

visitClass
def UShortArray__contains-impl(this, element):
    tmp = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@429a6f95
    visitWhen
    tmp = (special)(this)
    return contains((special)(element))

def UShortArray__contains-impl(this, element):
    visitWhen
    tmp = unboxIntrinsic(this)
    return UShortArray__contains-impl(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@b9f6daa)

def UShortArray__containsAll-impl(this, elements):
    tmp$ret$0
    visitDoWhileLoop
    return tmp$ret$0

def UShortArray__containsAll-impl(this, elements):
    return UShortArray__containsAll-impl(unboxIntrinsic(this), elements)

def UShortArray__isEmpty-impl(this):
    return jsEqeqeq(jsArrayLength((special)(this)), 0)

def UShortArray__toString-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrStringConcatenationImpl@656fcf12

def UShortArray__hashCode-impl(this):
    return hashCode(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@73bd146c)

def UShortArray__equals-impl(this, other):
    visitWhen
    tmp0_other_with_cast = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@522ef462
    visitWhen
    return visitConst-other

visitClass
def uintCompare(v1, v2):
    return compareTo(jsBitXor(v1, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@5afc4816), jsBitXor(v2, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@2b9f2f24))

def uintDivide(v1, v2):
    tmp = and(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@bda763e)
    tmp0_toUInt_0 = div(and(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5eac0402))
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@7d8b1735

def uintRemainder(v1, v2):
    tmp = and(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@52b4071c)
    tmp0_toUInt_0 = rem(and(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@59acd853))
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4fbac930

def uintToDouble(v):
    return jsPlus(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@268e6451, jsMult(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@51ac1dce, 2))

def ulongCompare(v1, v2):
    return compareTo(xor(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@8d70fd))

def ulongDivide(v1, v2):
    dividend = (special)(v1)
    divisor = (special)(v2)
    visitWhen
    visitWhen
    quotient = shl(1)
    rem = minus(times(divisor))
    tmp
    tmp0_compareTo_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@72924f19
    tmp1_compareTo_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4ff00844
    visitWhen
    tmp2_plus_0 = tmp
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@289b7efe

def ulongRemainder(v1, v2):
    dividend = (special)(v1)
    divisor = (special)(v2)
    visitWhen
    visitWhen
    quotient = shl(1)
    rem = minus(times(divisor))
    tmp
    tmp0_compareTo_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@3b4b2c03
    tmp1_compareTo_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5fb58f15
    visitWhen
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4e58eda2

def ulongToDouble(v):
    return jsPlus(jsMult(toDouble(), 2048), toDouble())

def ulongToString(v):
    return ulongToString(v, 10)

def ulongToString(v, base):
    visitWhen
    tmp0_div_0 = ushr(1)
    quotient = shl(1)
    tmp1_times_0 = quotient
    rem = minus(times(toLong(base)))
    visitWhen
    return jsPlus(toString(base), toString(base))

def doubleToUInt(v):
    tmp
    visitWhen
    return tmp

def doubleToULong(v):
    tmp
    visitWhen
    return tmp

visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
visitField
visitField
visitField
def values():
    return arrayLiteral(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrVarargImpl@37805004)

def valueOf(value):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@46329e85

visitField
def DeprecationLevel_initEntries():
    visitWhen
    visitSetField
    visitSetField
    visitSetField
    visitSetField

visitClass
visitClass
visitClass
def Deprecated_init_$Init$(message, replaceWith, level, $mask0, $marker, $this):
    visitWhen
    visitWhen
    visitDelegatingCOnstructorCall
    return $this

def Deprecated_init_$Create$(message, replaceWith, level, $mask0, $marker):
    return Deprecated_init_$Init$(message, replaceWith, level, $mask0, $marker, Object$create())

visitClass
visitClass
visitClass
visitClass
def DeprecationLevel_WARNING_getInstance():
    DeprecationLevel_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@1b71156f

def DeprecationLevel_ERROR_getInstance():
    DeprecationLevel_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@6796ec2b

def DeprecationLevel_HIDDEN_getInstance():
    DeprecationLevel_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@7a29305f

visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@24bd8907

def special($this, specialArg):
    visitSetField

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@439df92e

def special($this, specialArg):
    visitSetField

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@6bd3bb6

visitClass
def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@51e55964

def special($this, specialArg):
    visitSetField

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@145ac215

def special($this, specialArg):
    visitSetField

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@41d8e94

visitClass
def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@4dec9271

def special($this, specialArg):
    visitSetField

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@7d9d4205

def special($this, specialArg):
    visitSetField

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@50b9399a

visitClass
visitClass
visitField
def Companion_getInstance():
    visitWhen
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@1bbaf0d3

visitClass
visitClass
visitField
def Companion_getInstance():
    visitWhen
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@4b0e6ed6

visitClass
visitClass
visitField
def Companion_getInstance():
    visitWhen
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@7377d475

visitClass
visitClass
visitClass
visitField
def Companion_getInstance():
    visitWhen
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@1fa18b63

visitClass
visitClass
visitField
def Companion_getInstance():
    visitWhen
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@78c4bea3

visitClass
visitClass
visitField
def Companion_getInstance():
    visitWhen
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@747348f1

visitClass
visitClass
visitField
def Unit_getInstance():
    visitWhen
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@3f820906

visitClass
visitField
visitField
visitField
visitField
visitField
visitField
visitField
visitField
visitField
visitField
visitField
visitField
visitField
visitField
visitField
def values():
    return arrayLiteral(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrVarargImpl@46c0ad2d)

def valueOf(value):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@41143491

visitField
def AnnotationTarget_initEntries():
    visitWhen
    visitSetField
    visitSetField
    visitSetField
    visitSetField
    visitSetField
    visitSetField
    visitSetField
    visitSetField
    visitSetField
    visitSetField
    visitSetField
    visitSetField
    visitSetField
    visitSetField
    visitSetField
    visitSetField

visitClass
visitClass
def Retention_init_$Init$(value, $mask0, $marker, $this):
    visitWhen
    visitDelegatingCOnstructorCall
    return $this

def Retention_init_$Create$(value, $mask0, $marker):
    return Retention_init_$Init$(value, $mask0, $marker, Object$create())

visitClass
visitField
visitField
visitField
def values():
    return arrayLiteral(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrVarargImpl@32c23506)

def valueOf(value):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@484794d6

visitField
def AnnotationRetention_initEntries():
    visitWhen
    visitSetField
    visitSetField
    visitSetField
    visitSetField

visitClass
visitClass
def AnnotationTarget_CLASS_getInstance():
    AnnotationTarget_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@78fa8bb5

def AnnotationTarget_ANNOTATION_CLASS_getInstance():
    AnnotationTarget_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@82735f2

def AnnotationTarget_TYPE_PARAMETER_getInstance():
    AnnotationTarget_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@64d23a83

def AnnotationTarget_PROPERTY_getInstance():
    AnnotationTarget_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@3205c09a

def AnnotationTarget_FIELD_getInstance():
    AnnotationTarget_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@4f0f76b4

def AnnotationTarget_LOCAL_VARIABLE_getInstance():
    AnnotationTarget_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@674916ae

def AnnotationTarget_VALUE_PARAMETER_getInstance():
    AnnotationTarget_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@5b979374

def AnnotationTarget_CONSTRUCTOR_getInstance():
    AnnotationTarget_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@4787abde

def AnnotationTarget_FUNCTION_getInstance():
    AnnotationTarget_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@147c3b73

def AnnotationTarget_PROPERTY_GETTER_getInstance():
    AnnotationTarget_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@56c1a827

def AnnotationTarget_PROPERTY_SETTER_getInstance():
    AnnotationTarget_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@456c2b84

def AnnotationTarget_TYPE_getInstance():
    AnnotationTarget_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@6cf53627

def AnnotationTarget_EXPRESSION_getInstance():
    AnnotationTarget_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@b6eea98

def AnnotationTarget_FILE_getInstance():
    AnnotationTarget_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@257c7d2d

def AnnotationTarget_TYPEALIAS_getInstance():
    AnnotationTarget_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@6a1a57e4

def AnnotationRetention_SOURCE_getInstance():
    AnnotationRetention_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@78a7114f

def AnnotationRetention_BINARY_getInstance():
    AnnotationRetention_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@619e1cea

def AnnotationRetention_RUNTIME_getInstance():
    AnnotationRetention_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@f3bea57

def getProgressionLastElement(start, end, step):
    tmp
    visitWhen
    return tmp

def getProgressionLastElement(start, end, step):
    tmp
    visitWhen
    return tmp

def differenceModulo(a, b, c):
    return mod(jsBitOr(jsMinus(mod(a, c), mod(b, c)), 0), c)

def differenceModulo(a, b, c):
    return mod(minus(mod(b, c)), c)

def mod(a, b):
    mod = jsMod(a, b)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@1be391f2

def mod(a, b):
    mod = rem(b)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@5eb5556b

visitClass
visitField
def ByteCompanionObject_getInstance():
    visitWhen
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@4f25fe6e

visitClass
visitField
def ShortCompanionObject_getInstance():
    visitWhen
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@13c33a3d

visitClass
visitField
def IntCompanionObject_getInstance():
    visitWhen
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@714245ff

visitClass
visitField
def FloatCompanionObject_getInstance():
    visitWhen
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@15878bb8

visitClass
visitField
def DoubleCompanionObject_getInstance():
    visitWhen
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@61c6450f

visitClass
visitField
def StringCompanionObject_getInstance():
    visitWhen
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@7d372ea8

visitClass
visitField
def BooleanCompanionObject_getInstance():
    visitWhen
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@485f3327

visitClass
visitClass
def toTypedArray():
    return copyToArray((special))

def copyToArray(collection):
    tmp
    visitWhen
    return tmp

def copyToArrayImpl(collection):
    array = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@485b21ec
    iterator = iterator()
    while hasNext():
        visitExpression
    
    return array

def copyToArrayImpl(collection, array):
    visitWhen
    iterator = iterator()
    index = 0
    while hasNext():
        tmp0 = index
        index = jsBitOr(jsPlus(tmp0, 1), 0)
        tmp1_unsafeCast_0 = next()
        jsArraySet(array, tmp0, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@481c2454)
    
    visitWhen
    return array

visitClass
visitClass
visitClass
def <no name provided>$factory($elements):
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@43885360
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@45a8b90f

def <no name provided>$factory($elements):
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@50abbf54
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@6b787bd5

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@59065952

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@605bfc81

def special($this, specialArg):
    visitSetField

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@43ae3c30

visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
def <no name provided>$factory($elements):
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@3ac2300f
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@c27ea94

def <no name provided>$factory($elements):
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@f62fe59
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@36058c6b

def special($this, specialArg):
    visitSetField

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@7a668497

def special($this, specialArg):
    visitSetField

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@2650754f

def ArrayList_init_$Init$($this):
    visitDelegatingCOnstructorCall
    return $this

def ArrayList_init_$Create$():
    return ArrayList_init_$Init$(Object$create())

def ArrayList_init_$Init$(initialCapacity, $this):
    visitDelegatingCOnstructorCall
    return $this

def ArrayList_init_$Create$(initialCapacity):
    return ArrayList_init_$Init$(initialCapacity, Object$create())

def ArrayList_init_$Init$(initialCapacity, $mask0, $marker, $this):
    visitWhen
    ArrayList_init_$Init$(initialCapacity, $this)
    return $this

def ArrayList_init_$Create$(initialCapacity, $mask0, $marker):
    return ArrayList_init_$Init$(initialCapacity, $mask0, $marker, Object$create())

def ArrayList_init_$Init$(elements, $this):
    visitDelegatingCOnstructorCall
    return $this

def ArrayList_init_$Create$(elements):
    return ArrayList_init_$Init$(elements, Object$create())

def rangeCheck($this, index):
    checkElementIndex(index, (special)())
    return index

def insertionRangeCheck($this, index):
    checkPositionIndex(index, (special)())
    return index

visitClass
def special(specialArg):
    visitSetField

def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@6ecf239d

visitField
visitClass
def special(specialArg):
    visitSetField

def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@25e9f5e6

visitField
visitClass
visitClass
visitClass
def String(value):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@5d1915d1

visitClass
def println(message):
    println(message)

def output$init$():
    isNode_2 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@4717bdb3
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@4fda9835

def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@78652c15

visitField
visitClass
def EmptyContinuation$init$():
    tmp0_Continuation_0 = EmptyCoroutineContext_getInstance()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@7fcc9949

def asDynamic():
    return (special)

def unsafeCast():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@61b6e8c1

def unsafeCast():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@2efe360c

visitClass
def pow(n):
    return pow((special), visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@6af5b172)

def isNaN():
    return jsNot(jsEqeqeq((special), (special)))

def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@5e888fba

visitField
def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@4a2891d1

visitField
def INV_2_26$init$():
    tmp0_pow_0 = visitConst-other
    tmp1_pow_0 = -26
    return pow(tmp0_pow_0, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@3999ea91)

def INV_2_53$init$():
    tmp0_pow_0 = visitConst-other
    tmp1_pow_0 = -53
    return pow(tmp0_pow_0, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@72fdb79d)

def special():
    return (special)()

visitClass
visitClass
visitClass
def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@601122cd

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@5c64026c

visitClass
visitClass
visitField
def NothingKClassImpl_getInstance():
    visitWhen
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@2948e596

visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
def createKType(classifier, arguments, isMarkedNullable):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@2c1ffb9

def createDynamicKType():
    return DynamicKType_getInstance()

def createKTypeParameter(name, upperBounds, variance):
    tmp0_subject = variance
    kVariance = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@69a3c55b
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@705e24fb

def getStarKTypeProjection():
    return (special)()

def createCovariantKTypeProjection(type):
    return covariant(type)

def createInvariantKTypeProjection(type):
    return invariant(type)

def createContravariantKTypeProjection(type):
    return contravariant(type)

def asString($this):
    visitWhen
    return jsPlus(prefixString(), toString())

visitClass
visitClass
def prefixString():
    tmp0_subject = (special)
    tmp
    visitWhen
    return tmp

visitClass
visitField
def DynamicKType_getInstance():
    visitWhen
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@34eff199

def <no name provided>$factory(this$0):
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@e0957b5
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@1024b871

visitClass
def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@a6f34f5

visitField
visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
visitField
def PrimitiveClasses_getInstance():
    visitWhen
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@449c3c94

def <no name provided>$factory():
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@392b7436
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@3f88558d

def <no name provided>$factory():
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4fddc3cb
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@65bb0f13

def <no name provided>$factory():
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4656c63a
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@33de2803

def <no name provided>$factory():
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@1a4cfae4
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@7e4e6bdf

def <no name provided>$factory():
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4049837d
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@918ca32

def <no name provided>$factory():
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@3ac18a9e
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@486b9a36

def <no name provided>$factory():
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@455cd186
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@18626c8c

def <no name provided>$factory():
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@1062338c
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@4d40fe37

def <no name provided>$factory():
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5abe46b7
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@66a81c48

def <no name provided>$factory():
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4130052
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@1d1cfdac

def <no name provided>$factory():
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@7c6f306b
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@7876caae

def <no name provided>$factory():
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@35611d52
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@17c8dbae

def <no name provided>$factory():
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@45147221
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@52386242

def <no name provided>$factory():
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@43ec687e
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@30a9a7f3

def <no name provided>$factory():
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@76140476
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@3bd3cdc8

def <no name provided>$factory():
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@354dbfa3
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@493658fa

def <no name provided>$factory():
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@6f1fd7c1
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@7b742ec1

def <no name provided>$factory():
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4beab10
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@37265333

def <no name provided>$factory():
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5a8d411f
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@5d5181f2

def <no name provided>$factory($arity):
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@1561e62e
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@2e897323

def functionClasses$init$():
    tmp0_arrayOfNulls_0 = 0
    return fillArrayVal(Array(tmp0_arrayOfNulls_0), visitConst-other)

def getKClass(jClass):
    tmp
    visitWhen
    return tmp

def getKClassM(jClasses):
    tmp0_subject = jsArrayLength(jClasses)
    tmp
    visitWhen
    return tmp

def getKClass1(jClass):
    visitWhen
    metadata = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicMemberExpressionImpl@62a9e9bf
    tmp
    visitWhen
    return tmp

def getKClassFromExpression(e):
    tmp0_subject = jsTypeOf(e)
    tmp
    visitWhen
    tmp1_unsafeCast_0 = tmp
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@7bc0ff69

visitClass
def StringBuilder_init_$Init$(capacity, $this):
    StringBuilder_init_$Init$($this)
    return $this

def StringBuilder_init_$Create$(capacity):
    return StringBuilder_init_$Init$(capacity, Object$create())

def StringBuilder_init_$Init$(content, $this):
    visitDelegatingCOnstructorCall
    return $this

def StringBuilder_init_$Create$(content):
    return StringBuilder_init_$Init$(content, Object$create())

def StringBuilder_init_$Init$($this):
    visitDelegatingCOnstructorCall
    return $this

def StringBuilder_init_$Create$():
    return StringBuilder_init_$Init$(Object$create())

def special($this, specialArg):
    visitSetField

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@6b34e798

def checkReplaceRange($this, startIndex, endIndex, length):
    visitWhen
    visitWhen

visitClass
def isLowSurrogate():
    containsLower = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5f1f59e3
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@5aba40f

def isHighSurrogate():
    containsLower = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@3c98e574
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@51c8a421

def checkRadix(radix):
    visitWhen
    return radix

def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@2ae25358

visitField
def nativeLastIndexOf(str, fromIndex):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@6786a21d

def substring(startIndex, endIndex):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@15a4e7d8

def substring(startIndex):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@2b21842a

def compareTo(other, ignoreCase):
    visitWhen

def compareTo$default(other, ignoreCase, $mask0, $handler):
    visitWhen
    return compareTo(other, ignoreCase)

def toUpperCase():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@3f3a9fc4

def toLowerCase():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@3e0032f

def concatToString():
    result = ''
    indexedObject = (special)
    inductionVariable = 0
    last = jsArrayLength(indexedObject)
    while jsLt(inductionVariable, last):
        char = jsArrayGet(indexedObject, inductionVariable)
        inductionVariable = jsBitOr(jsPlus(inductionVariable, 1), 0)
        result = jsPlus(result, char)
    
    return result

def concatToString(startIndex, endIndex):
    checkBoundsIndexes(startIndex, endIndex, jsArrayLength((special)))
    result = ''
    inductionVariable = startIndex
    visitWhen
    return result

def concatToString$default(startIndex, endIndex, $mask0, $handler):
    visitWhen
    visitWhen
    return concatToString(startIndex, endIndex)

visitClass
visitClass
def <no name provided>$factory():
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@7c540787
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@54310ed3

def STRING_CASE_INSENSITIVE_ORDER$init$():
    tmp = <no name provided>$factory()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@76a34504

def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@6682e9b0

visitField
def REPLACEMENT_BYTE_SEQUENCE$init$():
    tmp0_byteArrayOf_0 = int8ArrayOf(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrVarargImpl@59fd35ad)
    return tmp0_byteArrayOf_0

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@3de0d61c

visitClass
visitField
def Companion_getInstance():
    visitWhen
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@7b37fcee

visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
visitField
def Companion_getInstance():
    visitWhen
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@259c2915

visitClass
def byteArrayOf(elements):
    return elements

def arrayOf(elements):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@34e8256b

def plus(other):
    tmp2_safe_receiver = (special)
    tmp3_elvis_lhs = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@7270c811
    tmp = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@30c6f027
    tmp0_safe_receiver = other
    tmp1_elvis_lhs = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@43264e4a
    return jsPlus(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@386b28b)

def toString():
    tmp0_safe_receiver = (special)
    tmp1_elvis_lhs = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@ca0ccb6
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@213229a5

def booleanArrayOf(elements):
    return elements

def charArrayOf(elements):
    return elements

def shortArrayOf(elements):
    return elements

def intArrayOf(elements):
    return elements

def floatArrayOf(elements):
    return elements

def longArrayOf(elements):
    return elements

def doubleArrayOf(elements):
    return elements

visitClass
visitField
def DefaultConstructorMarker_getInstance():
    visitWhen
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@1dbd1049

def fillArrayVal(array, initValue):
    inductionVariable = 0
    last = jsBitOr(jsMinus(jsArrayLength(array), 1), 0)
    visitWhen
    return array

def arrayWithFun(size, init):
    tmp0_fillArrayFun_0 = Array(size)
    result_1 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@2d5bfc3a
    i_2 = 0
    while jsNot(jsEqeqeq(i_2, jsArrayLength(result_1))):
        jsArraySet(result_1, i_2, invoke(i_2))
        i_2 = jsBitOr(jsPlus(i_2, 1), 0)
        Unit_getInstance()
    
    return result_1

def fillArrayFun(array, init):
    result = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@22249b41
    i = 0
    while jsNot(jsEqeqeq(i, jsArrayLength(result))):
        jsArraySet(result, i, invoke(i))
        i = jsBitOr(jsPlus(i, 1), 0)
        Unit_getInstance()
    
    return result

def arrayIterator(array):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@26b01fae

def booleanArrayIterator(array):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@37107ea0

def charArrayIterator(array):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@55b2cdcb

def byteArrayIterator(array):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@2899f9e9

def shortArrayIterator(array):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@305c8bf

def intArrayIterator(array):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@75a45239

def floatArrayIterator(array):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@2fdece0e

def longArrayIterator(array):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@573a43f4

def doubleArrayIterator(array):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5bf17128

def booleanArray(size):
    tmp0_withType_0 = 'BooleanArray'
    tmp1_withType_0 = fillArrayVal(Array(size), visitConst-other)
    visitExpression
    tmp2_unsafeCast_0 = tmp1_withType_0
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@1ebc4539

def charArray(size):
    tmp0_withType_0 = 'CharArray'
    tmp1_withType_0 = fillArrayVal(Array(size), visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5655d64)
    visitExpression
    tmp2_unsafeCast_0 = tmp1_withType_0
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@314ba270

def longArray(size):
    tmp0_withType_0 = 'LongArray'
    tmp1_withType_0 = fillArrayVal(Array(size), visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@48df2306)
    visitExpression
    tmp2_unsafeCast_0 = tmp1_withType_0
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@67040b58

def booleanArrayOf(arr):
    tmp0_withType_0 = 'BooleanArray'
    tmp1_withType_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@793937ec
    visitExpression
    tmp2_unsafeCast_0 = tmp1_withType_0
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@56c8c77e

def charArrayOf(arr):
    tmp0_withType_0 = 'CharArray'
    tmp1_withType_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@79499fa
    visitExpression
    tmp2_unsafeCast_0 = tmp1_withType_0
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@42e62465

def longArrayOf(arr):
    tmp0_withType_0 = 'LongArray'
    tmp1_withType_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@350a3df3
    visitExpression
    tmp2_unsafeCast_0 = tmp1_withType_0
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@43e97462

visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
visitClass
def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@4e43a23a

visitField
def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@43b45e77

visitField
def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@69c27acb

visitField
def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@77d5395a

visitField
def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@4e1fd34b

visitField
def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@6c8a806c

visitField
def getNumberHashCode(obj):
    tmp0_unsafeCast_0 = jsBitwiseOr(obj, 0)
    visitWhen
    jsArraySet(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@311ce8c0, 0, obj)
    return jsBitOr(jsPlus(imul(jsArrayGet(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@22360505, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@d0e05e8), 31), jsArrayGet(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@3ec40a18, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@2cc83ee8)), 0)

def bufFloat64$init$():
    tmp0_unsafeCast_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@31b846f
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@3a8d30e

def bufFloat32$init$():
    tmp0_unsafeCast_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@1cb3de26
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@291853ab

def bufInt32$init$():
    tmp0_unsafeCast_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@38dde7ec
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@7cc87859

def lowIndex$init$():
    jsArraySet(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@4b09f5f2, 0, visitConst-other)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@6fd2bc3a

visitClass
def charSequenceGet(a, index):
    tmp
    visitWhen
    return tmp

def isString(a):
    return jsEqeqeq(jsTypeOf(a), 'string')

def charSequenceLength(a):
    tmp
    visitWhen
    return tmp

def charSequenceSubSequence(a, startIndex, endIndex):
    tmp
    visitWhen
    return tmp

def arrayToString(array):
    return joinToString$default(', ', '[', ']', 0, visitConst-other, <no name provided>$factory(), 24, visitConst-other)

visitClass
def <no name provided>$factory():
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@63cbd058
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@494cd08e

def compareTo(a, b):
    tmp0_subject = jsTypeOf(a)
    tmp
    visitWhen
    return tmp

def doubleCompareTo(a, b):
    tmp
    visitWhen
    return tmp

def primitiveCompareTo(a, b):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@54543feb

def compareToDoNotIntrinsicify(a, b):
    return compareTo(b)

def construct(constructorType, resultType, args):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@6c78bb9a

def identityHashCode(obj):
    return getObjectHashCode(obj)

def getObjectHashCode(obj):
    visitWhen
    tmp0_unsafeCast_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@cea6297
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@196fe9d2

def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@262e2c8c

visitField
def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@3094111c

visitField
def hashCode(obj):
    visitWhen
    tmp0_subject = jsTypeOf(obj)
    tmp
    visitWhen
    return tmp

def getStringHashCode(str):
    hash = 0
    length = jsArrayLength(str)
    inductionVariable = 0
    last = jsBitOr(jsMinus(length, 1), 0)
    visitWhen
    return hash

def toString(o):
    tmp
    visitWhen
    return tmp

def anyToString(o):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@22e7dfeb

def equals(obj1, obj2):
    visitWhen
    visitWhen
    visitWhen
    visitWhen
    visitWhen
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@3b07b706

def boxIntrinsic(x):
    tmp0_error_0 = 'Should be lowered'
    visitThrow

def unboxIntrinsic(x):
    tmp0_error_0 = 'Should be lowered'
    visitThrow

def captureStack(instance, constructorFunction):
    visitWhen

def newThrowable(message, cause):
    throwable = js('new Error()')
    tmp
    visitWhen
    visitExpression
    visitExpression
    visitExpression
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@1c2f4713

def isUndefined(value):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@aecfc07

def extendThrowable(this_, message, cause):
    visitExpression
    setPropertiesToThrowableInstance(this_, message, cause)

def setPropertiesToThrowableInstance(this_, message, cause):
    visitWhen
    visitWhen
    visitExpression

def hasOwnPrototypeProperty(o, name):
    tmp0_unsafeCast_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@1fb947f6
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@401b14ac

def getContinuation():
    visitThrow

def returnIfSuspended(argument):
    visitThrow

def suspendCoroutineUninterceptedOrReturnJS(block):
    return invoke(getContinuation())

def getCoroutineContext():
    return (special)()

def ensureNotNull(v):
    tmp
    visitWhen
    return tmp

def THROW_NPE():
    visitThrow

def noWhenBranchMatchedException():
    visitThrow

def THROW_CCE():
    visitThrow

def throwUninitializedPropertyAccessException(name):
    visitThrow

def throwKotlinNothingValueException():
    visitThrow

def THROW_ISE():
    visitThrow

def THROW_IAE(msg):
    visitThrow

def emptyArray():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@2ec173e5

def enumValueOfIntrinsic(name):
    visitThrow

def enumValuesIntrinsic():
    visitThrow

visitClass
visitField
def Companion_getInstance():
    visitWhen
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@4c1b3e17

visitClass
def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@61b83fef

visitField
def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@52baaf87

visitField
def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@63eebb56

visitField
def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@4aed4ff

visitField
def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@14a3d15b

visitField
def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@17125ea9

visitField
def compare(other):
    visitWhen
    thisNeg = isNegative()
    otherNeg = isNegative()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@7b00f659

def add(other):
    a48 = jsBitShiftRU(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@5e397a71, 16)
    a32 = jsBitAnd(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@14c215d4, 65535)
    a16 = jsBitShiftRU(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@53f0d946, 16)
    a00 = jsBitAnd(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@4f02391b, 65535)
    b48 = jsBitShiftRU(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@2212c346, 16)
    b32 = jsBitAnd(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@6038186d, 65535)
    b16 = jsBitShiftRU(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@4b965312, 16)
    b00 = jsBitAnd(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@341c7913, 65535)
    c48 = 0
    c32 = 0
    c16 = 0
    c00 = 0
    c00 = jsBitOr(jsPlus(c00, jsBitOr(jsPlus(a00, b00), 0)), 0)
    c16 = jsBitOr(jsPlus(c16, jsBitShiftRU(c00, 16)), 0)
    c00 = jsBitAnd(c00, 65535)
    c16 = jsBitOr(jsPlus(c16, jsBitOr(jsPlus(a16, b16), 0)), 0)
    c32 = jsBitOr(jsPlus(c32, jsBitShiftRU(c16, 16)), 0)
    c16 = jsBitAnd(c16, 65535)
    c32 = jsBitOr(jsPlus(c32, jsBitOr(jsPlus(a32, b32), 0)), 0)
    c48 = jsBitOr(jsPlus(c48, jsBitShiftRU(c32, 16)), 0)
    c32 = jsBitAnd(c32, 65535)
    c48 = jsBitOr(jsPlus(c48, jsBitOr(jsPlus(a48, b48), 0)), 0)
    c48 = jsBitAnd(c48, 65535)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4a244aa3

def subtract(other):
    return add(unaryMinus())

def multiply(other):
    visitWhen
    visitWhen
    visitWhen
    visitWhen
    a48 = jsBitShiftRU(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@65463b83, 16)
    a32 = jsBitAnd(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@26154a00, 65535)
    a16 = jsBitShiftRU(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@30559e92, 16)
    a00 = jsBitAnd(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@505806c8, 65535)
    b48 = jsBitShiftRU(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@719edb69, 16)
    b32 = jsBitAnd(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@35356aef, 65535)
    b16 = jsBitShiftRU(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@4468aa66, 16)
    b00 = jsBitAnd(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@2596ae35, 65535)
    c48 = 0
    c32 = 0
    c16 = 0
    c00 = 0
    c00 = jsBitOr(jsPlus(c00, imul(a00, b00)), 0)
    c16 = jsBitOr(jsPlus(c16, jsBitShiftRU(c00, 16)), 0)
    c00 = jsBitAnd(c00, 65535)
    c16 = jsBitOr(jsPlus(c16, imul(a16, b00)), 0)
    c32 = jsBitOr(jsPlus(c32, jsBitShiftRU(c16, 16)), 0)
    c16 = jsBitAnd(c16, 65535)
    c16 = jsBitOr(jsPlus(c16, imul(a00, b16)), 0)
    c32 = jsBitOr(jsPlus(c32, jsBitShiftRU(c16, 16)), 0)
    c16 = jsBitAnd(c16, 65535)
    c32 = jsBitOr(jsPlus(c32, imul(a32, b00)), 0)
    c48 = jsBitOr(jsPlus(c48, jsBitShiftRU(c32, 16)), 0)
    c32 = jsBitAnd(c32, 65535)
    c32 = jsBitOr(jsPlus(c32, imul(a16, b16)), 0)
    c48 = jsBitOr(jsPlus(c48, jsBitShiftRU(c32, 16)), 0)
    c32 = jsBitAnd(c32, 65535)
    c32 = jsBitOr(jsPlus(c32, imul(a00, b32)), 0)
    c48 = jsBitOr(jsPlus(c48, jsBitShiftRU(c32, 16)), 0)
    c32 = jsBitAnd(c32, 65535)
    c48 = jsBitOr(jsPlus(c48, jsBitOr(jsPlus(jsBitOr(jsPlus(jsBitOr(jsPlus(imul(a48, b00), imul(a32, b16)), 0), imul(a16, b32)), 0), imul(a00, b48)), 0)), 0)
    c48 = jsBitAnd(c48, 65535)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@bcecdd

def divide(other):
    visitWhen
    visitWhen
    visitWhen
    res = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@4d7ddc1b
    rem = (special)
    while greaterThanOrEqual(other):
        approxDouble = jsDiv(toNumber(), toNumber())
        approx2 = max(visitConst-other, floor(approxDouble))
        log2 = ceil(jsDiv(log(approx2), (special)()))
        delta = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@63f410d0
        approxRes = fromNumber(approx2)
        approxRem = multiply(other)
        while visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@2d6e48c6:
            approx2 = jsMinus(approx2, delta)
            approxRes = fromNumber(approx2)
            approxRem = multiply(other)
        
        visitWhen
        res = add(approxRes)
        rem = subtract(approxRem)
    
    return res

def modulo(other):
    return subtract(multiply(other))

def shiftLeft(numBits):
    numBits = jsBitAnd(numBits, 63)
    visitWhen

def shiftRight(numBits):
    numBits = jsBitAnd(numBits, 63)
    visitWhen

def shiftRightUnsigned(numBits):
    numBits = jsBitAnd(numBits, 63)
    visitWhen

def toNumber():
    return jsPlus(jsMult(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@56c4bb46, visitConst-other), getLowBitsUnsigned())

def equalsLong(other):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@3d8b888f

def hashCode(l):
    return jsBitXor(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@486765f1, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@73b3dfe9)

def toStringImpl(radix):
    visitWhen
    visitWhen
    visitWhen
    radixToPower = fromNumber(pow(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@1c4f7807, visitConst-other))
    rem = (special)
    result = ''
    while visitConst-other:
        remDiv = div(radixToPower)
        intval = toInt()
        tmp1_unsafeCast_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@29701f1f
        digits = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@430c9347
        rem = remDiv
        visitWhen
    

def fromInt(value):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@46b4cddb

def isNegative():
    return jsLt(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@1816701b, 0)

def isZero():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@2a3d8a59

def isOdd():
    return jsEqeqeq(jsBitAnd(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@484ab2dc, 1), 1)

def negate():
    return unaryMinus()

def lessThan(other):
    return jsLt(compare(other), 0)

def fromNumber(value):
    visitWhen

def greaterThan(other):
    return jsGt(compare(other), 0)

def greaterThanOrEqual(other):
    return jsGtEq(compare(other), 0)

def getLowBitsUnsigned():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@1ee7aa6

def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@5dca1c50

visitField
def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@495fa126

visitField
def imul(a_local, b_local):
    lhs = jsMult(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@354ec60, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@504e23e7)
    rhs = jsMult(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@397ec6bb, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@1d6d1a18)
    return jsBitwiseOr(jsPlus(lhs, rhs), 0)

def withType(type, array):
    visitExpression
    return array

def arrayConcat(args):
    len = jsArrayLength(args)
    tmp0_unsafeCast_0 = js('Array(len)')
    typed = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@4f251b32
    inductionVariable = 0
    last = jsBitOr(jsMinus(len, 1), 0)
    visitWhen
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@ae11512

def primitiveArrayConcat(args):
    size_local = 0
    inductionVariable = 0
    last = jsBitOr(jsMinus(jsArrayLength(args), 1), 0)
    visitWhen
    a = jsArrayGet(args, 0)
    tmp1_unsafeCast_0 = js('new a.constructor(size_local)')
    result = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@9e03c6e
    visitWhen
    size_local = 0
    inductionVariable = 0
    last = jsBitOr(jsMinus(jsArrayLength(args), 1), 0)
    visitWhen
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@6c25b3ad

def taggedArrayCopy(array):
    res = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@112ec8a7
    visitExpression
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@1916147d

def numberToByte(a):
    return toByte(numberToInt(a))

def toByte(a):
    tmp0_unsafeCast_0 = js('a << 24 >> 24')
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@f38abd

def numberToInt(a):
    tmp
    visitWhen
    return tmp

def doubleToInt(a):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@4054397

def numberToDouble(a):
    tmp0_unsafeCast_0 = js('+a')
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@254b8be3

def numberToShort(a):
    return toShort(numberToInt(a))

def toShort(a):
    tmp0_unsafeCast_0 = js('a << 16 >> 16')
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@5cfd84e9

def numberToLong(a):
    tmp
    visitWhen
    return tmp

def numberToChar(a):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@59f4df4e

def toLong(a):
    return fromInt(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@5157d57c)

def numberRangeToNumber(start, endInclusive):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5ae6a240

def numberRangeToLong(start, endInclusive):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@3d2162c5

def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@4916619e

visitField
def metadataObject():
    return js('{ kind: 'class', interfaces: [] }')

def getPropertyCallableRef(name, paramCount, type, getter, setter):
    visitExpression
    visitExpression
    visitExpression
    tmp0_unsafeCast_0 = getPropertyRefClass(getter, getKPropMetadata(paramCount, setter, type))
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@312e3de0

def getPropertyRefClass(obj, metadata):
    visitExpression
    visitExpression
    return obj

def getKPropMetadata(paramCount, setter, type):
    mdata = jsArrayGet(jsArrayGet(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@6657c199, paramCount), visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@34f8cee0)
    visitWhen
    return mdata

def getLocalDelegateReference(name, type, mutable, lambda):
    return getPropertyCallableRef(name, 0, type, lambda, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@5d52508e)

def propertyRefClassMetadataCache$init$():
    tmp = js('{ kind: 'class', interfaces: [] }')
    tmp0_arrayOf_0 = arrayLiteral(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrVarargImpl@3ca2be5f)
    tmp = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@7c6edbd2
    tmp = js('{ kind: 'class', interfaces: [] }')
    tmp1_arrayOf_0 = arrayLiteral(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrVarargImpl@460d7e4a)
    tmp = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@21baa851
    tmp = js('{ kind: 'class', interfaces: [] }')
    tmp2_arrayOf_0 = arrayLiteral(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrVarargImpl@5071a1c5)
    tmp3_arrayOf_0 = arrayLiteral(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrVarargImpl@5a0ec14d)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@5145512c

def isInterface(obj, iface):
    tmp0_elvis_lhs = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicMemberExpressionImpl@31ebc5fa
    tmp
    visitWhen
    ctor = tmp
    return isInterfaceImpl(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@326c6ac1, iface)

def isInterfaceImpl(ctor, iface):
    visitWhen
    metadata = (special)()
    visitWhen
    superPrototype = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@6acc72c7
    superConstructor = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@3f29d13d
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@1ed5ba35

def isArray(obj):
    tmp
    visitWhen
    return tmp

def isJsArray(obj):
    tmp0_unsafeCast_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@124bc9fa
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@7a7303d8

def isObject(obj):
    objTypeOf = jsTypeOf(obj)
    tmp0_subject = objTypeOf
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@7bfca354

def isSuspendFunction(obj, arity):
    visitWhen
    return visitConst-other

def isNumber(a):
    tmp
    visitWhen
    return tmp

def isComparable(value):
    type = jsTypeOf(value)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@686ae84f

def isCharSequence(value):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@5c99d7ad

def isBooleanArray(a):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@dbc9d8d

def isByteArray(a):
    return jsInstanceOf(a, js('Int8Array'))

def isShortArray(a):
    return jsInstanceOf(a, js('Int16Array'))

def isCharArray(a):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@738db631

def isIntArray(a):
    return jsInstanceOf(a, js('Int32Array'))

def isFloatArray(a):
    return jsInstanceOf(a, js('Float32Array'))

def isLongArray(a):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@60c9f01

def isDoubleArray(a):
    return jsInstanceOf(a, js('Float64Array'))

def isArrayish(o):
    tmp
    visitWhen
    return tmp

def jsIsType(obj, jsClass):
    visitWhen
    visitWhen
    visitWhen
    proto = jsGetPrototypeOf(jsClass)
    tmp0_safe_receiver = proto
    constructor = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@24d4a409
    visitWhen
    klassMetadata = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicMemberExpressionImpl@7c2b2b56
    visitWhen
    visitWhen
    return visitConst-other

def jsGetPrototypeOf(jsClass):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@f542e08

def asList():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@7f14bdd1

def plus(elements):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@7ca5250b

def copyOfRange(fromIndex, toIndex):
    checkRangeIndexes(fromIndex, toIndex, jsArrayLength((special)))
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@5c33a1b3

def minOf(a, b):
    return min(int32ArrayOf(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrVarargImpl@2281ede7))

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@5adba350

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@1df41490

def special($this, specialArg):
    visitSetField

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@480f6625

def releaseIntercepted($this):
    intercepted = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@422a2263
    visitWhen
    visitSetField

visitClass
visitClass
visitField
def CompletedContinuation_getInstance():
    visitWhen
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@42f16e74

def Exception_init_$Init$($this):
    extendThrowable($this, $undefined(), $undefined())
    visitDelegatingCOnstructorCall
    return $this

def Exception_init_$Create$():
    tmp = Exception_init_$Init$(Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@2b95004a)
    return tmp

def Exception_init_$Init$(message, $this):
    extendThrowable($this, message, $undefined())
    visitDelegatingCOnstructorCall
    return $this

def Exception_init_$Create$(message):
    tmp = Exception_init_$Init$(message, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@f400c86)
    return tmp

def Exception_init_$Init$(message, cause, $this):
    extendThrowable($this, message, cause)
    visitDelegatingCOnstructorCall
    return $this

def Exception_init_$Create$(message, cause):
    tmp = Exception_init_$Init$(message, cause, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@582e8393)
    return tmp

def Exception_init_$Init$(cause, $this):
    extendThrowable($this, $undefined(), cause)
    visitDelegatingCOnstructorCall
    return $this

def Exception_init_$Create$(cause):
    tmp = Exception_init_$Init$(cause, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@7b07ef24)
    return tmp

visitClass
def Error_init_$Init$($this):
    extendThrowable($this, $undefined(), $undefined())
    visitDelegatingCOnstructorCall
    return $this

def Error_init_$Create$():
    tmp = Error_init_$Init$(Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@6b629dff)
    return tmp

def Error_init_$Init$(message, $this):
    extendThrowable($this, message, $undefined())
    visitDelegatingCOnstructorCall
    return $this

def Error_init_$Create$(message):
    tmp = Error_init_$Init$(message, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@3a3bd68c)
    return tmp

def Error_init_$Init$(message, cause, $this):
    extendThrowable($this, message, cause)
    visitDelegatingCOnstructorCall
    return $this

def Error_init_$Create$(message, cause):
    tmp = Error_init_$Init$(message, cause, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@32fd55a6)
    return tmp

def Error_init_$Init$(cause, $this):
    extendThrowable($this, $undefined(), cause)
    visitDelegatingCOnstructorCall
    return $this

def Error_init_$Create$(cause):
    tmp = Error_init_$Init$(cause, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@5c5eec57)
    return tmp

visitClass
def IllegalArgumentException_init_$Init$($this):
    RuntimeException_init_$Init$($this)
    visitDelegatingCOnstructorCall
    return $this

def IllegalArgumentException_init_$Create$():
    tmp = IllegalArgumentException_init_$Init$(Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@56b56566)
    return tmp

def IllegalArgumentException_init_$Init$(message, $this):
    RuntimeException_init_$Init$(message, $this)
    visitDelegatingCOnstructorCall
    return $this

def IllegalArgumentException_init_$Create$(message):
    tmp = IllegalArgumentException_init_$Init$(message, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@7ce9ec07)
    return tmp

def IllegalArgumentException_init_$Init$(message, cause, $this):
    RuntimeException_init_$Init$(message, cause, $this)
    visitDelegatingCOnstructorCall
    return $this

def IllegalArgumentException_init_$Create$(message, cause):
    tmp = IllegalArgumentException_init_$Init$(message, cause, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@17020207)
    return tmp

def IllegalArgumentException_init_$Init$(cause, $this):
    RuntimeException_init_$Init$(cause, $this)
    visitDelegatingCOnstructorCall
    return $this

def IllegalArgumentException_init_$Create$(cause):
    tmp = IllegalArgumentException_init_$Init$(cause, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@4762b2c0)
    return tmp

visitClass
def RuntimeException_init_$Init$($this):
    Exception_init_$Init$($this)
    visitDelegatingCOnstructorCall
    return $this

def RuntimeException_init_$Create$():
    tmp = RuntimeException_init_$Init$(Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@4813b3d1)
    return tmp

def RuntimeException_init_$Init$(message, $this):
    Exception_init_$Init$(message, $this)
    visitDelegatingCOnstructorCall
    return $this

def RuntimeException_init_$Create$(message):
    tmp = RuntimeException_init_$Init$(message, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@6bbf9cb2)
    return tmp

def RuntimeException_init_$Init$(message, cause, $this):
    Exception_init_$Init$(message, cause, $this)
    visitDelegatingCOnstructorCall
    return $this

def RuntimeException_init_$Create$(message, cause):
    tmp = RuntimeException_init_$Init$(message, cause, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@3f1ab9ce)
    return tmp

def RuntimeException_init_$Init$(cause, $this):
    Exception_init_$Init$(cause, $this)
    visitDelegatingCOnstructorCall
    return $this

def RuntimeException_init_$Create$(cause):
    tmp = RuntimeException_init_$Init$(cause, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@5030dfb8)
    return tmp

visitClass
def NoSuchElementException_init_$Init$($this):
    RuntimeException_init_$Init$($this)
    visitDelegatingCOnstructorCall
    return $this

def NoSuchElementException_init_$Create$():
    tmp = NoSuchElementException_init_$Init$(Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@78626f16)
    return tmp

def NoSuchElementException_init_$Init$(message, $this):
    RuntimeException_init_$Init$(message, $this)
    visitDelegatingCOnstructorCall
    return $this

def NoSuchElementException_init_$Create$(message):
    tmp = NoSuchElementException_init_$Init$(message, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@2f1661e6)
    return tmp

visitClass
def IllegalStateException_init_$Init$($this):
    RuntimeException_init_$Init$($this)
    visitDelegatingCOnstructorCall
    return $this

def IllegalStateException_init_$Create$():
    tmp = IllegalStateException_init_$Init$(Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@76fee3de)
    return tmp

def IllegalStateException_init_$Init$(message, $this):
    RuntimeException_init_$Init$(message, $this)
    visitDelegatingCOnstructorCall
    return $this

def IllegalStateException_init_$Create$(message):
    tmp = IllegalStateException_init_$Init$(message, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@5a209683)
    return tmp

def IllegalStateException_init_$Init$(message, cause, $this):
    RuntimeException_init_$Init$(message, cause, $this)
    visitDelegatingCOnstructorCall
    return $this

def IllegalStateException_init_$Create$(message, cause):
    tmp = IllegalStateException_init_$Init$(message, cause, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@bd3df07)
    return tmp

def IllegalStateException_init_$Init$(cause, $this):
    RuntimeException_init_$Init$(cause, $this)
    visitDelegatingCOnstructorCall
    return $this

def IllegalStateException_init_$Create$(cause):
    tmp = IllegalStateException_init_$Init$(cause, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@362c8889)
    return tmp

visitClass
def UnsupportedOperationException_init_$Init$($this):
    RuntimeException_init_$Init$($this)
    visitDelegatingCOnstructorCall
    return $this

def UnsupportedOperationException_init_$Create$():
    tmp = UnsupportedOperationException_init_$Init$(Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@3fbaeea7)
    return tmp

def UnsupportedOperationException_init_$Init$(message, $this):
    RuntimeException_init_$Init$(message, $this)
    visitDelegatingCOnstructorCall
    return $this

def UnsupportedOperationException_init_$Create$(message):
    tmp = UnsupportedOperationException_init_$Init$(message, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@5ba540a5)
    return tmp

def UnsupportedOperationException_init_$Init$(message, cause, $this):
    RuntimeException_init_$Init$(message, cause, $this)
    visitDelegatingCOnstructorCall
    return $this

def UnsupportedOperationException_init_$Create$(message, cause):
    tmp = UnsupportedOperationException_init_$Init$(message, cause, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@aa2ae2d)
    return tmp

def UnsupportedOperationException_init_$Init$(cause, $this):
    RuntimeException_init_$Init$(cause, $this)
    visitDelegatingCOnstructorCall
    return $this

def UnsupportedOperationException_init_$Create$(cause):
    tmp = UnsupportedOperationException_init_$Init$(cause, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@638c5472)
    return tmp

visitClass
def NullPointerException_init_$Init$($this):
    RuntimeException_init_$Init$($this)
    visitDelegatingCOnstructorCall
    return $this

def NullPointerException_init_$Create$():
    tmp = NullPointerException_init_$Init$(Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@3c874f23)
    return tmp

def NullPointerException_init_$Init$(message, $this):
    RuntimeException_init_$Init$(message, $this)
    visitDelegatingCOnstructorCall
    return $this

def NullPointerException_init_$Create$(message):
    tmp = NullPointerException_init_$Init$(message, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@1c585232)
    return tmp

visitClass
def IndexOutOfBoundsException_init_$Init$($this):
    RuntimeException_init_$Init$($this)
    visitDelegatingCOnstructorCall
    return $this

def IndexOutOfBoundsException_init_$Create$():
    tmp = IndexOutOfBoundsException_init_$Init$(Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@4e01cf43)
    return tmp

def IndexOutOfBoundsException_init_$Init$(message, $this):
    RuntimeException_init_$Init$(message, $this)
    visitDelegatingCOnstructorCall
    return $this

def IndexOutOfBoundsException_init_$Create$(message):
    tmp = IndexOutOfBoundsException_init_$Init$(message, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@12b19557)
    return tmp

visitClass
def NoWhenBranchMatchedException_init_$Init$($this):
    RuntimeException_init_$Init$($this)
    visitDelegatingCOnstructorCall
    return $this

def NoWhenBranchMatchedException_init_$Create$():
    tmp = NoWhenBranchMatchedException_init_$Init$(Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@48c7f0d9)
    return tmp

def NoWhenBranchMatchedException_init_$Init$(message, $this):
    RuntimeException_init_$Init$(message, $this)
    visitDelegatingCOnstructorCall
    return $this

def NoWhenBranchMatchedException_init_$Create$(message):
    tmp = NoWhenBranchMatchedException_init_$Init$(message, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@63b2ce4)
    return tmp

def NoWhenBranchMatchedException_init_$Init$(message, cause, $this):
    RuntimeException_init_$Init$(message, cause, $this)
    visitDelegatingCOnstructorCall
    return $this

def NoWhenBranchMatchedException_init_$Create$(message, cause):
    tmp = NoWhenBranchMatchedException_init_$Init$(message, cause, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@5e9c61cd)
    return tmp

def NoWhenBranchMatchedException_init_$Init$(cause, $this):
    RuntimeException_init_$Init$(cause, $this)
    visitDelegatingCOnstructorCall
    return $this

def NoWhenBranchMatchedException_init_$Create$(cause):
    tmp = NoWhenBranchMatchedException_init_$Init$(cause, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@618b995b)
    return tmp

visitClass
def ClassCastException_init_$Init$($this):
    RuntimeException_init_$Init$($this)
    visitDelegatingCOnstructorCall
    return $this

def ClassCastException_init_$Create$():
    tmp = ClassCastException_init_$Init$(Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@6f8fe7e8)
    return tmp

def ClassCastException_init_$Init$(message, $this):
    RuntimeException_init_$Init$(message, $this)
    visitDelegatingCOnstructorCall
    return $this

def ClassCastException_init_$Create$(message):
    tmp = ClassCastException_init_$Init$(message, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@35070f2b)
    return tmp

visitClass
def UninitializedPropertyAccessException_init_$Init$($this):
    RuntimeException_init_$Init$($this)
    visitDelegatingCOnstructorCall
    return $this

def UninitializedPropertyAccessException_init_$Create$():
    tmp = UninitializedPropertyAccessException_init_$Init$(Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@351ac4c7)
    return tmp

def UninitializedPropertyAccessException_init_$Init$(message, $this):
    RuntimeException_init_$Init$(message, $this)
    visitDelegatingCOnstructorCall
    return $this

def UninitializedPropertyAccessException_init_$Create$(message):
    tmp = UninitializedPropertyAccessException_init_$Init$(message, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@3e971bd5)
    return tmp

def UninitializedPropertyAccessException_init_$Init$(message, cause, $this):
    RuntimeException_init_$Init$(message, cause, $this)
    visitDelegatingCOnstructorCall
    return $this

def UninitializedPropertyAccessException_init_$Create$(message, cause):
    tmp = UninitializedPropertyAccessException_init_$Init$(message, cause, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@33032086)
    return tmp

def UninitializedPropertyAccessException_init_$Init$(cause, $this):
    RuntimeException_init_$Init$(cause, $this)
    visitDelegatingCOnstructorCall
    return $this

def UninitializedPropertyAccessException_init_$Create$(cause):
    tmp = UninitializedPropertyAccessException_init_$Init$(cause, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@59e33cea)
    return tmp

visitClass
def jsIn(lhs_hack, rhs_hack):
    tmp0_unsafeCast_0 = js('lhs_hack in rhs_hack')
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@6dc78fa8

def jsBitwiseOr(lhs_hack, rhs_hack):
    tmp0_unsafeCast_0 = js('lhs_hack | rhs_hack')
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@3fdd1006

def jsTypeOf(value_hack):
    tmp0_unsafeCast_0 = js('typeof value_hack')
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@56725cf0

def jsInstanceOf(obj_hack, jsClass_hack):
    tmp0_unsafeCast_0 = js('obj_hack instanceof jsClass_hack')
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@4359b2f3

def jsBitwiseAnd(lhs_hack, rhs_hack):
    tmp0_unsafeCast_0 = js('lhs_hack & rhs_hack')
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@70916ae5

def toString(radix):
    return toStringImpl(checkRadix(radix))

def pythonTest():
    println('Hello world')
