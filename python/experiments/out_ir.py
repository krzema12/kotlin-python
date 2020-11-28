def fold(initial, operation):
    accumulator = initial
    indexedObject = _this_
    inductionVariable = 0
    last = jsArrayLength(indexedObject)
    while jsLt(inductionVariable, last):
        element = jsArrayGet(indexedObject, inductionVariable)
        inductionVariable = jsBitOr(jsPlus(inductionVariable, 1), 0)
        accumulator = operation.invoke(accumulator, element)
    
    return accumulator

def _get_indices_():
    return IntRange(0, _get_lastIndex_())

def indexOf(element):
    if jsEqeq(element, None):
        inductionVariable = 0
        last = jsBitOr(jsMinus(jsArrayLength(_this_), 1), 0)
        if jsLtEq(inductionVariable, last):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_cf39749
        
    
    if True:
        inductionVariable = 0
        last = jsBitOr(jsMinus(jsArrayLength(_this_), 1), 0)
        if jsLtEq(inductionVariable, last):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_257a59c
        
    
    return -1

def lastIndexOf(element):
    if jsEqeq(element, None):
        inductionVariable = jsBitOr(jsMinus(jsArrayLength(_this_), 1), 0)
        if jsLtEq(0, inductionVariable):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_296a6a10
        
    
    if True:
        inductionVariable = jsBitOr(jsMinus(jsArrayLength(_this_), 1), 0)
        if jsLtEq(0, inductionVariable):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_77d68b94
        
    
    return -1

def _get_lastIndex_():
    return jsBitOr(jsMinus(jsArrayLength(_this_), 1), 0)

def joinToString(separator, prefix, postfix, limit, truncated, transform):
    return joinTo(StringBuilder_init__Create_(), separator, prefix, postfix, limit, truncated, transform).toString()

def joinToString_default(separator, prefix, postfix, limit, truncated, transform, _mask0, _handler):
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 1), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_12bc9450
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 2), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_58ea2bc2
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 4), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_8179cad
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 8), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_152f96e5
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 16), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_493d8aa7
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 32), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_36173114
    
    return joinToString(kotlin_CharSequence(separator), kotlin_CharSequence(prefix), kotlin_CharSequence(postfix), limit, kotlin_CharSequence(truncated), transform)

def joinTo(buffer, separator, prefix, postfix, limit, truncated, transform):
    buffer.append(prefix)
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
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_64b05928
        
        if True:
            pass
        
        if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_22251bb2:
            appendElement(element, transform)
        
        if True:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrBreakImpl_8ee1404
        
    
    if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_7155dce8:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_1313d0b3
    
    buffer.append(postfix)
    Unit_getInstance()
    return buffer

def joinTo_default(buffer, separator, prefix, postfix, limit, truncated, transform, _mask0, _handler):
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 2), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_320aecd3
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 4), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_18cc07ca
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 8), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_2aa93f15
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 16), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_bc9cd27
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 32), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_7316742f
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 64), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_3ce7a0d1
    
    return joinTo(buffer, kotlin_CharSequence(separator), kotlin_CharSequence(prefix), kotlin_CharSequence(postfix), limit, kotlin_CharSequence(truncated), transform)

def contains(element):
    return jsGtEq(indexOf(element), 0)

def indexOf(element):
    inductionVariable = 0
    last = jsBitOr(jsMinus(jsArrayLength(_this_), 1), 0)
    if jsLtEq(inductionVariable, last):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_25db5479
    
    return -1

def _get_indices_():
    return IntRange(0, _get_lastIndex_())

def _get_lastIndex_():
    return jsBitOr(jsMinus(jsArrayLength(_this_), 1), 0)

def contains(element):
    return jsGtEq(indexOf(element), 0)

def indexOf(element):
    inductionVariable = 0
    last = jsBitOr(jsMinus(jsArrayLength(_this_), 1), 0)
    if jsLtEq(inductionVariable, last):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_77d5a3ee
    
    return -1

def _get_indices_():
    return IntRange(0, _get_lastIndex_())

def _get_lastIndex_():
    return jsBitOr(jsMinus(jsArrayLength(_this_), 1), 0)

def contains(element):
    return jsGtEq(indexOf(element), 0)

def indexOf(element):
    inductionVariable = 0
    last = jsBitOr(jsMinus(jsArrayLength(_this_), 1), 0)
    if jsLtEq(inductionVariable, last):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_94af25
    
    return -1

def _get_indices_():
    return IntRange(0, _get_lastIndex_())

def _get_lastIndex_():
    return jsBitOr(jsMinus(jsArrayLength(_this_), 1), 0)

def contains(element):
    return jsGtEq(indexOf(element), 0)

def indexOf(element):
    inductionVariable = 0
    last = jsBitOr(jsMinus(jsArrayLength(_this_), 1), 0)
    if jsLtEq(inductionVariable, last):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_4f8aa5fe
    
    return -1

def _get_indices_():
    return IntRange(0, _get_lastIndex_())

def _get_lastIndex_():
    return jsBitOr(jsMinus(jsArrayLength(_this_), 1), 0)

def indexOfFirst(predicate):
    index = 0
    tmp0_iterator = _this_.iterator()
    while tmp0_iterator.hasNext():
        item = tmp0_iterator.next()
        if predicate.invoke(item):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_241b5364
        
        tmp1 = index
        index = jsBitOr(jsPlus(tmp1, 1), 0)
        Unit_getInstance()
    
    return -1

def indexOfLast(predicate):
    iterator = _this_.listIterator(_this_._get_size_())
    while iterator.hasPrevious():
        if predicate.invoke(iterator.previous()):
            return iterator.nextIndex()
        
    
    return -1

def any(predicate):
    tmp
    if isInterface(_this_, jsClass()):
        tmp = kotlin_collections_Collection_T_(_this_).isEmpty()
    
    if True:
        if True:
            tmp = False
        
    
    if tmp:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_35b1e5e5
    
    if True:
        pass
    
    tmp0_iterator = _this_.iterator()
    while tmp0_iterator.hasNext():
        element = tmp0_iterator.next()
        if predicate.invoke(element):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_38b65eb9
        
    
    return False

def all(predicate):
    tmp
    if isInterface(_this_, jsClass()):
        tmp = kotlin_collections_Collection_T_(_this_).isEmpty()
    
    if True:
        if True:
            tmp = False
        
    
    if tmp:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_704a0f9
    
    if True:
        pass
    
    tmp0_iterator = _this_.iterator()
    while tmp0_iterator.hasNext():
        element = tmp0_iterator.next()
        if jsNot(predicate.invoke(element)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_6add626f
        
    
    return True

def joinToString(separator, prefix, postfix, limit, truncated, transform):
    return joinTo(StringBuilder_init__Create_(), separator, prefix, postfix, limit, truncated, transform).toString()

def joinToString_default(separator, prefix, postfix, limit, truncated, transform, _mask0, _handler):
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 1), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_6d0937e
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 2), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_74a89061
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 4), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_3e7de165
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 8), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_167eab4
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 16), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_2280c0f5
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 32), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_76cb6d16
    
    return joinToString(kotlin_CharSequence(separator), kotlin_CharSequence(prefix), kotlin_CharSequence(postfix), limit, kotlin_CharSequence(truncated), transform)

def joinTo(buffer, separator, prefix, postfix, limit, truncated, transform):
    buffer.append(prefix)
    Unit_getInstance()
    count = 0
    tmp0_iterator = _this_.iterator()
    while tmp0_iterator.hasNext():
        element = tmp0_iterator.next()
        count = jsBitOr(jsPlus(count, 1), 0)
        if jsGt(count, 1):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_398c2298
        
        if True:
            pass
        
        if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_964a7b0:
            appendElement(element, transform)
        
        if True:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrBreakImpl_4d84688f
        
    
    if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_559ac87f:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_7a9ad451
    
    buffer.append(postfix)
    Unit_getInstance()
    return buffer

def joinTo_default(buffer, separator, prefix, postfix, limit, truncated, transform, _mask0, _handler):
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 2), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_2b360641
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 4), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_3729cdaf
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 8), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_6549ac6d
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 16), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_25a8ff84
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 32), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_2181e6b6
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 64), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_1dbecb0a
    
    return joinTo(buffer, kotlin_CharSequence(separator), kotlin_CharSequence(prefix), kotlin_CharSequence(postfix), limit, kotlin_CharSequence(truncated), transform)

def downTo(to):
    return Companion_getInstance().fromClosedRange(_this_, to, -1)

def until(to):
    if jsLtEq(to, MIN_VALUE):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_6a7ea7c
    
    return numberRangeToNumber(_this_, kotlin_Int(jsBitOr(jsMinus(to, 1), 0)))

def reversed():
    return Companion_getInstance().fromClosedRange(last, first, jsBitOr(jsUnaryMinus(step), 0))

def getOrElse(index, defaultValue):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_796a1cd1

def KotlinNothingValueException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_1465d125
    return _this

def KotlinNothingValueException_init__Create_():
    tmp = KotlinNothingValueException_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_3460165f)
    return tmp

def KotlinNothingValueException_init__Init_(message, _this):
    RuntimeException_init__Init_(message, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_2a67ed1f
    return _this

def KotlinNothingValueException_init__Create_(message):
    tmp = KotlinNothingValueException_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_1eeae9d)
    return tmp

def KotlinNothingValueException_init__Init_(message, cause, _this):
    RuntimeException_init__Init_(message, cause, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_21def2c
    return _this

def KotlinNothingValueException_init__Create_(message, cause):
    tmp = KotlinNothingValueException_init__Init_(message, cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_3c72031c)
    return tmp

def KotlinNothingValueException_init__Init_(cause, _this):
    RuntimeException_init__Init_(cause, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_7a977d23
    return _this

def KotlinNothingValueException_init__Create_(cause):
    tmp = KotlinNothingValueException_init__Init_(cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_6ebdbe96)
    return tmp

class KotlinNothingValueException:
    def _get_message_(self):
        pass
    
    def _get_cause_(self):
        pass
    
    def toString(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def _init_():
        captureStack(_this_, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_15d67d0f)
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_60a64104 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_12ceff30 = 0
def values():
    return arrayLiteral(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_5f016147)

def valueOf(value):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_e64ee56

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_65b75087 = 0
def Level_initEntries():
    if Level_entriesInitialized:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_5e0c445f
    
    Level_entriesInitialized = True
    Level_WARNING_instance = Level('WARNING', 0)
    Level_ERROR_instance = Level('ERROR', 1)

def Experimental_init__Init_(level, _mask0, _marker, _this):
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 1), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_781ebe48
    
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_3342ec79
    return _this

def Experimental_init__Create_(level, _mask0, _marker):
    return Experimental_init__Init_(level, _mask0, _marker, Object_create())

class Level:
    def _init_(name, ordinal):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_21da6808
    
    def _get_name_(self):
        pass
    
    def _get_ordinal_(self):
        pass
    
    def compareTo(self, other):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
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
    
    def _get_level_(self):
        return level
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class WasExperimental:
    def _init_(markerClass):
        _this_.markerClass = markerClass
    
    def _get_markerClass_(self):
        return markerClass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class ExperimentalStdlibApi:
    def _init_():
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class OptionalExpectation:
    def _init_():
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class ExperimentalMultiplatform:
    def _init_():
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_16e2a7be = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_7e915daa = 0
def values():
    return arrayLiteral(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_1e6f7127)

def valueOf(value):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_60cd2b02

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_3b5cf4c6 = 0
def Level_initEntries():
    if Level_entriesInitialized:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_4e7d1e2
    
    Level_entriesInitialized = True
    Level_WARNING_instance = Level('WARNING', 0)
    Level_ERROR_instance = Level('ERROR', 1)

def RequiresOptIn_init__Init_(message, level, _mask0, _marker, _this):
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 1), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_20677bc2
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 2), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_310d05c5
    
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_64746794
    return _this

def RequiresOptIn_init__Create_(message, level, _mask0, _marker):
    return RequiresOptIn_init__Init_(message, level, _mask0, _marker, Object_create())

class Level:
    def _init_(name, ordinal):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_59463bab
    
    def _get_name_(self):
        pass
    
    def _get_ordinal_(self):
        pass
    
    def compareTo(self, other):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
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
    
    def _get_message_(self):
        return message
    
    def _get_level_(self):
        return level
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class OptIn:
    def _init_(markerClass):
        _this_.markerClass = markerClass
    
    def _get_markerClass_(self):
        return markerClass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class _no_name_provided_:
    def _init_(this_0):
        _this_.this_0 = this_0
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_346c568d
    
    def invoke(self, it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3c9b416a
    
    def invoke(self, p1):
        return _this_.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2de0f3e3)
    

class AbstractCollection:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_66e62fc4
    
    def _get_size_(self):
        pass
    
    def iterator(self):
        pass
    
    def contains(self, element):
        tmp_ret_0
        visitDoWhileLoop_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_7b29d791
        return tmp_ret_0
    
    def containsAll(self, elements):
        tmp_ret_0
        visitDoWhileLoop_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_754c6edb
        return tmp_ret_0
    
    def isEmpty(self):
        return jsEqeqeq(_this_._get_size_(), 0)
    
    def toString(self):
        return joinToString_default(', ', '[', ']', 0, None, _no_name_provided__factory(_this_), 24, None)
    
    def toArray(self):
        return copyToArrayImpl(_this_)
    
    def toArray(self, array):
        return copyToArrayImpl(_this_, array)
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    

def _no_name_provided__factory(this_0):
    i = _no_name_provided_(this_0)
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_32f3174d

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
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_74cff17c
        _this_.list = list
        _this_.fromIndex = fromIndex
        _this_._size = 0
        Companion_getInstance().checkRangeIndexes(fromIndex, toIndex, list._get_size_())
        _this_._size = jsBitOr(jsMinus(toIndex, fromIndex), 0)
    
    def get(self, index):
        Companion_getInstance().checkElementIndex(index, _size)
        return list.get(jsBitOr(jsPlus(fromIndex, index), 0))
    
    def _get_size_(self):
        return _size
    
    def toArray(self):
        pass
    
    def toArray(self, array):
        pass
    
    def contains(self, element):
        pass
    
    def containsAll(self, elements):
        pass
    
    def indexOf(self, element):
        pass
    
    def isEmpty(self):
        pass
    
    def iterator(self):
        pass
    
    def lastIndexOf(self, element):
        pass
    
    def listIterator(self):
        pass
    
    def listIterator(self, index):
        pass
    
    def subList(self, fromIndex, toIndex):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class IteratorImpl:
    def _init_(_outer):
        _this_._this = _outer
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_8aa1562
        _this_.index = 0
    
    def _set_index_(self, _set___):
        _this_.index = _set___
    
    def _get_index_(self):
        return index
    
    def hasNext(self):
        return jsLt(index, _this._get_size_())
    
    def next(self):
        if jsNot(_this_.hasNext()):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_5186c801
        
        tmp0_this = _this_
        tmp1 = index
        tmp0_this.index = jsBitOr(jsPlus(tmp1, 1), 0)
        return _this.get(tmp1)
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class ListIteratorImpl:
    def _init_(_outer, index):
        _this_._this = _outer
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_153d5d5b
        Companion_getInstance().checkPositionIndex(index, _this._get_size_())
        _this_._set_index_(index)
    
    def hasPrevious(self):
        return jsGt(_this_._get_index_(), 0)
    
    def nextIndex(self):
        return _this_._get_index_()
    
    def previous(self):
        if jsNot(_this_.hasPrevious()):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_ea45a5b
        
        tmp0_this = _this_
        tmp0_this._set_index_(jsBitOr(jsMinus(tmp0_this._get_index_(), 1), 0))
        return _this.get(tmp0_this._get_index_())
    
    def previousIndex(self):
        return jsBitOr(jsMinus(_this_._get_index_(), 1), 0)
    
    def _set_index_(self, _set___):
        pass
    
    def _get_index_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hasNext(self):
        pass
    
    def hashCode(self):
        pass
    
    def next(self):
        pass
    
    def toString(self):
        pass
    

class Companion:
    def _init_():
        Companion_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_10e4cc6
    
    def checkElementIndex(self, index, size):
        if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6a377a:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_6b6606d1
        
    
    def checkPositionIndex(self, index, size):
        if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_1b06e304:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_8b1bfdf
        
    
    def checkRangeIndexes(self, fromIndex, toIndex, size):
        if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_536e5b21:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_7dfab58d
        
        if jsGt(fromIndex, toIndex):
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_282240
        
    
    def checkBoundsIndexes(self, startIndex, endIndex, size):
        if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_52e7bed1:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_675bf541
        
        if jsGt(startIndex, endIndex):
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_60e5eed0
        
    
    def orderedHashCode(self, c):
        hashCode = 1
        tmp0_iterator = c.iterator()
        while tmp0_iterator.hasNext():
            e = tmp0_iterator.next()
            tmp = imul(31, hashCode)
            tmp1_safe_receiver = e
            tmp2_elvis_lhs = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_7855167a
            hashCode = jsBitOr(jsPlus(tmp, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_5a930c03), 0)
        
        return hashCode
    
    def orderedEquals(self, c, other):
        if jsNot(jsEqeqeq(c._get_size_(), other._get_size_())):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_634d3439
        
        otherIterator = other.iterator()
        tmp0_iterator = c.iterator()
        while tmp0_iterator.hasNext():
            elem = tmp0_iterator.next()
            elemOther = otherIterator.next()
            if jsNot(equals(elem, elemOther)):
                return False
            
        
        return True
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_419c537 = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_9129682
    
    return Companion_instance

class AbstractList:
    def _init_():
        Companion_getInstance()
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_61aa6300
    
    def _get_size_(self):
        pass
    
    def get(self, index):
        pass
    
    def iterator(self):
        return IteratorImpl(_this_)
    
    def indexOf(self, element):
        tmp_ret_0
        visitDoWhileLoop_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_4a9e4be7
        return tmp_ret_0
    
    def lastIndexOf(self, element):
        tmp_ret_0
        visitDoWhileLoop_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_75f27234
        return tmp_ret_0
    
    def listIterator(self):
        return ListIteratorImpl(_this_, 0)
    
    def listIterator(self, index):
        return ListIteratorImpl(_this_, index)
    
    def subList(self, fromIndex, toIndex):
        return SubList(_this_, fromIndex, toIndex)
    
    def equals(self, other):
        if jsEqeqeq(other, _this_):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_4a29a1e6
        
        if jsNot(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_1f4c8062):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_34e53c02
        
        if True:
            pass
        
        return Companion_getInstance().orderedEquals(_this_, kotlin_collections_Collection___(other))
    
    def hashCode(self):
        return Companion_getInstance().orderedHashCode(_this_)
    
    def contains(self, element):
        pass
    
    def containsAll(self, elements):
        pass
    
    def isEmpty(self):
        pass
    
    def toString(self):
        pass
    
    def toArray(self):
        pass
    
    def toArray(self, array):
        pass
    

def listOf(elements):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_517fd762

def emptyList():
    return EmptyList_getInstance()

def _get_serialVersionUID_(_this):
    return serialVersionUID

def readResolve(_this):
    return EmptyList_getInstance()

class EmptyList:
    def _init_():
        EmptyList_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_6e22d6bf
        _this_.serialVersionUID = Long(-1478467534, -1720727600)
    
    def equals(self, other):
        tmp
        if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_1235abb2:
            tmp = kotlin_collections_List_kotlin_Any__(other).isEmpty()
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def hashCode(self):
        return 1
    
    def toString(self):
        return '[]'
    
    def _get_size_(self):
        return 0
    
    def isEmpty(self):
        return True
    
    def contains(self, element):
        return False
    
    def contains(self, element):
        if jsNot(False):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_61a098fa
        
        if True:
            pass
        
        tmp
        if False:
            tmp = kotlin_Nothing(element)
        
        if True:
            if True:
                tmp = THROW_CCE()
            
        
        return _this_.contains(tmp)
    
    def containsAll(self, elements):
        return elements.isEmpty()
    
    def containsAll(self, elements):
        return _this_.containsAll(elements)
    
    def get(self, index):
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_25dc2c0
    
    def indexOf(self, element):
        return -1
    
    def indexOf(self, element):
        if jsNot(False):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_4b8816f7
        
        if True:
            pass
        
        tmp
        if False:
            tmp = kotlin_Nothing(element)
        
        if True:
            if True:
                tmp = THROW_CCE()
            
        
        return _this_.indexOf(tmp)
    
    def lastIndexOf(self, element):
        return -1
    
    def lastIndexOf(self, element):
        if jsNot(False):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_42e0f71e
        
        if True:
            pass
        
        tmp
        if False:
            tmp = kotlin_Nothing(element)
        
        if True:
            if True:
                tmp = THROW_CCE()
            
        
        return _this_.lastIndexOf(tmp)
    
    def iterator(self):
        return EmptyIterator_getInstance()
    
    def listIterator(self):
        return EmptyIterator_getInstance()
    
    def listIterator(self, index):
        if jsNot(jsEqeqeq(index, 0)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_4601a148
        
        return EmptyIterator_getInstance()
    
    def subList(self, fromIndex, toIndex):
        if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_11326597:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_618e7761
        
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_34f8ce89
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_72dfac2e = 0
def EmptyList_getInstance():
    if jsEqeq(EmptyList_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_2acacb1
    
    return EmptyList_instance

class EmptyIterator:
    def _init_():
        EmptyIterator_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_41948c13
    
    def hasNext(self):
        return False
    
    def hasPrevious(self):
        return False
    
    def nextIndex(self):
        return 0
    
    def previousIndex(self):
        return -1
    
    def next(self):
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_18301763
    
    def previous(self):
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_29c21acb
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_6566da90 = 0
def EmptyIterator_getInstance():
    if jsEqeq(EmptyIterator_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_74d3c448
    
    return EmptyIterator_instance

def _get_lastIndex_():
    return jsBitOr(jsMinus(_this_._get_size_(), 1), 0)

def removeAll(predicate):
    return filterInPlace(predicate, True)

def removeAll(predicate):
    return filterInPlace(predicate, True)

def filterInPlace(predicate, predicateResultToRemove):
    if jsNot(isInterface(_this_, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_73d0dbbf
    
    if True:
        pass
    
    writeIndex = 0
    inductionVariable = 0
    last = _get_lastIndex_()
    if jsLtEq(inductionVariable, last):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_30dd9615
    
    if jsLt(writeIndex, _this_._get_size_()):
        inductionVariable = _get_lastIndex_()
        if jsLtEq(writeIndex, inductionVariable):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_11c885a6
        
        return True
    
    if True:
        return False
    

def filterInPlace(predicate, predicateResultToRemove):
    result = False
    tmp0_with_0 = _this_.iterator()
    while tmp0_with_0.hasNext():
        if jsEqeqeq(predicate.invoke(tmp0_with_0.next()), predicateResultToRemove):
            tmp0_with_0.remove()
            result = True
        
    
    return result

class Sequence:
    def iterator(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def _init_():
        pass
    

def contract(builder):
    pass

class ContractBuilder:
    def returns(self):
        pass
    
    def returns(self, value):
        pass
    
    def returnsNotNull(self):
        pass
    
    def callsInPlace(self, _lambda, kind):
        pass
    
    def callsInPlace_default(self, _lambda, kind, _mask0, _handler):
        if jsNot(jsEqeqeq(jsBitAnd(_mask0, 2), 0)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_37058d66
        
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_610f3f1b
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def _init_():
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_64a768e7 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_26ed4e27 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_413e4756 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_68dc6497 = 0
def values():
    return arrayLiteral(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_4377e40a)

def valueOf(value):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_38be950e

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_5f4ddd09 = 0
def InvocationKind_initEntries():
    if InvocationKind_entriesInitialized:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_7370f35b
    
    InvocationKind_entriesInitialized = True
    InvocationKind_AT_MOST_ONCE_instance = InvocationKind('AT_MOST_ONCE', 0)
    InvocationKind_AT_LEAST_ONCE_instance = InvocationKind('AT_LEAST_ONCE', 1)
    InvocationKind_EXACTLY_ONCE_instance = InvocationKind('EXACTLY_ONCE', 2)
    InvocationKind_UNKNOWN_instance = InvocationKind('UNKNOWN', 3)

class InvocationKind:
    def _init_(name, ordinal):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_1e9b9276
    
    def _get_name_(self):
        pass
    
    def _get_ordinal_(self):
        pass
    
    def compareTo(self, other):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class ExperimentalContracts:
    def _init_():
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
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
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def _init_():
        pass
    

class Returns:
    def implies(self, booleanExpression):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def _init_():
        pass
    

class ReturnsNotNull:
    def implies(self, booleanExpression):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def _init_():
        pass
    

class Effect:
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def _init_():
        pass
    

class SimpleEffect:
    def implies(self, booleanExpression):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def _init_():
        pass
    

class ConditionalEffect:
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def _init_():
        pass
    

class Continuation:
    def _get_context_(self):
        pass
    
    def resumeWith(self, result):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def _init_():
        pass
    

def Continuation(context, resumeWith):
    return _no_name_provided_(context, resumeWith)

def resumeWithException(exception):
    tmp0_failure_0 = Companion_getInstance()
    return _this_.resumeWith(Result(createFailure(exception)))

def resume(value):
    tmp0_success_0 = Companion_getInstance()
    return _this_.resumeWith(Result(value))

def _get_coroutineContext_():
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_14fd1bc

class _no_name_provided_:
    def _init_(_context, _resumeWith):
        _this_._context = _context
        _this_._resumeWith = _resumeWith
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_483381ea
    
    def _get_context_(self):
        return _context
    
    def resumeWith(self, result):
        return _resumeWith.invoke(boxIntrinsic(result))
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class Key:
    def _init_():
        Key_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_4440750
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_78e1625f = 0
def Key_getInstance():
    if jsEqeq(Key_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_2ee3549e
    
    return Key_instance

class ContinuationInterceptor:
    def interceptContinuation(self, continuation):
        pass
    
    def releaseInterceptedContinuation(self, continuation):
        pass
    
    def get(self, key):
        if jsInstanceOf(key, jsClass()):
            tmp
            if kotlin_coroutines_AbstractCoroutineContextKey_out_kotlin_coroutines_Element_out_kotlin_coroutines_Element_(key).isSubKey(_this_._get_key_()):
                tmp = kotlin_coroutines_AbstractCoroutineContextKey_out_kotlin_coroutines_Element_out_kotlin_coroutines_Element_(key).tryCast(_this_)
                tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3d91d937
            
            if True:
                tmp = None
            
            return tmp
        
        if True:
            pass
        
        tmp
        if jsEqeqeq(Key_getInstance(), key):
            tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_180e1754
        
        if True:
            tmp = None
        
        return tmp
    
    def minusKey(self, key):
        if jsInstanceOf(key, jsClass()):
            return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_5cf24f99
        
        if True:
            pass
        
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_485fe2cd
    
    def _get_key_(self):
        pass
    
    def fold(self, initial, operation):
        pass
    
    def plus(self, context):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def _init_():
        Key_getInstance()
    

class Key:
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def _init_():
        pass
    

class Element:
    def _get_key_(self):
        pass
    
    def get(self, key):
        tmp
        if equals(_this_._get_key_(), key):
            tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_751d9a40
        
        if True:
            tmp = None
        
        return tmp
    
    def fold(self, initial, operation):
        return operation.invoke(initial, _this_)
    
    def minusKey(self, key):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_1e060d4b
    
    def plus(self, context):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def _init_():
        pass
    

class _no_name_provided_:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_55c9400d
    
    def invoke(self, acc, element):
        removed = acc.minusKey(element._get_key_())
        tmp
        if jsEqeqeq(removed, EmptyCoroutineContext_getInstance()):
            tmp = element
        
        if True:
            interceptor = removed.get(Key_getInstance())
            tmp
            if jsEqeq(interceptor, None):
                tmp = CombinedContext(removed, element)
            
            if True:
                left = removed.minusKey(Key_getInstance())
                tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_65d07158
            
            tmp = tmp
        
        return tmp
    
    def invoke(self, p1, p2):
        tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2300d6fd
        return _this_.invoke(tmp, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_5e86dc1c)
    

class CoroutineContext:
    def get(self, key):
        pass
    
    def fold(self, initial, operation):
        pass
    
    def plus(self, context):
        tmp
        if jsEqeqeq(context, EmptyCoroutineContext_getInstance()):
            tmp = _this_
        
        if True:
            tmp = context.fold(_this_, _no_name_provided__factory())
        
        return tmp
    
    def minusKey(self, key):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def _init_():
        pass
    

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_79527eb9

def _get_serialVersionUID_(_this):
    return serialVersionUID

def readResolve(_this):
    return EmptyCoroutineContext_getInstance()

class EmptyCoroutineContext:
    def _init_():
        EmptyCoroutineContext_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_77acc95a
        _this_.serialVersionUID = Long(0, 0)
    
    def get(self, key):
        return None
    
    def fold(self, initial, operation):
        return initial
    
    def plus(self, context):
        return context
    
    def minusKey(self, key):
        return _this_
    
    def hashCode(self):
        return 0
    
    def toString(self):
        return 'EmptyCoroutineContext'
    
    def equals(self, other):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_4ddb882 = 0
def EmptyCoroutineContext_getInstance():
    if jsEqeq(EmptyCoroutineContext_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_4334aa1b
    
    return EmptyCoroutineContext_instance

def _get_serialVersionUID_(_this):
    return serialVersionUID

class Companion:
    def _init_():
        Companion_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_7983a5d5
        _this_.serialVersionUID = Long(0, 0)
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_12326ccb = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_43188555
    
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
        accumulator_1 = accumulator_1.plus(element_3)
    
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
        tmp0_elvis_lhs = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_f9a82ac
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
    return equals(_this.get(element._get_key_()), element)

def containsAll(_this, context):
    cur = context
    while True:
        if jsNot(contains(_this, element)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_ab58ff
        
        next = left
        if jsInstanceOf(next, jsClass()):
            cur = kotlin_coroutines_CombinedContext(next)
        
        if True:
            if True:
                return contains(_this, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_576c8cea)
            
        
    

def writeReplace(_this):
    n = size(_this)
    elements = fillArrayVal(Array(n), None)
    index = _sharedBox_create(0)
    _this.fold(Unit_getInstance(), _no_name_provided__factory(elements, index))
    tmp0_check_0 = jsEqeqeq(_sharedBox_read(index), n)
    if jsNot(tmp0_check_0):
        message_2 = 'Check failed.'
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_1e20dad5
    
    return Serialized(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_349247c9)

class Serialized:
    def _init_(elements):
        Companion_getInstance()
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_6e466fdf
        _this_.elements = elements
    
    def _get_elements_(self):
        return elements
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class _no_name_provided_:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_3ff4ed56
    
    def invoke(self, acc, element):
        tmp
        if jsEqeqeq(charSequenceLength(acc), 0):
            tmp = toString(element)
        
        if True:
            if True:
                tmp = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_32dbf42
            
        
        return tmp
    
    def invoke(self, p1, p2):
        tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_22aeac34
        return _this_.invoke(tmp, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_77e55368)
    

class _no_name_provided_:
    def _init_(_elements, _index):
        _this_._elements = _elements
        _this_._index = _index
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_29c2e92
    
    def invoke(self, _anonymous_parameter_0_, element):
        tmp0 = _sharedBox_read(_index)
        _sharedBox_write(_index, jsBitOr(jsPlus(tmp0, 1), 0))
        jsArraySet(_elements, tmp0, element)
    
    def invoke(self, p1, p2):
        tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_14062855
        _this_.invoke(tmp, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_24ba43e0)
        return Unit_getInstance()
    

class CombinedContext:
    def _init_(left, element):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_23ee70a7
        _this_.left = left
        _this_.element = element
    
    def get(self, key):
        cur = _this_
        while True:
            tmp0_safe_receiver = element.get(key)
            if jsEqeq(tmp0_safe_receiver, None):
                visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstImpl_67b20b4c
            
            if True:
                visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_447dd61f
            
            Unit_getInstance()
            next = left
            if jsInstanceOf(next, jsClass()):
                cur = kotlin_coroutines_CombinedContext(next)
            
            if True:
                if True:
                    return next.get(key)
                
            
        
    
    def fold(self, initial, operation):
        return operation.invoke(left.fold(initial, operation), element)
    
    def minusKey(self, key):
        tmp0_safe_receiver = element.get(key)
        if jsEqeq(tmp0_safe_receiver, None):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstImpl_5c261c74
        
        if True:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_3bc22ada
        
        Unit_getInstance()
        newLeft = left.minusKey(key)
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_568514f
    
    def equals(self, other):
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
    
    def hashCode(self):
        return jsBitOr(jsPlus(hashCode(left), hashCode(element)), 0)
    
    def toString(self):
        return jsPlus(jsPlus('[', _this_.fold('', _no_name_provided__factory())), ']')
    
    def plus(self, context):
        pass
    

def _get_safeCast_(_this):
    return safeCast

def _get_topmostKey_(_this):
    return topmostKey

class AbstractCoroutineContextKey:
    def _init_(baseKey, safeCast):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_19b0a9f2
        _this_.safeCast = safeCast
        tmp = _this_
        tmp
        if jsInstanceOf(baseKey, jsClass()):
            tmp = topmostKey
        
        if True:
            if True:
                tmp = baseKey
            
        
        tmp.topmostKey = tmp
    
    def tryCast(self, element):
        return safeCast.invoke(element)
    
    def isSubKey(self, key):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3479e14e
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_1cdb691a

def _no_name_provided__factory(_elements, _index):
    i = _no_name_provided_(_elements, _index)
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_c129b51

def _get_COROUTINE_SUSPENDED_():
    return CoroutineSingletons_COROUTINE_SUSPENDED_getInstance()

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_115e7c5e = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_1444fa42 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_ffc9278 = 0
def values():
    return arrayLiteral(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_27e93770)

def valueOf(value):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_46721812

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_39660d2 = 0
def CoroutineSingletons_initEntries():
    if CoroutineSingletons_entriesInitialized:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_30012b46
    
    CoroutineSingletons_entriesInitialized = True
    CoroutineSingletons_COROUTINE_SUSPENDED_instance = CoroutineSingletons('COROUTINE_SUSPENDED', 0)
    CoroutineSingletons_UNDECIDED_instance = CoroutineSingletons('UNDECIDED', 1)
    CoroutineSingletons_RESUMED_instance = CoroutineSingletons('RESUMED', 2)

class CoroutineSingletons:
    def _init_(name, ordinal):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_32c6eb3c
    
    def _get_name_(self):
        pass
    
    def _get_ordinal_(self):
        pass
    
    def compareTo(self, other):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
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
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def RequireKotlin_init__Init_(version, message, level, versionKind, errorCode, _mask0, _marker, _this):
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 2), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_42c63e72
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 4), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_6e14a376
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 8), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_6d340d36
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 16), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_24abee74
    
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_4da069f0
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
    
    def _get_version_(self):
        return version
    
    def _get_message_(self):
        return message
    
    def _get_level_(self):
        return level
    
    def _get_versionKind_(self):
        return versionKind
    
    def _get_errorCode_(self):
        return errorCode
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_4daa4a5a = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_16f86d8f = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_5a025435 = 0
def values():
    return arrayLiteral(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_7c394b55)

def valueOf(value):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2ff89271

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_d06a341 = 0
def RequireKotlinVersionKind_initEntries():
    if RequireKotlinVersionKind_entriesInitialized:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_6bf597a9
    
    RequireKotlinVersionKind_entriesInitialized = True
    RequireKotlinVersionKind_LANGUAGE_VERSION_instance = RequireKotlinVersionKind('LANGUAGE_VERSION', 0)
    RequireKotlinVersionKind_COMPILER_VERSION_instance = RequireKotlinVersionKind('COMPILER_VERSION', 1)
    RequireKotlinVersionKind_API_VERSION_instance = RequireKotlinVersionKind('API_VERSION', 2)

class RequireKotlinVersionKind:
    def _init_(name, ordinal):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_63f70fd7
    
    def _get_name_(self):
        pass
    
    def _get_ordinal_(self):
        pass
    
    def compareTo(self, other):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class InlineOnly:
    def _init_():
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class NoInfer:
    def _init_():
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class DynamicExtension:
    def _init_():
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class ContractsDsl:
    def _init_():
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class OnlyInputTypes:
    def _init_():
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
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
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def _init_():
        pass
    

class KTypeParameter:
    def _get_name_(self):
        pass
    
    def _get_upperBounds_(self):
        pass
    
    def _get_variance_(self):
        pass
    
    def _get_isReified_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def _init_():
        pass
    

class Companion:
    def _init_():
        Companion_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_30a5a58d
        _this_.star = KTypeProjection(None, None)
    
    def _get_star_(self):
        return star
    
    def _get_STAR_(self):
        return star
    
    def invariant(self, type):
        return KTypeProjection(KVariance_INVARIANT_getInstance(), type)
    
    def contravariant(self, type):
        return KTypeProjection(KVariance_IN_getInstance(), type)
    
    def covariant(self, type):
        return KTypeProjection(KVariance_OUT_getInstance(), type)
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_684d5845 = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_471e3e69
    
    return Companion_instance

class KTypeProjection:
    def _init_(variance, type):
        Companion_getInstance()
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_ea40c9f
        _this_.variance = variance
        _this_.type = type
        tmp0_require_0 = jsEqeqeq(jsEqeq(variance, None), jsEqeq(type, None))
        if jsNot(tmp0_require_0):
            message_2 = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_59ccdde4
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_f157271
        
    
    def _get_variance_(self):
        return variance
    
    def _get_type_(self):
        return type
    
    def toString(self):
        tmp0_subject = variance
        tmp
        if jsEqeq(tmp0_subject, None):
            tmp = '*'
        
        if equals(tmp0_subject, KVariance_INVARIANT_getInstance()):
            tmp = toString()
        
        if equals(tmp0_subject, KVariance_IN_getInstance()):
            tmp = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_48841b10
        
        if equals(tmp0_subject, KVariance_OUT_getInstance()):
            tmp = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_5e231326
        
        if True:
            noWhenBranchMatchedException()
        
        return tmp
    
    def component1(self):
        return variance
    
    def component2(self):
        return type
    
    def copy(self, variance, type):
        return KTypeProjection(variance, type)
    
    def copy_default(self, variance, type, _mask0, _handler):
        if jsNot(jsEqeqeq(jsBitAnd(_mask0, 1), 0)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_653e6996
        
        if jsNot(jsEqeqeq(jsBitAnd(_mask0, 2), 0)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_56ed77b1
        
        return _this_.copy(variance, type)
    
    def hashCode(self):
        result = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6b0090ca
        result = jsBitOr(jsPlus(imul(result, 31), visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6a1f63fd), 0)
        return result
    
    def equals(self, other):
        if jsEqeqeq(_this_, other):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_66b3eab0
        
        if jsNot(jsInstanceOf(other, jsClass())):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_7699e60a
        
        if True:
            pass
        
        tmp0_other_with_cast = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_25832704
        if jsNot(equals(variance, variance)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_4220468
        
        if jsNot(equals(type, type)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_1892865f
        
        return True
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_723c7f2f = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_5cb077e3 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_278758da = 0
def values():
    return arrayLiteral(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_2e740f3c)

def valueOf(value):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4a5bc21

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_54cf024c = 0
def KVariance_initEntries():
    if KVariance_entriesInitialized:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_2b3d662e
    
    KVariance_entriesInitialized = True
    KVariance_INVARIANT_instance = KVariance('INVARIANT', 0)
    KVariance_IN_instance = KVariance('IN', 1)
    KVariance_OUT_instance = KVariance('OUT', 2)

class KVariance:
    def _init_(name, ordinal):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_14c75caf
    
    def _get_name_(self):
        pass
    
    def _get_ordinal_(self):
        pass
    
    def compareTo(self, other):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
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
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_3e900cf4
    
    if True:
        if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_67ba7db3:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_3b0c48bd
        
        if True:
            if jsInstanceOf(element, jsClass()):
                visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_88d92e5
            
            if True:
                if True:
                    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_5e23d0db
                
            
        
    

def isEmpty():
    return jsEqeqeq(charSequenceLength(_this_), 0)

def _get_lastIndex_():
    return jsBitOr(jsMinus(charSequenceLength(_this_), 1), 0)

def _get_UNDEFINED_RESULT_():
    return UNDEFINED_RESULT

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_6bbb3280 = 0
def UNDEFINED_RESULT_init_():
    tmp0_success_0 = Companion_getInstance()
    tmp1_success_0 = _get_COROUTINE_SUSPENDED_()
    return Result(tmp1_success_0)

def check(value):
    if jsNot(value):
        message_2 = 'Check failed.'
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_6cf4325b
    

def check(value, lazyMessage):
    if jsNot(value):
        message = lazyMessage.invoke()
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_6bd5101f
    

def error(message):
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_7c1ac3b

def require(value, lazyMessage):
    if jsNot(value):
        message = lazyMessage.invoke()
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_24d7df03
    

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
        tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_304d96b5
    
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
            tmp = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_3887b71
        
    
    return tmp

class Companion:
    def _init_():
        Companion_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_5570ee6d
    
    def success(self, value):
        return Result(value)
    
    def failure(self, exception):
        return Result(createFailure(exception))
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_3aba9252 = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_30b9d1f0
    
    return Companion_instance

class Failure:
    def _init_(exception):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_293ba26c
        _this_.exception = exception
    
    def _get_exception_(self):
        return exception
    
    def equals(self, other):
        tmp
        if jsInstanceOf(other, jsClass()):
            tmp = equals(exception, exception)
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def hashCode(self):
        return hashCode(exception)
    
    def toString(self):
        return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_277cf420
    

def Result__hashCode_impl(this):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_22f9cea5

def Result__equals_impl(this, other):
    if jsNot(jsInstanceOf(other, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_789f5552
    
    if True:
        pass
    
    tmp0_other_with_cast = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_7b6bf067
    if jsNot(equals(value, value)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_4d7fba20
    
    return True

class Result:
    def _init_(value):
        Companion_getInstance()
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_7a6b214c
        _this_.value = value
    
    def toString(self):
        return Result__toString_impl(unboxIntrinsic(_this_))
    
    def hashCode(self):
        return Result__hashCode_impl(unboxIntrinsic(_this_))
    
    def equals(self, other):
        return Result__equals_impl(unboxIntrinsic(_this_), other)
    

def createFailure(exception):
    return Failure(exception)

def getOrThrow():
    throwOnFailure()
    tmp = _Result___get_value__impl_(_this_)
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3bc59637

def throwOnFailure():
    tmp = _Result___get_value__impl_(_this_)
    if jsInstanceOf(tmp, jsClass()):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_5d24703e
    
    if True:
        pass
    

def run(block):
    return block.invoke()

def TODO():
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_b106842

def NotImplementedError_init__Init_(message, _mask0, _marker, _this):
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 1), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_65bccd0f
    
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_63dee1b7
    return _this

def NotImplementedError_init__Create_(message, _mask0, _marker):
    tmp = NotImplementedError_init__Init_(message, _mask0, _marker, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_5eb1fd44)
    return tmp

class NotImplementedError:
    def _init_(message):
        Error_init__Init_(message, _this_)
        captureStack(_this_, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_786f4b15)
    
    def _get_message_(self):
        pass
    
    def _get_cause_(self):
        pass
    
    def toString(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    

def let(block):
    return block.invoke(_this_)

def apply(block):
    block.invoke(_this_)
    return _this_

def repeat(times, action):
    inductionVariable = 0
    if jsLt(inductionVariable, times):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_343418b2
    

def _with(receiver, block):
    return block.invoke(receiver)

def also(block):
    block.invoke(_this_)
    return _this_

def run(block):
    return block.invoke(_this_)

def _UByte___get_data__impl_(this):
    return data

class Companion:
    def _init_():
        Companion_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_61d9dd15
        _this_.MIN_VALUE = UByte(visitConst_other_Byte)
        _this_.MAX_VALUE = UByte(visitConst_other_Byte)
        _this_.SIZE_BYTES = 1
        _this_.SIZE_BITS = 8
    
    def _get_MIN_VALUE_(self):
        return MIN_VALUE
    
    def _get_MAX_VALUE_(self):
        return MAX_VALUE
    
    def _get_SIZE_BYTES_(self):
        return SIZE_BYTES
    
    def _get_SIZE_BITS_(self):
        return SIZE_BITS
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_6b6eaa73 = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_e2ff893
    
    return Companion_instance

def UByte__compareTo_impl(this, other):
    tmp = jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255)
    return compareTo(tmp, jsBitAnd(kotlin_Int(_UByte___get_data__impl_(other)), 255))

def UByte__compareTo_impl(this, other):
    tmp = unboxIntrinsic(this)
    return UByte__compareTo_impl(tmp, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_7edf6563)

def UByte__compareTo_impl(this, other):
    tmp = jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255)
    return compareTo(tmp, jsBitAnd(kotlin_Int(_UShort___get_data__impl_(other)), 65535))

def UByte__compareTo_impl(this, other):
    tmp0_compareTo_0 = UInt(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255))
    return uintCompare(_UInt___get_data__impl_(tmp0_compareTo_0), _UInt___get_data__impl_(other))

def UByte__compareTo_impl(this, other):
    tmp0_compareTo_0 = ULong(toLong(_UByte___get_data__impl_(this))._and(Long(255, 0)))
    return ulongCompare(_ULong___get_data__impl_(tmp0_compareTo_0), _ULong___get_data__impl_(other))

def UByte__plus_impl(this, other):
    tmp0_plus_0 = UInt(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255))
    tmp1_plus_0 = UInt(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(other)), 255))
    return UInt(jsBitOr(jsPlus(_UInt___get_data__impl_(tmp0_plus_0), _UInt___get_data__impl_(tmp1_plus_0)), 0))

def UByte__plus_impl(this, other):
    tmp0_plus_0 = UInt(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255))
    tmp1_plus_0 = UInt(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(other)), 65535))
    return UInt(jsBitOr(jsPlus(_UInt___get_data__impl_(tmp0_plus_0), _UInt___get_data__impl_(tmp1_plus_0)), 0))

def UByte__plus_impl(this, other):
    tmp0_plus_0 = UInt(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255))
    return UInt(jsBitOr(jsPlus(_UInt___get_data__impl_(tmp0_plus_0), _UInt___get_data__impl_(other)), 0))

def UByte__plus_impl(this, other):
    tmp0_plus_0 = ULong(toLong(_UByte___get_data__impl_(this))._and(Long(255, 0)))
    return ULong(_ULong___get_data__impl_(tmp0_plus_0).plus(_ULong___get_data__impl_(other)))

def UByte__minus_impl(this, other):
    tmp0_minus_0 = UInt(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255))
    tmp1_minus_0 = UInt(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(other)), 255))
    return UInt(jsBitOr(jsMinus(_UInt___get_data__impl_(tmp0_minus_0), _UInt___get_data__impl_(tmp1_minus_0)), 0))

def UByte__minus_impl(this, other):
    tmp0_minus_0 = UInt(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255))
    tmp1_minus_0 = UInt(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(other)), 65535))
    return UInt(jsBitOr(jsMinus(_UInt___get_data__impl_(tmp0_minus_0), _UInt___get_data__impl_(tmp1_minus_0)), 0))

def UByte__minus_impl(this, other):
    tmp0_minus_0 = UInt(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255))
    return UInt(jsBitOr(jsMinus(_UInt___get_data__impl_(tmp0_minus_0), _UInt___get_data__impl_(other)), 0))

def UByte__minus_impl(this, other):
    tmp0_minus_0 = ULong(toLong(_UByte___get_data__impl_(this))._and(Long(255, 0)))
    return ULong(_ULong___get_data__impl_(tmp0_minus_0).minus(_ULong___get_data__impl_(other)))

def UByte__times_impl(this, other):
    tmp0_times_0 = UInt(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255))
    tmp1_times_0 = UInt(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(other)), 255))
    return UInt(imul(_UInt___get_data__impl_(tmp0_times_0), _UInt___get_data__impl_(tmp1_times_0)))

def UByte__times_impl(this, other):
    tmp0_times_0 = UInt(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255))
    tmp1_times_0 = UInt(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(other)), 65535))
    return UInt(imul(_UInt___get_data__impl_(tmp0_times_0), _UInt___get_data__impl_(tmp1_times_0)))

def UByte__times_impl(this, other):
    tmp0_times_0 = UInt(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255))
    return UInt(imul(_UInt___get_data__impl_(tmp0_times_0), _UInt___get_data__impl_(other)))

def UByte__times_impl(this, other):
    tmp0_times_0 = ULong(toLong(_UByte___get_data__impl_(this))._and(Long(255, 0)))
    return ULong(_ULong___get_data__impl_(tmp0_times_0).times(_ULong___get_data__impl_(other)))

def UByte__div_impl(this, other):
    tmp0_div_0 = UInt(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255))
    tmp1_div_0 = UInt(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(other)), 255))
    return uintDivide(tmp0_div_0, tmp1_div_0)

def UByte__div_impl(this, other):
    tmp0_div_0 = UInt(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255))
    tmp1_div_0 = UInt(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(other)), 65535))
    return uintDivide(tmp0_div_0, tmp1_div_0)

def UByte__div_impl(this, other):
    tmp0_div_0 = UInt(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255))
    return uintDivide(tmp0_div_0, other)

def UByte__div_impl(this, other):
    tmp0_div_0 = ULong(toLong(_UByte___get_data__impl_(this))._and(Long(255, 0)))
    return ulongDivide(tmp0_div_0, other)

def UByte__rem_impl(this, other):
    tmp0_rem_0 = UInt(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255))
    tmp1_rem_0 = UInt(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(other)), 255))
    return uintRemainder(tmp0_rem_0, tmp1_rem_0)

def UByte__rem_impl(this, other):
    tmp0_rem_0 = UInt(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255))
    tmp1_rem_0 = UInt(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(other)), 65535))
    return uintRemainder(tmp0_rem_0, tmp1_rem_0)

def UByte__rem_impl(this, other):
    tmp0_rem_0 = UInt(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255))
    return uintRemainder(tmp0_rem_0, other)

def UByte__rem_impl(this, other):
    tmp0_rem_0 = ULong(toLong(_UByte___get_data__impl_(this))._and(Long(255, 0)))
    return ulongRemainder(tmp0_rem_0, other)

def UByte__inc_impl(this):
    return UByte(numberToByte(jsPlus(_UByte___get_data__impl_(this), 1)))

def UByte__dec_impl(this):
    return UByte(numberToByte(jsMinus(_UByte___get_data__impl_(this), 1)))

def UByte__rangeTo_impl(this, other):
    tmp = UInt(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255))
    return UIntRange(tmp, UInt(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(other)), 255)))

def UByte__and_impl(this, other):
    tmp0_and_0 = _UByte___get_data__impl_(this)
    tmp1_and_0 = _UByte___get_data__impl_(other)
    return UByte(toByte(jsBitAnd(kotlin_Int(tmp0_and_0), kotlin_Int(tmp1_and_0))))

def UByte__or_impl(this, other):
    tmp0_or_0 = _UByte___get_data__impl_(this)
    tmp1_or_0 = _UByte___get_data__impl_(other)
    return UByte(toByte(jsBitOr(kotlin_Int(tmp0_or_0), kotlin_Int(tmp1_or_0))))

def UByte__xor_impl(this, other):
    tmp0_xor_0 = _UByte___get_data__impl_(this)
    tmp1_xor_0 = _UByte___get_data__impl_(other)
    return UByte(toByte(jsBitXor(kotlin_Int(tmp0_xor_0), kotlin_Int(tmp1_xor_0))))

def UByte__inv_impl(this):
    tmp0_inv_0 = _UByte___get_data__impl_(this)
    return UByte(toByte(jsBitNot(kotlin_Int(tmp0_inv_0))))

def UByte__toByte_impl(this):
    return _UByte___get_data__impl_(this)

def UByte__toShort_impl(this):
    tmp0_and_0 = kotlin_Short(_UByte___get_data__impl_(this))
    tmp1_and_0 = visitConst_other_Short
    return toShort(jsBitAnd(kotlin_Int(tmp0_and_0), kotlin_Int(tmp1_and_0)))

def UByte__toInt_impl(this):
    return jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255)

def UByte__toLong_impl(this):
    return toLong(_UByte___get_data__impl_(this))._and(Long(255, 0))

def UByte__toUByte_impl(this):
    return this

def UByte__toUShort_impl(this):
    tmp0_and_0 = kotlin_Short(_UByte___get_data__impl_(this))
    tmp1_and_0 = visitConst_other_Short
    return UShort(toShort(jsBitAnd(kotlin_Int(tmp0_and_0), kotlin_Int(tmp1_and_0))))

def UByte__toUInt_impl(this):
    return UInt(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255))

def UByte__toULong_impl(this):
    return ULong(toLong(_UByte___get_data__impl_(this))._and(Long(255, 0)))

def UByte__toFloat_impl(this):
    return kotlin_Float(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255))

def UByte__toDouble_impl(this):
    return kotlin_Double(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255))

def UByte__toString_impl(this):
    return jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255).toString()

def UByte__hashCode_impl(this):
    return data

def UByte__equals_impl(this, other):
    if jsNot(jsInstanceOf(other, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_7712df76
    
    if True:
        pass
    
    tmp0_other_with_cast = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_341b0573
    if jsNot(jsEqeqeq(data, data)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_2c6d442d
    
    return True

class UByte:
    def _init_(data):
        Companion_getInstance()
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_3006aef5
        _this_.data = data
    
    def compareTo(self, other):
        return UByte__compareTo_impl(unboxIntrinsic(_this_), other)
    
    def compareTo(self, other):
        return UByte__compareTo_impl(_this_, other)
    
    def toString(self):
        return UByte__toString_impl(unboxIntrinsic(_this_))
    
    def hashCode(self):
        return UByte__hashCode_impl(unboxIntrinsic(_this_))
    
    def equals(self, other):
        return UByte__equals_impl(unboxIntrinsic(_this_), other)
    

def toUByte():
    return UByte(toByte(_this_))

def toUByte():
    return UByte(toByte(_this_))

def toUByte():
    return UByte(_this_.toByte())

def toUByte():
    return UByte(_this_)

def _get_array_(_this):
    return array

def _set_index_(_this, _set___):
    _this.index = _set___

def _get_index_(_this):
    return index

def _UByteArray___get_storage__impl_(this):
    return storage

def _UByteArray___init__impl_(size):
    tmp = UByteArray(int8Array(size))
    return tmp

def UByteArray__get_impl(this, index):
    tmp0_toUByte_0 = jsArrayGet(_UByteArray___get_storage__impl_(this), index)
    return UByte(tmp0_toUByte_0)

def UByteArray__set_impl(this, index, value):
    tmp = _UByteArray___get_storage__impl_(this)
    jsArraySet(tmp, index, _UByte___get_data__impl_(value))

def _UByteArray___get_size__impl_(this):
    return jsArrayLength(_UByteArray___get_storage__impl_(this))

def UByteArray__iterator_impl(this):
    return Iterator(_UByteArray___get_storage__impl_(this))

class Iterator:
    def _init_(array):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_6771efaa
        _this_.array = array
        _this_.index = 0
    
    def hasNext(self):
        return jsLt(index, jsArrayLength(array))
    
    def nextUByte(self):
        tmp
        if jsLt(index, jsArrayLength(array)):
            tmp0_this = _this_
            tmp1 = index
            tmp0_this.index = jsBitOr(jsPlus(tmp1, 1), 0)
            tmp0_toUByte_0 = jsArrayGet(array, tmp1)
            tmp = UByte(tmp0_toUByte_0)
        
        if True:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_5abc488d
        
        return tmp
    
    def next(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def UByteArray__contains_impl(this, element):
    tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_345292c1
    if jsNot(jsInstanceOf(tmp, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_2dbc66f0
    
    if True:
        pass
    
    tmp = _UByteArray___get_storage__impl_(this)
    return contains(_UByte___get_data__impl_(element))

def UByteArray__contains_impl(this, element):
    if jsNot(jsInstanceOf(element, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_61d4bc03
    
    if True:
        pass
    
    tmp = unboxIntrinsic(this)
    return UByteArray__contains_impl(tmp, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_230ac978)

def UByteArray__containsAll_impl(this, elements):
    tmp_ret_0
    visitDoWhileLoop_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_6e879a78
    return tmp_ret_0

def UByteArray__containsAll_impl(this, elements):
    return UByteArray__containsAll_impl(unboxIntrinsic(this), elements)

def UByteArray__isEmpty_impl(this):
    return jsEqeqeq(jsArrayLength(_UByteArray___get_storage__impl_(this)), 0)

def UByteArray__toString_impl(this):
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_5a2c8199

def UByteArray__hashCode_impl(this):
    return hashCode(storage)

def UByteArray__equals_impl(this, other):
    if jsNot(jsInstanceOf(other, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_5746609e
    
    if True:
        pass
    
    tmp0_other_with_cast = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_368d76d7
    if jsNot(equals(storage, storage)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_5c648e38
    
    return True

class UByteArray:
    def _init_(storage):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_92775a3
        _this_.storage = storage
    
    def _get_size_(self):
        return _UByteArray___get_size__impl_(unboxIntrinsic(_this_))
    
    def iterator(self):
        return UByteArray__iterator_impl(unboxIntrinsic(_this_))
    
    def contains(self, element):
        return UByteArray__contains_impl(unboxIntrinsic(_this_), element)
    
    def contains(self, element):
        return UByteArray__contains_impl(_this_, element)
    
    def containsAll(self, elements):
        return UByteArray__containsAll_impl(unboxIntrinsic(_this_), elements)
    
    def containsAll(self, elements):
        return UByteArray__containsAll_impl(_this_, elements)
    
    def isEmpty(self):
        return UByteArray__isEmpty_impl(unboxIntrinsic(_this_))
    
    def toString(self):
        return UByteArray__toString_impl(unboxIntrinsic(_this_))
    
    def hashCode(self):
        return UByteArray__hashCode_impl(unboxIntrinsic(_this_))
    
    def equals(self, other):
        return UByteArray__equals_impl(unboxIntrinsic(_this_), other)
    

def _UInt___get_data__impl_(this):
    return data

class Companion:
    def _init_():
        Companion_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_74cf2d5f
        _this_.MIN_VALUE = UInt(0)
        _this_.MAX_VALUE = UInt(-1)
        _this_.SIZE_BYTES = 4
        _this_.SIZE_BITS = 32
    
    def _get_MIN_VALUE_(self):
        return MIN_VALUE
    
    def _get_MAX_VALUE_(self):
        return MAX_VALUE
    
    def _get_SIZE_BYTES_(self):
        return SIZE_BYTES
    
    def _get_SIZE_BITS_(self):
        return SIZE_BITS
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_44e49229 = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_5a187cd4
    
    return Companion_instance

def UInt__compareTo_impl(this, other):
    tmp0_compareTo_0 = UInt(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(other)), 255))
    return uintCompare(_UInt___get_data__impl_(this), _UInt___get_data__impl_(tmp0_compareTo_0))

def UInt__compareTo_impl(this, other):
    tmp0_compareTo_0 = UInt(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(other)), 65535))
    return uintCompare(_UInt___get_data__impl_(this), _UInt___get_data__impl_(tmp0_compareTo_0))

def UInt__compareTo_impl(this, other):
    return uintCompare(_UInt___get_data__impl_(this), _UInt___get_data__impl_(other))

def UInt__compareTo_impl(this, other):
    tmp = unboxIntrinsic(this)
    return UInt__compareTo_impl(tmp, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_270741c2)

def UInt__compareTo_impl(this, other):
    tmp0_compareTo_0 = ULong(toLong(_UInt___get_data__impl_(this))._and(Long(-1, 0)))
    return ulongCompare(_ULong___get_data__impl_(tmp0_compareTo_0), _ULong___get_data__impl_(other))

def UInt__plus_impl(this, other):
    tmp0_plus_0 = UInt(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(other)), 255))
    return UInt(jsBitOr(jsPlus(_UInt___get_data__impl_(this), _UInt___get_data__impl_(tmp0_plus_0)), 0))

def UInt__plus_impl(this, other):
    tmp0_plus_0 = UInt(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(other)), 65535))
    return UInt(jsBitOr(jsPlus(_UInt___get_data__impl_(this), _UInt___get_data__impl_(tmp0_plus_0)), 0))

def UInt__plus_impl(this, other):
    return UInt(jsBitOr(jsPlus(_UInt___get_data__impl_(this), _UInt___get_data__impl_(other)), 0))

def UInt__plus_impl(this, other):
    tmp0_plus_0 = ULong(toLong(_UInt___get_data__impl_(this))._and(Long(-1, 0)))
    return ULong(_ULong___get_data__impl_(tmp0_plus_0).plus(_ULong___get_data__impl_(other)))

def UInt__minus_impl(this, other):
    tmp0_minus_0 = UInt(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(other)), 255))
    return UInt(jsBitOr(jsMinus(_UInt___get_data__impl_(this), _UInt___get_data__impl_(tmp0_minus_0)), 0))

def UInt__minus_impl(this, other):
    tmp0_minus_0 = UInt(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(other)), 65535))
    return UInt(jsBitOr(jsMinus(_UInt___get_data__impl_(this), _UInt___get_data__impl_(tmp0_minus_0)), 0))

def UInt__minus_impl(this, other):
    return UInt(jsBitOr(jsMinus(_UInt___get_data__impl_(this), _UInt___get_data__impl_(other)), 0))

def UInt__minus_impl(this, other):
    tmp0_minus_0 = ULong(toLong(_UInt___get_data__impl_(this))._and(Long(-1, 0)))
    return ULong(_ULong___get_data__impl_(tmp0_minus_0).minus(_ULong___get_data__impl_(other)))

def UInt__times_impl(this, other):
    tmp0_times_0 = UInt(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(other)), 255))
    return UInt(imul(_UInt___get_data__impl_(this), _UInt___get_data__impl_(tmp0_times_0)))

def UInt__times_impl(this, other):
    tmp0_times_0 = UInt(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(other)), 65535))
    return UInt(imul(_UInt___get_data__impl_(this), _UInt___get_data__impl_(tmp0_times_0)))

def UInt__times_impl(this, other):
    return UInt(imul(_UInt___get_data__impl_(this), _UInt___get_data__impl_(other)))

def UInt__times_impl(this, other):
    tmp0_times_0 = ULong(toLong(_UInt___get_data__impl_(this))._and(Long(-1, 0)))
    return ULong(_ULong___get_data__impl_(tmp0_times_0).times(_ULong___get_data__impl_(other)))

def UInt__div_impl(this, other):
    tmp0_div_0 = UInt(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(other)), 255))
    return uintDivide(this, tmp0_div_0)

def UInt__div_impl(this, other):
    tmp0_div_0 = UInt(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(other)), 65535))
    return uintDivide(this, tmp0_div_0)

def UInt__div_impl(this, other):
    return uintDivide(this, other)

def UInt__div_impl(this, other):
    tmp0_div_0 = ULong(toLong(_UInt___get_data__impl_(this))._and(Long(-1, 0)))
    return ulongDivide(tmp0_div_0, other)

def UInt__rem_impl(this, other):
    tmp0_rem_0 = UInt(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(other)), 255))
    return uintRemainder(this, tmp0_rem_0)

def UInt__rem_impl(this, other):
    tmp0_rem_0 = UInt(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(other)), 65535))
    return uintRemainder(this, tmp0_rem_0)

def UInt__rem_impl(this, other):
    return uintRemainder(this, other)

def UInt__rem_impl(this, other):
    tmp0_rem_0 = ULong(toLong(_UInt___get_data__impl_(this))._and(Long(-1, 0)))
    return ulongRemainder(tmp0_rem_0, other)

def UInt__inc_impl(this):
    return UInt(jsBitOr(jsPlus(_UInt___get_data__impl_(this), 1), 0))

def UInt__dec_impl(this):
    return UInt(jsBitOr(jsMinus(_UInt___get_data__impl_(this), 1), 0))

def UInt__rangeTo_impl(this, other):
    return UIntRange(this, other)

def UInt__shl_impl(this, bitCount):
    return UInt(jsBitShiftL(_UInt___get_data__impl_(this), bitCount))

def UInt__shr_impl(this, bitCount):
    return UInt(jsBitShiftRU(_UInt___get_data__impl_(this), bitCount))

def UInt__and_impl(this, other):
    return UInt(jsBitAnd(_UInt___get_data__impl_(this), _UInt___get_data__impl_(other)))

def UInt__or_impl(this, other):
    return UInt(jsBitOr(_UInt___get_data__impl_(this), _UInt___get_data__impl_(other)))

def UInt__xor_impl(this, other):
    return UInt(jsBitXor(_UInt___get_data__impl_(this), _UInt___get_data__impl_(other)))

def UInt__inv_impl(this):
    return UInt(jsBitNot(_UInt___get_data__impl_(this)))

def UInt__toByte_impl(this):
    return toByte(_UInt___get_data__impl_(this))

def UInt__toShort_impl(this):
    return toShort(_UInt___get_data__impl_(this))

def UInt__toInt_impl(this):
    return _UInt___get_data__impl_(this)

def UInt__toLong_impl(this):
    return toLong(_UInt___get_data__impl_(this))._and(Long(-1, 0))

def UInt__toUByte_impl(this):
    tmp0_toUByte_0 = _UInt___get_data__impl_(this)
    return UByte(toByte(tmp0_toUByte_0))

def UInt__toUShort_impl(this):
    tmp0_toUShort_0 = _UInt___get_data__impl_(this)
    return UShort(toShort(tmp0_toUShort_0))

def UInt__toUInt_impl(this):
    return this

def UInt__toULong_impl(this):
    return ULong(toLong(_UInt___get_data__impl_(this))._and(Long(-1, 0)))

def UInt__toFloat_impl(this):
    return kotlin_Float(uintToDouble(_UInt___get_data__impl_(this)))

def UInt__toDouble_impl(this):
    return uintToDouble(_UInt___get_data__impl_(this))

def UInt__toString_impl(this):
    return toLong(_UInt___get_data__impl_(this))._and(Long(-1, 0)).toString()

def UInt__hashCode_impl(this):
    return data

def UInt__equals_impl(this, other):
    if jsNot(jsInstanceOf(other, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_5390862e
    
    if True:
        pass
    
    tmp0_other_with_cast = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_51413fc7
    if jsNot(jsEqeqeq(data, data)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_5006a697
    
    return True

class UInt:
    def _init_(data):
        Companion_getInstance()
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_18f794e
        _this_.data = data
    
    def compareTo(self, other):
        return UInt__compareTo_impl(unboxIntrinsic(_this_), other)
    
    def compareTo(self, other):
        return UInt__compareTo_impl(_this_, other)
    
    def toString(self):
        return UInt__toString_impl(unboxIntrinsic(_this_))
    
    def hashCode(self):
        return UInt__hashCode_impl(unboxIntrinsic(_this_))
    
    def equals(self, other):
        return UInt__equals_impl(unboxIntrinsic(_this_), other)
    

def toUInt():
    return UInt(_this_.toInt())

def toUInt():
    return UInt(_this_)

def toUInt():
    return UInt(kotlin_Int(_this_))

def toUInt():
    return doubleToUInt(_this_)

def toUInt():
    return doubleToUInt(kotlin_Double(_this_))

def toUInt():
    return UInt(kotlin_Int(_this_))

def _get_array_(_this):
    return array

def _set_index_(_this, _set___):
    _this.index = _set___

def _get_index_(_this):
    return index

def _UIntArray___get_storage__impl_(this):
    return storage

def _UIntArray___init__impl_(size):
    tmp = UIntArray(int32Array(size))
    return tmp

def UIntArray__get_impl(this, index):
    tmp0_toUInt_0 = jsArrayGet(_UIntArray___get_storage__impl_(this), index)
    return UInt(tmp0_toUInt_0)

def UIntArray__set_impl(this, index, value):
    tmp = _UIntArray___get_storage__impl_(this)
    jsArraySet(tmp, index, _UInt___get_data__impl_(value))

def _UIntArray___get_size__impl_(this):
    return jsArrayLength(_UIntArray___get_storage__impl_(this))

def UIntArray__iterator_impl(this):
    return Iterator(_UIntArray___get_storage__impl_(this))

class Iterator:
    def _init_(array):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_3d0ce151
        _this_.array = array
        _this_.index = 0
    
    def hasNext(self):
        return jsLt(index, jsArrayLength(array))
    
    def nextUInt(self):
        tmp
        if jsLt(index, jsArrayLength(array)):
            tmp0_this = _this_
            tmp1 = index
            tmp0_this.index = jsBitOr(jsPlus(tmp1, 1), 0)
            tmp0_toUInt_0 = jsArrayGet(array, tmp1)
            tmp = UInt(tmp0_toUInt_0)
        
        if True:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_23307c6c
        
        return tmp
    
    def next(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def UIntArray__contains_impl(this, element):
    tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_284c84de
    if jsNot(jsInstanceOf(tmp, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_237b54bc
    
    if True:
        pass
    
    tmp = _UIntArray___get_storage__impl_(this)
    return contains(_UInt___get_data__impl_(element))

def UIntArray__contains_impl(this, element):
    if jsNot(jsInstanceOf(element, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_4beea618
    
    if True:
        pass
    
    tmp = unboxIntrinsic(this)
    return UIntArray__contains_impl(tmp, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_160a3238)

def UIntArray__containsAll_impl(this, elements):
    tmp_ret_0
    visitDoWhileLoop_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_882364e
    return tmp_ret_0

def UIntArray__containsAll_impl(this, elements):
    return UIntArray__containsAll_impl(unboxIntrinsic(this), elements)

def UIntArray__isEmpty_impl(this):
    return jsEqeqeq(jsArrayLength(_UIntArray___get_storage__impl_(this)), 0)

def UIntArray__toString_impl(this):
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_26dc0c5

def UIntArray__hashCode_impl(this):
    return hashCode(storage)

def UIntArray__equals_impl(this, other):
    if jsNot(jsInstanceOf(other, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_5b11d0d8
    
    if True:
        pass
    
    tmp0_other_with_cast = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_30a0c356
    if jsNot(equals(storage, storage)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_19b33b0d
    
    return True

class UIntArray:
    def _init_(storage):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_7f65639e
        _this_.storage = storage
    
    def _get_size_(self):
        return _UIntArray___get_size__impl_(unboxIntrinsic(_this_))
    
    def iterator(self):
        return UIntArray__iterator_impl(unboxIntrinsic(_this_))
    
    def contains(self, element):
        return UIntArray__contains_impl(unboxIntrinsic(_this_), element)
    
    def contains(self, element):
        return UIntArray__contains_impl(_this_, element)
    
    def containsAll(self, elements):
        return UIntArray__containsAll_impl(unboxIntrinsic(_this_), elements)
    
    def containsAll(self, elements):
        return UIntArray__containsAll_impl(_this_, elements)
    
    def isEmpty(self):
        return UIntArray__isEmpty_impl(unboxIntrinsic(_this_))
    
    def toString(self):
        return UIntArray__toString_impl(unboxIntrinsic(_this_))
    
    def hashCode(self):
        return UIntArray__hashCode_impl(unboxIntrinsic(_this_))
    
    def equals(self, other):
        return UIntArray__equals_impl(unboxIntrinsic(_this_), other)
    

class Companion:
    def _init_():
        Companion_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_53813f01
        _this_.EMPTY = UIntRange(UInt(-1), UInt(0))
    
    def _get_EMPTY_(self):
        return EMPTY
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_52214284 = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_5069b3c6
    
    return Companion_instance

class UIntRange:
    def _init_(start, endInclusive):
        Companion_getInstance()
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_6408a8ac
    
    def _get_start_(self):
        return _this_._get_first_()
    
    def _get_start_(self):
        return boxIntrinsic(_this_._get_start_())
    
    def _get_endInclusive_(self):
        return _this_._get_last_()
    
    def _get_endInclusive_(self):
        return boxIntrinsic(_this_._get_endInclusive_())
    
    def contains(self, value):
        tmp
        tmp0_compareTo_0 = _this_._get_first_()
        if jsLtEq(uintCompare(_UInt___get_data__impl_(tmp0_compareTo_0), _UInt___get_data__impl_(value)), 0):
            tmp1_compareTo_0 = _this_._get_last_()
            tmp = jsLtEq(uintCompare(_UInt___get_data__impl_(value), _UInt___get_data__impl_(tmp1_compareTo_0)), 0)
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def contains(self, value):
        return _this_.contains(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_675b0850)
    
    def isEmpty(self):
        tmp0_compareTo_0 = _this_._get_first_()
        tmp1_compareTo_0 = _this_._get_last_()
        return jsGt(uintCompare(_UInt___get_data__impl_(tmp0_compareTo_0), _UInt___get_data__impl_(tmp1_compareTo_0)), 0)
    
    def equals(self, other):
        tmp
        if jsInstanceOf(other, jsClass()):
            tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_80cec05
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def hashCode(self):
        tmp
        if _this_.isEmpty():
            tmp = -1
        
        if True:
            tmp0_toInt_0 = _this_._get_first_()
            tmp = imul(31, _UInt___get_data__impl_(tmp0_toInt_0))
            tmp1_toInt_0 = _this_._get_last_()
            tmp = jsBitOr(jsPlus(tmp, _UInt___get_data__impl_(tmp1_toInt_0)), 0)
        
        return tmp
    
    def toString(self):
        return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_3f096fa1
    
    def _get_first_(self):
        pass
    
    def _get_last_(self):
        pass
    
    def _get_step_(self):
        pass
    
    def iterator(self):
        pass
    

class Companion:
    def _init_():
        Companion_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_4b6fc231
    
    def fromClosedRange(self, rangeStart, rangeEnd, step):
        return UIntProgression(rangeStart, rangeEnd, step)
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_51aafde5 = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_6f75d11b
    
    return Companion_instance

class UIntProgression:
    def _init_(start, endInclusive, step):
        Companion_getInstance()
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_ae85aad
        if jsEqeqeq(step, 0):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_39b88618
        
        if jsEqeqeq(step, MIN_VALUE):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_2c0c1730
        
        _this_.first = start
        _this_.last = getProgressionLastElement(start, endInclusive, step)
        _this_.step = step
    
    def _get_first_(self):
        return first
    
    def _get_last_(self):
        return last
    
    def _get_step_(self):
        return step
    
    def iterator(self):
        return UIntProgressionIterator(first, last, step)
    
    def isEmpty(self):
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
    
    def equals(self, other):
        tmp
        if jsInstanceOf(other, jsClass()):
            tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_24a887a0
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def hashCode(self):
        tmp
        if _this_.isEmpty():
            tmp = -1
        
        if True:
            tmp0_toInt_0 = first
            tmp = imul(31, _UInt___get_data__impl_(tmp0_toInt_0))
            tmp1_toInt_0 = last
            tmp = jsBitOr(jsPlus(imul(31, jsBitOr(jsPlus(tmp, _UInt___get_data__impl_(tmp1_toInt_0)), 0)), kotlin_Int(step)), 0)
        
        return tmp
    
    def toString(self):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2d617d27
    

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
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_7d7888a5
        _this_.finalElement = last
        tmp = _this_
        tmp
        if jsGt(step, 0):
            tmp = jsLtEq(uintCompare(_UInt___get_data__impl_(first), _UInt___get_data__impl_(last)), 0)
        
        if True:
            tmp = jsGtEq(uintCompare(_UInt___get_data__impl_(first), _UInt___get_data__impl_(last)), 0)
        
        tmp.hasNext = tmp
        tmp = _this_
        tmp.step = UInt(step)
        _this_.next = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3c31c0c8
    
    def hasNext(self):
        return hasNext
    
    def nextUInt(self):
        value = next
        if equals(boxIntrinsic(value), boxIntrinsic(finalElement)):
            if jsNot(hasNext):
                visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_24455d50
            
            _this_.hasNext = False
        
        if True:
            tmp0_this = _this_
            tmp = tmp0_this
            tmp0_plus_0 = next
            tmp1_plus_0 = step
            tmp.next = UInt(jsBitOr(jsPlus(_UInt___get_data__impl_(tmp0_plus_0), _UInt___get_data__impl_(tmp1_plus_0)), 0))
        
        return value
    
    def next(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class UIntIterator:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_6a7cbeed
    
    def next(self):
        return _this_.nextUInt()
    
    def next(self):
        return boxIntrinsic(_this_.next())
    
    def nextUInt(self):
        pass
    
    def hasNext(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class ULongIterator:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_4b8c9729
    
    def next(self):
        return _this_.nextULong()
    
    def next(self):
        return boxIntrinsic(_this_.next())
    
    def nextULong(self):
        pass
    
    def hasNext(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class UByteIterator:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_7bbc11ed
    
    def next(self):
        return _this_.nextUByte()
    
    def next(self):
        return boxIntrinsic(_this_.next())
    
    def nextUByte(self):
        pass
    
    def hasNext(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class UShortIterator:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_76d220eb
    
    def next(self):
        return _this_.nextUShort()
    
    def next(self):
        return boxIntrinsic(_this_.next())
    
    def nextUShort(self):
        pass
    
    def hasNext(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def _ULong___get_data__impl_(this):
    return data

class Companion:
    def _init_():
        Companion_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_c5c2a84
        _this_.MIN_VALUE = ULong(Long(0, 0))
        _this_.MAX_VALUE = ULong(Long(-1, -1))
        _this_.SIZE_BYTES = 8
        _this_.SIZE_BITS = 64
    
    def _get_MIN_VALUE_(self):
        return MIN_VALUE
    
    def _get_MAX_VALUE_(self):
        return MAX_VALUE
    
    def _get_SIZE_BYTES_(self):
        return SIZE_BYTES
    
    def _get_SIZE_BITS_(self):
        return SIZE_BITS
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_5ab315ed = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_73959127
    
    return Companion_instance

def ULong__compareTo_impl(this, other):
    tmp0_compareTo_0 = ULong(toLong(_UByte___get_data__impl_(other))._and(Long(255, 0)))
    return ulongCompare(_ULong___get_data__impl_(this), _ULong___get_data__impl_(tmp0_compareTo_0))

def ULong__compareTo_impl(this, other):
    tmp0_compareTo_0 = ULong(toLong(_UShort___get_data__impl_(other))._and(Long(65535, 0)))
    return ulongCompare(_ULong___get_data__impl_(this), _ULong___get_data__impl_(tmp0_compareTo_0))

def ULong__compareTo_impl(this, other):
    tmp0_compareTo_0 = ULong(toLong(_UInt___get_data__impl_(other))._and(Long(-1, 0)))
    return ulongCompare(_ULong___get_data__impl_(this), _ULong___get_data__impl_(tmp0_compareTo_0))

def ULong__compareTo_impl(this, other):
    return ulongCompare(_ULong___get_data__impl_(this), _ULong___get_data__impl_(other))

def ULong__compareTo_impl(this, other):
    tmp = unboxIntrinsic(this)
    return ULong__compareTo_impl(tmp, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6acdbe95)

def ULong__plus_impl(this, other):
    tmp0_plus_0 = ULong(toLong(_UByte___get_data__impl_(other))._and(Long(255, 0)))
    return ULong(_ULong___get_data__impl_(this).plus(_ULong___get_data__impl_(tmp0_plus_0)))

def ULong__plus_impl(this, other):
    tmp0_plus_0 = ULong(toLong(_UShort___get_data__impl_(other))._and(Long(65535, 0)))
    return ULong(_ULong___get_data__impl_(this).plus(_ULong___get_data__impl_(tmp0_plus_0)))

def ULong__plus_impl(this, other):
    tmp0_plus_0 = ULong(toLong(_UInt___get_data__impl_(other))._and(Long(-1, 0)))
    return ULong(_ULong___get_data__impl_(this).plus(_ULong___get_data__impl_(tmp0_plus_0)))

def ULong__plus_impl(this, other):
    return ULong(_ULong___get_data__impl_(this).plus(_ULong___get_data__impl_(other)))

def ULong__minus_impl(this, other):
    tmp0_minus_0 = ULong(toLong(_UByte___get_data__impl_(other))._and(Long(255, 0)))
    return ULong(_ULong___get_data__impl_(this).minus(_ULong___get_data__impl_(tmp0_minus_0)))

def ULong__minus_impl(this, other):
    tmp0_minus_0 = ULong(toLong(_UShort___get_data__impl_(other))._and(Long(65535, 0)))
    return ULong(_ULong___get_data__impl_(this).minus(_ULong___get_data__impl_(tmp0_minus_0)))

def ULong__minus_impl(this, other):
    tmp0_minus_0 = ULong(toLong(_UInt___get_data__impl_(other))._and(Long(-1, 0)))
    return ULong(_ULong___get_data__impl_(this).minus(_ULong___get_data__impl_(tmp0_minus_0)))

def ULong__minus_impl(this, other):
    return ULong(_ULong___get_data__impl_(this).minus(_ULong___get_data__impl_(other)))

def ULong__times_impl(this, other):
    tmp0_times_0 = ULong(toLong(_UByte___get_data__impl_(other))._and(Long(255, 0)))
    return ULong(_ULong___get_data__impl_(this).times(_ULong___get_data__impl_(tmp0_times_0)))

def ULong__times_impl(this, other):
    tmp0_times_0 = ULong(toLong(_UShort___get_data__impl_(other))._and(Long(65535, 0)))
    return ULong(_ULong___get_data__impl_(this).times(_ULong___get_data__impl_(tmp0_times_0)))

def ULong__times_impl(this, other):
    tmp0_times_0 = ULong(toLong(_UInt___get_data__impl_(other))._and(Long(-1, 0)))
    return ULong(_ULong___get_data__impl_(this).times(_ULong___get_data__impl_(tmp0_times_0)))

def ULong__times_impl(this, other):
    return ULong(_ULong___get_data__impl_(this).times(_ULong___get_data__impl_(other)))

def ULong__div_impl(this, other):
    tmp0_div_0 = ULong(toLong(_UByte___get_data__impl_(other))._and(Long(255, 0)))
    return ulongDivide(this, tmp0_div_0)

def ULong__div_impl(this, other):
    tmp0_div_0 = ULong(toLong(_UShort___get_data__impl_(other))._and(Long(65535, 0)))
    return ulongDivide(this, tmp0_div_0)

def ULong__div_impl(this, other):
    tmp0_div_0 = ULong(toLong(_UInt___get_data__impl_(other))._and(Long(-1, 0)))
    return ulongDivide(this, tmp0_div_0)

def ULong__div_impl(this, other):
    return ulongDivide(this, other)

def ULong__rem_impl(this, other):
    tmp0_rem_0 = ULong(toLong(_UByte___get_data__impl_(other))._and(Long(255, 0)))
    return ulongRemainder(this, tmp0_rem_0)

def ULong__rem_impl(this, other):
    tmp0_rem_0 = ULong(toLong(_UShort___get_data__impl_(other))._and(Long(65535, 0)))
    return ulongRemainder(this, tmp0_rem_0)

def ULong__rem_impl(this, other):
    tmp0_rem_0 = ULong(toLong(_UInt___get_data__impl_(other))._and(Long(-1, 0)))
    return ulongRemainder(this, tmp0_rem_0)

def ULong__rem_impl(this, other):
    return ulongRemainder(this, other)

def ULong__inc_impl(this):
    return ULong(_ULong___get_data__impl_(this).inc())

def ULong__dec_impl(this):
    return ULong(_ULong___get_data__impl_(this).dec())

def ULong__rangeTo_impl(this, other):
    return ULongRange(this, other)

def ULong__shl_impl(this, bitCount):
    return ULong(_ULong___get_data__impl_(this).shl(bitCount))

def ULong__shr_impl(this, bitCount):
    return ULong(_ULong___get_data__impl_(this).ushr(bitCount))

def ULong__and_impl(this, other):
    return ULong(_ULong___get_data__impl_(this)._and(_ULong___get_data__impl_(other)))

def ULong__or_impl(this, other):
    return ULong(_ULong___get_data__impl_(this)._or(_ULong___get_data__impl_(other)))

def ULong__xor_impl(this, other):
    return ULong(_ULong___get_data__impl_(this).xor(_ULong___get_data__impl_(other)))

def ULong__inv_impl(this):
    return ULong(_ULong___get_data__impl_(this).inv())

def ULong__toByte_impl(this):
    return _ULong___get_data__impl_(this).toByte()

def ULong__toShort_impl(this):
    return _ULong___get_data__impl_(this).toShort()

def ULong__toInt_impl(this):
    return _ULong___get_data__impl_(this).toInt()

def ULong__toLong_impl(this):
    return _ULong___get_data__impl_(this)

def ULong__toUByte_impl(this):
    tmp0_toUByte_0 = _ULong___get_data__impl_(this)
    return UByte(tmp0_toUByte_0.toByte())

def ULong__toUShort_impl(this):
    tmp0_toUShort_0 = _ULong___get_data__impl_(this)
    return UShort(tmp0_toUShort_0.toShort())

def ULong__toUInt_impl(this):
    tmp0_toUInt_0 = _ULong___get_data__impl_(this)
    return UInt(tmp0_toUInt_0.toInt())

def ULong__toULong_impl(this):
    return this

def ULong__toFloat_impl(this):
    return kotlin_Float(ulongToDouble(_ULong___get_data__impl_(this)))

def ULong__toDouble_impl(this):
    return ulongToDouble(_ULong___get_data__impl_(this))

def ULong__toString_impl(this):
    return ulongToString(_ULong___get_data__impl_(this))

def ULong__hashCode_impl(this):
    return data.hashCode()

def ULong__equals_impl(this, other):
    if jsNot(jsInstanceOf(other, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_408bb173
    
    if True:
        pass
    
    tmp0_other_with_cast = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2bfd3970
    if jsNot(data.equals(data)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_7fb8d720
    
    return True

class ULong:
    def _init_(data):
        Companion_getInstance()
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_6f2b608e
        _this_.data = data
    
    def compareTo(self, other):
        return ULong__compareTo_impl(unboxIntrinsic(_this_), other)
    
    def compareTo(self, other):
        return ULong__compareTo_impl(_this_, other)
    
    def toString(self):
        return ULong__toString_impl(unboxIntrinsic(_this_))
    
    def hashCode(self):
        return ULong__hashCode_impl(unboxIntrinsic(_this_))
    
    def equals(self, other):
        return ULong__equals_impl(unboxIntrinsic(_this_), other)
    

def toULong():
    return ULong(_this_)

def toULong():
    return ULong(toLong(_this_))

def toULong():
    return doubleToULong(_this_)

def toULong():
    return doubleToULong(kotlin_Double(_this_))

def toULong():
    return ULong(toLong(_this_))

def toULong():
    return ULong(toLong(_this_))

def _get_array_(_this):
    return array

def _set_index_(_this, _set___):
    _this.index = _set___

def _get_index_(_this):
    return index

def _ULongArray___get_storage__impl_(this):
    return storage

def _ULongArray___init__impl_(size):
    tmp = ULongArray(longArray(size))
    return tmp

def ULongArray__get_impl(this, index):
    tmp0_toULong_0 = jsArrayGet(_ULongArray___get_storage__impl_(this), index)
    return ULong(tmp0_toULong_0)

def ULongArray__set_impl(this, index, value):
    tmp = _ULongArray___get_storage__impl_(this)
    jsArraySet(tmp, index, _ULong___get_data__impl_(value))

def _ULongArray___get_size__impl_(this):
    return jsArrayLength(_ULongArray___get_storage__impl_(this))

def ULongArray__iterator_impl(this):
    return Iterator(_ULongArray___get_storage__impl_(this))

class Iterator:
    def _init_(array):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_ee7a538
        _this_.array = array
        _this_.index = 0
    
    def hasNext(self):
        return jsLt(index, jsArrayLength(array))
    
    def nextULong(self):
        tmp
        if jsLt(index, jsArrayLength(array)):
            tmp0_this = _this_
            tmp1 = index
            tmp0_this.index = jsBitOr(jsPlus(tmp1, 1), 0)
            tmp0_toULong_0 = jsArrayGet(array, tmp1)
            tmp = ULong(tmp0_toULong_0)
        
        if True:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_2c1b10f2
        
        return tmp
    
    def next(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def ULongArray__contains_impl(this, element):
    tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2e4f3c14
    if jsNot(jsInstanceOf(tmp, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_2a3c3a04
    
    if True:
        pass
    
    tmp = _ULongArray___get_storage__impl_(this)
    return contains(_ULong___get_data__impl_(element))

def ULongArray__contains_impl(this, element):
    if jsNot(jsInstanceOf(element, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_4556a9a7
    
    if True:
        pass
    
    tmp = unboxIntrinsic(this)
    return ULongArray__contains_impl(tmp, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_61be6b03)

def ULongArray__containsAll_impl(this, elements):
    tmp_ret_0
    visitDoWhileLoop_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_5db7419c
    return tmp_ret_0

def ULongArray__containsAll_impl(this, elements):
    return ULongArray__containsAll_impl(unboxIntrinsic(this), elements)

def ULongArray__isEmpty_impl(this):
    return jsEqeqeq(jsArrayLength(_ULongArray___get_storage__impl_(this)), 0)

def ULongArray__toString_impl(this):
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_45a1f1d0

def ULongArray__hashCode_impl(this):
    return hashCode(storage)

def ULongArray__equals_impl(this, other):
    if jsNot(jsInstanceOf(other, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_2fda92e0
    
    if True:
        pass
    
    tmp0_other_with_cast = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_54a1be3a
    if jsNot(equals(storage, storage)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_4fa3bebe
    
    return True

class ULongArray:
    def _init_(storage):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_1e6cd1c
        _this_.storage = storage
    
    def _get_size_(self):
        return _ULongArray___get_size__impl_(unboxIntrinsic(_this_))
    
    def iterator(self):
        return ULongArray__iterator_impl(unboxIntrinsic(_this_))
    
    def contains(self, element):
        return ULongArray__contains_impl(unboxIntrinsic(_this_), element)
    
    def contains(self, element):
        return ULongArray__contains_impl(_this_, element)
    
    def containsAll(self, elements):
        return ULongArray__containsAll_impl(unboxIntrinsic(_this_), elements)
    
    def containsAll(self, elements):
        return ULongArray__containsAll_impl(_this_, elements)
    
    def isEmpty(self):
        return ULongArray__isEmpty_impl(unboxIntrinsic(_this_))
    
    def toString(self):
        return ULongArray__toString_impl(unboxIntrinsic(_this_))
    
    def hashCode(self):
        return ULongArray__hashCode_impl(unboxIntrinsic(_this_))
    
    def equals(self, other):
        return ULongArray__equals_impl(unboxIntrinsic(_this_), other)
    

class Companion:
    def _init_():
        Companion_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_30b0d5a7
        _this_.EMPTY = ULongRange(ULong(Long(-1, -1)), ULong(Long(0, 0)))
    
    def _get_EMPTY_(self):
        return EMPTY
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_36840e6c = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_24411981
    
    return Companion_instance

class ULongRange:
    def _init_(start, endInclusive):
        Companion_getInstance()
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_27f8f1cc
    
    def _get_start_(self):
        return _this_._get_first_()
    
    def _get_start_(self):
        return boxIntrinsic(_this_._get_start_())
    
    def _get_endInclusive_(self):
        return _this_._get_last_()
    
    def _get_endInclusive_(self):
        return boxIntrinsic(_this_._get_endInclusive_())
    
    def contains(self, value):
        tmp
        tmp0_compareTo_0 = _this_._get_first_()
        if jsLtEq(ulongCompare(_ULong___get_data__impl_(tmp0_compareTo_0), _ULong___get_data__impl_(value)), 0):
            tmp1_compareTo_0 = _this_._get_last_()
            tmp = jsLtEq(ulongCompare(_ULong___get_data__impl_(value), _ULong___get_data__impl_(tmp1_compareTo_0)), 0)
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def contains(self, value):
        return _this_.contains(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_5747a07c)
    
    def isEmpty(self):
        tmp0_compareTo_0 = _this_._get_first_()
        tmp1_compareTo_0 = _this_._get_last_()
        return jsGt(ulongCompare(_ULong___get_data__impl_(tmp0_compareTo_0), _ULong___get_data__impl_(tmp1_compareTo_0)), 0)
    
    def equals(self, other):
        tmp
        if jsInstanceOf(other, jsClass()):
            tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3e2e653d
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def hashCode(self):
        tmp
        if _this_.isEmpty():
            tmp = -1
        
        if True:
            tmp2_xor_0 = _this_._get_first_()
            tmp0_shr_0 = _this_._get_first_()
            tmp1_shr_0 = 32
            tmp3_xor_0 = ULong(_ULong___get_data__impl_(tmp0_shr_0).ushr(tmp1_shr_0))
            tmp4_toInt_0 = ULong(_ULong___get_data__impl_(tmp2_xor_0).xor(_ULong___get_data__impl_(tmp3_xor_0)))
            tmp = imul(31, _ULong___get_data__impl_(tmp4_toInt_0).toInt())
            tmp7_xor_0 = _this_._get_last_()
            tmp5_shr_0 = _this_._get_last_()
            tmp6_shr_0 = 32
            tmp8_xor_0 = ULong(_ULong___get_data__impl_(tmp5_shr_0).ushr(tmp6_shr_0))
            tmp9_toInt_0 = ULong(_ULong___get_data__impl_(tmp7_xor_0).xor(_ULong___get_data__impl_(tmp8_xor_0)))
            tmp = jsBitOr(jsPlus(tmp, _ULong___get_data__impl_(tmp9_toInt_0).toInt()), 0)
        
        return tmp
    
    def toString(self):
        return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_30ee00f6
    
    def _get_first_(self):
        pass
    
    def _get_last_(self):
        pass
    
    def _get_step_(self):
        pass
    
    def iterator(self):
        pass
    

class Companion:
    def _init_():
        Companion_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_74eae1e0
    
    def fromClosedRange(self, rangeStart, rangeEnd, step):
        return ULongProgression(rangeStart, rangeEnd, step)
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_3486cb21 = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_356be87
    
    return Companion_instance

class ULongProgression:
    def _init_(start, endInclusive, step):
        Companion_getInstance()
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_765e5a55
        if step.equals(Long(0, 0)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_1a180d5b
        
        if step.equals(Long(0, -2147483648)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_f04ed21
        
        _this_.first = start
        _this_.last = getProgressionLastElement(start, endInclusive, step)
        _this_.step = step
    
    def _get_first_(self):
        return first
    
    def _get_last_(self):
        return last
    
    def _get_step_(self):
        return step
    
    def iterator(self):
        return ULongProgressionIterator(first, last, step)
    
    def isEmpty(self):
        tmp
        if jsGt(step.compareTo(Long(0, 0)), 0):
            tmp0_compareTo_0 = first
            tmp1_compareTo_0 = last
            tmp = jsGt(ulongCompare(_ULong___get_data__impl_(tmp0_compareTo_0), _ULong___get_data__impl_(tmp1_compareTo_0)), 0)
        
        if True:
            tmp2_compareTo_0 = first
            tmp3_compareTo_0 = last
            tmp = jsLt(ulongCompare(_ULong___get_data__impl_(tmp2_compareTo_0), _ULong___get_data__impl_(tmp3_compareTo_0)), 0)
        
        return tmp
    
    def equals(self, other):
        tmp
        if jsInstanceOf(other, jsClass()):
            tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_13428b9d
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def hashCode(self):
        tmp
        if _this_.isEmpty():
            tmp = -1
        
        if True:
            tmp2_xor_0 = first
            tmp0_shr_0 = first
            tmp1_shr_0 = 32
            tmp3_xor_0 = ULong(_ULong___get_data__impl_(tmp0_shr_0).ushr(tmp1_shr_0))
            tmp4_toInt_0 = ULong(_ULong___get_data__impl_(tmp2_xor_0).xor(_ULong___get_data__impl_(tmp3_xor_0)))
            tmp = imul(31, _ULong___get_data__impl_(tmp4_toInt_0).toInt())
            tmp7_xor_0 = last
            tmp5_shr_0 = last
            tmp6_shr_0 = 32
            tmp8_xor_0 = ULong(_ULong___get_data__impl_(tmp5_shr_0).ushr(tmp6_shr_0))
            tmp9_toInt_0 = ULong(_ULong___get_data__impl_(tmp7_xor_0).xor(_ULong___get_data__impl_(tmp8_xor_0)))
            tmp = jsBitOr(jsPlus(imul(31, jsBitOr(jsPlus(tmp, _ULong___get_data__impl_(tmp9_toInt_0).toInt()), 0)), step.xor(step.ushr(32)).toInt()), 0)
        
        return tmp
    
    def toString(self):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_28feec4f
    

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
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_149ef64a
        _this_.finalElement = last
        tmp = _this_
        tmp
        if jsGt(step.compareTo(Long(0, 0)), 0):
            tmp = jsLtEq(ulongCompare(_ULong___get_data__impl_(first), _ULong___get_data__impl_(last)), 0)
        
        if True:
            tmp = jsGtEq(ulongCompare(_ULong___get_data__impl_(first), _ULong___get_data__impl_(last)), 0)
        
        tmp.hasNext = tmp
        tmp = _this_
        tmp.step = ULong(step)
        _this_.next = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_41d7b4cf
    
    def hasNext(self):
        return hasNext
    
    def nextULong(self):
        value = next
        if equals(boxIntrinsic(value), boxIntrinsic(finalElement)):
            if jsNot(hasNext):
                visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_519e14f6
            
            _this_.hasNext = False
        
        if True:
            tmp0_this = _this_
            tmp = tmp0_this
            tmp0_plus_0 = next
            tmp1_plus_0 = step
            tmp.next = ULong(_ULong___get_data__impl_(tmp0_plus_0).plus(_ULong___get_data__impl_(tmp1_plus_0)))
        
        return value
    
    def next(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def getProgressionLastElement(start, end, step):
    tmp
    if jsGt(step, 0):
        tmp
        if jsGtEq(uintCompare(_UInt___get_data__impl_(start), _UInt___get_data__impl_(end)), 0):
            tmp = end
        
        if True:
            if True:
                tmp0_minus_0 = differenceModulo(end, start, UInt(step))
                tmp = UInt(jsBitOr(jsMinus(_UInt___get_data__impl_(end), _UInt___get_data__impl_(tmp0_minus_0)), 0))
            
        
        tmp = tmp
    
    if jsLt(step, 0):
        tmp
        if jsLtEq(uintCompare(_UInt___get_data__impl_(start), _UInt___get_data__impl_(end)), 0):
            tmp = end
        
        if True:
            if True:
                tmp1_toUInt_0 = jsBitOr(jsUnaryMinus(step), 0)
                tmp2_plus_0 = differenceModulo(start, end, UInt(tmp1_toUInt_0))
                tmp = UInt(jsBitOr(jsPlus(_UInt___get_data__impl_(end), _UInt___get_data__impl_(tmp2_plus_0)), 0))
            
        
        tmp = tmp
    
    if True:
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_2044f708
    
    return tmp

def getProgressionLastElement(start, end, step):
    tmp
    if jsGt(step.compareTo(Long(0, 0)), 0):
        tmp
        if jsGtEq(ulongCompare(_ULong___get_data__impl_(start), _ULong___get_data__impl_(end)), 0):
            tmp = end
        
        if True:
            if True:
                tmp0_minus_0 = differenceModulo(end, start, ULong(step))
                tmp = ULong(_ULong___get_data__impl_(end).minus(_ULong___get_data__impl_(tmp0_minus_0)))
            
        
        tmp = tmp
    
    if jsLt(step.compareTo(Long(0, 0)), 0):
        tmp
        if jsLtEq(ulongCompare(_ULong___get_data__impl_(start), _ULong___get_data__impl_(end)), 0):
            tmp = end
        
        if True:
            if True:
                tmp1_toULong_0 = step.unaryMinus()
                tmp2_plus_0 = differenceModulo(start, end, ULong(tmp1_toULong_0))
                tmp = ULong(_ULong___get_data__impl_(end).plus(_ULong___get_data__impl_(tmp2_plus_0)))
            
        
        tmp = tmp
    
    if True:
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_5e38329d
    
    return tmp

def differenceModulo(a, b, c):
    ac = uintRemainder(a, c)
    bc = uintRemainder(b, c)
    tmp
    if jsGtEq(uintCompare(_UInt___get_data__impl_(ac), _UInt___get_data__impl_(bc)), 0):
        tmp = UInt(jsBitOr(jsMinus(_UInt___get_data__impl_(ac), _UInt___get_data__impl_(bc)), 0))
    
    if True:
        if True:
            tmp0_plus_0 = UInt(jsBitOr(jsMinus(_UInt___get_data__impl_(ac), _UInt___get_data__impl_(bc)), 0))
            tmp = UInt(jsBitOr(jsPlus(_UInt___get_data__impl_(tmp0_plus_0), _UInt___get_data__impl_(c)), 0))
        
    
    return tmp

def differenceModulo(a, b, c):
    ac = ulongRemainder(a, c)
    bc = ulongRemainder(b, c)
    tmp
    if jsGtEq(ulongCompare(_ULong___get_data__impl_(ac), _ULong___get_data__impl_(bc)), 0):
        tmp = ULong(_ULong___get_data__impl_(ac).minus(_ULong___get_data__impl_(bc)))
    
    if True:
        if True:
            tmp0_plus_0 = ULong(_ULong___get_data__impl_(ac).minus(_ULong___get_data__impl_(bc)))
            tmp = ULong(_ULong___get_data__impl_(tmp0_plus_0).plus(_ULong___get_data__impl_(c)))
        
    
    return tmp

def _UShort___get_data__impl_(this):
    return data

class Companion:
    def _init_():
        Companion_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_72ea5674
        _this_.MIN_VALUE = UShort(visitConst_other_Short)
        _this_.MAX_VALUE = UShort(visitConst_other_Short)
        _this_.SIZE_BYTES = 2
        _this_.SIZE_BITS = 16
    
    def _get_MIN_VALUE_(self):
        return MIN_VALUE
    
    def _get_MAX_VALUE_(self):
        return MAX_VALUE
    
    def _get_SIZE_BYTES_(self):
        return SIZE_BYTES
    
    def _get_SIZE_BITS_(self):
        return SIZE_BITS
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_4f00ee48 = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_27bcfd19
    
    return Companion_instance

def UShort__compareTo_impl(this, other):
    tmp = jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535)
    return compareTo(tmp, jsBitAnd(kotlin_Int(_UByte___get_data__impl_(other)), 255))

def UShort__compareTo_impl(this, other):
    tmp = jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535)
    return compareTo(tmp, jsBitAnd(kotlin_Int(_UShort___get_data__impl_(other)), 65535))

def UShort__compareTo_impl(this, other):
    tmp = unboxIntrinsic(this)
    return UShort__compareTo_impl(tmp, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_ab3cd69)

def UShort__compareTo_impl(this, other):
    tmp0_compareTo_0 = UInt(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535))
    return uintCompare(_UInt___get_data__impl_(tmp0_compareTo_0), _UInt___get_data__impl_(other))

def UShort__compareTo_impl(this, other):
    tmp0_compareTo_0 = ULong(toLong(_UShort___get_data__impl_(this))._and(Long(65535, 0)))
    return ulongCompare(_ULong___get_data__impl_(tmp0_compareTo_0), _ULong___get_data__impl_(other))

def UShort__plus_impl(this, other):
    tmp0_plus_0 = UInt(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535))
    tmp1_plus_0 = UInt(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(other)), 255))
    return UInt(jsBitOr(jsPlus(_UInt___get_data__impl_(tmp0_plus_0), _UInt___get_data__impl_(tmp1_plus_0)), 0))

def UShort__plus_impl(this, other):
    tmp0_plus_0 = UInt(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535))
    tmp1_plus_0 = UInt(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(other)), 65535))
    return UInt(jsBitOr(jsPlus(_UInt___get_data__impl_(tmp0_plus_0), _UInt___get_data__impl_(tmp1_plus_0)), 0))

def UShort__plus_impl(this, other):
    tmp0_plus_0 = UInt(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535))
    return UInt(jsBitOr(jsPlus(_UInt___get_data__impl_(tmp0_plus_0), _UInt___get_data__impl_(other)), 0))

def UShort__plus_impl(this, other):
    tmp0_plus_0 = ULong(toLong(_UShort___get_data__impl_(this))._and(Long(65535, 0)))
    return ULong(_ULong___get_data__impl_(tmp0_plus_0).plus(_ULong___get_data__impl_(other)))

def UShort__minus_impl(this, other):
    tmp0_minus_0 = UInt(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535))
    tmp1_minus_0 = UInt(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(other)), 255))
    return UInt(jsBitOr(jsMinus(_UInt___get_data__impl_(tmp0_minus_0), _UInt___get_data__impl_(tmp1_minus_0)), 0))

def UShort__minus_impl(this, other):
    tmp0_minus_0 = UInt(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535))
    tmp1_minus_0 = UInt(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(other)), 65535))
    return UInt(jsBitOr(jsMinus(_UInt___get_data__impl_(tmp0_minus_0), _UInt___get_data__impl_(tmp1_minus_0)), 0))

def UShort__minus_impl(this, other):
    tmp0_minus_0 = UInt(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535))
    return UInt(jsBitOr(jsMinus(_UInt___get_data__impl_(tmp0_minus_0), _UInt___get_data__impl_(other)), 0))

def UShort__minus_impl(this, other):
    tmp0_minus_0 = ULong(toLong(_UShort___get_data__impl_(this))._and(Long(65535, 0)))
    return ULong(_ULong___get_data__impl_(tmp0_minus_0).minus(_ULong___get_data__impl_(other)))

def UShort__times_impl(this, other):
    tmp0_times_0 = UInt(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535))
    tmp1_times_0 = UInt(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(other)), 255))
    return UInt(imul(_UInt___get_data__impl_(tmp0_times_0), _UInt___get_data__impl_(tmp1_times_0)))

def UShort__times_impl(this, other):
    tmp0_times_0 = UInt(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535))
    tmp1_times_0 = UInt(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(other)), 65535))
    return UInt(imul(_UInt___get_data__impl_(tmp0_times_0), _UInt___get_data__impl_(tmp1_times_0)))

def UShort__times_impl(this, other):
    tmp0_times_0 = UInt(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535))
    return UInt(imul(_UInt___get_data__impl_(tmp0_times_0), _UInt___get_data__impl_(other)))

def UShort__times_impl(this, other):
    tmp0_times_0 = ULong(toLong(_UShort___get_data__impl_(this))._and(Long(65535, 0)))
    return ULong(_ULong___get_data__impl_(tmp0_times_0).times(_ULong___get_data__impl_(other)))

def UShort__div_impl(this, other):
    tmp0_div_0 = UInt(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535))
    tmp1_div_0 = UInt(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(other)), 255))
    return uintDivide(tmp0_div_0, tmp1_div_0)

def UShort__div_impl(this, other):
    tmp0_div_0 = UInt(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535))
    tmp1_div_0 = UInt(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(other)), 65535))
    return uintDivide(tmp0_div_0, tmp1_div_0)

def UShort__div_impl(this, other):
    tmp0_div_0 = UInt(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535))
    return uintDivide(tmp0_div_0, other)

def UShort__div_impl(this, other):
    tmp0_div_0 = ULong(toLong(_UShort___get_data__impl_(this))._and(Long(65535, 0)))
    return ulongDivide(tmp0_div_0, other)

def UShort__rem_impl(this, other):
    tmp0_rem_0 = UInt(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535))
    tmp1_rem_0 = UInt(jsBitAnd(kotlin_Int(_UByte___get_data__impl_(other)), 255))
    return uintRemainder(tmp0_rem_0, tmp1_rem_0)

def UShort__rem_impl(this, other):
    tmp0_rem_0 = UInt(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535))
    tmp1_rem_0 = UInt(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(other)), 65535))
    return uintRemainder(tmp0_rem_0, tmp1_rem_0)

def UShort__rem_impl(this, other):
    tmp0_rem_0 = UInt(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535))
    return uintRemainder(tmp0_rem_0, other)

def UShort__rem_impl(this, other):
    tmp0_rem_0 = ULong(toLong(_UShort___get_data__impl_(this))._and(Long(65535, 0)))
    return ulongRemainder(tmp0_rem_0, other)

def UShort__inc_impl(this):
    return UShort(numberToShort(jsPlus(_UShort___get_data__impl_(this), 1)))

def UShort__dec_impl(this):
    return UShort(numberToShort(jsMinus(_UShort___get_data__impl_(this), 1)))

def UShort__rangeTo_impl(this, other):
    tmp = UInt(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535))
    return UIntRange(tmp, UInt(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(other)), 65535)))

def UShort__and_impl(this, other):
    tmp0_and_0 = _UShort___get_data__impl_(this)
    tmp1_and_0 = _UShort___get_data__impl_(other)
    return UShort(toShort(jsBitAnd(kotlin_Int(tmp0_and_0), kotlin_Int(tmp1_and_0))))

def UShort__or_impl(this, other):
    tmp0_or_0 = _UShort___get_data__impl_(this)
    tmp1_or_0 = _UShort___get_data__impl_(other)
    return UShort(toShort(jsBitOr(kotlin_Int(tmp0_or_0), kotlin_Int(tmp1_or_0))))

def UShort__xor_impl(this, other):
    tmp0_xor_0 = _UShort___get_data__impl_(this)
    tmp1_xor_0 = _UShort___get_data__impl_(other)
    return UShort(toShort(jsBitXor(kotlin_Int(tmp0_xor_0), kotlin_Int(tmp1_xor_0))))

def UShort__inv_impl(this):
    tmp0_inv_0 = _UShort___get_data__impl_(this)
    return UShort(toShort(jsBitNot(kotlin_Int(tmp0_inv_0))))

def UShort__toByte_impl(this):
    return toByte(_UShort___get_data__impl_(this))

def UShort__toShort_impl(this):
    return _UShort___get_data__impl_(this)

def UShort__toInt_impl(this):
    return jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535)

def UShort__toLong_impl(this):
    return toLong(_UShort___get_data__impl_(this))._and(Long(65535, 0))

def UShort__toUByte_impl(this):
    tmp0_toUByte_0 = _UShort___get_data__impl_(this)
    return UByte(toByte(tmp0_toUByte_0))

def UShort__toUShort_impl(this):
    return this

def UShort__toUInt_impl(this):
    return UInt(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535))

def UShort__toULong_impl(this):
    return ULong(toLong(_UShort___get_data__impl_(this))._and(Long(65535, 0)))

def UShort__toFloat_impl(this):
    return kotlin_Float(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535))

def UShort__toDouble_impl(this):
    return kotlin_Double(jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535))

def UShort__toString_impl(this):
    return jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535).toString()

def UShort__hashCode_impl(this):
    return data

def UShort__equals_impl(this, other):
    if jsNot(jsInstanceOf(other, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_6012bee8
    
    if True:
        pass
    
    tmp0_other_with_cast = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6982bcf4
    if jsNot(jsEqeqeq(data, data)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_13cec4ff
    
    return True

class UShort:
    def _init_(data):
        Companion_getInstance()
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_6bab373c
        _this_.data = data
    
    def compareTo(self, other):
        return UShort__compareTo_impl(unboxIntrinsic(_this_), other)
    
    def compareTo(self, other):
        return UShort__compareTo_impl(_this_, other)
    
    def toString(self):
        return UShort__toString_impl(unboxIntrinsic(_this_))
    
    def hashCode(self):
        return UShort__hashCode_impl(unboxIntrinsic(_this_))
    
    def equals(self, other):
        return UShort__equals_impl(unboxIntrinsic(_this_), other)
    

def toUShort():
    return UShort(toShort(_this_))

def toUShort():
    return UShort(_this_.toShort())

def toUShort():
    return UShort(_this_)

def _get_array_(_this):
    return array

def _set_index_(_this, _set___):
    _this.index = _set___

def _get_index_(_this):
    return index

def _UShortArray___get_storage__impl_(this):
    return storage

def _UShortArray___init__impl_(size):
    tmp = UShortArray(int16Array(size))
    return tmp

def UShortArray__get_impl(this, index):
    tmp0_toUShort_0 = jsArrayGet(_UShortArray___get_storage__impl_(this), index)
    return UShort(tmp0_toUShort_0)

def UShortArray__set_impl(this, index, value):
    tmp = _UShortArray___get_storage__impl_(this)
    jsArraySet(tmp, index, _UShort___get_data__impl_(value))

def _UShortArray___get_size__impl_(this):
    return jsArrayLength(_UShortArray___get_storage__impl_(this))

def UShortArray__iterator_impl(this):
    return Iterator(_UShortArray___get_storage__impl_(this))

class Iterator:
    def _init_(array):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_763a72da
        _this_.array = array
        _this_.index = 0
    
    def hasNext(self):
        return jsLt(index, jsArrayLength(array))
    
    def nextUShort(self):
        tmp
        if jsLt(index, jsArrayLength(array)):
            tmp0_this = _this_
            tmp1 = index
            tmp0_this.index = jsBitOr(jsPlus(tmp1, 1), 0)
            tmp0_toUShort_0 = jsArrayGet(array, tmp1)
            tmp = UShort(tmp0_toUShort_0)
        
        if True:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_4d6f951a
        
        return tmp
    
    def next(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def UShortArray__contains_impl(this, element):
    tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_7134cb8f
    if jsNot(jsInstanceOf(tmp, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_77a14911
    
    if True:
        pass
    
    tmp = _UShortArray___get_storage__impl_(this)
    return contains(_UShort___get_data__impl_(element))

def UShortArray__contains_impl(this, element):
    if jsNot(jsInstanceOf(element, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_45583680
    
    if True:
        pass
    
    tmp = unboxIntrinsic(this)
    return UShortArray__contains_impl(tmp, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2a6dab20)

def UShortArray__containsAll_impl(this, elements):
    tmp_ret_0
    visitDoWhileLoop_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_7aff1fa3
    return tmp_ret_0

def UShortArray__containsAll_impl(this, elements):
    return UShortArray__containsAll_impl(unboxIntrinsic(this), elements)

def UShortArray__isEmpty_impl(this):
    return jsEqeqeq(jsArrayLength(_UShortArray___get_storage__impl_(this)), 0)

def UShortArray__toString_impl(this):
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_28af6afe

def UShortArray__hashCode_impl(this):
    return hashCode(storage)

def UShortArray__equals_impl(this, other):
    if jsNot(jsInstanceOf(other, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_4f378d7e
    
    if True:
        pass
    
    tmp0_other_with_cast = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6831b1f6
    if jsNot(equals(storage, storage)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_2c40e456
    
    return True

class UShortArray:
    def _init_(storage):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_19370af1
        _this_.storage = storage
    
    def _get_size_(self):
        return _UShortArray___get_size__impl_(unboxIntrinsic(_this_))
    
    def iterator(self):
        return UShortArray__iterator_impl(unboxIntrinsic(_this_))
    
    def contains(self, element):
        return UShortArray__contains_impl(unboxIntrinsic(_this_), element)
    
    def contains(self, element):
        return UShortArray__contains_impl(_this_, element)
    
    def containsAll(self, elements):
        return UShortArray__containsAll_impl(unboxIntrinsic(_this_), elements)
    
    def containsAll(self, elements):
        return UShortArray__containsAll_impl(_this_, elements)
    
    def isEmpty(self):
        return UShortArray__isEmpty_impl(unboxIntrinsic(_this_))
    
    def toString(self):
        return UShortArray__toString_impl(unboxIntrinsic(_this_))
    
    def hashCode(self):
        return UShortArray__hashCode_impl(unboxIntrinsic(_this_))
    
    def equals(self, other):
        return UShortArray__equals_impl(unboxIntrinsic(_this_), other)
    

def uintCompare(v1, v2):
    return compareTo(jsBitXor(v1, MIN_VALUE), jsBitXor(v2, MIN_VALUE))

def uintDivide(v1, v2):
    tmp = toLong(_UInt___get_data__impl_(v1))._and(Long(-1, 0))
    tmp0_toUInt_0 = tmp.div(toLong(_UInt___get_data__impl_(v2))._and(Long(-1, 0)))
    return UInt(tmp0_toUInt_0.toInt())

def uintRemainder(v1, v2):
    tmp = toLong(_UInt___get_data__impl_(v1))._and(Long(-1, 0))
    tmp0_toUInt_0 = tmp.rem(toLong(_UInt___get_data__impl_(v2))._and(Long(-1, 0)))
    return UInt(tmp0_toUInt_0.toInt())

def uintToDouble(v):
    return jsPlus(kotlin_Double(jsBitAnd(v, MAX_VALUE)), jsMult(kotlin_Double(jsBitShiftL(jsBitShiftRU(v, 31), 30)), 2))

def ulongCompare(v1, v2):
    return v1.xor(Long(0, -2147483648)).compareTo(v2.xor(Long(0, -2147483648)))

def ulongDivide(v1, v2):
    dividend = _ULong___get_data__impl_(v1)
    divisor = _ULong___get_data__impl_(v2)
    if jsLt(divisor.compareTo(Long(0, 0)), 0):
        tmp
        if jsLt(ulongCompare(_ULong___get_data__impl_(v1), _ULong___get_data__impl_(v2)), 0):
            tmp = ULong(Long(0, 0))
        
        if True:
            if True:
                tmp = ULong(Long(1, 0))
            
        
        return tmp
    
    if jsGtEq(dividend.compareTo(Long(0, 0)), 0):
        return ULong(dividend.div(divisor))
    
    quotient = dividend.ushr(1).div(divisor).shl(1)
    rem = dividend.minus(quotient.times(divisor))
    tmp
    tmp0_compareTo_0 = ULong(rem)
    tmp1_compareTo_0 = ULong(divisor)
    if jsGtEq(ulongCompare(_ULong___get_data__impl_(tmp0_compareTo_0), _ULong___get_data__impl_(tmp1_compareTo_0)), 0):
        tmp = 1
    
    if True:
        if True:
            tmp = 0
        
    
    tmp2_plus_0 = tmp
    return ULong(quotient.plus(toLong(tmp2_plus_0)))

def ulongRemainder(v1, v2):
    dividend = _ULong___get_data__impl_(v1)
    divisor = _ULong___get_data__impl_(v2)
    if jsLt(divisor.compareTo(Long(0, 0)), 0):
        tmp
        if jsLt(ulongCompare(_ULong___get_data__impl_(v1), _ULong___get_data__impl_(v2)), 0):
            tmp = v1
        
        if True:
            if True:
                tmp = ULong(_ULong___get_data__impl_(v1).minus(_ULong___get_data__impl_(v2)))
            
        
        return tmp
    
    if jsGtEq(dividend.compareTo(Long(0, 0)), 0):
        return ULong(dividend.rem(divisor))
    
    quotient = dividend.ushr(1).div(divisor).shl(1)
    rem = dividend.minus(quotient.times(divisor))
    tmp
    tmp0_compareTo_0 = ULong(rem)
    tmp1_compareTo_0 = ULong(divisor)
    if jsGtEq(ulongCompare(_ULong___get_data__impl_(tmp0_compareTo_0), _ULong___get_data__impl_(tmp1_compareTo_0)), 0):
        tmp = divisor
    
    if True:
        if True:
            tmp = Long(0, 0)
        
    
    return ULong(rem.minus(tmp))

def ulongToDouble(v):
    return jsPlus(jsMult(v.ushr(11).toDouble(), 2048), v._and(Long(2047, 0)).toDouble())

def ulongToString(v):
    return ulongToString(v, 10)

def ulongToString(v, base):
    if jsGtEq(v.compareTo(Long(0, 0)), 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_2c914364
    
    tmp0_div_0 = v.ushr(1)
    quotient = tmp0_div_0.div(toLong(base)).shl(1)
    tmp1_times_0 = quotient
    rem = v.minus(tmp1_times_0.times(toLong(base)))
    if jsGtEq(rem.compareTo(toLong(base)), 0):
        tmp2_minus_0 = rem
        rem = tmp2_minus_0.minus(toLong(base))
        tmp3_plus_0 = quotient
        tmp4_plus_0 = 1
        quotient = tmp3_plus_0.plus(toLong(tmp4_plus_0))
    
    return jsPlus(toString(base), toString(base))

def doubleToUInt(v):
    tmp
    if isNaN():
        tmp = UInt(0)
    
    if True:
        tmp0_toDouble_0 = UInt(0)
        if jsLtEq(v, uintToDouble(_UInt___get_data__impl_(tmp0_toDouble_0))):
            tmp = UInt(0)
        
        if True:
            tmp1_toDouble_0 = UInt(-1)
            if jsGtEq(v, uintToDouble(_UInt___get_data__impl_(tmp1_toDouble_0))):
                tmp = UInt(-1)
            
            if True:
                if jsLtEq(v, kotlin_Double(MAX_VALUE)):
                    tmp2_toUInt_0 = numberToInt(v)
                    tmp = UInt(tmp2_toUInt_0)
                
                if True:
                    if True:
                        tmp3_toUInt_0 = numberToInt(jsMinus(v, MAX_VALUE))
                        tmp5_plus_0 = UInt(tmp3_toUInt_0)
                        tmp4_toUInt_0 = MAX_VALUE
                        tmp6_plus_0 = UInt(tmp4_toUInt_0)
                        tmp = UInt(jsBitOr(jsPlus(_UInt___get_data__impl_(tmp5_plus_0), _UInt___get_data__impl_(tmp6_plus_0)), 0))
                    
                
            
        
    
    return tmp

def doubleToULong(v):
    tmp
    if isNaN():
        tmp = ULong(Long(0, 0))
    
    if True:
        tmp0_toDouble_0 = ULong(Long(0, 0))
        if jsLtEq(v, ulongToDouble(_ULong___get_data__impl_(tmp0_toDouble_0))):
            tmp = ULong(Long(0, 0))
        
        if True:
            tmp1_toDouble_0 = ULong(Long(-1, -1))
            if jsGtEq(v, ulongToDouble(_ULong___get_data__impl_(tmp1_toDouble_0))):
                tmp = ULong(Long(-1, -1))
            
            if True:
                if jsLt(v, 9.223372036854776E18):
                    tmp2_toULong_0 = numberToLong(v)
                    tmp = ULong(tmp2_toULong_0)
                
                if True:
                    if True:
                        tmp3_toULong_0 = numberToLong(jsMinus(v, 9.223372036854776E18))
                        tmp4_plus_0 = ULong(tmp3_toULong_0)
                        tmp5_plus_0 = ULong(Long(0, -2147483648))
                        tmp = ULong(_ULong___get_data__impl_(tmp4_plus_0).plus(_ULong___get_data__impl_(tmp5_plus_0)))
                    
                
            
        
    
    return tmp

class ExperimentalUnsignedTypes:
    def _init_():
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class Annotation:
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def _init_():
        pass
    

class CharSequence:
    def _get_length_(self):
        pass
    
    def get(self, index):
        pass
    
    def subSequence(self, startIndex, endIndex):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def _init_():
        pass
    

class Comparable:
    def compareTo(self, other):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def _init_():
        pass
    

class Iterator:
    def next(self):
        pass
    
    def hasNext(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def _init_():
        pass
    

class ListIterator:
    def next(self):
        pass
    
    def hasNext(self):
        pass
    
    def hasPrevious(self):
        pass
    
    def previous(self):
        pass
    
    def nextIndex(self):
        pass
    
    def previousIndex(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def _init_():
        pass
    

class MutableIterator:
    def remove(self):
        pass
    
    def next(self):
        pass
    
    def hasNext(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def _init_():
        pass
    

class MutableListIterator:
    def next(self):
        pass
    
    def hasNext(self):
        pass
    
    def remove(self):
        pass
    
    def set(self, element):
        pass
    
    def add(self, element):
        pass
    
    def hasPrevious(self):
        pass
    
    def previous(self):
        pass
    
    def nextIndex(self):
        pass
    
    def previousIndex(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def _init_():
        pass
    

class Number:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_54af9cce
    
    def toDouble(self):
        pass
    
    def toFloat(self):
        pass
    
    def toLong(self):
        pass
    
    def toInt(self):
        pass
    
    def toChar(self):
        pass
    
    def toShort(self):
        pass
    
    def toByte(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class SinceKotlin:
    def _init_(version):
        _this_.version = version
    
    def _get_version_(self):
        return version
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class Suppress:
    def _init_(names):
        _this_.names = names
    
    def _get_names_(self):
        return names
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_59527c30 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_794bf212 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_6b1a2c9f = 0
def values():
    return arrayLiteral(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_a7240fe)

def valueOf(value):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_267a3722

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_3dc21e8d = 0
def DeprecationLevel_initEntries():
    if DeprecationLevel_entriesInitialized:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_484794d6
    
    DeprecationLevel_entriesInitialized = True
    DeprecationLevel_WARNING_instance = DeprecationLevel('WARNING', 0)
    DeprecationLevel_ERROR_instance = DeprecationLevel('ERROR', 1)
    DeprecationLevel_HIDDEN_instance = DeprecationLevel('HIDDEN', 2)

class DeprecationLevel:
    def _init_(name, ordinal):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_64589c34
    
    def _get_name_(self):
        pass
    
    def _get_ordinal_(self):
        pass
    
    def compareTo(self, other):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class PublishedApi:
    def _init_():
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class ParameterName:
    def _init_(name):
        _this_.name = name
    
    def _get_name_(self):
        return name
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def Deprecated_init__Init_(message, replaceWith, level, _mask0, _marker, _this):
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 2), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_24aca5f1
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 4), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_4f0f76b4
    
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_13ff179a
    return _this

def Deprecated_init__Create_(message, replaceWith, level, _mask0, _marker):
    return Deprecated_init__Init_(message, replaceWith, level, _mask0, _marker, Object_create())

class Deprecated:
    def _init_(message, replaceWith, level):
        _this_.message = message
        _this_.replaceWith = replaceWith
        _this_.level = level
    
    def _get_message_(self):
        return message
    
    def _get_replaceWith_(self):
        return replaceWith
    
    def _get_level_(self):
        return level
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class ReplaceWith:
    def _init_(expression, imports):
        _this_.expression = expression
        _this_.imports = imports
    
    def _get_expression_(self):
        return expression
    
    def _get_imports_(self):
        return imports
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class ExtensionFunctionType:
    def _init_():
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class UnsafeVariance:
    def _init_():
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
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
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_70ed03e4
    
    def next(self):
        return _this_.nextByte()
    
    def nextByte(self):
        pass
    
    def hasNext(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class IntIterator:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_15d0f2a3
    
    def next(self):
        return _this_.nextInt()
    
    def nextInt(self):
        pass
    
    def hasNext(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class DoubleIterator:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_62a78446
    
    def next(self):
        return _this_.nextDouble()
    
    def nextDouble(self):
        pass
    
    def hasNext(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class FloatIterator:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_26f0ab88
    
    def next(self):
        return _this_.nextFloat()
    
    def nextFloat(self):
        pass
    
    def hasNext(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class LongIterator:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_7f9b46ed
    
    def next(self):
        return _this_.nextLong()
    
    def nextLong(self):
        pass
    
    def hasNext(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class CharIterator:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_38a3c078
    
    def next(self):
        return _this_.nextChar()
    
    def nextChar(self):
        pass
    
    def hasNext(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class BooleanIterator:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_5982255e
    
    def next(self):
        return _this_.nextBoolean()
    
    def nextBoolean(self):
        pass
    
    def hasNext(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class ShortIterator:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_68bef3df
    
    def next(self):
        return _this_.nextShort()
    
    def nextShort(self):
        pass
    
    def hasNext(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
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
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_60052518
        _this_.step = step
        _this_.finalElement = last
        _this_.hasNext = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_f3bea57
        _this_.next = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4fc1edc3
    
    def _get_step_(self):
        return step
    
    def hasNext(self):
        return hasNext
    
    def nextInt(self):
        value = next
        if jsEqeqeq(value, finalElement):
            if jsNot(hasNext):
                visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_51a8aed8
            
            _this_.hasNext = False
        
        if True:
            tmp0_this = _this_
            tmp0_this.next = jsBitOr(jsPlus(next, step), 0)
        
        return value
    
    def next(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
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
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_10d8769e
        _this_.step = step
        _this_.finalElement = last
        _this_.hasNext = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4a8f6f49
        _this_.next = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_7a715766
    
    def _get_step_(self):
        return step
    
    def hasNext(self):
        return hasNext
    
    def nextLong(self):
        value = next
        if value.equals(finalElement):
            if jsNot(hasNext):
                visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_57d8d8e2
            
            _this_.hasNext = False
        
        if True:
            tmp0_this = _this_
            tmp0_this.next = next.plus(step)
        
        return value
    
    def next(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
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
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_eaf3dd0
        _this_.step = step
        _this_.finalElement = last.toInt()
        _this_.hasNext = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_1919382c
        _this_.next = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_617f42cc
    
    def _get_step_(self):
        return step
    
    def hasNext(self):
        return hasNext
    
    def nextChar(self):
        value = next
        if jsEqeqeq(value, finalElement):
            if jsNot(hasNext):
                visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_39a8c08f
            
            _this_.hasNext = False
        
        if True:
            tmp0_this = _this_
            tmp0_this.next = jsBitOr(jsPlus(next, step), 0)
        
        return numberToChar(value)
    
    def next(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class Companion:
    def _init_():
        Companion_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_49620576
    
    def fromClosedRange(self, rangeStart, rangeEnd, step):
        return IntProgression(rangeStart, rangeEnd, step)
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_5f24bda8 = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_474f8a2b
    
    return Companion_instance

class IntProgression:
    def _init_(start, endInclusive, step):
        Companion_getInstance()
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_74cd82f1
        if jsEqeqeq(step, 0):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_7f1dfdbc
        
        if jsEqeqeq(step, MIN_VALUE):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_7707cd05
        
        _this_.first = start
        _this_.last = kotlin_Int(getProgressionLastElement(kotlin_Int(start), kotlin_Int(endInclusive), step))
        _this_.step = step
    
    def _get_first_(self):
        return first
    
    def _get_last_(self):
        return last
    
    def _get_step_(self):
        return step
    
    def iterator(self):
        return IntProgressionIterator(first, last, step)
    
    def isEmpty(self):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_68311b85
    
    def equals(self, other):
        tmp
        if jsInstanceOf(other, jsClass()):
            tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6b873080
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def hashCode(self):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_485b21ec
    
    def toString(self):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_720c54c6
    

class Companion:
    def _init_():
        Companion_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_67857a20
    
    def fromClosedRange(self, rangeStart, rangeEnd, step):
        return LongProgression(rangeStart, rangeEnd, step)
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_119a8125 = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_2547d1b8
    
    return Companion_instance

class LongProgression:
    def _init_(start, endInclusive, step):
        Companion_getInstance()
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_38c7ad43
        if step.equals(Long(0, 0)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_1b12f58d
        
        if step.equals(Long(0, -2147483648)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_2c6dab96
        
        _this_.first = start
        _this_.last = getProgressionLastElement(start.toLong(), endInclusive.toLong(), step).toLong()
        _this_.step = step
    
    def _get_first_(self):
        return first
    
    def _get_last_(self):
        return last
    
    def _get_step_(self):
        return step
    
    def iterator(self):
        return LongProgressionIterator(first, last, step)
    
    def isEmpty(self):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_68817cd7
    
    def equals(self, other):
        tmp
        if jsInstanceOf(other, jsClass()):
            tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_25169558
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def hashCode(self):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_54c252a4
    
    def toString(self):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2e002852
    

class Companion:
    def _init_():
        Companion_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_7a7698f4
    
    def fromClosedRange(self, rangeStart, rangeEnd, step):
        return CharProgression(rangeStart, rangeEnd, step)
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_6e74986c = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_2eea76bc
    
    return Companion_instance

class CharProgression:
    def _init_(start, endInclusive, step):
        Companion_getInstance()
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_685e97e0
        if jsEqeqeq(step, 0):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_2b60c832
        
        if jsEqeqeq(step, MIN_VALUE):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_71d8985
        
        _this_.first = start
        _this_.last = numberToChar(getProgressionLastElement(start.toInt(), endInclusive.toInt(), step))
        _this_.step = step
    
    def _get_first_(self):
        return first
    
    def _get_last_(self):
        return last
    
    def _get_step_(self):
        return step
    
    def iterator(self):
        return CharProgressionIterator(first, last, step)
    
    def isEmpty(self):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_37526ddf
    
    def equals(self, other):
        tmp
        if jsInstanceOf(other, jsClass()):
            tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3b48e216
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def hashCode(self):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_437eeb4
    
    def toString(self):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6f303c5d
    

class ClosedRange:
    def _get_start_(self):
        pass
    
    def _get_endInclusive_(self):
        pass
    
    def contains(self, value):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_194910bc
    
    def isEmpty(self):
        return jsGt(compareTo(_this_._get_start_(), _this_._get_endInclusive_()), 0)
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def _init_():
        pass
    

class Companion:
    def _init_():
        Companion_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_2b08f55a
        _this_.EMPTY = IntRange(1, 0)
    
    def _get_EMPTY_(self):
        return EMPTY
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_ec75805 = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_790d28a7
    
    return Companion_instance

class IntRange:
    def _init_(start, endInclusive):
        Companion_getInstance()
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_594793d1
    
    def _get_start_(self):
        return _this_._get_first_()
    
    def _get_endInclusive_(self):
        return _this_._get_last_()
    
    def contains(self, value):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_1ee7a438
    
    def contains(self, value):
        return _this_.contains(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_725d70ca)
    
    def isEmpty(self):
        return jsGt(_this_._get_first_(), _this_._get_last_())
    
    def equals(self, other):
        tmp
        if jsInstanceOf(other, jsClass()):
            tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4327b21f
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def hashCode(self):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6d0dd338
    
    def toString(self):
        return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_5e0cc49d
    
    def _get_first_(self):
        pass
    
    def _get_last_(self):
        pass
    
    def _get_step_(self):
        pass
    
    def iterator(self):
        pass
    

class Companion:
    def _init_():
        Companion_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_f3ae18f
        _this_.EMPTY = LongRange(Long(1, 0), Long(0, 0))
    
    def _get_EMPTY_(self):
        return EMPTY
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_566809db = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_170f2883
    
    return Companion_instance

class LongRange:
    def _init_(start, endInclusive):
        Companion_getInstance()
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_5a004dd4
    
    def _get_start_(self):
        return _this_._get_first_()
    
    def _get_endInclusive_(self):
        return _this_._get_last_()
    
    def contains(self, value):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_8f1b830
    
    def contains(self, value):
        return _this_.contains(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_7767c18d)
    
    def isEmpty(self):
        return jsGt(_this_._get_first_().compareTo(_this_._get_last_()), 0)
    
    def equals(self, other):
        tmp
        if jsInstanceOf(other, jsClass()):
            tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3b181488
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def hashCode(self):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_697c3410
    
    def toString(self):
        return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_45348159
    
    def _get_first_(self):
        pass
    
    def _get_last_(self):
        pass
    
    def _get_step_(self):
        pass
    
    def iterator(self):
        pass
    

class Companion:
    def _init_():
        Companion_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_2aec09a3
        _this_.EMPTY = CharRange(Char(1), Char(0))
    
    def _get_EMPTY_(self):
        return EMPTY
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_1172a648 = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_2361dc11
    
    return Companion_instance

class CharRange:
    def _init_(start, endInclusive):
        Companion_getInstance()
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_207e3ffd
    
    def _get_start_(self):
        return _this_._get_first_()
    
    def _get_endInclusive_(self):
        return _this_._get_last_()
    
    def contains(self, value):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_143170b7
    
    def contains(self, value):
        return _this_.contains(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_7943d3ac)
    
    def isEmpty(self):
        return jsGt(_this_._get_first_().compareTo(_this_._get_last_()), 0)
    
    def equals(self, other):
        tmp
        if jsInstanceOf(other, jsClass()):
            tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_1b4bfdb
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def hashCode(self):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_15fd41c0
    
    def toString(self):
        return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_316296ae
    
    def _get_first_(self):
        pass
    
    def _get_last_(self):
        pass
    
    def _get_step_(self):
        pass
    
    def iterator(self):
        pass
    

class Unit:
    def _init_():
        Unit_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_405d123c
    
    def toString(self):
        return 'kotlin.Unit'
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_f62fe59 = 0
def Unit_getInstance():
    if jsEqeq(Unit_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_7f5c7538
    
    return Unit_instance

class Target:
    def _init_(allowedTargets):
        _this_.allowedTargets = allowedTargets
    
    def _get_allowedTargets_(self):
        return allowedTargets
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_3b5c6eee = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_4526b3d5 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_47120b41 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_525d09b7 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_aae360c = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_7a668497 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_2df9d099 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_17537420 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_6cb62e90 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_223a5dad = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_41a42c6b = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_4d5aa20b = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_1045c79e = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_60e2370e = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_45980d = 0
def values():
    return arrayLiteral(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_7bd203ce)

def valueOf(value):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_63d0920a

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_7ac71b01 = 0
def AnnotationTarget_initEntries():
    if AnnotationTarget_entriesInitialized:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_2b4ab7
    
    AnnotationTarget_entriesInitialized = True
    AnnotationTarget_CLASS_instance = AnnotationTarget('CLASS', 0)
    AnnotationTarget_ANNOTATION_CLASS_instance = AnnotationTarget('ANNOTATION_CLASS', 1)
    AnnotationTarget_TYPE_PARAMETER_instance = AnnotationTarget('TYPE_PARAMETER', 2)
    AnnotationTarget_PROPERTY_instance = AnnotationTarget('PROPERTY', 3)
    AnnotationTarget_FIELD_instance = AnnotationTarget('FIELD', 4)
    AnnotationTarget_LOCAL_VARIABLE_instance = AnnotationTarget('LOCAL_VARIABLE', 5)
    AnnotationTarget_VALUE_PARAMETER_instance = AnnotationTarget('VALUE_PARAMETER', 6)
    AnnotationTarget_CONSTRUCTOR_instance = AnnotationTarget('CONSTRUCTOR', 7)
    AnnotationTarget_FUNCTION_instance = AnnotationTarget('FUNCTION', 8)
    AnnotationTarget_PROPERTY_GETTER_instance = AnnotationTarget('PROPERTY_GETTER', 9)
    AnnotationTarget_PROPERTY_SETTER_instance = AnnotationTarget('PROPERTY_SETTER', 10)
    AnnotationTarget_TYPE_instance = AnnotationTarget('TYPE', 11)
    AnnotationTarget_EXPRESSION_instance = AnnotationTarget('EXPRESSION', 12)
    AnnotationTarget_FILE_instance = AnnotationTarget('FILE', 13)
    AnnotationTarget_TYPEALIAS_instance = AnnotationTarget('TYPEALIAS', 14)

class AnnotationTarget:
    def _init_(name, ordinal):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_7b70ae8e
    
    def _get_name_(self):
        pass
    
    def _get_ordinal_(self):
        pass
    
    def compareTo(self, other):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class MustBeDocumented:
    def _init_():
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def Retention_init__Init_(value, _mask0, _marker, _this):
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 1), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_789a8251
    
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_23dfcae3
    return _this

def Retention_init__Create_(value, _mask0, _marker):
    return Retention_init__Init_(value, _mask0, _marker, Object_create())

class Retention:
    def _init_(value):
        _this_.value = value
    
    def _get_value_(self):
        return value
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_2a2e21ea = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_29fea6c2 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_47c57d0f = 0
def values():
    return arrayLiteral(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_1641c156)

def valueOf(value):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_61cb973d

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_3b1261ed = 0
def AnnotationRetention_initEntries():
    if AnnotationRetention_entriesInitialized:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_22f31149
    
    AnnotationRetention_entriesInitialized = True
    AnnotationRetention_SOURCE_instance = AnnotationRetention('SOURCE', 0)
    AnnotationRetention_BINARY_instance = AnnotationRetention('BINARY', 1)
    AnnotationRetention_RUNTIME_instance = AnnotationRetention('RUNTIME', 2)

class AnnotationRetention:
    def _init_(name, ordinal):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_765ea1ac
    
    def _get_name_(self):
        pass
    
    def _get_ordinal_(self):
        pass
    
    def compareTo(self, other):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class Repeatable:
    def _init_():
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
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
        tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6376db97
    
    if jsLt(step, 0):
        tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_1c3455e5
    
    if True:
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_394e0104
    
    return tmp

def getProgressionLastElement(start, end, step):
    tmp
    if jsGt(step.compareTo(Long(0, 0)), 0):
        tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_471a163a
    
    if jsLt(step.compareTo(Long(0, 0)), 0):
        tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6315cb3c
    
    if True:
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_35fd987b
    
    return tmp

def differenceModulo(a, b, c):
    return mod(jsBitOr(jsMinus(mod(a, c), mod(b, c)), 0), c)

def differenceModulo(a, b, c):
    return mod(mod(a, c).minus(mod(b, c)), c)

def mod(a, b):
    mod = jsMod(a, b)
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6cc52eb1

def mod(a, b):
    mod = a.rem(b)
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_319c6f69

class ByteCompanionObject:
    def _init_():
        ByteCompanionObject_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_4540aade
        _this_.MIN_VALUE = visitConst_other_Byte
        _this_.MAX_VALUE = visitConst_other_Byte
        _this_.SIZE_BYTES = 1
        _this_.SIZE_BITS = 8
    
    def _get_MIN_VALUE_(self):
        return MIN_VALUE
    
    def _get_MAX_VALUE_(self):
        return MAX_VALUE
    
    def _get_SIZE_BYTES_(self):
        return SIZE_BYTES
    
    def _get_SIZE_BITS_(self):
        return SIZE_BITS
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_6cb84c4c = 0
def ByteCompanionObject_getInstance():
    if jsEqeq(ByteCompanionObject_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_3a6c74d9
    
    return ByteCompanionObject_instance

class ShortCompanionObject:
    def _init_():
        ShortCompanionObject_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_17da6e45
        _this_.MIN_VALUE = visitConst_other_Short
        _this_.MAX_VALUE = visitConst_other_Short
        _this_.SIZE_BYTES = 2
        _this_.SIZE_BITS = 16
    
    def _get_MIN_VALUE_(self):
        return MIN_VALUE
    
    def _get_MAX_VALUE_(self):
        return MAX_VALUE
    
    def _get_SIZE_BYTES_(self):
        return SIZE_BYTES
    
    def _get_SIZE_BITS_(self):
        return SIZE_BITS
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_2a7eb66e = 0
def ShortCompanionObject_getInstance():
    if jsEqeq(ShortCompanionObject_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_2f05cf02
    
    return ShortCompanionObject_instance

class IntCompanionObject:
    def _init_():
        IntCompanionObject_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_4b93a232
        _this_.MIN_VALUE = -2147483648
        _this_.MAX_VALUE = 2147483647
        _this_.SIZE_BYTES = 4
        _this_.SIZE_BITS = 32
    
    def _get_MIN_VALUE_(self):
        return MIN_VALUE
    
    def _get_MAX_VALUE_(self):
        return MAX_VALUE
    
    def _get_SIZE_BYTES_(self):
        return SIZE_BYTES
    
    def _get_SIZE_BITS_(self):
        return SIZE_BITS
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_b484c37 = 0
def IntCompanionObject_getInstance():
    if jsEqeq(IntCompanionObject_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_760eb57e
    
    return IntCompanionObject_instance

class FloatCompanionObject:
    def _init_():
        FloatCompanionObject_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_6affa355
        _this_.MIN_VALUE = visitConst_other_Float
        _this_.MAX_VALUE = visitConst_other_Float
        _this_.POSITIVE_INFINITY = visitConst_other_Float
        _this_.NEGATIVE_INFINITY = visitConst_other_Float
        _this_.NaN = visitConst_other_Float
        _this_.SIZE_BYTES = 4
        _this_.SIZE_BITS = 32
    
    def _get_MIN_VALUE_(self):
        return MIN_VALUE
    
    def _get_MAX_VALUE_(self):
        return MAX_VALUE
    
    def _get_POSITIVE_INFINITY_(self):
        return POSITIVE_INFINITY
    
    def _get_NEGATIVE_INFINITY_(self):
        return NEGATIVE_INFINITY
    
    def _get_NaN_(self):
        return NaN
    
    def _get_SIZE_BYTES_(self):
        return SIZE_BYTES
    
    def _get_SIZE_BITS_(self):
        return SIZE_BITS
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_56c390fc = 0
def FloatCompanionObject_getInstance():
    if jsEqeq(FloatCompanionObject_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_53937f1a
    
    return FloatCompanionObject_instance

class DoubleCompanionObject:
    def _init_():
        DoubleCompanionObject_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_71077d1
        _this_.MIN_VALUE = 4.9E-324
        _this_.MAX_VALUE = 1.7976931348623157E308
        _this_.POSITIVE_INFINITY = Infinity
        _this_.NEGATIVE_INFINITY = -Infinity
        _this_.NaN = NaN
        _this_.SIZE_BYTES = 8
        _this_.SIZE_BITS = 64
    
    def _get_MIN_VALUE_(self):
        return MIN_VALUE
    
    def _get_MAX_VALUE_(self):
        return MAX_VALUE
    
    def _get_POSITIVE_INFINITY_(self):
        return POSITIVE_INFINITY
    
    def _get_NEGATIVE_INFINITY_(self):
        return NEGATIVE_INFINITY
    
    def _get_NaN_(self):
        return NaN
    
    def _get_SIZE_BYTES_(self):
        return SIZE_BYTES
    
    def _get_SIZE_BITS_(self):
        return SIZE_BITS
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_829264f = 0
def DoubleCompanionObject_getInstance():
    if jsEqeq(DoubleCompanionObject_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_42bf98f0
    
    return DoubleCompanionObject_instance

class StringCompanionObject:
    def _init_():
        StringCompanionObject_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_554a4d18
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_3abb7923 = 0
def StringCompanionObject_getInstance():
    if jsEqeq(StringCompanionObject_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_687e13c4
    
    return StringCompanionObject_instance

class BooleanCompanionObject:
    def _init_():
        BooleanCompanionObject_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_65448932
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_2948e596 = 0
def BooleanCompanionObject_getInstance():
    if jsEqeq(BooleanCompanionObject_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_335c77fe
    
    return BooleanCompanionObject_instance

class Comparator:
    def compare(self, a, b):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def _init_():
        pass
    

class JsName:
    def _init_(name):
        _this_.name = name
    
    def _get_name_(self):
        return name
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def toTypedArray():
    return copyToArray(_this_)

def copyToArray(collection):
    tmp
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_4e7bf371:
        tmp0_unsafeCast_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_650929dc
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
    
    if True:
        if True:
            tmp1_unsafeCast_0 = copyToArrayImpl(collection)
            tmp = kotlin_Any_(tmp1_unsafeCast_0)
        
    
    return tmp

def copyToArrayImpl(collection):
    array = kotlin_Array_kotlin_Any__(js('[]'))
    iterator = collection.iterator()
    while iterator.hasNext():
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_cbf9cc1
    
    return array

def copyToArrayImpl(collection, array):
    if jsLt(jsArrayLength(array), collection._get_size_()):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_b93aba8
    
    iterator = collection.iterator()
    index = 0
    while iterator.hasNext():
        tmp0 = index
        index = jsBitOr(jsPlus(tmp0, 1), 0)
        tmp1_unsafeCast_0 = iterator.next()
        jsArraySet(array, tmp0, kotlin_Any_(tmp1_unsafeCast_0))
    
    if jsLt(index, jsArrayLength(array)):
        tmp = index
        tmp2_unsafeCast_0 = None
        jsArraySet(array, tmp, kotlin_Any_(tmp2_unsafeCast_0))
    
    return array

class _no_name_provided_:
    def _init_(_elements):
        _this_._elements = _elements
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_3d435f83
    
    def invoke(self, it):
        return _elements.contains(it)
    
    def invoke(self, p1):
        return _this_.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_f329350)
    

class _no_name_provided_:
    def _init_(_elements):
        _this_._elements = _elements
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_78ca3d6b
    
    def invoke(self, it):
        return jsNot(_elements.contains(it))
    
    def invoke(self, p1):
        return _this_.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3d6aa682)
    

class AbstractMutableCollection:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_4467088e
    
    def add(self, element):
        pass
    
    def remove(self, element):
        _this_.checkIsMutable()
        iterator = _this_.iterator()
        while iterator.hasNext():
            if equals(iterator.next(), element):
                iterator.remove()
                return True
            
        
        return False
    
    def addAll(self, elements):
        _this_.checkIsMutable()
        modified = False
        tmp0_iterator = elements.iterator()
        while tmp0_iterator.hasNext():
            element = tmp0_iterator.next()
            if _this_.add(element):
                visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_340f4723
            
        
        return modified
    
    def removeAll(self, elements):
        _this_.checkIsMutable()
        tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_44acc838
        return removeAll(_no_name_provided__factory(elements))
    
    def retainAll(self, elements):
        _this_.checkIsMutable()
        tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_230ca3c3
        return removeAll(_no_name_provided__factory(elements))
    
    def clear(self):
        _this_.checkIsMutable()
        iterator = _this_.iterator()
        while iterator.hasNext():
            iterator.next()
            Unit_getInstance()
            iterator.remove()
        
    
    def toJSON(self):
        return _this_.toArray()
    
    def checkIsMutable(self):
        pass
    
    def _get_size_(self):
        pass
    
    def iterator(self):
        pass
    
    def contains(self, element):
        pass
    
    def containsAll(self, elements):
        pass
    
    def isEmpty(self):
        pass
    
    def toString(self):
        pass
    
    def toArray(self):
        pass
    
    def toArray(self, array):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    

def _no_name_provided__factory(_elements):
    i = _no_name_provided_(_elements)
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_eddf865

def _no_name_provided__factory(_elements):
    i = _no_name_provided_(_elements)
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_3131a06d

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
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_771deee6
        _this_.index = 0
        _this_.last = -1
    
    def _set_index_(self, _set___):
        _this_.index = _set___
    
    def _get_index_(self):
        return index
    
    def _set_last_(self, _set___):
        _this_.last = _set___
    
    def _get_last_(self):
        return last
    
    def hasNext(self):
        return jsLt(index, _this._get_size_())
    
    def next(self):
        if jsNot(_this_.hasNext()):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_2b39e77d
        
        tmp = _this_
        tmp0_this = _this_
        tmp1 = index
        tmp0_this.index = jsBitOr(jsPlus(tmp1, 1), 0)
        tmp.last = tmp1
        return _this.get(last)
    
    def remove(self):
        tmp0_check_0 = jsNot(jsEqeqeq(last, -1))
        if jsNot(tmp0_check_0):
            message_1 = 'Call next() or previous() before removing element from the iterator.'
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_716a2c04
        
        _this.removeAt(last)
        Unit_getInstance()
        _this_.index = last
        _this_.last = -1
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class ListIteratorImpl:
    def _init_(_outer, index):
        _this_._this = _outer
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_67c09530
        Companion_getInstance().checkPositionIndex(index, _this._get_size_())
        _this_._set_index_(index)
    
    def hasPrevious(self):
        return jsGt(_this_._get_index_(), 0)
    
    def nextIndex(self):
        return _this_._get_index_()
    
    def previous(self):
        if jsNot(_this_.hasPrevious()):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_582b6362
        
        tmp0_this = _this_
        tmp0_this._set_index_(jsBitOr(jsMinus(tmp0_this._get_index_(), 1), 0))
        _this_._set_last_(tmp0_this._get_index_())
        return _this.get(_this_._get_last_())
    
    def previousIndex(self):
        return jsBitOr(jsMinus(_this_._get_index_(), 1), 0)
    
    def add(self, element):
        _this.add(_this_._get_index_(), element)
        tmp0_this = _this_
        tmp1 = tmp0_this._get_index_()
        tmp0_this._set_index_(jsBitOr(jsPlus(tmp1, 1), 0))
        Unit_getInstance()
        _this_._set_last_(-1)
    
    def add(self, element):
        return _this_.add(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4a50f850)
    
    def set(self, element):
        tmp0_check_0 = jsNot(jsEqeqeq(_this_._get_last_(), -1))
        if jsNot(tmp0_check_0):
            message_1 = 'Call next() or previous() before updating element value with the iterator.'
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_e84d76d
        
        _this.set(_this_._get_last_(), element)
        Unit_getInstance()
    
    def set(self, element):
        return _this_.set(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_432e9de9)
    
    def _set_index_(self, _set___):
        pass
    
    def _get_index_(self):
        pass
    
    def _set_last_(self, _set___):
        pass
    
    def _get_last_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hasNext(self):
        pass
    
    def hashCode(self):
        pass
    
    def next(self):
        pass
    
    def remove(self):
        pass
    
    def toString(self):
        pass
    

class SubList:
    def _init_(list, fromIndex, toIndex):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_679f3e12
        _this_.list = list
        _this_.fromIndex = fromIndex
        _this_._size = 0
        Companion_getInstance().checkRangeIndexes(fromIndex, toIndex, list._get_size_())
        _this_._size = jsBitOr(jsMinus(toIndex, fromIndex), 0)
    
    def add(self, index, element):
        Companion_getInstance().checkPositionIndex(index, _size)
        list.add(jsBitOr(jsPlus(fromIndex, index), 0), element)
        tmp0_this = _this_
        tmp1 = _size
        tmp0_this._size = jsBitOr(jsPlus(tmp1, 1), 0)
        Unit_getInstance()
    
    def get(self, index):
        Companion_getInstance().checkElementIndex(index, _size)
        return list.get(jsBitOr(jsPlus(fromIndex, index), 0))
    
    def removeAt(self, index):
        Companion_getInstance().checkElementIndex(index, _size)
        result = list.removeAt(jsBitOr(jsPlus(fromIndex, index), 0))
        tmp0_this = _this_
        tmp1 = _size
        tmp0_this._size = jsBitOr(jsMinus(tmp1, 1), 0)
        Unit_getInstance()
        return result
    
    def set(self, index, element):
        Companion_getInstance().checkElementIndex(index, _size)
        return list.set(jsBitOr(jsPlus(fromIndex, index), 0), element)
    
    def _get_size_(self):
        return _size
    
    def checkIsMutable(self):
        return list.checkIsMutable()
    
    def toArray(self):
        pass
    
    def toJSON(self):
        pass
    
    def _set_modCount_(self, _set___):
        pass
    
    def _get_modCount_(self):
        pass
    
    def toArray(self, array):
        pass
    
    def removeRange(self, fromIndex, toIndex):
        pass
    
    def add(self, element):
        pass
    
    def addAll(self, elements):
        pass
    
    def addAll(self, index, elements):
        pass
    
    def clear(self):
        pass
    
    def contains(self, element):
        pass
    
    def indexOf(self, element):
        pass
    
    def iterator(self):
        pass
    
    def lastIndexOf(self, element):
        pass
    
    def listIterator(self):
        pass
    
    def listIterator(self, index):
        pass
    
    def remove(self, element):
        pass
    
    def removeAll(self, elements):
        pass
    
    def retainAll(self, elements):
        pass
    
    def subList(self, fromIndex, toIndex):
        pass
    
    def containsAll(self, elements):
        pass
    
    def isEmpty(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class _no_name_provided_:
    def _init_(_elements):
        _this_._elements = _elements
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_771da67d
    
    def invoke(self, it):
        return _elements.contains(it)
    
    def invoke(self, p1):
        return _this_.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4f1a963b)
    

class _no_name_provided_:
    def _init_(_elements):
        _this_._elements = _elements
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_5b71f335
    
    def invoke(self, it):
        return jsNot(_elements.contains(it))
    
    def invoke(self, p1):
        return _this_.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_431e67f8)
    

class AbstractMutableList:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_6e1d939e
        _this_.modCount = 0
    
    def _set_modCount_(self, _set___):
        _this_.modCount = _set___
    
    def _get_modCount_(self):
        return modCount
    
    def add(self, index, element):
        pass
    
    def removeAt(self, index):
        pass
    
    def set(self, index, element):
        pass
    
    def add(self, element):
        _this_.checkIsMutable()
        _this_.add(_this_._get_size_(), element)
        return True
    
    def addAll(self, index, elements):
        _this_.checkIsMutable()
        _index = index
        changed = False
        tmp0_iterator = elements.iterator()
        while tmp0_iterator.hasNext():
            e = tmp0_iterator.next()
            tmp1 = _index
            _index = jsBitOr(jsPlus(tmp1, 1), 0)
            _this_.add(tmp1, e)
            changed = True
        
        return changed
    
    def clear(self):
        _this_.checkIsMutable()
        _this_.removeRange(0, _this_._get_size_())
    
    def removeAll(self, elements):
        _this_.checkIsMutable()
        return removeAll(_no_name_provided__factory(elements))
    
    def retainAll(self, elements):
        _this_.checkIsMutable()
        return removeAll(_no_name_provided__factory(elements))
    
    def iterator(self):
        return IteratorImpl(_this_)
    
    def contains(self, element):
        return jsGtEq(_this_.indexOf(element), 0)
    
    def indexOf(self, element):
        inductionVariable = 0
        last = _get_lastIndex_()
        if jsLtEq(inductionVariable, last):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_3fdc7786
        
        return -1
    
    def lastIndexOf(self, element):
        inductionVariable = _get_lastIndex_()
        if jsLtEq(0, inductionVariable):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_117eac4a
        
        return -1
    
    def listIterator(self):
        return _this_.listIterator(0)
    
    def listIterator(self, index):
        return ListIteratorImpl(_this_, index)
    
    def subList(self, fromIndex, toIndex):
        return SubList(_this_, fromIndex, toIndex)
    
    def removeRange(self, fromIndex, toIndex):
        iterator = _this_.listIterator(fromIndex)
        tmp0_repeat_0 = jsBitOr(jsMinus(toIndex, fromIndex), 0)
        inductionVariable = 0
        if jsLt(inductionVariable, tmp0_repeat_0):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_5d65a2f1
        
    
    def equals(self, other):
        if jsEqeqeq(other, _this_):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_5ceb6796
        
        if jsNot(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_67779915):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_6a9861de
        
        if True:
            pass
        
        return Companion_getInstance().orderedEquals(_this_, kotlin_collections_Collection___(other))
    
    def hashCode(self):
        return Companion_getInstance().orderedHashCode(_this_)
    
    def remove(self, element):
        pass
    
    def addAll(self, elements):
        pass
    
    def toJSON(self):
        pass
    
    def checkIsMutable(self):
        pass
    
    def _get_size_(self):
        pass
    
    def containsAll(self, elements):
        pass
    
    def isEmpty(self):
        pass
    
    def toString(self):
        pass
    
    def toArray(self):
        pass
    
    def toArray(self, array):
        pass
    
    def get(self, index):
        pass
    

def _no_name_provided__factory(_elements):
    i = _no_name_provided_(_elements)
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_4f613e30

def _no_name_provided__factory(_elements):
    i = _no_name_provided_(_elements)
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_3f05744b

def _set_array_(_this, _set___):
    _this.array = _set___

def _get_array_(_this):
    return array

def _set_isReadOnly_(_this, _set___):
    _this.isReadOnly = _set___

def _get_isReadOnly_(_this):
    return isReadOnly

def ArrayList_init__Init_(_this):
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_67503009
    return _this

def ArrayList_init__Create_():
    return ArrayList_init__Init_(Object_create())

def ArrayList_init__Init_(initialCapacity, _this):
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_5631baf5
    return _this

def ArrayList_init__Create_(initialCapacity):
    return ArrayList_init__Init_(initialCapacity, Object_create())

def ArrayList_init__Init_(initialCapacity, _mask0, _marker, _this):
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 1), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_182a5c56
    
    ArrayList_init__Init_(initialCapacity, _this)
    return _this

def ArrayList_init__Create_(initialCapacity, _mask0, _marker):
    return ArrayList_init__Init_(initialCapacity, _mask0, _marker, Object_create())

def ArrayList_init__Init_(elements, _this):
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_509c1d50
    return _this

def ArrayList_init__Create_(elements):
    return ArrayList_init__Init_(elements, Object_create())

def rangeCheck(_this, index):
    Companion_getInstance().checkElementIndex(index, _this._get_size_())
    return index

def insertionRangeCheck(_this, index):
    Companion_getInstance().checkPositionIndex(index, _this._get_size_())
    return index

class ArrayList:
    def _init_(array):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_4f1cb802
        _this_.array = array
        _this_.isReadOnly = False
    
    def build(self):
        _this_.checkIsMutable()
        _this_.isReadOnly = True
        return _this_
    
    def trimToSize(self):
        pass
    
    def ensureCapacity(self, minCapacity):
        pass
    
    def _get_size_(self):
        return jsArrayLength(array)
    
    def get(self, index):
        tmp = jsArrayGet(array, rangeCheck(_this_, index))
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_26dcac0d
    
    def set(self, index, element):
        _this_.checkIsMutable()
        rangeCheck(_this_, index)
        Unit_getInstance()
        tmp0_apply_0 = jsArrayGet(array, index)
        jsArraySet(array, index, element)
        tmp = tmp0_apply_0
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4008caaf
    
    def add(self, element):
        _this_.checkIsMutable()
        tmp0_asDynamic_0 = array
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_20e7ea20
        tmp0_this = _this_
        tmp1 = tmp0_this._get_modCount_()
        tmp0_this._set_modCount_(jsBitOr(jsPlus(tmp1, 1), 0))
        Unit_getInstance()
        return True
    
    def add(self, index, element):
        _this_.checkIsMutable()
        tmp0_asDynamic_0 = array
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_f2e28c7
        tmp0_this = _this_
        tmp1 = tmp0_this._get_modCount_()
        tmp0_this._set_modCount_(jsBitOr(jsPlus(tmp1, 1), 0))
        Unit_getInstance()
    
    def addAll(self, elements):
        _this_.checkIsMutable()
        if elements.isEmpty():
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_5bbd8118
        
        tmp0_this = _this_
        tmp = tmp0_this
        tmp0_plus_0 = array
        tmp1_plus_0 = copyToArray(elements)
        tmp.array = kotlin_Array_kotlin_Any__(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_30f2e0e0)
        tmp1_this = _this_
        tmp2 = tmp1_this._get_modCount_()
        tmp1_this._set_modCount_(jsBitOr(jsPlus(tmp2, 1), 0))
        Unit_getInstance()
        return True
    
    def addAll(self, index, elements):
        _this_.checkIsMutable()
        insertionRangeCheck(_this_, index)
        Unit_getInstance()
        if jsEqeqeq(index, _this_._get_size_()):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_3a3fc789
        
        if elements.isEmpty():
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_3d577add
        
        tmp0_subject = index
        if jsEqeqeq(tmp0_subject, _this_._get_size_()):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_2984edab
        
        if jsEqeqeq(tmp0_subject, 0):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_29dbf03f
        
        if True:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_5f83000c
        
        tmp1_this = _this_
        tmp2 = tmp1_this._get_modCount_()
        tmp1_this._set_modCount_(jsBitOr(jsPlus(tmp2, 1), 0))
        Unit_getInstance()
        return True
    
    def removeAt(self, index):
        _this_.checkIsMutable()
        rangeCheck(_this_, index)
        Unit_getInstance()
        tmp0_this = _this_
        tmp1 = tmp0_this._get_modCount_()
        tmp0_this._set_modCount_(jsBitOr(jsPlus(tmp1, 1), 0))
        Unit_getInstance()
        tmp
        if jsEqeqeq(index, _get_lastIndex_()):
            tmp0_asDynamic_0 = array
            tmp = E(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_58fa8762)
        
        if True:
            tmp1_asDynamic_0 = array
            tmp = E(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_35abfeba)
        
        return tmp
    
    def remove(self, element):
        _this_.checkIsMutable()
        inductionVariable = 0
        last = jsBitOr(jsMinus(jsArrayLength(array), 1), 0)
        if jsLtEq(inductionVariable, last):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_7027c359
        
        return False
    
    def removeRange(self, fromIndex, toIndex):
        _this_.checkIsMutable()
        tmp0_this = _this_
        tmp1 = tmp0_this._get_modCount_()
        tmp0_this._set_modCount_(jsBitOr(jsPlus(tmp1, 1), 0))
        Unit_getInstance()
        tmp0_asDynamic_0 = array
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_3343997b
    
    def clear(self):
        _this_.checkIsMutable()
        tmp = _this_
        tmp.array = kotlin_Array_kotlin_Any__(js('[]'))
        tmp0_this = _this_
        tmp1 = tmp0_this._get_modCount_()
        tmp0_this._set_modCount_(jsBitOr(jsPlus(tmp1, 1), 0))
        Unit_getInstance()
    
    def indexOf(self, element):
        return indexOf(element)
    
    def lastIndexOf(self, element):
        return lastIndexOf(element)
    
    def toString(self):
        return arrayToString(array)
    
    def toArray(self):
        return kotlin_Array_kotlin_Any__(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_75edfe9a)
    
    def toArray(self):
        return _this_.toArray()
    
    def checkIsMutable(self):
        if isReadOnly:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_4bdec54
        
    
    def _set_modCount_(self, _set___):
        pass
    
    def _get_modCount_(self):
        pass
    
    def removeAll(self, elements):
        pass
    
    def retainAll(self, elements):
        pass
    
    def iterator(self):
        pass
    
    def contains(self, element):
        pass
    
    def listIterator(self):
        pass
    
    def listIterator(self, index):
        pass
    
    def subList(self, fromIndex, toIndex):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toJSON(self):
        pass
    
    def containsAll(self, elements):
        pass
    
    def isEmpty(self):
        pass
    
    def toArray(self, array):
        pass
    

def _set__stableSortingIsSupported_(_set___):
    _stableSortingIsSupported = _set___

def _get__stableSortingIsSupported_():
    return _stableSortingIsSupported

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_59acb725 = 0
class RandomAccess:
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def _init_():
        pass
    

def _set_output_(_set___):
    output = _set___

def _get_output_():
    return output

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_71f9f8ba = 0
class BaseOutput:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_726e780a
    
    def println(self):
        _this_.print('\n')
    
    def println(self, message):
        _this_.print(message)
        _this_.println()
    
    def print(self, message):
        pass
    
    def flush(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class NodeJsOutput:
    def _init_(outputStream):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_1703e50d
        _this_.outputStream = outputStream
    
    def _get_outputStream_(self):
        return outputStream
    
    def print(self, message):
        messageString = kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_11cd442d)
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_734d870f
    
    def println(self):
        pass
    
    def println(self, message):
        pass
    
    def flush(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class BufferedOutputToConsoleLog:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_37b97394
    
    def print(self, message):
        s = kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_1443f11c)
        tmp0_nativeLastIndexOf_0 = s
        tmp1_nativeLastIndexOf_0 = '\n'
        tmp2_nativeLastIndexOf_0 = 0
        i = kotlin_Int(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_60fa2d75)
        if jsGtEq(i, 0):
            tmp0_this = _this_
            tmp = tmp0_this._get_buffer_()
            tmp3_substring_0 = s
            tmp4_substring_0 = 0
            tmp0_this._set_buffer_(jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_ffea9ca)))
            _this_.flush()
            tmp5_substring_0 = s
            tmp6_substring_0 = jsBitOr(jsPlus(i, 1), 0)
            s = kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_357d787b)
        
        tmp1_this = _this_
        tmp1_this._set_buffer_(jsPlus(tmp1_this._get_buffer_(), s))
    
    def flush(self):
        _get_console_().log(arrayLiteral(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_1f193005))
        _this_._set_buffer_('')
    
    def _set_buffer_(self, _set___):
        pass
    
    def _get_buffer_(self):
        pass
    
    def println(self):
        pass
    
    def println(self, message):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def String(value):
    return kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_19469022)

class BufferedOutput:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_7b2cd7ff
        _this_.buffer = ''
    
    def _set_buffer_(self, _set___):
        _this_.buffer = _set___
    
    def _get_buffer_(self):
        return buffer
    
    def print(self, message):
        tmp0_this = _this_
        tmp = tmp0_this
        tmp = buffer
        tmp.buffer = jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_17dd02ff))
    
    def flush(self):
        _this_.buffer = ''
    
    def println(self):
        pass
    
    def println(self, message):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def println(message):
    output.println(message)

def output_init_():
    isNode_2 = kotlin_Boolean(js('typeof process !== \'undefined\' && process.versions && !!process.versions.node'))
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_31cce16b

def _get_EmptyContinuation_():
    return EmptyContinuation

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_147c00c7 = 0
class _no_name_provided__1:
    def _init_(_tmp0_Continuation_0):
        _this_._tmp0_Continuation_0 = _tmp0_Continuation_0
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_35050186
    
    def _get_context__2(self):
        return _tmp0_Continuation_0
    
    def _get_context_(self):
        return _this_._get_context__2()
    
    def resumeWith_3(self, result):
        throwOnFailure()
        tmp = _Result___get_value__impl_(result)
        if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_68be702f:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrTypeOperatorCallImpl_3dade0d4
        
        if True:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCallImpl_eb8378c
        
        return Unit_getInstance()
    
    def resumeWith(self, result):
        return _this_.resumeWith_3(result)
    
    def equals_4(self, other):
        pass
    
    def hashCode_5(self):
        pass
    
    def toString_6(self):
        pass
    

def EmptyContinuation_init_():
    tmp0_Continuation_0 = EmptyCoroutineContext_getInstance()
    return _no_name_provided__1(tmp0_Continuation_0)

def asDynamic():
    return _this_

def unsafeCast():
    return T(_this_)

def unsafeCast():
    return T(_this_)

class Serializable:
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def _init_():
        pass
    

def pow(n):
    return visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl_2e9290bc.pow(_this_, kotlin_Double(n))

def isNaN():
    return jsNot(jsEqeqeq(_this_, _this_))

def _get_INV_2_26_():
    return INV_2_26

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_1bef1304 = 0
def _get_INV_2_53_():
    return INV_2_53

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_5188c0f2 = 0
def INV_2_26_init_():
    tmp0_pow_0 = 2.0
    tmp1_pow_0 = -26
    return visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl_4d61d93a.pow(tmp0_pow_0, kotlin_Double(tmp1_pow_0))

def INV_2_53_init_():
    tmp0_pow_0 = 2.0
    tmp1_pow_0 = -53
    return visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl_519565a5.pow(tmp0_pow_0, kotlin_Double(tmp1_pow_0))

def _get_js_():
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_253caf40._get_jClass_()

class KCallable:
    def _get_name_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def _init_():
        pass
    

class KClass:
    def _get_simpleName_(self):
        pass
    
    def _get_qualifiedName_(self):
        pass
    
    def isInstance(self, value):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def _init_():
        pass
    

class KClassImpl:
    def _init_(jClass):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_62a5e4c7
        _this_.jClass = jClass
    
    def _get_jClass_(self):
        return jClass
    
    def _get_qualifiedName_(self):
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_4a192cc6
    
    def equals(self, other):
        tmp
        if jsInstanceOf(other, jsClass()):
            tmp = equals(_this_._get_jClass_(), kotlin_reflect_js_internal_KClassImpl_out_kotlin_Any_(other)._get_jClass_())
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def hashCode(self):
        tmp0_safe_receiver = _this_._get_simpleName_()
        tmp1_elvis_lhs = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3027ba9b
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_d609083
    
    def toString(self):
        return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_3c9be087
    
    def _get_simpleName_(self):
        pass
    
    def isInstance(self, value):
        pass
    

def _get_givenSimpleName_(_this):
    return givenSimpleName

def _get_isInstanceFunction_(_this):
    return isInstanceFunction

class PrimitiveKClassImpl:
    def _init_(jClass, givenSimpleName, isInstanceFunction):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_76737130
        _this_.givenSimpleName = givenSimpleName
        _this_.isInstanceFunction = isInstanceFunction
    
    def equals(self, other):
        if jsNot(jsInstanceOf(other, jsClass())):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_7668edd7
        
        if True:
            pass
        
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_74ebbc13
    
    def _get_simpleName_(self):
        return givenSimpleName
    
    def isInstance(self, value):
        return isInstanceFunction.invoke(value)
    
    def _get_jClass_(self):
        pass
    
    def _get_qualifiedName_(self):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class NothingKClassImpl:
    def _init_():
        NothingKClassImpl_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_48028e11
        _this_.simpleName = 'Nothing'
    
    def _get_simpleName_(self):
        return simpleName
    
    def isInstance(self, value):
        return False
    
    def _get_jClass_(self):
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_26a5007
    
    def equals(self, other):
        return jsEqeqeq(other, _this_)
    
    def hashCode(self):
        return 0
    
    def _get_qualifiedName_(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_2c1312c1 = 0
def NothingKClassImpl_getInstance():
    if jsEqeq(NothingKClassImpl_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_68496278
    
    return NothingKClassImpl_instance

class ErrorKClass:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_33c6c4f
    
    def _get_simpleName_(self):
        tmp0_error_0 = 'Unknown simpleName for ErrorKClass'
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_2cfc75cb
    
    def _get_qualifiedName_(self):
        tmp0_error_0 = 'Unknown qualifiedName for ErrorKClass'
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_44af21cf
    
    def isInstance(self, value):
        tmp0_error_0 = 'Can\'s check isInstance on ErrorKClass'
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_144cf818
    
    def equals(self, other):
        return jsEqeqeq(other, _this_)
    
    def hashCode(self):
        return 0
    
    def toString(self):
        pass
    

class SimpleKClassImpl:
    def _init_(jClass):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_319c77de
        tmp = _this_
        tmp0_safe_receiver = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicMemberExpressionImpl_2860427c
        tmp0_unsafeCast_0 = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_15d24cb4
        tmp.simpleName = kotlin_Any_(tmp0_unsafeCast_0)
    
    def _get_simpleName_(self):
        return simpleName
    
    def isInstance(self, value):
        return jsIsType(value, _this_._get_jClass_())
    
    def _get_jClass_(self):
        pass
    
    def _get_qualifiedName_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class KFunction:
    def _get_name_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def _init_():
        pass
    

class KProperty:
    def _get_name_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def _init_():
        pass
    

class KProperty0:
    def get(self):
        pass
    
    def _get_name_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def invoke(self):
        pass
    
    def _init_():
        pass
    

class KProperty1:
    def get(self, receiver):
        pass
    
    def _get_name_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def invoke(self, p1):
        pass
    
    def _init_():
        pass
    

class KProperty2:
    def get(self, receiver1, receiver2):
        pass
    
    def _get_name_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def invoke(self, p1, p2):
        pass
    
    def _init_():
        pass
    

class KMutableProperty0:
    def set(self, value):
        pass
    
    def get(self):
        pass
    
    def _get_name_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def invoke(self):
        pass
    
    def _init_():
        pass
    

class KMutableProperty:
    def _get_name_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def _init_():
        pass
    

class KMutableProperty1:
    def set(self, receiver, value):
        pass
    
    def get(self, receiver):
        pass
    
    def _get_name_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def invoke(self, p1):
        pass
    
    def _init_():
        pass
    

class KMutableProperty2:
    def set(self, receiver1, receiver2, value):
        pass
    
    def get(self, receiver1, receiver2):
        pass
    
    def _get_name_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def invoke(self, p1, p2):
        pass
    
    def _init_():
        pass
    

class KType:
    def _get_classifier_(self):
        pass
    
    def _get_arguments_(self):
        pass
    
    def _get_isMarkedNullable_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def _init_():
        pass
    

def createKType(classifier, arguments, isMarkedNullable):
    return KTypeImpl(classifier, asList(), isMarkedNullable)

def createDynamicKType():
    return DynamicKType_getInstance()

def createKTypeParameter(name, upperBounds, variance):
    tmp0_subject = variance
    kVariance = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3c1aede3
    return KTypeParameterImpl(name, asList(), kVariance, False)

def getStarKTypeProjection():
    return Companion_getInstance()._get_STAR_()

def createCovariantKTypeProjection(type):
    return Companion_getInstance().covariant(type)

def createInvariantKTypeProjection(type):
    return Companion_getInstance().invariant(type)

def createContravariantKTypeProjection(type):
    return Companion_getInstance().contravariant(type)

def asString(_this):
    if jsEqeq(variance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_76797720
    
    return jsPlus(prefixString(), toString())

class _no_name_provided_:
    def _init_(this_0):
        _this_.this_0 = this_0
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_70ed9c7f
    
    def invoke(self, it):
        return asString(this_0)
    
    def invoke(self, p1):
        return _this_.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_33de2803)
    

class KTypeImpl:
    def _init_(classifier, arguments, isMarkedNullable):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_142f0ac1
        _this_.classifier = classifier
        _this_.arguments = arguments
        _this_.isMarkedNullable = isMarkedNullable
    
    def _get_classifier_(self):
        return classifier
    
    def _get_arguments_(self):
        return arguments
    
    def _get_isMarkedNullable_(self):
        return isMarkedNullable
    
    def equals(self, other):
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
    
    def hashCode(self):
        return jsBitOr(jsPlus(imul(jsBitOr(jsPlus(imul(hashCode(classifier), 31), hashCode(arguments)), 0), 31), jsBitOr(isMarkedNullable, 0)), 0)
    
    def toString(self):
        tmp = classifier
        kClass = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2687bf90
        classifierName = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_1b7c7d84
        tmp
        if arguments.isEmpty():
            tmp = ''
        
        if True:
            tmp = joinToString_default(', ', '<', '>', 0, None, _no_name_provided__factory(_this_), 24, None)
        
        args = tmp
        nullable = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_52d7889a
        return jsPlus(plus(args), nullable)
    

def prefixString():
    tmp0_subject = _this_
    tmp
    if tmp0_subject.equals(KVariance_INVARIANT_getInstance()):
        tmp = ''
    
    if tmp0_subject.equals(KVariance_IN_getInstance()):
        tmp = 'in '
    
    if tmp0_subject.equals(KVariance_OUT_getInstance()):
        tmp = 'out '
    
    if True:
        noWhenBranchMatchedException()
    
    return tmp

class DynamicKType:
    def _init_():
        DynamicKType_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_5304ac92
        _this_.classifier = None
        _this_.arguments = emptyList()
        _this_.isMarkedNullable = False
    
    def _get_classifier_(self):
        return classifier
    
    def _get_arguments_(self):
        return arguments
    
    def _get_isMarkedNullable_(self):
        return isMarkedNullable
    
    def toString(self):
        return 'dynamic'
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_46a4eecd = 0
def DynamicKType_getInstance():
    if jsEqeq(DynamicKType_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_36881f62
    
    return DynamicKType_instance

def _no_name_provided__factory(this_0):
    i = _no_name_provided_(this_0)
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_379ebdf

class KTypeParameterImpl:
    def _init_(name, upperBounds, variance, isReified):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_4044f07b
        _this_.name = name
        _this_.upperBounds = upperBounds
        _this_.variance = variance
        _this_.isReified = isReified
    
    def _get_name_(self):
        return name
    
    def _get_upperBounds_(self):
        return upperBounds
    
    def _get_variance_(self):
        return variance
    
    def _get_isReified_(self):
        return isReified
    
    def toString(self):
        return name
    
    def component1(self):
        return name
    
    def component2(self):
        return upperBounds
    
    def component3(self):
        return variance
    
    def component4(self):
        return isReified
    
    def copy(self, name, upperBounds, variance, isReified):
        return KTypeParameterImpl(name, upperBounds, variance, isReified)
    
    def copy_default(self, name, upperBounds, variance, isReified, _mask0, _handler):
        if jsNot(jsEqeqeq(jsBitAnd(_mask0, 1), 0)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_4e27eb57
        
        if jsNot(jsEqeqeq(jsBitAnd(_mask0, 2), 0)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_7643ae41
        
        if jsNot(jsEqeqeq(jsBitAnd(_mask0, 4), 0)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_52386242
        
        if jsNot(jsEqeqeq(jsBitAnd(_mask0, 8), 0)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_5a6e1d26
        
        return _this_.copy(kotlin_String(name), kotlin_collections_List_kotlin_reflect_KType_(upperBounds), kotlin_reflect_KVariance(variance), isReified)
    
    def hashCode(self):
        result = getStringHashCode(name)
        result = jsBitOr(jsPlus(imul(result, 31), hashCode(upperBounds)), 0)
        result = jsBitOr(jsPlus(imul(result, 31), variance.hashCode()), 0)
        result = jsBitOr(jsPlus(imul(result, 31), jsBitOr(isReified, 0)), 0)
        return result
    
    def equals(self, other):
        if jsEqeqeq(_this_, other):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_4b95fdf2
        
        if jsNot(jsInstanceOf(other, jsClass())):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_25727f74
        
        if True:
            pass
        
        tmp0_other_with_cast = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_35dbed4f
        if jsNot(jsEqeqeq(name, name)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_53a4637c
        
        if jsNot(equals(upperBounds, upperBounds)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_2c226db0
        
        if jsNot(variance.equals(variance)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_10db002c
        
        if jsNot(jsEqeqeq(isReified, isReified)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_5205b2e5
        
        return True
    

def _get_functionClasses_():
    return functionClasses

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_3abe8714 = 0
class _no_name_provided_:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_1acfd193
    
    def invoke(self, it):
        return isObject(it)
    
    def invoke(self, p1):
        return _this_.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_1b6ad296)
    

class _no_name_provided_:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_7fe1dee9
    
    def invoke(self, it):
        return isNumber(it)
    
    def invoke(self, p1):
        return _this_.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_14c5f96)
    

class _no_name_provided_:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_564c9626
    
    def invoke(self, it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_61523c3
    
    def invoke(self, p1):
        return _this_.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_37f5c5fd)
    

class _no_name_provided_:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_4dd1d767
    
    def invoke(self, it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_45f53ff6
    
    def invoke(self, p1):
        return _this_.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_459dea3e)
    

class _no_name_provided_:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_143cb21
    
    def invoke(self, it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_447d14a9
    
    def invoke(self, p1):
        return _this_.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6203846e)
    

class _no_name_provided_:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_3611cae8
    
    def invoke(self, it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6056e9b4
    
    def invoke(self, p1):
        return _this_.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_16a1738d)
    

class _no_name_provided_:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_53a3132f
    
    def invoke(self, it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2ab75fdc
    
    def invoke(self, p1):
        return _this_.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_55fd98e2)
    

class _no_name_provided_:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_67ea360f
    
    def invoke(self, it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_16abeca6
    
    def invoke(self, p1):
        return _this_.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6f79d583)
    

class _no_name_provided_:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_145f4f6c
    
    def invoke(self, it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_602d2058
    
    def invoke(self, p1):
        return _this_.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3b3809e2)
    

class _no_name_provided_:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_26c700ff
    
    def invoke(self, it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_7ec33496
    
    def invoke(self, p1):
        return _this_.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_517c30f)
    

class _no_name_provided_:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_5e24661a
    
    def invoke(self, it):
        return jsInstanceOf(it, jsClass())
    
    def invoke(self, p1):
        return _this_.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3b71b6b1)
    

class _no_name_provided_:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_47f71f50
    
    def invoke(self, it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_78c3b3ec
    
    def invoke(self, p1):
        return _this_.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3babb257)
    

class _no_name_provided_:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_40bf36b1
    
    def invoke(self, it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2294d35c
    
    def invoke(self, p1):
        return _this_.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3ccbc947)
    

class _no_name_provided_:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_5c56cb6d
    
    def invoke(self, it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_9f3d1b9
    
    def invoke(self, p1):
        return _this_.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_174058f0)
    

class _no_name_provided_:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_54366cf2
    
    def invoke(self, it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4a8afcae
    
    def invoke(self, p1):
        return _this_.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_21c1fb2e)
    

class _no_name_provided_:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_433b7810
    
    def invoke(self, it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6b6371a0
    
    def invoke(self, p1):
        return _this_.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_34f7b98b)
    

class _no_name_provided_:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_22c73577
    
    def invoke(self, it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_28e8c2d6
    
    def invoke(self, p1):
        return _this_.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3e843b50)
    

class _no_name_provided_:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_5eb0f030
    
    def invoke(self, it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_70fd626f
    
    def invoke(self, p1):
        return _this_.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_60bdba16)
    

class _no_name_provided_:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_2fe310b
    
    def invoke(self, it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_20de2518
    
    def invoke(self, p1):
        return _this_.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4d5d8bdb)
    

class _no_name_provided_:
    def _init_(_arity):
        _this_._arity = _arity
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_1487c3b3
    
    def invoke(self, it):
        tmp
        if jsEqeqeq(jsTypeOf(it), 'function'):
            tmp = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_75abea6
        
        if True:
            tmp = False
        
        return tmp
    
    def invoke(self, p1):
        return _this_.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_52924c1c)
    

class PrimitiveClasses:
    def _init_():
        PrimitiveClasses_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_2822ee4b
        tmp = _this_
        tmp0_unsafeCast_0 = js('Object')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.anyClass = PrimitiveKClassImpl(tmp, 'Any', _no_name_provided__factory())
        tmp = _this_
        tmp0_unsafeCast_0 = js('Number')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.numberClass = PrimitiveKClassImpl(tmp, 'Number', _no_name_provided__factory())
        _this_.nothingClass = NothingKClassImpl_getInstance()
        tmp = _this_
        tmp0_unsafeCast_0 = js('Boolean')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.booleanClass = PrimitiveKClassImpl(tmp, 'Boolean', _no_name_provided__factory())
        tmp = _this_
        tmp0_unsafeCast_0 = js('Number')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.byteClass = PrimitiveKClassImpl(tmp, 'Byte', _no_name_provided__factory())
        tmp = _this_
        tmp0_unsafeCast_0 = js('Number')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.shortClass = PrimitiveKClassImpl(tmp, 'Short', _no_name_provided__factory())
        tmp = _this_
        tmp0_unsafeCast_0 = js('Number')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.intClass = PrimitiveKClassImpl(tmp, 'Int', _no_name_provided__factory())
        tmp = _this_
        tmp0_unsafeCast_0 = js('Number')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.floatClass = PrimitiveKClassImpl(tmp, 'Float', _no_name_provided__factory())
        tmp = _this_
        tmp0_unsafeCast_0 = js('Number')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.doubleClass = PrimitiveKClassImpl(tmp, 'Double', _no_name_provided__factory())
        tmp = _this_
        tmp0_unsafeCast_0 = js('Array')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.arrayClass = PrimitiveKClassImpl(tmp, 'Array', _no_name_provided__factory())
        tmp = _this_
        tmp0_unsafeCast_0 = js('String')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.stringClass = PrimitiveKClassImpl(tmp, 'String', _no_name_provided__factory())
        tmp = _this_
        tmp0_unsafeCast_0 = js('Error')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.throwableClass = PrimitiveKClassImpl(tmp, 'Throwable', _no_name_provided__factory())
        tmp = _this_
        tmp0_unsafeCast_0 = js('Array')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.booleanArrayClass = PrimitiveKClassImpl(tmp, 'BooleanArray', _no_name_provided__factory())
        tmp = _this_
        tmp0_unsafeCast_0 = js('Uint16Array')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.charArrayClass = PrimitiveKClassImpl(tmp, 'CharArray', _no_name_provided__factory())
        tmp = _this_
        tmp0_unsafeCast_0 = js('Int8Array')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.byteArrayClass = PrimitiveKClassImpl(tmp, 'ByteArray', _no_name_provided__factory())
        tmp = _this_
        tmp0_unsafeCast_0 = js('Int16Array')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.shortArrayClass = PrimitiveKClassImpl(tmp, 'ShortArray', _no_name_provided__factory())
        tmp = _this_
        tmp0_unsafeCast_0 = js('Int32Array')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.intArrayClass = PrimitiveKClassImpl(tmp, 'IntArray', _no_name_provided__factory())
        tmp = _this_
        tmp0_unsafeCast_0 = js('Array')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.longArrayClass = PrimitiveKClassImpl(tmp, 'LongArray', _no_name_provided__factory())
        tmp = _this_
        tmp0_unsafeCast_0 = js('Float32Array')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.floatArrayClass = PrimitiveKClassImpl(tmp, 'FloatArray', _no_name_provided__factory())
        tmp = _this_
        tmp0_unsafeCast_0 = js('Float64Array')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.doubleArrayClass = PrimitiveKClassImpl(tmp, 'DoubleArray', _no_name_provided__factory())
    
    def _get_anyClass_(self):
        return anyClass
    
    def _get_numberClass_(self):
        return numberClass
    
    def _get_nothingClass_(self):
        return nothingClass
    
    def _get_booleanClass_(self):
        return booleanClass
    
    def _get_byteClass_(self):
        return byteClass
    
    def _get_shortClass_(self):
        return shortClass
    
    def _get_intClass_(self):
        return intClass
    
    def _get_floatClass_(self):
        return floatClass
    
    def _get_doubleClass_(self):
        return doubleClass
    
    def _get_arrayClass_(self):
        return arrayClass
    
    def _get_stringClass_(self):
        return stringClass
    
    def _get_throwableClass_(self):
        return throwableClass
    
    def _get_booleanArrayClass_(self):
        return booleanArrayClass
    
    def _get_charArrayClass_(self):
        return charArrayClass
    
    def _get_byteArrayClass_(self):
        return byteArrayClass
    
    def _get_shortArrayClass_(self):
        return shortArrayClass
    
    def _get_intArrayClass_(self):
        return intArrayClass
    
    def _get_longArrayClass_(self):
        return longArrayClass
    
    def _get_floatArrayClass_(self):
        return floatArrayClass
    
    def _get_doubleArrayClass_(self):
        return doubleArrayClass
    
    def functionClass(self, arity):
        tmp0_elvis_lhs = jsArrayGet(functionClasses, arity)
        tmp
        if jsEqeq(tmp0_elvis_lhs, None):
            tmp0_unsafeCast_0_3 = js('Function')
            tmp = kotlin_Any_(tmp0_unsafeCast_0_3)
            tmp = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_582b8d30
            result_2 = PrimitiveKClassImpl(tmp, tmp, _no_name_provided__factory(arity))
            tmp1_asDynamic_0_5 = functionClasses
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_53da3955
            tmp = result_2
        
        if True:
            tmp = tmp0_elvis_lhs
        
        return tmp
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_29420437 = 0
def PrimitiveClasses_getInstance():
    if jsEqeq(PrimitiveClasses_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_3d9033b
    
    return PrimitiveClasses_instance

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_11e3225c

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_17b9c3aa

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_5991020b

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_45d7e92

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_215f2743

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_3217fef1

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_4241aecb

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_21e5812b

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_6f1c19d

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_51ddc08e

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_57c09e37

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_2db51c5b

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_20c3f767

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_ddcd9f1

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_3d04a253

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_652b77eb

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_28449652

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_2f2c41d3

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_3bd3d820

def _no_name_provided__factory(_arity):
    i = _no_name_provided_(_arity)
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_47d054db

def functionClasses_init_():
    tmp0_arrayOfNulls_0 = 0
    return fillArrayVal(Array(tmp0_arrayOfNulls_0), None)

def getKClass(jClass):
    tmp
    if kotlin_Boolean(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_67d4e8f7):
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
        tmp1_unsafeCast_0 = ErrorKClass()
        tmp = kotlin_Any_(tmp1_unsafeCast_0)
    
    return tmp

def getKClass1(jClass):
    if jsEqeqeq(jClass, js('String')):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_7d9d59df
    
    metadata = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicMemberExpressionImpl_3a770af8
    tmp
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_4b6e296a:
        tmp
        if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_791b9887:
            kClass = SimpleKClassImpl(jClass)
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_7c689379
            tmp = kClass
        
        if True:
            tmp = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicMemberExpressionImpl_5a816a78
        
        tmp = kotlin_reflect_KClass_T_(tmp)
    
    if True:
        tmp = SimpleKClassImpl(jClass)
    
    return tmp

def getKClassFromExpression(e):
    tmp0_subject = jsTypeOf(e)
    tmp
    if jsEqeqeq(tmp0_subject, 'string'):
        tmp = stringClass
    
    if jsEqeqeq(tmp0_subject, 'number'):
        tmp
        tmp0_asDynamic_0 = jsBitwiseOr(e, 0)
        if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_77095c8c:
            tmp = intClass
        
        if True:
            if True:
                tmp = doubleClass
            
        
        tmp = tmp
    
    if jsEqeqeq(tmp0_subject, 'boolean'):
        tmp = booleanClass
    
    if jsEqeqeq(tmp0_subject, 'function'):
        tmp = PrimitiveClasses_getInstance()
        tmp = tmp.functionClass(kotlin_Int(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicMemberExpressionImpl_64bcf689))
    
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
                                                    constructor = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicMemberExpressionImpl_9918487
                                                    tmp
                                                    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_59f0ef6e:
                                                        tmp = anyClass
                                                    
                                                    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_8a0447e:
                                                        tmp = throwableClass
                                                    
                                                    if True:
                                                        jsClass = kotlin_js_JsClass_T_(constructor)
                                                        tmp = getKClass1(jsClass)
                                                    
                                                    tmp = tmp
                                                
                                            
                                        
                                    
                                
                            
                        
                    
                
            
        
        tmp = tmp
    
    tmp1_unsafeCast_0 = tmp
    return kotlin_Any_(tmp1_unsafeCast_0)

class Appendable:
    def append(self, value):
        pass
    
    def append(self, value):
        pass
    
    def append(self, value, startIndex, endIndex):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def _init_():
        pass
    

def StringBuilder_init__Init_(capacity, _this):
    StringBuilder_init__Init_(_this)
    return _this

def StringBuilder_init__Create_(capacity):
    return StringBuilder_init__Init_(capacity, Object_create())

def StringBuilder_init__Init_(content, _this):
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_61725c0e
    return _this

def StringBuilder_init__Create_(content):
    return StringBuilder_init__Init_(content, Object_create())

def StringBuilder_init__Init_(_this):
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_5be872b6
    return _this

def StringBuilder_init__Create_():
    return StringBuilder_init__Init_(Object_create())

def _set_string_(_this, _set___):
    _this.string = _set___

def _get_string_(_this):
    return string

def checkReplaceRange(_this, startIndex, endIndex, length):
    if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_7e5ffe4e:
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_f57058f
    
    if jsGt(startIndex, endIndex):
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_6cd7d43f
    

class StringBuilder:
    def _init_(content):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_7b01f056
        _this_.string = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_7b0dc526
    
    def _get_length_(self):
        tmp0_asDynamic_0 = string
        return kotlin_Int(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicMemberExpressionImpl_406ea770)
    
    def get(self, index):
        tmp0_getOrElse_0 = string
        tmp
        if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2c44833f:
            tmp = charSequenceGet(tmp0_getOrElse_0, index)
        
        if True:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_131879fc
        
        return tmp
    
    def subSequence(self, startIndex, endIndex):
        tmp0_substring_0 = string
        return kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_3ca941f6)
    
    def append(self, value):
        tmp0_this = _this_
        tmp0_this.string = jsPlus(string, value)
        return _this_
    
    def append(self, value):
        tmp0_this = _this_
        tmp0_this.string = jsPlus(string, toString())
        return _this_
    
    def append(self, value, startIndex, endIndex):
        tmp0_elvis_lhs = value
        return _this_.appendRange(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_23edc081, startIndex, endIndex)
    
    def reverse(self):
        reversed = ''
        index = jsBitOr(jsMinus(jsArrayLength(string), 1), 0)
        while jsGtEq(index, 0):
            tmp = string
            tmp0 = index
            index = jsBitOr(jsMinus(tmp0, 1), 0)
            low = charSequenceGet(tmp, tmp0)
            if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_47b9622:
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
    
    def append(self, value):
        tmp0_this = _this_
        tmp0_this.string = jsPlus(string, toString())
        return _this_
    
    def append(self, value):
        tmp0_this = _this_
        tmp0_this.string = jsPlus(string, value)
        return _this_
    
    def append(self, value):
        tmp0_this = _this_
        tmp0_this.string = jsPlus(string, concatToString())
        return _this_
    
    def append(self, value):
        return _this_.append(value)
    
    def append(self, value):
        tmp0_this = _this_
        tmp = tmp0_this
        tmp = string
        tmp1_elvis_lhs = value
        tmp.string = jsPlus(tmp, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6ff9b4f2)
        return _this_
    
    def capacity(self):
        return _this_._get_length_()
    
    def ensureCapacity(self, minimumCapacity):
        pass
    
    def indexOf(self, string):
        tmp0_asDynamic_0 = string
        return kotlin_Int(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_3fe8d57a)
    
    def indexOf(self, string, startIndex):
        tmp0_asDynamic_0 = string
        return kotlin_Int(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_64b262a7)
    
    def lastIndexOf(self, string):
        tmp0_asDynamic_0 = string
        return kotlin_Int(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_61d1315b)
    
    def lastIndexOf(self, string, startIndex):
        tmp
        if jsEqeqeq(charSequenceLength(string), 0):
            tmp = jsLt(startIndex, 0)
        
        if True:
            if True:
                tmp = False
            
        
        if tmp:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_60035f1e
        
        if True:
            pass
        
        tmp0_asDynamic_0 = string
        return kotlin_Int(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_2459715c)
    
    def insert(self, index, value):
        Companion_getInstance().checkPositionIndex(index, _this_._get_length_())
        tmp = _this_
        tmp0_substring_0 = string
        tmp1_substring_0 = 0
        tmp = jsPlus(kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_4e7148dd), value)
        tmp2_substring_0 = string
        tmp.string = jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_126606bc))
        return _this_
    
    def insert(self, index, value):
        Companion_getInstance().checkPositionIndex(index, _this_._get_length_())
        tmp = _this_
        tmp0_substring_0 = string
        tmp1_substring_0 = 0
        tmp = jsPlus(kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_4d957f5a), value)
        tmp2_substring_0 = string
        tmp.string = jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_669abb5c))
        return _this_
    
    def insert(self, index, value):
        Companion_getInstance().checkPositionIndex(index, _this_._get_length_())
        tmp = _this_
        tmp0_substring_0 = string
        tmp1_substring_0 = 0
        tmp = jsPlus(kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_548b7e1a), concatToString())
        tmp2_substring_0 = string
        tmp.string = jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_5f6ef272))
        return _this_
    
    def insert(self, index, value):
        Companion_getInstance().checkPositionIndex(index, _this_._get_length_())
        tmp = _this_
        tmp0_substring_0 = string
        tmp1_substring_0 = 0
        tmp = jsPlus(kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_416374ec), toString())
        tmp2_substring_0 = string
        tmp.string = jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_485b39d6))
        return _this_
    
    def insert(self, index, value):
        Companion_getInstance().checkPositionIndex(index, _this_._get_length_())
        tmp = _this_
        tmp0_substring_0 = string
        tmp1_substring_0 = 0
        tmp = jsPlus(kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_29ff6e15), toString())
        tmp2_substring_0 = string
        tmp.string = jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_76242b2c))
        return _this_
    
    def insert(self, index, value):
        return _this_.insert(index, value)
    
    def insert(self, index, value):
        Companion_getInstance().checkPositionIndex(index, _this_._get_length_())
        tmp0_elvis_lhs = value
        toInsert = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2ee6cb8a
        tmp = _this_
        tmp0_substring_0 = string
        tmp1_substring_0 = 0
        tmp = jsPlus(kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_7ee8882a), toInsert)
        tmp2_substring_0 = string
        tmp.string = jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_526c0134))
        return _this_
    
    def setLength(self, newLength):
        if jsLt(newLength, 0):
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_3619ecd
        
        if jsLtEq(newLength, _this_._get_length_()):
            tmp = _this_
            tmp0_substring_0 = string
            tmp1_substring_0 = 0
            tmp.string = kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_4d0aa772)
        
        if True:
            inductionVariable = _this_._get_length_()
            if jsLt(inductionVariable, newLength):
                visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_3fa87583
            
        
    
    def substring(self, startIndex):
        Companion_getInstance().checkPositionIndex(startIndex, _this_._get_length_())
        tmp0_substring_0 = string
        return kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_2c895dff)
    
    def substring(self, startIndex, endIndex):
        Companion_getInstance().checkBoundsIndexes(startIndex, endIndex, _this_._get_length_())
        tmp0_substring_0 = string
        return kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_70224e31)
    
    def trimToSize(self):
        pass
    
    def toString(self):
        return string
    
    def clear(self):
        _this_.string = ''
        return _this_
    
    def set(self, index, value):
        Companion_getInstance().checkElementIndex(index, _this_._get_length_())
        tmp = _this_
        tmp0_substring_0 = string
        tmp1_substring_0 = 0
        tmp = jsPlus(kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_6bc04a88), value)
        tmp2_substring_0 = string
        tmp3_substring_0 = jsBitOr(jsPlus(index, 1), 0)
        tmp.string = jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_1cd7de2))
    
    def setRange(self, startIndex, endIndex, value):
        checkReplaceRange(_this_, startIndex, endIndex, _this_._get_length_())
        tmp = _this_
        tmp0_substring_0 = string
        tmp1_substring_0 = 0
        tmp = jsPlus(kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_84b0639), value)
        tmp2_substring_0 = string
        tmp.string = jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_1fa0e5a8))
        return _this_
    
    def deleteAt(self, index):
        Companion_getInstance().checkElementIndex(index, _this_._get_length_())
        tmp = _this_
        tmp0_substring_0 = string
        tmp1_substring_0 = 0
        tmp = kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_2d38cc6)
        tmp2_substring_0 = string
        tmp3_substring_0 = jsBitOr(jsPlus(index, 1), 0)
        tmp.string = jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_a891214))
        return _this_
    
    def deleteRange(self, startIndex, endIndex):
        checkReplaceRange(_this_, startIndex, endIndex, _this_._get_length_())
        tmp = _this_
        tmp0_substring_0 = string
        tmp1_substring_0 = 0
        tmp = kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_6b61b3a8)
        tmp2_substring_0 = string
        tmp.string = jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_1b5c2310))
        return _this_
    
    def toCharArray(self, destination, destinationOffset, startIndex, endIndex):
        Companion_getInstance().checkBoundsIndexes(startIndex, endIndex, _this_._get_length_())
        Companion_getInstance().checkBoundsIndexes(destinationOffset, jsBitOr(jsMinus(jsBitOr(jsPlus(destinationOffset, endIndex), 0), startIndex), 0), jsArrayLength(destination))
        dstIndex = destinationOffset
        inductionVariable = startIndex
        if jsLt(inductionVariable, endIndex):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_687bf48e
        
    
    def toCharArray_default(self, destination, destinationOffset, startIndex, endIndex, _mask0, _handler):
        if jsNot(jsEqeqeq(jsBitAnd(_mask0, 2), 0)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_fe618cc
        
        if jsNot(jsEqeqeq(jsBitAnd(_mask0, 4), 0)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_603af797
        
        if jsNot(jsEqeqeq(jsBitAnd(_mask0, 8), 0)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_5b1965ea
        
        return _this_.toCharArray(destination, destinationOffset, startIndex, endIndex)
    
    def appendRange(self, value, startIndex, endIndex):
        tmp0_this = _this_
        tmp0_this.string = jsPlus(string, concatToString(startIndex, endIndex))
        return _this_
    
    def appendRange(self, value, startIndex, endIndex):
        stringCsq = toString(value)
        Companion_getInstance().checkBoundsIndexes(startIndex, endIndex, jsArrayLength(stringCsq))
        tmp0_this = _this_
        tmp = tmp0_this
        tmp = string
        tmp.string = jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_299bdcbf))
        return _this_
    
    def insertRange(self, index, value, startIndex, endIndex):
        Companion_getInstance().checkPositionIndex(index, _this_._get_length_())
        tmp = _this_
        tmp0_substring_0 = string
        tmp1_substring_0 = 0
        tmp = jsPlus(kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_79781e77), concatToString(startIndex, endIndex))
        tmp2_substring_0 = string
        tmp.string = jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_584b3bdc))
        return _this_
    
    def insertRange(self, index, value, startIndex, endIndex):
        Companion_getInstance().checkPositionIndex(index, _this_._get_length_())
        stringCsq = toString(value)
        Companion_getInstance().checkBoundsIndexes(startIndex, endIndex, jsArrayLength(stringCsq))
        tmp = _this_
        tmp0_substring_0 = string
        tmp1_substring_0 = 0
        tmp = kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_5a77475d)
        tmp = jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_3db1ebbb))
        tmp2_substring_0 = string
        tmp.string = jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_3cd7ca94))
        return _this_
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    

def isLowSurrogate():
    containsLower = Char(56320)
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_da3cab

def isHighSurrogate():
    containsLower = Char(55296)
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_1992ce66

def checkRadix(radix):
    if jsNot(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_105be2d9):
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_2d4eba14
    
    return radix

def _get_STRING_CASE_INSENSITIVE_ORDER_():
    return STRING_CASE_INSENSITIVE_ORDER

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_2693b289 = 0
def nativeLastIndexOf(str, fromIndex):
    return kotlin_Int(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_1fe56f3e)

def substring(startIndex, endIndex):
    return kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_73756237)

def substring(startIndex):
    return kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_68fb4908)

def compareTo(other, ignoreCase):
    if ignoreCase:
        n1 = jsArrayLength(_this_)
        n2 = jsArrayLength(other)
        min = visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl_3d8904f8.min(int32ArrayOf(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_6a348e99))
        if jsEqeqeq(min, 0):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_4691e2f5
        
        start = 0
        while True:
            tmp0_minOf_0 = jsBitOr(jsPlus(start, 16), 0)
            end = visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl_40dc88ca.min(int32ArrayOf(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_3f9d5896))
            tmp1_substring_0 = start
            s1 = kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_2241cafe)
            tmp2_substring_0 = start
            s2 = kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_531b77d)
            if jsNot(jsEqeqeq(s1, s2)):
                tmp3_toUpperCase_0 = s1
                s1 = kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_3baeb38d)
                tmp4_toUpperCase_0 = s2
                s2 = kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_709b21e0)
                if jsNot(jsEqeqeq(s1, s2)):
                    tmp5_toLowerCase_0 = s1
                    s1 = kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_727d51a)
                    tmp6_toLowerCase_0 = s2
                    s2 = kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_fb8fa44)
                    if jsNot(jsEqeqeq(s1, s2)):
                        return compareTo(s1, s2)
                    
                
            
            if jsEqeqeq(end, min):
                visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrBreakImpl_5e1d6ace
            
            start = end
        
        return jsBitOr(jsMinus(n1, n2), 0)
    
    if True:
        return compareTo(_this_, other)
    

def compareTo_default(other, ignoreCase, _mask0, _handler):
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 2), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_32124a62
    
    return compareTo(other, ignoreCase)

def toUpperCase():
    return kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_1c5c560a)

def toLowerCase():
    return kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_d57ba2a)

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
    Companion_getInstance().checkBoundsIndexes(startIndex, endIndex, jsArrayLength(_this_))
    result = ''
    inductionVariable = startIndex
    if jsLt(inductionVariable, endIndex):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_761a8ca1
    
    return result

def concatToString_default(startIndex, endIndex, _mask0, _handler):
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 1), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_34e79514
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 2), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_662c71e5
    
    return concatToString(startIndex, endIndex)

class sam_kotlin_Comparator_0:
    def _init_(function):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_32d608ce
        _this_.function = function
    
    def compare(self, a, b):
        return function.invoke(a, b)
    
    def compare(self, a, b):
        return _this_.compare(a, b)
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class _no_name_provided_:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_69faebc2
    
    def invoke(self, a, b):
        return compareTo(b, True)
    
    def invoke(self, p1, p2):
        tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4473d830
        return _this_.invoke(tmp, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3864569f)
    

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_6c1ff6a9

def STRING_CASE_INSENSITIVE_ORDER_init_():
    tmp = _no_name_provided__factory()
    return sam_kotlin_Comparator_0(tmp)

def _get_REPLACEMENT_BYTE_SEQUENCE_():
    return REPLACEMENT_BYTE_SEQUENCE

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_611d867 = 0
def REPLACEMENT_BYTE_SEQUENCE_init_():
    tmp0_byteArrayOf_0 = int8ArrayOf(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_694330ff)
    return tmp0_byteArrayOf_0

def _get_value_(_this):
    return value

class Companion:
    def _init_():
        Companion_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_15a8b228
        _this_.MIN_VALUE = Char(0)
        _this_.MAX_VALUE = Char(65535)
        _this_.MIN_HIGH_SURROGATE = Char(55296)
        _this_.MAX_HIGH_SURROGATE = Char(56319)
        _this_.MIN_LOW_SURROGATE = Char(56320)
        _this_.MAX_LOW_SURROGATE = Char(57343)
        _this_.MIN_SURROGATE = Char(55296)
        _this_.MAX_SURROGATE = Char(57343)
        _this_.SIZE_BYTES = 2
        _this_.SIZE_BITS = 16
    
    def _get_MIN_VALUE_(self):
        return MIN_VALUE
    
    def _get_MAX_VALUE_(self):
        return MAX_VALUE
    
    def _get_MIN_HIGH_SURROGATE_(self):
        return MIN_HIGH_SURROGATE
    
    def _get_MAX_HIGH_SURROGATE_(self):
        return MAX_HIGH_SURROGATE
    
    def _get_MIN_LOW_SURROGATE_(self):
        return MIN_LOW_SURROGATE
    
    def _get_MAX_LOW_SURROGATE_(self):
        return MAX_LOW_SURROGATE
    
    def _get_MIN_SURROGATE_(self):
        return MIN_SURROGATE
    
    def _get_MAX_SURROGATE_(self):
        return MAX_SURROGATE
    
    def _get_SIZE_BYTES_(self):
        return SIZE_BYTES
    
    def _get_SIZE_BITS_(self):
        return SIZE_BITS
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_a0b221f = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_b46b5ef
    
    return Companion_instance

class Char:
    def _init_(value):
        Companion_getInstance()
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_124ba047
        _this_.value = value
    
    def compareTo(self, other):
        return jsBitOr(jsMinus(value, value), 0)
    
    def compareTo(self, other):
        return _this_.compareTo(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3561a0f7)
    
    def plus(self, other):
        return numberToChar(jsBitOr(jsPlus(value, other), 0))
    
    def minus(self, other):
        return jsBitOr(jsMinus(value, value), 0)
    
    def minus(self, other):
        return numberToChar(jsBitOr(jsMinus(value, other), 0))
    
    def inc(self):
        return numberToChar(jsBitOr(jsPlus(value, 1), 0))
    
    def dec(self):
        return numberToChar(jsBitOr(jsMinus(value, 1), 0))
    
    def rangeTo(self, other):
        return CharRange(_this_, other)
    
    def toByte(self):
        return toByte(value)
    
    def toChar(self):
        return _this_
    
    def toShort(self):
        return toShort(value)
    
    def toInt(self):
        return value
    
    def toLong(self):
        return toLong(value)
    
    def toFloat(self):
        return kotlin_Float(value)
    
    def toDouble(self):
        return kotlin_Double(value)
    
    def equals(self, other):
        if jsEqeqeq(other, _this_):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_2b35976a
        
        if jsNot(jsInstanceOf(other, jsClass())):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_67a6f2c4
        
        if True:
            pass
        
        return jsEqeqeq(value, value)
    
    def hashCode(self):
        return value
    
    def toString(self):
        tmp0_unsafeCast_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_4a282c78
        return kotlin_Any_(tmp0_unsafeCast_0)
    

class Iterable:
    def iterator(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def _init_():
        pass
    

class Collection:
    def _get_size_(self):
        pass
    
    def isEmpty(self):
        pass
    
    def contains(self, element):
        pass
    
    def iterator(self):
        pass
    
    def containsAll(self, elements):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def _init_():
        pass
    

class List:
    def _get_size_(self):
        pass
    
    def isEmpty(self):
        pass
    
    def contains(self, element):
        pass
    
    def iterator(self):
        pass
    
    def containsAll(self, elements):
        pass
    
    def get(self, index):
        pass
    
    def indexOf(self, element):
        pass
    
    def lastIndexOf(self, element):
        pass
    
    def listIterator(self):
        pass
    
    def listIterator(self, index):
        pass
    
    def subList(self, fromIndex, toIndex):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def _init_():
        pass
    

class MutableList:
    def add(self, element):
        pass
    
    def remove(self, element):
        pass
    
    def addAll(self, elements):
        pass
    
    def addAll(self, index, elements):
        pass
    
    def removeAll(self, elements):
        pass
    
    def retainAll(self, elements):
        pass
    
    def clear(self):
        pass
    
    def set(self, index, element):
        pass
    
    def add(self, index, element):
        pass
    
    def removeAt(self, index):
        pass
    
    def listIterator(self):
        pass
    
    def listIterator(self, index):
        pass
    
    def subList(self, fromIndex, toIndex):
        pass
    
    def _get_size_(self):
        pass
    
    def isEmpty(self):
        pass
    
    def contains(self, element):
        pass
    
    def iterator(self):
        pass
    
    def containsAll(self, elements):
        pass
    
    def get(self, index):
        pass
    
    def indexOf(self, element):
        pass
    
    def lastIndexOf(self, element):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def _init_():
        pass
    

class MutableCollection:
    def iterator(self):
        pass
    
    def add(self, element):
        pass
    
    def remove(self, element):
        pass
    
    def addAll(self, elements):
        pass
    
    def removeAll(self, elements):
        pass
    
    def retainAll(self, elements):
        pass
    
    def clear(self):
        pass
    
    def _get_size_(self):
        pass
    
    def isEmpty(self):
        pass
    
    def contains(self, element):
        pass
    
    def containsAll(self, elements):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def _init_():
        pass
    

class MutableIterable:
    def iterator(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def _init_():
        pass
    

class Set:
    def _get_size_(self):
        pass
    
    def isEmpty(self):
        pass
    
    def contains(self, element):
        pass
    
    def iterator(self):
        pass
    
    def containsAll(self, elements):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def _init_():
        pass
    

class Entry:
    def _get_key_(self):
        pass
    
    def _get_value_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def _init_():
        pass
    

class Map:
    def _get_size_(self):
        pass
    
    def isEmpty(self):
        pass
    
    def containsKey(self, key):
        pass
    
    def containsValue(self, value):
        pass
    
    def get(self, key):
        pass
    
    def _get_keys_(self):
        pass
    
    def _get_values_(self):
        pass
    
    def _get_entries_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def _init_():
        pass
    

class MutableSet:
    def iterator(self):
        pass
    
    def add(self, element):
        pass
    
    def remove(self, element):
        pass
    
    def addAll(self, elements):
        pass
    
    def removeAll(self, elements):
        pass
    
    def retainAll(self, elements):
        pass
    
    def clear(self):
        pass
    
    def _get_size_(self):
        pass
    
    def isEmpty(self):
        pass
    
    def contains(self, element):
        pass
    
    def containsAll(self, elements):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def _init_():
        pass
    

class MutableEntry:
    def setValue(self, newValue):
        pass
    
    def _get_key_(self):
        pass
    
    def _get_value_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def _init_():
        pass
    

class MutableMap:
    def put(self, key, value):
        pass
    
    def remove(self, key):
        pass
    
    def putAll(self, _from):
        pass
    
    def clear(self):
        pass
    
    def _get_keys_(self):
        pass
    
    def _get_values_(self):
        pass
    
    def _get_entries_(self):
        pass
    
    def _get_size_(self):
        pass
    
    def isEmpty(self):
        pass
    
    def containsKey(self, key):
        pass
    
    def containsValue(self, value):
        pass
    
    def get(self, key):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def _init_():
        pass
    

class Companion:
    def _init_():
        Companion_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_10ac5a14
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_5e220be6 = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_27a4a890
    
    return Companion_instance

class Enum:
    def _init_(name, ordinal):
        Companion_getInstance()
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_249c96cf
        _this_.name = name
        _this_.ordinal = ordinal
    
    def _get_name_(self):
        return name
    
    def _get_ordinal_(self):
        return ordinal
    
    def compareTo(self, other):
        return compareTo(ordinal, ordinal)
    
    def compareTo(self, other):
        return _this_.compareTo(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_7fdcccd5)
    
    def equals(self, other):
        return jsEqeqeq(_this_, other)
    
    def hashCode(self):
        return identityHashCode(_this_)
    
    def toString(self):
        return name
    

def byteArrayOf(elements):
    return elements

def arrayOf(elements):
    return kotlin_Any_(elements)

def toString():
    tmp0_safe_receiver = _this_
    tmp1_elvis_lhs = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_349cde1a
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_7bc81a1f

def plus(other):
    tmp2_safe_receiver = _this_
    tmp3_elvis_lhs = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_71a3205
    tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4b4be42c
    tmp0_safe_receiver = other
    tmp1_elvis_lhs = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4176d8a1
    return jsPlus(tmp, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_7ac397d6)

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
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_2b3247f8
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_2b7c980 = 0
def DefaultConstructorMarker_getInstance():
    if jsEqeq(DefaultConstructorMarker_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_1ab5da0c
    
    return DefaultConstructorMarker_instance

def fillArrayVal(array, initValue):
    inductionVariable = 0
    last = jsBitOr(jsMinus(jsArrayLength(array), 1), 0)
    if jsLtEq(inductionVariable, last):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_501c3ef6
    
    return array

def arrayWithFun(size, init):
    tmp0_fillArrayFun_0 = Array(size)
    result_1 = kotlin_Any_(tmp0_fillArrayFun_0)
    i_2 = 0
    while jsNot(jsEqeqeq(i_2, jsArrayLength(result_1))):
        jsArraySet(result_1, i_2, init.invoke(i_2))
        i_2 = jsBitOr(jsPlus(i_2, 1), 0)
        Unit_getInstance()
    
    return result_1

def fillArrayFun(array, init):
    result = kotlin_Any_(array)
    i = 0
    while jsNot(jsEqeqeq(i, jsArrayLength(result))):
        jsArraySet(result, i, init.invoke(i))
        i = jsBitOr(jsPlus(i, 1), 0)
        Unit_getInstance()
    
    return result

def arrayIterator(array):
    return _no_name_provided_(array)

def booleanArrayIterator(array):
    return _no_name_provided_(array)

def charArrayIterator(array):
    return _no_name_provided_(array)

def byteArrayIterator(array):
    return _no_name_provided_(array)

def shortArrayIterator(array):
    return _no_name_provided_(array)

def intArrayIterator(array):
    return _no_name_provided_(array)

def floatArrayIterator(array):
    return _no_name_provided_(array)

def longArrayIterator(array):
    return _no_name_provided_(array)

def doubleArrayIterator(array):
    return _no_name_provided_(array)

def booleanArray(size):
    tmp0_withType_0 = 'BooleanArray'
    tmp1_withType_0 = fillArrayVal(Array(size), False)
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_1b3a25b9
    tmp2_unsafeCast_0 = tmp1_withType_0
    return kotlin_Any_(tmp2_unsafeCast_0)

def charArray(size):
    tmp0_withType_0 = 'CharArray'
    tmp1_withType_0 = fillArrayVal(Array(size), Char(0))
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_16a7b925
    tmp2_unsafeCast_0 = tmp1_withType_0
    return kotlin_Any_(tmp2_unsafeCast_0)

def longArray(size):
    tmp0_withType_0 = 'LongArray'
    tmp1_withType_0 = fillArrayVal(Array(size), Long(0, 0))
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_323fdbf0
    tmp2_unsafeCast_0 = tmp1_withType_0
    return kotlin_Any_(tmp2_unsafeCast_0)

def booleanArrayOf(arr):
    tmp0_withType_0 = 'BooleanArray'
    tmp1_withType_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_586be63c
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_53348b2d
    tmp2_unsafeCast_0 = tmp1_withType_0
    return kotlin_Any_(tmp2_unsafeCast_0)

def charArrayOf(arr):
    tmp0_withType_0 = 'CharArray'
    tmp1_withType_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_2295535f
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_480318c2
    tmp2_unsafeCast_0 = tmp1_withType_0
    return kotlin_Any_(tmp2_unsafeCast_0)

def longArrayOf(arr):
    tmp0_withType_0 = 'LongArray'
    tmp1_withType_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_62a30701
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_74ca0511
    tmp2_unsafeCast_0 = tmp1_withType_0
    return kotlin_Any_(tmp2_unsafeCast_0)

class _no_name_provided_:
    def _init_(_array):
        _this_._array = _array
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_16b48082
        _this_.index = 0
    
    def _set_index_(self, _set___):
        _this_.index = _set___
    
    def _get_index_(self):
        return index
    
    def hasNext(self):
        return jsNot(jsEqeqeq(index, jsArrayLength(_array)))
    
    def next(self):
        tmp
        if jsNot(jsEqeqeq(index, jsArrayLength(_array))):
            tmp0_this = _this_
            tmp1 = index
            tmp0_this.index = jsBitOr(jsPlus(tmp1, 1), 0)
            tmp = jsArrayGet(_array, tmp1)
        
        if True:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_cc655a
        
        return tmp
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class _no_name_provided_:
    def _init_(_array):
        _this_._array = _array
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_7cc7769d
        _this_.index = 0
    
    def _set_index_(self, _set___):
        _this_.index = _set___
    
    def _get_index_(self):
        return index
    
    def hasNext(self):
        return jsNot(jsEqeqeq(index, jsArrayLength(_array)))
    
    def nextBoolean(self):
        tmp
        if jsNot(jsEqeqeq(index, jsArrayLength(_array))):
            tmp0_this = _this_
            tmp1 = index
            tmp0_this.index = jsBitOr(jsPlus(tmp1, 1), 0)
            tmp = jsArrayGet(_array, tmp1)
        
        if True:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_d0c3793
        
        return tmp
    
    def next(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class _no_name_provided_:
    def _init_(_array):
        _this_._array = _array
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_5cdf6bb1
        _this_.index = 0
    
    def _set_index_(self, _set___):
        _this_.index = _set___
    
    def _get_index_(self):
        return index
    
    def hasNext(self):
        return jsNot(jsEqeqeq(index, jsArrayLength(_array)))
    
    def nextChar(self):
        tmp
        if jsNot(jsEqeqeq(index, jsArrayLength(_array))):
            tmp0_this = _this_
            tmp1 = index
            tmp0_this.index = jsBitOr(jsPlus(tmp1, 1), 0)
            tmp = jsArrayGet(_array, tmp1)
        
        if True:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_6c5fbe8a
        
        return tmp
    
    def next(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class _no_name_provided_:
    def _init_(_array):
        _this_._array = _array
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_5bbda8aa
        _this_.index = 0
    
    def _set_index_(self, _set___):
        _this_.index = _set___
    
    def _get_index_(self):
        return index
    
    def hasNext(self):
        return jsNot(jsEqeqeq(index, jsArrayLength(_array)))
    
    def nextByte(self):
        tmp
        if jsNot(jsEqeqeq(index, jsArrayLength(_array))):
            tmp0_this = _this_
            tmp1 = index
            tmp0_this.index = jsBitOr(jsPlus(tmp1, 1), 0)
            tmp = jsArrayGet(_array, tmp1)
        
        if True:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_58070889
        
        return tmp
    
    def next(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class _no_name_provided_:
    def _init_(_array):
        _this_._array = _array
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_5a7e2f07
        _this_.index = 0
    
    def _set_index_(self, _set___):
        _this_.index = _set___
    
    def _get_index_(self):
        return index
    
    def hasNext(self):
        return jsNot(jsEqeqeq(index, jsArrayLength(_array)))
    
    def nextShort(self):
        tmp
        if jsNot(jsEqeqeq(index, jsArrayLength(_array))):
            tmp0_this = _this_
            tmp1 = index
            tmp0_this.index = jsBitOr(jsPlus(tmp1, 1), 0)
            tmp = jsArrayGet(_array, tmp1)
        
        if True:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_70f446c
        
        return tmp
    
    def next(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class _no_name_provided_:
    def _init_(_array):
        _this_._array = _array
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_2dc0cbbc
        _this_.index = 0
    
    def _set_index_(self, _set___):
        _this_.index = _set___
    
    def _get_index_(self):
        return index
    
    def hasNext(self):
        return jsNot(jsEqeqeq(index, jsArrayLength(_array)))
    
    def nextInt(self):
        tmp
        if jsNot(jsEqeqeq(index, jsArrayLength(_array))):
            tmp0_this = _this_
            tmp1 = index
            tmp0_this.index = jsBitOr(jsPlus(tmp1, 1), 0)
            tmp = jsArrayGet(_array, tmp1)
        
        if True:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_597050fa
        
        return tmp
    
    def next(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class _no_name_provided_:
    def _init_(_array):
        _this_._array = _array
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_3579682
        _this_.index = 0
    
    def _set_index_(self, _set___):
        _this_.index = _set___
    
    def _get_index_(self):
        return index
    
    def hasNext(self):
        return jsNot(jsEqeqeq(index, jsArrayLength(_array)))
    
    def nextFloat(self):
        tmp
        if jsNot(jsEqeqeq(index, jsArrayLength(_array))):
            tmp0_this = _this_
            tmp1 = index
            tmp0_this.index = jsBitOr(jsPlus(tmp1, 1), 0)
            tmp = jsArrayGet(_array, tmp1)
        
        if True:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_1cea4fdf
        
        return tmp
    
    def next(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class _no_name_provided_:
    def _init_(_array):
        _this_._array = _array
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_70cc0601
        _this_.index = 0
    
    def _set_index_(self, _set___):
        _this_.index = _set___
    
    def _get_index_(self):
        return index
    
    def hasNext(self):
        return jsNot(jsEqeqeq(index, jsArrayLength(_array)))
    
    def nextLong(self):
        tmp
        if jsNot(jsEqeqeq(index, jsArrayLength(_array))):
            tmp0_this = _this_
            tmp1 = index
            tmp0_this.index = jsBitOr(jsPlus(tmp1, 1), 0)
            tmp = jsArrayGet(_array, tmp1)
        
        if True:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_5bc3c4e5
        
        return tmp
    
    def next(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class _no_name_provided_:
    def _init_(_array):
        _this_._array = _array
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_72a522f1
        _this_.index = 0
    
    def _set_index_(self, _set___):
        _this_.index = _set___
    
    def _get_index_(self):
        return index
    
    def hasNext(self):
        return jsNot(jsEqeqeq(index, jsArrayLength(_array)))
    
    def nextDouble(self):
        tmp
        if jsNot(jsEqeqeq(index, jsArrayLength(_array))):
            tmp0_this = _this_
            tmp1 = index
            tmp0_this.index = jsBitOr(jsPlus(tmp1, 1), 0)
            tmp = jsArrayGet(_array, tmp1)
        
        if True:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_2f71bb66
        
        return tmp
    
    def next(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def _get_buf_():
    return buf

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_7469d13a = 0
def _get_bufFloat64_():
    return bufFloat64

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_54832ad9 = 0
def _get_bufFloat32_():
    return bufFloat32

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_2f42f20f = 0
def _get_bufInt32_():
    return bufInt32

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_f5475d7 = 0
def _get_lowIndex_():
    return lowIndex

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_751df26c = 0
def _get_highIndex_():
    return highIndex

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_c534814 = 0
def getNumberHashCode(obj):
    tmp0_unsafeCast_0 = jsBitwiseOr(obj, 0)
    if jsEqeqeq(kotlin_Any_(tmp0_unsafeCast_0), obj):
        return numberToInt(obj)
    
    if True:
        pass
    
    jsArraySet(bufFloat64, 0, obj)
    return jsBitOr(jsPlus(imul(jsArrayGet(bufInt32, highIndex), 31), jsArrayGet(bufInt32, lowIndex)), 0)

def bufFloat64_init_():
    tmp0_unsafeCast_0 = Float64Array(buf)
    return kotlin_Any_(tmp0_unsafeCast_0)

def bufFloat32_init_():
    tmp0_unsafeCast_0 = Float32Array(buf)
    return kotlin_Any_(tmp0_unsafeCast_0)

def bufInt32_init_():
    tmp0_unsafeCast_0 = Int32Array(buf)
    return kotlin_Any_(tmp0_unsafeCast_0)

def lowIndex_init_():
    jsArraySet(bufFloat64, 0, -1.0)
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4798d907

class DoNotIntrinsify:
    def _init_():
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def charSequenceGet(a, index):
    tmp
    if isString(a):
        tmp0_unsafeCast_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_15beb40b
        tmp = Char(kotlin_Any_(tmp0_unsafeCast_0))
    
    if True:
        tmp = a.get(index)
    
    return tmp

def isString(a):
    return jsEqeqeq(jsTypeOf(a), 'string')

def charSequenceLength(a):
    tmp
    if isString(a):
        tmp0_unsafeCast_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicMemberExpressionImpl_7a9df9b2
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
    
    if True:
        tmp = a._get_length_()
    
    return tmp

def charSequenceSubSequence(a, startIndex, endIndex):
    tmp
    if isString(a):
        tmp0_unsafeCast_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_35007b7a
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
    
    if True:
        tmp = a.subSequence(startIndex, endIndex)
    
    return tmp

def arrayToString(array):
    return joinToString_default(', ', '[', ']', 0, None, _no_name_provided__factory(), 24, None)

class _no_name_provided_:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_349cb820
    
    def invoke(self, it):
        return toString(it)
    
    def invoke(self, p1):
        return _this_.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_1a867210)
    

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_4d168798

def compareTo(a, b):
    tmp0_subject = jsTypeOf(a)
    tmp
    if jsEqeqeq(tmp0_subject, 'number'):
        tmp
        if jsEqeqeq(jsTypeOf(b), 'number'):
            tmp = doubleCompareTo(a, b)
        
        if True:
            if jsInstanceOf(b, jsClass()):
                tmp = doubleCompareTo(a, kotlin_Long(b).toDouble())
            
            if True:
                if True:
                    tmp = primitiveCompareTo(a, b)
                
            
        
        tmp = tmp
    
    if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_62fd90a2:
        tmp = primitiveCompareTo(a, b)
    
    if True:
        tmp = compareToDoNotIntrinsicify(kotlin_Comparable_dynamic_(a), b)
    
    return tmp

def doubleCompareTo(a, b):
    tmp
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_447dec7e:
        tmp = -1
    
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_335aac7a:
        tmp = 1
    
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_46135aba:
        tmp
        if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_227ca700:
            tmp = 0
        
        if True:
            tmp0_asDynamic_0 = 1
            ia = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_5271c49b
            tmp
            tmp1_asDynamic_0 = 1
            if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_2c73a332:
                tmp = 0
            
            if True:
                if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_42e74fa3:
                    tmp = -1
                
                if True:
                    if True:
                        tmp = 1
                    
                
            
            tmp = tmp
        
        tmp = tmp
    
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_282fabe9:
        tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2431682d
    
    if True:
        tmp = -1
    
    return tmp

def primitiveCompareTo(a, b):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6657c199

def compareToDoNotIntrinsicify(a, b):
    return a.compareTo(b)

def construct(constructorType, resultType, args):
    return kotlin_Any(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_1f3b8bfe)

def identityHashCode(obj):
    return getObjectHashCode(obj)

def getObjectHashCode(obj):
    if jsNot(jsIn('kotlinHashCodeValue$', kotlin_Any(obj))):
        hash = jsBitwiseOr(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_243deb3f, 0)
        descriptor = js('new Object()')
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_40977fab
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_2c63f1fe
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_83b0d9f
    
    tmp0_unsafeCast_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_25e60726
    return kotlin_Any_(tmp0_unsafeCast_0)

def _get_OBJECT_HASH_CODE_PROPERTY_NAME_():
    return OBJECT_HASH_CODE_PROPERTY_NAME

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_2d8a45a = 0
def _get_POW_2_32_():
    return POW_2_32

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_1b856d2a = 0
def toString(o):
    tmp
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_4d768435:
        tmp = 'null'
    
    if isArrayish(o):
        tmp = '[...]'
    
    if True:
        tmp0_unsafeCast_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_1475cdbb
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
    
    return tmp

def hashCode(obj):
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_4f549906:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_65dce54c
    
    tmp0_subject = jsTypeOf(obj)
    tmp
    if jsEqeqeq(tmp0_subject, 'object'):
        tmp = kotlin_Int(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2a590e2f)
    
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
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_6acc72c7
    
    return hash

def anyToString(o):
    return kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_e8acdfc)

def equals(obj1, obj2):
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_1f94df5:
        return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_1b74dd88
    
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_720bf74d:
        return False
    
    if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_78db6b8e:
        return kotlin_Boolean(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_16a4d5a9)
    
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_664e8bb7:
        return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_16adf66f
    
    if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_191a957:
        tmp
        if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_763b279:
            tmp
            if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_1aa9635c:
                tmp = True
            
            if True:
                tmp0_asDynamic_0 = 1
                tmp = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_42eb459d
                tmp1_asDynamic_0 = 1
                tmp = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_2027e9f9
            
            tmp = tmp
        
        if True:
            tmp = False
        
        return tmp
    
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_3015fc1b

def boxIntrinsic(x):
    tmp0_error_0 = 'Should be lowered'
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_290aabc9

def unboxIntrinsic(x):
    tmp0_error_0 = 'Should be lowered'
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_7bed9e3

def captureStack(instance, constructorFunction):
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_9d7d83d:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_68754439
    
    if True:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_34dcd7a1
    

def newThrowable(message, cause):
    throwable = js('new Error()')
    tmp
    if isUndefined(message):
        tmp
        if isUndefined(cause):
            tmp = message
        
        if True:
            tmp0_safe_receiver = cause
            tmp1_elvis_lhs = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2c297832
            tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2ab0ee54
        
        tmp = tmp
    
    if True:
        tmp2_elvis_lhs = message
        tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2dc59d
    
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_9eaaecf
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_2bbc6496
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_1e512b3
    return kotlin_Any_(throwable)

def isUndefined(value):
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_70a7ebc9

def extendThrowable(this_, message, cause):
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_4f34f451
    setPropertiesToThrowableInstance(this_, message, cause)

def setPropertiesToThrowableInstance(this_, message, cause):
    if jsNot(hasOwnPrototypeProperty(kotlin_Any(this_), 'message')):
        tmp
        if jsEqeq(message, None):
            tmp
            if jsNot(jsEqeqeq(message, None)):
                tmp0_safe_receiver = cause
                tmp1_elvis_lhs = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_65420507
                tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_62e6f2db
            
            if True:
                tmp = _get_undefined_()
            
            tmp = tmp
        
        if True:
            tmp = message
        
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_732d2b59
    
    if jsNot(hasOwnPrototypeProperty(kotlin_Any(this_), 'cause')):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_5d81bc79
    
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_70a8d2e1

def hasOwnPrototypeProperty(o, name):
    tmp0_unsafeCast_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_2703fabd
    return kotlin_Any_(tmp0_unsafeCast_0)

def getContinuation():
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_77070012

def returnIfSuspended(argument):
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_41a56594

def suspendCoroutineUninterceptedOrReturnJS(block):
    return block.invoke(getContinuation())

def getCoroutineContext():
    return getContinuation()._get_context_()

def ensureNotNull(v):
    tmp
    if jsEqeq(v, None):
        THROW_NPE()
    
    if True:
        tmp = v
    
    return tmp

def THROW_NPE():
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_29f0e941

def noWhenBranchMatchedException():
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_4817bd3

def THROW_CCE():
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_35b799c0

def throwUninitializedPropertyAccessException(name):
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_6ca6a1a6

def throwKotlinNothingValueException():
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_22351330

def THROW_ISE():
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_7414167a

def THROW_IAE(msg):
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_79b07ccd

def emptyArray():
    return kotlin_Array_T_(js('[]'))

def enumValueOfIntrinsic(name):
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_618cfd1

def enumValuesIntrinsic():
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_153f6a67

class Companion:
    def _init_():
        Companion_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_6b50017c
        _this_.MIN_VALUE = Long(0, -2147483648)
        _this_.MAX_VALUE = Long(-1, 2147483647)
        _this_.SIZE_BYTES = 8
        _this_.SIZE_BITS = 64
    
    def _get_MIN_VALUE_(self):
        return MIN_VALUE
    
    def _get_MAX_VALUE_(self):
        return MAX_VALUE
    
    def _get_SIZE_BYTES_(self):
        return SIZE_BYTES
    
    def _get_SIZE_BITS_(self):
        return SIZE_BITS
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_1df41490 = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_7b116131
    
    return Companion_instance

class Long:
    def _init_(low, high):
        Companion_getInstance()
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_497746ea
        _this_.low = low
        _this_.high = high
    
    def _get_low_(self):
        return low
    
    def _get_high_(self):
        return high
    
    def compareTo(self, other):
        return _this_.compareTo(toLong(other))
    
    def compareTo(self, other):
        return _this_.compareTo(toLong(other))
    
    def compareTo(self, other):
        return _this_.compareTo(toLong(other))
    
    def compareTo(self, other):
        return compare(other)
    
    def compareTo(self, other):
        return _this_.compareTo(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_fc2d07f)
    
    def compareTo(self, other):
        return compareTo(_this_.toFloat(), other)
    
    def compareTo(self, other):
        return compareTo(_this_.toDouble(), other)
    
    def plus(self, other):
        return _this_.plus(toLong(other))
    
    def plus(self, other):
        return _this_.plus(toLong(other))
    
    def plus(self, other):
        return _this_.plus(toLong(other))
    
    def plus(self, other):
        return add(other)
    
    def plus(self, other):
        return jsPlus(_this_.toFloat(), other)
    
    def plus(self, other):
        return jsPlus(_this_.toDouble(), other)
    
    def minus(self, other):
        return _this_.minus(toLong(other))
    
    def minus(self, other):
        return _this_.minus(toLong(other))
    
    def minus(self, other):
        return _this_.minus(toLong(other))
    
    def minus(self, other):
        return subtract(other)
    
    def minus(self, other):
        return jsMinus(_this_.toFloat(), other)
    
    def minus(self, other):
        return jsMinus(_this_.toDouble(), other)
    
    def times(self, other):
        return _this_.times(toLong(other))
    
    def times(self, other):
        return _this_.times(toLong(other))
    
    def times(self, other):
        return _this_.times(toLong(other))
    
    def times(self, other):
        return multiply(other)
    
    def times(self, other):
        return jsMult(_this_.toFloat(), other)
    
    def times(self, other):
        return jsMult(_this_.toDouble(), other)
    
    def div(self, other):
        return _this_.div(toLong(other))
    
    def div(self, other):
        return _this_.div(toLong(other))
    
    def div(self, other):
        return _this_.div(toLong(other))
    
    def div(self, other):
        return divide(other)
    
    def div(self, other):
        return jsDiv(_this_.toFloat(), other)
    
    def div(self, other):
        return jsDiv(_this_.toDouble(), other)
    
    def rem(self, other):
        return _this_.rem(toLong(other))
    
    def rem(self, other):
        return _this_.rem(toLong(other))
    
    def rem(self, other):
        return _this_.rem(toLong(other))
    
    def rem(self, other):
        return modulo(other)
    
    def rem(self, other):
        return jsMod(_this_.toFloat(), other)
    
    def rem(self, other):
        return jsMod(_this_.toDouble(), other)
    
    def inc(self):
        return _this_.plus(Long(1, 0))
    
    def dec(self):
        return _this_.minus(Long(1, 0))
    
    def unaryPlus(self):
        return _this_
    
    def unaryMinus(self):
        return _this_.inv().plus(Long(1, 0))
    
    def rangeTo(self, other):
        return _this_.rangeTo(toLong(other))
    
    def rangeTo(self, other):
        return _this_.rangeTo(toLong(other))
    
    def rangeTo(self, other):
        return _this_.rangeTo(toLong(other))
    
    def rangeTo(self, other):
        return LongRange(_this_, other)
    
    def shl(self, bitCount):
        return shiftLeft(bitCount)
    
    def shr(self, bitCount):
        return shiftRight(bitCount)
    
    def ushr(self, bitCount):
        return shiftRightUnsigned(bitCount)
    
    def _and(self, other):
        return Long(jsBitAnd(low, low), jsBitAnd(high, high))
    
    def _or(self, other):
        return Long(jsBitOr(low, low), jsBitOr(high, high))
    
    def xor(self, other):
        return Long(jsBitXor(low, low), jsBitXor(high, high))
    
    def inv(self):
        return Long(jsBitNot(low), jsBitNot(high))
    
    def toByte(self):
        return toByte(low)
    
    def toChar(self):
        return numberToChar(low)
    
    def toShort(self):
        return toShort(low)
    
    def toInt(self):
        return low
    
    def toLong(self):
        return _this_
    
    def toFloat(self):
        return kotlin_Float(_this_.toDouble())
    
    def toDouble(self):
        return toNumber()
    
    def valueOf(self):
        return _this_.toDouble()
    
    def equals(self, other):
        tmp
        if jsInstanceOf(other, jsClass()):
            tmp = equalsLong(kotlin_Long(other))
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def hashCode(self):
        return hashCode(_this_)
    
    def toString(self):
        return toStringImpl(10)
    

def _get_ZERO_():
    return ZERO

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_1fe275d8 = 0
def _get_ONE_():
    return ONE

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_734990c1 = 0
def _get_NEG_ONE_():
    return NEG_ONE

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_6870f52a = 0
def _get_MAX_VALUE_():
    return MAX_VALUE

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_5dca1c50 = 0
def _get_MIN_VALUE_():
    return MIN_VALUE

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_5a487b86 = 0
def _get_TWO_PWR_24__():
    return TWO_PWR_24_

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_62c4ad40 = 0
def compare(other):
    if equalsLong(other):
        return 0
    
    thisNeg = isNegative()
    otherNeg = isNegative()
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2ebc4fc

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
    return Long(jsBitOr(jsBitShiftL(c16, 16), c00), jsBitOr(jsBitShiftL(c48, 16), c32))

def subtract(other):
    return add(other.unaryMinus())

def multiply(other):
    if isZero():
        return ZERO
    
    if isZero():
        return ZERO
    
    if equalsLong(MIN_VALUE):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_384f8455
    
    if equalsLong(MIN_VALUE):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_eba9ab4
    
    if isNegative():
        tmp
        if isNegative():
            tmp = multiply(negate())
        
        if True:
            tmp = negate()
        
        return tmp
    
    if isNegative():
        return negate()
    
    if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_66c3c813:
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
    return Long(jsBitOr(jsBitShiftL(c16, 16), c00), jsBitOr(jsBitShiftL(c48, 16), c32))

def divide(other):
    if isZero():
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_7308c29a
    
    if isZero():
        return ZERO
    
    if equalsLong(MIN_VALUE):
        if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_228af76e:
            return MIN_VALUE
        
        if equalsLong(MIN_VALUE):
            return ONE
        
        if True:
            halfThis = shiftRight(1)
            approx = shiftLeft(1)
            if equalsLong(ZERO):
                return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3609424e
            
            if True:
                rem = subtract(multiply(approx))
                return add(rem.div(other))
            
        
    
    if equalsLong(MIN_VALUE):
        return ZERO
    
    if isNegative():
        tmp
        if isNegative():
            tmp = negate().div(negate())
        
        if True:
            tmp = negate()
        
        return tmp
    
    if isNegative():
        return negate()
    
    res = ZERO
    rem = _this_
    while greaterThanOrEqual(other):
        approxDouble = jsDiv(toNumber(), toNumber())
        approx2 = visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl_47ce44ab.max(1.0, visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl_26562718.floor(approxDouble))
        log2 = visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl_6ef7e510.ceil(jsDiv(visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl_76145ef9.log(approx2), visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl_5b0af511._get_LN2_()))
        delta = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_780e214b
        approxRes = fromNumber(approx2)
        approxRem = multiply(other)
        while visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2aaa635d:
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
            return Long(jsBitShiftL(low, numBits), jsBitOr(jsBitShiftL(high, numBits), jsBitShiftRU(low, jsBitOr(jsMinus(32, numBits), 0))))
        
        if True:
            return Long(0, jsBitShiftL(low, jsBitOr(jsMinus(numBits, 32), 0)))
        
    

def shiftRight(numBits):
    numBits = jsBitAnd(numBits, 63)
    if jsEqeqeq(numBits, 0):
        return _this_
    
    if True:
        if jsLt(numBits, 32):
            return Long(jsBitOr(jsBitShiftRU(low, numBits), jsBitShiftL(high, jsBitOr(jsMinus(32, numBits), 0))), jsBitShiftR(high, numBits))
        
        if True:
            return Long(jsBitShiftR(high, jsBitOr(jsMinus(numBits, 32), 0)), visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_7a8bda44)
        
    

def shiftRightUnsigned(numBits):
    numBits = jsBitAnd(numBits, 63)
    if jsEqeqeq(numBits, 0):
        return _this_
    
    if True:
        if jsLt(numBits, 32):
            return Long(jsBitOr(jsBitShiftRU(low, numBits), jsBitShiftL(high, jsBitOr(jsMinus(32, numBits), 0))), jsBitShiftRU(high, numBits))
        
        if True:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_270706e3
        
    

def toNumber():
    return jsPlus(jsMult(high, 4.294967296E9), getLowBitsUnsigned())

def equalsLong(other):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_481bd693

def hashCode(l):
    return jsBitXor(low, high)

def toStringImpl(radix):
    if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_320d4122:
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_4d05b931
    
    if isZero():
        return '0'
    
    if isNegative():
        if equalsLong(MIN_VALUE):
            radixLong = fromInt(radix)
            div = _this_.div(radixLong)
            rem = subtract(_this_).toInt()
            tmp = toStringImpl(radix)
            tmp0_unsafeCast_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_70e966a5
            return jsPlus(tmp, kotlin_Any_(tmp0_unsafeCast_0))
        
        if True:
            return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_706b5d5e
        
    
    radixToPower = fromNumber(visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl_54b2416d.pow(kotlin_Double(radix), 6.0))
    rem = _this_
    result = ''
    while True:
        remDiv = rem.div(radixToPower)
        intval = subtract(multiply(radixToPower)).toInt()
        tmp1_unsafeCast_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_27868127
        digits = kotlin_Any_(tmp1_unsafeCast_0)
        rem = remDiv
        if isZero():
            return jsPlus(digits, result)
        
        if True:
            while jsLt(jsArrayLength(digits), 6):
                digits = jsPlus('0', digits)
            
            result = jsPlus(digits, result)
        
    

def fromInt(value):
    return Long(value, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4d2eafc5)

def isNegative():
    return jsLt(high, 0)

def isZero():
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_5a209683

def isOdd():
    return jsEqeqeq(jsBitAnd(low, 1), 1)

def negate():
    return _this_.unaryMinus()

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
        return Long(jsBitwiseOr(jsMod(value, twoPwr32), 0), jsBitwiseOr(jsDiv(value, twoPwr32), 0))
    

def greaterThan(other):
    return jsGt(compare(other), 0)

def greaterThanOrEqual(other):
    return jsGtEq(compare(other), 0)

def getLowBitsUnsigned():
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_698dd40c

def _get_TWO_PWR_32_DBL__():
    return TWO_PWR_32_DBL_

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_5fd40d2e = 0
def _get_TWO_PWR_63_DBL__():
    return TWO_PWR_63_DBL_

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_2463a9ec = 0
def imul(a_local, b_local):
    lhs = jsMult(kotlin_Double(jsBitwiseAnd(a_local, js('0xffff0000'))), kotlin_Double(jsBitwiseAnd(b_local, 65535)))
    rhs = jsMult(kotlin_Double(jsBitwiseAnd(a_local, 65535)), kotlin_Double(b_local))
    return jsBitwiseOr(jsPlus(lhs, rhs), 0)

def withType(type, array):
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_700735e2
    return array

def arrayConcat(args):
    len = jsArrayLength(args)
    tmp0_unsafeCast_0 = js('Array(len)')
    typed = kotlin_Any_(tmp0_unsafeCast_0)
    inductionVariable = 0
    last = jsBitOr(jsMinus(len, 1), 0)
    if jsLtEq(inductionVariable, last):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_6e42970a
    
    return T(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_38c6f088)

def primitiveArrayConcat(args):
    size_local = 0
    inductionVariable = 0
    last = jsBitOr(jsMinus(jsArrayLength(args), 1), 0)
    if jsLtEq(inductionVariable, last):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_60a38548
    
    a = jsArrayGet(args, 0)
    tmp1_unsafeCast_0 = js('new a.constructor(size_local)')
    result = kotlin_Any_(tmp1_unsafeCast_0)
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_1f3bd40a:
        tmp2_withType_0 = kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicMemberExpressionImpl_4e42beba)
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_28f9873c
    
    if True:
        pass
    
    size_local = 0
    inductionVariable = 0
    last = jsBitOr(jsMinus(jsArrayLength(args), 1), 0)
    if jsLtEq(inductionVariable, last):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_16ce05de
    
    return kotlin_Any_(result)

def taggedArrayCopy(array):
    res = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_7adde112
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_12cb9eda
    return kotlin_Any_(res)

def numberToByte(a):
    return toByte(numberToInt(a))

def toByte(a):
    tmp0_unsafeCast_0 = js('a << 24 >> 24')
    return kotlin_Any_(tmp0_unsafeCast_0)

def numberToInt(a):
    tmp
    if jsInstanceOf(a, jsClass()):
        tmp = kotlin_Long(a).toInt()
    
    if True:
        if True:
            tmp = doubleToInt(kotlin_Double(a))
        
    
    return tmp

def doubleToInt(a):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_36ed075b

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
    return Char(jsBitAnd(numberToInt(a), 65535))

def toLong(a):
    return fromInt(kotlin_Int(a))

def numberRangeToNumber(start, endInclusive):
    return IntRange(kotlin_Int(start), kotlin_Int(endInclusive))

def numberRangeToLong(start, endInclusive):
    return LongRange(numberToLong(start), kotlin_Long(endInclusive))

def _get_propertyRefClassMetadataCache_():
    return propertyRefClassMetadataCache

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_56059cf1 = 0
def metadataObject():
    return js('{ kind: \'class\', interfaces: [] }')

def getPropertyCallableRef(name, paramCount, type, getter, setter):
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_1b5496fd
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_56b972a8
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_16db70a0
    tmp0_unsafeCast_0 = getPropertyRefClass(getter, getKPropMetadata(paramCount, setter, type))
    return kotlin_Any_(tmp0_unsafeCast_0)

def getPropertyRefClass(obj, metadata):
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_64bf60c7
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_150f3678
    return obj

def getKPropMetadata(paramCount, setter, type):
    mdata = jsArrayGet(jsArrayGet(propertyRefClassMetadataCache, paramCount), visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_562c6d5c)
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_700e3b73:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_7a2c95e2
    
    return mdata

def getLocalDelegateReference(name, type, mutable, _lambda):
    return getPropertyCallableRef(name, 0, type, _lambda, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_720574a4)

def propertyRefClassMetadataCache_init_():
    tmp = js('{ kind: \'class\', interfaces: [] }')
    tmp0_arrayOf_0 = arrayLiteral(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_2348e36)
    tmp = kotlin_Any_(tmp0_arrayOf_0)
    tmp = js('{ kind: \'class\', interfaces: [] }')
    tmp1_arrayOf_0 = arrayLiteral(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_134d8f2b)
    tmp = kotlin_Any_(tmp1_arrayOf_0)
    tmp = js('{ kind: \'class\', interfaces: [] }')
    tmp2_arrayOf_0 = arrayLiteral(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_698ba673)
    tmp3_arrayOf_0 = arrayLiteral(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_6f8fe7e8)
    return kotlin_Any_(tmp3_arrayOf_0)

def isArrayish(o):
    tmp
    if isJsArray(kotlin_Any(o)):
        tmp = True
    
    if True:
        tmp0_unsafeCast_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_24cb530d
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
    
    return tmp

def isJsArray(obj):
    tmp0_unsafeCast_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_3c6c7782
    return kotlin_Any_(tmp0_unsafeCast_0)

def isInterface(obj, iface):
    tmp0_elvis_lhs = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicMemberExpressionImpl_749aa36f
    tmp
    if jsEqeq(tmp0_elvis_lhs, None):
        return False
    
    if True:
        tmp = tmp0_elvis_lhs
    
    ctor = tmp
    return isInterfaceImpl(kotlin_js_Ctor(ctor), iface)

def isInterfaceImpl(ctor, iface):
    if jsEqeqeq(ctor, iface):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_295692fd
    
    metadata = ctor._get__metadata__()
    if jsNot(jsEqeq(metadata, None)):
        interfaces = metadata._get_interfaces_()
        indexedObject = interfaces
        inductionVariable = 0
        last = jsArrayLength(indexedObject)
        while jsLt(inductionVariable, last):
            i = jsArrayGet(indexedObject, inductionVariable)
            inductionVariable = jsBitOr(jsPlus(inductionVariable, 1), 0)
            if isInterfaceImpl(i, iface):
                return True
            
        
    
    superPrototype = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2d583f20
    superConstructor = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_15210484
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_76a89ffa

def isArray(obj):
    tmp
    if isJsArray(obj):
        tmp = kotlin_Boolean(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_17746fcb)
    
    if True:
        tmp = False
    
    return tmp

def isObject(obj):
    objTypeOf = jsTypeOf(obj)
    tmp0_subject = objTypeOf
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_33032086

def isSuspendFunction(obj, arity):
    if jsEqeqeq(jsTypeOf(obj), 'function'):
        tmp0_unsafeCast_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicMemberExpressionImpl_508b9c16
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
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_451dfee3

def isCharSequence(value):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3ec05c9b

def isBooleanArray(a):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_a3f7621

def isByteArray(a):
    return jsInstanceOf(a, js('Int8Array'))

def isShortArray(a):
    return jsInstanceOf(a, js('Int16Array'))

def isCharArray(a):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_641ff891

def isIntArray(a):
    return jsInstanceOf(a, js('Int32Array'))

def isFloatArray(a):
    return jsInstanceOf(a, js('Float32Array'))

def isLongArray(a):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_316eb9b8

def isDoubleArray(a):
    return jsInstanceOf(a, js('Float64Array'))

def jsIsType(obj, jsClass):
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_7772549d:
        return isObject(obj)
    
    if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_7646c16:
        return False
    
    if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_51a6748f:
        return True
    
    proto = jsGetPrototypeOf(jsClass)
    tmp0_safe_receiver = proto
    constructor = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6b5af92
    if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_66a7e65:
        metadata = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicMemberExpressionImpl_21b298de
        if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_42b2a977:
            return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_6fec6b75
        
    
    klassMetadata = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicMemberExpressionImpl_293918f9
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_7d968ec1:
        return jsInstanceOf(obj, jsClass)
    
    if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4821b5f9:
        return isInterfaceImpl(kotlin_js_Ctor(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicMemberExpressionImpl_2907f58d), jsClass)
    
    return False

def jsGetPrototypeOf(jsClass):
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_79a81557

def asList():
    return ArrayList(kotlin_Any_(_this_))

def plus(elements):
    return kotlin_Array_T_(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_6263089d)

def copyOfRange(fromIndex, toIndex):
    Companion_getInstance().checkRangeIndexes(fromIndex, toIndex, jsArrayLength(_this_))
    return kotlin_Array_T_(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_4041b733)

def minOf(a, b):
    return visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl_5b0b7fd7.min(int32ArrayOf(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_3b342b4d))

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
    if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_b889306:
        ensureNotNull(_this._get_context_().get(Key_getInstance())).releaseInterceptedContinuation(intercepted)
    
    _this.intercepted_ = CompletedContinuation_getInstance()

class CoroutineImpl:
    def _init_(resultContinuation):
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_3e706fc2
        _this_.resultContinuation = resultContinuation
        _this_.state = 0
        _this_.exceptionState = 0
        _this_.result = None
        _this_.exception = None
        _this_.finallyPath = None
        tmp = _this_
        tmp0_safe_receiver = resultContinuation
        tmp._context = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2aaa4574
        _this_.intercepted_ = None
    
    def _set_state_(self, _set___):
        _this_.state = _set___
    
    def _get_state_(self):
        return state
    
    def _set_exceptionState_(self, _set___):
        _this_.exceptionState = _set___
    
    def _get_exceptionState_(self):
        return exceptionState
    
    def _set_result_(self, _set___):
        _this_.result = _set___
    
    def _get_result_(self):
        return result
    
    def _set_exception_(self, _set___):
        _this_.exception = _set___
    
    def _get_exception_(self):
        return exception
    
    def _set_finallyPath_(self, _set___):
        _this_.finallyPath = _set___
    
    def _get_finallyPath_(self):
        return finallyPath
    
    def _get_context_(self):
        return ensureNotNull(_context)
    
    def intercepted(self):
        tmp2_elvis_lhs = intercepted_
        tmp
        if jsEqeq(tmp2_elvis_lhs, None):
            tmp0_safe_receiver = _this_._get_context_().get(Key_getInstance())
            tmp1_elvis_lhs = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2de55285
            tmp0_also_0 = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_498bcd33
            _this_.intercepted_ = tmp0_also_0
            tmp = tmp0_also_0
        
        if True:
            tmp = tmp2_elvis_lhs
        
        return tmp
    
    def resumeWith(self, result):
        current = _this_
        tmp
        if _Result___get_isFailure__impl_(result):
            tmp = None
        
        if True:
            tmp = _Result___get_value__impl_(result)
            tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_33aa4a3a
        
        currentResult = tmp
        currentException = Result__exceptionOrNull_impl(result)
        while True:
            tmp0_with_0 = current
            if jsEqeq(currentException, None):
                tmp0_with_0.result = currentResult
            
            if True:
                tmp0_with_0.state = exceptionState
                tmp0_with_0.exception = currentException
            
            visitTry_org_jetbrains_kotlin_ir_expressions_impl_IrTryImpl_25c7c446
            releaseIntercepted(tmp0_with_0)
            completion_4 = ensureNotNull(resultContinuation)
            if jsInstanceOf(completion_4, jsClass()):
                current = kotlin_coroutines_CoroutineImpl(completion_4)
            
            if True:
                if True:
                    if jsNot(jsEqeq(currentException, None)):
                        tmp0_resumeWithException_0_5 = ensureNotNull(currentException)
                        tmp0_failure_0_1_6 = Companion_getInstance()
                        completion_4.resumeWith(Result(createFailure(tmp0_resumeWithException_0_5)))
                    
                    if True:
                        tmp1_resume_0_7 = currentResult
                        tmp0_success_0_1_8 = Companion_getInstance()
                        completion_4.resumeWith(Result(tmp1_resume_0_7))
                    
                    return Unit_getInstance()
                
            
        
    
    def resumeWith(self, result):
        return _this_.resumeWith(result)
    
    def doResume(self):
        pass
    
    def create(self, completion):
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_156b3428
    
    def create(self, value, completion):
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_7e3cea61
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class CompletedContinuation:
    def _init_():
        CompletedContinuation_instance = _this_
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_4f2e6db7
    
    def _get_context_(self):
        tmp0_error_0 = 'This continuation is already complete'
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_42ad9160
    
    def resumeWith(self, result):
        tmp0_error_0 = 'This continuation is already complete'
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_64a17bcc
    
    def resumeWith(self, result):
        return _this_.resumeWith(result)
    
    def toString(self):
        return 'This continuation is already complete'
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_45f4a0ee = 0
def CompletedContinuation_getInstance():
    if jsEqeq(CompletedContinuation_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_e7906af
    
    return CompletedContinuation_instance

def Exception_init__Init_(_this):
    extendThrowable(_this, _undefined(), _undefined())
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_703c6519
    return _this

def Exception_init__Create_():
    tmp = Exception_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_428ebfde)
    return tmp

def Exception_init__Init_(message, _this):
    extendThrowable(_this, message, _undefined())
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_6d7b4edf
    return _this

def Exception_init__Create_(message):
    tmp = Exception_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_2993c168)
    return tmp

def Exception_init__Init_(message, cause, _this):
    extendThrowable(_this, message, cause)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_1af83b4b
    return _this

def Exception_init__Create_(message, cause):
    tmp = Exception_init__Init_(message, cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_168dc9c3)
    return tmp

def Exception_init__Init_(cause, _this):
    extendThrowable(_this, _undefined(), cause)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_2e4e175
    return _this

def Exception_init__Create_(cause):
    tmp = Exception_init__Init_(cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_698e4e6c)
    return tmp

class Exception:
    def _get_message_(self):
        pass
    
    def _get_cause_(self):
        pass
    
    def toString(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def _init_():
        captureStack(_this_, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_78a47ca8)
    

def Error_init__Init_(_this):
    extendThrowable(_this, _undefined(), _undefined())
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_1d4c39c2
    return _this

def Error_init__Create_():
    tmp = Error_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_2b2415a7)
    return tmp

def Error_init__Init_(message, _this):
    extendThrowable(_this, message, _undefined())
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_26bddc84
    return _this

def Error_init__Create_(message):
    tmp = Error_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_151b7c03)
    return tmp

def Error_init__Init_(message, cause, _this):
    extendThrowable(_this, message, cause)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_5387e079
    return _this

def Error_init__Create_(message, cause):
    tmp = Error_init__Init_(message, cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_5fe11c40)
    return tmp

def Error_init__Init_(cause, _this):
    extendThrowable(_this, _undefined(), cause)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_55f00c43
    return _this

def Error_init__Create_(cause):
    tmp = Error_init__Init_(cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_334e5403)
    return tmp

class Error:
    def _get_message_(self):
        pass
    
    def _get_cause_(self):
        pass
    
    def toString(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def _init_():
        captureStack(_this_, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_b022ec3)
    

def IllegalArgumentException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_747f6990
    return _this

def IllegalArgumentException_init__Create_():
    tmp = IllegalArgumentException_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_30df4a72)
    return tmp

def IllegalArgumentException_init__Init_(message, _this):
    RuntimeException_init__Init_(message, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_72ddbe12
    return _this

def IllegalArgumentException_init__Create_(message):
    tmp = IllegalArgumentException_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_27f546)
    return tmp

def IllegalArgumentException_init__Init_(message, cause, _this):
    RuntimeException_init__Init_(message, cause, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_222303b9
    return _this

def IllegalArgumentException_init__Create_(message, cause):
    tmp = IllegalArgumentException_init__Init_(message, cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_6c7114db)
    return tmp

def IllegalArgumentException_init__Init_(cause, _this):
    RuntimeException_init__Init_(cause, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_4388206e
    return _this

def IllegalArgumentException_init__Create_(cause):
    tmp = IllegalArgumentException_init__Init_(cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_4e3db1c6)
    return tmp

class IllegalArgumentException:
    def _get_message_(self):
        pass
    
    def _get_cause_(self):
        pass
    
    def toString(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def _init_():
        captureStack(_this_, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_2c33bc4)
    

def RuntimeException_init__Init_(_this):
    Exception_init__Init_(_this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_672bc69a
    return _this

def RuntimeException_init__Create_():
    tmp = RuntimeException_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_786d9f87)
    return tmp

def RuntimeException_init__Init_(message, _this):
    Exception_init__Init_(message, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_2e3991bd
    return _this

def RuntimeException_init__Create_(message):
    tmp = RuntimeException_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_414331e4)
    return tmp

def RuntimeException_init__Init_(message, cause, _this):
    Exception_init__Init_(message, cause, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_60f9d3e1
    return _this

def RuntimeException_init__Create_(message, cause):
    tmp = RuntimeException_init__Init_(message, cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_71e67dd6)
    return tmp

def RuntimeException_init__Init_(cause, _this):
    Exception_init__Init_(cause, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_6b2ac950
    return _this

def RuntimeException_init__Create_(cause):
    tmp = RuntimeException_init__Init_(cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_7fa817ba)
    return tmp

class RuntimeException:
    def _get_message_(self):
        pass
    
    def _get_cause_(self):
        pass
    
    def toString(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def _init_():
        captureStack(_this_, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_7b66c7e9)
    

def NoSuchElementException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_3472f880
    return _this

def NoSuchElementException_init__Create_():
    tmp = NoSuchElementException_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_7588d46f)
    return tmp

def NoSuchElementException_init__Init_(message, _this):
    RuntimeException_init__Init_(message, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_226451a2
    return _this

def NoSuchElementException_init__Create_(message):
    tmp = NoSuchElementException_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_649e1f4c)
    return tmp

class NoSuchElementException:
    def _get_message_(self):
        pass
    
    def _get_cause_(self):
        pass
    
    def toString(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def _init_():
        captureStack(_this_, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_52c2906e)
    

def IllegalStateException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_6c20dae4
    return _this

def IllegalStateException_init__Create_():
    tmp = IllegalStateException_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_b7694aa)
    return tmp

def IllegalStateException_init__Init_(message, _this):
    RuntimeException_init__Init_(message, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_7cba7745
    return _this

def IllegalStateException_init__Create_(message):
    tmp = IllegalStateException_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_3ca962eb)
    return tmp

def IllegalStateException_init__Init_(message, cause, _this):
    RuntimeException_init__Init_(message, cause, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_2a6a0343
    return _this

def IllegalStateException_init__Create_(message, cause):
    tmp = IllegalStateException_init__Init_(message, cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_70c969a7)
    return tmp

def IllegalStateException_init__Init_(cause, _this):
    RuntimeException_init__Init_(cause, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_18495d2c
    return _this

def IllegalStateException_init__Create_(cause):
    tmp = IllegalStateException_init__Init_(cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_888925d)
    return tmp

class IllegalStateException:
    def _get_message_(self):
        pass
    
    def _get_cause_(self):
        pass
    
    def toString(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def _init_():
        captureStack(_this_, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_37fec49c)
    

def IndexOutOfBoundsException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_2ed33e81
    return _this

def IndexOutOfBoundsException_init__Create_():
    tmp = IndexOutOfBoundsException_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_777f58c3)
    return tmp

def IndexOutOfBoundsException_init__Init_(message, _this):
    RuntimeException_init__Init_(message, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_46a2f032
    return _this

def IndexOutOfBoundsException_init__Create_(message):
    tmp = IndexOutOfBoundsException_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_d78dd7f)
    return tmp

class IndexOutOfBoundsException:
    def _get_message_(self):
        pass
    
    def _get_cause_(self):
        pass
    
    def toString(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def _init_():
        captureStack(_this_, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_6acb0d0d)
    

def UnsupportedOperationException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_5d2ded
    return _this

def UnsupportedOperationException_init__Create_():
    tmp = UnsupportedOperationException_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_9f36eeb)
    return tmp

def UnsupportedOperationException_init__Init_(message, _this):
    RuntimeException_init__Init_(message, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_39794db6
    return _this

def UnsupportedOperationException_init__Create_(message):
    tmp = UnsupportedOperationException_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_5d9d1953)
    return tmp

def UnsupportedOperationException_init__Init_(message, cause, _this):
    RuntimeException_init__Init_(message, cause, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_67c9d537
    return _this

def UnsupportedOperationException_init__Create_(message, cause):
    tmp = UnsupportedOperationException_init__Init_(message, cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_39487f70)
    return tmp

def UnsupportedOperationException_init__Init_(cause, _this):
    RuntimeException_init__Init_(cause, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_6ea248fd
    return _this

def UnsupportedOperationException_init__Create_(cause):
    tmp = UnsupportedOperationException_init__Init_(cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_17675c2f)
    return tmp

class UnsupportedOperationException:
    def _get_message_(self):
        pass
    
    def _get_cause_(self):
        pass
    
    def toString(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def _init_():
        captureStack(_this_, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_169f4020)
    

def NullPointerException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_70c81870
    return _this

def NullPointerException_init__Create_():
    tmp = NullPointerException_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_5204a284)
    return tmp

def NullPointerException_init__Init_(message, _this):
    RuntimeException_init__Init_(message, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_26f44b4a
    return _this

def NullPointerException_init__Create_(message):
    tmp = NullPointerException_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_4f7e0ea7)
    return tmp

class NullPointerException:
    def _get_message_(self):
        pass
    
    def _get_cause_(self):
        pass
    
    def toString(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def _init_():
        captureStack(_this_, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_92b6b6f)
    

def NoWhenBranchMatchedException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_42306a87
    return _this

def NoWhenBranchMatchedException_init__Create_():
    tmp = NoWhenBranchMatchedException_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_41acbb51)
    return tmp

def NoWhenBranchMatchedException_init__Init_(message, _this):
    RuntimeException_init__Init_(message, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_69d58b75
    return _this

def NoWhenBranchMatchedException_init__Create_(message):
    tmp = NoWhenBranchMatchedException_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_20286a6b)
    return tmp

def NoWhenBranchMatchedException_init__Init_(message, cause, _this):
    RuntimeException_init__Init_(message, cause, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_2b648329
    return _this

def NoWhenBranchMatchedException_init__Create_(message, cause):
    tmp = NoWhenBranchMatchedException_init__Init_(message, cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_3c9e7377)
    return tmp

def NoWhenBranchMatchedException_init__Init_(cause, _this):
    RuntimeException_init__Init_(cause, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_5244b461
    return _this

def NoWhenBranchMatchedException_init__Create_(cause):
    tmp = NoWhenBranchMatchedException_init__Init_(cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_5aff837f)
    return tmp

class NoWhenBranchMatchedException:
    def _get_message_(self):
        pass
    
    def _get_cause_(self):
        pass
    
    def toString(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def _init_():
        captureStack(_this_, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_10c4eb9a)
    

def ClassCastException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_54a0f09d
    return _this

def ClassCastException_init__Create_():
    tmp = ClassCastException_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_53162e9c)
    return tmp

def ClassCastException_init__Init_(message, _this):
    RuntimeException_init__Init_(message, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_2749980a
    return _this

def ClassCastException_init__Create_(message):
    tmp = ClassCastException_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_50829172)
    return tmp

class ClassCastException:
    def _get_message_(self):
        pass
    
    def _get_cause_(self):
        pass
    
    def toString(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def _init_():
        captureStack(_this_, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_5c273b3e)
    

def UninitializedPropertyAccessException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_d9d2c3e
    return _this

def UninitializedPropertyAccessException_init__Create_():
    tmp = UninitializedPropertyAccessException_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_b28fd1)
    return tmp

def UninitializedPropertyAccessException_init__Init_(message, _this):
    RuntimeException_init__Init_(message, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_626a4cfa
    return _this

def UninitializedPropertyAccessException_init__Create_(message):
    tmp = UninitializedPropertyAccessException_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_2d6ddf48)
    return tmp

def UninitializedPropertyAccessException_init__Init_(message, cause, _this):
    RuntimeException_init__Init_(message, cause, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_7c4dd006
    return _this

def UninitializedPropertyAccessException_init__Create_(message, cause):
    tmp = UninitializedPropertyAccessException_init__Init_(message, cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_56598806)
    return tmp

def UninitializedPropertyAccessException_init__Init_(cause, _this):
    RuntimeException_init__Init_(cause, _this)
    visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_4e80e1b5
    return _this

def UninitializedPropertyAccessException_init__Create_(cause):
    tmp = UninitializedPropertyAccessException_init__Init_(cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_71a7ce25)
    return tmp

class UninitializedPropertyAccessException:
    def _get_message_(self):
        pass
    
    def _get_cause_(self):
        pass
    
    def toString(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def _init_():
        captureStack(_this_, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_252d7bcf)
    

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
    fruits = listOf(arrayLiteral(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_3f832bd))
    tmp0_iterator = fruits.iterator()
    while tmp0_iterator.hasNext():
        x = tmp0_iterator.next()
        println(x)
    

class TestClass:
    def _init_():
        visitDelegatingCOnstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_3c74aa0d
    
    def getSomeString(self):
        return 'Hello from Kotlin class!'
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def returnString():
    return 'Hello from Kotlin!'

def returnStringFromClass():
    testClass = TestClass()
    return testClass.getSomeString()
