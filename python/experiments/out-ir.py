def fold(initial, operation):
    accumulator = initial
    indexedObject = _this_
    inductionVariable = 0
    last = jsArrayLength(indexedObject)
    while jsLt(inductionVariable, last):
        element = jsArrayGet(indexedObject, inductionVariable)
        inductionVariable = jsBitOr(jsPlus(inductionVariable, 1), 0)
        accumulator = invoke(accumulator, element)
    
    return accumulator

def _get_indices_():
    return _init_(0, _get_lastIndex_())

def indexOf(element):
    if jsEqeq(element, None):
        inductionVariable = 0
        last = jsBitOr(jsMinus(jsArrayLength(_this_), 1), 0)
        if jsLtEq(inductionVariable, last):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_5fcf9bff
        
    
    if True:
        inductionVariable = 0
        last = jsBitOr(jsMinus(jsArrayLength(_this_), 1), 0)
        if jsLtEq(inductionVariable, last):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_7cb13e56
        
    
    return -1

def lastIndexOf(element):
    if jsEqeq(element, None):
        inductionVariable = jsBitOr(jsMinus(jsArrayLength(_this_), 1), 0)
        if jsLtEq(0, inductionVariable):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_688fa02f
        
    
    if True:
        inductionVariable = jsBitOr(jsMinus(jsArrayLength(_this_), 1), 0)
        if jsLtEq(0, inductionVariable):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_285290a1
        
    
    return -1

def _get_lastIndex_():
    return jsBitOr(jsMinus(jsArrayLength(_this_), 1), 0)

def joinToString(separator, prefix, postfix, limit, truncated, transform):
    return toString()

def joinToString_default(separator, prefix, postfix, limit, truncated, transform, _mask0, _handler):
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 1), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_54f3fd30
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 2), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_209c0be5
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 4), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_49ce2726
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 8), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_214ef199
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 16), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_680882bd
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 32), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_f5b079f
    
    return joinToString(kotlin_CharSequence(separator), kotlin_CharSequence(prefix), kotlin_CharSequence(postfix), limit, kotlin_CharSequence(truncated), transform)

def joinTo(buffer, separator, prefix, postfix, limit, truncated, transform):
    append(prefix)
    Unit_getInstance()
    count = 0
    indexedObject = _this_
    inductionVariable = 0
    last = jsArrayLength(indexedObject)
    while jsLt(inductionVariable, last):
        element = jsArrayGet(indexedObject, inductionVariable)
        inductionVariable = jsBitOr(jsPlus(inductionVariable, 1), 0)
        count = jsBitOr(jsPlus(count, 1), 0)
        if jsGt(count, 1):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_6a75d12
        
        if True:
            pass
        
        if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_73a815c2:
            appendElement(element, transform)
        
        if True:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrBreakImpl_71e2843b
        
    
    if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_16554f2e:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_14150a0a
    
    append(postfix)
    Unit_getInstance()
    return buffer

def joinTo_default(buffer, separator, prefix, postfix, limit, truncated, transform, _mask0, _handler):
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 2), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_2a063e1a
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 4), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_56d8f131
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 8), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_4fc6dcb7
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 16), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_84e1883
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 32), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_5f519714
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 64), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_3b05fba2
    
    return joinTo(buffer, kotlin_CharSequence(separator), kotlin_CharSequence(prefix), kotlin_CharSequence(postfix), limit, kotlin_CharSequence(truncated), transform)

def contains(element):
    return jsGtEq(indexOf(element), 0)

def indexOf(element):
    inductionVariable = 0
    last = jsBitOr(jsMinus(jsArrayLength(_this_), 1), 0)
    if jsLtEq(inductionVariable, last):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_14d25248
    
    return -1

def _get_indices_():
    return _init_(0, _get_lastIndex_())

def _get_lastIndex_():
    return jsBitOr(jsMinus(jsArrayLength(_this_), 1), 0)

def contains(element):
    return jsGtEq(indexOf(element), 0)

def indexOf(element):
    inductionVariable = 0
    last = jsBitOr(jsMinus(jsArrayLength(_this_), 1), 0)
    if jsLtEq(inductionVariable, last):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_1d05cbae
    
    return -1

def _get_indices_():
    return _init_(0, _get_lastIndex_())

def _get_lastIndex_():
    return jsBitOr(jsMinus(jsArrayLength(_this_), 1), 0)

def contains(element):
    return jsGtEq(indexOf(element), 0)

def indexOf(element):
    inductionVariable = 0
    last = jsBitOr(jsMinus(jsArrayLength(_this_), 1), 0)
    if jsLtEq(inductionVariable, last):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_7094dc0
    
    return -1

def _get_indices_():
    return _init_(0, _get_lastIndex_())

def _get_lastIndex_():
    return jsBitOr(jsMinus(jsArrayLength(_this_), 1), 0)

def contains(element):
    return jsGtEq(indexOf(element), 0)

def indexOf(element):
    inductionVariable = 0
    last = jsBitOr(jsMinus(jsArrayLength(_this_), 1), 0)
    if jsLtEq(inductionVariable, last):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_5c2463d8
    
    return -1

def _get_indices_():
    return _init_(0, _get_lastIndex_())

def _get_lastIndex_():
    return jsBitOr(jsMinus(jsArrayLength(_this_), 1), 0)

def indexOfFirst(predicate):
    index = 0
    tmp0_iterator = iterator()
    while hasNext():
        item = next()
        if invoke(item):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_3860542a
        
        tmp1 = index
        index = jsBitOr(jsPlus(tmp1, 1), 0)
        Unit_getInstance()
    
    return -1

def indexOfLast(predicate):
    iterator = listIterator(_get_size_())
    while hasPrevious():
        if invoke(previous()):
            return nextIndex()
        
    
    return -1

def any(predicate):
    tmp
    if isInterface(_this_, jsClass()):
        tmp = isEmpty()
    
    if True:
        if True:
            tmp = False
        
    
    if tmp:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_6dbcb435
    
    if True:
        pass
    
    tmp0_iterator = iterator()
    while hasNext():
        element = next()
        if invoke(element):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_4c5afa2d
        
    
    return False

def all(predicate):
    tmp
    if isInterface(_this_, jsClass()):
        tmp = isEmpty()
    
    if True:
        if True:
            tmp = False
        
    
    if tmp:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_7d3bf73f
    
    if True:
        pass
    
    tmp0_iterator = iterator()
    while hasNext():
        element = next()
        if jsNot(invoke(element)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_70420c70
        
    
    return True

def joinToString(separator, prefix, postfix, limit, truncated, transform):
    return toString()

def joinToString_default(separator, prefix, postfix, limit, truncated, transform, _mask0, _handler):
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 1), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_69c071db
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 2), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_1355d2a0
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 4), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_5aa345a5
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 8), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_2e7e9897
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 16), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_6c430548
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 32), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_77d5a3ee
    
    return joinToString(kotlin_CharSequence(separator), kotlin_CharSequence(prefix), kotlin_CharSequence(postfix), limit, kotlin_CharSequence(truncated), transform)

def joinTo(buffer, separator, prefix, postfix, limit, truncated, transform):
    append(prefix)
    Unit_getInstance()
    count = 0
    tmp0_iterator = iterator()
    while hasNext():
        element = next()
        count = jsBitOr(jsPlus(count, 1), 0)
        if jsGt(count, 1):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_60a4f677
        
        if True:
            pass
        
        if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_564d5883:
            appendElement(element, transform)
        
        if True:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrBreakImpl_77d58f3a
        
    
    if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_12025b72:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_13bd25ab
    
    append(postfix)
    Unit_getInstance()
    return buffer

def joinTo_default(buffer, separator, prefix, postfix, limit, truncated, transform, _mask0, _handler):
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 2), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_4e365c33
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 4), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_7ec65043
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 8), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_5ef99f75
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 16), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_22cc2ae5
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 32), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_6dd6c64c
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 64), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_53fa89e6
    
    return joinTo(buffer, kotlin_CharSequence(separator), kotlin_CharSequence(prefix), kotlin_CharSequence(postfix), limit, kotlin_CharSequence(truncated), transform)

def downTo(to):
    return fromClosedRange(_this_, to, -1)

def until(to):
    if jsLtEq(to, MIN_VALUE):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_4b5f022f
    
    return numberRangeToNumber(_this_, kotlin_Int(jsBitOr(jsMinus(to, 1), 0)))

def reversed():
    return fromClosedRange(last, first, jsBitOr(jsUnaryMinus(step), 0))

def getOrElse(index, defaultValue):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_11f8bff1

def KotlinNothingValueException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_5e805a0d
    return _this

def KotlinNothingValueException_init__Create_():
    tmp = KotlinNothingValueException_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_254ed9ba)
    return tmp

def KotlinNothingValueException_init__Init_(message, _this):
    RuntimeException_init__Init_(message, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_1d95957c
    return _this

def KotlinNothingValueException_init__Create_(message):
    tmp = KotlinNothingValueException_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_242270ae)
    return tmp

def KotlinNothingValueException_init__Init_(message, cause, _this):
    RuntimeException_init__Init_(message, cause, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_37c47166
    return _this

def KotlinNothingValueException_init__Create_(message, cause):
    tmp = KotlinNothingValueException_init__Init_(message, cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_4c1ce13a)
    return tmp

def KotlinNothingValueException_init__Init_(cause, _this):
    RuntimeException_init__Init_(cause, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_658ec00c
    return _this

def KotlinNothingValueException_init__Create_(cause):
    tmp = KotlinNothingValueException_init__Init_(cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_5d6d21e2)
    return tmp

class KotlinNothingValueException:
    pass

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_76cb6d16 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_764b7ff7 = 0
def values():
    return arrayLiteral(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_164fba04)

def valueOf(value):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2b647344

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_3b60efd8 = 0
def Level_initEntries():
    if Level_entriesInitialized:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_79036056
    
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_22e3d222
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_46f7c5c1
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_2afba04b

def Experimental_init__Init_(level, _mask0, _marker, _this):
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 1), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_11675922
    
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_3d2bb013
    return _this

def Experimental_init__Create_(level, _mask0, _marker):
    return Experimental_init__Init_(level, _mask0, _marker, Object_create())

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

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_599bda7e = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_39124055 = 0
def values():
    return arrayLiteral(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_31ca510a)

def valueOf(value):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_46eaf531

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_40383b24 = 0
def Level_initEntries():
    if Level_entriesInitialized:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_4e0d2ddd
    
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_24fa43f8
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_45ee48e7
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_55f77306

def RequiresOptIn_init__Init_(message, level, _mask0, _marker, _this):
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 1), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_75a45ce
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 2), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_bb0ca30
    
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_5ab30bb4
    return _this

def RequiresOptIn_init__Create_(message, level, _mask0, _marker):
    return RequiresOptIn_init__Init_(message, level, _mask0, _marker, Object_create())

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

class _no_name_provided_:
    pass

class AbstractCollection:
    pass

def _no_name_provided__factory(this_0):
    i = _init_(this_0)
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_3bd8032e

def _get_list_(_this):
    return list

def _get_fromIndex_(_this):
    return fromIndex

def _set__size_(_this, _set___):
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_63ed5580

def _get__size_(_this):
    return _size

class SubList:
    pass

class IteratorImpl:
    pass

class ListIteratorImpl:
    pass

class Companion:
    pass

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_606beba4 = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_3c9d64e4
    
    return Companion_instance

class AbstractList:
    pass

def listOf(elements):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_32f3174d

def emptyList():
    return EmptyList_getInstance()

def _get_serialVersionUID_(_this):
    return serialVersionUID

def readResolve(_this):
    return EmptyList_getInstance()

class EmptyList:
    pass

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_32a2da8c = 0
def EmptyList_getInstance():
    if jsEqeq(EmptyList_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_3f6aaa7
    
    return EmptyList_instance

class EmptyIterator:
    pass

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_42807bd7 = 0
def EmptyIterator_getInstance():
    if jsEqeq(EmptyIterator_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_1c244e31
    
    return EmptyIterator_instance

def _get_lastIndex_():
    return jsBitOr(jsMinus(_get_size_(), 1), 0)

def removeAll(predicate):
    return filterInPlace(predicate, True)

def removeAll(predicate):
    return filterInPlace(predicate, True)

def filterInPlace(predicate, predicateResultToRemove):
    if jsNot(isInterface(_this_, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_e7e6e94
    
    if True:
        pass
    
    writeIndex = 0
    inductionVariable = 0
    last = _get_lastIndex_()
    if jsLtEq(inductionVariable, last):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_66da2007
    
    if jsLt(writeIndex, _get_size_()):
        inductionVariable = _get_lastIndex_()
        if jsLtEq(writeIndex, inductionVariable):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_48313ada
        
        return True
    
    if True:
        return False
    

def filterInPlace(predicate, predicateResultToRemove):
    result = False
    tmp0_with_0 = iterator()
    while hasNext():
        if jsEqeqeq(invoke(next()), predicateResultToRemove):
            remove()
            result = True
        
    
    return result

class Sequence:
    pass

def contract(builder):
    pass

class ContractBuilder:
    pass

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_2a7648a9 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_54707af8 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_62c95d73 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_2abbe420 = 0
def values():
    return arrayLiteral(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_388555bd)

def valueOf(value):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_49702efb

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_20ea933f = 0
def InvocationKind_initEntries():
    if InvocationKind_entriesInitialized:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_1da9b95d
    
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_594c66ea
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_3aaa8361
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_4e6fb132
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_69724abb
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_56a2599a

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
    return _init_(context, resumeWith)

def resumeWithException(exception):
    tmp0_failure_0 = Companion_getInstance()
    return resumeWith(_init_(createFailure(exception)))

def resume(value):
    tmp0_success_0 = Companion_getInstance()
    return resumeWith(_init_(value))

def _get_coroutineContext_():
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_7843efc5

class _no_name_provided_:
    pass

class Key:
    pass

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_2b0a0c83 = 0
def Key_getInstance():
    if jsEqeq(Key_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_222e8b99
    
    return Key_instance

class ContinuationInterceptor:
    pass

class Key:
    pass

class Element:
    pass

class _no_name_provided_:
    pass

class CoroutineContext:
    pass

def _no_name_provided__factory():
    i = _init_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_5e206acb

def _get_serialVersionUID_(_this):
    return serialVersionUID

def readResolve(_this):
    return EmptyCoroutineContext_getInstance()

class EmptyCoroutineContext:
    pass

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_7a4154c = 0
def EmptyCoroutineContext_getInstance():
    if jsEqeq(EmptyCoroutineContext_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_aae69d3
    
    return EmptyCoroutineContext_instance

def _get_serialVersionUID_(_this):
    return serialVersionUID

class Companion:
    pass

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_5ef5455c = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_78828aca
    
    return Companion_instance

def readResolve(_this):
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

def _get_left_(_this):
    return left

def _get_element_(_this):
    return element

def size(_this):
    cur = _this
    size = 2
    while True:
        tmp = left
        tmp0_elvis_lhs = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4b3ebc09
        tmp
        if jsEqeq(tmp0_elvis_lhs, None):
            return size
        
        if True:
            tmp = tmp0_elvis_lhs
        
        cur = tmp
        tmp1 = size
        size = jsBitOr(jsPlus(tmp1, 1), 0)
        Unit_getInstance()
    

def contains(_this, element):
    return equals(get(_get_key_()), element)

def containsAll(_this, context):
    cur = context
    while True:
        if jsNot(contains(_this, element)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_56eb8c30
        
        next = left
        if jsInstanceOf(next, jsClass()):
            cur = kotlin_coroutines_CombinedContext(next)
        
        if True:
            if True:
                return contains(_this, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_17baf642)
            
        
    

def writeReplace(_this):
    n = size(_this)
    elements = fillArrayVal(Array(n), None)
    index = _sharedBox_create(0)
    fold(Unit_getInstance(), _no_name_provided__factory(elements, index))
    tmp0_check_0 = jsEqeqeq(_sharedBox_read(index), n)
    if jsNot(tmp0_check_0):
        message_2 = 'Check failed.'
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_13e4acf6
    
    return _init_(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4142586b)

class Serialized:
    pass

class _no_name_provided_:
    pass

class _no_name_provided_:
    pass

class CombinedContext:
    pass

def _get_safeCast_(_this):
    return safeCast

def _get_topmostKey_(_this):
    return topmostKey

class AbstractCoroutineContextKey:
    pass

def _no_name_provided__factory():
    i = _init_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_1ddf5237

def _no_name_provided__factory(_elements, _index):
    i = _init_(_elements, _index)
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_381f0bf4

def _get_COROUTINE_SUSPENDED_():
    return CoroutineSingletons_COROUTINE_SUSPENDED_getInstance()

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_c3976d4 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_7dc97564 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_23fee93a = 0
def values():
    return arrayLiteral(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_3b5f3ffb)

def valueOf(value):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_40904969

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_4d574ec7 = 0
def CoroutineSingletons_initEntries():
    if CoroutineSingletons_entriesInitialized:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_328b60fb
    
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_12326ccb
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_4a02197b
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_6948460f
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_1bffbac

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

def _and(other):
    return toByte(jsBitAnd(kotlin_Int(_this_), kotlin_Int(other)))

def _or(other):
    return toByte(jsBitOr(kotlin_Int(_this_), kotlin_Int(other)))

def xor(other):
    return toByte(jsBitXor(kotlin_Int(_this_), kotlin_Int(other)))

def inv():
    return toByte(jsBitNot(kotlin_Int(_this_)))

def _and(other):
    return toShort(jsBitAnd(kotlin_Int(_this_), kotlin_Int(other)))

def _or(other):
    return toShort(jsBitOr(kotlin_Int(_this_), kotlin_Int(other)))

def xor(other):
    return toShort(jsBitXor(kotlin_Int(_this_), kotlin_Int(other)))

def inv():
    return toShort(jsBitNot(kotlin_Int(_this_)))

class ExperimentalTypeInference:
    pass

def RequireKotlin_init__Init_(version, message, level, versionKind, errorCode, _mask0, _marker, _this):
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 2), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_5bbfd031
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 4), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_76ccefaf
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 8), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_43e78ed6
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 16), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_14062855
    
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_42542698
    return _this

def RequireKotlin_init__Create_(version, message, level, versionKind, errorCode, _mask0, _marker):
    return RequireKotlin_init__Init_(version, message, level, versionKind, errorCode, _mask0, _marker, Object_create())

class RequireKotlin:
    pass

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_4cd6143c = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_3ed50b5f = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_2ae63c84 = 0
def values():
    return arrayLiteral(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_3de4bfa9)

def valueOf(value):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_1d5e16a9

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_5f18ed13 = 0
def RequireKotlinVersionKind_initEntries():
    if RequireKotlinVersionKind_entriesInitialized:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_75b18097
    
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_5e81d985
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_3479e14e
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_74c2edc
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_69b9a61

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

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_5a5183ed = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_774ea667
    
    return Companion_instance

class KTypeProjection:
    pass

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_4474a287 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_47c90585 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_7cf6ea5b = 0
def values():
    return arrayLiteral(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_25fb28dd)

def valueOf(value):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_73344756

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_77a3c614 = 0
def KVariance_initEntries():
    if KVariance_entriesInitialized:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_48012514
    
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_472ab5a1
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_2712bbab
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_38ec1c34
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_58f252fe

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
    if jsNot(jsEqeq(transform, None)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_581242e1
    
    if True:
        if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6e29615e:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_65876774
        
        if True:
            if jsInstanceOf(element, jsClass()):
                visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_6bf597a9
            
            if True:
                if True:
                    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_5519eea8
                
            
        
    

def isEmpty():
    return jsEqeqeq(charSequenceLength(_this_), 0)

def _get_lastIndex_():
    return jsBitOr(jsMinus(charSequenceLength(_this_), 1), 0)

def _get_UNDEFINED_RESULT_():
    return UNDEFINED_RESULT

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_34cb1310 = 0
def UNDEFINED_RESULT_init_():
    tmp0_success_0 = Companion_getInstance()
    tmp1_success_0 = _get_COROUTINE_SUSPENDED_()
    return _init_(tmp1_success_0)

def check(value):
    if jsNot(value):
        message_2 = 'Check failed.'
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_5c6e4d6b
    

def check(value, lazyMessage):
    if jsNot(value):
        message = invoke()
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_48b4fecb
    

def error(message):
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_6e609e8a

def require(value, lazyMessage):
    if jsNot(value):
        message = invoke()
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_51e28071
    

def _Result___get_value__impl_(this):
    return value

def _Result___get_isSuccess__impl_(this):
    tmp = _Result___get_value__impl_(this)
    return jsNot(jsInstanceOf(tmp, jsClass()))

def _Result___get_isFailure__impl_(this):
    tmp = _Result___get_value__impl_(this)
    return jsInstanceOf(tmp, jsClass())

def Result__getOrNull_impl(this):
    tmp
    if _Result___get_isFailure__impl_(this):
        tmp = None
    
    if True:
        tmp = _Result___get_value__impl_(this)
        tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_10742c78
    
    return tmp

def Result__exceptionOrNull_impl(this):
    tmp0_subject = _Result___get_value__impl_(this)
    tmp
    if jsInstanceOf(tmp0_subject, jsClass()):
        tmp = exception
    
    if True:
        if True:
            tmp = None
        
    
    return tmp

def Result__toString_impl(this):
    tmp0_subject = _Result___get_value__impl_(this)
    tmp
    if jsInstanceOf(tmp0_subject, jsClass()):
        tmp = toString(_Result___get_value__impl_(this))
    
    if True:
        if True:
            tmp = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_261a0d86
        
    
    return tmp

class Companion:
    pass

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_278758da = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_62254d29
    
    return Companion_instance

class Failure:
    pass

def Result__hashCode_impl(this):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_760c63d0

def Result__equals_impl(this, other):
    if jsNot(jsInstanceOf(other, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_629fe84
    
    if True:
        pass
    
    tmp0_other_with_cast = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_147ee877
    if jsNot(equals(value, value)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_8942ece
    
    return True

class Result:
    pass

def createFailure(exception):
    return _init_(exception)

def getOrThrow():
    throwOnFailure()
    tmp = _Result___get_value__impl_(_this_)
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_67b1f69

def throwOnFailure():
    tmp = _Result___get_value__impl_(_this_)
    if jsInstanceOf(tmp, jsClass()):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_220a5163
    
    if True:
        pass
    

def run(block):
    return invoke()

def TODO():
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_c56ea7b

def NotImplementedError_init__Init_(message, _mask0, _marker, _this):
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 1), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_42e58f8e
    
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_1d67a1ad
    return _this

def NotImplementedError_init__Create_(message, _mask0, _marker):
    tmp = NotImplementedError_init__Init_(message, _mask0, _marker, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_1c486cec)
    return tmp

class NotImplementedError:
    pass

def let(block):
    return invoke(_this_)

def apply(block):
    invoke(_this_)
    return _this_

def repeat(times, action):
    inductionVariable = 0
    if jsLt(inductionVariable, times):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_5d548872
    

def _with(receiver, block):
    return invoke(receiver)

def also(block):
    invoke(_this_)
    return _this_

def run(block):
    return invoke(_this_)

def _UByte___get_data__impl_(this):
    return data

class Companion:
    pass

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_b2bfd65 = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_2a542f65
    
    return Companion_instance

def UByte__compareTo_impl(this, other):
    tmp = jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255)
    return compareTo(tmp, jsBitAnd(kotlin_Int(_UByte___get_data__impl_(other)), 255))

def UByte__compareTo_impl(this, other):
    tmp = unboxIntrinsic(this)
    return UByte__compareTo_impl(tmp, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_15411d35)

def UByte__compareTo_impl(this, other):
    tmp = jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255)
    return compareTo(tmp, jsBitAnd(kotlin_Int(_UShort___get_data__impl_(other)), 65535))

def UByte__compareTo_impl(this, other):
    tmp0_compareTo_0 = _init_(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255))
    return uintCompare(_UInt___get_data__impl_(tmp0_compareTo_0), _UInt___get_data__impl_(other))

def UByte__compareTo_impl(this, other):
    tmp0_compareTo_0 = _init_(_and(_init_(255, 0)))
    return ulongCompare(_ULong___get_data__impl_(tmp0_compareTo_0), _ULong___get_data__impl_(other))

def UByte__plus_impl(this, other):
    tmp0_plus_0 = _init_(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255))
    tmp1_plus_0 = _init_(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(other)), 255))
    return _init_(jsBitOr(jsPlus(_UInt___get_data__impl_(tmp0_plus_0), _UInt___get_data__impl_(tmp1_plus_0)), 0))

def UByte__plus_impl(this, other):
    tmp0_plus_0 = _init_(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255))
    tmp1_plus_0 = _init_(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(other)), 65535))
    return _init_(jsBitOr(jsPlus(_UInt___get_data__impl_(tmp0_plus_0), _UInt___get_data__impl_(tmp1_plus_0)), 0))

def UByte__plus_impl(this, other):
    tmp0_plus_0 = _init_(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255))
    return _init_(jsBitOr(jsPlus(_UInt___get_data__impl_(tmp0_plus_0), _UInt___get_data__impl_(other)), 0))

def UByte__plus_impl(this, other):
    tmp0_plus_0 = _init_(_and(_init_(255, 0)))
    return _init_(plus(_ULong___get_data__impl_(other)))

def UByte__minus_impl(this, other):
    tmp0_minus_0 = _init_(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255))
    tmp1_minus_0 = _init_(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(other)), 255))
    return _init_(jsBitOr(jsMinus(_UInt___get_data__impl_(tmp0_minus_0), _UInt___get_data__impl_(tmp1_minus_0)), 0))

def UByte__minus_impl(this, other):
    tmp0_minus_0 = _init_(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255))
    tmp1_minus_0 = _init_(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(other)), 65535))
    return _init_(jsBitOr(jsMinus(_UInt___get_data__impl_(tmp0_minus_0), _UInt___get_data__impl_(tmp1_minus_0)), 0))

def UByte__minus_impl(this, other):
    tmp0_minus_0 = _init_(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255))
    return _init_(jsBitOr(jsMinus(_UInt___get_data__impl_(tmp0_minus_0), _UInt___get_data__impl_(other)), 0))

def UByte__minus_impl(this, other):
    tmp0_minus_0 = _init_(_and(_init_(255, 0)))
    return _init_(minus(_ULong___get_data__impl_(other)))

def UByte__times_impl(this, other):
    tmp0_times_0 = _init_(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255))
    tmp1_times_0 = _init_(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(other)), 255))
    return _init_(imul(_UInt___get_data__impl_(tmp0_times_0), _UInt___get_data__impl_(tmp1_times_0)))

def UByte__times_impl(this, other):
    tmp0_times_0 = _init_(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255))
    tmp1_times_0 = _init_(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(other)), 65535))
    return _init_(imul(_UInt___get_data__impl_(tmp0_times_0), _UInt___get_data__impl_(tmp1_times_0)))

def UByte__times_impl(this, other):
    tmp0_times_0 = _init_(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255))
    return _init_(imul(_UInt___get_data__impl_(tmp0_times_0), _UInt___get_data__impl_(other)))

def UByte__times_impl(this, other):
    tmp0_times_0 = _init_(_and(_init_(255, 0)))
    return _init_(times(_ULong___get_data__impl_(other)))

def UByte__div_impl(this, other):
    tmp0_div_0 = _init_(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255))
    tmp1_div_0 = _init_(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(other)), 255))
    return uintDivide(tmp0_div_0, tmp1_div_0)

def UByte__div_impl(this, other):
    tmp0_div_0 = _init_(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255))
    tmp1_div_0 = _init_(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(other)), 65535))
    return uintDivide(tmp0_div_0, tmp1_div_0)

def UByte__div_impl(this, other):
    tmp0_div_0 = _init_(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255))
    return uintDivide(tmp0_div_0, other)

def UByte__div_impl(this, other):
    tmp0_div_0 = _init_(_and(_init_(255, 0)))
    return ulongDivide(tmp0_div_0, other)

def UByte__rem_impl(this, other):
    tmp0_rem_0 = _init_(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255))
    tmp1_rem_0 = _init_(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(other)), 255))
    return uintRemainder(tmp0_rem_0, tmp1_rem_0)

def UByte__rem_impl(this, other):
    tmp0_rem_0 = _init_(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255))
    tmp1_rem_0 = _init_(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(other)), 65535))
    return uintRemainder(tmp0_rem_0, tmp1_rem_0)

def UByte__rem_impl(this, other):
    tmp0_rem_0 = _init_(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255))
    return uintRemainder(tmp0_rem_0, other)

def UByte__rem_impl(this, other):
    tmp0_rem_0 = _init_(_and(_init_(255, 0)))
    return ulongRemainder(tmp0_rem_0, other)

def UByte__inc_impl(this):
    return _init_(numberToByte(jsPlus(_UByte___get_data__impl_(this), 1)))

def UByte__dec_impl(this):
    return _init_(numberToByte(jsMinus(_UByte___get_data__impl_(this), 1)))

def UByte__rangeTo_impl(this, other):
    tmp = _init_(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255))
    return _init_(tmp, _init_(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(other)), 255)))

def UByte__and_impl(this, other):
    tmp0_and_0 = _UByte___get_data__impl_(this)
    tmp1_and_0 = _UByte___get_data__impl_(other)
    return _init_(toByte(jsBitAnd(kotlin_Int(tmp0_and_0), kotlin_Int(tmp1_and_0))))

def UByte__or_impl(this, other):
    tmp0_or_0 = _UByte___get_data__impl_(this)
    tmp1_or_0 = _UByte___get_data__impl_(other)
    return _init_(toByte(jsBitOr(kotlin_Int(tmp0_or_0), kotlin_Int(tmp1_or_0))))

def UByte__xor_impl(this, other):
    tmp0_xor_0 = _UByte___get_data__impl_(this)
    tmp1_xor_0 = _UByte___get_data__impl_(other)
    return _init_(toByte(jsBitXor(kotlin_Int(tmp0_xor_0), kotlin_Int(tmp1_xor_0))))

def UByte__inv_impl(this):
    tmp0_inv_0 = _UByte___get_data__impl_(this)
    return _init_(toByte(jsBitNot(kotlin_Int(tmp0_inv_0))))

def UByte__toByte_impl(this):
    return _UByte___get_data__impl_(this)

def UByte__toShort_impl(this):
    tmp0_and_0 = kotlin_Short(_UByte___get_data__impl_(this))
    tmp1_and_0 = visitConst_other_Short
    return toShort(jsBitAnd(kotlin_Int(tmp0_and_0), kotlin_Int(tmp1_and_0)))

def UByte__toInt_impl(this):
    return jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255)

def UByte__toLong_impl(this):
    return _and(_init_(255, 0))

def UByte__toUByte_impl(this):
    return this

def UByte__toUShort_impl(this):
    tmp0_and_0 = kotlin_Short(_UByte___get_data__impl_(this))
    tmp1_and_0 = visitConst_other_Short
    return _init_(toShort(jsBitAnd(kotlin_Int(tmp0_and_0), kotlin_Int(tmp1_and_0))))

def UByte__toUInt_impl(this):
    return _init_(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255))

def UByte__toULong_impl(this):
    return _init_(_and(_init_(255, 0)))

def UByte__toFloat_impl(this):
    return kotlin_Float(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255))

def UByte__toDouble_impl(this):
    return kotlin_Double(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255))

def UByte__toString_impl(this):
    return toString()

def UByte__hashCode_impl(this):
    return data

def UByte__equals_impl(this, other):
    if jsNot(jsInstanceOf(other, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_18ab513d
    
    if True:
        pass
    
    tmp0_other_with_cast = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_26772e54
    if jsNot(jsEqeqeq(data, data)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_bb1b872
    
    return True

class UByte:
    pass

def toUByte():
    return _init_(toByte(_this_))

def toUByte():
    return _init_(toByte(_this_))

def toUByte():
    return _init_(toByte())

def toUByte():
    return _init_(_this_)

def _get_array_(_this):
    return array

def _set_index_(_this, _set___):
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_627e21c9

def _get_index_(_this):
    return index

def _UByteArray___get_storage__impl_(this):
    return storage

def _UByteArray___init__impl_(size):
    tmp = _init_(int8Array(size))
    return tmp

def UByteArray__get_impl(this, index):
    tmp0_toUByte_0 = jsArrayGet(_UByteArray___get_storage__impl_(this), index)
    return _init_(tmp0_toUByte_0)

def UByteArray__set_impl(this, index, value):
    tmp = _UByteArray___get_storage__impl_(this)
    jsArraySet(tmp, index, _UByte___get_data__impl_(value))

def _UByteArray___get_size__impl_(this):
    return jsArrayLength(_UByteArray___get_storage__impl_(this))

def UByteArray__iterator_impl(this):
    return _init_(_UByteArray___get_storage__impl_(this))

class Iterator:
    pass

def UByteArray__contains_impl(this, element):
    tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_58ba1195
    if jsNot(jsInstanceOf(tmp, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_25762f04
    
    if True:
        pass
    
    tmp = _UByteArray___get_storage__impl_(this)
    return contains(_UByte___get_data__impl_(element))

def UByteArray__contains_impl(this, element):
    if jsNot(jsInstanceOf(element, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_4ee706ff
    
    if True:
        pass
    
    tmp = unboxIntrinsic(this)
    return UByteArray__contains_impl(tmp, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_1f0eabb8)

def UByteArray__containsAll_impl(this, elements):
    tmp_ret_0
    visitDoWhileLoop_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_69d142f6
    return tmp_ret_0

def UByteArray__containsAll_impl(this, elements):
    return UByteArray__containsAll_impl(unboxIntrinsic(this), elements)

def UByteArray__isEmpty_impl(this):
    return jsEqeqeq(jsArrayLength(_UByteArray___get_storage__impl_(this)), 0)

def UByteArray__toString_impl(this):
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_15db982e

def UByteArray__hashCode_impl(this):
    return hashCode(storage)

def UByteArray__equals_impl(this, other):
    if jsNot(jsInstanceOf(other, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_77b01226
    
    if True:
        pass
    
    tmp0_other_with_cast = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3b764ae5
    if jsNot(equals(storage, storage)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_40b678b3
    
    return True

class UByteArray:
    pass

def _UInt___get_data__impl_(this):
    return data

class Companion:
    pass

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_20f7197f = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_515f104c
    
    return Companion_instance

def UInt__compareTo_impl(this, other):
    tmp0_compareTo_0 = _init_(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(other)), 255))
    return uintCompare(_UInt___get_data__impl_(this), _UInt___get_data__impl_(tmp0_compareTo_0))

def UInt__compareTo_impl(this, other):
    tmp0_compareTo_0 = _init_(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(other)), 65535))
    return uintCompare(_UInt___get_data__impl_(this), _UInt___get_data__impl_(tmp0_compareTo_0))

def UInt__compareTo_impl(this, other):
    return uintCompare(_UInt___get_data__impl_(this), _UInt___get_data__impl_(other))

def UInt__compareTo_impl(this, other):
    tmp = unboxIntrinsic(this)
    return UInt__compareTo_impl(tmp, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_716661b3)

def UInt__compareTo_impl(this, other):
    tmp0_compareTo_0 = _init_(_and(_init_(-1, 0)))
    return ulongCompare(_ULong___get_data__impl_(tmp0_compareTo_0), _ULong___get_data__impl_(other))

def UInt__plus_impl(this, other):
    tmp0_plus_0 = _init_(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(other)), 255))
    return _init_(jsBitOr(jsPlus(_UInt___get_data__impl_(this), _UInt___get_data__impl_(tmp0_plus_0)), 0))

def UInt__plus_impl(this, other):
    tmp0_plus_0 = _init_(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(other)), 65535))
    return _init_(jsBitOr(jsPlus(_UInt___get_data__impl_(this), _UInt___get_data__impl_(tmp0_plus_0)), 0))

def UInt__plus_impl(this, other):
    return _init_(jsBitOr(jsPlus(_UInt___get_data__impl_(this), _UInt___get_data__impl_(other)), 0))

def UInt__plus_impl(this, other):
    tmp0_plus_0 = _init_(_and(_init_(-1, 0)))
    return _init_(plus(_ULong___get_data__impl_(other)))

def UInt__minus_impl(this, other):
    tmp0_minus_0 = _init_(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(other)), 255))
    return _init_(jsBitOr(jsMinus(_UInt___get_data__impl_(this), _UInt___get_data__impl_(tmp0_minus_0)), 0))

def UInt__minus_impl(this, other):
    tmp0_minus_0 = _init_(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(other)), 65535))
    return _init_(jsBitOr(jsMinus(_UInt___get_data__impl_(this), _UInt___get_data__impl_(tmp0_minus_0)), 0))

def UInt__minus_impl(this, other):
    return _init_(jsBitOr(jsMinus(_UInt___get_data__impl_(this), _UInt___get_data__impl_(other)), 0))

def UInt__minus_impl(this, other):
    tmp0_minus_0 = _init_(_and(_init_(-1, 0)))
    return _init_(minus(_ULong___get_data__impl_(other)))

def UInt__times_impl(this, other):
    tmp0_times_0 = _init_(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(other)), 255))
    return _init_(imul(_UInt___get_data__impl_(this), _UInt___get_data__impl_(tmp0_times_0)))

def UInt__times_impl(this, other):
    tmp0_times_0 = _init_(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(other)), 65535))
    return _init_(imul(_UInt___get_data__impl_(this), _UInt___get_data__impl_(tmp0_times_0)))

def UInt__times_impl(this, other):
    return _init_(imul(_UInt___get_data__impl_(this), _UInt___get_data__impl_(other)))

def UInt__times_impl(this, other):
    tmp0_times_0 = _init_(_and(_init_(-1, 0)))
    return _init_(times(_ULong___get_data__impl_(other)))

def UInt__div_impl(this, other):
    tmp0_div_0 = _init_(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(other)), 255))
    return uintDivide(this, tmp0_div_0)

def UInt__div_impl(this, other):
    tmp0_div_0 = _init_(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(other)), 65535))
    return uintDivide(this, tmp0_div_0)

def UInt__div_impl(this, other):
    return uintDivide(this, other)

def UInt__div_impl(this, other):
    tmp0_div_0 = _init_(_and(_init_(-1, 0)))
    return ulongDivide(tmp0_div_0, other)

def UInt__rem_impl(this, other):
    tmp0_rem_0 = _init_(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(other)), 255))
    return uintRemainder(this, tmp0_rem_0)

def UInt__rem_impl(this, other):
    tmp0_rem_0 = _init_(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(other)), 65535))
    return uintRemainder(this, tmp0_rem_0)

def UInt__rem_impl(this, other):
    return uintRemainder(this, other)

def UInt__rem_impl(this, other):
    tmp0_rem_0 = _init_(_and(_init_(-1, 0)))
    return ulongRemainder(tmp0_rem_0, other)

def UInt__inc_impl(this):
    return _init_(jsBitOr(jsPlus(_UInt___get_data__impl_(this), 1), 0))

def UInt__dec_impl(this):
    return _init_(jsBitOr(jsMinus(_UInt___get_data__impl_(this), 1), 0))

def UInt__rangeTo_impl(this, other):
    return _init_(this, other)

def UInt__shl_impl(this, bitCount):
    return _init_(jsBitShiftL(_UInt___get_data__impl_(this), bitCount))

def UInt__shr_impl(this, bitCount):
    return _init_(jsBitShiftRU(_UInt___get_data__impl_(this), bitCount))

def UInt__and_impl(this, other):
    return _init_(jsBitAnd(_UInt___get_data__impl_(this), _UInt___get_data__impl_(other)))

def UInt__or_impl(this, other):
    return _init_(jsBitOr(_UInt___get_data__impl_(this), _UInt___get_data__impl_(other)))

def UInt__xor_impl(this, other):
    return _init_(jsBitXor(_UInt___get_data__impl_(this), _UInt___get_data__impl_(other)))

def UInt__inv_impl(this):
    return _init_(jsBitNot(_UInt___get_data__impl_(this)))

def UInt__toByte_impl(this):
    return toByte(_UInt___get_data__impl_(this))

def UInt__toShort_impl(this):
    return toShort(_UInt___get_data__impl_(this))

def UInt__toInt_impl(this):
    return _UInt___get_data__impl_(this)

def UInt__toLong_impl(this):
    return _and(_init_(-1, 0))

def UInt__toUByte_impl(this):
    tmp0_toUByte_0 = _UInt___get_data__impl_(this)
    return _init_(toByte(tmp0_toUByte_0))

def UInt__toUShort_impl(this):
    tmp0_toUShort_0 = _UInt___get_data__impl_(this)
    return _init_(toShort(tmp0_toUShort_0))

def UInt__toUInt_impl(this):
    return this

def UInt__toULong_impl(this):
    return _init_(_and(_init_(-1, 0)))

def UInt__toFloat_impl(this):
    return kotlin_Float(uintToDouble(_UInt___get_data__impl_(this)))

def UInt__toDouble_impl(this):
    return uintToDouble(_UInt___get_data__impl_(this))

def UInt__toString_impl(this):
    return toString()

def UInt__hashCode_impl(this):
    return data

def UInt__equals_impl(this, other):
    if jsNot(jsInstanceOf(other, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_16a14076
    
    if True:
        pass
    
    tmp0_other_with_cast = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4f5bb24d
    if jsNot(jsEqeqeq(data, data)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_3df4cd96
    
    return True

class UInt:
    pass

def toUInt():
    return _init_(toInt())

def toUInt():
    return _init_(_this_)

def toUInt():
    return _init_(kotlin_Int(_this_))

def toUInt():
    return doubleToUInt(_this_)

def toUInt():
    return doubleToUInt(kotlin_Double(_this_))

def toUInt():
    return _init_(kotlin_Int(_this_))

def _get_array_(_this):
    return array

def _set_index_(_this, _set___):
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_24dbdfa0

def _get_index_(_this):
    return index

def _UIntArray___get_storage__impl_(this):
    return storage

def _UIntArray___init__impl_(size):
    tmp = _init_(int32Array(size))
    return tmp

def UIntArray__get_impl(this, index):
    tmp0_toUInt_0 = jsArrayGet(_UIntArray___get_storage__impl_(this), index)
    return _init_(tmp0_toUInt_0)

def UIntArray__set_impl(this, index, value):
    tmp = _UIntArray___get_storage__impl_(this)
    jsArraySet(tmp, index, _UInt___get_data__impl_(value))

def _UIntArray___get_size__impl_(this):
    return jsArrayLength(_UIntArray___get_storage__impl_(this))

def UIntArray__iterator_impl(this):
    return _init_(_UIntArray___get_storage__impl_(this))

class Iterator:
    pass

def UIntArray__contains_impl(this, element):
    tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_7f31e2fb
    if jsNot(jsInstanceOf(tmp, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_75c30a4f
    
    if True:
        pass
    
    tmp = _UIntArray___get_storage__impl_(this)
    return contains(_UInt___get_data__impl_(element))

def UIntArray__contains_impl(this, element):
    if jsNot(jsInstanceOf(element, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_45c20d8f
    
    if True:
        pass
    
    tmp = unboxIntrinsic(this)
    return UIntArray__contains_impl(tmp, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_393751a0)

def UIntArray__containsAll_impl(this, elements):
    tmp_ret_0
    visitDoWhileLoop_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_555856fa
    return tmp_ret_0

def UIntArray__containsAll_impl(this, elements):
    return UIntArray__containsAll_impl(unboxIntrinsic(this), elements)

def UIntArray__isEmpty_impl(this):
    return jsEqeqeq(jsArrayLength(_UIntArray___get_storage__impl_(this)), 0)

def UIntArray__toString_impl(this):
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_34ea5eff

def UIntArray__hashCode_impl(this):
    return hashCode(storage)

def UIntArray__equals_impl(this, other):
    if jsNot(jsInstanceOf(other, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_6600d07d
    
    if True:
        pass
    
    tmp0_other_with_cast = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_7ffb60a4
    if jsNot(equals(storage, storage)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_6c38f4de
    
    return True

class UIntArray:
    pass

class Companion:
    pass

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_4c8a893e = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_34d27e12
    
    return Companion_instance

class UIntRange:
    pass

class Companion:
    pass

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_5a12819f = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_82300e1
    
    return Companion_instance

class UIntProgression:
    pass

def _get_finalElement_(_this):
    return finalElement

def _set_hasNext_(_this, _set___):
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_ce51a54

def _get_hasNext_(_this):
    return hasNext

def _get_step_(_this):
    return step

def _set_next_(_this, _set___):
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_70c1a887

def _get_next_(_this):
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

def _ULong___get_data__impl_(this):
    return data

class Companion:
    pass

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_6f377b1f = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_1d243ebb
    
    return Companion_instance

def ULong__compareTo_impl(this, other):
    tmp0_compareTo_0 = _init_(_and(_init_(255, 0)))
    return ulongCompare(_ULong___get_data__impl_(this), _ULong___get_data__impl_(tmp0_compareTo_0))

def ULong__compareTo_impl(this, other):
    tmp0_compareTo_0 = _init_(_and(_init_(65535, 0)))
    return ulongCompare(_ULong___get_data__impl_(this), _ULong___get_data__impl_(tmp0_compareTo_0))

def ULong__compareTo_impl(this, other):
    tmp0_compareTo_0 = _init_(_and(_init_(-1, 0)))
    return ulongCompare(_ULong___get_data__impl_(this), _ULong___get_data__impl_(tmp0_compareTo_0))

def ULong__compareTo_impl(this, other):
    return ulongCompare(_ULong___get_data__impl_(this), _ULong___get_data__impl_(other))

def ULong__compareTo_impl(this, other):
    tmp = unboxIntrinsic(this)
    return ULong__compareTo_impl(tmp, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_135a2a14)

def ULong__plus_impl(this, other):
    tmp0_plus_0 = _init_(_and(_init_(255, 0)))
    return _init_(plus(_ULong___get_data__impl_(tmp0_plus_0)))

def ULong__plus_impl(this, other):
    tmp0_plus_0 = _init_(_and(_init_(65535, 0)))
    return _init_(plus(_ULong___get_data__impl_(tmp0_plus_0)))

def ULong__plus_impl(this, other):
    tmp0_plus_0 = _init_(_and(_init_(-1, 0)))
    return _init_(plus(_ULong___get_data__impl_(tmp0_plus_0)))

def ULong__plus_impl(this, other):
    return _init_(plus(_ULong___get_data__impl_(other)))

def ULong__minus_impl(this, other):
    tmp0_minus_0 = _init_(_and(_init_(255, 0)))
    return _init_(minus(_ULong___get_data__impl_(tmp0_minus_0)))

def ULong__minus_impl(this, other):
    tmp0_minus_0 = _init_(_and(_init_(65535, 0)))
    return _init_(minus(_ULong___get_data__impl_(tmp0_minus_0)))

def ULong__minus_impl(this, other):
    tmp0_minus_0 = _init_(_and(_init_(-1, 0)))
    return _init_(minus(_ULong___get_data__impl_(tmp0_minus_0)))

def ULong__minus_impl(this, other):
    return _init_(minus(_ULong___get_data__impl_(other)))

def ULong__times_impl(this, other):
    tmp0_times_0 = _init_(_and(_init_(255, 0)))
    return _init_(times(_ULong___get_data__impl_(tmp0_times_0)))

def ULong__times_impl(this, other):
    tmp0_times_0 = _init_(_and(_init_(65535, 0)))
    return _init_(times(_ULong___get_data__impl_(tmp0_times_0)))

def ULong__times_impl(this, other):
    tmp0_times_0 = _init_(_and(_init_(-1, 0)))
    return _init_(times(_ULong___get_data__impl_(tmp0_times_0)))

def ULong__times_impl(this, other):
    return _init_(times(_ULong___get_data__impl_(other)))

def ULong__div_impl(this, other):
    tmp0_div_0 = _init_(_and(_init_(255, 0)))
    return ulongDivide(this, tmp0_div_0)

def ULong__div_impl(this, other):
    tmp0_div_0 = _init_(_and(_init_(65535, 0)))
    return ulongDivide(this, tmp0_div_0)

def ULong__div_impl(this, other):
    tmp0_div_0 = _init_(_and(_init_(-1, 0)))
    return ulongDivide(this, tmp0_div_0)

def ULong__div_impl(this, other):
    return ulongDivide(this, other)

def ULong__rem_impl(this, other):
    tmp0_rem_0 = _init_(_and(_init_(255, 0)))
    return ulongRemainder(this, tmp0_rem_0)

def ULong__rem_impl(this, other):
    tmp0_rem_0 = _init_(_and(_init_(65535, 0)))
    return ulongRemainder(this, tmp0_rem_0)

def ULong__rem_impl(this, other):
    tmp0_rem_0 = _init_(_and(_init_(-1, 0)))
    return ulongRemainder(this, tmp0_rem_0)

def ULong__rem_impl(this, other):
    return ulongRemainder(this, other)

def ULong__inc_impl(this):
    return _init_(inc())

def ULong__dec_impl(this):
    return _init_(dec())

def ULong__rangeTo_impl(this, other):
    return _init_(this, other)

def ULong__shl_impl(this, bitCount):
    return _init_(shl(bitCount))

def ULong__shr_impl(this, bitCount):
    return _init_(ushr(bitCount))

def ULong__and_impl(this, other):
    return _init_(_and(_ULong___get_data__impl_(other)))

def ULong__or_impl(this, other):
    return _init_(_or(_ULong___get_data__impl_(other)))

def ULong__xor_impl(this, other):
    return _init_(xor(_ULong___get_data__impl_(other)))

def ULong__inv_impl(this):
    return _init_(inv())

def ULong__toByte_impl(this):
    return toByte()

def ULong__toShort_impl(this):
    return toShort()

def ULong__toInt_impl(this):
    return toInt()

def ULong__toLong_impl(this):
    return _ULong___get_data__impl_(this)

def ULong__toUByte_impl(this):
    tmp0_toUByte_0 = _ULong___get_data__impl_(this)
    return _init_(toByte())

def ULong__toUShort_impl(this):
    tmp0_toUShort_0 = _ULong___get_data__impl_(this)
    return _init_(toShort())

def ULong__toUInt_impl(this):
    tmp0_toUInt_0 = _ULong___get_data__impl_(this)
    return _init_(toInt())

def ULong__toULong_impl(this):
    return this

def ULong__toFloat_impl(this):
    return kotlin_Float(ulongToDouble(_ULong___get_data__impl_(this)))

def ULong__toDouble_impl(this):
    return ulongToDouble(_ULong___get_data__impl_(this))

def ULong__toString_impl(this):
    return ulongToString(_ULong___get_data__impl_(this))

def ULong__hashCode_impl(this):
    return hashCode()

def ULong__equals_impl(this, other):
    if jsNot(jsInstanceOf(other, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_1415f18d
    
    if True:
        pass
    
    tmp0_other_with_cast = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3a369bbd
    if jsNot(equals(data)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_48cbb4c5
    
    return True

class ULong:
    pass

def toULong():
    return _init_(_this_)

def toULong():
    return _init_(toLong(_this_))

def toULong():
    return doubleToULong(_this_)

def toULong():
    return doubleToULong(kotlin_Double(_this_))

def toULong():
    return _init_(toLong(_this_))

def toULong():
    return _init_(toLong(_this_))

def _get_array_(_this):
    return array

def _set_index_(_this, _set___):
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_620af7f3

def _get_index_(_this):
    return index

def _ULongArray___get_storage__impl_(this):
    return storage

def _ULongArray___init__impl_(size):
    tmp = _init_(longArray(size))
    return tmp

def ULongArray__get_impl(this, index):
    tmp0_toULong_0 = jsArrayGet(_ULongArray___get_storage__impl_(this), index)
    return _init_(tmp0_toULong_0)

def ULongArray__set_impl(this, index, value):
    tmp = _ULongArray___get_storage__impl_(this)
    jsArraySet(tmp, index, _ULong___get_data__impl_(value))

def _ULongArray___get_size__impl_(this):
    return jsArrayLength(_ULongArray___get_storage__impl_(this))

def ULongArray__iterator_impl(this):
    return _init_(_ULongArray___get_storage__impl_(this))

class Iterator:
    pass

def ULongArray__contains_impl(this, element):
    tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_27df0864
    if jsNot(jsInstanceOf(tmp, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_53b579d2
    
    if True:
        pass
    
    tmp = _ULongArray___get_storage__impl_(this)
    return contains(_ULong___get_data__impl_(element))

def ULongArray__contains_impl(this, element):
    if jsNot(jsInstanceOf(element, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_16ae5d46
    
    if True:
        pass
    
    tmp = unboxIntrinsic(this)
    return ULongArray__contains_impl(tmp, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_45b4135)

def ULongArray__containsAll_impl(this, elements):
    tmp_ret_0
    visitDoWhileLoop_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_5766f830
    return tmp_ret_0

def ULongArray__containsAll_impl(this, elements):
    return ULongArray__containsAll_impl(unboxIntrinsic(this), elements)

def ULongArray__isEmpty_impl(this):
    return jsEqeqeq(jsArrayLength(_ULongArray___get_storage__impl_(this)), 0)

def ULongArray__toString_impl(this):
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_3ff5b628

def ULongArray__hashCode_impl(this):
    return hashCode(storage)

def ULongArray__equals_impl(this, other):
    if jsNot(jsInstanceOf(other, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_12a8d03b
    
    if True:
        pass
    
    tmp0_other_with_cast = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_53a517e9
    if jsNot(equals(storage, storage)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_32eeef08
    
    return True

class ULongArray:
    pass

class Companion:
    pass

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_5914bf5f = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_514111ca
    
    return Companion_instance

class ULongRange:
    pass

class Companion:
    pass

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_337348de = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_edc900a
    
    return Companion_instance

class ULongProgression:
    pass

def _get_finalElement_(_this):
    return finalElement

def _set_hasNext_(_this, _set___):
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_13bf0814

def _get_hasNext_(_this):
    return hasNext

def _get_step_(_this):
    return step

def _set_next_(_this, _set___):
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_36c1b50d

def _get_next_(_this):
    return next

class ULongProgressionIterator:
    pass

def getProgressionLastElement(start, end, step):
    tmp
    if jsGt(step, 0):
        tmp
        if jsGtEq(uintCompare(_UInt___get_data__impl_(start), _UInt___get_data__impl_(end)), 0):
            tmp = end
        
        if True:
            if True:
                tmp0_minus_0 = differenceModulo(end, start, _init_(step))
                tmp = _init_(jsBitOr(jsMinus(_UInt___get_data__impl_(end), _UInt___get_data__impl_(tmp0_minus_0)), 0))
            
        
        tmp = tmp
    
    if jsLt(step, 0):
        tmp
        if jsLtEq(uintCompare(_UInt___get_data__impl_(start), _UInt___get_data__impl_(end)), 0):
            tmp = end
        
        if True:
            if True:
                tmp1_toUInt_0 = jsBitOr(jsUnaryMinus(step), 0)
                tmp2_plus_0 = differenceModulo(start, end, _init_(tmp1_toUInt_0))
                tmp = _init_(jsBitOr(jsPlus(_UInt___get_data__impl_(end), _UInt___get_data__impl_(tmp2_plus_0)), 0))
            
        
        tmp = tmp
    
    if True:
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_7c5fbde4
    
    return tmp

def getProgressionLastElement(start, end, step):
    tmp
    if jsGt(compareTo(_init_(0, 0)), 0):
        tmp
        if jsGtEq(ulongCompare(_ULong___get_data__impl_(start), _ULong___get_data__impl_(end)), 0):
            tmp = end
        
        if True:
            if True:
                tmp0_minus_0 = differenceModulo(end, start, _init_(step))
                tmp = _init_(minus(_ULong___get_data__impl_(tmp0_minus_0)))
            
        
        tmp = tmp
    
    if jsLt(compareTo(_init_(0, 0)), 0):
        tmp
        if jsLtEq(ulongCompare(_ULong___get_data__impl_(start), _ULong___get_data__impl_(end)), 0):
            tmp = end
        
        if True:
            if True:
                tmp1_toULong_0 = unaryMinus()
                tmp2_plus_0 = differenceModulo(start, end, _init_(tmp1_toULong_0))
                tmp = _init_(plus(_ULong___get_data__impl_(tmp2_plus_0)))
            
        
        tmp = tmp
    
    if True:
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_2a41d17a
    
    return tmp

def differenceModulo(a, b, c):
    ac = uintRemainder(a, c)
    bc = uintRemainder(b, c)
    tmp
    if jsGtEq(uintCompare(_UInt___get_data__impl_(ac), _UInt___get_data__impl_(bc)), 0):
        tmp = _init_(jsBitOr(jsMinus(_UInt___get_data__impl_(ac), _UInt___get_data__impl_(bc)), 0))
    
    if True:
        if True:
            tmp0_plus_0 = _init_(jsBitOr(jsMinus(_UInt___get_data__impl_(ac), _UInt___get_data__impl_(bc)), 0))
            tmp = _init_(jsBitOr(jsPlus(_UInt___get_data__impl_(tmp0_plus_0), _UInt___get_data__impl_(c)), 0))
        
    
    return tmp

def differenceModulo(a, b, c):
    ac = ulongRemainder(a, c)
    bc = ulongRemainder(b, c)
    tmp
    if jsGtEq(ulongCompare(_ULong___get_data__impl_(ac), _ULong___get_data__impl_(bc)), 0):
        tmp = _init_(minus(_ULong___get_data__impl_(bc)))
    
    if True:
        if True:
            tmp0_plus_0 = _init_(minus(_ULong___get_data__impl_(bc)))
            tmp = _init_(plus(_ULong___get_data__impl_(c)))
        
    
    return tmp

def _UShort___get_data__impl_(this):
    return data

class Companion:
    pass

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_5b99ede3 = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_32b72d9d
    
    return Companion_instance

def UShort__compareTo_impl(this, other):
    tmp = jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535)
    return compareTo(tmp, jsBitAnd(kotlin_Int(_UByte___get_data__impl_(other)), 255))

def UShort__compareTo_impl(this, other):
    tmp = jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535)
    return compareTo(tmp, jsBitAnd(kotlin_Int(_UShort___get_data__impl_(other)), 65535))

def UShort__compareTo_impl(this, other):
    tmp = unboxIntrinsic(this)
    return UShort__compareTo_impl(tmp, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_5e428dde)

def UShort__compareTo_impl(this, other):
    tmp0_compareTo_0 = _init_(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535))
    return uintCompare(_UInt___get_data__impl_(tmp0_compareTo_0), _UInt___get_data__impl_(other))

def UShort__compareTo_impl(this, other):
    tmp0_compareTo_0 = _init_(_and(_init_(65535, 0)))
    return ulongCompare(_ULong___get_data__impl_(tmp0_compareTo_0), _ULong___get_data__impl_(other))

def UShort__plus_impl(this, other):
    tmp0_plus_0 = _init_(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535))
    tmp1_plus_0 = _init_(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(other)), 255))
    return _init_(jsBitOr(jsPlus(_UInt___get_data__impl_(tmp0_plus_0), _UInt___get_data__impl_(tmp1_plus_0)), 0))

def UShort__plus_impl(this, other):
    tmp0_plus_0 = _init_(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535))
    tmp1_plus_0 = _init_(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(other)), 65535))
    return _init_(jsBitOr(jsPlus(_UInt___get_data__impl_(tmp0_plus_0), _UInt___get_data__impl_(tmp1_plus_0)), 0))

def UShort__plus_impl(this, other):
    tmp0_plus_0 = _init_(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535))
    return _init_(jsBitOr(jsPlus(_UInt___get_data__impl_(tmp0_plus_0), _UInt___get_data__impl_(other)), 0))

def UShort__plus_impl(this, other):
    tmp0_plus_0 = _init_(_and(_init_(65535, 0)))
    return _init_(plus(_ULong___get_data__impl_(other)))

def UShort__minus_impl(this, other):
    tmp0_minus_0 = _init_(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535))
    tmp1_minus_0 = _init_(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(other)), 255))
    return _init_(jsBitOr(jsMinus(_UInt___get_data__impl_(tmp0_minus_0), _UInt___get_data__impl_(tmp1_minus_0)), 0))

def UShort__minus_impl(this, other):
    tmp0_minus_0 = _init_(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535))
    tmp1_minus_0 = _init_(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(other)), 65535))
    return _init_(jsBitOr(jsMinus(_UInt___get_data__impl_(tmp0_minus_0), _UInt___get_data__impl_(tmp1_minus_0)), 0))

def UShort__minus_impl(this, other):
    tmp0_minus_0 = _init_(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535))
    return _init_(jsBitOr(jsMinus(_UInt___get_data__impl_(tmp0_minus_0), _UInt___get_data__impl_(other)), 0))

def UShort__minus_impl(this, other):
    tmp0_minus_0 = _init_(_and(_init_(65535, 0)))
    return _init_(minus(_ULong___get_data__impl_(other)))

def UShort__times_impl(this, other):
    tmp0_times_0 = _init_(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535))
    tmp1_times_0 = _init_(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(other)), 255))
    return _init_(imul(_UInt___get_data__impl_(tmp0_times_0), _UInt___get_data__impl_(tmp1_times_0)))

def UShort__times_impl(this, other):
    tmp0_times_0 = _init_(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535))
    tmp1_times_0 = _init_(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(other)), 65535))
    return _init_(imul(_UInt___get_data__impl_(tmp0_times_0), _UInt___get_data__impl_(tmp1_times_0)))

def UShort__times_impl(this, other):
    tmp0_times_0 = _init_(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535))
    return _init_(imul(_UInt___get_data__impl_(tmp0_times_0), _UInt___get_data__impl_(other)))

def UShort__times_impl(this, other):
    tmp0_times_0 = _init_(_and(_init_(65535, 0)))
    return _init_(times(_ULong___get_data__impl_(other)))

def UShort__div_impl(this, other):
    tmp0_div_0 = _init_(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535))
    tmp1_div_0 = _init_(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(other)), 255))
    return uintDivide(tmp0_div_0, tmp1_div_0)

def UShort__div_impl(this, other):
    tmp0_div_0 = _init_(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535))
    tmp1_div_0 = _init_(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(other)), 65535))
    return uintDivide(tmp0_div_0, tmp1_div_0)

def UShort__div_impl(this, other):
    tmp0_div_0 = _init_(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535))
    return uintDivide(tmp0_div_0, other)

def UShort__div_impl(this, other):
    tmp0_div_0 = _init_(_and(_init_(65535, 0)))
    return ulongDivide(tmp0_div_0, other)

def UShort__rem_impl(this, other):
    tmp0_rem_0 = _init_(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535))
    tmp1_rem_0 = _init_(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(other)), 255))
    return uintRemainder(tmp0_rem_0, tmp1_rem_0)

def UShort__rem_impl(this, other):
    tmp0_rem_0 = _init_(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535))
    tmp1_rem_0 = _init_(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(other)), 65535))
    return uintRemainder(tmp0_rem_0, tmp1_rem_0)

def UShort__rem_impl(this, other):
    tmp0_rem_0 = _init_(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535))
    return uintRemainder(tmp0_rem_0, other)

def UShort__rem_impl(this, other):
    tmp0_rem_0 = _init_(_and(_init_(65535, 0)))
    return ulongRemainder(tmp0_rem_0, other)

def UShort__inc_impl(this):
    return _init_(numberToShort(jsPlus(_UShort___get_data__impl_(this), 1)))

def UShort__dec_impl(this):
    return _init_(numberToShort(jsMinus(_UShort___get_data__impl_(this), 1)))

def UShort__rangeTo_impl(this, other):
    tmp = _init_(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535))
    return _init_(tmp, _init_(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(other)), 65535)))

def UShort__and_impl(this, other):
    tmp0_and_0 = _UShort___get_data__impl_(this)
    tmp1_and_0 = _UShort___get_data__impl_(other)
    return _init_(toShort(jsBitAnd(kotlin_Int(tmp0_and_0), kotlin_Int(tmp1_and_0))))

def UShort__or_impl(this, other):
    tmp0_or_0 = _UShort___get_data__impl_(this)
    tmp1_or_0 = _UShort___get_data__impl_(other)
    return _init_(toShort(jsBitOr(kotlin_Int(tmp0_or_0), kotlin_Int(tmp1_or_0))))

def UShort__xor_impl(this, other):
    tmp0_xor_0 = _UShort___get_data__impl_(this)
    tmp1_xor_0 = _UShort___get_data__impl_(other)
    return _init_(toShort(jsBitXor(kotlin_Int(tmp0_xor_0), kotlin_Int(tmp1_xor_0))))

def UShort__inv_impl(this):
    tmp0_inv_0 = _UShort___get_data__impl_(this)
    return _init_(toShort(jsBitNot(kotlin_Int(tmp0_inv_0))))

def UShort__toByte_impl(this):
    return toByte(_UShort___get_data__impl_(this))

def UShort__toShort_impl(this):
    return _UShort___get_data__impl_(this)

def UShort__toInt_impl(this):
    return jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535)

def UShort__toLong_impl(this):
    return _and(_init_(65535, 0))

def UShort__toUByte_impl(this):
    tmp0_toUByte_0 = _UShort___get_data__impl_(this)
    return _init_(toByte(tmp0_toUByte_0))

def UShort__toUShort_impl(this):
    return this

def UShort__toUInt_impl(this):
    return _init_(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535))

def UShort__toULong_impl(this):
    return _init_(_and(_init_(65535, 0)))

def UShort__toFloat_impl(this):
    return kotlin_Float(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535))

def UShort__toDouble_impl(this):
    return kotlin_Double(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535))

def UShort__toString_impl(this):
    return toString()

def UShort__hashCode_impl(this):
    return data

def UShort__equals_impl(this, other):
    if jsNot(jsInstanceOf(other, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_7ecf4608
    
    if True:
        pass
    
    tmp0_other_with_cast = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_50be06c0
    if jsNot(jsEqeqeq(data, data)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_786de0a3
    
    return True

class UShort:
    pass

def toUShort():
    return _init_(toShort(_this_))

def toUShort():
    return _init_(toShort())

def toUShort():
    return _init_(_this_)

def _get_array_(_this):
    return array

def _set_index_(_this, _set___):
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_77aa566a

def _get_index_(_this):
    return index

def _UShortArray___get_storage__impl_(this):
    return storage

def _UShortArray___init__impl_(size):
    tmp = _init_(int16Array(size))
    return tmp

def UShortArray__get_impl(this, index):
    tmp0_toUShort_0 = jsArrayGet(_UShortArray___get_storage__impl_(this), index)
    return _init_(tmp0_toUShort_0)

def UShortArray__set_impl(this, index, value):
    tmp = _UShortArray___get_storage__impl_(this)
    jsArraySet(tmp, index, _UShort___get_data__impl_(value))

def _UShortArray___get_size__impl_(this):
    return jsArrayLength(_UShortArray___get_storage__impl_(this))

def UShortArray__iterator_impl(this):
    return _init_(_UShortArray___get_storage__impl_(this))

class Iterator:
    pass

def UShortArray__contains_impl(this, element):
    tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_510a5fe1
    if jsNot(jsInstanceOf(tmp, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_307eb95f
    
    if True:
        pass
    
    tmp = _UShortArray___get_storage__impl_(this)
    return contains(_UShort___get_data__impl_(element))

def UShortArray__contains_impl(this, element):
    if jsNot(jsInstanceOf(element, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_4dec9271
    
    if True:
        pass
    
    tmp = unboxIntrinsic(this)
    return UShortArray__contains_impl(tmp, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_7d9d4205)

def UShortArray__containsAll_impl(this, elements):
    tmp_ret_0
    visitDoWhileLoop_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_4eb3dacc
    return tmp_ret_0

def UShortArray__containsAll_impl(this, elements):
    return UShortArray__containsAll_impl(unboxIntrinsic(this), elements)

def UShortArray__isEmpty_impl(this):
    return jsEqeqeq(jsArrayLength(_UShortArray___get_storage__impl_(this)), 0)

def UShortArray__toString_impl(this):
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_26569cfa

def UShortArray__hashCode_impl(this):
    return hashCode(storage)

def UShortArray__equals_impl(this, other):
    if jsNot(jsInstanceOf(other, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_72b4ecb2
    
    if True:
        pass
    
    tmp0_other_with_cast = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_44a2f289
    if jsNot(equals(storage, storage)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_4582da06
    
    return True

class UShortArray:
    pass

def uintCompare(v1, v2):
    return compareTo(jsBitXor(v1, MIN_VALUE), jsBitXor(v2, MIN_VALUE))

def uintDivide(v1, v2):
    tmp = _and(_init_(-1, 0))
    tmp0_toUInt_0 = div(_and(_init_(-1, 0)))
    return _init_(toInt())

def uintRemainder(v1, v2):
    tmp = _and(_init_(-1, 0))
    tmp0_toUInt_0 = rem(_and(_init_(-1, 0)))
    return _init_(toInt())

def uintToDouble(v):
    return jsPlus(kotlin_Double(jsBitAnd(v, MAX_VALUE)), jsMult(kotlin_Double(jsBitShiftL(jsBitShiftRU(v, 31), 30)), 2))

def ulongCompare(v1, v2):
    return compareTo(xor(_init_(0, -2147483648)))

def ulongDivide(v1, v2):
    dividend = _ULong___get_data__impl_(v1)
    divisor = _ULong___get_data__impl_(v2)
    if jsLt(compareTo(_init_(0, 0)), 0):
        tmp
        if jsLt(ulongCompare(_ULong___get_data__impl_(v1), _ULong___get_data__impl_(v2)), 0):
            tmp = _init_(_init_(0, 0))
        
        if True:
            if True:
                tmp = _init_(_init_(1, 0))
            
        
        return tmp
    
    if jsGtEq(compareTo(_init_(0, 0)), 0):
        return _init_(div(divisor))
    
    quotient = shl(1)
    rem = minus(times(divisor))
    tmp
    tmp0_compareTo_0 = _init_(rem)
    tmp1_compareTo_0 = _init_(divisor)
    if jsGtEq(ulongCompare(_ULong___get_data__impl_(tmp0_compareTo_0), _ULong___get_data__impl_(tmp1_compareTo_0)), 0):
        tmp = 1
    
    if True:
        if True:
            tmp = 0
        
    
    tmp2_plus_0 = tmp
    return _init_(plus(toLong(tmp2_plus_0)))

def ulongRemainder(v1, v2):
    dividend = _ULong___get_data__impl_(v1)
    divisor = _ULong___get_data__impl_(v2)
    if jsLt(compareTo(_init_(0, 0)), 0):
        tmp
        if jsLt(ulongCompare(_ULong___get_data__impl_(v1), _ULong___get_data__impl_(v2)), 0):
            tmp = v1
        
        if True:
            if True:
                tmp = _init_(minus(_ULong___get_data__impl_(v2)))
            
        
        return tmp
    
    if jsGtEq(compareTo(_init_(0, 0)), 0):
        return _init_(rem(divisor))
    
    quotient = shl(1)
    rem = minus(times(divisor))
    tmp
    tmp0_compareTo_0 = _init_(rem)
    tmp1_compareTo_0 = _init_(divisor)
    if jsGtEq(ulongCompare(_ULong___get_data__impl_(tmp0_compareTo_0), _ULong___get_data__impl_(tmp1_compareTo_0)), 0):
        tmp = divisor
    
    if True:
        if True:
            tmp = _init_(0, 0)
        
    
    return _init_(minus(tmp))

def ulongToDouble(v):
    return jsPlus(jsMult(toDouble(), 2048), toDouble())

def ulongToString(v):
    return ulongToString(v, 10)

def ulongToString(v, base):
    if jsGtEq(compareTo(_init_(0, 0)), 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_39adf4e6
    
    tmp0_div_0 = ushr(1)
    quotient = shl(1)
    tmp1_times_0 = quotient
    rem = minus(times(toLong(base)))
    if jsGtEq(compareTo(toLong(base)), 0):
        tmp2_minus_0 = rem
        rem = minus(toLong(base))
        tmp3_plus_0 = quotient
        tmp4_plus_0 = 1
        quotient = plus(toLong(tmp4_plus_0))
    
    return jsPlus(toString(base), toString(base))

def doubleToUInt(v):
    tmp
    if isNaN():
        tmp = _init_(0)
    
    if True:
        tmp0_toDouble_0 = _init_(0)
        if jsLtEq(v, uintToDouble(_UInt___get_data__impl_(tmp0_toDouble_0))):
            tmp = _init_(0)
        
        if True:
            tmp1_toDouble_0 = _init_(-1)
            if jsGtEq(v, uintToDouble(_UInt___get_data__impl_(tmp1_toDouble_0))):
                tmp = _init_(-1)
            
            if True:
                if jsLtEq(v, kotlin_Double(MAX_VALUE)):
                    tmp2_toUInt_0 = numberToInt(v)
                    tmp = _init_(tmp2_toUInt_0)
                
                if True:
                    if True:
                        tmp3_toUInt_0 = numberToInt(jsMinus(v, MAX_VALUE))
                        tmp5_plus_0 = _init_(tmp3_toUInt_0)
                        tmp4_toUInt_0 = MAX_VALUE
                        tmp6_plus_0 = _init_(tmp4_toUInt_0)
                        tmp = _init_(jsBitOr(jsPlus(_UInt___get_data__impl_(tmp5_plus_0), _UInt___get_data__impl_(tmp6_plus_0)), 0))
                    
                
            
        
    
    return tmp

def doubleToULong(v):
    tmp
    if isNaN():
        tmp = _init_(_init_(0, 0))
    
    if True:
        tmp0_toDouble_0 = _init_(_init_(0, 0))
        if jsLtEq(v, ulongToDouble(_ULong___get_data__impl_(tmp0_toDouble_0))):
            tmp = _init_(_init_(0, 0))
        
        if True:
            tmp1_toDouble_0 = _init_(_init_(-1, -1))
            if jsGtEq(v, ulongToDouble(_ULong___get_data__impl_(tmp1_toDouble_0))):
                tmp = _init_(_init_(-1, -1))
            
            if True:
                if jsLt(v, 9.223372036854776E18):
                    tmp2_toULong_0 = numberToLong(v)
                    tmp = _init_(tmp2_toULong_0)
                
                if True:
                    if True:
                        tmp3_toULong_0 = numberToLong(jsMinus(v, 9.223372036854776E18))
                        tmp4_plus_0 = _init_(tmp3_toULong_0)
                        tmp5_plus_0 = _init_(_init_(0, -2147483648))
                        tmp = _init_(plus(_ULong___get_data__impl_(tmp5_plus_0)))
                    
                
            
        
    
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

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_78c4bea3 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_22336af7 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_7d814dc4 = 0
def values():
    return arrayLiteral(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_323f7bf)

def valueOf(value):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_186da764

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_2bbf85e2 = 0
def DeprecationLevel_initEntries():
    if DeprecationLevel_entriesInitialized:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_1f40fddd
    
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_3640989b
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_4809035f
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_20d9f6b8
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_3b9bdbe8

class DeprecationLevel:
    pass

class PublishedApi:
    pass

class ParameterName:
    pass

def Deprecated_init__Init_(message, replaceWith, level, _mask0, _marker, _this):
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 2), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_61af0834
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 4), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_717a5a92
    
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_27af34df
    return _this

def Deprecated_init__Create_(message, replaceWith, level, _mask0, _marker):
    return Deprecated_init__Init_(message, replaceWith, level, _mask0, _marker, Object_create())

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

def _get_finalElement_(_this):
    return finalElement

def _set_hasNext_(_this, _set___):
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_4a593c3c

def _get_hasNext_(_this):
    return hasNext

def _set_next_(_this, _set___):
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_606cf551

def _get_next_(_this):
    return next

class IntProgressionIterator:
    pass

def _get_finalElement_(_this):
    return finalElement

def _set_hasNext_(_this, _set___):
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_1ff45d4f

def _get_hasNext_(_this):
    return hasNext

def _set_next_(_this, _set___):
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_63a7a23a

def _get_next_(_this):
    return next

class LongProgressionIterator:
    pass

def _get_finalElement_(_this):
    return finalElement

def _set_hasNext_(_this, _set___):
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_327fc965

def _get_hasNext_(_this):
    return hasNext

def _set_next_(_this, _set___):
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_5be2a48f

def _get_next_(_this):
    return next

class CharProgressionIterator:
    pass

class Companion:
    pass

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_676f8fab = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_1f22ac9b
    
    return Companion_instance

class IntProgression:
    pass

class Companion:
    pass

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_e39a6c2 = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_610f8dd8
    
    return Companion_instance

class LongProgression:
    pass

class Companion:
    pass

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_c1f6a16 = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_3a9b4a6e
    
    return Companion_instance

class CharProgression:
    pass

class ClosedRange:
    pass

class Companion:
    pass

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_309c821d = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_2d06acfd
    
    return Companion_instance

class IntRange:
    pass

class Companion:
    pass

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_79871eeb = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_4260a1c
    
    return Companion_instance

class LongRange:
    pass

class Companion:
    pass

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_6e094fb7 = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_5dfabe82
    
    return Companion_instance

class CharRange:
    pass

class Unit:
    pass

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_2c1ce593 = 0
def Unit_getInstance():
    if jsEqeq(Unit_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_3a0d3af1
    
    return Unit_instance

class Target:
    pass

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_1ca749cb = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_1d7dca19 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_5bc776e2 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_5bf54c2c = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_7d3abf88 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_ee49f34 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_6e74986c = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_1f112da2 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_377f0737 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_1dc823d3 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_57b57ffe = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_41df3497 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_e56c524 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_525cb986 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_2eea76bc = 0
def values():
    return arrayLiteral(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_64ebcabf)

def valueOf(value):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_17598d70

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_16e73d83 = 0
def AnnotationTarget_initEntries():
    if AnnotationTarget_entriesInitialized:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_654b7497
    
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_487d0355
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_5e2cddf4
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_6927c79a
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_125c2dd5
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_7da21081
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_5cc6a1ec
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_23bd902f
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_9993258
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_7b53ea41
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_5902527f
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_4cf7e832
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_2e29a193
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_690e308c
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_26a4b864
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_678852b5
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_608c6eb0

class AnnotationTarget:
    pass

class MustBeDocumented:
    pass

def Retention_init__Init_(value, _mask0, _marker, _this):
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 1), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_7a140446
    
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_68fa9450
    return _this

def Retention_init__Create_(value, _mask0, _marker):
    return Retention_init__Init_(value, _mask0, _marker, Object_create())

class Retention:
    pass

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_6c262251 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_74bbaa1b = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_5b3a4c43 = 0
def values():
    return arrayLiteral(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_9322cfe)

def valueOf(value):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3c42114d

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_2b05257a = 0
def AnnotationRetention_initEntries():
    if AnnotationRetention_entriesInitialized:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_7a49c426
    
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_1f396ed8
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_53e0c50
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_5dcdaf17
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_6d33e177

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
        tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_bf90cf8
    
    if jsLt(step, 0):
        tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_169f1c39
    
    if True:
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_347770a9
    
    return tmp

def getProgressionLastElement(start, end, step):
    tmp
    if jsGt(compareTo(_init_(0, 0)), 0):
        tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_36f59005
    
    if jsLt(compareTo(_init_(0, 0)), 0):
        tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_43b36393
    
    if True:
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_4f6f7a86
    
    return tmp

def differenceModulo(a, b, c):
    return mod(jsBitOr(jsMinus(mod(a, c), mod(b, c)), 0), c)

def differenceModulo(a, b, c):
    return mod(minus(mod(b, c)), c)

def mod(a, b):
    mod = jsMod(a, b)
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2f22904

def mod(a, b):
    mod = rem(b)
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_58721f69

class ByteCompanionObject:
    pass

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_74b8bc34 = 0
def ByteCompanionObject_getInstance():
    if jsEqeq(ByteCompanionObject_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_380d3099
    
    return ByteCompanionObject_instance

class ShortCompanionObject:
    pass

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_76022ebd = 0
def ShortCompanionObject_getInstance():
    if jsEqeq(ShortCompanionObject_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_6c01bc57
    
    return ShortCompanionObject_instance

class IntCompanionObject:
    pass

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_f9ad4c9 = 0
def IntCompanionObject_getInstance():
    if jsEqeq(IntCompanionObject_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_153de49f
    
    return IntCompanionObject_instance

class FloatCompanionObject:
    pass

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_1d20aae4 = 0
def FloatCompanionObject_getInstance():
    if jsEqeq(FloatCompanionObject_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_22f31149
    
    return FloatCompanionObject_instance

class DoubleCompanionObject:
    pass

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_16109bed = 0
def DoubleCompanionObject_getInstance():
    if jsEqeq(DoubleCompanionObject_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_3cf3216c
    
    return DoubleCompanionObject_instance

class StringCompanionObject:
    pass

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_1325a2ba = 0
def StringCompanionObject_getInstance():
    if jsEqeq(StringCompanionObject_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_49290bfb
    
    return StringCompanionObject_instance

class BooleanCompanionObject:
    pass

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_4152faad = 0
def BooleanCompanionObject_getInstance():
    if jsEqeq(BooleanCompanionObject_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_44e60564
    
    return BooleanCompanionObject_instance

class Comparator:
    pass

class JsName:
    pass

def toTypedArray():
    return copyToArray(_this_)

def copyToArray(collection):
    tmp
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_3f803fae:
        tmp0_unsafeCast_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_76a13b12
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
    
    if True:
        if True:
            tmp1_unsafeCast_0 = copyToArrayImpl(collection)
            tmp = kotlin_Any_(tmp1_unsafeCast_0)
        
    
    return tmp

def copyToArrayImpl(collection):
    array = kotlin_Array_kotlin_Any__(js('[]'))
    iterator = iterator()
    while hasNext():
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_1dfd39fe
    
    return array

def copyToArrayImpl(collection, array):
    if jsLt(jsArrayLength(array), _get_size_()):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_6080eac7
    
    iterator = iterator()
    index = 0
    while hasNext():
        tmp0 = index
        index = jsBitOr(jsPlus(tmp0, 1), 0)
        tmp1_unsafeCast_0 = next()
        jsArraySet(array, tmp0, kotlin_Any_(tmp1_unsafeCast_0))
    
    if jsLt(index, jsArrayLength(array)):
        tmp = index
        tmp2_unsafeCast_0 = None
        jsArraySet(array, tmp, kotlin_Any_(tmp2_unsafeCast_0))
    
    return array

class _no_name_provided_:
    pass

class _no_name_provided_:
    pass

class AbstractMutableCollection:
    pass

def _no_name_provided__factory(_elements):
    i = _init_(_elements)
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_62231c0f

def _no_name_provided__factory(_elements):
    i = _init_(_elements)
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_6e3a9891

def _get_list_(_this):
    return list

def _get_fromIndex_(_this):
    return fromIndex

def _set__size_(_this, _set___):
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_725e942b

def _get__size_(_this):
    return _size

class IteratorImpl:
    pass

class ListIteratorImpl:
    pass

class SubList:
    pass

class _no_name_provided_:
    pass

class _no_name_provided_:
    pass

class AbstractMutableList:
    pass

def _no_name_provided__factory(_elements):
    i = _init_(_elements)
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_6ae9b2f0

def _no_name_provided__factory(_elements):
    i = _init_(_elements)
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_49ccecb0

def _set_array_(_this, _set___):
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_6834f33a

def _get_array_(_this):
    return array

def _set_isReadOnly_(_this, _set___):
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_6376534c

def _get_isReadOnly_(_this):
    return isReadOnly

def ArrayList_init__Init_(_this):
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_4e78b5bb
    return _this

def ArrayList_init__Create_():
    return ArrayList_init__Init_(Object_create())

def ArrayList_init__Init_(initialCapacity, _this):
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_121f1533
    return _this

def ArrayList_init__Create_(initialCapacity):
    return ArrayList_init__Init_(initialCapacity, Object_create())

def ArrayList_init__Init_(initialCapacity, _mask0, _marker, _this):
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 1), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_371a3078
    
    ArrayList_init__Init_(initialCapacity, _this)
    return _this

def ArrayList_init__Create_(initialCapacity, _mask0, _marker):
    return ArrayList_init__Init_(initialCapacity, _mask0, _marker, Object_create())

def ArrayList_init__Init_(elements, _this):
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_6e2ff120
    return _this

def ArrayList_init__Create_(elements):
    return ArrayList_init__Init_(elements, Object_create())

def rangeCheck(_this, index):
    checkElementIndex(index, _get_size_())
    return index

def insertionRangeCheck(_this, index):
    checkPositionIndex(index, _get_size_())
    return index

class ArrayList:
    pass

def _set__stableSortingIsSupported_(_set___):
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_67f5066e

def _get__stableSortingIsSupported_():
    return _stableSortingIsSupported

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_13e76a91 = 0
class RandomAccess:
    pass

def _set_output_(_set___):
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_444958a4

def _get_output_():
    return output

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_28dae87e = 0
class BaseOutput:
    pass

class NodeJsOutput:
    pass

class BufferedOutputToConsoleLog:
    pass

def String(value):
    return kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_371ce753)

class BufferedOutput:
    pass

def println(message):
    println(message)

def output_init_():
    isNode_2 = kotlin_Boolean(js('typeof process !== \'undefined\' && process.versions && !!process.versions.node'))
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_660afeb2

def _get_EmptyContinuation_():
    return EmptyContinuation

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_2620f935 = 0
class _no_name_provided__1:
    pass

def EmptyContinuation_init_():
    tmp0_Continuation_0 = EmptyCoroutineContext_getInstance()
    return _init_(tmp0_Continuation_0)

def asDynamic():
    return _this_

def unsafeCast():
    return T(_this_)

def unsafeCast():
    return T(_this_)

class Serializable:
    pass

def pow(n):
    return pow(_this_, kotlin_Double(n))

def isNaN():
    return jsNot(jsEqeqeq(_this_, _this_))

def _get_INV_2_26_():
    return INV_2_26

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_68b59e2f = 0
def _get_INV_2_53_():
    return INV_2_53

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_79dd79eb = 0
def INV_2_26_init_():
    tmp0_pow_0 = 2.0
    tmp1_pow_0 = -26
    return pow(tmp0_pow_0, kotlin_Double(tmp1_pow_0))

def INV_2_53_init_():
    tmp0_pow_0 = 2.0
    tmp1_pow_0 = -53
    return pow(tmp0_pow_0, kotlin_Double(tmp1_pow_0))

def _get_js_():
    return _get_jClass_()

class KCallable:
    pass

class KClass:
    pass

class KClassImpl:
    pass

def _get_givenSimpleName_(_this):
    return givenSimpleName

def _get_isInstanceFunction_(_this):
    return isInstanceFunction

class PrimitiveKClassImpl:
    pass

class NothingKClassImpl:
    pass

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_5ad07e46 = 0
def NothingKClassImpl_getInstance():
    if jsEqeq(NothingKClassImpl_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_13b18bd2
    
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
    return _init_(classifier, asList(), isMarkedNullable)

def createDynamicKType():
    return DynamicKType_getInstance()

def createKTypeParameter(name, upperBounds, variance):
    tmp0_subject = variance
    kVariance = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_230e2893
    return _init_(name, asList(), kVariance, False)

def getStarKTypeProjection():
    return _get_STAR_()

def createCovariantKTypeProjection(type):
    return covariant(type)

def createInvariantKTypeProjection(type):
    return invariant(type)

def createContravariantKTypeProjection(type):
    return contravariant(type)

def asString(_this):
    if jsEqeq(variance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_544a93b0
    
    return jsPlus(prefixString(), toString())

class _no_name_provided_:
    pass

class KTypeImpl:
    pass

def prefixString():
    tmp0_subject = _this_
    tmp
    if equals(KVariance_INVARIANT_getInstance()):
        tmp = ''
    
    if equals(KVariance_IN_getInstance()):
        tmp = 'in '
    
    if equals(KVariance_OUT_getInstance()):
        tmp = 'out '
    
    if True:
        noWhenBranchMatchedException()
    
    return tmp

class DynamicKType:
    pass

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_31e420b5 = 0
def DynamicKType_getInstance():
    if jsEqeq(DynamicKType_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_1d5c1e0b
    
    return DynamicKType_instance

def _no_name_provided__factory(this_0):
    i = _init_(this_0)
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_3cd39478

class KTypeParameterImpl:
    pass

def _get_functionClasses_():
    return functionClasses

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_3bd466bd = 0
class _no_name_provided_:
    pass

class _no_name_provided_:
    pass

class _no_name_provided_:
    pass

class _no_name_provided_:
    pass

class _no_name_provided_:
    pass

class _no_name_provided_:
    pass

class _no_name_provided_:
    pass

class _no_name_provided_:
    pass

class _no_name_provided_:
    pass

class _no_name_provided_:
    pass

class _no_name_provided_:
    pass

class _no_name_provided_:
    pass

class _no_name_provided_:
    pass

class _no_name_provided_:
    pass

class _no_name_provided_:
    pass

class _no_name_provided_:
    pass

class _no_name_provided_:
    pass

class _no_name_provided_:
    pass

class _no_name_provided_:
    pass

class _no_name_provided_:
    pass

class PrimitiveClasses:
    pass

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_9d45e6e = 0
def PrimitiveClasses_getInstance():
    if jsEqeq(PrimitiveClasses_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_352a4317
    
    return PrimitiveClasses_instance

def _no_name_provided__factory():
    i = _init_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_3675ad98

def _no_name_provided__factory():
    i = _init_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_755fbfab

def _no_name_provided__factory():
    i = _init_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_23d0a0

def _no_name_provided__factory():
    i = _init_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_174058f0

def _no_name_provided__factory():
    i = _init_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_259fabf7

def _no_name_provided__factory():
    i = _init_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_3b4e6329

def _no_name_provided__factory():
    i = _init_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_3c7da546

def _no_name_provided__factory():
    i = _init_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_4fe03311

def _no_name_provided__factory():
    i = _init_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_4182abba

def _no_name_provided__factory():
    i = _init_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_342dc6d4

def _no_name_provided__factory():
    i = _init_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_66f02ece

def _no_name_provided__factory():
    i = _init_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_28e8c2d6

def _no_name_provided__factory():
    i = _init_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_2242013

def _no_name_provided__factory():
    i = _init_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_7a287117

def _no_name_provided__factory():
    i = _init_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_5eb0f030

def _no_name_provided__factory():
    i = _init_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_6d97c8aa

def _no_name_provided__factory():
    i = _init_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_61b4da5c

def _no_name_provided__factory():
    i = _init_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_5f1f59e3

def _no_name_provided__factory():
    i = _init_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_20f21dd9

def _no_name_provided__factory(_arity):
    i = _init_(_arity)
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_261ddbf5

def functionClasses_init_():
    tmp0_arrayOfNulls_0 = 0
    return fillArrayVal(Array(tmp0_arrayOfNulls_0), None)

def getKClass(jClass):
    tmp
    if kotlin_Boolean(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_4fb53b76):
        tmp = getKClassM(kotlin_Any_(jClass))
    
    if True:
        tmp = getKClass1(kotlin_Any_(jClass))
    
    return tmp

def getKClassM(jClasses):
    tmp0_subject = jsArrayLength(jClasses)
    tmp
    if jsEqeqeq(tmp0_subject, 1):
        tmp = getKClass1(jsArrayGet(jClasses, 0))
    
    if jsEqeqeq(tmp0_subject, 0):
        tmp0_unsafeCast_0 = NothingKClassImpl_getInstance()
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
    
    if True:
        tmp1_unsafeCast_0 = _init_()
        tmp = kotlin_Any_(tmp1_unsafeCast_0)
    
    return tmp

def getKClass1(jClass):
    if jsEqeqeq(jClass, js('String')):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_15ddb82a
    
    metadata = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicMemberExpressionImpl_73ffe7b0
    tmp
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_30bd925c:
        tmp
        if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_5796ae15:
            kClass = _init_(jClass)
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_d4594a8
            tmp = kClass
        
        if True:
            tmp = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicMemberExpressionImpl_67744663
        
        tmp = kotlin_reflect_KClass_T_(tmp)
    
    if True:
        tmp = _init_(jClass)
    
    return tmp

def getKClassFromExpression(e):
    tmp0_subject = jsTypeOf(e)
    tmp
    if jsEqeqeq(tmp0_subject, 'string'):
        tmp = stringClass
    
    if jsEqeqeq(tmp0_subject, 'number'):
        tmp
        tmp0_asDynamic_0 = jsBitwiseOr(e, 0)
        if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_158bd27d:
            tmp = intClass
        
        if True:
            if True:
                tmp = doubleClass
            
        
        tmp = tmp
    
    if jsEqeqeq(tmp0_subject, 'boolean'):
        tmp = booleanClass
    
    if jsEqeqeq(tmp0_subject, 'function'):
        tmp = PrimitiveClasses_getInstance()
        tmp = functionClass(kotlin_Int(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicMemberExpressionImpl_21440e36))
    
    if True:
        tmp
        if isBooleanArray(e):
            tmp = booleanArrayClass
        
        if True:
            if isCharArray(e):
                tmp = charArrayClass
            
            if True:
                if isByteArray(e):
                    tmp = byteArrayClass
                
                if True:
                    if isShortArray(e):
                        tmp = shortArrayClass
                    
                    if True:
                        if isIntArray(e):
                            tmp = intArrayClass
                        
                        if True:
                            if isLongArray(e):
                                tmp = longArrayClass
                            
                            if True:
                                if isFloatArray(e):
                                    tmp = floatArrayClass
                                
                                if True:
                                    if isDoubleArray(e):
                                        tmp = doubleArrayClass
                                    
                                    if True:
                                        if isInterface(e, jsClass()):
                                            tmp = getKClass(jsClass())
                                        
                                        if True:
                                            if isArray(e):
                                                tmp = arrayClass
                                            
                                            if True:
                                                if True:
                                                    constructor = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicMemberExpressionImpl_2662997a
                                                    tmp
                                                    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_72ab75c:
                                                        tmp = anyClass
                                                    
                                                    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_30f39d9d:
                                                        tmp = throwableClass
                                                    
                                                    if True:
                                                        jsClass = kotlin_js_JsClass_T_(constructor)
                                                        tmp = getKClass1(jsClass)
                                                    
                                                    tmp = tmp
                                                
                                            
                                        
                                    
                                
                            
                        
                    
                
            
        
        tmp = tmp
    
    tmp1_unsafeCast_0 = tmp
    return kotlin_Any_(tmp1_unsafeCast_0)

class Appendable:
    pass

def StringBuilder_init__Init_(capacity, _this):
    StringBuilder_init__Init_(_this)
    return _this

def StringBuilder_init__Create_(capacity):
    return StringBuilder_init__Init_(capacity, Object_create())

def StringBuilder_init__Init_(content, _this):
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_1cc784c9
    return _this

def StringBuilder_init__Create_(content):
    return StringBuilder_init__Init_(content, Object_create())

def StringBuilder_init__Init_(_this):
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_18a71e25
    return _this

def StringBuilder_init__Create_():
    return StringBuilder_init__Init_(Object_create())

def _set_string_(_this, _set___):
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_26aeeac9

def _get_string_(_this):
    return string

def checkReplaceRange(_this, startIndex, endIndex, length):
    if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6b86a5a4:
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_ecd59a3
    
    if jsGt(startIndex, endIndex):
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_56984e92
    

class StringBuilder:
    pass

def isLowSurrogate():
    containsLower = _init_(56320)
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_493b0b09

def isHighSurrogate():
    containsLower = _init_(55296)
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_5be38ef2

def checkRadix(radix):
    if jsNot(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_482741af):
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_466d87a1
    
    return radix

def _get_STRING_CASE_INSENSITIVE_ORDER_():
    return STRING_CASE_INSENSITIVE_ORDER

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_7d6f31ef = 0
def nativeLastIndexOf(str, fromIndex):
    return kotlin_Int(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_158f30b5)

def substring(startIndex, endIndex):
    return kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_84b0639)

def substring(startIndex):
    return kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_1c45c8ad)

def compareTo(other, ignoreCase):
    if ignoreCase:
        n1 = jsArrayLength(_this_)
        n2 = jsArrayLength(other)
        min = min(int32ArrayOf(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_7a1be5d6))
        if jsEqeqeq(min, 0):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_4115b8a7
        
        start = 0
        while True:
            tmp0_minOf_0 = jsBitOr(jsPlus(start, 16), 0)
            end = min(int32ArrayOf(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_4d704218))
            tmp1_substring_0 = start
            s1 = kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_64fd2816)
            tmp2_substring_0 = start
            s2 = kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_6cd7d43f)
            if jsNot(jsEqeqeq(s1, s2)):
                tmp3_toUpperCase_0 = s1
                s1 = kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_5dbe891a)
                tmp4_toUpperCase_0 = s2
                s2 = kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_2a961de3)
                if jsNot(jsEqeqeq(s1, s2)):
                    tmp5_toLowerCase_0 = s1
                    s1 = kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_4f3ea60d)
                    tmp6_toLowerCase_0 = s2
                    s2 = kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_773bccc3)
                    if jsNot(jsEqeqeq(s1, s2)):
                        return compareTo(s1, s2)
                    
                
            
            if jsEqeqeq(end, min):
                visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrBreakImpl_4b477d05
            
            start = end
        
        return jsBitOr(jsMinus(n1, n2), 0)
    
    if True:
        return compareTo(_this_, other)
    

def compareTo_default(other, ignoreCase, _mask0, _handler):
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 2), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_6fc75d9c
    
    return compareTo(other, ignoreCase)

def toUpperCase():
    return kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_41d1b958)

def toLowerCase():
    return kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_8cd6635)

def concatToString():
    result = ''
    indexedObject = _this_
    inductionVariable = 0
    last = jsArrayLength(indexedObject)
    while jsLt(inductionVariable, last):
        char = jsArrayGet(indexedObject, inductionVariable)
        inductionVariable = jsBitOr(jsPlus(inductionVariable, 1), 0)
        result = jsPlus(result, char)
    
    return result

def concatToString(startIndex, endIndex):
    checkBoundsIndexes(startIndex, endIndex, jsArrayLength(_this_))
    result = ''
    inductionVariable = startIndex
    if jsLt(inductionVariable, endIndex):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_3984f360
    
    return result

def concatToString_default(startIndex, endIndex, _mask0, _handler):
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 1), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_2454ee88
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 2), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_7cc87859
    
    return concatToString(startIndex, endIndex)

class sam_kotlin_Comparator_0:
    pass

class _no_name_provided_:
    pass

def _no_name_provided__factory():
    i = _init_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_218f65a8

def STRING_CASE_INSENSITIVE_ORDER_init_():
    tmp = _no_name_provided__factory()
    return _init_(tmp)

def _get_REPLACEMENT_BYTE_SEQUENCE_():
    return REPLACEMENT_BYTE_SEQUENCE

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_39d0775c = 0
def REPLACEMENT_BYTE_SEQUENCE_init_():
    tmp0_byteArrayOf_0 = int8ArrayOf(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_5a5e7ddf)
    return tmp0_byteArrayOf_0

def _get_value_(_this):
    return value

class Companion:
    pass

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_7e2f2791 = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_383cd5d8
    
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

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_51b75097 = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_41f968b0
    
    return Companion_instance

class Enum:
    pass

def byteArrayOf(elements):
    return elements

def arrayOf(elements):
    return kotlin_Any_(elements)

def toString():
    tmp0_safe_receiver = _this_
    tmp1_elvis_lhs = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_382d4ad8
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_aed8be

def plus(other):
    tmp2_safe_receiver = _this_
    tmp3_elvis_lhs = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_7c36ce16
    tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4407b019
    tmp0_safe_receiver = other
    tmp1_elvis_lhs = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_59e182
    return jsPlus(tmp, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_138c53c7)

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

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_6c1ff6a9 = 0
def DefaultConstructorMarker_getInstance():
    if jsEqeq(DefaultConstructorMarker_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_50e7a238
    
    return DefaultConstructorMarker_instance

def fillArrayVal(array, initValue):
    inductionVariable = 0
    last = jsBitOr(jsMinus(jsArrayLength(array), 1), 0)
    if jsLtEq(inductionVariable, last):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_333b5a6e
    
    return array

def arrayWithFun(size, init):
    tmp0_fillArrayFun_0 = Array(size)
    result_1 = kotlin_Any_(tmp0_fillArrayFun_0)
    i_2 = 0
    while jsNot(jsEqeqeq(i_2, jsArrayLength(result_1))):
        jsArraySet(result_1, i_2, invoke(i_2))
        i_2 = jsBitOr(jsPlus(i_2, 1), 0)
        Unit_getInstance()
    
    return result_1

def fillArrayFun(array, init):
    result = kotlin_Any_(array)
    i = 0
    while jsNot(jsEqeqeq(i, jsArrayLength(result))):
        jsArraySet(result, i, invoke(i))
        i = jsBitOr(jsPlus(i, 1), 0)
        Unit_getInstance()
    
    return result

def arrayIterator(array):
    return _init_(array)

def booleanArrayIterator(array):
    return _init_(array)

def charArrayIterator(array):
    return _init_(array)

def byteArrayIterator(array):
    return _init_(array)

def shortArrayIterator(array):
    return _init_(array)

def intArrayIterator(array):
    return _init_(array)

def floatArrayIterator(array):
    return _init_(array)

def longArrayIterator(array):
    return _init_(array)

def doubleArrayIterator(array):
    return _init_(array)

def booleanArray(size):
    tmp0_withType_0 = 'BooleanArray'
    tmp1_withType_0 = fillArrayVal(Array(size), False)
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_4682b468
    tmp2_unsafeCast_0 = tmp1_withType_0
    return kotlin_Any_(tmp2_unsafeCast_0)

def charArray(size):
    tmp0_withType_0 = 'CharArray'
    tmp1_withType_0 = fillArrayVal(Array(size), _init_(0))
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_428ff618
    tmp2_unsafeCast_0 = tmp1_withType_0
    return kotlin_Any_(tmp2_unsafeCast_0)

def longArray(size):
    tmp0_withType_0 = 'LongArray'
    tmp1_withType_0 = fillArrayVal(Array(size), _init_(0, 0))
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_31cc510d
    tmp2_unsafeCast_0 = tmp1_withType_0
    return kotlin_Any_(tmp2_unsafeCast_0)

def booleanArrayOf(arr):
    tmp0_withType_0 = 'BooleanArray'
    tmp1_withType_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_2c34c819
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_75a9add6
    tmp2_unsafeCast_0 = tmp1_withType_0
    return kotlin_Any_(tmp2_unsafeCast_0)

def charArrayOf(arr):
    tmp0_withType_0 = 'CharArray'
    tmp1_withType_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_5fc3333f
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_5849ffdb
    tmp2_unsafeCast_0 = tmp1_withType_0
    return kotlin_Any_(tmp2_unsafeCast_0)

def longArrayOf(arr):
    tmp0_withType_0 = 'LongArray'
    tmp1_withType_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_34ef9879
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_983f21e
    tmp2_unsafeCast_0 = tmp1_withType_0
    return kotlin_Any_(tmp2_unsafeCast_0)

class _no_name_provided_:
    pass

class _no_name_provided_:
    pass

class _no_name_provided_:
    pass

class _no_name_provided_:
    pass

class _no_name_provided_:
    pass

class _no_name_provided_:
    pass

class _no_name_provided_:
    pass

class _no_name_provided_:
    pass

class _no_name_provided_:
    pass

def _get_buf_():
    return buf

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_5f8a0d7f = 0
def _get_bufFloat64_():
    return bufFloat64

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_3fa13835 = 0
def _get_bufFloat32_():
    return bufFloat32

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_22eccd2c = 0
def _get_bufInt32_():
    return bufInt32

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_280fa441 = 0
def _get_lowIndex_():
    return lowIndex

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_6e5506c9 = 0
def _get_highIndex_():
    return highIndex

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_4b27a3fc = 0
def getNumberHashCode(obj):
    tmp0_unsafeCast_0 = jsBitwiseOr(obj, 0)
    if jsEqeqeq(kotlin_Any_(tmp0_unsafeCast_0), obj):
        return numberToInt(obj)
    
    if True:
        pass
    
    jsArraySet(bufFloat64, 0, obj)
    return jsBitOr(jsPlus(imul(jsArrayGet(bufInt32, highIndex), 31), jsArrayGet(bufInt32, lowIndex)), 0)

def bufFloat64_init_():
    tmp0_unsafeCast_0 = _init_(buf)
    return kotlin_Any_(tmp0_unsafeCast_0)

def bufFloat32_init_():
    tmp0_unsafeCast_0 = _init_(buf)
    return kotlin_Any_(tmp0_unsafeCast_0)

def bufInt32_init_():
    tmp0_unsafeCast_0 = _init_(buf)
    return kotlin_Any_(tmp0_unsafeCast_0)

def lowIndex_init_():
    jsArraySet(bufFloat64, 0, -1.0)
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2b112657

class DoNotIntrinsify:
    pass

def charSequenceGet(a, index):
    tmp
    if isString(a):
        tmp0_unsafeCast_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_5bc3c4e5
        tmp = _init_(kotlin_Any_(tmp0_unsafeCast_0))
    
    if True:
        tmp = get(index)
    
    return tmp

def isString(a):
    return jsEqeqeq(jsTypeOf(a), 'string')

def charSequenceLength(a):
    tmp
    if isString(a):
        tmp0_unsafeCast_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicMemberExpressionImpl_25c5fc41
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
    
    if True:
        tmp = _get_length_()
    
    return tmp

def charSequenceSubSequence(a, startIndex, endIndex):
    tmp
    if isString(a):
        tmp0_unsafeCast_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_4d73b25b
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
    
    if True:
        tmp = subSequence(startIndex, endIndex)
    
    return tmp

def arrayToString(array):
    return joinToString_default(', ', '[', ']', 0, None, _no_name_provided__factory(), 24, None)

class _no_name_provided_:
    pass

def _no_name_provided__factory():
    i = _init_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_7548f7cd

def compareTo(a, b):
    tmp0_subject = jsTypeOf(a)
    tmp
    if jsEqeqeq(tmp0_subject, 'number'):
        tmp
        if jsEqeqeq(jsTypeOf(b), 'number'):
            tmp = doubleCompareTo(a, b)
        
        if True:
            if jsInstanceOf(b, jsClass()):
                tmp = doubleCompareTo(a, toDouble())
            
            if True:
                if True:
                    tmp = primitiveCompareTo(a, b)
                
            
        
        tmp = tmp
    
    if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2e5f9491:
        tmp = primitiveCompareTo(a, b)
    
    if True:
        tmp = compareToDoNotIntrinsicify(kotlin_Comparable_dynamic_(a), b)
    
    return tmp

def doubleCompareTo(a, b):
    tmp
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_c92d694:
        tmp = -1
    
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_60adea01:
        tmp = 1
    
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_75ba33b8:
        tmp
        if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_58da6f7d:
            tmp = 0
        
        if True:
            tmp0_asDynamic_0 = 1
            ia = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_2471cfa0
            tmp
            tmp1_asDynamic_0 = 1
            if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_48ca44cd:
                tmp = 0
            
            if True:
                if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_62267a22:
                    tmp = -1
                
                if True:
                    if True:
                        tmp = 1
                    
                
            
            tmp = tmp
        
        tmp = tmp
    
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_63a9ab7d:
        tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6e0d30e4
    
    if True:
        tmp = -1
    
    return tmp

def primitiveCompareTo(a, b):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_14d2b5bf

def compareToDoNotIntrinsicify(a, b):
    return compareTo(b)

def construct(constructorType, resultType, args):
    return kotlin_Any(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_4cef1ea6)

def identityHashCode(obj):
    return getObjectHashCode(obj)

def getObjectHashCode(obj):
    if jsNot(jsIn('kotlinHashCodeValue$', kotlin_Any(obj))):
        hash = jsBitwiseOr(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_1dbb3001, 0)
        descriptor = js('new Object()')
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_23591a2c
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_4de3a1ca
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_1f953e51
    
    tmp0_unsafeCast_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_72cbe3b6
    return kotlin_Any_(tmp0_unsafeCast_0)

def _get_OBJECT_HASH_CODE_PROPERTY_NAME_():
    return OBJECT_HASH_CODE_PROPERTY_NAME

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_1df1bd44 = 0
def _get_POW_2_32_():
    return POW_2_32

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_7b80be13 = 0
def toString(o):
    tmp
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_46a6b8d6:
        tmp = 'null'
    
    if isArrayish(o):
        tmp = '[...]'
    
    if True:
        tmp0_unsafeCast_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_17b3b021
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
    
    return tmp

def hashCode(obj):
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_3af30ab8:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_1a5b8f77
    
    tmp0_subject = jsTypeOf(obj)
    tmp
    if jsEqeqeq(tmp0_subject, 'object'):
        tmp = kotlin_Int(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4b74fb68)
    
    if jsEqeqeq(tmp0_subject, 'function'):
        tmp = getObjectHashCode(obj)
    
    if jsEqeqeq(tmp0_subject, 'number'):
        tmp = getNumberHashCode(kotlin_Double(obj))
    
    if jsEqeqeq(tmp0_subject, 'boolean'):
        tmp
        if kotlin_Any_(obj):
            tmp = 1
        
        if True:
            if True:
                tmp = 0
            
        
        tmp = tmp
    
    if True:
        tmp = getStringHashCode(kotlin_String(js('String(obj)')))
    
    return tmp

def getStringHashCode(str):
    hash = 0
    length = jsArrayLength(str)
    inductionVariable = 0
    last = jsBitOr(jsMinus(length, 1), 0)
    if jsLtEq(inductionVariable, last):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_7991726b
    
    return hash

def anyToString(o):
    return kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_227ca700)

def equals(obj1, obj2):
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_c4ba591:
        return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_5a4929f5
    
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_42e74fa3:
        return False
    
    if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_62ae5e9:
        return kotlin_Boolean(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_3d3362f5)
    
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_338f96f5:
        return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_7431f4b8
    
    if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_636a9d18:
        tmp
        if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_1ae3d0a8:
            tmp
            if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_7de1cc9f:
                tmp = True
            
            if True:
                tmp0_asDynamic_0 = 1
                tmp = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_334c80be
                tmp1_asDynamic_0 = 1
                tmp = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_7a506493
            
            tmp = tmp
        
        if True:
            tmp = False
        
        return tmp
    
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_63eebb56

def boxIntrinsic(x):
    tmp0_error_0 = 'Should be lowered'
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_378ffded

def unboxIntrinsic(x):
    tmp0_error_0 = 'Should be lowered'
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_21dcd0b5

def captureStack(instance, constructorFunction):
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_83b0d9f:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_303c195f
    
    if True:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_568cc1c5
    

def newThrowable(message, cause):
    throwable = js('new Error()')
    tmp
    if isUndefined(message):
        tmp
        if isUndefined(cause):
            tmp = message
        
        if True:
            tmp0_safe_receiver = cause
            tmp1_elvis_lhs = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6bc0b35c
            tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_337b9526
        
        tmp = tmp
    
    if True:
        tmp2_elvis_lhs = message
        tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_34545f5f
    
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_4fc50fee
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_5e18309e
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_26c09f3f
    return kotlin_Any_(throwable)

def isUndefined(value):
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_31360632

def extendThrowable(this_, message, cause):
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_75922191
    setPropertiesToThrowableInstance(this_, message, cause)

def setPropertiesToThrowableInstance(this_, message, cause):
    if jsNot(hasOwnPrototypeProperty(kotlin_Any(this_), 'message')):
        tmp
        if jsEqeq(message, None):
            tmp
            if jsNot(jsEqeqeq(message, None)):
                tmp0_safe_receiver = cause
                tmp1_elvis_lhs = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_670df518
                tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_96c36db
            
            if True:
                tmp = _get_undefined_()
            
            tmp = tmp
        
        if True:
            tmp = message
        
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_33c9910e
    
    if jsNot(hasOwnPrototypeProperty(kotlin_Any(this_), 'cause')):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_19146ad8
    
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_1bbbede1

def hasOwnPrototypeProperty(o, name):
    tmp0_unsafeCast_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_56803e70
    return kotlin_Any_(tmp0_unsafeCast_0)

def getContinuation():
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_7324d83

def returnIfSuspended(argument):
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_49925329

def suspendCoroutineUninterceptedOrReturnJS(block):
    return invoke(getContinuation())

def getCoroutineContext():
    return _get_context_()

def ensureNotNull(v):
    tmp
    if jsEqeq(v, None):
        THROW_NPE()
    
    if True:
        tmp = v
    
    return tmp

def THROW_NPE():
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_661fe6c4

def noWhenBranchMatchedException():
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_793c2cde

def THROW_CCE():
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_6022cf7e

def throwUninitializedPropertyAccessException(name):
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_7f83cc90

def throwKotlinNothingValueException():
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_6895b608

def THROW_ISE():
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_ed37f28

def THROW_IAE(msg):
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_3be94b12

def emptyArray():
    return kotlin_Array_T_(js('[]'))

def enumValueOfIntrinsic(name):
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_44bd11a2

def enumValuesIntrinsic():
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_7959d16a

class Companion:
    pass

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_19d6bb0c = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_70ce5a0a
    
    return Companion_instance

class Long:
    pass

def _get_ZERO_():
    return ZERO

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_7f951dd2 = 0
def _get_ONE_():
    return ONE

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_a426150 = 0
def _get_NEG_ONE_():
    return NEG_ONE

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_3f32c65f = 0
def _get_MAX_VALUE_():
    return MAX_VALUE

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_2921aa59 = 0
def _get_MIN_VALUE_():
    return MIN_VALUE

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_3bb04b53 = 0
def _get_TWO_PWR_24__():
    return TWO_PWR_24_

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_882c166 = 0
def compare(other):
    if equalsLong(other):
        return 0
    
    thisNeg = isNegative()
    otherNeg = isNegative()
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_7168741f

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
    return _init_(jsBitOr(jsBitShiftL(c16, 16), c00), jsBitOr(jsBitShiftL(c48, 16), c32))

def subtract(other):
    return add(unaryMinus())

def multiply(other):
    if isZero():
        return ZERO
    
    if isZero():
        return ZERO
    
    if equalsLong(MIN_VALUE):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2881c04a
    
    if equalsLong(MIN_VALUE):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6d31bae5
    
    if isNegative():
        tmp
        if isNegative():
            tmp = multiply(negate())
        
        if True:
            tmp = negate()
        
        return tmp
    
    if isNegative():
        return negate()
    
    if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_28a9f772:
        return fromNumber(jsMult(toNumber(), toNumber()))
    
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
    return _init_(jsBitOr(jsBitShiftL(c16, 16), c00), jsBitOr(jsBitShiftL(c48, 16), c32))

def divide(other):
    if isZero():
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_f7b6b9e
    
    if isZero():
        return ZERO
    
    if equalsLong(MIN_VALUE):
        if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6c101a64:
            return MIN_VALUE
        
        if equalsLong(MIN_VALUE):
            return ONE
        
        if True:
            halfThis = shiftRight(1)
            approx = shiftLeft(1)
            if equalsLong(ZERO):
                return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3b9a82bc
            
            if True:
                rem = subtract(multiply(approx))
                return add(div(other))
            
        
    
    if equalsLong(MIN_VALUE):
        return ZERO
    
    if isNegative():
        tmp
        if isNegative():
            tmp = div(negate())
        
        if True:
            tmp = negate()
        
        return tmp
    
    if isNegative():
        return negate()
    
    res = ZERO
    rem = _this_
    while greaterThanOrEqual(other):
        approxDouble = jsDiv(toNumber(), toNumber())
        approx2 = max(1.0, floor(approxDouble))
        log2 = ceil(jsDiv(log(approx2), _get_LN2_()))
        delta = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_5442accb
        approxRes = fromNumber(approx2)
        approxRem = multiply(other)
        while visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2ed8882e:
            approx2 = jsMinus(approx2, delta)
            approxRes = fromNumber(approx2)
            approxRem = multiply(other)
        
        if isZero():
            approxRes = ONE
        
        res = add(approxRes)
        rem = subtract(approxRem)
    
    return res

def modulo(other):
    return subtract(multiply(other))

def shiftLeft(numBits):
    numBits = jsBitAnd(numBits, 63)
    if jsEqeqeq(numBits, 0):
        return _this_
    
    if True:
        if jsLt(numBits, 32):
            return _init_(jsBitShiftL(low, numBits), jsBitOr(jsBitShiftL(high, numBits), jsBitShiftRU(low, jsBitOr(jsMinus(32, numBits), 0))))
        
        if True:
            return _init_(0, jsBitShiftL(low, jsBitOr(jsMinus(numBits, 32), 0)))
        
    

def shiftRight(numBits):
    numBits = jsBitAnd(numBits, 63)
    if jsEqeqeq(numBits, 0):
        return _this_
    
    if True:
        if jsLt(numBits, 32):
            return _init_(jsBitOr(jsBitShiftRU(low, numBits), jsBitShiftL(high, jsBitOr(jsMinus(32, numBits), 0))), jsBitShiftR(high, numBits))
        
        if True:
            return _init_(jsBitShiftR(high, jsBitOr(jsMinus(numBits, 32), 0)), visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_5632369f)
        
    

def shiftRightUnsigned(numBits):
    numBits = jsBitAnd(numBits, 63)
    if jsEqeqeq(numBits, 0):
        return _this_
    
    if True:
        if jsLt(numBits, 32):
            return _init_(jsBitOr(jsBitShiftRU(low, numBits), jsBitShiftL(high, jsBitOr(jsMinus(32, numBits), 0))), jsBitShiftRU(high, numBits))
        
        if True:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_582e8393
        
    

def toNumber():
    return jsPlus(jsMult(high, 4.294967296E9), getLowBitsUnsigned())

def equalsLong(other):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4cd451fb

def hashCode(l):
    return jsBitXor(low, high)

def toStringImpl(radix):
    if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_365d1cbf:
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_11f633f
    
    if isZero():
        return '0'
    
    if isNegative():
        if equalsLong(MIN_VALUE):
            radixLong = fromInt(radix)
            div = div(radixLong)
            rem = toInt()
            tmp = toStringImpl(radix)
            tmp0_unsafeCast_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_7ff167c4
            return jsPlus(tmp, kotlin_Any_(tmp0_unsafeCast_0))
        
        if True:
            return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_eba9ab4
        
    
    radixToPower = fromNumber(pow(kotlin_Double(radix), 6.0))
    rem = _this_
    result = ''
    while True:
        remDiv = div(radixToPower)
        intval = toInt()
        tmp1_unsafeCast_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_2b82254b
        digits = kotlin_Any_(tmp1_unsafeCast_0)
        rem = remDiv
        if isZero():
            return jsPlus(digits, result)
        
        if True:
            while jsLt(jsArrayLength(digits), 6):
                digits = jsPlus('0', digits)
            
            result = jsPlus(digits, result)
        
    

def fromInt(value):
    return _init_(value, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_577017c6)

def isNegative():
    return jsLt(high, 0)

def isZero():
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_52fec246

def isOdd():
    return jsEqeqeq(jsBitAnd(low, 1), 1)

def negate():
    return unaryMinus()

def lessThan(other):
    return jsLt(compare(other), 0)

def fromNumber(value):
    if isNaN():
        return ZERO
    
    if jsLtEq(value, -9.223372036854776E18):
        return MIN_VALUE
    
    if jsGtEq(jsPlus(value, 1), 9.223372036854776E18):
        return MAX_VALUE
    
    if jsLt(value, 0.0):
        return negate()
    
    if True:
        twoPwr32 = 4.294967296E9
        return _init_(jsBitwiseOr(jsMod(value, twoPwr32), 0), jsBitwiseOr(jsDiv(value, twoPwr32), 0))
    

def greaterThan(other):
    return jsGt(compare(other), 0)

def greaterThanOrEqual(other):
    return jsGtEq(compare(other), 0)

def getLowBitsUnsigned():
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2e2d04d7

def _get_TWO_PWR_32_DBL__():
    return TWO_PWR_32_DBL_

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_6dbf203c = 0
def _get_TWO_PWR_63_DBL__():
    return TWO_PWR_63_DBL_

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_698d07ac = 0
def imul(a_local, b_local):
    lhs = jsMult(kotlin_Double(jsBitwiseAnd(a_local, js('0xffff0000'))), kotlin_Double(jsBitwiseAnd(b_local, 65535)))
    rhs = jsMult(kotlin_Double(jsBitwiseAnd(a_local, 65535)), kotlin_Double(b_local))
    return jsBitwiseOr(jsPlus(lhs, rhs), 0)

def withType(type, array):
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_6014b386
    return array

def arrayConcat(args):
    len = jsArrayLength(args)
    tmp0_unsafeCast_0 = js('Array(len)')
    typed = kotlin_Any_(tmp0_unsafeCast_0)
    inductionVariable = 0
    last = jsBitOr(jsMinus(len, 1), 0)
    if jsLtEq(inductionVariable, last):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_7ab63914
    
    return T(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_1e954b94)

def primitiveArrayConcat(args):
    size_local = 0
    inductionVariable = 0
    last = jsBitOr(jsMinus(jsArrayLength(args), 1), 0)
    if jsLtEq(inductionVariable, last):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_3609424e
    
    a = jsArrayGet(args, 0)
    tmp1_unsafeCast_0 = js('new a.constructor(size_local)')
    result = kotlin_Any_(tmp1_unsafeCast_0)
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_6ebdd981:
        tmp2_withType_0 = kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicMemberExpressionImpl_35a7c2cc)
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_2cc42eef
    
    if True:
        pass
    
    size_local = 0
    inductionVariable = 0
    last = jsBitOr(jsMinus(jsArrayLength(args), 1), 0)
    if jsLtEq(inductionVariable, last):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_6bf552d2
    
    return kotlin_Any_(result)

def taggedArrayCopy(array):
    res = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_4eeda18f
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_60ccf498
    return kotlin_Any_(res)

def numberToByte(a):
    return toByte(numberToInt(a))

def toByte(a):
    tmp0_unsafeCast_0 = js('a << 24 >> 24')
    return kotlin_Any_(tmp0_unsafeCast_0)

def numberToInt(a):
    tmp
    if jsInstanceOf(a, jsClass()):
        tmp = toInt()
    
    if True:
        if True:
            tmp = doubleToInt(kotlin_Double(a))
        
    
    return tmp

def doubleToInt(a):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_226ddb69

def numberToDouble(a):
    tmp0_unsafeCast_0 = js('+a')
    return kotlin_Any_(tmp0_unsafeCast_0)

def numberToShort(a):
    return toShort(numberToInt(a))

def toShort(a):
    tmp0_unsafeCast_0 = js('a << 16 >> 16')
    return kotlin_Any_(tmp0_unsafeCast_0)

def numberToLong(a):
    tmp
    if jsInstanceOf(a, jsClass()):
        tmp = kotlin_Long(a)
    
    if True:
        if True:
            tmp = fromNumber(kotlin_Double(a))
        
    
    return tmp

def numberToChar(a):
    return _init_(jsBitAnd(numberToInt(a), 65535))

def toLong(a):
    return fromInt(kotlin_Int(a))

def numberRangeToNumber(start, endInclusive):
    return _init_(kotlin_Int(start), kotlin_Int(endInclusive))

def numberRangeToLong(start, endInclusive):
    return _init_(numberToLong(start), kotlin_Long(endInclusive))

def _get_propertyRefClassMetadataCache_():
    return propertyRefClassMetadataCache

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_3c20af2 = 0
def metadataObject():
    return js('{ kind: \'class\', interfaces: [] }')

def getPropertyCallableRef(name, paramCount, type, getter, setter):
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_7f1f6c22
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_6bcc277a
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_6e9d60e1
    tmp0_unsafeCast_0 = getPropertyRefClass(getter, getKPropMetadata(paramCount, setter, type))
    return kotlin_Any_(tmp0_unsafeCast_0)

def getPropertyRefClass(obj, metadata):
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_44d51c85
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_68b2ce71
    return obj

def getKPropMetadata(paramCount, setter, type):
    mdata = jsArrayGet(jsArrayGet(propertyRefClassMetadataCache, paramCount), visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_71efa55d)
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_6bc72ab6:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_2b0061b7
    
    return mdata

def getLocalDelegateReference(name, type, mutable, _lambda):
    return getPropertyCallableRef(name, 0, type, _lambda, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_7dcbb6e5)

def propertyRefClassMetadataCache_init_():
    tmp = js('{ kind: \'class\', interfaces: [] }')
    tmp0_arrayOf_0 = arrayLiteral(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_29a3e9e8)
    tmp = kotlin_Any_(tmp0_arrayOf_0)
    tmp = js('{ kind: \'class\', interfaces: [] }')
    tmp1_arrayOf_0 = arrayLiteral(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_784ceacb)
    tmp = kotlin_Any_(tmp1_arrayOf_0)
    tmp = js('{ kind: \'class\', interfaces: [] }')
    tmp2_arrayOf_0 = arrayLiteral(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_bd3df07)
    tmp3_arrayOf_0 = arrayLiteral(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_57eab3f5)
    return kotlin_Any_(tmp3_arrayOf_0)

def isArrayish(o):
    tmp
    if isJsArray(kotlin_Any(o)):
        tmp = True
    
    if True:
        tmp0_unsafeCast_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_4064cd60
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
    
    return tmp

def isJsArray(obj):
    tmp0_unsafeCast_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_4fb56bdf
    return kotlin_Any_(tmp0_unsafeCast_0)

def isInterface(obj, iface):
    tmp0_elvis_lhs = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicMemberExpressionImpl_70b38e0
    tmp
    if jsEqeq(tmp0_elvis_lhs, None):
        return False
    
    if True:
        tmp = tmp0_elvis_lhs
    
    ctor = tmp
    return isInterfaceImpl(kotlin_js_Ctor(ctor), iface)

def isInterfaceImpl(ctor, iface):
    if jsEqeqeq(ctor, iface):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_7d3405c0
    
    metadata = _get__metadata__()
    if jsNot(jsEqeq(metadata, None)):
        interfaces = _get_interfaces_()
        indexedObject = interfaces
        inductionVariable = 0
        last = jsArrayLength(indexedObject)
        while jsLt(inductionVariable, last):
            i = jsArrayGet(indexedObject, inductionVariable)
            inductionVariable = jsBitOr(jsPlus(inductionVariable, 1), 0)
            if isInterfaceImpl(i, iface):
                return True
            
        
    
    superPrototype = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2204dff6
    superConstructor = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_27ed234f
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_10130823

def isArray(obj):
    tmp
    if isJsArray(obj):
        tmp = kotlin_Boolean(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_35e59c13)
    
    if True:
        tmp = False
    
    return tmp

def isObject(obj):
    objTypeOf = jsTypeOf(obj)
    tmp0_subject = objTypeOf
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4b26a938

def isSuspendFunction(obj, arity):
    if jsEqeqeq(jsTypeOf(obj), 'function'):
        tmp0_unsafeCast_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicMemberExpressionImpl_4dd94931
        return jsEqeqeq(kotlin_Any_(tmp0_unsafeCast_0), arity)
    
    return False

def isNumber(a):
    tmp
    if jsEqeqeq(jsTypeOf(a), 'number'):
        tmp = True
    
    if True:
        tmp = jsInstanceOf(a, jsClass())
    
    return tmp

def isComparable(value):
    type = jsTypeOf(value)
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_56f809e5

def isCharSequence(value):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_23e892d3

def isBooleanArray(a):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_106f7ddd

def isByteArray(a):
    return jsInstanceOf(a, js('Int8Array'))

def isShortArray(a):
    return jsInstanceOf(a, js('Int16Array'))

def isCharArray(a):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6a554ba0

def isIntArray(a):
    return jsInstanceOf(a, js('Int32Array'))

def isFloatArray(a):
    return jsInstanceOf(a, js('Float32Array'))

def isLongArray(a):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_a8af0a3

def isDoubleArray(a):
    return jsInstanceOf(a, js('Float64Array'))

def jsIsType(obj, jsClass):
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_6f54a7be:
        return isObject(obj)
    
    if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3e914e4b:
        return False
    
    if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4e01cf43:
        return True
    
    proto = jsGetPrototypeOf(jsClass)
    tmp0_safe_receiver = proto
    constructor = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_c2622f8
    if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_5ec32f69:
        metadata = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicMemberExpressionImpl_46c8a8e0
        if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_1844e563:
            return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_5f0d1a0d
        
    
    klassMetadata = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicMemberExpressionImpl_160ecb8f
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_1bff5ad0:
        return jsInstanceOf(obj, jsClass)
    
    if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_380f934e:
        return isInterfaceImpl(kotlin_js_Ctor(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicMemberExpressionImpl_4306191), jsClass)
    
    return False

def jsGetPrototypeOf(jsClass):
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_7b255b15

def asList():
    return _init_(kotlin_Any_(_this_))

def plus(elements):
    return kotlin_Array_T_(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_20c8457f)

def copyOfRange(fromIndex, toIndex):
    checkRangeIndexes(fromIndex, toIndex, jsArrayLength(_this_))
    return kotlin_Array_T_(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_7b9866c6)

def minOf(a, b):
    return min(int32ArrayOf(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_164ee145))

def _get_resultContinuation_(_this):
    return resultContinuation

def _get__context_(_this):
    return _context

def _set_intercepted__(_this, _set___):
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_59d768de

def _get_intercepted__(_this):
    return intercepted_

def releaseIntercepted(_this):
    intercepted = intercepted_
    if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3ae8394:
        releaseInterceptedContinuation(intercepted)
    
    visitSetField_org_jetbrains_kotlin_ir_expressions_impl_IrSetFieldImpl_180f3ae8

class CoroutineImpl:
    pass

class CompletedContinuation:
    pass

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_6a89d89b = 0
def CompletedContinuation_getInstance():
    if jsEqeq(CompletedContinuation_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_39ca785e
    
    return CompletedContinuation_instance

def Exception_init__Init_(_this):
    extendThrowable(_this, _undefined(), _undefined())
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_1fa3c4f7
    return _this

def Exception_init__Create_():
    tmp = Exception_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_39d0670c)
    return tmp

def Exception_init__Init_(message, _this):
    extendThrowable(_this, message, _undefined())
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_77e7be90
    return _this

def Exception_init__Create_(message):
    tmp = Exception_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_2dff4ef9)
    return tmp

def Exception_init__Init_(message, cause, _this):
    extendThrowable(_this, message, cause)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_1e3d7df9
    return _this

def Exception_init__Create_(message, cause):
    tmp = Exception_init__Init_(message, cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_298e95ed)
    return tmp

def Exception_init__Init_(cause, _this):
    extendThrowable(_this, _undefined(), cause)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_15d5761d
    return _this

def Exception_init__Create_(cause):
    tmp = Exception_init__Init_(cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_38cde4f2)
    return tmp

class Exception:
    pass

def Error_init__Init_(_this):
    extendThrowable(_this, _undefined(), _undefined())
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_290b031e
    return _this

def Error_init__Create_():
    tmp = Error_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_9385016)
    return tmp

def Error_init__Init_(message, _this):
    extendThrowable(_this, message, _undefined())
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_34a174f8
    return _this

def Error_init__Create_(message):
    tmp = Error_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_1fafb2ae)
    return tmp

def Error_init__Init_(message, cause, _this):
    extendThrowable(_this, message, cause)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_77f965a0
    return _this

def Error_init__Create_(message, cause):
    tmp = Error_init__Init_(message, cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_18db7998)
    return tmp

def Error_init__Init_(cause, _this):
    extendThrowable(_this, _undefined(), cause)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_aeb6d4d
    return _this

def Error_init__Create_(cause):
    tmp = Error_init__Init_(cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_63b66b0f)
    return tmp

class Error:
    pass

def IllegalArgumentException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_2306d66c
    return _this

def IllegalArgumentException_init__Create_():
    tmp = IllegalArgumentException_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_31fc2a08)
    return tmp

def IllegalArgumentException_init__Init_(message, _this):
    RuntimeException_init__Init_(message, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_25329370
    return _this

def IllegalArgumentException_init__Create_(message):
    tmp = IllegalArgumentException_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_63822d44)
    return tmp

def IllegalArgumentException_init__Init_(message, cause, _this):
    RuntimeException_init__Init_(message, cause, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_ca160e0
    return _this

def IllegalArgumentException_init__Create_(message, cause):
    tmp = IllegalArgumentException_init__Init_(message, cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_b889306)
    return tmp

def IllegalArgumentException_init__Init_(cause, _this):
    RuntimeException_init__Init_(cause, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_40aabc7b
    return _this

def IllegalArgumentException_init__Create_(cause):
    tmp = IllegalArgumentException_init__Init_(cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_50d8c98c)
    return tmp

class IllegalArgumentException:
    pass

def RuntimeException_init__Init_(_this):
    Exception_init__Init_(_this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_3160fef3
    return _this

def RuntimeException_init__Create_():
    tmp = RuntimeException_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_45f4a0ee)
    return tmp

def RuntimeException_init__Init_(message, _this):
    Exception_init__Init_(message, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_60b7f05c
    return _this

def RuntimeException_init__Create_(message):
    tmp = RuntimeException_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_6ffa30e3)
    return tmp

def RuntimeException_init__Init_(message, cause, _this):
    Exception_init__Init_(message, cause, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_1dd241a0
    return _this

def RuntimeException_init__Create_(message, cause):
    tmp = RuntimeException_init__Init_(message, cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_42178353)
    return tmp

def RuntimeException_init__Init_(cause, _this):
    Exception_init__Init_(cause, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_70c825c9
    return _this

def RuntimeException_init__Create_(cause):
    tmp = RuntimeException_init__Init_(cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_39c1ba8b)
    return tmp

class RuntimeException:
    pass

def NoSuchElementException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_129d65a0
    return _this

def NoSuchElementException_init__Create_():
    tmp = NoSuchElementException_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_496e5047)
    return tmp

def NoSuchElementException_init__Init_(message, _this):
    RuntimeException_init__Init_(message, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_4e492d18
    return _this

def NoSuchElementException_init__Create_(message):
    tmp = NoSuchElementException_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_1d4c39c2)
    return tmp

class NoSuchElementException:
    pass

def IllegalStateException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_7d686953
    return _this

def IllegalStateException_init__Create_():
    tmp = IllegalStateException_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_6fd46b61)
    return tmp

def IllegalStateException_init__Init_(message, _this):
    RuntimeException_init__Init_(message, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_247f60a3
    return _this

def IllegalStateException_init__Create_(message):
    tmp = IllegalStateException_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_474b3a3d)
    return tmp

def IllegalStateException_init__Init_(message, cause, _this):
    RuntimeException_init__Init_(message, cause, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_35ae4079
    return _this

def IllegalStateException_init__Create_(message, cause):
    tmp = IllegalStateException_init__Init_(message, cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_55f00c43)
    return tmp

def IllegalStateException_init__Init_(cause, _this):
    RuntimeException_init__Init_(cause, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_1ab1e83a
    return _this

def IllegalStateException_init__Create_(cause):
    tmp = IllegalStateException_init__Init_(cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_2c9a5a1b)
    return tmp

class IllegalStateException:
    pass

def IndexOutOfBoundsException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_30df4a72
    return _this

def IndexOutOfBoundsException_init__Create_():
    tmp = IndexOutOfBoundsException_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_72ddbe12)
    return tmp

def IndexOutOfBoundsException_init__Init_(message, _this):
    RuntimeException_init__Init_(message, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_25539a73
    return _this

def IndexOutOfBoundsException_init__Create_(message):
    tmp = IndexOutOfBoundsException_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_77bb51e3)
    return tmp

class IndexOutOfBoundsException:
    pass

def UnsupportedOperationException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_6048cacf
    return _this

def UnsupportedOperationException_init__Create_():
    tmp = UnsupportedOperationException_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_6147ff01)
    return tmp

def UnsupportedOperationException_init__Init_(message, _this):
    RuntimeException_init__Init_(message, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_38407b0e
    return _this

def UnsupportedOperationException_init__Create_(message):
    tmp = UnsupportedOperationException_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_2c33bc4)
    return tmp

def UnsupportedOperationException_init__Init_(message, cause, _this):
    RuntimeException_init__Init_(message, cause, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_66d2ed64
    return _this

def UnsupportedOperationException_init__Create_(message, cause):
    tmp = UnsupportedOperationException_init__Init_(message, cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_2e3991bd)
    return tmp

def UnsupportedOperationException_init__Init_(cause, _this):
    RuntimeException_init__Init_(cause, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_798673ea
    return _this

def UnsupportedOperationException_init__Create_(cause):
    tmp = UnsupportedOperationException_init__Init_(cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_30625f51)
    return tmp

class UnsupportedOperationException:
    pass

def NullPointerException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_5cba45e8
    return _this

def NullPointerException_init__Create_():
    tmp = NullPointerException_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_7b58475e)
    return tmp

def NullPointerException_init__Init_(message, _this):
    RuntimeException_init__Init_(message, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_2034e91c
    return _this

def NullPointerException_init__Create_(message):
    tmp = NullPointerException_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_7b66c7e9)
    return tmp

class NullPointerException:
    pass

def NoWhenBranchMatchedException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_5ca758b9
    return _this

def NoWhenBranchMatchedException_init__Create_():
    tmp = NoWhenBranchMatchedException_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_2b1d39b2)
    return tmp

def NoWhenBranchMatchedException_init__Init_(message, _this):
    RuntimeException_init__Init_(message, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_56a11071
    return _this

def NoWhenBranchMatchedException_init__Create_(message):
    tmp = NoWhenBranchMatchedException_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_52c2906e)
    return tmp

def NoWhenBranchMatchedException_init__Init_(message, cause, _this):
    RuntimeException_init__Init_(message, cause, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_49c96044
    return _this

def NoWhenBranchMatchedException_init__Create_(message, cause):
    tmp = NoWhenBranchMatchedException_init__Init_(message, cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_7cba7745)
    return tmp

def NoWhenBranchMatchedException_init__Init_(cause, _this):
    RuntimeException_init__Init_(cause, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_38daeeff
    return _this

def NoWhenBranchMatchedException_init__Create_(cause):
    tmp = NoWhenBranchMatchedException_init__Init_(cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_69faffba)
    return tmp

class NoWhenBranchMatchedException:
    pass

def ClassCastException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_689719ee
    return _this

def ClassCastException_init__Create_():
    tmp = ClassCastException_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_430a748)
    return tmp

def ClassCastException_init__Init_(message, _this):
    RuntimeException_init__Init_(message, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_39b525a2
    return _this

def ClassCastException_init__Create_(message):
    tmp = ClassCastException_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_37fec49c)
    return tmp

class ClassCastException:
    pass

def UninitializedPropertyAccessException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_66c755cc
    return _this

def UninitializedPropertyAccessException_init__Create_():
    tmp = UninitializedPropertyAccessException_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_645e2cfe)
    return tmp

def UninitializedPropertyAccessException_init__Init_(message, _this):
    RuntimeException_init__Init_(message, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_57543d4c
    return _this

def UninitializedPropertyAccessException_init__Create_(message):
    tmp = UninitializedPropertyAccessException_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_6acb0d0d)
    return tmp

def UninitializedPropertyAccessException_init__Init_(message, cause, _this):
    RuntimeException_init__Init_(message, cause, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_3cd38685
    return _this

def UninitializedPropertyAccessException_init__Create_(message, cause):
    tmp = UninitializedPropertyAccessException_init__Init_(message, cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_39794db6)
    return tmp

def UninitializedPropertyAccessException_init__Init_(cause, _this):
    RuntimeException_init__Init_(cause, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_533167f0
    return _this

def UninitializedPropertyAccessException_init__Create_(cause):
    tmp = UninitializedPropertyAccessException_init__Init_(cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_1d067bce)
    return tmp

class UninitializedPropertyAccessException:
    pass

def jsIn(lhs_hack, rhs_hack):
    tmp0_unsafeCast_0 = js('lhs_hack in rhs_hack')
    return kotlin_Any_(tmp0_unsafeCast_0)

def jsBitwiseOr(lhs_hack, rhs_hack):
    tmp0_unsafeCast_0 = js('lhs_hack | rhs_hack')
    return kotlin_Any_(tmp0_unsafeCast_0)

def jsTypeOf(value_hack):
    tmp0_unsafeCast_0 = js('typeof value_hack')
    return kotlin_Any_(tmp0_unsafeCast_0)

def jsInstanceOf(obj_hack, jsClass_hack):
    tmp0_unsafeCast_0 = js('obj_hack instanceof jsClass_hack')
    return kotlin_Any_(tmp0_unsafeCast_0)

def jsBitwiseAnd(lhs_hack, rhs_hack):
    tmp0_unsafeCast_0 = js('lhs_hack & rhs_hack')
    return kotlin_Any_(tmp0_unsafeCast_0)

def toString(radix):
    return toStringImpl(checkRadix(radix))

def pythonTest():
    println('Hello world')

def exampleFromAstTest():
    fruits = listOf(arrayLiteral(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_4f347dbe))
    tmp0_iterator = iterator()
    while hasNext():
        x = next()
        println(x)
    

def returnString():
    return 'Hello from Kotlin!'
