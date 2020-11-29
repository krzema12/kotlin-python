def fold(initial, operation):
    accumulator = initial
    indexedObject = self
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
        last = jsBitOr(jsMinus(jsArrayLength(self), 1), 0)
        if jsLtEq(inductionVariable, last):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_5c2463d8
        
    
    if True:
        inductionVariable = 0
        last = jsBitOr(jsMinus(jsArrayLength(self), 1), 0)
        if jsLtEq(inductionVariable, last):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_59c4921f
        
    
    return -1

def lastIndexOf(element):
    if jsEqeq(element, None):
        inductionVariable = jsBitOr(jsMinus(jsArrayLength(self), 1), 0)
        if jsLtEq(0, inductionVariable):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_477ac359
        
    
    if True:
        inductionVariable = jsBitOr(jsMinus(jsArrayLength(self), 1), 0)
        if jsLtEq(0, inductionVariable):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_63888c14
        
    
    return -1

def _get_lastIndex_():
    return jsBitOr(jsMinus(jsArrayLength(self), 1), 0)

def joinToString(separator, prefix, postfix, limit, truncated, transform):
    return joinTo(StringBuilder_init__Create_(), separator, prefix, postfix, limit, truncated, transform).toString()

def joinToString_default(separator, prefix, postfix, limit, truncated, transform, _mask0, _handler):
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 1), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_654b9f0
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 2), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_4b3642c4
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 4), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_78679286
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 8), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_18b0bbc3
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 16), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_3e4162ee
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 32), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_3186b07d
    
    return joinToString(kotlin_CharSequence(separator), kotlin_CharSequence(prefix), kotlin_CharSequence(postfix), limit, kotlin_CharSequence(truncated), transform)

def joinTo(buffer, separator, prefix, postfix, limit, truncated, transform):
    buffer.append(prefix)
    Unit_getInstance()
    count = 0
    indexedObject = self
    inductionVariable = 0
    last = jsArrayLength(indexedObject)
    while jsLt(inductionVariable, last):
        element = jsArrayGet(indexedObject, inductionVariable)
        inductionVariable = jsBitOr(jsPlus(inductionVariable, 1), 0)
        count = jsBitOr(jsPlus(count, 1), 0)
        if jsGt(count, 1):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_34ceabf1
        
        if True:
            pass
        
        if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_482f59f4:
            appendElement(element, transform)
        
        if True:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrBreakImpl_6a562255
        
    
    if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6dbdfa38:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_5b0d8236
    
    buffer.append(postfix)
    Unit_getInstance()
    return buffer

def joinTo_default(buffer, separator, prefix, postfix, limit, truncated, transform, _mask0, _handler):
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 2), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_563b9462
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 4), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_42ef0b7c
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 8), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_4f7c5402
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 16), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_46808854
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 32), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_13666880
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 64), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_25428bab
    
    return joinTo(buffer, kotlin_CharSequence(separator), kotlin_CharSequence(prefix), kotlin_CharSequence(postfix), limit, kotlin_CharSequence(truncated), transform)

def contains(element):
    return jsGtEq(indexOf(element), 0)

def indexOf(element):
    inductionVariable = 0
    last = jsBitOr(jsMinus(jsArrayLength(self), 1), 0)
    if jsLtEq(inductionVariable, last):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_58e48d9
    
    return -1

def _get_indices_():
    return IntRange(0, _get_lastIndex_())

def _get_lastIndex_():
    return jsBitOr(jsMinus(jsArrayLength(self), 1), 0)

def contains(element):
    return jsGtEq(indexOf(element), 0)

def indexOf(element):
    inductionVariable = 0
    last = jsBitOr(jsMinus(jsArrayLength(self), 1), 0)
    if jsLtEq(inductionVariable, last):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_26f6fbbd
    
    return -1

def _get_indices_():
    return IntRange(0, _get_lastIndex_())

def _get_lastIndex_():
    return jsBitOr(jsMinus(jsArrayLength(self), 1), 0)

def contains(element):
    return jsGtEq(indexOf(element), 0)

def indexOf(element):
    inductionVariable = 0
    last = jsBitOr(jsMinus(jsArrayLength(self), 1), 0)
    if jsLtEq(inductionVariable, last):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_3dd916d9
    
    return -1

def _get_indices_():
    return IntRange(0, _get_lastIndex_())

def _get_lastIndex_():
    return jsBitOr(jsMinus(jsArrayLength(self), 1), 0)

def contains(element):
    return jsGtEq(indexOf(element), 0)

def indexOf(element):
    inductionVariable = 0
    last = jsBitOr(jsMinus(jsArrayLength(self), 1), 0)
    if jsLtEq(inductionVariable, last):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_69894182
    
    return -1

def _get_indices_():
    return IntRange(0, _get_lastIndex_())

def _get_lastIndex_():
    return jsBitOr(jsMinus(jsArrayLength(self), 1), 0)

def indexOfFirst(predicate):
    index = 0
    tmp0_iterator = self.iterator()
    while tmp0_iterator.hasNext():
        item = tmp0_iterator.next()
        if predicate.invoke(item):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_66fd7b2
        
        tmp1 = index
        index = jsBitOr(jsPlus(tmp1, 1), 0)
        Unit_getInstance()
    
    return -1

def indexOfLast(predicate):
    iterator = self.listIterator(self._get_size_())
    while iterator.hasPrevious():
        if predicate.invoke(iterator.previous()):
            return iterator.nextIndex()
        
    
    return -1

def any(predicate):
    tmp
    if isInterface(self, jsClass()):
        tmp = kotlin_collections_Collection_T_(self).isEmpty()
    
    if True:
        if True:
            tmp = False
        
    
    if tmp:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_234a8c1f
    
    if True:
        pass
    
    tmp0_iterator = self.iterator()
    while tmp0_iterator.hasNext():
        element = tmp0_iterator.next()
        if predicate.invoke(element):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_79f6e671
        
    
    return False

def all(predicate):
    tmp
    if isInterface(self, jsClass()):
        tmp = kotlin_collections_Collection_T_(self).isEmpty()
    
    if True:
        if True:
            tmp = False
        
    
    if tmp:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_2c3f9229
    
    if True:
        pass
    
    tmp0_iterator = self.iterator()
    while tmp0_iterator.hasNext():
        element = tmp0_iterator.next()
        if jsNot(predicate.invoke(element)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_2b360641
        
    
    return True

def joinToString(separator, prefix, postfix, limit, truncated, transform):
    return joinTo(StringBuilder_init__Create_(), separator, prefix, postfix, limit, truncated, transform).toString()

def joinToString_default(separator, prefix, postfix, limit, truncated, transform, _mask0, _handler):
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 1), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_72b1ee4b
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 2), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_2dbc56fb
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 4), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_37aae870
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 8), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_2876584f
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 16), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_1d0305fb
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 32), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_2d6dbcec
    
    return joinToString(kotlin_CharSequence(separator), kotlin_CharSequence(prefix), kotlin_CharSequence(postfix), limit, kotlin_CharSequence(truncated), transform)

def joinTo(buffer, separator, prefix, postfix, limit, truncated, transform):
    buffer.append(prefix)
    Unit_getInstance()
    count = 0
    tmp0_iterator = self.iterator()
    while tmp0_iterator.hasNext():
        element = tmp0_iterator.next()
        count = jsBitOr(jsPlus(count, 1), 0)
        if jsGt(count, 1):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_431ac922
        
        if True:
            pass
        
        if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_62ce5261:
            appendElement(element, transform)
        
        if True:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrBreakImpl_1e4d93f7
        
    
    if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_287e35df:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_352e8cb3
    
    buffer.append(postfix)
    Unit_getInstance()
    return buffer

def joinTo_default(buffer, separator, prefix, postfix, limit, truncated, transform, _mask0, _handler):
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 2), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_64a96593
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 4), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_3e5080ce
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 8), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_785d194d
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 16), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_16bee5fe
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 32), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_5973e4ec
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 64), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_1d9ad64f
    
    return joinTo(buffer, kotlin_CharSequence(separator), kotlin_CharSequence(prefix), kotlin_CharSequence(postfix), limit, kotlin_CharSequence(truncated), transform)

def downTo(to):
    return Companion_getInstance().fromClosedRange(self, to, -1)

def until(to):
    if jsLtEq(to, IntCompanionObject_getInstance().MIN_VALUE):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_3c1df0e9
    
    return numberRangeToNumber(self, kotlin_Int(jsBitOr(jsMinus(to, 1), 0)))

def reversed():
    return Companion_getInstance().fromClosedRange(self.last, self.first, jsBitOr(jsUnaryMinus(self.step), 0))

def getOrElse(index, defaultValue):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_36eff8df

def KotlinNothingValueException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_4a5939cb
    return _this

def KotlinNothingValueException_init__Create_():
    tmp = KotlinNothingValueException_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_10e25b2a)
    return tmp

def KotlinNothingValueException_init__Init_(message, _this):
    RuntimeException_init__Init_(message, _this)
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_249334b9
    return _this

def KotlinNothingValueException_init__Create_(message):
    tmp = KotlinNothingValueException_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_3cc8f1c)
    return tmp

def KotlinNothingValueException_init__Init_(message, cause, _this):
    RuntimeException_init__Init_(message, cause, _this)
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_1e31cf9b
    return _this

def KotlinNothingValueException_init__Create_(message, cause):
    tmp = KotlinNothingValueException_init__Init_(message, cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_143f4d52)
    return tmp

def KotlinNothingValueException_init__Init_(cause, _this):
    RuntimeException_init__Init_(cause, _this)
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_3a4af228
    return _this

def KotlinNothingValueException_init__Create_(cause):
    tmp = KotlinNothingValueException_init__Init_(cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_13b85e31)
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
    
    def __init__(self):
        captureStack(self, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_176ba277)
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_3fcb6c7b = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_63ed5580 = 0
def values():
    return arrayLiteral(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_1fbe8592)

def valueOf(value):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_e9b227f

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_24f89b6b = 0
def Level_initEntries():
    if Level_entriesInitialized:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_22be8211
    
    Level_entriesInitialized = True
    Level_WARNING_instance = Level('WARNING', 0)
    Level_ERROR_instance = Level('ERROR', 1)

def Experimental_init__Init_(level, _mask0, _marker, _this):
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 1), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_6a670dcc
    
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_4cfc4eb2
    return _this

def Experimental_init__Create_(level, _mask0, _marker):
    return Experimental_init__Init_(level, _mask0, _marker, Object_create())

class Level:
    def __init__(self, name, ordinal):
        visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_3b5cf4c6
    
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
    def __init__(self, level):
        self.level = level
    
    def _get_level_(self):
        return self.level
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class WasExperimental:
    def __init__(self, markerClass):
        self.markerClass = markerClass
    
    def _get_markerClass_(self):
        return self.markerClass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class ExperimentalStdlibApi:
    def __init__(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class OptionalExpectation:
    def __init__(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class ExperimentalMultiplatform:
    def __init__(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_67988d92 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_286bd902 = 0
def values():
    return arrayLiteral(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_ef10390)

def valueOf(value):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_59a9769e

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_78bbc584 = 0
def Level_initEntries():
    if Level_entriesInitialized:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_43f88cba
    
    Level_entriesInitialized = True
    Level_WARNING_instance = Level('WARNING', 0)
    Level_ERROR_instance = Level('ERROR', 1)

def RequiresOptIn_init__Init_(message, level, _mask0, _marker, _this):
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 1), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_5a77b7cc
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 2), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_1201d134
    
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_3178f903
    return _this

def RequiresOptIn_init__Create_(message, level, _mask0, _marker):
    return RequiresOptIn_init__Init_(message, level, _mask0, _marker, Object_create())

class Level:
    def __init__(self, name, ordinal):
        visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_2ddc5c07
    
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
    def __init__(self, message, level):
        self.message = message
        self.level = level
    
    def _get_message_(self):
        return self.message
    
    def _get_level_(self):
        return self.level
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class OptIn:
    def __init__(self, markerClass):
        self.markerClass = markerClass
    
    def _get_markerClass_(self):
        return self.markerClass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class _no_name_provided_:
    def __init__(self, this_0):
        self.this_0 = this_0
    
    def invoke(self, it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_78cbb140
    
    def invoke(self, p1):
        return self.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2111c3cc)
    

class AbstractCollection:
    def __init__(self):
        pass
    
    def _get_size_(self):
        pass
    
    def iterator(self):
        pass
    
    def contains(self, element):
        tmp_ret_0
        visitDoWhileLoop_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_3072b38f
        return tmp_ret_0
    
    def containsAll(self, elements):
        tmp_ret_0
        visitDoWhileLoop_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_61c3b31c
        return tmp_ret_0
    
    def isEmpty(self):
        return jsEqeqeq(self._get_size_(), 0)
    
    def toString(self):
        return joinToString_default(', ', '[', ']', 0, None, _no_name_provided__factory(self), 24, None)
    
    def toArray(self):
        return copyToArrayImpl(self)
    
    def toArray(self, array):
        return copyToArrayImpl(self, array)
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    

def _no_name_provided__factory(this_0):
    i = _no_name_provided_(this_0)
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_666e1965

def _get_list_(_this):
    return _this.list

def _get_fromIndex_(_this):
    return _this.fromIndex

def _set__size_(_this, _set___):
    _this._size = _set___

def _get__size_(_this):
    return _this._size

class SubList:
    def __init__(self, list, fromIndex, toIndex):
        visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_5f877009
        self.list = list
        self.fromIndex = fromIndex
        self._size = 0
        Companion_getInstance().checkRangeIndexes(self.fromIndex, toIndex, self.list._get_size_())
        self._size = jsBitOr(jsMinus(toIndex, self.fromIndex), 0)
    
    def get(self, index):
        Companion_getInstance().checkElementIndex(index, self._size)
        return self.list.get(jsBitOr(jsPlus(self.fromIndex, index), 0))
    
    def _get_size_(self):
        return self._size
    
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
    def __init__(self, _outer):
        self._this = _outer
        self.index = 0
    
    def _set_index_(self, _set___):
        self.index = _set___
    
    def _get_index_(self):
        return self.index
    
    def hasNext(self):
        return jsLt(self.index, self._this._get_size_())
    
    def next(self):
        if jsNot(self.hasNext()):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_542754be
        
        tmp0_this = self
        tmp1 = tmp0_this.index
        tmp0_this.index = jsBitOr(jsPlus(tmp1, 1), 0)
        return self._this.get(tmp1)
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class ListIteratorImpl:
    def __init__(self, _outer, index):
        self._this = _outer
        visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_403e8b5
        Companion_getInstance().checkPositionIndex(index, self._this._get_size_())
        self._set_index_(index)
    
    def hasPrevious(self):
        return jsGt(self._get_index_(), 0)
    
    def nextIndex(self):
        return self._get_index_()
    
    def previous(self):
        if jsNot(self.hasPrevious()):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_2d114d27
        
        tmp0_this = self
        tmp0_this._set_index_(jsBitOr(jsMinus(tmp0_this._get_index_(), 1), 0))
        return self._this.get(tmp0_this._get_index_())
    
    def previousIndex(self):
        return jsBitOr(jsMinus(self._get_index_(), 1), 0)
    
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
    def __init__(self):
        Companion_instance = self
    
    def checkElementIndex(self, index, size):
        if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_62c95d73:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_608c2042
        
    
    def checkPositionIndex(self, index, size):
        if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6ad57ee3:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_237c8718
        
    
    def checkRangeIndexes(self, fromIndex, toIndex, size):
        if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_b76d8a8:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_1ac2829e
        
        if jsGt(fromIndex, toIndex):
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_56820446
        
    
    def checkBoundsIndexes(self, startIndex, endIndex, size):
        if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_1da9b95d:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_74ee97cb
        
        if jsGt(startIndex, endIndex):
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_1b881f1f
        
    
    def orderedHashCode(self, c):
        hashCode = 1
        tmp0_iterator = c.iterator()
        while tmp0_iterator.hasNext():
            e = tmp0_iterator.next()
            tmp = imul(31, hashCode)
            tmp1_safe_receiver = e
            tmp2_elvis_lhs = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6be7c9d9
            hashCode = jsBitOr(jsPlus(tmp, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_19f31c85), 0)
        
        return hashCode
    
    def orderedEquals(self, c, other):
        if jsNot(jsEqeqeq(c._get_size_(), other._get_size_())):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_37f627d0
        
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
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_554d0ec1 = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_464de3f6
    
    return Companion_instance

class AbstractList:
    def __init__(self):
        Companion_getInstance()
        visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_79c2bc34
    
    def _get_size_(self):
        pass
    
    def get(self, index):
        pass
    
    def iterator(self):
        return IteratorImpl(self)
    
    def indexOf(self, element):
        tmp_ret_0
        visitDoWhileLoop_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_623f27a9
        return tmp_ret_0
    
    def lastIndexOf(self, element):
        tmp_ret_0
        visitDoWhileLoop_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_7d1a1ee9
        return tmp_ret_0
    
    def listIterator(self):
        return ListIteratorImpl(self, 0)
    
    def listIterator(self, index):
        return ListIteratorImpl(self, index)
    
    def subList(self, fromIndex, toIndex):
        return SubList(self, fromIndex, toIndex)
    
    def equals(self, other):
        if jsEqeqeq(other, self):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_af96ac9
        
        if jsNot(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_27564996):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_408d12fc
        
        if True:
            pass
        
        return Companion_getInstance().orderedEquals(self, kotlin_collections_Collection___(other))
    
    def hashCode(self):
        return Companion_getInstance().orderedHashCode(self)
    
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
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_66f73411

def emptyList():
    return EmptyList_getInstance()

def _get_serialVersionUID_(_this):
    return _this.serialVersionUID

def readResolve(_this):
    return EmptyList_getInstance()

class EmptyList:
    def __init__(self):
        EmptyList_instance = self
        self.serialVersionUID = Long(-1478467534, -1720727600)
    
    def equals(self, other):
        tmp
        if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_30f1487d:
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
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_752114f1
        
        if True:
            pass
        
        tmp
        if False:
            tmp = kotlin_Nothing(element)
        
        if True:
            if True:
                tmp = THROW_CCE()
            
        
        return self.contains(tmp)
    
    def containsAll(self, elements):
        return elements.isEmpty()
    
    def containsAll(self, elements):
        return self.containsAll(elements)
    
    def get(self, index):
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_23ee92df
    
    def indexOf(self, element):
        return -1
    
    def indexOf(self, element):
        if jsNot(False):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_43fa643e
        
        if True:
            pass
        
        tmp
        if False:
            tmp = kotlin_Nothing(element)
        
        if True:
            if True:
                tmp = THROW_CCE()
            
        
        return self.indexOf(tmp)
    
    def lastIndexOf(self, element):
        return -1
    
    def lastIndexOf(self, element):
        if jsNot(False):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_18fd1464
        
        if True:
            pass
        
        tmp
        if False:
            tmp = kotlin_Nothing(element)
        
        if True:
            if True:
                tmp = THROW_CCE()
            
        
        return self.lastIndexOf(tmp)
    
    def iterator(self):
        return EmptyIterator_getInstance()
    
    def listIterator(self):
        return EmptyIterator_getInstance()
    
    def listIterator(self, index):
        if jsNot(jsEqeqeq(index, 0)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_25fcdcc6
        
        return EmptyIterator_getInstance()
    
    def subList(self, fromIndex, toIndex):
        if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_42994d28:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_633cad4d
        
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_5b86f4cb
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_37058d66 = 0
def EmptyList_getInstance():
    if jsEqeq(EmptyList_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_6aa4a749
    
    return EmptyList_instance

class EmptyIterator:
    def __init__(self):
        EmptyIterator_instance = self
    
    def hasNext(self):
        return False
    
    def hasPrevious(self):
        return False
    
    def nextIndex(self):
        return 0
    
    def previousIndex(self):
        return -1
    
    def next(self):
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_31de8099
    
    def previous(self):
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_12478b4e
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_25ce4114 = 0
def EmptyIterator_getInstance():
    if jsEqeq(EmptyIterator_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_38d5f5d5
    
    return EmptyIterator_instance

def _get_lastIndex_():
    return jsBitOr(jsMinus(self._get_size_(), 1), 0)

def removeAll(predicate):
    return filterInPlace(predicate, True)

def removeAll(predicate):
    return filterInPlace(predicate, True)

def filterInPlace(predicate, predicateResultToRemove):
    if jsNot(isInterface(self, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_6af4c74e
    
    if True:
        pass
    
    writeIndex = 0
    inductionVariable = 0
    last = _get_lastIndex_()
    if jsLtEq(inductionVariable, last):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_40dcd875
    
    if jsLt(writeIndex, self._get_size_()):
        inductionVariable = _get_lastIndex_()
        if jsLtEq(writeIndex, inductionVariable):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_19b6eefb
        
        return True
    
    if True:
        return False
    

def filterInPlace(predicate, predicateResultToRemove):
    result = False
    tmp0_with_0 = self.iterator()
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
    
    def __init__(self):
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
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_3d4d5af7
        
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_23d45f7d
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def __init__(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_6cbac170 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_5ef79613 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_4bf4cd2e = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_2ee3549e = 0
def values():
    return arrayLiteral(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_2fce34e4)

def valueOf(value):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4ca87783

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_5e583af4 = 0
def InvocationKind_initEntries():
    if InvocationKind_entriesInitialized:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_60155d7f
    
    InvocationKind_entriesInitialized = True
    InvocationKind_AT_MOST_ONCE_instance = InvocationKind('AT_MOST_ONCE', 0)
    InvocationKind_AT_LEAST_ONCE_instance = InvocationKind('AT_LEAST_ONCE', 1)
    InvocationKind_EXACTLY_ONCE_instance = InvocationKind('EXACTLY_ONCE', 2)
    InvocationKind_UNKNOWN_instance = InvocationKind('UNKNOWN', 3)

class InvocationKind:
    def __init__(self, name, ordinal):
        visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_3f11add1
    
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
    def __init__(self):
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
    
    def __init__(self):
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
    
    def __init__(self):
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
    
    def __init__(self):
        pass
    

class Effect:
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def __init__(self):
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
    
    def __init__(self):
        pass
    

class ConditionalEffect:
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def __init__(self):
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
    
    def __init__(self):
        pass
    

def Continuation(context, resumeWith):
    return _no_name_provided_(context, resumeWith)

def resumeWithException(exception):
    tmp0_failure_0 = Companion_getInstance()
    return self.resumeWith(Result(createFailure(exception)))

def resume(value):
    tmp0_success_0 = Companion_getInstance()
    return self.resumeWith(Result(value))

def _get_coroutineContext_():
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_1ab07559

class _no_name_provided_:
    def __init__(self, _context, _resumeWith):
        self._context = _context
        self._resumeWith = _resumeWith
    
    def _get_context_(self):
        return self._context
    
    def resumeWith(self, result):
        return self._resumeWith.invoke(boxIntrinsic(result))
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class Key:
    def __init__(self):
        Key_instance = self
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_5a5d16c2 = 0
def Key_getInstance():
    if jsEqeq(Key_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_5ace491
    
    return Key_instance

class ContinuationInterceptor:
    def interceptContinuation(self, continuation):
        pass
    
    def releaseInterceptedContinuation(self, continuation):
        pass
    
    def get(self, key):
        if jsInstanceOf(key, jsClass()):
            tmp
            if kotlin_coroutines_AbstractCoroutineContextKey_out_kotlin_coroutines_Element_out_kotlin_coroutines_Element_(key).isSubKey(self._get_key_()):
                tmp = kotlin_coroutines_AbstractCoroutineContextKey_out_kotlin_coroutines_Element_out_kotlin_coroutines_Element_(key).tryCast(self)
                tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_455d026d
            
            if True:
                tmp = None
            
            return tmp
        
        if True:
            pass
        
        tmp
        if jsEqeqeq(Key_getInstance(), key):
            tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2cd92fd
        
        if True:
            tmp = None
        
        return tmp
    
    def minusKey(self, key):
        if jsInstanceOf(key, jsClass()):
            return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_37d4b676
        
        if True:
            pass
        
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_20873a9
    
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
    
    def __init__(self):
        Key_getInstance()
    

class Key:
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def __init__(self):
        pass
    

class Element:
    def _get_key_(self):
        pass
    
    def get(self, key):
        tmp
        if equals(self._get_key_(), key):
            tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4ddb882
        
        if True:
            tmp = None
        
        return tmp
    
    def fold(self, initial, operation):
        return operation.invoke(initial, self)
    
    def minusKey(self, key):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4c0fe501
    
    def plus(self, context):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def __init__(self):
        pass
    

class _no_name_provided_:
    def __init__(self):
        pass
    
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
                tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_636ee65a
            
            tmp = tmp
        
        return tmp
    
    def invoke(self, p1, p2):
        tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_612a0d49
        return self.invoke(tmp, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_1829184b)
    

class CoroutineContext:
    def get(self, key):
        pass
    
    def fold(self, initial, operation):
        pass
    
    def plus(self, context):
        tmp
        if jsEqeqeq(context, EmptyCoroutineContext_getInstance()):
            tmp = self
        
        if True:
            tmp = context.fold(self, _no_name_provided__factory())
        
        return tmp
    
    def minusKey(self, key):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def __init__(self):
        pass
    

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_1ac7ec0e

def _get_serialVersionUID_(_this):
    return _this.serialVersionUID

def readResolve(_this):
    return EmptyCoroutineContext_getInstance()

class EmptyCoroutineContext:
    def __init__(self):
        EmptyCoroutineContext_instance = self
        self.serialVersionUID = Long(0, 0)
    
    def get(self, key):
        return None
    
    def fold(self, initial, operation):
        return initial
    
    def plus(self, context):
        return context
    
    def minusKey(self, key):
        return self
    
    def hashCode(self):
        return 0
    
    def toString(self):
        return 'EmptyCoroutineContext'
    
    def equals(self, other):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_4a35f473 = 0
def EmptyCoroutineContext_getInstance():
    if jsEqeq(EmptyCoroutineContext_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_6a39c005
    
    return EmptyCoroutineContext_instance

def _get_serialVersionUID_(_this):
    return _this.serialVersionUID

class Companion:
    def __init__(self):
        Companion_instance = self
        self.serialVersionUID = Long(0, 0)
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_43e78ed6 = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_75bd7c4a
    
    return Companion_instance

def readResolve(_this):
    tmp0_fold_0 = _this.elements
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
    return _this.left

def _get_element_(_this):
    return _this.element

def size(_this):
    cur = _this
    size = 2
    while True:
        tmp = cur.left
        tmp0_elvis_lhs = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_1ddf5237
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
        if jsNot(contains(_this, cur.element)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_74e3836a
        
        next = cur.left
        if jsInstanceOf(next, jsClass()):
            cur = kotlin_coroutines_CombinedContext(next)
        
        if True:
            if True:
                return contains(_this, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_43188555)
            
        
    

def writeReplace(_this):
    n = size(_this)
    elements = fillArrayVal(Array(n), None)
    index = _sharedBox_create(0)
    _this.fold(Unit_getInstance(), _no_name_provided__factory(elements, index))
    tmp0_check_0 = jsEqeqeq(_sharedBox_read(index), n)
    if jsNot(tmp0_check_0):
        message_2 = 'Check failed.'
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_44ebd5e9
    
    return Serialized(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_1fee651f)

class Serialized:
    def __init__(self, elements):
        Companion_getInstance()
        self.elements = elements
    
    def _get_elements_(self):
        return self.elements
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class _no_name_provided_:
    def __init__(self):
        pass
    
    def invoke(self, acc, element):
        tmp
        if jsEqeqeq(charSequenceLength(acc), 0):
            tmp = toString(element)
        
        if True:
            if True:
                tmp = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_1f0630a9
            
        
        return tmp
    
    def invoke(self, p1, p2):
        tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2ba70002
        return self.invoke(tmp, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_59edc76c)
    

class _no_name_provided_:
    def __init__(self, _elements, _index):
        self._elements = _elements
        self._index = _index
    
    def invoke(self, _anonymous_parameter_0_, element):
        tmp0 = _sharedBox_read(self._index)
        _sharedBox_write(self._index, jsBitOr(jsPlus(tmp0, 1), 0))
        jsArraySet(self._elements, tmp0, element)
    
    def invoke(self, p1, p2):
        tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_77aa1e4
        self.invoke(tmp, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3f3953c3)
        return Unit_getInstance()
    

class CombinedContext:
    def __init__(self, left, element):
        self.left = left
        self.element = element
    
    def get(self, key):
        cur = self
        while True:
            tmp0_safe_receiver = cur.element.get(key)
            if jsEqeq(tmp0_safe_receiver, None):
                visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstImpl_66e434e8
            
            if True:
                visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_520acc7a
            
            Unit_getInstance()
            next = cur.left
            if jsInstanceOf(next, jsClass()):
                cur = kotlin_coroutines_CombinedContext(next)
            
            if True:
                if True:
                    return next.get(key)
                
            
        
    
    def fold(self, initial, operation):
        return operation.invoke(self.left.fold(initial, operation), self.element)
    
    def minusKey(self, key):
        tmp0_safe_receiver = self.element.get(key)
        if jsEqeq(tmp0_safe_receiver, None):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstImpl_628aea61
        
        if True:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_7d8e1c87
        
        Unit_getInstance()
        newLeft = self.left.minusKey(key)
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_24d5a11a
    
    def equals(self, other):
        tmp
        if jsEqeqeq(self, other):
            tmp = True
        
        if True:
            tmp
            tmp
            if jsInstanceOf(other, jsClass()):
                tmp = jsEqeqeq(size(kotlin_coroutines_CombinedContext(other)), size(self))
            
            if True:
                if True:
                    tmp = False
                
            
            if tmp:
                tmp = containsAll(kotlin_coroutines_CombinedContext(other), self)
            
            if True:
                if True:
                    tmp = False
                
            
            tmp = tmp
        
        return tmp
    
    def hashCode(self):
        return jsBitOr(jsPlus(hashCode(self.left), hashCode(self.element)), 0)
    
    def toString(self):
        return jsPlus(jsPlus('[', self.fold('', _no_name_provided__factory())), ']')
    
    def plus(self, context):
        pass
    

def _get_safeCast_(_this):
    return _this.safeCast

def _get_topmostKey_(_this):
    return _this.topmostKey

class AbstractCoroutineContextKey:
    def __init__(self, baseKey, safeCast):
        self.safeCast = safeCast
        tmp = self
        tmp
        if jsInstanceOf(baseKey, jsClass()):
            tmp = kotlin_coroutines_AbstractCoroutineContextKey_out_kotlin_coroutines_Element_out_kotlin_coroutines_Element_(baseKey).topmostKey
        
        if True:
            if True:
                tmp = baseKey
            
        
        tmp.topmostKey = tmp
    
    def tryCast(self, element):
        return self.safeCast.invoke(element)
    
    def isSubKey(self, key):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_51f39482
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_54e9d42e

def _no_name_provided__factory(_elements, _index):
    i = _no_name_provided_(_elements, _index)
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_72a2b17d

def _get_COROUTINE_SUSPENDED_():
    return CoroutineSingletons_COROUTINE_SUSPENDED_getInstance()

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_620bb4ea = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_16c5974d = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_7c3013ea = 0
def values():
    return arrayLiteral(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_6da640fe)

def valueOf(value):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3c4161d1

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_4bc40cb8 = 0
def CoroutineSingletons_initEntries():
    if CoroutineSingletons_entriesInitialized:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_737935a4
    
    CoroutineSingletons_entriesInitialized = True
    CoroutineSingletons_COROUTINE_SUSPENDED_instance = CoroutineSingletons('COROUTINE_SUSPENDED', 0)
    CoroutineSingletons_UNDECIDED_instance = CoroutineSingletons('UNDECIDED', 1)
    CoroutineSingletons_RESUMED_instance = CoroutineSingletons('RESUMED', 2)

class CoroutineSingletons:
    def __init__(self, name, ordinal):
        visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_78519d63
    
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
    return toByte(jsBitAnd(kotlin_Int(self), kotlin_Int(other)))

def _or(other):
    return toByte(jsBitOr(kotlin_Int(self), kotlin_Int(other)))

def xor(other):
    return toByte(jsBitXor(kotlin_Int(self), kotlin_Int(other)))

def inv():
    return toByte(jsBitNot(kotlin_Int(self)))

def _and(other):
    return toShort(jsBitAnd(kotlin_Int(self), kotlin_Int(other)))

def _or(other):
    return toShort(jsBitOr(kotlin_Int(self), kotlin_Int(other)))

def xor(other):
    return toShort(jsBitXor(kotlin_Int(self), kotlin_Int(other)))

def inv():
    return toShort(jsBitNot(kotlin_Int(self)))

class ExperimentalTypeInference:
    def __init__(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def RequireKotlin_init__Init_(version, message, level, versionKind, errorCode, _mask0, _marker, _this):
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 2), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_4df03572
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 4), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_48b4fecb
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 8), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_6e9197d1
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 16), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_406ba622
    
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_f157271
    return _this

def RequireKotlin_init__Create_(version, message, level, versionKind, errorCode, _mask0, _marker):
    return RequireKotlin_init__Init_(version, message, level, versionKind, errorCode, _mask0, _marker, Object_create())

class RequireKotlin:
    def __init__(self, version, message, level, versionKind, errorCode):
        self.version = version
        self.message = message
        self.level = level
        self.versionKind = versionKind
        self.errorCode = errorCode
    
    def _get_version_(self):
        return self.version
    
    def _get_message_(self):
        return self.message
    
    def _get_level_(self):
        return self.level
    
    def _get_versionKind_(self):
        return self.versionKind
    
    def _get_errorCode_(self):
        return self.errorCode
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_209fa1fc = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_66e33cea = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_5b81d35c = 0
def values():
    return arrayLiteral(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_510e260d)

def valueOf(value):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_7cc880cf

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_5022aaa3 = 0
def RequireKotlinVersionKind_initEntries():
    if RequireKotlinVersionKind_entriesInitialized:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_7e3559b4
    
    RequireKotlinVersionKind_entriesInitialized = True
    RequireKotlinVersionKind_LANGUAGE_VERSION_instance = RequireKotlinVersionKind('LANGUAGE_VERSION', 0)
    RequireKotlinVersionKind_COMPILER_VERSION_instance = RequireKotlinVersionKind('COMPILER_VERSION', 1)
    RequireKotlinVersionKind_API_VERSION_instance = RequireKotlinVersionKind('API_VERSION', 2)

class RequireKotlinVersionKind:
    def __init__(self, name, ordinal):
        visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_5e231326
    
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
    def __init__(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class NoInfer:
    def __init__(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class DynamicExtension:
    def __init__(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class ContractsDsl:
    def __init__(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class OnlyInputTypes:
    def __init__(self):
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
    
    def __init__(self):
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
    
    def __init__(self):
        pass
    

class Companion:
    def __init__(self):
        Companion_instance = self
        self.star = KTypeProjection(None, None)
    
    def _get_star_(self):
        return self.star
    
    def _get_STAR_(self):
        return self.star
    
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
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_56dc6b33 = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_12ce5274
    
    return Companion_instance

class KTypeProjection:
    def __init__(self, variance, type):
        Companion_getInstance()
        self.variance = variance
        self.type = type
        tmp0_require_0 = jsEqeqeq(jsEqeq(self.variance, None), jsEqeq(self.type, None))
        if jsNot(tmp0_require_0):
            message_2 = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_122de194
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_c1add62
        
    
    def _get_variance_(self):
        return self.variance
    
    def _get_type_(self):
        return self.type
    
    def toString(self):
        tmp0_subject = self.variance
        tmp
        if jsEqeq(tmp0_subject, None):
            tmp = '*'
        
        if equals(tmp0_subject, KVariance_INVARIANT_getInstance()):
            tmp = toString()
        
        if equals(tmp0_subject, KVariance_IN_getInstance()):
            tmp = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_4a402ba3
        
        if equals(tmp0_subject, KVariance_OUT_getInstance()):
            tmp = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_7cdfb8c3
        
        if True:
            noWhenBranchMatchedException()
        
        return tmp
    
    def component1(self):
        return self.variance
    
    def component2(self):
        return self.type
    
    def copy(self, variance, type):
        return KTypeProjection(variance, type)
    
    def copy_default(self, variance, type, _mask0, _handler):
        if jsNot(jsEqeqeq(jsBitAnd(_mask0, 1), 0)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_4bc88ccb
        
        if jsNot(jsEqeqeq(jsBitAnd(_mask0, 2), 0)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_27129ef5
        
        return self.copy(variance, type)
    
    def hashCode(self):
        result = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_5b64bc02
        result = jsBitOr(jsPlus(imul(result, 31), visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3f5f610d), 0)
        return result
    
    def equals(self, other):
        if jsEqeqeq(self, other):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_43aa767
        
        if jsNot(jsInstanceOf(other, jsClass())):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_6bbb3280
        
        if True:
            pass
        
        tmp0_other_with_cast = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_41c22d59
        if jsNot(equals(self.variance, tmp0_other_with_cast.variance)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_351fadfa
        
        if jsNot(equals(self.type, tmp0_other_with_cast.type)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_6fa2d0b2
        
        return True
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_6a4899c = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_1b406bc2 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_30d0e28e = 0
def values():
    return arrayLiteral(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_5ca64b79)

def valueOf(value):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4790a29a

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_343f01c7 = 0
def KVariance_initEntries():
    if KVariance_entriesInitialized:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_52ac57e7
    
    KVariance_entriesInitialized = True
    KVariance_INVARIANT_instance = KVariance('INVARIANT', 0)
    KVariance_IN_instance = KVariance('IN', 1)
    KVariance_OUT_instance = KVariance('OUT', 2)

class KVariance:
    def __init__(self, name, ordinal):
        visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_35e50381
    
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
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_2bda778a
    
    if True:
        if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_21c09e90:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_6a056d13
        
        if True:
            if jsInstanceOf(element, jsClass()):
                visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_1dafe1d2
            
            if True:
                if True:
                    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_140fc16f
                
            
        
    

def isEmpty():
    return jsEqeqeq(charSequenceLength(self), 0)

def _get_lastIndex_():
    return jsBitOr(jsMinus(charSequenceLength(self), 1), 0)

def _get_UNDEFINED_RESULT_():
    return UNDEFINED_RESULT

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_2f3d5cd = 0
def UNDEFINED_RESULT_init_():
    tmp0_success_0 = Companion_getInstance()
    tmp1_success_0 = _get_COROUTINE_SUSPENDED_()
    return Result(tmp1_success_0)

def check(value):
    if jsNot(value):
        message_2 = 'Check failed.'
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_31d31620
    

def check(value, lazyMessage):
    if jsNot(value):
        message = lazyMessage.invoke()
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_417081c8
    

def error(message):
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_52889c68

def require(value, lazyMessage):
    if jsNot(value):
        message = lazyMessage.invoke()
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_7ad4085c
    

def _Result___get_value__impl_(this):
    return this.value

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
        tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6d1e558b
    
    return tmp

def Result__exceptionOrNull_impl(this):
    tmp0_subject = _Result___get_value__impl_(this)
    tmp
    if jsInstanceOf(tmp0_subject, jsClass()):
        tmp = kotlin_Failure(_Result___get_value__impl_(this)).exception
    
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
            tmp = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_3b4971c4
        
    
    return tmp

class Companion:
    def __init__(self):
        Companion_instance = self
    
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
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_2f8afb66 = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_33ded464
    
    return Companion_instance

class Failure:
    def __init__(self, exception):
        self.exception = exception
    
    def _get_exception_(self):
        return self.exception
    
    def equals(self, other):
        tmp
        if jsInstanceOf(other, jsClass()):
            tmp = equals(self.exception, kotlin_Failure(other).exception)
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def hashCode(self):
        return hashCode(self.exception)
    
    def toString(self):
        return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_20b42094
    

def Result__hashCode_impl(this):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_43582af1

def Result__equals_impl(this, other):
    if jsNot(jsInstanceOf(other, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_54cce500
    
    if True:
        pass
    
    tmp0_other_with_cast = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_7b16d337
    if jsNot(equals(this.value, tmp0_other_with_cast.value)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_7077ae9c
    
    return True

class Result:
    def __init__(self, value):
        Companion_getInstance()
        self.value = value
    
    def toString(self):
        return Result__toString_impl(unboxIntrinsic(self))
    
    def hashCode(self):
        return Result__hashCode_impl(unboxIntrinsic(self))
    
    def equals(self, other):
        return Result__equals_impl(unboxIntrinsic(self), other)
    

def createFailure(exception):
    return Failure(exception)

def getOrThrow():
    throwOnFailure()
    tmp = _Result___get_value__impl_(self)
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_5b36c066

def throwOnFailure():
    tmp = _Result___get_value__impl_(self)
    if jsInstanceOf(tmp, jsClass()):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_3458be63
    
    if True:
        pass
    

def run(block):
    return block.invoke()

def TODO():
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_2812c884

def NotImplementedError_init__Init_(message, _mask0, _marker, _this):
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 1), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_6c8eab63
    
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_3dd3f237
    return _this

def NotImplementedError_init__Create_(message, _mask0, _marker):
    tmp = NotImplementedError_init__Init_(message, _mask0, _marker, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_73fe55f9)
    return tmp

class NotImplementedError:
    def __init__(self, message):
        Error_init__Init_(message, self)
        captureStack(self, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_6281326f)
    
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
    return block.invoke(self)

def apply(block):
    block.invoke(self)
    return self

def repeat(times, action):
    inductionVariable = 0
    if jsLt(inductionVariable, times):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_133a8a9f
    

def _with(receiver, block):
    return block.invoke(receiver)

def also(block):
    block.invoke(self)
    return self

def run(block):
    return block.invoke(self)

def _UByte___get_data__impl_(this):
    return this.data

class Companion:
    def __init__(self):
        Companion_instance = self
        self.MIN_VALUE = UByte(visitConst_other_Byte)
        self.MAX_VALUE = UByte(visitConst_other_Byte)
        self.SIZE_BYTES = 1
        self.SIZE_BITS = 8
    
    def _get_MIN_VALUE_(self):
        return self.MIN_VALUE
    
    def _get_MAX_VALUE_(self):
        return self.MAX_VALUE
    
    def _get_SIZE_BYTES_(self):
        return self.SIZE_BYTES
    
    def _get_SIZE_BITS_(self):
        return self.SIZE_BITS
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_a22be4c = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_4ad667c8
    
    return Companion_instance

def UByte__compareTo_impl(this, other):
    tmp = jsBitAnd(kotlin_Int(_UByte___get_data__impl_(this)), 255)
    return compareTo(tmp, jsBitAnd(kotlin_Int(_UByte___get_data__impl_(other)), 255))

def UByte__compareTo_impl(this, other):
    tmp = unboxIntrinsic(this)
    return UByte__compareTo_impl(tmp, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_50f77755)

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
    return this.data

def UByte__equals_impl(this, other):
    if jsNot(jsInstanceOf(other, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_29a5f924
    
    if True:
        pass
    
    tmp0_other_with_cast = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_1dde2d1
    if jsNot(jsEqeqeq(this.data, tmp0_other_with_cast.data)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_322593ed
    
    return True

class UByte:
    def __init__(self, data):
        Companion_getInstance()
        self.data = data
    
    def compareTo(self, other):
        return UByte__compareTo_impl(unboxIntrinsic(self), other)
    
    def compareTo(self, other):
        return UByte__compareTo_impl(self, other)
    
    def toString(self):
        return UByte__toString_impl(unboxIntrinsic(self))
    
    def hashCode(self):
        return UByte__hashCode_impl(unboxIntrinsic(self))
    
    def equals(self, other):
        return UByte__equals_impl(unboxIntrinsic(self), other)
    

def toUByte():
    return UByte(toByte(self))

def toUByte():
    return UByte(toByte(self))

def toUByte():
    return UByte(self.toByte())

def toUByte():
    return UByte(self)

def _get_array_(_this):
    return _this.array

def _set_index_(_this, _set___):
    _this.index = _set___

def _get_index_(_this):
    return _this.index

def _UByteArray___get_storage__impl_(this):
    return this.storage

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
    def __init__(self, array):
        visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_5058fefb
        self.array = array
        self.index = 0
    
    def hasNext(self):
        return jsLt(self.index, jsArrayLength(self.array))
    
    def nextUByte(self):
        tmp
        if jsLt(self.index, jsArrayLength(self.array)):
            tmp0_this = self
            tmp1 = tmp0_this.index
            tmp0_this.index = jsBitOr(jsPlus(tmp1, 1), 0)
            tmp0_toUByte_0 = jsArrayGet(self.array, tmp1)
            tmp = UByte(tmp0_toUByte_0)
        
        if True:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_15af06f
        
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
    tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_96b3034
    if jsNot(jsInstanceOf(tmp, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_5bfeb9ba
    
    if True:
        pass
    
    tmp = _UByteArray___get_storage__impl_(this)
    return contains(_UByte___get_data__impl_(element))

def UByteArray__contains_impl(this, element):
    if jsNot(jsInstanceOf(element, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_72fb8a1d
    
    if True:
        pass
    
    tmp = unboxIntrinsic(this)
    return UByteArray__contains_impl(tmp, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_1ceefb02)

def UByteArray__containsAll_impl(this, elements):
    tmp_ret_0
    visitDoWhileLoop_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_3f6f5e03
    return tmp_ret_0

def UByteArray__containsAll_impl(this, elements):
    return UByteArray__containsAll_impl(unboxIntrinsic(this), elements)

def UByteArray__isEmpty_impl(this):
    return jsEqeqeq(jsArrayLength(_UByteArray___get_storage__impl_(this)), 0)

def UByteArray__toString_impl(this):
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_7d12c4dd

def UByteArray__hashCode_impl(this):
    return hashCode(this.storage)

def UByteArray__equals_impl(this, other):
    if jsNot(jsInstanceOf(other, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_22e253c7
    
    if True:
        pass
    
    tmp0_other_with_cast = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4faf4191
    if jsNot(equals(this.storage, tmp0_other_with_cast.storage)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_3b8a8abc
    
    return True

class UByteArray:
    def __init__(self, storage):
        self.storage = storage
    
    def _get_size_(self):
        return _UByteArray___get_size__impl_(unboxIntrinsic(self))
    
    def iterator(self):
        return UByteArray__iterator_impl(unboxIntrinsic(self))
    
    def contains(self, element):
        return UByteArray__contains_impl(unboxIntrinsic(self), element)
    
    def contains(self, element):
        return UByteArray__contains_impl(self, element)
    
    def containsAll(self, elements):
        return UByteArray__containsAll_impl(unboxIntrinsic(self), elements)
    
    def containsAll(self, elements):
        return UByteArray__containsAll_impl(self, elements)
    
    def isEmpty(self):
        return UByteArray__isEmpty_impl(unboxIntrinsic(self))
    
    def toString(self):
        return UByteArray__toString_impl(unboxIntrinsic(self))
    
    def hashCode(self):
        return UByteArray__hashCode_impl(unboxIntrinsic(self))
    
    def equals(self, other):
        return UByteArray__equals_impl(unboxIntrinsic(self), other)
    

def _UInt___get_data__impl_(this):
    return this.data

class Companion:
    def __init__(self):
        Companion_instance = self
        self.MIN_VALUE = UInt(0)
        self.MAX_VALUE = UInt(-1)
        self.SIZE_BYTES = 4
        self.SIZE_BITS = 32
    
    def _get_MIN_VALUE_(self):
        return self.MIN_VALUE
    
    def _get_MAX_VALUE_(self):
        return self.MAX_VALUE
    
    def _get_SIZE_BYTES_(self):
        return self.SIZE_BYTES
    
    def _get_SIZE_BITS_(self):
        return self.SIZE_BITS
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_6180afa9 = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_2c18cde7
    
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
    return UInt__compareTo_impl(tmp, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_11fbbc08)

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
    return this.data

def UInt__equals_impl(this, other):
    if jsNot(jsInstanceOf(other, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_134ec0f3
    
    if True:
        pass
    
    tmp0_other_with_cast = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_40b0e4e6
    if jsNot(jsEqeqeq(this.data, tmp0_other_with_cast.data)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_7925e772
    
    return True

class UInt:
    def __init__(self, data):
        Companion_getInstance()
        self.data = data
    
    def compareTo(self, other):
        return UInt__compareTo_impl(unboxIntrinsic(self), other)
    
    def compareTo(self, other):
        return UInt__compareTo_impl(self, other)
    
    def toString(self):
        return UInt__toString_impl(unboxIntrinsic(self))
    
    def hashCode(self):
        return UInt__hashCode_impl(unboxIntrinsic(self))
    
    def equals(self, other):
        return UInt__equals_impl(unboxIntrinsic(self), other)
    

def toUInt():
    return UInt(self.toInt())

def toUInt():
    return UInt(self)

def toUInt():
    return UInt(kotlin_Int(self))

def toUInt():
    return doubleToUInt(self)

def toUInt():
    return doubleToUInt(kotlin_Double(self))

def toUInt():
    return UInt(kotlin_Int(self))

def _get_array_(_this):
    return _this.array

def _set_index_(_this, _set___):
    _this.index = _set___

def _get_index_(_this):
    return _this.index

def _UIntArray___get_storage__impl_(this):
    return this.storage

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
    def __init__(self, array):
        visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_15324f25
        self.array = array
        self.index = 0
    
    def hasNext(self):
        return jsLt(self.index, jsArrayLength(self.array))
    
    def nextUInt(self):
        tmp
        if jsLt(self.index, jsArrayLength(self.array)):
            tmp0_this = self
            tmp1 = tmp0_this.index
            tmp0_this.index = jsBitOr(jsPlus(tmp1, 1), 0)
            tmp0_toUInt_0 = jsArrayGet(self.array, tmp1)
            tmp = UInt(tmp0_toUInt_0)
        
        if True:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_2f70d78c
        
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
    tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_54b7bfbe
    if jsNot(jsInstanceOf(tmp, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_51eeae0a
    
    if True:
        pass
    
    tmp = _UIntArray___get_storage__impl_(this)
    return contains(_UInt___get_data__impl_(element))

def UIntArray__contains_impl(this, element):
    if jsNot(jsInstanceOf(element, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_e314809
    
    if True:
        pass
    
    tmp = unboxIntrinsic(this)
    return UIntArray__contains_impl(tmp, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_1d8f923f)

def UIntArray__containsAll_impl(this, elements):
    tmp_ret_0
    visitDoWhileLoop_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_122ff251
    return tmp_ret_0

def UIntArray__containsAll_impl(this, elements):
    return UIntArray__containsAll_impl(unboxIntrinsic(this), elements)

def UIntArray__isEmpty_impl(this):
    return jsEqeqeq(jsArrayLength(_UIntArray___get_storage__impl_(this)), 0)

def UIntArray__toString_impl(this):
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_22125b57

def UIntArray__hashCode_impl(this):
    return hashCode(this.storage)

def UIntArray__equals_impl(this, other):
    if jsNot(jsInstanceOf(other, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_52737c1
    
    if True:
        pass
    
    tmp0_other_with_cast = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_c334f3b
    if jsNot(equals(this.storage, tmp0_other_with_cast.storage)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_6eff05e7
    
    return True

class UIntArray:
    def __init__(self, storage):
        self.storage = storage
    
    def _get_size_(self):
        return _UIntArray___get_size__impl_(unboxIntrinsic(self))
    
    def iterator(self):
        return UIntArray__iterator_impl(unboxIntrinsic(self))
    
    def contains(self, element):
        return UIntArray__contains_impl(unboxIntrinsic(self), element)
    
    def contains(self, element):
        return UIntArray__contains_impl(self, element)
    
    def containsAll(self, elements):
        return UIntArray__containsAll_impl(unboxIntrinsic(self), elements)
    
    def containsAll(self, elements):
        return UIntArray__containsAll_impl(self, elements)
    
    def isEmpty(self):
        return UIntArray__isEmpty_impl(unboxIntrinsic(self))
    
    def toString(self):
        return UIntArray__toString_impl(unboxIntrinsic(self))
    
    def hashCode(self):
        return UIntArray__hashCode_impl(unboxIntrinsic(self))
    
    def equals(self, other):
        return UIntArray__equals_impl(unboxIntrinsic(self), other)
    

class Companion:
    def __init__(self):
        Companion_instance = self
        self.EMPTY = UIntRange(UInt(-1), UInt(0))
    
    def _get_EMPTY_(self):
        return self.EMPTY
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_983983e = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_767e28e5
    
    return Companion_instance

class UIntRange:
    def __init__(self, start, endInclusive):
        Companion_getInstance()
        visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_46e38c28
    
    def _get_start_(self):
        return self._get_first_()
    
    def _get_start_(self):
        return boxIntrinsic(self._get_start_())
    
    def _get_endInclusive_(self):
        return self._get_last_()
    
    def _get_endInclusive_(self):
        return boxIntrinsic(self._get_endInclusive_())
    
    def contains(self, value):
        tmp
        tmp0_compareTo_0 = self._get_first_()
        if jsLtEq(uintCompare(_UInt___get_data__impl_(tmp0_compareTo_0), _UInt___get_data__impl_(value)), 0):
            tmp1_compareTo_0 = self._get_last_()
            tmp = jsLtEq(uintCompare(_UInt___get_data__impl_(value), _UInt___get_data__impl_(tmp1_compareTo_0)), 0)
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def contains(self, value):
        return self.contains(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_50233f7d)
    
    def isEmpty(self):
        tmp0_compareTo_0 = self._get_first_()
        tmp1_compareTo_0 = self._get_last_()
        return jsGt(uintCompare(_UInt___get_data__impl_(tmp0_compareTo_0), _UInt___get_data__impl_(tmp1_compareTo_0)), 0)
    
    def equals(self, other):
        tmp
        if jsInstanceOf(other, jsClass()):
            tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6fad2da0
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def hashCode(self):
        tmp
        if self.isEmpty():
            tmp = -1
        
        if True:
            tmp0_toInt_0 = self._get_first_()
            tmp = imul(31, _UInt___get_data__impl_(tmp0_toInt_0))
            tmp1_toInt_0 = self._get_last_()
            tmp = jsBitOr(jsPlus(tmp, _UInt___get_data__impl_(tmp1_toInt_0)), 0)
        
        return tmp
    
    def toString(self):
        return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_8aa70fd
    
    def _get_first_(self):
        pass
    
    def _get_last_(self):
        pass
    
    def _get_step_(self):
        pass
    
    def iterator(self):
        pass
    

class Companion:
    def __init__(self):
        Companion_instance = self
    
    def fromClosedRange(self, rangeStart, rangeEnd, step):
        return UIntProgression(rangeStart, rangeEnd, step)
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_4fd5db1d = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_2d25a125
    
    return Companion_instance

class UIntProgression:
    def __init__(self, start, endInclusive, step):
        Companion_getInstance()
        if jsEqeqeq(step, 0):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_10d0ca5a
        
        if jsEqeqeq(step, IntCompanionObject_getInstance().MIN_VALUE):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_32a4284d
        
        self.first = start
        self.last = getProgressionLastElement(start, endInclusive, step)
        self.step = step
    
    def _get_first_(self):
        return self.first
    
    def _get_last_(self):
        return self.last
    
    def _get_step_(self):
        return self.step
    
    def iterator(self):
        return UIntProgressionIterator(self.first, self.last, self.step)
    
    def isEmpty(self):
        tmp
        if jsGt(self.step, 0):
            tmp0_compareTo_0 = self.first
            tmp1_compareTo_0 = self.last
            tmp = jsGt(uintCompare(_UInt___get_data__impl_(tmp0_compareTo_0), _UInt___get_data__impl_(tmp1_compareTo_0)), 0)
        
        if True:
            tmp2_compareTo_0 = self.first
            tmp3_compareTo_0 = self.last
            tmp = jsLt(uintCompare(_UInt___get_data__impl_(tmp2_compareTo_0), _UInt___get_data__impl_(tmp3_compareTo_0)), 0)
        
        return tmp
    
    def equals(self, other):
        tmp
        if jsInstanceOf(other, jsClass()):
            tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_256f298e
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def hashCode(self):
        tmp
        if self.isEmpty():
            tmp = -1
        
        if True:
            tmp0_toInt_0 = self.first
            tmp = imul(31, _UInt___get_data__impl_(tmp0_toInt_0))
            tmp1_toInt_0 = self.last
            tmp = jsBitOr(jsPlus(imul(31, jsBitOr(jsPlus(tmp, _UInt___get_data__impl_(tmp1_toInt_0)), 0)), kotlin_Int(self.step)), 0)
        
        return tmp
    
    def toString(self):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_1f69937a
    

def _get_finalElement_(_this):
    return _this.finalElement

def _set_hasNext_(_this, _set___):
    _this.hasNext = _set___

def _get_hasNext_(_this):
    return _this.hasNext

def _get_step_(_this):
    return _this.step

def _set_next_(_this, _set___):
    _this.next = _set___

def _get_next_(_this):
    return _this.next

class UIntProgressionIterator:
    def __init__(self, first, last, step):
        visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_7860a014
        self.finalElement = last
        tmp = self
        tmp
        if jsGt(step, 0):
            tmp = jsLtEq(uintCompare(_UInt___get_data__impl_(first), _UInt___get_data__impl_(last)), 0)
        
        if True:
            tmp = jsGtEq(uintCompare(_UInt___get_data__impl_(first), _UInt___get_data__impl_(last)), 0)
        
        tmp.hasNext = tmp
        tmp = self
        tmp.step = UInt(step)
        self.next = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3b886b0f
    
    def hasNext(self):
        return self.hasNext
    
    def nextUInt(self):
        value = self.next
        if equals(boxIntrinsic(value), boxIntrinsic(self.finalElement)):
            if jsNot(self.hasNext):
                visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_711261c7
            
            self.hasNext = False
        
        if True:
            tmp0_this = self
            tmp = tmp0_this
            tmp0_plus_0 = tmp0_this.next
            tmp1_plus_0 = self.step
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
    def __init__(self):
        pass
    
    def next(self):
        return self.nextUInt()
    
    def next(self):
        return boxIntrinsic(self.next())
    
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
    def __init__(self):
        pass
    
    def next(self):
        return self.nextULong()
    
    def next(self):
        return boxIntrinsic(self.next())
    
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
    def __init__(self):
        pass
    
    def next(self):
        return self.nextUByte()
    
    def next(self):
        return boxIntrinsic(self.next())
    
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
    def __init__(self):
        pass
    
    def next(self):
        return self.nextUShort()
    
    def next(self):
        return boxIntrinsic(self.next())
    
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
    return this.data

class Companion:
    def __init__(self):
        Companion_instance = self
        self.MIN_VALUE = ULong(Long(0, 0))
        self.MAX_VALUE = ULong(Long(-1, -1))
        self.SIZE_BYTES = 8
        self.SIZE_BITS = 64
    
    def _get_MIN_VALUE_(self):
        return self.MIN_VALUE
    
    def _get_MAX_VALUE_(self):
        return self.MAX_VALUE
    
    def _get_SIZE_BYTES_(self):
        return self.SIZE_BYTES
    
    def _get_SIZE_BITS_(self):
        return self.SIZE_BITS
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_4e9c29eb = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_7ff2ad88
    
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
    return ULong__compareTo_impl(tmp, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_65f653f0)

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
    return this.data.hashCode()

def ULong__equals_impl(this, other):
    if jsNot(jsInstanceOf(other, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_31887330
    
    if True:
        pass
    
    tmp0_other_with_cast = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_1aff6f46
    if jsNot(this.data.equals(tmp0_other_with_cast.data)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_b21cbbf
    
    return True

class ULong:
    def __init__(self, data):
        Companion_getInstance()
        self.data = data
    
    def compareTo(self, other):
        return ULong__compareTo_impl(unboxIntrinsic(self), other)
    
    def compareTo(self, other):
        return ULong__compareTo_impl(self, other)
    
    def toString(self):
        return ULong__toString_impl(unboxIntrinsic(self))
    
    def hashCode(self):
        return ULong__hashCode_impl(unboxIntrinsic(self))
    
    def equals(self, other):
        return ULong__equals_impl(unboxIntrinsic(self), other)
    

def toULong():
    return ULong(self)

def toULong():
    return ULong(toLong(self))

def toULong():
    return doubleToULong(self)

def toULong():
    return doubleToULong(kotlin_Double(self))

def toULong():
    return ULong(toLong(self))

def toULong():
    return ULong(toLong(self))

def _get_array_(_this):
    return _this.array

def _set_index_(_this, _set___):
    _this.index = _set___

def _get_index_(_this):
    return _this.index

def _ULongArray___get_storage__impl_(this):
    return this.storage

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
    def __init__(self, array):
        visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_73c6ebec
        self.array = array
        self.index = 0
    
    def hasNext(self):
        return jsLt(self.index, jsArrayLength(self.array))
    
    def nextULong(self):
        tmp
        if jsLt(self.index, jsArrayLength(self.array)):
            tmp0_this = self
            tmp1 = tmp0_this.index
            tmp0_this.index = jsBitOr(jsPlus(tmp1, 1), 0)
            tmp0_toULong_0 = jsArrayGet(self.array, tmp1)
            tmp = ULong(tmp0_toULong_0)
        
        if True:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_473c491
        
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
    tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3ff19826
    if jsNot(jsInstanceOf(tmp, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_10efb806
    
    if True:
        pass
    
    tmp = _ULongArray___get_storage__impl_(this)
    return contains(_ULong___get_data__impl_(element))

def ULongArray__contains_impl(this, element):
    if jsNot(jsInstanceOf(element, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_5132ea9b
    
    if True:
        pass
    
    tmp = unboxIntrinsic(this)
    return ULongArray__contains_impl(tmp, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_7fef7c55)

def ULongArray__containsAll_impl(this, elements):
    tmp_ret_0
    visitDoWhileLoop_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_438fc55e
    return tmp_ret_0

def ULongArray__containsAll_impl(this, elements):
    return ULongArray__containsAll_impl(unboxIntrinsic(this), elements)

def ULongArray__isEmpty_impl(this):
    return jsEqeqeq(jsArrayLength(_ULongArray___get_storage__impl_(this)), 0)

def ULongArray__toString_impl(this):
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_2d0529f2

def ULongArray__hashCode_impl(this):
    return hashCode(this.storage)

def ULongArray__equals_impl(this, other):
    if jsNot(jsInstanceOf(other, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_45c10678
    
    if True:
        pass
    
    tmp0_other_with_cast = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_432005ce
    if jsNot(equals(this.storage, tmp0_other_with_cast.storage)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_4ed90b04
    
    return True

class ULongArray:
    def __init__(self, storage):
        self.storage = storage
    
    def _get_size_(self):
        return _ULongArray___get_size__impl_(unboxIntrinsic(self))
    
    def iterator(self):
        return ULongArray__iterator_impl(unboxIntrinsic(self))
    
    def contains(self, element):
        return ULongArray__contains_impl(unboxIntrinsic(self), element)
    
    def contains(self, element):
        return ULongArray__contains_impl(self, element)
    
    def containsAll(self, elements):
        return ULongArray__containsAll_impl(unboxIntrinsic(self), elements)
    
    def containsAll(self, elements):
        return ULongArray__containsAll_impl(self, elements)
    
    def isEmpty(self):
        return ULongArray__isEmpty_impl(unboxIntrinsic(self))
    
    def toString(self):
        return ULongArray__toString_impl(unboxIntrinsic(self))
    
    def hashCode(self):
        return ULongArray__hashCode_impl(unboxIntrinsic(self))
    
    def equals(self, other):
        return ULongArray__equals_impl(unboxIntrinsic(self), other)
    

class Companion:
    def __init__(self):
        Companion_instance = self
        self.EMPTY = ULongRange(ULong(Long(-1, -1)), ULong(Long(0, 0)))
    
    def _get_EMPTY_(self):
        return self.EMPTY
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_2b0bd16b = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_5bc26351
    
    return Companion_instance

class ULongRange:
    def __init__(self, start, endInclusive):
        Companion_getInstance()
        visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_65013d71
    
    def _get_start_(self):
        return self._get_first_()
    
    def _get_start_(self):
        return boxIntrinsic(self._get_start_())
    
    def _get_endInclusive_(self):
        return self._get_last_()
    
    def _get_endInclusive_(self):
        return boxIntrinsic(self._get_endInclusive_())
    
    def contains(self, value):
        tmp
        tmp0_compareTo_0 = self._get_first_()
        if jsLtEq(ulongCompare(_ULong___get_data__impl_(tmp0_compareTo_0), _ULong___get_data__impl_(value)), 0):
            tmp1_compareTo_0 = self._get_last_()
            tmp = jsLtEq(ulongCompare(_ULong___get_data__impl_(value), _ULong___get_data__impl_(tmp1_compareTo_0)), 0)
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def contains(self, value):
        return self.contains(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4704ad3f)
    
    def isEmpty(self):
        tmp0_compareTo_0 = self._get_first_()
        tmp1_compareTo_0 = self._get_last_()
        return jsGt(ulongCompare(_ULong___get_data__impl_(tmp0_compareTo_0), _ULong___get_data__impl_(tmp1_compareTo_0)), 0)
    
    def equals(self, other):
        tmp
        if jsInstanceOf(other, jsClass()):
            tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_518a9c8a
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def hashCode(self):
        tmp
        if self.isEmpty():
            tmp = -1
        
        if True:
            tmp2_xor_0 = self._get_first_()
            tmp0_shr_0 = self._get_first_()
            tmp1_shr_0 = 32
            tmp3_xor_0 = ULong(_ULong___get_data__impl_(tmp0_shr_0).ushr(tmp1_shr_0))
            tmp4_toInt_0 = ULong(_ULong___get_data__impl_(tmp2_xor_0).xor(_ULong___get_data__impl_(tmp3_xor_0)))
            tmp = imul(31, _ULong___get_data__impl_(tmp4_toInt_0).toInt())
            tmp7_xor_0 = self._get_last_()
            tmp5_shr_0 = self._get_last_()
            tmp6_shr_0 = 32
            tmp8_xor_0 = ULong(_ULong___get_data__impl_(tmp5_shr_0).ushr(tmp6_shr_0))
            tmp9_toInt_0 = ULong(_ULong___get_data__impl_(tmp7_xor_0).xor(_ULong___get_data__impl_(tmp8_xor_0)))
            tmp = jsBitOr(jsPlus(tmp, _ULong___get_data__impl_(tmp9_toInt_0).toInt()), 0)
        
        return tmp
    
    def toString(self):
        return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_33d1d1ef
    
    def _get_first_(self):
        pass
    
    def _get_last_(self):
        pass
    
    def _get_step_(self):
        pass
    
    def iterator(self):
        pass
    

class Companion:
    def __init__(self):
        Companion_instance = self
    
    def fromClosedRange(self, rangeStart, rangeEnd, step):
        return ULongProgression(rangeStart, rangeEnd, step)
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_1b75f094 = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_29a08daf
    
    return Companion_instance

class ULongProgression:
    def __init__(self, start, endInclusive, step):
        Companion_getInstance()
        if step.equals(Long(0, 0)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_17cc72cb
        
        if step.equals(Long(0, -2147483648)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_630a32f8
        
        self.first = start
        self.last = getProgressionLastElement(start, endInclusive, step)
        self.step = step
    
    def _get_first_(self):
        return self.first
    
    def _get_last_(self):
        return self.last
    
    def _get_step_(self):
        return self.step
    
    def iterator(self):
        return ULongProgressionIterator(self.first, self.last, self.step)
    
    def isEmpty(self):
        tmp
        if jsGt(self.step.compareTo(Long(0, 0)), 0):
            tmp0_compareTo_0 = self.first
            tmp1_compareTo_0 = self.last
            tmp = jsGt(ulongCompare(_ULong___get_data__impl_(tmp0_compareTo_0), _ULong___get_data__impl_(tmp1_compareTo_0)), 0)
        
        if True:
            tmp2_compareTo_0 = self.first
            tmp3_compareTo_0 = self.last
            tmp = jsLt(ulongCompare(_ULong___get_data__impl_(tmp2_compareTo_0), _ULong___get_data__impl_(tmp3_compareTo_0)), 0)
        
        return tmp
    
    def equals(self, other):
        tmp
        if jsInstanceOf(other, jsClass()):
            tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_64922e2f
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def hashCode(self):
        tmp
        if self.isEmpty():
            tmp = -1
        
        if True:
            tmp2_xor_0 = self.first
            tmp0_shr_0 = self.first
            tmp1_shr_0 = 32
            tmp3_xor_0 = ULong(_ULong___get_data__impl_(tmp0_shr_0).ushr(tmp1_shr_0))
            tmp4_toInt_0 = ULong(_ULong___get_data__impl_(tmp2_xor_0).xor(_ULong___get_data__impl_(tmp3_xor_0)))
            tmp = imul(31, _ULong___get_data__impl_(tmp4_toInt_0).toInt())
            tmp7_xor_0 = self.last
            tmp5_shr_0 = self.last
            tmp6_shr_0 = 32
            tmp8_xor_0 = ULong(_ULong___get_data__impl_(tmp5_shr_0).ushr(tmp6_shr_0))
            tmp9_toInt_0 = ULong(_ULong___get_data__impl_(tmp7_xor_0).xor(_ULong___get_data__impl_(tmp8_xor_0)))
            tmp = jsBitOr(jsPlus(imul(31, jsBitOr(jsPlus(tmp, _ULong___get_data__impl_(tmp9_toInt_0).toInt()), 0)), self.step.xor(self.step.ushr(32)).toInt()), 0)
        
        return tmp
    
    def toString(self):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2857f172
    

def _get_finalElement_(_this):
    return _this.finalElement

def _set_hasNext_(_this, _set___):
    _this.hasNext = _set___

def _get_hasNext_(_this):
    return _this.hasNext

def _get_step_(_this):
    return _this.step

def _set_next_(_this, _set___):
    _this.next = _set___

def _get_next_(_this):
    return _this.next

class ULongProgressionIterator:
    def __init__(self, first, last, step):
        visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_147203c2
        self.finalElement = last
        tmp = self
        tmp
        if jsGt(step.compareTo(Long(0, 0)), 0):
            tmp = jsLtEq(ulongCompare(_ULong___get_data__impl_(first), _ULong___get_data__impl_(last)), 0)
        
        if True:
            tmp = jsGtEq(ulongCompare(_ULong___get_data__impl_(first), _ULong___get_data__impl_(last)), 0)
        
        tmp.hasNext = tmp
        tmp = self
        tmp.step = ULong(step)
        self.next = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6e8123dd
    
    def hasNext(self):
        return self.hasNext
    
    def nextULong(self):
        value = self.next
        if equals(boxIntrinsic(value), boxIntrinsic(self.finalElement)):
            if jsNot(self.hasNext):
                visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_3e79473d
            
            self.hasNext = False
        
        if True:
            tmp0_this = self
            tmp = tmp0_this
            tmp0_plus_0 = tmp0_this.next
            tmp1_plus_0 = self.step
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
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_36995784
    
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
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_2735a7dc
    
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
    return this.data

class Companion:
    def __init__(self):
        Companion_instance = self
        self.MIN_VALUE = UShort(visitConst_other_Short)
        self.MAX_VALUE = UShort(visitConst_other_Short)
        self.SIZE_BYTES = 2
        self.SIZE_BITS = 16
    
    def _get_MIN_VALUE_(self):
        return self.MIN_VALUE
    
    def _get_MAX_VALUE_(self):
        return self.MAX_VALUE
    
    def _get_SIZE_BYTES_(self):
        return self.SIZE_BYTES
    
    def _get_SIZE_BITS_(self):
        return self.SIZE_BITS
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_69f89cbc = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_ebfa509
    
    return Companion_instance

def UShort__compareTo_impl(this, other):
    tmp = jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535)
    return compareTo(tmp, jsBitAnd(kotlin_Int(_UByte___get_data__impl_(other)), 255))

def UShort__compareTo_impl(this, other):
    tmp = jsBitAnd(kotlin_Int(_UShort___get_data__impl_(this)), 65535)
    return compareTo(tmp, jsBitAnd(kotlin_Int(_UShort___get_data__impl_(other)), 65535))

def UShort__compareTo_impl(this, other):
    tmp = unboxIntrinsic(this)
    return UShort__compareTo_impl(tmp, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4aab6203)

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
    return this.data

def UShort__equals_impl(this, other):
    if jsNot(jsInstanceOf(other, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_3d273300
    
    if True:
        pass
    
    tmp0_other_with_cast = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_e3b9b44
    if jsNot(jsEqeqeq(this.data, tmp0_other_with_cast.data)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_631c6ef4
    
    return True

class UShort:
    def __init__(self, data):
        Companion_getInstance()
        self.data = data
    
    def compareTo(self, other):
        return UShort__compareTo_impl(unboxIntrinsic(self), other)
    
    def compareTo(self, other):
        return UShort__compareTo_impl(self, other)
    
    def toString(self):
        return UShort__toString_impl(unboxIntrinsic(self))
    
    def hashCode(self):
        return UShort__hashCode_impl(unboxIntrinsic(self))
    
    def equals(self, other):
        return UShort__equals_impl(unboxIntrinsic(self), other)
    

def toUShort():
    return UShort(toShort(self))

def toUShort():
    return UShort(self.toShort())

def toUShort():
    return UShort(self)

def _get_array_(_this):
    return _this.array

def _set_index_(_this, _set___):
    _this.index = _set___

def _get_index_(_this):
    return _this.index

def _UShortArray___get_storage__impl_(this):
    return this.storage

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
    def __init__(self, array):
        visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_541d8a9e
        self.array = array
        self.index = 0
    
    def hasNext(self):
        return jsLt(self.index, jsArrayLength(self.array))
    
    def nextUShort(self):
        tmp
        if jsLt(self.index, jsArrayLength(self.array)):
            tmp0_this = self
            tmp1 = tmp0_this.index
            tmp0_this.index = jsBitOr(jsPlus(tmp1, 1), 0)
            tmp0_toUShort_0 = jsArrayGet(self.array, tmp1)
            tmp = UShort(tmp0_toUShort_0)
        
        if True:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_3ce71bbb
        
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
    tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_1c0ed7c1
    if jsNot(jsInstanceOf(tmp, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_396a4dea
    
    if True:
        pass
    
    tmp = _UShortArray___get_storage__impl_(this)
    return contains(_UShort___get_data__impl_(element))

def UShortArray__contains_impl(this, element):
    if jsNot(jsInstanceOf(element, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_5811502e
    
    if True:
        pass
    
    tmp = unboxIntrinsic(this)
    return UShortArray__contains_impl(tmp, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_70329364)

def UShortArray__containsAll_impl(this, elements):
    tmp_ret_0
    visitDoWhileLoop_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_56567e9b
    return tmp_ret_0

def UShortArray__containsAll_impl(this, elements):
    return UShortArray__containsAll_impl(unboxIntrinsic(this), elements)

def UShortArray__isEmpty_impl(this):
    return jsEqeqeq(jsArrayLength(_UShortArray___get_storage__impl_(this)), 0)

def UShortArray__toString_impl(this):
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_4885b386

def UShortArray__hashCode_impl(this):
    return hashCode(this.storage)

def UShortArray__equals_impl(this, other):
    if jsNot(jsInstanceOf(other, jsClass())):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_7786c2e0
    
    if True:
        pass
    
    tmp0_other_with_cast = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4718eb01
    if jsNot(equals(this.storage, tmp0_other_with_cast.storage)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_b22bebc
    
    return True

class UShortArray:
    def __init__(self, storage):
        self.storage = storage
    
    def _get_size_(self):
        return _UShortArray___get_size__impl_(unboxIntrinsic(self))
    
    def iterator(self):
        return UShortArray__iterator_impl(unboxIntrinsic(self))
    
    def contains(self, element):
        return UShortArray__contains_impl(unboxIntrinsic(self), element)
    
    def contains(self, element):
        return UShortArray__contains_impl(self, element)
    
    def containsAll(self, elements):
        return UShortArray__containsAll_impl(unboxIntrinsic(self), elements)
    
    def containsAll(self, elements):
        return UShortArray__containsAll_impl(self, elements)
    
    def isEmpty(self):
        return UShortArray__isEmpty_impl(unboxIntrinsic(self))
    
    def toString(self):
        return UShortArray__toString_impl(unboxIntrinsic(self))
    
    def hashCode(self):
        return UShortArray__hashCode_impl(unboxIntrinsic(self))
    
    def equals(self, other):
        return UShortArray__equals_impl(unboxIntrinsic(self), other)
    

def uintCompare(v1, v2):
    return compareTo(jsBitXor(v1, IntCompanionObject_getInstance().MIN_VALUE), jsBitXor(v2, IntCompanionObject_getInstance().MIN_VALUE))

def uintDivide(v1, v2):
    tmp = toLong(_UInt___get_data__impl_(v1))._and(Long(-1, 0))
    tmp0_toUInt_0 = tmp.div(toLong(_UInt___get_data__impl_(v2))._and(Long(-1, 0)))
    return UInt(tmp0_toUInt_0.toInt())

def uintRemainder(v1, v2):
    tmp = toLong(_UInt___get_data__impl_(v1))._and(Long(-1, 0))
    tmp0_toUInt_0 = tmp.rem(toLong(_UInt___get_data__impl_(v2))._and(Long(-1, 0)))
    return UInt(tmp0_toUInt_0.toInt())

def uintToDouble(v):
    return jsPlus(kotlin_Double(jsBitAnd(v, IntCompanionObject_getInstance().MAX_VALUE)), jsMult(kotlin_Double(jsBitShiftL(jsBitShiftRU(v, 31), 30)), 2))

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
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_639c5ab4
    
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
                if jsLtEq(v, kotlin_Double(IntCompanionObject_getInstance().MAX_VALUE)):
                    tmp2_toUInt_0 = numberToInt(v)
                    tmp = UInt(tmp2_toUInt_0)
                
                if True:
                    if True:
                        tmp3_toUInt_0 = numberToInt(jsMinus(v, IntCompanionObject_getInstance().MAX_VALUE))
                        tmp5_plus_0 = UInt(tmp3_toUInt_0)
                        tmp4_toUInt_0 = IntCompanionObject_getInstance().MAX_VALUE
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
    def __init__(self):
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
    
    def __init__(self):
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
    
    def __init__(self):
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
    
    def __init__(self):
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
    
    def __init__(self):
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
    
    def __init__(self):
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
    
    def __init__(self):
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
    
    def __init__(self):
        pass
    

class Number:
    def __init__(self):
        pass
    
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
    def __init__(self, version):
        self.version = version
    
    def _get_version_(self):
        return self.version
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class Suppress:
    def __init__(self, names):
        self.names = names
    
    def _get_names_(self):
        return self.names
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_ace10f9 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_37013dda = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_21f34cf2 = 0
def values():
    return arrayLiteral(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_1e53dc3b)

def valueOf(value):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_61fbd0a0

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_52a7893a = 0
def DeprecationLevel_initEntries():
    if DeprecationLevel_entriesInitialized:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_1dc0f59d
    
    DeprecationLevel_entriesInitialized = True
    DeprecationLevel_WARNING_instance = DeprecationLevel('WARNING', 0)
    DeprecationLevel_ERROR_instance = DeprecationLevel('ERROR', 1)
    DeprecationLevel_HIDDEN_instance = DeprecationLevel('HIDDEN', 2)

class DeprecationLevel:
    def __init__(self, name, ordinal):
        visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_2203ee34
    
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
    def __init__(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class ParameterName:
    def __init__(self, name):
        self.name = name
    
    def _get_name_(self):
        return self.name
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def Deprecated_init__Init_(message, replaceWith, level, _mask0, _marker, _this):
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 2), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_7df60197
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 4), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_6b00dec8
    
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_10544888
    return _this

def Deprecated_init__Create_(message, replaceWith, level, _mask0, _marker):
    return Deprecated_init__Init_(message, replaceWith, level, _mask0, _marker, Object_create())

class Deprecated:
    def __init__(self, message, replaceWith, level):
        self.message = message
        self.replaceWith = replaceWith
        self.level = level
    
    def _get_message_(self):
        return self.message
    
    def _get_replaceWith_(self):
        return self.replaceWith
    
    def _get_level_(self):
        return self.level
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class ReplaceWith:
    def __init__(self, expression, imports):
        self.expression = expression
        self.imports = imports
    
    def _get_expression_(self):
        return self.expression
    
    def _get_imports_(self):
        return self.imports
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class ExtensionFunctionType:
    def __init__(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class UnsafeVariance:
    def __init__(self):
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
    def __init__(self):
        pass
    
    def next(self):
        return self.nextByte()
    
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
    def __init__(self):
        pass
    
    def next(self):
        return self.nextInt()
    
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
    def __init__(self):
        pass
    
    def next(self):
        return self.nextDouble()
    
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
    def __init__(self):
        pass
    
    def next(self):
        return self.nextFloat()
    
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
    def __init__(self):
        pass
    
    def next(self):
        return self.nextLong()
    
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
    def __init__(self):
        pass
    
    def next(self):
        return self.nextChar()
    
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
    def __init__(self):
        pass
    
    def next(self):
        return self.nextBoolean()
    
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
    def __init__(self):
        pass
    
    def next(self):
        return self.nextShort()
    
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
    return _this.finalElement

def _set_hasNext_(_this, _set___):
    _this.hasNext = _set___

def _get_hasNext_(_this):
    return _this.hasNext

def _set_next_(_this, _set___):
    _this.next = _set___

def _get_next_(_this):
    return _this.next

class IntProgressionIterator:
    def __init__(self, first, last, step):
        visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_bedebe9
        self.step = step
        self.finalElement = last
        self.hasNext = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_609b91b4
        self.next = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_68217ca5
    
    def _get_step_(self):
        return self.step
    
    def hasNext(self):
        return self.hasNext
    
    def nextInt(self):
        value = self.next
        if jsEqeqeq(value, self.finalElement):
            if jsNot(self.hasNext):
                visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_20673498
            
            self.hasNext = False
        
        if True:
            tmp0_this = self
            tmp0_this.next = jsBitOr(jsPlus(tmp0_this.next, self.step), 0)
        
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
    return _this.finalElement

def _set_hasNext_(_this, _set___):
    _this.hasNext = _set___

def _get_hasNext_(_this):
    return _this.hasNext

def _set_next_(_this, _set___):
    _this.next = _set___

def _get_next_(_this):
    return _this.next

class LongProgressionIterator:
    def __init__(self, first, last, step):
        visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_56511eda
        self.step = step
        self.finalElement = last
        self.hasNext = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2228082d
        self.next = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_150ae70c
    
    def _get_step_(self):
        return self.step
    
    def hasNext(self):
        return self.hasNext
    
    def nextLong(self):
        value = self.next
        if value.equals(self.finalElement):
            if jsNot(self.hasNext):
                visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_5eb4b746
            
            self.hasNext = False
        
        if True:
            tmp0_this = self
            tmp0_this.next = tmp0_this.next.plus(self.step)
        
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
    return _this.finalElement

def _set_hasNext_(_this, _set___):
    _this.hasNext = _set___

def _get_hasNext_(_this):
    return _this.hasNext

def _set_next_(_this, _set___):
    _this.next = _set___

def _get_next_(_this):
    return _this.next

class CharProgressionIterator:
    def __init__(self, first, last, step):
        visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_6f5df147
        self.step = step
        self.finalElement = last.toInt()
        self.hasNext = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_b6ae271
        self.next = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4086b547
    
    def _get_step_(self):
        return self.step
    
    def hasNext(self):
        return self.hasNext
    
    def nextChar(self):
        value = self.next
        if jsEqeqeq(value, self.finalElement):
            if jsNot(self.hasNext):
                visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_7f478529
            
            self.hasNext = False
        
        if True:
            tmp0_this = self
            tmp0_this.next = jsBitOr(jsPlus(tmp0_this.next, self.step), 0)
        
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
    def __init__(self):
        Companion_instance = self
    
    def fromClosedRange(self, rangeStart, rangeEnd, step):
        return IntProgression(rangeStart, rangeEnd, step)
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_57a9be7f = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_119a8125
    
    return Companion_instance

class IntProgression:
    def __init__(self, start, endInclusive, step):
        Companion_getInstance()
        if jsEqeqeq(step, 0):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_762deb10
        
        if jsEqeqeq(step, IntCompanionObject_getInstance().MIN_VALUE):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_4679df4b
        
        self.first = start
        self.last = kotlin_Int(getProgressionLastElement(kotlin_Int(start), kotlin_Int(endInclusive), step))
        self.step = step
    
    def _get_first_(self):
        return self.first
    
    def _get_last_(self):
        return self.last
    
    def _get_step_(self):
        return self.step
    
    def iterator(self):
        return IntProgressionIterator(self.first, self.last, self.step)
    
    def isEmpty(self):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_535203b8
    
    def equals(self, other):
        tmp
        if jsInstanceOf(other, jsClass()):
            tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2a4d39fa
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def hashCode(self):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4bbb4b4
    
    def toString(self):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_15b59258
    

class Companion:
    def __init__(self):
        Companion_instance = self
    
    def fromClosedRange(self, rangeStart, rangeEnd, step):
        return LongProgression(rangeStart, rangeEnd, step)
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_41df3497 = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_3e3b081c
    
    return Companion_instance

class LongProgression:
    def __init__(self, start, endInclusive, step):
        Companion_getInstance()
        if step.equals(Long(0, 0)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_6256d908
        
        if step.equals(Long(0, -2147483648)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_292a73f2
        
        self.first = start
        self.last = getProgressionLastElement(start.toLong(), endInclusive.toLong(), step).toLong()
        self.step = step
    
    def _get_first_(self):
        return self.first
    
    def _get_last_(self):
        return self.last
    
    def _get_step_(self):
        return self.step
    
    def iterator(self):
        return LongProgressionIterator(self.first, self.last, self.step)
    
    def isEmpty(self):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_cd7df73
    
    def equals(self, other):
        tmp
        if jsInstanceOf(other, jsClass()):
            tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_63fac644
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def hashCode(self):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_5dfabe82
    
    def toString(self):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3a0d3af1
    

class Companion:
    def __init__(self):
        Companion_instance = self
    
    def fromClosedRange(self, rangeStart, rangeEnd, step):
        return CharProgression(rangeStart, rangeEnd, step)
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_466aee52 = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_3de7a660
    
    return Companion_instance

class CharProgression:
    def __init__(self, start, endInclusive, step):
        Companion_getInstance()
        if jsEqeqeq(step, 0):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_1ee7a438
        
        if jsEqeqeq(step, IntCompanionObject_getInstance().MIN_VALUE):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_d574831
        
        self.first = start
        self.last = numberToChar(getProgressionLastElement(start.toInt(), endInclusive.toInt(), step))
        self.step = step
    
    def _get_first_(self):
        return self.first
    
    def _get_last_(self):
        return self.last
    
    def _get_step_(self):
        return self.step
    
    def iterator(self):
        return CharProgressionIterator(self.first, self.last, self.step)
    
    def isEmpty(self):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_72f1a1a7
    
    def equals(self, other):
        tmp
        if jsInstanceOf(other, jsClass()):
            tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2579d604
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def hashCode(self):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_76ad04a1
    
    def toString(self):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_7e7cb19c
    

class ClosedRange:
    def _get_start_(self):
        pass
    
    def _get_endInclusive_(self):
        pass
    
    def contains(self, value):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_779b12b
    
    def isEmpty(self):
        return jsGt(compareTo(self._get_start_(), self._get_endInclusive_()), 0)
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def __init__(self):
        pass
    

class Companion:
    def __init__(self):
        Companion_instance = self
        self.EMPTY = IntRange(1, 0)
    
    def _get_EMPTY_(self):
        return self.EMPTY
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_48b3a9ed = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_70a8159f
    
    return Companion_instance

class IntRange:
    def __init__(self, start, endInclusive):
        Companion_getInstance()
        visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_5b256ab5
    
    def _get_start_(self):
        return self._get_first_()
    
    def _get_endInclusive_(self):
        return self._get_last_()
    
    def contains(self, value):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_81847c4
    
    def contains(self, value):
        return self.contains(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3006b388)
    
    def isEmpty(self):
        return jsGt(self._get_first_(), self._get_last_())
    
    def equals(self, other):
        tmp
        if jsInstanceOf(other, jsClass()):
            tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_a3ed130
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def hashCode(self):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_7fda0e89
    
    def toString(self):
        return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_e320f5
    
    def _get_first_(self):
        pass
    
    def _get_last_(self):
        pass
    
    def _get_step_(self):
        pass
    
    def iterator(self):
        pass
    

class Companion:
    def __init__(self):
        Companion_instance = self
        self.EMPTY = LongRange(Long(1, 0), Long(0, 0))
    
    def _get_EMPTY_(self):
        return self.EMPTY
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_5c0b05f4 = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_df31866
    
    return Companion_instance

class LongRange:
    def __init__(self, start, endInclusive):
        Companion_getInstance()
        visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_5a90ea5c
    
    def _get_start_(self):
        return self._get_first_()
    
    def _get_endInclusive_(self):
        return self._get_last_()
    
    def contains(self, value):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_40d6c69f
    
    def contains(self, value):
        return self.contains(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_69f7da24)
    
    def isEmpty(self):
        return jsGt(self._get_first_().compareTo(self._get_last_()), 0)
    
    def equals(self, other):
        tmp
        if jsInstanceOf(other, jsClass()):
            tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_36058c6b
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def hashCode(self):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_7a668497
    
    def toString(self):
        return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_41a42c6b
    
    def _get_first_(self):
        pass
    
    def _get_last_(self):
        pass
    
    def _get_step_(self):
        pass
    
    def iterator(self):
        pass
    

class Companion:
    def __init__(self):
        Companion_instance = self
        self.EMPTY = CharRange(Char(1), Char(0))
    
    def _get_EMPTY_(self):
        return self.EMPTY
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_203cab01 = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_7ac71b01
    
    return Companion_instance

class CharRange:
    def __init__(self, start, endInclusive):
        Companion_getInstance()
        visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_19070326
    
    def _get_start_(self):
        return self._get_first_()
    
    def _get_endInclusive_(self):
        return self._get_last_()
    
    def contains(self, value):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_66e6bb8e
    
    def contains(self, value):
        return self.contains(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_bf90cf8)
    
    def isEmpty(self):
        return jsGt(self._get_first_().compareTo(self._get_last_()), 0)
    
    def equals(self, other):
        tmp
        if jsInstanceOf(other, jsClass()):
            tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_cce1aeb
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def hashCode(self):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3f9e1b6
    
    def toString(self):
        return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_29a83a1f
    
    def _get_first_(self):
        pass
    
    def _get_last_(self):
        pass
    
    def _get_step_(self):
        pass
    
    def iterator(self):
        pass
    

class Unit:
    def __init__(self):
        Unit_instance = self
    
    def toString(self):
        return 'kotlin.Unit'
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_2b4ab7 = 0
def Unit_getInstance():
    if jsEqeq(Unit_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_48ea0ab7
    
    return Unit_instance

class Target:
    def __init__(self, allowedTargets):
        self.allowedTargets = allowedTargets
    
    def _get_allowedTargets_(self):
        return self.allowedTargets
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_7b836cf6 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_59412c = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_42f461c5 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_6377ec2a = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_373d86e = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_4969b90d = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_287213ac = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_74b8bc34 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_6915ba65 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_6d30d79b = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_556746e2 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_640f1966 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_208d5110 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_4beac695 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_2455c95c = 0
def values():
    return arrayLiteral(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_6514666f)

def valueOf(value):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_76022ebd

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_385865dd = 0
def AnnotationTarget_initEntries():
    if AnnotationTarget_entriesInitialized:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_6d9ebd88
    
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
    def __init__(self, name, ordinal):
        visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_39785b39
    
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
    def __init__(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def Retention_init__Init_(value, _mask0, _marker, _this):
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 1), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_2793fafa
    
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_6aa70f5b
    return _this

def Retention_init__Create_(value, _mask0, _marker):
    return Retention_init__Init_(value, _mask0, _marker, Object_create())

class Retention:
    def __init__(self, value):
        self.value = value
    
    def _get_value_(self):
        return self.value
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_47893392 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_1c3455e5 = 0
visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_2ed0f3ec = 0
def values():
    return arrayLiteral(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_7db205ba)

def valueOf(value):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6080eac7

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_5d1915d1 = 0
def AnnotationRetention_initEntries():
    if AnnotationRetention_entriesInitialized:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_6caef908
    
    AnnotationRetention_entriesInitialized = True
    AnnotationRetention_SOURCE_instance = AnnotationRetention('SOURCE', 0)
    AnnotationRetention_BINARY_instance = AnnotationRetention('BINARY', 1)
    AnnotationRetention_RUNTIME_instance = AnnotationRetention('RUNTIME', 2)

class AnnotationRetention:
    def __init__(self, name, ordinal):
        visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_6c26f80e
    
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
    def __init__(self):
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
        tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_792484df
    
    if jsLt(step, 0):
        tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6b542f10
    
    if True:
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_23b260ed
    
    return tmp

def getProgressionLastElement(start, end, step):
    tmp
    if jsGt(step.compareTo(Long(0, 0)), 0):
        tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_5ec40569
    
    if jsLt(step.compareTo(Long(0, 0)), 0):
        tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_10af2b91
    
    if True:
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_21a09c5a
    
    return tmp

def differenceModulo(a, b, c):
    return mod(jsBitOr(jsMinus(mod(a, c), mod(b, c)), 0), c)

def differenceModulo(a, b, c):
    return mod(mod(a, c).minus(mod(b, c)), c)

def mod(a, b):
    mod = jsMod(a, b)
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_698b9d17

def mod(a, b):
    mod = a.rem(b)
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_53937f1a

class ByteCompanionObject:
    def __init__(self):
        ByteCompanionObject_instance = self
        self.MIN_VALUE = visitConst_other_Byte
        self.MAX_VALUE = visitConst_other_Byte
        self.SIZE_BYTES = 1
        self.SIZE_BITS = 8
    
    def _get_MIN_VALUE_(self):
        return self.MIN_VALUE
    
    def _get_MAX_VALUE_(self):
        return self.MAX_VALUE
    
    def _get_SIZE_BYTES_(self):
        return self.SIZE_BYTES
    
    def _get_SIZE_BITS_(self):
        return self.SIZE_BITS
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_5346038 = 0
def ByteCompanionObject_getInstance():
    if jsEqeq(ByteCompanionObject_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_3cde655c
    
    return ByteCompanionObject_instance

class ShortCompanionObject:
    def __init__(self):
        ShortCompanionObject_instance = self
        self.MIN_VALUE = visitConst_other_Short
        self.MAX_VALUE = visitConst_other_Short
        self.SIZE_BYTES = 2
        self.SIZE_BITS = 16
    
    def _get_MIN_VALUE_(self):
        return self.MIN_VALUE
    
    def _get_MAX_VALUE_(self):
        return self.MAX_VALUE
    
    def _get_SIZE_BYTES_(self):
        return self.SIZE_BYTES
    
    def _get_SIZE_BITS_(self):
        return self.SIZE_BITS
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_634324c9 = 0
def ShortCompanionObject_getInstance():
    if jsEqeq(ShortCompanionObject_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_7497f142
    
    return ShortCompanionObject_instance

class IntCompanionObject:
    def __init__(self):
        IntCompanionObject_instance = self
        self.MIN_VALUE = -2147483648
        self.MAX_VALUE = 2147483647
        self.SIZE_BYTES = 4
        self.SIZE_BITS = 32
    
    def _get_MIN_VALUE_(self):
        return self.MIN_VALUE
    
    def _get_MAX_VALUE_(self):
        return self.MAX_VALUE
    
    def _get_SIZE_BYTES_(self):
        return self.SIZE_BYTES
    
    def _get_SIZE_BITS_(self):
        return self.SIZE_BITS
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_45c2fa2 = 0
def IntCompanionObject_getInstance():
    if jsEqeq(IntCompanionObject_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_6ea7fdc5
    
    return IntCompanionObject_instance

class FloatCompanionObject:
    def __init__(self):
        FloatCompanionObject_instance = self
        self.MIN_VALUE = visitConst_other_Float
        self.MAX_VALUE = visitConst_other_Float
        self.POSITIVE_INFINITY = visitConst_other_Float
        self.NEGATIVE_INFINITY = visitConst_other_Float
        self.NaN = visitConst_other_Float
        self.SIZE_BYTES = 4
        self.SIZE_BITS = 32
    
    def _get_MIN_VALUE_(self):
        return self.MIN_VALUE
    
    def _get_MAX_VALUE_(self):
        return self.MAX_VALUE
    
    def _get_POSITIVE_INFINITY_(self):
        return self.POSITIVE_INFINITY
    
    def _get_NEGATIVE_INFINITY_(self):
        return self.NEGATIVE_INFINITY
    
    def _get_NaN_(self):
        return self.NaN
    
    def _get_SIZE_BYTES_(self):
        return self.SIZE_BYTES
    
    def _get_SIZE_BITS_(self):
        return self.SIZE_BITS
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_7238fdd6 = 0
def FloatCompanionObject_getInstance():
    if jsEqeq(FloatCompanionObject_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_5eeb6908
    
    return FloatCompanionObject_instance

class DoubleCompanionObject:
    def __init__(self):
        DoubleCompanionObject_instance = self
        self.MIN_VALUE = 4.9E-324
        self.MAX_VALUE = 1.7976931348623157E308
        self.POSITIVE_INFINITY = Infinity
        self.NEGATIVE_INFINITY = -Infinity
        self.NaN = NaN
        self.SIZE_BYTES = 8
        self.SIZE_BITS = 64
    
    def _get_MIN_VALUE_(self):
        return self.MIN_VALUE
    
    def _get_MAX_VALUE_(self):
        return self.MAX_VALUE
    
    def _get_POSITIVE_INFINITY_(self):
        return self.POSITIVE_INFINITY
    
    def _get_NEGATIVE_INFINITY_(self):
        return self.NEGATIVE_INFINITY
    
    def _get_NaN_(self):
        return self.NaN
    
    def _get_SIZE_BYTES_(self):
        return self.SIZE_BYTES
    
    def _get_SIZE_BITS_(self):
        return self.SIZE_BITS
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_7776dee7 = 0
def DoubleCompanionObject_getInstance():
    if jsEqeq(DoubleCompanionObject_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_4b961cb6
    
    return DoubleCompanionObject_instance

class StringCompanionObject:
    def __init__(self):
        StringCompanionObject_instance = self
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_63143b83 = 0
def StringCompanionObject_getInstance():
    if jsEqeq(StringCompanionObject_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_73fa38cb
    
    return StringCompanionObject_instance

class BooleanCompanionObject:
    def __init__(self):
        BooleanCompanionObject_instance = self
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_11f5ab76 = 0
def BooleanCompanionObject_getInstance():
    if jsEqeq(BooleanCompanionObject_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_39edd51c
    
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
    
    def __init__(self):
        pass
    

class JsName:
    def __init__(self, name):
        self.name = name
    
    def _get_name_(self):
        return self.name
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def toTypedArray():
    return copyToArray(self)

def copyToArray(collection):
    tmp
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_17179a7e:
        tmp0_unsafeCast_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_1988e095
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
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_210e971e
    
    return array

def copyToArrayImpl(collection, array):
    if jsLt(jsArrayLength(array), collection._get_size_()):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_3fd96ec8
    
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
    def __init__(self, _elements):
        self._elements = _elements
    
    def invoke(self, it):
        return self._elements.contains(it)
    
    def invoke(self, p1):
        return self.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_53851bb9)
    

class _no_name_provided_:
    def __init__(self, _elements):
        self._elements = _elements
    
    def invoke(self, it):
        return jsNot(self._elements.contains(it))
    
    def invoke(self, p1):
        return self.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_7169c184)
    

class AbstractMutableCollection:
    def __init__(self):
        visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_61ee9672
    
    def add(self, element):
        pass
    
    def remove(self, element):
        self.checkIsMutable()
        iterator = self.iterator()
        while iterator.hasNext():
            if equals(iterator.next(), element):
                iterator.remove()
                return True
            
        
        return False
    
    def addAll(self, elements):
        self.checkIsMutable()
        modified = False
        tmp0_iterator = elements.iterator()
        while tmp0_iterator.hasNext():
            element = tmp0_iterator.next()
            if self.add(element):
                visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_38007ead
            
        
        return modified
    
    def removeAll(self, elements):
        self.checkIsMutable()
        tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_182b9c6f
        return removeAll(_no_name_provided__factory(elements))
    
    def retainAll(self, elements):
        self.checkIsMutable()
        tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_5258833e
        return removeAll(_no_name_provided__factory(elements))
    
    def clear(self):
        self.checkIsMutable()
        iterator = self.iterator()
        while iterator.hasNext():
            iterator.next()
            Unit_getInstance()
            iterator.remove()
        
    
    def toJSON(self):
        return self.toArray()
    
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
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_3f1870bc

def _no_name_provided__factory(_elements):
    i = _no_name_provided_(_elements)
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_b73e7ff

def _get_list_(_this):
    return _this.list

def _get_fromIndex_(_this):
    return _this.fromIndex

def _set__size_(_this, _set___):
    _this._size = _set___

def _get__size_(_this):
    return _this._size

class IteratorImpl:
    def __init__(self, _outer):
        self._this = _outer
        self.index = 0
        self.last = -1
    
    def _set_index_(self, _set___):
        self.index = _set___
    
    def _get_index_(self):
        return self.index
    
    def _set_last_(self, _set___):
        self.last = _set___
    
    def _get_last_(self):
        return self.last
    
    def hasNext(self):
        return jsLt(self.index, self._this._get_size_())
    
    def next(self):
        if jsNot(self.hasNext()):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_4e8e0052
        
        tmp = self
        tmp0_this = self
        tmp1 = tmp0_this.index
        tmp0_this.index = jsBitOr(jsPlus(tmp1, 1), 0)
        tmp.last = tmp1
        return self._this.get(self.last)
    
    def remove(self):
        tmp0_check_0 = jsNot(jsEqeqeq(self.last, -1))
        if jsNot(tmp0_check_0):
            message_1 = 'Call next() or previous() before removing element from the iterator.'
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_55150964
        
        self._this.removeAt(self.last)
        Unit_getInstance()
        self.index = self.last
        self.last = -1
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class ListIteratorImpl:
    def __init__(self, _outer, index):
        self._this = _outer
        visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_77073238
        Companion_getInstance().checkPositionIndex(index, self._this._get_size_())
        self._set_index_(index)
    
    def hasPrevious(self):
        return jsGt(self._get_index_(), 0)
    
    def nextIndex(self):
        return self._get_index_()
    
    def previous(self):
        if jsNot(self.hasPrevious()):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_2296926d
        
        tmp0_this = self
        tmp0_this._set_index_(jsBitOr(jsMinus(tmp0_this._get_index_(), 1), 0))
        self._set_last_(tmp0_this._get_index_())
        return self._this.get(self._get_last_())
    
    def previousIndex(self):
        return jsBitOr(jsMinus(self._get_index_(), 1), 0)
    
    def add(self, element):
        self._this.add(self._get_index_(), element)
        tmp0_this = self
        tmp1 = tmp0_this._get_index_()
        tmp0_this._set_index_(jsBitOr(jsPlus(tmp1, 1), 0))
        Unit_getInstance()
        self._set_last_(-1)
    
    def add(self, element):
        return self.add(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_699d0fba)
    
    def set(self, element):
        tmp0_check_0 = jsNot(jsEqeqeq(self._get_last_(), -1))
        if jsNot(tmp0_check_0):
            message_1 = 'Call next() or previous() before updating element value with the iterator.'
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_1cbd4ced
        
        self._this.set(self._get_last_(), element)
        Unit_getInstance()
    
    def set(self, element):
        return self.set(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2ee98de)
    
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
    def __init__(self, list, fromIndex, toIndex):
        visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_33903444
        self.list = list
        self.fromIndex = fromIndex
        self._size = 0
        Companion_getInstance().checkRangeIndexes(self.fromIndex, toIndex, self.list._get_size_())
        self._size = jsBitOr(jsMinus(toIndex, self.fromIndex), 0)
    
    def add(self, index, element):
        Companion_getInstance().checkPositionIndex(index, self._size)
        self.list.add(jsBitOr(jsPlus(self.fromIndex, index), 0), element)
        tmp0_this = self
        tmp1 = tmp0_this._size
        tmp0_this._size = jsBitOr(jsPlus(tmp1, 1), 0)
        Unit_getInstance()
    
    def get(self, index):
        Companion_getInstance().checkElementIndex(index, self._size)
        return self.list.get(jsBitOr(jsPlus(self.fromIndex, index), 0))
    
    def removeAt(self, index):
        Companion_getInstance().checkElementIndex(index, self._size)
        result = self.list.removeAt(jsBitOr(jsPlus(self.fromIndex, index), 0))
        tmp0_this = self
        tmp1 = tmp0_this._size
        tmp0_this._size = jsBitOr(jsMinus(tmp1, 1), 0)
        Unit_getInstance()
        return result
    
    def set(self, index, element):
        Companion_getInstance().checkElementIndex(index, self._size)
        return self.list.set(jsBitOr(jsPlus(self.fromIndex, index), 0), element)
    
    def _get_size_(self):
        return self._size
    
    def checkIsMutable(self):
        return self.list.checkIsMutable()
    
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
    def __init__(self, _elements):
        self._elements = _elements
    
    def invoke(self, it):
        return self._elements.contains(it)
    
    def invoke(self, p1):
        return self.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_58f0acce)
    

class _no_name_provided_:
    def __init__(self, _elements):
        self._elements = _elements
    
    def invoke(self, it):
        return jsNot(self._elements.contains(it))
    
    def invoke(self, p1):
        return self.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_75388ef2)
    

class AbstractMutableList:
    def __init__(self):
        visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_27a717a7
        self.modCount = 0
    
    def _set_modCount_(self, _set___):
        self.modCount = _set___
    
    def _get_modCount_(self):
        return self.modCount
    
    def add(self, index, element):
        pass
    
    def removeAt(self, index):
        pass
    
    def set(self, index, element):
        pass
    
    def add(self, element):
        self.checkIsMutable()
        self.add(self._get_size_(), element)
        return True
    
    def addAll(self, index, elements):
        self.checkIsMutable()
        _index = index
        changed = False
        tmp0_iterator = elements.iterator()
        while tmp0_iterator.hasNext():
            e = tmp0_iterator.next()
            tmp1 = _index
            _index = jsBitOr(jsPlus(tmp1, 1), 0)
            self.add(tmp1, e)
            changed = True
        
        return changed
    
    def clear(self):
        self.checkIsMutable()
        self.removeRange(0, self._get_size_())
    
    def removeAll(self, elements):
        self.checkIsMutable()
        return removeAll(_no_name_provided__factory(elements))
    
    def retainAll(self, elements):
        self.checkIsMutable()
        return removeAll(_no_name_provided__factory(elements))
    
    def iterator(self):
        return IteratorImpl(self)
    
    def contains(self, element):
        return jsGtEq(self.indexOf(element), 0)
    
    def indexOf(self, element):
        inductionVariable = 0
        last = _get_lastIndex_()
        if jsLtEq(inductionVariable, last):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_6492428e
        
        return -1
    
    def lastIndexOf(self, element):
        inductionVariable = _get_lastIndex_()
        if jsLtEq(0, inductionVariable):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_3d02feb6
        
        return -1
    
    def listIterator(self):
        return self.listIterator(0)
    
    def listIterator(self, index):
        return ListIteratorImpl(self, index)
    
    def subList(self, fromIndex, toIndex):
        return SubList(self, fromIndex, toIndex)
    
    def removeRange(self, fromIndex, toIndex):
        iterator = self.listIterator(fromIndex)
        tmp0_repeat_0 = jsBitOr(jsMinus(toIndex, fromIndex), 0)
        inductionVariable = 0
        if jsLt(inductionVariable, tmp0_repeat_0):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_258b584c
        
    
    def equals(self, other):
        if jsEqeqeq(other, self):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_808f65
        
        if jsNot(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2b1205a7):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_7225f871
        
        if True:
            pass
        
        return Companion_getInstance().orderedEquals(self, kotlin_collections_Collection___(other))
    
    def hashCode(self):
        return Companion_getInstance().orderedHashCode(self)
    
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
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_46014193

def _no_name_provided__factory(_elements):
    i = _no_name_provided_(_elements)
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_e94908c

def _set_array_(_this, _set___):
    _this.array = _set___

def _get_array_(_this):
    return _this.array

def _set_isReadOnly_(_this, _set___):
    _this.isReadOnly = _set___

def _get_isReadOnly_(_this):
    return _this.isReadOnly

def ArrayList_init__Init_(_this):
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_36b3240f
    return _this

def ArrayList_init__Create_():
    return ArrayList_init__Init_(Object_create())

def ArrayList_init__Init_(initialCapacity, _this):
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_12b0b36
    return _this

def ArrayList_init__Create_(initialCapacity):
    return ArrayList_init__Init_(initialCapacity, Object_create())

def ArrayList_init__Init_(initialCapacity, _mask0, _marker, _this):
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 1), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_3bd35bd0
    
    ArrayList_init__Init_(initialCapacity, _this)
    return _this

def ArrayList_init__Create_(initialCapacity, _mask0, _marker):
    return ArrayList_init__Init_(initialCapacity, _mask0, _marker, Object_create())

def ArrayList_init__Init_(elements, _this):
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_19544c36
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
    def __init__(self, array):
        visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_3787eac3
        self.array = array
        self.isReadOnly = False
    
    def build(self):
        self.checkIsMutable()
        self.isReadOnly = True
        return self
    
    def trimToSize(self):
        pass
    
    def ensureCapacity(self, minCapacity):
        pass
    
    def _get_size_(self):
        return jsArrayLength(self.array)
    
    def get(self, index):
        tmp = jsArrayGet(self.array, rangeCheck(self, index))
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_381d7867
    
    def set(self, index, element):
        self.checkIsMutable()
        rangeCheck(self, index)
        Unit_getInstance()
        tmp0_apply_0 = jsArrayGet(self.array, index)
        jsArraySet(self.array, index, element)
        tmp = tmp0_apply_0
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_5c1c44b9
    
    def add(self, element):
        self.checkIsMutable()
        tmp0_asDynamic_0 = self.array
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_165634aa
        tmp0_this = self
        tmp1 = tmp0_this._get_modCount_()
        tmp0_this._set_modCount_(jsBitOr(jsPlus(tmp1, 1), 0))
        Unit_getInstance()
        return True
    
    def add(self, index, element):
        self.checkIsMutable()
        tmp0_asDynamic_0 = self.array
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_6be7a271
        tmp0_this = self
        tmp1 = tmp0_this._get_modCount_()
        tmp0_this._set_modCount_(jsBitOr(jsPlus(tmp1, 1), 0))
        Unit_getInstance()
    
    def addAll(self, elements):
        self.checkIsMutable()
        if elements.isEmpty():
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_4e8036bb
        
        tmp0_this = self
        tmp = tmp0_this
        tmp0_plus_0 = tmp0_this.array
        tmp1_plus_0 = copyToArray(elements)
        tmp.array = kotlin_Array_kotlin_Any__(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_111b6a5a)
        tmp1_this = self
        tmp2 = tmp1_this._get_modCount_()
        tmp1_this._set_modCount_(jsBitOr(jsPlus(tmp2, 1), 0))
        Unit_getInstance()
        return True
    
    def addAll(self, index, elements):
        self.checkIsMutable()
        insertionRangeCheck(self, index)
        Unit_getInstance()
        if jsEqeqeq(index, self._get_size_()):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_6baa673d
        
        if elements.isEmpty():
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_7902a4d7
        
        tmp0_subject = index
        if jsEqeqeq(tmp0_subject, self._get_size_()):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_457f43a2
        
        if jsEqeqeq(tmp0_subject, 0):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_598ffbc8
        
        if True:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_1834b71b
        
        tmp1_this = self
        tmp2 = tmp1_this._get_modCount_()
        tmp1_this._set_modCount_(jsBitOr(jsPlus(tmp2, 1), 0))
        Unit_getInstance()
        return True
    
    def removeAt(self, index):
        self.checkIsMutable()
        rangeCheck(self, index)
        Unit_getInstance()
        tmp0_this = self
        tmp1 = tmp0_this._get_modCount_()
        tmp0_this._set_modCount_(jsBitOr(jsPlus(tmp1, 1), 0))
        Unit_getInstance()
        tmp
        if jsEqeqeq(index, _get_lastIndex_()):
            tmp0_asDynamic_0 = self.array
            tmp = E(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_5811f080)
        
        if True:
            tmp1_asDynamic_0 = self.array
            tmp = E(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_63c6579)
        
        return tmp
    
    def remove(self, element):
        self.checkIsMutable()
        inductionVariable = 0
        last = jsBitOr(jsMinus(jsArrayLength(self.array), 1), 0)
        if jsLtEq(inductionVariable, last):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_7c671bcb
        
        return False
    
    def removeRange(self, fromIndex, toIndex):
        self.checkIsMutable()
        tmp0_this = self
        tmp1 = tmp0_this._get_modCount_()
        tmp0_this._set_modCount_(jsBitOr(jsPlus(tmp1, 1), 0))
        Unit_getInstance()
        tmp0_asDynamic_0 = self.array
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_71b01319
    
    def clear(self):
        self.checkIsMutable()
        tmp = self
        tmp.array = kotlin_Array_kotlin_Any__(js('[]'))
        tmp0_this = self
        tmp1 = tmp0_this._get_modCount_()
        tmp0_this._set_modCount_(jsBitOr(jsPlus(tmp1, 1), 0))
        Unit_getInstance()
    
    def indexOf(self, element):
        return indexOf(element)
    
    def lastIndexOf(self, element):
        return lastIndexOf(element)
    
    def toString(self):
        return arrayToString(self.array)
    
    def toArray(self):
        return kotlin_Array_kotlin_Any__(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_7ae88df1)
    
    def toArray(self):
        return self.toArray()
    
    def checkIsMutable(self):
        if self.isReadOnly:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_557ed49a
        
    
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

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_7308e2d6 = 0
class RandomAccess:
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def __init__(self):
        pass
    

def _set_output_(_set___):
    output = _set___

def _get_output_():
    return output

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_18e4bbec = 0
class BaseOutput:
    def __init__(self):
        pass
    
    def println(self):
        self.print('\n')
    
    def println(self, message):
        self.print(message)
        self.println()
    
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
    def __init__(self, outputStream):
        visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_708378cc
        self.outputStream = outputStream
    
    def _get_outputStream_(self):
        return self.outputStream
    
    def print(self, message):
        messageString = kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_1add226e)
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_30130a31
    
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
    def __init__(self):
        visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_4951c45f
    
    def print(self, message):
        s = kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_1a9d5a73)
        tmp0_nativeLastIndexOf_0 = s
        tmp1_nativeLastIndexOf_0 = '\n'
        tmp2_nativeLastIndexOf_0 = 0
        i = kotlin_Int(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_49ecd74f)
        if jsGtEq(i, 0):
            tmp0_this = self
            tmp = tmp0_this._get_buffer_()
            tmp3_substring_0 = s
            tmp4_substring_0 = 0
            tmp0_this._set_buffer_(jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_4d61d93a)))
            self.flush()
            tmp5_substring_0 = s
            tmp6_substring_0 = jsBitOr(jsPlus(i, 1), 0)
            s = kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_519565a5)
        
        tmp1_this = self
        tmp1_this._set_buffer_(jsPlus(tmp1_this._get_buffer_(), s))
    
    def flush(self):
        _get_console_().log(arrayLiteral(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_42b35632))
        self._set_buffer_('')
    
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
    return kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_370efa14)

class BufferedOutput:
    def __init__(self):
        visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_6c39ba30
        self.buffer = ''
    
    def _set_buffer_(self, _set___):
        self.buffer = _set___
    
    def _get_buffer_(self):
        return self.buffer
    
    def print(self, message):
        tmp0_this = self
        tmp = tmp0_this
        tmp = tmp0_this.buffer
        tmp.buffer = jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_76871b39))
    
    def flush(self):
        self.buffer = ''
    
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
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4d031f38

def _get_EmptyContinuation_():
    return EmptyContinuation

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_1f02ce3 = 0
class _no_name_provided__1:
    def __init__(self, _tmp0_Continuation_0):
        self._tmp0_Continuation_0 = _tmp0_Continuation_0
    
    def _get_context__2(self):
        return self._tmp0_Continuation_0
    
    def _get_context_(self):
        return self._get_context__2()
    
    def resumeWith_3(self, result):
        throwOnFailure()
        tmp = _Result___get_value__impl_(result)
        if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2efb827e:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrTypeOperatorCallImpl_4afbc9bf
        
        if True:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCallImpl_4611a950
        
        return Unit_getInstance()
    
    def resumeWith(self, result):
        return self.resumeWith_3(result)
    
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
    return self

def unsafeCast():
    return T(self)

def unsafeCast():
    return T(self)

class Serializable:
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def __init__(self):
        pass
    

def pow(n):
    return visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl_144cf818.pow(self, kotlin_Double(n))

def isNaN():
    return jsNot(jsEqeqeq(self, self))

def _get_INV_2_26_():
    return INV_2_26

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_3ad142f0 = 0
def _get_INV_2_53_():
    return INV_2_53

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_5a98983b = 0
def INV_2_26_init_():
    tmp0_pow_0 = 2.0
    tmp1_pow_0 = -26
    return visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl_423b3ef5.pow(tmp0_pow_0, kotlin_Double(tmp1_pow_0))

def INV_2_53_init_():
    tmp0_pow_0 = 2.0
    tmp1_pow_0 = -53
    return visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl_4a14227a.pow(tmp0_pow_0, kotlin_Double(tmp1_pow_0))

def _get_js_():
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_aa85268._get_jClass_()

class KCallable:
    def _get_name_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def __init__(self):
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
    
    def __init__(self):
        pass
    

class KClassImpl:
    def __init__(self, jClass):
        self.jClass = jClass
    
    def _get_jClass_(self):
        return self.jClass
    
    def _get_qualifiedName_(self):
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_280b56fb
    
    def equals(self, other):
        tmp
        if jsInstanceOf(other, jsClass()):
            tmp = equals(self._get_jClass_(), kotlin_reflect_js_internal_KClassImpl_out_kotlin_Any_(other)._get_jClass_())
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def hashCode(self):
        tmp0_safe_receiver = self._get_simpleName_()
        tmp1_elvis_lhs = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_31962524
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_662936a
    
    def toString(self):
        return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_15f7a4c2
    
    def _get_simpleName_(self):
        pass
    
    def isInstance(self, value):
        pass
    

def _get_givenSimpleName_(_this):
    return _this.givenSimpleName

def _get_isInstanceFunction_(_this):
    return _this.isInstanceFunction

class PrimitiveKClassImpl:
    def __init__(self, jClass, givenSimpleName, isInstanceFunction):
        visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_4d53dfb7
        self.givenSimpleName = givenSimpleName
        self.isInstanceFunction = isInstanceFunction
    
    def equals(self, other):
        if jsNot(jsInstanceOf(other, jsClass())):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_14fed48e
        
        if True:
            pass
        
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_20fe006e
    
    def _get_simpleName_(self):
        return self.givenSimpleName
    
    def isInstance(self, value):
        return self.isInstanceFunction.invoke(value)
    
    def _get_jClass_(self):
        pass
    
    def _get_qualifiedName_(self):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class NothingKClassImpl:
    def __init__(self):
        NothingKClassImpl_instance = self
        visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_49afaf65
        self.simpleName = 'Nothing'
    
    def _get_simpleName_(self):
        return self.simpleName
    
    def isInstance(self, value):
        return False
    
    def _get_jClass_(self):
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_1ba00c0c
    
    def equals(self, other):
        return jsEqeqeq(other, self)
    
    def hashCode(self):
        return 0
    
    def _get_qualifiedName_(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_76e5f0ea = 0
def NothingKClassImpl_getInstance():
    if jsEqeq(NothingKClassImpl_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_2687bf90
    
    return NothingKClassImpl_instance

class ErrorKClass:
    def __init__(self):
        pass
    
    def _get_simpleName_(self):
        tmp0_error_0 = 'Unknown simpleName for ErrorKClass'
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_1abf7c9d
    
    def _get_qualifiedName_(self):
        tmp0_error_0 = 'Unknown qualifiedName for ErrorKClass'
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_2afb361c
    
    def isInstance(self, value):
        tmp0_error_0 = 'Can\'s check isInstance on ErrorKClass'
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_68c4f321
    
    def equals(self, other):
        return jsEqeqeq(other, self)
    
    def hashCode(self):
        return 0
    
    def toString(self):
        pass
    

class SimpleKClassImpl:
    def __init__(self, jClass):
        visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_9124278
        tmp = self
        tmp0_safe_receiver = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicMemberExpressionImpl_48c5e6fb
        tmp0_unsafeCast_0 = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_39b266b2
        tmp.simpleName = kotlin_Any_(tmp0_unsafeCast_0)
    
    def _get_simpleName_(self):
        return self.simpleName
    
    def isInstance(self, value):
        return jsIsType(value, self._get_jClass_())
    
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
    
    def __init__(self):
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
    
    def __init__(self):
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
    
    def __init__(self):
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
    
    def __init__(self):
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
    
    def __init__(self):
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
    
    def __init__(self):
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
    
    def __init__(self):
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
    
    def __init__(self):
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
    
    def __init__(self):
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
    
    def __init__(self):
        pass
    

def createKType(classifier, arguments, isMarkedNullable):
    return KTypeImpl(classifier, asList(), isMarkedNullable)

def createDynamicKType():
    return DynamicKType_getInstance()

def createKTypeParameter(name, upperBounds, variance):
    tmp0_subject = variance
    kVariance = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_476bf67d
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
    if jsEqeq(self.variance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_59ad1606
    
    return jsPlus(prefixString(), toString())

class _no_name_provided_:
    def __init__(self, this_0):
        self.this_0 = this_0
    
    def invoke(self, it):
        return asString(self.this_0)
    
    def invoke(self, p1):
        return self.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_7ab9d59f)
    

class KTypeImpl:
    def __init__(self, classifier, arguments, isMarkedNullable):
        self.classifier = classifier
        self.arguments = arguments
        self.isMarkedNullable = isMarkedNullable
    
    def _get_classifier_(self):
        return self.classifier
    
    def _get_arguments_(self):
        return self.arguments
    
    def _get_isMarkedNullable_(self):
        return self.isMarkedNullable
    
    def equals(self, other):
        tmp
        tmp
        tmp
        if jsInstanceOf(other, jsClass()):
            tmp = equals(self.classifier, kotlin_reflect_js_internal_KTypeImpl(other).classifier)
        
        if True:
            if True:
                tmp = False
            
        
        if tmp:
            tmp = equals(self.arguments, kotlin_reflect_js_internal_KTypeImpl(other).arguments)
        
        if True:
            if True:
                tmp = False
            
        
        if tmp:
            tmp = jsEqeqeq(self.isMarkedNullable, kotlin_reflect_js_internal_KTypeImpl(other).isMarkedNullable)
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def hashCode(self):
        return jsBitOr(jsPlus(imul(jsBitOr(jsPlus(imul(hashCode(self.classifier), 31), hashCode(self.arguments)), 0), 31), jsBitOr(self.isMarkedNullable, 0)), 0)
    
    def toString(self):
        tmp = self.classifier
        kClass = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_61bfee77
        classifierName = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_60880394
        tmp
        if self.arguments.isEmpty():
            tmp = ''
        
        if True:
            tmp = joinToString_default(', ', '<', '>', 0, None, _no_name_provided__factory(self), 24, None)
        
        args = tmp
        nullable = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4eb7ff99
        return jsPlus(plus(args), nullable)
    

def prefixString():
    tmp0_subject = self
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
    def __init__(self):
        DynamicKType_instance = self
        self.classifier = None
        self.arguments = emptyList()
        self.isMarkedNullable = False
    
    def _get_classifier_(self):
        return self.classifier
    
    def _get_arguments_(self):
        return self.arguments
    
    def _get_isMarkedNullable_(self):
        return self.isMarkedNullable
    
    def toString(self):
        return 'dynamic'
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_17b83c7e = 0
def DynamicKType_getInstance():
    if jsEqeq(DynamicKType_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_6d4714bb
    
    return DynamicKType_instance

def _no_name_provided__factory(this_0):
    i = _no_name_provided_(this_0)
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_797168d9

class KTypeParameterImpl:
    def __init__(self, name, upperBounds, variance, isReified):
        self.name = name
        self.upperBounds = upperBounds
        self.variance = variance
        self.isReified = isReified
    
    def _get_name_(self):
        return self.name
    
    def _get_upperBounds_(self):
        return self.upperBounds
    
    def _get_variance_(self):
        return self.variance
    
    def _get_isReified_(self):
        return self.isReified
    
    def toString(self):
        return self.name
    
    def component1(self):
        return self.name
    
    def component2(self):
        return self.upperBounds
    
    def component3(self):
        return self.variance
    
    def component4(self):
        return self.isReified
    
    def copy(self, name, upperBounds, variance, isReified):
        return KTypeParameterImpl(name, upperBounds, variance, isReified)
    
    def copy_default(self, name, upperBounds, variance, isReified, _mask0, _handler):
        if jsNot(jsEqeqeq(jsBitAnd(_mask0, 1), 0)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_bc8921c
        
        if jsNot(jsEqeqeq(jsBitAnd(_mask0, 2), 0)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_a547191
        
        if jsNot(jsEqeqeq(jsBitAnd(_mask0, 4), 0)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_7e8011e2
        
        if jsNot(jsEqeqeq(jsBitAnd(_mask0, 8), 0)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_6eb5f95d
        
        return self.copy(kotlin_String(name), kotlin_collections_List_kotlin_reflect_KType_(upperBounds), kotlin_reflect_KVariance(variance), isReified)
    
    def hashCode(self):
        result = getStringHashCode(self.name)
        result = jsBitOr(jsPlus(imul(result, 31), hashCode(self.upperBounds)), 0)
        result = jsBitOr(jsPlus(imul(result, 31), self.variance.hashCode()), 0)
        result = jsBitOr(jsPlus(imul(result, 31), jsBitOr(self.isReified, 0)), 0)
        return result
    
    def equals(self, other):
        if jsEqeqeq(self, other):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_58477355
        
        if jsNot(jsInstanceOf(other, jsClass())):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_d69fd7a
        
        if True:
            pass
        
        tmp0_other_with_cast = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4415b9fa
        if jsNot(jsEqeqeq(self.name, tmp0_other_with_cast.name)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_7c5a7f
        
        if jsNot(equals(self.upperBounds, tmp0_other_with_cast.upperBounds)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_453c10c2
        
        if jsNot(self.variance.equals(tmp0_other_with_cast.variance)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_24a38ef3
        
        if jsNot(jsEqeqeq(self.isReified, tmp0_other_with_cast.isReified)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_347c7b
        
        return True
    

def _get_functionClasses_():
    return functionClasses

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_aad1270 = 0
class _no_name_provided_:
    def __init__(self):
        pass
    
    def invoke(self, it):
        return isObject(it)
    
    def invoke(self, p1):
        return self.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6e520c9a)
    

class _no_name_provided_:
    def __init__(self):
        pass
    
    def invoke(self, it):
        return isNumber(it)
    
    def invoke(self, p1):
        return self.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_27574ba9)
    

class _no_name_provided_:
    def __init__(self):
        pass
    
    def invoke(self, it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6d0c8cd0
    
    def invoke(self, p1):
        return self.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4509f40f)
    

class _no_name_provided_:
    def __init__(self):
        pass
    
    def invoke(self, it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_65a9e8d7
    
    def invoke(self, p1):
        return self.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_475add19)
    

class _no_name_provided_:
    def __init__(self):
        pass
    
    def invoke(self, it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_d5fd167
    
    def invoke(self, p1):
        return self.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2b35e309)
    

class _no_name_provided_:
    def __init__(self):
        pass
    
    def invoke(self, it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_5ed5ac49
    
    def invoke(self, p1):
        return self.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3e127718)
    

class _no_name_provided_:
    def __init__(self):
        pass
    
    def invoke(self, it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_61db65ae
    
    def invoke(self, p1):
        return self.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3a9d395a)
    

class _no_name_provided_:
    def __init__(self):
        pass
    
    def invoke(self, it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_70c3b62b
    
    def invoke(self, p1):
        return self.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_79703b86)
    

class _no_name_provided_:
    def __init__(self):
        pass
    
    def invoke(self, it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2c69eec5
    
    def invoke(self, p1):
        return self.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_352a4317)
    

class _no_name_provided_:
    def __init__(self):
        pass
    
    def invoke(self, it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6fac8b24
    
    def invoke(self, p1):
        return self.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_27cde156)
    

class _no_name_provided_:
    def __init__(self):
        pass
    
    def invoke(self, it):
        return jsInstanceOf(it, jsClass())
    
    def invoke(self, p1):
        return self.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2b55799f)
    

class _no_name_provided_:
    def __init__(self):
        pass
    
    def invoke(self, it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_291be813
    
    def invoke(self, p1):
        return self.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_449e0693)
    

class _no_name_provided_:
    def __init__(self):
        pass
    
    def invoke(self, it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6c56e004
    
    def invoke(self, p1):
        return self.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3aa6fef3)
    

class _no_name_provided_:
    def __init__(self):
        pass
    
    def invoke(self, it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_452811e3
    
    def invoke(self, p1):
        return self.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_59b47d06)
    

class _no_name_provided_:
    def __init__(self):
        pass
    
    def invoke(self, it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_1daf016d
    
    def invoke(self, p1):
        return self.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_5c32f8af)
    

class _no_name_provided_:
    def __init__(self):
        pass
    
    def invoke(self, it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6160ae57
    
    def invoke(self, p1):
        return self.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_71ec5154)
    

class _no_name_provided_:
    def __init__(self):
        pass
    
    def invoke(self, it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3a5aa359
    
    def invoke(self, p1):
        return self.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_66893cd4)
    

class _no_name_provided_:
    def __init__(self):
        pass
    
    def invoke(self, it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_c77f6b0
    
    def invoke(self, p1):
        return self.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3400f5aa)
    

class _no_name_provided_:
    def __init__(self):
        pass
    
    def invoke(self, it):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4608590d
    
    def invoke(self, p1):
        return self.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_1441dc49)
    

class _no_name_provided_:
    def __init__(self, _arity):
        self._arity = _arity
    
    def invoke(self, it):
        tmp
        if jsEqeqeq(jsTypeOf(it), 'function'):
            tmp = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_7809027c
        
        if True:
            tmp = False
        
        return tmp
    
    def invoke(self, p1):
        return self.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_51ddc08e)
    

class PrimitiveClasses:
    def __init__(self):
        PrimitiveClasses_instance = self
        tmp = self
        tmp0_unsafeCast_0 = js('Object')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.anyClass = PrimitiveKClassImpl(tmp, 'Any', _no_name_provided__factory())
        tmp = self
        tmp0_unsafeCast_0 = js('Number')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.numberClass = PrimitiveKClassImpl(tmp, 'Number', _no_name_provided__factory())
        self.nothingClass = NothingKClassImpl_getInstance()
        tmp = self
        tmp0_unsafeCast_0 = js('Boolean')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.booleanClass = PrimitiveKClassImpl(tmp, 'Boolean', _no_name_provided__factory())
        tmp = self
        tmp0_unsafeCast_0 = js('Number')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.byteClass = PrimitiveKClassImpl(tmp, 'Byte', _no_name_provided__factory())
        tmp = self
        tmp0_unsafeCast_0 = js('Number')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.shortClass = PrimitiveKClassImpl(tmp, 'Short', _no_name_provided__factory())
        tmp = self
        tmp0_unsafeCast_0 = js('Number')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.intClass = PrimitiveKClassImpl(tmp, 'Int', _no_name_provided__factory())
        tmp = self
        tmp0_unsafeCast_0 = js('Number')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.floatClass = PrimitiveKClassImpl(tmp, 'Float', _no_name_provided__factory())
        tmp = self
        tmp0_unsafeCast_0 = js('Number')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.doubleClass = PrimitiveKClassImpl(tmp, 'Double', _no_name_provided__factory())
        tmp = self
        tmp0_unsafeCast_0 = js('Array')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.arrayClass = PrimitiveKClassImpl(tmp, 'Array', _no_name_provided__factory())
        tmp = self
        tmp0_unsafeCast_0 = js('String')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.stringClass = PrimitiveKClassImpl(tmp, 'String', _no_name_provided__factory())
        tmp = self
        tmp0_unsafeCast_0 = js('Error')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.throwableClass = PrimitiveKClassImpl(tmp, 'Throwable', _no_name_provided__factory())
        tmp = self
        tmp0_unsafeCast_0 = js('Array')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.booleanArrayClass = PrimitiveKClassImpl(tmp, 'BooleanArray', _no_name_provided__factory())
        tmp = self
        tmp0_unsafeCast_0 = js('Uint16Array')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.charArrayClass = PrimitiveKClassImpl(tmp, 'CharArray', _no_name_provided__factory())
        tmp = self
        tmp0_unsafeCast_0 = js('Int8Array')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.byteArrayClass = PrimitiveKClassImpl(tmp, 'ByteArray', _no_name_provided__factory())
        tmp = self
        tmp0_unsafeCast_0 = js('Int16Array')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.shortArrayClass = PrimitiveKClassImpl(tmp, 'ShortArray', _no_name_provided__factory())
        tmp = self
        tmp0_unsafeCast_0 = js('Int32Array')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.intArrayClass = PrimitiveKClassImpl(tmp, 'IntArray', _no_name_provided__factory())
        tmp = self
        tmp0_unsafeCast_0 = js('Array')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.longArrayClass = PrimitiveKClassImpl(tmp, 'LongArray', _no_name_provided__factory())
        tmp = self
        tmp0_unsafeCast_0 = js('Float32Array')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.floatArrayClass = PrimitiveKClassImpl(tmp, 'FloatArray', _no_name_provided__factory())
        tmp = self
        tmp0_unsafeCast_0 = js('Float64Array')
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
        tmp.doubleArrayClass = PrimitiveKClassImpl(tmp, 'DoubleArray', _no_name_provided__factory())
    
    def _get_anyClass_(self):
        return self.anyClass
    
    def _get_numberClass_(self):
        return self.numberClass
    
    def _get_nothingClass_(self):
        return self.nothingClass
    
    def _get_booleanClass_(self):
        return self.booleanClass
    
    def _get_byteClass_(self):
        return self.byteClass
    
    def _get_shortClass_(self):
        return self.shortClass
    
    def _get_intClass_(self):
        return self.intClass
    
    def _get_floatClass_(self):
        return self.floatClass
    
    def _get_doubleClass_(self):
        return self.doubleClass
    
    def _get_arrayClass_(self):
        return self.arrayClass
    
    def _get_stringClass_(self):
        return self.stringClass
    
    def _get_throwableClass_(self):
        return self.throwableClass
    
    def _get_booleanArrayClass_(self):
        return self.booleanArrayClass
    
    def _get_charArrayClass_(self):
        return self.charArrayClass
    
    def _get_byteArrayClass_(self):
        return self.byteArrayClass
    
    def _get_shortArrayClass_(self):
        return self.shortArrayClass
    
    def _get_intArrayClass_(self):
        return self.intArrayClass
    
    def _get_longArrayClass_(self):
        return self.longArrayClass
    
    def _get_floatArrayClass_(self):
        return self.floatArrayClass
    
    def _get_doubleArrayClass_(self):
        return self.doubleArrayClass
    
    def functionClass(self, arity):
        tmp0_elvis_lhs = jsArrayGet(functionClasses, arity)
        tmp
        if jsEqeq(tmp0_elvis_lhs, None):
            tmp0_unsafeCast_0_3 = js('Function')
            tmp = kotlin_Any_(tmp0_unsafeCast_0_3)
            tmp = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_44ebf052
            result_2 = PrimitiveKClassImpl(tmp, tmp, _no_name_provided__factory(arity))
            tmp1_asDynamic_0_5 = functionClasses
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_198f92c5
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
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_7d60ab = 0
def PrimitiveClasses_getInstance():
    if jsEqeq(PrimitiveClasses_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_5c74f377
    
    return PrimitiveClasses_instance

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_4b66a923

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_2c021a0b

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_5371083b

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_36dc3fae

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_2bd20f96

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_2754e467

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_34ee9000

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_1cc784c9

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_2f1e14cf

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_295af3a1

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_279b5232

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_57daa852

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_2655bb88

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_637bae77

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_4ae19d45

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_6025a000

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_69d2fc03

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_23ea8293

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_68548f59

def _no_name_provided__factory(_arity):
    i = _no_name_provided_(_arity)
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_55acad46

def functionClasses_init_():
    tmp0_arrayOfNulls_0 = 0
    return fillArrayVal(Array(tmp0_arrayOfNulls_0), None)

def getKClass(jClass):
    tmp
    if kotlin_Boolean(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_655e024):
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
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_6d68257
    
    metadata = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicMemberExpressionImpl_4a83740e
    tmp
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_6faa24:
        tmp
        if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_3a973b5e:
            kClass = SimpleKClassImpl(jClass)
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_1c0455c4
            tmp = kClass
        
        if True:
            tmp = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicMemberExpressionImpl_9918487
        
        tmp = kotlin_reflect_KClass_T_(tmp)
    
    if True:
        tmp = SimpleKClassImpl(jClass)
    
    return tmp

def getKClassFromExpression(e):
    tmp0_subject = jsTypeOf(e)
    tmp
    if jsEqeqeq(tmp0_subject, 'string'):
        tmp = PrimitiveClasses_getInstance().stringClass
    
    if jsEqeqeq(tmp0_subject, 'number'):
        tmp
        tmp0_asDynamic_0 = jsBitwiseOr(e, 0)
        if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_6e1e9a10:
            tmp = PrimitiveClasses_getInstance().intClass
        
        if True:
            if True:
                tmp = PrimitiveClasses_getInstance().doubleClass
            
        
        tmp = tmp
    
    if jsEqeqeq(tmp0_subject, 'boolean'):
        tmp = PrimitiveClasses_getInstance().booleanClass
    
    if jsEqeqeq(tmp0_subject, 'function'):
        tmp = PrimitiveClasses_getInstance()
        tmp = tmp.functionClass(kotlin_Int(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicMemberExpressionImpl_7b14e7dc))
    
    if True:
        tmp
        if isBooleanArray(e):
            tmp = PrimitiveClasses_getInstance().booleanArrayClass
        
        if True:
            if isCharArray(e):
                tmp = PrimitiveClasses_getInstance().charArrayClass
            
            if True:
                if isByteArray(e):
                    tmp = PrimitiveClasses_getInstance().byteArrayClass
                
                if True:
                    if isShortArray(e):
                        tmp = PrimitiveClasses_getInstance().shortArrayClass
                    
                    if True:
                        if isIntArray(e):
                            tmp = PrimitiveClasses_getInstance().intArrayClass
                        
                        if True:
                            if isLongArray(e):
                                tmp = PrimitiveClasses_getInstance().longArrayClass
                            
                            if True:
                                if isFloatArray(e):
                                    tmp = PrimitiveClasses_getInstance().floatArrayClass
                                
                                if True:
                                    if isDoubleArray(e):
                                        tmp = PrimitiveClasses_getInstance().doubleArrayClass
                                    
                                    if True:
                                        if isInterface(e, jsClass()):
                                            tmp = getKClass(jsClass())
                                        
                                        if True:
                                            if isArray(e):
                                                tmp = PrimitiveClasses_getInstance().arrayClass
                                            
                                            if True:
                                                if True:
                                                    constructor = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicMemberExpressionImpl_13088030
                                                    tmp
                                                    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_334d96af:
                                                        tmp = PrimitiveClasses_getInstance().anyClass
                                                    
                                                    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_298154d4:
                                                        tmp = PrimitiveClasses_getInstance().throwableClass
                                                    
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
    
    def __init__(self):
        pass
    

def StringBuilder_init__Init_(capacity, _this):
    StringBuilder_init__Init_(_this)
    return _this

def StringBuilder_init__Create_(capacity):
    return StringBuilder_init__Init_(capacity, Object_create())

def StringBuilder_init__Init_(content, _this):
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_3a35e669
    return _this

def StringBuilder_init__Create_(content):
    return StringBuilder_init__Init_(content, Object_create())

def StringBuilder_init__Init_(_this):
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_2c861fc2
    return _this

def StringBuilder_init__Create_():
    return StringBuilder_init__Init_(Object_create())

def _set_string_(_this, _set___):
    _this.string = _set___

def _get_string_(_this):
    return _this.string

def checkReplaceRange(_this, startIndex, endIndex, length):
    if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_46f89863:
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_3ec40a18
    
    if jsGt(startIndex, endIndex):
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_7b09274
    

class StringBuilder:
    def __init__(self, content):
        self.string = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_5f3e12fc
    
    def _get_length_(self):
        tmp0_asDynamic_0 = self.string
        return kotlin_Int(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicMemberExpressionImpl_5869f15f)
    
    def get(self, index):
        tmp0_getOrElse_0 = self.string
        tmp
        if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_db6183a:
            tmp = charSequenceGet(tmp0_getOrElse_0, index)
        
        if True:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_aff6d3f
        
        return tmp
    
    def subSequence(self, startIndex, endIndex):
        tmp0_substring_0 = self.string
        return kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_7b84b4fb)
    
    def append(self, value):
        tmp0_this = self
        tmp0_this.string = jsPlus(tmp0_this.string, value)
        return self
    
    def append(self, value):
        tmp0_this = self
        tmp0_this.string = jsPlus(tmp0_this.string, toString())
        return self
    
    def append(self, value, startIndex, endIndex):
        tmp0_elvis_lhs = value
        return self.appendRange(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_14269e0, startIndex, endIndex)
    
    def reverse(self):
        reversed = ''
        index = jsBitOr(jsMinus(jsArrayLength(self.string), 1), 0)
        while jsGtEq(index, 0):
            tmp = self.string
            tmp0 = index
            index = jsBitOr(jsMinus(tmp0, 1), 0)
            low = charSequenceGet(tmp, tmp0)
            if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_582a1e4e:
                tmp = self.string
                tmp1 = index
                index = jsBitOr(jsMinus(tmp1, 1), 0)
                high = charSequenceGet(tmp, tmp1)
                if isHighSurrogate():
                    reversed = jsPlus(jsPlus(reversed, high), low)
                
                if True:
                    reversed = jsPlus(jsPlus(reversed, low), high)
                
            
            if True:
                reversed = jsPlus(reversed, low)
            
        
        self.string = reversed
        return self
    
    def append(self, value):
        tmp0_this = self
        tmp0_this.string = jsPlus(tmp0_this.string, toString())
        return self
    
    def append(self, value):
        tmp0_this = self
        tmp0_this.string = jsPlus(tmp0_this.string, value)
        return self
    
    def append(self, value):
        tmp0_this = self
        tmp0_this.string = jsPlus(tmp0_this.string, concatToString())
        return self
    
    def append(self, value):
        return self.append(value)
    
    def append(self, value):
        tmp0_this = self
        tmp = tmp0_this
        tmp = tmp0_this.string
        tmp1_elvis_lhs = value
        tmp.string = jsPlus(tmp, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_51d15a98)
        return self
    
    def capacity(self):
        return self._get_length_()
    
    def ensureCapacity(self, minimumCapacity):
        pass
    
    def indexOf(self, string):
        tmp0_asDynamic_0 = self.string
        return kotlin_Int(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_5cf4c93)
    
    def indexOf(self, string, startIndex):
        tmp0_asDynamic_0 = self.string
        return kotlin_Int(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_1c7159d5)
    
    def lastIndexOf(self, string):
        tmp0_asDynamic_0 = self.string
        return kotlin_Int(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_320bfc61)
    
    def lastIndexOf(self, string, startIndex):
        tmp
        if jsEqeqeq(charSequenceLength(string), 0):
            tmp = jsLt(startIndex, 0)
        
        if True:
            if True:
                tmp = False
            
        
        if tmp:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_44f433db
        
        if True:
            pass
        
        tmp0_asDynamic_0 = self.string
        return kotlin_Int(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_362d91ef)
    
    def insert(self, index, value):
        Companion_getInstance().checkPositionIndex(index, self._get_length_())
        tmp = self
        tmp0_substring_0 = self.string
        tmp1_substring_0 = 0
        tmp = jsPlus(kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_24af2901), value)
        tmp2_substring_0 = self.string
        tmp.string = jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_552b5799))
        return self
    
    def insert(self, index, value):
        Companion_getInstance().checkPositionIndex(index, self._get_length_())
        tmp = self
        tmp0_substring_0 = self.string
        tmp1_substring_0 = 0
        tmp = jsPlus(kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_cf2662b), value)
        tmp2_substring_0 = self.string
        tmp.string = jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_37548587))
        return self
    
    def insert(self, index, value):
        Companion_getInstance().checkPositionIndex(index, self._get_length_())
        tmp = self
        tmp0_substring_0 = self.string
        tmp1_substring_0 = 0
        tmp = jsPlus(kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_5cb8009e), concatToString())
        tmp2_substring_0 = self.string
        tmp.string = jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_5a7e245e))
        return self
    
    def insert(self, index, value):
        Companion_getInstance().checkPositionIndex(index, self._get_length_())
        tmp = self
        tmp0_substring_0 = self.string
        tmp1_substring_0 = 0
        tmp = jsPlus(kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_6a754f89), toString())
        tmp2_substring_0 = self.string
        tmp.string = jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_507099cc))
        return self
    
    def insert(self, index, value):
        Companion_getInstance().checkPositionIndex(index, self._get_length_())
        tmp = self
        tmp0_substring_0 = self.string
        tmp1_substring_0 = 0
        tmp = jsPlus(kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_1c45c8ad), toString())
        tmp2_substring_0 = self.string
        tmp.string = jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_7a1be5d6))
        return self
    
    def insert(self, index, value):
        return self.insert(index, value)
    
    def insert(self, index, value):
        Companion_getInstance().checkPositionIndex(index, self._get_length_())
        tmp0_elvis_lhs = value
        toInsert = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_7544c962
        tmp = self
        tmp0_substring_0 = self.string
        tmp1_substring_0 = 0
        tmp = jsPlus(kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_d33be88), toInsert)
        tmp2_substring_0 = self.string
        tmp.string = jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_6ac5fdb))
        return self
    
    def setLength(self, newLength):
        if jsLt(newLength, 0):
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_411bed55
        
        if jsLtEq(newLength, self._get_length_()):
            tmp = self
            tmp0_substring_0 = self.string
            tmp1_substring_0 = 0
            tmp.string = kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_165ed70d)
        
        if True:
            inductionVariable = self._get_length_()
            if jsLt(inductionVariable, newLength):
                visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_4f3ea60d
            
        
    
    def substring(self, startIndex):
        Companion_getInstance().checkPositionIndex(startIndex, self._get_length_())
        tmp0_substring_0 = self.string
        return kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_59687397)
    
    def substring(self, startIndex, endIndex):
        Companion_getInstance().checkBoundsIndexes(startIndex, endIndex, self._get_length_())
        tmp0_substring_0 = self.string
        return kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_7bea6d16)
    
    def trimToSize(self):
        pass
    
    def toString(self):
        return self.string
    
    def clear(self):
        self.string = ''
        return self
    
    def set(self, index, value):
        Companion_getInstance().checkElementIndex(index, self._get_length_())
        tmp = self
        tmp0_substring_0 = self.string
        tmp1_substring_0 = 0
        tmp = jsPlus(kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_153d35f3), value)
        tmp2_substring_0 = self.string
        tmp3_substring_0 = jsBitOr(jsPlus(index, 1), 0)
        tmp.string = jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_6634f211))
    
    def setRange(self, startIndex, endIndex, value):
        checkReplaceRange(self, startIndex, endIndex, self._get_length_())
        tmp = self
        tmp0_substring_0 = self.string
        tmp1_substring_0 = 0
        tmp = jsPlus(kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_8b1263c), value)
        tmp2_substring_0 = self.string
        tmp.string = jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_3951efe0))
        return self
    
    def deleteAt(self, index):
        Companion_getInstance().checkElementIndex(index, self._get_length_())
        tmp = self
        tmp0_substring_0 = self.string
        tmp1_substring_0 = 0
        tmp = kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_47211e6e)
        tmp2_substring_0 = self.string
        tmp3_substring_0 = jsBitOr(jsPlus(index, 1), 0)
        tmp.string = jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_6d1fc55))
        return self
    
    def deleteRange(self, startIndex, endIndex):
        checkReplaceRange(self, startIndex, endIndex, self._get_length_())
        tmp = self
        tmp0_substring_0 = self.string
        tmp1_substring_0 = 0
        tmp = kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_14145f2b)
        tmp2_substring_0 = self.string
        tmp.string = jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_3db1ebbb))
        return self
    
    def toCharArray(self, destination, destinationOffset, startIndex, endIndex):
        Companion_getInstance().checkBoundsIndexes(startIndex, endIndex, self._get_length_())
        Companion_getInstance().checkBoundsIndexes(destinationOffset, jsBitOr(jsMinus(jsBitOr(jsPlus(destinationOffset, endIndex), 0), startIndex), 0), jsArrayLength(destination))
        dstIndex = destinationOffset
        inductionVariable = startIndex
        if jsLt(inductionVariable, endIndex):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_da3cab
        
    
    def toCharArray_default(self, destination, destinationOffset, startIndex, endIndex, _mask0, _handler):
        if jsNot(jsEqeqeq(jsBitAnd(_mask0, 2), 0)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_4c2373c3
        
        if jsNot(jsEqeqeq(jsBitAnd(_mask0, 4), 0)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_56255ee4
        
        if jsNot(jsEqeqeq(jsBitAnd(_mask0, 8), 0)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_281a39d8
        
        return self.toCharArray(destination, destinationOffset, startIndex, endIndex)
    
    def appendRange(self, value, startIndex, endIndex):
        tmp0_this = self
        tmp0_this.string = jsPlus(tmp0_this.string, concatToString(startIndex, endIndex))
        return self
    
    def appendRange(self, value, startIndex, endIndex):
        stringCsq = toString(value)
        Companion_getInstance().checkBoundsIndexes(startIndex, endIndex, jsArrayLength(stringCsq))
        tmp0_this = self
        tmp = tmp0_this
        tmp = tmp0_this.string
        tmp.string = jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_765eb017))
        return self
    
    def insertRange(self, index, value, startIndex, endIndex):
        Companion_getInstance().checkPositionIndex(index, self._get_length_())
        tmp = self
        tmp0_substring_0 = self.string
        tmp1_substring_0 = 0
        tmp = jsPlus(kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_280005ed), concatToString(startIndex, endIndex))
        tmp2_substring_0 = self.string
        tmp.string = jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_64eda459))
        return self
    
    def insertRange(self, index, value, startIndex, endIndex):
        Companion_getInstance().checkPositionIndex(index, self._get_length_())
        stringCsq = toString(value)
        Companion_getInstance().checkBoundsIndexes(startIndex, endIndex, jsArrayLength(stringCsq))
        tmp = self
        tmp0_substring_0 = self.string
        tmp1_substring_0 = 0
        tmp = kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_6ee59636)
        tmp = jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_38026edf))
        tmp2_substring_0 = self.string
        tmp.string = jsPlus(tmp, kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_7783661c))
        return self
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    

def isLowSurrogate():
    containsLower = Char(56320)
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_17937b11

def isHighSurrogate():
    containsLower = Char(55296)
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3ea44e17

def checkRadix(radix):
    if jsNot(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_731d34d):
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_5d6e77a4
    
    return radix

def _get_STRING_CASE_INSENSITIVE_ORDER_():
    return STRING_CASE_INSENSITIVE_ORDER

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_27c68ccb = 0
def nativeLastIndexOf(str, fromIndex):
    return kotlin_Int(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_571ae6d5)

def substring(startIndex, endIndex):
    return kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_4a0ebb10)

def substring(startIndex):
    return kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_88dfbc0)

def compareTo(other, ignoreCase):
    if ignoreCase:
        n1 = jsArrayLength(self)
        n2 = jsArrayLength(other)
        min = visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl_ccf49f.min(int32ArrayOf(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_56fb1679))
        if jsEqeqeq(min, 0):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_7cd50c3d
        
        start = 0
        while True:
            tmp0_minOf_0 = jsBitOr(jsPlus(start, 16), 0)
            end = visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl_2eaafa39.min(int32ArrayOf(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_31b1c1a8))
            tmp1_substring_0 = start
            s1 = kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_1cbfca27)
            tmp2_substring_0 = start
            s2 = kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_258cb16c)
            if jsNot(jsEqeqeq(s1, s2)):
                tmp3_toUpperCase_0 = s1
                s1 = kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_536b669)
                tmp4_toUpperCase_0 = s2
                s2 = kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_2966695e)
                if jsNot(jsEqeqeq(s1, s2)):
                    tmp5_toLowerCase_0 = s1
                    s1 = kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_381711cd)
                    tmp6_toLowerCase_0 = s2
                    s2 = kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_233c4b40)
                    if jsNot(jsEqeqeq(s1, s2)):
                        return compareTo(s1, s2)
                    
                
            
            if jsEqeqeq(end, min):
                visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrBreakImpl_700b9a54
            
            start = end
        
        return jsBitOr(jsMinus(n1, n2), 0)
    
    if True:
        return compareTo(self, other)
    

def compareTo_default(other, ignoreCase, _mask0, _handler):
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 2), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_4407b019
    
    return compareTo(other, ignoreCase)

def toUpperCase():
    return kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_9fd26ec)

def toLowerCase():
    return kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_4987383f)

def concatToString():
    result = ''
    indexedObject = self
    inductionVariable = 0
    last = jsArrayLength(indexedObject)
    while jsLt(inductionVariable, last):
        char = jsArrayGet(indexedObject, inductionVariable)
        inductionVariable = jsBitOr(jsPlus(inductionVariable, 1), 0)
        result = jsPlus(result, char)
    
    return result

def concatToString(startIndex, endIndex):
    Companion_getInstance().checkBoundsIndexes(startIndex, endIndex, jsArrayLength(self))
    result = ''
    inductionVariable = startIndex
    if jsLt(inductionVariable, endIndex):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_4c263d9c
    
    return result

def concatToString_default(startIndex, endIndex, _mask0, _handler):
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 1), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_25ebbb3e
    
    if jsNot(jsEqeqeq(jsBitAnd(_mask0, 2), 0)):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl_7b522f61
    
    return concatToString(startIndex, endIndex)

class sam_kotlin_Comparator_0:
    def __init__(self, function):
        self.function = function
    
    def compare(self, a, b):
        return self.function.invoke(a, b)
    
    def compare(self, a, b):
        return self.compare(a, b)
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class _no_name_provided_:
    def __init__(self):
        pass
    
    def invoke(self, a, b):
        return compareTo(b, True)
    
    def invoke(self, p1, p2):
        tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_31eb23c8
        return self.invoke(tmp, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_29e4ad7a)
    

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_2d6aefe1

def STRING_CASE_INSENSITIVE_ORDER_init_():
    tmp = _no_name_provided__factory()
    return sam_kotlin_Comparator_0(tmp)

def _get_REPLACEMENT_BYTE_SEQUENCE_():
    return REPLACEMENT_BYTE_SEQUENCE

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_255845b1 = 0
def REPLACEMENT_BYTE_SEQUENCE_init_():
    tmp0_byteArrayOf_0 = int8ArrayOf(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_1d047267)
    return tmp0_byteArrayOf_0

def _get_value_(_this):
    return _this.value

class Companion:
    def __init__(self):
        Companion_instance = self
        self.MIN_VALUE = Char(0)
        self.MAX_VALUE = Char(65535)
        self.MIN_HIGH_SURROGATE = Char(55296)
        self.MAX_HIGH_SURROGATE = Char(56319)
        self.MIN_LOW_SURROGATE = Char(56320)
        self.MAX_LOW_SURROGATE = Char(57343)
        self.MIN_SURROGATE = Char(55296)
        self.MAX_SURROGATE = Char(57343)
        self.SIZE_BYTES = 2
        self.SIZE_BITS = 16
    
    def _get_MIN_VALUE_(self):
        return self.MIN_VALUE
    
    def _get_MAX_VALUE_(self):
        return self.MAX_VALUE
    
    def _get_MIN_HIGH_SURROGATE_(self):
        return self.MIN_HIGH_SURROGATE
    
    def _get_MAX_HIGH_SURROGATE_(self):
        return self.MAX_HIGH_SURROGATE
    
    def _get_MIN_LOW_SURROGATE_(self):
        return self.MIN_LOW_SURROGATE
    
    def _get_MAX_LOW_SURROGATE_(self):
        return self.MAX_LOW_SURROGATE
    
    def _get_MIN_SURROGATE_(self):
        return self.MIN_SURROGATE
    
    def _get_MAX_SURROGATE_(self):
        return self.MAX_SURROGATE
    
    def _get_SIZE_BYTES_(self):
        return self.SIZE_BYTES
    
    def _get_SIZE_BITS_(self):
        return self.SIZE_BITS
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_6d06b5bf = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_501c3ef6
    
    return Companion_instance

class Char:
    def __init__(self, value):
        Companion_getInstance()
        self.value = value
    
    def compareTo(self, other):
        return jsBitOr(jsMinus(self.value, other.value), 0)
    
    def compareTo(self, other):
        return self.compareTo(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_1e98f6f2)
    
    def plus(self, other):
        return numberToChar(jsBitOr(jsPlus(self.value, other), 0))
    
    def minus(self, other):
        return jsBitOr(jsMinus(self.value, other.value), 0)
    
    def minus(self, other):
        return numberToChar(jsBitOr(jsMinus(self.value, other), 0))
    
    def inc(self):
        return numberToChar(jsBitOr(jsPlus(self.value, 1), 0))
    
    def dec(self):
        return numberToChar(jsBitOr(jsMinus(self.value, 1), 0))
    
    def rangeTo(self, other):
        return CharRange(self, other)
    
    def toByte(self):
        return toByte(self.value)
    
    def toChar(self):
        return self
    
    def toShort(self):
        return toShort(self.value)
    
    def toInt(self):
        return self.value
    
    def toLong(self):
        return toLong(self.value)
    
    def toFloat(self):
        return kotlin_Float(self.value)
    
    def toDouble(self):
        return kotlin_Double(self.value)
    
    def equals(self, other):
        if jsEqeqeq(other, self):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_770093c5
        
        if jsNot(jsInstanceOf(other, jsClass())):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_7e199cec
        
        if True:
            pass
        
        return jsEqeqeq(self.value, kotlin_Char(other).value)
    
    def hashCode(self):
        return self.value
    
    def toString(self):
        tmp0_unsafeCast_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_13ae0ffd
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
    
    def __init__(self):
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
    
    def __init__(self):
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
    
    def __init__(self):
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
    
    def __init__(self):
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
    
    def __init__(self):
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
    
    def __init__(self):
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
    
    def __init__(self):
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
    
    def __init__(self):
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
    
    def __init__(self):
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
    
    def __init__(self):
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
    
    def __init__(self):
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
    
    def __init__(self):
        pass
    

class Companion:
    def __init__(self):
        Companion_instance = self
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_57bf6f1 = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_5bb060b1
    
    return Companion_instance

class Enum:
    def __init__(self, name, ordinal):
        Companion_getInstance()
        self.name = name
        self.ordinal = ordinal
    
    def _get_name_(self):
        return self.name
    
    def _get_ordinal_(self):
        return self.ordinal
    
    def compareTo(self, other):
        return compareTo(self.ordinal, other.ordinal)
    
    def compareTo(self, other):
        return self.compareTo(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2af6e44c)
    
    def equals(self, other):
        return jsEqeqeq(self, other)
    
    def hashCode(self):
        return identityHashCode(self)
    
    def toString(self):
        return self.name
    

def byteArrayOf(elements):
    return elements

def arrayOf(elements):
    return kotlin_Any_(elements)

def toString():
    tmp0_safe_receiver = self
    tmp1_elvis_lhs = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_40a4435a
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2814bb39

def plus(other):
    tmp2_safe_receiver = self
    tmp3_elvis_lhs = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4d5397b6
    tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_71f9b03b
    tmp0_safe_receiver = other
    tmp1_elvis_lhs = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_14c215d4
    return jsPlus(tmp, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6038186d)

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
    def __init__(self):
        DefaultConstructorMarker_instance = self
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_6c84fdaa = 0
def DefaultConstructorMarker_getInstance():
    if jsEqeq(DefaultConstructorMarker_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_506661cf
    
    return DefaultConstructorMarker_instance

def fillArrayVal(array, initValue):
    inductionVariable = 0
    last = jsBitOr(jsMinus(jsArrayLength(array), 1), 0)
    if jsLtEq(inductionVariable, last):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_480318c2
    
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
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_3a9fe0d4
    tmp2_unsafeCast_0 = tmp1_withType_0
    return kotlin_Any_(tmp2_unsafeCast_0)

def charArray(size):
    tmp0_withType_0 = 'CharArray'
    tmp1_withType_0 = fillArrayVal(Array(size), Char(0))
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_c9b0783
    tmp2_unsafeCast_0 = tmp1_withType_0
    return kotlin_Any_(tmp2_unsafeCast_0)

def longArray(size):
    tmp0_withType_0 = 'LongArray'
    tmp1_withType_0 = fillArrayVal(Array(size), Long(0, 0))
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_229d81e3
    tmp2_unsafeCast_0 = tmp1_withType_0
    return kotlin_Any_(tmp2_unsafeCast_0)

def booleanArrayOf(arr):
    tmp0_withType_0 = 'BooleanArray'
    tmp1_withType_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_58d85a00
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_6e7253b7
    tmp2_unsafeCast_0 = tmp1_withType_0
    return kotlin_Any_(tmp2_unsafeCast_0)

def charArrayOf(arr):
    tmp0_withType_0 = 'CharArray'
    tmp1_withType_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_4374c051
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_70c88923
    tmp2_unsafeCast_0 = tmp1_withType_0
    return kotlin_Any_(tmp2_unsafeCast_0)

def longArrayOf(arr):
    tmp0_withType_0 = 'LongArray'
    tmp1_withType_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_33fa6a8b
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_593bda0e
    tmp2_unsafeCast_0 = tmp1_withType_0
    return kotlin_Any_(tmp2_unsafeCast_0)

class _no_name_provided_:
    def __init__(self, _array):
        self._array = _array
        self.index = 0
    
    def _set_index_(self, _set___):
        self.index = _set___
    
    def _get_index_(self):
        return self.index
    
    def hasNext(self):
        return jsNot(jsEqeqeq(self.index, jsArrayLength(self._array)))
    
    def next(self):
        tmp
        if jsNot(jsEqeqeq(self.index, jsArrayLength(self._array))):
            tmp0_this = self
            tmp1 = tmp0_this.index
            tmp0_this.index = jsBitOr(jsPlus(tmp1, 1), 0)
            tmp = jsArrayGet(self._array, tmp1)
        
        if True:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_48515dfc
        
        return tmp
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class _no_name_provided_:
    def __init__(self, _array):
        self._array = _array
        visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_3b76dfa6
        self.index = 0
    
    def _set_index_(self, _set___):
        self.index = _set___
    
    def _get_index_(self):
        return self.index
    
    def hasNext(self):
        return jsNot(jsEqeqeq(self.index, jsArrayLength(self._array)))
    
    def nextBoolean(self):
        tmp
        if jsNot(jsEqeqeq(self.index, jsArrayLength(self._array))):
            tmp0_this = self
            tmp1 = tmp0_this.index
            tmp0_this.index = jsBitOr(jsPlus(tmp1, 1), 0)
            tmp = jsArrayGet(self._array, tmp1)
        
        if True:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_38f0de07
        
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
    def __init__(self, _array):
        self._array = _array
        visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_3569f0f1
        self.index = 0
    
    def _set_index_(self, _set___):
        self.index = _set___
    
    def _get_index_(self):
        return self.index
    
    def hasNext(self):
        return jsNot(jsEqeqeq(self.index, jsArrayLength(self._array)))
    
    def nextChar(self):
        tmp
        if jsNot(jsEqeqeq(self.index, jsArrayLength(self._array))):
            tmp0_this = self
            tmp1 = tmp0_this.index
            tmp0_this.index = jsBitOr(jsPlus(tmp1, 1), 0)
            tmp = jsArrayGet(self._array, tmp1)
        
        if True:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_763960eb
        
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
    def __init__(self, _array):
        self._array = _array
        visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_46791608
        self.index = 0
    
    def _set_index_(self, _set___):
        self.index = _set___
    
    def _get_index_(self):
        return self.index
    
    def hasNext(self):
        return jsNot(jsEqeqeq(self.index, jsArrayLength(self._array)))
    
    def nextByte(self):
        tmp
        if jsNot(jsEqeqeq(self.index, jsArrayLength(self._array))):
            tmp0_this = self
            tmp1 = tmp0_this.index
            tmp0_this.index = jsBitOr(jsPlus(tmp1, 1), 0)
            tmp = jsArrayGet(self._array, tmp1)
        
        if True:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_106f566b
        
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
    def __init__(self, _array):
        self._array = _array
        visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_50ca509b
        self.index = 0
    
    def _set_index_(self, _set___):
        self.index = _set___
    
    def _get_index_(self):
        return self.index
    
    def hasNext(self):
        return jsNot(jsEqeqeq(self.index, jsArrayLength(self._array)))
    
    def nextShort(self):
        tmp
        if jsNot(jsEqeqeq(self.index, jsArrayLength(self._array))):
            tmp0_this = self
            tmp1 = tmp0_this.index
            tmp0_this.index = jsBitOr(jsPlus(tmp1, 1), 0)
            tmp = jsArrayGet(self._array, tmp1)
        
        if True:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_47c163bb
        
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
    def __init__(self, _array):
        self._array = _array
        visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_5d39797a
        self.index = 0
    
    def _set_index_(self, _set___):
        self.index = _set___
    
    def _get_index_(self):
        return self.index
    
    def hasNext(self):
        return jsNot(jsEqeqeq(self.index, jsArrayLength(self._array)))
    
    def nextInt(self):
        tmp
        if jsNot(jsEqeqeq(self.index, jsArrayLength(self._array))):
            tmp0_this = self
            tmp1 = tmp0_this.index
            tmp0_this.index = jsBitOr(jsPlus(tmp1, 1), 0)
            tmp = jsArrayGet(self._array, tmp1)
        
        if True:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_286e2b71
        
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
    def __init__(self, _array):
        self._array = _array
        visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_14d9d042
        self.index = 0
    
    def _set_index_(self, _set___):
        self.index = _set___
    
    def _get_index_(self):
        return self.index
    
    def hasNext(self):
        return jsNot(jsEqeqeq(self.index, jsArrayLength(self._array)))
    
    def nextFloat(self):
        tmp
        if jsNot(jsEqeqeq(self.index, jsArrayLength(self._array))):
            tmp0_this = self
            tmp1 = tmp0_this.index
            tmp0_this.index = jsBitOr(jsPlus(tmp1, 1), 0)
            tmp = jsArrayGet(self._array, tmp1)
        
        if True:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_3df99d5e
        
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
    def __init__(self, _array):
        self._array = _array
        visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_4a3b0387
        self.index = 0
    
    def _set_index_(self, _set___):
        self.index = _set___
    
    def _get_index_(self):
        return self.index
    
    def hasNext(self):
        return jsNot(jsEqeqeq(self.index, jsArrayLength(self._array)))
    
    def nextLong(self):
        tmp
        if jsNot(jsEqeqeq(self.index, jsArrayLength(self._array))):
            tmp0_this = self
            tmp1 = tmp0_this.index
            tmp0_this.index = jsBitOr(jsPlus(tmp1, 1), 0)
            tmp = jsArrayGet(self._array, tmp1)
        
        if True:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_22152da0
        
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
    def __init__(self, _array):
        self._array = _array
        visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_15d844b2
        self.index = 0
    
    def _set_index_(self, _set___):
        self.index = _set___
    
    def _get_index_(self):
        return self.index
    
    def hasNext(self):
        return jsNot(jsEqeqeq(self.index, jsArrayLength(self._array)))
    
    def nextDouble(self):
        tmp
        if jsNot(jsEqeqeq(self.index, jsArrayLength(self._array))):
            tmp0_this = self
            tmp1 = tmp0_this.index
            tmp0_this.index = jsBitOr(jsPlus(tmp1, 1), 0)
            tmp = jsArrayGet(self._array, tmp1)
        
        if True:
            visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_20382851
        
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

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_6e16fcaf = 0
def _get_bufFloat64_():
    return bufFloat64

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_1bc41170 = 0
def _get_bufFloat32_():
    return bufFloat32

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_1df1bd44 = 0
def _get_bufInt32_():
    return bufInt32

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_1b316cac = 0
def _get_lowIndex_():
    return lowIndex

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_14eaab92 = 0
def _get_highIndex_():
    return highIndex

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_de0922c = 0
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
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6594fbc9

class DoNotIntrinsify:
    def __init__(self):
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
        tmp0_unsafeCast_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_283eb984
        tmp = Char(kotlin_Any_(tmp0_unsafeCast_0))
    
    if True:
        tmp = a.get(index)
    
    return tmp

def isString(a):
    return jsEqeqeq(jsTypeOf(a), 'string')

def charSequenceLength(a):
    tmp
    if isString(a):
        tmp0_unsafeCast_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicMemberExpressionImpl_71c1ba6d
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
    
    if True:
        tmp = a._get_length_()
    
    return tmp

def charSequenceSubSequence(a, startIndex, endIndex):
    tmp
    if isString(a):
        tmp0_unsafeCast_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_a1cac17
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
    
    if True:
        tmp = a.subSequence(startIndex, endIndex)
    
    return tmp

def arrayToString(array):
    return joinToString_default(', ', '[', ']', 0, None, _no_name_provided__factory(), 24, None)

class _no_name_provided_:
    def __init__(self):
        pass
    
    def invoke(self, it):
        return toString(it)
    
    def invoke(self, p1):
        return self.invoke(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_1477b4ab)
    

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl_7371f9b7

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
    
    if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_ed7d39:
        tmp = primitiveCompareTo(a, b)
    
    if True:
        tmp = compareToDoNotIntrinsicify(kotlin_Comparable_dynamic_(a), b)
    
    return tmp

def doubleCompareTo(a, b):
    tmp
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_54539319:
        tmp = -1
    
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_2e006f67:
        tmp = 1
    
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_cec9f23:
        tmp
        if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_7a970f:
            tmp = 0
        
        if True:
            tmp0_asDynamic_0 = 1
            ia = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_57f2a68c
            tmp
            tmp1_asDynamic_0 = 1
            if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_14a3d15b:
                tmp = 0
            
            if True:
                if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_75401424:
                    tmp = -1
                
                if True:
                    if True:
                        tmp = 1
                    
                
            
            tmp = tmp
        
        tmp = tmp
    
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_1228a579:
        tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3e77de0a
    
    if True:
        tmp = -1
    
    return tmp

def primitiveCompareTo(a, b):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_5ad6760c

def compareToDoNotIntrinsicify(a, b):
    return a.compareTo(b)

def construct(constructorType, resultType, args):
    return kotlin_Any(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_3c0403a)

def identityHashCode(obj):
    return getObjectHashCode(obj)

def getObjectHashCode(obj):
    if jsNot(jsIn('kotlinHashCodeValue$', kotlin_Any(obj))):
        hash = jsBitwiseOr(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_31360632, 0)
        descriptor = js('new Object()')
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_7c8c2d03
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_36f8c95a
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_507c795e
    
    tmp0_unsafeCast_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_184d73af
    return kotlin_Any_(tmp0_unsafeCast_0)

def _get_OBJECT_HASH_CODE_PROPERTY_NAME_():
    return OBJECT_HASH_CODE_PROPERTY_NAME

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_40ea5cd3 = 0
def _get_POW_2_32_():
    return POW_2_32

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_18fa4822 = 0
def toString(o):
    tmp
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_48dbf9d:
        tmp = 'null'
    
    if isArrayish(o):
        tmp = '[...]'
    
    if True:
        tmp0_unsafeCast_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_ef64a8f
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
    
    return tmp

def hashCode(obj):
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_7ec53f8f:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_1f94df5
    
    tmp0_subject = jsTypeOf(obj)
    tmp
    if jsEqeqeq(tmp0_subject, 'object'):
        tmp = kotlin_Int(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_c986a89)
    
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
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_b9f1f88
    
    return hash

def anyToString(o):
    return kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_4b33b5b0)

def equals(obj1, obj2):
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_9d7d83d:
        return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_341f2f4c
    
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_59e7a6d8:
        return False
    
    if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_958fec:
        return kotlin_Boolean(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_76b17a78)
    
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_8004b2d:
        return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_274d10aa
    
    if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_63c75a30:
        tmp
        if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_3d118651:
            tmp
            if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_11caa21d:
                tmp = True
            
            if True:
                tmp0_asDynamic_0 = 1
                tmp = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_2a38b5c7
                tmp1_asDynamic_0 = 1
                tmp = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_5bf963a
            
            tmp = tmp
        
        if True:
            tmp = False
        
        return tmp
    
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_1159a049

def boxIntrinsic(x):
    tmp0_error_0 = 'Should be lowered'
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_262a8f7e

def unboxIntrinsic(x):
    tmp0_error_0 = 'Should be lowered'
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_128c3189

def captureStack(instance, constructorFunction):
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_7e6bfd2:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_768dcd21
    
    if True:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_65b869b4
    

def newThrowable(message, cause):
    throwable = js('new Error()')
    tmp
    if isUndefined(message):
        tmp
        if isUndefined(cause):
            tmp = message
        
        if True:
            tmp0_safe_receiver = cause
            tmp1_elvis_lhs = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_70db4172
            tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_4ec0f36e
        
        tmp = tmp
    
    if True:
        tmp2_elvis_lhs = message
        tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_76a72a1b
    
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_3057a923
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_5d4f35cb
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_34672fb
    return kotlin_Any_(throwable)

def isUndefined(value):
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_22e470f4

def extendThrowable(this_, message, cause):
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_10009505
    setPropertiesToThrowableInstance(this_, message, cause)

def setPropertiesToThrowableInstance(this_, message, cause):
    if jsNot(hasOwnPrototypeProperty(kotlin_Any(this_), 'message')):
        tmp
        if jsEqeq(message, None):
            tmp
            if jsNot(jsEqeqeq(message, None)):
                tmp0_safe_receiver = cause
                tmp1_elvis_lhs = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_34e7832d
                tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_316245b6
            
            if True:
                tmp = _get_undefined_()
            
            tmp = tmp
        
        if True:
            tmp = message
        
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_7a6cab6f
    
    if jsNot(hasOwnPrototypeProperty(kotlin_Any(this_), 'cause')):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_6b732d6
    
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_64a2966a

def hasOwnPrototypeProperty(o, name):
    tmp0_unsafeCast_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_db62b5f
    return kotlin_Any_(tmp0_unsafeCast_0)

def getContinuation():
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_5c00b341

def returnIfSuspended(argument):
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_7adc8212

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
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_41019971

def noWhenBranchMatchedException():
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_5989f463

def THROW_CCE():
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_3b8adbda

def throwUninitializedPropertyAccessException(name):
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_37a522c8

def throwKotlinNothingValueException():
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_49808d41

def THROW_ISE():
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_626e3b18

def THROW_IAE(msg):
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_20b1f874

def emptyArray():
    return kotlin_Array_T_(js('[]'))

def enumValueOfIntrinsic(name):
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_6385af63

def enumValuesIntrinsic():
    visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_6a5c67cf

class Companion:
    def __init__(self):
        Companion_instance = self
        self.MIN_VALUE = Long(0, -2147483648)
        self.MAX_VALUE = Long(-1, 2147483647)
        self.SIZE_BYTES = 8
        self.SIZE_BITS = 64
    
    def _get_MIN_VALUE_(self):
        return self.MIN_VALUE
    
    def _get_MAX_VALUE_(self):
        return self.MAX_VALUE
    
    def _get_SIZE_BYTES_(self):
        return self.SIZE_BYTES
    
    def _get_SIZE_BITS_(self):
        return self.SIZE_BITS
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_5e5978e5 = 0
def Companion_getInstance():
    if jsEqeq(Companion_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_16c1fc82
    
    return Companion_instance

class Long:
    def __init__(self, low, high):
        Companion_getInstance()
        visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_2f062dbc
        self.low = low
        self.high = high
    
    def _get_low_(self):
        return self.low
    
    def _get_high_(self):
        return self.high
    
    def compareTo(self, other):
        return self.compareTo(toLong(other))
    
    def compareTo(self, other):
        return self.compareTo(toLong(other))
    
    def compareTo(self, other):
        return self.compareTo(toLong(other))
    
    def compareTo(self, other):
        return compare(other)
    
    def compareTo(self, other):
        return self.compareTo(visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3e38a99c)
    
    def compareTo(self, other):
        return compareTo(self.toFloat(), other)
    
    def compareTo(self, other):
        return compareTo(self.toDouble(), other)
    
    def plus(self, other):
        return self.plus(toLong(other))
    
    def plus(self, other):
        return self.plus(toLong(other))
    
    def plus(self, other):
        return self.plus(toLong(other))
    
    def plus(self, other):
        return add(other)
    
    def plus(self, other):
        return jsPlus(self.toFloat(), other)
    
    def plus(self, other):
        return jsPlus(self.toDouble(), other)
    
    def minus(self, other):
        return self.minus(toLong(other))
    
    def minus(self, other):
        return self.minus(toLong(other))
    
    def minus(self, other):
        return self.minus(toLong(other))
    
    def minus(self, other):
        return subtract(other)
    
    def minus(self, other):
        return jsMinus(self.toFloat(), other)
    
    def minus(self, other):
        return jsMinus(self.toDouble(), other)
    
    def times(self, other):
        return self.times(toLong(other))
    
    def times(self, other):
        return self.times(toLong(other))
    
    def times(self, other):
        return self.times(toLong(other))
    
    def times(self, other):
        return multiply(other)
    
    def times(self, other):
        return jsMult(self.toFloat(), other)
    
    def times(self, other):
        return jsMult(self.toDouble(), other)
    
    def div(self, other):
        return self.div(toLong(other))
    
    def div(self, other):
        return self.div(toLong(other))
    
    def div(self, other):
        return self.div(toLong(other))
    
    def div(self, other):
        return divide(other)
    
    def div(self, other):
        return jsDiv(self.toFloat(), other)
    
    def div(self, other):
        return jsDiv(self.toDouble(), other)
    
    def rem(self, other):
        return self.rem(toLong(other))
    
    def rem(self, other):
        return self.rem(toLong(other))
    
    def rem(self, other):
        return self.rem(toLong(other))
    
    def rem(self, other):
        return modulo(other)
    
    def rem(self, other):
        return jsMod(self.toFloat(), other)
    
    def rem(self, other):
        return jsMod(self.toDouble(), other)
    
    def inc(self):
        return self.plus(Long(1, 0))
    
    def dec(self):
        return self.minus(Long(1, 0))
    
    def unaryPlus(self):
        return self
    
    def unaryMinus(self):
        return self.inv().plus(Long(1, 0))
    
    def rangeTo(self, other):
        return self.rangeTo(toLong(other))
    
    def rangeTo(self, other):
        return self.rangeTo(toLong(other))
    
    def rangeTo(self, other):
        return self.rangeTo(toLong(other))
    
    def rangeTo(self, other):
        return LongRange(self, other)
    
    def shl(self, bitCount):
        return shiftLeft(bitCount)
    
    def shr(self, bitCount):
        return shiftRight(bitCount)
    
    def ushr(self, bitCount):
        return shiftRightUnsigned(bitCount)
    
    def _and(self, other):
        return Long(jsBitAnd(self.low, other.low), jsBitAnd(self.high, other.high))
    
    def _or(self, other):
        return Long(jsBitOr(self.low, other.low), jsBitOr(self.high, other.high))
    
    def xor(self, other):
        return Long(jsBitXor(self.low, other.low), jsBitXor(self.high, other.high))
    
    def inv(self):
        return Long(jsBitNot(self.low), jsBitNot(self.high))
    
    def toByte(self):
        return toByte(self.low)
    
    def toChar(self):
        return numberToChar(self.low)
    
    def toShort(self):
        return toShort(self.low)
    
    def toInt(self):
        return self.low
    
    def toLong(self):
        return self
    
    def toFloat(self):
        return kotlin_Float(self.toDouble())
    
    def toDouble(self):
        return toNumber()
    
    def valueOf(self):
        return self.toDouble()
    
    def equals(self, other):
        tmp
        if jsInstanceOf(other, jsClass()):
            tmp = equalsLong(kotlin_Long(other))
        
        if True:
            if True:
                tmp = False
            
        
        return tmp
    
    def hashCode(self):
        return hashCode(self)
    
    def toString(self):
        return toStringImpl(10)
    

def _get_ZERO_():
    return ZERO

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_90efbba = 0
def _get_ONE_():
    return ONE

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_3532f633 = 0
def _get_NEG_ONE_():
    return NEG_ONE

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_48adb967 = 0
def _get_MAX_VALUE_():
    return MAX_VALUE

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_6f286e1d = 0
def _get_MIN_VALUE_():
    return MIN_VALUE

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_66049424 = 0
def _get_TWO_PWR_24__():
    return TWO_PWR_24_

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_58968733 = 0
def compare(other):
    if equalsLong(other):
        return 0
    
    thisNeg = isNegative()
    otherNeg = isNegative()
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_5923482

def add(other):
    a48 = jsBitShiftRU(self.high, 16)
    a32 = jsBitAnd(self.high, 65535)
    a16 = jsBitShiftRU(self.low, 16)
    a00 = jsBitAnd(self.low, 65535)
    b48 = jsBitShiftRU(other.high, 16)
    b32 = jsBitAnd(other.high, 65535)
    b16 = jsBitShiftRU(other.low, 16)
    b00 = jsBitAnd(other.low, 65535)
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
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_40fec4ad
    
    if equalsLong(MIN_VALUE):
        return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3c90ed37
    
    if isNegative():
        tmp
        if isNegative():
            tmp = multiply(negate())
        
        if True:
            tmp = negate()
        
        return tmp
    
    if isNegative():
        return negate()
    
    if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_67ad47dd:
        return fromNumber(jsMult(toNumber(), toNumber()))
    
    a48 = jsBitShiftRU(self.high, 16)
    a32 = jsBitAnd(self.high, 65535)
    a16 = jsBitShiftRU(self.low, 16)
    a00 = jsBitAnd(self.low, 65535)
    b48 = jsBitShiftRU(other.high, 16)
    b32 = jsBitAnd(other.high, 65535)
    b16 = jsBitShiftRU(other.low, 16)
    b00 = jsBitAnd(other.low, 65535)
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
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_435e857c
    
    if isZero():
        return ZERO
    
    if equalsLong(MIN_VALUE):
        if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_226ddb69:
            return MIN_VALUE
        
        if equalsLong(MIN_VALUE):
            return ONE
        
        if True:
            halfThis = shiftRight(1)
            approx = shiftLeft(1)
            if equalsLong(ZERO):
                return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_49ee3426
            
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
    rem = self
    while greaterThanOrEqual(other):
        approxDouble = jsDiv(toNumber(), toNumber())
        approx2 = visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl_702f99a5.max(1.0, visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl_220f2d1b.floor(approxDouble))
        log2 = visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl_32317a37.ceil(jsDiv(visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl_19dffe76.log(approx2), visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl_4d484eda._get_LN2_()))
        delta = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_608cd3ec
        approxRes = fromNumber(approx2)
        approxRem = multiply(other)
        while visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_185db22c:
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
        return self
    
    if True:
        if jsLt(numBits, 32):
            return Long(jsBitShiftL(self.low, numBits), jsBitOr(jsBitShiftL(self.high, numBits), jsBitShiftRU(self.low, jsBitOr(jsMinus(32, numBits), 0))))
        
        if True:
            return Long(0, jsBitShiftL(self.low, jsBitOr(jsMinus(numBits, 32), 0)))
        
    

def shiftRight(numBits):
    numBits = jsBitAnd(numBits, 63)
    if jsEqeqeq(numBits, 0):
        return self
    
    if True:
        if jsLt(numBits, 32):
            return Long(jsBitOr(jsBitShiftRU(self.low, numBits), jsBitShiftL(self.high, jsBitOr(jsMinus(32, numBits), 0))), jsBitShiftR(self.high, numBits))
        
        if True:
            return Long(jsBitShiftR(self.high, jsBitOr(jsMinus(numBits, 32), 0)), visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3b6b0bf4)
        
    

def shiftRightUnsigned(numBits):
    numBits = jsBitAnd(numBits, 63)
    if jsEqeqeq(numBits, 0):
        return self
    
    if True:
        if jsLt(numBits, 32):
            return Long(jsBitOr(jsBitShiftRU(self.low, numBits), jsBitShiftL(self.high, jsBitOr(jsMinus(32, numBits), 0))), jsBitShiftRU(self.high, numBits))
        
        if True:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCompositeImpl_79a290ff
        
    

def toNumber():
    return jsPlus(jsMult(self.high, 4.294967296E9), getLowBitsUnsigned())

def equalsLong(other):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_47b0bffc

def hashCode(l):
    return jsBitXor(l.low, l.high)

def toStringImpl(radix):
    if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_43ddde24:
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_442bb11b
    
    if isZero():
        return '0'
    
    if isNegative():
        if equalsLong(MIN_VALUE):
            radixLong = fromInt(radix)
            div = self.div(radixLong)
            rem = subtract(self).toInt()
            tmp = toStringImpl(radix)
            tmp0_unsafeCast_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_17236e87
            return jsPlus(tmp, kotlin_Any_(tmp0_unsafeCast_0))
        
        if True:
            return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrStringConcatenationImpl_3a6f00f
        
    
    radixToPower = fromNumber(visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl_75cb2090.pow(kotlin_Double(radix), 6.0))
    rem = self
    result = ''
    while True:
        remDiv = rem.div(radixToPower)
        intval = subtract(multiply(radixToPower)).toInt()
        tmp1_unsafeCast_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_7e122a87
        digits = kotlin_Any_(tmp1_unsafeCast_0)
        rem = remDiv
        if isZero():
            return jsPlus(digits, result)
        
        if True:
            while jsLt(jsArrayLength(digits), 6):
                digits = jsPlus('0', digits)
            
            result = jsPlus(digits, result)
        
    

def fromInt(value):
    return Long(value, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_76cad044)

def isNegative():
    return jsLt(self.high, 0)

def isZero():
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_6e706a1a

def isOdd():
    return jsEqeqeq(jsBitAnd(self.low, 1), 1)

def negate():
    return self.unaryMinus()

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
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_76e9662b

def _get_TWO_PWR_32_DBL__():
    return TWO_PWR_32_DBL_

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_b807b32 = 0
def _get_TWO_PWR_63_DBL__():
    return TWO_PWR_63_DBL_

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_6b6d68d2 = 0
def imul(a_local, b_local):
    lhs = jsMult(kotlin_Double(jsBitwiseAnd(a_local, js('0xffff0000'))), kotlin_Double(jsBitwiseAnd(b_local, 65535)))
    rhs = jsMult(kotlin_Double(jsBitwiseAnd(a_local, 65535)), kotlin_Double(b_local))
    return jsBitwiseOr(jsPlus(lhs, rhs), 0)

def withType(type, array):
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_631f692d
    return array

def arrayConcat(args):
    len = jsArrayLength(args)
    tmp0_unsafeCast_0 = js('Array(len)')
    typed = kotlin_Any_(tmp0_unsafeCast_0)
    inductionVariable = 0
    last = jsBitOr(jsMinus(len, 1), 0)
    if jsLtEq(inductionVariable, last):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_782c927d
    
    return T(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_31a65ddd)

def primitiveArrayConcat(args):
    size_local = 0
    inductionVariable = 0
    last = jsBitOr(jsMinus(jsArrayLength(args), 1), 0)
    if jsLtEq(inductionVariable, last):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_2bdb0d42
    
    a = jsArrayGet(args, 0)
    tmp1_unsafeCast_0 = js('new a.constructor(size_local)')
    result = kotlin_Any_(tmp1_unsafeCast_0)
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_507a53b6:
        tmp2_withType_0 = kotlin_String(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicMemberExpressionImpl_325fa8c)
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_20295ff2
    
    if True:
        pass
    
    size_local = 0
    inductionVariable = 0
    last = jsBitOr(jsMinus(jsArrayLength(args), 1), 0)
    if jsLtEq(inductionVariable, last):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDoWhileLoopImpl_4f6a501c
    
    return kotlin_Any_(result)

def taggedArrayCopy(array):
    res = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_238fd9cc
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_ad58e2c
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
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_5e5eaa7f

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

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_2aeffa55 = 0
def metadataObject():
    return js('{ kind: \'class\', interfaces: [] }')

def getPropertyCallableRef(name, paramCount, type, getter, setter):
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_2489ee11
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_6dd8dfe5
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_5f966dee
    tmp0_unsafeCast_0 = getPropertyRefClass(getter, getKPropMetadata(paramCount, setter, type))
    return kotlin_Any_(tmp0_unsafeCast_0)

def getPropertyRefClass(obj, metadata):
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_425436b4
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_23639e5
    return obj

def getKPropMetadata(paramCount, setter, type):
    mdata = jsArrayGet(jsArrayGet(propertyRefClassMetadataCache, paramCount), visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3112da58)
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_5c8b15f5:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_89537c1
    
    return mdata

def getLocalDelegateReference(name, type, mutable, _lambda):
    return getPropertyCallableRef(name, 0, type, _lambda, visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_1e1f808c)

def propertyRefClassMetadataCache_init_():
    tmp = js('{ kind: \'class\', interfaces: [] }')
    tmp0_arrayOf_0 = arrayLiteral(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_6a45af66)
    tmp = kotlin_Any_(tmp0_arrayOf_0)
    tmp = js('{ kind: \'class\', interfaces: [] }')
    tmp1_arrayOf_0 = arrayLiteral(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_451dfee3)
    tmp = kotlin_Any_(tmp1_arrayOf_0)
    tmp = js('{ kind: \'class\', interfaces: [] }')
    tmp2_arrayOf_0 = arrayLiteral(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_4359b2f3)
    tmp3_arrayOf_0 = arrayLiteral(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_3ae8394)
    return kotlin_Any_(tmp3_arrayOf_0)

def isArrayish(o):
    tmp
    if isJsArray(kotlin_Any(o)):
        tmp = True
    
    if True:
        tmp0_unsafeCast_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_12919b7b
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
    
    return tmp

def isJsArray(obj):
    tmp0_unsafeCast_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_5c5e301f
    return kotlin_Any_(tmp0_unsafeCast_0)

def isInterface(obj, iface):
    tmp0_elvis_lhs = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicMemberExpressionImpl_1aef48f0
    tmp
    if jsEqeq(tmp0_elvis_lhs, None):
        return False
    
    if True:
        tmp = tmp0_elvis_lhs
    
    ctor = tmp
    return isInterfaceImpl(kotlin_js_Ctor(ctor), iface)

def isInterfaceImpl(ctor, iface):
    if jsEqeqeq(ctor, iface):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrReturnImpl_2929ef51
    
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
            
        
    
    superPrototype = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2b080464
    superConstructor = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2d5b950b
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_5a9f6c6c

def isArray(obj):
    tmp
    if isJsArray(obj):
        tmp = kotlin_Boolean(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_5cef76a2)
    
    if True:
        tmp = False
    
    return tmp

def isObject(obj):
    objTypeOf = jsTypeOf(obj)
    tmp0_subject = objTypeOf
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_16c82dc7

def isSuspendFunction(obj, arity):
    if jsEqeqeq(jsTypeOf(obj), 'function'):
        tmp0_unsafeCast_0 = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicMemberExpressionImpl_7db373b2
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
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_23e585e4

def isCharSequence(value):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_76e1c593

def isBooleanArray(a):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_63e1dd68

def isByteArray(a):
    return jsInstanceOf(a, js('Int8Array'))

def isShortArray(a):
    return jsInstanceOf(a, js('Int16Array'))

def isCharArray(a):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_38763e26

def isIntArray(a):
    return jsInstanceOf(a, js('Int32Array'))

def isFloatArray(a):
    return jsInstanceOf(a, js('Float32Array'))

def isLongArray(a):
    return visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_7cb961fd

def isDoubleArray(a):
    return jsInstanceOf(a, js('Float64Array'))

def jsIsType(obj, jsClass):
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_7d968ec1:
        return isObject(obj)
    
    if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3dd34335:
        return False
    
    if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_7a58b77b:
        return True
    
    proto = jsGetPrototypeOf(jsClass)
    tmp0_safe_receiver = proto
    constructor = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_69e0917
    if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_41a0a072:
        metadata = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicMemberExpressionImpl_760d9d4a
        if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_5a7810e1:
            return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_6b4684b4
        
    
    klassMetadata = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicMemberExpressionImpl_537231c1
    if visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_1fa59b0d:
        return jsInstanceOf(obj, jsClass)
    
    if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_5ddae4c5:
        return isInterfaceImpl(kotlin_js_Ctor(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicMemberExpressionImpl_68d2e6eb), jsClass)
    
    return False

def jsGetPrototypeOf(jsClass):
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_1f878eed

def asList():
    return ArrayList(kotlin_Any_(self))

def plus(elements):
    return kotlin_Array_T_(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_55ea7b4d)

def copyOfRange(fromIndex, toIndex):
    Companion_getInstance().checkRangeIndexes(fromIndex, toIndex, jsArrayLength(self))
    return kotlin_Array_T_(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl_75643efa)

def minOf(a, b):
    return visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl_18db7998.min(int32ArrayOf(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_4fc1f04e))

def _get_resultContinuation_(_this):
    return _this.resultContinuation

def _get__context_(_this):
    return _this._context

def _set_intercepted__(_this, _set___):
    _this.intercepted_ = _set___

def _get_intercepted__(_this):
    return _this.intercepted_

def releaseIntercepted(_this):
    intercepted = _this.intercepted_
    if visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_42657f8:
        ensureNotNull(_this._get_context_().get(Key_getInstance())).releaseInterceptedContinuation(intercepted)
    
    _this.intercepted_ = CompletedContinuation_getInstance()

class CoroutineImpl:
    def __init__(self, resultContinuation):
        self.resultContinuation = resultContinuation
        self.state = 0
        self.exceptionState = 0
        self.result = None
        self.exception = None
        self.finallyPath = None
        tmp = self
        tmp0_safe_receiver = self.resultContinuation
        tmp._context = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_2e142db2
        self.intercepted_ = None
    
    def _set_state_(self, _set___):
        self.state = _set___
    
    def _get_state_(self):
        return self.state
    
    def _set_exceptionState_(self, _set___):
        self.exceptionState = _set___
    
    def _get_exceptionState_(self):
        return self.exceptionState
    
    def _set_result_(self, _set___):
        self.result = _set___
    
    def _get_result_(self):
        return self.result
    
    def _set_exception_(self, _set___):
        self.exception = _set___
    
    def _get_exception_(self):
        return self.exception
    
    def _set_finallyPath_(self, _set___):
        self.finallyPath = _set___
    
    def _get_finallyPath_(self):
        return self.finallyPath
    
    def _get_context_(self):
        return ensureNotNull(self._context)
    
    def intercepted(self):
        tmp2_elvis_lhs = self.intercepted_
        tmp
        if jsEqeq(tmp2_elvis_lhs, None):
            tmp0_safe_receiver = self._get_context_().get(Key_getInstance())
            tmp1_elvis_lhs = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_526388ee
            tmp0_also_0 = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_3e828eb6
            self.intercepted_ = tmp0_also_0
            tmp = tmp0_also_0
        
        if True:
            tmp = tmp2_elvis_lhs
        
        return tmp
    
    def resumeWith(self, result):
        current = self
        tmp
        if _Result___get_isFailure__impl_(result):
            tmp = None
        
        if True:
            tmp = _Result___get_value__impl_(result)
            tmp = visitWhen_inToByExpressionTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrWhenImpl_1c0ffb7e
        
        currentResult = tmp
        currentException = Result__exceptionOrNull_impl(result)
        while True:
            tmp0_with_0 = current
            if jsEqeq(currentException, None):
                tmp0_with_0.result = currentResult
            
            if True:
                tmp0_with_0.state = tmp0_with_0.exceptionState
                tmp0_with_0.exception = currentException
            
            visitTry_org_jetbrains_kotlin_ir_expressions_impl_IrTryImpl_114c2c2b
            releaseIntercepted(tmp0_with_0)
            completion_4 = ensureNotNull(tmp0_with_0.resultContinuation)
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
        return self.resumeWith(result)
    
    def doResume(self):
        pass
    
    def create(self, completion):
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_2945a3c1
    
    def create(self, value, completion):
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_6314b195
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class CompletedContinuation:
    def __init__(self):
        CompletedContinuation_instance = self
    
    def _get_context_(self):
        tmp0_error_0 = 'This continuation is already complete'
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_3e5796a0
    
    def resumeWith(self, result):
        tmp0_error_0 = 'This continuation is already complete'
        visitThrow_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl_25713130
    
    def resumeWith(self, result):
        return self.resumeWith(result)
    
    def toString(self):
        return 'This continuation is already complete'
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    

visitField_org_jetbrains_kotlin_ir_declarations_persistent_PersistentIrField_69cf9dd = 0
def CompletedContinuation_getInstance():
    if jsEqeq(CompletedContinuation_instance, None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstructorCallImpl_6e71c9dc
    
    return CompletedContinuation_instance

def Exception_init__Init_(_this):
    extendThrowable(_this, _undefined(), _undefined())
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_5387e079
    return _this

def Exception_init__Create_():
    tmp = Exception_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_c59b505)
    return tmp

def Exception_init__Init_(message, _this):
    extendThrowable(_this, message, _undefined())
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_fc5f2a9
    return _this

def Exception_init__Create_(message):
    tmp = Exception_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_4091ccc2)
    return tmp

def Exception_init__Init_(message, cause, _this):
    extendThrowable(_this, message, cause)
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_3772b95a
    return _this

def Exception_init__Create_(message, cause):
    tmp = Exception_init__Init_(message, cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_30df4a72)
    return tmp

def Exception_init__Init_(cause, _this):
    extendThrowable(_this, _undefined(), cause)
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_428d5eb8
    return _this

def Exception_init__Create_(cause):
    tmp = Exception_init__Init_(cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_186eae52)
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
    
    def __init__(self):
        captureStack(self, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_43ddb43d)
    

def Error_init__Init_(_this):
    extendThrowable(_this, _undefined(), _undefined())
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_41a56ad9
    return _this

def Error_init__Create_():
    tmp = Error_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_4ac9a1ff)
    return tmp

def Error_init__Init_(message, _this):
    extendThrowable(_this, message, _undefined())
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_4388206e
    return _this

def Error_init__Create_(message):
    tmp = Error_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_4e3db1c6)
    return tmp

def Error_init__Init_(message, cause, _this):
    extendThrowable(_this, message, cause)
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_672bc69a
    return _this

def Error_init__Create_(message, cause):
    tmp = Error_init__Init_(message, cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_664724e7)
    return tmp

def Error_init__Init_(cause, _this):
    extendThrowable(_this, _undefined(), cause)
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_475c02b5
    return _this

def Error_init__Create_(cause):
    tmp = Error_init__Init_(cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_160b966a)
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
    
    def __init__(self):
        captureStack(self, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_263059cd)
    

def IllegalArgumentException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_5ea231be
    return _this

def IllegalArgumentException_init__Create_():
    tmp = IllegalArgumentException_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_1090cb79)
    return tmp

def IllegalArgumentException_init__Init_(message, _this):
    RuntimeException_init__Init_(message, _this)
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_5569ea9e
    return _this

def IllegalArgumentException_init__Create_(message):
    tmp = IllegalArgumentException_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_43424634)
    return tmp

def IllegalArgumentException_init__Init_(message, cause, _this):
    RuntimeException_init__Init_(message, cause, _this)
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_23701ff5
    return _this

def IllegalArgumentException_init__Create_(message, cause):
    tmp = IllegalArgumentException_init__Init_(message, cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_50bd8cfa)
    return tmp

def IllegalArgumentException_init__Init_(cause, _this):
    RuntimeException_init__Init_(cause, _this)
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_4246aa06
    return _this

def IllegalArgumentException_init__Create_(cause):
    tmp = IllegalArgumentException_init__Init_(cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_1c2618d8)
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
    
    def __init__(self):
        captureStack(self, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_7006e4c6)
    

def RuntimeException_init__Init_(_this):
    Exception_init__Init_(_this)
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_c59c954
    return _this

def RuntimeException_init__Create_():
    tmp = RuntimeException_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_4f4ba1ea)
    return tmp

def RuntimeException_init__Init_(message, _this):
    Exception_init__Init_(message, _this)
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_74f41fd2
    return _this

def RuntimeException_init__Create_(message):
    tmp = RuntimeException_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_2cdaf44c)
    return tmp

def RuntimeException_init__Init_(message, cause, _this):
    Exception_init__Init_(message, cause, _this)
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_1ab3f085
    return _this

def RuntimeException_init__Create_(message, cause):
    tmp = RuntimeException_init__Init_(message, cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_2c9e9116)
    return tmp

def RuntimeException_init__Init_(cause, _this):
    Exception_init__Init_(cause, _this)
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_198d6bc7
    return _this

def RuntimeException_init__Create_(cause):
    tmp = RuntimeException_init__Init_(cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_4ef3a9c3)
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
    
    def __init__(self):
        captureStack(self, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_6b828f7b)
    

def NoSuchElementException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_109d51e8
    return _this

def NoSuchElementException_init__Create_():
    tmp = NoSuchElementException_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_1ae0fde4)
    return tmp

def NoSuchElementException_init__Init_(message, _this):
    RuntimeException_init__Init_(message, _this)
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_31f656e6
    return _this

def NoSuchElementException_init__Create_(message):
    tmp = NoSuchElementException_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_25b20814)
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
    
    def __init__(self):
        captureStack(self, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_172c9256)
    

def IllegalStateException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_13a68fb7
    return _this

def IllegalStateException_init__Create_():
    tmp = IllegalStateException_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_5c6cf123)
    return tmp

def IllegalStateException_init__Init_(message, _this):
    RuntimeException_init__Init_(message, _this)
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_2d921c9
    return _this

def IllegalStateException_init__Create_(message):
    tmp = IllegalStateException_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_29e77b41)
    return tmp

def IllegalStateException_init__Init_(message, cause, _this):
    RuntimeException_init__Init_(message, cause, _this)
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_194a8a09
    return _this

def IllegalStateException_init__Create_(message, cause):
    tmp = IllegalStateException_init__Init_(message, cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_6b10123f)
    return tmp

def IllegalStateException_init__Init_(cause, _this):
    RuntimeException_init__Init_(cause, _this)
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_612bfb57
    return _this

def IllegalStateException_init__Create_(cause):
    tmp = IllegalStateException_init__Init_(cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_5faea3cb)
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
    
    def __init__(self):
        captureStack(self, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_1100a8f6)
    

def IndexOutOfBoundsException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_2c7e1fce
    return _this

def IndexOutOfBoundsException_init__Create_():
    tmp = IndexOutOfBoundsException_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_208ac9b8)
    return tmp

def IndexOutOfBoundsException_init__Init_(message, _this):
    RuntimeException_init__Init_(message, _this)
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_728dfa37
    return _this

def IndexOutOfBoundsException_init__Create_(message):
    tmp = IndexOutOfBoundsException_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_732301d1)
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
    
    def __init__(self):
        captureStack(self, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_5af6fae9)
    

def UnsupportedOperationException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_713c4d95
    return _this

def UnsupportedOperationException_init__Create_():
    tmp = UnsupportedOperationException_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_48895b1d)
    return tmp

def UnsupportedOperationException_init__Init_(message, _this):
    RuntimeException_init__Init_(message, _this)
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_7a217059
    return _this

def UnsupportedOperationException_init__Create_(message):
    tmp = UnsupportedOperationException_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_4a03acb6)
    return tmp

def UnsupportedOperationException_init__Init_(message, cause, _this):
    RuntimeException_init__Init_(message, cause, _this)
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_2f6b2a01
    return _this

def UnsupportedOperationException_init__Create_(message, cause):
    tmp = UnsupportedOperationException_init__Init_(message, cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_73f0d4f)
    return tmp

def UnsupportedOperationException_init__Init_(cause, _this):
    RuntimeException_init__Init_(cause, _this)
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_2e365bd3
    return _this

def UnsupportedOperationException_init__Create_(cause):
    tmp = UnsupportedOperationException_init__Init_(cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_3005644e)
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
    
    def __init__(self):
        captureStack(self, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_5dfeb2e3)
    

def NullPointerException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_47f309d8
    return _this

def NullPointerException_init__Create_():
    tmp = NullPointerException_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_5861c89)
    return tmp

def NullPointerException_init__Init_(message, _this):
    RuntimeException_init__Init_(message, _this)
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_7577843e
    return _this

def NullPointerException_init__Create_(message):
    tmp = NullPointerException_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_f0ca75)
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
    
    def __init__(self):
        captureStack(self, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_3ed6437b)
    

def NoWhenBranchMatchedException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_552f3c3b
    return _this

def NoWhenBranchMatchedException_init__Create_():
    tmp = NoWhenBranchMatchedException_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_453ccc85)
    return tmp

def NoWhenBranchMatchedException_init__Init_(message, _this):
    RuntimeException_init__Init_(message, _this)
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_11fe2600
    return _this

def NoWhenBranchMatchedException_init__Create_(message):
    tmp = NoWhenBranchMatchedException_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_29b343c7)
    return tmp

def NoWhenBranchMatchedException_init__Init_(message, cause, _this):
    RuntimeException_init__Init_(message, cause, _this)
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_7c77f8a9
    return _this

def NoWhenBranchMatchedException_init__Create_(message, cause):
    tmp = NoWhenBranchMatchedException_init__Init_(message, cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_b4e52a4)
    return tmp

def NoWhenBranchMatchedException_init__Init_(cause, _this):
    RuntimeException_init__Init_(cause, _this)
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_2ae1e7e0
    return _this

def NoWhenBranchMatchedException_init__Create_(cause):
    tmp = NoWhenBranchMatchedException_init__Init_(cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_7ae87fbe)
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
    
    def __init__(self):
        captureStack(self, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_4e9e4145)
    

def ClassCastException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_315441a6
    return _this

def ClassCastException_init__Create_():
    tmp = ClassCastException_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_5bced7f6)
    return tmp

def ClassCastException_init__Init_(message, _this):
    RuntimeException_init__Init_(message, _this)
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_3e4c4911
    return _this

def ClassCastException_init__Create_(message):
    tmp = ClassCastException_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_1493c922)
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
    
    def __init__(self):
        captureStack(self, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_6abb34a5)
    

def UninitializedPropertyAccessException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_44e8d9dc
    return _this

def UninitializedPropertyAccessException_init__Create_():
    tmp = UninitializedPropertyAccessException_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_44a4829b)
    return tmp

def UninitializedPropertyAccessException_init__Init_(message, _this):
    RuntimeException_init__Init_(message, _this)
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_2d6911a9
    return _this

def UninitializedPropertyAccessException_init__Create_(message):
    tmp = UninitializedPropertyAccessException_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_31d26296)
    return tmp

def UninitializedPropertyAccessException_init__Init_(message, cause, _this):
    RuntimeException_init__Init_(message, cause, _this)
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_5acf7f12
    return _this

def UninitializedPropertyAccessException_init__Create_(message, cause):
    tmp = UninitializedPropertyAccessException_init__Init_(message, cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_5ab0260)
    return tmp

def UninitializedPropertyAccessException_init__Init_(cause, _this):
    RuntimeException_init__Init_(cause, _this)
    visitDelegatingConstructorCall_org_jetbrains_kotlin_ir_expressions_impl_IrDelegatingConstructorCallImpl_6603902b
    return _this

def UninitializedPropertyAccessException_init__Create_(cause):
    tmp = UninitializedPropertyAccessException_init__Init_(cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_6d5a8e08)
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
    
    def __init__(self):
        captureStack(self, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl_63fbb062)
    

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
    fruits = listOf(arrayLiteral(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrVarargImpl_6612d9aa))
    tmp0_iterator = fruits.iterator()
    while tmp0_iterator.hasNext():
        x = tmp0_iterator.next()
        println(x)
    

class TestClass:
    def __init__(self, classParameter):
        self.classParameter = classParameter
    
    def _get_classParameter_(self):
        return self.classParameter
    
    def getSomeString(self):
        return 'Hello from Kotlin class!'
    
    def functionReturningClassParameter(self):
        return self.classParameter
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def returnString():
    return 'Hello from Kotlin!'

def returnStringFromClass():
    testClass = TestClass('paramVal')
    return testClass.getSomeString()

def returnParameterFromClass():
    return TestClass('paramVal').functionReturningClassParameter()
