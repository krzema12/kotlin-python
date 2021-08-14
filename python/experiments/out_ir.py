def fold(initial, operation):
    accumulator = initial
    indexedObject = self
    inductionVariable = 0
    last = len(indexedObject)
    while inductionVariable < last:
        element = indexedObject[inductionVariable]
        inductionVariable = (inductionVariable + 1) | 0
        accumulator = operation.invoke(accumulator, element)
    
    return accumulator

def contains(element):
    return indexOf(element) >= 0

def indexOf(element):
    inductionVariable = 0
    last = (len(self) - 1) | 0
    if inductionVariable <= last:
        while True:
            index = inductionVariable
            inductionVariable = (inductionVariable + 1) | 0
            if kotlin_Int(element) == kotlin_Int(self[index]):
                return index
            
            if inductionVariable <= last:
                break
            
        
    
    return -1

def _get_indices_():
    return IntRange(0, _get_lastIndex_())

def _get_lastIndex_():
    return (len(self) - 1) | 0

def contains(element):
    return indexOf(element) >= 0

def indexOf(element):
    inductionVariable = 0
    last = (len(self) - 1) | 0
    if inductionVariable <= last:
        while True:
            index = inductionVariable
            inductionVariable = (inductionVariable + 1) | 0
            if kotlin_Int(element) == kotlin_Int(self[index]):
                return index
            
            if inductionVariable <= last:
                break
            
        
    
    return -1

def _get_indices_():
    return IntRange(0, _get_lastIndex_())

def _get_lastIndex_():
    return (len(self) - 1) | 0

def contains(element):
    return indexOf(element) >= 0

def indexOf(element):
    inductionVariable = 0
    last = (len(self) - 1) | 0
    if inductionVariable <= last:
        while True:
            index = inductionVariable
            inductionVariable = (inductionVariable + 1) | 0
            if element == self[index]:
                return index
            
            if inductionVariable <= last:
                break
            
        
    
    return -1

def _get_indices_():
    return IntRange(0, _get_lastIndex_())

def _get_lastIndex_():
    return (len(self) - 1) | 0

def contains(element):
    return indexOf(element) >= 0

def indexOf(element):
    inductionVariable = 0
    last = (len(self) - 1) | 0
    if inductionVariable <= last:
        while True:
            index = inductionVariable
            inductionVariable = (inductionVariable + 1) | 0
            if element.equals(self[index]):
                return index
            
            if inductionVariable <= last:
                break
            
        
    
    return -1

def _get_indices_():
    return IntRange(0, _get_lastIndex_())

def _get_lastIndex_():
    return (len(self) - 1) | 0

def _get_indices_():
    return IntRange(0, _get_lastIndex_())

def indexOf(element):
    if element == None:
        inductionVariable = 0
        last = (len(self) - 1) | 0
        if inductionVariable <= last:
            while True:
                index = inductionVariable
                inductionVariable = (inductionVariable + 1) | 0
                if self[index] == None:
                    return index
                
                if inductionVariable <= last:
                    break
                
            
        
    else:
        inductionVariable = 0
        last = (len(self) - 1) | 0
        if inductionVariable <= last:
            while True:
                index = inductionVariable
                inductionVariable = (inductionVariable + 1) | 0
                if equals(element, self[index]):
                    return index
                
                if inductionVariable <= last:
                    break
                
            
        
    
    return -1

def lastIndexOf(element):
    if element == None:
        inductionVariable = (len(self) - 1) | 0
        if 0 <= inductionVariable:
            while True:
                index = inductionVariable
                inductionVariable = (inductionVariable + -1) | 0
                if self[index] == None:
                    return index
                
                if 0 <= inductionVariable:
                    break
                
            
        
    else:
        inductionVariable = (len(self) - 1) | 0
        if 0 <= inductionVariable:
            while True:
                index = inductionVariable
                inductionVariable = (inductionVariable + -1) | 0
                if equals(element, self[index]):
                    return index
                
                if 0 <= inductionVariable:
                    break
                
            
        
    
    return -1

def _get_lastIndex_():
    return (len(self) - 1) | 0

def joinToString(separator, prefix, postfix, limit, truncated, transform):
    return joinTo(StringBuilder_init__Create_(), separator, prefix, postfix, limit, truncated, transform).toString()

def joinToString_default(separator, prefix, postfix, limit, truncated, transform, _mask0, _handler):
    if not (_mask0 & 1 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    if not (_mask0 & 2 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    if not (_mask0 & 4 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    if not (_mask0 & 8 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    if not (_mask0 & 16 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    if not (_mask0 & 32 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    return joinToString(kotlin_CharSequence(separator), kotlin_CharSequence(prefix), kotlin_CharSequence(postfix), limit, kotlin_CharSequence(truncated), transform)

def joinTo(buffer, separator, prefix, postfix, limit, truncated, transform):
    buffer.append(prefix)
    Unit_getInstance()
    count = 0
    indexedObject = self
    inductionVariable = 0
    last = len(indexedObject)
    while inductionVariable < last:
        element = indexedObject[inductionVariable]
        inductionVariable = (inductionVariable + 1) | 0
        count = (count + 1) | 0
        if count > 1:
            buffer.append(separator)
            Unit_getInstance()
        
        if (True) if (limit < 0) else (count <= limit):
            appendElement(element, transform)
        else:
            break
        
    
    if (count > limit) if (limit >= 0) else (False):
        buffer.append(truncated)
        Unit_getInstance()
    
    buffer.append(postfix)
    Unit_getInstance()
    return buffer

def joinTo_default(buffer, separator, prefix, postfix, limit, truncated, transform, _mask0, _handler):
    if not (_mask0 & 2 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    if not (_mask0 & 4 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    if not (_mask0 & 8 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    if not (_mask0 & 16 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    if not (_mask0 & 32 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    if not (_mask0 & 64 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    return joinTo(buffer, kotlin_CharSequence(separator), kotlin_CharSequence(prefix), kotlin_CharSequence(postfix), limit, kotlin_CharSequence(truncated), transform)

def all(predicate):
    if isInterface(self, jsClass()):
        tmp = kotlin_collections_Collection_T_(self).isEmpty()
    elif True:
        tmp = False
    
    if tmp:
        return True
    
    tmp0_iterator = self.iterator()
    while tmp0_iterator.hasNext():
        element = tmp0_iterator.next()
        if not predicate.invoke(element):
            return False
        
    
    return True

def joinToString(separator, prefix, postfix, limit, truncated, transform):
    return joinTo(StringBuilder_init__Create_(), separator, prefix, postfix, limit, truncated, transform).toString()

def joinToString_default(separator, prefix, postfix, limit, truncated, transform, _mask0, _handler):
    if not (_mask0 & 1 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    if not (_mask0 & 2 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    if not (_mask0 & 4 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    if not (_mask0 & 8 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    if not (_mask0 & 16 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    if not (_mask0 & 32 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    return joinToString(kotlin_CharSequence(separator), kotlin_CharSequence(prefix), kotlin_CharSequence(postfix), limit, kotlin_CharSequence(truncated), transform)

def joinTo(buffer, separator, prefix, postfix, limit, truncated, transform):
    buffer.append(prefix)
    Unit_getInstance()
    count = 0
    tmp0_iterator = self.iterator()
    while tmp0_iterator.hasNext():
        element = tmp0_iterator.next()
        count = (count + 1) | 0
        if count > 1:
            buffer.append(separator)
            Unit_getInstance()
        
        if (True) if (limit < 0) else (count <= limit):
            appendElement(element, transform)
        else:
            break
        
    
    if (count > limit) if (limit >= 0) else (False):
        buffer.append(truncated)
        Unit_getInstance()
    
    buffer.append(postfix)
    Unit_getInstance()
    return buffer

def joinTo_default(buffer, separator, prefix, postfix, limit, truncated, transform, _mask0, _handler):
    if not (_mask0 & 2 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    if not (_mask0 & 4 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    if not (_mask0 & 8 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    if not (_mask0 & 16 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    if not (_mask0 & 32 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    if not (_mask0 & 64 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    return joinTo(buffer, kotlin_CharSequence(separator), kotlin_CharSequence(prefix), kotlin_CharSequence(postfix), limit, kotlin_CharSequence(truncated), transform)

def indexOfFirst(predicate):
    index = 0
    tmp0_iterator = self.iterator()
    while tmp0_iterator.hasNext():
        item = tmp0_iterator.next()
        if predicate.invoke(item):
            return index
        
        tmp1 = index
        index = (tmp1 + 1) | 0
        Unit_getInstance()
    
    return -1

def indexOfLast(predicate):
    iterator = self.listIterator(self._get_size_())
    while iterator.hasPrevious():
        if predicate.invoke(iterator.previous()):
            return iterator.nextIndex()
        
    
    return -1

def any(predicate):
    if isInterface(self, jsClass()):
        tmp = kotlin_collections_Collection_T_(self).isEmpty()
    elif True:
        tmp = False
    
    if tmp:
        return False
    
    tmp0_iterator = self.iterator()
    while tmp0_iterator.hasNext():
        element = tmp0_iterator.next()
        if predicate.invoke(element):
            return True
        
    
    return False

def until(to):
    if to <= IntCompanionObject_getInstance().MIN_VALUE:
        return Companion_getInstance().EMPTY
    
    return numberRangeToNumber(self, kotlin_Int((to - 1) | 0))

def downTo(to):
    return Companion_getInstance().fromClosedRange(self, to, -1)

def reversed():
    return Companion_getInstance().fromClosedRange(self.last, self.first, -self.step | 0)

def getOrElse(index, defaultValue):
    return (charSequenceGet(self, index)) if ((index <= _get_lastIndex_()) if (index >= 0) else (False)) else (defaultValue.invoke(index))

def KotlinNothingValueException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    super()
    return _this

def KotlinNothingValueException_init__Create_():
    tmp = KotlinNothingValueException_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def KotlinNothingValueException_init__Init_(message, _this):
    RuntimeException_init__Init_(message, _this)
    super()
    return _this

def KotlinNothingValueException_init__Create_(message):
    tmp = KotlinNothingValueException_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def KotlinNothingValueException_init__Init_(message, cause, _this):
    RuntimeException_init__Init_(message, cause, _this)
    super()
    return _this

def KotlinNothingValueException_init__Create_(message, cause):
    tmp = KotlinNothingValueException_init__Init_(message, cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def KotlinNothingValueException_init__Init_(cause, _this):
    RuntimeException_init__Init_(cause, _this)
    super()
    return _this

def KotlinNothingValueException_init__Create_(cause):
    tmp = KotlinNothingValueException_init__Init_(cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
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
        captureStack(self, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    

def _get_code_():
    return self.toInt()

def Char(code):
    Companion_getInstance()
    tmp0__get_code__0 = Char(0)
    if code < tmp0__get_code__0.toInt():
        tmp = True
    elif True:
        Companion_getInstance()
        tmp1__get_code__0 = Char(65535)
        tmp = code > tmp1__get_code__0.toInt()
    
    if tmp:
        raise IllegalArgumentException_init__Create_(str('Invalid Char code: ') + str(code))
    
    return numberToChar(code)

pass
pass
def values():
    return Level_WARNING_getInstance()

def valueOf(value):
    if 'WARNING' == value:
        return Level_WARNING_getInstance()
    elif 'ERROR' == value:
        return Level_ERROR_getInstance()
    else:
        Level_initEntries()
        THROW_ISE()
    

pass
def Level_initEntries():
    if Level_entriesInitialized:
        return Unit_getInstance()
    
    Level_entriesInitialized = True
    Level_WARNING_instance = Level('WARNING', 0)
    Level_ERROR_instance = Level('ERROR', 1)

def Experimental_init__Init_(level, _mask0, _marker, _this):
    if not (_mask0 & 1 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    super(level)
    return _this

def Experimental_init__Create_(level, _mask0, _marker):
    return Experimental_init__Init_(level, _mask0, _marker, Object_create())

class Level:
    def __init__(self, name, ordinal):
        super(name, ordinal)
    
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
    def __init__(self, *markerClass):
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
    

pass
pass
def values():
    return Level_WARNING_getInstance()

def valueOf(value):
    if 'WARNING' == value:
        return Level_WARNING_getInstance()
    elif 'ERROR' == value:
        return Level_ERROR_getInstance()
    else:
        Level_initEntries()
        THROW_ISE()
    

pass
def Level_initEntries():
    if Level_entriesInitialized:
        return Unit_getInstance()
    
    Level_entriesInitialized = True
    Level_WARNING_instance = Level('WARNING', 0)
    Level_ERROR_instance = Level('ERROR', 1)

def RequiresOptIn_init__Init_(message, level, _mask0, _marker, _this):
    if not (_mask0 & 1 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    if not (_mask0 & 2 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    super(message, level)
    return _this

def RequiresOptIn_init__Create_(message, level, _mask0, _marker):
    return RequiresOptIn_init__Init_(message, level, _mask0, _marker, Object_create())

class Level:
    def __init__(self, name, ordinal):
        super(name, ordinal)
    
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
    def __init__(self, *markerClass):
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
        return ('(this Collection)') if (it is self.this_0) else (toString())
    
    def invoke(self, p1):
        return self.invoke((E(p1)) if ((True) if (p1 == None) else (isObject(p1))) else (THROW_CCE()))
    

class AbstractCollection:
    def __init__(self):
        pass
    
    def _get_size_(self):
        pass
    
    def iterator(self):
        pass
    
    def contains(self, element):
        while True:
            if isInterface(self, jsClass()):
                tmp = kotlin_collections_Collection_kotlin_Any__(self).isEmpty()
            elif True:
                tmp = False
            
            if tmp:
                tmp_ret_0 = False
                break
            
            tmp0_iterator_1 = self.iterator()
            while tmp0_iterator_1.hasNext():
                element_2 = tmp0_iterator_1.next()
                if equals(element_2, element):
                    tmp_ret_0 = True
                    break
                
            
            tmp_ret_0 = False
            if False:
                break
            
        
        return tmp_ret_0
    
    def containsAll(self, elements):
        while True:
            if isInterface(elements, jsClass()):
                tmp = kotlin_collections_Collection_kotlin_Any__(elements).isEmpty()
            elif True:
                tmp = False
            
            if tmp:
                tmp_ret_0 = True
                break
            
            tmp0_iterator_1 = elements.iterator()
            while tmp0_iterator_1.hasNext():
                element_2 = tmp0_iterator_1.next()
                if not self.contains(element_2):
                    tmp_ret_0 = False
                    break
                
            
            tmp_ret_0 = True
            if False:
                break
            
        
        return tmp_ret_0
    
    def isEmpty(self):
        return self._get_size_() == 0
    
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
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl

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
        super()
        self.list = list
        self.fromIndex = fromIndex
        self._size = 0
        Companion_getInstance().checkRangeIndexes(self.fromIndex, toIndex, self.list._get_size_())
        self._size = (toIndex - self.fromIndex) | 0
    
    def get(self, index):
        Companion_getInstance().checkElementIndex(index, self._size)
        return self.list.get((self.fromIndex + index) | 0)
    
    def _get_size_(self):
        return self._size
    
    def iterator(self):
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
    

class IteratorImpl:
    def __init__(self, _outer):
        self._this = _outer
        self.index = 0
    
    def _set_index_(self, _set___):
        self.index = _set___
    
    def _get_index_(self):
        return self.index
    
    def hasNext(self):
        return self.index < self._this._get_size_()
    
    def next(self):
        if not self.hasNext():
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl
        
        tmp0_this = self
        tmp1 = tmp0_this.index
        tmp0_this.index = (tmp1 + 1) | 0
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
        super(_outer)
        Companion_getInstance().checkPositionIndex(index, self._this._get_size_())
        self._set_index_(index)
    
    def hasPrevious(self):
        return self._get_index_() > 0
    
    def nextIndex(self):
        return self._get_index_()
    
    def previous(self):
        if not self.hasPrevious():
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl
        
        tmp0_this = self
        tmp0_this._set_index_((tmp0_this._get_index_() - 1) | 0)
        return self._this.get(tmp0_this._get_index_())
    
    def previousIndex(self):
        return (self._get_index_() - 1) | 0
    
    def _set_index_(self, _set___):
        pass
    
    def _get_index_(self):
        pass
    
    def hasNext(self):
        pass
    
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
    
    def checkElementIndex(self, index, size):
        if (True) if (index < 0) else (index >= size):
            raise IndexOutOfBoundsException_init__Create_(((str('index: ') + str(index)) + str(', size: ')) + str(size))
        
    
    def checkPositionIndex(self, index, size):
        if (True) if (index < 0) else (index > size):
            raise IndexOutOfBoundsException_init__Create_(((str('index: ') + str(index)) + str(', size: ')) + str(size))
        
    
    def checkRangeIndexes(self, fromIndex, toIndex, size):
        if (True) if (fromIndex < 0) else (toIndex > size):
            raise IndexOutOfBoundsException_init__Create_(((((str('fromIndex: ') + str(fromIndex)) + str(', toIndex: ')) + str(toIndex)) + str(', size: ')) + str(size))
        
        if fromIndex > toIndex:
            raise IllegalArgumentException_init__Create_(((str('fromIndex: ') + str(fromIndex)) + str(' > toIndex: ')) + str(toIndex))
        
    
    def checkBoundsIndexes(self, startIndex, endIndex, size):
        if (True) if (startIndex < 0) else (endIndex > size):
            raise IndexOutOfBoundsException_init__Create_(((((str('startIndex: ') + str(startIndex)) + str(', endIndex: ')) + str(endIndex)) + str(', size: ')) + str(size))
        
        if startIndex > endIndex:
            raise IllegalArgumentException_init__Create_(((str('startIndex: ') + str(startIndex)) + str(' > endIndex: ')) + str(endIndex))
        
    
    def orderedHashCode(self, c):
        hashCode = 1
        tmp0_iterator = c.iterator()
        while tmp0_iterator.hasNext():
            e = tmp0_iterator.next()
            tmp = imul(31, hashCode)
            tmp1_safe_receiver = e
            tmp2_elvis_lhs = (None) if (tmp1_safe_receiver == None) else (hashCode(tmp1_safe_receiver))
            hashCode = (tmp + ((0) if (tmp2_elvis_lhs == None) else (tmp2_elvis_lhs))) | 0
        
        return hashCode
    
    def orderedEquals(self, c, other):
        if not (c._get_size_() == other._get_size_()):
            return False
        
        otherIterator = other.iterator()
        tmp0_iterator = c.iterator()
        while tmp0_iterator.hasNext():
            elem = tmp0_iterator.next()
            elemOther = otherIterator.next()
            if not equals(elem, elemOther):
                return False
            
        
        return True
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

pass
def Companion_getInstance():
    if Companion_instance == None:
        Companion()
    
    return Companion_instance

class AbstractList:
    def __init__(self):
        Companion_getInstance()
        super()
    
    def _get_size_(self):
        pass
    
    def get(self, index):
        pass
    
    def iterator(self):
        return IteratorImpl(self)
    
    def indexOf(self, element):
        while True:
            index_1 = 0
            tmp0_iterator_2 = self.iterator()
            while tmp0_iterator_2.hasNext():
                item_3 = tmp0_iterator_2.next()
                if equals(item_3, element):
                    tmp_ret_0 = index_1
                    break
                
                tmp1_4 = index_1
                index_1 = (tmp1_4 + 1) | 0
                Unit_getInstance()
            
            tmp_ret_0 = -1
            if False:
                break
            
        
        return tmp_ret_0
    
    def lastIndexOf(self, element):
        while True:
            iterator_1 = self.listIterator(self._get_size_())
            while iterator_1.hasPrevious():
                tmp0__anonymous__2 = iterator_1.previous()
                if equals(tmp0__anonymous__2, element):
                    tmp_ret_0 = iterator_1.nextIndex()
                    break
                
            
            tmp_ret_0 = -1
            if False:
                break
            
        
        return tmp_ret_0
    
    def listIterator(self):
        return ListIteratorImpl(self, 0)
    
    def listIterator(self, index):
        return ListIteratorImpl(self, index)
    
    def subList(self, fromIndex, toIndex):
        return SubList(self, fromIndex, toIndex)
    
    def equals(self, other):
        if other is self:
            return True
        
        if not ((isInterface(other, jsClass())) if (not (other == None)) else (False)):
            return False
        
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
    

def _get_lastIndex_():
    return (self._get_size_() - 1) | 0

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
        if (isInterface(other, jsClass())) if (not (other == None)) else (False):
            tmp = kotlin_collections_List___(other).isEmpty()
        elif True:
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
        if not False:
            return False
        
        if False:
            tmp = kotlin_Nothing(element)
        elif True:
            tmp = THROW_CCE()
        
        return self.contains(tmp)
    
    def containsAll(self, elements):
        return elements.isEmpty()
    
    def containsAll(self, elements):
        return self.containsAll(elements)
    
    def get(self, index):
        raise IndexOutOfBoundsException_init__Create_((str('Empty list doesn\'t contain element at index ') + str(index)) + str('.'))
    
    def indexOf(self, element):
        return -1
    
    def indexOf(self, element):
        if not False:
            return -1
        
        if False:
            tmp = kotlin_Nothing(element)
        elif True:
            tmp = THROW_CCE()
        
        return self.indexOf(tmp)
    
    def lastIndexOf(self, element):
        return -1
    
    def lastIndexOf(self, element):
        if not False:
            return -1
        
        if False:
            tmp = kotlin_Nothing(element)
        elif True:
            tmp = THROW_CCE()
        
        return self.lastIndexOf(tmp)
    
    def iterator(self):
        return EmptyIterator_getInstance()
    
    def listIterator(self):
        return EmptyIterator_getInstance()
    
    def listIterator(self, index):
        if not (index == 0):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl
        
        return EmptyIterator_getInstance()
    
    def subList(self, fromIndex, toIndex):
        if (toIndex == 0) if (fromIndex == 0) else (False):
            return self
        
        raise IndexOutOfBoundsException_init__Create_(((str('fromIndex: ') + str(fromIndex)) + str(', toIndex: ')) + str(toIndex))
    

pass
def EmptyList_getInstance():
    if EmptyList_instance == None:
        EmptyList()
    
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
        raise NoSuchElementException_init__Create_()
    
    def previous(self):
        raise NoSuchElementException_init__Create_()
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

pass
def EmptyIterator_getInstance():
    if EmptyIterator_instance == None:
        EmptyIterator()
    
    return EmptyIterator_instance

def removeAll(predicate):
    return filterInPlace(predicate, True)

def removeAll(predicate):
    return filterInPlace(predicate, True)

def filterInPlace(predicate, predicateResultToRemove):
    if not isInterface(self, jsClass()):
        return filterInPlace(predicate, predicateResultToRemove)
    
    writeIndex = 0
    inductionVariable = 0
    last = _get_lastIndex_()
    if inductionVariable <= last:
        while True:
            readIndex = inductionVariable
            inductionVariable = (inductionVariable + 1) | 0
            element = self.get(readIndex)
            if predicate.invoke(element) == predicateResultToRemove:
                continue
            
            if not (writeIndex == readIndex):
                self.set(writeIndex, element)
                Unit_getInstance()
            
            tmp1 = writeIndex
            writeIndex = (tmp1 + 1) | 0
            Unit_getInstance()
            if not (readIndex == last):
                break
            
        
    
    if writeIndex < self._get_size_():
        inductionVariable = _get_lastIndex_()
        if writeIndex <= inductionVariable:
            while True:
                removeIndex = inductionVariable
                inductionVariable = (inductionVariable + -1) | 0
                self.removeAt(removeIndex)
                Unit_getInstance()
                if not (removeIndex == writeIndex):
                    break
                
            
        
        return True
    else:
        return False
    

def filterInPlace(predicate, predicateResultToRemove):
    result = False
    tmp0_with_0 = self.iterator()
    while tmp0_with_0.hasNext():
        if predicate.invoke(tmp0_with_0.next()) == predicateResultToRemove:
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
        if not (_mask0 & 2 == 0):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
        
        return (self.callsInPlace(_lambda, kotlin_contracts_InvocationKind(kind))) if (_handler == None) else (kotlin_Function2_kotlin_Function2_kotlin_Function2_kotlin_Function2_(_handler).invoke(_lambda, kind))
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def __init__(self):
        pass
    

pass
pass
pass
pass
def values():
    return InvocationKind_AT_MOST_ONCE_getInstance()

def valueOf(value):
    if 'AT_MOST_ONCE' == value:
        return InvocationKind_AT_MOST_ONCE_getInstance()
    elif 'AT_LEAST_ONCE' == value:
        return InvocationKind_AT_LEAST_ONCE_getInstance()
    elif 'EXACTLY_ONCE' == value:
        return InvocationKind_EXACTLY_ONCE_getInstance()
    elif 'UNKNOWN' == value:
        return InvocationKind_UNKNOWN_getInstance()
    else:
        InvocationKind_initEntries()
        THROW_ISE()
    

pass
def InvocationKind_initEntries():
    if InvocationKind_entriesInitialized:
        return Unit_getInstance()
    
    InvocationKind_entriesInitialized = True
    InvocationKind_AT_MOST_ONCE_instance = InvocationKind('AT_MOST_ONCE', 0)
    InvocationKind_AT_LEAST_ONCE_instance = InvocationKind('AT_LEAST_ONCE', 1)
    InvocationKind_EXACTLY_ONCE_instance = InvocationKind('EXACTLY_ONCE', 2)
    InvocationKind_UNKNOWN_instance = InvocationKind('UNKNOWN', 3)

class InvocationKind:
    def __init__(self, name, ordinal):
        super(name, ordinal)
    
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
    return self.resumeWith(_Result___init__impl_(createFailure(exception)))

def resume(value):
    tmp0_success_0 = Companion_getInstance()
    return self.resumeWith(_Result___init__impl_(value))

def _get_coroutineContext_():
    raise NotImplementedError('Implemented as intrinsic')

class _no_name_provided_:
    def __init__(self, _context, _resumeWith):
        self._context = _context
        self._resumeWith = _resumeWith
    
    def _get_context_(self):
        return self._context
    
    def resumeWith(self, result):
        return self._resumeWith.invoke(result)
    
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
    

pass
def Key_getInstance():
    if Key_instance == None:
        Key()
    
    return Key_instance

class ContinuationInterceptor:
    def interceptContinuation(self, continuation):
        pass
    
    def releaseInterceptedContinuation(self, continuation):
        pass
    
    def get(self, key):
        if jsInstanceOf(key, jsClass()):
            if kotlin_coroutines_AbstractCoroutineContextKey_____(key).isSubKey(self._get_key_()):
                tmp = kotlin_coroutines_AbstractCoroutineContextKey_____(key).tryCast(self)
                tmp = (E(tmp)) if ((isInterface(tmp, jsClass())) if (not (tmp == None)) else (False)) else (None)
            else:
                tmp = None
            
            return tmp
        
        if Key_getInstance() is key:
            tmp = (E(self)) if (isInterface(self, jsClass())) else (THROW_CCE())
        else:
            tmp = None
        
        return tmp
    
    def minusKey(self, key):
        if jsInstanceOf(key, jsClass()):
            return (EmptyCoroutineContext_getInstance()) if ((not (kotlin_coroutines_AbstractCoroutineContextKey_out_kotlin_coroutines_Element_out_kotlin_coroutines_Element_(key).tryCast(self) == None)) if (kotlin_coroutines_AbstractCoroutineContextKey_out_kotlin_coroutines_Element_out_kotlin_coroutines_Element_(key).isSubKey(self._get_key_())) else (False)) else (self)
        
        return (EmptyCoroutineContext_getInstance()) if (Key_getInstance() is key) else (self)
    
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
        if equals(self._get_key_(), key):
            tmp = (E(self)) if (isInterface(self, jsClass())) else (THROW_CCE())
        else:
            tmp = None
        
        return tmp
    
    def fold(self, initial, operation):
        return operation.invoke(initial, self)
    
    def minusKey(self, key):
        return (EmptyCoroutineContext_getInstance()) if (equals(self._get_key_(), key)) else (self)
    
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
        if removed is EmptyCoroutineContext_getInstance():
            tmp = element
        else:
            interceptor = removed.get(Key_getInstance())
            if interceptor == None:
                tmp = CombinedContext(removed, element)
            else:
                left = removed.minusKey(Key_getInstance())
                tmp = (CombinedContext(element, interceptor)) if (left is EmptyCoroutineContext_getInstance()) else (CombinedContext(CombinedContext(left, element), interceptor))
            
            tmp = tmp
        
        return tmp
    
    def invoke(self, p1, p2):
        tmp = (kotlin_coroutines_CoroutineContext(p1)) if ((isInterface(p1, jsClass())) if (not (p1 == None)) else (False)) else (THROW_CCE())
        return self.invoke(tmp, (kotlin_coroutines_Element(p2)) if ((isInterface(p2, jsClass())) if (not (p2 == None)) else (False)) else (THROW_CCE()))
    

class CoroutineContext:
    def get(self, key):
        pass
    
    def fold(self, initial, operation):
        pass
    
    def plus(self, context):
        if context is EmptyCoroutineContext_getInstance():
            tmp = self
        else:
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
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl

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
    

pass
def EmptyCoroutineContext_getInstance():
    if EmptyCoroutineContext_instance == None:
        EmptyCoroutineContext()
    
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
    

pass
def Companion_getInstance():
    if Companion_instance == None:
        Companion()
    
    return Companion_instance

def readResolve(_this):
    tmp0_fold_0 = _this.elements
    tmp1_fold_0 = EmptyCoroutineContext_getInstance()
    accumulator_1 = tmp1_fold_0
    indexedObject = tmp0_fold_0
    inductionVariable = 0
    last = len(indexedObject)
    while inductionVariable < last:
        element_3 = indexedObject[inductionVariable]
        inductionVariable = (inductionVariable + 1) | 0
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
        tmp0_elvis_lhs = (kotlin_coroutines_CombinedContext(tmp)) if (jsInstanceOf(tmp, jsClass())) else (None)
        if tmp0_elvis_lhs == None:
            return size
        else:
            tmp = tmp0_elvis_lhs
        
        cur = tmp
        tmp1 = size
        size = (tmp1 + 1) | 0
        Unit_getInstance()
    

def contains(_this, element):
    return equals(_this.get(element._get_key_()), element)

def containsAll(_this, context):
    cur = context
    while True:
        if not contains(_this, cur.element):
            return False
        
        next = cur.left
        if jsInstanceOf(next, jsClass()):
            cur = kotlin_coroutines_CombinedContext(next)
        elif True:
            return contains(_this, (kotlin_coroutines_Element(next)) if (isInterface(next, jsClass())) else (THROW_CCE()))
        
    

def writeReplace(_this):
    n = size(_this)
    elements = fillArrayVal(Array(n), None)
    index = _sharedBox_create(0)
    _this.fold(Unit_getInstance(), _no_name_provided__factory(elements, index))
    tmp0_check_0 = _sharedBox_read(index) == n
    if not tmp0_check_0:
        message_2 = 'Check failed.'
        raise IllegalStateException_init__Create_(toString(message_2))
    
    return Serialized((kotlin_Array_kotlin_coroutines_CoroutineContext_(elements)) if (isArray(elements)) else (THROW_CCE()))

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
        if charSequenceLength(acc) == 0:
            tmp = toString(element)
        elif True:
            tmp = (str(acc) + str(', ')) + str(element)
        
        return tmp
    
    def invoke(self, p1, p2):
        tmp = (kotlin_String(p1)) if ((jsTypeOf(p1) == 'string') if (not (p1 == None)) else (False)) else (THROW_CCE())
        return self.invoke(tmp, (kotlin_coroutines_Element(p2)) if ((isInterface(p2, jsClass())) if (not (p2 == None)) else (False)) else (THROW_CCE()))
    

class _no_name_provided_:
    def __init__(self, _elements, _index):
        self._elements = _elements
        self._index = _index
    
    def invoke(self, _anonymous_parameter_0_, element):
        tmp0 = _sharedBox_read(self._index)
        _sharedBox_write(self._index, (tmp0 + 1) | 0)
        self._elements.__setitem__(tmp0, element)
    
    def invoke(self, p1, p2):
        tmp = (kotlin_Unit(p1)) if (jsInstanceOf(p1, jsClass())) else (THROW_CCE())
        self.invoke(tmp, (kotlin_coroutines_Element(p2)) if ((isInterface(p2, jsClass())) if (not (p2 == None)) else (False)) else (THROW_CCE()))
        return Unit_getInstance()
    

class CombinedContext:
    def __init__(self, left, element):
        self.left = left
        self.element = element
    
    def get(self, key):
        cur = self
        while True:
            tmp0_safe_receiver = cur.element.get(key)
            if tmp0_safe_receiver == None:
                visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstImpl
            else:
                return tmp0_safe_receiver
            
            Unit_getInstance()
            next = cur.left
            if jsInstanceOf(next, jsClass()):
                cur = kotlin_coroutines_CombinedContext(next)
            elif True:
                return next.get(key)
            
        
    
    def fold(self, initial, operation):
        return operation.invoke(self.left.fold(initial, operation), self.element)
    
    def minusKey(self, key):
        tmp0_safe_receiver = self.element.get(key)
        if tmp0_safe_receiver == None:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstImpl
        else:
            return self.left
        
        Unit_getInstance()
        newLeft = self.left.minusKey(key)
        return (self) if (newLeft is self.left) else ((self.element) if (newLeft is EmptyCoroutineContext_getInstance()) else (CombinedContext(newLeft, self.element)))
    
    def equals(self, other):
        if self is other:
            tmp = True
        else:
            if jsInstanceOf(other, jsClass()):
                tmp = size(kotlin_coroutines_CombinedContext(other)) == size(self)
            elif True:
                tmp = False
            
            if tmp:
                tmp = containsAll(kotlin_coroutines_CombinedContext(other), self)
            elif True:
                tmp = False
            
            tmp = tmp
        
        return tmp
    
    def hashCode(self):
        return (hashCode(self.left) + hashCode(self.element)) | 0
    
    def toString(self):
        return ('[' + self.fold('', _no_name_provided__factory())) + ']'
    
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
        if jsInstanceOf(baseKey, jsClass()):
            tmp = kotlin_coroutines_AbstractCoroutineContextKey_____(baseKey).topmostKey
        elif True:
            tmp = baseKey
        
        tmp.topmostKey = tmp
    
    def tryCast(self, element):
        return self.safeCast.invoke(element)
    
    def isSubKey(self, key):
        return (True) if (key is self) else (self.topmostKey is key)
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl

def _no_name_provided__factory(_elements, _index):
    i = _no_name_provided_(_elements, _index)
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl

def _get_COROUTINE_SUSPENDED_():
    return CoroutineSingletons_COROUTINE_SUSPENDED_getInstance()

pass
pass
pass
def values():
    return CoroutineSingletons_COROUTINE_SUSPENDED_getInstance()

def valueOf(value):
    if 'COROUTINE_SUSPENDED' == value:
        return CoroutineSingletons_COROUTINE_SUSPENDED_getInstance()
    elif 'UNDECIDED' == value:
        return CoroutineSingletons_UNDECIDED_getInstance()
    elif 'RESUMED' == value:
        return CoroutineSingletons_RESUMED_getInstance()
    else:
        CoroutineSingletons_initEntries()
        THROW_ISE()
    

pass
def CoroutineSingletons_initEntries():
    if CoroutineSingletons_entriesInitialized:
        return Unit_getInstance()
    
    CoroutineSingletons_entriesInitialized = True
    CoroutineSingletons_COROUTINE_SUSPENDED_instance = CoroutineSingletons('COROUTINE_SUSPENDED', 0)
    CoroutineSingletons_UNDECIDED_instance = CoroutineSingletons('UNDECIDED', 1)
    CoroutineSingletons_RESUMED_instance = CoroutineSingletons('RESUMED', 2)

class CoroutineSingletons:
    def __init__(self, name, ordinal):
        super(name, ordinal)
    
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
    return toShort(kotlin_Int(self) & kotlin_Int(other))

def _or(other):
    return toShort(kotlin_Int(self) | kotlin_Int(other))

def xor(other):
    return toShort(kotlin_Int(self) ^ kotlin_Int(other))

def inv():
    return toShort(~kotlin_Int(self))

def _and(other):
    return toByte(kotlin_Int(self) & kotlin_Int(other))

def _or(other):
    return toByte(kotlin_Int(self) | kotlin_Int(other))

def xor(other):
    return toByte(kotlin_Int(self) ^ kotlin_Int(other))

def inv():
    return toByte(~kotlin_Int(self))

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
    if not (_mask0 & 2 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    if not (_mask0 & 4 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    if not (_mask0 & 8 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    if not (_mask0 & 16 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    super(version, message, level, versionKind, errorCode)
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
    

pass
pass
pass
def values():
    return RequireKotlinVersionKind_LANGUAGE_VERSION_getInstance()

def valueOf(value):
    if 'LANGUAGE_VERSION' == value:
        return RequireKotlinVersionKind_LANGUAGE_VERSION_getInstance()
    elif 'COMPILER_VERSION' == value:
        return RequireKotlinVersionKind_COMPILER_VERSION_getInstance()
    elif 'API_VERSION' == value:
        return RequireKotlinVersionKind_API_VERSION_getInstance()
    else:
        RequireKotlinVersionKind_initEntries()
        THROW_ISE()
    

pass
def RequireKotlinVersionKind_initEntries():
    if RequireKotlinVersionKind_entriesInitialized:
        return Unit_getInstance()
    
    RequireKotlinVersionKind_entriesInitialized = True
    RequireKotlinVersionKind_LANGUAGE_VERSION_instance = RequireKotlinVersionKind('LANGUAGE_VERSION', 0)
    RequireKotlinVersionKind_COMPILER_VERSION_instance = RequireKotlinVersionKind('COMPILER_VERSION', 1)
    RequireKotlinVersionKind_API_VERSION_instance = RequireKotlinVersionKind('API_VERSION', 2)

class RequireKotlinVersionKind:
    def __init__(self, name, ordinal):
        super(name, ordinal)
    
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
    

pass
def Companion_getInstance():
    if Companion_instance == None:
        Companion()
    
    return Companion_instance

class KTypeProjection:
    def __init__(self, variance, type):
        Companion_getInstance()
        self.variance = variance
        self.type = type
        tmp0_require_0 = self.variance == None == self.type == None
        if not tmp0_require_0:
            message_2 = ('Star projection must have no type specified.') if (self.variance == None) else ((str('The projection variance ') + str(self.variance)) + str(' requires type to be specified.'))
            raise IllegalArgumentException_init__Create_(toString(message_2))
        
    
    def _get_variance_(self):
        return self.variance
    
    def _get_type_(self):
        return self.type
    
    def toString(self):
        tmp0_subject = self.variance
        if tmp0_subject == None:
            tmp = '*'
        elif equals(tmp0_subject, KVariance_INVARIANT_getInstance()):
            tmp = toString()
        elif equals(tmp0_subject, KVariance_IN_getInstance()):
            tmp = str('in ') + str(self.type)
        elif equals(tmp0_subject, KVariance_OUT_getInstance()):
            tmp = str('out ') + str(self.type)
        else:
            noWhenBranchMatchedException()
        
        return tmp
    
    def component1(self):
        return self.variance
    
    def component2(self):
        return self.type
    
    def copy(self, variance, type):
        return KTypeProjection(variance, type)
    
    def copy_default(self, variance, type, _mask0, _handler):
        if not (_mask0 & 1 == 0):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
        
        if not (_mask0 & 2 == 0):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
        
        return self.copy(variance, type)
    
    def hashCode(self):
        result = (0) if (self.variance == None) else (self.variance.hashCode())
        result = (imul(result, 31) + ((0) if (self.type == None) else (hashCode(self.type)))) | 0
        return result
    
    def equals(self, other):
        if self is other:
            return True
        
        if not jsInstanceOf(other, jsClass()):
            return False
        
        tmp0_other_with_cast = (kotlin_reflect_KTypeProjection(other)) if (jsInstanceOf(other, jsClass())) else (THROW_CCE())
        if not equals(self.variance, tmp0_other_with_cast.variance):
            return False
        
        if not equals(self.type, tmp0_other_with_cast.type):
            return False
        
        return True
    

pass
pass
pass
def values():
    return KVariance_INVARIANT_getInstance()

def valueOf(value):
    if 'INVARIANT' == value:
        return KVariance_INVARIANT_getInstance()
    elif 'IN' == value:
        return KVariance_IN_getInstance()
    elif 'OUT' == value:
        return KVariance_OUT_getInstance()
    else:
        KVariance_initEntries()
        THROW_ISE()
    

pass
def KVariance_initEntries():
    if KVariance_entriesInitialized:
        return Unit_getInstance()
    
    KVariance_entriesInitialized = True
    KVariance_INVARIANT_instance = KVariance('INVARIANT', 0)
    KVariance_IN_instance = KVariance('IN', 1)
    KVariance_OUT_instance = KVariance('OUT', 2)

class KVariance:
    def __init__(self, name, ordinal):
        super(name, ordinal)
    
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
    if not (transform == None):
        self.append(transform.invoke(element))
        Unit_getInstance()
    elif (True) if (element == None) else (isCharSequence(element)):
        self.append(kotlin_CharSequence_(element))
        Unit_getInstance()
    elif jsInstanceOf(element, jsClass()):
        self.append(kotlin_Char(element))
        Unit_getInstance()
    elif True:
        self.append(toString())
        Unit_getInstance()
    

def isEmpty():
    return charSequenceLength(self) == 0

def _get_lastIndex_():
    return (charSequenceLength(self) - 1) | 0

def _get_UNDEFINED_RESULT_():
    init_properties_DeepRecursive_kt()
    return UNDEFINED_RESULT

UNDEFINED_RESULT = None
properties_initialized_DeepRecursive_kt = False
def init_properties_DeepRecursive_kt():
    global properties_initialized_DeepRecursive_kt
    if not properties_initialized_DeepRecursive_kt:
        properties_initialized_DeepRecursive_kt = True
        global UNDEFINED_RESULT
        tmp0_success_0 = Companion_getInstance()
        tmp1_success_0 = _get_COROUTINE_SUSPENDED_()
        UNDEFINED_RESULT = _Result___init__impl_(tmp1_success_0)
    

def check(value):
    if not value:
        message_2 = 'Check failed.'
        raise IllegalStateException_init__Create_(toString(message_2))
    

def check(value, lazyMessage):
    if not value:
        message = lazyMessage.invoke()
        raise IllegalStateException_init__Create_(toString(message))
    

def error(message):
    raise IllegalStateException_init__Create_(toString(message))

def require(value, lazyMessage):
    if not value:
        message = lazyMessage.invoke()
        raise IllegalArgumentException_init__Create_(toString(message))
    

def _Result___init__impl_(value):
    return kotlin_Result_T_(value)

def _Result___get_value__impl_(this):
    return this.value

def _Result___get_isSuccess__impl_(this):
    tmp = _Result___get_value__impl_(this)
    return not jsInstanceOf(tmp, jsClass())

def _Result___get_isFailure__impl_(this):
    tmp = _Result___get_value__impl_(this)
    return jsInstanceOf(tmp, jsClass())

def Result__getOrNull_impl(this):
    if _Result___get_isFailure__impl_(this):
        tmp = None
    else:
        tmp = _Result___get_value__impl_(this)
        tmp = (T(tmp)) if ((True) if (tmp == None) else (isObject(tmp))) else (THROW_CCE())
    
    return tmp

def Result__exceptionOrNull_impl(this):
    tmp0_subject = _Result___get_value__impl_(this)
    if jsInstanceOf(tmp0_subject, jsClass()):
        tmp = kotlin_Failure(_Result___get_value__impl_(this)).exception
    elif True:
        tmp = None
    
    return tmp

def Result__toString_impl(this):
    tmp0_subject = _Result___get_value__impl_(this)
    if jsInstanceOf(tmp0_subject, jsClass()):
        tmp = toString(_Result___get_value__impl_(this))
    elif True:
        tmp = (str('Success(') + str(_Result___get_value__impl_(this))) + str(')')
    
    return tmp

class Companion:
    def __init__(self):
        Companion_instance = self
    
    def success(self, value):
        return _Result___init__impl_(value)
    
    def failure(self, exception):
        return _Result___init__impl_(createFailure(exception))
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

pass
def Companion_getInstance():
    if Companion_instance == None:
        Companion()
    
    return Companion_instance

class Failure:
    def __init__(self, exception):
        self.exception = exception
    
    def _get_exception_(self):
        return self.exception
    
    def equals(self, other):
        if jsInstanceOf(other, jsClass()):
            tmp = equals(self.exception, kotlin_Failure(other).exception)
        elif True:
            tmp = False
        
        return tmp
    
    def hashCode(self):
        return hashCode(self.exception)
    
    def toString(self):
        return (str('Failure(') + str(self.exception)) + str(')')
    

def Result__hashCode_impl(this):
    return (0) if (this.value == None) else (hashCode(this.value))

def Result__equals_impl(this, other):
    if not jsInstanceOf(other, jsClass()):
        return False
    
    tmp0_other_with_cast = (other) if (jsInstanceOf(other, jsClass())) else (THROW_CCE())
    if not equals(this.value, tmp0_other_with_cast.value):
        return False
    
    return True

class Result:
    def __init__(self, value):
        Companion_getInstance()
        self.value = value
    
    def toString(self):
        return Result__toString_impl(self)
    
    def hashCode(self):
        return Result__hashCode_impl(self)
    
    def equals(self, other):
        return Result__equals_impl(self, other)
    

def createFailure(exception):
    return Failure(exception)

def getOrThrow():
    throwOnFailure()
    tmp = _Result___get_value__impl_(self)
    return (T(tmp)) if ((True) if (tmp == None) else (isObject(tmp))) else (THROW_CCE())

def throwOnFailure():
    tmp = _Result___get_value__impl_(self)
    if jsInstanceOf(tmp, jsClass()):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl
    

def run(block):
    return block.invoke()

def TODO():
    raise NotImplementedError_init__Create_(None, 1, None)

def NotImplementedError_init__Init_(message, _mask0, _marker, _this):
    if not (_mask0 & 1 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    super(message)
    return _this

def NotImplementedError_init__Create_(message, _mask0, _marker):
    tmp = NotImplementedError_init__Init_(message, _mask0, _marker, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

class NotImplementedError:
    def __init__(self, message):
        Error_init__Init_(message, self)
        captureStack(self, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    
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

def also(block):
    block.invoke(self)
    return self

def _with(receiver, block):
    return block.invoke(receiver)

def run(block):
    return block.invoke(self)

def apply(block):
    block.invoke(self)
    return self

def repeat(times, action):
    inductionVariable = 0
    if inductionVariable < times:
        while True:
            index = inductionVariable
            inductionVariable = (inductionVariable + 1) | 0
            action.invoke(index)
            if inductionVariable < times:
                break
            
        
    

def _UByte___init__impl_(data):
    return kotlin_UByte(data)

def _UByte___get_data__impl_(this):
    return this.data

class Companion:
    def __init__(self):
        Companion_instance = self
        self.MIN_VALUE = _UByte___init__impl_(0)
        self.MAX_VALUE = _UByte___init__impl_(-1)
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
    

pass
def Companion_getInstance():
    if Companion_instance == None:
        Companion()
    
    return Companion_instance

def UByte__compareTo_impl(this, other):
    tmp = kotlin_Int(_UByte___get_data__impl_(this)) & 255
    return compareTo(tmp, kotlin_Int(_UByte___get_data__impl_(other)) & 255)

def UByte__compareTo_impl(this, other):
    return UByte__compareTo_impl(this, (other) if (jsInstanceOf(other, jsClass())) else (THROW_CCE()))

def UByte__compareTo_impl(this, other):
    tmp = kotlin_Int(_UByte___get_data__impl_(this)) & 255
    return compareTo(tmp, kotlin_Int(_UShort___get_data__impl_(other)) & 65535)

def UByte__compareTo_impl(this, other):
    tmp0_compareTo_0 = _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(this)) & 255)
    return uintCompare(_UInt___get_data__impl_(tmp0_compareTo_0), _UInt___get_data__impl_(other))

def UByte__compareTo_impl(this, other):
    tmp0_compareTo_0 = _ULong___init__impl_(toLong(_UByte___get_data__impl_(this))._and(Long(255, 0)))
    return ulongCompare(_ULong___get_data__impl_(tmp0_compareTo_0), _ULong___get_data__impl_(other))

def UByte__plus_impl(this, other):
    tmp0_plus_0 = _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(this)) & 255)
    tmp1_plus_0 = _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(other)) & 255)
    return _UInt___init__impl_((_UInt___get_data__impl_(tmp0_plus_0) + _UInt___get_data__impl_(tmp1_plus_0)) | 0)

def UByte__plus_impl(this, other):
    tmp0_plus_0 = _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(this)) & 255)
    tmp1_plus_0 = _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(other)) & 65535)
    return _UInt___init__impl_((_UInt___get_data__impl_(tmp0_plus_0) + _UInt___get_data__impl_(tmp1_plus_0)) | 0)

def UByte__plus_impl(this, other):
    tmp0_plus_0 = _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(this)) & 255)
    return _UInt___init__impl_((_UInt___get_data__impl_(tmp0_plus_0) + _UInt___get_data__impl_(other)) | 0)

def UByte__plus_impl(this, other):
    tmp0_plus_0 = _ULong___init__impl_(toLong(_UByte___get_data__impl_(this))._and(Long(255, 0)))
    return _ULong___init__impl_(_ULong___get_data__impl_(tmp0_plus_0).plus(_ULong___get_data__impl_(other)))

def UByte__minus_impl(this, other):
    tmp0_minus_0 = _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(this)) & 255)
    tmp1_minus_0 = _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(other)) & 255)
    return _UInt___init__impl_((_UInt___get_data__impl_(tmp0_minus_0) - _UInt___get_data__impl_(tmp1_minus_0)) | 0)

def UByte__minus_impl(this, other):
    tmp0_minus_0 = _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(this)) & 255)
    tmp1_minus_0 = _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(other)) & 65535)
    return _UInt___init__impl_((_UInt___get_data__impl_(tmp0_minus_0) - _UInt___get_data__impl_(tmp1_minus_0)) | 0)

def UByte__minus_impl(this, other):
    tmp0_minus_0 = _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(this)) & 255)
    return _UInt___init__impl_((_UInt___get_data__impl_(tmp0_minus_0) - _UInt___get_data__impl_(other)) | 0)

def UByte__minus_impl(this, other):
    tmp0_minus_0 = _ULong___init__impl_(toLong(_UByte___get_data__impl_(this))._and(Long(255, 0)))
    return _ULong___init__impl_(_ULong___get_data__impl_(tmp0_minus_0).minus(_ULong___get_data__impl_(other)))

def UByte__times_impl(this, other):
    tmp0_times_0 = _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(this)) & 255)
    tmp1_times_0 = _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(other)) & 255)
    return _UInt___init__impl_(imul(_UInt___get_data__impl_(tmp0_times_0), _UInt___get_data__impl_(tmp1_times_0)))

def UByte__times_impl(this, other):
    tmp0_times_0 = _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(this)) & 255)
    tmp1_times_0 = _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(other)) & 65535)
    return _UInt___init__impl_(imul(_UInt___get_data__impl_(tmp0_times_0), _UInt___get_data__impl_(tmp1_times_0)))

def UByte__times_impl(this, other):
    tmp0_times_0 = _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(this)) & 255)
    return _UInt___init__impl_(imul(_UInt___get_data__impl_(tmp0_times_0), _UInt___get_data__impl_(other)))

def UByte__times_impl(this, other):
    tmp0_times_0 = _ULong___init__impl_(toLong(_UByte___get_data__impl_(this))._and(Long(255, 0)))
    return _ULong___init__impl_(_ULong___get_data__impl_(tmp0_times_0).times(_ULong___get_data__impl_(other)))

def UByte__div_impl(this, other):
    tmp0_div_0 = _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(this)) & 255)
    tmp1_div_0 = _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(other)) & 255)
    return uintDivide(tmp0_div_0, tmp1_div_0)

def UByte__div_impl(this, other):
    tmp0_div_0 = _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(this)) & 255)
    tmp1_div_0 = _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(other)) & 65535)
    return uintDivide(tmp0_div_0, tmp1_div_0)

def UByte__div_impl(this, other):
    tmp0_div_0 = _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(this)) & 255)
    return uintDivide(tmp0_div_0, other)

def UByte__div_impl(this, other):
    tmp0_div_0 = _ULong___init__impl_(toLong(_UByte___get_data__impl_(this))._and(Long(255, 0)))
    return ulongDivide(tmp0_div_0, other)

def UByte__rem_impl(this, other):
    tmp0_rem_0 = _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(this)) & 255)
    tmp1_rem_0 = _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(other)) & 255)
    return uintRemainder(tmp0_rem_0, tmp1_rem_0)

def UByte__rem_impl(this, other):
    tmp0_rem_0 = _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(this)) & 255)
    tmp1_rem_0 = _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(other)) & 65535)
    return uintRemainder(tmp0_rem_0, tmp1_rem_0)

def UByte__rem_impl(this, other):
    tmp0_rem_0 = _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(this)) & 255)
    return uintRemainder(tmp0_rem_0, other)

def UByte__rem_impl(this, other):
    tmp0_rem_0 = _ULong___init__impl_(toLong(_UByte___get_data__impl_(this))._and(Long(255, 0)))
    return ulongRemainder(tmp0_rem_0, other)

def UByte__floorDiv_impl(this, other):
    tmp0_floorDiv_0 = _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(this)) & 255)
    tmp1_floorDiv_0 = _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(other)) & 255)
    return uintDivide(tmp0_floorDiv_0, tmp1_floorDiv_0)

def UByte__floorDiv_impl(this, other):
    tmp0_floorDiv_0 = _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(this)) & 255)
    tmp1_floorDiv_0 = _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(other)) & 65535)
    return uintDivide(tmp0_floorDiv_0, tmp1_floorDiv_0)

def UByte__floorDiv_impl(this, other):
    tmp0_floorDiv_0 = _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(this)) & 255)
    return uintDivide(tmp0_floorDiv_0, other)

def UByte__floorDiv_impl(this, other):
    tmp0_floorDiv_0 = _ULong___init__impl_(toLong(_UByte___get_data__impl_(this))._and(Long(255, 0)))
    return ulongDivide(tmp0_floorDiv_0, other)

def UByte__mod_impl(this, other):
    tmp0_mod_0 = _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(this)) & 255)
    tmp1_mod_0 = _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(other)) & 255)
    tmp3_toUByte_0 = uintRemainder(tmp0_mod_0, tmp1_mod_0)
    tmp2_toUByte_0 = _UInt___get_data__impl_(tmp3_toUByte_0)
    return _UByte___init__impl_(toByte(tmp2_toUByte_0))

def UByte__mod_impl(this, other):
    tmp0_mod_0 = _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(this)) & 255)
    tmp1_mod_0 = _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(other)) & 65535)
    tmp3_toUShort_0 = uintRemainder(tmp0_mod_0, tmp1_mod_0)
    tmp2_toUShort_0 = _UInt___get_data__impl_(tmp3_toUShort_0)
    return _UShort___init__impl_(toShort(tmp2_toUShort_0))

def UByte__mod_impl(this, other):
    tmp0_mod_0 = _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(this)) & 255)
    return uintRemainder(tmp0_mod_0, other)

def UByte__mod_impl(this, other):
    tmp0_mod_0 = _ULong___init__impl_(toLong(_UByte___get_data__impl_(this))._and(Long(255, 0)))
    return ulongRemainder(tmp0_mod_0, other)

def UByte__inc_impl(this):
    return _UByte___init__impl_(numberToByte(_UByte___get_data__impl_(this) + 1))

def UByte__dec_impl(this):
    return _UByte___init__impl_(numberToByte(_UByte___get_data__impl_(this) - 1))

def UByte__rangeTo_impl(this, other):
    tmp = _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(this)) & 255)
    return UIntRange(tmp, _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(other)) & 255))

def UByte__and_impl(this, other):
    tmp0_and_0 = _UByte___get_data__impl_(this)
    tmp1_and_0 = _UByte___get_data__impl_(other)
    return _UByte___init__impl_(toByte(kotlin_Int(tmp0_and_0) & kotlin_Int(tmp1_and_0)))

def UByte__or_impl(this, other):
    tmp0_or_0 = _UByte___get_data__impl_(this)
    tmp1_or_0 = _UByte___get_data__impl_(other)
    return _UByte___init__impl_(toByte(kotlin_Int(tmp0_or_0) | kotlin_Int(tmp1_or_0)))

def UByte__xor_impl(this, other):
    tmp0_xor_0 = _UByte___get_data__impl_(this)
    tmp1_xor_0 = _UByte___get_data__impl_(other)
    return _UByte___init__impl_(toByte(kotlin_Int(tmp0_xor_0) ^ kotlin_Int(tmp1_xor_0)))

def UByte__inv_impl(this):
    tmp0_inv_0 = _UByte___get_data__impl_(this)
    return _UByte___init__impl_(toByte(~kotlin_Int(tmp0_inv_0)))

def UByte__toByte_impl(this):
    return _UByte___get_data__impl_(this)

def UByte__toShort_impl(this):
    tmp0_and_0 = kotlin_Short(_UByte___get_data__impl_(this))
    return toShort(kotlin_Int(tmp0_and_0) & 255)

def UByte__toInt_impl(this):
    return kotlin_Int(_UByte___get_data__impl_(this)) & 255

def UByte__toLong_impl(this):
    return toLong(_UByte___get_data__impl_(this))._and(Long(255, 0))

def UByte__toUByte_impl(this):
    return this

def UByte__toUShort_impl(this):
    tmp0_and_0 = kotlin_Short(_UByte___get_data__impl_(this))
    return _UShort___init__impl_(toShort(kotlin_Int(tmp0_and_0) & 255))

def UByte__toUInt_impl(this):
    return _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(this)) & 255)

def UByte__toULong_impl(this):
    return _ULong___init__impl_(toLong(_UByte___get_data__impl_(this))._and(Long(255, 0)))

def UByte__toFloat_impl(this):
    return kotlin_Float(kotlin_Int(_UByte___get_data__impl_(this)) & 255)

def UByte__toDouble_impl(this):
    return kotlin_Double(kotlin_Int(_UByte___get_data__impl_(this)) & 255)

def UByte__toString_impl(this):
    return (kotlin_Int(_UByte___get_data__impl_(this)) & 255).toString()

def UByte__hashCode_impl(this):
    return this.data

def UByte__equals_impl(this, other):
    if not jsInstanceOf(other, jsClass()):
        return False
    
    tmp0_other_with_cast = (other) if (jsInstanceOf(other, jsClass())) else (THROW_CCE())
    if not (this.data == tmp0_other_with_cast.data):
        return False
    
    return True

class UByte:
    def __init__(self, data):
        Companion_getInstance()
        self.data = data
    
    def compareTo(self, other):
        return UByte__compareTo_impl(self, other)
    
    def compareTo(self, other):
        return UByte__compareTo_impl(self, other)
    
    def toString(self):
        return UByte__toString_impl(self)
    
    def hashCode(self):
        return UByte__hashCode_impl(self)
    
    def equals(self, other):
        return UByte__equals_impl(self, other)
    

def toUByte():
    return _UByte___init__impl_(toByte(self))

def toUByte():
    return _UByte___init__impl_(toByte(self))

def toUByte():
    return _UByte___init__impl_(self.toByte())

def toUByte():
    return _UByte___init__impl_(self)

def _get_array_(_this):
    return _this.array

def _set_index_(_this, _set___):
    _this.index = _set___

def _get_index_(_this):
    return _this.index

def _UByteArray___init__impl_(storage):
    return kotlin_UByteArray(storage)

def _UByteArray___get_storage__impl_(this):
    return this.storage

def _UByteArray___init__impl_(size):
    tmp = _UByteArray___init__impl_(int8Array(size))
    return tmp

def UByteArray__get_impl(this, index):
    tmp0_toUByte_0 = _UByteArray___get_storage__impl_(this)[index]
    return _UByte___init__impl_(tmp0_toUByte_0)

def UByteArray__set_impl(this, index, value):
    tmp = _UByteArray___get_storage__impl_(this)
    tmp.__setitem__(index, _UByte___get_data__impl_(value))

def _UByteArray___get_size__impl_(this):
    return len(_UByteArray___get_storage__impl_(this))

def UByteArray__iterator_impl(this):
    return Iterator(_UByteArray___get_storage__impl_(this))

class Iterator:
    def __init__(self, array):
        super()
        self.array = array
        self.index = 0
    
    def hasNext(self):
        return self.index < len(self.array)
    
    def nextUByte(self):
        if self.index < len(self.array):
            tmp0_this = self
            tmp1 = tmp0_this.index
            tmp0_this.index = (tmp1 + 1) | 0
            tmp0_toUByte_0 = self.array[tmp1]
            tmp = _UByte___init__impl_(tmp0_toUByte_0)
        else:
            raise NoSuchElementException_init__Create_(self.index.toString())
        
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
    tmp = (element) if (isObject(element)) else (THROW_CCE())
    if not jsInstanceOf(tmp, jsClass()):
        return False
    
    tmp = _UByteArray___get_storage__impl_(this)
    return contains(_UByte___get_data__impl_(element))

def UByteArray__contains_impl(this, element):
    if not jsInstanceOf(element, jsClass()):
        return False
    
    return UByteArray__contains_impl(this, (element) if (jsInstanceOf(element, jsClass())) else (THROW_CCE()))

def UByteArray__containsAll_impl(this, elements):
    while True:
        tmp0_all_0 = (kotlin_collections_Collection___(elements)) if (isInterface(elements, jsClass())) else (THROW_CCE())
        if isInterface(tmp0_all_0, jsClass()):
            tmp = kotlin_collections_Collection_kotlin_Any__(tmp0_all_0).isEmpty()
        elif True:
            tmp = False
        
        if tmp:
            tmp_ret_0 = True
            break
        
        tmp0_iterator_1 = tmp0_all_0.iterator()
        while tmp0_iterator_1.hasNext():
            element_2 = tmp0_iterator_1.next()
            if jsInstanceOf(element_2, jsClass()):
                tmp = _UByteArray___get_storage__impl_(this)
                tmp0_toByte_0_4 = element_2
                tmp = contains(_UByte___get_data__impl_(tmp0_toByte_0_4))
            elif True:
                tmp = False
            
            if not tmp:
                tmp_ret_0 = False
                break
            
        
        tmp_ret_0 = True
        if False:
            break
        
    
    return tmp_ret_0

def UByteArray__containsAll_impl(this, elements):
    return UByteArray__containsAll_impl(this, elements)

def UByteArray__isEmpty_impl(this):
    return len(_UByteArray___get_storage__impl_(this)) == 0

def UByteArray__toString_impl(this):
    return (str('UByteArray(storage=') + str(toString(this.storage))) + str(')')

def UByteArray__hashCode_impl(this):
    return hashCode(this.storage)

def UByteArray__equals_impl(this, other):
    if not jsInstanceOf(other, jsClass()):
        return False
    
    tmp0_other_with_cast = (other) if (jsInstanceOf(other, jsClass())) else (THROW_CCE())
    if not equals(this.storage, tmp0_other_with_cast.storage):
        return False
    
    return True

class UByteArray:
    def __init__(self, storage):
        self.storage = storage
    
    def _get_size_(self):
        return _UByteArray___get_size__impl_(self)
    
    def iterator(self):
        return UByteArray__iterator_impl(self)
    
    def contains(self, element):
        return UByteArray__contains_impl(self, element)
    
    def contains(self, element):
        return UByteArray__contains_impl(self, element)
    
    def containsAll(self, elements):
        return UByteArray__containsAll_impl(self, elements)
    
    def containsAll(self, elements):
        return UByteArray__containsAll_impl(self, elements)
    
    def isEmpty(self):
        return UByteArray__isEmpty_impl(self)
    
    def toString(self):
        return UByteArray__toString_impl(self)
    
    def hashCode(self):
        return UByteArray__hashCode_impl(self)
    
    def equals(self, other):
        return UByteArray__equals_impl(self, other)
    

def _UInt___init__impl_(data):
    return kotlin_UInt(data)

def _UInt___get_data__impl_(this):
    return this.data

class Companion:
    def __init__(self):
        Companion_instance = self
        self.MIN_VALUE = _UInt___init__impl_(0)
        self.MAX_VALUE = _UInt___init__impl_(-1)
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
    

pass
def Companion_getInstance():
    if Companion_instance == None:
        Companion()
    
    return Companion_instance

def UInt__compareTo_impl(this, other):
    tmp0_compareTo_0 = _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(other)) & 255)
    return uintCompare(_UInt___get_data__impl_(this), _UInt___get_data__impl_(tmp0_compareTo_0))

def UInt__compareTo_impl(this, other):
    tmp0_compareTo_0 = _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(other)) & 65535)
    return uintCompare(_UInt___get_data__impl_(this), _UInt___get_data__impl_(tmp0_compareTo_0))

def UInt__compareTo_impl(this, other):
    return uintCompare(_UInt___get_data__impl_(this), _UInt___get_data__impl_(other))

def UInt__compareTo_impl(this, other):
    return UInt__compareTo_impl(this, (other) if (jsInstanceOf(other, jsClass())) else (THROW_CCE()))

def UInt__compareTo_impl(this, other):
    tmp0_compareTo_0 = _ULong___init__impl_(toLong(_UInt___get_data__impl_(this))._and(Long(-1, 0)))
    return ulongCompare(_ULong___get_data__impl_(tmp0_compareTo_0), _ULong___get_data__impl_(other))

def UInt__plus_impl(this, other):
    tmp0_plus_0 = _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(other)) & 255)
    return _UInt___init__impl_((_UInt___get_data__impl_(this) + _UInt___get_data__impl_(tmp0_plus_0)) | 0)

def UInt__plus_impl(this, other):
    tmp0_plus_0 = _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(other)) & 65535)
    return _UInt___init__impl_((_UInt___get_data__impl_(this) + _UInt___get_data__impl_(tmp0_plus_0)) | 0)

def UInt__plus_impl(this, other):
    return _UInt___init__impl_((_UInt___get_data__impl_(this) + _UInt___get_data__impl_(other)) | 0)

def UInt__plus_impl(this, other):
    tmp0_plus_0 = _ULong___init__impl_(toLong(_UInt___get_data__impl_(this))._and(Long(-1, 0)))
    return _ULong___init__impl_(_ULong___get_data__impl_(tmp0_plus_0).plus(_ULong___get_data__impl_(other)))

def UInt__minus_impl(this, other):
    tmp0_minus_0 = _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(other)) & 255)
    return _UInt___init__impl_((_UInt___get_data__impl_(this) - _UInt___get_data__impl_(tmp0_minus_0)) | 0)

def UInt__minus_impl(this, other):
    tmp0_minus_0 = _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(other)) & 65535)
    return _UInt___init__impl_((_UInt___get_data__impl_(this) - _UInt___get_data__impl_(tmp0_minus_0)) | 0)

def UInt__minus_impl(this, other):
    return _UInt___init__impl_((_UInt___get_data__impl_(this) - _UInt___get_data__impl_(other)) | 0)

def UInt__minus_impl(this, other):
    tmp0_minus_0 = _ULong___init__impl_(toLong(_UInt___get_data__impl_(this))._and(Long(-1, 0)))
    return _ULong___init__impl_(_ULong___get_data__impl_(tmp0_minus_0).minus(_ULong___get_data__impl_(other)))

def UInt__times_impl(this, other):
    tmp0_times_0 = _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(other)) & 255)
    return _UInt___init__impl_(imul(_UInt___get_data__impl_(this), _UInt___get_data__impl_(tmp0_times_0)))

def UInt__times_impl(this, other):
    tmp0_times_0 = _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(other)) & 65535)
    return _UInt___init__impl_(imul(_UInt___get_data__impl_(this), _UInt___get_data__impl_(tmp0_times_0)))

def UInt__times_impl(this, other):
    return _UInt___init__impl_(imul(_UInt___get_data__impl_(this), _UInt___get_data__impl_(other)))

def UInt__times_impl(this, other):
    tmp0_times_0 = _ULong___init__impl_(toLong(_UInt___get_data__impl_(this))._and(Long(-1, 0)))
    return _ULong___init__impl_(_ULong___get_data__impl_(tmp0_times_0).times(_ULong___get_data__impl_(other)))

def UInt__div_impl(this, other):
    tmp0_div_0 = _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(other)) & 255)
    return uintDivide(this, tmp0_div_0)

def UInt__div_impl(this, other):
    tmp0_div_0 = _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(other)) & 65535)
    return uintDivide(this, tmp0_div_0)

def UInt__div_impl(this, other):
    return uintDivide(this, other)

def UInt__div_impl(this, other):
    tmp0_div_0 = _ULong___init__impl_(toLong(_UInt___get_data__impl_(this))._and(Long(-1, 0)))
    return ulongDivide(tmp0_div_0, other)

def UInt__rem_impl(this, other):
    tmp0_rem_0 = _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(other)) & 255)
    return uintRemainder(this, tmp0_rem_0)

def UInt__rem_impl(this, other):
    tmp0_rem_0 = _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(other)) & 65535)
    return uintRemainder(this, tmp0_rem_0)

def UInt__rem_impl(this, other):
    return uintRemainder(this, other)

def UInt__rem_impl(this, other):
    tmp0_rem_0 = _ULong___init__impl_(toLong(_UInt___get_data__impl_(this))._and(Long(-1, 0)))
    return ulongRemainder(tmp0_rem_0, other)

def UInt__floorDiv_impl(this, other):
    tmp0_floorDiv_0 = _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(other)) & 255)
    return uintDivide(this, tmp0_floorDiv_0)

def UInt__floorDiv_impl(this, other):
    tmp0_floorDiv_0 = _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(other)) & 65535)
    return uintDivide(this, tmp0_floorDiv_0)

def UInt__floorDiv_impl(this, other):
    return uintDivide(this, other)

def UInt__floorDiv_impl(this, other):
    tmp0_floorDiv_0 = _ULong___init__impl_(toLong(_UInt___get_data__impl_(this))._and(Long(-1, 0)))
    return ulongDivide(tmp0_floorDiv_0, other)

def UInt__mod_impl(this, other):
    tmp0_mod_0 = _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(other)) & 255)
    tmp2_toUByte_0 = uintRemainder(this, tmp0_mod_0)
    tmp1_toUByte_0 = _UInt___get_data__impl_(tmp2_toUByte_0)
    return _UByte___init__impl_(toByte(tmp1_toUByte_0))

def UInt__mod_impl(this, other):
    tmp0_mod_0 = _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(other)) & 65535)
    tmp2_toUShort_0 = uintRemainder(this, tmp0_mod_0)
    tmp1_toUShort_0 = _UInt___get_data__impl_(tmp2_toUShort_0)
    return _UShort___init__impl_(toShort(tmp1_toUShort_0))

def UInt__mod_impl(this, other):
    return uintRemainder(this, other)

def UInt__mod_impl(this, other):
    tmp0_mod_0 = _ULong___init__impl_(toLong(_UInt___get_data__impl_(this))._and(Long(-1, 0)))
    return ulongRemainder(tmp0_mod_0, other)

def UInt__inc_impl(this):
    return _UInt___init__impl_((_UInt___get_data__impl_(this) + 1) | 0)

def UInt__dec_impl(this):
    return _UInt___init__impl_((_UInt___get_data__impl_(this) - 1) | 0)

def UInt__rangeTo_impl(this, other):
    return UIntRange(this, other)

def UInt__shl_impl(this, bitCount):
    return _UInt___init__impl_(_UInt___get_data__impl_(this) << bitCount)

def UInt__shr_impl(this, bitCount):
    return _UInt___init__impl_(jsBitShiftRU(_UInt___get_data__impl_(this), bitCount))

def UInt__and_impl(this, other):
    return _UInt___init__impl_(_UInt___get_data__impl_(this) & _UInt___get_data__impl_(other))

def UInt__or_impl(this, other):
    return _UInt___init__impl_(_UInt___get_data__impl_(this) | _UInt___get_data__impl_(other))

def UInt__xor_impl(this, other):
    return _UInt___init__impl_(_UInt___get_data__impl_(this) ^ _UInt___get_data__impl_(other))

def UInt__inv_impl(this):
    return _UInt___init__impl_(~_UInt___get_data__impl_(this))

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
    return _UByte___init__impl_(toByte(tmp0_toUByte_0))

def UInt__toUShort_impl(this):
    tmp0_toUShort_0 = _UInt___get_data__impl_(this)
    return _UShort___init__impl_(toShort(tmp0_toUShort_0))

def UInt__toUInt_impl(this):
    return this

def UInt__toULong_impl(this):
    return _ULong___init__impl_(toLong(_UInt___get_data__impl_(this))._and(Long(-1, 0)))

def UInt__toFloat_impl(this):
    return kotlin_Float(uintToDouble(_UInt___get_data__impl_(this)))

def UInt__toDouble_impl(this):
    return uintToDouble(_UInt___get_data__impl_(this))

def UInt__toString_impl(this):
    return toLong(_UInt___get_data__impl_(this))._and(Long(-1, 0)).toString()

def UInt__hashCode_impl(this):
    return this.data

def UInt__equals_impl(this, other):
    if not jsInstanceOf(other, jsClass()):
        return False
    
    tmp0_other_with_cast = (other) if (jsInstanceOf(other, jsClass())) else (THROW_CCE())
    if not (this.data == tmp0_other_with_cast.data):
        return False
    
    return True

class UInt:
    def __init__(self, data):
        Companion_getInstance()
        self.data = data
    
    def compareTo(self, other):
        return UInt__compareTo_impl(self, other)
    
    def compareTo(self, other):
        return UInt__compareTo_impl(self, other)
    
    def toString(self):
        return UInt__toString_impl(self)
    
    def hashCode(self):
        return UInt__hashCode_impl(self)
    
    def equals(self, other):
        return UInt__equals_impl(self, other)
    

def toUInt():
    return _UInt___init__impl_(self.toInt())

def toUInt():
    return _UInt___init__impl_(self)

def toUInt():
    return _UInt___init__impl_(kotlin_Int(self))

def toUInt():
    return doubleToUInt(self)

def toUInt():
    return doubleToUInt(kotlin_Double(self))

def toUInt():
    return _UInt___init__impl_(kotlin_Int(self))

def _get_array_(_this):
    return _this.array

def _set_index_(_this, _set___):
    _this.index = _set___

def _get_index_(_this):
    return _this.index

def _UIntArray___init__impl_(storage):
    return kotlin_UIntArray(storage)

def _UIntArray___get_storage__impl_(this):
    return this.storage

def _UIntArray___init__impl_(size):
    tmp = _UIntArray___init__impl_(int32Array(size))
    return tmp

def UIntArray__get_impl(this, index):
    tmp0_toUInt_0 = _UIntArray___get_storage__impl_(this)[index]
    return _UInt___init__impl_(tmp0_toUInt_0)

def UIntArray__set_impl(this, index, value):
    tmp = _UIntArray___get_storage__impl_(this)
    tmp.__setitem__(index, _UInt___get_data__impl_(value))

def _UIntArray___get_size__impl_(this):
    return len(_UIntArray___get_storage__impl_(this))

def UIntArray__iterator_impl(this):
    return Iterator(_UIntArray___get_storage__impl_(this))

class Iterator:
    def __init__(self, array):
        super()
        self.array = array
        self.index = 0
    
    def hasNext(self):
        return self.index < len(self.array)
    
    def nextUInt(self):
        if self.index < len(self.array):
            tmp0_this = self
            tmp1 = tmp0_this.index
            tmp0_this.index = (tmp1 + 1) | 0
            tmp0_toUInt_0 = self.array[tmp1]
            tmp = _UInt___init__impl_(tmp0_toUInt_0)
        else:
            raise NoSuchElementException_init__Create_(self.index.toString())
        
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
    tmp = (element) if (isObject(element)) else (THROW_CCE())
    if not jsInstanceOf(tmp, jsClass()):
        return False
    
    tmp = _UIntArray___get_storage__impl_(this)
    return contains(_UInt___get_data__impl_(element))

def UIntArray__contains_impl(this, element):
    if not jsInstanceOf(element, jsClass()):
        return False
    
    return UIntArray__contains_impl(this, (element) if (jsInstanceOf(element, jsClass())) else (THROW_CCE()))

def UIntArray__containsAll_impl(this, elements):
    while True:
        tmp0_all_0 = (kotlin_collections_Collection___(elements)) if (isInterface(elements, jsClass())) else (THROW_CCE())
        if isInterface(tmp0_all_0, jsClass()):
            tmp = kotlin_collections_Collection_kotlin_Any__(tmp0_all_0).isEmpty()
        elif True:
            tmp = False
        
        if tmp:
            tmp_ret_0 = True
            break
        
        tmp0_iterator_1 = tmp0_all_0.iterator()
        while tmp0_iterator_1.hasNext():
            element_2 = tmp0_iterator_1.next()
            if jsInstanceOf(element_2, jsClass()):
                tmp = _UIntArray___get_storage__impl_(this)
                tmp0_toInt_0_4 = element_2
                tmp = contains(_UInt___get_data__impl_(tmp0_toInt_0_4))
            elif True:
                tmp = False
            
            if not tmp:
                tmp_ret_0 = False
                break
            
        
        tmp_ret_0 = True
        if False:
            break
        
    
    return tmp_ret_0

def UIntArray__containsAll_impl(this, elements):
    return UIntArray__containsAll_impl(this, elements)

def UIntArray__isEmpty_impl(this):
    return len(_UIntArray___get_storage__impl_(this)) == 0

def UIntArray__toString_impl(this):
    return (str('UIntArray(storage=') + str(toString(this.storage))) + str(')')

def UIntArray__hashCode_impl(this):
    return hashCode(this.storage)

def UIntArray__equals_impl(this, other):
    if not jsInstanceOf(other, jsClass()):
        return False
    
    tmp0_other_with_cast = (other) if (jsInstanceOf(other, jsClass())) else (THROW_CCE())
    if not equals(this.storage, tmp0_other_with_cast.storage):
        return False
    
    return True

class UIntArray:
    def __init__(self, storage):
        self.storage = storage
    
    def _get_size_(self):
        return _UIntArray___get_size__impl_(self)
    
    def iterator(self):
        return UIntArray__iterator_impl(self)
    
    def contains(self, element):
        return UIntArray__contains_impl(self, element)
    
    def contains(self, element):
        return UIntArray__contains_impl(self, element)
    
    def containsAll(self, elements):
        return UIntArray__containsAll_impl(self, elements)
    
    def containsAll(self, elements):
        return UIntArray__containsAll_impl(self, elements)
    
    def isEmpty(self):
        return UIntArray__isEmpty_impl(self)
    
    def toString(self):
        return UIntArray__toString_impl(self)
    
    def hashCode(self):
        return UIntArray__hashCode_impl(self)
    
    def equals(self, other):
        return UIntArray__equals_impl(self, other)
    

class Companion:
    def __init__(self):
        Companion_instance = self
        tmp = self
        Companion_getInstance()
        tmp = _UInt___init__impl_(-1)
        Companion_getInstance()
        tmp.EMPTY = UIntRange(tmp, _UInt___init__impl_(0))
    
    def _get_EMPTY_(self):
        return self.EMPTY
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

pass
def Companion_getInstance():
    if Companion_instance == None:
        Companion()
    
    return Companion_instance

class UIntRange:
    def __init__(self, start, endInclusive):
        Companion_getInstance()
        super(start, endInclusive, 1)
    
    def _get_start_(self):
        return self._get_first_()
    
    def _get_start_(self):
        return self._get_start_()
    
    def _get_endInclusive_(self):
        return self._get_last_()
    
    def _get_endInclusive_(self):
        return self._get_endInclusive_()
    
    def contains(self, value):
        tmp0_compareTo_0 = self._get_first_()
        if uintCompare(_UInt___get_data__impl_(tmp0_compareTo_0), _UInt___get_data__impl_(value)) <= 0:
            tmp1_compareTo_0 = self._get_last_()
            tmp = uintCompare(_UInt___get_data__impl_(value), _UInt___get_data__impl_(tmp1_compareTo_0)) <= 0
        elif True:
            tmp = False
        
        return tmp
    
    def contains(self, value):
        return self.contains((value) if (jsInstanceOf(value, jsClass())) else (THROW_CCE()))
    
    def isEmpty(self):
        tmp0_compareTo_0 = self._get_first_()
        tmp1_compareTo_0 = self._get_last_()
        return uintCompare(_UInt___get_data__impl_(tmp0_compareTo_0), _UInt___get_data__impl_(tmp1_compareTo_0)) > 0
    
    def equals(self, other):
        if jsInstanceOf(other, jsClass()):
            tmp = (True) if ((kotlin_ranges_UIntRange(other).isEmpty()) if (self.isEmpty()) else (False)) else ((self._get_last_().equals(kotlin_ranges_UIntRange(other)._get_last_())) if (self._get_first_().equals(kotlin_ranges_UIntRange(other)._get_first_())) else (False))
        elif True:
            tmp = False
        
        return tmp
    
    def hashCode(self):
        if self.isEmpty():
            tmp = -1
        else:
            tmp0_toInt_0 = self._get_first_()
            tmp = imul(31, _UInt___get_data__impl_(tmp0_toInt_0))
            tmp1_toInt_0 = self._get_last_()
            tmp = (tmp + _UInt___get_data__impl_(tmp1_toInt_0)) | 0
        
        return tmp
    
    def toString(self):
        return (str(self._get_first_()) + str('..')) + str(self._get_last_())
    
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
    

pass
def Companion_getInstance():
    if Companion_instance == None:
        Companion()
    
    return Companion_instance

class UIntProgression:
    def __init__(self, start, endInclusive, step):
        Companion_getInstance()
        if step == 0:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl
        
        if step == IntCompanionObject_getInstance().MIN_VALUE:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl
        
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
        if self.step > 0:
            tmp0_compareTo_0 = self.first
            tmp1_compareTo_0 = self.last
            tmp = uintCompare(_UInt___get_data__impl_(tmp0_compareTo_0), _UInt___get_data__impl_(tmp1_compareTo_0)) > 0
        else:
            tmp2_compareTo_0 = self.first
            tmp3_compareTo_0 = self.last
            tmp = uintCompare(_UInt___get_data__impl_(tmp2_compareTo_0), _UInt___get_data__impl_(tmp3_compareTo_0)) < 0
        
        return tmp
    
    def equals(self, other):
        if jsInstanceOf(other, jsClass()):
            tmp = (True) if ((kotlin_ranges_UIntProgression(other).isEmpty()) if (self.isEmpty()) else (False)) else ((self.step == kotlin_ranges_UIntProgression(other).step) if ((self.last.equals(kotlin_ranges_UIntProgression(other).last)) if (self.first.equals(kotlin_ranges_UIntProgression(other).first)) else (False)) else (False))
        elif True:
            tmp = False
        
        return tmp
    
    def hashCode(self):
        if self.isEmpty():
            tmp = -1
        else:
            tmp0_toInt_0 = self.first
            tmp = imul(31, _UInt___get_data__impl_(tmp0_toInt_0))
            tmp1_toInt_0 = self.last
            tmp = (imul(31, (tmp + _UInt___get_data__impl_(tmp1_toInt_0)) | 0) + kotlin_Int(self.step)) | 0
        
        return tmp
    
    def toString(self):
        return ((((str(self.first) + str('..')) + str(self.last)) + str(' step ')) + str(self.step)) if (self.step > 0) else ((((str(self.first) + str(' downTo ')) + str(self.last)) + str(' step ')) + str(-self.step | 0))
    

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
        super()
        self.finalElement = last
        tmp = self
        if step > 0:
            tmp = uintCompare(_UInt___get_data__impl_(first), _UInt___get_data__impl_(last)) <= 0
        else:
            tmp = uintCompare(_UInt___get_data__impl_(first), _UInt___get_data__impl_(last)) >= 0
        
        tmp.hasNext = tmp
        tmp = self
        tmp.step = _UInt___init__impl_(step)
        self.next = (first) if (self.hasNext) else (self.finalElement)
    
    def hasNext(self):
        return self.hasNext
    
    def nextUInt(self):
        value = self.next
        if value.equals(self.finalElement):
            if not self.hasNext:
                visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl
            
            self.hasNext = False
        else:
            tmp0_this = self
            tmp = tmp0_this
            tmp0_plus_0 = tmp0_this.next
            tmp1_plus_0 = self.step
            tmp.next = _UInt___init__impl_((_UInt___get_data__impl_(tmp0_plus_0) + _UInt___get_data__impl_(tmp1_plus_0)) | 0)
        
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
        return self.next()
    
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
        return self.next()
    
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
        return self.next()
    
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
        return self.next()
    
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
    

def _ULong___init__impl_(data):
    return kotlin_ULong(data)

def _ULong___get_data__impl_(this):
    return this.data

class Companion:
    def __init__(self):
        Companion_instance = self
        self.MIN_VALUE = _ULong___init__impl_(Long(0, 0))
        self.MAX_VALUE = _ULong___init__impl_(Long(-1, -1))
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
    

pass
def Companion_getInstance():
    if Companion_instance == None:
        Companion()
    
    return Companion_instance

def ULong__compareTo_impl(this, other):
    tmp0_compareTo_0 = _ULong___init__impl_(toLong(_UByte___get_data__impl_(other))._and(Long(255, 0)))
    return ulongCompare(_ULong___get_data__impl_(this), _ULong___get_data__impl_(tmp0_compareTo_0))

def ULong__compareTo_impl(this, other):
    tmp0_compareTo_0 = _ULong___init__impl_(toLong(_UShort___get_data__impl_(other))._and(Long(65535, 0)))
    return ulongCompare(_ULong___get_data__impl_(this), _ULong___get_data__impl_(tmp0_compareTo_0))

def ULong__compareTo_impl(this, other):
    tmp0_compareTo_0 = _ULong___init__impl_(toLong(_UInt___get_data__impl_(other))._and(Long(-1, 0)))
    return ulongCompare(_ULong___get_data__impl_(this), _ULong___get_data__impl_(tmp0_compareTo_0))

def ULong__compareTo_impl(this, other):
    return ulongCompare(_ULong___get_data__impl_(this), _ULong___get_data__impl_(other))

def ULong__compareTo_impl(this, other):
    return ULong__compareTo_impl(this, (other) if (jsInstanceOf(other, jsClass())) else (THROW_CCE()))

def ULong__plus_impl(this, other):
    tmp0_plus_0 = _ULong___init__impl_(toLong(_UByte___get_data__impl_(other))._and(Long(255, 0)))
    return _ULong___init__impl_(_ULong___get_data__impl_(this).plus(_ULong___get_data__impl_(tmp0_plus_0)))

def ULong__plus_impl(this, other):
    tmp0_plus_0 = _ULong___init__impl_(toLong(_UShort___get_data__impl_(other))._and(Long(65535, 0)))
    return _ULong___init__impl_(_ULong___get_data__impl_(this).plus(_ULong___get_data__impl_(tmp0_plus_0)))

def ULong__plus_impl(this, other):
    tmp0_plus_0 = _ULong___init__impl_(toLong(_UInt___get_data__impl_(other))._and(Long(-1, 0)))
    return _ULong___init__impl_(_ULong___get_data__impl_(this).plus(_ULong___get_data__impl_(tmp0_plus_0)))

def ULong__plus_impl(this, other):
    return _ULong___init__impl_(_ULong___get_data__impl_(this).plus(_ULong___get_data__impl_(other)))

def ULong__minus_impl(this, other):
    tmp0_minus_0 = _ULong___init__impl_(toLong(_UByte___get_data__impl_(other))._and(Long(255, 0)))
    return _ULong___init__impl_(_ULong___get_data__impl_(this).minus(_ULong___get_data__impl_(tmp0_minus_0)))

def ULong__minus_impl(this, other):
    tmp0_minus_0 = _ULong___init__impl_(toLong(_UShort___get_data__impl_(other))._and(Long(65535, 0)))
    return _ULong___init__impl_(_ULong___get_data__impl_(this).minus(_ULong___get_data__impl_(tmp0_minus_0)))

def ULong__minus_impl(this, other):
    tmp0_minus_0 = _ULong___init__impl_(toLong(_UInt___get_data__impl_(other))._and(Long(-1, 0)))
    return _ULong___init__impl_(_ULong___get_data__impl_(this).minus(_ULong___get_data__impl_(tmp0_minus_0)))

def ULong__minus_impl(this, other):
    return _ULong___init__impl_(_ULong___get_data__impl_(this).minus(_ULong___get_data__impl_(other)))

def ULong__times_impl(this, other):
    tmp0_times_0 = _ULong___init__impl_(toLong(_UByte___get_data__impl_(other))._and(Long(255, 0)))
    return _ULong___init__impl_(_ULong___get_data__impl_(this).times(_ULong___get_data__impl_(tmp0_times_0)))

def ULong__times_impl(this, other):
    tmp0_times_0 = _ULong___init__impl_(toLong(_UShort___get_data__impl_(other))._and(Long(65535, 0)))
    return _ULong___init__impl_(_ULong___get_data__impl_(this).times(_ULong___get_data__impl_(tmp0_times_0)))

def ULong__times_impl(this, other):
    tmp0_times_0 = _ULong___init__impl_(toLong(_UInt___get_data__impl_(other))._and(Long(-1, 0)))
    return _ULong___init__impl_(_ULong___get_data__impl_(this).times(_ULong___get_data__impl_(tmp0_times_0)))

def ULong__times_impl(this, other):
    return _ULong___init__impl_(_ULong___get_data__impl_(this).times(_ULong___get_data__impl_(other)))

def ULong__div_impl(this, other):
    tmp0_div_0 = _ULong___init__impl_(toLong(_UByte___get_data__impl_(other))._and(Long(255, 0)))
    return ulongDivide(this, tmp0_div_0)

def ULong__div_impl(this, other):
    tmp0_div_0 = _ULong___init__impl_(toLong(_UShort___get_data__impl_(other))._and(Long(65535, 0)))
    return ulongDivide(this, tmp0_div_0)

def ULong__div_impl(this, other):
    tmp0_div_0 = _ULong___init__impl_(toLong(_UInt___get_data__impl_(other))._and(Long(-1, 0)))
    return ulongDivide(this, tmp0_div_0)

def ULong__div_impl(this, other):
    return ulongDivide(this, other)

def ULong__rem_impl(this, other):
    tmp0_rem_0 = _ULong___init__impl_(toLong(_UByte___get_data__impl_(other))._and(Long(255, 0)))
    return ulongRemainder(this, tmp0_rem_0)

def ULong__rem_impl(this, other):
    tmp0_rem_0 = _ULong___init__impl_(toLong(_UShort___get_data__impl_(other))._and(Long(65535, 0)))
    return ulongRemainder(this, tmp0_rem_0)

def ULong__rem_impl(this, other):
    tmp0_rem_0 = _ULong___init__impl_(toLong(_UInt___get_data__impl_(other))._and(Long(-1, 0)))
    return ulongRemainder(this, tmp0_rem_0)

def ULong__rem_impl(this, other):
    return ulongRemainder(this, other)

def ULong__floorDiv_impl(this, other):
    tmp0_floorDiv_0 = _ULong___init__impl_(toLong(_UByte___get_data__impl_(other))._and(Long(255, 0)))
    return ulongDivide(this, tmp0_floorDiv_0)

def ULong__floorDiv_impl(this, other):
    tmp0_floorDiv_0 = _ULong___init__impl_(toLong(_UShort___get_data__impl_(other))._and(Long(65535, 0)))
    return ulongDivide(this, tmp0_floorDiv_0)

def ULong__floorDiv_impl(this, other):
    tmp0_floorDiv_0 = _ULong___init__impl_(toLong(_UInt___get_data__impl_(other))._and(Long(-1, 0)))
    return ulongDivide(this, tmp0_floorDiv_0)

def ULong__floorDiv_impl(this, other):
    return ulongDivide(this, other)

def ULong__mod_impl(this, other):
    tmp0_mod_0 = _ULong___init__impl_(toLong(_UByte___get_data__impl_(other))._and(Long(255, 0)))
    tmp2_toUByte_0 = ulongRemainder(this, tmp0_mod_0)
    tmp1_toUByte_0 = _ULong___get_data__impl_(tmp2_toUByte_0)
    return _UByte___init__impl_(tmp1_toUByte_0.toByte())

def ULong__mod_impl(this, other):
    tmp0_mod_0 = _ULong___init__impl_(toLong(_UShort___get_data__impl_(other))._and(Long(65535, 0)))
    tmp2_toUShort_0 = ulongRemainder(this, tmp0_mod_0)
    tmp1_toUShort_0 = _ULong___get_data__impl_(tmp2_toUShort_0)
    return _UShort___init__impl_(tmp1_toUShort_0.toShort())

def ULong__mod_impl(this, other):
    tmp0_mod_0 = _ULong___init__impl_(toLong(_UInt___get_data__impl_(other))._and(Long(-1, 0)))
    tmp2_toUInt_0 = ulongRemainder(this, tmp0_mod_0)
    tmp1_toUInt_0 = _ULong___get_data__impl_(tmp2_toUInt_0)
    return _UInt___init__impl_(tmp1_toUInt_0.toInt())

def ULong__mod_impl(this, other):
    return ulongRemainder(this, other)

def ULong__inc_impl(this):
    return _ULong___init__impl_(_ULong___get_data__impl_(this).inc())

def ULong__dec_impl(this):
    return _ULong___init__impl_(_ULong___get_data__impl_(this).dec())

def ULong__rangeTo_impl(this, other):
    return ULongRange(this, other)

def ULong__shl_impl(this, bitCount):
    return _ULong___init__impl_(_ULong___get_data__impl_(this).shl(bitCount))

def ULong__shr_impl(this, bitCount):
    return _ULong___init__impl_(_ULong___get_data__impl_(this).ushr(bitCount))

def ULong__and_impl(this, other):
    return _ULong___init__impl_(_ULong___get_data__impl_(this)._and(_ULong___get_data__impl_(other)))

def ULong__or_impl(this, other):
    return _ULong___init__impl_(_ULong___get_data__impl_(this)._or(_ULong___get_data__impl_(other)))

def ULong__xor_impl(this, other):
    return _ULong___init__impl_(_ULong___get_data__impl_(this).xor(_ULong___get_data__impl_(other)))

def ULong__inv_impl(this):
    return _ULong___init__impl_(_ULong___get_data__impl_(this).inv())

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
    return _UByte___init__impl_(tmp0_toUByte_0.toByte())

def ULong__toUShort_impl(this):
    tmp0_toUShort_0 = _ULong___get_data__impl_(this)
    return _UShort___init__impl_(tmp0_toUShort_0.toShort())

def ULong__toUInt_impl(this):
    tmp0_toUInt_0 = _ULong___get_data__impl_(this)
    return _UInt___init__impl_(tmp0_toUInt_0.toInt())

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
    if not jsInstanceOf(other, jsClass()):
        return False
    
    tmp0_other_with_cast = (other) if (jsInstanceOf(other, jsClass())) else (THROW_CCE())
    if not this.data.equals(tmp0_other_with_cast.data):
        return False
    
    return True

class ULong:
    def __init__(self, data):
        Companion_getInstance()
        self.data = data
    
    def compareTo(self, other):
        return ULong__compareTo_impl(self, other)
    
    def compareTo(self, other):
        return ULong__compareTo_impl(self, other)
    
    def toString(self):
        return ULong__toString_impl(self)
    
    def hashCode(self):
        return ULong__hashCode_impl(self)
    
    def equals(self, other):
        return ULong__equals_impl(self, other)
    

def toULong():
    return _ULong___init__impl_(self)

def toULong():
    return _ULong___init__impl_(toLong(self))

def toULong():
    return doubleToULong(self)

def toULong():
    return doubleToULong(kotlin_Double(self))

def toULong():
    return _ULong___init__impl_(toLong(self))

def toULong():
    return _ULong___init__impl_(toLong(self))

def _get_array_(_this):
    return _this.array

def _set_index_(_this, _set___):
    _this.index = _set___

def _get_index_(_this):
    return _this.index

def _ULongArray___init__impl_(storage):
    return kotlin_ULongArray(storage)

def _ULongArray___get_storage__impl_(this):
    return this.storage

def _ULongArray___init__impl_(size):
    tmp = _ULongArray___init__impl_(longArray(size))
    return tmp

def ULongArray__get_impl(this, index):
    tmp0_toULong_0 = _ULongArray___get_storage__impl_(this)[index]
    return _ULong___init__impl_(tmp0_toULong_0)

def ULongArray__set_impl(this, index, value):
    tmp = _ULongArray___get_storage__impl_(this)
    tmp.__setitem__(index, _ULong___get_data__impl_(value))

def _ULongArray___get_size__impl_(this):
    return len(_ULongArray___get_storage__impl_(this))

def ULongArray__iterator_impl(this):
    return Iterator(_ULongArray___get_storage__impl_(this))

class Iterator:
    def __init__(self, array):
        super()
        self.array = array
        self.index = 0
    
    def hasNext(self):
        return self.index < len(self.array)
    
    def nextULong(self):
        if self.index < len(self.array):
            tmp0_this = self
            tmp1 = tmp0_this.index
            tmp0_this.index = (tmp1 + 1) | 0
            tmp0_toULong_0 = self.array[tmp1]
            tmp = _ULong___init__impl_(tmp0_toULong_0)
        else:
            raise NoSuchElementException_init__Create_(self.index.toString())
        
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
    tmp = (element) if (isObject(element)) else (THROW_CCE())
    if not jsInstanceOf(tmp, jsClass()):
        return False
    
    tmp = _ULongArray___get_storage__impl_(this)
    return contains(_ULong___get_data__impl_(element))

def ULongArray__contains_impl(this, element):
    if not jsInstanceOf(element, jsClass()):
        return False
    
    return ULongArray__contains_impl(this, (element) if (jsInstanceOf(element, jsClass())) else (THROW_CCE()))

def ULongArray__containsAll_impl(this, elements):
    while True:
        tmp0_all_0 = (kotlin_collections_Collection___(elements)) if (isInterface(elements, jsClass())) else (THROW_CCE())
        if isInterface(tmp0_all_0, jsClass()):
            tmp = kotlin_collections_Collection_kotlin_Any__(tmp0_all_0).isEmpty()
        elif True:
            tmp = False
        
        if tmp:
            tmp_ret_0 = True
            break
        
        tmp0_iterator_1 = tmp0_all_0.iterator()
        while tmp0_iterator_1.hasNext():
            element_2 = tmp0_iterator_1.next()
            if jsInstanceOf(element_2, jsClass()):
                tmp = _ULongArray___get_storage__impl_(this)
                tmp0_toLong_0_4 = element_2
                tmp = contains(_ULong___get_data__impl_(tmp0_toLong_0_4))
            elif True:
                tmp = False
            
            if not tmp:
                tmp_ret_0 = False
                break
            
        
        tmp_ret_0 = True
        if False:
            break
        
    
    return tmp_ret_0

def ULongArray__containsAll_impl(this, elements):
    return ULongArray__containsAll_impl(this, elements)

def ULongArray__isEmpty_impl(this):
    return len(_ULongArray___get_storage__impl_(this)) == 0

def ULongArray__toString_impl(this):
    return (str('ULongArray(storage=') + str(toString(this.storage))) + str(')')

def ULongArray__hashCode_impl(this):
    return hashCode(this.storage)

def ULongArray__equals_impl(this, other):
    if not jsInstanceOf(other, jsClass()):
        return False
    
    tmp0_other_with_cast = (other) if (jsInstanceOf(other, jsClass())) else (THROW_CCE())
    if not equals(this.storage, tmp0_other_with_cast.storage):
        return False
    
    return True

class ULongArray:
    def __init__(self, storage):
        self.storage = storage
    
    def _get_size_(self):
        return _ULongArray___get_size__impl_(self)
    
    def iterator(self):
        return ULongArray__iterator_impl(self)
    
    def contains(self, element):
        return ULongArray__contains_impl(self, element)
    
    def contains(self, element):
        return ULongArray__contains_impl(self, element)
    
    def containsAll(self, elements):
        return ULongArray__containsAll_impl(self, elements)
    
    def containsAll(self, elements):
        return ULongArray__containsAll_impl(self, elements)
    
    def isEmpty(self):
        return ULongArray__isEmpty_impl(self)
    
    def toString(self):
        return ULongArray__toString_impl(self)
    
    def hashCode(self):
        return ULongArray__hashCode_impl(self)
    
    def equals(self, other):
        return ULongArray__equals_impl(self, other)
    

class Companion:
    def __init__(self):
        Companion_instance = self
        tmp = self
        Companion_getInstance()
        tmp = _ULong___init__impl_(Long(-1, -1))
        Companion_getInstance()
        tmp.EMPTY = ULongRange(tmp, _ULong___init__impl_(Long(0, 0)))
    
    def _get_EMPTY_(self):
        return self.EMPTY
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

pass
def Companion_getInstance():
    if Companion_instance == None:
        Companion()
    
    return Companion_instance

class ULongRange:
    def __init__(self, start, endInclusive):
        Companion_getInstance()
        super(start, endInclusive, Long(1, 0))
    
    def _get_start_(self):
        return self._get_first_()
    
    def _get_start_(self):
        return self._get_start_()
    
    def _get_endInclusive_(self):
        return self._get_last_()
    
    def _get_endInclusive_(self):
        return self._get_endInclusive_()
    
    def contains(self, value):
        tmp0_compareTo_0 = self._get_first_()
        if ulongCompare(_ULong___get_data__impl_(tmp0_compareTo_0), _ULong___get_data__impl_(value)) <= 0:
            tmp1_compareTo_0 = self._get_last_()
            tmp = ulongCompare(_ULong___get_data__impl_(value), _ULong___get_data__impl_(tmp1_compareTo_0)) <= 0
        elif True:
            tmp = False
        
        return tmp
    
    def contains(self, value):
        return self.contains((value) if (jsInstanceOf(value, jsClass())) else (THROW_CCE()))
    
    def isEmpty(self):
        tmp0_compareTo_0 = self._get_first_()
        tmp1_compareTo_0 = self._get_last_()
        return ulongCompare(_ULong___get_data__impl_(tmp0_compareTo_0), _ULong___get_data__impl_(tmp1_compareTo_0)) > 0
    
    def equals(self, other):
        if jsInstanceOf(other, jsClass()):
            tmp = (True) if ((kotlin_ranges_ULongRange(other).isEmpty()) if (self.isEmpty()) else (False)) else ((self._get_last_().equals(kotlin_ranges_ULongRange(other)._get_last_())) if (self._get_first_().equals(kotlin_ranges_ULongRange(other)._get_first_())) else (False))
        elif True:
            tmp = False
        
        return tmp
    
    def hashCode(self):
        if self.isEmpty():
            tmp = -1
        else:
            tmp1_xor_0 = self._get_first_()
            tmp0_shr_0 = self._get_first_()
            tmp2_xor_0 = _ULong___init__impl_(_ULong___get_data__impl_(tmp0_shr_0).ushr(32))
            tmp3_toInt_0 = _ULong___init__impl_(_ULong___get_data__impl_(tmp1_xor_0).xor(_ULong___get_data__impl_(tmp2_xor_0)))
            tmp = imul(31, _ULong___get_data__impl_(tmp3_toInt_0).toInt())
            tmp5_xor_0 = self._get_last_()
            tmp4_shr_0 = self._get_last_()
            tmp6_xor_0 = _ULong___init__impl_(_ULong___get_data__impl_(tmp4_shr_0).ushr(32))
            tmp7_toInt_0 = _ULong___init__impl_(_ULong___get_data__impl_(tmp5_xor_0).xor(_ULong___get_data__impl_(tmp6_xor_0)))
            tmp = (tmp + _ULong___get_data__impl_(tmp7_toInt_0).toInt()) | 0
        
        return tmp
    
    def toString(self):
        return (str(self._get_first_()) + str('..')) + str(self._get_last_())
    
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
    

pass
def Companion_getInstance():
    if Companion_instance == None:
        Companion()
    
    return Companion_instance

class ULongProgression:
    def __init__(self, start, endInclusive, step):
        Companion_getInstance()
        if step.equals(Long(0, 0)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl
        
        Companion_getInstance()
        if step.equals(Long(0, -2147483648)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl
        
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
        if self.step.compareTo(Long(0, 0)) > 0:
            tmp0_compareTo_0 = self.first
            tmp1_compareTo_0 = self.last
            tmp = ulongCompare(_ULong___get_data__impl_(tmp0_compareTo_0), _ULong___get_data__impl_(tmp1_compareTo_0)) > 0
        else:
            tmp2_compareTo_0 = self.first
            tmp3_compareTo_0 = self.last
            tmp = ulongCompare(_ULong___get_data__impl_(tmp2_compareTo_0), _ULong___get_data__impl_(tmp3_compareTo_0)) < 0
        
        return tmp
    
    def equals(self, other):
        if jsInstanceOf(other, jsClass()):
            tmp = (True) if ((kotlin_ranges_ULongProgression(other).isEmpty()) if (self.isEmpty()) else (False)) else ((self.step.equals(kotlin_ranges_ULongProgression(other).step)) if ((self.last.equals(kotlin_ranges_ULongProgression(other).last)) if (self.first.equals(kotlin_ranges_ULongProgression(other).first)) else (False)) else (False))
        elif True:
            tmp = False
        
        return tmp
    
    def hashCode(self):
        if self.isEmpty():
            tmp = -1
        else:
            tmp1_xor_0 = self.first
            tmp0_shr_0 = self.first
            tmp2_xor_0 = _ULong___init__impl_(_ULong___get_data__impl_(tmp0_shr_0).ushr(32))
            tmp3_toInt_0 = _ULong___init__impl_(_ULong___get_data__impl_(tmp1_xor_0).xor(_ULong___get_data__impl_(tmp2_xor_0)))
            tmp = imul(31, _ULong___get_data__impl_(tmp3_toInt_0).toInt())
            tmp5_xor_0 = self.last
            tmp4_shr_0 = self.last
            tmp6_xor_0 = _ULong___init__impl_(_ULong___get_data__impl_(tmp4_shr_0).ushr(32))
            tmp7_toInt_0 = _ULong___init__impl_(_ULong___get_data__impl_(tmp5_xor_0).xor(_ULong___get_data__impl_(tmp6_xor_0)))
            tmp = (imul(31, (tmp + _ULong___get_data__impl_(tmp7_toInt_0).toInt()) | 0) + self.step.xor(self.step.ushr(32)).toInt()) | 0
        
        return tmp
    
    def toString(self):
        return ((((str(self.first) + str('..')) + str(self.last)) + str(' step ')) + str(self.step)) if (self.step.compareTo(Long(0, 0)) > 0) else ((((str(self.first) + str(' downTo ')) + str(self.last)) + str(' step ')) + str(self.step.unaryMinus()))
    

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
        super()
        self.finalElement = last
        tmp = self
        if step.compareTo(Long(0, 0)) > 0:
            tmp = ulongCompare(_ULong___get_data__impl_(first), _ULong___get_data__impl_(last)) <= 0
        else:
            tmp = ulongCompare(_ULong___get_data__impl_(first), _ULong___get_data__impl_(last)) >= 0
        
        tmp.hasNext = tmp
        tmp = self
        tmp.step = _ULong___init__impl_(step)
        self.next = (first) if (self.hasNext) else (self.finalElement)
    
    def hasNext(self):
        return self.hasNext
    
    def nextULong(self):
        value = self.next
        if value.equals(self.finalElement):
            if not self.hasNext:
                visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl
            
            self.hasNext = False
        else:
            tmp0_this = self
            tmp = tmp0_this
            tmp0_plus_0 = tmp0_this.next
            tmp1_plus_0 = self.step
            tmp.next = _ULong___init__impl_(_ULong___get_data__impl_(tmp0_plus_0).plus(_ULong___get_data__impl_(tmp1_plus_0)))
        
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
    if step > 0:
        if uintCompare(_UInt___get_data__impl_(start), _UInt___get_data__impl_(end)) >= 0:
            tmp = end
        elif True:
            tmp0_minus_0 = differenceModulo(end, start, _UInt___init__impl_(step))
            tmp = _UInt___init__impl_((_UInt___get_data__impl_(end) - _UInt___get_data__impl_(tmp0_minus_0)) | 0)
        
        tmp = tmp
    elif step < 0:
        if uintCompare(_UInt___get_data__impl_(start), _UInt___get_data__impl_(end)) <= 0:
            tmp = end
        elif True:
            tmp1_toUInt_0 = -step | 0
            tmp2_plus_0 = differenceModulo(start, end, _UInt___init__impl_(tmp1_toUInt_0))
            tmp = _UInt___init__impl_((_UInt___get_data__impl_(end) + _UInt___get_data__impl_(tmp2_plus_0)) | 0)
        
        tmp = tmp
    else:
        raise IllegalArgumentException_init__Create_('Step is zero.')
    
    return tmp

def getProgressionLastElement(start, end, step):
    if step.compareTo(Long(0, 0)) > 0:
        if ulongCompare(_ULong___get_data__impl_(start), _ULong___get_data__impl_(end)) >= 0:
            tmp = end
        elif True:
            tmp0_minus_0 = differenceModulo(end, start, _ULong___init__impl_(step))
            tmp = _ULong___init__impl_(_ULong___get_data__impl_(end).minus(_ULong___get_data__impl_(tmp0_minus_0)))
        
        tmp = tmp
    elif step.compareTo(Long(0, 0)) < 0:
        if ulongCompare(_ULong___get_data__impl_(start), _ULong___get_data__impl_(end)) <= 0:
            tmp = end
        elif True:
            tmp1_toULong_0 = step.unaryMinus()
            tmp2_plus_0 = differenceModulo(start, end, _ULong___init__impl_(tmp1_toULong_0))
            tmp = _ULong___init__impl_(_ULong___get_data__impl_(end).plus(_ULong___get_data__impl_(tmp2_plus_0)))
        
        tmp = tmp
    else:
        raise IllegalArgumentException_init__Create_('Step is zero.')
    
    return tmp

def differenceModulo(a, b, c):
    ac = uintRemainder(a, c)
    bc = uintRemainder(b, c)
    if uintCompare(_UInt___get_data__impl_(ac), _UInt___get_data__impl_(bc)) >= 0:
        tmp = _UInt___init__impl_((_UInt___get_data__impl_(ac) - _UInt___get_data__impl_(bc)) | 0)
    elif True:
        tmp0_plus_0 = _UInt___init__impl_((_UInt___get_data__impl_(ac) - _UInt___get_data__impl_(bc)) | 0)
        tmp = _UInt___init__impl_((_UInt___get_data__impl_(tmp0_plus_0) + _UInt___get_data__impl_(c)) | 0)
    
    return tmp

def differenceModulo(a, b, c):
    ac = ulongRemainder(a, c)
    bc = ulongRemainder(b, c)
    if ulongCompare(_ULong___get_data__impl_(ac), _ULong___get_data__impl_(bc)) >= 0:
        tmp = _ULong___init__impl_(_ULong___get_data__impl_(ac).minus(_ULong___get_data__impl_(bc)))
    elif True:
        tmp0_plus_0 = _ULong___init__impl_(_ULong___get_data__impl_(ac).minus(_ULong___get_data__impl_(bc)))
        tmp = _ULong___init__impl_(_ULong___get_data__impl_(tmp0_plus_0).plus(_ULong___get_data__impl_(c)))
    
    return tmp

def _UShort___init__impl_(data):
    return kotlin_UShort(data)

def _UShort___get_data__impl_(this):
    return this.data

class Companion:
    def __init__(self):
        Companion_instance = self
        self.MIN_VALUE = _UShort___init__impl_(0)
        self.MAX_VALUE = _UShort___init__impl_(-1)
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
    

pass
def Companion_getInstance():
    if Companion_instance == None:
        Companion()
    
    return Companion_instance

def UShort__compareTo_impl(this, other):
    tmp = kotlin_Int(_UShort___get_data__impl_(this)) & 65535
    return compareTo(tmp, kotlin_Int(_UByte___get_data__impl_(other)) & 255)

def UShort__compareTo_impl(this, other):
    tmp = kotlin_Int(_UShort___get_data__impl_(this)) & 65535
    return compareTo(tmp, kotlin_Int(_UShort___get_data__impl_(other)) & 65535)

def UShort__compareTo_impl(this, other):
    return UShort__compareTo_impl(this, (other) if (jsInstanceOf(other, jsClass())) else (THROW_CCE()))

def UShort__compareTo_impl(this, other):
    tmp0_compareTo_0 = _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(this)) & 65535)
    return uintCompare(_UInt___get_data__impl_(tmp0_compareTo_0), _UInt___get_data__impl_(other))

def UShort__compareTo_impl(this, other):
    tmp0_compareTo_0 = _ULong___init__impl_(toLong(_UShort___get_data__impl_(this))._and(Long(65535, 0)))
    return ulongCompare(_ULong___get_data__impl_(tmp0_compareTo_0), _ULong___get_data__impl_(other))

def UShort__plus_impl(this, other):
    tmp0_plus_0 = _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(this)) & 65535)
    tmp1_plus_0 = _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(other)) & 255)
    return _UInt___init__impl_((_UInt___get_data__impl_(tmp0_plus_0) + _UInt___get_data__impl_(tmp1_plus_0)) | 0)

def UShort__plus_impl(this, other):
    tmp0_plus_0 = _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(this)) & 65535)
    tmp1_plus_0 = _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(other)) & 65535)
    return _UInt___init__impl_((_UInt___get_data__impl_(tmp0_plus_0) + _UInt___get_data__impl_(tmp1_plus_0)) | 0)

def UShort__plus_impl(this, other):
    tmp0_plus_0 = _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(this)) & 65535)
    return _UInt___init__impl_((_UInt___get_data__impl_(tmp0_plus_0) + _UInt___get_data__impl_(other)) | 0)

def UShort__plus_impl(this, other):
    tmp0_plus_0 = _ULong___init__impl_(toLong(_UShort___get_data__impl_(this))._and(Long(65535, 0)))
    return _ULong___init__impl_(_ULong___get_data__impl_(tmp0_plus_0).plus(_ULong___get_data__impl_(other)))

def UShort__minus_impl(this, other):
    tmp0_minus_0 = _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(this)) & 65535)
    tmp1_minus_0 = _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(other)) & 255)
    return _UInt___init__impl_((_UInt___get_data__impl_(tmp0_minus_0) - _UInt___get_data__impl_(tmp1_minus_0)) | 0)

def UShort__minus_impl(this, other):
    tmp0_minus_0 = _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(this)) & 65535)
    tmp1_minus_0 = _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(other)) & 65535)
    return _UInt___init__impl_((_UInt___get_data__impl_(tmp0_minus_0) - _UInt___get_data__impl_(tmp1_minus_0)) | 0)

def UShort__minus_impl(this, other):
    tmp0_minus_0 = _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(this)) & 65535)
    return _UInt___init__impl_((_UInt___get_data__impl_(tmp0_minus_0) - _UInt___get_data__impl_(other)) | 0)

def UShort__minus_impl(this, other):
    tmp0_minus_0 = _ULong___init__impl_(toLong(_UShort___get_data__impl_(this))._and(Long(65535, 0)))
    return _ULong___init__impl_(_ULong___get_data__impl_(tmp0_minus_0).minus(_ULong___get_data__impl_(other)))

def UShort__times_impl(this, other):
    tmp0_times_0 = _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(this)) & 65535)
    tmp1_times_0 = _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(other)) & 255)
    return _UInt___init__impl_(imul(_UInt___get_data__impl_(tmp0_times_0), _UInt___get_data__impl_(tmp1_times_0)))

def UShort__times_impl(this, other):
    tmp0_times_0 = _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(this)) & 65535)
    tmp1_times_0 = _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(other)) & 65535)
    return _UInt___init__impl_(imul(_UInt___get_data__impl_(tmp0_times_0), _UInt___get_data__impl_(tmp1_times_0)))

def UShort__times_impl(this, other):
    tmp0_times_0 = _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(this)) & 65535)
    return _UInt___init__impl_(imul(_UInt___get_data__impl_(tmp0_times_0), _UInt___get_data__impl_(other)))

def UShort__times_impl(this, other):
    tmp0_times_0 = _ULong___init__impl_(toLong(_UShort___get_data__impl_(this))._and(Long(65535, 0)))
    return _ULong___init__impl_(_ULong___get_data__impl_(tmp0_times_0).times(_ULong___get_data__impl_(other)))

def UShort__div_impl(this, other):
    tmp0_div_0 = _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(this)) & 65535)
    tmp1_div_0 = _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(other)) & 255)
    return uintDivide(tmp0_div_0, tmp1_div_0)

def UShort__div_impl(this, other):
    tmp0_div_0 = _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(this)) & 65535)
    tmp1_div_0 = _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(other)) & 65535)
    return uintDivide(tmp0_div_0, tmp1_div_0)

def UShort__div_impl(this, other):
    tmp0_div_0 = _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(this)) & 65535)
    return uintDivide(tmp0_div_0, other)

def UShort__div_impl(this, other):
    tmp0_div_0 = _ULong___init__impl_(toLong(_UShort___get_data__impl_(this))._and(Long(65535, 0)))
    return ulongDivide(tmp0_div_0, other)

def UShort__rem_impl(this, other):
    tmp0_rem_0 = _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(this)) & 65535)
    tmp1_rem_0 = _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(other)) & 255)
    return uintRemainder(tmp0_rem_0, tmp1_rem_0)

def UShort__rem_impl(this, other):
    tmp0_rem_0 = _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(this)) & 65535)
    tmp1_rem_0 = _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(other)) & 65535)
    return uintRemainder(tmp0_rem_0, tmp1_rem_0)

def UShort__rem_impl(this, other):
    tmp0_rem_0 = _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(this)) & 65535)
    return uintRemainder(tmp0_rem_0, other)

def UShort__rem_impl(this, other):
    tmp0_rem_0 = _ULong___init__impl_(toLong(_UShort___get_data__impl_(this))._and(Long(65535, 0)))
    return ulongRemainder(tmp0_rem_0, other)

def UShort__floorDiv_impl(this, other):
    tmp0_floorDiv_0 = _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(this)) & 65535)
    tmp1_floorDiv_0 = _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(other)) & 255)
    return uintDivide(tmp0_floorDiv_0, tmp1_floorDiv_0)

def UShort__floorDiv_impl(this, other):
    tmp0_floorDiv_0 = _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(this)) & 65535)
    tmp1_floorDiv_0 = _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(other)) & 65535)
    return uintDivide(tmp0_floorDiv_0, tmp1_floorDiv_0)

def UShort__floorDiv_impl(this, other):
    tmp0_floorDiv_0 = _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(this)) & 65535)
    return uintDivide(tmp0_floorDiv_0, other)

def UShort__floorDiv_impl(this, other):
    tmp0_floorDiv_0 = _ULong___init__impl_(toLong(_UShort___get_data__impl_(this))._and(Long(65535, 0)))
    return ulongDivide(tmp0_floorDiv_0, other)

def UShort__mod_impl(this, other):
    tmp0_mod_0 = _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(this)) & 65535)
    tmp1_mod_0 = _UInt___init__impl_(kotlin_Int(_UByte___get_data__impl_(other)) & 255)
    tmp2_toUByte_0 = uintRemainder(tmp0_mod_0, tmp1_mod_0)
    tmp0_toUByte_0_1 = _UInt___get_data__impl_(tmp2_toUByte_0)
    return _UByte___init__impl_(toByte(tmp0_toUByte_0_1))

def UShort__mod_impl(this, other):
    tmp0_mod_0 = _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(this)) & 65535)
    tmp1_mod_0 = _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(other)) & 65535)
    tmp2_toUShort_0 = uintRemainder(tmp0_mod_0, tmp1_mod_0)
    tmp0_toUShort_0_1 = _UInt___get_data__impl_(tmp2_toUShort_0)
    return _UShort___init__impl_(toShort(tmp0_toUShort_0_1))

def UShort__mod_impl(this, other):
    tmp0_mod_0 = _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(this)) & 65535)
    return uintRemainder(tmp0_mod_0, other)

def UShort__mod_impl(this, other):
    tmp0_mod_0 = _ULong___init__impl_(toLong(_UShort___get_data__impl_(this))._and(Long(65535, 0)))
    return ulongRemainder(tmp0_mod_0, other)

def UShort__inc_impl(this):
    return _UShort___init__impl_(numberToShort(_UShort___get_data__impl_(this) + 1))

def UShort__dec_impl(this):
    return _UShort___init__impl_(numberToShort(_UShort___get_data__impl_(this) - 1))

def UShort__rangeTo_impl(this, other):
    tmp = _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(this)) & 65535)
    return UIntRange(tmp, _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(other)) & 65535))

def UShort__and_impl(this, other):
    tmp0_and_0 = _UShort___get_data__impl_(this)
    tmp1_and_0 = _UShort___get_data__impl_(other)
    return _UShort___init__impl_(toShort(kotlin_Int(tmp0_and_0) & kotlin_Int(tmp1_and_0)))

def UShort__or_impl(this, other):
    tmp0_or_0 = _UShort___get_data__impl_(this)
    tmp1_or_0 = _UShort___get_data__impl_(other)
    return _UShort___init__impl_(toShort(kotlin_Int(tmp0_or_0) | kotlin_Int(tmp1_or_0)))

def UShort__xor_impl(this, other):
    tmp0_xor_0 = _UShort___get_data__impl_(this)
    tmp1_xor_0 = _UShort___get_data__impl_(other)
    return _UShort___init__impl_(toShort(kotlin_Int(tmp0_xor_0) ^ kotlin_Int(tmp1_xor_0)))

def UShort__inv_impl(this):
    tmp0_inv_0 = _UShort___get_data__impl_(this)
    return _UShort___init__impl_(toShort(~kotlin_Int(tmp0_inv_0)))

def UShort__toByte_impl(this):
    return toByte(_UShort___get_data__impl_(this))

def UShort__toShort_impl(this):
    return _UShort___get_data__impl_(this)

def UShort__toInt_impl(this):
    return kotlin_Int(_UShort___get_data__impl_(this)) & 65535

def UShort__toLong_impl(this):
    return toLong(_UShort___get_data__impl_(this))._and(Long(65535, 0))

def UShort__toUByte_impl(this):
    tmp0_toUByte_0 = _UShort___get_data__impl_(this)
    return _UByte___init__impl_(toByte(tmp0_toUByte_0))

def UShort__toUShort_impl(this):
    return this

def UShort__toUInt_impl(this):
    return _UInt___init__impl_(kotlin_Int(_UShort___get_data__impl_(this)) & 65535)

def UShort__toULong_impl(this):
    return _ULong___init__impl_(toLong(_UShort___get_data__impl_(this))._and(Long(65535, 0)))

def UShort__toFloat_impl(this):
    return kotlin_Float(kotlin_Int(_UShort___get_data__impl_(this)) & 65535)

def UShort__toDouble_impl(this):
    return kotlin_Double(kotlin_Int(_UShort___get_data__impl_(this)) & 65535)

def UShort__toString_impl(this):
    return (kotlin_Int(_UShort___get_data__impl_(this)) & 65535).toString()

def UShort__hashCode_impl(this):
    return this.data

def UShort__equals_impl(this, other):
    if not jsInstanceOf(other, jsClass()):
        return False
    
    tmp0_other_with_cast = (other) if (jsInstanceOf(other, jsClass())) else (THROW_CCE())
    if not (this.data == tmp0_other_with_cast.data):
        return False
    
    return True

class UShort:
    def __init__(self, data):
        Companion_getInstance()
        self.data = data
    
    def compareTo(self, other):
        return UShort__compareTo_impl(self, other)
    
    def compareTo(self, other):
        return UShort__compareTo_impl(self, other)
    
    def toString(self):
        return UShort__toString_impl(self)
    
    def hashCode(self):
        return UShort__hashCode_impl(self)
    
    def equals(self, other):
        return UShort__equals_impl(self, other)
    

def toUShort():
    return _UShort___init__impl_(toShort(self))

def toUShort():
    return _UShort___init__impl_(self.toShort())

def toUShort():
    return _UShort___init__impl_(self)

def _get_array_(_this):
    return _this.array

def _set_index_(_this, _set___):
    _this.index = _set___

def _get_index_(_this):
    return _this.index

def _UShortArray___init__impl_(storage):
    return kotlin_UShortArray(storage)

def _UShortArray___get_storage__impl_(this):
    return this.storage

def _UShortArray___init__impl_(size):
    tmp = _UShortArray___init__impl_(int16Array(size))
    return tmp

def UShortArray__get_impl(this, index):
    tmp0_toUShort_0 = _UShortArray___get_storage__impl_(this)[index]
    return _UShort___init__impl_(tmp0_toUShort_0)

def UShortArray__set_impl(this, index, value):
    tmp = _UShortArray___get_storage__impl_(this)
    tmp.__setitem__(index, _UShort___get_data__impl_(value))

def _UShortArray___get_size__impl_(this):
    return len(_UShortArray___get_storage__impl_(this))

def UShortArray__iterator_impl(this):
    return Iterator(_UShortArray___get_storage__impl_(this))

class Iterator:
    def __init__(self, array):
        super()
        self.array = array
        self.index = 0
    
    def hasNext(self):
        return self.index < len(self.array)
    
    def nextUShort(self):
        if self.index < len(self.array):
            tmp0_this = self
            tmp1 = tmp0_this.index
            tmp0_this.index = (tmp1 + 1) | 0
            tmp0_toUShort_0 = self.array[tmp1]
            tmp = _UShort___init__impl_(tmp0_toUShort_0)
        else:
            raise NoSuchElementException_init__Create_(self.index.toString())
        
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
    tmp = (element) if (isObject(element)) else (THROW_CCE())
    if not jsInstanceOf(tmp, jsClass()):
        return False
    
    tmp = _UShortArray___get_storage__impl_(this)
    return contains(_UShort___get_data__impl_(element))

def UShortArray__contains_impl(this, element):
    if not jsInstanceOf(element, jsClass()):
        return False
    
    return UShortArray__contains_impl(this, (element) if (jsInstanceOf(element, jsClass())) else (THROW_CCE()))

def UShortArray__containsAll_impl(this, elements):
    while True:
        tmp0_all_0 = (kotlin_collections_Collection___(elements)) if (isInterface(elements, jsClass())) else (THROW_CCE())
        if isInterface(tmp0_all_0, jsClass()):
            tmp = kotlin_collections_Collection_kotlin_Any__(tmp0_all_0).isEmpty()
        elif True:
            tmp = False
        
        if tmp:
            tmp_ret_0 = True
            break
        
        tmp0_iterator_1 = tmp0_all_0.iterator()
        while tmp0_iterator_1.hasNext():
            element_2 = tmp0_iterator_1.next()
            if jsInstanceOf(element_2, jsClass()):
                tmp = _UShortArray___get_storage__impl_(this)
                tmp0_toShort_0_4 = element_2
                tmp = contains(_UShort___get_data__impl_(tmp0_toShort_0_4))
            elif True:
                tmp = False
            
            if not tmp:
                tmp_ret_0 = False
                break
            
        
        tmp_ret_0 = True
        if False:
            break
        
    
    return tmp_ret_0

def UShortArray__containsAll_impl(this, elements):
    return UShortArray__containsAll_impl(this, elements)

def UShortArray__isEmpty_impl(this):
    return len(_UShortArray___get_storage__impl_(this)) == 0

def UShortArray__toString_impl(this):
    return (str('UShortArray(storage=') + str(toString(this.storage))) + str(')')

def UShortArray__hashCode_impl(this):
    return hashCode(this.storage)

def UShortArray__equals_impl(this, other):
    if not jsInstanceOf(other, jsClass()):
        return False
    
    tmp0_other_with_cast = (other) if (jsInstanceOf(other, jsClass())) else (THROW_CCE())
    if not equals(this.storage, tmp0_other_with_cast.storage):
        return False
    
    return True

class UShortArray:
    def __init__(self, storage):
        self.storage = storage
    
    def _get_size_(self):
        return _UShortArray___get_size__impl_(self)
    
    def iterator(self):
        return UShortArray__iterator_impl(self)
    
    def contains(self, element):
        return UShortArray__contains_impl(self, element)
    
    def contains(self, element):
        return UShortArray__contains_impl(self, element)
    
    def containsAll(self, elements):
        return UShortArray__containsAll_impl(self, elements)
    
    def containsAll(self, elements):
        return UShortArray__containsAll_impl(self, elements)
    
    def isEmpty(self):
        return UShortArray__isEmpty_impl(self)
    
    def toString(self):
        return UShortArray__toString_impl(self)
    
    def hashCode(self):
        return UShortArray__hashCode_impl(self)
    
    def equals(self, other):
        return UShortArray__equals_impl(self, other)
    

def uintCompare(v1, v2):
    return compareTo(v1 ^ IntCompanionObject_getInstance().MIN_VALUE, v2 ^ IntCompanionObject_getInstance().MIN_VALUE)

def uintDivide(v1, v2):
    tmp = toLong(_UInt___get_data__impl_(v1))._and(Long(-1, 0))
    tmp0_toUInt_0 = tmp.div(toLong(_UInt___get_data__impl_(v2))._and(Long(-1, 0)))
    return _UInt___init__impl_(tmp0_toUInt_0.toInt())

def uintRemainder(v1, v2):
    tmp = toLong(_UInt___get_data__impl_(v1))._and(Long(-1, 0))
    tmp0_toUInt_0 = tmp.rem(toLong(_UInt___get_data__impl_(v2))._and(Long(-1, 0)))
    return _UInt___init__impl_(tmp0_toUInt_0.toInt())

def uintToDouble(v):
    return kotlin_Double(v & IntCompanionObject_getInstance().MAX_VALUE) + (kotlin_Double(jsBitShiftRU(v, 31) << 30) * 2)

def ulongCompare(v1, v2):
    Companion_getInstance()
    tmp = v1.xor(Long(0, -2147483648))
    Companion_getInstance()
    return tmp.compareTo(v2.xor(Long(0, -2147483648)))

def ulongDivide(v1, v2):
    dividend = _ULong___get_data__impl_(v1)
    divisor = _ULong___get_data__impl_(v2)
    if divisor.compareTo(Long(0, 0)) < 0:
        if ulongCompare(_ULong___get_data__impl_(v1), _ULong___get_data__impl_(v2)) < 0:
            tmp = _ULong___init__impl_(Long(0, 0))
        elif True:
            tmp = _ULong___init__impl_(Long(1, 0))
        
        return tmp
    
    if dividend.compareTo(Long(0, 0)) >= 0:
        return _ULong___init__impl_(dividend.div(divisor))
    
    quotient = dividend.ushr(1).div(divisor).shl(1)
    rem = dividend.minus(quotient.times(divisor))
    tmp0_compareTo_0 = _ULong___init__impl_(rem)
    tmp1_compareTo_0 = _ULong___init__impl_(divisor)
    if ulongCompare(_ULong___get_data__impl_(tmp0_compareTo_0), _ULong___get_data__impl_(tmp1_compareTo_0)) >= 0:
        tmp = 1
    elif True:
        tmp = 0
    
    tmp2_plus_0 = tmp
    return _ULong___init__impl_(quotient.plus(toLong(tmp2_plus_0)))

def ulongRemainder(v1, v2):
    dividend = _ULong___get_data__impl_(v1)
    divisor = _ULong___get_data__impl_(v2)
    if divisor.compareTo(Long(0, 0)) < 0:
        if ulongCompare(_ULong___get_data__impl_(v1), _ULong___get_data__impl_(v2)) < 0:
            tmp = v1
        elif True:
            tmp = _ULong___init__impl_(_ULong___get_data__impl_(v1).minus(_ULong___get_data__impl_(v2)))
        
        return tmp
    
    if dividend.compareTo(Long(0, 0)) >= 0:
        return _ULong___init__impl_(dividend.rem(divisor))
    
    quotient = dividend.ushr(1).div(divisor).shl(1)
    rem = dividend.minus(quotient.times(divisor))
    tmp0_compareTo_0 = _ULong___init__impl_(rem)
    tmp1_compareTo_0 = _ULong___init__impl_(divisor)
    if ulongCompare(_ULong___get_data__impl_(tmp0_compareTo_0), _ULong___get_data__impl_(tmp1_compareTo_0)) >= 0:
        tmp = divisor
    elif True:
        tmp = Long(0, 0)
    
    return _ULong___init__impl_(rem.minus(tmp))

def ulongToDouble(v):
    return (v.ushr(11).toDouble() * 2048) + v._and(Long(2047, 0)).toDouble()

def ulongToString(v):
    return ulongToString(v, 10)

def ulongToString(v, base):
    if v.compareTo(Long(0, 0)) >= 0:
        return toString(base)
    
    tmp0_div_0 = v.ushr(1)
    quotient = tmp0_div_0.div(toLong(base)).shl(1)
    tmp1_times_0 = quotient
    rem = v.minus(tmp1_times_0.times(toLong(base)))
    if rem.compareTo(toLong(base)) >= 0:
        tmp2_minus_0 = rem
        rem = tmp2_minus_0.minus(toLong(base))
        tmp3_plus_0 = quotient
        quotient = tmp3_plus_0.plus(Long(1, 0))
    
    return toString(base) + toString(base)

def doubleToUInt(v):
    if isNaN():
        tmp = _UInt___init__impl_(0)
    else:
        Companion_getInstance()
        tmp0_toDouble_0 = _UInt___init__impl_(0)
        if v <= uintToDouble(_UInt___get_data__impl_(tmp0_toDouble_0)):
            Companion_getInstance()
            tmp = _UInt___init__impl_(0)
        else:
            Companion_getInstance()
            tmp1_toDouble_0 = _UInt___init__impl_(-1)
            if v >= uintToDouble(_UInt___get_data__impl_(tmp1_toDouble_0)):
                Companion_getInstance()
                tmp = _UInt___init__impl_(-1)
            elif v <= kotlin_Double(IntCompanionObject_getInstance().MAX_VALUE):
                tmp2_toUInt_0 = numberToInt(v)
                tmp = _UInt___init__impl_(tmp2_toUInt_0)
            elif True:
                tmp3_toUInt_0 = numberToInt(v - IntCompanionObject_getInstance().MAX_VALUE)
                tmp5_plus_0 = _UInt___init__impl_(tmp3_toUInt_0)
                tmp4_toUInt_0 = IntCompanionObject_getInstance().MAX_VALUE
                tmp6_plus_0 = _UInt___init__impl_(tmp4_toUInt_0)
                tmp = _UInt___init__impl_((_UInt___get_data__impl_(tmp5_plus_0) + _UInt___get_data__impl_(tmp6_plus_0)) | 0)
            
        
    
    return tmp

def doubleToULong(v):
    if isNaN():
        tmp = _ULong___init__impl_(Long(0, 0))
    else:
        Companion_getInstance()
        tmp0_toDouble_0 = _ULong___init__impl_(Long(0, 0))
        if v <= ulongToDouble(_ULong___get_data__impl_(tmp0_toDouble_0)):
            Companion_getInstance()
            tmp = _ULong___init__impl_(Long(0, 0))
        else:
            Companion_getInstance()
            tmp1_toDouble_0 = _ULong___init__impl_(Long(-1, -1))
            if v >= ulongToDouble(_ULong___get_data__impl_(tmp1_toDouble_0)):
                Companion_getInstance()
                tmp = _ULong___init__impl_(Long(-1, -1))
            else:
                Companion_getInstance()
                if v < Long(-1, 2147483647).toDouble():
                    tmp2_toULong_0 = numberToLong(v)
                    tmp = _ULong___init__impl_(tmp2_toULong_0)
                elif True:
                    tmp3_toULong_0 = numberToLong(v - 9.223372036854776E18)
                    tmp4_plus_0 = _ULong___init__impl_(tmp3_toULong_0)
                    tmp = _ULong___init__impl_(_ULong___get_data__impl_(tmp4_plus_0).plus(_ULong___get_data__impl_(_ULong___init__impl_(Long(0, -2147483648)))))
                
            
        
    
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
    def __init__(self, *names):
        self.names = names
    
    def _get_names_(self):
        return self.names
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

pass
pass
pass
def values():
    return DeprecationLevel_WARNING_getInstance()

def valueOf(value):
    if 'WARNING' == value:
        return DeprecationLevel_WARNING_getInstance()
    elif 'ERROR' == value:
        return DeprecationLevel_ERROR_getInstance()
    elif 'HIDDEN' == value:
        return DeprecationLevel_HIDDEN_getInstance()
    else:
        DeprecationLevel_initEntries()
        THROW_ISE()
    

pass
def DeprecationLevel_initEntries():
    if DeprecationLevel_entriesInitialized:
        return Unit_getInstance()
    
    DeprecationLevel_entriesInitialized = True
    DeprecationLevel_WARNING_instance = DeprecationLevel('WARNING', 0)
    DeprecationLevel_ERROR_instance = DeprecationLevel('ERROR', 1)
    DeprecationLevel_HIDDEN_instance = DeprecationLevel('HIDDEN', 2)

class DeprecationLevel:
    def __init__(self, name, ordinal):
        super(name, ordinal)
    
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
    if not (_mask0 & 2 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    if not (_mask0 & 4 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    super(message, replaceWith, level)
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
    def __init__(self, expression, *imports):
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
    

def DeprecatedSinceKotlin_init__Init_(warningSince, errorSince, hiddenSince, _mask0, _marker, _this):
    if not (_mask0 & 1 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    if not (_mask0 & 2 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    if not (_mask0 & 4 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    super(warningSince, errorSince, hiddenSince)
    return _this

def DeprecatedSinceKotlin_init__Create_(warningSince, errorSince, hiddenSince, _mask0, _marker):
    return DeprecatedSinceKotlin_init__Init_(warningSince, errorSince, hiddenSince, _mask0, _marker, Object_create())

class DeprecatedSinceKotlin:
    def __init__(self, warningSince, errorSince, hiddenSince):
        self.warningSince = warningSince
        self.errorSince = errorSince
        self.hiddenSince = hiddenSince
    
    def _get_warningSince_(self):
        return self.warningSince
    
    def _get_errorSince_(self):
        return self.errorSince
    
    def _get_hiddenSince_(self):
        return self.hiddenSince
    
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
        super()
        self.step = step
        self.finalElement = last
        self.hasNext = (first <= last) if (self.step > 0) else (first >= last)
        self.next = (first) if (self.hasNext) else (self.finalElement)
    
    def _get_step_(self):
        return self.step
    
    def hasNext(self):
        return self.hasNext
    
    def nextInt(self):
        value = self.next
        if value == self.finalElement:
            if not self.hasNext:
                visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl
            
            self.hasNext = False
        else:
            tmp0_this = self
            tmp0_this.next = (tmp0_this.next + self.step) | 0
        
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
        super()
        self.step = step
        self.finalElement = last
        self.hasNext = (first.compareTo(last) <= 0) if (self.step.compareTo(Long(0, 0)) > 0) else (first.compareTo(last) >= 0)
        self.next = (first) if (self.hasNext) else (self.finalElement)
    
    def _get_step_(self):
        return self.step
    
    def hasNext(self):
        return self.hasNext
    
    def nextLong(self):
        value = self.next
        if value.equals(self.finalElement):
            if not self.hasNext:
                visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl
            
            self.hasNext = False
        else:
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
        super()
        self.step = step
        tmp = self
        tmp.finalElement = last.toInt()
        self.hasNext = (first.compareTo(last) <= 0) if (self.step > 0) else (first.compareTo(last) >= 0)
        tmp = self
        if self.hasNext:
            tmp = first.toInt()
        else:
            tmp = self.finalElement
        
        tmp.next = tmp
    
    def _get_step_(self):
        return self.step
    
    def hasNext(self):
        return self.hasNext
    
    def nextChar(self):
        value = self.next
        if value == self.finalElement:
            if not self.hasNext:
                visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl
            
            self.hasNext = False
        else:
            tmp0_this = self
            tmp0_this.next = (tmp0_this.next + self.step) | 0
        
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
    

pass
def Companion_getInstance():
    if Companion_instance == None:
        Companion()
    
    return Companion_instance

class IntProgression:
    def __init__(self, start, endInclusive, step):
        Companion_getInstance()
        if step == 0:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl
        
        if step == IntCompanionObject_getInstance().MIN_VALUE:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl
        
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
        return IntProgressionIterator(self.first, self.last, self.step)
    
    def isEmpty(self):
        return (self.first > self.last) if (self.step > 0) else (self.first < self.last)
    
    def equals(self, other):
        if jsInstanceOf(other, jsClass()):
            tmp = (True) if ((kotlin_ranges_IntProgression(other).isEmpty()) if (self.isEmpty()) else (False)) else ((self.step == kotlin_ranges_IntProgression(other).step) if ((self.last == kotlin_ranges_IntProgression(other).last) if (self.first == kotlin_ranges_IntProgression(other).first) else (False)) else (False))
        elif True:
            tmp = False
        
        return tmp
    
    def hashCode(self):
        return (-1) if (self.isEmpty()) else ((imul(31, (imul(31, self.first) + self.last) | 0) + self.step) | 0)
    
    def toString(self):
        return ((((str(self.first) + str('..')) + str(self.last)) + str(' step ')) + str(self.step)) if (self.step > 0) else ((((str(self.first) + str(' downTo ')) + str(self.last)) + str(' step ')) + str(-self.step | 0))
    

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
    

pass
def Companion_getInstance():
    if Companion_instance == None:
        Companion()
    
    return Companion_instance

class LongProgression:
    def __init__(self, start, endInclusive, step):
        Companion_getInstance()
        if step.equals(Long(0, 0)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl
        
        Companion_getInstance()
        if step.equals(Long(0, -2147483648)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl
        
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
        return LongProgressionIterator(self.first, self.last, self.step)
    
    def isEmpty(self):
        return (self.first.compareTo(self.last) > 0) if (self.step.compareTo(Long(0, 0)) > 0) else (self.first.compareTo(self.last) < 0)
    
    def equals(self, other):
        if jsInstanceOf(other, jsClass()):
            tmp = (True) if ((kotlin_ranges_LongProgression(other).isEmpty()) if (self.isEmpty()) else (False)) else ((self.step.equals(kotlin_ranges_LongProgression(other).step)) if ((self.last.equals(kotlin_ranges_LongProgression(other).last)) if (self.first.equals(kotlin_ranges_LongProgression(other).first)) else (False)) else (False))
        elif True:
            tmp = False
        
        return tmp
    
    def hashCode(self):
        return (-1) if (self.isEmpty()) else (numberToLong(31).times(numberToLong(31).times(self.first.xor(self.first.ushr(32))).plus(self.last.xor(self.last.ushr(32)))).plus(self.step.xor(self.step.ushr(32))).toInt())
    
    def toString(self):
        return ((((str(self.first) + str('..')) + str(self.last)) + str(' step ')) + str(self.step)) if (self.step.compareTo(Long(0, 0)) > 0) else ((((str(self.first) + str(' downTo ')) + str(self.last)) + str(' step ')) + str(self.step.unaryMinus()))
    

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
    

pass
def Companion_getInstance():
    if Companion_instance == None:
        Companion()
    
    return Companion_instance

class CharProgression:
    def __init__(self, start, endInclusive, step):
        Companion_getInstance()
        if step == 0:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl
        
        if step == IntCompanionObject_getInstance().MIN_VALUE:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl
        
        self.first = start
        tmp = self
        tmp = start.toInt()
        tmp.last = numberToChar(getProgressionLastElement(tmp, endInclusive.toInt(), step))
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
        return (self.first.compareTo(self.last) > 0) if (self.step > 0) else (self.first.compareTo(self.last) < 0)
    
    def equals(self, other):
        if jsInstanceOf(other, jsClass()):
            tmp = (True) if ((kotlin_ranges_CharProgression(other).isEmpty()) if (self.isEmpty()) else (False)) else ((self.step == kotlin_ranges_CharProgression(other).step) if ((self.last.equals(kotlin_ranges_CharProgression(other).last)) if (self.first.equals(kotlin_ranges_CharProgression(other).first)) else (False)) else (False))
        elif True:
            tmp = False
        
        return tmp
    
    def hashCode(self):
        if self.isEmpty():
            tmp = -1
        else:
            tmp0__get_code__0 = self.first
            tmp = imul(31, tmp0__get_code__0.toInt())
            tmp1__get_code__0 = self.last
            tmp = (imul(31, (tmp + tmp1__get_code__0.toInt()) | 0) + self.step) | 0
        
        return tmp
    
    def toString(self):
        return ((((str(self.first) + str('..')) + str(self.last)) + str(' step ')) + str(self.step)) if (self.step > 0) else ((((str(self.first) + str(' downTo ')) + str(self.last)) + str(' step ')) + str(-self.step | 0))
    

class ClosedRange:
    def _get_start_(self):
        pass
    
    def _get_endInclusive_(self):
        pass
    
    def contains(self, value):
        return (compareTo(value, self._get_endInclusive_()) <= 0) if (compareTo(value, self._get_start_()) >= 0) else (False)
    
    def isEmpty(self):
        return compareTo(self._get_start_(), self._get_endInclusive_()) > 0
    
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
    

pass
def Companion_getInstance():
    if Companion_instance == None:
        Companion()
    
    return Companion_instance

class IntRange:
    def __init__(self, start, endInclusive):
        Companion_getInstance()
        super(start, endInclusive, 1)
    
    def _get_start_(self):
        return self._get_first_()
    
    def _get_endInclusive_(self):
        return self._get_last_()
    
    def contains(self, value):
        return (value <= self._get_last_()) if (self._get_first_() <= value) else (False)
    
    def contains(self, value):
        return self.contains((kotlin_Int(value)) if (jsTypeOf(value) == 'number') else (THROW_CCE()))
    
    def isEmpty(self):
        return self._get_first_() > self._get_last_()
    
    def equals(self, other):
        if jsInstanceOf(other, jsClass()):
            tmp = (True) if ((kotlin_ranges_IntRange(other).isEmpty()) if (self.isEmpty()) else (False)) else ((self._get_last_() == kotlin_ranges_IntRange(other)._get_last_()) if (self._get_first_() == kotlin_ranges_IntRange(other)._get_first_()) else (False))
        elif True:
            tmp = False
        
        return tmp
    
    def hashCode(self):
        return (-1) if (self.isEmpty()) else ((imul(31, self._get_first_()) + self._get_last_()) | 0)
    
    def toString(self):
        return (str(self._get_first_()) + str('..')) + str(self._get_last_())
    
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
    

pass
def Companion_getInstance():
    if Companion_instance == None:
        Companion()
    
    return Companion_instance

class LongRange:
    def __init__(self, start, endInclusive):
        Companion_getInstance()
        super(start, endInclusive, Long(1, 0))
    
    def _get_start_(self):
        return self._get_first_()
    
    def _get_endInclusive_(self):
        return self._get_last_()
    
    def contains(self, value):
        return (value.compareTo(self._get_last_()) <= 0) if (self._get_first_().compareTo(value) <= 0) else (False)
    
    def contains(self, value):
        return self.contains((kotlin_Long(value)) if (jsInstanceOf(value, jsClass())) else (THROW_CCE()))
    
    def isEmpty(self):
        return self._get_first_().compareTo(self._get_last_()) > 0
    
    def equals(self, other):
        if jsInstanceOf(other, jsClass()):
            tmp = (True) if ((kotlin_ranges_LongRange(other).isEmpty()) if (self.isEmpty()) else (False)) else ((self._get_last_().equals(kotlin_ranges_LongRange(other)._get_last_())) if (self._get_first_().equals(kotlin_ranges_LongRange(other)._get_first_())) else (False))
        elif True:
            tmp = False
        
        return tmp
    
    def hashCode(self):
        return (-1) if (self.isEmpty()) else (numberToLong(31).times(self._get_first_().xor(self._get_first_().ushr(32))).plus(self._get_last_().xor(self._get_last_().ushr(32))).toInt())
    
    def toString(self):
        return (str(self._get_first_()) + str('..')) + str(self._get_last_())
    
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
    

pass
def Companion_getInstance():
    if Companion_instance == None:
        Companion()
    
    return Companion_instance

class CharRange:
    def __init__(self, start, endInclusive):
        Companion_getInstance()
        super(start, endInclusive, 1)
    
    def _get_start_(self):
        return self._get_first_()
    
    def _get_endInclusive_(self):
        return self._get_last_()
    
    def contains(self, value):
        return (value.compareTo(self._get_last_()) <= 0) if (self._get_first_().compareTo(value) <= 0) else (False)
    
    def contains(self, value):
        return self.contains((kotlin_Char(value)) if (jsInstanceOf(value, jsClass())) else (THROW_CCE()))
    
    def isEmpty(self):
        return self._get_first_().compareTo(self._get_last_()) > 0
    
    def equals(self, other):
        if jsInstanceOf(other, jsClass()):
            tmp = (True) if ((kotlin_ranges_CharRange(other).isEmpty()) if (self.isEmpty()) else (False)) else ((self._get_last_().equals(kotlin_ranges_CharRange(other)._get_last_())) if (self._get_first_().equals(kotlin_ranges_CharRange(other)._get_first_())) else (False))
        elif True:
            tmp = False
        
        return tmp
    
    def hashCode(self):
        if self.isEmpty():
            tmp = -1
        else:
            tmp0__get_code__0 = self._get_first_()
            tmp = imul(31, tmp0__get_code__0.toInt())
            tmp1__get_code__0 = self._get_last_()
            tmp = (tmp + tmp1__get_code__0.toInt()) | 0
        
        return tmp
    
    def toString(self):
        return (str(self._get_first_()) + str('..')) + str(self._get_last_())
    
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
    

Unit_instance = None
def Unit_getInstance():
    if Unit_instance == None:
        Unit()
    
    return Unit_instance

class Target:
    def __init__(self, *allowedTargets):
        self.allowedTargets = allowedTargets
    
    def _get_allowedTargets_(self):
        return self.allowedTargets
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
def values():
    return AnnotationTarget_CLASS_getInstance()

def valueOf(value):
    if 'CLASS' == value:
        return AnnotationTarget_CLASS_getInstance()
    elif 'ANNOTATION_CLASS' == value:
        return AnnotationTarget_ANNOTATION_CLASS_getInstance()
    elif 'TYPE_PARAMETER' == value:
        return AnnotationTarget_TYPE_PARAMETER_getInstance()
    elif 'PROPERTY' == value:
        return AnnotationTarget_PROPERTY_getInstance()
    elif 'FIELD' == value:
        return AnnotationTarget_FIELD_getInstance()
    elif 'LOCAL_VARIABLE' == value:
        return AnnotationTarget_LOCAL_VARIABLE_getInstance()
    elif 'VALUE_PARAMETER' == value:
        return AnnotationTarget_VALUE_PARAMETER_getInstance()
    elif 'CONSTRUCTOR' == value:
        return AnnotationTarget_CONSTRUCTOR_getInstance()
    elif 'FUNCTION' == value:
        return AnnotationTarget_FUNCTION_getInstance()
    elif 'PROPERTY_GETTER' == value:
        return AnnotationTarget_PROPERTY_GETTER_getInstance()
    elif 'PROPERTY_SETTER' == value:
        return AnnotationTarget_PROPERTY_SETTER_getInstance()
    elif 'TYPE' == value:
        return AnnotationTarget_TYPE_getInstance()
    elif 'EXPRESSION' == value:
        return AnnotationTarget_EXPRESSION_getInstance()
    elif 'FILE' == value:
        return AnnotationTarget_FILE_getInstance()
    elif 'TYPEALIAS' == value:
        return AnnotationTarget_TYPEALIAS_getInstance()
    else:
        AnnotationTarget_initEntries()
        THROW_ISE()
    

pass
def AnnotationTarget_initEntries():
    if AnnotationTarget_entriesInitialized:
        return Unit_getInstance()
    
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
        super(name, ordinal)
    
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
    if not (_mask0 & 1 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    super(value)
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
    

pass
pass
pass
def values():
    return AnnotationRetention_SOURCE_getInstance()

def valueOf(value):
    if 'SOURCE' == value:
        return AnnotationRetention_SOURCE_getInstance()
    elif 'BINARY' == value:
        return AnnotationRetention_BINARY_getInstance()
    elif 'RUNTIME' == value:
        return AnnotationRetention_RUNTIME_getInstance()
    else:
        AnnotationRetention_initEntries()
        THROW_ISE()
    

pass
def AnnotationRetention_initEntries():
    if AnnotationRetention_entriesInitialized:
        return Unit_getInstance()
    
    AnnotationRetention_entriesInitialized = True
    AnnotationRetention_SOURCE_instance = AnnotationRetention('SOURCE', 0)
    AnnotationRetention_BINARY_instance = AnnotationRetention('BINARY', 1)
    AnnotationRetention_RUNTIME_instance = AnnotationRetention('RUNTIME', 2)

class AnnotationRetention:
    def __init__(self, name, ordinal):
        super(name, ordinal)
    
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
    if step > 0:
        tmp = (end) if (start >= end) else ((end - differenceModulo(end, start, step)) | 0)
    elif step < 0:
        tmp = (end) if (start <= end) else ((end + differenceModulo(start, end, -step | 0)) | 0)
    else:
        raise IllegalArgumentException_init__Create_('Step is zero.')
    
    return tmp

def getProgressionLastElement(start, end, step):
    if step.compareTo(Long(0, 0)) > 0:
        tmp = (end) if (start.compareTo(end) >= 0) else (end.minus(differenceModulo(end, start, step)))
    elif step.compareTo(Long(0, 0)) < 0:
        tmp = (end) if (start.compareTo(end) <= 0) else (end.plus(differenceModulo(start, end, step.unaryMinus())))
    else:
        raise IllegalArgumentException_init__Create_('Step is zero.')
    
    return tmp

def differenceModulo(a, b, c):
    return mod((mod(a, c) - mod(b, c)) | 0, c)

def differenceModulo(a, b, c):
    return mod(mod(a, c).minus(mod(b, c)), c)

def mod(a, b):
    mod = a % b
    return (mod) if (mod >= 0) else ((mod + b) | 0)

def mod(a, b):
    mod = a.rem(b)
    return (mod) if (mod.compareTo(Long(0, 0)) >= 0) else (mod.plus(b))

class ByteCompanionObject:
    def __init__(self):
        ByteCompanionObject_instance = self
        self.MIN_VALUE = -128
        self.MAX_VALUE = 127
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
    

pass
def ByteCompanionObject_getInstance():
    if ByteCompanionObject_instance == None:
        ByteCompanionObject()
    
    return ByteCompanionObject_instance

class ShortCompanionObject:
    def __init__(self):
        ShortCompanionObject_instance = self
        self.MIN_VALUE = -32768
        self.MAX_VALUE = 32767
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
    

pass
def ShortCompanionObject_getInstance():
    if ShortCompanionObject_instance == None:
        ShortCompanionObject()
    
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
    

pass
def IntCompanionObject_getInstance():
    if IntCompanionObject_instance == None:
        IntCompanionObject()
    
    return IntCompanionObject_instance

class FloatCompanionObject:
    def __init__(self):
        FloatCompanionObject_instance = self
        self.MIN_VALUE = 1.4E-45
        self.MAX_VALUE = 3.4028235E38
        self.POSITIVE_INFINITY = Infinity
        self.NEGATIVE_INFINITY = -Infinity
        self.NaN = NaN
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
    

pass
def FloatCompanionObject_getInstance():
    if FloatCompanionObject_instance == None:
        FloatCompanionObject()
    
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
    

pass
def DoubleCompanionObject_getInstance():
    if DoubleCompanionObject_instance == None:
        DoubleCompanionObject()
    
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
    

pass
def StringCompanionObject_getInstance():
    if StringCompanionObject_instance == None:
        StringCompanionObject()
    
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
    

pass
def BooleanCompanionObject_getInstance():
    if BooleanCompanionObject_instance == None:
        BooleanCompanionObject()
    
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
    if EXCLEQEQ(toArray(collection), _get_undefined_()):
        tmp0_unsafeCast_0 = INVOKE(toArray(collection))
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
    elif True:
        tmp1_unsafeCast_0 = copyToArrayImpl(collection)
        tmp = kotlin_Any_(tmp1_unsafeCast_0)
    
    return tmp

def copyToArrayImpl(collection):
    array = kotlin_Array_kotlin_Any__(js('[]'))
    iterator = collection.iterator()
    while iterator.hasNext():
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    
    return array

def arrayCopy(source, destination, destinationOffset, startIndex, endIndex):
    Companion_getInstance().checkRangeIndexes(startIndex, endIndex, len(source))
    rangeSize = (endIndex - startIndex) | 0
    Companion_getInstance().checkRangeIndexes(destinationOffset, (destinationOffset + rangeSize) | 0, len(destination))
    if ANDAND(INVOKE(isView(js('ArrayBuffer')), destination), INVOKE(isView(js('ArrayBuffer')), source)):
        subrange = INVOKE(subarray(source), startIndex, endIndex)
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    elif (True) if (not (source is destination)) else (destinationOffset <= startIndex):
        inductionVariable = 0
        if inductionVariable < rangeSize:
            while True:
                index = inductionVariable
                inductionVariable = (inductionVariable + 1) | 0
                destination.__setitem__((destinationOffset + index) | 0, source[(startIndex + index) | 0])
                if inductionVariable < rangeSize:
                    break
                
            
        
    else:
        inductionVariable = (rangeSize - 1) | 0
        if 0 <= inductionVariable:
            while True:
                index = inductionVariable
                inductionVariable = (inductionVariable + -1) | 0
                destination.__setitem__((destinationOffset + index) | 0, source[(startIndex + index) | 0])
                if 0 <= inductionVariable:
                    break
                
            
        
    

def copyToArrayImpl(collection, array):
    if len(array) < collection._get_size_():
        tmp0_unsafeCast_0 = copyToArrayImpl(collection)
        return kotlin_Any_(tmp0_unsafeCast_0)
    
    iterator = collection.iterator()
    index = 0
    while iterator.hasNext():
        tmp0 = index
        index = (tmp0 + 1) | 0
        tmp1_unsafeCast_0 = iterator.next()
        array.__setitem__(tmp0, kotlin_Any_(tmp1_unsafeCast_0))
    
    if index < len(array):
        tmp = index
        array.__setitem__(tmp, kotlin_Any_(None))
    
    return array

class _no_name_provided_:
    def __init__(self, _elements):
        self._elements = _elements
    
    def invoke(self, it):
        return self._elements.contains(it)
    
    def invoke(self, p1):
        return self.invoke((E(p1)) if ((True) if (p1 == None) else (isObject(p1))) else (THROW_CCE()))
    

class _no_name_provided_:
    def __init__(self, _elements):
        self._elements = _elements
    
    def invoke(self, it):
        return not self._elements.contains(it)
    
    def invoke(self, p1):
        return self.invoke((E(p1)) if ((True) if (p1 == None) else (isObject(p1))) else (THROW_CCE()))
    

class AbstractMutableCollection:
    def __init__(self):
        super()
    
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
                visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
            
        
        return modified
    
    def removeAll(self, elements):
        self.checkIsMutable()
        tmp = (kotlin_collections_MutableIterable_E_(self)) if (isInterface(self, jsClass())) else (THROW_CCE())
        return removeAll(_no_name_provided__factory(elements))
    
    def retainAll(self, elements):
        self.checkIsMutable()
        tmp = (kotlin_collections_MutableIterable_E_(self)) if (isInterface(self, jsClass())) else (THROW_CCE())
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
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl

def _no_name_provided__factory(_elements):
    i = _no_name_provided_(_elements)
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl

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
        return self.index < self._this._get_size_()
    
    def next(self):
        if not self.hasNext():
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl
        
        tmp = self
        tmp0_this = self
        tmp1 = tmp0_this.index
        tmp0_this.index = (tmp1 + 1) | 0
        tmp.last = tmp1
        return self._this.get(self.last)
    
    def remove(self):
        tmp0_check_0 = not (self.last == -1)
        if not tmp0_check_0:
            message_1 = 'Call next() or previous() before removing element from the iterator.'
            raise IllegalStateException_init__Create_(toString(message_1))
        
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
        super(_outer)
        Companion_getInstance().checkPositionIndex(index, self._this._get_size_())
        self._set_index_(index)
    
    def hasPrevious(self):
        return self._get_index_() > 0
    
    def nextIndex(self):
        return self._get_index_()
    
    def previous(self):
        if not self.hasPrevious():
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl
        
        tmp0_this = self
        tmp0_this._set_index_((tmp0_this._get_index_() - 1) | 0)
        self._set_last_(tmp0_this._get_index_())
        return self._this.get(self._get_last_())
    
    def previousIndex(self):
        return (self._get_index_() - 1) | 0
    
    def add(self, element):
        self._this.add(self._get_index_(), element)
        tmp0_this = self
        tmp1 = tmp0_this._get_index_()
        tmp0_this._set_index_((tmp1 + 1) | 0)
        Unit_getInstance()
        self._set_last_(-1)
    
    def add(self, element):
        return self.add((E(element)) if ((True) if (element == None) else (isObject(element))) else (THROW_CCE()))
    
    def set(self, element):
        tmp0_check_0 = not (self._get_last_() == -1)
        if not tmp0_check_0:
            message_1 = 'Call next() or previous() before updating element value with the iterator.'
            raise IllegalStateException_init__Create_(toString(message_1))
        
        self._this.set(self._get_last_(), element)
        Unit_getInstance()
    
    def set(self, element):
        return self.set((E(element)) if ((True) if (element == None) else (isObject(element))) else (THROW_CCE()))
    
    def _set_index_(self, _set___):
        pass
    
    def _get_index_(self):
        pass
    
    def _set_last_(self, _set___):
        pass
    
    def _get_last_(self):
        pass
    
    def hasNext(self):
        pass
    
    def next(self):
        pass
    
    def remove(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class SubList:
    def __init__(self, list, fromIndex, toIndex):
        super()
        self.list = list
        self.fromIndex = fromIndex
        self._size = 0
        Companion_getInstance().checkRangeIndexes(self.fromIndex, toIndex, self.list._get_size_())
        self._size = (toIndex - self.fromIndex) | 0
    
    def add(self, index, element):
        Companion_getInstance().checkPositionIndex(index, self._size)
        self.list.add((self.fromIndex + index) | 0, element)
        tmp0_this = self
        tmp1 = tmp0_this._size
        tmp0_this._size = (tmp1 + 1) | 0
        Unit_getInstance()
    
    def get(self, index):
        Companion_getInstance().checkElementIndex(index, self._size)
        return self.list.get((self.fromIndex + index) | 0)
    
    def removeAt(self, index):
        Companion_getInstance().checkElementIndex(index, self._size)
        result = self.list.removeAt((self.fromIndex + index) | 0)
        tmp0_this = self
        tmp1 = tmp0_this._size
        tmp0_this._size = (tmp1 - 1) | 0
        Unit_getInstance()
        return result
    
    def set(self, index, element):
        Companion_getInstance().checkElementIndex(index, self._size)
        return self.list.set((self.fromIndex + index) | 0, element)
    
    def _get_size_(self):
        return self._size
    
    def checkIsMutable(self):
        return self.list.checkIsMutable()
    
    def _set_modCount_(self, _set___):
        pass
    
    def _get_modCount_(self):
        pass
    
    def add(self, element):
        pass
    
    def addAll(self, index, elements):
        pass
    
    def addAll(self, elements):
        pass
    
    def clear(self):
        pass
    
    def removeAll(self, elements):
        pass
    
    def retainAll(self, elements):
        pass
    
    def iterator(self):
        pass
    
    def contains(self, element):
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
    
    def removeRange(self, fromIndex, toIndex):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def remove(self, element):
        pass
    
    def toJSON(self):
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
    

class _no_name_provided_:
    def __init__(self, _elements):
        self._elements = _elements
    
    def invoke(self, it):
        return self._elements.contains(it)
    
    def invoke(self, p1):
        return self.invoke((E(p1)) if ((True) if (p1 == None) else (isObject(p1))) else (THROW_CCE()))
    

class _no_name_provided_:
    def __init__(self, _elements):
        self._elements = _elements
    
    def invoke(self, it):
        return not self._elements.contains(it)
    
    def invoke(self, p1):
        return self.invoke((E(p1)) if ((True) if (p1 == None) else (isObject(p1))) else (THROW_CCE()))
    

class AbstractMutableList:
    def __init__(self):
        super()
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
            _index = (tmp1 + 1) | 0
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
        return self.indexOf(element) >= 0
    
    def indexOf(self, element):
        inductionVariable = 0
        last = _get_lastIndex_()
        if inductionVariable <= last:
            while True:
                index = inductionVariable
                inductionVariable = (inductionVariable + 1) | 0
                if equals(self.get(index), element):
                    return index
                
                if not (index == last):
                    break
                
            
        
        return -1
    
    def lastIndexOf(self, element):
        inductionVariable = _get_lastIndex_()
        if 0 <= inductionVariable:
            while True:
                index = inductionVariable
                inductionVariable = (inductionVariable + -1) | 0
                if equals(self.get(index), element):
                    return index
                
                if 0 <= inductionVariable:
                    break
                
            
        
        return -1
    
    def listIterator(self):
        return self.listIterator(0)
    
    def listIterator(self, index):
        return ListIteratorImpl(self, index)
    
    def subList(self, fromIndex, toIndex):
        return SubList(self, fromIndex, toIndex)
    
    def removeRange(self, fromIndex, toIndex):
        iterator = self.listIterator(fromIndex)
        tmp0_repeat_0 = (toIndex - fromIndex) | 0
        inductionVariable = 0
        if inductionVariable < tmp0_repeat_0:
            while True:
                index_2 = inductionVariable
                inductionVariable = (inductionVariable + 1) | 0
                iterator.next()
                Unit_getInstance()
                iterator.remove()
                if inductionVariable < tmp0_repeat_0:
                    break
                
            
        
    
    def equals(self, other):
        if other is self:
            return True
        
        if not ((isInterface(other, jsClass())) if (not (other == None)) else (False)):
            return False
        
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
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl

def _no_name_provided__factory(_elements):
    i = _no_name_provided_(_elements)
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl

def _set_array_(_this, _set___):
    _this.array = _set___

def _get_array_(_this):
    return _this.array

def _set_isReadOnly_(_this, _set___):
    _this.isReadOnly = _set___

def _get_isReadOnly_(_this):
    return _this.isReadOnly

def ArrayList_init__Init_(_this):
    super(kotlin_Array_kotlin_Any__(js('[]')))
    return _this

def ArrayList_init__Create_():
    return ArrayList_init__Init_(Object_create())

def ArrayList_init__Init_(initialCapacity, _this):
    super(kotlin_Array_kotlin_Any__(js('[]')))
    return _this

def ArrayList_init__Create_(initialCapacity):
    return ArrayList_init__Init_(initialCapacity, Object_create())

def ArrayList_init__Init_(initialCapacity, _mask0, _marker, _this):
    if not (_mask0 & 1 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    ArrayList_init__Init_(initialCapacity, _this)
    return _this

def ArrayList_init__Create_(initialCapacity, _mask0, _marker):
    return ArrayList_init__Init_(initialCapacity, _mask0, _marker, Object_create())

def ArrayList_init__Init_(elements, _this):
    super(copyToArray(elements))
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
        super()
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
        return len(self.array)
    
    def get(self, index):
        tmp = self.array[rangeCheck(self, index)]
        return (E(tmp)) if ((True) if (tmp == None) else (isObject(tmp))) else (THROW_CCE())
    
    def set(self, index, element):
        self.checkIsMutable()
        rangeCheck(self, index)
        Unit_getInstance()
        tmp0_apply_0 = self.array[index]
        self.array.__setitem__(index, element)
        tmp = tmp0_apply_0
        return (E(tmp)) if ((True) if (tmp == None) else (isObject(tmp))) else (THROW_CCE())
    
    def add(self, element):
        self.checkIsMutable()
        tmp0_asDynamic_0 = self.array
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
        tmp0_this = self
        tmp1 = tmp0_this._get_modCount_()
        tmp0_this._set_modCount_((tmp1 + 1) | 0)
        Unit_getInstance()
        return True
    
    def add(self, index, element):
        self.checkIsMutable()
        tmp0_asDynamic_0 = self.array
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
        tmp0_this = self
        tmp1 = tmp0_this._get_modCount_()
        tmp0_this._set_modCount_((tmp1 + 1) | 0)
        Unit_getInstance()
    
    def addAll(self, elements):
        self.checkIsMutable()
        if elements.isEmpty():
            return False
        
        tmp0_this = self
        tmp = tmp0_this
        tmp0_plus_0 = tmp0_this.array
        tmp1_plus_0 = copyToArray(elements)
        tmp.array = kotlin_Array_kotlin_Any__(INVOKE(concat(tmp0_plus_0), tmp1_plus_0))
        tmp1_this = self
        tmp2 = tmp1_this._get_modCount_()
        tmp1_this._set_modCount_((tmp2 + 1) | 0)
        Unit_getInstance()
        return True
    
    def addAll(self, index, elements):
        self.checkIsMutable()
        insertionRangeCheck(self, index)
        Unit_getInstance()
        if index == self._get_size_():
            return self.addAll(elements)
        
        if elements.isEmpty():
            return False
        
        tmp0_subject = index
        if tmp0_subject == self._get_size_():
            return self.addAll(elements)
        elif tmp0_subject == 0:
            tmp = self
            tmp0_plus_0 = copyToArray(elements)
            tmp1_plus_0 = self.array
            tmp.array = kotlin_Array_kotlin_Any__(INVOKE(concat(tmp0_plus_0), tmp1_plus_0))
        else:
            tmp = self
            tmp2_asDynamic_0 = copyOfRange(0, index)
            tmp.array = kotlin_Array_kotlin_Any__(INVOKE(concat(tmp2_asDynamic_0), copyToArray(elements), copyOfRange(index, self._get_size_())))
        
        tmp1_this = self
        tmp2 = tmp1_this._get_modCount_()
        tmp1_this._set_modCount_((tmp2 + 1) | 0)
        Unit_getInstance()
        return True
    
    def removeAt(self, index):
        self.checkIsMutable()
        rangeCheck(self, index)
        Unit_getInstance()
        tmp0_this = self
        tmp1 = tmp0_this._get_modCount_()
        tmp0_this._set_modCount_((tmp1 + 1) | 0)
        Unit_getInstance()
        if index == _get_lastIndex_():
            tmp0_asDynamic_0 = self.array
            tmp = E(INVOKE(pop(tmp0_asDynamic_0)))
        else:
            tmp1_asDynamic_0 = self.array
            tmp = E(ARRAY_ACCESS(INVOKE(splice(tmp1_asDynamic_0), index, 1), 0))
        
        return tmp
    
    def remove(self, element):
        self.checkIsMutable()
        inductionVariable = 0
        last = (len(self.array) - 1) | 0
        if inductionVariable <= last:
            while True:
                index = inductionVariable
                inductionVariable = (inductionVariable + 1) | 0
                if equals(self.array[index], element):
                    tmp0_asDynamic_0 = self.array
                    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
                    tmp1_this = self
                    tmp2 = tmp1_this._get_modCount_()
                    tmp1_this._set_modCount_((tmp2 + 1) | 0)
                    Unit_getInstance()
                    return True
                
                if inductionVariable <= last:
                    break
                
            
        
        return False
    
    def removeRange(self, fromIndex, toIndex):
        self.checkIsMutable()
        tmp0_this = self
        tmp1 = tmp0_this._get_modCount_()
        tmp0_this._set_modCount_((tmp1 + 1) | 0)
        Unit_getInstance()
        tmp0_asDynamic_0 = self.array
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    
    def clear(self):
        self.checkIsMutable()
        tmp = self
        tmp.array = kotlin_Array_kotlin_Any__(js('[]'))
        tmp0_this = self
        tmp1 = tmp0_this._get_modCount_()
        tmp0_this._set_modCount_((tmp1 + 1) | 0)
        Unit_getInstance()
    
    def indexOf(self, element):
        return indexOf(element)
    
    def lastIndexOf(self, element):
        return lastIndexOf(element)
    
    def toString(self):
        return arrayToString(self.array)
    
    def toArray(self, array):
        if len(array) < self._get_size_():
            tmp = self.toArray()
            return (kotlin_Array_T_(tmp)) if (isArray(tmp)) else (THROW_CCE())
        
        tmp = self.array
        tmp0_copyInto_0 = (kotlin_Array_T_(tmp)) if (isArray(tmp)) else (THROW_CCE())
        tmp1_copyInto_0 = len(tmp0_copyInto_0)
        arrayCopy(tmp0_copyInto_0, array, 0, 0, tmp1_copyInto_0)
        Unit_getInstance()
        if len(array) > self._get_size_():
            tmp = self._get_size_()
            array.__setitem__(tmp, (T(None)) if ((True) if (None == None) else (isObject(None))) else (THROW_CCE()))
        
        return array
    
    def toArray(self):
        return kotlin_Array_kotlin_Any__(INVOKE(call(slice(js('[]'))), self.array))
    
    def toArray(self):
        return self.toArray()
    
    def checkIsMutable(self):
        if self.isReadOnly:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrThrowImpl
        
    
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
    

def _set__stableSortingIsSupported_(_set___):
    _stableSortingIsSupported = _set___

def _get__stableSortingIsSupported_():
    return _stableSortingIsSupported

_stableSortingIsSupported = None
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
    init_properties_console_kt()
    output = _set___

def _get_output_():
    init_properties_console_kt()
    return output

output = None
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
        super()
        self.outputStream = outputStream
    
    def _get_outputStream_(self):
        return self.outputStream
    
    def print(self, message):
        messageString = kotlin_String(INVOKE(js('String'), message))
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    
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
        super()
    
    def print(self, message):
        s = kotlin_String(INVOKE(js('String'), message))
        tmp0_nativeLastIndexOf_0 = s
        i = kotlin_Int(INVOKE(lastIndexOf(tmp0_nativeLastIndexOf_0), '\n', 0))
        if i >= 0:
            tmp0_this = self
            tmp = tmp0_this._get_buffer_()
            tmp1_substring_0 = s
            tmp0_this._set_buffer_(tmp + kotlin_String(INVOKE(substring(tmp1_substring_0), 0, i)))
            self.flush()
            tmp2_substring_0 = s
            tmp3_substring_0 = (i + 1) | 0
            s = kotlin_String(INVOKE(substring(tmp2_substring_0), tmp3_substring_0))
        
        tmp1_this = self
        tmp1_this._set_buffer_(tmp1_this._get_buffer_() + s)
    
    def flush(self):
        _get_console_().log(self._get_buffer_())
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
    init_properties_console_kt()
    return kotlin_String(INVOKE(js('String'), value))

class BufferedOutput:
    def __init__(self):
        super()
        self.buffer = ''
    
    def _set_buffer_(self, _set___):
        self.buffer = _set___
    
    def _get_buffer_(self):
        return self.buffer
    
    def print(self, message):
        tmp0_this = self
        tmp = tmp0_this
        tmp = tmp0_this.buffer
        tmp.buffer = tmp + kotlin_String(INVOKE(js('String'), message))
    
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
    

properties_initialized_console_kt = False
def init_properties_console_kt():
    global properties_initialized_console_kt
    if not properties_initialized_console_kt:
        properties_initialized_console_kt = True
        global output
        isNode_2 = kotlin_Boolean(js('typeof process !== \'undefined\' && process.versions && !!process.versions.node'))
        output = (NodeJsOutput(js('process.stdout'))) if (isNode_2) else (BufferedOutputToConsoleLog())
    

def _get_EmptyContinuation_():
    init_properties_EmptyContinuation_kt()
    return EmptyContinuation

EmptyContinuation = None
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
        if (True) if (tmp == None) else (isObject(tmp)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrTypeOperatorCallImpl
        else:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCallImpl
        
        return Unit_getInstance()
    
    def resumeWith(self, result):
        return self.resumeWith_3(result)
    
    def equals_4(self, other):
        pass
    
    def hashCode_5(self):
        pass
    
    def toString_6(self):
        pass
    

properties_initialized_EmptyContinuation_kt = False
def init_properties_EmptyContinuation_kt():
    global properties_initialized_EmptyContinuation_kt
    if not properties_initialized_EmptyContinuation_kt:
        properties_initialized_EmptyContinuation_kt = True
        global EmptyContinuation
        tmp0_Continuation_0 = EmptyCoroutineContext_getInstance()
        EmptyContinuation = _no_name_provided__1(tmp0_Continuation_0)
    

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
    return visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl.pow(self, kotlin_Double(n))

def isNaN():
    return not (self == self)

def _get_INV_2_26_():
    init_properties_PlatformRandom_kt()
    return INV_2_26

INV_2_26 = None
def _get_INV_2_53_():
    init_properties_PlatformRandom_kt()
    return INV_2_53

INV_2_53 = None
properties_initialized_PlatformRandom_kt = False
def init_properties_PlatformRandom_kt():
    global properties_initialized_PlatformRandom_kt
    if not properties_initialized_PlatformRandom_kt:
        properties_initialized_PlatformRandom_kt = True
        global INV_2_26
        INV_2_26 = visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl.pow(2.0, -26.0)
        global INV_2_53
        INV_2_53 = visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl.pow(2.0, -53.0)
    

def _get_js_():
    return ((kotlin_reflect_js_internal_KClassImpl_T_(self)) if (jsInstanceOf(self, jsClass())) else (THROW_CCE()))._get_jClass_()

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
        raise NotImplementedError_init__Create_(None, 1, None)
    
    def equals(self, other):
        if jsInstanceOf(other, jsClass()):
            tmp = equals(self._get_jClass_(), kotlin_reflect_js_internal_KClassImpl___(other)._get_jClass_())
        elif True:
            tmp = False
        
        return tmp
    
    def hashCode(self):
        tmp0_safe_receiver = self._get_simpleName_()
        tmp1_elvis_lhs = (None) if (tmp0_safe_receiver == None) else (getStringHashCode(tmp0_safe_receiver))
        return (0) if (tmp1_elvis_lhs == None) else (tmp1_elvis_lhs)
    
    def toString(self):
        return str('class ') + str(self._get_simpleName_())
    
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
        super(jClass)
        self.givenSimpleName = givenSimpleName
        self.isInstanceFunction = isInstanceFunction
    
    def equals(self, other):
        if not jsInstanceOf(other, jsClass()):
            return False
        
        return (self.givenSimpleName == kotlin_reflect_js_internal_PrimitiveKClassImpl___(other).givenSimpleName) if (self.equals(other)) else (False)
    
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
        super(kotlin_js_JsClass_kotlin_Nothing_(js('Object')))
        self.simpleName = 'Nothing'
    
    def _get_simpleName_(self):
        return self.simpleName
    
    def isInstance(self, value):
        return False
    
    def _get_jClass_(self):
        raise UnsupportedOperationException_init__Create_('There\'s no native JS class for Nothing type')
    
    def equals(self, other):
        return other is self
    
    def hashCode(self):
        return 0
    
    def _get_qualifiedName_(self):
        pass
    
    def toString(self):
        pass
    

pass
def NothingKClassImpl_getInstance():
    if NothingKClassImpl_instance == None:
        NothingKClassImpl()
    
    return NothingKClassImpl_instance

class ErrorKClass:
    def __init__(self):
        pass
    
    def _get_simpleName_(self):
        raise IllegalStateException_init__Create_('Unknown simpleName for ErrorKClass')
    
    def _get_qualifiedName_(self):
        raise IllegalStateException_init__Create_('Unknown qualifiedName for ErrorKClass')
    
    def isInstance(self, value):
        raise IllegalStateException_init__Create_('Can\'s check isInstance on ErrorKClass')
    
    def equals(self, other):
        return other is self
    
    def hashCode(self):
        return 0
    
    def toString(self):
        pass
    

class SimpleKClassImpl:
    def __init__(self, jClass):
        super(jClass)
        tmp = self
        tmp0_safe_receiver = _metadata_(jClass)
        tmp0_unsafeCast_0 = (None) if (tmp0_safe_receiver == None) else (simpleName(tmp0_safe_receiver))
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
    kVariance = (KVariance_IN_getInstance()) if (tmp0_subject == 'in') else ((KVariance_OUT_getInstance()) if (tmp0_subject == 'out') else (KVariance_INVARIANT_getInstance()))
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
    if self.variance == None:
        return '*'
    
    return prefixString() + toString()

class _no_name_provided_:
    def __init__(self, this_0):
        self.this_0 = this_0
    
    def invoke(self, it):
        return asString(self.this_0)
    
    def invoke(self, p1):
        return self.invoke((kotlin_reflect_KTypeProjection(p1)) if (jsInstanceOf(p1, jsClass())) else (THROW_CCE()))
    

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
        if jsInstanceOf(other, jsClass()):
            tmp = equals(self.classifier, kotlin_reflect_js_internal_KTypeImpl(other).classifier)
        elif True:
            tmp = False
        
        if tmp:
            tmp = equals(self.arguments, kotlin_reflect_js_internal_KTypeImpl(other).arguments)
        elif True:
            tmp = False
        
        if tmp:
            tmp = self.isMarkedNullable == kotlin_reflect_js_internal_KTypeImpl(other).isMarkedNullable
        elif True:
            tmp = False
        
        return tmp
    
    def hashCode(self):
        return (imul((imul(hashCode(self.classifier), 31) + hashCode(self.arguments)) | 0, 31) + (self.isMarkedNullable | 0)) | 0
    
    def toString(self):
        tmp = self.classifier
        kClass = (kotlin_reflect_KClass___(tmp)) if (isInterface(tmp, jsClass())) else (None)
        classifierName = (toString(self.classifier)) if (kClass == None) else ((kClass._get_simpleName_()) if (not (kClass._get_simpleName_() == None)) else ('(non-denotable type)'))
        if self.arguments.isEmpty():
            tmp = ''
        else:
            tmp = joinToString_default(', ', '<', '>', 0, None, _no_name_provided__factory(self), 24, None)
        
        args = tmp
        nullable = ('?') if (self.isMarkedNullable) else ('')
        return plus(args) + nullable
    

def prefixString():
    tmp0_subject = self
    if tmp0_subject.equals(KVariance_INVARIANT_getInstance()):
        tmp = ''
    elif tmp0_subject.equals(KVariance_IN_getInstance()):
        tmp = 'in '
    elif tmp0_subject.equals(KVariance_OUT_getInstance()):
        tmp = 'out '
    else:
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
    

pass
def DynamicKType_getInstance():
    if DynamicKType_instance == None:
        DynamicKType()
    
    return DynamicKType_instance

def _no_name_provided__factory(this_0):
    i = _no_name_provided_(this_0)
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl

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
        if not (_mask0 & 1 == 0):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
        
        if not (_mask0 & 2 == 0):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
        
        if not (_mask0 & 4 == 0):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
        
        if not (_mask0 & 8 == 0):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
        
        return self.copy(kotlin_String(name), kotlin_collections_List_kotlin_reflect_KType_(upperBounds), kotlin_reflect_KVariance(variance), isReified)
    
    def hashCode(self):
        result = getStringHashCode(self.name)
        result = (imul(result, 31) + hashCode(self.upperBounds)) | 0
        result = (imul(result, 31) + self.variance.hashCode()) | 0
        result = (imul(result, 31) + (self.isReified | 0)) | 0
        return result
    
    def equals(self, other):
        if self is other:
            return True
        
        if not jsInstanceOf(other, jsClass()):
            return False
        
        tmp0_other_with_cast = (kotlin_reflect_js_internal_KTypeParameterImpl(other)) if (jsInstanceOf(other, jsClass())) else (THROW_CCE())
        if not (self.name == tmp0_other_with_cast.name):
            return False
        
        if not equals(self.upperBounds, tmp0_other_with_cast.upperBounds):
            return False
        
        if not self.variance.equals(tmp0_other_with_cast.variance):
            return False
        
        if not (self.isReified == tmp0_other_with_cast.isReified):
            return False
        
        return True
    

def _get_functionClasses_():
    init_properties_primitives_kt()
    return functionClasses

functionClasses = None
class _no_name_provided_:
    def __init__(self):
        pass
    
    def invoke(self, it):
        return isObject(it)
    
    def invoke(self, p1):
        return self.invoke((kotlin_Any_(p1)) if ((True) if (p1 == None) else (isObject(p1))) else (THROW_CCE()))
    

class _no_name_provided_:
    def __init__(self):
        pass
    
    def invoke(self, it):
        return isNumber(it)
    
    def invoke(self, p1):
        return self.invoke((kotlin_Any_(p1)) if ((True) if (p1 == None) else (isObject(p1))) else (THROW_CCE()))
    

class _no_name_provided_:
    def __init__(self):
        pass
    
    def invoke(self, it):
        return (jsTypeOf(it) == 'boolean') if (not (it == None)) else (False)
    
    def invoke(self, p1):
        return self.invoke((kotlin_Any_(p1)) if ((True) if (p1 == None) else (isObject(p1))) else (THROW_CCE()))
    

class _no_name_provided_:
    def __init__(self):
        pass
    
    def invoke(self, it):
        return (jsTypeOf(it) == 'number') if (not (it == None)) else (False)
    
    def invoke(self, p1):
        return self.invoke((kotlin_Any_(p1)) if ((True) if (p1 == None) else (isObject(p1))) else (THROW_CCE()))
    

class _no_name_provided_:
    def __init__(self):
        pass
    
    def invoke(self, it):
        return (jsTypeOf(it) == 'number') if (not (it == None)) else (False)
    
    def invoke(self, p1):
        return self.invoke((kotlin_Any_(p1)) if ((True) if (p1 == None) else (isObject(p1))) else (THROW_CCE()))
    

class _no_name_provided_:
    def __init__(self):
        pass
    
    def invoke(self, it):
        return (jsTypeOf(it) == 'number') if (not (it == None)) else (False)
    
    def invoke(self, p1):
        return self.invoke((kotlin_Any_(p1)) if ((True) if (p1 == None) else (isObject(p1))) else (THROW_CCE()))
    

class _no_name_provided_:
    def __init__(self):
        pass
    
    def invoke(self, it):
        return (jsTypeOf(it) == 'number') if (not (it == None)) else (False)
    
    def invoke(self, p1):
        return self.invoke((kotlin_Any_(p1)) if ((True) if (p1 == None) else (isObject(p1))) else (THROW_CCE()))
    

class _no_name_provided_:
    def __init__(self):
        pass
    
    def invoke(self, it):
        return (jsTypeOf(it) == 'number') if (not (it == None)) else (False)
    
    def invoke(self, p1):
        return self.invoke((kotlin_Any_(p1)) if ((True) if (p1 == None) else (isObject(p1))) else (THROW_CCE()))
    

class _no_name_provided_:
    def __init__(self):
        pass
    
    def invoke(self, it):
        return (isArray(it)) if (not (it == None)) else (False)
    
    def invoke(self, p1):
        return self.invoke((kotlin_Any_(p1)) if ((True) if (p1 == None) else (isObject(p1))) else (THROW_CCE()))
    

class _no_name_provided_:
    def __init__(self):
        pass
    
    def invoke(self, it):
        return (jsTypeOf(it) == 'string') if (not (it == None)) else (False)
    
    def invoke(self, p1):
        return self.invoke((kotlin_Any_(p1)) if ((True) if (p1 == None) else (isObject(p1))) else (THROW_CCE()))
    

class _no_name_provided_:
    def __init__(self):
        pass
    
    def invoke(self, it):
        return jsInstanceOf(it, jsClass())
    
    def invoke(self, p1):
        return self.invoke((kotlin_Any_(p1)) if ((True) if (p1 == None) else (isObject(p1))) else (THROW_CCE()))
    

class _no_name_provided_:
    def __init__(self):
        pass
    
    def invoke(self, it):
        return (isBooleanArray(it)) if (not (it == None)) else (False)
    
    def invoke(self, p1):
        return self.invoke((kotlin_Any_(p1)) if ((True) if (p1 == None) else (isObject(p1))) else (THROW_CCE()))
    

class _no_name_provided_:
    def __init__(self):
        pass
    
    def invoke(self, it):
        return (isCharArray(it)) if (not (it == None)) else (False)
    
    def invoke(self, p1):
        return self.invoke((kotlin_Any_(p1)) if ((True) if (p1 == None) else (isObject(p1))) else (THROW_CCE()))
    

class _no_name_provided_:
    def __init__(self):
        pass
    
    def invoke(self, it):
        return (isByteArray(it)) if (not (it == None)) else (False)
    
    def invoke(self, p1):
        return self.invoke((kotlin_Any_(p1)) if ((True) if (p1 == None) else (isObject(p1))) else (THROW_CCE()))
    

class _no_name_provided_:
    def __init__(self):
        pass
    
    def invoke(self, it):
        return (isShortArray(it)) if (not (it == None)) else (False)
    
    def invoke(self, p1):
        return self.invoke((kotlin_Any_(p1)) if ((True) if (p1 == None) else (isObject(p1))) else (THROW_CCE()))
    

class _no_name_provided_:
    def __init__(self):
        pass
    
    def invoke(self, it):
        return (isIntArray(it)) if (not (it == None)) else (False)
    
    def invoke(self, p1):
        return self.invoke((kotlin_Any_(p1)) if ((True) if (p1 == None) else (isObject(p1))) else (THROW_CCE()))
    

class _no_name_provided_:
    def __init__(self):
        pass
    
    def invoke(self, it):
        return (isLongArray(it)) if (not (it == None)) else (False)
    
    def invoke(self, p1):
        return self.invoke((kotlin_Any_(p1)) if ((True) if (p1 == None) else (isObject(p1))) else (THROW_CCE()))
    

class _no_name_provided_:
    def __init__(self):
        pass
    
    def invoke(self, it):
        return (isFloatArray(it)) if (not (it == None)) else (False)
    
    def invoke(self, p1):
        return self.invoke((kotlin_Any_(p1)) if ((True) if (p1 == None) else (isObject(p1))) else (THROW_CCE()))
    

class _no_name_provided_:
    def __init__(self):
        pass
    
    def invoke(self, it):
        return (isDoubleArray(it)) if (not (it == None)) else (False)
    
    def invoke(self, p1):
        return self.invoke((kotlin_Any_(p1)) if ((True) if (p1 == None) else (isObject(p1))) else (THROW_CCE()))
    

class _no_name_provided_:
    def __init__(self, _arity):
        self._arity = _arity
    
    def invoke(self, it):
        if jsTypeOf(it) is 'function':
            tmp = EQEQEQ(length(it), self._arity)
        else:
            tmp = False
        
        return tmp
    
    def invoke(self, p1):
        return self.invoke((kotlin_Any_(p1)) if ((True) if (p1 == None) else (isObject(p1))) else (THROW_CCE()))
    

class PrimitiveClasses:
    def __init__(self):
        PrimitiveClasses_instance = self
        tmp = self
        tmp0_unsafeCast_0 = js('Object')
        tmp.anyClass = PrimitiveKClassImpl(kotlin_Any_(tmp0_unsafeCast_0), 'Any', _no_name_provided__factory())
        tmp = self
        tmp0_unsafeCast_0 = js('Number')
        tmp.numberClass = PrimitiveKClassImpl(kotlin_Any_(tmp0_unsafeCast_0), 'Number', _no_name_provided__factory())
        self.nothingClass = NothingKClassImpl_getInstance()
        tmp = self
        tmp0_unsafeCast_0 = js('Boolean')
        tmp.booleanClass = PrimitiveKClassImpl(kotlin_Any_(tmp0_unsafeCast_0), 'Boolean', _no_name_provided__factory())
        tmp = self
        tmp0_unsafeCast_0 = js('Number')
        tmp.byteClass = PrimitiveKClassImpl(kotlin_Any_(tmp0_unsafeCast_0), 'Byte', _no_name_provided__factory())
        tmp = self
        tmp0_unsafeCast_0 = js('Number')
        tmp.shortClass = PrimitiveKClassImpl(kotlin_Any_(tmp0_unsafeCast_0), 'Short', _no_name_provided__factory())
        tmp = self
        tmp0_unsafeCast_0 = js('Number')
        tmp.intClass = PrimitiveKClassImpl(kotlin_Any_(tmp0_unsafeCast_0), 'Int', _no_name_provided__factory())
        tmp = self
        tmp0_unsafeCast_0 = js('Number')
        tmp.floatClass = PrimitiveKClassImpl(kotlin_Any_(tmp0_unsafeCast_0), 'Float', _no_name_provided__factory())
        tmp = self
        tmp0_unsafeCast_0 = js('Number')
        tmp.doubleClass = PrimitiveKClassImpl(kotlin_Any_(tmp0_unsafeCast_0), 'Double', _no_name_provided__factory())
        tmp = self
        tmp0_unsafeCast_0 = js('Array')
        tmp.arrayClass = PrimitiveKClassImpl(kotlin_Any_(tmp0_unsafeCast_0), 'Array', _no_name_provided__factory())
        tmp = self
        tmp0_unsafeCast_0 = js('String')
        tmp.stringClass = PrimitiveKClassImpl(kotlin_Any_(tmp0_unsafeCast_0), 'String', _no_name_provided__factory())
        tmp = self
        tmp0_unsafeCast_0 = js('Error')
        tmp.throwableClass = PrimitiveKClassImpl(kotlin_Any_(tmp0_unsafeCast_0), 'Throwable', _no_name_provided__factory())
        tmp = self
        tmp0_unsafeCast_0 = js('Array')
        tmp.booleanArrayClass = PrimitiveKClassImpl(kotlin_Any_(tmp0_unsafeCast_0), 'BooleanArray', _no_name_provided__factory())
        tmp = self
        tmp0_unsafeCast_0 = js('Uint16Array')
        tmp.charArrayClass = PrimitiveKClassImpl(kotlin_Any_(tmp0_unsafeCast_0), 'CharArray', _no_name_provided__factory())
        tmp = self
        tmp0_unsafeCast_0 = js('Int8Array')
        tmp.byteArrayClass = PrimitiveKClassImpl(kotlin_Any_(tmp0_unsafeCast_0), 'ByteArray', _no_name_provided__factory())
        tmp = self
        tmp0_unsafeCast_0 = js('Int16Array')
        tmp.shortArrayClass = PrimitiveKClassImpl(kotlin_Any_(tmp0_unsafeCast_0), 'ShortArray', _no_name_provided__factory())
        tmp = self
        tmp0_unsafeCast_0 = js('Int32Array')
        tmp.intArrayClass = PrimitiveKClassImpl(kotlin_Any_(tmp0_unsafeCast_0), 'IntArray', _no_name_provided__factory())
        tmp = self
        tmp0_unsafeCast_0 = js('Array')
        tmp.longArrayClass = PrimitiveKClassImpl(kotlin_Any_(tmp0_unsafeCast_0), 'LongArray', _no_name_provided__factory())
        tmp = self
        tmp0_unsafeCast_0 = js('Float32Array')
        tmp.floatArrayClass = PrimitiveKClassImpl(kotlin_Any_(tmp0_unsafeCast_0), 'FloatArray', _no_name_provided__factory())
        tmp = self
        tmp0_unsafeCast_0 = js('Float64Array')
        tmp.doubleArrayClass = PrimitiveKClassImpl(kotlin_Any_(tmp0_unsafeCast_0), 'DoubleArray', _no_name_provided__factory())
    
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
        tmp0_elvis_lhs = _get_functionClasses_()[arity]
        if tmp0_elvis_lhs == None:
            tmp0_unsafeCast_0_3 = js('Function')
            tmp = str('Function') + str(arity)
            result_2 = PrimitiveKClassImpl(kotlin_Any_(tmp0_unsafeCast_0_3), tmp, _no_name_provided__factory(arity))
            tmp1_asDynamic_0_5 = _get_functionClasses_()
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
            tmp = result_2
        else:
            tmp = tmp0_elvis_lhs
        
        return tmp
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

pass
def PrimitiveClasses_getInstance():
    if PrimitiveClasses_instance == None:
        PrimitiveClasses()
    
    return PrimitiveClasses_instance

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl

def _no_name_provided__factory(_arity):
    i = _no_name_provided_(_arity)
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl

properties_initialized_primitives_kt = False
def init_properties_primitives_kt():
    global properties_initialized_primitives_kt
    if not properties_initialized_primitives_kt:
        properties_initialized_primitives_kt = True
        global functionClasses
        functionClasses = fillArrayVal(Array(0), None)
    

def getKClass(jClass):
    if kotlin_Boolean(INVOKE(isArray(js('Array')), jClass)):
        tmp = getKClassM(kotlin_Any_(jClass))
    else:
        tmp = getKClass1(kotlin_Any_(jClass))
    
    return tmp

def getKClassM(jClasses):
    tmp0_subject = len(jClasses)
    if tmp0_subject == 1:
        tmp = getKClass1(jClasses[0])
    elif tmp0_subject == 0:
        tmp0_unsafeCast_0 = NothingKClassImpl_getInstance()
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
    else:
        tmp1_unsafeCast_0 = ErrorKClass()
        tmp = kotlin_Any_(tmp1_unsafeCast_0)
    
    return tmp

def getKClass1(jClass):
    if jClass is js('String'):
        tmp0_unsafeCast_0 = PrimitiveClasses_getInstance().stringClass
        return kotlin_Any_(tmp0_unsafeCast_0)
    
    metadata = _metadata_(jClass)
    if EXCLEQ(metadata, None):
        if EQEQ(_kClass_(metadata), None):
            kClass = SimpleKClassImpl(jClass)
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
            tmp = kClass
        else:
            tmp = _kClass_(metadata)
        
        tmp = kotlin_reflect_KClass_T_(tmp)
    else:
        tmp = SimpleKClassImpl(jClass)
    
    return tmp

def getKClassFromExpression(e):
    tmp0_subject = jsTypeOf(e)
    if tmp0_subject == 'string':
        tmp = PrimitiveClasses_getInstance().stringClass
    elif tmp0_subject == 'number':
        tmp0_asDynamic_0 = jsBitwiseOr(e, 0)
        if EQEQEQ(tmp0_asDynamic_0, e):
            tmp = PrimitiveClasses_getInstance().intClass
        elif True:
            tmp = PrimitiveClasses_getInstance().doubleClass
        
        tmp = tmp
    elif tmp0_subject == 'boolean':
        tmp = PrimitiveClasses_getInstance().booleanClass
    elif tmp0_subject == 'function':
        tmp = PrimitiveClasses_getInstance()
        tmp = tmp.functionClass(kotlin_Int(length(e)))
    else:
        if isBooleanArray(e):
            tmp = PrimitiveClasses_getInstance().booleanArrayClass
        elif isCharArray(e):
            tmp = PrimitiveClasses_getInstance().charArrayClass
        elif isByteArray(e):
            tmp = PrimitiveClasses_getInstance().byteArrayClass
        elif isShortArray(e):
            tmp = PrimitiveClasses_getInstance().shortArrayClass
        elif isIntArray(e):
            tmp = PrimitiveClasses_getInstance().intArrayClass
        elif isLongArray(e):
            tmp = PrimitiveClasses_getInstance().longArrayClass
        elif isFloatArray(e):
            tmp = PrimitiveClasses_getInstance().floatArrayClass
        elif isDoubleArray(e):
            tmp = PrimitiveClasses_getInstance().doubleArrayClass
        elif isInterface(e, jsClass()):
            tmp = getKClass(jsClass())
        elif isArray(e):
            tmp = PrimitiveClasses_getInstance().arrayClass
        elif True:
            constructor = constructor(INVOKE(getPrototypeOf(js('Object')), e))
            if EQEQEQ(constructor, js('Object')):
                tmp = PrimitiveClasses_getInstance().anyClass
            elif EQEQEQ(constructor, js('Error')):
                tmp = PrimitiveClasses_getInstance().throwableClass
            else:
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
    super(toString(content))
    return _this

def StringBuilder_init__Create_(content):
    return StringBuilder_init__Init_(content, Object_create())

def StringBuilder_init__Init_(_this):
    super('')
    return _this

def StringBuilder_init__Create_():
    return StringBuilder_init__Init_(Object_create())

def _set_string_(_this, _set___):
    _this.string = _set___

def _get_string_(_this):
    return _this.string

def checkReplaceRange(_this, startIndex, endIndex, length):
    if (True) if (startIndex < 0) else (startIndex > length):
        raise IndexOutOfBoundsException_init__Create_(((str('startIndex: ') + str(startIndex)) + str(', length: ')) + str(length))
    
    if startIndex > endIndex:
        raise IllegalArgumentException_init__Create_((((str('startIndex(') + str(startIndex)) + str(') > endIndex(')) + str(endIndex)) + str(')'))
    

class StringBuilder:
    def __init__(self, content):
        self.string = (content) if (not (content is _get_undefined_())) else ('')
    
    def _get_length_(self):
        tmp0_asDynamic_0 = self.string
        return kotlin_Int(length(tmp0_asDynamic_0))
    
    def get(self, index):
        tmp0_getOrElse_0 = self.string
        if (index <= _get_lastIndex_()) if (index >= 0) else (False):
            tmp = charSequenceGet(tmp0_getOrElse_0, index)
        else:
            raise IndexOutOfBoundsException_init__Create_((((str('index: ') + str(index)) + str(', length: ')) + str(self._get_length_())) + str('}'))
        
        return tmp
    
    def subSequence(self, startIndex, endIndex):
        tmp0_substring_0 = self.string
        return kotlin_String(INVOKE(substring(tmp0_substring_0), startIndex, endIndex))
    
    def append(self, value):
        tmp0_this = self
        tmp0_this.string = tmp0_this.string + value
        return self
    
    def append(self, value):
        tmp0_this = self
        tmp0_this.string = tmp0_this.string + toString()
        return self
    
    def append(self, value, startIndex, endIndex):
        tmp0_elvis_lhs = value
        return self.appendRange(('null') if (tmp0_elvis_lhs == None) else (tmp0_elvis_lhs), startIndex, endIndex)
    
    def reverse(self):
        reversed = ''
        index = (len(self.string) - 1) | 0
        while index >= 0:
            tmp = self.string
            tmp0 = index
            index = (tmp0 - 1) | 0
            low = charSequenceGet(tmp, tmp0)
            if (index >= 0) if (isLowSurrogate()) else (False):
                tmp = self.string
                tmp1 = index
                index = (tmp1 - 1) | 0
                high = charSequenceGet(tmp, tmp1)
                if isHighSurrogate():
                    reversed = (reversed + high) + low
                else:
                    reversed = (reversed + low) + high
                
            else:
                reversed = reversed + low
            
        
        self.string = reversed
        return self
    
    def append(self, value):
        tmp0_this = self
        tmp0_this.string = tmp0_this.string + toString()
        return self
    
    def append(self, value):
        tmp0_this = self
        tmp0_this.string = tmp0_this.string + value
        return self
    
    def append(self, value):
        tmp0_this = self
        tmp0_this.string = tmp0_this.string + concatToString()
        return self
    
    def append(self, value):
        return self.append(value)
    
    def append(self, value):
        tmp0_this = self
        tmp = tmp0_this
        tmp = tmp0_this.string
        tmp1_elvis_lhs = value
        tmp.string = tmp + (('null') if (tmp1_elvis_lhs == None) else (tmp1_elvis_lhs))
        return self
    
    def capacity(self):
        return self._get_length_()
    
    def ensureCapacity(self, minimumCapacity):
        pass
    
    def indexOf(self, string):
        tmp0_asDynamic_0 = self.string
        return kotlin_Int(INVOKE(indexOf(tmp0_asDynamic_0), string))
    
    def indexOf(self, string, startIndex):
        tmp0_asDynamic_0 = self.string
        return kotlin_Int(INVOKE(indexOf(tmp0_asDynamic_0), string, startIndex))
    
    def lastIndexOf(self, string):
        tmp0_asDynamic_0 = self.string
        return kotlin_Int(INVOKE(lastIndexOf(tmp0_asDynamic_0), string))
    
    def lastIndexOf(self, string, startIndex):
        if charSequenceLength(string) == 0:
            tmp = startIndex < 0
        elif True:
            tmp = False
        
        if tmp:
            return -1
        
        tmp0_asDynamic_0 = self.string
        return kotlin_Int(INVOKE(lastIndexOf(tmp0_asDynamic_0), string, startIndex))
    
    def insert(self, index, value):
        Companion_getInstance().checkPositionIndex(index, self._get_length_())
        tmp = self
        tmp0_substring_0 = self.string
        tmp = kotlin_String(INVOKE(substring(tmp0_substring_0), 0, index)) + value
        tmp1_substring_0 = self.string
        tmp.string = tmp + kotlin_String(INVOKE(substring(tmp1_substring_0), index))
        return self
    
    def insert(self, index, value):
        Companion_getInstance().checkPositionIndex(index, self._get_length_())
        tmp = self
        tmp0_substring_0 = self.string
        tmp = kotlin_String(INVOKE(substring(tmp0_substring_0), 0, index)) + value
        tmp1_substring_0 = self.string
        tmp.string = tmp + kotlin_String(INVOKE(substring(tmp1_substring_0), index))
        return self
    
    def insert(self, index, value):
        Companion_getInstance().checkPositionIndex(index, self._get_length_())
        tmp = self
        tmp0_substring_0 = self.string
        tmp = kotlin_String(INVOKE(substring(tmp0_substring_0), 0, index)) + concatToString()
        tmp1_substring_0 = self.string
        tmp.string = tmp + kotlin_String(INVOKE(substring(tmp1_substring_0), index))
        return self
    
    def insert(self, index, value):
        Companion_getInstance().checkPositionIndex(index, self._get_length_())
        tmp = self
        tmp0_substring_0 = self.string
        tmp = kotlin_String(INVOKE(substring(tmp0_substring_0), 0, index)) + toString()
        tmp1_substring_0 = self.string
        tmp.string = tmp + kotlin_String(INVOKE(substring(tmp1_substring_0), index))
        return self
    
    def insert(self, index, value):
        Companion_getInstance().checkPositionIndex(index, self._get_length_())
        tmp = self
        tmp0_substring_0 = self.string
        tmp = kotlin_String(INVOKE(substring(tmp0_substring_0), 0, index)) + toString()
        tmp1_substring_0 = self.string
        tmp.string = tmp + kotlin_String(INVOKE(substring(tmp1_substring_0), index))
        return self
    
    def insert(self, index, value):
        return self.insert(index, value)
    
    def insert(self, index, value):
        Companion_getInstance().checkPositionIndex(index, self._get_length_())
        tmp0_elvis_lhs = value
        toInsert = ('null') if (tmp0_elvis_lhs == None) else (tmp0_elvis_lhs)
        tmp = self
        tmp0_substring_0 = self.string
        tmp = kotlin_String(INVOKE(substring(tmp0_substring_0), 0, index)) + toInsert
        tmp1_substring_0 = self.string
        tmp.string = tmp + kotlin_String(INVOKE(substring(tmp1_substring_0), index))
        return self
    
    def setLength(self, newLength):
        if newLength < 0:
            raise IllegalArgumentException_init__Create_((str('Negative new length: ') + str(newLength)) + str('.'))
        
        if newLength <= self._get_length_():
            tmp = self
            tmp0_substring_0 = self.string
            tmp.string = kotlin_String(INVOKE(substring(tmp0_substring_0), 0, newLength))
        else:
            inductionVariable = self._get_length_()
            if inductionVariable < newLength:
                while True:
                    i = inductionVariable
                    inductionVariable = (inductionVariable + 1) | 0
                    tmp1_this = self
                    tmp1_this.string = tmp1_this.string + Char(0)
                    if inductionVariable < newLength:
                        break
                    
                
            
        
    
    def substring(self, startIndex):
        Companion_getInstance().checkPositionIndex(startIndex, self._get_length_())
        tmp0_substring_0 = self.string
        return kotlin_String(INVOKE(substring(tmp0_substring_0), startIndex))
    
    def substring(self, startIndex, endIndex):
        Companion_getInstance().checkBoundsIndexes(startIndex, endIndex, self._get_length_())
        tmp0_substring_0 = self.string
        return kotlin_String(INVOKE(substring(tmp0_substring_0), startIndex, endIndex))
    
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
        tmp = kotlin_String(INVOKE(substring(tmp0_substring_0), 0, index)) + value
        tmp1_substring_0 = self.string
        tmp2_substring_0 = (index + 1) | 0
        tmp.string = tmp + kotlin_String(INVOKE(substring(tmp1_substring_0), tmp2_substring_0))
    
    def setRange(self, startIndex, endIndex, value):
        checkReplaceRange(self, startIndex, endIndex, self._get_length_())
        tmp = self
        tmp0_substring_0 = self.string
        tmp = kotlin_String(INVOKE(substring(tmp0_substring_0), 0, startIndex)) + value
        tmp1_substring_0 = self.string
        tmp.string = tmp + kotlin_String(INVOKE(substring(tmp1_substring_0), endIndex))
        return self
    
    def deleteAt(self, index):
        Companion_getInstance().checkElementIndex(index, self._get_length_())
        tmp = self
        tmp0_substring_0 = self.string
        tmp = kotlin_String(INVOKE(substring(tmp0_substring_0), 0, index))
        tmp1_substring_0 = self.string
        tmp2_substring_0 = (index + 1) | 0
        tmp.string = tmp + kotlin_String(INVOKE(substring(tmp1_substring_0), tmp2_substring_0))
        return self
    
    def deleteRange(self, startIndex, endIndex):
        checkReplaceRange(self, startIndex, endIndex, self._get_length_())
        tmp = self
        tmp0_substring_0 = self.string
        tmp = kotlin_String(INVOKE(substring(tmp0_substring_0), 0, startIndex))
        tmp1_substring_0 = self.string
        tmp.string = tmp + kotlin_String(INVOKE(substring(tmp1_substring_0), endIndex))
        return self
    
    def toCharArray(self, destination, destinationOffset, startIndex, endIndex):
        Companion_getInstance().checkBoundsIndexes(startIndex, endIndex, self._get_length_())
        Companion_getInstance().checkBoundsIndexes(destinationOffset, (((destinationOffset + endIndex) | 0) - startIndex) | 0, len(destination))
        dstIndex = destinationOffset
        inductionVariable = startIndex
        if inductionVariable < endIndex:
            while True:
                index = inductionVariable
                inductionVariable = (inductionVariable + 1) | 0
                tmp1 = dstIndex
                dstIndex = (tmp1 + 1) | 0
                destination.__setitem__(tmp1, charSequenceGet(self.string, index))
                if inductionVariable < endIndex:
                    break
                
            
        
    
    def toCharArray_default(self, destination, destinationOffset, startIndex, endIndex, _mask0, _handler):
        if not (_mask0 & 2 == 0):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
        
        if not (_mask0 & 4 == 0):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
        
        if not (_mask0 & 8 == 0):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
        
        return self.toCharArray(destination, destinationOffset, startIndex, endIndex)
    
    def appendRange(self, value, startIndex, endIndex):
        tmp0_this = self
        tmp0_this.string = tmp0_this.string + concatToString(startIndex, endIndex)
        return self
    
    def appendRange(self, value, startIndex, endIndex):
        stringCsq = toString(value)
        Companion_getInstance().checkBoundsIndexes(startIndex, endIndex, len(stringCsq))
        tmp0_this = self
        tmp = tmp0_this
        tmp = tmp0_this.string
        tmp.string = tmp + kotlin_String(INVOKE(substring(stringCsq), startIndex, endIndex))
        return self
    
    def insertRange(self, index, value, startIndex, endIndex):
        Companion_getInstance().checkPositionIndex(index, self._get_length_())
        tmp = self
        tmp0_substring_0 = self.string
        tmp = kotlin_String(INVOKE(substring(tmp0_substring_0), 0, index)) + concatToString(startIndex, endIndex)
        tmp1_substring_0 = self.string
        tmp.string = tmp + kotlin_String(INVOKE(substring(tmp1_substring_0), index))
        return self
    
    def insertRange(self, index, value, startIndex, endIndex):
        Companion_getInstance().checkPositionIndex(index, self._get_length_())
        stringCsq = toString(value)
        Companion_getInstance().checkBoundsIndexes(startIndex, endIndex, len(stringCsq))
        tmp = self
        tmp0_substring_0 = self.string
        tmp = kotlin_String(INVOKE(substring(tmp0_substring_0), 0, index))
        tmp = tmp + kotlin_String(INVOKE(substring(stringCsq), startIndex, endIndex))
        tmp1_substring_0 = self.string
        tmp.string = tmp + kotlin_String(INVOKE(substring(tmp1_substring_0), index))
        return self
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    

def isLowSurrogate():
    Companion_getInstance()
    containsLower = Char(56320)
    Companion_getInstance()
    if self <= Char(57343):
        tmp = containsLower <= self
    elif True:
        tmp = False
    
    return tmp

def isHighSurrogate():
    Companion_getInstance()
    containsLower = Char(55296)
    Companion_getInstance()
    if self <= Char(56319):
        tmp = containsLower <= self
    elif True:
        tmp = False
    
    return tmp

def checkRadix(radix):
    if not ((radix <= 36) if (2 <= radix) else (False)):
        raise IllegalArgumentException_init__Create_((str('radix ') + str(radix)) + str(' was not in valid range 2..36'))
    
    return radix

def _get_STRING_CASE_INSENSITIVE_ORDER_():
    init_properties_string_kt()
    return STRING_CASE_INSENSITIVE_ORDER

STRING_CASE_INSENSITIVE_ORDER = None
def nativeLastIndexOf(str, fromIndex):
    init_properties_string_kt()
    return kotlin_Int(INVOKE(lastIndexOf(self), str, fromIndex))

def substring(startIndex, endIndex):
    init_properties_string_kt()
    return kotlin_String(INVOKE(substring(self), startIndex, endIndex))

def substring(startIndex):
    init_properties_string_kt()
    return kotlin_String(INVOKE(substring(self), startIndex))

def compareTo(other, ignoreCase):
    init_properties_string_kt()
    if ignoreCase:
        n1 = len(self)
        n2 = len(other)
        min = visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl.min(n1, n2)
        if min == 0:
            return (n1 - n2) | 0
        
        start = 0
        while True:
            tmp0_minOf_0 = (start + 16) | 0
            end = visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl.min(tmp0_minOf_0, min)
            tmp1_substring_0 = start
            s1 = kotlin_String(INVOKE(substring(self), tmp1_substring_0, end))
            tmp2_substring_0 = start
            s2 = kotlin_String(INVOKE(substring(other), tmp2_substring_0, end))
            if not (s1 == s2):
                tmp3_uppercase_0 = s1
                s1 = kotlin_String(INVOKE(toUpperCase(tmp3_uppercase_0)))
                tmp4_uppercase_0 = s2
                s2 = kotlin_String(INVOKE(toUpperCase(tmp4_uppercase_0)))
                if not (s1 == s2):
                    tmp5_lowercase_0 = s1
                    s1 = kotlin_String(INVOKE(toLowerCase(tmp5_lowercase_0)))
                    tmp6_lowercase_0 = s2
                    s2 = kotlin_String(INVOKE(toLowerCase(tmp6_lowercase_0)))
                    if not (s1 == s2):
                        return compareTo(s1, s2)
                    
                
            
            if end == min:
                break
            
            start = end
        
        return (n1 - n2) | 0
    else:
        return compareTo(self, other)
    

def compareTo_default(other, ignoreCase, _mask0, _handler):
    if not (_mask0 & 2 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    return compareTo(other, ignoreCase)

def uppercase():
    init_properties_string_kt()
    return kotlin_String(INVOKE(toUpperCase(self)))

def lowercase():
    init_properties_string_kt()
    return kotlin_String(INVOKE(toLowerCase(self)))

def concatToString():
    init_properties_string_kt()
    result = ''
    indexedObject = self
    inductionVariable = 0
    last = len(indexedObject)
    while inductionVariable < last:
        char = indexedObject[inductionVariable]
        inductionVariable = (inductionVariable + 1) | 0
        result = result + char
    
    return result

def concatToString(startIndex, endIndex):
    init_properties_string_kt()
    Companion_getInstance().checkBoundsIndexes(startIndex, endIndex, len(self))
    result = ''
    inductionVariable = startIndex
    if inductionVariable < endIndex:
        while True:
            index = inductionVariable
            inductionVariable = (inductionVariable + 1) | 0
            result = result + self[index]
            if inductionVariable < endIndex:
                break
            
        
    
    return result

def concatToString_default(startIndex, endIndex, _mask0, _handler):
    if not (_mask0 & 1 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    if not (_mask0 & 2 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
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
        tmp = (kotlin_String(p1)) if ((jsTypeOf(p1) == 'string') if (not (p1 == None)) else (False)) else (THROW_CCE())
        return self.invoke(tmp, (kotlin_String(p2)) if ((jsTypeOf(p2) == 'string') if (not (p2 == None)) else (False)) else (THROW_CCE()))
    

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl

properties_initialized_string_kt = False
def init_properties_string_kt():
    global properties_initialized_string_kt
    if not properties_initialized_string_kt:
        properties_initialized_string_kt = True
        global STRING_CASE_INSENSITIVE_ORDER
        tmp = _no_name_provided__factory()
        STRING_CASE_INSENSITIVE_ORDER = sam_kotlin_Comparator_0(tmp)
    

def _get_REPLACEMENT_BYTE_SEQUENCE_():
    init_properties_utf8Encoding_kt()
    return REPLACEMENT_BYTE_SEQUENCE

REPLACEMENT_BYTE_SEQUENCE = None
properties_initialized_utf8Encoding_kt = False
def init_properties_utf8Encoding_kt():
    global properties_initialized_utf8Encoding_kt
    if not properties_initialized_utf8Encoding_kt:
        properties_initialized_utf8Encoding_kt = True
        global REPLACEMENT_BYTE_SEQUENCE
        tmp0_byteArrayOf_0 = -17
        REPLACEMENT_BYTE_SEQUENCE = tmp0_byteArrayOf_0
    

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
    

pass
def Companion_getInstance():
    if Companion_instance == None:
        Companion()
    
    return Companion_instance

class Char:
    def __init__(self, code):
        Companion_getInstance()
        tmp = self
        tmp.value = kotlin_Int(_UShort___get_data__impl_(code)) & 65535
    
    def compareTo(self, other):
        return (self.value - other.value) | 0
    
    def compareTo(self, other):
        return self.compareTo((kotlin_Char(other)) if (jsInstanceOf(other, jsClass())) else (THROW_CCE()))
    
    def plus(self, other):
        return numberToChar((self.value + other) | 0)
    
    def minus(self, other):
        return (self.value - other.value) | 0
    
    def minus(self, other):
        return numberToChar((self.value - other) | 0)
    
    def inc(self):
        return numberToChar((self.value + 1) | 0)
    
    def dec(self):
        return numberToChar((self.value - 1) | 0)
    
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
        if other is self:
            return True
        
        if not jsInstanceOf(other, jsClass()):
            return False
        
        return self.value == kotlin_Char(other).value
    
    def hashCode(self):
        return self.value
    
    def toString(self):
        tmp0_unsafeCast_0 = INVOKE(fromCharCode(js('String')), self.value)
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
    

pass
def Companion_getInstance():
    if Companion_instance == None:
        Companion()
    
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
        return self.compareTo((E(other)) if (jsInstanceOf(other, jsClass())) else (THROW_CCE()))
    
    def equals(self, other):
        return self is other
    
    def hashCode(self):
        return identityHashCode(self)
    
    def toString(self):
        return self.name
    

def byteArrayOf(*elements):
    return elements

def arrayOf(*elements):
    return kotlin_Any_(elements)

def plus(other):
    tmp2_safe_receiver = self
    tmp3_elvis_lhs = (None) if (tmp2_safe_receiver == None) else (toString(tmp2_safe_receiver))
    tmp = ('null') if (tmp3_elvis_lhs == None) else (tmp3_elvis_lhs)
    tmp0_safe_receiver = other
    tmp1_elvis_lhs = (None) if (tmp0_safe_receiver == None) else (toString(tmp0_safe_receiver))
    return tmp + (('null') if (tmp1_elvis_lhs == None) else (tmp1_elvis_lhs))

def toString():
    tmp0_safe_receiver = self
    tmp1_elvis_lhs = (None) if (tmp0_safe_receiver == None) else (toString(tmp0_safe_receiver))
    return ('null') if (tmp1_elvis_lhs == None) else (tmp1_elvis_lhs)

def booleanArrayOf(*elements):
    return elements

def charArrayOf(*elements):
    return elements

def shortArrayOf(*elements):
    return elements

def intArrayOf(*elements):
    return elements

def floatArrayOf(*elements):
    return elements

def longArrayOf(*elements):
    return elements

def doubleArrayOf(*elements):
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
    

pass
def DefaultConstructorMarker_getInstance():
    if DefaultConstructorMarker_instance == None:
        DefaultConstructorMarker()
    
    return DefaultConstructorMarker_instance

def fillArrayVal(array, initValue):
    inductionVariable = 0
    last = (len(array) - 1) | 0
    if inductionVariable <= last:
        while True:
            i = inductionVariable
            inductionVariable = (inductionVariable + 1) | 0
            array.__setitem__(i, initValue)
            if not (i == last):
                break
            
        
    
    return array

def arrayWithFun(size, init):
    tmp0_fillArrayFun_0 = Array(size)
    result_1 = kotlin_Any_(tmp0_fillArrayFun_0)
    i_2 = 0
    while not (i_2 == len(result_1)):
        result_1.__setitem__(i_2, init.invoke(i_2))
        i_2 = (i_2 + 1) | 0
        Unit_getInstance()
    
    return result_1

def fillArrayFun(array, init):
    result = kotlin_Any_(array)
    i = 0
    while not (i == len(result)):
        result.__setitem__(i, init.invoke(i))
        i = (i + 1) | 0
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
    tmp0_withType_0 = fillArrayVal(Array(size), False)
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    tmp1_unsafeCast_0 = tmp0_withType_0
    return kotlin_Any_(tmp1_unsafeCast_0)

def charArray(size):
    tmp = Array(size)
    Companion_getInstance()
    tmp0__get_code__0_1 = Char(0)
    if 0 < tmp0__get_code__0_1.toInt():
        tmp = True
    elif True:
        Companion_getInstance()
        tmp1__get_code__0_2 = Char(65535)
        tmp = 0 > tmp1__get_code__0_2.toInt()
    
    if tmp:
        raise IllegalArgumentException_init__Create_('Invalid Char code: 0')
    
    tmp0_withType_0 = fillArrayVal(tmp, Char(0))
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    tmp1_unsafeCast_0 = tmp0_withType_0
    return kotlin_Any_(tmp1_unsafeCast_0)

def longArray(size):
    tmp0_withType_0 = fillArrayVal(Array(size), Long(0, 0))
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    tmp1_unsafeCast_0 = tmp0_withType_0
    return kotlin_Any_(tmp1_unsafeCast_0)

def booleanArrayOf(arr):
    tmp0_withType_0 = INVOKE(slice(arr))
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    tmp1_unsafeCast_0 = tmp0_withType_0
    return kotlin_Any_(tmp1_unsafeCast_0)

def charArrayOf(arr):
    tmp0_withType_0 = INVOKE(slice(arr))
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    tmp1_unsafeCast_0 = tmp0_withType_0
    return kotlin_Any_(tmp1_unsafeCast_0)

def longArrayOf(arr):
    tmp0_withType_0 = INVOKE(slice(arr))
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    tmp1_unsafeCast_0 = tmp0_withType_0
    return kotlin_Any_(tmp1_unsafeCast_0)

class _no_name_provided_:
    def __init__(self, _array):
        self._array = _array
        self.index = 0
    
    def _set_index_(self, _set___):
        self.index = _set___
    
    def _get_index_(self):
        return self.index
    
    def hasNext(self):
        return not (self.index == len(self._array))
    
    def next(self):
        if not (self.index == len(self._array)):
            tmp0_this = self
            tmp1 = tmp0_this.index
            tmp0_this.index = (tmp1 + 1) | 0
            tmp = self._array[tmp1]
        else:
            raise NoSuchElementException_init__Create_(str(self.index))
        
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
        super()
        self.index = 0
    
    def _set_index_(self, _set___):
        self.index = _set___
    
    def _get_index_(self):
        return self.index
    
    def hasNext(self):
        return not (self.index == len(self._array))
    
    def nextBoolean(self):
        if not (self.index == len(self._array)):
            tmp0_this = self
            tmp1 = tmp0_this.index
            tmp0_this.index = (tmp1 + 1) | 0
            tmp = self._array[tmp1]
        else:
            raise NoSuchElementException_init__Create_(str(self.index))
        
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
        super()
        self.index = 0
    
    def _set_index_(self, _set___):
        self.index = _set___
    
    def _get_index_(self):
        return self.index
    
    def hasNext(self):
        return not (self.index == len(self._array))
    
    def nextChar(self):
        if not (self.index == len(self._array)):
            tmp0_this = self
            tmp1 = tmp0_this.index
            tmp0_this.index = (tmp1 + 1) | 0
            tmp = self._array[tmp1]
        else:
            raise NoSuchElementException_init__Create_(str(self.index))
        
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
        super()
        self.index = 0
    
    def _set_index_(self, _set___):
        self.index = _set___
    
    def _get_index_(self):
        return self.index
    
    def hasNext(self):
        return not (self.index == len(self._array))
    
    def nextByte(self):
        if not (self.index == len(self._array)):
            tmp0_this = self
            tmp1 = tmp0_this.index
            tmp0_this.index = (tmp1 + 1) | 0
            tmp = self._array[tmp1]
        else:
            raise NoSuchElementException_init__Create_(str(self.index))
        
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
        super()
        self.index = 0
    
    def _set_index_(self, _set___):
        self.index = _set___
    
    def _get_index_(self):
        return self.index
    
    def hasNext(self):
        return not (self.index == len(self._array))
    
    def nextShort(self):
        if not (self.index == len(self._array)):
            tmp0_this = self
            tmp1 = tmp0_this.index
            tmp0_this.index = (tmp1 + 1) | 0
            tmp = self._array[tmp1]
        else:
            raise NoSuchElementException_init__Create_(str(self.index))
        
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
        super()
        self.index = 0
    
    def _set_index_(self, _set___):
        self.index = _set___
    
    def _get_index_(self):
        return self.index
    
    def hasNext(self):
        return not (self.index == len(self._array))
    
    def nextInt(self):
        if not (self.index == len(self._array)):
            tmp0_this = self
            tmp1 = tmp0_this.index
            tmp0_this.index = (tmp1 + 1) | 0
            tmp = self._array[tmp1]
        else:
            raise NoSuchElementException_init__Create_(str(self.index))
        
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
        super()
        self.index = 0
    
    def _set_index_(self, _set___):
        self.index = _set___
    
    def _get_index_(self):
        return self.index
    
    def hasNext(self):
        return not (self.index == len(self._array))
    
    def nextFloat(self):
        if not (self.index == len(self._array)):
            tmp0_this = self
            tmp1 = tmp0_this.index
            tmp0_this.index = (tmp1 + 1) | 0
            tmp = self._array[tmp1]
        else:
            raise NoSuchElementException_init__Create_(str(self.index))
        
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
        super()
        self.index = 0
    
    def _set_index_(self, _set___):
        self.index = _set___
    
    def _get_index_(self):
        return self.index
    
    def hasNext(self):
        return not (self.index == len(self._array))
    
    def nextLong(self):
        if not (self.index == len(self._array)):
            tmp0_this = self
            tmp1 = tmp0_this.index
            tmp0_this.index = (tmp1 + 1) | 0
            tmp = self._array[tmp1]
        else:
            raise NoSuchElementException_init__Create_(str(self.index))
        
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
        super()
        self.index = 0
    
    def _set_index_(self, _set___):
        self.index = _set___
    
    def _get_index_(self):
        return self.index
    
    def hasNext(self):
        return not (self.index == len(self._array))
    
    def nextDouble(self):
        if not (self.index == len(self._array)):
            tmp0_this = self
            tmp1 = tmp0_this.index
            tmp0_this.index = (tmp1 + 1) | 0
            tmp = self._array[tmp1]
        else:
            raise NoSuchElementException_init__Create_(str(self.index))
        
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
    init_properties_bitUtils_kt()
    return buf

buf = None
def _get_bufFloat64_():
    init_properties_bitUtils_kt()
    return bufFloat64

bufFloat64 = None
def _get_bufFloat32_():
    init_properties_bitUtils_kt()
    return bufFloat32

bufFloat32 = None
def _get_bufInt32_():
    init_properties_bitUtils_kt()
    return bufInt32

bufInt32 = None
def _get_lowIndex_():
    init_properties_bitUtils_kt()
    return lowIndex

lowIndex = None
def _get_highIndex_():
    init_properties_bitUtils_kt()
    return highIndex

highIndex = None
def getNumberHashCode(obj):
    init_properties_bitUtils_kt()
    tmp0_unsafeCast_0 = jsBitwiseOr(obj, 0)
    if kotlin_Any_(tmp0_unsafeCast_0) is obj:
        return numberToInt(obj)
    
    _get_bufFloat64_().__setitem__(0, obj)
    return (imul(_get_bufInt32_()[_get_highIndex_()], 31) + _get_bufInt32_()[_get_lowIndex_()]) | 0

properties_initialized_bitUtils_kt = False
def init_properties_bitUtils_kt():
    global properties_initialized_bitUtils_kt
    if not properties_initialized_bitUtils_kt:
        properties_initialized_bitUtils_kt = True
        global buf
        buf = ArrayBuffer(8)
        global bufFloat64
        tmp0_unsafeCast_0 = Float64Array(_get_buf_())
        bufFloat64 = kotlin_Any_(tmp0_unsafeCast_0)
        global bufFloat32
        tmp0_unsafeCast_0 = Float32Array(_get_buf_())
        bufFloat32 = kotlin_Any_(tmp0_unsafeCast_0)
        global bufInt32
        tmp0_unsafeCast_0 = Int32Array(_get_buf_())
        bufInt32 = kotlin_Any_(tmp0_unsafeCast_0)
        global lowIndex
        _get_bufFloat64_().__setitem__(0, -1.0)
        lowIndex = (1) if (not (_get_bufInt32_()[0] == 0)) else (0)
        global highIndex
        highIndex = (1 - _get_lowIndex_()) | 0
    

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
    if isString(a):
        tmp0_unsafeCast_0 = INVOKE(charCodeAt(a), index)
        tmp1_Char_0 = kotlin_Any_(tmp0_unsafeCast_0)
        Companion_getInstance()
        tmp0__get_code__0_1 = Char(0)
        if tmp1_Char_0 < tmp0__get_code__0_1.toInt():
            tmp = True
        elif True:
            Companion_getInstance()
            tmp1__get_code__0_2 = Char(65535)
            tmp = tmp1_Char_0 > tmp1__get_code__0_2.toInt()
        
        if tmp:
            raise IllegalArgumentException_init__Create_(str('Invalid Char code: ') + str(tmp1_Char_0))
        
        tmp = numberToChar(tmp1_Char_0)
    else:
        tmp = a.get(index)
    
    return tmp

def isString(a):
    return jsTypeOf(a) == 'string'

def charSequenceLength(a):
    if isString(a):
        tmp0_unsafeCast_0 = length(a)
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
    else:
        tmp = a._get_length_()
    
    return tmp

def charSequenceSubSequence(a, startIndex, endIndex):
    if isString(a):
        tmp0_unsafeCast_0 = INVOKE(substring(a), startIndex, endIndex)
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
    else:
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
        return self.invoke((kotlin_Any_(p1)) if ((True) if (p1 == None) else (isObject(p1))) else (THROW_CCE()))
    

def _no_name_provided__factory():
    i = _no_name_provided_()
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionExpressionImpl

def compareTo(a, b):
    tmp0_subject = jsTypeOf(a)
    if tmp0_subject == 'number':
        if jsTypeOf(b) == 'number':
            tmp = doubleCompareTo(a, b)
        elif jsInstanceOf(b, jsClass()):
            tmp = doubleCompareTo(a, kotlin_Long(b).toDouble())
        elif True:
            tmp = primitiveCompareTo(a, b)
        
        tmp = tmp
    elif (True) if (tmp0_subject == 'string') else (tmp0_subject == 'boolean'):
        tmp = primitiveCompareTo(a, b)
    else:
        tmp = compareToDoNotIntrinsicify(kotlin_Comparable_dynamic_(a), b)
    
    return tmp

def doubleCompareTo(a, b):
    if LT(a, b):
        tmp = -1
    elif GT(a, b):
        tmp = 1
    elif EQEQEQ(a, b):
        if EXCLEQEQ(a, 0):
            tmp = 0
        else:
            ia = DIV(1, a)
            if EQEQEQ(ia, DIV(1, b)):
                tmp = 0
            elif LT(ia, 0):
                tmp = -1
            elif True:
                tmp = 1
            
            tmp = tmp
        
        tmp = tmp
    elif EXCLEQEQ(a, a):
        tmp = (0) if (EXCLEQEQ(b, b)) else (1)
    else:
        tmp = -1
    
    return tmp

def primitiveCompareTo(a, b):
    return (-1) if (LT(a, b)) else ((1) if (GT(a, b)) else (0))

def compareToDoNotIntrinsicify(a, b):
    return a.compareTo(b)

def construct(constructorType, resultType, *args):
    return kotlin_Any(INVOKE(construct(js('Reflect')), constructorType, args, resultType))

def identityHashCode(obj):
    return getObjectHashCode(obj)

def getObjectHashCode(obj):
    if not jsIn('kotlinHashCodeValue$', kotlin_Any(obj)):
        hash = jsBitwiseOr(MUL(INVOKE(random(js('Math'))), 4.294967296E9), 0)
        descriptor = js('new Object()')
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    
    tmp0_unsafeCast_0 = ARRAY_ACCESS(obj, 'kotlinHashCodeValue$')
    return kotlin_Any_(tmp0_unsafeCast_0)

def _get_OBJECT_HASH_CODE_PROPERTY_NAME_():
    return OBJECT_HASH_CODE_PROPERTY_NAME

OBJECT_HASH_CODE_PROPERTY_NAME = 'kotlinHashCodeValue$'
def _get_POW_2_32_():
    return POW_2_32

POW_2_32 = 4.294967296E9
def hashCode(obj):
    if EQEQ(obj, None):
        return 0
    
    tmp0_subject = jsTypeOf(obj)
    if tmp0_subject == 'object':
        tmp = kotlin_Int((INVOKE(hashCode(obj))) if ('function' is jsTypeOf(hashCode(obj))) else (getObjectHashCode(obj)))
    elif tmp0_subject == 'function':
        tmp = getObjectHashCode(obj)
    elif tmp0_subject == 'number':
        tmp = getNumberHashCode(kotlin_Double(obj))
    elif tmp0_subject == 'boolean':
        if kotlin_Any_(obj):
            tmp = 1
        elif True:
            tmp = 0
        
        tmp = tmp
    else:
        tmp = getStringHashCode(kotlin_String(INVOKE(js('String'), obj)))
    
    return tmp

def getStringHashCode(str):
    hash = 0
    length = len(str)
    inductionVariable = 0
    last = (length - 1) | 0
    if inductionVariable <= last:
        while True:
            i = inductionVariable
            inductionVariable = (inductionVariable + 1) | 0
            code = kotlin_Int(INVOKE(charCodeAt(str), i))
            hash = (imul(hash, 31) + code) | 0
            if not (i == last):
                break
            
        
    
    return hash

def toString(o):
    if EQEQ(o, None):
        tmp = 'null'
    elif isArrayish(o):
        tmp = '[...]'
    else:
        tmp0_unsafeCast_0 = INVOKE(toString(o))
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
    
    return tmp

def anyToString(o):
    return kotlin_String(INVOKE(call(toString(prototype(js('Object')))), o))

def equals(obj1, obj2):
    if EQEQ(obj1, None):
        return EQEQ(obj2, None)
    
    if EQEQ(obj2, None):
        return False
    
    if (jsTypeOf(equals(obj1)) == 'function') if (jsTypeOf(obj1) == 'object') else (False):
        return kotlin_Boolean(INVOKE(equals(obj1), obj2))
    
    if EXCLEQEQ(obj1, obj1):
        return EXCLEQEQ(obj2, obj2)
    
    if (jsTypeOf(obj2) == 'number') if (jsTypeOf(obj1) == 'number') else (False):
        if EQEQEQ(obj1, obj2):
            if EXCLEQEQ(obj1, 0):
                tmp = True
            else:
                tmp = DIV(1, obj1)
                tmp = EQEQEQ(tmp, DIV(1, obj2))
            
            tmp = tmp
        else:
            tmp = False
        
        return tmp
    
    return EQEQEQ(obj1, obj2)

def boxIntrinsic(x):
    raise IllegalStateException_init__Create_('Should be lowered')

def unboxIntrinsic(x):
    raise IllegalStateException_init__Create_('Should be lowered')

def captureStack(instance, constructorFunction):
    if EXCLEQ(captureStackTrace(js('Error')), None):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    else:
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    

def newThrowable(message, cause):
    throwable = js('new Error()')
    if isUndefined(message):
        if isUndefined(cause):
            tmp = message
        else:
            tmp0_safe_receiver = cause
            tmp1_elvis_lhs = (None) if (tmp0_safe_receiver == None) else (tmp0_safe_receiver.toString())
            tmp = (_get_undefined_()) if (tmp1_elvis_lhs == None) else (tmp1_elvis_lhs)
        
        tmp = tmp
    else:
        tmp2_elvis_lhs = message
        tmp = (_get_undefined_()) if (tmp2_elvis_lhs == None) else (tmp2_elvis_lhs)
    
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    return kotlin_Any_(throwable)

def isUndefined(value):
    return EQEQEQ(value, _get_undefined_())

def extendThrowable(this_, message, cause):
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    setPropertiesToThrowableInstance(this_, message, cause)

def setPropertiesToThrowableInstance(this_, message, cause):
    if not hasOwnPrototypeProperty(kotlin_Any(this_), 'message'):
        if message == None:
            if not (message is None):
                tmp0_safe_receiver = cause
                tmp1_elvis_lhs = (None) if (tmp0_safe_receiver == None) else (tmp0_safe_receiver.toString())
                tmp = (_get_undefined_()) if (tmp1_elvis_lhs == None) else (tmp1_elvis_lhs)
            else:
                tmp = _get_undefined_()
            
            tmp = tmp
        else:
            tmp = message
        
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    
    if not hasOwnPrototypeProperty(kotlin_Any(this_), 'cause'):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl

def hasOwnPrototypeProperty(o, name):
    tmp0_unsafeCast_0 = INVOKE(hasOwnProperty(visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl.getPrototypeOf(o)), name)
    return kotlin_Any_(tmp0_unsafeCast_0)

def getContinuation():
    raise Exception_init__Create_('Implemented as intrinsic')

def returnIfSuspended(argument):
    raise Exception_init__Create_('Implemented as intrinsic')

def suspendCoroutineUninterceptedOrReturnJS(block):
    return block.invoke(getContinuation())

def getCoroutineContext():
    return getContinuation()._get_context_()

def unreachableDeclarationLog():
    tmp0_asDynamic_0 = _get_console_()
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl

def unreachableDeclarationException():
    raise JsError('Unreachable declaration')

def ensureNotNull(v):
    if v == None:
        THROW_NPE()
    else:
        tmp = v
    
    return tmp

def THROW_NPE():
    raise NullPointerException_init__Create_()

def noWhenBranchMatchedException():
    raise NoWhenBranchMatchedException_init__Create_()

def THROW_CCE():
    raise ClassCastException_init__Create_()

def throwUninitializedPropertyAccessException(name):
    raise UninitializedPropertyAccessException_init__Create_((str('lateinit property ') + str(name)) + str(' has not been initialized'))

def throwKotlinNothingValueException():
    raise KotlinNothingValueException_init__Create_()

def THROW_ISE():
    raise IllegalStateException_init__Create_()

def THROW_IAE(msg):
    raise IllegalArgumentException_init__Create_(msg)

def emptyArray():
    return kotlin_Array_T_(js('[]'))

class JsFun:
    def __init__(self, code):
        self.code = code
    
    def _get_code_(self):
        return self.code
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def enumValueOfIntrinsic(name):
    raise IllegalStateException_init__Create_('Should be replaced by compiler')

def enumValuesIntrinsic():
    raise IllegalStateException_init__Create_('Should be replaced by compiler')

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
    

pass
def Companion_getInstance():
    if Companion_instance == None:
        Companion()
    
    return Companion_instance

class Long:
    def __init__(self, low, high):
        Companion_getInstance()
        super()
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
        return self.compareTo((kotlin_Long(other)) if (jsInstanceOf(other, jsClass())) else (THROW_CCE()))
    
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
        return self.toFloat() + other
    
    def plus(self, other):
        return self.toDouble() + other
    
    def minus(self, other):
        return self.minus(toLong(other))
    
    def minus(self, other):
        return self.minus(toLong(other))
    
    def minus(self, other):
        return self.minus(toLong(other))
    
    def minus(self, other):
        return subtract(other)
    
    def minus(self, other):
        return self.toFloat() - other
    
    def minus(self, other):
        return self.toDouble() - other
    
    def times(self, other):
        return self.times(toLong(other))
    
    def times(self, other):
        return self.times(toLong(other))
    
    def times(self, other):
        return self.times(toLong(other))
    
    def times(self, other):
        return multiply(other)
    
    def times(self, other):
        return self.toFloat() * other
    
    def times(self, other):
        return self.toDouble() * other
    
    def div(self, other):
        return self.div(toLong(other))
    
    def div(self, other):
        return self.div(toLong(other))
    
    def div(self, other):
        return self.div(toLong(other))
    
    def div(self, other):
        return divide(other)
    
    def div(self, other):
        return self.toFloat() / other
    
    def div(self, other):
        return self.toDouble() / other
    
    def rem(self, other):
        return self.rem(toLong(other))
    
    def rem(self, other):
        return self.rem(toLong(other))
    
    def rem(self, other):
        return self.rem(toLong(other))
    
    def rem(self, other):
        return modulo(other)
    
    def rem(self, other):
        return self.toFloat() % other
    
    def rem(self, other):
        return self.toDouble() % other
    
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
        return Long(self.low & other.low, self.high & other.high)
    
    def _or(self, other):
        return Long(self.low | other.low, self.high | other.high)
    
    def xor(self, other):
        return Long(self.low ^ other.low, self.high ^ other.high)
    
    def inv(self):
        return Long(~self.low, ~self.high)
    
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
        if jsInstanceOf(other, jsClass()):
            tmp = equalsLong(kotlin_Long(other))
        elif True:
            tmp = False
        
        return tmp
    
    def hashCode(self):
        return hashCode(self)
    
    def toString(self):
        return toStringImpl(10)
    

def _get_ZERO_():
    init_properties_longjs_kt()
    return ZERO

ZERO = None
def _get_ONE_():
    init_properties_longjs_kt()
    return ONE

ONE = None
def _get_NEG_ONE_():
    init_properties_longjs_kt()
    return NEG_ONE

NEG_ONE = None
def _get_MAX_VALUE_():
    init_properties_longjs_kt()
    return MAX_VALUE

MAX_VALUE = None
def _get_MIN_VALUE_():
    init_properties_longjs_kt()
    return MIN_VALUE

MIN_VALUE = None
def _get_TWO_PWR_24__():
    init_properties_longjs_kt()
    return TWO_PWR_24_

TWO_PWR_24_ = None
def compare(other):
    init_properties_longjs_kt()
    if equalsLong(other):
        return 0
    
    thisNeg = isNegative()
    otherNeg = isNegative()
    return (-1) if ((not otherNeg) if (thisNeg) else (False)) else ((1) if ((otherNeg) if (not thisNeg) else (False)) else ((-1) if (isNegative()) else (1)))

def add(other):
    init_properties_longjs_kt()
    a48 = jsBitShiftRU(self.high, 16)
    a32 = self.high & 65535
    a16 = jsBitShiftRU(self.low, 16)
    a00 = self.low & 65535
    b48 = jsBitShiftRU(other.high, 16)
    b32 = other.high & 65535
    b16 = jsBitShiftRU(other.low, 16)
    b00 = other.low & 65535
    c48 = 0
    c32 = 0
    c16 = 0
    c00 = 0
    c00 = (c00 + ((a00 + b00) | 0)) | 0
    c16 = (c16 + jsBitShiftRU(c00, 16)) | 0
    c00 = c00 & 65535
    c16 = (c16 + ((a16 + b16) | 0)) | 0
    c32 = (c32 + jsBitShiftRU(c16, 16)) | 0
    c16 = c16 & 65535
    c32 = (c32 + ((a32 + b32) | 0)) | 0
    c48 = (c48 + jsBitShiftRU(c32, 16)) | 0
    c32 = c32 & 65535
    c48 = (c48 + ((a48 + b48) | 0)) | 0
    c48 = c48 & 65535
    return Long((c16 << 16) | c00, (c48 << 16) | c32)

def subtract(other):
    init_properties_longjs_kt()
    return add(other.unaryMinus())

def multiply(other):
    init_properties_longjs_kt()
    if isZero():
        return _get_ZERO_()
    elif isZero():
        return _get_ZERO_()
    
    if equalsLong(_get_MIN_VALUE_()):
        return (_get_MIN_VALUE_()) if (isOdd()) else (_get_ZERO_())
    elif equalsLong(_get_MIN_VALUE_()):
        return (_get_MIN_VALUE_()) if (isOdd()) else (_get_ZERO_())
    
    if isNegative():
        if isNegative():
            tmp = multiply(negate())
        else:
            tmp = negate()
        
        return tmp
    elif isNegative():
        return negate()
    
    if (lessThan(_get_TWO_PWR_24__())) if (lessThan(_get_TWO_PWR_24__())) else (False):
        return fromNumber(toNumber() * toNumber())
    
    a48 = jsBitShiftRU(self.high, 16)
    a32 = self.high & 65535
    a16 = jsBitShiftRU(self.low, 16)
    a00 = self.low & 65535
    b48 = jsBitShiftRU(other.high, 16)
    b32 = other.high & 65535
    b16 = jsBitShiftRU(other.low, 16)
    b00 = other.low & 65535
    c48 = 0
    c32 = 0
    c16 = 0
    c00 = 0
    c00 = (c00 + imul(a00, b00)) | 0
    c16 = (c16 + jsBitShiftRU(c00, 16)) | 0
    c00 = c00 & 65535
    c16 = (c16 + imul(a16, b00)) | 0
    c32 = (c32 + jsBitShiftRU(c16, 16)) | 0
    c16 = c16 & 65535
    c16 = (c16 + imul(a00, b16)) | 0
    c32 = (c32 + jsBitShiftRU(c16, 16)) | 0
    c16 = c16 & 65535
    c32 = (c32 + imul(a32, b00)) | 0
    c48 = (c48 + jsBitShiftRU(c32, 16)) | 0
    c32 = c32 & 65535
    c32 = (c32 + imul(a16, b16)) | 0
    c48 = (c48 + jsBitShiftRU(c32, 16)) | 0
    c32 = c32 & 65535
    c32 = (c32 + imul(a00, b32)) | 0
    c48 = (c48 + jsBitShiftRU(c32, 16)) | 0
    c32 = c32 & 65535
    c48 = (c48 + ((((((imul(a48, b00) + imul(a32, b16)) | 0) + imul(a16, b32)) | 0) + imul(a00, b48)) | 0)) | 0
    c48 = c48 & 65535
    return Long((c16 << 16) | c00, (c48 << 16) | c32)

def divide(other):
    init_properties_longjs_kt()
    if isZero():
        raise Exception_init__Create_('division by zero')
    elif isZero():
        return _get_ZERO_()
    
    if equalsLong(_get_MIN_VALUE_()):
        if (True) if (equalsLong(_get_ONE_())) else (equalsLong(_get_NEG_ONE_())):
            return _get_MIN_VALUE_()
        elif equalsLong(_get_MIN_VALUE_()):
            return _get_ONE_()
        else:
            halfThis = shiftRight(1)
            approx = shiftLeft(1)
            if equalsLong(_get_ZERO_()):
                return (_get_ONE_()) if (isNegative()) else (_get_NEG_ONE_())
            else:
                rem = subtract(multiply(approx))
                return add(rem.div(other))
            
        
    elif equalsLong(_get_MIN_VALUE_()):
        return _get_ZERO_()
    
    if isNegative():
        if isNegative():
            tmp = negate().div(negate())
        else:
            tmp = negate()
        
        return tmp
    elif isNegative():
        return negate()
    
    res = _get_ZERO_()
    rem = self
    while greaterThanOrEqual(other):
        approxDouble = toNumber() / toNumber()
        approx2 = visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl.max(1.0, visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl.floor(approxDouble))
        log2 = visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl.ceil(visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl.log(approx2) / visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl._get_LN2_())
        delta = (1.0) if (log2 <= 48.0) else (visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl.pow(2.0, log2 - 48))
        approxRes = fromNumber(approx2)
        approxRem = multiply(other)
        while (True) if (isNegative()) else (greaterThan(rem)):
            approx2 = approx2 - delta
            approxRes = fromNumber(approx2)
            approxRem = multiply(other)
        
        if isZero():
            approxRes = _get_ONE_()
        
        res = add(approxRes)
        rem = subtract(approxRem)
    
    return res

def modulo(other):
    init_properties_longjs_kt()
    return subtract(multiply(other))

def shiftLeft(numBits):
    init_properties_longjs_kt()
    numBits = numBits & 63
    if numBits == 0:
        return self
    elif numBits < 32:
        return Long(self.low << numBits, (self.high << numBits) | jsBitShiftRU(self.low, (32 - numBits) | 0))
    else:
        return Long(0, self.low << ((numBits - 32) | 0))
    

def shiftRight(numBits):
    init_properties_longjs_kt()
    numBits = numBits & 63
    if numBits == 0:
        return self
    elif numBits < 32:
        return Long(jsBitShiftRU(self.low, numBits) | (self.high << ((32 - numBits) | 0)), self.high >> numBits)
    else:
        return Long(self.high >> ((numBits - 32) | 0), (0) if (self.high >= 0) else (-1))
    

def shiftRightUnsigned(numBits):
    init_properties_longjs_kt()
    numBits = numBits & 63
    if numBits == 0:
        return self
    elif numBits < 32:
        return Long(jsBitShiftRU(self.low, numBits) | (self.high << ((32 - numBits) | 0)), jsBitShiftRU(self.high, numBits))
    else:
        if numBits == 32:
            tmp = Long(self.high, 0)
        else:
            tmp = Long(jsBitShiftRU(self.high, (numBits - 32) | 0), 0)
        
        return tmp
    

def toNumber():
    init_properties_longjs_kt()
    return (self.high * 4.294967296E9) + getLowBitsUnsigned()

def equalsLong(other):
    init_properties_longjs_kt()
    return (self.low == other.low) if (self.high == other.high) else (False)

def hashCode(l):
    init_properties_longjs_kt()
    return l.low ^ l.high

def toStringImpl(radix):
    init_properties_longjs_kt()
    if (True) if (radix < 2) else (36 < radix):
        raise Exception_init__Create_(str('radix out of range: ') + str(radix))
    
    if isZero():
        return '0'
    
    if isNegative():
        if equalsLong(_get_MIN_VALUE_()):
            radixLong = fromInt(radix)
            div = self.div(radixLong)
            rem = subtract(self).toInt()
            tmp = toStringImpl(radix)
            tmp0_unsafeCast_0 = INVOKE(toString(rem), radix)
            return tmp + kotlin_Any_(tmp0_unsafeCast_0)
        else:
            return str('-') + str(toStringImpl(radix))
        
    
    radixToPower = fromNumber(visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl.pow(kotlin_Double(radix), 6.0))
    rem = self
    result = ''
    while True:
        remDiv = rem.div(radixToPower)
        intval = subtract(multiply(radixToPower)).toInt()
        tmp1_unsafeCast_0 = INVOKE(toString(intval), radix)
        digits = kotlin_Any_(tmp1_unsafeCast_0)
        rem = remDiv
        if isZero():
            return digits + result
        else:
            while len(digits) < 6:
                digits = '0' + digits
            
            result = digits + result
        
    

def fromInt(value):
    init_properties_longjs_kt()
    return Long(value, (-1) if (value < 0) else (0))

def isNegative():
    init_properties_longjs_kt()
    return self.high < 0

def isZero():
    init_properties_longjs_kt()
    return (self.low == 0) if (self.high == 0) else (False)

def isOdd():
    init_properties_longjs_kt()
    return self.low & 1 == 1

def negate():
    init_properties_longjs_kt()
    return self.unaryMinus()

def lessThan(other):
    init_properties_longjs_kt()
    return compare(other) < 0

def fromNumber(value):
    init_properties_longjs_kt()
    if isNaN():
        return _get_ZERO_()
    elif value <= -9.223372036854776E18:
        return _get_MIN_VALUE_()
    elif value + 1 >= 9.223372036854776E18:
        return _get_MAX_VALUE_()
    elif value < 0.0:
        return negate()
    else:
        twoPwr32 = 4.294967296E9
        return Long(jsBitwiseOr(value % twoPwr32, 0), jsBitwiseOr(value / twoPwr32, 0))
    

def greaterThan(other):
    init_properties_longjs_kt()
    return compare(other) > 0

def greaterThanOrEqual(other):
    init_properties_longjs_kt()
    return compare(other) >= 0

def getLowBitsUnsigned():
    init_properties_longjs_kt()
    return (kotlin_Double(self.low)) if (self.low >= 0) else (4.294967296E9 + self.low)

def _get_TWO_PWR_32_DBL__():
    init_properties_longjs_kt()
    return TWO_PWR_32_DBL_

TWO_PWR_32_DBL_ = 4.294967296E9
def _get_TWO_PWR_63_DBL__():
    init_properties_longjs_kt()
    return TWO_PWR_63_DBL_

TWO_PWR_63_DBL_ = 9.223372036854776E18
properties_initialized_longjs_kt = False
def init_properties_longjs_kt():
    global properties_initialized_longjs_kt
    if not properties_initialized_longjs_kt:
        properties_initialized_longjs_kt = True
        global ZERO
        ZERO = fromInt(0)
        global ONE
        ONE = fromInt(1)
        global NEG_ONE
        NEG_ONE = fromInt(-1)
        global MAX_VALUE
        MAX_VALUE = Long(-1, 2147483647)
        global MIN_VALUE
        MIN_VALUE = Long(0, -2147483648)
        global TWO_PWR_24_
        TWO_PWR_24_ = fromInt(16777216)
    

def imul(a_local, b_local):
    lhs = kotlin_Double(jsBitwiseAnd(a_local, js('0xffff0000'))) * kotlin_Double(jsBitwiseAnd(b_local, 65535))
    rhs = kotlin_Double(jsBitwiseAnd(a_local, 65535)) * kotlin_Double(b_local)
    return jsBitwiseOr(lhs + rhs, 0)

def withType(type, array):
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    return array

def arrayConcat(*args):
    len = len(args)
    tmp0_unsafeCast_0 = js('Array(len)')
    typed = kotlin_Any_(tmp0_unsafeCast_0)
    inductionVariable = 0
    last = (len - 1) | 0
    if inductionVariable <= last:
        while True:
            i = inductionVariable
            inductionVariable = (inductionVariable + 1) | 0
            arr = args[i]
            if not ((isArray(arr)) if (not (arr == None)) else (False)):
                typed.__setitem__(i, T(INVOKE(call(slice(js('[]'))), arr)))
            elif True:
                typed.__setitem__(i, arr)
            
            if not (i == last):
                break
            
        
    
    return T(INVOKE(apply(concat(js('[]'))), js('[]'), typed))

def primitiveArrayConcat(*args):
    size_local = 0
    inductionVariable = 0
    last = (len(args) - 1) | 0
    if inductionVariable <= last:
        while True:
            i = inductionVariable
            inductionVariable = (inductionVariable + 1) | 0
            tmp = size_local
            tmp0_unsafeCast_0 = args[i]
            size_local = (tmp + len(kotlin_Any_(tmp0_unsafeCast_0))) | 0
            if not (i == last):
                break
            
        
    
    a = args[0]
    tmp1_unsafeCast_0 = js('new a.constructor(size_local)')
    result = kotlin_Any_(tmp1_unsafeCast_0)
    if EXCLEQ(_type_(a), None):
        tmp2_withType_0 = kotlin_String(_type_(a))
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    
    size_local = 0
    inductionVariable = 0
    last = (len(args) - 1) | 0
    if inductionVariable <= last:
        while True:
            i = inductionVariable
            inductionVariable = (inductionVariable + 1) | 0
            tmp3_unsafeCast_0 = args[i]
            arr = kotlin_Any_(tmp3_unsafeCast_0)
            inductionVariable = 0
            last = (len(arr) - 1) | 0
            if inductionVariable <= last:
                while True:
                    j = inductionVariable
                    inductionVariable = (inductionVariable + 1) | 0
                    tmp3 = size_local
                    size_local = (tmp3 + 1) | 0
                    result.__setitem__(tmp3, arr[j])
                    if not (j == last):
                        break
                    
                
            
            if not (i == last):
                break
            
        
    
    return kotlin_Any_(result)

def taggedArrayCopy(array):
    res = INVOKE(slice(array))
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    return kotlin_Any_(res)

def numberToByte(a):
    return toByte(numberToInt(a))

def toByte(a):
    tmp0_unsafeCast_0 = js('a << 24 >> 24')
    return kotlin_Any_(tmp0_unsafeCast_0)

def numberToInt(a):
    if jsInstanceOf(a, jsClass()):
        tmp = kotlin_Long(a).toInt()
    elif True:
        tmp = doubleToInt(kotlin_Double(a))
    
    return tmp

def doubleToInt(a):
    return (2147483647) if (a > 2.147483647E9) else ((-2147483648) if (a < -2.147483648E9) else (jsBitwiseOr(a, 0)))

def numberToDouble(a):
    tmp0_unsafeCast_0 = js('+a')
    return kotlin_Any_(tmp0_unsafeCast_0)

def numberToShort(a):
    return toShort(numberToInt(a))

def toShort(a):
    tmp0_unsafeCast_0 = js('a << 16 >> 16')
    return kotlin_Any_(tmp0_unsafeCast_0)

def numberToLong(a):
    if jsInstanceOf(a, jsClass()):
        tmp = kotlin_Long(a)
    elif True:
        tmp = fromNumber(kotlin_Double(a))
    
    return tmp

def numberToChar(a):
    tmp0_toUShort_0 = numberToInt(a)
    return Char(_UShort___init__impl_(toShort(tmp0_toUShort_0)))

def toLong(a):
    return fromInt(kotlin_Int(a))

def numberRangeToNumber(start, endInclusive):
    return IntRange(kotlin_Int(start), kotlin_Int(endInclusive))

def numberRangeToLong(start, endInclusive):
    return LongRange(numberToLong(start), kotlin_Long(endInclusive))

def _get_propertyRefClassMetadataCache_():
    init_properties_reflectRuntime_kt()
    return propertyRefClassMetadataCache

propertyRefClassMetadataCache = None
def metadataObject():
    init_properties_reflectRuntime_kt()
    return js('{ kind: \'class\', interfaces: [] }')

def getPropertyCallableRef(name, paramCount, type, getter, setter):
    init_properties_reflectRuntime_kt()
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    tmp0_unsafeCast_0 = getPropertyRefClass(getter, getKPropMetadata(paramCount, setter, type))
    return kotlin_Any_(tmp0_unsafeCast_0)

def getPropertyRefClass(obj, metadata):
    init_properties_reflectRuntime_kt()
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    return obj

def getKPropMetadata(paramCount, setter, type):
    init_properties_reflectRuntime_kt()
    mdata = _get_propertyRefClassMetadataCache_()[paramCount][(0) if (setter == None) else (1)]
    if EQEQ(length(interfaces(mdata)), 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    
    return mdata

def getLocalDelegateReference(name, type, mutable, _lambda):
    init_properties_reflectRuntime_kt()
    return getPropertyCallableRef(name, 0, type, _lambda, (_lambda) if (mutable) else (None))

properties_initialized_reflectRuntime_kt = False
def init_properties_reflectRuntime_kt():
    global properties_initialized_reflectRuntime_kt
    if not properties_initialized_reflectRuntime_kt:
        properties_initialized_reflectRuntime_kt = True
        global propertyRefClassMetadataCache
        tmp = js('{ kind: \'class\', interfaces: [] }')
        tmp0_arrayOf_0 = tmp
        tmp = js('{ kind: \'class\', interfaces: [] }')
        tmp1_arrayOf_0 = tmp
        tmp = js('{ kind: \'class\', interfaces: [] }')
        tmp2_arrayOf_0 = tmp
        tmp3_arrayOf_0 = kotlin_Any_(tmp0_arrayOf_0)
        propertyRefClassMetadataCache = kotlin_Any_(tmp3_arrayOf_0)
    

def isInterface(obj, iface):
    tmp0_elvis_lhs = constructor(obj)
    if tmp0_elvis_lhs == None:
        return False
    else:
        tmp = tmp0_elvis_lhs
    
    ctor = tmp
    return isInterfaceImpl(kotlin_js_Ctor(ctor), iface)

def isInterfaceImpl(ctor, iface):
    if ctor is iface:
        return True
    
    metadata = ctor._get__metadata__()
    if not (metadata == None):
        interfaces = metadata._get_interfaces_()
        indexedObject = interfaces
        inductionVariable = 0
        last = len(indexedObject)
        while inductionVariable < last:
            i = indexedObject[inductionVariable]
            inductionVariable = (inductionVariable + 1) | 0
            if isInterfaceImpl(i, iface):
                return True
            
        
    
    superPrototype = (INVOKE(getPrototypeOf(js('Object')), ctor._get_prototype_())) if (not (ctor._get_prototype_() == None)) else (None)
    superConstructor = (kotlin_js_Ctor_(constructor(superPrototype))) if (EXCLEQ(superPrototype, None)) else (None)
    return (isInterfaceImpl(superConstructor, iface)) if (not (superConstructor == None)) else (False)

def isArray(obj):
    if isJsArray(obj):
        tmp = kotlin_Boolean(EXCL(_type_(obj)))
    else:
        tmp = False
    
    return tmp

def isJsArray(obj):
    tmp0_unsafeCast_0 = INVOKE(isArray(js('Array')), obj)
    return kotlin_Any_(tmp0_unsafeCast_0)

def isObject(obj):
    objTypeOf = jsTypeOf(obj)
    tmp0_subject = objTypeOf
    return (True) if (tmp0_subject == 'string') else ((True) if (tmp0_subject == 'number') else ((True) if (tmp0_subject == 'boolean') else ((True) if (tmp0_subject == 'function') else (jsInstanceOf(obj, js('Object'))))))

def isSuspendFunction(obj, arity):
    if jsTypeOf(obj) == 'function':
        tmp0_unsafeCast_0 = _arity(obj)
        return kotlin_Any_(tmp0_unsafeCast_0) is arity
    
    return False

def isNumber(a):
    if jsTypeOf(a) == 'number':
        tmp = True
    else:
        tmp = jsInstanceOf(a, jsClass())
    
    return tmp

def isComparable(value):
    type = jsTypeOf(value)
    return (True) if ((True) if ((True) if (type == 'string') else (type == 'boolean')) else (isNumber(value))) else (isInterface(value, _get_js_()))

def isCharSequence(value):
    return (True) if (jsTypeOf(value) == 'string') else (isInterface(value, _get_js_()))

def isBooleanArray(a):
    return (EQEQEQ(_type_(a), 'BooleanArray')) if (isJsArray(kotlin_Any(a))) else (False)

def isByteArray(a):
    return jsInstanceOf(a, js('Int8Array'))

def isShortArray(a):
    return jsInstanceOf(a, js('Int16Array'))

def isCharArray(a):
    return (EQEQEQ(_type_(a), 'CharArray')) if (isJsArray(kotlin_Any(a))) else (False)

def isIntArray(a):
    return jsInstanceOf(a, js('Int32Array'))

def isFloatArray(a):
    return jsInstanceOf(a, js('Float32Array'))

def isLongArray(a):
    return (EQEQEQ(_type_(a), 'LongArray')) if (isJsArray(kotlin_Any(a))) else (False)

def isDoubleArray(a):
    return jsInstanceOf(a, js('Float64Array'))

def isArrayish(o):
    if isJsArray(kotlin_Any(o)):
        tmp = True
    else:
        tmp0_unsafeCast_0 = INVOKE(isView(js('ArrayBuffer')), o)
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
    
    return tmp

def jsIsType(obj, jsClass):
    if EQEQEQ(jsClass, js('Object')):
        return isObject(obj)
    
    if (True) if ((True) if (EQEQ(obj, None)) else (EQEQ(jsClass, None))) else ((not (jsTypeOf(obj) == 'function')) if (not (jsTypeOf(obj) == 'object')) else (False)):
        return False
    
    if (jsInstanceOf(obj, jsClass)) if (jsTypeOf(jsClass) == 'function') else (False):
        return True
    
    proto = jsGetPrototypeOf(jsClass)
    tmp0_safe_receiver = proto
    constructor = (None) if (tmp0_safe_receiver == None) else (constructor(tmp0_safe_receiver))
    if (jsIn('$metadata$', kotlin_Any(constructor))) if (EXCLEQ(constructor, None)) else (False):
        metadata = _metadata_(constructor)
        if EQEQEQ(kind(metadata), 'object'):
            return EQEQEQ(obj, jsClass)
        
    
    klassMetadata = _metadata_(jsClass)
    if EQEQ(klassMetadata, None):
        return jsInstanceOf(obj, jsClass)
    
    if (EXCLEQ(constructor(obj), None)) if (EQEQEQ(kind(klassMetadata), 'interface')) else (False):
        return isInterfaceImpl(kotlin_js_Ctor(constructor(obj)), jsClass)
    
    return False

def jsGetPrototypeOf(jsClass):
    return INVOKE(getPrototypeOf(js('Object')), jsClass)

def asList():
    return ArrayList(kotlin_Any_(self))

def plus(elements):
    return kotlin_Array_T_(INVOKE(concat(self), elements))

def copyOfRange(fromIndex, toIndex):
    Companion_getInstance().checkRangeIndexes(fromIndex, toIndex, len(self))
    return kotlin_Array_T_(INVOKE(slice(self), fromIndex, toIndex))

def copyInto(destination, destinationOffset, startIndex, endIndex):
    arrayCopy(self, destination, destinationOffset, startIndex, endIndex)
    return destination

def minOf(a, b):
    return visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl.min(a, b)

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
    if (not (intercepted is _this)) if (not (intercepted == None)) else (False):
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
        tmp._context = (None) if (tmp0_safe_receiver == None) else (tmp0_safe_receiver._get_context_())
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
        if tmp2_elvis_lhs == None:
            tmp0_safe_receiver = self._get_context_().get(Key_getInstance())
            tmp1_elvis_lhs = (None) if (tmp0_safe_receiver == None) else (tmp0_safe_receiver.interceptContinuation(self))
            tmp0_also_0 = (self) if (tmp1_elvis_lhs == None) else (tmp1_elvis_lhs)
            self.intercepted_ = tmp0_also_0
            tmp = tmp0_also_0
        else:
            tmp = tmp2_elvis_lhs
        
        return tmp
    
    def resumeWith(self, result):
        current = self
        if _Result___get_isFailure__impl_(result):
            tmp = None
        else:
            tmp = _Result___get_value__impl_(result)
            tmp = (T(tmp)) if ((True) if (tmp == None) else (isObject(tmp))) else (THROW_CCE())
        
        currentResult = tmp
        currentException = Result__exceptionOrNull_impl(result)
        while True:
            tmp0_with_0 = current
            if currentException == None:
                tmp0_with_0.result = currentResult
            else:
                tmp0_with_0.state = tmp0_with_0.exceptionState
                tmp0_with_0.exception = currentException
            
            visitTry_org_jetbrains_kotlin_ir_expressions_impl_IrTryImpl
            releaseIntercepted(tmp0_with_0)
            completion_4 = ensureNotNull(tmp0_with_0.resultContinuation)
            if jsInstanceOf(completion_4, jsClass()):
                current = kotlin_coroutines_CoroutineImpl(completion_4)
            elif True:
                if not (currentException == None):
                    tmp0_resumeWithException_0_5 = ensureNotNull(currentException)
                    tmp0_failure_0_1_6 = Companion_getInstance()
                    completion_4.resumeWith(_Result___init__impl_(createFailure(tmp0_resumeWithException_0_5)))
                else:
                    tmp1_resume_0_7 = currentResult
                    tmp0_success_0_1_8 = Companion_getInstance()
                    completion_4.resumeWith(_Result___init__impl_(tmp1_resume_0_7))
                
                return Unit_getInstance()
            
        
    
    def resumeWith(self, result):
        return self.resumeWith(result)
    
    def doResume(self):
        pass
    
    def create(self, completion):
        raise UnsupportedOperationException_init__Create_('create(Continuation) has not been overridden')
    
    def create(self, value, completion):
        raise UnsupportedOperationException_init__Create_('create(Any?;Continuation) has not been overridden')
    
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
        raise IllegalStateException_init__Create_('This continuation is already complete')
    
    def resumeWith(self, result):
        raise IllegalStateException_init__Create_('This continuation is already complete')
    
    def resumeWith(self, result):
        return self.resumeWith(result)
    
    def toString(self):
        return 'This continuation is already complete'
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    

pass
def CompletedContinuation_getInstance():
    if CompletedContinuation_instance == None:
        CompletedContinuation()
    
    return CompletedContinuation_instance

def Exception_init__Init_(_this):
    extendThrowable(_this, _undefined(), _undefined())
    super()
    return _this

def Exception_init__Create_():
    tmp = Exception_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def Exception_init__Init_(message, _this):
    extendThrowable(_this, message, _undefined())
    super()
    return _this

def Exception_init__Create_(message):
    tmp = Exception_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def Exception_init__Init_(message, cause, _this):
    extendThrowable(_this, message, cause)
    super()
    return _this

def Exception_init__Create_(message, cause):
    tmp = Exception_init__Init_(message, cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def Exception_init__Init_(cause, _this):
    extendThrowable(_this, _undefined(), cause)
    super()
    return _this

def Exception_init__Create_(cause):
    tmp = Exception_init__Init_(cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
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
        captureStack(self, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    

def Error_init__Init_(_this):
    extendThrowable(_this, _undefined(), _undefined())
    super()
    return _this

def Error_init__Create_():
    tmp = Error_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def Error_init__Init_(message, _this):
    extendThrowable(_this, message, _undefined())
    super()
    return _this

def Error_init__Create_(message):
    tmp = Error_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def Error_init__Init_(message, cause, _this):
    extendThrowable(_this, message, cause)
    super()
    return _this

def Error_init__Create_(message, cause):
    tmp = Error_init__Init_(message, cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def Error_init__Init_(cause, _this):
    extendThrowable(_this, _undefined(), cause)
    super()
    return _this

def Error_init__Create_(cause):
    tmp = Error_init__Init_(cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
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
        captureStack(self, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    

def IllegalArgumentException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    super()
    return _this

def IllegalArgumentException_init__Create_():
    tmp = IllegalArgumentException_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def IllegalArgumentException_init__Init_(message, _this):
    RuntimeException_init__Init_(message, _this)
    super()
    return _this

def IllegalArgumentException_init__Create_(message):
    tmp = IllegalArgumentException_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def IllegalArgumentException_init__Init_(message, cause, _this):
    RuntimeException_init__Init_(message, cause, _this)
    super()
    return _this

def IllegalArgumentException_init__Create_(message, cause):
    tmp = IllegalArgumentException_init__Init_(message, cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def IllegalArgumentException_init__Init_(cause, _this):
    RuntimeException_init__Init_(cause, _this)
    super()
    return _this

def IllegalArgumentException_init__Create_(cause):
    tmp = IllegalArgumentException_init__Init_(cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
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
        captureStack(self, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    

def RuntimeException_init__Init_(_this):
    Exception_init__Init_(_this)
    super()
    return _this

def RuntimeException_init__Create_():
    tmp = RuntimeException_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def RuntimeException_init__Init_(message, _this):
    Exception_init__Init_(message, _this)
    super()
    return _this

def RuntimeException_init__Create_(message):
    tmp = RuntimeException_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def RuntimeException_init__Init_(message, cause, _this):
    Exception_init__Init_(message, cause, _this)
    super()
    return _this

def RuntimeException_init__Create_(message, cause):
    tmp = RuntimeException_init__Init_(message, cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def RuntimeException_init__Init_(cause, _this):
    Exception_init__Init_(cause, _this)
    super()
    return _this

def RuntimeException_init__Create_(cause):
    tmp = RuntimeException_init__Init_(cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
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
        captureStack(self, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    

def NoSuchElementException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    super()
    return _this

def NoSuchElementException_init__Create_():
    tmp = NoSuchElementException_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def NoSuchElementException_init__Init_(message, _this):
    RuntimeException_init__Init_(message, _this)
    super()
    return _this

def NoSuchElementException_init__Create_(message):
    tmp = NoSuchElementException_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
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
        captureStack(self, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    

def IllegalStateException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    super()
    return _this

def IllegalStateException_init__Create_():
    tmp = IllegalStateException_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def IllegalStateException_init__Init_(message, _this):
    RuntimeException_init__Init_(message, _this)
    super()
    return _this

def IllegalStateException_init__Create_(message):
    tmp = IllegalStateException_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def IllegalStateException_init__Init_(message, cause, _this):
    RuntimeException_init__Init_(message, cause, _this)
    super()
    return _this

def IllegalStateException_init__Create_(message, cause):
    tmp = IllegalStateException_init__Init_(message, cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def IllegalStateException_init__Init_(cause, _this):
    RuntimeException_init__Init_(cause, _this)
    super()
    return _this

def IllegalStateException_init__Create_(cause):
    tmp = IllegalStateException_init__Init_(cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
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
        captureStack(self, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    

def UnsupportedOperationException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    super()
    return _this

def UnsupportedOperationException_init__Create_():
    tmp = UnsupportedOperationException_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def UnsupportedOperationException_init__Init_(message, _this):
    RuntimeException_init__Init_(message, _this)
    super()
    return _this

def UnsupportedOperationException_init__Create_(message):
    tmp = UnsupportedOperationException_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def UnsupportedOperationException_init__Init_(message, cause, _this):
    RuntimeException_init__Init_(message, cause, _this)
    super()
    return _this

def UnsupportedOperationException_init__Create_(message, cause):
    tmp = UnsupportedOperationException_init__Init_(message, cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def UnsupportedOperationException_init__Init_(cause, _this):
    RuntimeException_init__Init_(cause, _this)
    super()
    return _this

def UnsupportedOperationException_init__Create_(cause):
    tmp = UnsupportedOperationException_init__Init_(cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
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
        captureStack(self, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    

def NullPointerException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    super()
    return _this

def NullPointerException_init__Create_():
    tmp = NullPointerException_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def NullPointerException_init__Init_(message, _this):
    RuntimeException_init__Init_(message, _this)
    super()
    return _this

def NullPointerException_init__Create_(message):
    tmp = NullPointerException_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
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
        captureStack(self, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    

def IndexOutOfBoundsException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    super()
    return _this

def IndexOutOfBoundsException_init__Create_():
    tmp = IndexOutOfBoundsException_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def IndexOutOfBoundsException_init__Init_(message, _this):
    RuntimeException_init__Init_(message, _this)
    super()
    return _this

def IndexOutOfBoundsException_init__Create_(message):
    tmp = IndexOutOfBoundsException_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
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
        captureStack(self, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    

def NoWhenBranchMatchedException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    super()
    return _this

def NoWhenBranchMatchedException_init__Create_():
    tmp = NoWhenBranchMatchedException_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def NoWhenBranchMatchedException_init__Init_(message, _this):
    RuntimeException_init__Init_(message, _this)
    super()
    return _this

def NoWhenBranchMatchedException_init__Create_(message):
    tmp = NoWhenBranchMatchedException_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def NoWhenBranchMatchedException_init__Init_(message, cause, _this):
    RuntimeException_init__Init_(message, cause, _this)
    super()
    return _this

def NoWhenBranchMatchedException_init__Create_(message, cause):
    tmp = NoWhenBranchMatchedException_init__Init_(message, cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def NoWhenBranchMatchedException_init__Init_(cause, _this):
    RuntimeException_init__Init_(cause, _this)
    super()
    return _this

def NoWhenBranchMatchedException_init__Create_(cause):
    tmp = NoWhenBranchMatchedException_init__Init_(cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
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
        captureStack(self, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    

def ClassCastException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    super()
    return _this

def ClassCastException_init__Create_():
    tmp = ClassCastException_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def ClassCastException_init__Init_(message, _this):
    RuntimeException_init__Init_(message, _this)
    super()
    return _this

def ClassCastException_init__Create_(message):
    tmp = ClassCastException_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
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
        captureStack(self, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    

def UninitializedPropertyAccessException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    super()
    return _this

def UninitializedPropertyAccessException_init__Create_():
    tmp = UninitializedPropertyAccessException_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def UninitializedPropertyAccessException_init__Init_(message, _this):
    RuntimeException_init__Init_(message, _this)
    super()
    return _this

def UninitializedPropertyAccessException_init__Create_(message):
    tmp = UninitializedPropertyAccessException_init__Init_(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def UninitializedPropertyAccessException_init__Init_(message, cause, _this):
    RuntimeException_init__Init_(message, cause, _this)
    super()
    return _this

def UninitializedPropertyAccessException_init__Create_(message, cause):
    tmp = UninitializedPropertyAccessException_init__Init_(message, cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def UninitializedPropertyAccessException_init__Init_(cause, _this):
    RuntimeException_init__Init_(cause, _this)
    super()
    return _this

def UninitializedPropertyAccessException_init__Create_(cause):
    tmp = UninitializedPropertyAccessException_init__Init_(cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
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
        captureStack(self, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    

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

def _get_c_():
    init_properties_python_kt()
    return c

c = None
def _get_d_():
    init_properties_python_kt()
    return d

d = None
def box():
    init_properties_python_kt()
    _get_c_()
    _get_d_()
    return 'OK'

properties_initialized_python_kt = False
def init_properties_python_kt():
    global properties_initialized_python_kt
    if not properties_initialized_python_kt:
        properties_initialized_python_kt = True
        global c
        c = Unit_getInstance()
        global d
        d = _get_c_()
    
