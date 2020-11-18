def fold(initial, operation):
    accumulator = initial
    indexedObject = <this>
    inductionVariable = 0
    last = jsArrayLength(indexedObject)
    while jsLt(inductionVariable, last):
        element = jsArrayGet(indexedObject, inductionVariable)
        inductionVariable = jsBitOr(jsPlus(inductionVariable, 1), 0)
        accumulator = invoke(accumulator, element)
    
    return accumulator

def <get-indices>():
    return <init>(0, <get-lastIndex>())

def indexOf(element):
    if jsEqeq(element, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@51e0f2eb):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@7a51dc38
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@2626aa35:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@5ca8c904
    
    return -1

def lastIndexOf(element):
    if jsEqeq(element, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@5e9f1a4c):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@4bf89d3d
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@696ce057:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@5eba9e41
    
    return -1

def <get-lastIndex>():
    return jsBitOr(jsMinus(jsArrayLength(<this>), 1), 0)

def joinToString(separator, prefix, postfix, limit, truncated, transform):
    return toString()

def joinToString$default(separator, prefix, postfix, limit, truncated, transform, $mask0, $handler):
    if jsNot(jsEqeqeq(jsBitAnd($mask0, 1), 0)):
        visitSetValue-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrSetValueImpl@6801b4a4
    
    if jsNot(jsEqeqeq(jsBitAnd($mask0, 2), 0)):
        visitSetValue-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrSetValueImpl@1e69a310
    
    if jsNot(jsEqeqeq(jsBitAnd($mask0, 4), 0)):
        visitSetValue-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrSetValueImpl@6415a53d
    
    if jsNot(jsEqeqeq(jsBitAnd($mask0, 8), 0)):
        visitSetValue-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrSetValueImpl@5a1e47d3
    
    if jsNot(jsEqeqeq(jsBitAnd($mask0, 16), 0)):
        visitSetValue-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrSetValueImpl@10c0d39d
    
    if jsNot(jsEqeqeq(jsBitAnd($mask0, 32), 0)):
        visitSetValue-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrSetValueImpl@719a208f
    
    return joinToString(kotlin.CharSequence(separator), kotlin.CharSequence(prefix), kotlin.CharSequence(postfix), limit, kotlin.CharSequence(truncated), transform)

def joinTo(buffer, separator, prefix, postfix, limit, truncated, transform):
    append(prefix)
    Unit_getInstance()
    count = 0
    indexedObject = <this>
    inductionVariable = 0
    last = jsArrayLength(indexedObject)
    while jsLt(inductionVariable, last):
        element = jsArrayGet(indexedObject, inductionVariable)
        inductionVariable = jsBitOr(jsPlus(inductionVariable, 1), 0)
        count = jsBitOr(jsPlus(count, 1), 0)
        if jsGt(count, 1):
            visitComposite-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrCompositeImpl@386643e
        
        if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@1c825108:
            visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@2c956132
        
        if visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@68d93913:
            visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@3dfa2f64
        
        if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@4fce3ed7:
            visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBreakImpl@54033a65
        
    
    if visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@7590ce28:
        visitComposite-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrCompositeImpl@39fc5c09
    
    append(postfix)
    Unit_getInstance()
    return buffer

def joinTo$default(buffer, separator, prefix, postfix, limit, truncated, transform, $mask0, $handler):
    if jsNot(jsEqeqeq(jsBitAnd($mask0, 2), 0)):
        visitSetValue-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrSetValueImpl@73a815c2
    
    if jsNot(jsEqeqeq(jsBitAnd($mask0, 4), 0)):
        visitSetValue-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrSetValueImpl@10dad714
    
    if jsNot(jsEqeqeq(jsBitAnd($mask0, 8), 0)):
        visitSetValue-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrSetValueImpl@60274863
    
    if jsNot(jsEqeqeq(jsBitAnd($mask0, 16), 0)):
        visitSetValue-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrSetValueImpl@5e3d3bfd
    
    if jsNot(jsEqeqeq(jsBitAnd($mask0, 32), 0)):
        visitSetValue-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrSetValueImpl@4891aee2
    
    if jsNot(jsEqeqeq(jsBitAnd($mask0, 64), 0)):
        visitSetValue-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrSetValueImpl@37630101
    
    return joinTo(buffer, kotlin.CharSequence(separator), kotlin.CharSequence(prefix), kotlin.CharSequence(postfix), limit, kotlin.CharSequence(truncated), transform)

def contains(element):
    return jsGtEq(indexOf(element), 0)

def indexOf(element):
    inductionVariable = 0
    last = jsBitOr(jsMinus(jsArrayLength(<this>), 1), 0)
    if jsLtEq(inductionVariable, last):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDoWhileLoopImpl@23e883fb
    
    return -1

def <get-indices>():
    return <init>(0, <get-lastIndex>())

def <get-lastIndex>():
    return jsBitOr(jsMinus(jsArrayLength(<this>), 1), 0)

def contains(element):
    return jsGtEq(indexOf(element), 0)

def indexOf(element):
    inductionVariable = 0
    last = jsBitOr(jsMinus(jsArrayLength(<this>), 1), 0)
    if jsLtEq(inductionVariable, last):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDoWhileLoopImpl@22272bac
    
    return -1

def <get-indices>():
    return <init>(0, <get-lastIndex>())

def <get-lastIndex>():
    return jsBitOr(jsMinus(jsArrayLength(<this>), 1), 0)

def contains(element):
    return jsGtEq(indexOf(element), 0)

def indexOf(element):
    inductionVariable = 0
    last = jsBitOr(jsMinus(jsArrayLength(<this>), 1), 0)
    if jsLtEq(inductionVariable, last):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDoWhileLoopImpl@52f3859a
    
    return -1

def <get-indices>():
    return <init>(0, <get-lastIndex>())

def <get-lastIndex>():
    return jsBitOr(jsMinus(jsArrayLength(<this>), 1), 0)

def contains(element):
    return jsGtEq(indexOf(element), 0)

def indexOf(element):
    inductionVariable = 0
    last = jsBitOr(jsMinus(jsArrayLength(<this>), 1), 0)
    if jsLtEq(inductionVariable, last):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDoWhileLoopImpl@10eddc8b
    
    return -1

def <get-indices>():
    return <init>(0, <get-lastIndex>())

def <get-lastIndex>():
    return jsBitOr(jsMinus(jsArrayLength(<this>), 1), 0)

def indexOfFirst(predicate):
    index = 0
    tmp0_iterator = iterator()
    while hasNext():
        item = next()
        if invoke(item):
            visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@5599f7a5
        
        tmp1 = index
        index = jsBitOr(jsPlus(tmp1, 1), 0)
        Unit_getInstance()
    
    return -1

def indexOfLast(predicate):
    iterator = listIterator(<get-size>())
    while hasPrevious():
        if invoke(previous()):
            visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@59c4921f
        
    
    return -1

def any(predicate):
    tmp
    if isInterface(<this>, jsClass()):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@712a6e68
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@2f6a923d:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@6cd76b55
    
    if tmp:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@477ac359
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@39c65cb4:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@283730de
    
    tmp0_iterator = iterator()
    while hasNext():
        element = next()
        if invoke(element):
            visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@64b05928
        
    
    return visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@7cb77d5

def all(predicate):
    tmp
    if isInterface(<this>, jsClass()):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@688d3e2a
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@6dbcb435:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@5b270c33
    
    if tmp:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@3e9a0143
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@23368646:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@4dc80b7a
    
    tmp0_iterator = iterator()
    while hasNext():
        element = next()
        if jsNot(invoke(element)):
            visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@179b88a6
        
    
    return visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@456d03cd

def joinToString(separator, prefix, postfix, limit, truncated, transform):
    return toString()

def joinToString$default(separator, prefix, postfix, limit, truncated, transform, $mask0, $handler):
    if jsNot(jsEqeqeq(jsBitAnd($mask0, 1), 0)):
        visitSetValue-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrSetValueImpl@742b91a5
    
    if jsNot(jsEqeqeq(jsBitAnd($mask0, 2), 0)):
        visitSetValue-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrSetValueImpl@4c48564d
    
    if jsNot(jsEqeqeq(jsBitAnd($mask0, 4), 0)):
        visitSetValue-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrSetValueImpl@3ed3bfcb
    
    if jsNot(jsEqeqeq(jsBitAnd($mask0, 8), 0)):
        visitSetValue-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrSetValueImpl@7ba92958
    
    if jsNot(jsEqeqeq(jsBitAnd($mask0, 16), 0)):
        visitSetValue-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrSetValueImpl@10d28ee2
    
    if jsNot(jsEqeqeq(jsBitAnd($mask0, 32), 0)):
        visitSetValue-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrSetValueImpl@18a6451f
    
    return joinToString(kotlin.CharSequence(separator), kotlin.CharSequence(prefix), kotlin.CharSequence(postfix), limit, kotlin.CharSequence(truncated), transform)

def joinTo(buffer, separator, prefix, postfix, limit, truncated, transform):
    append(prefix)
    Unit_getInstance()
    count = 0
    tmp0_iterator = iterator()
    while hasNext():
        element = next()
        count = jsBitOr(jsPlus(count, 1), 0)
        if jsGt(count, 1):
            visitComposite-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrCompositeImpl@1618b4fa
        
        if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@3f2fd933:
            visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@6c430548
        
        if visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@3bd05779:
            visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@63243c8f
        
        if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@599310ab:
            visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBreakImpl@770cbe5d
        
    
    if visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@5b0d8236:
        visitComposite-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrCompositeImpl@aa24615
    
    append(postfix)
    Unit_getInstance()
    return buffer

def joinTo$default(buffer, separator, prefix, postfix, limit, truncated, transform, $mask0, $handler):
    if jsNot(jsEqeqeq(jsBitAnd($mask0, 2), 0)):
        visitSetValue-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrSetValueImpl@564d5883
    
    if jsNot(jsEqeqeq(jsBitAnd($mask0, 4), 0)):
        visitSetValue-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrSetValueImpl@dc46916
    
    if jsNot(jsEqeqeq(jsBitAnd($mask0, 8), 0)):
        visitSetValue-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrSetValueImpl@14f03098
    
    if jsNot(jsEqeqeq(jsBitAnd($mask0, 16), 0)):
        visitSetValue-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrSetValueImpl@2d66a5d3
    
    if jsNot(jsEqeqeq(jsBitAnd($mask0, 32), 0)):
        visitSetValue-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrSetValueImpl@4f8aa5fe
    
    if jsNot(jsEqeqeq(jsBitAnd($mask0, 64), 0)):
        visitSetValue-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrSetValueImpl@26505df2
    
    return joinTo(buffer, kotlin.CharSequence(separator), kotlin.CharSequence(prefix), kotlin.CharSequence(postfix), limit, kotlin.CharSequence(truncated), transform)

def downTo(to):
    return fromClosedRange(<this>, to, -1)

def until(to):
    if jsLtEq(to, MIN_VALUE):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@68f264bf
    
    return numberRangeToNumber(<this>, kotlin.Int(jsBitOr(jsMinus(to, 1), 0)))

def reversed():
    return fromClosedRange(last, first, jsBitOr(jsUnaryMinus(step), 0))

def getOrElse(index, defaultValue):
    return visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@6670d46e

def KotlinNothingValueException_init_$Init$($this):
    RuntimeException_init_$Init$($this)
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@54557dd8
    return $this

def KotlinNothingValueException_init_$Create$():
    tmp = KotlinNothingValueException_init_$Init$(Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@11f8bff1)
    return tmp

def KotlinNothingValueException_init_$Init$(message, $this):
    RuntimeException_init_$Init$(message, $this)
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@29862f60
    return $this

def KotlinNothingValueException_init_$Create$(message):
    tmp = KotlinNothingValueException_init_$Init$(message, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@3dd916d9)
    return tmp

def KotlinNothingValueException_init_$Init$(message, cause, $this):
    RuntimeException_init_$Init$(message, cause, $this)
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@39a54d70
    return $this

def KotlinNothingValueException_init_$Create$(message, cause):
    tmp = KotlinNothingValueException_init_$Init$(message, cause, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@2be33ac)
    return tmp

def KotlinNothingValueException_init_$Init$(cause, $this):
    RuntimeException_init_$Init$(cause, $this)
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@67a02460
    return $this

def KotlinNothingValueException_init_$Create$(cause):
    tmp = KotlinNothingValueException_init_$Init$(cause, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@3bbb5b2)
    return tmp

class KotlinNothingValueException:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@33dbd53
visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@33260ecd
def values():
    return arrayLiteral(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrVarargImpl@49c15ad2)

def valueOf(value):
    return visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@6644b7b9

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@27ca3040
def Level_initEntries():
    if Level_entriesInitialized:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@435a2e1f
    
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@2b60acb3
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@18211894
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@76cb6d16

def Experimental_init_$Init$(level, $mask0, $marker, $this):
    if jsNot(jsEqeqeq(jsBitAnd($mask0, 1), 0)):
        visitSetValue-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrSetValueImpl@658ec00c
    
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@4fe3d15f
    return $this

def Experimental_init_$Create$(level, $mask0, $marker):
    return Experimental_init_$Init$(level, $mask0, $marker, Object$create())

class Level:
    pass

def Level_WARNING_getInstance():
    Level_initEntries()
    return Level_WARNING_instance

def Level_ERROR_getInstance():
    Level_initEntries()
    return Level_ERROR_instance

class Experimental:
    pass

class WasExperimental:
    pass

class ExperimentalStdlibApi:
    pass

class OptionalExpectation:
    pass

class ExperimentalMultiplatform:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@3729cdaf
visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@75a45ce
def values():
    return arrayLiteral(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrVarargImpl@6910e725)

def valueOf(value):
    return visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@6549ac6d

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@2dbc56fb
def Level_initEntries():
    if Level_entriesInitialized:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@3ebda1be
    
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@2cf1c10e
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@19b019a6
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@599bda7e

def RequiresOptIn_init_$Init$(message, level, $mask0, $marker, $this):
    if jsNot(jsEqeqeq(jsBitAnd($mask0, 1), 0)):
        visitSetValue-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrSetValueImpl@1332d4ae
    
    if jsNot(jsEqeqeq(jsBitAnd($mask0, 2), 0)):
        visitSetValue-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrSetValueImpl@1bdaa13c
    
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@ff18823
    return $this

def RequiresOptIn_init_$Create$(message, level, $mask0, $marker):
    return RequiresOptIn_init_$Init$(message, level, $mask0, $marker, Object$create())

class Level:
    pass

def Level_WARNING_getInstance():
    Level_initEntries()
    return Level_WARNING_instance

def Level_ERROR_getInstance():
    Level_initEntries()
    return Level_ERROR_instance

class RequiresOptIn:
    pass

class OptIn:
    pass

class <no name provided>:
    pass

class AbstractCollection:
    pass

def <no name provided>$factory(this$0):
    i = <init>(this$0)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@4977e352

def <get-list>($this):
    return list

def <get-fromIndex>($this):
    return fromIndex

def <set-_size>($this, <set-?>):
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@35cb8b64

def <get-_size>($this):
    return _size

class SubList:
    pass

class IteratorImpl:
    pass

class ListIteratorImpl:
    pass

class Companion:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@7343df40
def Companion_getInstance():
    if jsEqeq(Companion_instance, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@346c568d):
        <init>()
    
    return Companion_instance

class AbstractList:
    pass

def listOf(elements):
    return visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@4de37f33

def emptyList():
    return EmptyList_getInstance()

def <get-serialVersionUID>($this):
    return serialVersionUID

def readResolve($this):
    return EmptyList_getInstance()

class EmptyList:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@2028ecf4
def EmptyList_getInstance():
    if jsEqeq(EmptyList_instance, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@26dcce41):
        <init>()
    
    return EmptyList_instance

class EmptyIterator:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@7bd03562
def EmptyIterator_getInstance():
    if jsEqeq(EmptyIterator_instance, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@6e7da5f4):
        <init>()
    
    return EmptyIterator_instance

def <get-lastIndex>():
    return jsBitOr(jsMinus(<get-size>(), 1), 0)

def removeAll(predicate):
    return filterInPlace(predicate, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@745c8a04)

def removeAll(predicate):
    return filterInPlace(predicate, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@6b4a2887)

def filterInPlace(predicate, predicateResultToRemove):
    if jsNot(isInterface(<this>, jsClass())):
        visitComposite-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrCompositeImpl@153d5d5b
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@30360716:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@6232025
    
    writeIndex = 0
    inductionVariable = 0
    last = <get-lastIndex>()
    if jsLtEq(inductionVariable, last):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDoWhileLoopImpl@6a4fb518
    
    if jsLt(writeIndex, <get-size>()):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@74ee97cb
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@39fc17be:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@106edde4
    

def filterInPlace(predicate, predicateResultToRemove):
    result = visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@5eae392d
    tmp0_with_0 = iterator()
    while hasNext():
        if jsEqeqeq(invoke(next()), predicateResultToRemove):
            visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@58e8535e
        
    
    return result

class Sequence:
    pass

def contract(builder):
    

class ContractBuilder:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@2275d28a
visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@598dca0a
visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@1b38563a
visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@1c7c56d
def values():
    return arrayLiteral(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrVarargImpl@5c43a52e)

def valueOf(value):
    return visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@6130156b

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@54707af8
def InvocationKind_initEntries():
    if InvocationKind_entriesInitialized:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@4d6a32d4
    
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@c377641
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@731a1399
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@49702efb
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@60f6aa4b
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@527ff176

class InvocationKind:
    pass

class ExperimentalContracts:
    pass

def InvocationKind_AT_MOST_ONCE_getInstance():
    InvocationKind_initEntries()
    return InvocationKind_AT_MOST_ONCE_instance

def InvocationKind_AT_LEAST_ONCE_getInstance():
    InvocationKind_initEntries()
    return InvocationKind_AT_LEAST_ONCE_instance

def InvocationKind_EXACTLY_ONCE_getInstance():
    InvocationKind_initEntries()
    return InvocationKind_EXACTLY_ONCE_instance

def InvocationKind_UNKNOWN_getInstance():
    InvocationKind_initEntries()
    return InvocationKind_UNKNOWN_instance

class CallsInPlace:
    pass

class Returns:
    pass

class ReturnsNotNull:
    pass

class Effect:
    pass

class SimpleEffect:
    pass

class ConditionalEffect:
    pass

class Continuation:
    pass

def Continuation(context, resumeWith):
    return <init>(context, resumeWith)

def resumeWithException(exception):
    tmp0_failure_0 = Companion_getInstance()
    return resumeWith(<init>(createFailure(exception)))

def resume(value):
    tmp0_success_0 = Companion_getInstance()
    return resumeWith(<init>(value))

def <get-coroutineContext>():
    visitThrow org.jetbrains.kotlin.ir.expressions.impl.IrThrowImpl@553f3655

class <no name provided>:
    pass

class Key:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@9d112d2
def Key_getInstance():
    if jsEqeq(Key_instance, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@4f1422f7):
        <init>()
    
    return Key_instance

class ContinuationInterceptor:
    pass

class Key:
    pass

class Element:
    pass

class <no name provided>:
    pass

class CoroutineContext:
    pass

def <no name provided>$factory():
    i = <init>()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@4358e209

def <get-serialVersionUID>($this):
    return serialVersionUID

def readResolve($this):
    return EmptyCoroutineContext_getInstance()

class EmptyCoroutineContext:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@9def6d
def EmptyCoroutineContext_getInstance():
    if jsEqeq(EmptyCoroutineContext_instance, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@5e206acb):
        <init>()
    
    return EmptyCoroutineContext_instance

def <get-serialVersionUID>($this):
    return serialVersionUID

class Companion:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@9ba905b
def Companion_getInstance():
    if jsEqeq(Companion_instance, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@6801536):
        <init>()
    
    return Companion_instance

def readResolve($this):
    tmp0_fold_0 = elements
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

def <get-left>($this):
    return left

def <get-element>($this):
    return element

def size($this):
    cur = $this
    size = 2
    while visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@3ed1cff:
        tmp = left
        tmp0_elvis_lhs = visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@1cccf90d
        tmp
        if jsEqeq(tmp0_elvis_lhs, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@7efceb57):
            visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@677f0c19
        
        if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@4a1ac68f:
            visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@4ca87783
        
        cur = tmp
        tmp1 = size
        size = jsBitOr(jsPlus(tmp1, 1), 0)
        Unit_getInstance()
    

def contains($this, element):
    return equals(get(<get-key>()), element)

def containsAll($this, context):
    cur = context
    while visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@60155d7f:
        if jsNot(contains($this, element)):
            visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@78483404
        
        next = left
        if jsInstanceOf(next, jsClass()):
            visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@13126d46
        
        if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@5e4b9f22:
            visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@5b4f77e1
        
    

def writeReplace($this):
    n = size($this)
    elements = fillArrayVal(Array(n), visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@196f7dfd)
    index = $sharedBox$create(0)
    fold(Unit_getInstance(), <no name provided>$factory(elements, index))
    tmp0_check_0 = jsEqeqeq($sharedBox$read(index), n)
    if jsNot(tmp0_check_0):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@2515ed62
    
    return <init>(visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@2300d6fd)

class Serialized:
    pass

class <no name provided>:
    pass

class <no name provided>:
    pass

class CombinedContext:
    pass

def <get-safeCast>($this):
    return safeCast

def <get-topmostKey>($this):
    return topmostKey

class AbstractCoroutineContextKey:
    pass

def <no name provided>$factory():
    i = <init>()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@754f951a

def <no name provided>$factory($elements, $index):
    i = <init>($elements, $index)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@134d6f96

def <get-COROUTINE_SUSPENDED>():
    return CoroutineSingletons_COROUTINE_SUSPENDED_getInstance()

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@7dc175c6
visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@1ddf5237
visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@5e4b92b3
def values():
    return arrayLiteral(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrVarargImpl@1f78d3bc)

def valueOf(value):
    return visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@4ac73165

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@2fc1b04a
def CoroutineSingletons_initEntries():
    if CoroutineSingletons_entriesInitialized:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@16c574c4
    
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@7dc97564
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@1e20dad5
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@2331ac37
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@588e4caa

class CoroutineSingletons:
    pass

def CoroutineSingletons_COROUTINE_SUSPENDED_getInstance():
    CoroutineSingletons_initEntries()
    return CoroutineSingletons_COROUTINE_SUSPENDED_instance

def CoroutineSingletons_UNDECIDED_getInstance():
    CoroutineSingletons_initEntries()
    return CoroutineSingletons_UNDECIDED_instance

def CoroutineSingletons_RESUMED_getInstance():
    CoroutineSingletons_initEntries()
    return CoroutineSingletons_RESUMED_instance

def and(other):
    return toByte(jsBitAnd(kotlin.Int(<this>), kotlin.Int(other)))

def or(other):
    return toByte(jsBitOr(kotlin.Int(<this>), kotlin.Int(other)))

def xor(other):
    return toByte(jsBitXor(kotlin.Int(<this>), kotlin.Int(other)))

def inv():
    return toByte(jsBitNot(kotlin.Int(<this>)))

def and(other):
    return toShort(jsBitAnd(kotlin.Int(<this>), kotlin.Int(other)))

def or(other):
    return toShort(jsBitOr(kotlin.Int(<this>), kotlin.Int(other)))

def xor(other):
    return toShort(jsBitXor(kotlin.Int(<this>), kotlin.Int(other)))

def inv():
    return toShort(jsBitNot(kotlin.Int(<this>)))

class ExperimentalTypeInference:
    pass

def RequireKotlin_init_$Init$(version, message, level, versionKind, errorCode, $mask0, $marker, $this):
    if jsNot(jsEqeqeq(jsBitAnd($mask0, 2), 0)):
        visitSetValue-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrSetValueImpl@6f3b07ed
    
    if jsNot(jsEqeqeq(jsBitAnd($mask0, 4), 0)):
        visitSetValue-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrSetValueImpl@725645f4
    
    if jsNot(jsEqeqeq(jsBitAnd($mask0, 8), 0)):
        visitSetValue-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrSetValueImpl@77e55368
    
    if jsNot(jsEqeqeq(jsBitAnd($mask0, 16), 0)):
        visitSetValue-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrSetValueImpl@73d4aa54
    
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@7c45bd55
    return $this

def RequireKotlin_init_$Create$(version, message, level, versionKind, errorCode, $mask0, $marker):
    return RequireKotlin_init_$Init$(version, message, level, versionKind, errorCode, $mask0, $marker, Object$create())

class RequireKotlin:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@75bd7c4a
visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@68535137
visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@14062855
def values():
    return arrayLiteral(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrVarargImpl@151ddfc6)

def valueOf(value):
    return visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@54fe40e0

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@4e572e47
def RequireKotlinVersionKind_initEntries():
    if RequireKotlinVersionKind_entriesInitialized:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@4e751350
    
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@3ed50b5f
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@4c6f451b
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@b956293
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@6ea4403f

class RequireKotlinVersionKind:
    pass

class InlineOnly:
    pass

class NoInfer:
    pass

class DynamicExtension:
    pass

class ContractsDsl:
    pass

class OnlyInputTypes:
    pass

def RequireKotlinVersionKind_LANGUAGE_VERSION_getInstance():
    RequireKotlinVersionKind_initEntries()
    return RequireKotlinVersionKind_LANGUAGE_VERSION_instance

def RequireKotlinVersionKind_COMPILER_VERSION_getInstance():
    RequireKotlinVersionKind_initEntries()
    return RequireKotlinVersionKind_COMPILER_VERSION_instance

def RequireKotlinVersionKind_API_VERSION_getInstance():
    RequireKotlinVersionKind_initEntries()
    return RequireKotlinVersionKind_API_VERSION_instance

class KClassifier:
    pass

class KTypeParameter:
    pass

class Companion:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@633f8efd
def Companion_getInstance():
    if jsEqeq(Companion_instance, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@14467f3b):
        <init>()
    
    return Companion_instance

class KTypeProjection:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@6acee861
visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@f60910d
visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@1a1c68f5
def values():
    return arrayLiteral(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrVarargImpl@7c0b71b5)

def valueOf(value):
    return visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@4f54b976

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@26ffe94e
def KVariance_initEntries():
    if KVariance_entriesInitialized:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@1adcd53b
    
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@47c90585
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@ff8df3
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@5917b984
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@18fe293d

class KVariance:
    pass

def KVariance_INVARIANT_getInstance():
    KVariance_initEntries()
    return KVariance_INVARIANT_instance

def KVariance_IN_getInstance():
    KVariance_initEntries()
    return KVariance_IN_instance

def KVariance_OUT_getInstance():
    KVariance_initEntries()
    return KVariance_OUT_instance

def appendElement(element, transform):
    if jsNot(jsEqeq(transform, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@50d91a0f)):
        visitComposite-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrCompositeImpl@77a3c614
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@3f341562:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@56cee7f6
    

def isEmpty():
    return jsEqeqeq(charSequenceLength(<this>), 0)

def <get-lastIndex>():
    return jsBitOr(jsMinus(charSequenceLength(<this>), 1), 0)

def <get-UNDEFINED_RESULT>():
    return UNDEFINED_RESULT

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@5a941fb4
def UNDEFINED_RESULT$init$():
    tmp0_success_0 = Companion_getInstance()
    tmp1_success_0 = <get-COROUTINE_SUSPENDED>()
    return <init>(tmp1_success_0)

def check(value):
    if jsNot(value):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@40df1311
    

def check(value, lazyMessage):
    if jsNot(value):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@34f195e8
    

def error(message):
    visitThrow org.jetbrains.kotlin.ir.expressions.impl.IrThrowImpl@54ba8e11

def require(value, lazyMessage):
    if jsNot(value):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@66e81cdd
    

def <Result__<get-value>-impl>(this):
    return value

def <Result__<get-isSuccess>-impl>(this):
    tmp = <Result__<get-value>-impl>(this)
    return jsNot(jsInstanceOf(tmp, jsClass()))

def <Result__<get-isFailure>-impl>(this):
    tmp = <Result__<get-value>-impl>(this)
    return jsInstanceOf(tmp, jsClass())

def Result__getOrNull-impl(this):
    tmp
    if <Result__<get-isFailure>-impl>(this):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@2c6a222a
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@39415641:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@7e26e452
    
    return tmp

def Result__exceptionOrNull-impl(this):
    tmp0_subject = <Result__<get-value>-impl>(this)
    tmp
    if jsInstanceOf(tmp0_subject, jsClass()):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@7cc880cf
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@1b67ea5f:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@19ea1606
    
    return tmp

def Result__toString-impl(this):
    tmp0_subject = <Result__<get-value>-impl>(this)
    tmp
    if jsInstanceOf(tmp0_subject, jsClass()):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@2b15d066
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@48a26095:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@79ae4822
    
    return tmp

class Companion:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@4bab64a2
def Companion_getInstance():
    if jsEqeq(Companion_instance, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@4af2f991):
        <init>()
    
    return Companion_instance

class Failure:
    pass

def Result__hashCode-impl(this):
    return visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@7e35c8b5

def Result__equals-impl(this, other):
    if jsNot(jsInstanceOf(other, jsClass())):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@551725e4
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@197cf24e:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@2c663246
    
    tmp0_other_with_cast = visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@22d2d248
    if jsNot(equals(value, value)):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@396519b
    
    return visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@7f3a92fd

class Result:
    pass

def createFailure(exception):
    return <init>(exception)

def getOrThrow():
    throwOnFailure()
    tmp = <Result__<get-value>-impl>(<this>)
    return visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@4710332d

def throwOnFailure():
    tmp = <Result__<get-value>-impl>(<this>)
    if jsInstanceOf(tmp, jsClass()):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrThrowImpl@14745c3c
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@5b64bc02:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@2572d409
    

def run(block):
    return invoke()

def TODO():
    visitThrow org.jetbrains.kotlin.ir.expressions.impl.IrThrowImpl@3f5f610d

def NotImplementedError_init_$Init$(message, $mask0, $marker, $this):
    if jsNot(jsEqeqeq(jsBitAnd($mask0, 1), 0)):
        visitSetValue-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrSetValueImpl@23497c5e
    
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@315139e2
    return $this

def NotImplementedError_init_$Create$(message, $mask0, $marker):
    tmp = NotImplementedError_init_$Init$(message, $mask0, $marker, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@1b406bc2)
    return tmp

class NotImplementedError:
    pass

def let(block):
    return invoke(<this>)

def apply(block):
    invoke(<this>)
    return <this>

def repeat(times, action):
    inductionVariable = 0
    if jsLt(inductionVariable, times):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDoWhileLoopImpl@24d7df03
    

def with(receiver, block):
    return invoke(receiver)

def also(block):
    invoke(<this>)
    return <this>

def run(block):
    return invoke(<this>)

def <UByte__<get-data>-impl>(this):
    return data

class Companion:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@511966dc
def Companion_getInstance():
    if jsEqeq(Companion_instance, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@1dafe1d2):
        <init>()
    
    return Companion_instance

def UByte__compareTo-impl(this, other):
    tmp = jsBitAnd(kotlin.Int(<UByte__<get-data>-impl>(this)), 255)
    return compareTo(tmp, jsBitAnd(kotlin.Int(<UByte__<get-data>-impl>(other)), 255))

def UByte__compareTo-impl(this, other):
    tmp = unboxIntrinsic(this)
    return UByte__compareTo-impl(tmp, visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@1275d11b)

def UByte__compareTo-impl(this, other):
    tmp = jsBitAnd(kotlin.Int(<UByte__<get-data>-impl>(this)), 255)
    return compareTo(tmp, jsBitAnd(kotlin.Int(<UShort__<get-data>-impl>(other)), 65535))

def UByte__compareTo-impl(this, other):
    tmp0_compareTo_0 = <init>(jsBitAnd(kotlin.Int(<UByte__<get-data>-impl>(this)), 255))
    return uintCompare(<UInt__<get-data>-impl>(tmp0_compareTo_0), <UInt__<get-data>-impl>(other))

def UByte__compareTo-impl(this, other):
    tmp0_compareTo_0 = <init>(and(<init>(255, 0)))
    return ulongCompare(<ULong__<get-data>-impl>(tmp0_compareTo_0), <ULong__<get-data>-impl>(other))

def UByte__plus-impl(this, other):
    tmp0_plus_0 = <init>(jsBitAnd(kotlin.Int(<UByte__<get-data>-impl>(this)), 255))
    tmp1_plus_0 = <init>(jsBitAnd(kotlin.Int(<UByte__<get-data>-impl>(other)), 255))
    return <init>(jsBitOr(jsPlus(<UInt__<get-data>-impl>(tmp0_plus_0), <UInt__<get-data>-impl>(tmp1_plus_0)), 0))

def UByte__plus-impl(this, other):
    tmp0_plus_0 = <init>(jsBitAnd(kotlin.Int(<UByte__<get-data>-impl>(this)), 255))
    tmp1_plus_0 = <init>(jsBitAnd(kotlin.Int(<UShort__<get-data>-impl>(other)), 65535))
    return <init>(jsBitOr(jsPlus(<UInt__<get-data>-impl>(tmp0_plus_0), <UInt__<get-data>-impl>(tmp1_plus_0)), 0))

def UByte__plus-impl(this, other):
    tmp0_plus_0 = <init>(jsBitAnd(kotlin.Int(<UByte__<get-data>-impl>(this)), 255))
    return <init>(jsBitOr(jsPlus(<UInt__<get-data>-impl>(tmp0_plus_0), <UInt__<get-data>-impl>(other)), 0))

def UByte__plus-impl(this, other):
    tmp0_plus_0 = <init>(and(<init>(255, 0)))
    return <init>(plus(<ULong__<get-data>-impl>(other)))

def UByte__minus-impl(this, other):
    tmp0_minus_0 = <init>(jsBitAnd(kotlin.Int(<UByte__<get-data>-impl>(this)), 255))
    tmp1_minus_0 = <init>(jsBitAnd(kotlin.Int(<UByte__<get-data>-impl>(other)), 255))
    return <init>(jsBitOr(jsMinus(<UInt__<get-data>-impl>(tmp0_minus_0), <UInt__<get-data>-impl>(tmp1_minus_0)), 0))

def UByte__minus-impl(this, other):
    tmp0_minus_0 = <init>(jsBitAnd(kotlin.Int(<UByte__<get-data>-impl>(this)), 255))
    tmp1_minus_0 = <init>(jsBitAnd(kotlin.Int(<UShort__<get-data>-impl>(other)), 65535))
    return <init>(jsBitOr(jsMinus(<UInt__<get-data>-impl>(tmp0_minus_0), <UInt__<get-data>-impl>(tmp1_minus_0)), 0))

def UByte__minus-impl(this, other):
    tmp0_minus_0 = <init>(jsBitAnd(kotlin.Int(<UByte__<get-data>-impl>(this)), 255))
    return <init>(jsBitOr(jsMinus(<UInt__<get-data>-impl>(tmp0_minus_0), <UInt__<get-data>-impl>(other)), 0))

def UByte__minus-impl(this, other):
    tmp0_minus_0 = <init>(and(<init>(255, 0)))
    return <init>(minus(<ULong__<get-data>-impl>(other)))

def UByte__times-impl(this, other):
    tmp0_times_0 = <init>(jsBitAnd(kotlin.Int(<UByte__<get-data>-impl>(this)), 255))
    tmp1_times_0 = <init>(jsBitAnd(kotlin.Int(<UByte__<get-data>-impl>(other)), 255))
    return <init>(imul(<UInt__<get-data>-impl>(tmp0_times_0), <UInt__<get-data>-impl>(tmp1_times_0)))

def UByte__times-impl(this, other):
    tmp0_times_0 = <init>(jsBitAnd(kotlin.Int(<UByte__<get-data>-impl>(this)), 255))
    tmp1_times_0 = <init>(jsBitAnd(kotlin.Int(<UShort__<get-data>-impl>(other)), 65535))
    return <init>(imul(<UInt__<get-data>-impl>(tmp0_times_0), <UInt__<get-data>-impl>(tmp1_times_0)))

def UByte__times-impl(this, other):
    tmp0_times_0 = <init>(jsBitAnd(kotlin.Int(<UByte__<get-data>-impl>(this)), 255))
    return <init>(imul(<UInt__<get-data>-impl>(tmp0_times_0), <UInt__<get-data>-impl>(other)))

def UByte__times-impl(this, other):
    tmp0_times_0 = <init>(and(<init>(255, 0)))
    return <init>(times(<ULong__<get-data>-impl>(other)))

def UByte__div-impl(this, other):
    tmp0_div_0 = <init>(jsBitAnd(kotlin.Int(<UByte__<get-data>-impl>(this)), 255))
    tmp1_div_0 = <init>(jsBitAnd(kotlin.Int(<UByte__<get-data>-impl>(other)), 255))
    return uintDivide(tmp0_div_0, tmp1_div_0)

def UByte__div-impl(this, other):
    tmp0_div_0 = <init>(jsBitAnd(kotlin.Int(<UByte__<get-data>-impl>(this)), 255))
    tmp1_div_0 = <init>(jsBitAnd(kotlin.Int(<UShort__<get-data>-impl>(other)), 65535))
    return uintDivide(tmp0_div_0, tmp1_div_0)

def UByte__div-impl(this, other):
    tmp0_div_0 = <init>(jsBitAnd(kotlin.Int(<UByte__<get-data>-impl>(this)), 255))
    return uintDivide(tmp0_div_0, other)

def UByte__div-impl(this, other):
    tmp0_div_0 = <init>(and(<init>(255, 0)))
    return ulongDivide(tmp0_div_0, other)

def UByte__rem-impl(this, other):
    tmp0_rem_0 = <init>(jsBitAnd(kotlin.Int(<UByte__<get-data>-impl>(this)), 255))
    tmp1_rem_0 = <init>(jsBitAnd(kotlin.Int(<UByte__<get-data>-impl>(other)), 255))
    return uintRemainder(tmp0_rem_0, tmp1_rem_0)

def UByte__rem-impl(this, other):
    tmp0_rem_0 = <init>(jsBitAnd(kotlin.Int(<UByte__<get-data>-impl>(this)), 255))
    tmp1_rem_0 = <init>(jsBitAnd(kotlin.Int(<UShort__<get-data>-impl>(other)), 65535))
    return uintRemainder(tmp0_rem_0, tmp1_rem_0)

def UByte__rem-impl(this, other):
    tmp0_rem_0 = <init>(jsBitAnd(kotlin.Int(<UByte__<get-data>-impl>(this)), 255))
    return uintRemainder(tmp0_rem_0, other)

def UByte__rem-impl(this, other):
    tmp0_rem_0 = <init>(and(<init>(255, 0)))
    return ulongRemainder(tmp0_rem_0, other)

def UByte__inc-impl(this):
    return <init>(numberToByte(jsPlus(<UByte__<get-data>-impl>(this), 1)))

def UByte__dec-impl(this):
    return <init>(numberToByte(jsMinus(<UByte__<get-data>-impl>(this), 1)))

def UByte__rangeTo-impl(this, other):
    tmp = <init>(jsBitAnd(kotlin.Int(<UByte__<get-data>-impl>(this)), 255))
    return <init>(tmp, <init>(jsBitAnd(kotlin.Int(<UByte__<get-data>-impl>(other)), 255)))

def UByte__and-impl(this, other):
    tmp0_and_0 = <UByte__<get-data>-impl>(this)
    tmp1_and_0 = <UByte__<get-data>-impl>(other)
    return <init>(toByte(jsBitAnd(kotlin.Int(tmp0_and_0), kotlin.Int(tmp1_and_0))))

def UByte__or-impl(this, other):
    tmp0_or_0 = <UByte__<get-data>-impl>(this)
    tmp1_or_0 = <UByte__<get-data>-impl>(other)
    return <init>(toByte(jsBitOr(kotlin.Int(tmp0_or_0), kotlin.Int(tmp1_or_0))))

def UByte__xor-impl(this, other):
    tmp0_xor_0 = <UByte__<get-data>-impl>(this)
    tmp1_xor_0 = <UByte__<get-data>-impl>(other)
    return <init>(toByte(jsBitXor(kotlin.Int(tmp0_xor_0), kotlin.Int(tmp1_xor_0))))

def UByte__inv-impl(this):
    tmp0_inv_0 = <UByte__<get-data>-impl>(this)
    return <init>(toByte(jsBitNot(kotlin.Int(tmp0_inv_0))))

def UByte__toByte-impl(this):
    return <UByte__<get-data>-impl>(this)

def UByte__toShort-impl(this):
    tmp0_and_0 = kotlin.Short(<UByte__<get-data>-impl>(this))
    tmp1_and_0 = visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@720a3eff
    return toShort(jsBitAnd(kotlin.Int(tmp0_and_0), kotlin.Int(tmp1_and_0)))

def UByte__toInt-impl(this):
    return jsBitAnd(kotlin.Int(<UByte__<get-data>-impl>(this)), 255)

def UByte__toLong-impl(this):
    return and(<init>(255, 0))

def UByte__toUByte-impl(this):
    return this

def UByte__toUShort-impl(this):
    tmp0_and_0 = kotlin.Short(<UByte__<get-data>-impl>(this))
    tmp1_and_0 = visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@5a934ef9
    return <init>(toShort(jsBitAnd(kotlin.Int(tmp0_and_0), kotlin.Int(tmp1_and_0))))

def UByte__toUInt-impl(this):
    return <init>(jsBitAnd(kotlin.Int(<UByte__<get-data>-impl>(this)), 255))

def UByte__toULong-impl(this):
    return <init>(and(<init>(255, 0)))

def UByte__toFloat-impl(this):
    return kotlin.Float(jsBitAnd(kotlin.Int(<UByte__<get-data>-impl>(this)), 255))

def UByte__toDouble-impl(this):
    return kotlin.Double(jsBitAnd(kotlin.Int(<UByte__<get-data>-impl>(this)), 255))

def UByte__toString-impl(this):
    return toString()

def UByte__hashCode-impl(this):
    return data

def UByte__equals-impl(this, other):
    if jsNot(jsInstanceOf(other, jsClass())):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@2148849f
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@58afc14:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@56ec941b
    
    tmp0_other_with_cast = visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@18a3095d
    if jsNot(jsEqeqeq(data, data)):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@2165d4ab
    
    return visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@4d529bc0

class UByte:
    pass

def toUByte():
    return <init>(toByte(<this>))

def toUByte():
    return <init>(toByte(<this>))

def toUByte():
    return <init>(toByte())

def toUByte():
    return <init>(<this>)

def <get-array>($this):
    return array

def <set-index>($this, <set-?>):
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@6da50b8f

def <get-index>($this):
    return index

def <UByteArray__<get-storage>-impl>(this):
    return storage

def <UByteArray__<init>-impl>(size):
    tmp = <init>(int8Array(size))
    return tmp

def UByteArray__get-impl(this, index):
    tmp0_toUByte_0 = jsArrayGet(<UByteArray__<get-storage>-impl>(this), index)
    return <init>(tmp0_toUByte_0)

def UByteArray__set-impl(this, index, value):
    tmp = <UByteArray__<get-storage>-impl>(this)
    jsArraySet(tmp, index, <UByte__<get-data>-impl>(value))

def <UByteArray__<get-size>-impl>(this):
    return jsArrayLength(<UByteArray__<get-storage>-impl>(this))

def UByteArray__iterator-impl(this):
    return <init>(<UByteArray__<get-storage>-impl>(this))

class Iterator:
    pass

def UByteArray__contains-impl(this, element):
    tmp = visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@142409b4
    if jsNot(jsInstanceOf(tmp, jsClass())):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@eda7dd3
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@25b14faf:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@6e0576da
    
    tmp = <UByteArray__<get-storage>-impl>(this)
    return contains(<UByte__<get-data>-impl>(element))

def UByteArray__contains-impl(this, element):
    if jsNot(jsInstanceOf(element, jsClass())):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@5a2cb8e5
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@83ffa7b:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@37eb8009
    
    tmp = unboxIntrinsic(this)
    return UByteArray__contains-impl(tmp, visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@51cea39e)

def UByteArray__containsAll-impl(this, elements):
    tmp$ret$0
    visitDoWhileLoop org.jetbrains.kotlin.ir.expressions.impl.IrDoWhileLoopImpl@3a3a0b3b
    return tmp$ret$0

def UByteArray__containsAll-impl(this, elements):
    return UByteArray__containsAll-impl(unboxIntrinsic(this), elements)

def UByteArray__isEmpty-impl(this):
    return jsEqeqeq(jsArrayLength(<UByteArray__<get-storage>-impl>(this)), 0)

def UByteArray__toString-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrStringConcatenationImpl@1c057fc8

def UByteArray__hashCode-impl(this):
    return hashCode(storage)

def UByteArray__equals-impl(this, other):
    if jsNot(jsInstanceOf(other, jsClass())):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@432b883
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@1f8c7cd7:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@6ba1a7fd
    
    tmp0_other_with_cast = visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@3a42b2b6
    if jsNot(equals(storage, storage)):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@2a4f1bc5
    
    return visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@4d145177

class UByteArray:
    pass

def <UInt__<get-data>-impl>(this):
    return data

class Companion:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@4c6d1f1f
def Companion_getInstance():
    if jsEqeq(Companion_instance, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@70ab102c):
        <init>()
    
    return Companion_instance

def UInt__compareTo-impl(this, other):
    tmp0_compareTo_0 = <init>(jsBitAnd(kotlin.Int(<UByte__<get-data>-impl>(other)), 255))
    return uintCompare(<UInt__<get-data>-impl>(this), <UInt__<get-data>-impl>(tmp0_compareTo_0))

def UInt__compareTo-impl(this, other):
    tmp0_compareTo_0 = <init>(jsBitAnd(kotlin.Int(<UShort__<get-data>-impl>(other)), 65535))
    return uintCompare(<UInt__<get-data>-impl>(this), <UInt__<get-data>-impl>(tmp0_compareTo_0))

def UInt__compareTo-impl(this, other):
    return uintCompare(<UInt__<get-data>-impl>(this), <UInt__<get-data>-impl>(other))

def UInt__compareTo-impl(this, other):
    tmp = unboxIntrinsic(this)
    return UInt__compareTo-impl(tmp, visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@41ee3c99)

def UInt__compareTo-impl(this, other):
    tmp0_compareTo_0 = <init>(and(<init>(-1, 0)))
    return ulongCompare(<ULong__<get-data>-impl>(tmp0_compareTo_0), <ULong__<get-data>-impl>(other))

def UInt__plus-impl(this, other):
    tmp0_plus_0 = <init>(jsBitAnd(kotlin.Int(<UByte__<get-data>-impl>(other)), 255))
    return <init>(jsBitOr(jsPlus(<UInt__<get-data>-impl>(this), <UInt__<get-data>-impl>(tmp0_plus_0)), 0))

def UInt__plus-impl(this, other):
    tmp0_plus_0 = <init>(jsBitAnd(kotlin.Int(<UShort__<get-data>-impl>(other)), 65535))
    return <init>(jsBitOr(jsPlus(<UInt__<get-data>-impl>(this), <UInt__<get-data>-impl>(tmp0_plus_0)), 0))

def UInt__plus-impl(this, other):
    return <init>(jsBitOr(jsPlus(<UInt__<get-data>-impl>(this), <UInt__<get-data>-impl>(other)), 0))

def UInt__plus-impl(this, other):
    tmp0_plus_0 = <init>(and(<init>(-1, 0)))
    return <init>(plus(<ULong__<get-data>-impl>(other)))

def UInt__minus-impl(this, other):
    tmp0_minus_0 = <init>(jsBitAnd(kotlin.Int(<UByte__<get-data>-impl>(other)), 255))
    return <init>(jsBitOr(jsMinus(<UInt__<get-data>-impl>(this), <UInt__<get-data>-impl>(tmp0_minus_0)), 0))

def UInt__minus-impl(this, other):
    tmp0_minus_0 = <init>(jsBitAnd(kotlin.Int(<UShort__<get-data>-impl>(other)), 65535))
    return <init>(jsBitOr(jsMinus(<UInt__<get-data>-impl>(this), <UInt__<get-data>-impl>(tmp0_minus_0)), 0))

def UInt__minus-impl(this, other):
    return <init>(jsBitOr(jsMinus(<UInt__<get-data>-impl>(this), <UInt__<get-data>-impl>(other)), 0))

def UInt__minus-impl(this, other):
    tmp0_minus_0 = <init>(and(<init>(-1, 0)))
    return <init>(minus(<ULong__<get-data>-impl>(other)))

def UInt__times-impl(this, other):
    tmp0_times_0 = <init>(jsBitAnd(kotlin.Int(<UByte__<get-data>-impl>(other)), 255))
    return <init>(imul(<UInt__<get-data>-impl>(this), <UInt__<get-data>-impl>(tmp0_times_0)))

def UInt__times-impl(this, other):
    tmp0_times_0 = <init>(jsBitAnd(kotlin.Int(<UShort__<get-data>-impl>(other)), 65535))
    return <init>(imul(<UInt__<get-data>-impl>(this), <UInt__<get-data>-impl>(tmp0_times_0)))

def UInt__times-impl(this, other):
    return <init>(imul(<UInt__<get-data>-impl>(this), <UInt__<get-data>-impl>(other)))

def UInt__times-impl(this, other):
    tmp0_times_0 = <init>(and(<init>(-1, 0)))
    return <init>(times(<ULong__<get-data>-impl>(other)))

def UInt__div-impl(this, other):
    tmp0_div_0 = <init>(jsBitAnd(kotlin.Int(<UByte__<get-data>-impl>(other)), 255))
    return uintDivide(this, tmp0_div_0)

def UInt__div-impl(this, other):
    tmp0_div_0 = <init>(jsBitAnd(kotlin.Int(<UShort__<get-data>-impl>(other)), 65535))
    return uintDivide(this, tmp0_div_0)

def UInt__div-impl(this, other):
    return uintDivide(this, other)

def UInt__div-impl(this, other):
    tmp0_div_0 = <init>(and(<init>(-1, 0)))
    return ulongDivide(tmp0_div_0, other)

def UInt__rem-impl(this, other):
    tmp0_rem_0 = <init>(jsBitAnd(kotlin.Int(<UByte__<get-data>-impl>(other)), 255))
    return uintRemainder(this, tmp0_rem_0)

def UInt__rem-impl(this, other):
    tmp0_rem_0 = <init>(jsBitAnd(kotlin.Int(<UShort__<get-data>-impl>(other)), 65535))
    return uintRemainder(this, tmp0_rem_0)

def UInt__rem-impl(this, other):
    return uintRemainder(this, other)

def UInt__rem-impl(this, other):
    tmp0_rem_0 = <init>(and(<init>(-1, 0)))
    return ulongRemainder(tmp0_rem_0, other)

def UInt__inc-impl(this):
    return <init>(jsBitOr(jsPlus(<UInt__<get-data>-impl>(this), 1), 0))

def UInt__dec-impl(this):
    return <init>(jsBitOr(jsMinus(<UInt__<get-data>-impl>(this), 1), 0))

def UInt__rangeTo-impl(this, other):
    return <init>(this, other)

def UInt__shl-impl(this, bitCount):
    return <init>(jsBitShiftL(<UInt__<get-data>-impl>(this), bitCount))

def UInt__shr-impl(this, bitCount):
    return <init>(jsBitShiftRU(<UInt__<get-data>-impl>(this), bitCount))

def UInt__and-impl(this, other):
    return <init>(jsBitAnd(<UInt__<get-data>-impl>(this), <UInt__<get-data>-impl>(other)))

def UInt__or-impl(this, other):
    return <init>(jsBitOr(<UInt__<get-data>-impl>(this), <UInt__<get-data>-impl>(other)))

def UInt__xor-impl(this, other):
    return <init>(jsBitXor(<UInt__<get-data>-impl>(this), <UInt__<get-data>-impl>(other)))

def UInt__inv-impl(this):
    return <init>(jsBitNot(<UInt__<get-data>-impl>(this)))

def UInt__toByte-impl(this):
    return toByte(<UInt__<get-data>-impl>(this))

def UInt__toShort-impl(this):
    return toShort(<UInt__<get-data>-impl>(this))

def UInt__toInt-impl(this):
    return <UInt__<get-data>-impl>(this)

def UInt__toLong-impl(this):
    return and(<init>(-1, 0))

def UInt__toUByte-impl(this):
    tmp0_toUByte_0 = <UInt__<get-data>-impl>(this)
    return <init>(toByte(tmp0_toUByte_0))

def UInt__toUShort-impl(this):
    tmp0_toUShort_0 = <UInt__<get-data>-impl>(this)
    return <init>(toShort(tmp0_toUShort_0))

def UInt__toUInt-impl(this):
    return this

def UInt__toULong-impl(this):
    return <init>(and(<init>(-1, 0)))

def UInt__toFloat-impl(this):
    return kotlin.Float(uintToDouble(<UInt__<get-data>-impl>(this)))

def UInt__toDouble-impl(this):
    return uintToDouble(<UInt__<get-data>-impl>(this))

def UInt__toString-impl(this):
    return toString()

def UInt__hashCode-impl(this):
    return data

def UInt__equals-impl(this, other):
    if jsNot(jsInstanceOf(other, jsClass())):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@ad6255e
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@7b5de23c:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@6f39e2a6
    
    tmp0_other_with_cast = visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@2dd61113
    if jsNot(jsEqeqeq(data, data)):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@26bbbe9e
    
    return visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@72ad577b

class UInt:
    pass

def toUInt():
    return <init>(toInt())

def toUInt():
    return <init>(<this>)

def toUInt():
    return <init>(kotlin.Int(<this>))

def toUInt():
    return doubleToUInt(<this>)

def toUInt():
    return doubleToUInt(kotlin.Double(<this>))

def toUInt():
    return <init>(kotlin.Int(<this>))

def <get-array>($this):
    return array

def <set-index>($this, <set-?>):
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@257d8340

def <get-index>($this):
    return index

def <UIntArray__<get-storage>-impl>(this):
    return storage

def <UIntArray__<init>-impl>(size):
    tmp = <init>(int32Array(size))
    return tmp

def UIntArray__get-impl(this, index):
    tmp0_toUInt_0 = jsArrayGet(<UIntArray__<get-storage>-impl>(this), index)
    return <init>(tmp0_toUInt_0)

def UIntArray__set-impl(this, index, value):
    tmp = <UIntArray__<get-storage>-impl>(this)
    jsArraySet(tmp, index, <UInt__<get-data>-impl>(value))

def <UIntArray__<get-size>-impl>(this):
    return jsArrayLength(<UIntArray__<get-storage>-impl>(this))

def UIntArray__iterator-impl(this):
    return <init>(<UIntArray__<get-storage>-impl>(this))

class Iterator:
    pass

def UIntArray__contains-impl(this, element):
    tmp = visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@3d8777ce
    if jsNot(jsInstanceOf(tmp, jsClass())):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@6ab6ec33
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@418a5228:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@20ed6c31
    
    tmp = <UIntArray__<get-storage>-impl>(this)
    return contains(<UInt__<get-data>-impl>(element))

def UIntArray__contains-impl(this, element):
    if jsNot(jsInstanceOf(element, jsClass())):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@6e12352d
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@a404535:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@7584b20d
    
    tmp = unboxIntrinsic(this)
    return UIntArray__contains-impl(tmp, visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@260aeb5a)

def UIntArray__containsAll-impl(this, elements):
    tmp$ret$0
    visitDoWhileLoop org.jetbrains.kotlin.ir.expressions.impl.IrDoWhileLoopImpl@19c37463
    return tmp$ret$0

def UIntArray__containsAll-impl(this, elements):
    return UIntArray__containsAll-impl(unboxIntrinsic(this), elements)

def UIntArray__isEmpty-impl(this):
    return jsEqeqeq(jsArrayLength(<UIntArray__<get-storage>-impl>(this)), 0)

def UIntArray__toString-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrStringConcatenationImpl@5341eab4

def UIntArray__hashCode-impl(this):
    return hashCode(storage)

def UIntArray__equals-impl(this, other):
    if jsNot(jsInstanceOf(other, jsClass())):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@3c39c739
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@285289cd:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@697699cb
    
    tmp0_other_with_cast = visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@3a7f7201
    if jsNot(equals(storage, storage)):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@3e7da4cb
    
    return visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@3a2881d6

class UIntArray:
    pass

class Companion:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@3f81872b
def Companion_getInstance():
    if jsEqeq(Companion_instance, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@561fdee3):
        <init>()
    
    return Companion_instance

class UIntRange:
    pass

class Companion:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@641c872d
def Companion_getInstance():
    if jsEqeq(Companion_instance, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@4cf22d79):
        <init>()
    
    return Companion_instance

class UIntProgression:
    pass

def <get-finalElement>($this):
    return finalElement

def <set-hasNext>($this, <set-?>):
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@7c4a0245

def <get-hasNext>($this):
    return hasNext

def <get-step>($this):
    return step

def <set-next>($this, <set-?>):
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@7c0514f

def <get-next>($this):
    return next

class UIntProgressionIterator:
    pass

class UIntIterator:
    pass

class ULongIterator:
    pass

class UByteIterator:
    pass

class UShortIterator:
    pass

def <ULong__<get-data>-impl>(this):
    return data

class Companion:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@39b88618
def Companion_getInstance():
    if jsEqeq(Companion_instance, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@321f3b88):
        <init>()
    
    return Companion_instance

def ULong__compareTo-impl(this, other):
    tmp0_compareTo_0 = <init>(and(<init>(255, 0)))
    return ulongCompare(<ULong__<get-data>-impl>(this), <ULong__<get-data>-impl>(tmp0_compareTo_0))

def ULong__compareTo-impl(this, other):
    tmp0_compareTo_0 = <init>(and(<init>(65535, 0)))
    return ulongCompare(<ULong__<get-data>-impl>(this), <ULong__<get-data>-impl>(tmp0_compareTo_0))

def ULong__compareTo-impl(this, other):
    tmp0_compareTo_0 = <init>(and(<init>(-1, 0)))
    return ulongCompare(<ULong__<get-data>-impl>(this), <ULong__<get-data>-impl>(tmp0_compareTo_0))

def ULong__compareTo-impl(this, other):
    return ulongCompare(<ULong__<get-data>-impl>(this), <ULong__<get-data>-impl>(other))

def ULong__compareTo-impl(this, other):
    tmp = unboxIntrinsic(this)
    return ULong__compareTo-impl(tmp, visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@633f30af)

def ULong__plus-impl(this, other):
    tmp0_plus_0 = <init>(and(<init>(255, 0)))
    return <init>(plus(<ULong__<get-data>-impl>(tmp0_plus_0)))

def ULong__plus-impl(this, other):
    tmp0_plus_0 = <init>(and(<init>(65535, 0)))
    return <init>(plus(<ULong__<get-data>-impl>(tmp0_plus_0)))

def ULong__plus-impl(this, other):
    tmp0_plus_0 = <init>(and(<init>(-1, 0)))
    return <init>(plus(<ULong__<get-data>-impl>(tmp0_plus_0)))

def ULong__plus-impl(this, other):
    return <init>(plus(<ULong__<get-data>-impl>(other)))

def ULong__minus-impl(this, other):
    tmp0_minus_0 = <init>(and(<init>(255, 0)))
    return <init>(minus(<ULong__<get-data>-impl>(tmp0_minus_0)))

def ULong__minus-impl(this, other):
    tmp0_minus_0 = <init>(and(<init>(65535, 0)))
    return <init>(minus(<ULong__<get-data>-impl>(tmp0_minus_0)))

def ULong__minus-impl(this, other):
    tmp0_minus_0 = <init>(and(<init>(-1, 0)))
    return <init>(minus(<ULong__<get-data>-impl>(tmp0_minus_0)))

def ULong__minus-impl(this, other):
    return <init>(minus(<ULong__<get-data>-impl>(other)))

def ULong__times-impl(this, other):
    tmp0_times_0 = <init>(and(<init>(255, 0)))
    return <init>(times(<ULong__<get-data>-impl>(tmp0_times_0)))

def ULong__times-impl(this, other):
    tmp0_times_0 = <init>(and(<init>(65535, 0)))
    return <init>(times(<ULong__<get-data>-impl>(tmp0_times_0)))

def ULong__times-impl(this, other):
    tmp0_times_0 = <init>(and(<init>(-1, 0)))
    return <init>(times(<ULong__<get-data>-impl>(tmp0_times_0)))

def ULong__times-impl(this, other):
    return <init>(times(<ULong__<get-data>-impl>(other)))

def ULong__div-impl(this, other):
    tmp0_div_0 = <init>(and(<init>(255, 0)))
    return ulongDivide(this, tmp0_div_0)

def ULong__div-impl(this, other):
    tmp0_div_0 = <init>(and(<init>(65535, 0)))
    return ulongDivide(this, tmp0_div_0)

def ULong__div-impl(this, other):
    tmp0_div_0 = <init>(and(<init>(-1, 0)))
    return ulongDivide(this, tmp0_div_0)

def ULong__div-impl(this, other):
    return ulongDivide(this, other)

def ULong__rem-impl(this, other):
    tmp0_rem_0 = <init>(and(<init>(255, 0)))
    return ulongRemainder(this, tmp0_rem_0)

def ULong__rem-impl(this, other):
    tmp0_rem_0 = <init>(and(<init>(65535, 0)))
    return ulongRemainder(this, tmp0_rem_0)

def ULong__rem-impl(this, other):
    tmp0_rem_0 = <init>(and(<init>(-1, 0)))
    return ulongRemainder(this, tmp0_rem_0)

def ULong__rem-impl(this, other):
    return ulongRemainder(this, other)

def ULong__inc-impl(this):
    return <init>(inc())

def ULong__dec-impl(this):
    return <init>(dec())

def ULong__rangeTo-impl(this, other):
    return <init>(this, other)

def ULong__shl-impl(this, bitCount):
    return <init>(shl(bitCount))

def ULong__shr-impl(this, bitCount):
    return <init>(ushr(bitCount))

def ULong__and-impl(this, other):
    return <init>(and(<ULong__<get-data>-impl>(other)))

def ULong__or-impl(this, other):
    return <init>(or(<ULong__<get-data>-impl>(other)))

def ULong__xor-impl(this, other):
    return <init>(xor(<ULong__<get-data>-impl>(other)))

def ULong__inv-impl(this):
    return <init>(inv())

def ULong__toByte-impl(this):
    return toByte()

def ULong__toShort-impl(this):
    return toShort()

def ULong__toInt-impl(this):
    return toInt()

def ULong__toLong-impl(this):
    return <ULong__<get-data>-impl>(this)

def ULong__toUByte-impl(this):
    tmp0_toUByte_0 = <ULong__<get-data>-impl>(this)
    return <init>(toByte())

def ULong__toUShort-impl(this):
    tmp0_toUShort_0 = <ULong__<get-data>-impl>(this)
    return <init>(toShort())

def ULong__toUInt-impl(this):
    tmp0_toUInt_0 = <ULong__<get-data>-impl>(this)
    return <init>(toInt())

def ULong__toULong-impl(this):
    return this

def ULong__toFloat-impl(this):
    return kotlin.Float(ulongToDouble(<ULong__<get-data>-impl>(this)))

def ULong__toDouble-impl(this):
    return ulongToDouble(<ULong__<get-data>-impl>(this))

def ULong__toString-impl(this):
    return ulongToString(<ULong__<get-data>-impl>(this))

def ULong__hashCode-impl(this):
    return hashCode()

def ULong__equals-impl(this, other):
    if jsNot(jsInstanceOf(other, jsClass())):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@7a0f1f9d
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@462d4f3c:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@5002aa66
    
    tmp0_other_with_cast = visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@17b41d39
    if jsNot(equals(data)):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@d98ce13
    
    return visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@4865434e

class ULong:
    pass

def toULong():
    return <init>(<this>)

def toULong():
    return <init>(toLong(<this>))

def toULong():
    return doubleToULong(<this>)

def toULong():
    return doubleToULong(kotlin.Double(<this>))

def toULong():
    return <init>(toLong(<this>))

def toULong():
    return <init>(toLong(<this>))

def <get-array>($this):
    return array

def <set-index>($this, <set-?>):
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@4d437408

def <get-index>($this):
    return index

def <ULongArray__<get-storage>-impl>(this):
    return storage

def <ULongArray__<init>-impl>(size):
    tmp = <init>(longArray(size))
    return tmp

def ULongArray__get-impl(this, index):
    tmp0_toULong_0 = jsArrayGet(<ULongArray__<get-storage>-impl>(this), index)
    return <init>(tmp0_toULong_0)

def ULongArray__set-impl(this, index, value):
    tmp = <ULongArray__<get-storage>-impl>(this)
    jsArraySet(tmp, index, <ULong__<get-data>-impl>(value))

def <ULongArray__<get-size>-impl>(this):
    return jsArrayLength(<ULongArray__<get-storage>-impl>(this))

def ULongArray__iterator-impl(this):
    return <init>(<ULongArray__<get-storage>-impl>(this))

class Iterator:
    pass

def ULongArray__contains-impl(this, element):
    tmp = visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@3a23241e
    if jsNot(jsInstanceOf(tmp, jsClass())):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@64641998
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@18cf55df:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@3c193a5a
    
    tmp = <ULongArray__<get-storage>-impl>(this)
    return contains(<ULong__<get-data>-impl>(element))

def ULongArray__contains-impl(this, element):
    if jsNot(jsInstanceOf(element, jsClass())):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@7a5db772
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@4e41fbf5:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@59302368
    
    tmp = unboxIntrinsic(this)
    return ULongArray__contains-impl(tmp, visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@6dceb58c)

def ULongArray__containsAll-impl(this, elements):
    tmp$ret$0
    visitDoWhileLoop org.jetbrains.kotlin.ir.expressions.impl.IrDoWhileLoopImpl@d57624a
    return tmp$ret$0

def ULongArray__containsAll-impl(this, elements):
    return ULongArray__containsAll-impl(unboxIntrinsic(this), elements)

def ULongArray__isEmpty-impl(this):
    return jsEqeqeq(jsArrayLength(<ULongArray__<get-storage>-impl>(this)), 0)

def ULongArray__toString-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrStringConcatenationImpl@50bdd956

def ULongArray__hashCode-impl(this):
    return hashCode(storage)

def ULongArray__equals-impl(this, other):
    if jsNot(jsInstanceOf(other, jsClass())):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@f776b4a
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@8d902f:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@6414b660
    
    tmp0_other_with_cast = visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@62144e81
    if jsNot(equals(storage, storage)):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@7ab8f93
    
    return visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@14c7ab73

class ULongArray:
    pass

class Companion:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@2f73cc9d
def Companion_getInstance():
    if jsEqeq(Companion_instance, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@6614987b):
        <init>()
    
    return Companion_instance

class ULongRange:
    pass

class Companion:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@25af5c7f
def Companion_getInstance():
    if jsEqeq(Companion_instance, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@58d5bdb0):
        <init>()
    
    return Companion_instance

class ULongProgression:
    pass

def <get-finalElement>($this):
    return finalElement

def <set-hasNext>($this, <set-?>):
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@6f1c9f54

def <get-hasNext>($this):
    return hasNext

def <get-step>($this):
    return step

def <set-next>($this, <set-?>):
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@372f005a

def <get-next>($this):
    return next

class ULongProgressionIterator:
    pass

def getProgressionLastElement(start, end, step):
    tmp
    if jsGt(step, 0):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@6a474e00
    
    if jsLt(step, 0):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@11620d7b
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@2ac00dc9:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@12fb67f6
    
    return tmp

def getProgressionLastElement(start, end, step):
    tmp
    if jsGt(compareTo(<init>(0, 0)), 0):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@286dba42
    
    if jsLt(compareTo(<init>(0, 0)), 0):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@7fafb60
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@40e41f88:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@76b24f7b
    
    return tmp

def differenceModulo(a, b, c):
    ac = uintRemainder(a, c)
    bc = uintRemainder(b, c)
    tmp
    if jsGtEq(uintCompare(<UInt__<get-data>-impl>(ac), <UInt__<get-data>-impl>(bc)), 0):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@43addda0
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@630a32f8:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@5344604d
    
    return tmp

def differenceModulo(a, b, c):
    ac = ulongRemainder(a, c)
    bc = ulongRemainder(b, c)
    tmp
    if jsGtEq(ulongCompare(<ULong__<get-data>-impl>(ac), <ULong__<get-data>-impl>(bc)), 0):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@429a6f95
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@7fad58f8:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@4939730c
    
    return tmp

def <UShort__<get-data>-impl>(this):
    return data

class Companion:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@5938d600
def Companion_getInstance():
    if jsEqeq(Companion_instance, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@5a6e1f51):
        <init>()
    
    return Companion_instance

def UShort__compareTo-impl(this, other):
    tmp = jsBitAnd(kotlin.Int(<UShort__<get-data>-impl>(this)), 65535)
    return compareTo(tmp, jsBitAnd(kotlin.Int(<UByte__<get-data>-impl>(other)), 255))

def UShort__compareTo-impl(this, other):
    tmp = jsBitAnd(kotlin.Int(<UShort__<get-data>-impl>(this)), 65535)
    return compareTo(tmp, jsBitAnd(kotlin.Int(<UShort__<get-data>-impl>(other)), 65535))

def UShort__compareTo-impl(this, other):
    tmp = unboxIntrinsic(this)
    return UShort__compareTo-impl(tmp, visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@48d60abd)

def UShort__compareTo-impl(this, other):
    tmp0_compareTo_0 = <init>(jsBitAnd(kotlin.Int(<UShort__<get-data>-impl>(this)), 65535))
    return uintCompare(<UInt__<get-data>-impl>(tmp0_compareTo_0), <UInt__<get-data>-impl>(other))

def UShort__compareTo-impl(this, other):
    tmp0_compareTo_0 = <init>(and(<init>(65535, 0)))
    return ulongCompare(<ULong__<get-data>-impl>(tmp0_compareTo_0), <ULong__<get-data>-impl>(other))

def UShort__plus-impl(this, other):
    tmp0_plus_0 = <init>(jsBitAnd(kotlin.Int(<UShort__<get-data>-impl>(this)), 65535))
    tmp1_plus_0 = <init>(jsBitAnd(kotlin.Int(<UByte__<get-data>-impl>(other)), 255))
    return <init>(jsBitOr(jsPlus(<UInt__<get-data>-impl>(tmp0_plus_0), <UInt__<get-data>-impl>(tmp1_plus_0)), 0))

def UShort__plus-impl(this, other):
    tmp0_plus_0 = <init>(jsBitAnd(kotlin.Int(<UShort__<get-data>-impl>(this)), 65535))
    tmp1_plus_0 = <init>(jsBitAnd(kotlin.Int(<UShort__<get-data>-impl>(other)), 65535))
    return <init>(jsBitOr(jsPlus(<UInt__<get-data>-impl>(tmp0_plus_0), <UInt__<get-data>-impl>(tmp1_plus_0)), 0))

def UShort__plus-impl(this, other):
    tmp0_plus_0 = <init>(jsBitAnd(kotlin.Int(<UShort__<get-data>-impl>(this)), 65535))
    return <init>(jsBitOr(jsPlus(<UInt__<get-data>-impl>(tmp0_plus_0), <UInt__<get-data>-impl>(other)), 0))

def UShort__plus-impl(this, other):
    tmp0_plus_0 = <init>(and(<init>(65535, 0)))
    return <init>(plus(<ULong__<get-data>-impl>(other)))

def UShort__minus-impl(this, other):
    tmp0_minus_0 = <init>(jsBitAnd(kotlin.Int(<UShort__<get-data>-impl>(this)), 65535))
    tmp1_minus_0 = <init>(jsBitAnd(kotlin.Int(<UByte__<get-data>-impl>(other)), 255))
    return <init>(jsBitOr(jsMinus(<UInt__<get-data>-impl>(tmp0_minus_0), <UInt__<get-data>-impl>(tmp1_minus_0)), 0))

def UShort__minus-impl(this, other):
    tmp0_minus_0 = <init>(jsBitAnd(kotlin.Int(<UShort__<get-data>-impl>(this)), 65535))
    tmp1_minus_0 = <init>(jsBitAnd(kotlin.Int(<UShort__<get-data>-impl>(other)), 65535))
    return <init>(jsBitOr(jsMinus(<UInt__<get-data>-impl>(tmp0_minus_0), <UInt__<get-data>-impl>(tmp1_minus_0)), 0))

def UShort__minus-impl(this, other):
    tmp0_minus_0 = <init>(jsBitAnd(kotlin.Int(<UShort__<get-data>-impl>(this)), 65535))
    return <init>(jsBitOr(jsMinus(<UInt__<get-data>-impl>(tmp0_minus_0), <UInt__<get-data>-impl>(other)), 0))

def UShort__minus-impl(this, other):
    tmp0_minus_0 = <init>(and(<init>(65535, 0)))
    return <init>(minus(<ULong__<get-data>-impl>(other)))

def UShort__times-impl(this, other):
    tmp0_times_0 = <init>(jsBitAnd(kotlin.Int(<UShort__<get-data>-impl>(this)), 65535))
    tmp1_times_0 = <init>(jsBitAnd(kotlin.Int(<UByte__<get-data>-impl>(other)), 255))
    return <init>(imul(<UInt__<get-data>-impl>(tmp0_times_0), <UInt__<get-data>-impl>(tmp1_times_0)))

def UShort__times-impl(this, other):
    tmp0_times_0 = <init>(jsBitAnd(kotlin.Int(<UShort__<get-data>-impl>(this)), 65535))
    tmp1_times_0 = <init>(jsBitAnd(kotlin.Int(<UShort__<get-data>-impl>(other)), 65535))
    return <init>(imul(<UInt__<get-data>-impl>(tmp0_times_0), <UInt__<get-data>-impl>(tmp1_times_0)))

def UShort__times-impl(this, other):
    tmp0_times_0 = <init>(jsBitAnd(kotlin.Int(<UShort__<get-data>-impl>(this)), 65535))
    return <init>(imul(<UInt__<get-data>-impl>(tmp0_times_0), <UInt__<get-data>-impl>(other)))

def UShort__times-impl(this, other):
    tmp0_times_0 = <init>(and(<init>(65535, 0)))
    return <init>(times(<ULong__<get-data>-impl>(other)))

def UShort__div-impl(this, other):
    tmp0_div_0 = <init>(jsBitAnd(kotlin.Int(<UShort__<get-data>-impl>(this)), 65535))
    tmp1_div_0 = <init>(jsBitAnd(kotlin.Int(<UByte__<get-data>-impl>(other)), 255))
    return uintDivide(tmp0_div_0, tmp1_div_0)

def UShort__div-impl(this, other):
    tmp0_div_0 = <init>(jsBitAnd(kotlin.Int(<UShort__<get-data>-impl>(this)), 65535))
    tmp1_div_0 = <init>(jsBitAnd(kotlin.Int(<UShort__<get-data>-impl>(other)), 65535))
    return uintDivide(tmp0_div_0, tmp1_div_0)

def UShort__div-impl(this, other):
    tmp0_div_0 = <init>(jsBitAnd(kotlin.Int(<UShort__<get-data>-impl>(this)), 65535))
    return uintDivide(tmp0_div_0, other)

def UShort__div-impl(this, other):
    tmp0_div_0 = <init>(and(<init>(65535, 0)))
    return ulongDivide(tmp0_div_0, other)

def UShort__rem-impl(this, other):
    tmp0_rem_0 = <init>(jsBitAnd(kotlin.Int(<UShort__<get-data>-impl>(this)), 65535))
    tmp1_rem_0 = <init>(jsBitAnd(kotlin.Int(<UByte__<get-data>-impl>(other)), 255))
    return uintRemainder(tmp0_rem_0, tmp1_rem_0)

def UShort__rem-impl(this, other):
    tmp0_rem_0 = <init>(jsBitAnd(kotlin.Int(<UShort__<get-data>-impl>(this)), 65535))
    tmp1_rem_0 = <init>(jsBitAnd(kotlin.Int(<UShort__<get-data>-impl>(other)), 65535))
    return uintRemainder(tmp0_rem_0, tmp1_rem_0)

def UShort__rem-impl(this, other):
    tmp0_rem_0 = <init>(jsBitAnd(kotlin.Int(<UShort__<get-data>-impl>(this)), 65535))
    return uintRemainder(tmp0_rem_0, other)

def UShort__rem-impl(this, other):
    tmp0_rem_0 = <init>(and(<init>(65535, 0)))
    return ulongRemainder(tmp0_rem_0, other)

def UShort__inc-impl(this):
    return <init>(numberToShort(jsPlus(<UShort__<get-data>-impl>(this), 1)))

def UShort__dec-impl(this):
    return <init>(numberToShort(jsMinus(<UShort__<get-data>-impl>(this), 1)))

def UShort__rangeTo-impl(this, other):
    tmp = <init>(jsBitAnd(kotlin.Int(<UShort__<get-data>-impl>(this)), 65535))
    return <init>(tmp, <init>(jsBitAnd(kotlin.Int(<UShort__<get-data>-impl>(other)), 65535)))

def UShort__and-impl(this, other):
    tmp0_and_0 = <UShort__<get-data>-impl>(this)
    tmp1_and_0 = <UShort__<get-data>-impl>(other)
    return <init>(toShort(jsBitAnd(kotlin.Int(tmp0_and_0), kotlin.Int(tmp1_and_0))))

def UShort__or-impl(this, other):
    tmp0_or_0 = <UShort__<get-data>-impl>(this)
    tmp1_or_0 = <UShort__<get-data>-impl>(other)
    return <init>(toShort(jsBitOr(kotlin.Int(tmp0_or_0), kotlin.Int(tmp1_or_0))))

def UShort__xor-impl(this, other):
    tmp0_xor_0 = <UShort__<get-data>-impl>(this)
    tmp1_xor_0 = <UShort__<get-data>-impl>(other)
    return <init>(toShort(jsBitXor(kotlin.Int(tmp0_xor_0), kotlin.Int(tmp1_xor_0))))

def UShort__inv-impl(this):
    tmp0_inv_0 = <UShort__<get-data>-impl>(this)
    return <init>(toShort(jsBitNot(kotlin.Int(tmp0_inv_0))))

def UShort__toByte-impl(this):
    return toByte(<UShort__<get-data>-impl>(this))

def UShort__toShort-impl(this):
    return <UShort__<get-data>-impl>(this)

def UShort__toInt-impl(this):
    return jsBitAnd(kotlin.Int(<UShort__<get-data>-impl>(this)), 65535)

def UShort__toLong-impl(this):
    return and(<init>(65535, 0))

def UShort__toUByte-impl(this):
    tmp0_toUByte_0 = <UShort__<get-data>-impl>(this)
    return <init>(toByte(tmp0_toUByte_0))

def UShort__toUShort-impl(this):
    return this

def UShort__toUInt-impl(this):
    return <init>(jsBitAnd(kotlin.Int(<UShort__<get-data>-impl>(this)), 65535))

def UShort__toULong-impl(this):
    return <init>(and(<init>(65535, 0)))

def UShort__toFloat-impl(this):
    return kotlin.Float(jsBitAnd(kotlin.Int(<UShort__<get-data>-impl>(this)), 65535))

def UShort__toDouble-impl(this):
    return kotlin.Double(jsBitAnd(kotlin.Int(<UShort__<get-data>-impl>(this)), 65535))

def UShort__toString-impl(this):
    return toString()

def UShort__hashCode-impl(this):
    return data

def UShort__equals-impl(this, other):
    if jsNot(jsInstanceOf(other, jsClass())):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@6015c745
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@71e55649:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@3810e141
    
    tmp0_other_with_cast = visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@65eb16f7
    if jsNot(jsEqeqeq(data, data)):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@776b7fa2
    
    return visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@2403c1c5

class UShort:
    pass

def toUShort():
    return <init>(toShort(<this>))

def toUShort():
    return <init>(toShort())

def toUShort():
    return <init>(<this>)

def <get-array>($this):
    return array

def <set-index>($this, <set-?>):
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@342b545a

def <get-index>($this):
    return index

def <UShortArray__<get-storage>-impl>(this):
    return storage

def <UShortArray__<init>-impl>(size):
    tmp = <init>(int16Array(size))
    return tmp

def UShortArray__get-impl(this, index):
    tmp0_toUShort_0 = jsArrayGet(<UShortArray__<get-storage>-impl>(this), index)
    return <init>(tmp0_toUShort_0)

def UShortArray__set-impl(this, index, value):
    tmp = <UShortArray__<get-storage>-impl>(this)
    jsArraySet(tmp, index, <UShort__<get-data>-impl>(value))

def <UShortArray__<get-size>-impl>(this):
    return jsArrayLength(<UShortArray__<get-storage>-impl>(this))

def UShortArray__iterator-impl(this):
    return <init>(<UShortArray__<get-storage>-impl>(this))

class Iterator:
    pass

def UShortArray__contains-impl(this, element):
    tmp = visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@487969d
    if jsNot(jsInstanceOf(tmp, jsClass())):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@900ffc4
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@429691:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@af4d246
    
    tmp = <UShortArray__<get-storage>-impl>(this)
    return contains(<UShort__<get-data>-impl>(element))

def UShortArray__contains-impl(this, element):
    if jsNot(jsInstanceOf(element, jsClass())):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@4f724360
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@c546f73:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@51e044da
    
    tmp = unboxIntrinsic(this)
    return UShortArray__contains-impl(tmp, visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@76baeab)

def UShortArray__containsAll-impl(this, elements):
    tmp$ret$0
    visitDoWhileLoop org.jetbrains.kotlin.ir.expressions.impl.IrDoWhileLoopImpl@15cdc117
    return tmp$ret$0

def UShortArray__containsAll-impl(this, elements):
    return UShortArray__containsAll-impl(unboxIntrinsic(this), elements)

def UShortArray__isEmpty-impl(this):
    return jsEqeqeq(jsArrayLength(<UShortArray__<get-storage>-impl>(this)), 0)

def UShortArray__toString-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrStringConcatenationImpl@19ed6130

def UShortArray__hashCode-impl(this):
    return hashCode(storage)

def UShortArray__equals-impl(this, other):
    if jsNot(jsInstanceOf(other, jsClass())):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@19412eef
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@485aa0d9:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@79832158
    
    tmp0_other_with_cast = visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@5ca69552
    if jsNot(equals(storage, storage)):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@6bbff652
    
    return visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@45ea6c24

class UShortArray:
    pass

def uintCompare(v1, v2):
    return compareTo(jsBitXor(v1, MIN_VALUE), jsBitXor(v2, MIN_VALUE))

def uintDivide(v1, v2):
    tmp = and(<init>(-1, 0))
    tmp0_toUInt_0 = div(and(<init>(-1, 0)))
    return <init>(toInt())

def uintRemainder(v1, v2):
    tmp = and(<init>(-1, 0))
    tmp0_toUInt_0 = rem(and(<init>(-1, 0)))
    return <init>(toInt())

def uintToDouble(v):
    return jsPlus(kotlin.Double(jsBitAnd(v, MAX_VALUE)), jsMult(kotlin.Double(jsBitShiftL(jsBitShiftRU(v, 31), 30)), 2))

def ulongCompare(v1, v2):
    return compareTo(xor(<init>(0, -2147483648)))

def ulongDivide(v1, v2):
    dividend = <ULong__<get-data>-impl>(v1)
    divisor = <ULong__<get-data>-impl>(v2)
    if jsLt(compareTo(<init>(0, 0)), 0):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@67c912d3
    
    if jsGtEq(compareTo(<init>(0, 0)), 0):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@78c9c38a
    
    quotient = shl(1)
    rem = minus(times(divisor))
    tmp
    tmp0_compareTo_0 = <init>(rem)
    tmp1_compareTo_0 = <init>(divisor)
    if jsGtEq(ulongCompare(<ULong__<get-data>-impl>(tmp0_compareTo_0), <ULong__<get-data>-impl>(tmp1_compareTo_0)), 0):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@5e17bdb1
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@22bf3c03:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@41a6e7d0
    
    tmp2_plus_0 = tmp
    return <init>(plus(toLong(tmp2_plus_0)))

def ulongRemainder(v1, v2):
    dividend = <ULong__<get-data>-impl>(v1)
    divisor = <ULong__<get-data>-impl>(v2)
    if jsLt(compareTo(<init>(0, 0)), 0):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@3fe7c87c
    
    if jsGtEq(compareTo(<init>(0, 0)), 0):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@1899c7ae
    
    quotient = shl(1)
    rem = minus(times(divisor))
    tmp
    tmp0_compareTo_0 = <init>(rem)
    tmp1_compareTo_0 = <init>(divisor)
    if jsGtEq(ulongCompare(<ULong__<get-data>-impl>(tmp0_compareTo_0), <ULong__<get-data>-impl>(tmp1_compareTo_0)), 0):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@6b907f80
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@e93f8b4:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@6617fa99
    
    return <init>(minus(tmp))

def ulongToDouble(v):
    return jsPlus(jsMult(toDouble(), 2048), toDouble())

def ulongToString(v):
    return ulongToString(v, 10)

def ulongToString(v, base):
    if jsGtEq(compareTo(<init>(0, 0)), 0):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@42ceb67f
    
    tmp0_div_0 = ushr(1)
    quotient = shl(1)
    tmp1_times_0 = quotient
    rem = minus(times(toLong(base)))
    if jsGtEq(compareTo(toLong(base)), 0):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@f1d5f3
    
    return jsPlus(toString(base), toString(base))

def doubleToUInt(v):
    tmp
    if isNaN():
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@7b32e17b
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@79f40cc5:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@3cbc1752
    
    return tmp

def doubleToULong(v):
    tmp
    if isNaN():
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@7370c288
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@60b16a5b:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@6bb4568
    
    return tmp

class ExperimentalUnsignedTypes:
    pass

class Annotation:
    pass

class CharSequence:
    pass

class Comparable:
    pass

class Iterator:
    pass

class ListIterator:
    pass

class MutableIterator:
    pass

class MutableListIterator:
    pass

class Number:
    pass

class SinceKotlin:
    pass

class Suppress:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@44a99029
visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@215512b9
visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@4a47a1b5
def values():
    return arrayLiteral(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrVarargImpl@7f95dc2)

def valueOf(value):
    return visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@2cf4dd07

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@4718eb01
def DeprecationLevel_initEntries():
    if DeprecationLevel_entriesInitialized:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@1d0e0d0d
    
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@22336af7
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@108a411c
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@41e3d466
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@568bbbcd

class DeprecationLevel:
    pass

class PublishedApi:
    pass

class ParameterName:
    pass

def Deprecated_init_$Init$(message, replaceWith, level, $mask0, $marker, $this):
    if jsNot(jsEqeqeq(jsBitAnd($mask0, 2), 0)):
        visitSetValue-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrSetValueImpl@2472a75c
    
    if jsNot(jsEqeqeq(jsBitAnd($mask0, 4), 0)):
        visitSetValue-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrSetValueImpl@4e91272d
    
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@1efec9f3
    return $this

def Deprecated_init_$Create$(message, replaceWith, level, $mask0, $marker):
    return Deprecated_init_$Init$(message, replaceWith, level, $mask0, $marker, Object$create())

class Deprecated:
    pass

class ReplaceWith:
    pass

class ExtensionFunctionType:
    pass

class UnsafeVariance:
    pass

def DeprecationLevel_WARNING_getInstance():
    DeprecationLevel_initEntries()
    return DeprecationLevel_WARNING_instance

def DeprecationLevel_ERROR_getInstance():
    DeprecationLevel_initEntries()
    return DeprecationLevel_ERROR_instance

def DeprecationLevel_HIDDEN_getInstance():
    DeprecationLevel_initEntries()
    return DeprecationLevel_HIDDEN_instance

class ByteIterator:
    pass

class IntIterator:
    pass

class DoubleIterator:
    pass

class FloatIterator:
    pass

class LongIterator:
    pass

class CharIterator:
    pass

class BooleanIterator:
    pass

class ShortIterator:
    pass

def <get-finalElement>($this):
    return finalElement

def <set-hasNext>($this, <set-?>):
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@41143491

def <get-hasNext>($this):
    return hasNext

def <set-next>($this, <set-?>):
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@7516aa4

def <get-next>($this):
    return next

class IntProgressionIterator:
    pass

def <get-finalElement>($this):
    return finalElement

def <set-hasNext>($this, <set-?>):
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@321fc4c5

def <get-hasNext>($this):
    return hasNext

def <set-next>($this, <set-?>):
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@5ca3308c

def <get-next>($this):
    return next

class LongProgressionIterator:
    pass

def <get-finalElement>($this):
    return finalElement

def <set-hasNext>($this, <set-?>):
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@5cb20350

def <get-hasNext>($this):
    return hasNext

def <set-next>($this, <set-?>):
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@5046ad1c

def <get-next>($this):
    return next

class CharProgressionIterator:
    pass

class Companion:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@2c13db34
def Companion_getInstance():
    if jsEqeq(Companion_instance, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@55398902):
        <init>()
    
    return Companion_instance

class IntProgression:
    pass

class Companion:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@79bc0ceb
def Companion_getInstance():
    if jsEqeq(Companion_instance, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@129e23fc):
        <init>()
    
    return Companion_instance

class LongProgression:
    pass

class Companion:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@73858ba
def Companion_getInstance():
    if jsEqeq(Companion_instance, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@68b4e3a1):
        <init>()
    
    return Companion_instance

class CharProgression:
    pass

class ClosedRange:
    pass

class Companion:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@4679df4b
def Companion_getInstance():
    if jsEqeq(Companion_instance, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@5b96272e):
        <init>()
    
    return Companion_instance

class IntRange:
    pass

class Companion:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@60e4d95
def Companion_getInstance():
    if jsEqeq(Companion_instance, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@461b078f):
        <init>()
    
    return Companion_instance

class LongRange:
    pass

class Companion:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@5e2975ff
def Companion_getInstance():
    if jsEqeq(Companion_instance, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@3b48e216):
        <init>()
    
    return Companion_instance

class CharRange:
    pass

class Unit:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@2dac0733
def Unit_getInstance():
    if jsEqeq(Unit_instance, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@6b2f16b9):
        <init>()
    
    return Unit_instance

class Target:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@6bdd7fef
visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@58d9d844
visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@2c6e8eed
visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@6e094fb7
visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@6e2b679e
visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@78a689e7
visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@206769f8
visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@437eeb4
visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@31156e3b
visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@7d30304f
visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@6603aeb8
visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@5dfabe82
visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@470467b0
visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@3bca8557
visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@40478af8
def values():
    return arrayLiteral(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrVarargImpl@3f7f7faa)

def valueOf(value):
    return visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@5d6bbb25

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@4ca2c467
def AnnotationTarget_initEntries():
    if AnnotationTarget_entriesInitialized:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@6d0dd338
    
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@173e347f
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@7780a93c
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@2cb74f29
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@3ec06e6d
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@ec75805
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@4737a2d0
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@790d28a7
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@76ad04a1
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@16e73d83
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@442d90ba
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@607df2a0
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@515c6338
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@451029fa
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@e63a61d
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@310d8954
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@4a1d9141

class AnnotationTarget:
    pass

class MustBeDocumented:
    pass

def Retention_init_$Init$(value, $mask0, $marker, $this):
    if jsNot(jsEqeqeq(jsBitAnd($mask0, 1), 0)):
        visitSetValue-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrSetValueImpl@34392048
    
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@690e308c
    return $this

def Retention_init_$Create$(value, $mask0, $marker):
    return Retention_init_$Init$(value, $mask0, $marker, Object$create())

class Retention:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@48754a85
visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@5ceafd4b
visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@58942d7b
def values():
    return arrayLiteral(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrVarargImpl@4626eef0)

def valueOf(value):
    return visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@a3ed130

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@9febb7c
def AnnotationRetention_initEntries():
    if AnnotationRetention_entriesInitialized:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@70ebf6d8
    
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@74bbaa1b
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@74c82cca
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@3c29ef6e
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@6ad8f801

class AnnotationRetention:
    pass

class Repeatable:
    pass

def AnnotationTarget_CLASS_getInstance():
    AnnotationTarget_initEntries()
    return AnnotationTarget_CLASS_instance

def AnnotationTarget_ANNOTATION_CLASS_getInstance():
    AnnotationTarget_initEntries()
    return AnnotationTarget_ANNOTATION_CLASS_instance

def AnnotationTarget_TYPE_PARAMETER_getInstance():
    AnnotationTarget_initEntries()
    return AnnotationTarget_TYPE_PARAMETER_instance

def AnnotationTarget_PROPERTY_getInstance():
    AnnotationTarget_initEntries()
    return AnnotationTarget_PROPERTY_instance

def AnnotationTarget_FIELD_getInstance():
    AnnotationTarget_initEntries()
    return AnnotationTarget_FIELD_instance

def AnnotationTarget_LOCAL_VARIABLE_getInstance():
    AnnotationTarget_initEntries()
    return AnnotationTarget_LOCAL_VARIABLE_instance

def AnnotationTarget_VALUE_PARAMETER_getInstance():
    AnnotationTarget_initEntries()
    return AnnotationTarget_VALUE_PARAMETER_instance

def AnnotationTarget_CONSTRUCTOR_getInstance():
    AnnotationTarget_initEntries()
    return AnnotationTarget_CONSTRUCTOR_instance

def AnnotationTarget_FUNCTION_getInstance():
    AnnotationTarget_initEntries()
    return AnnotationTarget_FUNCTION_instance

def AnnotationTarget_PROPERTY_GETTER_getInstance():
    AnnotationTarget_initEntries()
    return AnnotationTarget_PROPERTY_GETTER_instance

def AnnotationTarget_PROPERTY_SETTER_getInstance():
    AnnotationTarget_initEntries()
    return AnnotationTarget_PROPERTY_SETTER_instance

def AnnotationTarget_TYPE_getInstance():
    AnnotationTarget_initEntries()
    return AnnotationTarget_TYPE_instance

def AnnotationTarget_EXPRESSION_getInstance():
    AnnotationTarget_initEntries()
    return AnnotationTarget_EXPRESSION_instance

def AnnotationTarget_FILE_getInstance():
    AnnotationTarget_initEntries()
    return AnnotationTarget_FILE_instance

def AnnotationTarget_TYPEALIAS_getInstance():
    AnnotationTarget_initEntries()
    return AnnotationTarget_TYPEALIAS_instance

def AnnotationRetention_SOURCE_getInstance():
    AnnotationRetention_initEntries()
    return AnnotationRetention_SOURCE_instance

def AnnotationRetention_BINARY_getInstance():
    AnnotationRetention_initEntries()
    return AnnotationRetention_BINARY_instance

def AnnotationRetention_RUNTIME_getInstance():
    AnnotationRetention_initEntries()
    return AnnotationRetention_RUNTIME_instance

def getProgressionLastElement(start, end, step):
    tmp
    if jsGt(step, 0):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@6cb62e90
    
    if jsLt(step, 0):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@5a23d4d8
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@efe75a2:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@e01664e
    
    return tmp

def getProgressionLastElement(start, end, step):
    tmp
    if jsGt(compareTo(<init>(0, 0)), 0):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@350e34e7
    
    if jsLt(compareTo(<init>(0, 0)), 0):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@213dd15d
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@297bbd41:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@2c526883
    
    return tmp

def differenceModulo(a, b, c):
    return mod(jsBitOr(jsMinus(mod(a, c), mod(b, c)), 0), c)

def differenceModulo(a, b, c):
    return mod(minus(mod(b, c)), c)

def mod(a, b):
    mod = jsMod(a, b)
    return visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@742c7d35

def mod(a, b):
    mod = rem(b)
    return visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@36f59005

class ByteCompanionObject:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@7e30dfa4
def ByteCompanionObject_getInstance():
    if jsEqeq(ByteCompanionObject_instance, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@46c805be):
        <init>()
    
    return ByteCompanionObject_instance

class ShortCompanionObject:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@551e9796
def ShortCompanionObject_getInstance():
    if jsEqeq(ShortCompanionObject_instance, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@287213ac):
        <init>()
    
    return ShortCompanionObject_instance

class IntCompanionObject:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@3b10c5d
def IntCompanionObject_getInstance():
    if jsEqeq(IntCompanionObject_instance, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@88d9da0):
        <init>()
    
    return IntCompanionObject_instance

class FloatCompanionObject:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@104305f
def FloatCompanionObject_getInstance():
    if jsEqeq(FloatCompanionObject_instance, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@38cac3f9):
        <init>()
    
    return FloatCompanionObject_instance

class DoubleCompanionObject:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@2e643cad
def DoubleCompanionObject_getInstance():
    if jsEqeq(DoubleCompanionObject_instance, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@281b0f38):
        <init>()
    
    return DoubleCompanionObject_instance

class StringCompanionObject:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@4e51a9f3
def StringCompanionObject_getInstance():
    if jsEqeq(StringCompanionObject_instance, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@605d67f8):
        <init>()
    
    return StringCompanionObject_instance

class BooleanCompanionObject:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@2cbad233
def BooleanCompanionObject_getInstance():
    if jsEqeq(BooleanCompanionObject_instance, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@34289e5f):
        <init>()
    
    return BooleanCompanionObject_instance

class Comparator:
    pass

class JsName:
    pass

def toTypedArray():
    return copyToArray(<this>)

def copyToArray(collection):
    tmp
    if visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@2474331d:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@1325a2ba
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@5b891149:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@49290bfb
    
    return tmp

def copyToArrayImpl(collection):
    array = kotlin.Array<kotlin.Any?>(js('[]'))
    iterator = iterator()
    while hasNext():
        visitExpression org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@27ae6f9e
    
    return array

def copyToArrayImpl(collection, array):
    if jsLt(jsArrayLength(array), <get-size>()):
        visitComposite-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrCompositeImpl@1cc552fe
    
    iterator = iterator()
    index = 0
    while hasNext():
        tmp0 = index
        index = jsBitOr(jsPlus(tmp0, 1), 0)
        tmp1_unsafeCast_0 = next()
        jsArraySet(array, tmp0, kotlin.Any?(tmp1_unsafeCast_0))
    
    if jsLt(index, jsArrayLength(array)):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@5fe7454c
    
    return array

class <no name provided>:
    pass

class <no name provided>:
    pass

class AbstractMutableCollection:
    pass

def <no name provided>$factory($elements):
    i = <init>($elements)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@7e860a11

def <no name provided>$factory($elements):
    i = <init>($elements)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@1eb2d718

def <get-list>($this):
    return list

def <get-fromIndex>($this):
    return fromIndex

def <set-_size>($this, <set-?>):
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@3d6aa682

def <get-_size>($this):
    return _size

class IteratorImpl:
    pass

class ListIteratorImpl:
    pass

class SubList:
    pass

class <no name provided>:
    pass

class <no name provided>:
    pass

class AbstractMutableList:
    pass

def <no name provided>$factory($elements):
    i = <init>($elements)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@4b5c0183

def <no name provided>$factory($elements):
    i = <init>($elements)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@7169c184

def <set-array>($this, <set-?>):
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@221ae367

def <get-array>($this):
    return array

def <set-isReadOnly>($this, <set-?>):
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@e0895b3

def <get-isReadOnly>($this):
    return isReadOnly

def ArrayList_init_$Init$($this):
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@18bbcce8
    return $this

def ArrayList_init_$Create$():
    return ArrayList_init_$Init$(Object$create())

def ArrayList_init_$Init$(initialCapacity, $this):
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@2858d667
    return $this

def ArrayList_init_$Create$(initialCapacity):
    return ArrayList_init_$Init$(initialCapacity, Object$create())

def ArrayList_init_$Init$(initialCapacity, $mask0, $marker, $this):
    if jsNot(jsEqeqeq(jsBitAnd($mask0, 1), 0)):
        visitSetValue-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrSetValueImpl@74d16083
    
    ArrayList_init_$Init$(initialCapacity, $this)
    return $this

def ArrayList_init_$Create$(initialCapacity, $mask0, $marker):
    return ArrayList_init_$Init$(initialCapacity, $mask0, $marker, Object$create())

def ArrayList_init_$Init$(elements, $this):
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@1f3241b3
    return $this

def ArrayList_init_$Create$(elements):
    return ArrayList_init_$Init$(elements, Object$create())

def rangeCheck($this, index):
    checkElementIndex(index, <get-size>())
    return index

def insertionRangeCheck($this, index):
    checkPositionIndex(index, <get-size>())
    return index

class ArrayList:
    pass

def <set-_stableSortingIsSupported>(<set-?>):
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@2a6dfbb2

def <get-_stableSortingIsSupported>():
    return _stableSortingIsSupported

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@165634aa
class RandomAccess:
    pass

def <set-output>(<set-?>):
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@2f6fcc70

def <get-output>():
    return output

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@20bc6f4d
class BaseOutput:
    pass

class NodeJsOutput:
    pass

class BufferedOutputToConsoleLog:
    pass

def String(value):
    return kotlin.String(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@6edd2ef4)

class BufferedOutput:
    pass

def println(message):
    println(message)

def output$init$():
    isNode_2 = kotlin.Boolean(js('typeof process !== 'undefined' && process.versions && !!process.versions.node'))
    return visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@50a59a0b

def <get-EmptyContinuation>():
    return EmptyContinuation

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@6c07666f
class <no name provided>_1:
    pass

def EmptyContinuation$init$():
    tmp0_Continuation_0 = EmptyCoroutineContext_getInstance()
    return <init>(tmp0_Continuation_0)

def asDynamic():
    return <this>

def unsafeCast():
    return T(<this>)

def unsafeCast():
    return T(<this>)

class Serializable:
    pass

def pow(n):
    return pow(<this>, kotlin.Double(n))

def isNaN():
    return jsNot(jsEqeqeq(<this>, <this>))

def <get-INV_2_26>():
    return INV_2_26

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@57ab7b32
def <get-INV_2_53>():
    return INV_2_53

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@1606ecbb
def INV_2_26$init$():
    tmp0_pow_0 = visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@5bb00dcc
    tmp1_pow_0 = -26
    return pow(tmp0_pow_0, kotlin.Double(tmp1_pow_0))

def INV_2_53$init$():
    tmp0_pow_0 = visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@55732ae6
    tmp1_pow_0 = -53
    return pow(tmp0_pow_0, kotlin.Double(tmp1_pow_0))

def <get-js>():
    return <get-jClass>()

class KCallable:
    pass

class KClass:
    pass

class KClassImpl:
    pass

def <get-givenSimpleName>($this):
    return givenSimpleName

def <get-isInstanceFunction>($this):
    return isInstanceFunction

class PrimitiveKClassImpl:
    pass

class NothingKClassImpl:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@5e9feddd
def NothingKClassImpl_getInstance():
    if jsEqeq(NothingKClassImpl_instance, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@1bad6995):
        <init>()
    
    return NothingKClassImpl_instance

class ErrorKClass:
    pass

class SimpleKClassImpl:
    pass

class KFunction:
    pass

class KProperty:
    pass

class KProperty0:
    pass

class KProperty1:
    pass

class KProperty2:
    pass

class KMutableProperty0:
    pass

class KMutableProperty:
    pass

class KMutableProperty1:
    pass

class KMutableProperty2:
    pass

class KType:
    pass

def createKType(classifier, arguments, isMarkedNullable):
    return <init>(classifier, asList(), isMarkedNullable)

def createDynamicKType():
    return DynamicKType_getInstance()

def createKTypeParameter(name, upperBounds, variance):
    tmp0_subject = variance
    kVariance = visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@363f986e
    return <init>(name, asList(), kVariance, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@3fc2197d)

def getStarKTypeProjection():
    return <get-STAR>()

def createCovariantKTypeProjection(type):
    return covariant(type)

def createInvariantKTypeProjection(type):
    return invariant(type)

def createContravariantKTypeProjection(type):
    return contravariant(type)

def asString($this):
    if jsEqeq(variance, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@7879e3ac):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@4b288c86
    
    return jsPlus(prefixString(), toString())

class <no name provided>:
    pass

class KTypeImpl:
    pass

def prefixString():
    tmp0_subject = <this>
    tmp
    if equals(KVariance_INVARIANT_getInstance()):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@293b7870
    
    if equals(KVariance_IN_getInstance()):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@4e7b9365
    
    if equals(KVariance_OUT_getInstance()):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@1bf22938
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@70f5f6c7:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@25639962
    
    return tmp

class DynamicKType:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@476fb241
def DynamicKType_getInstance():
    if jsEqeq(DynamicKType_instance, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@6270fadb):
        <init>()
    
    return DynamicKType_instance

def <no name provided>$factory(this$0):
    i = <init>(this$0)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@6ff36ec8

class KTypeParameterImpl:
    pass

def <get-functionClasses>():
    return functionClasses

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@70a9f4b7
class <no name provided>:
    pass

class <no name provided>:
    pass

class <no name provided>:
    pass

class <no name provided>:
    pass

class <no name provided>:
    pass

class <no name provided>:
    pass

class <no name provided>:
    pass

class <no name provided>:
    pass

class <no name provided>:
    pass

class <no name provided>:
    pass

class <no name provided>:
    pass

class <no name provided>:
    pass

class <no name provided>:
    pass

class <no name provided>:
    pass

class <no name provided>:
    pass

class <no name provided>:
    pass

class <no name provided>:
    pass

class <no name provided>:
    pass

class <no name provided>:
    pass

class <no name provided>:
    pass

class PrimitiveClasses:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@467c9ad9
def PrimitiveClasses_getInstance():
    if jsEqeq(PrimitiveClasses_instance, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@79703b86):
        <init>()
    
    return PrimitiveClasses_instance

def <no name provided>$factory():
    i = <init>()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@11ec85a0

def <no name provided>$factory():
    i = <init>()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@2c69eec5

def <no name provided>$factory():
    i = <init>()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@24766217

def <no name provided>$factory():
    i = <init>()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@669cb3c7

def <no name provided>$factory():
    i = <init>()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@3411ba50

def <no name provided>$factory():
    i = <init>()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@39c65ffc

def <no name provided>$factory():
    i = <init>()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@5916507e

def <no name provided>$factory():
    i = <init>()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@4d583069

def <no name provided>$factory():
    i = <init>()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@26bc84dc

def <no name provided>$factory():
    i = <init>()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@7c26f301

def <no name provided>$factory():
    i = <init>()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@291be813

def <no name provided>$factory():
    i = <init>()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@5961a37e

def <no name provided>$factory():
    i = <init>()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@7124d407

def <no name provided>$factory():
    i = <init>()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@153daff

def <no name provided>$factory():
    i = <init>()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@28af99b4

def <no name provided>$factory():
    i = <init>()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@27937c21

def <no name provided>$factory():
    i = <init>()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@587efefa

def <no name provided>$factory():
    i = <init>()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@1b5b5ac9

def <no name provided>$factory():
    i = <init>()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@77025469

def <no name provided>$factory($arity):
    i = <init>($arity)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@6c882cb4

def functionClasses$init$():
    tmp0_arrayOfNulls_0 = 0
    return fillArrayVal(Array(tmp0_arrayOfNulls_0), visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@20de2518)

def getKClass(jClass):
    tmp
    if kotlin.Boolean(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@4398d):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@1e06006f
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@722a2ba2:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@47884230
    
    return tmp

def getKClassM(jClasses):
    tmp0_subject = jsArrayLength(jClasses)
    tmp
    if jsEqeqeq(tmp0_subject, 1):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@73f9b9a
    
    if jsEqeqeq(tmp0_subject, 0):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@77544d06
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@31eb5ed6:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@4f920265
    
    return tmp

def getKClass1(jClass):
    if jsEqeqeq(jClass, js('String')):
        visitComposite-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrCompositeImpl@2103697b
    
    metadata = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicMemberExpressionImpl@32b273c1
    tmp
    if visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@5b810b54:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@15a4e7d8
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@73ffe7b0:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@5d71baf8
    
    return tmp

def getKClassFromExpression(e):
    tmp0_subject = jsTypeOf(e)
    tmp
    if jsEqeqeq(tmp0_subject, 'string'):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@4e5dd9b
    
    if jsEqeqeq(tmp0_subject, 'number'):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@54c659a1
    
    if jsEqeqeq(tmp0_subject, 'boolean'):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@c77f6b0
    
    if jsEqeqeq(tmp0_subject, 'function'):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@460e1763
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@24a024c8:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@4436b8b
    
    tmp1_unsafeCast_0 = tmp
    return kotlin.Any?(tmp1_unsafeCast_0)

class Appendable:
    pass

def StringBuilder_init_$Init$(capacity, $this):
    StringBuilder_init_$Init$($this)
    return $this

def StringBuilder_init_$Create$(capacity):
    return StringBuilder_init_$Init$(capacity, Object$create())

def StringBuilder_init_$Init$(content, $this):
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@f625021
    return $this

def StringBuilder_init_$Create$(content):
    return StringBuilder_init_$Init$(content, Object$create())

def StringBuilder_init_$Init$($this):
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@6f99ed9f
    return $this

def StringBuilder_init_$Create$():
    return StringBuilder_init_$Init$(Object$create())

def <set-string>($this, <set-?>):
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@6546c39

def <get-string>($this):
    return string

def checkReplaceRange($this, startIndex, endIndex, length):
    if visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@22249b41:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@356feae3
    
    if jsGt(startIndex, endIndex):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@5f3e12fc
    

class StringBuilder:
    pass

def isLowSurrogate():
    containsLower = <init>(56320)
    return visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@de7336d

def isHighSurrogate():
    containsLower = <init>(55296)
    return visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@66f39429

def checkRadix(radix):
    if jsNot(visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@1612fdb6):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@6924ff83
    
    return radix

def <get-STRING_CASE_INSENSITIVE_ORDER>():
    return STRING_CASE_INSENSITIVE_ORDER

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@3cc148d
def nativeLastIndexOf(str, fromIndex):
    return kotlin.Int(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@2c895dff)

def substring(startIndex, endIndex):
    return kotlin.String(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@70224e31)

def substring(startIndex):
    return kotlin.String(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@26fd9642)

def compareTo(other, ignoreCase):
    if ignoreCase:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@27bde886
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@26a2106e:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@2c75b0c8
    

def compareTo$default(other, ignoreCase, $mask0, $handler):
    if jsNot(jsEqeqeq(jsBitAnd($mask0, 2), 0)):
        visitSetValue-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrSetValueImpl@a891214
    
    return compareTo(other, ignoreCase)

def toUpperCase():
    return kotlin.String(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@7ef93968)

def toLowerCase():
    return kotlin.String(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@69dc42f2)

def concatToString():
    result = ''
    indexedObject = <this>
    inductionVariable = 0
    last = jsArrayLength(indexedObject)
    while jsLt(inductionVariable, last):
        char = jsArrayGet(indexedObject, inductionVariable)
        inductionVariable = jsBitOr(jsPlus(inductionVariable, 1), 0)
        result = jsPlus(result, char)
    
    return result

def concatToString(startIndex, endIndex):
    checkBoundsIndexes(startIndex, endIndex, jsArrayLength(<this>))
    result = ''
    inductionVariable = startIndex
    if jsLt(inductionVariable, endIndex):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDoWhileLoopImpl@538e1baa
    
    return result

def concatToString$default(startIndex, endIndex, $mask0, $handler):
    if jsNot(jsEqeqeq(jsBitAnd($mask0, 1), 0)):
        visitSetValue-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrSetValueImpl@300f34aa
    
    if jsNot(jsEqeqeq(jsBitAnd($mask0, 2), 0)):
        visitSetValue-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrSetValueImpl@10db9c65
    
    return concatToString(startIndex, endIndex)

class sam$kotlin_Comparator$0:
    pass

class <no name provided>:
    pass

def <no name provided>$factory():
    i = <init>()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@da3cab

def STRING_CASE_INSENSITIVE_ORDER$init$():
    tmp = <no name provided>$factory()
    return <init>(tmp)

def <get-REPLACEMENT_BYTE_SEQUENCE>():
    return REPLACEMENT_BYTE_SEQUENCE

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@79927a7c
def REPLACEMENT_BYTE_SEQUENCE$init$():
    tmp0_byteArrayOf_0 = int8ArrayOf(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrVarargImpl@3d29a22d)
    return tmp0_byteArrayOf_0

def <get-value>($this):
    return value

class Companion:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@d57ba2a
def Companion_getInstance():
    if jsEqeq(Companion_instance, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@48b5a380):
        <init>()
    
    return Companion_instance

class Char:
    pass

class Iterable:
    pass

class Collection:
    pass

class List:
    pass

class MutableList:
    pass

class MutableCollection:
    pass

class MutableIterable:
    pass

class Set:
    pass

class Entry:
    pass

class Map:
    pass

class MutableSet:
    pass

class MutableEntry:
    pass

class MutableMap:
    pass

class Companion:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@1cbfca27
def Companion_getInstance():
    if jsEqeq(Companion_instance, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@258cb16c):
        <init>()
    
    return Companion_instance

class Enum:
    pass

def byteArrayOf(elements):
    return elements

def arrayOf(elements):
    return kotlin.Any?(elements)

def toString():
    tmp0_safe_receiver = <this>
    tmp1_elvis_lhs = visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@354d078f
    return visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@fd01dc5

def plus(other):
    tmp2_safe_receiver = <this>
    tmp3_elvis_lhs = visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@3d98f7fc
    tmp = visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@3782d1e6
    tmp0_safe_receiver = other
    tmp1_elvis_lhs = visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@709bb6a6
    return jsPlus(tmp, visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@300f2857)

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

class DefaultConstructorMarker:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@6fee485b
def DefaultConstructorMarker_getInstance():
    if jsEqeq(DefaultConstructorMarker_instance, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@89d4a1a):
        <init>()
    
    return DefaultConstructorMarker_instance

def fillArrayVal(array, initValue):
    inductionVariable = 0
    last = jsBitOr(jsMinus(jsArrayLength(array), 1), 0)
    if jsLtEq(inductionVariable, last):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDoWhileLoopImpl@513b730
    
    return array

def arrayWithFun(size, init):
    tmp0_fillArrayFun_0 = Array(size)
    result_1 = kotlin.Any?(tmp0_fillArrayFun_0)
    i_2 = 0
    while jsNot(jsEqeqeq(i_2, jsArrayLength(result_1))):
        jsArraySet(result_1, i_2, invoke(i_2))
        i_2 = jsBitOr(jsPlus(i_2, 1), 0)
        Unit_getInstance()
    
    return result_1

def fillArrayFun(array, init):
    result = kotlin.Any?(array)
    i = 0
    while jsNot(jsEqeqeq(i, jsArrayLength(result))):
        jsArraySet(result, i, invoke(i))
        i = jsBitOr(jsPlus(i, 1), 0)
        Unit_getInstance()
    
    return result

def arrayIterator(array):
    return <init>(array)

def booleanArrayIterator(array):
    return <init>(array)

def charArrayIterator(array):
    return <init>(array)

def byteArrayIterator(array):
    return <init>(array)

def shortArrayIterator(array):
    return <init>(array)

def intArrayIterator(array):
    return <init>(array)

def floatArrayIterator(array):
    return <init>(array)

def longArrayIterator(array):
    return <init>(array)

def doubleArrayIterator(array):
    return <init>(array)

def booleanArray(size):
    tmp0_withType_0 = 'BooleanArray'
    tmp1_withType_0 = fillArrayVal(Array(size), visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@319fe034)
    visitExpression org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@34b2a6f4
    tmp2_unsafeCast_0 = tmp1_withType_0
    return kotlin.Any?(tmp2_unsafeCast_0)

def charArray(size):
    tmp0_withType_0 = 'CharArray'
    tmp1_withType_0 = fillArrayVal(Array(size), <init>(0))
    visitExpression org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@263ac7
    tmp2_unsafeCast_0 = tmp1_withType_0
    return kotlin.Any?(tmp2_unsafeCast_0)

def longArray(size):
    tmp0_withType_0 = 'LongArray'
    tmp1_withType_0 = fillArrayVal(Array(size), <init>(0, 0))
    visitExpression org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@5138d63a
    tmp2_unsafeCast_0 = tmp1_withType_0
    return kotlin.Any?(tmp2_unsafeCast_0)

def booleanArrayOf(arr):
    tmp0_withType_0 = 'BooleanArray'
    tmp1_withType_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@50ca509b
    visitExpression org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@45af5362
    tmp2_unsafeCast_0 = tmp1_withType_0
    return kotlin.Any?(tmp2_unsafeCast_0)

def charArrayOf(arr):
    tmp0_withType_0 = 'CharArray'
    tmp1_withType_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@3e6f3ad5
    visitExpression org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@1e832e79
    tmp2_unsafeCast_0 = tmp1_withType_0
    return kotlin.Any?(tmp2_unsafeCast_0)

def longArrayOf(arr):
    tmp0_withType_0 = 'LongArray'
    tmp1_withType_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@597050fa
    visitExpression org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@26d49375
    tmp2_unsafeCast_0 = tmp1_withType_0
    return kotlin.Any?(tmp2_unsafeCast_0)

class <no name provided>:
    pass

class <no name provided>:
    pass

class <no name provided>:
    pass

class <no name provided>:
    pass

class <no name provided>:
    pass

class <no name provided>:
    pass

class <no name provided>:
    pass

class <no name provided>:
    pass

class <no name provided>:
    pass

def <get-buf>():
    return buf

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@36dd68f1
def <get-bufFloat64>():
    return bufFloat64

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@45b244c4
def <get-bufFloat32>():
    return bufFloat32

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@297840d7
def <get-bufInt32>():
    return bufInt32

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@fcecc45
def <get-lowIndex>():
    return lowIndex

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@77199818
def <get-highIndex>():
    return highIndex

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@308bd473
def getNumberHashCode(obj):
    tmp0_unsafeCast_0 = jsBitwiseOr(obj, 0)
    if jsEqeqeq(kotlin.Any?(tmp0_unsafeCast_0), obj):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@79e2aa2d
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@505806c8:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@6d237951
    
    jsArraySet(bufFloat64, 0, obj)
    return jsBitOr(jsPlus(imul(jsArrayGet(bufInt32, highIndex), 31), jsArrayGet(bufInt32, lowIndex)), 0)

def bufFloat64$init$():
    tmp0_unsafeCast_0 = <init>(buf)
    return kotlin.Any?(tmp0_unsafeCast_0)

def bufFloat32$init$():
    tmp0_unsafeCast_0 = <init>(buf)
    return kotlin.Any?(tmp0_unsafeCast_0)

def bufInt32$init$():
    tmp0_unsafeCast_0 = <init>(buf)
    return kotlin.Any?(tmp0_unsafeCast_0)

def lowIndex$init$():
    jsArraySet(bufFloat64, 0, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@434fa353)
    return visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@68b7a133

class DoNotIntrinsify:
    pass

def charSequenceGet(a, index):
    tmp
    if isString(a):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@26c1f174
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@13437ce5:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@43aeca02
    
    return tmp

def isString(a):
    return jsEqeqeq(jsTypeOf(a), 'string')

def charSequenceLength(a):
    tmp
    if isString(a):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@17d864f8
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@3e492199:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@6c0959f4
    
    return tmp

def charSequenceSubSequence(a, startIndex, endIndex):
    tmp
    if isString(a):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@9d91005
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@4e9ab294:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@694f8227
    
    return tmp

def arrayToString(array):
    return joinToString$default(', ', '[', ']', 0, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@762618bb, <no name provided>$factory(), 24, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@51413e47)

class <no name provided>:
    pass

def <no name provided>$factory():
    i = <init>()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@77e11884

def compareTo(a, b):
    tmp0_subject = jsTypeOf(a)
    tmp
    if jsEqeqeq(tmp0_subject, 'number'):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@72db6e52
    
    if visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@6f750dea:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@4bddc770
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@380ea757:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@2d475ee6
    
    return tmp

def doubleCompareTo(a, b):
    tmp
    if visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@3e13a74:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@7a5bc003
    
    if visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@2d0ed017:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@6f019523
    
    if visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@2f96e49f:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@dce343c
    
    if visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@2d0f850:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@3d8b888f
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@48ca44cd:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@6373f5de
    
    return tmp

def primitiveCompareTo(a, b):
    return visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@486765f1

def compareToDoNotIntrinsicify(a, b):
    return compareTo(b)

def construct(constructorType, resultType, args):
    return kotlin.Any(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@271ced5f)

def identityHashCode(obj):
    return getObjectHashCode(obj)

def getObjectHashCode(obj):
    if jsNot(jsIn('kotlinHashCodeValue$', kotlin.Any(obj))):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@4e38b4ea
    
    tmp0_unsafeCast_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@3f41a1f3
    return kotlin.Any?(tmp0_unsafeCast_0)

def <get-OBJECT_HASH_CODE_PROPERTY_NAME>():
    return OBJECT_HASH_CODE_PROPERTY_NAME

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@7828111d
def <get-POW_2_32>():
    return POW_2_32

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@33fa6a8b
def toString(o):
    tmp
    if visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@15beb40b:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@3b94d98d
    
    if isArrayish(o):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@6f6c01d9
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@6f8060ac:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@de4dd7
    
    return tmp

def hashCode(obj):
    if visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@7b80be13:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@737652a9
    
    tmp0_subject = jsTypeOf(obj)
    tmp
    if jsEqeqeq(tmp0_subject, 'object'):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@55f48623
    
    if jsEqeqeq(tmp0_subject, 'function'):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@1816701b
    
    if jsEqeqeq(tmp0_subject, 'number'):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@7dab2645
    
    if jsEqeqeq(tmp0_subject, 'boolean'):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@4c96f850
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@890196b:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@5494cf4b
    
    return tmp

def getStringHashCode(str):
    hash = 0
    length = jsArrayLength(str)
    inductionVariable = 0
    last = jsBitOr(jsMinus(length, 1), 0)
    if jsLtEq(inductionVariable, last):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDoWhileLoopImpl@7e86f9ba
    
    return hash

def anyToString(o):
    return kotlin.String(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@2de526f9)

def equals(obj1, obj2):
    if visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@4fbd0d1:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@447dec7e
    
    if visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@287d9e0c:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@46135aba
    
    if visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@338e70c8:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@c4ba591
    
    if visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@31e90355:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@b680059
    
    if visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@6987b0e8:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@51be4bf5
    
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@7db4c883

def boxIntrinsic(x):
    tmp0_error_0 = 'Should be lowered'
    visitThrow org.jetbrains.kotlin.ir.expressions.impl.IrThrowImpl@7a602de2

def unboxIntrinsic(x):
    tmp0_error_0 = 'Should be lowered'
    visitThrow org.jetbrains.kotlin.ir.expressions.impl.IrThrowImpl@6690629e

def captureStack(instance, constructorFunction):
    if visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@52baaf87:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@7277fa93
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@cec9f23:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@243deb3f
    

def newThrowable(message, cause):
    throwable = js('new Error()')
    tmp
    if isUndefined(message):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@7f448d3d
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@3048ec86:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@9e03c6e
    
    visitExpression org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@7c4c091a
    visitExpression org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@1fb66050
    visitExpression org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@634cd45c
    return kotlin.Any?(throwable)

def isUndefined(value):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@562b791b

def extendThrowable(this_, message, cause):
    visitExpression org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@7c87c960
    setPropertiesToThrowableInstance(this_, message, cause)

def setPropertiesToThrowableInstance(this_, message, cause):
    if jsNot(hasOwnPrototypeProperty(kotlin.Any(this_), 'message')):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@4c55d3ce
    
    if jsNot(hasOwnPrototypeProperty(kotlin.Any(this_), 'cause')):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@48dbf9d
    
    visitExpression org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@7e4f42c0

def hasOwnPrototypeProperty(o, name):
    tmp0_unsafeCast_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@7ec53f8f
    return kotlin.Any?(tmp0_unsafeCast_0)

def getContinuation():
    visitThrow org.jetbrains.kotlin.ir.expressions.impl.IrThrowImpl@736ded17

def returnIfSuspended(argument):
    visitThrow org.jetbrains.kotlin.ir.expressions.impl.IrThrowImpl@cdf3ee2

def suspendCoroutineUninterceptedOrReturnJS(block):
    return invoke(getContinuation())

def getCoroutineContext():
    return <get-context>()

def ensureNotNull(v):
    tmp
    if jsEqeq(v, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@370bd951):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@27b0124a
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@73859ca8:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@145ff25d
    
    return tmp

def THROW_NPE():
    visitThrow org.jetbrains.kotlin.ir.expressions.impl.IrThrowImpl@16adf66f

def noWhenBranchMatchedException():
    visitThrow org.jetbrains.kotlin.ir.expressions.impl.IrThrowImpl@6465f4a

def THROW_CCE():
    visitThrow org.jetbrains.kotlin.ir.expressions.impl.IrThrowImpl@2dad6fc9

def throwUninitializedPropertyAccessException(name):
    visitThrow org.jetbrains.kotlin.ir.expressions.impl.IrThrowImpl@1f47e14d

def throwKotlinNothingValueException():
    visitThrow org.jetbrains.kotlin.ir.expressions.impl.IrThrowImpl@26e437dd

def THROW_ISE():
    visitThrow org.jetbrains.kotlin.ir.expressions.impl.IrThrowImpl@66dad66f

def THROW_IAE(msg):
    visitThrow org.jetbrains.kotlin.ir.expressions.impl.IrThrowImpl@f9da676

def emptyArray():
    return kotlin.Array<T>(js('[]'))

def enumValueOfIntrinsic(name):
    visitThrow org.jetbrains.kotlin.ir.expressions.impl.IrThrowImpl@faff2bf

def enumValuesIntrinsic():
    visitThrow org.jetbrains.kotlin.ir.expressions.impl.IrThrowImpl@4310007c

class Companion:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@1e5066ac
def Companion_getInstance():
    if jsEqeq(Companion_instance, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@361069db):
        <init>()
    
    return Companion_instance

class Long:
    pass

def <get-ZERO>():
    return ZERO

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@31fd8e6f
def <get-ONE>():
    return ONE

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@3c833d43
def <get-NEG_ONE>():
    return NEG_ONE

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@6472dd0c
def <get-MAX_VALUE>():
    return MAX_VALUE

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@6b3b9a19
def <get-MIN_VALUE>():
    return MIN_VALUE

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@5a8a50b8
def <get-TWO_PWR_24_>():
    return TWO_PWR_24_

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@374d3128
def compare(other):
    if equalsLong(other):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@7dd63fcc
    
    thisNeg = isNegative()
    otherNeg = isNegative()
    return visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@45a935e5

def add(other):
    a48 = jsBitShiftRU(high, 16)
    a32 = jsBitAnd(high, 65535)
    a16 = jsBitShiftRU(low, 16)
    a00 = jsBitAnd(low, 65535)
    b48 = jsBitShiftRU(high, 16)
    b32 = jsBitAnd(high, 65535)
    b16 = jsBitShiftRU(low, 16)
    b00 = jsBitAnd(low, 65535)
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
    return <init>(jsBitOr(jsBitShiftL(c16, 16), c00), jsBitOr(jsBitShiftL(c48, 16), c32))

def subtract(other):
    return add(unaryMinus())

def multiply(other):
    if isZero():
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@15e8918
    
    if isZero():
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@306cb0a0
    
    if equalsLong(MIN_VALUE):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@533053b4
    
    if equalsLong(MIN_VALUE):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@62f11904
    
    if isNegative():
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@72722a6b
    
    if isNegative():
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@6074f8f9
    
    if visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@6a7ba38b:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@651a3e01
    
    a48 = jsBitShiftRU(high, 16)
    a32 = jsBitAnd(high, 65535)
    a16 = jsBitShiftRU(low, 16)
    a00 = jsBitAnd(low, 65535)
    b48 = jsBitShiftRU(high, 16)
    b32 = jsBitAnd(high, 65535)
    b16 = jsBitShiftRU(low, 16)
    b00 = jsBitAnd(low, 65535)
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
    return <init>(jsBitOr(jsBitShiftL(c16, 16), c00), jsBitOr(jsBitShiftL(c48, 16), c32))

def divide(other):
    if isZero():
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@46969355
    
    if isZero():
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@2b4b3918
    
    if equalsLong(MIN_VALUE):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@71103416
    
    if equalsLong(MIN_VALUE):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@2f9bd5ac
    
    if isNegative():
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@eb3b4d7
    
    if isNegative():
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@56d5a50f
    
    res = ZERO
    rem = <this>
    while greaterThanOrEqual(other):
        approxDouble = jsDiv(toNumber(), toNumber())
        approx2 = max(visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@4d400e77, floor(approxDouble))
        log2 = ceil(jsDiv(log(approx2), <get-LN2>()))
        delta = visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@c63a15f
        approxRes = fromNumber(approx2)
        approxRem = multiply(other)
        while visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@3eb05a64:
            approx2 = jsMinus(approx2, delta)
            approxRes = fromNumber(approx2)
            approxRem = multiply(other)
        
        if isZero():
            visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@380cb7e3
        
        res = add(approxRes)
        rem = subtract(approxRem)
    
    return res

def modulo(other):
    return subtract(multiply(other))

def shiftLeft(numBits):
    numBits = jsBitAnd(numBits, 63)
    if jsEqeqeq(numBits, 0):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@14aeb8e6
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@403ca4ec:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@17bda3
    

def shiftRight(numBits):
    numBits = jsBitAnd(numBits, 63)
    if jsEqeqeq(numBits, 0):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@3d7fc4b3
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@47609e3d:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@7555782c
    

def shiftRightUnsigned(numBits):
    numBits = jsBitAnd(numBits, 63)
    if jsEqeqeq(numBits, 0):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@60cfa399
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@4ed74b13:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@463fc3f6
    

def toNumber():
    return jsPlus(jsMult(high, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@35f15782), getLowBitsUnsigned())

def equalsLong(other):
    return visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@23efa674

def hashCode(l):
    return jsBitXor(low, high)

def toStringImpl(radix):
    if visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@13a09d37:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@279afa4e
    
    if isZero():
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@16209621
    
    if isNegative():
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@2c47135c
    
    radixToPower = fromNumber(pow(kotlin.Double(radix), visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@5e077a32))
    rem = <this>
    result = ''
    while visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@7fb57b7c:
        remDiv = div(radixToPower)
        intval = toInt()
        tmp1_unsafeCast_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@51edc97d
        digits = kotlin.Any?(tmp1_unsafeCast_0)
        rem = remDiv
        if isZero():
            visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@6c861b25
        
        if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@3c05fb12:
            visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@702f99a5
        
    

def fromInt(value):
    return <init>(value, visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@37156bfb)

def isNegative():
    return jsLt(high, 0)

def isZero():
    return visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@2330861e

def isOdd():
    return jsEqeqeq(jsBitAnd(low, 1), 1)

def negate():
    return unaryMinus()

def lessThan(other):
    return jsLt(compare(other), 0)

def fromNumber(value):
    if isNaN():
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@65227bd6
    
    if jsLtEq(value, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@eba9ab4):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@6cee6eb7
    
    if jsGtEq(jsPlus(value, 1), visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@d3e77a3):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@1925be93
    
    if jsLt(value, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@1199a91):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@59711ea7
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@b92cdf9:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@464aff63
    

def greaterThan(other):
    return jsGt(compare(other), 0)

def greaterThanOrEqual(other):
    return jsGtEq(compare(other), 0)

def getLowBitsUnsigned():
    return visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@1cf51f82

def <get-TWO_PWR_32_DBL_>():
    return TWO_PWR_32_DBL_

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@60e72ced
def <get-TWO_PWR_63_DBL_>():
    return TWO_PWR_63_DBL_

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@65653da2
def imul(a_local, b_local):
    lhs = jsMult(kotlin.Double(jsBitwiseAnd(a_local, js('0xffff0000'))), kotlin.Double(jsBitwiseAnd(b_local, 65535)))
    rhs = jsMult(kotlin.Double(jsBitwiseAnd(a_local, 65535)), kotlin.Double(b_local))
    return jsBitwiseOr(jsPlus(lhs, rhs), 0)

def withType(type, array):
    visitExpression org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@19503dfa
    return array

def arrayConcat(args):
    len = jsArrayLength(args)
    tmp0_unsafeCast_0 = js('Array(len)')
    typed = kotlin.Any?(tmp0_unsafeCast_0)
    inductionVariable = 0
    last = jsBitOr(jsMinus(len, 1), 0)
    if jsLtEq(inductionVariable, last):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDoWhileLoopImpl@388f2bca
    
    return T(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@6fc26fb1)

def primitiveArrayConcat(args):
    size_local = 0
    inductionVariable = 0
    last = jsBitOr(jsMinus(jsArrayLength(args), 1), 0)
    if jsLtEq(inductionVariable, last):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDoWhileLoopImpl@7ce9ec07
    
    a = jsArrayGet(args, 0)
    tmp1_unsafeCast_0 = js('new a.constructor(size_local)')
    result = kotlin.Any?(tmp1_unsafeCast_0)
    if visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@3ac09fe2:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@1a57bb34
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@6b92b8c9:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@2b8cd1d4
    
    size_local = 0
    inductionVariable = 0
    last = jsBitOr(jsMinus(jsArrayLength(args), 1), 0)
    if jsLtEq(inductionVariable, last):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDoWhileLoopImpl@f053608
    
    return kotlin.Any?(result)

def taggedArrayCopy(array):
    res = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@3f114f13
    visitExpression org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@5b610c90
    return kotlin.Any?(res)

def numberToByte(a):
    return toByte(numberToInt(a))

def toByte(a):
    tmp0_unsafeCast_0 = js('a << 24 >> 24')
    return kotlin.Any?(tmp0_unsafeCast_0)

def numberToInt(a):
    tmp
    if jsInstanceOf(a, jsClass()):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@41f1feae
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@71d0240d:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@44695eb9
    
    return tmp

def doubleToInt(a):
    return visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@7092a14f

def numberToDouble(a):
    tmp0_unsafeCast_0 = js('+a')
    return kotlin.Any?(tmp0_unsafeCast_0)

def numberToShort(a):
    return toShort(numberToInt(a))

def toShort(a):
    tmp0_unsafeCast_0 = js('a << 16 >> 16')
    return kotlin.Any?(tmp0_unsafeCast_0)

def numberToLong(a):
    tmp
    if jsInstanceOf(a, jsClass()):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@2f8a57c2
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@61d2ff30:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@7a8a2cd8
    
    return tmp

def numberToChar(a):
    return <init>(jsBitAnd(numberToInt(a), 65535))

def toLong(a):
    return fromInt(kotlin.Int(a))

def numberRangeToNumber(start, endInclusive):
    return <init>(kotlin.Int(start), kotlin.Int(endInclusive))

def numberRangeToLong(start, endInclusive):
    return <init>(numberToLong(start), kotlin.Long(endInclusive))

def <get-propertyRefClassMetadataCache>():
    return propertyRefClassMetadataCache

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@55bd9d1
def metadataObject():
    return js('{ kind: 'class', interfaces: [] }')

def getPropertyCallableRef(name, paramCount, type, getter, setter):
    visitExpression org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@3c20af2
    visitExpression org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@7cb81ae
    visitExpression org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@3d872a12
    tmp0_unsafeCast_0 = getPropertyRefClass(getter, getKPropMetadata(paramCount, setter, type))
    return kotlin.Any?(tmp0_unsafeCast_0)

def getPropertyRefClass(obj, metadata):
    visitExpression org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@50853850
    visitExpression org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@38c6f088
    return obj

def getKPropMetadata(paramCount, setter, type):
    mdata = jsArrayGet(jsArrayGet(propertyRefClassMetadataCache, paramCount), visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@25471835)
    if visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@5cf21908:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@68b2ce71
    
    return mdata

def getLocalDelegateReference(name, type, mutable, lambda):
    return getPropertyCallableRef(name, 0, type, lambda, visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@2d1e3187)

def propertyRefClassMetadataCache$init$():
    tmp = js('{ kind: 'class', interfaces: [] }')
    tmp0_arrayOf_0 = arrayLiteral(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrVarargImpl@81ebdb0)
    tmp = kotlin.Any?(tmp0_arrayOf_0)
    tmp = js('{ kind: 'class', interfaces: [] }')
    tmp1_arrayOf_0 = arrayLiteral(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrVarargImpl@76fee3de)
    tmp = kotlin.Any?(tmp1_arrayOf_0)
    tmp = js('{ kind: 'class', interfaces: [] }')
    tmp2_arrayOf_0 = arrayLiteral(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrVarargImpl@71efa55d)
    tmp3_arrayOf_0 = arrayLiteral(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrVarargImpl@7dcbb6e5)
    return kotlin.Any?(tmp3_arrayOf_0)

def isArrayish(o):
    tmp
    if isJsArray(kotlin.Any(o)):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@2f6a30d2
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@4690132:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@6967bbf3
    
    return tmp

def isJsArray(obj):
    tmp0_unsafeCast_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@30cf61ca
    return kotlin.Any?(tmp0_unsafeCast_0)

def isInterface(obj, iface):
    tmp0_elvis_lhs = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicMemberExpressionImpl@5b5b9038
    tmp
    if jsEqeq(tmp0_elvis_lhs, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@2a09e0d4):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@2664d94
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@4064cd60:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@1e7fcf3a
    
    ctor = tmp
    return isInterfaceImpl(kotlin.js.Ctor(ctor), iface)

def isInterfaceImpl(ctor, iface):
    if jsEqeqeq(ctor, iface):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@65bcc339
    
    metadata = <get-$metadata$>()
    if jsNot(jsEqeq(metadata, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@2164f202)):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@5242e9f7
    
    superPrototype = visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@79a290ff
    superConstructor = visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@11bc8a1a
    return visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@bfcdc45

def isArray(obj):
    tmp
    if isJsArray(obj):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@36e7932f
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@1c5123ca:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@47b0bffc
    
    return tmp

def isObject(obj):
    objTypeOf = jsTypeOf(obj)
    tmp0_subject = objTypeOf
    return visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@6b2b46cf

def isSuspendFunction(obj, arity):
    if jsEqeqeq(jsTypeOf(obj), 'function'):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@299a0651
    
    return visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@3c88bef5

def isNumber(a):
    tmp
    if jsEqeqeq(jsTypeOf(a), 'number'):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@54e8ba11
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@311a569d:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@4e99b33
    
    return tmp

def isComparable(value):
    type = jsTypeOf(value)
    return visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@60a38548

def isCharSequence(value):
    return visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@97e310

def isBooleanArray(a):
    return visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@5b91c767

def isByteArray(a):
    return jsInstanceOf(a, js('Int8Array'))

def isShortArray(a):
    return jsInstanceOf(a, js('Int16Array'))

def isCharArray(a):
    return visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@3b0f224c

def isIntArray(a):
    return jsInstanceOf(a, js('Int32Array'))

def isFloatArray(a):
    return jsInstanceOf(a, js('Float32Array'))

def isLongArray(a):
    return visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@25df373d

def isDoubleArray(a):
    return jsInstanceOf(a, js('Float64Array'))

def jsIsType(obj, jsClass):
    if visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@425436b4:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@23639e5
    
    if visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@fb07c40:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@24287e5e
    
    if visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@23e892d3:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@3a96b5a1
    
    proto = jsGetPrototypeOf(jsClass)
    tmp0_safe_receiver = proto
    constructor = visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@41ff6f38
    if visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@6a554ba0:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@17746fcb
    
    klassMetadata = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicMemberExpressionImpl@631c244c
    if visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@1e9b1d9f:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@3c75fb73
    
    if visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@5d84189:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@76067600
    
    return visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@7b4db485

def jsGetPrototypeOf(jsClass):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@49342fb7

def asList():
    return <init>(kotlin.Any?(<this>))

def plus(elements):
    return kotlin.Array<T>(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@747fc4b6)

def copyOfRange(fromIndex, toIndex):
    checkRangeIndexes(fromIndex, toIndex, jsArrayLength(<this>))
    return kotlin.Array<T>(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@76b96594)

def minOf(a, b):
    return min(int32ArrayOf(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrVarargImpl@65a288e7))

def <get-resultContinuation>($this):
    return resultContinuation

def <get-_context>($this):
    return _context

def <set-intercepted_>($this, <set-?>):
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@73707d4

def <get-intercepted_>($this):
    return intercepted_

def releaseIntercepted($this):
    intercepted = intercepted_
    if visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@1e1f808c:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@6a49bf51
    
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@6ed4eacd

class CoroutineImpl:
    pass

class CompletedContinuation:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@41e8b043
def CompletedContinuation_getInstance():
    if jsEqeq(CompletedContinuation_instance, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@51110a39):
        <init>()
    
    return CompletedContinuation_instance

def Exception_init_$Init$($this):
    extendThrowable($this, $undefined(), $undefined())
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@5a1dc831
    return $this

def Exception_init_$Create$():
    tmp = Exception_init_$Init$(Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@4eb8d146)
    return tmp

def Exception_init_$Init$(message, $this):
    extendThrowable($this, message, $undefined())
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@64918740
    return $this

def Exception_init_$Create$(message):
    tmp = Exception_init_$Init$(message, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@7b07a20c)
    return tmp

def Exception_init_$Init$(message, cause, $this):
    extendThrowable($this, message, cause)
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@2d5b950b
    return $this

def Exception_init_$Create$(message, cause):
    tmp = Exception_init_$Init$(message, cause, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@710225a6)
    return tmp

def Exception_init_$Init$(cause, $this):
    extendThrowable($this, $undefined(), cause)
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@2dff4ef9
    return $this

def Exception_init_$Create$(cause):
    tmp = Exception_init_$Init$(cause, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@1e3d7df9)
    return tmp

class Exception:
    pass

def Error_init_$Init$($this):
    extendThrowable($this, $undefined(), $undefined())
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@298e95ed
    return $this

def Error_init_$Create$():
    tmp = Error_init_$Init$(Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@24ab288c)
    return tmp

def Error_init_$Init$(message, $this):
    extendThrowable($this, message, $undefined())
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@135e3c72
    return $this

def Error_init_$Create$(message):
    tmp = Error_init_$Init$(message, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@3453e1f)
    return tmp

def Error_init_$Init$(message, cause, $this):
    extendThrowable($this, message, cause)
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@11f2846
    return $this

def Error_init_$Create$(message, cause):
    tmp = Error_init_$Init$(message, cause, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@68f4a142)
    return tmp

def Error_init_$Init$(cause, $this):
    extendThrowable($this, $undefined(), cause)
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@1fafb2ae
    return $this

def Error_init_$Create$(cause):
    tmp = Error_init_$Init$(cause, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@77f965a0)
    return tmp

class Error:
    pass

def IllegalArgumentException_init_$Init$($this):
    RuntimeException_init_$Init$($this)
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@63cf3153
    return $this

def IllegalArgumentException_init_$Create$():
    tmp = IllegalArgumentException_init_$Init$(Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@65fdd81d)
    return tmp

def IllegalArgumentException_init_$Init$(message, $this):
    RuntimeException_init_$Init$(message, $this)
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@44707383
    return $this

def IllegalArgumentException_init_$Create$(message):
    tmp = IllegalArgumentException_init_$Init$(message, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@2e142db2)
    return tmp

def IllegalArgumentException_init_$Init$(message, cause, $this):
    RuntimeException_init_$Init$(message, cause, $this)
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@5c909d4d
    return $this

def IllegalArgumentException_init_$Create$(message, cause):
    tmp = IllegalArgumentException_init_$Init$(message, cause, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@1208fe55)
    return tmp

def IllegalArgumentException_init_$Init$(cause, $this):
    RuntimeException_init_$Init$(cause, $this)
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@37d77fd2
    return $this

def IllegalArgumentException_init_$Create$(cause):
    tmp = IllegalArgumentException_init_$Init$(cause, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@54d8774c)
    return tmp

class IllegalArgumentException:
    pass

def RuntimeException_init_$Init$($this):
    Exception_init_$Init$($this)
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@6cdabac8
    return $this

def RuntimeException_init_$Create$():
    tmp = RuntimeException_init_$Init$(Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@7e260d25)
    return tmp

def RuntimeException_init_$Init$(message, $this):
    Exception_init_$Init$(message, $this)
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@343a80d5
    return $this

def RuntimeException_init_$Create$(message):
    tmp = RuntimeException_init_$Init$(message, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@7a9bc6c1)
    return tmp

def RuntimeException_init_$Init$(message, cause, $this):
    Exception_init_$Init$(message, cause, $this)
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@3bf6dc0e
    return $this

def RuntimeException_init_$Create$(message, cause):
    tmp = RuntimeException_init_$Init$(message, cause, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@10eaa515)
    return tmp

def RuntimeException_init_$Init$(cause, $this):
    Exception_init_$Init$(cause, $this)
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@7cfd86c8
    return $this

def RuntimeException_init_$Create$(cause):
    tmp = RuntimeException_init_$Init$(cause, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@5fb03284)
    return tmp

class RuntimeException:
    pass

def NoSuchElementException_init_$Init$($this):
    RuntimeException_init_$Init$($this)
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@30b1f83
    return $this

def NoSuchElementException_init_$Create$():
    tmp = NoSuchElementException_init_$Init$(Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@516a97eb)
    return tmp

def NoSuchElementException_init_$Init$(message, $this):
    RuntimeException_init_$Init$(message, $this)
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@58fbaa6c
    return $this

def NoSuchElementException_init_$Create$(message):
    tmp = NoSuchElementException_init_$Init$(message, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@168dc9c3)
    return tmp

class NoSuchElementException:
    pass

def IllegalStateException_init_$Init$($this):
    RuntimeException_init_$Init$($this)
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@195c7f61
    return $this

def IllegalStateException_init_$Create$():
    tmp = IllegalStateException_init_$Init$(Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@4cc6713c)
    return tmp

def IllegalStateException_init_$Init$(message, $this):
    RuntimeException_init_$Init$(message, $this)
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@3fd13170
    return $this

def IllegalStateException_init_$Create$(message):
    tmp = IllegalStateException_init_$Init$(message, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@6226893)
    return tmp

def IllegalStateException_init_$Init$(message, cause, $this):
    RuntimeException_init_$Init$(message, cause, $this)
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@292dc20f
    return $this

def IllegalStateException_init_$Create$(message, cause):
    tmp = IllegalStateException_init_$Init$(message, cause, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@151b7c03)
    return tmp

def IllegalStateException_init_$Init$(cause, $this):
    RuntimeException_init_$Init$(cause, $this)
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@65c29c4c
    return $this

def IllegalStateException_init_$Create$(cause):
    tmp = IllegalStateException_init_$Init$(cause, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@c59b505)
    return tmp

class IllegalStateException:
    pass

def IndexOutOfBoundsException_init_$Init$($this):
    RuntimeException_init_$Init$($this)
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@46bde78e
    return $this

def IndexOutOfBoundsException_init_$Create$():
    tmp = IndexOutOfBoundsException_init_$Init$(Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@77320275)
    return tmp

def IndexOutOfBoundsException_init_$Init$(message, $this):
    RuntimeException_init_$Init$(message, $this)
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@103236a2
    return $this

def IndexOutOfBoundsException_init_$Create$(message):
    tmp = IndexOutOfBoundsException_init_$Init$(message, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@6d653110)
    return tmp

class IndexOutOfBoundsException:
    pass

def UnsupportedOperationException_init_$Init$($this):
    RuntimeException_init_$Init$($this)
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@2bd3767f
    return $this

def UnsupportedOperationException_init_$Create$():
    tmp = UnsupportedOperationException_init_$Init$(Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@39fabfea)
    return tmp

def UnsupportedOperationException_init_$Init$(message, $this):
    RuntimeException_init_$Init$(message, $this)
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@69925e55
    return $this

def UnsupportedOperationException_init_$Create$(message):
    tmp = UnsupportedOperationException_init_$Init$(message, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@63be584e)
    return tmp

def UnsupportedOperationException_init_$Init$(message, cause, $this):
    RuntimeException_init_$Init$(message, cause, $this)
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@48d46402
    return $this

def UnsupportedOperationException_init_$Create$(message, cause):
    tmp = UnsupportedOperationException_init_$Init$(message, cause, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@72225e34)
    return tmp

def UnsupportedOperationException_init_$Init$(cause, $this):
    RuntimeException_init_$Init$(cause, $this)
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@7192075e
    return $this

def UnsupportedOperationException_init_$Create$(cause):
    tmp = UnsupportedOperationException_init_$Init$(cause, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@26381009)
    return tmp

class UnsupportedOperationException:
    pass

def NullPointerException_init_$Init$($this):
    RuntimeException_init_$Init$($this)
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@3ca57afe
    return $this

def NullPointerException_init_$Create$():
    tmp = NullPointerException_init_$Init$(Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@1aac10b5)
    return tmp

def NullPointerException_init_$Init$(message, $this):
    RuntimeException_init_$Init$(message, $this)
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@160b966a
    return $this

def NullPointerException_init_$Create$(message):
    tmp = NullPointerException_init_$Init$(message, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@5ea231be)
    return tmp

class NullPointerException:
    pass

def NoWhenBranchMatchedException_init_$Init$($this):
    RuntimeException_init_$Init$($this)
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@372cd8fd
    return $this

def NoWhenBranchMatchedException_init_$Create$():
    tmp = NoWhenBranchMatchedException_init_$Init$(Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@29174934)
    return tmp

def NoWhenBranchMatchedException_init_$Init$(message, $this):
    RuntimeException_init_$Init$(message, $this)
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@43424634
    return $this

def NoWhenBranchMatchedException_init_$Create$(message):
    tmp = NoWhenBranchMatchedException_init_$Init$(message, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@23701ff5)
    return tmp

def NoWhenBranchMatchedException_init_$Init$(message, cause, $this):
    RuntimeException_init_$Init$(message, cause, $this)
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@5ce59857
    return $this

def NoWhenBranchMatchedException_init_$Create$(message, cause):
    tmp = NoWhenBranchMatchedException_init_$Init$(message, cause, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@50bd37f)
    return tmp

def NoWhenBranchMatchedException_init_$Init$(cause, $this):
    RuntimeException_init_$Init$(cause, $this)
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@1c2618d8
    return $this

def NoWhenBranchMatchedException_init_$Create$(cause):
    tmp = NoWhenBranchMatchedException_init_$Init$(cause, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@c59c954)
    return tmp

class NoWhenBranchMatchedException:
    pass

def ClassCastException_init_$Init$($this):
    RuntimeException_init_$Init$($this)
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@6a737ee1
    return $this

def ClassCastException_init_$Create$():
    tmp = ClassCastException_init_$Init$(Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@4f4769dd)
    return tmp

def ClassCastException_init_$Init$(message, $this):
    RuntimeException_init_$Init$(message, $this)
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@2cdaf44c
    return $this

def ClassCastException_init_$Create$(message):
    tmp = ClassCastException_init_$Init$(message, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@1ab3f085)
    return tmp

class ClassCastException:
    pass

def UninitializedPropertyAccessException_init_$Init$($this):
    RuntimeException_init_$Init$($this)
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@692751a9
    return $this

def UninitializedPropertyAccessException_init_$Create$():
    tmp = UninitializedPropertyAccessException_init_$Init$(Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@2ea3ed9f)
    return tmp

def UninitializedPropertyAccessException_init_$Init$(message, $this):
    RuntimeException_init_$Init$(message, $this)
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@34163940
    return $this

def UninitializedPropertyAccessException_init_$Create$(message):
    tmp = UninitializedPropertyAccessException_init_$Init$(message, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@486417fc)
    return tmp

def UninitializedPropertyAccessException_init_$Init$(message, cause, $this):
    RuntimeException_init_$Init$(message, cause, $this)
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@106976f4
    return $this

def UninitializedPropertyAccessException_init_$Create$(message, cause):
    tmp = UninitializedPropertyAccessException_init_$Init$(message, cause, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@21af88c6)
    return tmp

def UninitializedPropertyAccessException_init_$Init$(cause, $this):
    RuntimeException_init_$Init$(cause, $this)
    visitDelegatingCOnstructorCall org.jetbrains.kotlin.ir.expressions.impl.IrDelegatingConstructorCallImpl@25b20814
    return $this

def UninitializedPropertyAccessException_init_$Create$(cause):
    tmp = UninitializedPropertyAccessException_init_$Init$(cause, Object$create())
    captureStack(tmp, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrRawFunctionReferenceImpl@13a68fb7)
    return tmp

class UninitializedPropertyAccessException:
    pass

def jsIn(lhs_hack, rhs_hack):
    tmp0_unsafeCast_0 = js('lhs_hack in rhs_hack')
    return kotlin.Any?(tmp0_unsafeCast_0)

def jsBitwiseOr(lhs_hack, rhs_hack):
    tmp0_unsafeCast_0 = js('lhs_hack | rhs_hack')
    return kotlin.Any?(tmp0_unsafeCast_0)

def jsTypeOf(value_hack):
    tmp0_unsafeCast_0 = js('typeof value_hack')
    return kotlin.Any?(tmp0_unsafeCast_0)

def jsInstanceOf(obj_hack, jsClass_hack):
    tmp0_unsafeCast_0 = js('obj_hack instanceof jsClass_hack')
    return kotlin.Any?(tmp0_unsafeCast_0)

def jsBitwiseAnd(lhs_hack, rhs_hack):
    tmp0_unsafeCast_0 = js('lhs_hack & rhs_hack')
    return kotlin.Any?(tmp0_unsafeCast_0)

def toString(radix):
    return toStringImpl(checkRadix(radix))

def pythonTest():
    println('Hello world')

def exampleFromAstTest():
    fruits = listOf(arrayLiteral(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrVarargImpl@4bc757c1))
    tmp0_iterator = iterator()
    while hasNext():
        x = next()
        println(x)
    
