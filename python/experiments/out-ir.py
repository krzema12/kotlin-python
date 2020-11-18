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

def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@3ec62141

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

def special():
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
    
    return joinToString(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@3f67d229, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@49ce2726, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@1dece75a, limit, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@129b75c, transform)

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
    
    return joinTo(buffer, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@49ffcd07, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@4512085c, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@49e11ca7, limit, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@10063448, transform)

def contains(element):
    return jsGtEq(indexOf(element), 0)

def indexOf(element):
    inductionVariable = 0
    last = jsBitOr(jsMinus(jsArrayLength(<this>), 1), 0)
    if jsLtEq(inductionVariable, last):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDoWhileLoopImpl@23e883fb
    
    return -1

def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@462f8fe9

def special():
    return jsBitOr(jsMinus(jsArrayLength(<this>), 1), 0)

def contains(element):
    return jsGtEq(indexOf(element), 0)

def indexOf(element):
    inductionVariable = 0
    last = jsBitOr(jsMinus(jsArrayLength(<this>), 1), 0)
    if jsLtEq(inductionVariable, last):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDoWhileLoopImpl@22272bac
    
    return -1

def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@60cc20e1

def special():
    return jsBitOr(jsMinus(jsArrayLength(<this>), 1), 0)

def contains(element):
    return jsGtEq(indexOf(element), 0)

def indexOf(element):
    inductionVariable = 0
    last = jsBitOr(jsMinus(jsArrayLength(<this>), 1), 0)
    if jsLtEq(inductionVariable, last):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDoWhileLoopImpl@52f3859a
    
    return -1

def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5cc669d

def special():
    return jsBitOr(jsMinus(jsArrayLength(<this>), 1), 0)

def contains(element):
    return jsGtEq(indexOf(element), 0)

def indexOf(element):
    inductionVariable = 0
    last = jsBitOr(jsMinus(jsArrayLength(<this>), 1), 0)
    if jsLtEq(inductionVariable, last):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDoWhileLoopImpl@10eddc8b
    
    return -1

def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@21f479cd

def special():
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
    iterator = listIterator((special)())
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
    
    return joinToString(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@8742b32, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@5aa345a5, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@1a343d3e, limit, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@29e3c7fe, transform)

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
    
    return joinTo(buffer, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@65450878, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@1a9d873b, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@76600c90, limit, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@7746ae18, transform)

def downTo(to):
    return fromClosedRange(<this>, to, -1)

def until(to):
    if jsLtEq(to, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@cfc9c4f):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@68f264bf
    
    return numberRangeToNumber(<this>, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@58e48d9)

def reversed():
    return fromClosedRange(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@203f929, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@59bcab83, jsBitOr(jsUnaryMinus(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@49bf800f), 0))

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
    if visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@543eacd5:
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
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@750a4fc1

def Level_ERROR_getInstance():
    Level_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@c3745ae

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
    if visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@194ff162:
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
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@2876584f

def Level_ERROR_getInstance():
    Level_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@5c447983

class RequiresOptIn:
    pass

class OptIn:
    pass

class <no name provided>:
    pass

class AbstractCollection:
    pass

def <no name provided>$factory(this$0):
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@36eff8df
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@4977e352

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@7c81b1e1

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@473dbad

def special($this, specialArg):
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@35cb8b64

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@59463bab

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
    if jsEqeq(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@497dc589, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@346c568d):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@7fa1004
    
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@1bed8afd

class AbstractList:
    pass

def listOf(elements):
    return visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@4de37f33

def emptyList():
    return EmptyList_getInstance()

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@49f4de0e

def readResolve($this):
    return EmptyList_getInstance()

class EmptyList:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@2028ecf4
def EmptyList_getInstance():
    if jsEqeq(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@15971523, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@26dcce41):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@328f4e46
    
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@17e9e99

class EmptyIterator:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@7bd03562
def EmptyIterator_getInstance():
    if jsEqeq(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@1f583c44, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@6e7da5f4):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@6f099f77
    
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@51768401

def special():
    return jsBitOr(jsMinus((special)(), 1), 0)

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
    last = (special)()
    if jsLtEq(inductionVariable, last):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDoWhileLoopImpl@6a4fb518
    
    if jsLt(writeIndex, (special)()):
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
    if visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@65e0d9de:
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
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@32f7b6a2

def InvocationKind_AT_LEAST_ONCE_getInstance():
    InvocationKind_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@665c8e0f

def InvocationKind_EXACTLY_ONCE_getInstance():
    InvocationKind_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@20ea933f

def InvocationKind_UNKNOWN_getInstance():
    InvocationKind_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@505c675a

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
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4063af6

def resumeWithException(exception):
    tmp0_failure_0 = Companion_getInstance()
    return resumeWith(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@310bf0ed)

def resume(value):
    tmp0_success_0 = Companion_getInstance()
    return resumeWith(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@6b4848d9)

def special():
    visitThrow org.jetbrains.kotlin.ir.expressions.impl.IrThrowImpl@553f3655

class <no name provided>:
    pass

class Key:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@9d112d2
def Key_getInstance():
    if jsEqeq(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@1790a1d6, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@4f1422f7):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@2012f14e
    
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@16ae647d

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
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@63cdae1d
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@4358e209

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@25c7713e

def readResolve($this):
    return EmptyCoroutineContext_getInstance()

class EmptyCoroutineContext:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@9def6d
def EmptyCoroutineContext_getInstance():
    if jsEqeq(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@34151e5d, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@5e206acb):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@10ca3611
    
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@5ed4796f

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@5e86dc1c

class Companion:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@9ba905b
def Companion_getInstance():
    if jsEqeq(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@37d4b676, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@6801536):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4142586b
    
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@5b133d16

def readResolve($this):
    tmp0_fold_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@37601089
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
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@3ba34018

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@3463d70a

def size($this):
    cur = $this
    size = 2
    while visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@3ed1cff:
        tmp = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@58f49b5e
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
    return equals(get((special)()), element)

def containsAll($this, context):
    cur = context
    while visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@60155d7f:
        if jsNot(contains($this, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@4f9d220b)):
            visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@78483404
        
        next = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@3ea5f324
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
    
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@2169596d

class Serialized:
    pass

class <no name provided>:
    pass

class <no name provided>:
    pass

class CombinedContext:
    pass

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@3519f35

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@2566428f

class AbstractCoroutineContextKey:
    pass

def <no name provided>$factory():
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4228da9a
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@754f951a

def <no name provided>$factory($elements, $index):
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@24d5a11a
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@134d6f96

def special():
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
    if visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@36fd028d:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@16c574c4
    
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@7dc97564
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@1e20dad5
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@2331ac37
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@588e4caa

class CoroutineSingletons:
    pass

def CoroutineSingletons_COROUTINE_SUSPENDED_getInstance():
    CoroutineSingletons_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@2d923d2c

def CoroutineSingletons_UNDECIDED_getInstance():
    CoroutineSingletons_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@15682e7f

def CoroutineSingletons_RESUMED_getInstance():
    CoroutineSingletons_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@2587f18d

def and(other):
    return toByte(jsBitAnd(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@4d574ec7, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@39cdbc4e))

def or(other):
    return toByte(jsBitOr(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@23673954, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@28391cc6))

def xor(other):
    return toByte(jsBitXor(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@2a6ca8d0, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@353a829f))

def inv():
    return toByte(jsBitNot(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@59e285e))

def and(other):
    return toShort(jsBitAnd(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@1772cc68, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@23ebd596))

def or(other):
    return toShort(jsBitOr(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@4260de0d, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@6e5b7446))

def xor(other):
    return toShort(jsBitXor(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@7effdd04, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@2e259c54))

def inv():
    return toShort(jsBitNot(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@12680685))

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
    if visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@691fa716:
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
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@1f0630a9

def RequireKotlinVersionKind_COMPILER_VERSION_getInstance():
    RequireKotlinVersionKind_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@772739ee

def RequireKotlinVersionKind_API_VERSION_getInstance():
    RequireKotlinVersionKind_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@5f18ed13

class KClassifier:
    pass

class KTypeParameter:
    pass

class Companion:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@633f8efd
def Companion_getInstance():
    if jsEqeq(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@4f401aac, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@14467f3b):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@6980c9c3
    
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@42bd5540

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
    if visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@699a53d4:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@1adcd53b
    
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@47c90585
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@ff8df3
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@5917b984
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@18fe293d

class KVariance:
    pass

def KVariance_INVARIANT_getInstance():
    KVariance_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@5162ccc9

def KVariance_IN_getInstance():
    KVariance_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@172249cd

def KVariance_OUT_getInstance():
    KVariance_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@2142b70d

def appendElement(element, transform):
    if jsNot(jsEqeq(transform, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@50d91a0f)):
        visitComposite-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrCompositeImpl@77a3c614
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@3f341562:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@56cee7f6
    

def isEmpty():
    return jsEqeqeq(charSequenceLength(<this>), 0)

def special():
    return jsBitOr(jsMinus(charSequenceLength(<this>), 1), 0)

def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@34114276

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@5a941fb4
def UNDEFINED_RESULT$init$():
    tmp0_success_0 = Companion_getInstance()
    tmp1_success_0 = (special)()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@11ef3bee

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
    

def special(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@47bfde21

def special(this):
    tmp = (special)(this)
    return jsNot(jsInstanceOf(tmp, jsClass()))

def special(this):
    tmp = (special)(this)
    return jsInstanceOf(tmp, jsClass())

def Result__getOrNull-impl(this):
    tmp
    if (special)(this):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@2c6a222a
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@39415641:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@7e26e452
    
    return tmp

def Result__exceptionOrNull-impl(this):
    tmp0_subject = (special)(this)
    tmp
    if jsInstanceOf(tmp0_subject, jsClass()):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@7cc880cf
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@1b67ea5f:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@19ea1606
    
    return tmp

def Result__toString-impl(this):
    tmp0_subject = (special)(this)
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
    if jsEqeq(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@2c29342a, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@4af2f991):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4b5d2a4c
    
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@78e077f8

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
    if jsNot(equals(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@7fba492e, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@17635531)):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@396519b
    
    return visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@7f3a92fd

class Result:
    pass

def createFailure(exception):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@16e5c19f

def getOrThrow():
    throwOnFailure()
    tmp = (special)(<this>)
    return visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@4710332d

def throwOnFailure():
    tmp = (special)(<this>)
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

def special(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@3ec98000

class Companion:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@511966dc
def Companion_getInstance():
    if jsEqeq(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@40fd518f, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@1dafe1d2):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@77e86a53
    
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@3249c81a

def UByte__compareTo-impl(this, other):
    tmp = jsBitAnd(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@3703bc7e, 255)
    return compareTo(tmp, jsBitAnd(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@469dfbf7, 255))

def UByte__compareTo-impl(this, other):
    tmp = unboxIntrinsic(this)
    return UByte__compareTo-impl(tmp, visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@1275d11b)

def UByte__compareTo-impl(this, other):
    tmp = jsBitAnd(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@2c107b94, 255)
    return compareTo(tmp, jsBitAnd(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@1ca0f80, 65535))

def UByte__compareTo-impl(this, other):
    tmp0_compareTo_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@56967355
    return uintCompare((special)(tmp0_compareTo_0), (special)(other))

def UByte__compareTo-impl(this, other):
    tmp0_compareTo_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@284d1c98
    return ulongCompare((special)(tmp0_compareTo_0), (special)(other))

def UByte__plus-impl(this, other):
    tmp0_plus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@630d7bce
    tmp1_plus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@7e471ad
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5401976b

def UByte__plus-impl(this, other):
    tmp0_plus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@9d464e7
    tmp1_plus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@30c6a810
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@45b97486

def UByte__plus-impl(this, other):
    tmp0_plus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@47d57aae
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@385376c

def UByte__plus-impl(this, other):
    tmp0_plus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@25d44c7
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@26d78474

def UByte__minus-impl(this, other):
    tmp0_minus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@770feaab
    tmp1_minus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@7cfc6110
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@6916566d

def UByte__minus-impl(this, other):
    tmp0_minus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@33ded464
    tmp1_minus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@d12009f
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@398072c6

def UByte__minus-impl(this, other):
    tmp0_minus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4d5665bb
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@7f256398

def UByte__minus-impl(this, other):
    tmp0_minus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@6cd56b97
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@6c8fa6b3

def UByte__times-impl(this, other):
    tmp0_times_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@3c199e06
    tmp1_times_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@7b16d337
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@65bc66bb

def UByte__times-impl(this, other):
    tmp0_times_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@23e080a9
    tmp1_times_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@43d356e1
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@18f9bc99

def UByte__times-impl(this, other):
    tmp0_times_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@a26daf9
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@6b6eaa73

def UByte__times-impl(this, other):
    tmp0_times_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@2812c884
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@6281326f

def UByte__div-impl(this, other):
    tmp0_div_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5fea6cdb
    tmp1_div_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5f0a452d
    return uintDivide(tmp0_div_0, tmp1_div_0)

def UByte__div-impl(this, other):
    tmp0_div_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@1db203d2
    tmp1_div_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@720bacd7
    return uintDivide(tmp0_div_0, tmp1_div_0)

def UByte__div-impl(this, other):
    tmp0_div_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@705ba09a
    return uintDivide(tmp0_div_0, other)

def UByte__div-impl(this, other):
    tmp0_div_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@275d46a8
    return ulongDivide(tmp0_div_0, other)

def UByte__rem-impl(this, other):
    tmp0_rem_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@24d5a3b8
    tmp1_rem_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@1ecb3cde
    return uintRemainder(tmp0_rem_0, tmp1_rem_0)

def UByte__rem-impl(this, other):
    tmp0_rem_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@a674645
    tmp1_rem_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@8911222
    return uintRemainder(tmp0_rem_0, tmp1_rem_0)

def UByte__rem-impl(this, other):
    tmp0_rem_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4913778f
    return uintRemainder(tmp0_rem_0, other)

def UByte__rem-impl(this, other):
    tmp0_rem_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@1bd051c4
    return ulongRemainder(tmp0_rem_0, other)

def UByte__inc-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@152e530d

def UByte__dec-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@59ca0db6

def UByte__rangeTo-impl(this, other):
    tmp = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@67e85559
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@939f06

def UByte__and-impl(this, other):
    tmp0_and_0 = (special)(this)
    tmp1_and_0 = (special)(other)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@293f855b

def UByte__or-impl(this, other):
    tmp0_or_0 = (special)(this)
    tmp1_or_0 = (special)(other)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@34c73992

def UByte__xor-impl(this, other):
    tmp0_xor_0 = (special)(this)
    tmp1_xor_0 = (special)(other)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4c57b0e7

def UByte__inv-impl(this):
    tmp0_inv_0 = (special)(this)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@3f608bde

def UByte__toByte-impl(this):
    return (special)(this)

def UByte__toShort-impl(this):
    tmp0_and_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@720d007b
    tmp1_and_0 = visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@720a3eff
    return toShort(jsBitAnd(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@59957e31, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@71e869c2))

def UByte__toInt-impl(this):
    return jsBitAnd(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@f7269a2, 255)

def UByte__toLong-impl(this):
    return and(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@75440613)

def UByte__toUByte-impl(this):
    return this

def UByte__toUShort-impl(this):
    tmp0_and_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@3b847d31
    tmp1_and_0 = visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@5a934ef9
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@54271d08

def UByte__toUInt-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@438a0024

def UByte__toULong-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@364b2c46

def UByte__toFloat-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@5a524a19

def UByte__toDouble-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@8d27060

def UByte__toString-impl(this):
    return toString()

def UByte__hashCode-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@62376bdd

def UByte__equals-impl(this, other):
    if jsNot(jsInstanceOf(other, jsClass())):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@2148849f
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@58afc14:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@56ec941b
    
    tmp0_other_with_cast = visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@18a3095d
    if jsNot(jsEqeqeq(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@7a023e34, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@65fe1f47)):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@2165d4ab
    
    return visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@4d529bc0

class UByte:
    pass

def toUByte():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@3ef8b4

def toUByte():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@3c83bde0

def toUByte():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5e76eb5a

def toUByte():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@479729d3

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@3f78b3b2

def special($this, specialArg):
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@6da50b8f

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@1ed8d18c

def special(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@e21d73

def special(size):
    tmp = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@1878815a
    return tmp

def UByteArray__get-impl(this, index):
    tmp0_toUByte_0 = jsArrayGet((special)(this), index)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@d4f223e

def UByteArray__set-impl(this, index, value):
    tmp = (special)(this)
    jsArraySet(tmp, index, (special)(value))

def special(this):
    return jsArrayLength((special)(this))

def UByteArray__iterator-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@750adad8

class Iterator:
    pass

def UByteArray__contains-impl(this, element):
    tmp = visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@142409b4
    if jsNot(jsInstanceOf(tmp, jsClass())):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@eda7dd3
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@25b14faf:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@6e0576da
    
    tmp = (special)(this)
    return contains((special)(element))

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
    return jsEqeqeq(jsArrayLength((special)(this)), 0)

def UByteArray__toString-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrStringConcatenationImpl@1c057fc8

def UByteArray__hashCode-impl(this):
    return hashCode(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@344cf00f)

def UByteArray__equals-impl(this, other):
    if jsNot(jsInstanceOf(other, jsClass())):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@432b883
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@1f8c7cd7:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@6ba1a7fd
    
    tmp0_other_with_cast = visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@3a42b2b6
    if jsNot(equals(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@4a7c8cb7, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@2351255a)):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@2a4f1bc5
    
    return visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@4d145177

class UByteArray:
    pass

def special(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@508abc74

class Companion:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@4c6d1f1f
def Companion_getInstance():
    if jsEqeq(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@84ab902, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@70ab102c):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@2793f84c
    
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@3501c1de

def UInt__compareTo-impl(this, other):
    tmp0_compareTo_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@cfef34
    return uintCompare((special)(this), (special)(tmp0_compareTo_0))

def UInt__compareTo-impl(this, other):
    tmp0_compareTo_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@7c329d38
    return uintCompare((special)(this), (special)(tmp0_compareTo_0))

def UInt__compareTo-impl(this, other):
    return uintCompare((special)(this), (special)(other))

def UInt__compareTo-impl(this, other):
    tmp = unboxIntrinsic(this)
    return UInt__compareTo-impl(tmp, visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@41ee3c99)

def UInt__compareTo-impl(this, other):
    tmp0_compareTo_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@189faf12
    return ulongCompare((special)(tmp0_compareTo_0), (special)(other))

def UInt__plus-impl(this, other):
    tmp0_plus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@86e170e
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@413195dc

def UInt__plus-impl(this, other):
    tmp0_plus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@7e798721
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@2b4f99e5

def UInt__plus-impl(this, other):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@1300bc97

def UInt__plus-impl(this, other):
    tmp0_plus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@38ede85d
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@111d4b1c

def UInt__minus-impl(this, other):
    tmp0_minus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@2ca57834
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4f415a37

def UInt__minus-impl(this, other):
    tmp0_minus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@304175d6
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@1d5f1fa5

def UInt__minus-impl(this, other):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@1adac232

def UInt__minus-impl(this, other):
    tmp0_minus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@7973d55a
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5548d5c4

def UInt__times-impl(this, other):
    tmp0_times_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@7157b2d4
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@b96fb73

def UInt__times-impl(this, other):
    tmp0_times_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5460452a
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@32dca84b

def UInt__times-impl(this, other):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@578ce232

def UInt__times-impl(this, other):
    tmp0_times_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@52b2aa6e
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@50c43f7d

def UInt__div-impl(this, other):
    tmp0_div_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5d131f37
    return uintDivide(this, tmp0_div_0)

def UInt__div-impl(this, other):
    tmp0_div_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@41ef53a9
    return uintDivide(this, tmp0_div_0)

def UInt__div-impl(this, other):
    return uintDivide(this, other)

def UInt__div-impl(this, other):
    tmp0_div_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@3ad9012f
    return ulongDivide(tmp0_div_0, other)

def UInt__rem-impl(this, other):
    tmp0_rem_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@6e6b3dbf
    return uintRemainder(this, tmp0_rem_0)

def UInt__rem-impl(this, other):
    tmp0_rem_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5bdd5b86
    return uintRemainder(this, tmp0_rem_0)

def UInt__rem-impl(this, other):
    return uintRemainder(this, other)

def UInt__rem-impl(this, other):
    tmp0_rem_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@203ea126
    return ulongRemainder(tmp0_rem_0, other)

def UInt__inc-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@42bc7ca2

def UInt__dec-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@618c6ba8

def UInt__rangeTo-impl(this, other):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4faf4191

def UInt__shl-impl(this, bitCount):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@48409124

def UInt__shr-impl(this, bitCount):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4ed5c276

def UInt__and-impl(this, other):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4e9b4e98

def UInt__or-impl(this, other):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@18e26ed4

def UInt__xor-impl(this, other):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@7a6cec15

def UInt__inv-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@105cb38b

def UInt__toByte-impl(this):
    return toByte((special)(this))

def UInt__toShort-impl(this):
    return toShort((special)(this))

def UInt__toInt-impl(this):
    return (special)(this)

def UInt__toLong-impl(this):
    return and(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@7f4796e)

def UInt__toUByte-impl(this):
    tmp0_toUByte_0 = (special)(this)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@79adc343

def UInt__toUShort-impl(this):
    tmp0_toUShort_0 = (special)(this)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@565d2dab

def UInt__toUInt-impl(this):
    return this

def UInt__toULong-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@6f8a516c

def UInt__toFloat-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@69f1887c

def UInt__toDouble-impl(this):
    return uintToDouble((special)(this))

def UInt__toString-impl(this):
    return toString()

def UInt__hashCode-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@35d145fb

def UInt__equals-impl(this, other):
    if jsNot(jsInstanceOf(other, jsClass())):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@ad6255e
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@7b5de23c:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@6f39e2a6
    
    tmp0_other_with_cast = visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@2dd61113
    if jsNot(jsEqeqeq(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@3e574f9c, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@218fc40d)):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@26bbbe9e
    
    return visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@72ad577b

class UInt:
    pass

def toUInt():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@bb96f3f

def toUInt():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@2e484f94

def toUInt():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@11e0a164

def toUInt():
    return doubleToUInt(<this>)

def toUInt():
    return doubleToUInt(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@6e68cd0f)

def toUInt():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@6ce766fa

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@1a61a2c4

def special($this, specialArg):
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@257d8340

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@29a1c0b7

def special(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@47f8374

def special(size):
    tmp = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@6689f455
    return tmp

def UIntArray__get-impl(this, index):
    tmp0_toUInt_0 = jsArrayGet((special)(this), index)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@7c3341c9

def UIntArray__set-impl(this, index, value):
    tmp = (special)(this)
    jsArraySet(tmp, index, (special)(value))

def special(this):
    return jsArrayLength((special)(this))

def UIntArray__iterator-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@7137cd14

class Iterator:
    pass

def UIntArray__contains-impl(this, element):
    tmp = visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@3d8777ce
    if jsNot(jsInstanceOf(tmp, jsClass())):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@6ab6ec33
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@418a5228:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@20ed6c31
    
    tmp = (special)(this)
    return contains((special)(element))

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
    return jsEqeqeq(jsArrayLength((special)(this)), 0)

def UIntArray__toString-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrStringConcatenationImpl@5341eab4

def UIntArray__hashCode-impl(this):
    return hashCode(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@b0e6d4e)

def UIntArray__equals-impl(this, other):
    if jsNot(jsInstanceOf(other, jsClass())):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@3c39c739
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@285289cd:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@697699cb
    
    tmp0_other_with_cast = visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@3a7f7201
    if jsNot(equals(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@91c11b6, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@1dfd6023)):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@3e7da4cb
    
    return visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@3a2881d6

class UIntArray:
    pass

class Companion:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@3f81872b
def Companion_getInstance():
    if jsEqeq(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@4beea618, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@561fdee3):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@23092aba
    
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@30661521

class UIntRange:
    pass

class Companion:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@641c872d
def Companion_getInstance():
    if jsEqeq(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@5881d8da, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@4cf22d79):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@76be352d
    
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@24270e65

class UIntProgression:
    pass

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@6f4809ae

def special($this, specialArg):
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@7c4a0245

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@6dd1e22

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@43a188b6

def special($this, specialArg):
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@7c0514f

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@1e7d3d93

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

def special(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@6f627a1a

class Companion:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@39b88618
def Companion_getInstance():
    if jsEqeq(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@3bbf850b, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@321f3b88):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@68374279
    
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@6b5c4867

def ULong__compareTo-impl(this, other):
    tmp0_compareTo_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@30f13b3a
    return ulongCompare((special)(this), (special)(tmp0_compareTo_0))

def ULong__compareTo-impl(this, other):
    tmp0_compareTo_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@6d8e8a06
    return ulongCompare((special)(this), (special)(tmp0_compareTo_0))

def ULong__compareTo-impl(this, other):
    tmp0_compareTo_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@55c38884
    return ulongCompare((special)(this), (special)(tmp0_compareTo_0))

def ULong__compareTo-impl(this, other):
    return ulongCompare((special)(this), (special)(other))

def ULong__compareTo-impl(this, other):
    tmp = unboxIntrinsic(this)
    return ULong__compareTo-impl(tmp, visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@633f30af)

def ULong__plus-impl(this, other):
    tmp0_plus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@1c2608e3
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5c4d30a5

def ULong__plus-impl(this, other):
    tmp0_plus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@71fc80df
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@1ef06deb

def ULong__plus-impl(this, other):
    tmp0_plus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@32a4284d
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@3eafe537

def ULong__plus-impl(this, other):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@42f5ee2d

def ULong__minus-impl(this, other):
    tmp0_minus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@26276868
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@2014fd86

def ULong__minus-impl(this, other):
    tmp0_minus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@23031a56
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@3c31c0c8

def ULong__minus-impl(this, other):
    tmp0_minus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4dd8a37e
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@152364f0

def ULong__minus-impl(this, other):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@2cf22f15

def ULong__times-impl(this, other):
    tmp0_times_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@1812ba7f
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4418ef84

def ULong__times-impl(this, other):
    tmp0_times_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@43b5a9fd
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@1d73c2fa

def ULong__times-impl(this, other):
    tmp0_times_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@61e1ecd5
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@1ec7b3f2

def ULong__times-impl(this, other):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@3d352fb4

def ULong__div-impl(this, other):
    tmp0_div_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4b9a2df7
    return ulongDivide(this, tmp0_div_0)

def ULong__div-impl(this, other):
    tmp0_div_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@aa9bf75
    return ulongDivide(this, tmp0_div_0)

def ULong__div-impl(this, other):
    tmp0_div_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@47d0e949
    return ulongDivide(this, tmp0_div_0)

def ULong__div-impl(this, other):
    return ulongDivide(this, other)

def ULong__rem-impl(this, other):
    tmp0_rem_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@de44b10
    return ulongRemainder(this, tmp0_rem_0)

def ULong__rem-impl(this, other):
    tmp0_rem_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5741bc9
    return ulongRemainder(this, tmp0_rem_0)

def ULong__rem-impl(this, other):
    tmp0_rem_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@30a3c1e1
    return ulongRemainder(this, tmp0_rem_0)

def ULong__rem-impl(this, other):
    return ulongRemainder(this, other)

def ULong__inc-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@a4664f3

def ULong__dec-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@446454af

def ULong__rangeTo-impl(this, other):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@6acdbe95

def ULong__shl-impl(this, bitCount):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@19a7b10d

def ULong__shr-impl(this, bitCount):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@421d9b57

def ULong__and-impl(this, other):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@32f4d719

def ULong__or-impl(this, other):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@1ad03f80

def ULong__xor-impl(this, other):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4dee8b9a

def ULong__inv-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@3ce30f67

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
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@3d381435

def ULong__toUShort-impl(this):
    tmp0_toUShort_0 = (special)(this)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@42404d83

def ULong__toUInt-impl(this):
    tmp0_toUInt_0 = (special)(this)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@71dce61e

def ULong__toULong-impl(this):
    return this

def ULong__toFloat-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@1f85abd9

def ULong__toDouble-impl(this):
    return ulongToDouble((special)(this))

def ULong__toString-impl(this):
    return ulongToString((special)(this))

def ULong__hashCode-impl(this):
    return hashCode()

def ULong__equals-impl(this, other):
    if jsNot(jsInstanceOf(other, jsClass())):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@7a0f1f9d
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@462d4f3c:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@5002aa66
    
    tmp0_other_with_cast = visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@17b41d39
    if jsNot(equals(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@443b9ebb)):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@d98ce13
    
    return visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@4865434e

class ULong:
    pass

def toULong():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@337a9406

def toULong():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@ebe20fd

def toULong():
    return doubleToULong(<this>)

def toULong():
    return doubleToULong(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@4b787980)

def toULong():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@75723fe1

def toULong():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@f46fff6

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@3f0c46e8

def special($this, specialArg):
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@4d437408

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@17d75ecc

def special(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@140fa482

def special(size):
    tmp = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@2b488a42
    return tmp

def ULongArray__get-impl(this, index):
    tmp0_toULong_0 = jsArrayGet((special)(this), index)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@1ccc4cc5

def ULongArray__set-impl(this, index, value):
    tmp = (special)(this)
    jsArraySet(tmp, index, (special)(value))

def special(this):
    return jsArrayLength((special)(this))

def ULongArray__iterator-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@1dcc0bb8

class Iterator:
    pass

def ULongArray__contains-impl(this, element):
    tmp = visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@3a23241e
    if jsNot(jsInstanceOf(tmp, jsClass())):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@64641998
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@18cf55df:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@3c193a5a
    
    tmp = (special)(this)
    return contains((special)(element))

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
    return jsEqeqeq(jsArrayLength((special)(this)), 0)

def ULongArray__toString-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrStringConcatenationImpl@50bdd956

def ULongArray__hashCode-impl(this):
    return hashCode(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@1174ff02)

def ULongArray__equals-impl(this, other):
    if jsNot(jsInstanceOf(other, jsClass())):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@f776b4a
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@8d902f:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@6414b660
    
    tmp0_other_with_cast = visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@62144e81
    if jsNot(equals(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@7e9ea888, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@7e4a6afd)):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@7ab8f93
    
    return visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@14c7ab73

class ULongArray:
    pass

class Companion:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@2f73cc9d
def Companion_getInstance():
    if jsEqeq(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@7ba44d2d, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@6614987b):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@7bb8ede7
    
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@2421fd62

class ULongRange:
    pass

class Companion:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@25af5c7f
def Companion_getInstance():
    if jsEqeq(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@498ae73c, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@58d5bdb0):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@9162869
    
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@3e9feb92

class ULongProgression:
    pass

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@64c9a84b

def special($this, specialArg):
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@6f1c9f54

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@595ebb98

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@4404dee7

def special($this, specialArg):
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@372f005a

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@218cf600

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
    if jsGt(compareTo(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4919cfcf), 0):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@286dba42
    
    if jsLt(compareTo(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@3a702dcc), 0):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@7fafb60
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@40e41f88:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@76b24f7b
    
    return tmp

def differenceModulo(a, b, c):
    ac = uintRemainder(a, c)
    bc = uintRemainder(b, c)
    tmp
    if jsGtEq(uintCompare((special)(ac), (special)(bc)), 0):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@43addda0
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@630a32f8:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@5344604d
    
    return tmp

def differenceModulo(a, b, c):
    ac = ulongRemainder(a, c)
    bc = ulongRemainder(b, c)
    tmp
    if jsGtEq(ulongCompare((special)(ac), (special)(bc)), 0):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@429a6f95
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@7fad58f8:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@4939730c
    
    return tmp

def special(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@4d25943d

class Companion:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@5938d600
def Companion_getInstance():
    if jsEqeq(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@79aac496, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@5a6e1f51):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5c2424a0
    
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@1faa627c

def UShort__compareTo-impl(this, other):
    tmp = jsBitAnd(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@a7adeb1, 65535)
    return compareTo(tmp, jsBitAnd(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@11a02447, 255))

def UShort__compareTo-impl(this, other):
    tmp = jsBitAnd(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@62b81449, 65535)
    return compareTo(tmp, jsBitAnd(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@482f0077, 65535))

def UShort__compareTo-impl(this, other):
    tmp = unboxIntrinsic(this)
    return UShort__compareTo-impl(tmp, visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@48d60abd)

def UShort__compareTo-impl(this, other):
    tmp0_compareTo_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@64bc291b
    return uintCompare((special)(tmp0_compareTo_0), (special)(other))

def UShort__compareTo-impl(this, other):
    tmp0_compareTo_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@d5eed70
    return ulongCompare((special)(tmp0_compareTo_0), (special)(other))

def UShort__plus-impl(this, other):
    tmp0_plus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5c3c0e5
    tmp1_plus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@263f26b3
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@1460c688

def UShort__plus-impl(this, other):
    tmp0_plus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@66c8c875
    tmp1_plus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4d256e0
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@e51fa39

def UShort__plus-impl(this, other):
    tmp0_plus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@74eed145
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@6572bcb5

def UShort__plus-impl(this, other):
    tmp0_plus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@42b4b037
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@37a2806c

def UShort__minus-impl(this, other):
    tmp0_minus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@b27b17d
    tmp1_minus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@7d8b1735
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5c72271e

def UShort__minus-impl(this, other):
    tmp0_minus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@40429f12
    tmp1_minus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@268e6451
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5286aa41

def UShort__minus-impl(this, other):
    tmp0_minus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@1881fb7d
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4f0ee1eb

def UShort__minus-impl(this, other):
    tmp0_minus_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@1da074ef
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@bf1b11f

def UShort__times-impl(this, other):
    tmp0_times_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@2a63cd84
    tmp1_times_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@6c6664c4
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@60a44e4

def UShort__times-impl(this, other):
    tmp0_times_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@69a3e1ef
    tmp1_times_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@6c7b518b
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@3fc6ae7b

def UShort__times-impl(this, other):
    tmp0_times_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@7cfc07ef
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4f00ee48

def UShort__times-impl(this, other):
    tmp0_times_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@402fd8ab
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@57b9ccc3

def UShort__div-impl(this, other):
    tmp0_div_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@13190f44
    tmp1_div_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5fedaf7c
    return uintDivide(tmp0_div_0, tmp1_div_0)

def UShort__div-impl(this, other):
    tmp0_div_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4560dbd2
    tmp1_div_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@717b03be
    return uintDivide(tmp0_div_0, tmp1_div_0)

def UShort__div-impl(this, other):
    tmp0_div_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@6477d129
    return uintDivide(tmp0_div_0, other)

def UShort__div-impl(this, other):
    tmp0_div_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@691cc52c
    return ulongDivide(tmp0_div_0, other)

def UShort__rem-impl(this, other):
    tmp0_rem_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@1e7e67d3
    tmp1_rem_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@6b584b8c
    return uintRemainder(tmp0_rem_0, tmp1_rem_0)

def UShort__rem-impl(this, other):
    tmp0_rem_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@28a186e4
    tmp1_rem_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@d67e1c5
    return uintRemainder(tmp0_rem_0, tmp1_rem_0)

def UShort__rem-impl(this, other):
    tmp0_rem_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@11ce721f
    return uintRemainder(tmp0_rem_0, other)

def UShort__rem-impl(this, other):
    tmp0_rem_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@24a99b1c
    return ulongRemainder(tmp0_rem_0, other)

def UShort__inc-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4a73cc75

def UShort__dec-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@54385172

def UShort__rangeTo-impl(this, other):
    tmp = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@6b1e1a07
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@13a5e115

def UShort__and-impl(this, other):
    tmp0_and_0 = (special)(this)
    tmp1_and_0 = (special)(other)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@8be6fcf

def UShort__or-impl(this, other):
    tmp0_or_0 = (special)(this)
    tmp1_or_0 = (special)(other)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5b5954bd

def UShort__xor-impl(this, other):
    tmp0_xor_0 = (special)(this)
    tmp1_xor_0 = (special)(other)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@1a27077c

def UShort__inv-impl(this):
    tmp0_inv_0 = (special)(this)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@61349cdd

def UShort__toByte-impl(this):
    return toByte((special)(this))

def UShort__toShort-impl(this):
    return (special)(this)

def UShort__toInt-impl(this):
    return jsBitAnd(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@5615f2ac, 65535)

def UShort__toLong-impl(this):
    return and(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@46329e85)

def UShort__toUByte-impl(this):
    tmp0_toUByte_0 = (special)(this)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5d1b7a57

def UShort__toUShort-impl(this):
    return this

def UShort__toUInt-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@39fb9d55

def UShort__toULong-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@275e7b06

def UShort__toFloat-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@5c652a4e

def UShort__toDouble-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@2f193ff4

def UShort__toString-impl(this):
    return toString()

def UShort__hashCode-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@6bc1c8d0

def UShort__equals-impl(this, other):
    if jsNot(jsInstanceOf(other, jsClass())):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@6015c745
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@71e55649:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@3810e141
    
    tmp0_other_with_cast = visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@65eb16f7
    if jsNot(jsEqeqeq(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@6c27be1d, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@51a06fd5)):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@776b7fa2
    
    return visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@2403c1c5

class UShort:
    pass

def toUShort():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4fbfc86f

def toUShort():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@6796ec2b

def toUShort():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@52cd1595

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@50ed196f

def special($this, specialArg):
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@342b545a

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@79eaf64

def special(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@e196238

def special(size):
    tmp = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@6b3d3a9a
    return tmp

def UShortArray__get-impl(this, index):
    tmp0_toUShort_0 = jsArrayGet((special)(this), index)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@9d43cf

def UShortArray__set-impl(this, index, value):
    tmp = (special)(this)
    jsArraySet(tmp, index, (special)(value))

def special(this):
    return jsArrayLength((special)(this))

def UShortArray__iterator-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@216de23a

class Iterator:
    pass

def UShortArray__contains-impl(this, element):
    tmp = visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@487969d
    if jsNot(jsInstanceOf(tmp, jsClass())):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@900ffc4
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@429691:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@af4d246
    
    tmp = (special)(this)
    return contains((special)(element))

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
    return jsEqeqeq(jsArrayLength((special)(this)), 0)

def UShortArray__toString-impl(this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrStringConcatenationImpl@19ed6130

def UShortArray__hashCode-impl(this):
    return hashCode(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@75128cf)

def UShortArray__equals-impl(this, other):
    if jsNot(jsInstanceOf(other, jsClass())):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@19412eef
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@485aa0d9:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@79832158
    
    tmp0_other_with_cast = visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@5ca69552
    if jsNot(equals(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@24244ea, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@67c61551)):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@6bbff652
    
    return visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@45ea6c24

class UShortArray:
    pass

def uintCompare(v1, v2):
    return compareTo(jsBitXor(v1, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@57f28893), jsBitXor(v2, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@4e949342))

def uintDivide(v1, v2):
    tmp = and(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@31a19d25)
    tmp0_toUInt_0 = div(and(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@62d6caf9))
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@2cb6bc65

def uintRemainder(v1, v2):
    tmp = and(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@29cd9511)
    tmp0_toUInt_0 = rem(and(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@6ed68a2e))
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@2af733b5

def uintToDouble(v):
    return jsPlus(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@4856ec9, jsMult(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@1085fad8, 2))

def ulongCompare(v1, v2):
    return compareTo(xor(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@692e4a35))

def ulongDivide(v1, v2):
    dividend = (special)(v1)
    divisor = (special)(v2)
    if jsLt(compareTo(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4b9f2522), 0):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@67c912d3
    
    if jsGtEq(compareTo(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@47c81691), 0):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@78c9c38a
    
    quotient = shl(1)
    rem = minus(times(divisor))
    tmp
    tmp0_compareTo_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@331da721
    tmp1_compareTo_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@64c79b69
    if jsGtEq(ulongCompare((special)(tmp0_compareTo_0), (special)(tmp1_compareTo_0)), 0):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@5e17bdb1
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@22bf3c03:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@41a6e7d0
    
    tmp2_plus_0 = tmp
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@729eef5f

def ulongRemainder(v1, v2):
    dividend = (special)(v1)
    divisor = (special)(v2)
    if jsLt(compareTo(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@782f208e), 0):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@3fe7c87c
    
    if jsGtEq(compareTo(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4733b248), 0):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@1899c7ae
    
    quotient = shl(1)
    rem = minus(times(divisor))
    tmp
    tmp0_compareTo_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4d6f951a
    tmp1_compareTo_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@6ade4ac6
    if jsGtEq(ulongCompare((special)(tmp0_compareTo_0), (special)(tmp1_compareTo_0)), 0):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@6b907f80
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@e93f8b4:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@6617fa99
    
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4700064f

def ulongToDouble(v):
    return jsPlus(jsMult(toDouble(), 2048), toDouble())

def ulongToString(v):
    return ulongToString(v, 10)

def ulongToString(v, base):
    if jsGtEq(compareTo(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5f63e1c9), 0):
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
    if visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@1f5816bb:
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
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@59c82fb6

def DeprecationLevel_ERROR_getInstance():
    DeprecationLevel_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@27af34df

def DeprecationLevel_HIDDEN_getInstance():
    DeprecationLevel_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@30dd7cc5

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

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@20c411ea

def special($this, specialArg):
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@41143491

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@25b4304c

def special($this, specialArg):
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@7516aa4

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@60e50c6

class IntProgressionIterator:
    pass

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@7220d10c

def special($this, specialArg):
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@321fc4c5

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@60734e93

def special($this, specialArg):
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@5ca3308c

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@3c2e5c75

class LongProgressionIterator:
    pass

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@235632a6

def special($this, specialArg):
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@5cb20350

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@d7da0ae

def special($this, specialArg):
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@5046ad1c

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@26ee7676

class CharProgressionIterator:
    pass

class Companion:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@2c13db34
def Companion_getInstance():
    if jsEqeq(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@42b09d68, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@55398902):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@35ddc99b
    
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@1dc0f59d

class IntProgression:
    pass

class Companion:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@79bc0ceb
def Companion_getInstance():
    if jsEqeq(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@7c362e56, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@129e23fc):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@714245ff
    
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@777898ff

class LongProgression:
    pass

class Companion:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@73858ba
def Companion_getInstance():
    if jsEqeq(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@37cac511, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@68b4e3a1):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@315c13b4
    
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@7dbafe9d

class CharProgression:
    pass

class ClosedRange:
    pass

class Companion:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@4679df4b
def Companion_getInstance():
    if jsEqeq(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@1cf516fa, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@5b96272e):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4c5c8926
    
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@5ed59e7f

class IntRange:
    pass

class Companion:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@60e4d95
def Companion_getInstance():
    if jsEqeq(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@75f929a0, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@461b078f):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@35f0652c
    
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@3af91e7e

class LongRange:
    pass

class Companion:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@5e2975ff
def Companion_getInstance():
    if jsEqeq(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@68fab818, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@3b48e216):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@65e8bcef
    
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@1fdedffb

class CharRange:
    pass

class Unit:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@2dac0733
def Unit_getInstance():
    if jsEqeq(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@be74f53, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@6b2f16b9):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@67d15f2
    
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@2e1e02b8

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
    if visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@2568c451:
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
    if visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@7fda0e89:
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
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@325401b3

def AnnotationTarget_ANNOTATION_CLASS_getInstance():
    AnnotationTarget_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@62e3dba0

def AnnotationTarget_TYPE_PARAMETER_getInstance():
    AnnotationTarget_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@2d2c3ab2

def AnnotationTarget_PROPERTY_getInstance():
    AnnotationTarget_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@2b05257a

def AnnotationTarget_FIELD_getInstance():
    AnnotationTarget_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@5c5761f

def AnnotationTarget_LOCAL_VARIABLE_getInstance():
    AnnotationTarget_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@316296ae

def AnnotationTarget_VALUE_PARAMETER_getInstance():
    AnnotationTarget_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@28647ac7

def AnnotationTarget_CONSTRUCTOR_getInstance():
    AnnotationTarget_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@5d3658d1

def AnnotationTarget_FUNCTION_getInstance():
    AnnotationTarget_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@7eed8467

def AnnotationTarget_PROPERTY_GETTER_getInstance():
    AnnotationTarget_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@31d635ba

def AnnotationTarget_PROPERTY_SETTER_getInstance():
    AnnotationTarget_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@231a5622

def AnnotationTarget_TYPE_getInstance():
    AnnotationTarget_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@f62fe59

def AnnotationTarget_EXPRESSION_getInstance():
    AnnotationTarget_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@2e0d2cc4

def AnnotationTarget_FILE_getInstance():
    AnnotationTarget_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@7f5c7538

def AnnotationTarget_TYPEALIAS_getInstance():
    AnnotationTarget_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@27b88459

def AnnotationRetention_SOURCE_getInstance():
    AnnotationRetention_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@2f4c5b51

def AnnotationRetention_BINARY_getInstance():
    AnnotationRetention_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@56d87044

def AnnotationRetention_RUNTIME_getInstance():
    AnnotationRetention_initEntries()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@525d09b7

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
    if jsGt(compareTo(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5a93dccc), 0):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@350e34e7
    
    if jsLt(compareTo(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@13365eb9), 0):
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
    if jsEqeq(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@55e1ac0f, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@46c805be):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4150175
    
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@58721f69

class ShortCompanionObject:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@551e9796
def ShortCompanionObject_getInstance():
    if jsEqeq(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@4969b90d, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@287213ac):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@74b8bc34
    
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@6d30d79b

class IntCompanionObject:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@3b10c5d
def IntCompanionObject_getInstance():
    if jsEqeq(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@3c255b01, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@88d9da0):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@76022ebd
    
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@464cbc59

class FloatCompanionObject:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@104305f
def FloatCompanionObject_getInstance():
    if jsEqeq(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@765ea1ac, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@38cac3f9):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@642bd75c
    
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@29fea6c2

class DoubleCompanionObject:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@2e643cad
def DoubleCompanionObject_getInstance():
    if jsEqeq(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@52e494a2, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@281b0f38):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@2bde6971
    
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@7545c015

class StringCompanionObject:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@4e51a9f3
def StringCompanionObject_getInstance():
    if jsEqeq(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@44798d81, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@605d67f8):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@6e56373e
    
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@65a381ce

class BooleanCompanionObject:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@2cbad233
def BooleanCompanionObject_getInstance():
    if jsEqeq(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@72435def, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@34289e5f):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@363843e
    
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@663a2b13

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
    array = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@3a74b2f1
    iterator = iterator()
    while hasNext():
        visitExpression org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@27ae6f9e
    
    return array

def copyToArrayImpl(collection, array):
    if jsLt(jsArrayLength(array), (special)()):
        visitComposite-inToPyExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrCompositeImpl@1cc552fe
    
    iterator = iterator()
    index = 0
    while hasNext():
        tmp0 = index
        index = jsBitOr(jsPlus(tmp0, 1), 0)
        tmp1_unsafeCast_0 = next()
        jsArraySet(array, tmp0, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@75ab999f)
    
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
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@48821e3c
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@7e860a11

def <no name provided>$factory($elements):
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@2a7eb66e
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@1eb2d718

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@2f2fda15

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@74a930

def special($this, specialArg):
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@3d6aa682

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@15f67a4f

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
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@60c952ea
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@4b5c0183

def <no name provided>$factory($elements):
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5ba3e590
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@7169c184

def special($this, specialArg):
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@221ae367

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@6ae9b2f0

def special($this, specialArg):
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@e0895b3

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@6f45a719

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
    checkElementIndex(index, (special)())
    return index

def insertionRangeCheck($this, index):
    checkPositionIndex(index, (special)())
    return index

class ArrayList:
    pass

def special(specialArg):
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@2a6dfbb2

def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@24a4e9c0

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@165634aa
class RandomAccess:
    pass

def special(specialArg):
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@2f6fcc70

def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@4300b54c

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@20bc6f4d
class BaseOutput:
    pass

class NodeJsOutput:
    pass

class BufferedOutputToConsoleLog:
    pass

def String(value):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@66bf08d

class BufferedOutput:
    pass

def println(message):
    println(message)

def output$init$():
    isNode_2 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@61c3d248
    return visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@50a59a0b

def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@4e1ffe54

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@6c07666f
class <no name provided>_1:
    pass

def EmptyContinuation$init$():
    tmp0_Continuation_0 = EmptyCoroutineContext_getInstance()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4008caaf

def asDynamic():
    return <this>

def unsafeCast():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@19eb658

def unsafeCast():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@245237eb

class Serializable:
    pass

def pow(n):
    return pow(<this>, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@402af74)

def isNaN():
    return jsNot(jsEqeqeq(<this>, <this>))

def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@213f2d00

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@57ab7b32
def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@640890bc

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@1606ecbb
def INV_2_26$init$():
    tmp0_pow_0 = visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@5bb00dcc
    tmp1_pow_0 = -26
    return pow(tmp0_pow_0, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@54c04642)

def INV_2_53$init$():
    tmp0_pow_0 = visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@55732ae6
    tmp1_pow_0 = -53
    return pow(tmp0_pow_0, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@6479596)

def special():
    return (special)()

class KCallable:
    pass

class KClass:
    pass

class KClassImpl:
    pass

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@27815329

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@79251dae

class PrimitiveKClassImpl:
    pass

class NothingKClassImpl:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@5e9feddd
def NothingKClassImpl_getInstance():
    if jsEqeq(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@2eac48ea, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@1bad6995):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@8c790e7
    
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@b7a9093

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
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@62a9d176

def createDynamicKType():
    return DynamicKType_getInstance()

def createKTypeParameter(name, upperBounds, variance):
    tmp0_subject = variance
    kVariance = visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@363f986e
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@7a461744

def getStarKTypeProjection():
    return (special)()

def createCovariantKTypeProjection(type):
    return covariant(type)

def createInvariantKTypeProjection(type):
    return invariant(type)

def createContravariantKTypeProjection(type):
    return contravariant(type)

def asString($this):
    if jsEqeq(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@5398ece7, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@7879e3ac):
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
    if jsEqeq(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@2c6062bd, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@6270fadb):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@2cee7445
    
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@7acec6db

def <no name provided>$factory(this$0):
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@38106bc4
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@6ff36ec8

class KTypeParameterImpl:
    pass

def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@24663d05

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
    if jsEqeq(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@4a3cc680, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@79703b86):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@2f8892c5
    
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@288aaeaf

def <no name provided>$factory():
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4c7108ce
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@11ec85a0

def <no name provided>$factory():
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@17774484
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@2c69eec5

def <no name provided>$factory():
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@9d45e6e
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@24766217

def <no name provided>$factory():
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@37f5c0cf
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@669cb3c7

def <no name provided>$factory():
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@29b66bf7
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@3411ba50

def <no name provided>$factory():
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@40b5dbe9
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@39c65ffc

def <no name provided>$factory():
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@27cde156
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@5916507e

def <no name provided>$factory():
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@65951393
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@4d583069

def <no name provided>$factory():
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4fb5590e
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@26bc84dc

def <no name provided>$factory():
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@34beebe0
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@7c26f301

def <no name provided>$factory():
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@343047c
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@291be813

def <no name provided>$factory():
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@44ce4591
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@5961a37e

def <no name provided>$factory():
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@3e97cdeb
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@7124d407

def <no name provided>$factory():
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@575baeea
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@153daff

def <no name provided>$factory():
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@3b69ad19
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@28af99b4

def <no name provided>$factory():
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@119ec2e4
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@27937c21

def <no name provided>$factory():
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@58d1e6ed
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@587efefa

def <no name provided>$factory():
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@b18d1ff
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@1b5b5ac9

def <no name provided>$factory():
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@59b47d06
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@77025469

def <no name provided>$factory($arity):
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4432c7bd
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@6c882cb4

def functionClasses$init$():
    tmp0_arrayOfNulls_0 = 0
    return fillArrayVal(Array(tmp0_arrayOfNulls_0), visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@20de2518)

def getKClass(jClass):
    tmp
    if visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@122dc222:
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
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@7ad0cf01

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

def special($this, specialArg):
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@6546c39

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@2310e8a4

def checkReplaceRange($this, startIndex, endIndex, length):
    if visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@22249b41:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@356feae3
    
    if jsGt(startIndex, endIndex):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@5f3e12fc
    

class StringBuilder:
    pass

def isLowSurrogate():
    containsLower = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@2646531d
    return visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@de7336d

def isHighSurrogate():
    containsLower = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@412077c9
    return visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@66f39429

def checkRadix(radix):
    if jsNot(visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@1612fdb6):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@6924ff83
    
    return radix

def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@5e9c6d8a

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@3cc148d
def nativeLastIndexOf(str, fromIndex):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@60789398

def substring(startIndex, endIndex):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@7a3655b4

def substring(startIndex):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@54f10c5c

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
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@6b61b3a8

def toLowerCase():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@4ac5dcd8

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
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@df98e69
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrFunctionExpressionImpl@da3cab

def STRING_CASE_INSENSITIVE_ORDER$init$():
    tmp = <no name provided>$factory()
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@7d8e1e59

def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@474f69d

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@79927a7c
def REPLACEMENT_BYTE_SEQUENCE$init$():
    tmp0_byteArrayOf_0 = int8ArrayOf(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrVarargImpl@3d29a22d)
    return tmp0_byteArrayOf_0

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@3210454

class Companion:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@d57ba2a
def Companion_getInstance():
    if jsEqeq(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@571ae6d5, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@48b5a380):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@54a336d8
    
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@1c0293a

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
    if jsEqeq(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@34e79514, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@258cb16c):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@3663806a
    
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@40fc9cce

class Enum:
    pass

def byteArrayOf(elements):
    return elements

def arrayOf(elements):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@662c71e5

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
    if jsEqeq(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@1db078d9, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@89d4a1a):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@9fd26ec
    
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@138c53c7

def fillArrayVal(array, initValue):
    inductionVariable = 0
    last = jsBitOr(jsMinus(jsArrayLength(array), 1), 0)
    if jsLtEq(inductionVariable, last):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDoWhileLoopImpl@513b730
    
    return array

def arrayWithFun(size, init):
    tmp0_fillArrayFun_0 = Array(size)
    result_1 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@40c87228
    i_2 = 0
    while jsNot(jsEqeqeq(i_2, jsArrayLength(result_1))):
        jsArraySet(result_1, i_2, invoke(i_2))
        i_2 = jsBitOr(jsPlus(i_2, 1), 0)
        Unit_getInstance()
    
    return result_1

def fillArrayFun(array, init):
    result = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@210b558d
    i = 0
    while jsNot(jsEqeqeq(i, jsArrayLength(result))):
        jsArraySet(result, i, invoke(i))
        i = jsBitOr(jsPlus(i, 1), 0)
        Unit_getInstance()
    
    return result

def arrayIterator(array):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@3c2fdd04

def booleanArrayIterator(array):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@2b96d5ea

def charArrayIterator(array):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5daa2392

def byteArrayIterator(array):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@472e1f2f

def shortArrayIterator(array):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@8b55c50

def intArrayIterator(array):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@48b5669c

def floatArrayIterator(array):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@47f76ade

def longArrayIterator(array):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5daf5ea5

def doubleArrayIterator(array):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@21fdc052

def booleanArray(size):
    tmp0_withType_0 = 'BooleanArray'
    tmp1_withType_0 = fillArrayVal(Array(size), visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@319fe034)
    visitExpression org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@34b2a6f4
    tmp2_unsafeCast_0 = tmp1_withType_0
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@1f69063

def charArray(size):
    tmp0_withType_0 = 'CharArray'
    tmp1_withType_0 = fillArrayVal(Array(size), visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@6621ab0c)
    visitExpression org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@263ac7
    tmp2_unsafeCast_0 = tmp1_withType_0
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@42501284

def longArray(size):
    tmp0_withType_0 = 'LongArray'
    tmp1_withType_0 = fillArrayVal(Array(size), visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@30f71b30)
    visitExpression org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@5138d63a
    tmp2_unsafeCast_0 = tmp1_withType_0
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@dac317c

def booleanArrayOf(arr):
    tmp0_withType_0 = 'BooleanArray'
    tmp1_withType_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@50ca509b
    visitExpression org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@45af5362
    tmp2_unsafeCast_0 = tmp1_withType_0
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@5e5a6217

def charArrayOf(arr):
    tmp0_withType_0 = 'CharArray'
    tmp1_withType_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@3e6f3ad5
    visitExpression org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@1e832e79
    tmp2_unsafeCast_0 = tmp1_withType_0
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@a98a875

def longArrayOf(arr):
    tmp0_withType_0 = 'LongArray'
    tmp1_withType_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@597050fa
    visitExpression org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@26d49375
    tmp2_unsafeCast_0 = tmp1_withType_0
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@31cc510d

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

def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@54543211

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@36dd68f1
def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@13623138

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@45b244c4
def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@34ef9879

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@297840d7
def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@1e6a74fe

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@fcecc45
def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@2cde0397

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@77199818
def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@1cea4fdf

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@308bd473
def getNumberHashCode(obj):
    tmp0_unsafeCast_0 = jsBitwiseOr(obj, 0)
    if jsEqeqeq(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@26154a00, obj):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@79e2aa2d
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@505806c8:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@6d237951
    
    jsArraySet(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@25cb46d8, 0, obj)
    return jsBitOr(jsPlus(imul(jsArrayGet(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@2596ae35, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@358b0b42), 31), jsArrayGet(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@59fbfc5d, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@498c0651)), 0)

def bufFloat64$init$():
    tmp0_unsafeCast_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@72cec2e2
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@6efd96c7

def bufFloat32$init$():
    tmp0_unsafeCast_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@52d1bb9c
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@2ae85262

def bufInt32$init$():
    tmp0_unsafeCast_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@5f8a0d7f
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@19d4057

def lowIndex$init$():
    jsArraySet(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@6aa2599f, 0, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@434fa353)
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
    i = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@781e2388
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
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@2bcb8c82

def identityHashCode(obj):
    return getObjectHashCode(obj)

def getObjectHashCode(obj):
    if jsNot(jsIn('kotlinHashCodeValue$', visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@75cbb215)):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@4e38b4ea
    
    tmp0_unsafeCast_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@3f41a1f3
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@220700c1

def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@49a6b730

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@7828111d
def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@2680474c

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
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@1475268a

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
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@730fcd33

def isUndefined(value):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@562b791b

def extendThrowable(this_, message, cause):
    visitExpression org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@7c87c960
    setPropertiesToThrowableInstance(this_, message, cause)

def setPropertiesToThrowableInstance(this_, message, cause):
    if jsNot(hasOwnPrototypeProperty(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@79d55957, 'message')):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@4c55d3ce
    
    if jsNot(hasOwnPrototypeProperty(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@60d4e243, 'cause')):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@48dbf9d
    
    visitExpression org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@7e4f42c0

def hasOwnPrototypeProperty(o, name):
    tmp0_unsafeCast_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@7ec53f8f
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@1b2b2b6d

def getContinuation():
    visitThrow org.jetbrains.kotlin.ir.expressions.impl.IrThrowImpl@736ded17

def returnIfSuspended(argument):
    visitThrow org.jetbrains.kotlin.ir.expressions.impl.IrThrowImpl@cdf3ee2

def suspendCoroutineUninterceptedOrReturnJS(block):
    return invoke(getContinuation())

def getCoroutineContext():
    return (special)()

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
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@336e1bcf

def enumValueOfIntrinsic(name):
    visitThrow org.jetbrains.kotlin.ir.expressions.impl.IrThrowImpl@faff2bf

def enumValuesIntrinsic():
    visitThrow org.jetbrains.kotlin.ir.expressions.impl.IrThrowImpl@4310007c

class Companion:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@1e5066ac
def Companion_getInstance():
    if jsEqeq(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@48811d85, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@361069db):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@168f1f0f
    
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@571362c4

class Long:
    pass

def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@24537e30

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@31fd8e6f
def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@6f4327ab

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@3c833d43
def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@7a0619a8

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@6472dd0c
def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@42f2c28d

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@6b3b9a19
def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@611f8128

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@5a8a50b8
def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@47e7eb7

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@374d3128
def compare(other):
    if equalsLong(other):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@7dd63fcc
    
    thisNeg = isNegative()
    otherNeg = isNegative()
    return visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@45a935e5

def add(other):
    a48 = jsBitShiftRU(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@2bd733ad, 16)
    a32 = jsBitAnd(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@885620d, 65535)
    a16 = jsBitShiftRU(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@12cd9e08, 16)
    a00 = jsBitAnd(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@70841eba, 65535)
    b48 = jsBitShiftRU(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@2281ede7, 16)
    b32 = jsBitAnd(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@358bf5fe, 65535)
    b16 = jsBitShiftRU(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@54eb65bc, 16)
    b00 = jsBitAnd(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@90967b3, 65535)
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
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@61f26cba

def subtract(other):
    return add(unaryMinus())

def multiply(other):
    if isZero():
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@15e8918
    
    if isZero():
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@306cb0a0
    
    if equalsLong(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@6615cc2e):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@533053b4
    
    if equalsLong(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@4ec0f36e):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@62f11904
    
    if isNegative():
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@72722a6b
    
    if isNegative():
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@6074f8f9
    
    if visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@6a7ba38b:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@651a3e01
    
    a48 = jsBitShiftRU(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@7f5c74db, 16)
    a32 = jsBitAnd(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@26827f2e, 65535)
    a16 = jsBitShiftRU(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@34e7832d, 16)
    a00 = jsBitAnd(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@57b2e99, 65535)
    b48 = jsBitShiftRU(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@2ba83c41, 16)
    b32 = jsBitAnd(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@6d31bae5, 65535)
    b16 = jsBitShiftRU(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@55f2a26d, 16)
    b00 = jsBitAnd(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@16987824, 65535)
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
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@39c78cf9

def divide(other):
    if isZero():
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@46969355
    
    if isZero():
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@2b4b3918
    
    if equalsLong(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@5e5978e5):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@71103416
    
    if equalsLong(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@586b59b4):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@2f9bd5ac
    
    if isNegative():
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@eb3b4d7
    
    if isNegative():
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@56d5a50f
    
    res = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@422a2263
    rem = <this>
    while greaterThanOrEqual(other):
        approxDouble = jsDiv(toNumber(), toNumber())
        approx2 = max(visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@4d400e77, floor(approxDouble))
        log2 = ceil(jsDiv(log(approx2), (special)()))
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
    return jsPlus(jsMult(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@344520ce, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@35f15782), getLowBitsUnsigned())

def equalsLong(other):
    return visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@23efa674

def hashCode(l):
    return jsBitXor(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@54d6c1e6, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@3c91189)

def toStringImpl(radix):
    if visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@13a09d37:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@279afa4e
    
    if isZero():
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@16209621
    
    if isNegative():
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@2c47135c
    
    radixToPower = fromNumber(pow(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@1ba44388, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@5e077a32))
    rem = <this>
    result = ''
    while visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@7fb57b7c:
        remDiv = div(radixToPower)
        intval = toInt()
        tmp1_unsafeCast_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@51edc97d
        digits = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@4c18a316
        rem = remDiv
        if isZero():
            visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@6c861b25
        
        if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@3c05fb12:
            visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@702f99a5
        
    

def fromInt(value):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4ba61340

def isNegative():
    return jsLt(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@57368c72, 0)

def isZero():
    return visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@2330861e

def isOdd():
    return jsEqeqeq(jsBitAnd(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@384f8455, 1), 1)

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

def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@721fbae2

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@60e72ced
def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@4ee6b207

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@65653da2
def imul(a_local, b_local):
    lhs = jsMult(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@303bbd02, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@1c55237e)
    rhs = jsMult(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@37904d56, visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@5a2e250b)
    return jsBitwiseOr(jsPlus(lhs, rhs), 0)

def withType(type, array):
    visitExpression org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@19503dfa
    return array

def arrayConcat(args):
    len = jsArrayLength(args)
    tmp0_unsafeCast_0 = js('Array(len)')
    typed = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@1a63f9ea
    inductionVariable = 0
    last = jsBitOr(jsMinus(len, 1), 0)
    if jsLtEq(inductionVariable, last):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDoWhileLoopImpl@388f2bca
    
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@23b9d353

def primitiveArrayConcat(args):
    size_local = 0
    inductionVariable = 0
    last = jsBitOr(jsMinus(jsArrayLength(args), 1), 0)
    if jsLtEq(inductionVariable, last):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDoWhileLoopImpl@7ce9ec07
    
    a = jsArrayGet(args, 0)
    tmp1_unsafeCast_0 = js('new a.constructor(size_local)')
    result = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@17020207
    if visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@3ac09fe2:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@1a57bb34
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@6b92b8c9:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@2b8cd1d4
    
    size_local = 0
    inductionVariable = 0
    last = jsBitOr(jsMinus(jsArrayLength(args), 1), 0)
    if jsLtEq(inductionVariable, last):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDoWhileLoopImpl@f053608
    
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@40f65d8f

def taggedArrayCopy(array):
    res = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@3f114f13
    visitExpression org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@5b610c90
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@475193d4

def numberToByte(a):
    return toByte(numberToInt(a))

def toByte(a):
    tmp0_unsafeCast_0 = js('a << 24 >> 24')
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@5c8c1f0d

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
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@63c10f2d

def numberToShort(a):
    return toShort(numberToInt(a))

def toShort(a):
    tmp0_unsafeCast_0 = js('a << 16 >> 16')
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@514753f4

def numberToLong(a):
    tmp
    if jsInstanceOf(a, jsClass()):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@2f8a57c2
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@61d2ff30:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@7a8a2cd8
    
    return tmp

def numberToChar(a):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@3b21b0f5

def toLong(a):
    return fromInt(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@3e666559)

def numberRangeToNumber(start, endInclusive):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@4aebdaff

def numberRangeToLong(start, endInclusive):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@51470a6c

def special():
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@5a0379e2

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@55bd9d1
def metadataObject():
    return js('{ kind: 'class', interfaces: [] }')

def getPropertyCallableRef(name, paramCount, type, getter, setter):
    visitExpression org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@3c20af2
    visitExpression org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@7cb81ae
    visitExpression org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@3d872a12
    tmp0_unsafeCast_0 = getPropertyRefClass(getter, getKPropMetadata(paramCount, setter, type))
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@7c49fbd8

def getPropertyRefClass(obj, metadata):
    visitExpression org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@50853850
    visitExpression org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@38c6f088
    return obj

def getKPropMetadata(paramCount, setter, type):
    mdata = jsArrayGet(jsArrayGet(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@7a4a91f8, paramCount), visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@25471835)
    if visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@5cf21908:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@68b2ce71
    
    return mdata

def getLocalDelegateReference(name, type, mutable, lambda):
    return getPropertyCallableRef(name, 0, type, lambda, visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@2d1e3187)

def propertyRefClassMetadataCache$init$():
    tmp = js('{ kind: 'class', interfaces: [] }')
    tmp0_arrayOf_0 = arrayLiteral(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrVarargImpl@81ebdb0)
    tmp = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@1ab37c94
    tmp = js('{ kind: 'class', interfaces: [] }')
    tmp1_arrayOf_0 = arrayLiteral(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrVarargImpl@76fee3de)
    tmp = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@33176d2e
    tmp = js('{ kind: 'class', interfaces: [] }')
    tmp2_arrayOf_0 = arrayLiteral(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrVarargImpl@71efa55d)
    tmp3_arrayOf_0 = arrayLiteral(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrVarargImpl@7dcbb6e5)
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@3064af47

def isArrayish(o):
    tmp
    if isJsArray(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@17d30e9d):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@2f6a30d2
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@4690132:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@6967bbf3
    
    return tmp

def isJsArray(obj):
    tmp0_unsafeCast_0 = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicOperatorExpressionImpl@30cf61ca
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@383176e1

def isInterface(obj, iface):
    tmp0_elvis_lhs = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrDynamicMemberExpressionImpl@5b5b9038
    tmp
    if jsEqeq(tmp0_elvis_lhs, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@2a09e0d4):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@2664d94
    
    if visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@4064cd60:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@1e7fcf3a
    
    ctor = tmp
    return isInterfaceImpl(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@6e4667af, iface)

def isInterfaceImpl(ctor, iface):
    if jsEqeqeq(ctor, iface):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrReturnImpl@65bcc339
    
    metadata = (special)()
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
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@58bf45ca

def plus(elements):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@bbb5f74

def copyOfRange(fromIndex, toIndex):
    checkRangeIndexes(fromIndex, toIndex, jsArrayLength(<this>))
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@2d5edbad

def minOf(a, b):
    return min(int32ArrayOf(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrVarargImpl@65a288e7))

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@365abbd

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@25d42dee

def special($this, specialArg):
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@73707d4

def special($this):
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@4ef5f92d

def releaseIntercepted($this):
    intercepted = visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@73e5c86e
    if visitWhen-inToByExpressionTransformer org.jetbrains.kotlin.ir.expressions.impl.IrWhenImpl@1e1f808c:
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrBlockImpl@6a49bf51
    
    visitSetField org.jetbrains.kotlin.ir.expressions.impl.IrSetFieldImpl@6ed4eacd

class CoroutineImpl:
    pass

class CompletedContinuation:
    pass

visitField org.jetbrains.kotlin.ir.declarations.persistent.PersistentIrField@41e8b043
def CompletedContinuation_getInstance():
    if jsEqeq(visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@15f6d246, visitConst-other org.jetbrains.kotlin.ir.expressions.impl.IrConstImpl@51110a39):
        visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrConstructorCallImpl@67cce6e8
    
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrGetFieldImpl@5efdf532

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
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@ad1c474

def jsBitwiseOr(lhs_hack, rhs_hack):
    tmp0_unsafeCast_0 = js('lhs_hack | rhs_hack')
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@dfba755

def jsTypeOf(value_hack):
    tmp0_unsafeCast_0 = js('typeof value_hack')
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@9069115

def jsInstanceOf(obj_hack, jsClass_hack):
    tmp0_unsafeCast_0 = js('obj_hack instanceof jsClass_hack')
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@3f6a96be

def jsBitwiseAnd(lhs_hack, rhs_hack):
    tmp0_unsafeCast_0 = js('lhs_hack & rhs_hack')
    return visitExpression-other org.jetbrains.kotlin.ir.expressions.impl.IrTypeOperatorCallImpl@533167f0

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
    
