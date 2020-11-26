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
    def _get_message_():
        pass
    
    def _get_cause_():
        pass
    
    def toString():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def _init_():
        captureStack(_this_, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_726bbe64)
    

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
    
    Level_entriesInitialized = True
    Level_WARNING_instance = _init_('WARNING', 0)
    Level_ERROR_instance = _init_('ERROR', 1)

def Experimental_init__Init_(level, _mask0, _marker, _this):
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 1), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_11675922
    
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_3d2bb013
    return _this

def Experimental_init__Create_(level, _mask0, _marker):
    return Experimental_init__Init_(level, _mask0, _marker, Object_create())

class Level:
    def _init_(name, ordinal):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_d61ac34
    
    def _get_name_():
        pass
    
    def _get_ordinal_():
        pass
    
    def compareTo(other):
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

def Level_WARNING_getInstance():
    Level_initEntries()
    return Level_WARNING_instance

def Level_ERROR_getInstance():
    Level_initEntries()
    return Level_ERROR_instance

class Experimental:
    def _init_(level):
        _this_.level = level
    
    def _get_level_():
        return level
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class WasExperimental:
    def _init_(markerClass):
        _this_.markerClass = markerClass
    
    def _get_markerClass_():
        return markerClass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class ExperimentalStdlibApi:
    def _init_():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class OptionalExpectation:
    def _init_():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class ExperimentalMultiplatform:
    def _init_():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
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
    
    Level_entriesInitialized = True
    Level_WARNING_instance = _init_('WARNING', 0)
    Level_ERROR_instance = _init_('ERROR', 1)

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
    def _init_(name, ordinal):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_37aae870
    
    def _get_name_():
        pass
    
    def _get_ordinal_():
        pass
    
    def compareTo(other):
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

def Level_WARNING_getInstance():
    Level_initEntries()
    return Level_WARNING_instance

def Level_ERROR_getInstance():
    Level_initEntries()
    return Level_ERROR_instance

class RequiresOptIn:
    def _init_(message, level):
        _this_.message = message
        _this_.level = level
    
    def _get_message_():
        return message
    
    def _get_level_():
        return level
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class OptIn:
    def _init_(markerClass):
        _this_.markerClass = markerClass
    
    def _get_markerClass_():
        return markerClass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class _no_name_provided_:
    def _init_(this_0):
        _this_.this_0 = this_0
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_5379839c
    
    def invoke(it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_5fa851ac
    
    def invoke(p1):
        return invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2d550996)
    

class AbstractCollection:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_44117b0d
    
    def _get_size_():
        pass
    
    def iterator():
        pass
    
    def contains(element):
        tmp_ret_0
        visitDoWhileLoop_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_6592f06
        return tmp_ret_0
    
    def containsAll(elements):
        tmp_ret_0
        visitDoWhileLoop_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_726d34de
        return tmp_ret_0
    
    def isEmpty():
        return jsEqeqeq(_get_size_(), 0)
    
    def toString():
        return joinToString_default(', ', '[', ']', 0, None, _no_name_provided__factory(_this_), 24, None)
    
    def toArray():
        return copyToArrayImpl(_this_)
    
    def toArray(array):
        return copyToArrayImpl(_this_, array)
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    

def _no_name_provided__factory(this_0):
    i = _init_(this_0)
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_3bd8032e

def _get_list_(_this):
    return list

def _get_fromIndex_(_this):
    return fromIndex

def _set__size_(_this, _set___):
    _this._size = _set___

def _get__size_(_this):
    return _size

class SubList:
    def _init_(list, fromIndex, toIndex):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_64829470
        _this_.list = list
        _this_.fromIndex = fromIndex
        _this_._size = 0
        checkRangeIndexes(fromIndex, toIndex, _get_size_())
        _this_._size = jsBitOr(jsMinus(toIndex, fromIndex), 0)
    
    def get(index):
        checkElementIndex(index, _size)
        return get(jsBitOr(jsPlus(fromIndex, index), 0))
    
    def _get_size_():
        return _size
    
    def toArray():
        pass
    
    def toArray(array):
        pass
    
    def contains(element):
        pass
    
    def containsAll(elements):
        pass
    
    def indexOf(element):
        pass
    
    def isEmpty():
        pass
    
    def iterator():
        pass
    
    def lastIndexOf(element):
        pass
    
    def listIterator():
        pass
    
    def listIterator(index):
        pass
    
    def subList(fromIndex, toIndex):
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class IteratorImpl:
    def _init_(_outer):
        _this_._this = _outer
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_7c857e8f
        _this_.index = 0
    
    def _set_index_(_set___):
        _this_.index = _set___
    
    def _get_index_():
        return index
    
    def hasNext():
        return jsLt(index, _get_size_())
    
    def next():
        if jsNot(hasNext()):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_3a66d97e
        
        tmp0_this = _this_
        tmp1 = index
        tmp0_this.index = jsBitOr(jsPlus(tmp1, 1), 0)
        return get(tmp1)
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class ListIteratorImpl:
    def _init_(_outer, index):
        _this_._this = _outer
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_69919fed
        checkPositionIndex(index, _get_size_())
        _set_index_(index)
    
    def hasPrevious():
        return jsGt(_get_index_(), 0)
    
    def nextIndex():
        return _get_index_()
    
    def previous():
        if jsNot(hasPrevious()):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_12dc702b
        
        tmp0_this = _this_
        _set_index_(jsBitOr(jsMinus(_get_index_(), 1), 0))
        return get(_get_index_())
    
    def previousIndex():
        return jsBitOr(jsMinus(_get_index_(), 1), 0)
    
    def _set_index_(_set___):
        pass
    
    def _get_index_():
        pass
    
    def equals(other):
        pass
    
    def hasNext():
        pass
    
    def hashCode():
        pass
    
    def next():
        pass
    
    def toString():
        pass
    

class Companion:
    def _init_():
        Companion_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_4902c584
    
    def checkElementIndex(index, size):
        if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_5b9fbaca:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_236a3e4
        
    
    def checkPositionIndex(index, size):
        if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3dee7142:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_40105b39
        
    
    def checkRangeIndexes(fromIndex, toIndex, size):
        if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_59a9769e:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_1b96d447
        
        if jsGt(fromIndex, toIndex):
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_29d81c22
        
    
    def checkBoundsIndexes(startIndex, endIndex, size):
        if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_43f88cba:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_5357de0e
        
        if jsGt(startIndex, endIndex):
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_1fab0394
        
    
    def orderedHashCode(c):
        hashCode = 1
        tmp0_iterator = iterator()
        while hasNext():
            e = next()
            tmp = imul(31, hashCode)
            tmp1_safe_receiver = e
            tmp2_elvis_lhs = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_5db9952b
            hashCode = jsBitOr(jsPlus(tmp, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2de0f3e3), 0)
        
        return hashCode
    
    def orderedEquals(c, other):
        if jsNot(jsEqeqeq(_get_size_(), _get_size_())):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_394331a8
        
        otherIterator = iterator()
        tmp0_iterator = iterator()
        while hasNext():
            elem = next()
            elemOther = next()
            if jsNot(equals(elem, elemOther)):
                return False
            
        
        return True
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_606beba4 = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_3c9d64e4
    
    return Companion_instance

class AbstractList:
    def _init_():
        Companion_getInstance()
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_32245b66
    
    def _get_size_():
        pass
    
    def get(index):
        pass
    
    def iterator():
        return _init_(_this_)
    
    def indexOf(element):
        tmp_ret_0
        visitDoWhileLoop_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_162796e1
        return tmp_ret_0
    
    def lastIndexOf(element):
        tmp_ret_0
        visitDoWhileLoop_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_17556c0a
        return tmp_ret_0
    
    def listIterator():
        return _init_(_this_, 0)
    
    def listIterator(index):
        return _init_(_this_, index)
    
    def subList(fromIndex, toIndex):
        return _init_(_this_, fromIndex, toIndex)
    
    def equals(other):
        if jsEqeqeq(other, _this_):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_66e62fc4
        
        if jsNot(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_54dd6160):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_35efd12c
        
        if True:
            pass
        
        return orderedEquals(_this_, kotlin_collections_Collection___(other))
    
    def hashCode():
        return orderedHashCode(_this_)
    
    def contains(element):
        pass
    
    def containsAll(elements):
        pass
    
    def isEmpty():
        pass
    
    def toString():
        pass
    
    def toArray():
        pass
    
    def toArray(array):
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
    def _init_():
        EmptyList_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_755009f2
        _this_.serialVersionUID = _init_(-1478467534, -1720727600)
    
    def equals(other):
        tmp
        if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4591a080:
            tmp = isEmpty()
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def hashCode():
        return 1
    
    def toString():
        return '[]'
    
    def _get_size_():
        return 0
    
    def isEmpty():
        return True
    
    def contains(element):
        return False
    
    def contains(element):
        if jsNot(False):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_69f6b00b
        
        if True:
            pass
        
        tmp
        if False:
            tmp = kotlin_Nothing(element)
        
        if True:
            if True:
                tmp = THROW_CCE()
            
        
        return contains(tmp)
    
    def containsAll(elements):
        return isEmpty()
    
    def containsAll(elements):
        return containsAll(elements)
    
    def get(index):
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_8b1bfdf
    
    def indexOf(element):
        return -1
    
    def indexOf(element):
        if jsNot(False):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_72a14347
        
        if True:
            pass
        
        tmp
        if False:
            tmp = kotlin_Nothing(element)
        
        if True:
            if True:
                tmp = THROW_CCE()
            
        
        return indexOf(tmp)
    
    def lastIndexOf(element):
        return -1
    
    def lastIndexOf(element):
        if jsNot(False):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_365a0910
        
        if True:
            pass
        
        tmp
        if False:
            tmp = kotlin_Nothing(element)
        
        if True:
            if True:
                tmp = THROW_CCE()
            
        
        return lastIndexOf(tmp)
    
    def iterator():
        return EmptyIterator_getInstance()
    
    def listIterator():
        return EmptyIterator_getInstance()
    
    def listIterator(index):
        if jsNot(jsEqeqeq(index, 0)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_48126a17
        
        return EmptyIterator_getInstance()
    
    def subList(fromIndex, toIndex):
        if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_f9233ab:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_7b6b466a
        
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_2123a61c
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_32a2da8c = 0
def EmptyList_getInstance():
    if jsEqeq(EmptyList_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_3f6aaa7
    
    return EmptyList_instance

class EmptyIterator:
    def _init_():
        EmptyIterator_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_7533923b
    
    def hasNext():
        return False
    
    def hasPrevious():
        return False
    
    def nextIndex():
        return 0
    
    def previousIndex():
        return -1
    
    def next():
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_7a13ad55
    
    def previous():
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_5773f83d
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
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
    def iterator():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def _init_():
        pass
    

def contract(builder):
    pass

class ContractBuilder:
    def returns():
        pass
    
    def returns(value):
        pass
    
    def returnsNotNull():
        pass
    
    def callsInPlace(_lambda, kind):
        pass
    
    def callsInPlace_default(_lambda, kind, _mask0, _handler):
        if jsNot(jsEqeqeq(jsBitAnd(_mask0, 2), 0)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_5dcd5046
        
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_56482084
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def _init_():
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
    
    InvocationKind_entriesInitialized = True
    InvocationKind_AT_MOST_ONCE_instance = _init_('AT_MOST_ONCE', 0)
    InvocationKind_AT_LEAST_ONCE_instance = _init_('AT_LEAST_ONCE', 1)
    InvocationKind_EXACTLY_ONCE_instance = _init_('EXACTLY_ONCE', 2)
    InvocationKind_UNKNOWN_instance = _init_('UNKNOWN', 3)

class InvocationKind:
    def _init_(name, ordinal):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_4c864fd0
    
    def _get_name_():
        pass
    
    def _get_ordinal_():
        pass
    
    def compareTo(other):
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class ExperimentalContracts:
    def _init_():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
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
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def _init_():
        pass
    

class Returns:
    def implies(booleanExpression):
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def _init_():
        pass
    

class ReturnsNotNull:
    def implies(booleanExpression):
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def _init_():
        pass
    

class Effect:
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def _init_():
        pass
    

class SimpleEffect:
    def implies(booleanExpression):
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def _init_():
        pass
    

class ConditionalEffect:
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def _init_():
        pass
    

class Continuation:
    def _get_context_():
        pass
    
    def resumeWith(result):
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def _init_():
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
    def _init_(_context, _resumeWith):
        _this_._context = _context
        _this_._resumeWith = _resumeWith
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_30f1487d
    
    def _get_context_():
        return _context
    
    def resumeWith(result):
        return invoke(boxIntrinsic(result))
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class Key:
    def _init_():
        Key_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_623ded82
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_2b0a0c83 = 0
def Key_getInstance():
    if jsEqeq(Key_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_222e8b99
    
    return Key_instance

class ContinuationInterceptor:
    def interceptContinuation(continuation):
        pass
    
    def releaseInterceptedContinuation(continuation):
        pass
    
    def get(key):
        if jsInstanceOf(key, jsClass()):
            tmp
            if isSubKey(_get_key_()):
                tmp = tryCast(_this_)
                tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2858d3d9
            
            if True:
                tmp = None
            
            return tmp
        
        if True:
            pass
        
        tmp
        if jsEqeqeq(Key_getInstance(), key):
            tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_31b07a16
        
        if True:
            tmp = None
        
        return tmp
    
    def minusKey(key):
        if jsInstanceOf(key, jsClass()):
            return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6a67e945
        
        if True:
            pass
        
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_71c9e0a4
    
    def _get_key_():
        pass
    
    def fold(initial, operation):
        pass
    
    def plus(context):
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def _init_():
        Key_getInstance()
    

class Key:
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def _init_():
        pass
    

class Element:
    def _get_key_():
        pass
    
    def get(key):
        tmp
        if equals(_get_key_(), key):
            tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_7beb2da0
        
        if True:
            tmp = None
        
        return tmp
    
    def fold(initial, operation):
        return invoke(initial, _this_)
    
    def minusKey(key):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_7e821499
    
    def plus(context):
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def _init_():
        pass
    

class _no_name_provided_:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_21e860cd
    
    def invoke(acc, element):
        removed = minusKey(_get_key_())
        tmp
        if jsEqeqeq(removed, EmptyCoroutineContext_getInstance()):
            tmp = element
        
        if True:
            interceptor = get(Key_getInstance())
            tmp
            if jsEqeq(interceptor, None):
                tmp = _init_(removed, element)
            
            if True:
                left = minusKey(Key_getInstance())
                tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4eed10a1
            
            tmp = tmp
        
        return tmp
    
    def invoke(p1, p2):
        tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6629ce82
        return invoke(tmp, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_76117cac)
    

class CoroutineContext:
    def get(key):
        pass
    
    def fold(initial, operation):
        pass
    
    def plus(context):
        tmp
        if jsEqeqeq(context, EmptyCoroutineContext_getInstance()):
            tmp = _this_
        
        if True:
            tmp = fold(_this_, _no_name_provided__factory())
        
        return tmp
    
    def minusKey(key):
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def _init_():
        pass
    

def _no_name_provided__factory():
    i = _init_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_5e206acb

def _get_serialVersionUID_(_this):
    return serialVersionUID

def readResolve(_this):
    return EmptyCoroutineContext_getInstance()

class EmptyCoroutineContext:
    def _init_():
        EmptyCoroutineContext_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_6c96346b
        _this_.serialVersionUID = _init_(0, 0)
    
    def get(key):
        return None
    
    def fold(initial, operation):
        return initial
    
    def plus(context):
        return context
    
    def minusKey(key):
        return _this_
    
    def hashCode():
        return 0
    
    def toString():
        return 'EmptyCoroutineContext'
    
    def equals(other):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_7a4154c = 0
def EmptyCoroutineContext_getInstance():
    if jsEqeq(EmptyCoroutineContext_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_aae69d3
    
    return EmptyCoroutineContext_instance

def _get_serialVersionUID_(_this):
    return serialVersionUID

class Companion:
    def _init_():
        Companion_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_69a3944
        _this_.serialVersionUID = _init_(0, 0)
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
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
    def _init_(elements):
        Companion_getInstance()
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_102f3f05
        _this_.elements = elements
    
    def _get_elements_():
        return elements
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class _no_name_provided_:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_2dbc453a
    
    def invoke(acc, element):
        tmp
        if jsEqeqeq(charSequenceLength(acc), 0):
            tmp = toString(element)
        
        if True:
            if True:
                tmp = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_7650e219
            
        
        return tmp
    
    def invoke(p1, p2):
        tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_19a3bfb5
        return invoke(tmp, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_7df7cc64)
    

class _no_name_provided_:
    def _init_(_elements, _index):
        _this_._elements = _elements
        _this_._index = _index
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_3291cfad
    
    def invoke(_anonymous_parameter_0_, element):
        tmp0 = _sharedBox_read(_index)
        _sharedBox_write(_index, jsBitOr(jsPlus(tmp0, 1), 0))
        jsArraySet(_elements, tmp0, element)
    
    def invoke(p1, p2):
        tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_912756d
        invoke(tmp, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3243b967)
        return Unit_getInstance()
    

class CombinedContext:
    def _init_(left, element):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_44aa5585
        _this_.left = left
        _this_.element = element
    
    def get(key):
        cur = _this_
        while True:
            tmp0_safe_receiver = get(key)
            if jsEqeq(tmp0_safe_receiver, None):
                visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstImpl_447630c4
            
            if True:
                visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_7d32399a
            
            Unit_getInstance()
            next = left
            if jsInstanceOf(next, jsClass()):
                cur = kotlin_coroutines_CombinedContext(next)
            
            if True:
                if True:
                    return get(key)
                
            
        
    
    def fold(initial, operation):
        return invoke(fold(initial, operation), element)
    
    def minusKey(key):
        tmp0_safe_receiver = get(key)
        if jsEqeq(tmp0_safe_receiver, None):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstImpl_3c34c491
        
        if True:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_5ef79613
        
        Unit_getInstance()
        newLeft = minusKey(key)
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2fce34e4
    
    def equals(other):
        tmp
        if jsEqeqeq(_this_, other):
            tmp = True
        
        if True:
            tmp
            tmp
            if jsInstanceOf(other, jsClass()):
                tmp = jsEqeqeq(size(kotlin_coroutines_CombinedContext(other)), size(_this_))
            
            if True:
                if True:
                    tmp = False
                
            
            if tmp:
                tmp = containsAll(kotlin_coroutines_CombinedContext(other), _this_)
            
            if True:
                if True:
                    tmp = False
                
            
            tmp = tmp
        
        return tmp
    
    def hashCode():
        return jsBitOr(jsPlus(hashCode(left), hashCode(element)), 0)
    
    def toString():
        return jsPlus(jsPlus('[', fold('', _no_name_provided__factory())), ']')
    
    def plus(context):
        pass
    

def _get_safeCast_(_this):
    return safeCast

def _get_topmostKey_(_this):
    return topmostKey

class AbstractCoroutineContextKey:
    def _init_(baseKey, safeCast):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_1fc386f8
        _this_.safeCast = safeCast
        tmp = _this_
        tmp
        if jsInstanceOf(baseKey, jsClass()):
            tmp = topmostKey
        
        if True:
            if True:
                tmp = baseKey
            
        
        tmp.topmostKey = tmp
    
    def tryCast(element):
        return invoke(element)
    
    def isSubKey(key):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2933669e
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
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
    
    CoroutineSingletons_entriesInitialized = True
    CoroutineSingletons_COROUTINE_SUSPENDED_instance = _init_('COROUTINE_SUSPENDED', 0)
    CoroutineSingletons_UNDECIDED_instance = _init_('UNDECIDED', 1)
    CoroutineSingletons_RESUMED_instance = _init_('RESUMED', 2)

class CoroutineSingletons:
    def _init_(name, ordinal):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_141cb3a4
    
    def _get_name_():
        pass
    
    def _get_ordinal_():
        pass
    
    def compareTo(other):
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
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
    def _init_():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
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
    def _init_(version, message, level, versionKind, errorCode):
        _this_.version = version
        _this_.message = message
        _this_.level = level
        _this_.versionKind = versionKind
        _this_.errorCode = errorCode
    
    def _get_version_():
        return version
    
    def _get_message_():
        return message
    
    def _get_level_():
        return level
    
    def _get_versionKind_():
        return versionKind
    
    def _get_errorCode_():
        return errorCode
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
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
    
    RequireKotlinVersionKind_entriesInitialized = True
    RequireKotlinVersionKind_LANGUAGE_VERSION_instance = _init_('LANGUAGE_VERSION', 0)
    RequireKotlinVersionKind_COMPILER_VERSION_instance = _init_('COMPILER_VERSION', 1)
    RequireKotlinVersionKind_API_VERSION_instance = _init_('API_VERSION', 2)

class RequireKotlinVersionKind:
    def _init_(name, ordinal):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_1ecd979e
    
    def _get_name_():
        pass
    
    def _get_ordinal_():
        pass
    
    def compareTo(other):
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class InlineOnly:
    def _init_():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class NoInfer:
    def _init_():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class DynamicExtension:
    def _init_():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class ContractsDsl:
    def _init_():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class OnlyInputTypes:
    def _init_():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
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
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def _init_():
        pass
    

class KTypeParameter:
    def _get_name_():
        pass
    
    def _get_upperBounds_():
        pass
    
    def _get_variance_():
        pass
    
    def _get_isReified_():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def _init_():
        pass
    

class Companion:
    def _init_():
        Companion_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_1db5de29
        _this_.star = _init_(None, None)
    
    def _get_star_():
        return star
    
    def _get_STAR_():
        return star
    
    def invariant(type):
        return _init_(KVariance_INVARIANT_getInstance(), type)
    
    def contravariant(type):
        return _init_(KVariance_IN_getInstance(), type)
    
    def covariant(type):
        return _init_(KVariance_OUT_getInstance(), type)
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_5a5183ed = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_774ea667
    
    return Companion_instance

class KTypeProjection:
    def _init_(variance, type):
        Companion_getInstance()
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_255d4d7
        _this_.variance = variance
        _this_.type = type
        tmp0_require_0 = jsEqeqeq(jsEqeq(variance, None), jsEqeq(type, None))
        if jsNot(tmp0_require_0):
            message_2 = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_343f54c7
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_2e3e587
        
    
    def _get_variance_():
        return variance
    
    def _get_type_():
        return type
    
    def toString():
        tmp0_subject = variance
        tmp
        if jsEqeq(tmp0_subject, None):
            tmp = '*'
        
        if equals(tmp0_subject, KVariance_INVARIANT_getInstance()):
            tmp = toString()
        
        if equals(tmp0_subject, KVariance_IN_getInstance()):
            tmp = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_42bd5540
        
        if equals(tmp0_subject, KVariance_OUT_getInstance()):
            tmp = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_27a93cfa
        
        if True:
            noWhenBranchMatchedException()
        
        return tmp
    
    def component1():
        return variance
    
    def component2():
        return type
    
    def copy(variance, type):
        return _init_(variance, type)
    
    def copy_default(variance, type, _mask0, _handler):
        if jsNot(jsEqeqeq(jsBitAnd(_mask0, 1), 0)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_60f66b9
        
        if jsNot(jsEqeqeq(jsBitAnd(_mask0, 2), 0)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_24bbe3c6
        
        return copy(variance, type)
    
    def hashCode():
        result = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3cfa429c
        result = jsBitOr(jsPlus(imul(result, 31), visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_60eabf53), 0)
        return result
    
    def equals(other):
        if jsEqeqeq(_this_, other):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_28befd62
        
        if jsNot(jsInstanceOf(other, jsClass())):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_612531a3
        
        if True:
            pass
        
        tmp0_other_with_cast = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_23096e4d
        if jsNot(equals(variance, variance)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_52667676
        
        if jsNot(equals(type, type)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_44d6f9cf
        
        return True
    

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
    
    KVariance_entriesInitialized = True
    KVariance_INVARIANT_instance = _init_('INVARIANT', 0)
    KVariance_IN_instance = _init_('IN', 1)
    KVariance_OUT_instance = _init_('OUT', 2)

class KVariance:
    def _init_(name, ordinal):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_30f6791d
    
    def _get_name_():
        pass
    
    def _get_ordinal_():
        pass
    
    def compareTo(other):
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
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
    def _init_():
        Companion_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_34604b32
    
    def success(value):
        return _init_(value)
    
    def failure(exception):
        return _init_(createFailure(exception))
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_278758da = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_62254d29
    
    return Companion_instance

class Failure:
    def _init_(exception):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_45b2b0ed
        _this_.exception = exception
    
    def _get_exception_():
        return exception
    
    def equals(other):
        tmp
        if jsInstanceOf(other, jsClass()):
            tmp = equals(exception, exception)
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def hashCode():
        return hashCode(exception)
    
    def toString():
        return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_5930e350
    

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
    def _init_(value):
        Companion_getInstance()
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_2fbb098f
        _this_.value = value
    
    def toString():
        return Result__toString_impl(unboxIntrinsic(_this_))
    
    def hashCode():
        return Result__hashCode_impl(unboxIntrinsic(_this_))
    
    def equals(other):
        return Result__equals_impl(unboxIntrinsic(_this_), other)
    

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
    def _init_(message):
        Error_init__Init_(message, _this_)
        captureStack(_this_, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_73536bcc)
    
    def _get_message_():
        pass
    
    def _get_cause_():
        pass
    
    def toString():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
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
    def _init_():
        Companion_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_3f030217
        _this_.MIN_VALUE = _init_(visitConst_other_Byte)
        _this_.MAX_VALUE = _init_(visitConst_other_Byte)
        _this_.SIZE_BYTES = 1
        _this_.SIZE_BITS = 8
    
    def _get_MIN_VALUE_():
        return MIN_VALUE
    
    def _get_MAX_VALUE_():
        return MAX_VALUE
    
    def _get_SIZE_BYTES_():
        return SIZE_BYTES
    
    def _get_SIZE_BITS_():
        return SIZE_BITS
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
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
    def _init_(data):
        Companion_getInstance()
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_5cff6d1d
        _this_.data = data
    
    def compareTo(other):
        return UByte__compareTo_impl(unboxIntrinsic(_this_), other)
    
    def compareTo(other):
        return UByte__compareTo_impl(_this_, other)
    
    def toString():
        return UByte__toString_impl(unboxIntrinsic(_this_))
    
    def hashCode():
        return UByte__hashCode_impl(unboxIntrinsic(_this_))
    
    def equals(other):
        return UByte__equals_impl(unboxIntrinsic(_this_), other)
    

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
    _this.index = _set___

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
    def _init_(array):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_96448ee
        _this_.array = array
        _this_.index = 0
    
    def hasNext():
        return jsLt(index, jsArrayLength(array))
    
    def nextUByte():
        tmp
        if jsLt(index, jsArrayLength(array)):
            tmp0_this = _this_
            tmp1 = index
            tmp0_this.index = jsBitOr(jsPlus(tmp1, 1), 0)
            tmp0_toUByte_0 = jsArrayGet(array, tmp1)
            tmp = _init_(tmp0_toUByte_0)
        
        if True:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_1ee126de
        
        return tmp
    
    def next():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
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
    def _init_(storage):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_2daa5092
        _this_.storage = storage
    
    def _get_size_():
        return _UByteArray___get_size__impl_(unboxIntrinsic(_this_))
    
    def iterator():
        return UByteArray__iterator_impl(unboxIntrinsic(_this_))
    
    def contains(element):
        return UByteArray__contains_impl(unboxIntrinsic(_this_), element)
    
    def contains(element):
        return UByteArray__contains_impl(_this_, element)
    
    def containsAll(elements):
        return UByteArray__containsAll_impl(unboxIntrinsic(_this_), elements)
    
    def containsAll(elements):
        return UByteArray__containsAll_impl(_this_, elements)
    
    def isEmpty():
        return UByteArray__isEmpty_impl(unboxIntrinsic(_this_))
    
    def toString():
        return UByteArray__toString_impl(unboxIntrinsic(_this_))
    
    def hashCode():
        return UByteArray__hashCode_impl(unboxIntrinsic(_this_))
    
    def equals(other):
        return UByteArray__equals_impl(unboxIntrinsic(_this_), other)
    

def _UInt___get_data__impl_(this):
    return data

class Companion:
    def _init_():
        Companion_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_13cc3984
        _this_.MIN_VALUE = _init_(0)
        _this_.MAX_VALUE = _init_(-1)
        _this_.SIZE_BYTES = 4
        _this_.SIZE_BITS = 32
    
    def _get_MIN_VALUE_():
        return MIN_VALUE
    
    def _get_MAX_VALUE_():
        return MAX_VALUE
    
    def _get_SIZE_BYTES_():
        return SIZE_BYTES
    
    def _get_SIZE_BITS_():
        return SIZE_BITS
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
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
    def _init_(data):
        Companion_getInstance()
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_e98adb2
        _this_.data = data
    
    def compareTo(other):
        return UInt__compareTo_impl(unboxIntrinsic(_this_), other)
    
    def compareTo(other):
        return UInt__compareTo_impl(_this_, other)
    
    def toString():
        return UInt__toString_impl(unboxIntrinsic(_this_))
    
    def hashCode():
        return UInt__hashCode_impl(unboxIntrinsic(_this_))
    
    def equals(other):
        return UInt__equals_impl(unboxIntrinsic(_this_), other)
    

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
    _this.index = _set___

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
    def _init_(array):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_7b6b8cea
        _this_.array = array
        _this_.index = 0
    
    def hasNext():
        return jsLt(index, jsArrayLength(array))
    
    def nextUInt():
        tmp
        if jsLt(index, jsArrayLength(array)):
            tmp0_this = _this_
            tmp1 = index
            tmp0_this.index = jsBitOr(jsPlus(tmp1, 1), 0)
            tmp0_toUInt_0 = jsArrayGet(array, tmp1)
            tmp = _init_(tmp0_toUInt_0)
        
        if True:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_402fdef1
        
        return tmp
    
    def next():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
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
    def _init_(storage):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_1cdb280b
        _this_.storage = storage
    
    def _get_size_():
        return _UIntArray___get_size__impl_(unboxIntrinsic(_this_))
    
    def iterator():
        return UIntArray__iterator_impl(unboxIntrinsic(_this_))
    
    def contains(element):
        return UIntArray__contains_impl(unboxIntrinsic(_this_), element)
    
    def contains(element):
        return UIntArray__contains_impl(_this_, element)
    
    def containsAll(elements):
        return UIntArray__containsAll_impl(unboxIntrinsic(_this_), elements)
    
    def containsAll(elements):
        return UIntArray__containsAll_impl(_this_, elements)
    
    def isEmpty():
        return UIntArray__isEmpty_impl(unboxIntrinsic(_this_))
    
    def toString():
        return UIntArray__toString_impl(unboxIntrinsic(_this_))
    
    def hashCode():
        return UIntArray__hashCode_impl(unboxIntrinsic(_this_))
    
    def equals(other):
        return UIntArray__equals_impl(unboxIntrinsic(_this_), other)
    

class Companion:
    def _init_():
        Companion_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_41041c31
        _this_.EMPTY = _init_(_init_(-1), _init_(0))
    
    def _get_EMPTY_():
        return EMPTY
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_4c8a893e = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_34d27e12
    
    return Companion_instance

class UIntRange:
    def _init_(start, endInclusive):
        Companion_getInstance()
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_21f9a305
    
    def _get_start_():
        return _get_first_()
    
    def _get_start_():
        return boxIntrinsic(_get_start_())
    
    def _get_endInclusive_():
        return _get_last_()
    
    def _get_endInclusive_():
        return boxIntrinsic(_get_endInclusive_())
    
    def contains(value):
        tmp
        tmp0_compareTo_0 = _get_first_()
        if jsLtEq(uintCompare(_UInt___get_data__impl_(tmp0_compareTo_0), _UInt___get_data__impl_(value)), 0):
            tmp1_compareTo_0 = _get_last_()
            tmp = jsLtEq(uintCompare(_UInt___get_data__impl_(value), _UInt___get_data__impl_(tmp1_compareTo_0)), 0)
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def contains(value):
        return contains(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_1c0b38af)
    
    def isEmpty():
        tmp0_compareTo_0 = _get_first_()
        tmp1_compareTo_0 = _get_last_()
        return jsGt(uintCompare(_UInt___get_data__impl_(tmp0_compareTo_0), _UInt___get_data__impl_(tmp1_compareTo_0)), 0)
    
    def equals(other):
        tmp
        if jsInstanceOf(other, jsClass()):
            tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_b6aa7e9
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def hashCode():
        tmp
        if isEmpty():
            tmp = -1
        
        if True:
            tmp0_toInt_0 = _get_first_()
            tmp = imul(31, _UInt___get_data__impl_(tmp0_toInt_0))
            tmp1_toInt_0 = _get_last_()
            tmp = jsBitOr(jsPlus(tmp, _UInt___get_data__impl_(tmp1_toInt_0)), 0)
        
        return tmp
    
    def toString():
        return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_46441754
    
    def _get_first_():
        pass
    
    def _get_last_():
        pass
    
    def _get_step_():
        pass
    
    def iterator():
        pass
    

class Companion:
    def _init_():
        Companion_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_5d50e7f6
    
    def fromClosedRange(rangeStart, rangeEnd, step):
        return _init_(rangeStart, rangeEnd, step)
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_5a12819f = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_82300e1
    
    return Companion_instance

class UIntProgression:
    def _init_(start, endInclusive, step):
        Companion_getInstance()
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_93c66ef
        if jsEqeqeq(step, 0):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_736e4a59
        
        if jsEqeqeq(step, MIN_VALUE):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_3369fe5c
        
        _this_.first = start
        _this_.last = getProgressionLastElement(start, endInclusive, step)
        _this_.step = step
    
    def _get_first_():
        return first
    
    def _get_last_():
        return last
    
    def _get_step_():
        return step
    
    def iterator():
        return _init_(first, last, step)
    
    def isEmpty():
        tmp
        if jsGt(step, 0):
            tmp0_compareTo_0 = first
            tmp1_compareTo_0 = last
            tmp = jsGt(uintCompare(_UInt___get_data__impl_(tmp0_compareTo_0), _UInt___get_data__impl_(tmp1_compareTo_0)), 0)
        
        if True:
            tmp2_compareTo_0 = first
            tmp3_compareTo_0 = last
            tmp = jsLt(uintCompare(_UInt___get_data__impl_(tmp2_compareTo_0), _UInt___get_data__impl_(tmp3_compareTo_0)), 0)
        
        return tmp
    
    def equals(other):
        tmp
        if jsInstanceOf(other, jsClass()):
            tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_d1ccec8
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def hashCode():
        tmp
        if isEmpty():
            tmp = -1
        
        if True:
            tmp0_toInt_0 = first
            tmp = imul(31, _UInt___get_data__impl_(tmp0_toInt_0))
            tmp1_toInt_0 = last
            tmp = jsBitOr(jsPlus(imul(31, jsBitOr(jsPlus(tmp, _UInt___get_data__impl_(tmp1_toInt_0)), 0)), kotlin_Int(step)), 0)
        
        return tmp
    
    def toString():
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_7963767d
    

def _get_finalElement_(_this):
    return finalElement

def _set_hasNext_(_this, _set___):
    _this.hasNext = _set___

def _get_hasNext_(_this):
    return hasNext

def _get_step_(_this):
    return step

def _set_next_(_this, _set___):
    _this.next = _set___

def _get_next_(_this):
    return next

class UIntProgressionIterator:
    def _init_(first, last, step):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_3054cdd3
        _this_.finalElement = last
        tmp = _this_
        tmp
        if jsGt(step, 0):
            tmp = jsLtEq(uintCompare(_UInt___get_data__impl_(first), _UInt___get_data__impl_(last)), 0)
        
        if True:
            tmp = jsGtEq(uintCompare(_UInt___get_data__impl_(first), _UInt___get_data__impl_(last)), 0)
        
        tmp.hasNext = tmp
        tmp = _this_
        tmp.step = _init_(step)
        _this_.next = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_675b0850
    
    def hasNext():
        return hasNext
    
    def nextUInt():
        value = next
        if equals(boxIntrinsic(value), boxIntrinsic(finalElement)):
            if jsNot(hasNext):
                visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_4ae435a3
            
            _this_.hasNext = False
        
        if True:
            tmp0_this = _this_
            tmp = tmp0_this
            tmp0_plus_0 = next
            tmp1_plus_0 = step
            tmp.next = _init_(jsBitOr(jsPlus(_UInt___get_data__impl_(tmp0_plus_0), _UInt___get_data__impl_(tmp1_plus_0)), 0))
        
        return value
    
    def next():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class UIntIterator:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_31c31fa6
    
    def next():
        return nextUInt()
    
    def next():
        return boxIntrinsic(next())
    
    def nextUInt():
        pass
    
    def hasNext():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class ULongIterator:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_39d37da8
    
    def next():
        return nextULong()
    
    def next():
        return boxIntrinsic(next())
    
    def nextULong():
        pass
    
    def hasNext():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class UByteIterator:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_62966c9f
    
    def next():
        return nextUByte()
    
    def next():
        return boxIntrinsic(next())
    
    def nextUByte():
        pass
    
    def hasNext():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class UShortIterator:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_62536882
    
    def next():
        return nextUShort()
    
    def next():
        return boxIntrinsic(next())
    
    def nextUShort():
        pass
    
    def hasNext():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

def _ULong___get_data__impl_(this):
    return data

class Companion:
    def _init_():
        Companion_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_2f83467
        _this_.MIN_VALUE = _init_(_init_(0, 0))
        _this_.MAX_VALUE = _init_(_init_(-1, -1))
        _this_.SIZE_BYTES = 8
        _this_.SIZE_BITS = 64
    
    def _get_MIN_VALUE_():
        return MIN_VALUE
    
    def _get_MAX_VALUE_():
        return MAX_VALUE
    
    def _get_SIZE_BYTES_():
        return SIZE_BYTES
    
    def _get_SIZE_BITS_():
        return SIZE_BITS
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
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
    def _init_(data):
        Companion_getInstance()
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_785477e5
        _this_.data = data
    
    def compareTo(other):
        return ULong__compareTo_impl(unboxIntrinsic(_this_), other)
    
    def compareTo(other):
        return ULong__compareTo_impl(_this_, other)
    
    def toString():
        return ULong__toString_impl(unboxIntrinsic(_this_))
    
    def hashCode():
        return ULong__hashCode_impl(unboxIntrinsic(_this_))
    
    def equals(other):
        return ULong__equals_impl(unboxIntrinsic(_this_), other)
    

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
    _this.index = _set___

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
    def _init_(array):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_35a81281
        _this_.array = array
        _this_.index = 0
    
    def hasNext():
        return jsLt(index, jsArrayLength(array))
    
    def nextULong():
        tmp
        if jsLt(index, jsArrayLength(array)):
            tmp0_this = _this_
            tmp1 = index
            tmp0_this.index = jsBitOr(jsPlus(tmp1, 1), 0)
            tmp0_toULong_0 = jsArrayGet(array, tmp1)
            tmp = _init_(tmp0_toULong_0)
        
        if True:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_35bb3fea
        
        return tmp
    
    def next():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
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
    def _init_(storage):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_171b0d3
        _this_.storage = storage
    
    def _get_size_():
        return _ULongArray___get_size__impl_(unboxIntrinsic(_this_))
    
    def iterator():
        return ULongArray__iterator_impl(unboxIntrinsic(_this_))
    
    def contains(element):
        return ULongArray__contains_impl(unboxIntrinsic(_this_), element)
    
    def contains(element):
        return ULongArray__contains_impl(_this_, element)
    
    def containsAll(elements):
        return ULongArray__containsAll_impl(unboxIntrinsic(_this_), elements)
    
    def containsAll(elements):
        return ULongArray__containsAll_impl(_this_, elements)
    
    def isEmpty():
        return ULongArray__isEmpty_impl(unboxIntrinsic(_this_))
    
    def toString():
        return ULongArray__toString_impl(unboxIntrinsic(_this_))
    
    def hashCode():
        return ULongArray__hashCode_impl(unboxIntrinsic(_this_))
    
    def equals(other):
        return ULongArray__equals_impl(unboxIntrinsic(_this_), other)
    

class Companion:
    def _init_():
        Companion_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_2086f336
        _this_.EMPTY = _init_(_init_(_init_(-1, -1)), _init_(_init_(0, 0)))
    
    def _get_EMPTY_():
        return EMPTY
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_5914bf5f = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_514111ca
    
    return Companion_instance

class ULongRange:
    def _init_(start, endInclusive):
        Companion_getInstance()
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_6202f8bf
    
    def _get_start_():
        return _get_first_()
    
    def _get_start_():
        return boxIntrinsic(_get_start_())
    
    def _get_endInclusive_():
        return _get_last_()
    
    def _get_endInclusive_():
        return boxIntrinsic(_get_endInclusive_())
    
    def contains(value):
        tmp
        tmp0_compareTo_0 = _get_first_()
        if jsLtEq(ulongCompare(_ULong___get_data__impl_(tmp0_compareTo_0), _ULong___get_data__impl_(value)), 0):
            tmp1_compareTo_0 = _get_last_()
            tmp = jsLtEq(ulongCompare(_ULong___get_data__impl_(value), _ULong___get_data__impl_(tmp1_compareTo_0)), 0)
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def contains(value):
        return contains(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6c3dae0f)
    
    def isEmpty():
        tmp0_compareTo_0 = _get_first_()
        tmp1_compareTo_0 = _get_last_()
        return jsGt(ulongCompare(_ULong___get_data__impl_(tmp0_compareTo_0), _ULong___get_data__impl_(tmp1_compareTo_0)), 0)
    
    def equals(other):
        tmp
        if jsInstanceOf(other, jsClass()):
            tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_54fb9fef
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def hashCode():
        tmp
        if isEmpty():
            tmp = -1
        
        if True:
            tmp2_xor_0 = _get_first_()
            tmp0_shr_0 = _get_first_()
            tmp1_shr_0 = 32
            tmp3_xor_0 = _init_(ushr(tmp1_shr_0))
            tmp4_toInt_0 = _init_(xor(_ULong___get_data__impl_(tmp3_xor_0)))
            tmp = imul(31, toInt())
            tmp7_xor_0 = _get_last_()
            tmp5_shr_0 = _get_last_()
            tmp6_shr_0 = 32
            tmp8_xor_0 = _init_(ushr(tmp6_shr_0))
            tmp9_toInt_0 = _init_(xor(_ULong___get_data__impl_(tmp8_xor_0)))
            tmp = jsBitOr(jsPlus(tmp, toInt()), 0)
        
        return tmp
    
    def toString():
        return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_387051e3
    
    def _get_first_():
        pass
    
    def _get_last_():
        pass
    
    def _get_step_():
        pass
    
    def iterator():
        pass
    

class Companion:
    def _init_():
        Companion_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_7dd92a36
    
    def fromClosedRange(rangeStart, rangeEnd, step):
        return _init_(rangeStart, rangeEnd, step)
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_337348de = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_edc900a
    
    return Companion_instance

class ULongProgression:
    def _init_(start, endInclusive, step):
        Companion_getInstance()
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_4b718c45
        if equals(_init_(0, 0)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_41277db
        
        if equals(_init_(0, -2147483648)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_402b10af
        
        _this_.first = start
        _this_.last = getProgressionLastElement(start, endInclusive, step)
        _this_.step = step
    
    def _get_first_():
        return first
    
    def _get_last_():
        return last
    
    def _get_step_():
        return step
    
    def iterator():
        return _init_(first, last, step)
    
    def isEmpty():
        tmp
        if jsGt(compareTo(_init_(0, 0)), 0):
            tmp0_compareTo_0 = first
            tmp1_compareTo_0 = last
            tmp = jsGt(ulongCompare(_ULong___get_data__impl_(tmp0_compareTo_0), _ULong___get_data__impl_(tmp1_compareTo_0)), 0)
        
        if True:
            tmp2_compareTo_0 = first
            tmp3_compareTo_0 = last
            tmp = jsLt(ulongCompare(_ULong___get_data__impl_(tmp2_compareTo_0), _ULong___get_data__impl_(tmp3_compareTo_0)), 0)
        
        return tmp
    
    def equals(other):
        tmp
        if jsInstanceOf(other, jsClass()):
            tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_41a3a2fd
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def hashCode():
        tmp
        if isEmpty():
            tmp = -1
        
        if True:
            tmp2_xor_0 = first
            tmp0_shr_0 = first
            tmp1_shr_0 = 32
            tmp3_xor_0 = _init_(ushr(tmp1_shr_0))
            tmp4_toInt_0 = _init_(xor(_ULong___get_data__impl_(tmp3_xor_0)))
            tmp = imul(31, toInt())
            tmp7_xor_0 = last
            tmp5_shr_0 = last
            tmp6_shr_0 = 32
            tmp8_xor_0 = _init_(ushr(tmp6_shr_0))
            tmp9_toInt_0 = _init_(xor(_ULong___get_data__impl_(tmp8_xor_0)))
            tmp = jsBitOr(jsPlus(imul(31, jsBitOr(jsPlus(tmp, toInt()), 0)), toInt()), 0)
        
        return tmp
    
    def toString():
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_20325baf
    

def _get_finalElement_(_this):
    return finalElement

def _set_hasNext_(_this, _set___):
    _this.hasNext = _set___

def _get_hasNext_(_this):
    return hasNext

def _get_step_(_this):
    return step

def _set_next_(_this, _set___):
    _this.next = _set___

def _get_next_(_this):
    return next

class ULongProgressionIterator:
    def _init_(first, last, step):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_66487713
        _this_.finalElement = last
        tmp = _this_
        tmp
        if jsGt(compareTo(_init_(0, 0)), 0):
            tmp = jsLtEq(ulongCompare(_ULong___get_data__impl_(first), _ULong___get_data__impl_(last)), 0)
        
        if True:
            tmp = jsGtEq(ulongCompare(_ULong___get_data__impl_(first), _ULong___get_data__impl_(last)), 0)
        
        tmp.hasNext = tmp
        tmp = _this_
        tmp.step = _init_(step)
        _this_.next = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_574c8a2a
    
    def hasNext():
        return hasNext
    
    def nextULong():
        value = next
        if equals(boxIntrinsic(value), boxIntrinsic(finalElement)):
            if jsNot(hasNext):
                visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_752e50c6
            
            _this_.hasNext = False
        
        if True:
            tmp0_this = _this_
            tmp = tmp0_this
            tmp0_plus_0 = next
            tmp1_plus_0 = step
            tmp.next = _init_(plus(_ULong___get_data__impl_(tmp1_plus_0)))
        
        return value
    
    def next():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
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
    def _init_():
        Companion_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_1300112e
        _this_.MIN_VALUE = _init_(visitConst_other_Short)
        _this_.MAX_VALUE = _init_(visitConst_other_Short)
        _this_.SIZE_BYTES = 2
        _this_.SIZE_BITS = 16
    
    def _get_MIN_VALUE_():
        return MIN_VALUE
    
    def _get_MAX_VALUE_():
        return MAX_VALUE
    
    def _get_SIZE_BYTES_():
        return SIZE_BYTES
    
    def _get_SIZE_BITS_():
        return SIZE_BITS
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
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
    def _init_(data):
        Companion_getInstance()
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_c2ddfeb
        _this_.data = data
    
    def compareTo(other):
        return UShort__compareTo_impl(unboxIntrinsic(_this_), other)
    
    def compareTo(other):
        return UShort__compareTo_impl(_this_, other)
    
    def toString():
        return UShort__toString_impl(unboxIntrinsic(_this_))
    
    def hashCode():
        return UShort__hashCode_impl(unboxIntrinsic(_this_))
    
    def equals(other):
        return UShort__equals_impl(unboxIntrinsic(_this_), other)
    

def toUShort():
    return _init_(toShort(_this_))

def toUShort():
    return _init_(toShort())

def toUShort():
    return _init_(_this_)

def _get_array_(_this):
    return array

def _set_index_(_this, _set___):
    _this.index = _set___

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
    def _init_(array):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_6a35cccf
        _this_.array = array
        _this_.index = 0
    
    def hasNext():
        return jsLt(index, jsArrayLength(array))
    
    def nextUShort():
        tmp
        if jsLt(index, jsArrayLength(array)):
            tmp0_this = _this_
            tmp1 = index
            tmp0_this.index = jsBitOr(jsPlus(tmp1, 1), 0)
            tmp0_toUShort_0 = jsArrayGet(array, tmp1)
            tmp = _init_(tmp0_toUShort_0)
        
        if True:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_1ec96512
        
        return tmp
    
    def next():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
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
    def _init_(storage):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_e763080
        _this_.storage = storage
    
    def _get_size_():
        return _UShortArray___get_size__impl_(unboxIntrinsic(_this_))
    
    def iterator():
        return UShortArray__iterator_impl(unboxIntrinsic(_this_))
    
    def contains(element):
        return UShortArray__contains_impl(unboxIntrinsic(_this_), element)
    
    def contains(element):
        return UShortArray__contains_impl(_this_, element)
    
    def containsAll(elements):
        return UShortArray__containsAll_impl(unboxIntrinsic(_this_), elements)
    
    def containsAll(elements):
        return UShortArray__containsAll_impl(_this_, elements)
    
    def isEmpty():
        return UShortArray__isEmpty_impl(unboxIntrinsic(_this_))
    
    def toString():
        return UShortArray__toString_impl(unboxIntrinsic(_this_))
    
    def hashCode():
        return UShortArray__hashCode_impl(unboxIntrinsic(_this_))
    
    def equals(other):
        return UShortArray__equals_impl(unboxIntrinsic(_this_), other)
    

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
    def _init_():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class Annotation:
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def _init_():
        pass
    

class CharSequence:
    def _get_length_():
        pass
    
    def get(index):
        pass
    
    def subSequence(startIndex, endIndex):
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def _init_():
        pass
    

class Comparable:
    def compareTo(other):
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def _init_():
        pass
    

class Iterator:
    def next():
        pass
    
    def hasNext():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def _init_():
        pass
    

class ListIterator:
    def next():
        pass
    
    def hasNext():
        pass
    
    def hasPrevious():
        pass
    
    def previous():
        pass
    
    def nextIndex():
        pass
    
    def previousIndex():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def _init_():
        pass
    

class MutableIterator:
    def remove():
        pass
    
    def next():
        pass
    
    def hasNext():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def _init_():
        pass
    

class MutableListIterator:
    def next():
        pass
    
    def hasNext():
        pass
    
    def remove():
        pass
    
    def set(element):
        pass
    
    def add(element):
        pass
    
    def hasPrevious():
        pass
    
    def previous():
        pass
    
    def nextIndex():
        pass
    
    def previousIndex():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def _init_():
        pass
    

class Number:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_67e12e28
    
    def toDouble():
        pass
    
    def toFloat():
        pass
    
    def toLong():
        pass
    
    def toInt():
        pass
    
    def toChar():
        pass
    
    def toShort():
        pass
    
    def toByte():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class SinceKotlin:
    def _init_(version):
        _this_.version = version
    
    def _get_version_():
        return version
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class Suppress:
    def _init_(names):
        _this_.names = names
    
    def _get_names_():
        return names
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
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
    
    DeprecationLevel_entriesInitialized = True
    DeprecationLevel_WARNING_instance = _init_('WARNING', 0)
    DeprecationLevel_ERROR_instance = _init_('ERROR', 1)
    DeprecationLevel_HIDDEN_instance = _init_('HIDDEN', 2)

class DeprecationLevel:
    def _init_(name, ordinal):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_1f98b6aa
    
    def _get_name_():
        pass
    
    def _get_ordinal_():
        pass
    
    def compareTo(other):
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class PublishedApi:
    def _init_():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class ParameterName:
    def _init_(name):
        _this_.name = name
    
    def _get_name_():
        return name
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
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
    def _init_(message, replaceWith, level):
        _this_.message = message
        _this_.replaceWith = replaceWith
        _this_.level = level
    
    def _get_message_():
        return message
    
    def _get_replaceWith_():
        return replaceWith
    
    def _get_level_():
        return level
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class ReplaceWith:
    def _init_(expression, imports):
        _this_.expression = expression
        _this_.imports = imports
    
    def _get_expression_():
        return expression
    
    def _get_imports_():
        return imports
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class ExtensionFunctionType:
    def _init_():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class UnsafeVariance:
    def _init_():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
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
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_10ecf244
    
    def next():
        return nextByte()
    
    def nextByte():
        pass
    
    def hasNext():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class IntIterator:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_7510824
    
    def next():
        return nextInt()
    
    def nextInt():
        pass
    
    def hasNext():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class DoubleIterator:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_23c0fcf0
    
    def next():
        return nextDouble()
    
    def nextDouble():
        pass
    
    def hasNext():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class FloatIterator:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_1cafb30
    
    def next():
        return nextFloat()
    
    def nextFloat():
        pass
    
    def hasNext():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class LongIterator:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_48e859f7
    
    def next():
        return nextLong()
    
    def nextLong():
        pass
    
    def hasNext():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class CharIterator:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_5f113867
    
    def next():
        return nextChar()
    
    def nextChar():
        pass
    
    def hasNext():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class BooleanIterator:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_39aaa7db
    
    def next():
        return nextBoolean()
    
    def nextBoolean():
        pass
    
    def hasNext():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class ShortIterator:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_4848681d
    
    def next():
        return nextShort()
    
    def nextShort():
        pass
    
    def hasNext():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

def _get_finalElement_(_this):
    return finalElement

def _set_hasNext_(_this, _set___):
    _this.hasNext = _set___

def _get_hasNext_(_this):
    return hasNext

def _set_next_(_this, _set___):
    _this.next = _set___

def _get_next_(_this):
    return next

class IntProgressionIterator:
    def _init_(first, last, step):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_5817b0d1
        _this_.step = step
        _this_.finalElement = last
        _this_.hasNext = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_1eb45da0
        _this_.next = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6e0c20b8
    
    def _get_step_():
        return step
    
    def hasNext():
        return hasNext
    
    def nextInt():
        value = next
        if jsEqeqeq(value, finalElement):
            if jsNot(hasNext):
                visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_2d10160a
            
            _this_.hasNext = False
        
        if True:
            tmp0_this = _this_
            tmp0_this.next = jsBitOr(jsPlus(next, step), 0)
        
        return value
    
    def next():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

def _get_finalElement_(_this):
    return finalElement

def _set_hasNext_(_this, _set___):
    _this.hasNext = _set___

def _get_hasNext_(_this):
    return hasNext

def _set_next_(_this, _set___):
    _this.next = _set___

def _get_next_(_this):
    return next

class LongProgressionIterator:
    def _init_(first, last, step):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_1ae8556c
        _this_.step = step
        _this_.finalElement = last
        _this_.hasNext = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_7445d24
        _this_.next = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_571aeb15
    
    def _get_step_():
        return step
    
    def hasNext():
        return hasNext
    
    def nextLong():
        value = next
        if equals(finalElement):
            if jsNot(hasNext):
                visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_4d6fa22c
            
            _this_.hasNext = False
        
        if True:
            tmp0_this = _this_
            tmp0_this.next = plus(step)
        
        return value
    
    def next():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

def _get_finalElement_(_this):
    return finalElement

def _set_hasNext_(_this, _set___):
    _this.hasNext = _set___

def _get_hasNext_(_this):
    return hasNext

def _set_next_(_this, _set___):
    _this.next = _set___

def _get_next_(_this):
    return next

class CharProgressionIterator:
    def _init_(first, last, step):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_31e5d408
        _this_.step = step
        _this_.finalElement = toInt()
        _this_.hasNext = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6b1a2c9f
        _this_.next = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_18121865
    
    def _get_step_():
        return step
    
    def hasNext():
        return hasNext
    
    def nextChar():
        value = next
        if jsEqeqeq(value, finalElement):
            if jsNot(hasNext):
                visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_35e0d91e
            
            _this_.hasNext = False
        
        if True:
            tmp0_this = _this_
            tmp0_this.next = jsBitOr(jsPlus(next, step), 0)
        
        return numberToChar(value)
    
    def next():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class Companion:
    def _init_():
        Companion_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_1cc5d8a9
    
    def fromClosedRange(rangeStart, rangeEnd, step):
        return _init_(rangeStart, rangeEnd, step)
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_676f8fab = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_1f22ac9b
    
    return Companion_instance

class IntProgression:
    def _init_(start, endInclusive, step):
        Companion_getInstance()
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_5cb654e3
        if jsEqeqeq(step, 0):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_71b0d2ec
        
        if jsEqeqeq(step, MIN_VALUE):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_2372ada3
        
        _this_.first = start
        _this_.last = kotlin_Int(getProgressionLastElement(kotlin_Int(start), kotlin_Int(endInclusive), step))
        _this_.step = step
    
    def _get_first_():
        return first
    
    def _get_last_():
        return last
    
    def _get_step_():
        return step
    
    def iterator():
        return _init_(first, last, step)
    
    def isEmpty():
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2393b885
    
    def equals(other):
        tmp
        if jsInstanceOf(other, jsClass()):
            tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_264cef82
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def hashCode():
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6c7c8480
    
    def toString():
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_31222be0
    

class Companion:
    def _init_():
        Companion_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_7c1e5d14
    
    def fromClosedRange(rangeStart, rangeEnd, step):
        return _init_(rangeStart, rangeEnd, step)
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_e39a6c2 = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_610f8dd8
    
    return Companion_instance

class LongProgression:
    def _init_(start, endInclusive, step):
        Companion_getInstance()
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_7cd6b76a
        if equals(_init_(0, 0)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_2fe328b9
        
        if equals(_init_(0, -2147483648)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_58620d12
        
        _this_.first = start
        _this_.last = toLong()
        _this_.step = step
    
    def _get_first_():
        return first
    
    def _get_last_():
        return last
    
    def _get_step_():
        return step
    
    def iterator():
        return _init_(first, last, step)
    
    def isEmpty():
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_51dfb693
    
    def equals(other):
        tmp
        if jsInstanceOf(other, jsClass()):
            tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4dafab49
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def hashCode():
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_79bc0ceb
    
    def toString():
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_47fe4f78
    

class Companion:
    def _init_():
        Companion_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_64dc0a5f
    
    def fromClosedRange(rangeStart, rangeEnd, step):
        return _init_(rangeStart, rangeEnd, step)
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_c1f6a16 = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_3a9b4a6e
    
    return Companion_instance

class CharProgression:
    def _init_(start, endInclusive, step):
        Companion_getInstance()
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_7ee0dbd1
        if jsEqeqeq(step, 0):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_6707fc3e
        
        if jsEqeqeq(step, MIN_VALUE):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_347bc2ad
        
        _this_.first = start
        _this_.last = numberToChar(getProgressionLastElement(toInt(), toInt(), step))
        _this_.step = step
    
    def _get_first_():
        return first
    
    def _get_last_():
        return last
    
    def _get_step_():
        return step
    
    def iterator():
        return _init_(first, last, step)
    
    def isEmpty():
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_579ffb7e
    
    def equals(other):
        tmp
        if jsInstanceOf(other, jsClass()):
            tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6e96ff9a
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def hashCode():
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_b6ae271
    
    def toString():
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4845abe5
    

class ClosedRange:
    def _get_start_():
        pass
    
    def _get_endInclusive_():
        pass
    
    def contains(value):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_e9c78b3
    
    def isEmpty():
        return jsGt(compareTo(_get_start_(), _get_endInclusive_()), 0)
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def _init_():
        pass
    

class Companion:
    def _init_():
        Companion_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_5f0c45ae
        _this_.EMPTY = _init_(1, 0)
    
    def _get_EMPTY_():
        return EMPTY
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_309c821d = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_2d06acfd
    
    return Companion_instance

class IntRange:
    def _init_(start, endInclusive):
        Companion_getInstance()
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_294aaa6
    
    def _get_start_():
        return _get_first_()
    
    def _get_endInclusive_():
        return _get_last_()
    
    def contains(value):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_198d9e3b
    
    def contains(value):
        return contains(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_300eabce)
    
    def isEmpty():
        return jsGt(_get_first_(), _get_last_())
    
    def equals(other):
        tmp
        if jsInstanceOf(other, jsClass()):
            tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2c6dab96
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def hashCode():
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_535203b8
    
    def toString():
        return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_1a8b3791
    
    def _get_first_():
        pass
    
    def _get_last_():
        pass
    
    def _get_step_():
        pass
    
    def iterator():
        pass
    

class Companion:
    def _init_():
        Companion_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_63bdf82d
        _this_.EMPTY = _init_(_init_(1, 0), _init_(0, 0))
    
    def _get_EMPTY_():
        return EMPTY
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_79871eeb = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_4260a1c
    
    return Companion_instance

class LongRange:
    def _init_(start, endInclusive):
        Companion_getInstance()
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_29a51ff1
    
    def _get_start_():
        return _get_first_()
    
    def _get_endInclusive_():
        return _get_last_()
    
    def contains(value):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4d087555
    
    def contains(value):
        return contains(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_532ad0fd)
    
    def isEmpty():
        return jsGt(compareTo(_get_last_()), 0)
    
    def equals(other):
        tmp
        if jsInstanceOf(other, jsClass()):
            tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_1f78d2a7
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def hashCode():
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_31f5f65a
    
    def toString():
        return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_156eb310
    
    def _get_first_():
        pass
    
    def _get_last_():
        pass
    
    def _get_step_():
        pass
    
    def iterator():
        pass
    

class Companion:
    def _init_():
        Companion_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_5afbbf9b
        _this_.EMPTY = _init_(_init_(1), _init_(0))
    
    def _get_EMPTY_():
        return EMPTY
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_6e094fb7 = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_5dfabe82
    
    return Companion_instance

class CharRange:
    def _init_(start, endInclusive):
        Companion_getInstance()
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_4ff5711b
    
    def _get_start_():
        return _get_first_()
    
    def _get_endInclusive_():
        return _get_last_()
    
    def contains(value):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_1d7ca8b0
    
    def contains(value):
        return contains(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_73b6167d)
    
    def isEmpty():
        return jsGt(compareTo(_get_last_()), 0)
    
    def equals(other):
        tmp
        if jsInstanceOf(other, jsClass()):
            tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3c521d01
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def hashCode():
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_be74f53
    
    def toString():
        return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_5eca6e7d
    
    def _get_first_():
        pass
    
    def _get_last_():
        pass
    
    def _get_step_():
        pass
    
    def iterator():
        pass
    

class Unit:
    def _init_():
        Unit_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_16817bad
    
    def toString():
        return 'kotlin.Unit'
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_2c1ce593 = 0
def Unit_getInstance():
    if jsEqeq(Unit_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_3a0d3af1
    
    return Unit_instance

class Target:
    def _init_(allowedTargets):
        _this_.allowedTargets = allowedTargets
    
    def _get_allowedTargets_():
        return allowedTargets
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
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
    
    AnnotationTarget_entriesInitialized = True
    AnnotationTarget_CLASS_instance = _init_('CLASS', 0)
    AnnotationTarget_ANNOTATION_CLASS_instance = _init_('ANNOTATION_CLASS', 1)
    AnnotationTarget_TYPE_PARAMETER_instance = _init_('TYPE_PARAMETER', 2)
    AnnotationTarget_PROPERTY_instance = _init_('PROPERTY', 3)
    AnnotationTarget_FIELD_instance = _init_('FIELD', 4)
    AnnotationTarget_LOCAL_VARIABLE_instance = _init_('LOCAL_VARIABLE', 5)
    AnnotationTarget_VALUE_PARAMETER_instance = _init_('VALUE_PARAMETER', 6)
    AnnotationTarget_CONSTRUCTOR_instance = _init_('CONSTRUCTOR', 7)
    AnnotationTarget_FUNCTION_instance = _init_('FUNCTION', 8)
    AnnotationTarget_PROPERTY_GETTER_instance = _init_('PROPERTY_GETTER', 9)
    AnnotationTarget_PROPERTY_SETTER_instance = _init_('PROPERTY_SETTER', 10)
    AnnotationTarget_TYPE_instance = _init_('TYPE', 11)
    AnnotationTarget_EXPRESSION_instance = _init_('EXPRESSION', 12)
    AnnotationTarget_FILE_instance = _init_('FILE', 13)
    AnnotationTarget_TYPEALIAS_instance = _init_('TYPEALIAS', 14)

class AnnotationTarget:
    def _init_(name, ordinal):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_1c43b31d
    
    def _get_name_():
        pass
    
    def _get_ordinal_():
        pass
    
    def compareTo(other):
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class MustBeDocumented:
    def _init_():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

def Retention_init__Init_(value, _mask0, _marker, _this):
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 1), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_7a140446
    
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_68fa9450
    return _this

def Retention_init__Create_(value, _mask0, _marker):
    return Retention_init__Init_(value, _mask0, _marker, Object_create())

class Retention:
    def _init_(value):
        _this_.value = value
    
    def _get_value_():
        return value
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
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
    
    AnnotationRetention_entriesInitialized = True
    AnnotationRetention_SOURCE_instance = _init_('SOURCE', 0)
    AnnotationRetention_BINARY_instance = _init_('BINARY', 1)
    AnnotationRetention_RUNTIME_instance = _init_('RUNTIME', 2)

class AnnotationRetention:
    def _init_(name, ordinal):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_30370ce
    
    def _get_name_():
        pass
    
    def _get_ordinal_():
        pass
    
    def compareTo(other):
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class Repeatable:
    def _init_():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
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
    def _init_():
        ByteCompanionObject_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_50c442a5
        _this_.MIN_VALUE = visitConst_other_Byte
        _this_.MAX_VALUE = visitConst_other_Byte
        _this_.SIZE_BYTES = 1
        _this_.SIZE_BITS = 8
    
    def _get_MIN_VALUE_():
        return MIN_VALUE
    
    def _get_MAX_VALUE_():
        return MAX_VALUE
    
    def _get_SIZE_BYTES_():
        return SIZE_BYTES
    
    def _get_SIZE_BITS_():
        return SIZE_BITS
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_74b8bc34 = 0
def ByteCompanionObject_getInstance():
    if jsEqeq(ByteCompanionObject_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_380d3099
    
    return ByteCompanionObject_instance

class ShortCompanionObject:
    def _init_():
        ShortCompanionObject_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_1495f70
        _this_.MIN_VALUE = visitConst_other_Short
        _this_.MAX_VALUE = visitConst_other_Short
        _this_.SIZE_BYTES = 2
        _this_.SIZE_BITS = 16
    
    def _get_MIN_VALUE_():
        return MIN_VALUE
    
    def _get_MAX_VALUE_():
        return MAX_VALUE
    
    def _get_SIZE_BYTES_():
        return SIZE_BYTES
    
    def _get_SIZE_BITS_():
        return SIZE_BITS
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_76022ebd = 0
def ShortCompanionObject_getInstance():
    if jsEqeq(ShortCompanionObject_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_6c01bc57
    
    return ShortCompanionObject_instance

class IntCompanionObject:
    def _init_():
        IntCompanionObject_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_7d440378
        _this_.MIN_VALUE = -2147483648
        _this_.MAX_VALUE = 2147483647
        _this_.SIZE_BYTES = 4
        _this_.SIZE_BITS = 32
    
    def _get_MIN_VALUE_():
        return MIN_VALUE
    
    def _get_MAX_VALUE_():
        return MAX_VALUE
    
    def _get_SIZE_BYTES_():
        return SIZE_BYTES
    
    def _get_SIZE_BITS_():
        return SIZE_BITS
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_f9ad4c9 = 0
def IntCompanionObject_getInstance():
    if jsEqeq(IntCompanionObject_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_153de49f
    
    return IntCompanionObject_instance

class FloatCompanionObject:
    def _init_():
        FloatCompanionObject_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_33e6176b
        _this_.MIN_VALUE = visitConst_other_Float
        _this_.MAX_VALUE = visitConst_other_Float
        _this_.POSITIVE_INFINITY = visitConst_other_Float
        _this_.NEGATIVE_INFINITY = visitConst_other_Float
        _this_.NaN = visitConst_other_Float
        _this_.SIZE_BYTES = 4
        _this_.SIZE_BITS = 32
    
    def _get_MIN_VALUE_():
        return MIN_VALUE
    
    def _get_MAX_VALUE_():
        return MAX_VALUE
    
    def _get_POSITIVE_INFINITY_():
        return POSITIVE_INFINITY
    
    def _get_NEGATIVE_INFINITY_():
        return NEGATIVE_INFINITY
    
    def _get_NaN_():
        return NaN
    
    def _get_SIZE_BYTES_():
        return SIZE_BYTES
    
    def _get_SIZE_BITS_():
        return SIZE_BITS
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_1d20aae4 = 0
def FloatCompanionObject_getInstance():
    if jsEqeq(FloatCompanionObject_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_22f31149
    
    return FloatCompanionObject_instance

class DoubleCompanionObject:
    def _init_():
        DoubleCompanionObject_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_2c841ac4
        _this_.MIN_VALUE = 4.9E-324
        _this_.MAX_VALUE = 1.7976931348623157E308
        _this_.POSITIVE_INFINITY = Infinity
        _this_.NEGATIVE_INFINITY = -Infinity
        _this_.NaN = NaN
        _this_.SIZE_BYTES = 8
        _this_.SIZE_BITS = 64
    
    def _get_MIN_VALUE_():
        return MIN_VALUE
    
    def _get_MAX_VALUE_():
        return MAX_VALUE
    
    def _get_POSITIVE_INFINITY_():
        return POSITIVE_INFINITY
    
    def _get_NEGATIVE_INFINITY_():
        return NEGATIVE_INFINITY
    
    def _get_NaN_():
        return NaN
    
    def _get_SIZE_BYTES_():
        return SIZE_BYTES
    
    def _get_SIZE_BITS_():
        return SIZE_BITS
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_16109bed = 0
def DoubleCompanionObject_getInstance():
    if jsEqeq(DoubleCompanionObject_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_3cf3216c
    
    return DoubleCompanionObject_instance

class StringCompanionObject:
    def _init_():
        StringCompanionObject_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_327af731
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_1325a2ba = 0
def StringCompanionObject_getInstance():
    if jsEqeq(StringCompanionObject_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_49290bfb
    
    return StringCompanionObject_instance

class BooleanCompanionObject:
    def _init_():
        BooleanCompanionObject_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_7ba70b3b
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_4152faad = 0
def BooleanCompanionObject_getInstance():
    if jsEqeq(BooleanCompanionObject_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_44e60564
    
    return BooleanCompanionObject_instance

class Comparator:
    def compare(a, b):
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def _init_():
        pass
    

class JsName:
    def _init_(name):
        _this_.name = name
    
    def _get_name_():
        return name
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
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
    def _init_(_elements):
        _this_._elements = _elements
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_19019811
    
    def invoke(it):
        return contains(it)
    
    def invoke(p1):
        return invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_699ae22e)
    

class _no_name_provided_:
    def _init_(_elements):
        _this_._elements = _elements
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_7e860a11
    
    def invoke(it):
        return jsNot(contains(it))
    
    def invoke(p1):
        return invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_7fcc9949)
    

class AbstractMutableCollection:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_408573b1
    
    def add(element):
        pass
    
    def remove(element):
        checkIsMutable()
        iterator = iterator()
        while hasNext():
            if equals(next(), element):
                remove()
                return True
            
        
        return False
    
    def addAll(elements):
        checkIsMutable()
        modified = False
        tmp0_iterator = iterator()
        while hasNext():
            element = next()
            if add(element):
                visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_7e383712
            
        
        return modified
    
    def removeAll(elements):
        checkIsMutable()
        tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4262ac5e
        return removeAll(_no_name_provided__factory(elements))
    
    def retainAll(elements):
        checkIsMutable()
        tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_10151ecd
        return removeAll(_no_name_provided__factory(elements))
    
    def clear():
        checkIsMutable()
        iterator = iterator()
        while hasNext():
            next()
            Unit_getInstance()
            remove()
        
    
    def toJSON():
        return toArray()
    
    def checkIsMutable():
        pass
    
    def _get_size_():
        pass
    
    def iterator():
        pass
    
    def contains(element):
        pass
    
    def containsAll(elements):
        pass
    
    def isEmpty():
        pass
    
    def toString():
        pass
    
    def toArray():
        pass
    
    def toArray(array):
        pass
    
    def equals(other):
        pass
    
    def hashCode():
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
    _this._size = _set___

def _get__size_(_this):
    return _size

class IteratorImpl:
    def _init_(_outer):
        _this_._this = _outer
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_598f065f
        _this_.index = 0
        _this_.last = -1
    
    def _set_index_(_set___):
        _this_.index = _set___
    
    def _get_index_():
        return index
    
    def _set_last_(_set___):
        _this_.last = _set___
    
    def _get_last_():
        return last
    
    def hasNext():
        return jsLt(index, _get_size_())
    
    def next():
        if jsNot(hasNext()):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_57cd77e1
        
        tmp = _this_
        tmp0_this = _this_
        tmp1 = index
        tmp0_this.index = jsBitOr(jsPlus(tmp1, 1), 0)
        tmp.last = tmp1
        return get(last)
    
    def remove():
        tmp0_check_0 = jsNot(jsEqeqeq(last, -1))
        if jsNot(tmp0_check_0):
            message_1 = 'Call next() or previous() before removing element from the iterator.'
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_2585437a
        
        removeAt(last)
        Unit_getInstance()
        _this_.index = last
        _this_.last = -1
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class ListIteratorImpl:
    def _init_(_outer, index):
        _this_._this = _outer
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_131e10ca
        checkPositionIndex(index, _get_size_())
        _set_index_(index)
    
    def hasPrevious():
        return jsGt(_get_index_(), 0)
    
    def nextIndex():
        return _get_index_()
    
    def previous():
        if jsNot(hasPrevious()):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_4eba6e1f
        
        tmp0_this = _this_
        _set_index_(jsBitOr(jsMinus(_get_index_(), 1), 0))
        _set_last_(_get_index_())
        return get(_get_last_())
    
    def previousIndex():
        return jsBitOr(jsMinus(_get_index_(), 1), 0)
    
    def add(element):
        add(_get_index_(), element)
        tmp0_this = _this_
        tmp1 = _get_index_()
        _set_index_(jsBitOr(jsPlus(tmp1, 1), 0))
        Unit_getInstance()
        _set_last_(-1)
    
    def add(element):
        return add(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4a4525a1)
    
    def set(element):
        tmp0_check_0 = jsNot(jsEqeqeq(_get_last_(), -1))
        if jsNot(tmp0_check_0):
            message_1 = 'Call next() or previous() before updating element value with the iterator.'
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_63143b83
        
        set(_get_last_(), element)
        Unit_getInstance()
    
    def set(element):
        return set(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_62b899bf)
    
    def _set_index_(_set___):
        pass
    
    def _get_index_():
        pass
    
    def _set_last_(_set___):
        pass
    
    def _get_last_():
        pass
    
    def equals(other):
        pass
    
    def hasNext():
        pass
    
    def hashCode():
        pass
    
    def next():
        pass
    
    def remove():
        pass
    
    def toString():
        pass
    

class SubList:
    def _init_(list, fromIndex, toIndex):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_5b1dd206
        _this_.list = list
        _this_.fromIndex = fromIndex
        _this_._size = 0
        checkRangeIndexes(fromIndex, toIndex, _get_size_())
        _this_._size = jsBitOr(jsMinus(toIndex, fromIndex), 0)
    
    def add(index, element):
        checkPositionIndex(index, _size)
        add(jsBitOr(jsPlus(fromIndex, index), 0), element)
        tmp0_this = _this_
        tmp1 = _size
        tmp0_this._size = jsBitOr(jsPlus(tmp1, 1), 0)
        Unit_getInstance()
    
    def get(index):
        checkElementIndex(index, _size)
        return get(jsBitOr(jsPlus(fromIndex, index), 0))
    
    def removeAt(index):
        checkElementIndex(index, _size)
        result = removeAt(jsBitOr(jsPlus(fromIndex, index), 0))
        tmp0_this = _this_
        tmp1 = _size
        tmp0_this._size = jsBitOr(jsMinus(tmp1, 1), 0)
        Unit_getInstance()
        return result
    
    def set(index, element):
        checkElementIndex(index, _size)
        return set(jsBitOr(jsPlus(fromIndex, index), 0), element)
    
    def _get_size_():
        return _size
    
    def checkIsMutable():
        return checkIsMutable()
    
    def toArray():
        pass
    
    def toJSON():
        pass
    
    def _set_modCount_(_set___):
        pass
    
    def _get_modCount_():
        pass
    
    def toArray(array):
        pass
    
    def removeRange(fromIndex, toIndex):
        pass
    
    def add(element):
        pass
    
    def addAll(elements):
        pass
    
    def addAll(index, elements):
        pass
    
    def clear():
        pass
    
    def contains(element):
        pass
    
    def indexOf(element):
        pass
    
    def iterator():
        pass
    
    def lastIndexOf(element):
        pass
    
    def listIterator():
        pass
    
    def listIterator(index):
        pass
    
    def remove(element):
        pass
    
    def removeAll(elements):
        pass
    
    def retainAll(elements):
        pass
    
    def subList(fromIndex, toIndex):
        pass
    
    def containsAll(elements):
        pass
    
    def isEmpty():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class _no_name_provided_:
    def _init_(_elements):
        _this_._elements = _elements
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_1f520187
    
    def invoke(it):
        return contains(it)
    
    def invoke(p1):
        return invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_7bf62880)
    

class _no_name_provided_:
    def _init_(_elements):
        _this_._elements = _elements
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_4b5c0183
    
    def invoke(it):
        return jsNot(contains(it))
    
    def invoke(p1):
        return invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_7697fc45)
    

class AbstractMutableList:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_7bb78381
        _this_.modCount = 0
    
    def _set_modCount_(_set___):
        _this_.modCount = _set___
    
    def _get_modCount_():
        return modCount
    
    def add(index, element):
        pass
    
    def removeAt(index):
        pass
    
    def set(index, element):
        pass
    
    def add(element):
        checkIsMutable()
        add(_get_size_(), element)
        return True
    
    def addAll(index, elements):
        checkIsMutable()
        _index = index
        changed = False
        tmp0_iterator = iterator()
        while hasNext():
            e = next()
            tmp1 = _index
            _index = jsBitOr(jsPlus(tmp1, 1), 0)
            add(tmp1, e)
            changed = True
        
        return changed
    
    def clear():
        checkIsMutable()
        removeRange(0, _get_size_())
    
    def removeAll(elements):
        checkIsMutable()
        return removeAll(_no_name_provided__factory(elements))
    
    def retainAll(elements):
        checkIsMutable()
        return removeAll(_no_name_provided__factory(elements))
    
    def iterator():
        return _init_(_this_)
    
    def contains(element):
        return jsGtEq(indexOf(element), 0)
    
    def indexOf(element):
        inductionVariable = 0
        last = _get_lastIndex_()
        if jsLtEq(inductionVariable, last):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_2ce33999
        
        return -1
    
    def lastIndexOf(element):
        inductionVariable = _get_lastIndex_()
        if jsLtEq(0, inductionVariable):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_69745cfe
        
        return -1
    
    def listIterator():
        return listIterator(0)
    
    def listIterator(index):
        return _init_(_this_, index)
    
    def subList(fromIndex, toIndex):
        return _init_(_this_, fromIndex, toIndex)
    
    def removeRange(fromIndex, toIndex):
        iterator = listIterator(fromIndex)
        tmp0_repeat_0 = jsBitOr(jsMinus(toIndex, fromIndex), 0)
        inductionVariable = 0
        if jsLt(inductionVariable, tmp0_repeat_0):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_6180eb8
        
    
    def equals(other):
        if jsEqeqeq(other, _this_):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_3dc976da
        
        if jsNot(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_634324c9):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_70b437bb
        
        if True:
            pass
        
        return orderedEquals(_this_, kotlin_collections_Collection___(other))
    
    def hashCode():
        return orderedHashCode(_this_)
    
    def remove(element):
        pass
    
    def addAll(elements):
        pass
    
    def toJSON():
        pass
    
    def checkIsMutable():
        pass
    
    def _get_size_():
        pass
    
    def containsAll(elements):
        pass
    
    def isEmpty():
        pass
    
    def toString():
        pass
    
    def toArray():
        pass
    
    def toArray(array):
        pass
    
    def get(index):
        pass
    

def _no_name_provided__factory(_elements):
    i = _init_(_elements)
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_6ae9b2f0

def _no_name_provided__factory(_elements):
    i = _init_(_elements)
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_49ccecb0

def _set_array_(_this, _set___):
    _this.array = _set___

def _get_array_(_this):
    return array

def _set_isReadOnly_(_this, _set___):
    _this.isReadOnly = _set___

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
    def _init_(array):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_74ee8f57
        _this_.array = array
        _this_.isReadOnly = False
    
    def build():
        checkIsMutable()
        _this_.isReadOnly = True
        return _this_
    
    def trimToSize():
        pass
    
    def ensureCapacity(minCapacity):
        pass
    
    def _get_size_():
        return jsArrayLength(array)
    
    def get(index):
        tmp = jsArrayGet(array, rangeCheck(_this_, index))
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_7c510a83
    
    def set(index, element):
        checkIsMutable()
        rangeCheck(_this_, index)
        Unit_getInstance()
        tmp0_apply_0 = jsArrayGet(array, index)
        jsArraySet(array, index, element)
        tmp = tmp0_apply_0
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_46af3131
    
    def add(element):
        checkIsMutable()
        tmp0_asDynamic_0 = array
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_5e05dd42
        tmp0_this = _this_
        tmp1 = _get_modCount_()
        _set_modCount_(jsBitOr(jsPlus(tmp1, 1), 0))
        Unit_getInstance()
        return True
    
    def add(index, element):
        checkIsMutable()
        tmp0_asDynamic_0 = array
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_264f18fe
        tmp0_this = _this_
        tmp1 = _get_modCount_()
        _set_modCount_(jsBitOr(jsPlus(tmp1, 1), 0))
        Unit_getInstance()
    
    def addAll(elements):
        checkIsMutable()
        if isEmpty():
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_7d4bb16b
        
        tmp0_this = _this_
        tmp = tmp0_this
        tmp0_plus_0 = array
        tmp1_plus_0 = copyToArray(elements)
        tmp.array = kotlin_Array_kotlin_Any__(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_44a98855)
        tmp1_this = _this_
        tmp2 = _get_modCount_()
        _set_modCount_(jsBitOr(jsPlus(tmp2, 1), 0))
        Unit_getInstance()
        return True
    
    def addAll(index, elements):
        checkIsMutable()
        insertionRangeCheck(_this_, index)
        Unit_getInstance()
        if jsEqeqeq(index, _get_size_()):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_7abc838a
        
        if isEmpty():
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_417f7d7f
        
        tmp0_subject = index
        if jsEqeqeq(tmp0_subject, _get_size_()):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_69173bb7
        
        if jsEqeqeq(tmp0_subject, 0):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_3af1dda5
        
        if True:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_4b305823
        
        tmp1_this = _this_
        tmp2 = _get_modCount_()
        _set_modCount_(jsBitOr(jsPlus(tmp2, 1), 0))
        Unit_getInstance()
        return True
    
    def removeAt(index):
        checkIsMutable()
        rangeCheck(_this_, index)
        Unit_getInstance()
        tmp0_this = _this_
        tmp1 = _get_modCount_()
        _set_modCount_(jsBitOr(jsPlus(tmp1, 1), 0))
        Unit_getInstance()
        tmp
        if jsEqeqeq(index, _get_lastIndex_()):
            tmp0_asDynamic_0 = array
            tmp = E(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_5a14a8c1)
        
        if True:
            tmp1_asDynamic_0 = array
            tmp = E(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_1f6af096)
        
        return tmp
    
    def remove(element):
        checkIsMutable()
        inductionVariable = 0
        last = jsBitOr(jsMinus(jsArrayLength(array), 1), 0)
        if jsLtEq(inductionVariable, last):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_eb5589
        
        return False
    
    def removeRange(fromIndex, toIndex):
        checkIsMutable()
        tmp0_this = _this_
        tmp1 = _get_modCount_()
        _set_modCount_(jsBitOr(jsPlus(tmp1, 1), 0))
        Unit_getInstance()
        tmp0_asDynamic_0 = array
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_34d08905
    
    def clear():
        checkIsMutable()
        tmp = _this_
        tmp.array = kotlin_Array_kotlin_Any__(js('[]'))
        tmp0_this = _this_
        tmp1 = _get_modCount_()
        _set_modCount_(jsBitOr(jsPlus(tmp1, 1), 0))
        Unit_getInstance()
    
    def indexOf(element):
        return indexOf(element)
    
    def lastIndexOf(element):
        return lastIndexOf(element)
    
    def toString():
        return arrayToString(array)
    
    def toArray():
        return kotlin_Array_kotlin_Any__(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_e00f822)
    
    def toArray():
        return toArray()
    
    def checkIsMutable():
        if isReadOnly:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_1a2d9177
        
    
    def _set_modCount_(_set___):
        pass
    
    def _get_modCount_():
        pass
    
    def removeAll(elements):
        pass
    
    def retainAll(elements):
        pass
    
    def iterator():
        pass
    
    def contains(element):
        pass
    
    def listIterator():
        pass
    
    def listIterator(index):
        pass
    
    def subList(fromIndex, toIndex):
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toJSON():
        pass
    
    def containsAll(elements):
        pass
    
    def isEmpty():
        pass
    
    def toArray(array):
        pass
    

def _set__stableSortingIsSupported_(_set___):
    _stableSortingIsSupported = _set___

def _get__stableSortingIsSupported_():
    return _stableSortingIsSupported

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_13e76a91 = 0
class RandomAccess:
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def _init_():
        pass
    

def _set_output_(_set___):
    output = _set___

def _get_output_():
    return output

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_28dae87e = 0
class BaseOutput:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_3e5e7f4c
    
    def println():
        print('\n')
    
    def println(message):
        print(message)
        println()
    
    def print(message):
        pass
    
    def flush():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class NodeJsOutput:
    def _init_(outputStream):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_7902a4d7
        _this_.outputStream = outputStream
    
    def _get_outputStream_():
        return outputStream
    
    def print(message):
        messageString = kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_44c639d4)
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_19f007c4
    
    def println():
        pass
    
    def println(message):
        pass
    
    def flush():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class BufferedOutputToConsoleLog:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_3f6f26cb
    
    def print(message):
        s = kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_6edd2ef4)
        tmp0_nativeLastIndexOf_0 = s
        tmp1_nativeLastIndexOf_0 = '\n'
        tmp2_nativeLastIndexOf_0 = 0
        i = kotlin_Int(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_29ed425e)
        if jsGtEq(i, 0):
            tmp0_this = _this_
            tmp = _get_buffer_()
            tmp3_substring_0 = s
            tmp4_substring_0 = 0
            _set_buffer_(jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_7f91d389)))
            flush()
            tmp5_substring_0 = s
            tmp6_substring_0 = jsBitOr(jsPlus(i, 1), 0)
            s = kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_50a59a0b)
        
        tmp1_this = _this_
        _set_buffer_(jsPlus(_get_buffer_(), s))
    
    def flush():
        log(arrayLiteral(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_75388ef2))
        _set_buffer_('')
    
    def _set_buffer_(_set___):
        pass
    
    def _get_buffer_():
        pass
    
    def println():
        pass
    
    def println(message):
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

def String(value):
    return kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_371ce753)

class BufferedOutput:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_529a2d6f
        _this_.buffer = ''
    
    def _set_buffer_(_set___):
        _this_.buffer = _set___
    
    def _get_buffer_():
        return buffer
    
    def print(message):
        tmp0_this = _this_
        tmp = tmp0_this
        tmp = buffer
        tmp.buffer = jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_22d12034))
    
    def flush():
        _this_.buffer = ''
    
    def println():
        pass
    
    def println(message):
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
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
    def _init_(_tmp0_Continuation_0):
        _this_._tmp0_Continuation_0 = _tmp0_Continuation_0
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_692cea53
    
    def _get_context__2():
        return _tmp0_Continuation_0
    
    def _get_context_():
        return _get_context__2()
    
    def resumeWith_3(result):
        throwOnFailure()
        tmp = _Result___get_value__impl_(result)
        if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_19eb658:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrTypeOperatorCallImpl_75c99797
        
        if True:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCallImpl_36b3240f
        
        return Unit_getInstance()
    
    def resumeWith(result):
        return resumeWith_3(result)
    
    def equals_4(other):
        pass
    
    def hashCode_5():
        pass
    
    def toString_6():
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
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def _init_():
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
    def _get_name_():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def _init_():
        pass
    

class KClass:
    def _get_simpleName_():
        pass
    
    def _get_qualifiedName_():
        pass
    
    def isInstance(value):
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def _init_():
        pass
    

class KClassImpl:
    def _init_(jClass):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_4ec1192f
        _this_.jClass = jClass
    
    def _get_jClass_():
        return jClass
    
    def _get_qualifiedName_():
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_7e5432ca
    
    def equals(other):
        tmp
        if jsInstanceOf(other, jsClass()):
            tmp = equals(_get_jClass_(), _get_jClass_())
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def hashCode():
        tmp0_safe_receiver = _get_simpleName_()
        tmp1_elvis_lhs = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_e31b415
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_7027c359
    
    def toString():
        return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_7458d7a9
    
    def _get_simpleName_():
        pass
    
    def isInstance(value):
        pass
    

def _get_givenSimpleName_(_this):
    return givenSimpleName

def _get_isInstanceFunction_(_this):
    return isInstanceFunction

class PrimitiveKClassImpl:
    def _init_(jClass, givenSimpleName, isInstanceFunction):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_642ebd4c
        _this_.givenSimpleName = givenSimpleName
        _this_.isInstanceFunction = isInstanceFunction
    
    def equals(other):
        if jsNot(jsInstanceOf(other, jsClass())):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_1d691d4f
        
        if True:
            pass
        
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3b43a957
    
    def _get_simpleName_():
        return givenSimpleName
    
    def isInstance(value):
        return invoke(value)
    
    def _get_jClass_():
        pass
    
    def _get_qualifiedName_():
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class NothingKClassImpl:
    def _init_():
        NothingKClassImpl_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_3d70dab8
        _this_.simpleName = 'Nothing'
    
    def _get_simpleName_():
        return simpleName
    
    def isInstance(value):
        return False
    
    def _get_jClass_():
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_3c2b7322
    
    def equals(other):
        return jsEqeqeq(other, _this_)
    
    def hashCode():
        return 0
    
    def _get_qualifiedName_():
        pass
    
    def toString():
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_5ad07e46 = 0
def NothingKClassImpl_getInstance():
    if jsEqeq(NothingKClassImpl_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_13b18bd2
    
    return NothingKClassImpl_instance

class ErrorKClass:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_6d821475
    
    def _get_simpleName_():
        tmp0_error_0 = 'Unknown simpleName for ErrorKClass'
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_3845dedd
    
    def _get_qualifiedName_():
        tmp0_error_0 = 'Unknown qualifiedName for ErrorKClass'
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_64c555f7
    
    def isInstance(value):
        tmp0_error_0 = 'Can\'s check isInstance on ErrorKClass'
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_781b09b3
    
    def equals(other):
        return jsEqeqeq(other, _this_)
    
    def hashCode():
        return 0
    
    def toString():
        pass
    

class SimpleKClassImpl:
    def _init_(jClass):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_3a7e13c0
        tmp = _this_
        tmp0_safe_receiver = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicMemberExpressionImpl_598ffbc8
        tmp0_unsafeCast_0 = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_49a23dd4
        tmp.simpleName = kotlin_Any_(tmp0_unsafeCast_0)
    
    def _get_simpleName_():
        return simpleName
    
    def isInstance(value):
        return jsIsType(value, _get_jClass_())
    
    def _get_jClass_():
        pass
    
    def _get_qualifiedName_():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class KFunction:
    def _get_name_():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def _init_():
        pass
    

class KProperty:
    def _get_name_():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def _init_():
        pass
    

class KProperty0:
    def get():
        pass
    
    def _get_name_():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def invoke():
        pass
    
    def _init_():
        pass
    

class KProperty1:
    def get(receiver):
        pass
    
    def _get_name_():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def invoke(p1):
        pass
    
    def _init_():
        pass
    

class KProperty2:
    def get(receiver1, receiver2):
        pass
    
    def _get_name_():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def invoke(p1, p2):
        pass
    
    def _init_():
        pass
    

class KMutableProperty0:
    def set(value):
        pass
    
    def get():
        pass
    
    def _get_name_():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def invoke():
        pass
    
    def _init_():
        pass
    

class KMutableProperty:
    def _get_name_():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def _init_():
        pass
    

class KMutableProperty1:
    def set(receiver, value):
        pass
    
    def get(receiver):
        pass
    
    def _get_name_():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def invoke(p1):
        pass
    
    def _init_():
        pass
    

class KMutableProperty2:
    def set(receiver1, receiver2, value):
        pass
    
    def get(receiver1, receiver2):
        pass
    
    def _get_name_():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def invoke(p1, p2):
        pass
    
    def _init_():
        pass
    

class KType:
    def _get_classifier_():
        pass
    
    def _get_arguments_():
        pass
    
    def _get_isMarkedNullable_():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def _init_():
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
    def _init_(this_0):
        _this_.this_0 = this_0
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_73c29540
    
    def invoke(it):
        return asString(this_0)
    
    def invoke(p1):
        return invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_49172e03)
    

class KTypeImpl:
    def _init_(classifier, arguments, isMarkedNullable):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_561494af
        _this_.classifier = classifier
        _this_.arguments = arguments
        _this_.isMarkedNullable = isMarkedNullable
    
    def _get_classifier_():
        return classifier
    
    def _get_arguments_():
        return arguments
    
    def _get_isMarkedNullable_():
        return isMarkedNullable
    
    def equals(other):
        tmp
        tmp
        tmp
        if jsInstanceOf(other, jsClass()):
            tmp = equals(classifier, classifier)
        
        if True:
            if True:
                tmp = False
            
        
        if tmp:
            tmp = equals(arguments, arguments)
        
        if True:
            if True:
                tmp = False
            
        
        if tmp:
            tmp = jsEqeqeq(isMarkedNullable, isMarkedNullable)
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def hashCode():
        return jsBitOr(jsPlus(imul(jsBitOr(jsPlus(imul(hashCode(classifier), 31), hashCode(arguments)), 0), 31), jsBitOr(isMarkedNullable, 0)), 0)
    
    def toString():
        tmp = classifier
        kClass = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4808c603
        classifierName = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2ab33a27
        tmp
        if isEmpty():
            tmp = ''
        
        if True:
            tmp = joinToString_default(', ', '<', '>', 0, None, _no_name_provided__factory(_this_), 24, None)
        
        args = tmp
        nullable = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3a05ba57
        return jsPlus(plus(args), nullable)
    

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
    def _init_():
        DynamicKType_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_3f04847e
        _this_.classifier = None
        _this_.arguments = emptyList()
        _this_.isMarkedNullable = False
    
    def _get_classifier_():
        return classifier
    
    def _get_arguments_():
        return arguments
    
    def _get_isMarkedNullable_():
        return isMarkedNullable
    
    def toString():
        return 'dynamic'
    
    def equals(other):
        pass
    
    def hashCode():
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
    def _init_(name, upperBounds, variance, isReified):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_2265a052
        _this_.name = name
        _this_.upperBounds = upperBounds
        _this_.variance = variance
        _this_.isReified = isReified
    
    def _get_name_():
        return name
    
    def _get_upperBounds_():
        return upperBounds
    
    def _get_variance_():
        return variance
    
    def _get_isReified_():
        return isReified
    
    def toString():
        return name
    
    def component1():
        return name
    
    def component2():
        return upperBounds
    
    def component3():
        return variance
    
    def component4():
        return isReified
    
    def copy(name, upperBounds, variance, isReified):
        return _init_(name, upperBounds, variance, isReified)
    
    def copy_default(name, upperBounds, variance, isReified, _mask0, _handler):
        if jsNot(jsEqeqeq(jsBitAnd(_mask0, 1), 0)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_44af21cf
        
        if jsNot(jsEqeqeq(jsBitAnd(_mask0, 2), 0)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_141b6877
        
        if jsNot(jsEqeqeq(jsBitAnd(_mask0, 4), 0)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_f8f9ce0
        
        if jsNot(jsEqeqeq(jsBitAnd(_mask0, 8), 0)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_aa85268
        
        return copy(kotlin_String(name), kotlin_collections_List_kotlin_reflect_KType_(upperBounds), kotlin_reflect_KVariance(variance), isReified)
    
    def hashCode():
        result = getStringHashCode(name)
        result = jsBitOr(jsPlus(imul(result, 31), hashCode(upperBounds)), 0)
        result = jsBitOr(jsPlus(imul(result, 31), hashCode()), 0)
        result = jsBitOr(jsPlus(imul(result, 31), jsBitOr(isReified, 0)), 0)
        return result
    
    def equals(other):
        if jsEqeqeq(_this_, other):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_5cb6fac3
        
        if jsNot(jsInstanceOf(other, jsClass())):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_2ea3f905
        
        if True:
            pass
        
        tmp0_other_with_cast = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6a18bbeb
        if jsNot(jsEqeqeq(name, name)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_122557f8
        
        if jsNot(equals(upperBounds, upperBounds)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_24663d05
        
        if jsNot(equals(variance)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_279e9c95
        
        if jsNot(jsEqeqeq(isReified, isReified)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_427c8f6
        
        return True
    

def _get_functionClasses_():
    return functionClasses

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_3bd466bd = 0
class _no_name_provided_:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_48d54b1c
    
    def invoke(it):
        return isObject(it)
    
    def invoke(p1):
        return invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2e897323)
    

class _no_name_provided_:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_6c439a57
    
    def invoke(it):
        return isNumber(it)
    
    def invoke(p1):
        return invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3b678c5)
    

class _no_name_provided_:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_6d4d4108
    
    def invoke(it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_365b1eb5
    
    def invoke(p1):
        return invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_5aef3960)
    

class _no_name_provided_:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_412dd71b
    
    def invoke(it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_332f6402
    
    def invoke(p1):
        return invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6399a7e2)
    

class _no_name_provided_:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_4a9f9ed2
    
    def invoke(it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_a9781d8
    
    def invoke(p1):
        return invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4e26774d)
    

class _no_name_provided_:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_3032aa88
    
    def invoke(it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_21a9e25a
    
    def invoke(p1):
        return invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_74134494)
    

class _no_name_provided_:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_5feb2d13
    
    def invoke(it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3195d44a
    
    def invoke(p1):
        return invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_5e90de14)
    

class _no_name_provided_:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_702a0b7d
    
    def invoke(it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_31786c4c
    
    def invoke(p1):
        return invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_5fdc1f4a)
    

class _no_name_provided_:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_7e1716c2
    
    def invoke(it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_34a86c40
    
    def invoke(p1):
        return invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_a98ce67)
    

class _no_name_provided_:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_7c397b0c
    
    def invoke(it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_752ee6e1
    
    def invoke(p1):
        return invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_173de441)
    

class _no_name_provided_:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_372741bb
    
    def invoke(it):
        return jsInstanceOf(it, jsClass())
    
    def invoke(p1):
        return invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3eb36de9)
    

class _no_name_provided_:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_1a7da0b9
    
    def invoke(it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4dd1d767
    
    def invoke(p1):
        return invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_5f5bc594)
    

class _no_name_provided_:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_515e9100
    
    def invoke(it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_51d502a6
    
    def invoke(p1):
        return invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_1ac864d7)
    

class _no_name_provided_:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_464735bf
    
    def invoke(it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3b3cc6b1
    
    def invoke(p1):
        return invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3a37d3b6)
    

class _no_name_provided_:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_3adb51f2
    
    def invoke(it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_26b3f25b
    
    def invoke(p1):
        return invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6a907765)
    

class _no_name_provided_:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_4497e084
    
    def invoke(it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_5d3b93b4
    
    def invoke(p1):
        return invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_77833456)
    

class _no_name_provided_:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_45b0f44b
    
    def invoke(it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_44ce8395
    
    def invoke(p1):
        return invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_11214149)
    

class _no_name_provided_:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_6cd17c11
    
    def invoke(it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_74ecaa35
    
    def invoke(p1):
        return invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_360b8448)
    

class _no_name_provided_:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_5aefdd21
    
    def invoke(it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_57fb5ebf
    
    def invoke(p1):
        return invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_73f55299)
    

class _no_name_provided_:
    def _init_(_arity):
        _this_._arity = _arity
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_169b16dd
    
    def invoke(it):
        tmp
        if jsEqeqeq(jsTypeOf(it), 'function'):
            tmp = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_467c9ad9
        
        if True:
            tmp = False
        
        return tmp
    
    def invoke(p1):
        return invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6eeee66f)
    

class PrimitiveClasses:
    def _init_():
        PrimitiveClasses_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_5ccf1542
        tmp = _this_
        tmp0_unsafeCast_0 = js('Object')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.anyClass = _init_(tmp, 'Any', _no_name_provided__factory())
        tmp = _this_
        tmp0_unsafeCast_0 = js('Number')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.numberClass = _init_(tmp, 'Number', _no_name_provided__factory())
        _this_.nothingClass = NothingKClassImpl_getInstance()
        tmp = _this_
        tmp0_unsafeCast_0 = js('Boolean')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.booleanClass = _init_(tmp, 'Boolean', _no_name_provided__factory())
        tmp = _this_
        tmp0_unsafeCast_0 = js('Number')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.byteClass = _init_(tmp, 'Byte', _no_name_provided__factory())
        tmp = _this_
        tmp0_unsafeCast_0 = js('Number')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.shortClass = _init_(tmp, 'Short', _no_name_provided__factory())
        tmp = _this_
        tmp0_unsafeCast_0 = js('Number')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.intClass = _init_(tmp, 'Int', _no_name_provided__factory())
        tmp = _this_
        tmp0_unsafeCast_0 = js('Number')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.floatClass = _init_(tmp, 'Float', _no_name_provided__factory())
        tmp = _this_
        tmp0_unsafeCast_0 = js('Number')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.doubleClass = _init_(tmp, 'Double', _no_name_provided__factory())
        tmp = _this_
        tmp0_unsafeCast_0 = js('Array')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.arrayClass = _init_(tmp, 'Array', _no_name_provided__factory())
        tmp = _this_
        tmp0_unsafeCast_0 = js('String')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.stringClass = _init_(tmp, 'String', _no_name_provided__factory())
        tmp = _this_
        tmp0_unsafeCast_0 = js('Error')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.throwableClass = _init_(tmp, 'Throwable', _no_name_provided__factory())
        tmp = _this_
        tmp0_unsafeCast_0 = js('Array')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.booleanArrayClass = _init_(tmp, 'BooleanArray', _no_name_provided__factory())
        tmp = _this_
        tmp0_unsafeCast_0 = js('Uint16Array')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.charArrayClass = _init_(tmp, 'CharArray', _no_name_provided__factory())
        tmp = _this_
        tmp0_unsafeCast_0 = js('Int8Array')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.byteArrayClass = _init_(tmp, 'ByteArray', _no_name_provided__factory())
        tmp = _this_
        tmp0_unsafeCast_0 = js('Int16Array')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.shortArrayClass = _init_(tmp, 'ShortArray', _no_name_provided__factory())
        tmp = _this_
        tmp0_unsafeCast_0 = js('Int32Array')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.intArrayClass = _init_(tmp, 'IntArray', _no_name_provided__factory())
        tmp = _this_
        tmp0_unsafeCast_0 = js('Array')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.longArrayClass = _init_(tmp, 'LongArray', _no_name_provided__factory())
        tmp = _this_
        tmp0_unsafeCast_0 = js('Float32Array')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.floatArrayClass = _init_(tmp, 'FloatArray', _no_name_provided__factory())
        tmp = _this_
        tmp0_unsafeCast_0 = js('Float64Array')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.doubleArrayClass = _init_(tmp, 'DoubleArray', _no_name_provided__factory())
    
    def _get_anyClass_():
        return anyClass
    
    def _get_numberClass_():
        return numberClass
    
    def _get_nothingClass_():
        return nothingClass
    
    def _get_booleanClass_():
        return booleanClass
    
    def _get_byteClass_():
        return byteClass
    
    def _get_shortClass_():
        return shortClass
    
    def _get_intClass_():
        return intClass
    
    def _get_floatClass_():
        return floatClass
    
    def _get_doubleClass_():
        return doubleClass
    
    def _get_arrayClass_():
        return arrayClass
    
    def _get_stringClass_():
        return stringClass
    
    def _get_throwableClass_():
        return throwableClass
    
    def _get_booleanArrayClass_():
        return booleanArrayClass
    
    def _get_charArrayClass_():
        return charArrayClass
    
    def _get_byteArrayClass_():
        return byteArrayClass
    
    def _get_shortArrayClass_():
        return shortArrayClass
    
    def _get_intArrayClass_():
        return intArrayClass
    
    def _get_longArrayClass_():
        return longArrayClass
    
    def _get_floatArrayClass_():
        return floatArrayClass
    
    def _get_doubleArrayClass_():
        return doubleArrayClass
    
    def functionClass(arity):
        tmp0_elvis_lhs = jsArrayGet(functionClasses, arity)
        tmp
        if jsEqeq(tmp0_elvis_lhs, None):
            tmp0_unsafeCast_0_3 = js('Function')
            tmp = kotlin_Any_(tmp0_unsafeCast_0_3)
            tmp = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_3dc3c293
            result_2 = _init_(tmp, tmp, _no_name_provided__factory(arity))
            tmp1_asDynamic_0_5 = functionClasses
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_1d132288
            tmp = result_2
        
        if True:
            tmp = tmp0_elvis_lhs
        
        return tmp
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
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
    def append(value):
        pass
    
    def append(value):
        pass
    
    def append(value, startIndex, endIndex):
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def _init_():
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
    _this.string = _set___

def _get_string_(_this):
    return string

def checkReplaceRange(_this, startIndex, endIndex, length):
    if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6b86a5a4:
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_ecd59a3
    
    if jsGt(startIndex, endIndex):
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_56984e92
    

class StringBuilder:
    def _init_(content):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_13ebbdab
        _this_.string = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_38934406
    
    def _get_length_():
        tmp0_asDynamic_0 = string
        return kotlin_Int(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicMemberExpressionImpl_2a03b87)
    
    def get(index):
        tmp0_getOrElse_0 = string
        tmp
        if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_5d978663:
            tmp = charSequenceGet(tmp0_getOrElse_0, index)
        
        if True:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_7d9d59df
        
        return tmp
    
    def subSequence(startIndex, endIndex):
        tmp0_substring_0 = string
        return kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_7296a632)
    
    def append(value):
        tmp0_this = _this_
        tmp0_this.string = jsPlus(string, value)
        return _this_
    
    def append(value):
        tmp0_this = _this_
        tmp0_this.string = jsPlus(string, toString())
        return _this_
    
    def append(value, startIndex, endIndex):
        tmp0_elvis_lhs = value
        return appendRange(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_1fc0e258, startIndex, endIndex)
    
    def reverse():
        reversed = ''
        index = jsBitOr(jsMinus(jsArrayLength(string), 1), 0)
        while jsGtEq(index, 0):
            tmp = string
            tmp0 = index
            index = jsBitOr(jsMinus(tmp0, 1), 0)
            low = charSequenceGet(tmp, tmp0)
            if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_423a5c9c:
                tmp = string
                tmp1 = index
                index = jsBitOr(jsMinus(tmp1, 1), 0)
                high = charSequenceGet(tmp, tmp1)
                if isHighSurrogate():
                    reversed = jsPlus(jsPlus(reversed, high), low)
                
                if True:
                    reversed = jsPlus(jsPlus(reversed, low), high)
                
            
            if True:
                reversed = jsPlus(reversed, low)
            
        
        _this_.string = reversed
        return _this_
    
    def append(value):
        tmp0_this = _this_
        tmp0_this.string = jsPlus(string, toString())
        return _this_
    
    def append(value):
        tmp0_this = _this_
        tmp0_this.string = jsPlus(string, value)
        return _this_
    
    def append(value):
        tmp0_this = _this_
        tmp0_this.string = jsPlus(string, concatToString())
        return _this_
    
    def append(value):
        return append(value)
    
    def append(value):
        tmp0_this = _this_
        tmp = tmp0_this
        tmp = string
        tmp1_elvis_lhs = value
        tmp.string = jsPlus(tmp, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_736500e6)
        return _this_
    
    def capacity():
        return _get_length_()
    
    def ensureCapacity(minimumCapacity):
        pass
    
    def indexOf(string):
        tmp0_asDynamic_0 = string
        return kotlin_Int(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_4d619aa0)
    
    def indexOf(string, startIndex):
        tmp0_asDynamic_0 = string
        return kotlin_Int(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_4e64e44c)
    
    def lastIndexOf(string):
        tmp0_asDynamic_0 = string
        return kotlin_Int(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_510c6b9)
    
    def lastIndexOf(string, startIndex):
        tmp
        if jsEqeqeq(charSequenceLength(string), 0):
            tmp = jsLt(startIndex, 0)
        
        if True:
            if True:
                tmp = False
            
        
        if tmp:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_298154d4
        
        if True:
            pass
        
        tmp0_asDynamic_0 = string
        return kotlin_Int(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_8e654f7)
    
    def insert(index, value):
        checkPositionIndex(index, _get_length_())
        tmp = _this_
        tmp0_substring_0 = string
        tmp1_substring_0 = 0
        tmp = jsPlus(kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_3144dd1a), value)
        tmp2_substring_0 = string
        tmp.string = jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_6795c28a))
        return _this_
    
    def insert(index, value):
        checkPositionIndex(index, _get_length_())
        tmp = _this_
        tmp0_substring_0 = string
        tmp1_substring_0 = 0
        tmp = jsPlus(kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_596416c5), value)
        tmp2_substring_0 = string
        tmp.string = jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_3f575bad))
        return _this_
    
    def insert(index, value):
        checkPositionIndex(index, _get_length_())
        tmp = _this_
        tmp0_substring_0 = string
        tmp1_substring_0 = 0
        tmp = jsPlus(kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_2bc8c738), concatToString())
        tmp2_substring_0 = string
        tmp.string = jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_346df1c0))
        return _this_
    
    def insert(index, value):
        checkPositionIndex(index, _get_length_())
        tmp = _this_
        tmp0_substring_0 = string
        tmp1_substring_0 = 0
        tmp = jsPlus(kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_21612e76), toString())
        tmp2_substring_0 = string
        tmp.string = jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_26d60427))
        return _this_
    
    def insert(index, value):
        checkPositionIndex(index, _get_length_())
        tmp = _this_
        tmp0_substring_0 = string
        tmp1_substring_0 = 0
        tmp = jsPlus(kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_30c6f027), toString())
        tmp2_substring_0 = string
        tmp.string = jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_59c08dd4))
        return _this_
    
    def insert(index, value):
        return insert(index, value)
    
    def insert(index, value):
        checkPositionIndex(index, _get_length_())
        tmp0_elvis_lhs = value
        toInsert = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_ca0ccb6
        tmp = _this_
        tmp0_substring_0 = string
        tmp1_substring_0 = 0
        tmp = jsPlus(kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_10b69457), toInsert)
        tmp2_substring_0 = string
        tmp.string = jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_6e2a031b))
        return _this_
    
    def setLength(newLength):
        if jsLt(newLength, 0):
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_1129775
        
        if jsLtEq(newLength, _get_length_()):
            tmp = _this_
            tmp0_substring_0 = string
            tmp1_substring_0 = 0
            tmp.string = kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_1c097e3)
        
        if True:
            inductionVariable = _get_length_()
            if jsLt(inductionVariable, newLength):
                visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_25a85c9
            
        
    
    def substring(startIndex):
        checkPositionIndex(startIndex, _get_length_())
        tmp0_substring_0 = string
        return kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_67b5a089)
    
    def substring(startIndex, endIndex):
        checkBoundsIndexes(startIndex, endIndex, _get_length_())
        tmp0_substring_0 = string
        return kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_714bd7ad)
    
    def trimToSize():
        pass
    
    def toString():
        return string
    
    def clear():
        _this_.string = ''
        return _this_
    
    def set(index, value):
        checkElementIndex(index, _get_length_())
        tmp = _this_
        tmp0_substring_0 = string
        tmp1_substring_0 = 0
        tmp = jsPlus(kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_3209eb), value)
        tmp2_substring_0 = string
        tmp3_substring_0 = jsBitOr(jsPlus(index, 1), 0)
        tmp.string = jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_57ddbe75))
    
    def setRange(startIndex, endIndex, value):
        checkReplaceRange(_this_, startIndex, endIndex, _get_length_())
        tmp = _this_
        tmp0_substring_0 = string
        tmp1_substring_0 = 0
        tmp = jsPlus(kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_5233090a), value)
        tmp2_substring_0 = string
        tmp.string = jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_68e66fff))
        return _this_
    
    def deleteAt(index):
        checkElementIndex(index, _get_length_())
        tmp = _this_
        tmp0_substring_0 = string
        tmp1_substring_0 = 0
        tmp = kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_5d5790ea)
        tmp2_substring_0 = string
        tmp3_substring_0 = jsBitOr(jsPlus(index, 1), 0)
        tmp.string = jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_614eceb))
        return _this_
    
    def deleteRange(startIndex, endIndex):
        checkReplaceRange(_this_, startIndex, endIndex, _get_length_())
        tmp = _this_
        tmp0_substring_0 = string
        tmp1_substring_0 = 0
        tmp = kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_5b4bdee3)
        tmp2_substring_0 = string
        tmp.string = jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_56e18141))
        return _this_
    
    def toCharArray(destination, destinationOffset, startIndex, endIndex):
        checkBoundsIndexes(startIndex, endIndex, _get_length_())
        checkBoundsIndexes(destinationOffset, jsBitOr(jsMinus(jsBitOr(jsPlus(destinationOffset, endIndex), 0), startIndex), 0), jsArrayLength(destination))
        dstIndex = destinationOffset
        inductionVariable = startIndex
        if jsLt(inductionVariable, endIndex):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_38c203a6
        
    
    def toCharArray_default(destination, destinationOffset, startIndex, endIndex, _mask0, _handler):
        if jsNot(jsEqeqeq(jsBitAnd(_mask0, 2), 0)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_55b678dc
        
        if jsNot(jsEqeqeq(jsBitAnd(_mask0, 4), 0)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_c541518
        
        if jsNot(jsEqeqeq(jsBitAnd(_mask0, 8), 0)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_d0a2a80
        
        return toCharArray(destination, destinationOffset, startIndex, endIndex)
    
    def appendRange(value, startIndex, endIndex):
        tmp0_this = _this_
        tmp0_this.string = jsPlus(string, concatToString(startIndex, endIndex))
        return _this_
    
    def appendRange(value, startIndex, endIndex):
        stringCsq = toString(value)
        checkBoundsIndexes(startIndex, endIndex, jsArrayLength(stringCsq))
        tmp0_this = _this_
        tmp = tmp0_this
        tmp = string
        tmp.string = jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_56b3165c))
        return _this_
    
    def insertRange(index, value, startIndex, endIndex):
        checkPositionIndex(index, _get_length_())
        tmp = _this_
        tmp0_substring_0 = string
        tmp1_substring_0 = 0
        tmp = jsPlus(kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_4e59830b), concatToString(startIndex, endIndex))
        tmp2_substring_0 = string
        tmp.string = jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_2646531d))
        return _this_
    
    def insertRange(index, value, startIndex, endIndex):
        checkPositionIndex(index, _get_length_())
        stringCsq = toString(value)
        checkBoundsIndexes(startIndex, endIndex, jsArrayLength(stringCsq))
        tmp = _this_
        tmp0_substring_0 = string
        tmp1_substring_0 = 0
        tmp = kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_4077b71e)
        tmp = jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_515a4ee))
        tmp2_substring_0 = string
        tmp.string = jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_f86b42c))
        return _this_
    
    def equals(other):
        pass
    
    def hashCode():
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
    def _init_(function):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_56609c11
        _this_.function = function
    
    def compare(a, b):
        return invoke(a, b)
    
    def compare(a, b):
        return compare(a, b)
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class _no_name_provided_:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_29031a38
    
    def invoke(a, b):
        return compareTo(b, True)
    
    def invoke(p1, p2):
        tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_5494539a
        return invoke(tmp, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4a114a53)
    

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
    def _init_():
        Companion_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_6042b613
        _this_.MIN_VALUE = _init_(0)
        _this_.MAX_VALUE = _init_(65535)
        _this_.MIN_HIGH_SURROGATE = _init_(55296)
        _this_.MAX_HIGH_SURROGATE = _init_(56319)
        _this_.MIN_LOW_SURROGATE = _init_(56320)
        _this_.MAX_LOW_SURROGATE = _init_(57343)
        _this_.MIN_SURROGATE = _init_(55296)
        _this_.MAX_SURROGATE = _init_(57343)
        _this_.SIZE_BYTES = 2
        _this_.SIZE_BITS = 16
    
    def _get_MIN_VALUE_():
        return MIN_VALUE
    
    def _get_MAX_VALUE_():
        return MAX_VALUE
    
    def _get_MIN_HIGH_SURROGATE_():
        return MIN_HIGH_SURROGATE
    
    def _get_MAX_HIGH_SURROGATE_():
        return MAX_HIGH_SURROGATE
    
    def _get_MIN_LOW_SURROGATE_():
        return MIN_LOW_SURROGATE
    
    def _get_MAX_LOW_SURROGATE_():
        return MAX_LOW_SURROGATE
    
    def _get_MIN_SURROGATE_():
        return MIN_SURROGATE
    
    def _get_MAX_SURROGATE_():
        return MAX_SURROGATE
    
    def _get_SIZE_BYTES_():
        return SIZE_BYTES
    
    def _get_SIZE_BITS_():
        return SIZE_BITS
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_7e2f2791 = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_383cd5d8
    
    return Companion_instance

class Char:
    def _init_(value):
        Companion_getInstance()
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_66ab765c
        _this_.value = value
    
    def compareTo(other):
        return jsBitOr(jsMinus(value, value), 0)
    
    def compareTo(other):
        return compareTo(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_263ecd4b)
    
    def plus(other):
        return numberToChar(jsBitOr(jsPlus(value, other), 0))
    
    def minus(other):
        return jsBitOr(jsMinus(value, value), 0)
    
    def minus(other):
        return numberToChar(jsBitOr(jsMinus(value, other), 0))
    
    def inc():
        return numberToChar(jsBitOr(jsPlus(value, 1), 0))
    
    def dec():
        return numberToChar(jsBitOr(jsMinus(value, 1), 0))
    
    def rangeTo(other):
        return _init_(_this_, other)
    
    def toByte():
        return toByte(value)
    
    def toChar():
        return _this_
    
    def toShort():
        return toShort(value)
    
    def toInt():
        return value
    
    def toLong():
        return toLong(value)
    
    def toFloat():
        return kotlin_Float(value)
    
    def toDouble():
        return kotlin_Double(value)
    
    def equals(other):
        if jsEqeqeq(other, _this_):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_76c5599b
        
        if jsNot(jsInstanceOf(other, jsClass())):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_3b68a50c
        
        if True:
            pass
        
        return jsEqeqeq(value, value)
    
    def hashCode():
        return value
    
    def toString():
        tmp0_unsafeCast_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_7b9661d4
        return kotlin_Any_(tmp0_unsafeCast_0)
    

class Iterable:
    def iterator():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def _init_():
        pass
    

class Collection:
    def _get_size_():
        pass
    
    def isEmpty():
        pass
    
    def contains(element):
        pass
    
    def iterator():
        pass
    
    def containsAll(elements):
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def _init_():
        pass
    

class List:
    def _get_size_():
        pass
    
    def isEmpty():
        pass
    
    def contains(element):
        pass
    
    def iterator():
        pass
    
    def containsAll(elements):
        pass
    
    def get(index):
        pass
    
    def indexOf(element):
        pass
    
    def lastIndexOf(element):
        pass
    
    def listIterator():
        pass
    
    def listIterator(index):
        pass
    
    def subList(fromIndex, toIndex):
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def _init_():
        pass
    

class MutableList:
    def add(element):
        pass
    
    def remove(element):
        pass
    
    def addAll(elements):
        pass
    
    def addAll(index, elements):
        pass
    
    def removeAll(elements):
        pass
    
    def retainAll(elements):
        pass
    
    def clear():
        pass
    
    def set(index, element):
        pass
    
    def add(index, element):
        pass
    
    def removeAt(index):
        pass
    
    def listIterator():
        pass
    
    def listIterator(index):
        pass
    
    def subList(fromIndex, toIndex):
        pass
    
    def _get_size_():
        pass
    
    def isEmpty():
        pass
    
    def contains(element):
        pass
    
    def iterator():
        pass
    
    def containsAll(elements):
        pass
    
    def get(index):
        pass
    
    def indexOf(element):
        pass
    
    def lastIndexOf(element):
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def _init_():
        pass
    

class MutableCollection:
    def iterator():
        pass
    
    def add(element):
        pass
    
    def remove(element):
        pass
    
    def addAll(elements):
        pass
    
    def removeAll(elements):
        pass
    
    def retainAll(elements):
        pass
    
    def clear():
        pass
    
    def _get_size_():
        pass
    
    def isEmpty():
        pass
    
    def contains(element):
        pass
    
    def containsAll(elements):
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def _init_():
        pass
    

class MutableIterable:
    def iterator():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def _init_():
        pass
    

class Set:
    def _get_size_():
        pass
    
    def isEmpty():
        pass
    
    def contains(element):
        pass
    
    def iterator():
        pass
    
    def containsAll(elements):
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def _init_():
        pass
    

class Entry:
    def _get_key_():
        pass
    
    def _get_value_():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def _init_():
        pass
    

class Map:
    def _get_size_():
        pass
    
    def isEmpty():
        pass
    
    def containsKey(key):
        pass
    
    def containsValue(value):
        pass
    
    def get(key):
        pass
    
    def _get_keys_():
        pass
    
    def _get_values_():
        pass
    
    def _get_entries_():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def _init_():
        pass
    

class MutableSet:
    def iterator():
        pass
    
    def add(element):
        pass
    
    def remove(element):
        pass
    
    def addAll(elements):
        pass
    
    def removeAll(elements):
        pass
    
    def retainAll(elements):
        pass
    
    def clear():
        pass
    
    def _get_size_():
        pass
    
    def isEmpty():
        pass
    
    def contains(element):
        pass
    
    def containsAll(elements):
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def _init_():
        pass
    

class MutableEntry:
    def setValue(newValue):
        pass
    
    def _get_key_():
        pass
    
    def _get_value_():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def _init_():
        pass
    

class MutableMap:
    def put(key, value):
        pass
    
    def remove(key):
        pass
    
    def putAll(_from):
        pass
    
    def clear():
        pass
    
    def _get_keys_():
        pass
    
    def _get_values_():
        pass
    
    def _get_entries_():
        pass
    
    def _get_size_():
        pass
    
    def isEmpty():
        pass
    
    def containsKey(key):
        pass
    
    def containsValue(value):
        pass
    
    def get(key):
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    
    def _init_():
        pass
    

class Companion:
    def _init_():
        Companion_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_a5f5b96
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_51b75097 = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_41f968b0
    
    return Companion_instance

class Enum:
    def _init_(name, ordinal):
        Companion_getInstance()
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_13ae0ffd
        _this_.name = name
        _this_.ordinal = ordinal
    
    def _get_name_():
        return name
    
    def _get_ordinal_():
        return ordinal
    
    def compareTo(other):
        return compareTo(ordinal, ordinal)
    
    def compareTo(other):
        return compareTo(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_da1abd6)
    
    def equals(other):
        return jsEqeqeq(_this_, other)
    
    def hashCode():
        return identityHashCode(_this_)
    
    def toString():
        return name
    

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
    def _init_():
        DefaultConstructorMarker_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_4dbf902
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
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
    def _init_(_array):
        _this_._array = _array
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_249c96cf
        _this_.index = 0
    
    def _set_index_(_set___):
        _this_.index = _set___
    
    def _get_index_():
        return index
    
    def hasNext():
        return jsNot(jsEqeqeq(index, jsArrayLength(_array)))
    
    def next():
        tmp
        if jsNot(jsEqeqeq(index, jsArrayLength(_array))):
            tmp0_this = _this_
            tmp1 = index
            tmp0_this.index = jsBitOr(jsPlus(tmp1, 1), 0)
            tmp = jsArrayGet(_array, tmp1)
        
        if True:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_416dd4d8
        
        return tmp
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class _no_name_provided_:
    def _init_(_array):
        _this_._array = _array
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_40eb85e9
        _this_.index = 0
    
    def _set_index_(_set___):
        _this_.index = _set___
    
    def _get_index_():
        return index
    
    def hasNext():
        return jsNot(jsEqeqeq(index, jsArrayLength(_array)))
    
    def nextBoolean():
        tmp
        if jsNot(jsEqeqeq(index, jsArrayLength(_array))):
            tmp0_this = _this_
            tmp1 = index
            tmp0_this.index = jsBitOr(jsPlus(tmp1, 1), 0)
            tmp = jsArrayGet(_array, tmp1)
        
        if True:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_1de78f97
        
        return tmp
    
    def next():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class _no_name_provided_:
    def _init_(_array):
        _this_._array = _array
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_554f6e30
        _this_.index = 0
    
    def _set_index_(_set___):
        _this_.index = _set___
    
    def _get_index_():
        return index
    
    def hasNext():
        return jsNot(jsEqeqeq(index, jsArrayLength(_array)))
    
    def nextChar():
        tmp
        if jsNot(jsEqeqeq(index, jsArrayLength(_array))):
            tmp0_this = _this_
            tmp1 = index
            tmp0_this.index = jsBitOr(jsPlus(tmp1, 1), 0)
            tmp = jsArrayGet(_array, tmp1)
        
        if True:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_815e8e3
        
        return tmp
    
    def next():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class _no_name_provided_:
    def _init_(_array):
        _this_._array = _array
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_3a837f7
        _this_.index = 0
    
    def _set_index_(_set___):
        _this_.index = _set___
    
    def _get_index_():
        return index
    
    def hasNext():
        return jsNot(jsEqeqeq(index, jsArrayLength(_array)))
    
    def nextByte():
        tmp
        if jsNot(jsEqeqeq(index, jsArrayLength(_array))):
            tmp0_this = _this_
            tmp1 = index
            tmp0_this.index = jsBitOr(jsPlus(tmp1, 1), 0)
            tmp = jsArrayGet(_array, tmp1)
        
        if True:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_161138c8
        
        return tmp
    
    def next():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class _no_name_provided_:
    def _init_(_array):
        _this_._array = _array
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_4c006046
        _this_.index = 0
    
    def _set_index_(_set___):
        _this_.index = _set___
    
    def _get_index_():
        return index
    
    def hasNext():
        return jsNot(jsEqeqeq(index, jsArrayLength(_array)))
    
    def nextShort():
        tmp
        if jsNot(jsEqeqeq(index, jsArrayLength(_array))):
            tmp0_this = _this_
            tmp1 = index
            tmp0_this.index = jsBitOr(jsPlus(tmp1, 1), 0)
            tmp = jsArrayGet(_array, tmp1)
        
        if True:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_77ec911
        
        return tmp
    
    def next():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class _no_name_provided_:
    def _init_(_array):
        _this_._array = _array
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_5d7807b0
        _this_.index = 0
    
    def _set_index_(_set___):
        _this_.index = _set___
    
    def _get_index_():
        return index
    
    def hasNext():
        return jsNot(jsEqeqeq(index, jsArrayLength(_array)))
    
    def nextInt():
        tmp
        if jsNot(jsEqeqeq(index, jsArrayLength(_array))):
            tmp0_this = _this_
            tmp1 = index
            tmp0_this.index = jsBitOr(jsPlus(tmp1, 1), 0)
            tmp = jsArrayGet(_array, tmp1)
        
        if True:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_705606ac
        
        return tmp
    
    def next():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class _no_name_provided_:
    def _init_(_array):
        _this_._array = _array
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_3b07b706
        _this_.index = 0
    
    def _set_index_(_set___):
        _this_.index = _set___
    
    def _get_index_():
        return index
    
    def hasNext():
        return jsNot(jsEqeqeq(index, jsArrayLength(_array)))
    
    def nextFloat():
        tmp
        if jsNot(jsEqeqeq(index, jsArrayLength(_array))):
            tmp0_this = _this_
            tmp1 = index
            tmp0_this.index = jsBitOr(jsPlus(tmp1, 1), 0)
            tmp = jsArrayGet(_array, tmp1)
        
        if True:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_27af14bd
        
        return tmp
    
    def next():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class _no_name_provided_:
    def _init_(_array):
        _this_._array = _array
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_447522b4
        _this_.index = 0
    
    def _set_index_(_set___):
        _this_.index = _set___
    
    def _get_index_():
        return index
    
    def hasNext():
        return jsNot(jsEqeqeq(index, jsArrayLength(_array)))
    
    def nextLong():
        tmp
        if jsNot(jsEqeqeq(index, jsArrayLength(_array))):
            tmp0_this = _this_
            tmp1 = index
            tmp0_this.index = jsBitOr(jsPlus(tmp1, 1), 0)
            tmp = jsArrayGet(_array, tmp1)
        
        if True:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_1fb8b89e
        
        return tmp
    
    def next():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class _no_name_provided_:
    def _init_(_array):
        _this_._array = _array
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_77b987f3
        _this_.index = 0
    
    def _set_index_(_set___):
        _this_.index = _set___
    
    def _get_index_():
        return index
    
    def hasNext():
        return jsNot(jsEqeqeq(index, jsArrayLength(_array)))
    
    def nextDouble():
        tmp
        if jsNot(jsEqeqeq(index, jsArrayLength(_array))):
            tmp0_this = _this_
            tmp1 = index
            tmp0_this.index = jsBitOr(jsPlus(tmp1, 1), 0)
            tmp = jsArrayGet(_array, tmp1)
        
        if True:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_5d852761
        
        return tmp
    
    def next():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
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
    def _init_():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
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
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_4a0bc4cc
    
    def invoke(it):
        return toString(it)
    
    def invoke(p1):
        return invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6c37a904)
    

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
    def _init_():
        Companion_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_274d10aa
        _this_.MIN_VALUE = _init_(0, -2147483648)
        _this_.MAX_VALUE = _init_(-1, 2147483647)
        _this_.SIZE_BYTES = 8
        _this_.SIZE_BITS = 64
    
    def _get_MIN_VALUE_():
        return MIN_VALUE
    
    def _get_MAX_VALUE_():
        return MAX_VALUE
    
    def _get_SIZE_BYTES_():
        return SIZE_BYTES
    
    def _get_SIZE_BITS_():
        return SIZE_BITS
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_19d6bb0c = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_70ce5a0a
    
    return Companion_instance

class Long:
    def _init_(low, high):
        Companion_getInstance()
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_5a558335
        _this_.low = low
        _this_.high = high
    
    def _get_low_():
        return low
    
    def _get_high_():
        return high
    
    def compareTo(other):
        return compareTo(toLong(other))
    
    def compareTo(other):
        return compareTo(toLong(other))
    
    def compareTo(other):
        return compareTo(toLong(other))
    
    def compareTo(other):
        return compare(other)
    
    def compareTo(other):
        return compareTo(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_5071a1c5)
    
    def compareTo(other):
        return compareTo(toFloat(), other)
    
    def compareTo(other):
        return compareTo(toDouble(), other)
    
    def plus(other):
        return plus(toLong(other))
    
    def plus(other):
        return plus(toLong(other))
    
    def plus(other):
        return plus(toLong(other))
    
    def plus(other):
        return add(other)
    
    def plus(other):
        return jsPlus(toFloat(), other)
    
    def plus(other):
        return jsPlus(toDouble(), other)
    
    def minus(other):
        return minus(toLong(other))
    
    def minus(other):
        return minus(toLong(other))
    
    def minus(other):
        return minus(toLong(other))
    
    def minus(other):
        return subtract(other)
    
    def minus(other):
        return jsMinus(toFloat(), other)
    
    def minus(other):
        return jsMinus(toDouble(), other)
    
    def times(other):
        return times(toLong(other))
    
    def times(other):
        return times(toLong(other))
    
    def times(other):
        return times(toLong(other))
    
    def times(other):
        return multiply(other)
    
    def times(other):
        return jsMult(toFloat(), other)
    
    def times(other):
        return jsMult(toDouble(), other)
    
    def div(other):
        return div(toLong(other))
    
    def div(other):
        return div(toLong(other))
    
    def div(other):
        return div(toLong(other))
    
    def div(other):
        return divide(other)
    
    def div(other):
        return jsDiv(toFloat(), other)
    
    def div(other):
        return jsDiv(toDouble(), other)
    
    def rem(other):
        return rem(toLong(other))
    
    def rem(other):
        return rem(toLong(other))
    
    def rem(other):
        return rem(toLong(other))
    
    def rem(other):
        return modulo(other)
    
    def rem(other):
        return jsMod(toFloat(), other)
    
    def rem(other):
        return jsMod(toDouble(), other)
    
    def inc():
        return plus(_init_(1, 0))
    
    def dec():
        return minus(_init_(1, 0))
    
    def unaryPlus():
        return _this_
    
    def unaryMinus():
        return plus(_init_(1, 0))
    
    def rangeTo(other):
        return rangeTo(toLong(other))
    
    def rangeTo(other):
        return rangeTo(toLong(other))
    
    def rangeTo(other):
        return rangeTo(toLong(other))
    
    def rangeTo(other):
        return _init_(_this_, other)
    
    def shl(bitCount):
        return shiftLeft(bitCount)
    
    def shr(bitCount):
        return shiftRight(bitCount)
    
    def ushr(bitCount):
        return shiftRightUnsigned(bitCount)
    
    def _and(other):
        return _init_(jsBitAnd(low, low), jsBitAnd(high, high))
    
    def _or(other):
        return _init_(jsBitOr(low, low), jsBitOr(high, high))
    
    def xor(other):
        return _init_(jsBitXor(low, low), jsBitXor(high, high))
    
    def inv():
        return _init_(jsBitNot(low), jsBitNot(high))
    
    def toByte():
        return toByte(low)
    
    def toChar():
        return numberToChar(low)
    
    def toShort():
        return toShort(low)
    
    def toInt():
        return low
    
    def toLong():
        return _this_
    
    def toFloat():
        return kotlin_Float(toDouble())
    
    def toDouble():
        return toNumber()
    
    def valueOf():
        return toDouble()
    
    def equals(other):
        tmp
        if jsInstanceOf(other, jsClass()):
            tmp = equalsLong(kotlin_Long(other))
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def hashCode():
        return hashCode(_this_)
    
    def toString():
        return toStringImpl(10)
    

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
    _this.intercepted_ = _set___

def _get_intercepted__(_this):
    return intercepted_

def releaseIntercepted(_this):
    intercepted = intercepted_
    if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3ae8394:
        releaseInterceptedContinuation(intercepted)
    
    _this.intercepted_ = CompletedContinuation_getInstance()

class CoroutineImpl:
    def _init_(resultContinuation):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_3f937c0e
        _this_.resultContinuation = resultContinuation
        _this_.state = 0
        _this_.exceptionState = 0
        _this_.result = None
        _this_.exception = None
        _this_.finallyPath = None
        tmp = _this_
        tmp0_safe_receiver = resultContinuation
        tmp._context = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_60509848
        _this_.intercepted_ = None
    
    def _set_state_(_set___):
        _this_.state = _set___
    
    def _get_state_():
        return state
    
    def _set_exceptionState_(_set___):
        _this_.exceptionState = _set___
    
    def _get_exceptionState_():
        return exceptionState
    
    def _set_result_(_set___):
        _this_.result = _set___
    
    def _get_result_():
        return result
    
    def _set_exception_(_set___):
        _this_.exception = _set___
    
    def _get_exception_():
        return exception
    
    def _set_finallyPath_(_set___):
        _this_.finallyPath = _set___
    
    def _get_finallyPath_():
        return finallyPath
    
    def _get_context_():
        return ensureNotNull(_context)
    
    def intercepted():
        tmp2_elvis_lhs = intercepted_
        tmp
        if jsEqeq(tmp2_elvis_lhs, None):
            tmp0_safe_receiver = get(Key_getInstance())
            tmp1_elvis_lhs = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_5c6d1a38
            tmp0_also_0 = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_27c5fba0
            _this_.intercepted_ = tmp0_also_0
            tmp = tmp0_also_0
        
        if True:
            tmp = tmp2_elvis_lhs
        
        return tmp
    
    def resumeWith(result):
        current = _this_
        tmp
        if _Result___get_isFailure__impl_(result):
            tmp = None
        
        if True:
            tmp = _Result___get_value__impl_(result)
            tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_30183725
        
        currentResult = tmp
        currentException = Result__exceptionOrNull_impl(result)
        while True:
            tmp0_with_0 = current
            if jsEqeq(currentException, None):
                tmp0_with_0.result = currentResult
            
            if True:
                tmp0_with_0.state = exceptionState
                tmp0_with_0.exception = currentException
            
            visitTry_org_jetbrains_kotlin_ir_expressions_impl_IrTryImpl_f23b785
            releaseIntercepted(tmp0_with_0)
            completion_4 = ensureNotNull(resultContinuation)
            if jsInstanceOf(completion_4, jsClass()):
                current = kotlin_coroutines_CoroutineImpl(completion_4)
            
            if True:
                if True:
                    if jsNot(jsEqeq(currentException, None)):
                        tmp0_resumeWithException_0_5 = ensureNotNull(currentException)
                        tmp0_failure_0_1_6 = Companion_getInstance()
                        resumeWith(_init_(createFailure(tmp0_resumeWithException_0_5)))
                    
                    if True:
                        tmp1_resume_0_7 = currentResult
                        tmp0_success_0_1_8 = Companion_getInstance()
                        resumeWith(_init_(tmp1_resume_0_7))
                    
                    return Unit_getInstance()
                
            
        
    
    def resumeWith(result):
        return resumeWith(result)
    
    def doResume():
        pass
    
    def create(completion):
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_a0c027a
    
    def create(value, completion):
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_1f878eed
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def toString():
        pass
    

class CompletedContinuation:
    def _init_():
        CompletedContinuation_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_3815c525
    
    def _get_context_():
        tmp0_error_0 = 'This continuation is already complete'
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_5c181a62
    
    def resumeWith(result):
        tmp0_error_0 = 'This continuation is already complete'
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_395272b8
    
    def resumeWith(result):
        return resumeWith(result)
    
    def toString():
        return 'This continuation is already complete'
    
    def equals(other):
        pass
    
    def hashCode():
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
    def _get_message_():
        pass
    
    def _get_cause_():
        pass
    
    def toString():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def _init_():
        captureStack(_this_, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_7537f673)
    

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
    def _get_message_():
        pass
    
    def _get_cause_():
        pass
    
    def toString():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def _init_():
        captureStack(_this_, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_7b2196d4)
    

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
    def _get_message_():
        pass
    
    def _get_cause_():
        pass
    
    def toString():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def _init_():
        captureStack(_this_, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_42ad9160)
    

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
    def _get_message_():
        pass
    
    def _get_cause_():
        pass
    
    def toString():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def _init_():
        captureStack(_this_, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_145a0fd0)
    

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
    def _get_message_():
        pass
    
    def _get_cause_():
        pass
    
    def toString():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def _init_():
        captureStack(_this_, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_21302fe7)
    

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
    def _get_message_():
        pass
    
    def _get_cause_():
        pass
    
    def toString():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def _init_():
        captureStack(_this_, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_68e9c1d8)
    

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
    def _get_message_():
        pass
    
    def _get_cause_():
        pass
    
    def toString():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def _init_():
        captureStack(_this_, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_7b21879f)
    

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
    def _get_message_():
        pass
    
    def _get_cause_():
        pass
    
    def toString():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def _init_():
        captureStack(_this_, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_5706f658)
    

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
    def _get_message_():
        pass
    
    def _get_cause_():
        pass
    
    def toString():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def _init_():
        captureStack(_this_, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_3472f880)
    

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
    def _get_message_():
        pass
    
    def _get_cause_():
        pass
    
    def toString():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def _init_():
        captureStack(_this_, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_6cb48bf4)
    

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
    def _get_message_():
        pass
    
    def _get_cause_():
        pass
    
    def toString():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def _init_():
        captureStack(_this_, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_2ed33e81)
    

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
    def _get_message_():
        pass
    
    def _get_cause_():
        pass
    
    def toString():
        pass
    
    def equals(other):
        pass
    
    def hashCode():
        pass
    
    def _init_():
        captureStack(_this_, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_61ffe4cf)
    

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
