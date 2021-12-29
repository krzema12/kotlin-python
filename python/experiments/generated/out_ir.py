def fold(self, initial, operation):
    accumulator = initial
    tmp0_iterator = arrayIterator(self)
    while tmp0_iterator.hasNext_0_k_():
        element = tmp0_iterator.next_0_k_()
        accumulator = operation(accumulator, element)
    
    return accumulator

def contains(self, element):
    return indexOf(self, element) >= 0

def indexOf(self, element):
    tmp0_iterator = _get_indices_(self).iterator_0_k_()
    while tmp0_iterator.hasNext_0_k_():
        index = tmp0_iterator.next_0_k_()
        if element == self[index]:
            return index
        
    
    return -1

def _get_indices_(self):
    return IntRange(0, _get_lastIndex_(self))

def _get_lastIndex_(self):
    return (((len(self) - 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000

def contains_0(self, element):
    return indexOf_0(self, element) >= 0

def indexOf_0(self, element):
    tmp0_iterator = _get_indices__0(self).iterator_0_k_()
    while tmp0_iterator.hasNext_0_k_():
        index = tmp0_iterator.next_0_k_()
        if element == self[index]:
            return index
        
    
    return -1

def _get_indices__0(self):
    return IntRange(0, _get_lastIndex__0(self))

def _get_lastIndex__0(self):
    return (((len(self) - 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000

def contains_1(self, element):
    return indexOf_1(self, element) >= 0

def indexOf_1(self, element):
    tmp0_iterator = _get_indices__1(self).iterator_0_k_()
    while tmp0_iterator.hasNext_0_k_():
        index = tmp0_iterator.next_0_k_()
        if element == self[index]:
            return index
        
    
    return -1

def _get_indices__1(self):
    return IntRange(0, _get_lastIndex__1(self))

def _get_lastIndex__1(self):
    return (((len(self) - 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000

def contains_2(self, element):
    return indexOf_2(self, element) >= 0

def indexOf_2(self, element):
    tmp0_iterator = _get_indices__2(self).iterator_0_k_()
    while tmp0_iterator.hasNext_0_k_():
        index = tmp0_iterator.next_0_k_()
        if element == self[index]:
            return index
        
    
    return -1

def _get_indices__2(self):
    return IntRange(0, _get_lastIndex__2(self))

def _get_lastIndex__2(self):
    return (((len(self) - 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000

def _get_indices__3(self):
    return IntRange(0, _get_lastIndex__3(self))

def indexOf_3(self, element):
    if element == None:
        tmp0_iterator = _get_indices__3(self).iterator_0_k_()
        while tmp0_iterator.hasNext_0_k_():
            index = tmp0_iterator.next_0_k_()
            if self[index] == None:
                return index
            
        
    else:
        tmp1_iterator = _get_indices__3(self).iterator_0_k_()
        while tmp1_iterator.hasNext_0_k_():
            index = tmp1_iterator.next_0_k_()
            if element == self[index]:
                return index
            
        
    
    return -1

def lastIndexOf(self, element):
    if element == None:
        tmp0_iterator = reversed(_get_indices__3(self)).iterator_0_k_()
        while tmp0_iterator.hasNext_0_k_():
            index = tmp0_iterator.next_0_k_()
            if self[index] == None:
                return index
            
        
    else:
        tmp1_iterator = reversed(_get_indices__3(self)).iterator_0_k_()
        while tmp1_iterator.hasNext_0_k_():
            index = tmp1_iterator.next_0_k_()
            if element == self[index]:
                return index
            
        
    
    return -1

def _get_lastIndex__3(self):
    return (((len(self) - 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000

def joinToString(self, separator, prefix, postfix, limit, truncated, transform):
    return joinTo(self, StringBuilder_init__Create__1(), separator, prefix, postfix, limit, truncated, transform).toString()

def joinTo(self, buffer, separator, prefix, postfix, limit, truncated, transform):
    buffer.append_v1o70a_k_(prefix)
    Unit_getInstance()
    count = 0
    tmp0_iterator = arrayIterator(self)
    while tmp0_iterator.hasNext_0_k_():
        element = tmp0_iterator.next_0_k_()
        count = (((count + 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
        if count > 1:
            buffer.append_v1o70a_k_(separator)
            Unit_getInstance()
        
        if (True) if (limit < 0) else (count <= limit):
            appendElement(buffer, element, transform)
        else:
            break
        
    
    if (count > limit) if (limit >= 0) else (False):
        buffer.append_v1o70a_k_(truncated)
        Unit_getInstance()
    
    buffer.append_v1o70a_k_(postfix)
    Unit_getInstance()
    return buffer

def all(self, predicate):
    if isInterface(self, Collection):
        tmp = kotlin_collections_Collection_T_(self).isEmpty_0_k_()
    elif True:
        tmp = False
    
    if tmp:
        return True
    
    tmp0_iterator = self.iterator_0_k_()
    while tmp0_iterator.hasNext_0_k_():
        element = tmp0_iterator.next_0_k_()
        if not predicate(element):
            return False
        
    
    return True

def indexOfFirst(self, predicate):
    index = 0
    tmp0_iterator = self.iterator_0_k_()
    while tmp0_iterator.hasNext_0_k_():
        item = tmp0_iterator.next_0_k_()
        if predicate(item):
            return index
        
        tmp1 = index
        index = (((tmp1 + 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
        Unit_getInstance()
    
    return -1

def indexOfLast(self, predicate):
    iterator = self.listIterator_ha5a7z_k_(self._get_size__0_k_())
    while iterator.hasPrevious_0_k_():
        if predicate(iterator.previous_0_k_()):
            return iterator.nextIndex_0_k_()
        
    
    return -1

def any(self, predicate):
    if isInterface(self, Collection):
        tmp = kotlin_collections_Collection_T_(self).isEmpty_0_k_()
    elif True:
        tmp = False
    
    if tmp:
        return False
    
    tmp0_iterator = self.iterator_0_k_()
    while tmp0_iterator.hasNext_0_k_():
        element = tmp0_iterator.next_0_k_()
        if predicate(element):
            return True
        
    
    return False

def joinToString_0(self, separator, prefix, postfix, limit, truncated, transform):
    return joinTo_0(self, StringBuilder_init__Create__1(), separator, prefix, postfix, limit, truncated, transform).toString()

def joinTo_0(self, buffer, separator, prefix, postfix, limit, truncated, transform):
    buffer.append_v1o70a_k_(prefix)
    Unit_getInstance()
    count = 0
    tmp0_iterator = self.iterator_0_k_()
    while tmp0_iterator.hasNext_0_k_():
        element = tmp0_iterator.next_0_k_()
        count = (((count + 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
        if count > 1:
            buffer.append_v1o70a_k_(separator)
            Unit_getInstance()
        
        if (True) if (limit < 0) else (count <= limit):
            appendElement(buffer, element, transform)
        else:
            break
        
    
    if (count > limit) if (limit >= 0) else (False):
        buffer.append_v1o70a_k_(truncated)
        Unit_getInstance()
    
    buffer.append_v1o70a_k_(postfix)
    Unit_getInstance()
    return buffer

def forEach(self, action):
    tmp0_iterator = self.iterator_0_k_()
    while tmp0_iterator.hasNext_0_k_():
        element = tmp0_iterator.next_0_k_()
        action(element)
    

def map(self, transform):
    return mapTo(self, ArrayList_init__Create__0(collectionSizeOrDefault(self, 10)), transform)

def mapTo(self, destination, transform):
    tmp0_iterator = self.iterator_0_k_()
    while tmp0_iterator.hasNext_0_k_():
        item = tmp0_iterator.next_0_k_()
        destination.add_2bq_k_(transform(item))
        Unit_getInstance()
    
    return destination

def until(self, to):
    if to <= visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OBJECT_GET_INSTANCE_FUNCTION_name_Companion_getInstance_visibility_public_modality_FINAL_______returnType_kotlin_Int_Companion._get_MIN_VALUE__0_k_():
        return Companion_getInstance_14()._get_EMPTY__0_k_()
    
    return numberRangeToNumber(self, (((to - 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)

def downTo(self, to):
    return Companion_getInstance_11().fromClosedRange_fcwjfj_k_(self, to, -1)

def reversed(self):
    return Companion_getInstance_11().fromClosedRange_fcwjfj_k_(self._get_last__0_k_(), self._get_first__0_k_(), ((-self._get_step__0_k_() + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)

def getOrElse(self, index, defaultValue):
    return (charSequenceGet(self, index)) if ((index <= _get_lastIndex__5(self)) if (index >= 0) else (False)) else (defaultValue(index))

def KotlinNothingValueException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    return _this

def KotlinNothingValueException_init__Create_():
    tmp = KotlinNothingValueException_init__Init_(KotlinNothingValueException.__new__(KotlinNothingValueException))
    captureStack(tmp, KotlinNothingValueException_init__Create_)
    return tmp

def KotlinNothingValueException_init__Init__0(message, _this):
    RuntimeException_init__Init__0(message, _this)
    return _this

def KotlinNothingValueException_init__Create__0(message):
    tmp = KotlinNothingValueException_init__Init__0(message, KotlinNothingValueException.__new__(KotlinNothingValueException))
    captureStack(tmp, KotlinNothingValueException_init__Create_)
    return tmp

def KotlinNothingValueException_init__Init__1(message, cause, _this):
    RuntimeException_init__Init__1(message, cause, _this)
    return _this

def KotlinNothingValueException_init__Create__1(message, cause):
    tmp = KotlinNothingValueException_init__Init__1(message, cause, KotlinNothingValueException.__new__(KotlinNothingValueException))
    captureStack(tmp, KotlinNothingValueException_init__Create_)
    return tmp

def KotlinNothingValueException_init__Init__2(cause, _this):
    RuntimeException_init__Init__2(cause, _this)
    return _this

def KotlinNothingValueException_init__Create__2(cause):
    tmp = KotlinNothingValueException_init__Init__2(cause, KotlinNothingValueException.__new__(KotlinNothingValueException))
    captureStack(tmp, KotlinNothingValueException_init__Create_)
    return tmp

class RuntimeException:
    pass

class KotlinNothingValueException(RuntimeException):
    def _get_message__0_k_(self):
        pass
    
    def _get_cause__0_k_(self):
        pass
    
    def toString(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    

class Annotation:
    pass

class JvmMultifileClass(Annotation):
    def __init__(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class JvmName(Annotation):
    def __init__(self, name):
        pass
    
    def _get_name__0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class JvmPackageName(Annotation):
    def __init__(self, name):
        pass
    
    def _get_name__0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class JvmField(Annotation):
    def __init__(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class JvmInline(Annotation):
    def __init__(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class JvmStatic(Annotation):
    def __init__(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def _get_code_(self):
    return self.toInt_0_k_()

def Char(code):
    if (True) if (code < _get_code_(Companion_getInstance_17()._get_MIN_VALUE__0_k_())) else (code > _get_code_(Companion_getInstance_17()._get_MAX_VALUE__0_k_())):
        raise IllegalArgumentException_init__Create__0(str('Invalid Char code: ') + str(code))
    
    return numberToChar(code)

Level_WARNING_instance = None
Level_ERROR_instance = None
def values():
    return (Level_WARNING_getInstance(), Level_ERROR_getInstance())

def valueOf(value):
    if 'WARNING' == value:
        return Level_WARNING_getInstance()
    elif 'ERROR' == value:
        return Level_ERROR_getInstance()
    else:
        Level_initEntries()
        THROW_ISE()
    

Level_entriesInitialized = None
def Level_initEntries():
    global Level_entriesInitialized, Level_WARNING_instance, Level_ERROR_instance
    if Level_entriesInitialized:
        return Unit_getInstance()
    
    Level_entriesInitialized = True
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    Level_WARNING_instance = Unit_getInstance()
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    Level_ERROR_instance = Unit_getInstance()

class Enum:
    pass

class Level(Enum):
    def __init__(self):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    
    def _get_name__0_k_(self):
        pass
    
    def _get_ordinal__0_k_(self):
        pass
    
    def compareTo_desqae_k_(self, other):
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

class Experimental(Annotation):
    def __init__(self, level):
        pass
    
    def _get_level__0_k_(self):
        return self.level
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class WasExperimental(Annotation):
    def __init__(self, *markerClass):
        pass
    
    def _get_markerClass__0_k_(self):
        return self.markerClass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class ExperimentalStdlibApi(Annotation):
    def __init__(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class OptionalExpectation(Annotation):
    def __init__(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class ExperimentalMultiplatform(Annotation):
    def __init__(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class SharedImmutable(Annotation):
    def __init__(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

Level_WARNING_instance = None
Level_ERROR_instance = None
def values_0():
    return (Level_WARNING_getInstance_0(), Level_ERROR_getInstance_0())

def valueOf_0(value):
    if 'WARNING' == value:
        return Level_WARNING_getInstance_0()
    elif 'ERROR' == value:
        return Level_ERROR_getInstance_0()
    else:
        Level_initEntries_0()
        THROW_ISE()
    

Level_entriesInitialized = None
def Level_initEntries_0():
    global Level_entriesInitialized, Level_WARNING_instance, Level_ERROR_instance
    if Level_entriesInitialized:
        return Unit_getInstance()
    
    Level_entriesInitialized = True
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    Level_WARNING_instance = Unit_getInstance()
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    Level_ERROR_instance = Unit_getInstance()

class Level_0(Enum):
    def __init__(self):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    
    def _get_name__0_k_(self):
        pass
    
    def _get_ordinal__0_k_(self):
        pass
    
    def compareTo_desqae_k_(self, other):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def Level_WARNING_getInstance_0():
    Level_initEntries_0()
    return Level_WARNING_instance

def Level_ERROR_getInstance_0():
    Level_initEntries_0()
    return Level_ERROR_instance

class RequiresOptIn(Annotation):
    def __init__(self, message, level):
        pass
    
    def _get_message__0_k_(self):
        return self.message
    
    def _get_level__0_k_(self):
        return self.level
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class OptIn(Annotation):
    def __init__(self, *markerClass):
        pass
    
    def _get_markerClass__0_k_(self):
        return self.markerClass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class Collection:
    pass

class AbstractCollection(Collection):
    def __init__(self):
        pass
    
    def _get_size__0_k_(self):
        pass
    
    def iterator_0_k_(self):
        pass
    
    def contains_2bq_k_(self, element):
        return any(self, lambda it: it == element)
    
    def containsAll_dxd4eo_k_(self, elements):
        return all(elements, lambda it: self.contains_2bq_k_(it))
    
    def isEmpty_0_k_(self):
        return self._get_size__0_k_() == 0
    
    def toString(self):
        return joinToString_0(self, ', ', '[', ']', translateCallArguments_3, translateCallArguments_4, lambda it: ('(this Collection)') if (it is self) else (toString(it)))
    
    def toArray(self):
        return copyToArrayImpl_0(self)
    
    def toArray_gjotr5_k_(self, array):
        return copyToArrayImpl_1(self, array)
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    

class AbstractList:
    pass

class RandomAccess:
    pass

class SubList(AbstractList, RandomAccess):
    def __init__(self, list, fromIndex, toIndex):
        AbstractList.__init__(self)
        self.list = list
        self.fromIndex = fromIndex
        self._size = 0
        Companion_getInstance().checkRangeIndexes_zd700_k_(self._get_fromIndex__0_k_(), toIndex, self._get_list__0_k_()._get_size__0_k_())
        self._set__size__majfzk_k_((((toIndex - self._get_fromIndex__0_k_()) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
    
    def _get_list__0_k_(self):
        return self.list
    
    def _get_fromIndex__0_k_(self):
        return self.fromIndex
    
    def _set__size__majfzk_k_(self, _set___):
        self._size = _set___
    
    def _get__size__0_k_(self):
        return self._size
    
    def get_ha5a7z_k_(self, index):
        Companion_getInstance().checkElementIndex_rvwcgf_k_(index, self._get__size__0_k_())
        return self._get_list__0_k_().get_ha5a7z_k_((((self._get_fromIndex__0_k_() + index) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
    
    def _get_size__0_k_(self):
        return self._get__size__0_k_()
    
    def iterator_0_k_(self):
        pass
    
    def indexOf_2bq_k_(self, element):
        pass
    
    def lastIndexOf_2bq_k_(self, element):
        pass
    
    def listIterator_0_k_(self):
        pass
    
    def listIterator_ha5a7z_k_(self, index):
        pass
    
    def subList_27zxwg_k_(self, fromIndex, toIndex):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def contains_2bq_k_(self, element):
        pass
    
    def containsAll_dxd4eo_k_(self, elements):
        pass
    
    def isEmpty_0_k_(self):
        pass
    
    def toString(self):
        pass
    
    def toArray(self):
        pass
    
    def toArray_gjotr5_k_(self, array):
        pass
    

class Iterator_3:
    pass

class IteratorImpl(Iterator_3):
    def __init__(self):
        self.index = 0
    
    def _set_index__majfzk_k_(self, _set___):
        self.index = _set___
    
    def _get_index__0_k_(self):
        return self.index
    
    def hasNext_0_k_(self):
        return self._get_index__0_k_() < self._get_size__0_k_()
    
    def next_0_k_(self):
        if not self.hasNext_0_k_():
            raise NoSuchElementException_init__Create_()
        
        tmp0_this = self
        tmp1 = tmp0_this._get_index__0_k_()
        tmp0_this._set_index__majfzk_k_((((tmp1 + 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
        return self.get_ha5a7z_k_(tmp1)
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class ListIterator:
    pass

class ListIteratorImpl(IteratorImpl, ListIterator):
    def __init__(self, index):
        IteratorImpl.__init__(self)
        Companion_getInstance().checkPositionIndex_rvwcgf_k_(index, self._get_size__0_k_())
        self._set_index__majfzk_k_(index)
    
    def hasPrevious_0_k_(self):
        return self._get_index__0_k_() > 0
    
    def nextIndex_0_k_(self):
        return self._get_index__0_k_()
    
    def previous_0_k_(self):
        if not self.hasPrevious_0_k_():
            raise NoSuchElementException_init__Create_()
        
        tmp0_this = self
        tmp0_this._set_index__majfzk_k_((((tmp0_this._get_index__0_k_() - 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
        return self.get_ha5a7z_k_(tmp0_this._get_index__0_k_())
    
    def previousIndex_0_k_(self):
        return (((self._get_index__0_k_() - 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
    
    def _set_index__majfzk_k_(self, _set___):
        pass
    
    def _get_index__0_k_(self):
        pass
    
    def hasNext_0_k_(self):
        pass
    
    def next_0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class Any:
    pass

class Companion_0(Any):
    def __init__(self):
        global Companion_instance
        Companion_instance = self
    
    def checkElementIndex_rvwcgf_k_(self, index, size):
        if (True) if (index < 0) else (index >= size):
            raise IndexOutOfBoundsException_init__Create__0(((str('index: ') + str(index)) + str(', size: ')) + str(size))
        
    
    def checkPositionIndex_rvwcgf_k_(self, index, size):
        if (True) if (index < 0) else (index > size):
            raise IndexOutOfBoundsException_init__Create__0(((str('index: ') + str(index)) + str(', size: ')) + str(size))
        
    
    def checkRangeIndexes_zd700_k_(self, fromIndex, toIndex, size):
        if (True) if (fromIndex < 0) else (toIndex > size):
            raise IndexOutOfBoundsException_init__Create__0(((((str('fromIndex: ') + str(fromIndex)) + str(', toIndex: ')) + str(toIndex)) + str(', size: ')) + str(size))
        
        if fromIndex > toIndex:
            raise IllegalArgumentException_init__Create__0(((str('fromIndex: ') + str(fromIndex)) + str(' > toIndex: ')) + str(toIndex))
        
    
    def checkBoundsIndexes_zd700_k_(self, startIndex, endIndex, size):
        if (True) if (startIndex < 0) else (endIndex > size):
            raise IndexOutOfBoundsException_init__Create__0(((((str('startIndex: ') + str(startIndex)) + str(', endIndex: ')) + str(endIndex)) + str(', size: ')) + str(size))
        
        if startIndex > endIndex:
            raise IllegalArgumentException_init__Create__0(((str('startIndex: ') + str(startIndex)) + str(' > endIndex: ')) + str(endIndex))
        
    
    def orderedHashCode_dxd51x_k_(self, c):
        hashCode = 1
        tmp0_iterator = c.iterator_0_k_()
        while tmp0_iterator.hasNext_0_k_():
            e = tmp0_iterator.next_0_k_()
            tmp = imul(31, hashCode)
            tmp1_safe_receiver = e
            tmp2_elvis_lhs = (None) if (tmp1_safe_receiver == None) else (hashCode(tmp1_safe_receiver))
            hashCode = (((tmp + ((0) if (tmp2_elvis_lhs == None) else (tmp2_elvis_lhs))) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
        
        return hashCode
    
    def orderedEquals_tuq55s_k_(self, c, other):
        if not (c._get_size__0_k_() == other._get_size__0_k_()):
            return False
        
        otherIterator = other.iterator_0_k_()
        tmp0_iterator = c.iterator_0_k_()
        while tmp0_iterator.hasNext_0_k_():
            elem = tmp0_iterator.next_0_k_()
            elemOther = otherIterator.next_0_k_()
            if not (elem == elemOther):
                return False
            
        
        return True
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

Companion_instance = None
def Companion_getInstance():
    if Companion_instance == None:
        Companion_0()
    
    return Companion_instance

class List:
    pass

class AbstractList(AbstractCollection, List):
    def __init__(self):
        Companion_getInstance()
        AbstractCollection.__init__(self)
    
    def _get_size__0_k_(self):
        pass
    
    def get_ha5a7z_k_(self, index):
        pass
    
    def iterator_0_k_(self):
        return IteratorImpl()
    
    def indexOf_2bq_k_(self, element):
        return indexOfFirst(self, lambda it: it == element)
    
    def lastIndexOf_2bq_k_(self, element):
        return indexOfLast(self, lambda it: it == element)
    
    def listIterator_0_k_(self):
        return ListIteratorImpl(0)
    
    def listIterator_ha5a7z_k_(self, index):
        return ListIteratorImpl(index)
    
    def subList_27zxwg_k_(self, fromIndex, toIndex):
        return SubList(self, fromIndex, toIndex)
    
    def equals(self, other):
        if other is self:
            return True
        
        if not ((isInterface(other, List)) if (not (other == None)) else (False)):
            return False
        
        return Companion_getInstance().orderedEquals_tuq55s_k_(self, kotlin_collections_Collection___(other))
    
    def hashCode(self):
        return Companion_getInstance().orderedHashCode_dxd51x_k_(self)
    
    def contains_2bq_k_(self, element):
        pass
    
    def containsAll_dxd4eo_k_(self, elements):
        pass
    
    def isEmpty_0_k_(self):
        pass
    
    def toString(self):
        pass
    
    def toArray(self):
        pass
    
    def toArray_gjotr5_k_(self, array):
        pass
    

def listOf(*elements):
    return (asList(elements)) if (len(elements) > 0) else (emptyList())

def emptyList():
    return EmptyList_getInstance()

class Serializable:
    pass

class EmptyList(List, Serializable, RandomAccess):
    def __init__(self):
        global EmptyList_instance
        EmptyList_instance = self
        self.serialVersionUID = -7390468764508069838
    
    def _get_serialVersionUID__0_k_(self):
        return self.serialVersionUID
    
    def equals(self, other):
        if (isInterface(other, List)) if (not (other == None)) else (False):
            tmp = kotlin_collections_List___(other).isEmpty_0_k_()
        elif True:
            tmp = False
        
        return tmp
    
    def hashCode(self):
        return 1
    
    def toString(self):
        return '[]'
    
    def _get_size__0_k_(self):
        return 0
    
    def isEmpty_0_k_(self):
        return True
    
    def contains_5jd3j5_k_(self, element):
        return False
    
    def containsAll_lwol4p_k_(self, elements):
        return elements.isEmpty_0_k_()
    
    def get_ha5a7z_k_(self, index):
        raise IndexOutOfBoundsException_init__Create__0((str('Empty list doesn\'t contain element at index ') + str(index)) + str('.'))
    
    def indexOf_5jd3j5_k_(self, element):
        return -1
    
    def lastIndexOf_5jd3j5_k_(self, element):
        return -1
    
    def iterator_0_k_(self):
        return EmptyIterator_getInstance()
    
    def listIterator_0_k_(self):
        return EmptyIterator_getInstance()
    
    def listIterator_ha5a7z_k_(self, index):
        if not (index == 0):
            raise IndexOutOfBoundsException_init__Create__0(str('Index: ') + str(index))
        
        return EmptyIterator_getInstance()
    
    def subList_27zxwg_k_(self, fromIndex, toIndex):
        if (toIndex == 0) if (fromIndex == 0) else (False):
            return self
        
        raise IndexOutOfBoundsException_init__Create__0(((str('fromIndex: ') + str(fromIndex)) + str(', toIndex: ')) + str(toIndex))
    
    def readResolve_0_k_(self):
        return EmptyList_getInstance()
    

EmptyList_instance = None
def EmptyList_getInstance():
    if EmptyList_instance == None:
        EmptyList()
    
    return EmptyList_instance

class EmptyIterator(ListIterator):
    def __init__(self):
        global EmptyIterator_instance
        EmptyIterator_instance = self
    
    def hasNext_0_k_(self):
        return False
    
    def hasPrevious_0_k_(self):
        return False
    
    def nextIndex_0_k_(self):
        return 0
    
    def previousIndex_0_k_(self):
        return -1
    
    def next_0_k_(self):
        raise NoSuchElementException_init__Create_()
    
    def previous_0_k_(self):
        raise NoSuchElementException_init__Create_()
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

EmptyIterator_instance = None
def EmptyIterator_getInstance():
    if EmptyIterator_instance == None:
        EmptyIterator()
    
    return EmptyIterator_instance

def _get_lastIndex__4(self):
    return (((self._get_size__0_k_() - 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000

def collectionSizeOrDefault(self, default):
    if isInterface(self, Collection):
        tmp = kotlin_collections_Collection_kotlin_Any__(self)._get_size__0_k_()
    elif True:
        tmp = default
    
    return tmp

def removeAll(self, predicate):
    return filterInPlace(self, predicate, True)

def removeAll_0(self, predicate):
    return filterInPlace_0(self, predicate, True)

def filterInPlace(self, predicate, predicateResultToRemove):
    if not isInterface(self, RandomAccess):
        return filterInPlace_0((kotlin_collections_MutableIterable_T_(self)) if (isInterface(self, MutableIterable)) else (THROW_CCE()), predicate, predicateResultToRemove)
    
    writeIndex = 0
    tmp0_iterator = numberRangeToNumber(0, _get_lastIndex__4(self)).iterator_0_k_()
    while tmp0_iterator.hasNext_0_k_():
        readIndex = tmp0_iterator.next_0_k_()
        element = self.get_ha5a7z_k_(readIndex)
        if predicate(element) == predicateResultToRemove:
            continue
        
        if not (writeIndex == readIndex):
            self.set_ddb1qf_k_(writeIndex, element)
            Unit_getInstance()
        
        tmp1 = writeIndex
        writeIndex = (((tmp1 + 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
        Unit_getInstance()
    
    if writeIndex < self._get_size__0_k_():
        tmp2_iterator = downTo(_get_lastIndex__4(self), writeIndex).iterator_0_k_()
        while tmp2_iterator.hasNext_0_k_():
            removeIndex = tmp2_iterator.next_0_k_()
            self.removeAt_ha5a7z_k_(removeIndex)
            Unit_getInstance()
        
        return True
    else:
        return False
    

def filterInPlace_0(self, predicate, predicateResultToRemove):
    result = False
    def complexFunction_x2__While__Expr__0(_this_with):
        while _this_with.hasNext_0_k_():
            if predicate(_this_with.next_0_k_()) == predicateResultToRemove:
                _this_with.remove_sv8swh_k_()
                result = True
            
        
        Unit_getInstance()
    
    with_0(self.iterator_0_k_(), complexFunction_x2__While__Expr__0)
    return result

class Sequence(Any):
    def iterator_0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def contract(builder):
    pass

class ContractBuilder(Any):
    def returns_0_k_(self):
        pass
    
    def returns_wi7j7l_k_(self, value):
        pass
    
    def returnsNotNull_0_k_(self):
        pass
    
    def callsInPlace_x6l8zl_k_(self, _lambda, kind):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

InvocationKind_AT_MOST_ONCE_instance = None
InvocationKind_AT_LEAST_ONCE_instance = None
InvocationKind_EXACTLY_ONCE_instance = None
InvocationKind_UNKNOWN_instance = None
def values_1():
    return (InvocationKind_AT_MOST_ONCE_getInstance(), InvocationKind_AT_LEAST_ONCE_getInstance(), InvocationKind_EXACTLY_ONCE_getInstance(), InvocationKind_UNKNOWN_getInstance())

def valueOf_1(value):
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
    

InvocationKind_entriesInitialized = None
def InvocationKind_initEntries():
    global InvocationKind_entriesInitialized, InvocationKind_AT_MOST_ONCE_instance, InvocationKind_AT_LEAST_ONCE_instance, InvocationKind_EXACTLY_ONCE_instance, InvocationKind_UNKNOWN_instance
    if InvocationKind_entriesInitialized:
        return Unit_getInstance()
    
    InvocationKind_entriesInitialized = True
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    InvocationKind_AT_MOST_ONCE_instance = Unit_getInstance()
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    InvocationKind_AT_LEAST_ONCE_instance = Unit_getInstance()
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    InvocationKind_EXACTLY_ONCE_instance = Unit_getInstance()
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    InvocationKind_UNKNOWN_instance = Unit_getInstance()

class InvocationKind(Enum):
    def __init__(self):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    
    def _get_name__0_k_(self):
        pass
    
    def _get_ordinal__0_k_(self):
        pass
    
    def compareTo_qsy1jz_k_(self, other):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class ExperimentalContracts(Annotation):
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

class Effect:
    pass

class CallsInPlace(Effect):
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class SimpleEffect:
    pass

class Returns(SimpleEffect):
    def implies_vcj5fe_k_(self, booleanExpression):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class ReturnsNotNull(SimpleEffect):
    def implies_vcj5fe_k_(self, booleanExpression):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class Effect(Any):
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class SimpleEffect(Effect):
    def implies_vcj5fe_k_(self, booleanExpression):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class ConditionalEffect(Effect):
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class Continuation(Any):
    def _get_context__0_k_(self):
        pass
    
    def resumeWith_bnunh2_k_(self, result):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def Continuation_0(context, resumeWith):
    return _no_name_provided_()

def resumeWithException(self, exception):
    return self.resumeWith_bnunh2_k_(Companion_getInstance_2().failure_ml8yr4_k_(exception))

def resume(self, value):
    return self.resumeWith_bnunh2_k_(Companion_getInstance_2().success_o91zl1_k_(value))

def _get_coroutineContext_():
    raise NotImplementedError('Implemented as intrinsic')

class _no_name_provided_(Continuation):
    def __init__(self):
        pass
    
    def _get_context__0_k_(self):
        return context
    
    def resumeWith_bnunh2_k_(self, result):
        return resumeWith(boxIntrinsic(result))
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class Key_0:
    pass

class Key(Key_0):
    def __init__(self):
        global Key_instance
        Key_instance = self
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

Key_instance = None
def Key_getInstance():
    if Key_instance == None:
        Key()
    
    return Key_instance

class Element:
    pass

class ContinuationInterceptor(Element):
    def interceptContinuation_x4ijla_k_(self, continuation):
        pass
    
    def releaseInterceptedContinuation_h7c6yl_k_(self, continuation):
        pass
    
    def get_9uvjra_k_(self, key):
        if isinstance(key, AbstractCoroutineContextKey):
            if kotlin_coroutines_AbstractCoroutineContextKey_____(key).isSubKey_djuxjq_k_(self._get_key__0_k_()):
                tmp = kotlin_coroutines_AbstractCoroutineContextKey_____(key).tryCast_k332zt_k_(self)
                tmp = (E(tmp)) if ((isInterface(tmp, Element)) if (not (tmp == None)) else (False)) else (None)
            else:
                tmp = None
            
            return tmp
        
        if Key_getInstance() is key:
            tmp = (E(self)) if (isInterface(self, Element)) else (THROW_CCE())
        else:
            tmp = None
        
        return tmp
    
    def minusKey_djuxjq_k_(self, key):
        if isinstance(key, AbstractCoroutineContextKey):
            return (EmptyCoroutineContext_getInstance()) if ((not (kotlin_coroutines_AbstractCoroutineContextKey_out_kotlin_coroutines_Element_out_kotlin_coroutines_Element_(key).tryCast_k332zt_k_(self) == None)) if (kotlin_coroutines_AbstractCoroutineContextKey_out_kotlin_coroutines_Element_out_kotlin_coroutines_Element_(key).isSubKey_djuxjq_k_(self._get_key__0_k_())) else (False)) else (self)
        
        return (EmptyCoroutineContext_getInstance()) if (Key_getInstance() is key) else (self)
    
    def _get_key__0_k_(self):
        pass
    
    def fold_cq605b_k_(self, initial, operation):
        pass
    
    def plus_d7pszg_k_(self, context):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class Key_0(Any):
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class CoroutineContext:
    pass

class Element(CoroutineContext):
    def _get_key__0_k_(self):
        pass
    
    def get_9uvjra_k_(self, key):
        if self._get_key__0_k_() == key:
            tmp = (E(self)) if (isInterface(self, Element)) else (THROW_CCE())
        else:
            tmp = None
        
        return tmp
    
    def fold_cq605b_k_(self, initial, operation):
        return operation(initial, self)
    
    def minusKey_djuxjq_k_(self, key):
        return (EmptyCoroutineContext_getInstance()) if (self._get_key__0_k_() == key) else (self)
    
    def plus_d7pszg_k_(self, context):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class CoroutineContext(Any):
    def get_9uvjra_k_(self, key):
        pass
    
    def fold_cq605b_k_(self, initial, operation):
        pass
    
    def plus_d7pszg_k_(self, context):
        def complexFunction_x4__Assign__Expr__If__Return__0(acc, element):
            removed = acc.minusKey_djuxjq_k_(element._get_key__0_k_())
            Unit_getInstance()
            if removed is EmptyCoroutineContext_getInstance():
                tmp = element
            else:
                interceptor = removed.get_9uvjra_k_(Key_getInstance())
                if interceptor == None:
                    tmp = CombinedContext(removed, element)
                else:
                    left = removed.minusKey_djuxjq_k_(Key_getInstance())
                    tmp = (CombinedContext(element, interceptor)) if (left is EmptyCoroutineContext_getInstance()) else (CombinedContext(CombinedContext(left, element), interceptor))
                
                tmp = tmp
            
            return tmp
        
        return (self) if (context is EmptyCoroutineContext_getInstance()) else (context.fold_cq605b_k_(self, complexFunction_x4__Assign__Expr__If__Return__0))
    
    def minusKey_djuxjq_k_(self, key):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class EmptyCoroutineContext(CoroutineContext, Serializable):
    def __init__(self):
        global EmptyCoroutineContext_instance
        EmptyCoroutineContext_instance = self
        self.serialVersionUID = 0
    
    def _get_serialVersionUID__0_k_(self):
        return self.serialVersionUID
    
    def readResolve_0_k_(self):
        return EmptyCoroutineContext_getInstance()
    
    def get_9uvjra_k_(self, key):
        return None
    
    def fold_cq605b_k_(self, initial, operation):
        return initial
    
    def plus_d7pszg_k_(self, context):
        return context
    
    def minusKey_djuxjq_k_(self, key):
        return self
    
    def hashCode(self):
        return 0
    
    def toString(self):
        return 'EmptyCoroutineContext'
    
    def equals(self, other):
        pass
    

EmptyCoroutineContext_instance = None
def EmptyCoroutineContext_getInstance():
    if EmptyCoroutineContext_instance == None:
        EmptyCoroutineContext()
    
    return EmptyCoroutineContext_instance

class Companion_1(Any):
    def __init__(self):
        global Companion_instance
        Companion_instance = self
        self.serialVersionUID = 0
    
    def _get_serialVersionUID__0_k_(self):
        return self.serialVersionUID
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

Companion_instance = None
def Companion_getInstance_0():
    if Companion_instance == None:
        Companion_1()
    
    return Companion_instance

class Serialized(Serializable):
    def __init__(self, elements):
        Companion_getInstance_0()
        self.elements = elements
    
    def _get_elements__0_k_(self):
        return self.elements
    
    def readResolve_0_k_(self):
        return fold(self._get_elements__0_k_(), EmptyCoroutineContext_getInstance(), visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrFunctionReferenceImpl)
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class CombinedContext(CoroutineContext, Serializable):
    def __init__(self, left, element):
        self.left = left
        self.element = element
    
    def _get_left__0_k_(self):
        return self.left
    
    def _get_element__0_k_(self):
        return self.element
    
    def get_9uvjra_k_(self, key):
        cur = self
        while True:
            tmp0_safe_receiver = cur._get_element__0_k_().get_9uvjra_k_(key)
            if tmp0_safe_receiver == None:
                None
            else:
                visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCallImpl
            
            Unit_getInstance()
            next = cur._get_left__0_k_()
            if isinstance(next, CombinedContext):
                cur = kotlin_coroutines_CombinedContext(next)
            elif True:
                return next.get_9uvjra_k_(key)
            
        
    
    def fold_cq605b_k_(self, initial, operation):
        return operation(self._get_left__0_k_().fold_cq605b_k_(initial, operation), self._get_element__0_k_())
    
    def minusKey_djuxjq_k_(self, key):
        tmp0_safe_receiver = self._get_element__0_k_().get_9uvjra_k_(key)
        if tmp0_safe_receiver == None:
            None
        else:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCallImpl
        
        Unit_getInstance()
        newLeft = self._get_left__0_k_().minusKey_djuxjq_k_(key)
        return (self) if (newLeft is self._get_left__0_k_()) else ((self._get_element__0_k_()) if (newLeft is EmptyCoroutineContext_getInstance()) else (CombinedContext(newLeft, self._get_element__0_k_())))
    
    def size_0_k_(self):
        cur = self
        size = 2
        while True:
            tmp = cur._get_left__0_k_()
            tmp0_elvis_lhs = (kotlin_coroutines_CombinedContext(tmp)) if (isinstance(tmp, CombinedContext)) else (None)
            if tmp0_elvis_lhs == None:
                return size
            else:
                tmp = tmp0_elvis_lhs
            
            cur = tmp
            tmp1 = size
            size = (((tmp1 + 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
            Unit_getInstance()
        
    
    def contains_k332zt_k_(self, element):
        return self.get_9uvjra_k_(element._get_key__0_k_()) == element
    
    def containsAll_ewoovv_k_(self, context):
        cur = context
        while True:
            if not self.contains_k332zt_k_(cur._get_element__0_k_()):
                return False
            
            next = cur._get_left__0_k_()
            if isinstance(next, CombinedContext):
                cur = kotlin_coroutines_CombinedContext(next)
            elif True:
                return self.contains_k332zt_k_((kotlin_coroutines_Element(next)) if (isInterface(next, Element)) else (THROW_CCE()))
            
        
    
    def equals(self, other):
        if self is other:
            tmp = True
        else:
            if isinstance(other, CombinedContext):
                tmp = kotlin_coroutines_CombinedContext(other).size_0_k_() == self.size_0_k_()
            elif True:
                tmp = False
            
            if tmp:
                tmp = kotlin_coroutines_CombinedContext(other).containsAll_ewoovv_k_(self)
            elif True:
                tmp = False
            
            tmp = tmp
        
        return tmp
    
    def hashCode(self):
        return (((hashCode(self._get_left__0_k_()) + hashCode(self._get_element__0_k_())) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
    
    def toString(self):
        return ('[' + self.fold_cq605b_k_('', lambda acc, element: (toString_0(element)) if (isEmpty(acc)) else ((str(acc) + str(', ')) + str(element)))) + ']'
    
    def writeReplace_0_k_(self):
        n = self.size_0_k_()
        elements = arrayOfNulls(n)
        index = 0
        def complexFunction_x3__Assign__Assign__Expr__0(_anonymous_parameter_0_, element):
            tmp0 = index
            index = (((tmp0 + 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
            elements.__setitem__(tmp0, element)
        
        self.fold_cq605b_k_(Unit_getInstance(), complexFunction_x3__Assign__Assign__Expr__0)
        check(index == n)
        return Serialized((kotlin_Array_kotlin_coroutines_CoroutineContext_(elements)) if (isArray(elements)) else (THROW_CCE()))
    
    def plus_d7pszg_k_(self, context):
        pass
    

class AbstractCoroutineContextKey(Key_0):
    def __init__(self, baseKey, safeCast):
        self.safeCast = safeCast
        tmp = self
        if isinstance(baseKey, AbstractCoroutineContextKey):
            tmp = kotlin_coroutines_AbstractCoroutineContextKey_____(baseKey)._get_topmostKey__0_k_()
        elif True:
            tmp = baseKey
        
        tmp.topmostKey = tmp
    
    def _get_safeCast__0_k_(self):
        return self.safeCast
    
    def _get_topmostKey__0_k_(self):
        return self.topmostKey
    
    def tryCast_k332zt_k_(self, element):
        return self._get_safeCast__0_k_()(element)
    
    def isSubKey_djuxjq_k_(self, key):
        return (True) if (key is self) else (self._get_topmostKey__0_k_() is key)
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def _get_COROUTINE_SUSPENDED_():
    return visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrGetEnumValueImpl

CoroutineSingletons_COROUTINE_SUSPENDED_instance = None
CoroutineSingletons_UNDECIDED_instance = None
CoroutineSingletons_RESUMED_instance = None
def values_2():
    return (CoroutineSingletons_COROUTINE_SUSPENDED_getInstance(), CoroutineSingletons_UNDECIDED_getInstance(), CoroutineSingletons_RESUMED_getInstance())

def valueOf_2(value):
    if 'COROUTINE_SUSPENDED' == value:
        return CoroutineSingletons_COROUTINE_SUSPENDED_getInstance()
    elif 'UNDECIDED' == value:
        return CoroutineSingletons_UNDECIDED_getInstance()
    elif 'RESUMED' == value:
        return CoroutineSingletons_RESUMED_getInstance()
    else:
        CoroutineSingletons_initEntries()
        THROW_ISE()
    

CoroutineSingletons_entriesInitialized = None
def CoroutineSingletons_initEntries():
    global CoroutineSingletons_entriesInitialized, CoroutineSingletons_COROUTINE_SUSPENDED_instance, CoroutineSingletons_UNDECIDED_instance, CoroutineSingletons_RESUMED_instance
    if CoroutineSingletons_entriesInitialized:
        return Unit_getInstance()
    
    CoroutineSingletons_entriesInitialized = True
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    CoroutineSingletons_COROUTINE_SUSPENDED_instance = Unit_getInstance()
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    CoroutineSingletons_UNDECIDED_instance = Unit_getInstance()
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    CoroutineSingletons_RESUMED_instance = Unit_getInstance()

class CoroutineSingletons(Enum):
    def __init__(self):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    
    def _get_name__0_k_(self):
        pass
    
    def _get_ordinal__0_k_(self):
        pass
    
    def compareTo_w8y6n9_k_(self, other):
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

def _and(self, other):
    return (((self & other) + 0x8000) & 0xffff) - 0x8000

def _or(self, other):
    return (((self | other) + 0x8000) & 0xffff) - 0x8000

def xor(self, other):
    return (((self ^ other) + 0x8000) & 0xffff) - 0x8000

def inv(self):
    return ((~self + 0x8000) & 0xffff) - 0x8000

def and_0(self, other):
    return (((self & other) + 0x80) & 0xff) - 0x80

def or_0(self, other):
    return (((self | other) + 0x80) & 0xff) - 0x80

def xor_0(self, other):
    return (((self ^ other) + 0x80) & 0xff) - 0x80

def inv_0(self):
    return ((~self + 0x80) & 0xff) - 0x80

class ExperimentalTypeInference(Annotation):
    def __init__(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class RequireKotlin(Annotation):
    def __init__(self, version, message, level, versionKind, errorCode):
        pass
    
    def _get_version__0_k_(self):
        return self.version
    
    def _get_message__0_k_(self):
        return self.message
    
    def _get_level__0_k_(self):
        return self.level
    
    def _get_versionKind__0_k_(self):
        return self.versionKind
    
    def _get_errorCode__0_k_(self):
        return self.errorCode
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

RequireKotlinVersionKind_LANGUAGE_VERSION_instance = None
RequireKotlinVersionKind_COMPILER_VERSION_instance = None
RequireKotlinVersionKind_API_VERSION_instance = None
def values_3():
    return (RequireKotlinVersionKind_LANGUAGE_VERSION_getInstance(), RequireKotlinVersionKind_COMPILER_VERSION_getInstance(), RequireKotlinVersionKind_API_VERSION_getInstance())

def valueOf_3(value):
    if 'LANGUAGE_VERSION' == value:
        return RequireKotlinVersionKind_LANGUAGE_VERSION_getInstance()
    elif 'COMPILER_VERSION' == value:
        return RequireKotlinVersionKind_COMPILER_VERSION_getInstance()
    elif 'API_VERSION' == value:
        return RequireKotlinVersionKind_API_VERSION_getInstance()
    else:
        RequireKotlinVersionKind_initEntries()
        THROW_ISE()
    

RequireKotlinVersionKind_entriesInitialized = None
def RequireKotlinVersionKind_initEntries():
    global RequireKotlinVersionKind_entriesInitialized, RequireKotlinVersionKind_LANGUAGE_VERSION_instance, RequireKotlinVersionKind_COMPILER_VERSION_instance, RequireKotlinVersionKind_API_VERSION_instance
    if RequireKotlinVersionKind_entriesInitialized:
        return Unit_getInstance()
    
    RequireKotlinVersionKind_entriesInitialized = True
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    RequireKotlinVersionKind_LANGUAGE_VERSION_instance = Unit_getInstance()
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    RequireKotlinVersionKind_COMPILER_VERSION_instance = Unit_getInstance()
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    RequireKotlinVersionKind_API_VERSION_instance = Unit_getInstance()

class RequireKotlinVersionKind(Enum):
    def __init__(self):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    
    def _get_name__0_k_(self):
        pass
    
    def _get_ordinal__0_k_(self):
        pass
    
    def compareTo_rr53gp_k_(self, other):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class InlineOnly(Annotation):
    def __init__(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class NoInfer(Annotation):
    def __init__(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class DynamicExtension(Annotation):
    def __init__(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class ContractsDsl(Annotation):
    def __init__(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class OnlyInputTypes(Annotation):
    def __init__(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class HidesMembers(Annotation):
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

class KClassifier(Any):
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class KTypeParameter(KClassifier):
    def _get_name__0_k_(self):
        pass
    
    def _get_upperBounds__0_k_(self):
        pass
    
    def _get_variance__0_k_(self):
        pass
    
    def _get_isReified__0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class Companion_2(Any):
    def __init__(self):
        global Companion_instance
        Companion_instance = self
        self.star = KTypeProjection(None, None)
    
    def _get_star__0_k_(self):
        return self.star
    
    def _get_STAR__0_k_(self):
        return self._get_star__0_k_()
    
    def invariant_573d5y_k_(self, type):
        return KTypeProjection(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrGetEnumValueImpl, type)
    
    def contravariant_573d5y_k_(self, type):
        return KTypeProjection(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrGetEnumValueImpl, type)
    
    def covariant_573d5y_k_(self, type):
        return KTypeProjection(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrGetEnumValueImpl, type)
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

Companion_instance = None
def Companion_getInstance_1():
    if Companion_instance == None:
        Companion_2()
    
    return Companion_instance

class KTypeProjection(Any):
    def __init__(self, variance, type):
        Companion_getInstance_1()
        self.variance = variance
        self.type = type
        require_0(self._get_variance__0_k_() == None == self._get_type__0_k_() == None, lambda : ('Star projection must have no type specified.') if (self._get_variance__0_k_() == None) else ((str('The projection variance ') + str(self._get_variance__0_k_())) + str(' requires type to be specified.')))
    
    def _get_variance__0_k_(self):
        return self.variance
    
    def _get_type__0_k_(self):
        return self.type
    
    def toString(self):
        tmp0_subject = self._get_variance__0_k_()
        return ('*') if (tmp0_subject == None) else ((toString(self._get_type__0_k_())) if (tmp0_subject == visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrGetEnumValueImpl) else ((str('in ') + str(self._get_type__0_k_())) if (tmp0_subject == visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrGetEnumValueImpl) else ((str('out ') + str(self._get_type__0_k_())) if (tmp0_subject == visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrGetEnumValueImpl) else (noWhenBranchMatchedException()))))
    
    def component1_0_k_(self):
        return self.variance
    
    def component2_0_k_(self):
        return self.type
    
    def copy_fey4rp_k_(self, variance, type):
        return KTypeProjection(variance, type)
    
    def hashCode(self):
        result = (0) if (self.variance == None) else (self.variance.hashCode())
        result = (((imul(result, 31) + ((0) if (self.type == None) else (hashCode(self.type)))) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
        return result
    
    def equals(self, other):
        if self is other:
            return True
        
        if not isinstance(other, KTypeProjection):
            return False
        
        tmp0_other_with_cast = (kotlin_reflect_KTypeProjection(other)) if (isinstance(other, KTypeProjection)) else (THROW_CCE())
        if not (self.variance == tmp0_other_with_cast.variance):
            return False
        
        if not (self.type == tmp0_other_with_cast.type):
            return False
        
        return True
    

KVariance_INVARIANT_instance = None
KVariance_IN_instance = None
KVariance_OUT_instance = None
def values_4():
    return (KVariance_INVARIANT_getInstance(), KVariance_IN_getInstance(), KVariance_OUT_getInstance())

def valueOf_4(value):
    if 'INVARIANT' == value:
        return KVariance_INVARIANT_getInstance()
    elif 'IN' == value:
        return KVariance_IN_getInstance()
    elif 'OUT' == value:
        return KVariance_OUT_getInstance()
    else:
        KVariance_initEntries()
        THROW_ISE()
    

KVariance_entriesInitialized = None
def KVariance_initEntries():
    global KVariance_entriesInitialized, KVariance_INVARIANT_instance, KVariance_IN_instance, KVariance_OUT_instance
    if KVariance_entriesInitialized:
        return Unit_getInstance()
    
    KVariance_entriesInitialized = True
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    KVariance_INVARIANT_instance = Unit_getInstance()
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    KVariance_IN_instance = Unit_getInstance()
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    KVariance_OUT_instance = Unit_getInstance()

class KVariance(Enum):
    def __init__(self):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    
    def _get_name__0_k_(self):
        pass
    
    def _get_ordinal__0_k_(self):
        pass
    
    def compareTo_93y5y5_k_(self, other):
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

def appendElement(self, element, transform):
    if not (transform == None):
        self.append_v1o70a_k_(transform(element))
        Unit_getInstance()
    elif (True) if (element == None) else (isCharSequence(element)):
        self.append_v1o70a_k_(kotlin_CharSequence_(element))
        Unit_getInstance()
    elif isinstance(element, Char_0):
        self.append_wi8o78_k_(kotlin_Char(element))
        Unit_getInstance()
    elif True:
        self.append_v1o70a_k_(toString(element))
        Unit_getInstance()
    

def isEmpty(self):
    return charSequenceLength(self) == 0

def _get_lastIndex__5(self):
    return (((charSequenceLength(self) - 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000

def _get_UNDEFINED_RESULT_():
    return UNDEFINED_RESULT

UNDEFINED_RESULT = None
def check(value):
    def complexFunction_x2__Expr__Expr__0(_this_contract):
        _this_contract.returns_0_k_().implies_vcj5fe_k_(value)
        Unit_getInstance()
    
    contract(complexFunction_x2__Expr__Expr__0)
    check_0(value, lambda : 'Check failed.')

def check_0(value, lazyMessage):
    def complexFunction_x2__Expr__Expr__0(_this_contract):
        _this_contract.returns_0_k_().implies_vcj5fe_k_(value)
        Unit_getInstance()
    
    contract(complexFunction_x2__Expr__Expr__0)
    if not value:
        message = lazyMessage()
        raise IllegalStateException_init__Create__0(toString_0(message))
    

def error(message):
    raise IllegalStateException_init__Create__0(toString_0(message))

def require_0(value, lazyMessage):
    def complexFunction_x2__Expr__Expr__0(_this_contract):
        _this_contract.returns_0_k_().implies_vcj5fe_k_(value)
        Unit_getInstance()
    
    contract(complexFunction_x2__Expr__Expr__0)
    if not value:
        message = lazyMessage()
        raise IllegalArgumentException_init__Create__0(toString_0(message))
    

def _Result___init__impl_(value):
    return kotlin_Result_T_(value)

def _Result___get_value__impl_(this):
    return this.value

def _Result___get_isSuccess__impl_(this):
    tmp = _Result___get_value__impl_(this)
    return not isinstance(tmp, Failure)

def _Result___get_isFailure__impl_(this):
    tmp = _Result___get_value__impl_(this)
    return isinstance(tmp, Failure)

def Result__getOrNull_impl(this):
    if _Result___get_isFailure__impl_(this):
        tmp = None
    else:
        tmp = _Result___get_value__impl_(this)
        tmp = (T(tmp)) if ((True) if (tmp == None) else (isObject(tmp))) else (THROW_CCE())
    
    return tmp

def Result__exceptionOrNull_impl(this):
    tmp0_subject = _Result___get_value__impl_(this)
    if isinstance(tmp0_subject, Failure):
        tmp = kotlin_Failure(_Result___get_value__impl_(this))._get_exception__0_k_()
    elif True:
        tmp = None
    
    return tmp

def Result__toString_impl(this):
    tmp0_subject = _Result___get_value__impl_(this)
    if isinstance(tmp0_subject, Failure):
        tmp = toString_0(kotlin_Failure(_Result___get_value__impl_(this)))
    elif True:
        tmp = (str('Success(') + str(_Result___get_value__impl_(this))) + str(')')
    
    return tmp

class Companion_3(Any):
    def __init__(self):
        global Companion_instance
        Companion_instance = self
    
    def success_o91zl1_k_(self, value):
        return _Result___init__impl_(value)
    
    def failure_ml8yr4_k_(self, exception):
        return _Result___init__impl_(createFailure(exception))
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

Companion_instance = None
def Companion_getInstance_2():
    if Companion_instance == None:
        Companion_3()
    
    return Companion_instance

class Failure(Serializable):
    def __init__(self, exception):
        self.exception = exception
    
    def _get_exception__0_k_(self):
        return self.exception
    
    def equals(self, other):
        if isinstance(other, Failure):
            tmp = self._get_exception__0_k_() == kotlin_Failure(other)._get_exception__0_k_()
        elif True:
            tmp = False
        
        return tmp
    
    def hashCode(self):
        return hashCode(self._get_exception__0_k_())
    
    def toString(self):
        return (str('Failure(') + str(self._get_exception__0_k_())) + str(')')
    

def Result__hashCode_impl(this):
    return (0) if (this.value == None) else (hashCode(this.value))

def Result__equals_impl(this, other):
    if not isinstance(other, Result):
        return False
    
    tmp0_other_with_cast = (unboxIntrinsic(other)) if (isinstance(other, Result)) else (THROW_CCE())
    if not (this.value == tmp0_other_with_cast.value):
        return False
    
    return True

class Result(Serializable):
    def __init__(self, value):
        Companion_getInstance_2()
        self.value = value
    
    def toString(self):
        return Result__toString_impl(unboxIntrinsic(self))
    
    def hashCode(self):
        return Result__hashCode_impl(unboxIntrinsic(self))
    
    def equals(self, other):
        return Result__equals_impl(unboxIntrinsic(self), other)
    

def createFailure(exception):
    return Failure(exception)

def getOrThrow(self):
    throwOnFailure(self)
    tmp = _Result___get_value__impl_(self)
    return (T(tmp)) if ((True) if (tmp == None) else (isObject(tmp))) else (THROW_CCE())

def throwOnFailure(self):
    tmp = _Result___get_value__impl_(self)
    if isinstance(tmp, Failure):
        raise kotlin_Failure(_Result___get_value__impl_(self))._get_exception__0_k_()
    

def run(block):
    def complexFunction_x2__Expr__Expr__0(_this_contract):
        _this_contract.callsInPlace_x6l8zl_k_(block, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrGetEnumValueImpl)
        Unit_getInstance()
    
    contract(complexFunction_x2__Expr__Expr__0)
    return block()

def TODO():
    raise NotImplementedError(translateCallArguments_0)

class Error_0:
    pass

class NotImplementedError(Error_0):
    def __init__(self, message):
        Error_init__Init__0(message, self)
        captureStack(self, _init_)
    
    def _get_message__0_k_(self):
        pass
    
    def _get_cause__0_k_(self):
        pass
    
    def toString(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    

def let_0(self, block):
    def complexFunction_x2__Expr__Expr__0(_this_contract):
        _this_contract.callsInPlace_x6l8zl_k_(block, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrGetEnumValueImpl)
        Unit_getInstance()
    
    contract(complexFunction_x2__Expr__Expr__0)
    return block(self)

def apply(self, block):
    def complexFunction_x2__Expr__Expr__0(_this_contract):
        _this_contract.callsInPlace_x6l8zl_k_(block, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrGetEnumValueImpl)
        Unit_getInstance()
    
    contract(complexFunction_x2__Expr__Expr__0)
    block(self)
    return self

def repeat(times, action):
    def complexFunction_x2__Expr__Expr__0(_this_contract):
        _this_contract.callsInPlace_x6l8zl_k_(action, translateCallArguments_1)
        Unit_getInstance()
    
    contract(complexFunction_x2__Expr__Expr__0)
    tmp0_iterator = until(0, times).iterator_0_k_()
    while tmp0_iterator.hasNext_0_k_():
        index = tmp0_iterator.next_0_k_()
        action(index)
    

def with_0(receiver, block):
    def complexFunction_x2__Expr__Expr__0(_this_contract):
        _this_contract.callsInPlace_x6l8zl_k_(block, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrGetEnumValueImpl)
        Unit_getInstance()
    
    contract(complexFunction_x2__Expr__Expr__0)
    return block(receiver)

def also(self, block):
    def complexFunction_x2__Expr__Expr__0(_this_contract):
        _this_contract.callsInPlace_x6l8zl_k_(block, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrGetEnumValueImpl)
        Unit_getInstance()
    
    contract(complexFunction_x2__Expr__Expr__0)
    block(self)
    return self

def run_0(self, block):
    def complexFunction_x2__Expr__Expr__0(_this_contract):
        _this_contract.callsInPlace_x6l8zl_k_(block, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrGetEnumValueImpl)
        Unit_getInstance()
    
    contract(complexFunction_x2__Expr__Expr__0)
    return block(self)

def _UByte___init__impl_(data):
    return kotlin_UByte(data)

def _UByte___get_data__impl_(this):
    return this.data

class Companion_4(Any):
    def __init__(self):
        global Companion_instance
        Companion_instance = self
        self.MIN_VALUE = _UByte___init__impl_(0)
        self.MAX_VALUE = _UByte___init__impl_(-1)
        self.SIZE_BYTES = 1
        self.SIZE_BITS = 8
    
    def _get_MIN_VALUE__sh428i_k_(self):
        return self.MIN_VALUE
    
    def _get_MAX_VALUE__sh428i_k_(self):
        return self.MAX_VALUE
    
    def _get_SIZE_BYTES__0_k_(self):
        return self.SIZE_BYTES
    
    def _get_SIZE_BITS__0_k_(self):
        return self.SIZE_BITS
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

Companion_instance = None
def Companion_getInstance_3():
    if Companion_instance == None:
        Companion_4()
    
    return Companion_instance

def UByte__compareTo_impl(this, other):
    return compareTo_0(UByte__toInt_impl(this), UByte__toInt_impl(other))

def UByte__compareTo_impl_0(this, other):
    return compareTo_0(UByte__toInt_impl(this), UShort__toInt_impl(other))

def UByte__compareTo_impl_1(this, other):
    return UInt__compareTo_impl_1(UByte__toUInt_impl(this), other)

def UByte__compareTo_impl_2(this, other):
    return ULong__compareTo_impl_2(UByte__toULong_impl(this), other)

def UByte__plus_impl(this, other):
    return UInt__plus_impl_1(UByte__toUInt_impl(this), UByte__toUInt_impl(other))

def UByte__plus_impl_0(this, other):
    return UInt__plus_impl_1(UByte__toUInt_impl(this), UShort__toUInt_impl(other))

def UByte__plus_impl_1(this, other):
    return UInt__plus_impl_1(UByte__toUInt_impl(this), other)

def UByte__plus_impl_2(this, other):
    return ULong__plus_impl_2(UByte__toULong_impl(this), other)

def UByte__minus_impl(this, other):
    return UInt__minus_impl_1(UByte__toUInt_impl(this), UByte__toUInt_impl(other))

def UByte__minus_impl_0(this, other):
    return UInt__minus_impl_1(UByte__toUInt_impl(this), UShort__toUInt_impl(other))

def UByte__minus_impl_1(this, other):
    return UInt__minus_impl_1(UByte__toUInt_impl(this), other)

def UByte__minus_impl_2(this, other):
    return ULong__minus_impl_2(UByte__toULong_impl(this), other)

def UByte__times_impl(this, other):
    return UInt__times_impl_1(UByte__toUInt_impl(this), UByte__toUInt_impl(other))

def UByte__times_impl_0(this, other):
    return UInt__times_impl_1(UByte__toUInt_impl(this), UShort__toUInt_impl(other))

def UByte__times_impl_1(this, other):
    return UInt__times_impl_1(UByte__toUInt_impl(this), other)

def UByte__times_impl_2(this, other):
    return ULong__times_impl_2(UByte__toULong_impl(this), other)

def UByte__div_impl(this, other):
    return UInt__div_impl_1(UByte__toUInt_impl(this), UByte__toUInt_impl(other))

def UByte__div_impl_0(this, other):
    return UInt__div_impl_1(UByte__toUInt_impl(this), UShort__toUInt_impl(other))

def UByte__div_impl_1(this, other):
    return UInt__div_impl_1(UByte__toUInt_impl(this), other)

def UByte__div_impl_2(this, other):
    return ULong__div_impl_2(UByte__toULong_impl(this), other)

def UByte__rem_impl(this, other):
    return UInt__rem_impl_1(UByte__toUInt_impl(this), UByte__toUInt_impl(other))

def UByte__rem_impl_0(this, other):
    return UInt__rem_impl_1(UByte__toUInt_impl(this), UShort__toUInt_impl(other))

def UByte__rem_impl_1(this, other):
    return UInt__rem_impl_1(UByte__toUInt_impl(this), other)

def UByte__rem_impl_2(this, other):
    return ULong__rem_impl_2(UByte__toULong_impl(this), other)

def UByte__floorDiv_impl(this, other):
    return UInt__floorDiv_impl_1(UByte__toUInt_impl(this), UByte__toUInt_impl(other))

def UByte__floorDiv_impl_0(this, other):
    return UInt__floorDiv_impl_1(UByte__toUInt_impl(this), UShort__toUInt_impl(other))

def UByte__floorDiv_impl_1(this, other):
    return UInt__floorDiv_impl_1(UByte__toUInt_impl(this), other)

def UByte__floorDiv_impl_2(this, other):
    return ULong__floorDiv_impl_2(UByte__toULong_impl(this), other)

def UByte__mod_impl(this, other):
    return UInt__toUByte_impl(UInt__mod_impl_1(UByte__toUInt_impl(this), UByte__toUInt_impl(other)))

def UByte__mod_impl_0(this, other):
    return UInt__toUShort_impl(UInt__mod_impl_1(UByte__toUInt_impl(this), UShort__toUInt_impl(other)))

def UByte__mod_impl_1(this, other):
    return UInt__mod_impl_1(UByte__toUInt_impl(this), other)

def UByte__mod_impl_2(this, other):
    return ULong__mod_impl_2(UByte__toULong_impl(this), other)

def UByte__inc_impl(this):
    return _UByte___init__impl_((((_UByte___get_data__impl_(this) + 1) + 0x80) & 0xff) - 0x80)

def UByte__dec_impl(this):
    return _UByte___init__impl_((((_UByte___get_data__impl_(this) - 1) + 0x80) & 0xff) - 0x80)

def UByte__rangeTo_impl(this, other):
    return UIntRange(UByte__toUInt_impl(this), UByte__toUInt_impl(other))

def UByte__and_impl(this, other):
    return _UByte___init__impl_(and_0(_UByte___get_data__impl_(this), _UByte___get_data__impl_(other)))

def UByte__or_impl(this, other):
    return _UByte___init__impl_(or_0(_UByte___get_data__impl_(this), _UByte___get_data__impl_(other)))

def UByte__xor_impl(this, other):
    return _UByte___init__impl_(xor_0(_UByte___get_data__impl_(this), _UByte___get_data__impl_(other)))

def UByte__inv_impl(this):
    return _UByte___init__impl_(inv_0(_UByte___get_data__impl_(this)))

def UByte__toByte_impl(this):
    return _UByte___get_data__impl_(this)

def UByte__toShort_impl(this):
    return _and(_UByte___get_data__impl_(this), 255)

def UByte__toInt_impl(this):
    return _UByte___get_data__impl_(this) & 255

def UByte__toLong_impl(this):
    return (((_UByte___get_data__impl_(this) & 255) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000

def UByte__toUByte_impl(this):
    return this

def UByte__toUShort_impl(this):
    return _UShort___init__impl_(_and(_UByte___get_data__impl_(this), 255))

def UByte__toUInt_impl(this):
    return _UInt___init__impl_(_UByte___get_data__impl_(this) & 255)

def UByte__toULong_impl(this):
    return _ULong___init__impl_((((_UByte___get_data__impl_(this) & 255) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000)

def UByte__toFloat_impl(this):
    return kotlin_Float(UByte__toInt_impl(this))

def UByte__toDouble_impl(this):
    return kotlin_Double(UByte__toInt_impl(this))

def UByte__toString_impl(this):
    return UByte__toInt_impl(this).toString()

def UByte__hashCode_impl(this):
    return this.data

def UByte__equals_impl(this, other):
    if not isinstance(other, UByte):
        return False
    
    tmp0_other_with_cast = (unboxIntrinsic(other)) if (isinstance(other, UByte)) else (THROW_CCE())
    if not (this.data == tmp0_other_with_cast.data):
        return False
    
    return True

class Comparable:
    pass

class UByte(Comparable):
    def __init__(self, data):
        Companion_getInstance_3()
        self.data = data
    
    def compareTo_dj4lnz_k_(self, other):
        return UByte__compareTo_impl(unboxIntrinsic(self), other)
    
    def toString(self):
        return UByte__toString_impl(unboxIntrinsic(self))
    
    def hashCode(self):
        return UByte__hashCode_impl(unboxIntrinsic(self))
    
    def equals(self, other):
        return UByte__equals_impl(unboxIntrinsic(self), other)
    

def toUByte(self):
    return _UByte___init__impl_(((self + 0x80) & 0xff) - 0x80)

def toUByte_0(self):
    return _UByte___init__impl_(((self + 0x80) & 0xff) - 0x80)

def toUByte_1(self):
    return _UByte___init__impl_(((self + 0x80) & 0xff) - 0x80)

def toUByte_2(self):
    return _UByte___init__impl_(self)

def _UByteArray___init__impl_(storage):
    return kotlin_UByteArray(storage)

def _UByteArray___get_storage__impl_(this):
    return this.storage

def _UByteArray___init__impl__0(size):
    tmp = _UByteArray___init__impl_(int8Array(size))
    return tmp

def UByteArray__get_impl(this, index):
    return toUByte_2(_UByteArray___get_storage__impl_(this)[index])

def UByteArray__set_impl(this, index, value):
    _UByteArray___get_storage__impl_(this).__setitem__(index, UByte__toByte_impl(value))

def _UByteArray___get_size__impl_(this):
    return len(_UByteArray___get_storage__impl_(this))

def UByteArray__iterator_impl(this):
    return Iterator(_UByteArray___get_storage__impl_(this))

class UByteIterator:
    pass

class Iterator(UByteIterator):
    def __init__(self, array):
        UByteIterator.__init__(self)
        self.array = array
        self.index = 0
    
    def _get_array__0_k_(self):
        return self.array
    
    def _set_index__majfzk_k_(self, _set___):
        self.index = _set___
    
    def _get_index__0_k_(self):
        return self.index
    
    def hasNext_0_k_(self):
        return self._get_index__0_k_() < len(self._get_array__0_k_())
    
    def nextUByte_sh428i_k_(self):
        if self._get_index__0_k_() < len(self._get_array__0_k_()):
            tmp = self._get_array__0_k_()
            tmp0_this = self
            tmp1 = tmp0_this._get_index__0_k_()
            tmp0_this._set_index__majfzk_k_((((tmp1 + 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
            tmp = toUByte_2(tmp[tmp1])
        else:
            raise NoSuchElementException_init__Create__0(self._get_index__0_k_().toString())
        
        return tmp
    
    def next_sh428i_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def UByteArray__contains_impl(this, element):
    tmp = (boxIntrinsic(element)) if (isObject(boxIntrinsic(element))) else (THROW_CCE())
    if not isinstance(tmp, UByte):
        return False
    
    return contains(_UByteArray___get_storage__impl_(this), UByte__toByte_impl(element))

def UByteArray__containsAll_impl(this, elements):
    def complexFunction_x2__If__Return__0(it):
        if isinstance(it, UByte):
            tmp = contains(_UByteArray___get_storage__impl_(this), UByte__toByte_impl(unboxIntrinsic(it)))
        elif True:
            tmp = False
        
        return tmp
    
    return all((kotlin_collections_Collection___(elements)) if (isInterface(elements, Collection)) else (THROW_CCE()), complexFunction_x2__If__Return__0)

def UByteArray__isEmpty_impl(this):
    return len(_UByteArray___get_storage__impl_(this)) == 0

def UByteArray__toString_impl(this):
    return ((str('UByteArray(') + str('storage=')) + str(toString_0(this.storage))) + str(')')

def UByteArray__hashCode_impl(this):
    return hashCode(this.storage)

def UByteArray__equals_impl(this, other):
    if not isinstance(other, UByteArray):
        return False
    
    tmp0_other_with_cast = (unboxIntrinsic(other)) if (isinstance(other, UByteArray)) else (THROW_CCE())
    if not (this.storage == tmp0_other_with_cast.storage):
        return False
    
    return True

class UByteArray(Collection):
    def __init__(self, storage):
        self.storage = storage
    
    def _get_size__0_k_(self):
        return _UByteArray___get_size__impl_(unboxIntrinsic(self))
    
    def iterator_0_k_(self):
        return UByteArray__iterator_impl(unboxIntrinsic(self))
    
    def contains_dj4lnz_k_(self, element):
        return UByteArray__contains_impl(unboxIntrinsic(self), element)
    
    def containsAll_wji8mv_k_(self, elements):
        return UByteArray__containsAll_impl(unboxIntrinsic(self), elements)
    
    def isEmpty_0_k_(self):
        return UByteArray__isEmpty_impl(unboxIntrinsic(self))
    
    def toString(self):
        return UByteArray__toString_impl(unboxIntrinsic(self))
    
    def hashCode(self):
        return UByteArray__hashCode_impl(unboxIntrinsic(self))
    
    def equals(self, other):
        return UByteArray__equals_impl(unboxIntrinsic(self), other)
    

def _UInt___init__impl_(data):
    return kotlin_UInt(data)

def _UInt___get_data__impl_(this):
    return this.data

class Companion_5(Any):
    def __init__(self):
        global Companion_instance
        Companion_instance = self
        self.MIN_VALUE = _UInt___init__impl_(0)
        self.MAX_VALUE = _UInt___init__impl_(-1)
        self.SIZE_BYTES = 4
        self.SIZE_BITS = 32
    
    def _get_MIN_VALUE__sv9k7v_k_(self):
        return self.MIN_VALUE
    
    def _get_MAX_VALUE__sv9k7v_k_(self):
        return self.MAX_VALUE
    
    def _get_SIZE_BYTES__0_k_(self):
        return self.SIZE_BYTES
    
    def _get_SIZE_BITS__0_k_(self):
        return self.SIZE_BITS
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

Companion_instance = None
def Companion_getInstance_4():
    if Companion_instance == None:
        Companion_5()
    
    return Companion_instance

def UInt__compareTo_impl(this, other):
    return UInt__compareTo_impl_1(this, UByte__toUInt_impl(other))

def UInt__compareTo_impl_0(this, other):
    return UInt__compareTo_impl_1(this, UShort__toUInt_impl(other))

def UInt__compareTo_impl_1(this, other):
    return uintCompare(_UInt___get_data__impl_(this), _UInt___get_data__impl_(other))

def UInt__compareTo_impl_2(this, other):
    return ULong__compareTo_impl_2(UInt__toULong_impl(this), other)

def UInt__plus_impl(this, other):
    return UInt__plus_impl_1(this, UByte__toUInt_impl(other))

def UInt__plus_impl_0(this, other):
    return UInt__plus_impl_1(this, UShort__toUInt_impl(other))

def UInt__plus_impl_1(this, other):
    return _UInt___init__impl_((((_UInt___get_data__impl_(this) + _UInt___get_data__impl_(other)) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)

def UInt__plus_impl_2(this, other):
    return ULong__plus_impl_2(UInt__toULong_impl(this), other)

def UInt__minus_impl(this, other):
    return UInt__minus_impl_1(this, UByte__toUInt_impl(other))

def UInt__minus_impl_0(this, other):
    return UInt__minus_impl_1(this, UShort__toUInt_impl(other))

def UInt__minus_impl_1(this, other):
    return _UInt___init__impl_((((_UInt___get_data__impl_(this) - _UInt___get_data__impl_(other)) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)

def UInt__minus_impl_2(this, other):
    return ULong__minus_impl_2(UInt__toULong_impl(this), other)

def UInt__times_impl(this, other):
    return UInt__times_impl_1(this, UByte__toUInt_impl(other))

def UInt__times_impl_0(this, other):
    return UInt__times_impl_1(this, UShort__toUInt_impl(other))

def UInt__times_impl_1(this, other):
    return _UInt___init__impl_(imul(_UInt___get_data__impl_(this), _UInt___get_data__impl_(other)))

def UInt__times_impl_2(this, other):
    return ULong__times_impl_2(UInt__toULong_impl(this), other)

def UInt__div_impl(this, other):
    return UInt__div_impl_1(this, UByte__toUInt_impl(other))

def UInt__div_impl_0(this, other):
    return UInt__div_impl_1(this, UShort__toUInt_impl(other))

def UInt__div_impl_1(this, other):
    return uintDivide(this, other)

def UInt__div_impl_2(this, other):
    return ULong__div_impl_2(UInt__toULong_impl(this), other)

def UInt__rem_impl(this, other):
    return UInt__rem_impl_1(this, UByte__toUInt_impl(other))

def UInt__rem_impl_0(this, other):
    return UInt__rem_impl_1(this, UShort__toUInt_impl(other))

def UInt__rem_impl_1(this, other):
    return uintRemainder(this, other)

def UInt__rem_impl_2(this, other):
    return ULong__rem_impl_2(UInt__toULong_impl(this), other)

def UInt__floorDiv_impl(this, other):
    return UInt__floorDiv_impl_1(this, UByte__toUInt_impl(other))

def UInt__floorDiv_impl_0(this, other):
    return UInt__floorDiv_impl_1(this, UShort__toUInt_impl(other))

def UInt__floorDiv_impl_1(this, other):
    return UInt__div_impl_1(this, other)

def UInt__floorDiv_impl_2(this, other):
    return ULong__floorDiv_impl_2(UInt__toULong_impl(this), other)

def UInt__mod_impl(this, other):
    return UInt__toUByte_impl(UInt__mod_impl_1(this, UByte__toUInt_impl(other)))

def UInt__mod_impl_0(this, other):
    return UInt__toUShort_impl(UInt__mod_impl_1(this, UShort__toUInt_impl(other)))

def UInt__mod_impl_1(this, other):
    return UInt__rem_impl_1(this, other)

def UInt__mod_impl_2(this, other):
    return ULong__mod_impl_2(UInt__toULong_impl(this), other)

def UInt__inc_impl(this):
    return _UInt___init__impl_((((_UInt___get_data__impl_(this) + 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)

def UInt__dec_impl(this):
    return _UInt___init__impl_((((_UInt___get_data__impl_(this) - 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)

def UInt__rangeTo_impl(this, other):
    return UIntRange(this, other)

def UInt__shl_impl(this, bitCount):
    return _UInt___init__impl_((((_UInt___get_data__impl_(this) << bitCount) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)

def UInt__shr_impl(this, bitCount):
    return _UInt___init__impl_((_UInt___get_data__impl_(this) & 0xffff_ffff) >> bitCount)

def UInt__and_impl(this, other):
    return _UInt___init__impl_(_UInt___get_data__impl_(this) & _UInt___get_data__impl_(other))

def UInt__or_impl(this, other):
    return _UInt___init__impl_(_UInt___get_data__impl_(this) | _UInt___get_data__impl_(other))

def UInt__xor_impl(this, other):
    return _UInt___init__impl_(_UInt___get_data__impl_(this) ^ _UInt___get_data__impl_(other))

def UInt__inv_impl(this):
    return _UInt___init__impl_(~_UInt___get_data__impl_(this))

def UInt__toByte_impl(this):
    return ((_UInt___get_data__impl_(this) + 0x80) & 0xff) - 0x80

def UInt__toShort_impl(this):
    return ((_UInt___get_data__impl_(this) + 0x8000) & 0xffff) - 0x8000

def UInt__toInt_impl(this):
    return _UInt___get_data__impl_(this)

def UInt__toLong_impl(this):
    return (((_UInt___get_data__impl_(this) & 4294967295) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000

def UInt__toUByte_impl(this):
    return toUByte_0(_UInt___get_data__impl_(this))

def UInt__toUShort_impl(this):
    return toUShort(_UInt___get_data__impl_(this))

def UInt__toUInt_impl(this):
    return this

def UInt__toULong_impl(this):
    return _ULong___init__impl_((((_UInt___get_data__impl_(this) & 4294967295) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000)

def UInt__toFloat_impl(this):
    return kotlin_Float(UInt__toDouble_impl(this))

def UInt__toDouble_impl(this):
    return uintToDouble(_UInt___get_data__impl_(this))

def UInt__toString_impl(this):
    return UInt__toLong_impl(this).toString()

def UInt__hashCode_impl(this):
    return this.data

def UInt__equals_impl(this, other):
    if not isinstance(other, UInt):
        return False
    
    tmp0_other_with_cast = (unboxIntrinsic(other)) if (isinstance(other, UInt)) else (THROW_CCE())
    if not (this.data == tmp0_other_with_cast.data):
        return False
    
    return True

class UInt(Comparable):
    def __init__(self, data):
        Companion_getInstance_4()
        self.data = data
    
    def compareTo_wijjag_k_(self, other):
        return UInt__compareTo_impl_1(unboxIntrinsic(self), other)
    
    def toString(self):
        return UInt__toString_impl(unboxIntrinsic(self))
    
    def hashCode(self):
        return UInt__hashCode_impl(unboxIntrinsic(self))
    
    def equals(self, other):
        return UInt__equals_impl(unboxIntrinsic(self), other)
    

def toUInt(self):
    return _UInt___init__impl_(((self + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)

def toUInt_0(self):
    return _UInt___init__impl_(self)

def toUInt_1(self):
    return _UInt___init__impl_(self)

def toUInt_2(self):
    return doubleToUInt(self)

def toUInt_3(self):
    return doubleToUInt(kotlin_Double(self))

def toUInt_4(self):
    return _UInt___init__impl_(self)

def _UIntArray___init__impl_(storage):
    return kotlin_UIntArray(storage)

def _UIntArray___get_storage__impl_(this):
    return this.storage

def _UIntArray___init__impl__0(size):
    tmp = _UIntArray___init__impl_(int32Array(size))
    return tmp

def UIntArray__get_impl(this, index):
    return toUInt_0(_UIntArray___get_storage__impl_(this)[index])

def UIntArray__set_impl(this, index, value):
    _UIntArray___get_storage__impl_(this).__setitem__(index, UInt__toInt_impl(value))

def _UIntArray___get_size__impl_(this):
    return len(_UIntArray___get_storage__impl_(this))

def UIntArray__iterator_impl(this):
    return Iterator_0(_UIntArray___get_storage__impl_(this))

class UIntIterator:
    pass

class Iterator_0(UIntIterator):
    def __init__(self, array):
        UIntIterator.__init__(self)
        self.array = array
        self.index = 0
    
    def _get_array__0_k_(self):
        return self.array
    
    def _set_index__majfzk_k_(self, _set___):
        self.index = _set___
    
    def _get_index__0_k_(self):
        return self.index
    
    def hasNext_0_k_(self):
        return self._get_index__0_k_() < len(self._get_array__0_k_())
    
    def nextUInt_sv9k7v_k_(self):
        if self._get_index__0_k_() < len(self._get_array__0_k_()):
            tmp = self._get_array__0_k_()
            tmp0_this = self
            tmp1 = tmp0_this._get_index__0_k_()
            tmp0_this._set_index__majfzk_k_((((tmp1 + 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
            tmp = toUInt_0(tmp[tmp1])
        else:
            raise NoSuchElementException_init__Create__0(self._get_index__0_k_().toString())
        
        return tmp
    
    def next_sv9k7v_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def UIntArray__contains_impl(this, element):
    tmp = (boxIntrinsic(element)) if (isObject(boxIntrinsic(element))) else (THROW_CCE())
    if not isinstance(tmp, UInt):
        return False
    
    return contains_1(_UIntArray___get_storage__impl_(this), UInt__toInt_impl(element))

def UIntArray__containsAll_impl(this, elements):
    def complexFunction_x2__If__Return__0(it):
        if isinstance(it, UInt):
            tmp = contains_1(_UIntArray___get_storage__impl_(this), UInt__toInt_impl(unboxIntrinsic(it)))
        elif True:
            tmp = False
        
        return tmp
    
    return all((kotlin_collections_Collection___(elements)) if (isInterface(elements, Collection)) else (THROW_CCE()), complexFunction_x2__If__Return__0)

def UIntArray__isEmpty_impl(this):
    return len(_UIntArray___get_storage__impl_(this)) == 0

def UIntArray__toString_impl(this):
    return ((str('UIntArray(') + str('storage=')) + str(toString_0(this.storage))) + str(')')

def UIntArray__hashCode_impl(this):
    return hashCode(this.storage)

def UIntArray__equals_impl(this, other):
    if not isinstance(other, UIntArray):
        return False
    
    tmp0_other_with_cast = (unboxIntrinsic(other)) if (isinstance(other, UIntArray)) else (THROW_CCE())
    if not (this.storage == tmp0_other_with_cast.storage):
        return False
    
    return True

class UIntArray(Collection):
    def __init__(self, storage):
        self.storage = storage
    
    def _get_size__0_k_(self):
        return _UIntArray___get_size__impl_(unboxIntrinsic(self))
    
    def iterator_0_k_(self):
        return UIntArray__iterator_impl(unboxIntrinsic(self))
    
    def contains_wijjag_k_(self, element):
        return UIntArray__contains_impl(unboxIntrinsic(self), element)
    
    def containsAll_sjraxa_k_(self, elements):
        return UIntArray__containsAll_impl(unboxIntrinsic(self), elements)
    
    def isEmpty_0_k_(self):
        return UIntArray__isEmpty_impl(unboxIntrinsic(self))
    
    def toString(self):
        return UIntArray__toString_impl(unboxIntrinsic(self))
    
    def hashCode(self):
        return UIntArray__hashCode_impl(unboxIntrinsic(self))
    
    def equals(self, other):
        return UIntArray__equals_impl(unboxIntrinsic(self), other)
    

class Companion_6(Any):
    def __init__(self):
        global Companion_instance
        Companion_instance = self
        self.EMPTY = UIntRange(Companion_getInstance_4()._get_MAX_VALUE__sv9k7v_k_(), Companion_getInstance_4()._get_MIN_VALUE__sv9k7v_k_())
    
    def _get_EMPTY__0_k_(self):
        return self.EMPTY
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

Companion_instance = None
def Companion_getInstance_5():
    if Companion_instance == None:
        Companion_6()
    
    return Companion_instance

class UIntProgression:
    pass

class ClosedRange:
    pass

class UIntRange(UIntProgression, ClosedRange):
    def __init__(self, start, endInclusive):
        Companion_getInstance_5()
        UIntProgression.__init__(self, start, endInclusive, 1)
    
    def _get_start__sv9k7v_k_(self):
        return self._get_first__sv9k7v_k_()
    
    def _get_endInclusive__sv9k7v_k_(self):
        return self._get_last__sv9k7v_k_()
    
    def contains_wijjag_k_(self, value):
        return (UInt__compareTo_impl_1(value, self._get_last__sv9k7v_k_()) <= 0) if (UInt__compareTo_impl_1(self._get_first__sv9k7v_k_(), value) <= 0) else (False)
    
    def isEmpty_0_k_(self):
        return UInt__compareTo_impl_1(self._get_first__sv9k7v_k_(), self._get_last__sv9k7v_k_()) > 0
    
    def equals(self, other):
        if isinstance(other, UIntRange):
            tmp = (True) if ((kotlin_ranges_UIntRange(other).isEmpty_0_k_()) if (self.isEmpty_0_k_()) else (False)) else ((boxIntrinsic(self._get_last__sv9k7v_k_()) == boxIntrinsic(kotlin_ranges_UIntRange(other)._get_last__sv9k7v_k_())) if (boxIntrinsic(self._get_first__sv9k7v_k_()) == boxIntrinsic(kotlin_ranges_UIntRange(other)._get_first__sv9k7v_k_())) else (False))
        elif True:
            tmp = False
        
        return tmp
    
    def hashCode(self):
        return (-1) if (self.isEmpty_0_k_()) else ((((imul(31, UInt__toInt_impl(self._get_first__sv9k7v_k_())) + UInt__toInt_impl(self._get_last__sv9k7v_k_())) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
    
    def toString(self):
        return (str(boxIntrinsic(self._get_first__sv9k7v_k_())) + str('..')) + str(boxIntrinsic(self._get_last__sv9k7v_k_()))
    
    def _get_first__sv9k7v_k_(self):
        pass
    
    def _get_last__sv9k7v_k_(self):
        pass
    
    def _get_step__0_k_(self):
        pass
    
    def iterator_0_k_(self):
        pass
    

class Companion_7(Any):
    def __init__(self):
        global Companion_instance
        Companion_instance = self
    
    def fromClosedRange_rpfvw1_k_(self, rangeStart, rangeEnd, step):
        return UIntProgression(rangeStart, rangeEnd, step)
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

Companion_instance = None
def Companion_getInstance_6():
    if Companion_instance == None:
        Companion_7()
    
    return Companion_instance

class Iterable:
    pass

class UIntProgression(Iterable):
    def __init__(self, start, endInclusive, step):
        Companion_getInstance_6()
        if step == 0:
            raise IllegalArgumentException_init__Create__0('Step must be non-zero.')
        
        if step == visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OBJECT_GET_INSTANCE_FUNCTION_name_Companion_getInstance_visibility_public_modality_FINAL_______returnType_kotlin_Int_Companion._get_MIN_VALUE__0_k_():
            raise IllegalArgumentException_init__Create__0('Step must be greater than Int.MIN_VALUE to avoid overflow on negation.')
        
        self.first = start
        self.last = getProgressionLastElement(start, endInclusive, step)
        self.step = step
    
    def _get_first__sv9k7v_k_(self):
        return self.first
    
    def _get_last__sv9k7v_k_(self):
        return self.last
    
    def _get_step__0_k_(self):
        return self.step
    
    def iterator_0_k_(self):
        return UIntProgressionIterator(self._get_first__sv9k7v_k_(), self._get_last__sv9k7v_k_(), self._get_step__0_k_())
    
    def isEmpty_0_k_(self):
        return (UInt__compareTo_impl_1(self._get_first__sv9k7v_k_(), self._get_last__sv9k7v_k_()) > 0) if (self._get_step__0_k_() > 0) else (UInt__compareTo_impl_1(self._get_first__sv9k7v_k_(), self._get_last__sv9k7v_k_()) < 0)
    
    def equals(self, other):
        if isinstance(other, UIntProgression):
            tmp = (True) if ((kotlin_ranges_UIntProgression(other).isEmpty_0_k_()) if (self.isEmpty_0_k_()) else (False)) else ((self._get_step__0_k_() == kotlin_ranges_UIntProgression(other)._get_step__0_k_()) if ((boxIntrinsic(self._get_last__sv9k7v_k_()) == boxIntrinsic(kotlin_ranges_UIntProgression(other)._get_last__sv9k7v_k_())) if (boxIntrinsic(self._get_first__sv9k7v_k_()) == boxIntrinsic(kotlin_ranges_UIntProgression(other)._get_first__sv9k7v_k_())) else (False)) else (False))
        elif True:
            tmp = False
        
        return tmp
    
    def hashCode(self):
        return (-1) if (self.isEmpty_0_k_()) else ((((imul(31, (((imul(31, UInt__toInt_impl(self._get_first__sv9k7v_k_())) + UInt__toInt_impl(self._get_last__sv9k7v_k_())) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000) + self._get_step__0_k_()) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
    
    def toString(self):
        return ((((str(boxIntrinsic(self._get_first__sv9k7v_k_())) + str('..')) + str(boxIntrinsic(self._get_last__sv9k7v_k_()))) + str(' step ')) + str(self._get_step__0_k_())) if (self._get_step__0_k_() > 0) else ((((str(boxIntrinsic(self._get_first__sv9k7v_k_())) + str(' downTo ')) + str(boxIntrinsic(self._get_last__sv9k7v_k_()))) + str(' step ')) + str(((-self._get_step__0_k_() + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000))
    

class UIntProgressionIterator(UIntIterator):
    def __init__(self, first, last, step):
        UIntIterator.__init__(self)
        self.finalElement = last
        self.hasNext = (UInt__compareTo_impl_1(first, last) <= 0) if (step > 0) else (UInt__compareTo_impl_1(first, last) >= 0)
        self.step = toUInt_0(step)
        self.next = (first) if (self._get_hasNext__0_k_()) else (self._get_finalElement__sv9k7v_k_())
    
    def _get_finalElement__sv9k7v_k_(self):
        return self.finalElement
    
    def _set_hasNext__rpwsgn_k_(self, _set___):
        self.hasNext = _set___
    
    def _get_hasNext__0_k_(self):
        return self.hasNext
    
    def _get_step__sv9k7v_k_(self):
        return self.step
    
    def _set_next__5hr6x_k_(self, _set___):
        self.next = _set___
    
    def _get_next__sv9k7v_k_(self):
        return self.next
    
    def hasNext_0_k_(self):
        return self._get_hasNext__0_k_()
    
    def nextUInt_sv9k7v_k_(self):
        value = self._get_next__sv9k7v_k_()
        if boxIntrinsic(value) == boxIntrinsic(self._get_finalElement__sv9k7v_k_()):
            if not self._get_hasNext__0_k_():
                raise NoSuchElementException_init__Create_()
            
            self._set_hasNext__rpwsgn_k_(False)
        else:
            tmp0_this = self
            tmp0_this._set_next__5hr6x_k_(UInt__plus_impl_1(tmp0_this._get_next__sv9k7v_k_(), self._get_step__sv9k7v_k_()))
        
        return value
    
    def next_sv9k7v_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class UIntIterator(Iterator_3):
    def __init__(self):
        pass
    
    def next_sv9k7v_k_(self):
        return self.nextUInt_sv9k7v_k_()
    
    def nextUInt_sv9k7v_k_(self):
        pass
    
    def hasNext_0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class ULongIterator(Iterator_3):
    def __init__(self):
        pass
    
    def next_sha8jq_k_(self):
        return self.nextULong_sha8jq_k_()
    
    def nextULong_sha8jq_k_(self):
        pass
    
    def hasNext_0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class UByteIterator(Iterator_3):
    def __init__(self):
        pass
    
    def next_sh428i_k_(self):
        return self.nextUByte_sh428i_k_()
    
    def nextUByte_sh428i_k_(self):
        pass
    
    def hasNext_0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class UShortIterator(Iterator_3):
    def __init__(self):
        pass
    
    def next_um6tma_k_(self):
        return self.nextUShort_um6tma_k_()
    
    def nextUShort_um6tma_k_(self):
        pass
    
    def hasNext_0_k_(self):
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

class Companion_8(Any):
    def __init__(self):
        global Companion_instance
        Companion_instance = self
        self.MIN_VALUE = _ULong___init__impl_(Long(0, 0))
        self.MAX_VALUE = _ULong___init__impl_(Long(-1, -1))
        self.SIZE_BYTES = 8
        self.SIZE_BITS = 64
    
    def _get_MIN_VALUE__sha8jq_k_(self):
        return self.MIN_VALUE
    
    def _get_MAX_VALUE__sha8jq_k_(self):
        return self.MAX_VALUE
    
    def _get_SIZE_BYTES__0_k_(self):
        return self.SIZE_BYTES
    
    def _get_SIZE_BITS__0_k_(self):
        return self.SIZE_BITS
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

Companion_instance = None
def Companion_getInstance_7():
    if Companion_instance == None:
        Companion_8()
    
    return Companion_instance

def ULong__compareTo_impl(this, other):
    return ULong__compareTo_impl_2(this, UByte__toULong_impl(other))

def ULong__compareTo_impl_0(this, other):
    return ULong__compareTo_impl_2(this, UShort__toULong_impl(other))

def ULong__compareTo_impl_1(this, other):
    return ULong__compareTo_impl_2(this, UInt__toULong_impl(other))

def ULong__compareTo_impl_2(this, other):
    return ulongCompare(_ULong___get_data__impl_(this), _ULong___get_data__impl_(other))

def ULong__plus_impl(this, other):
    return ULong__plus_impl_2(this, UByte__toULong_impl(other))

def ULong__plus_impl_0(this, other):
    return ULong__plus_impl_2(this, UShort__toULong_impl(other))

def ULong__plus_impl_1(this, other):
    return ULong__plus_impl_2(this, UInt__toULong_impl(other))

def ULong__plus_impl_2(this, other):
    return _ULong___init__impl_((((_ULong___get_data__impl_(this) + _ULong___get_data__impl_(other)) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000)

def ULong__minus_impl(this, other):
    return ULong__minus_impl_2(this, UByte__toULong_impl(other))

def ULong__minus_impl_0(this, other):
    return ULong__minus_impl_2(this, UShort__toULong_impl(other))

def ULong__minus_impl_1(this, other):
    return ULong__minus_impl_2(this, UInt__toULong_impl(other))

def ULong__minus_impl_2(this, other):
    return _ULong___init__impl_((((_ULong___get_data__impl_(this) - _ULong___get_data__impl_(other)) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000)

def ULong__times_impl(this, other):
    return ULong__times_impl_2(this, UByte__toULong_impl(other))

def ULong__times_impl_0(this, other):
    return ULong__times_impl_2(this, UShort__toULong_impl(other))

def ULong__times_impl_1(this, other):
    return ULong__times_impl_2(this, UInt__toULong_impl(other))

def ULong__times_impl_2(this, other):
    return _ULong___init__impl_((((_ULong___get_data__impl_(this) * _ULong___get_data__impl_(other)) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000)

def ULong__div_impl(this, other):
    return ULong__div_impl_2(this, UByte__toULong_impl(other))

def ULong__div_impl_0(this, other):
    return ULong__div_impl_2(this, UShort__toULong_impl(other))

def ULong__div_impl_1(this, other):
    return ULong__div_impl_2(this, UInt__toULong_impl(other))

def ULong__div_impl_2(this, other):
    return ulongDivide(this, other)

def ULong__rem_impl(this, other):
    return ULong__rem_impl_2(this, UByte__toULong_impl(other))

def ULong__rem_impl_0(this, other):
    return ULong__rem_impl_2(this, UShort__toULong_impl(other))

def ULong__rem_impl_1(this, other):
    return ULong__rem_impl_2(this, UInt__toULong_impl(other))

def ULong__rem_impl_2(this, other):
    return ulongRemainder(this, other)

def ULong__floorDiv_impl(this, other):
    return ULong__floorDiv_impl_2(this, UByte__toULong_impl(other))

def ULong__floorDiv_impl_0(this, other):
    return ULong__floorDiv_impl_2(this, UShort__toULong_impl(other))

def ULong__floorDiv_impl_1(this, other):
    return ULong__floorDiv_impl_2(this, UInt__toULong_impl(other))

def ULong__floorDiv_impl_2(this, other):
    return ULong__div_impl_2(this, other)

def ULong__mod_impl(this, other):
    return ULong__toUByte_impl(ULong__mod_impl_2(this, UByte__toULong_impl(other)))

def ULong__mod_impl_0(this, other):
    return ULong__toUShort_impl(ULong__mod_impl_2(this, UShort__toULong_impl(other)))

def ULong__mod_impl_1(this, other):
    return ULong__toUInt_impl(ULong__mod_impl_2(this, UInt__toULong_impl(other)))

def ULong__mod_impl_2(this, other):
    return ULong__rem_impl_2(this, other)

def ULong__inc_impl(this):
    return _ULong___init__impl_((((_ULong___get_data__impl_(this) + 1) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000)

def ULong__dec_impl(this):
    return _ULong___init__impl_((((_ULong___get_data__impl_(this) - 1) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000)

def ULong__rangeTo_impl(this, other):
    return ULongRange(this, other)

def ULong__shl_impl(this, bitCount):
    return _ULong___init__impl_((((_ULong___get_data__impl_(this) << bitCount) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000)

def ULong__shr_impl(this, bitCount):
    return _ULong___init__impl_(((((_ULong___get_data__impl_(this) & 0xffff_ffff_ffff_ffff) >> bitCount) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000)

def ULong__and_impl(this, other):
    return _ULong___init__impl_((((_ULong___get_data__impl_(this) & _ULong___get_data__impl_(other)) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000)

def ULong__or_impl(this, other):
    return _ULong___init__impl_((((_ULong___get_data__impl_(this) | _ULong___get_data__impl_(other)) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000)

def ULong__xor_impl(this, other):
    return _ULong___init__impl_((((_ULong___get_data__impl_(this) ^ _ULong___get_data__impl_(other)) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000)

def ULong__inv_impl(this):
    return _ULong___init__impl_(~_ULong___get_data__impl_(this))

def ULong__toByte_impl(this):
    return ((_ULong___get_data__impl_(this) + 0x80) & 0xff) - 0x80

def ULong__toShort_impl(this):
    return ((_ULong___get_data__impl_(this) + 0x8000) & 0xffff) - 0x8000

def ULong__toInt_impl(this):
    return ((_ULong___get_data__impl_(this) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000

def ULong__toLong_impl(this):
    return _ULong___get_data__impl_(this)

def ULong__toUByte_impl(this):
    return toUByte_1(_ULong___get_data__impl_(this))

def ULong__toUShort_impl(this):
    return toUShort_0(_ULong___get_data__impl_(this))

def ULong__toUInt_impl(this):
    return toUInt(_ULong___get_data__impl_(this))

def ULong__toULong_impl(this):
    return this

def ULong__toFloat_impl(this):
    return kotlin_Float(ULong__toDouble_impl(this))

def ULong__toDouble_impl(this):
    return ulongToDouble(_ULong___get_data__impl_(this))

def ULong__toString_impl(this):
    return ulongToString(_ULong___get_data__impl_(this))

def ULong__hashCode_impl(this):
    return this.data.hashCode()

def ULong__equals_impl(this, other):
    if not isinstance(other, ULong):
        return False
    
    tmp0_other_with_cast = (unboxIntrinsic(other)) if (isinstance(other, ULong)) else (THROW_CCE())
    if not (this.data == tmp0_other_with_cast.data):
        return False
    
    return True

class ULong(Comparable):
    def __init__(self, data):
        Companion_getInstance_7()
        self.data = data
    
    def compareTo_djarz7_k_(self, other):
        return ULong__compareTo_impl_2(unboxIntrinsic(self), other)
    
    def toString(self):
        return ULong__toString_impl(unboxIntrinsic(self))
    
    def hashCode(self):
        return ULong__hashCode_impl(unboxIntrinsic(self))
    
    def equals(self, other):
        return ULong__equals_impl(unboxIntrinsic(self), other)
    

def toULong(self):
    return _ULong___init__impl_(self)

def toULong_0(self):
    return _ULong___init__impl_(self)

def toULong_1(self):
    return doubleToULong(self)

def toULong_2(self):
    return doubleToULong(kotlin_Double(self))

def toULong_3(self):
    return _ULong___init__impl_(self)

def toULong_4(self):
    return _ULong___init__impl_(self)

def _ULongArray___init__impl_(storage):
    return kotlin_ULongArray(storage)

def _ULongArray___get_storage__impl_(this):
    return this.storage

def _ULongArray___init__impl__0(size):
    tmp = _ULongArray___init__impl_(longArray(size))
    return tmp

def ULongArray__get_impl(this, index):
    return toULong(_ULongArray___get_storage__impl_(this)[index])

def ULongArray__set_impl(this, index, value):
    _ULongArray___get_storage__impl_(this).__setitem__(index, ULong__toLong_impl(value))

def _ULongArray___get_size__impl_(this):
    return len(_ULongArray___get_storage__impl_(this))

def ULongArray__iterator_impl(this):
    return Iterator_1(_ULongArray___get_storage__impl_(this))

class Iterator_1(ULongIterator):
    def __init__(self, array):
        ULongIterator.__init__(self)
        self.array = array
        self.index = 0
    
    def _get_array__0_k_(self):
        return self.array
    
    def _set_index__majfzk_k_(self, _set___):
        self.index = _set___
    
    def _get_index__0_k_(self):
        return self.index
    
    def hasNext_0_k_(self):
        return self._get_index__0_k_() < len(self._get_array__0_k_())
    
    def nextULong_sha8jq_k_(self):
        if self._get_index__0_k_() < len(self._get_array__0_k_()):
            tmp = self._get_array__0_k_()
            tmp0_this = self
            tmp1 = tmp0_this._get_index__0_k_()
            tmp0_this._set_index__majfzk_k_((((tmp1 + 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
            tmp = toULong(tmp[tmp1])
        else:
            raise NoSuchElementException_init__Create__0(self._get_index__0_k_().toString())
        
        return tmp
    
    def next_sha8jq_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def ULongArray__contains_impl(this, element):
    tmp = (boxIntrinsic(element)) if (isObject(boxIntrinsic(element))) else (THROW_CCE())
    if not isinstance(tmp, ULong):
        return False
    
    return contains_2(_ULongArray___get_storage__impl_(this), ULong__toLong_impl(element))

def ULongArray__containsAll_impl(this, elements):
    def complexFunction_x2__If__Return__0(it):
        if isinstance(it, ULong):
            tmp = contains_2(_ULongArray___get_storage__impl_(this), ULong__toLong_impl(unboxIntrinsic(it)))
        elif True:
            tmp = False
        
        return tmp
    
    return all((kotlin_collections_Collection___(elements)) if (isInterface(elements, Collection)) else (THROW_CCE()), complexFunction_x2__If__Return__0)

def ULongArray__isEmpty_impl(this):
    return len(_ULongArray___get_storage__impl_(this)) == 0

def ULongArray__toString_impl(this):
    return ((str('ULongArray(') + str('storage=')) + str(toString_0(this.storage))) + str(')')

def ULongArray__hashCode_impl(this):
    return hashCode(this.storage)

def ULongArray__equals_impl(this, other):
    if not isinstance(other, ULongArray):
        return False
    
    tmp0_other_with_cast = (unboxIntrinsic(other)) if (isinstance(other, ULongArray)) else (THROW_CCE())
    if not (this.storage == tmp0_other_with_cast.storage):
        return False
    
    return True

class ULongArray(Collection):
    def __init__(self, storage):
        self.storage = storage
    
    def _get_size__0_k_(self):
        return _ULongArray___get_size__impl_(unboxIntrinsic(self))
    
    def iterator_0_k_(self):
        return ULongArray__iterator_impl(unboxIntrinsic(self))
    
    def contains_djarz7_k_(self, element):
        return ULongArray__contains_impl(unboxIntrinsic(self), element)
    
    def containsAll_wotoar_k_(self, elements):
        return ULongArray__containsAll_impl(unboxIntrinsic(self), elements)
    
    def isEmpty_0_k_(self):
        return ULongArray__isEmpty_impl(unboxIntrinsic(self))
    
    def toString(self):
        return ULongArray__toString_impl(unboxIntrinsic(self))
    
    def hashCode(self):
        return ULongArray__hashCode_impl(unboxIntrinsic(self))
    
    def equals(self, other):
        return ULongArray__equals_impl(unboxIntrinsic(self), other)
    

class Companion_9(Any):
    def __init__(self):
        global Companion_instance
        Companion_instance = self
        self.EMPTY = ULongRange(Companion_getInstance_7()._get_MAX_VALUE__sha8jq_k_(), Companion_getInstance_7()._get_MIN_VALUE__sha8jq_k_())
    
    def _get_EMPTY__0_k_(self):
        return self.EMPTY
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

Companion_instance = None
def Companion_getInstance_8():
    if Companion_instance == None:
        Companion_9()
    
    return Companion_instance

class ULongProgression:
    pass

class ULongRange(ULongProgression, ClosedRange):
    def __init__(self, start, endInclusive):
        Companion_getInstance_8()
        ULongProgression.__init__(self, start, endInclusive, 1)
    
    def _get_start__sha8jq_k_(self):
        return self._get_first__sha8jq_k_()
    
    def _get_endInclusive__sha8jq_k_(self):
        return self._get_last__sha8jq_k_()
    
    def contains_djarz7_k_(self, value):
        return (ULong__compareTo_impl_2(value, self._get_last__sha8jq_k_()) <= 0) if (ULong__compareTo_impl_2(self._get_first__sha8jq_k_(), value) <= 0) else (False)
    
    def isEmpty_0_k_(self):
        return ULong__compareTo_impl_2(self._get_first__sha8jq_k_(), self._get_last__sha8jq_k_()) > 0
    
    def equals(self, other):
        if isinstance(other, ULongRange):
            tmp = (True) if ((kotlin_ranges_ULongRange(other).isEmpty_0_k_()) if (self.isEmpty_0_k_()) else (False)) else ((boxIntrinsic(self._get_last__sha8jq_k_()) == boxIntrinsic(kotlin_ranges_ULongRange(other)._get_last__sha8jq_k_())) if (boxIntrinsic(self._get_first__sha8jq_k_()) == boxIntrinsic(kotlin_ranges_ULongRange(other)._get_first__sha8jq_k_())) else (False))
        elif True:
            tmp = False
        
        return tmp
    
    def hashCode(self):
        return (-1) if (self.isEmpty_0_k_()) else ((((imul(31, ULong__toInt_impl(ULong__xor_impl(self._get_first__sha8jq_k_(), ULong__shr_impl(self._get_first__sha8jq_k_(), 32)))) + ULong__toInt_impl(ULong__xor_impl(self._get_last__sha8jq_k_(), ULong__shr_impl(self._get_last__sha8jq_k_(), 32)))) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
    
    def toString(self):
        return (str(boxIntrinsic(self._get_first__sha8jq_k_())) + str('..')) + str(boxIntrinsic(self._get_last__sha8jq_k_()))
    
    def _get_first__sha8jq_k_(self):
        pass
    
    def _get_last__sha8jq_k_(self):
        pass
    
    def _get_step__0_k_(self):
        pass
    
    def iterator_0_k_(self):
        pass
    

class Companion_10(Any):
    def __init__(self):
        global Companion_instance
        Companion_instance = self
    
    def fromClosedRange_19wfq_k_(self, rangeStart, rangeEnd, step):
        return ULongProgression(rangeStart, rangeEnd, step)
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

Companion_instance = None
def Companion_getInstance_9():
    if Companion_instance == None:
        Companion_10()
    
    return Companion_instance

class ULongProgression(Iterable):
    def __init__(self, start, endInclusive, step):
        Companion_getInstance_9()
        if step == 0:
            raise IllegalArgumentException_init__Create__0('Step must be non-zero.')
        
        if step == Companion_getInstance_19()._get_MIN_VALUE__0_k_():
            raise IllegalArgumentException_init__Create__0('Step must be greater than Long.MIN_VALUE to avoid overflow on negation.')
        
        self.first = start
        self.last = getProgressionLastElement_0(start, endInclusive, step)
        self.step = step
    
    def _get_first__sha8jq_k_(self):
        return self.first
    
    def _get_last__sha8jq_k_(self):
        return self.last
    
    def _get_step__0_k_(self):
        return self.step
    
    def iterator_0_k_(self):
        return ULongProgressionIterator(self._get_first__sha8jq_k_(), self._get_last__sha8jq_k_(), self._get_step__0_k_())
    
    def isEmpty_0_k_(self):
        return (ULong__compareTo_impl_2(self._get_first__sha8jq_k_(), self._get_last__sha8jq_k_()) > 0) if (self._get_step__0_k_().compareTo_wiekkq_k_(0) > 0) else (ULong__compareTo_impl_2(self._get_first__sha8jq_k_(), self._get_last__sha8jq_k_()) < 0)
    
    def equals(self, other):
        if isinstance(other, ULongProgression):
            tmp = (True) if ((kotlin_ranges_ULongProgression(other).isEmpty_0_k_()) if (self.isEmpty_0_k_()) else (False)) else ((self._get_step__0_k_() == kotlin_ranges_ULongProgression(other)._get_step__0_k_()) if ((boxIntrinsic(self._get_last__sha8jq_k_()) == boxIntrinsic(kotlin_ranges_ULongProgression(other)._get_last__sha8jq_k_())) if (boxIntrinsic(self._get_first__sha8jq_k_()) == boxIntrinsic(kotlin_ranges_ULongProgression(other)._get_first__sha8jq_k_())) else (False)) else (False))
        elif True:
            tmp = False
        
        return tmp
    
    def hashCode(self):
        return (-1) if (self.isEmpty_0_k_()) else ((((imul(31, (((imul(31, ULong__toInt_impl(ULong__xor_impl(self._get_first__sha8jq_k_(), ULong__shr_impl(self._get_first__sha8jq_k_(), 32)))) + ULong__toInt_impl(ULong__xor_impl(self._get_last__sha8jq_k_(), ULong__shr_impl(self._get_last__sha8jq_k_(), 32)))) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000) + (((((((self._get_step__0_k_() ^ (((((self._get_step__0_k_() & 0xffff_ffff_ffff_ffff) >> 32) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000)) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
    
    def toString(self):
        return ((((str(boxIntrinsic(self._get_first__sha8jq_k_())) + str('..')) + str(boxIntrinsic(self._get_last__sha8jq_k_()))) + str(' step ')) + str(self._get_step__0_k_())) if (self._get_step__0_k_().compareTo_wiekkq_k_(0) > 0) else ((((str(boxIntrinsic(self._get_first__sha8jq_k_())) + str(' downTo ')) + str(boxIntrinsic(self._get_last__sha8jq_k_()))) + str(' step ')) + str(((-self._get_step__0_k_() + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000))
    

class ULongProgressionIterator(ULongIterator):
    def __init__(self, first, last, step):
        ULongIterator.__init__(self)
        self.finalElement = last
        self.hasNext = (ULong__compareTo_impl_2(first, last) <= 0) if (step.compareTo_wiekkq_k_(0) > 0) else (ULong__compareTo_impl_2(first, last) >= 0)
        self.step = toULong(step)
        self.next = (first) if (self._get_hasNext__0_k_()) else (self._get_finalElement__sha8jq_k_())
    
    def _get_finalElement__sha8jq_k_(self):
        return self.finalElement
    
    def _set_hasNext__rpwsgn_k_(self, _set___):
        self.hasNext = _set___
    
    def _get_hasNext__0_k_(self):
        return self.hasNext
    
    def _get_step__sha8jq_k_(self):
        return self.step
    
    def _set_next__yvipqq_k_(self, _set___):
        self.next = _set___
    
    def _get_next__sha8jq_k_(self):
        return self.next
    
    def hasNext_0_k_(self):
        return self._get_hasNext__0_k_()
    
    def nextULong_sha8jq_k_(self):
        value = self._get_next__sha8jq_k_()
        if boxIntrinsic(value) == boxIntrinsic(self._get_finalElement__sha8jq_k_()):
            if not self._get_hasNext__0_k_():
                raise NoSuchElementException_init__Create_()
            
            self._set_hasNext__rpwsgn_k_(False)
        else:
            tmp0_this = self
            tmp0_this._set_next__yvipqq_k_(ULong__plus_impl_2(tmp0_this._get_next__sha8jq_k_(), self._get_step__sha8jq_k_()))
        
        return value
    
    def next_sha8jq_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def getProgressionLastElement(start, end, step):
    if step > 0:
        tmp = (end) if (UInt__compareTo_impl_1(start, end) >= 0) else (UInt__minus_impl_1(end, differenceModulo(end, start, toUInt_0(step))))
    elif step < 0:
        tmp = (end) if (UInt__compareTo_impl_1(start, end) <= 0) else (UInt__plus_impl_1(end, differenceModulo(start, end, toUInt_0(((-step + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000))))
    else:
        raise IllegalArgumentException_init__Create__0('Step is zero.')
    
    return tmp

def getProgressionLastElement_0(start, end, step):
    if step.compareTo_wiekkq_k_(0) > 0:
        tmp = (end) if (ULong__compareTo_impl_2(start, end) >= 0) else (ULong__minus_impl_2(end, differenceModulo_0(end, start, toULong(step))))
    elif step.compareTo_wiekkq_k_(0) < 0:
        tmp = (end) if (ULong__compareTo_impl_2(start, end) <= 0) else (ULong__plus_impl_2(end, differenceModulo_0(start, end, toULong(((-step + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000))))
    else:
        raise IllegalArgumentException_init__Create__0('Step is zero.')
    
    return tmp

def differenceModulo(a, b, c):
    ac = UInt__rem_impl_1(a, c)
    bc = UInt__rem_impl_1(b, c)
    return (UInt__minus_impl_1(ac, bc)) if (UInt__compareTo_impl_1(ac, bc) >= 0) else (UInt__plus_impl_1(UInt__minus_impl_1(ac, bc), c))

def differenceModulo_0(a, b, c):
    ac = ULong__rem_impl_2(a, c)
    bc = ULong__rem_impl_2(b, c)
    return (ULong__minus_impl_2(ac, bc)) if (ULong__compareTo_impl_2(ac, bc) >= 0) else (ULong__plus_impl_2(ULong__minus_impl_2(ac, bc), c))

def _UShort___init__impl_(data):
    return kotlin_UShort(data)

def _UShort___get_data__impl_(this):
    return this.data

class Companion_11(Any):
    def __init__(self):
        global Companion_instance
        Companion_instance = self
        self.MIN_VALUE = _UShort___init__impl_(0)
        self.MAX_VALUE = _UShort___init__impl_(-1)
        self.SIZE_BYTES = 2
        self.SIZE_BITS = 16
    
    def _get_MIN_VALUE__um6tma_k_(self):
        return self.MIN_VALUE
    
    def _get_MAX_VALUE__um6tma_k_(self):
        return self.MAX_VALUE
    
    def _get_SIZE_BYTES__0_k_(self):
        return self.SIZE_BYTES
    
    def _get_SIZE_BITS__0_k_(self):
        return self.SIZE_BITS
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

Companion_instance = None
def Companion_getInstance_10():
    if Companion_instance == None:
        Companion_11()
    
    return Companion_instance

def UShort__compareTo_impl(this, other):
    return compareTo_0(UShort__toInt_impl(this), UByte__toInt_impl(other))

def UShort__compareTo_impl_0(this, other):
    return compareTo_0(UShort__toInt_impl(this), UShort__toInt_impl(other))

def UShort__compareTo_impl_1(this, other):
    return UInt__compareTo_impl_1(UShort__toUInt_impl(this), other)

def UShort__compareTo_impl_2(this, other):
    return ULong__compareTo_impl_2(UShort__toULong_impl(this), other)

def UShort__plus_impl(this, other):
    return UInt__plus_impl_1(UShort__toUInt_impl(this), UByte__toUInt_impl(other))

def UShort__plus_impl_0(this, other):
    return UInt__plus_impl_1(UShort__toUInt_impl(this), UShort__toUInt_impl(other))

def UShort__plus_impl_1(this, other):
    return UInt__plus_impl_1(UShort__toUInt_impl(this), other)

def UShort__plus_impl_2(this, other):
    return ULong__plus_impl_2(UShort__toULong_impl(this), other)

def UShort__minus_impl(this, other):
    return UInt__minus_impl_1(UShort__toUInt_impl(this), UByte__toUInt_impl(other))

def UShort__minus_impl_0(this, other):
    return UInt__minus_impl_1(UShort__toUInt_impl(this), UShort__toUInt_impl(other))

def UShort__minus_impl_1(this, other):
    return UInt__minus_impl_1(UShort__toUInt_impl(this), other)

def UShort__minus_impl_2(this, other):
    return ULong__minus_impl_2(UShort__toULong_impl(this), other)

def UShort__times_impl(this, other):
    return UInt__times_impl_1(UShort__toUInt_impl(this), UByte__toUInt_impl(other))

def UShort__times_impl_0(this, other):
    return UInt__times_impl_1(UShort__toUInt_impl(this), UShort__toUInt_impl(other))

def UShort__times_impl_1(this, other):
    return UInt__times_impl_1(UShort__toUInt_impl(this), other)

def UShort__times_impl_2(this, other):
    return ULong__times_impl_2(UShort__toULong_impl(this), other)

def UShort__div_impl(this, other):
    return UInt__div_impl_1(UShort__toUInt_impl(this), UByte__toUInt_impl(other))

def UShort__div_impl_0(this, other):
    return UInt__div_impl_1(UShort__toUInt_impl(this), UShort__toUInt_impl(other))

def UShort__div_impl_1(this, other):
    return UInt__div_impl_1(UShort__toUInt_impl(this), other)

def UShort__div_impl_2(this, other):
    return ULong__div_impl_2(UShort__toULong_impl(this), other)

def UShort__rem_impl(this, other):
    return UInt__rem_impl_1(UShort__toUInt_impl(this), UByte__toUInt_impl(other))

def UShort__rem_impl_0(this, other):
    return UInt__rem_impl_1(UShort__toUInt_impl(this), UShort__toUInt_impl(other))

def UShort__rem_impl_1(this, other):
    return UInt__rem_impl_1(UShort__toUInt_impl(this), other)

def UShort__rem_impl_2(this, other):
    return ULong__rem_impl_2(UShort__toULong_impl(this), other)

def UShort__floorDiv_impl(this, other):
    return UInt__floorDiv_impl_1(UShort__toUInt_impl(this), UByte__toUInt_impl(other))

def UShort__floorDiv_impl_0(this, other):
    return UInt__floorDiv_impl_1(UShort__toUInt_impl(this), UShort__toUInt_impl(other))

def UShort__floorDiv_impl_1(this, other):
    return UInt__floorDiv_impl_1(UShort__toUInt_impl(this), other)

def UShort__floorDiv_impl_2(this, other):
    return ULong__floorDiv_impl_2(UShort__toULong_impl(this), other)

def UShort__mod_impl(this, other):
    return UInt__toUByte_impl(UInt__mod_impl_1(UShort__toUInt_impl(this), UByte__toUInt_impl(other)))

def UShort__mod_impl_0(this, other):
    return UInt__toUShort_impl(UInt__mod_impl_1(UShort__toUInt_impl(this), UShort__toUInt_impl(other)))

def UShort__mod_impl_1(this, other):
    return UInt__mod_impl_1(UShort__toUInt_impl(this), other)

def UShort__mod_impl_2(this, other):
    return ULong__mod_impl_2(UShort__toULong_impl(this), other)

def UShort__inc_impl(this):
    return _UShort___init__impl_((((_UShort___get_data__impl_(this) + 1) + 0x8000) & 0xffff) - 0x8000)

def UShort__dec_impl(this):
    return _UShort___init__impl_((((_UShort___get_data__impl_(this) - 1) + 0x8000) & 0xffff) - 0x8000)

def UShort__rangeTo_impl(this, other):
    return UIntRange(UShort__toUInt_impl(this), UShort__toUInt_impl(other))

def UShort__and_impl(this, other):
    return _UShort___init__impl_(_and(_UShort___get_data__impl_(this), _UShort___get_data__impl_(other)))

def UShort__or_impl(this, other):
    return _UShort___init__impl_(_or(_UShort___get_data__impl_(this), _UShort___get_data__impl_(other)))

def UShort__xor_impl(this, other):
    return _UShort___init__impl_(xor(_UShort___get_data__impl_(this), _UShort___get_data__impl_(other)))

def UShort__inv_impl(this):
    return _UShort___init__impl_(inv(_UShort___get_data__impl_(this)))

def UShort__toByte_impl(this):
    return ((_UShort___get_data__impl_(this) + 0x80) & 0xff) - 0x80

def UShort__toShort_impl(this):
    return _UShort___get_data__impl_(this)

def UShort__toInt_impl(this):
    return _UShort___get_data__impl_(this) & 65535

def UShort__toLong_impl(this):
    return (((_UShort___get_data__impl_(this) & 65535) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000

def UShort__toUByte_impl(this):
    return toUByte(_UShort___get_data__impl_(this))

def UShort__toUShort_impl(this):
    return this

def UShort__toUInt_impl(this):
    return _UInt___init__impl_(_UShort___get_data__impl_(this) & 65535)

def UShort__toULong_impl(this):
    return _ULong___init__impl_((((_UShort___get_data__impl_(this) & 65535) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000)

def UShort__toFloat_impl(this):
    return kotlin_Float(UShort__toInt_impl(this))

def UShort__toDouble_impl(this):
    return kotlin_Double(UShort__toInt_impl(this))

def UShort__toString_impl(this):
    return UShort__toInt_impl(this).toString()

def UShort__hashCode_impl(this):
    return this.data

def UShort__equals_impl(this, other):
    if not isinstance(other, UShort):
        return False
    
    tmp0_other_with_cast = (unboxIntrinsic(other)) if (isinstance(other, UShort)) else (THROW_CCE())
    if not (this.data == tmp0_other_with_cast.data):
        return False
    
    return True

class UShort(Comparable):
    def __init__(self, data):
        Companion_getInstance_10()
        self.data = data
    
    def compareTo_6go47f_k_(self, other):
        return UShort__compareTo_impl_0(unboxIntrinsic(self), other)
    
    def toString(self):
        return UShort__toString_impl(unboxIntrinsic(self))
    
    def hashCode(self):
        return UShort__hashCode_impl(unboxIntrinsic(self))
    
    def equals(self, other):
        return UShort__equals_impl(unboxIntrinsic(self), other)
    

def toUShort(self):
    return _UShort___init__impl_(((self + 0x8000) & 0xffff) - 0x8000)

def toUShort_0(self):
    return _UShort___init__impl_(((self + 0x8000) & 0xffff) - 0x8000)

def toUShort_1(self):
    return _UShort___init__impl_(self)

def _UShortArray___init__impl_(storage):
    return kotlin_UShortArray(storage)

def _UShortArray___get_storage__impl_(this):
    return this.storage

def _UShortArray___init__impl__0(size):
    tmp = _UShortArray___init__impl_(int16Array(size))
    return tmp

def UShortArray__get_impl(this, index):
    return toUShort_1(_UShortArray___get_storage__impl_(this)[index])

def UShortArray__set_impl(this, index, value):
    _UShortArray___get_storage__impl_(this).__setitem__(index, UShort__toShort_impl(value))

def _UShortArray___get_size__impl_(this):
    return len(_UShortArray___get_storage__impl_(this))

def UShortArray__iterator_impl(this):
    return Iterator_2(_UShortArray___get_storage__impl_(this))

class Iterator_2(UShortIterator):
    def __init__(self, array):
        UShortIterator.__init__(self)
        self.array = array
        self.index = 0
    
    def _get_array__0_k_(self):
        return self.array
    
    def _set_index__majfzk_k_(self, _set___):
        self.index = _set___
    
    def _get_index__0_k_(self):
        return self.index
    
    def hasNext_0_k_(self):
        return self._get_index__0_k_() < len(self._get_array__0_k_())
    
    def nextUShort_um6tma_k_(self):
        if self._get_index__0_k_() < len(self._get_array__0_k_()):
            tmp = self._get_array__0_k_()
            tmp0_this = self
            tmp1 = tmp0_this._get_index__0_k_()
            tmp0_this._set_index__majfzk_k_((((tmp1 + 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
            tmp = toUShort_1(tmp[tmp1])
        else:
            raise NoSuchElementException_init__Create__0(self._get_index__0_k_().toString())
        
        return tmp
    
    def next_um6tma_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def UShortArray__contains_impl(this, element):
    tmp = (boxIntrinsic(element)) if (isObject(boxIntrinsic(element))) else (THROW_CCE())
    if not isinstance(tmp, UShort):
        return False
    
    return contains_0(_UShortArray___get_storage__impl_(this), UShort__toShort_impl(element))

def UShortArray__containsAll_impl(this, elements):
    def complexFunction_x2__If__Return__0(it):
        if isinstance(it, UShort):
            tmp = contains_0(_UShortArray___get_storage__impl_(this), UShort__toShort_impl(unboxIntrinsic(it)))
        elif True:
            tmp = False
        
        return tmp
    
    return all((kotlin_collections_Collection___(elements)) if (isInterface(elements, Collection)) else (THROW_CCE()), complexFunction_x2__If__Return__0)

def UShortArray__isEmpty_impl(this):
    return len(_UShortArray___get_storage__impl_(this)) == 0

def UShortArray__toString_impl(this):
    return ((str('UShortArray(') + str('storage=')) + str(toString_0(this.storage))) + str(')')

def UShortArray__hashCode_impl(this):
    return hashCode(this.storage)

def UShortArray__equals_impl(this, other):
    if not isinstance(other, UShortArray):
        return False
    
    tmp0_other_with_cast = (unboxIntrinsic(other)) if (isinstance(other, UShortArray)) else (THROW_CCE())
    if not (this.storage == tmp0_other_with_cast.storage):
        return False
    
    return True

class UShortArray(Collection):
    def __init__(self, storage):
        self.storage = storage
    
    def _get_size__0_k_(self):
        return _UShortArray___get_size__impl_(unboxIntrinsic(self))
    
    def iterator_0_k_(self):
        return UShortArray__iterator_impl(unboxIntrinsic(self))
    
    def contains_6go47f_k_(self, element):
        return UShortArray__contains_impl(unboxIntrinsic(self), element)
    
    def containsAll_m5guox_k_(self, elements):
        return UShortArray__containsAll_impl(unboxIntrinsic(self), elements)
    
    def isEmpty_0_k_(self):
        return UShortArray__isEmpty_impl(unboxIntrinsic(self))
    
    def toString(self):
        return UShortArray__toString_impl(unboxIntrinsic(self))
    
    def hashCode(self):
        return UShortArray__hashCode_impl(unboxIntrinsic(self))
    
    def equals(self, other):
        return UShortArray__equals_impl(unboxIntrinsic(self), other)
    

def uintCompare(v1, v2):
    return compareTo_0(v1 ^ visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OBJECT_GET_INSTANCE_FUNCTION_name_Companion_getInstance_visibility_public_modality_FINAL_______returnType_kotlin_Int_Companion._get_MIN_VALUE__0_k_(), v2 ^ visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OBJECT_GET_INSTANCE_FUNCTION_name_Companion_getInstance_visibility_public_modality_FINAL_______returnType_kotlin_Int_Companion._get_MIN_VALUE__0_k_())

def uintDivide(v1, v2):
    return toUInt((((UInt__toLong_impl(v1) // UInt__toLong_impl(v2)) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000)

def uintRemainder(v1, v2):
    return toUInt(UInt__toLong_impl(v1).rem_wiekkq_k_(UInt__toLong_impl(v2)))

def uintToDouble(v):
    return kotlin_Double(v & visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OBJECT_GET_INSTANCE_FUNCTION_name_Companion_getInstance_visibility_public_modality_FINAL_______returnType_kotlin_Int_Companion._get_MAX_VALUE__0_k_()) + (kotlin_Double((((((v & 0xffff_ffff) >> 31) << 30) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000) * 2)

def ulongCompare(v1, v2):
    return ((((v1 ^ Companion_getInstance_19()._get_MIN_VALUE__0_k_()) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000).compareTo_wiekkq_k_((((v2 ^ Companion_getInstance_19()._get_MIN_VALUE__0_k_()) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000)

def ulongDivide(v1, v2):
    dividend = ULong__toLong_impl(v1)
    divisor = ULong__toLong_impl(v2)
    if divisor.compareTo_wiekkq_k_(0) < 0:
        return (_ULong___init__impl_(0)) if (ULong__compareTo_impl_2(v1, v2) < 0) else (_ULong___init__impl_(1))
    
    if dividend.compareTo_wiekkq_k_(0) >= 0:
        return _ULong___init__impl_((((dividend // divisor) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000)
    
    quotient = ((((((((((((dividend & 0xffff_ffff_ffff_ffff) >> 1) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000) // divisor) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000) << 1) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000
    rem = (((dividend - ((((quotient * divisor) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000)) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000
    return _ULong___init__impl_((((quotient + ((1) if (ULong__compareTo_impl_2(_ULong___init__impl_(rem), _ULong___init__impl_(divisor)) >= 0) else (0))) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000)

def ulongRemainder(v1, v2):
    dividend = ULong__toLong_impl(v1)
    divisor = ULong__toLong_impl(v2)
    if divisor.compareTo_wiekkq_k_(0) < 0:
        if ULong__compareTo_impl_2(v1, v2) < 0:
            tmp = v1
        else:
            tmp = ULong__minus_impl_2(v1, v2)
        
        return tmp
    
    if dividend.compareTo_wiekkq_k_(0) >= 0:
        return _ULong___init__impl_(dividend.rem_wiekkq_k_(divisor))
    
    quotient = ((((((((((((dividend & 0xffff_ffff_ffff_ffff) >> 1) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000) // divisor) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000) << 1) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000
    rem = (((dividend - ((((quotient * divisor) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000)) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000
    return _ULong___init__impl_((((rem - ((divisor) if (ULong__compareTo_impl_2(_ULong___init__impl_(rem), _ULong___init__impl_(divisor)) >= 0) else (0))) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000)

def ulongToDouble(v):
    return ((((((v & 0xffff_ffff_ffff_ffff) >> 11) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000).toDouble_0_k_() * 2048) + ((((v & 2047) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000).toDouble_0_k_()

def ulongToString(v):
    return ulongToString_0(v, 10)

def ulongToString_0(v, base):
    if v.compareTo_wiekkq_k_(0) >= 0:
        return toString_1(v, base)
    
    quotient = ((((((((((((v & 0xffff_ffff_ffff_ffff) >> 1) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000) // base) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000) << 1) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000
    rem = (((v - ((((quotient * base) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000)) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000
    if rem.compareTo_wiekkq_k_(base) >= 0:
        rem = (((rem - base) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000
        quotient = (((quotient + 1) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000
    
    return toString_1(quotient, base) + toString_1(rem, base)

def doubleToUInt(v):
    return (_UInt___init__impl_(0)) if (isNaN_0(v)) else ((Companion_getInstance_4()._get_MIN_VALUE__sv9k7v_k_()) if (v <= UInt__toDouble_impl(Companion_getInstance_4()._get_MIN_VALUE__sv9k7v_k_())) else ((Companion_getInstance_4()._get_MAX_VALUE__sv9k7v_k_()) if (v >= UInt__toDouble_impl(Companion_getInstance_4()._get_MAX_VALUE__sv9k7v_k_())) else ((toUInt_0(((v + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)) if (v <= kotlin_Double(visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OBJECT_GET_INSTANCE_FUNCTION_name_Companion_getInstance_visibility_public_modality_FINAL_______returnType_kotlin_Int_Companion._get_MAX_VALUE__0_k_())) else (UInt__plus_impl_1(toUInt_0((((v - visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OBJECT_GET_INSTANCE_FUNCTION_name_Companion_getInstance_visibility_public_modality_FINAL_______returnType_kotlin_Int_Companion._get_MAX_VALUE__0_k_()) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000), toUInt_0(visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OBJECT_GET_INSTANCE_FUNCTION_name_Companion_getInstance_visibility_public_modality_FINAL_______returnType_kotlin_Int_Companion._get_MAX_VALUE__0_k_()))))))

def doubleToULong(v):
    return (_ULong___init__impl_(Long(0, 0))) if (isNaN_0(v)) else ((Companion_getInstance_7()._get_MIN_VALUE__sha8jq_k_()) if (v <= ULong__toDouble_impl(Companion_getInstance_7()._get_MIN_VALUE__sha8jq_k_())) else ((Companion_getInstance_7()._get_MAX_VALUE__sha8jq_k_()) if (v >= ULong__toDouble_impl(Companion_getInstance_7()._get_MAX_VALUE__sha8jq_k_())) else ((toULong(((v + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000)) if (v < Companion_getInstance_19()._get_MAX_VALUE__0_k_().toDouble_0_k_()) else (ULong__plus_impl_2(toULong((((v - 9.223372036854776E18) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000), _ULong___init__impl_(Long(0, -2147483648)))))))

class ExperimentalUnsignedTypes(Annotation):
    def __init__(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class Annotation(Any):
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class CharSequence(Any):
    def _get_length__0_k_(self):
        pass
    
    def get_ha5a7z_k_(self, index):
        pass
    
    def subSequence_27zxwg_k_(self, startIndex, endIndex):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class Comparable(Any):
    def compareTo_2c5_k_(self, other):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class Iterator_3(Any):
    def next_0_k_(self):
        pass
    
    def hasNext_0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class ListIterator(Iterator_3):
    def next_0_k_(self):
        pass
    
    def hasNext_0_k_(self):
        pass
    
    def hasPrevious_0_k_(self):
        pass
    
    def previous_0_k_(self):
        pass
    
    def nextIndex_0_k_(self):
        pass
    
    def previousIndex_0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class MutableIterator(Iterator_3):
    def remove_sv8swh_k_(self):
        pass
    
    def next_0_k_(self):
        pass
    
    def hasNext_0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class MutableListIterator(ListIterator, MutableIterator):
    def next_0_k_(self):
        pass
    
    def hasNext_0_k_(self):
        pass
    
    def remove_sv8swh_k_(self):
        pass
    
    def set_iav7o_k_(self, element):
        pass
    
    def add_iav7o_k_(self, element):
        pass
    
    def hasPrevious_0_k_(self):
        pass
    
    def previous_0_k_(self):
        pass
    
    def nextIndex_0_k_(self):
        pass
    
    def previousIndex_0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class Number_0(Any):
    def __init__(self):
        pass
    
    def toDouble_0_k_(self):
        pass
    
    def toFloat_0_k_(self):
        pass
    
    def toLong_0_k_(self):
        pass
    
    def toInt_0_k_(self):
        pass
    
    def toChar_0_k_(self):
        pass
    
    def toShort_0_k_(self):
        pass
    
    def toByte_0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class SinceKotlin(Annotation):
    def __init__(self, version):
        pass
    
    def _get_version__0_k_(self):
        return self.version
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class Suppress(Annotation):
    def __init__(self, *names):
        pass
    
    def _get_names__0_k_(self):
        return self.names
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

DeprecationLevel_WARNING_instance = None
DeprecationLevel_ERROR_instance = None
DeprecationLevel_HIDDEN_instance = None
def values_5():
    return (DeprecationLevel_WARNING_getInstance(), DeprecationLevel_ERROR_getInstance(), DeprecationLevel_HIDDEN_getInstance())

def valueOf_5(value):
    if 'WARNING' == value:
        return DeprecationLevel_WARNING_getInstance()
    elif 'ERROR' == value:
        return DeprecationLevel_ERROR_getInstance()
    elif 'HIDDEN' == value:
        return DeprecationLevel_HIDDEN_getInstance()
    else:
        DeprecationLevel_initEntries()
        THROW_ISE()
    

DeprecationLevel_entriesInitialized = None
def DeprecationLevel_initEntries():
    global DeprecationLevel_entriesInitialized, DeprecationLevel_WARNING_instance, DeprecationLevel_ERROR_instance, DeprecationLevel_HIDDEN_instance
    if DeprecationLevel_entriesInitialized:
        return Unit_getInstance()
    
    DeprecationLevel_entriesInitialized = True
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    DeprecationLevel_WARNING_instance = Unit_getInstance()
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    DeprecationLevel_ERROR_instance = Unit_getInstance()
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    DeprecationLevel_HIDDEN_instance = Unit_getInstance()

class DeprecationLevel(Enum):
    def __init__(self):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    
    def _get_name__0_k_(self):
        pass
    
    def _get_ordinal__0_k_(self):
        pass
    
    def compareTo_ow4oyq_k_(self, other):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class PublishedApi(Annotation):
    def __init__(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class ParameterName(Annotation):
    def __init__(self, name):
        pass
    
    def _get_name__0_k_(self):
        return self.name
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class Deprecated(Annotation):
    def __init__(self, message, replaceWith, level):
        pass
    
    def _get_message__0_k_(self):
        return self.message
    
    def _get_replaceWith__0_k_(self):
        return self.replaceWith
    
    def _get_level__0_k_(self):
        return self.level
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class ReplaceWith(Annotation):
    def __init__(self, expression, *imports):
        pass
    
    def _get_expression__0_k_(self):
        return self.expression
    
    def _get_imports__0_k_(self):
        return self.imports
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class DeprecatedSinceKotlin(Annotation):
    def __init__(self, warningSince, errorSince, hiddenSince):
        pass
    
    def _get_warningSince__0_k_(self):
        return self.warningSince
    
    def _get_errorSince__0_k_(self):
        return self.errorSince
    
    def _get_hiddenSince__0_k_(self):
        return self.hiddenSince
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class ExtensionFunctionType(Annotation):
    def __init__(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class UnsafeVariance(Annotation):
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

class IntIterator(Iterator_3):
    def __init__(self):
        pass
    
    def next_0_k_(self):
        return self.nextInt_0_k_()
    
    def nextInt_0_k_(self):
        pass
    
    def hasNext_0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class ByteIterator(Iterator_3):
    def __init__(self):
        pass
    
    def next_0_k_(self):
        return self.nextByte_0_k_()
    
    def nextByte_0_k_(self):
        pass
    
    def hasNext_0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class DoubleIterator(Iterator_3):
    def __init__(self):
        pass
    
    def next_0_k_(self):
        return self.nextDouble_0_k_()
    
    def nextDouble_0_k_(self):
        pass
    
    def hasNext_0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class FloatIterator(Iterator_3):
    def __init__(self):
        pass
    
    def next_0_k_(self):
        return self.nextFloat_0_k_()
    
    def nextFloat_0_k_(self):
        pass
    
    def hasNext_0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class CharIterator(Iterator_3):
    def __init__(self):
        pass
    
    def next_0_k_(self):
        return self.nextChar_0_k_()
    
    def nextChar_0_k_(self):
        pass
    
    def hasNext_0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class LongIterator(Iterator_3):
    def __init__(self):
        pass
    
    def next_0_k_(self):
        return self.nextLong_0_k_()
    
    def nextLong_0_k_(self):
        pass
    
    def hasNext_0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class ShortIterator(Iterator_3):
    def __init__(self):
        pass
    
    def next_0_k_(self):
        return self.nextShort_0_k_()
    
    def nextShort_0_k_(self):
        pass
    
    def hasNext_0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class BooleanIterator(Iterator_3):
    def __init__(self):
        pass
    
    def next_0_k_(self):
        return self.nextBoolean_0_k_()
    
    def nextBoolean_0_k_(self):
        pass
    
    def hasNext_0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class IntProgressionIterator(IntIterator):
    def __init__(self, first, last, step):
        IntIterator.__init__(self)
        self.step = step
        self.finalElement = last
        self.hasNext = (first <= last) if (self._get_step__0_k_() > 0) else (first >= last)
        self.next = (first) if (self._get_hasNext__0_k_()) else (self._get_finalElement__0_k_())
    
    def _get_step__0_k_(self):
        return self.step
    
    def _get_finalElement__0_k_(self):
        return self.finalElement
    
    def _set_hasNext__rpwsgn_k_(self, _set___):
        self.hasNext = _set___
    
    def _get_hasNext__0_k_(self):
        return self.hasNext
    
    def _set_next__majfzk_k_(self, _set___):
        self.next = _set___
    
    def _get_next__0_k_(self):
        return self.next
    
    def hasNext_0_k_(self):
        return self._get_hasNext__0_k_()
    
    def nextInt_0_k_(self):
        value = self._get_next__0_k_()
        if value == self._get_finalElement__0_k_():
            if not self._get_hasNext__0_k_():
                raise NoSuchElementException_init__Create_()
            
            self._set_hasNext__rpwsgn_k_(False)
        else:
            tmp0_this = self
            tmp0_this._set_next__majfzk_k_((((tmp0_this._get_next__0_k_() + self._get_step__0_k_()) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
        
        return value
    
    def next_0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class CharProgressionIterator(CharIterator):
    def __init__(self, first, last, step):
        CharIterator.__init__(self)
        self.step = step
        self.finalElement = _get_code_(last)
        self.hasNext = (first.compareTo_wi8o78_k_(last) <= 0) if (self._get_step__0_k_() > 0) else (first.compareTo_wi8o78_k_(last) >= 0)
        self.next = (_get_code_(first)) if (self._get_hasNext__0_k_()) else (self._get_finalElement__0_k_())
    
    def _get_step__0_k_(self):
        return self.step
    
    def _get_finalElement__0_k_(self):
        return self.finalElement
    
    def _set_hasNext__rpwsgn_k_(self, _set___):
        self.hasNext = _set___
    
    def _get_hasNext__0_k_(self):
        return self.hasNext
    
    def _set_next__majfzk_k_(self, _set___):
        self.next = _set___
    
    def _get_next__0_k_(self):
        return self.next
    
    def hasNext_0_k_(self):
        return self._get_hasNext__0_k_()
    
    def nextChar_0_k_(self):
        value = self._get_next__0_k_()
        if value == self._get_finalElement__0_k_():
            if not self._get_hasNext__0_k_():
                raise NoSuchElementException_init__Create_()
            
            self._set_hasNext__rpwsgn_k_(False)
        else:
            tmp0_this = self
            tmp0_this._set_next__majfzk_k_((((tmp0_this._get_next__0_k_() + self._get_step__0_k_()) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
        
        return numberToChar(value)
    
    def next_0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class LongProgressionIterator(LongIterator):
    def __init__(self, first, last, step):
        LongIterator.__init__(self)
        self.step = step
        self.finalElement = last
        self.hasNext = (first.compareTo_wiekkq_k_(last) <= 0) if (self._get_step__0_k_().compareTo_wiekkq_k_(0) > 0) else (first.compareTo_wiekkq_k_(last) >= 0)
        self.next = (first) if (self._get_hasNext__0_k_()) else (self._get_finalElement__0_k_())
    
    def _get_step__0_k_(self):
        return self.step
    
    def _get_finalElement__0_k_(self):
        return self.finalElement
    
    def _set_hasNext__rpwsgn_k_(self, _set___):
        self.hasNext = _set___
    
    def _get_hasNext__0_k_(self):
        return self.hasNext
    
    def _set_next__kdfck9_k_(self, _set___):
        self.next = _set___
    
    def _get_next__0_k_(self):
        return self.next
    
    def hasNext_0_k_(self):
        return self._get_hasNext__0_k_()
    
    def nextLong_0_k_(self):
        value = self._get_next__0_k_()
        if value == self._get_finalElement__0_k_():
            if not self._get_hasNext__0_k_():
                raise NoSuchElementException_init__Create_()
            
            self._set_hasNext__rpwsgn_k_(False)
        else:
            tmp0_this = self
            tmp0_this._set_next__kdfck9_k_((((tmp0_this._get_next__0_k_() + self._get_step__0_k_()) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000)
        
        return value
    
    def next_0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class Companion_12(Any):
    def __init__(self):
        global Companion_instance
        Companion_instance = self
    
    def fromClosedRange_fcwjfj_k_(self, rangeStart, rangeEnd, step):
        return IntProgression(rangeStart, rangeEnd, step)
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

Companion_instance = None
def Companion_getInstance_11():
    if Companion_instance == None:
        Companion_12()
    
    return Companion_instance

class IntProgression(Iterable):
    def __init__(self, start, endInclusive, step):
        Companion_getInstance_11()
        if step == 0:
            raise IllegalArgumentException_init__Create__0('Step must be non-zero.')
        
        if step == visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OBJECT_GET_INSTANCE_FUNCTION_name_Companion_getInstance_visibility_public_modality_FINAL_______returnType_kotlin_Int_Companion._get_MIN_VALUE__0_k_():
            raise IllegalArgumentException_init__Create__0('Step must be greater than Int.MIN_VALUE to avoid overflow on negation.')
        
        self.first = start
        self.last = getProgressionLastElement_1(start, endInclusive, step)
        self.step = step
    
    def _get_first__0_k_(self):
        return self.first
    
    def _get_last__0_k_(self):
        return self.last
    
    def _get_step__0_k_(self):
        return self.step
    
    def iterator_0_k_(self):
        return IntProgressionIterator(self._get_first__0_k_(), self._get_last__0_k_(), self._get_step__0_k_())
    
    def isEmpty_0_k_(self):
        return (self._get_first__0_k_() > self._get_last__0_k_()) if (self._get_step__0_k_() > 0) else (self._get_first__0_k_() < self._get_last__0_k_())
    
    def equals(self, other):
        if isinstance(other, IntProgression):
            tmp = (True) if ((kotlin_ranges_IntProgression(other).isEmpty_0_k_()) if (self.isEmpty_0_k_()) else (False)) else ((self._get_step__0_k_() == kotlin_ranges_IntProgression(other)._get_step__0_k_()) if ((self._get_last__0_k_() == kotlin_ranges_IntProgression(other)._get_last__0_k_()) if (self._get_first__0_k_() == kotlin_ranges_IntProgression(other)._get_first__0_k_()) else (False)) else (False))
        elif True:
            tmp = False
        
        return tmp
    
    def hashCode(self):
        return (-1) if (self.isEmpty_0_k_()) else ((((imul(31, (((imul(31, self._get_first__0_k_()) + self._get_last__0_k_()) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000) + self._get_step__0_k_()) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
    
    def toString(self):
        return ((((str(self._get_first__0_k_()) + str('..')) + str(self._get_last__0_k_())) + str(' step ')) + str(self._get_step__0_k_())) if (self._get_step__0_k_() > 0) else ((((str(self._get_first__0_k_()) + str(' downTo ')) + str(self._get_last__0_k_())) + str(' step ')) + str(((-self._get_step__0_k_() + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000))
    

class Companion_13(Any):
    def __init__(self):
        global Companion_instance
        Companion_instance = self
    
    def fromClosedRange_gtcn47_k_(self, rangeStart, rangeEnd, step):
        return CharProgression(rangeStart, rangeEnd, step)
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

Companion_instance = None
def Companion_getInstance_12():
    if Companion_instance == None:
        Companion_13()
    
    return Companion_instance

class CharProgression(Iterable):
    def __init__(self, start, endInclusive, step):
        Companion_getInstance_12()
        if step == 0:
            raise IllegalArgumentException_init__Create__0('Step must be non-zero.')
        
        if step == visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OBJECT_GET_INSTANCE_FUNCTION_name_Companion_getInstance_visibility_public_modality_FINAL_______returnType_kotlin_Int_Companion._get_MIN_VALUE__0_k_():
            raise IllegalArgumentException_init__Create__0('Step must be greater than Int.MIN_VALUE to avoid overflow on negation.')
        
        self.first = start
        self.last = numberToChar(getProgressionLastElement_1(_get_code_(start), _get_code_(endInclusive), step))
        self.step = step
    
    def _get_first__0_k_(self):
        return self.first
    
    def _get_last__0_k_(self):
        return self.last
    
    def _get_step__0_k_(self):
        return self.step
    
    def iterator_0_k_(self):
        return CharProgressionIterator(self._get_first__0_k_(), self._get_last__0_k_(), self._get_step__0_k_())
    
    def isEmpty_0_k_(self):
        return (self._get_first__0_k_().compareTo_wi8o78_k_(self._get_last__0_k_()) > 0) if (self._get_step__0_k_() > 0) else (self._get_first__0_k_().compareTo_wi8o78_k_(self._get_last__0_k_()) < 0)
    
    def equals(self, other):
        if isinstance(other, CharProgression):
            tmp = (True) if ((kotlin_ranges_CharProgression(other).isEmpty_0_k_()) if (self.isEmpty_0_k_()) else (False)) else ((self._get_step__0_k_() == kotlin_ranges_CharProgression(other)._get_step__0_k_()) if ((self._get_last__0_k_() == kotlin_ranges_CharProgression(other)._get_last__0_k_()) if (self._get_first__0_k_() == kotlin_ranges_CharProgression(other)._get_first__0_k_()) else (False)) else (False))
        elif True:
            tmp = False
        
        return tmp
    
    def hashCode(self):
        return (-1) if (self.isEmpty_0_k_()) else ((((imul(31, (((imul(31, _get_code_(self._get_first__0_k_())) + _get_code_(self._get_last__0_k_())) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000) + self._get_step__0_k_()) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
    
    def toString(self):
        return ((((str(self._get_first__0_k_()) + str('..')) + str(self._get_last__0_k_())) + str(' step ')) + str(self._get_step__0_k_())) if (self._get_step__0_k_() > 0) else ((((str(self._get_first__0_k_()) + str(' downTo ')) + str(self._get_last__0_k_())) + str(' step ')) + str(((-self._get_step__0_k_() + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000))
    

class Companion_14(Any):
    def __init__(self):
        global Companion_instance
        Companion_instance = self
    
    def fromClosedRange_k3cbgi_k_(self, rangeStart, rangeEnd, step):
        return LongProgression(rangeStart, rangeEnd, step)
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

Companion_instance = None
def Companion_getInstance_13():
    if Companion_instance == None:
        Companion_14()
    
    return Companion_instance

class LongProgression(Iterable):
    def __init__(self, start, endInclusive, step):
        Companion_getInstance_13()
        if step == 0:
            raise IllegalArgumentException_init__Create__0('Step must be non-zero.')
        
        if step == Companion_getInstance_19()._get_MIN_VALUE__0_k_():
            raise IllegalArgumentException_init__Create__0('Step must be greater than Long.MIN_VALUE to avoid overflow on negation.')
        
        self.first = start
        self.last = getProgressionLastElement_2(start, endInclusive, step)
        self.step = step
    
    def _get_first__0_k_(self):
        return self.first
    
    def _get_last__0_k_(self):
        return self.last
    
    def _get_step__0_k_(self):
        return self.step
    
    def iterator_0_k_(self):
        return LongProgressionIterator(self._get_first__0_k_(), self._get_last__0_k_(), self._get_step__0_k_())
    
    def isEmpty_0_k_(self):
        return (self._get_first__0_k_().compareTo_wiekkq_k_(self._get_last__0_k_()) > 0) if (self._get_step__0_k_().compareTo_wiekkq_k_(0) > 0) else (self._get_first__0_k_().compareTo_wiekkq_k_(self._get_last__0_k_()) < 0)
    
    def equals(self, other):
        if isinstance(other, LongProgression):
            tmp = (True) if ((kotlin_ranges_LongProgression(other).isEmpty_0_k_()) if (self.isEmpty_0_k_()) else (False)) else ((self._get_step__0_k_() == kotlin_ranges_LongProgression(other)._get_step__0_k_()) if ((self._get_last__0_k_() == kotlin_ranges_LongProgression(other)._get_last__0_k_()) if (self._get_first__0_k_() == kotlin_ranges_LongProgression(other)._get_first__0_k_()) else (False)) else (False))
        elif True:
            tmp = False
        
        return tmp
    
    def hashCode(self):
        return (-1) if (self.isEmpty_0_k_()) else ((((((((31 * (((((31 * ((((self._get_first__0_k_() ^ (((((self._get_first__0_k_() & 0xffff_ffff_ffff_ffff) >> 32) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000)) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000)) + ((((self._get_last__0_k_() ^ (((((self._get_last__0_k_() & 0xffff_ffff_ffff_ffff) >> 32) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000)) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000)) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000)) + ((((self._get_step__0_k_() ^ (((((self._get_step__0_k_() & 0xffff_ffff_ffff_ffff) >> 32) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000)) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000)) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
    
    def toString(self):
        return ((((str(self._get_first__0_k_()) + str('..')) + str(self._get_last__0_k_())) + str(' step ')) + str(self._get_step__0_k_())) if (self._get_step__0_k_().compareTo_wiekkq_k_(0) > 0) else ((((str(self._get_first__0_k_()) + str(' downTo ')) + str(self._get_last__0_k_())) + str(' step ')) + str(((-self._get_step__0_k_() + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000))
    

class ClosedRange(Any):
    def _get_start__0_k_(self):
        pass
    
    def _get_endInclusive__0_k_(self):
        pass
    
    def contains_2c5_k_(self, value):
        return (compareTo_0(value, self._get_endInclusive__0_k_()) <= 0) if (compareTo_0(value, self._get_start__0_k_()) >= 0) else (False)
    
    def isEmpty_0_k_(self):
        return compareTo_0(self._get_start__0_k_(), self._get_endInclusive__0_k_()) > 0
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class Companion_15(Any):
    def __init__(self):
        global Companion_instance
        Companion_instance = self
        self.EMPTY = IntRange(1, 0)
    
    def _get_EMPTY__0_k_(self):
        return self.EMPTY
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

Companion_instance = None
def Companion_getInstance_14():
    if Companion_instance == None:
        Companion_15()
    
    return Companion_instance

class IntRange(IntProgression, ClosedRange):
    def __init__(self, start, endInclusive):
        Companion_getInstance_14()
        IntProgression.__init__(self, start, endInclusive, 1)
    
    def _get_start__0_k_(self):
        return self._get_first__0_k_()
    
    def _get_endInclusive__0_k_(self):
        return self._get_last__0_k_()
    
    def contains_ha5a7z_k_(self, value):
        return (value <= self._get_last__0_k_()) if (self._get_first__0_k_() <= value) else (False)
    
    def isEmpty_0_k_(self):
        return self._get_first__0_k_() > self._get_last__0_k_()
    
    def equals(self, other):
        if isinstance(other, IntRange):
            tmp = (True) if ((kotlin_ranges_IntRange(other).isEmpty_0_k_()) if (self.isEmpty_0_k_()) else (False)) else ((self._get_last__0_k_() == kotlin_ranges_IntRange(other)._get_last__0_k_()) if (self._get_first__0_k_() == kotlin_ranges_IntRange(other)._get_first__0_k_()) else (False))
        elif True:
            tmp = False
        
        return tmp
    
    def hashCode(self):
        return (-1) if (self.isEmpty_0_k_()) else ((((imul(31, self._get_first__0_k_()) + self._get_last__0_k_()) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
    
    def toString(self):
        return (str(self._get_first__0_k_()) + str('..')) + str(self._get_last__0_k_())
    
    def _get_first__0_k_(self):
        pass
    
    def _get_last__0_k_(self):
        pass
    
    def _get_step__0_k_(self):
        pass
    
    def iterator_0_k_(self):
        pass
    

class Companion_16(Any):
    def __init__(self):
        global Companion_instance
        Companion_instance = self
        self.EMPTY = CharRange(numberToChar(1), numberToChar(0))
    
    def _get_EMPTY__0_k_(self):
        return self.EMPTY
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

Companion_instance = None
def Companion_getInstance_15():
    if Companion_instance == None:
        Companion_16()
    
    return Companion_instance

class CharRange(CharProgression, ClosedRange):
    def __init__(self, start, endInclusive):
        Companion_getInstance_15()
        CharProgression.__init__(self, start, endInclusive, 1)
    
    def _get_start__0_k_(self):
        return self._get_first__0_k_()
    
    def _get_endInclusive__0_k_(self):
        return self._get_last__0_k_()
    
    def contains_wi8o78_k_(self, value):
        return (value.compareTo_wi8o78_k_(self._get_last__0_k_()) <= 0) if (self._get_first__0_k_().compareTo_wi8o78_k_(value) <= 0) else (False)
    
    def isEmpty_0_k_(self):
        return self._get_first__0_k_().compareTo_wi8o78_k_(self._get_last__0_k_()) > 0
    
    def equals(self, other):
        if isinstance(other, CharRange):
            tmp = (True) if ((kotlin_ranges_CharRange(other).isEmpty_0_k_()) if (self.isEmpty_0_k_()) else (False)) else ((self._get_last__0_k_() == kotlin_ranges_CharRange(other)._get_last__0_k_()) if (self._get_first__0_k_() == kotlin_ranges_CharRange(other)._get_first__0_k_()) else (False))
        elif True:
            tmp = False
        
        return tmp
    
    def hashCode(self):
        return (-1) if (self.isEmpty_0_k_()) else ((((imul(31, _get_code_(self._get_first__0_k_())) + _get_code_(self._get_last__0_k_())) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
    
    def toString(self):
        return (str(self._get_first__0_k_()) + str('..')) + str(self._get_last__0_k_())
    
    def _get_first__0_k_(self):
        pass
    
    def _get_last__0_k_(self):
        pass
    
    def _get_step__0_k_(self):
        pass
    
    def iterator_0_k_(self):
        pass
    

class Companion_17(Any):
    def __init__(self):
        global Companion_instance
        Companion_instance = self
        self.EMPTY = LongRange(1, 0)
    
    def _get_EMPTY__0_k_(self):
        return self.EMPTY
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

Companion_instance = None
def Companion_getInstance_16():
    if Companion_instance == None:
        Companion_17()
    
    return Companion_instance

class LongRange(LongProgression, ClosedRange):
    def __init__(self, start, endInclusive):
        Companion_getInstance_16()
        LongProgression.__init__(self, start, endInclusive, 1)
    
    def _get_start__0_k_(self):
        return self._get_first__0_k_()
    
    def _get_endInclusive__0_k_(self):
        return self._get_last__0_k_()
    
    def contains_wiekkq_k_(self, value):
        return (value.compareTo_wiekkq_k_(self._get_last__0_k_()) <= 0) if (self._get_first__0_k_().compareTo_wiekkq_k_(value) <= 0) else (False)
    
    def isEmpty_0_k_(self):
        return self._get_first__0_k_().compareTo_wiekkq_k_(self._get_last__0_k_()) > 0
    
    def equals(self, other):
        if isinstance(other, LongRange):
            tmp = (True) if ((kotlin_ranges_LongRange(other).isEmpty_0_k_()) if (self.isEmpty_0_k_()) else (False)) else ((self._get_last__0_k_() == kotlin_ranges_LongRange(other)._get_last__0_k_()) if (self._get_first__0_k_() == kotlin_ranges_LongRange(other)._get_first__0_k_()) else (False))
        elif True:
            tmp = False
        
        return tmp
    
    def hashCode(self):
        return (-1) if (self.isEmpty_0_k_()) else ((((((((31 * ((((self._get_first__0_k_() ^ (((((self._get_first__0_k_() & 0xffff_ffff_ffff_ffff) >> 32) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000)) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000)) + ((((self._get_last__0_k_() ^ (((((self._get_last__0_k_() & 0xffff_ffff_ffff_ffff) >> 32) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000)) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000)) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
    
    def toString(self):
        return (str(self._get_first__0_k_()) + str('..')) + str(self._get_last__0_k_())
    
    def _get_first__0_k_(self):
        pass
    
    def _get_last__0_k_(self):
        pass
    
    def _get_step__0_k_(self):
        pass
    
    def iterator_0_k_(self):
        pass
    

class Unit(Any):
    def __init__(self):
        global Unit_instance
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

class Target(Annotation):
    def __init__(self, *allowedTargets):
        pass
    
    def _get_allowedTargets__0_k_(self):
        return self.allowedTargets
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

AnnotationTarget_CLASS_instance = None
AnnotationTarget_ANNOTATION_CLASS_instance = None
AnnotationTarget_TYPE_PARAMETER_instance = None
AnnotationTarget_PROPERTY_instance = None
AnnotationTarget_FIELD_instance = None
AnnotationTarget_LOCAL_VARIABLE_instance = None
AnnotationTarget_VALUE_PARAMETER_instance = None
AnnotationTarget_CONSTRUCTOR_instance = None
AnnotationTarget_FUNCTION_instance = None
AnnotationTarget_PROPERTY_GETTER_instance = None
AnnotationTarget_PROPERTY_SETTER_instance = None
AnnotationTarget_TYPE_instance = None
AnnotationTarget_EXPRESSION_instance = None
AnnotationTarget_FILE_instance = None
AnnotationTarget_TYPEALIAS_instance = None
def values_6():
    return (AnnotationTarget_CLASS_getInstance(), AnnotationTarget_ANNOTATION_CLASS_getInstance(), AnnotationTarget_TYPE_PARAMETER_getInstance(), AnnotationTarget_PROPERTY_getInstance(), AnnotationTarget_FIELD_getInstance(), AnnotationTarget_LOCAL_VARIABLE_getInstance(), AnnotationTarget_VALUE_PARAMETER_getInstance(), AnnotationTarget_CONSTRUCTOR_getInstance(), AnnotationTarget_FUNCTION_getInstance(), AnnotationTarget_PROPERTY_GETTER_getInstance(), AnnotationTarget_PROPERTY_SETTER_getInstance(), AnnotationTarget_TYPE_getInstance(), AnnotationTarget_EXPRESSION_getInstance(), AnnotationTarget_FILE_getInstance(), AnnotationTarget_TYPEALIAS_getInstance())

def valueOf_6(value):
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
    

AnnotationTarget_entriesInitialized = None
def AnnotationTarget_initEntries():
    global AnnotationTarget_entriesInitialized, AnnotationTarget_CLASS_instance, AnnotationTarget_ANNOTATION_CLASS_instance, AnnotationTarget_TYPE_PARAMETER_instance, AnnotationTarget_PROPERTY_instance, AnnotationTarget_FIELD_instance, AnnotationTarget_LOCAL_VARIABLE_instance, AnnotationTarget_VALUE_PARAMETER_instance, AnnotationTarget_CONSTRUCTOR_instance, AnnotationTarget_FUNCTION_instance, AnnotationTarget_PROPERTY_GETTER_instance, AnnotationTarget_PROPERTY_SETTER_instance, AnnotationTarget_TYPE_instance, AnnotationTarget_EXPRESSION_instance, AnnotationTarget_FILE_instance, AnnotationTarget_TYPEALIAS_instance
    if AnnotationTarget_entriesInitialized:
        return Unit_getInstance()
    
    AnnotationTarget_entriesInitialized = True
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    AnnotationTarget_CLASS_instance = Unit_getInstance()
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    AnnotationTarget_ANNOTATION_CLASS_instance = Unit_getInstance()
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    AnnotationTarget_TYPE_PARAMETER_instance = Unit_getInstance()
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    AnnotationTarget_PROPERTY_instance = Unit_getInstance()
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    AnnotationTarget_FIELD_instance = Unit_getInstance()
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    AnnotationTarget_LOCAL_VARIABLE_instance = Unit_getInstance()
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    AnnotationTarget_VALUE_PARAMETER_instance = Unit_getInstance()
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    AnnotationTarget_CONSTRUCTOR_instance = Unit_getInstance()
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    AnnotationTarget_FUNCTION_instance = Unit_getInstance()
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    AnnotationTarget_PROPERTY_GETTER_instance = Unit_getInstance()
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    AnnotationTarget_PROPERTY_SETTER_instance = Unit_getInstance()
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    AnnotationTarget_TYPE_instance = Unit_getInstance()
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    AnnotationTarget_EXPRESSION_instance = Unit_getInstance()
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    AnnotationTarget_FILE_instance = Unit_getInstance()
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    AnnotationTarget_TYPEALIAS_instance = Unit_getInstance()

class AnnotationTarget(Enum):
    def __init__(self):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    
    def _get_name__0_k_(self):
        pass
    
    def _get_ordinal__0_k_(self):
        pass
    
    def compareTo_h5tgwh_k_(self, other):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class MustBeDocumented(Annotation):
    def __init__(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class Retention(Annotation):
    def __init__(self, value):
        pass
    
    def _get_value__0_k_(self):
        return self.value
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

AnnotationRetention_SOURCE_instance = None
AnnotationRetention_BINARY_instance = None
AnnotationRetention_RUNTIME_instance = None
def values_7():
    return (AnnotationRetention_SOURCE_getInstance(), AnnotationRetention_BINARY_getInstance(), AnnotationRetention_RUNTIME_getInstance())

def valueOf_7(value):
    if 'SOURCE' == value:
        return AnnotationRetention_SOURCE_getInstance()
    elif 'BINARY' == value:
        return AnnotationRetention_BINARY_getInstance()
    elif 'RUNTIME' == value:
        return AnnotationRetention_RUNTIME_getInstance()
    else:
        AnnotationRetention_initEntries()
        THROW_ISE()
    

AnnotationRetention_entriesInitialized = None
def AnnotationRetention_initEntries():
    global AnnotationRetention_entriesInitialized, AnnotationRetention_SOURCE_instance, AnnotationRetention_BINARY_instance, AnnotationRetention_RUNTIME_instance
    if AnnotationRetention_entriesInitialized:
        return Unit_getInstance()
    
    AnnotationRetention_entriesInitialized = True
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    AnnotationRetention_SOURCE_instance = Unit_getInstance()
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    AnnotationRetention_BINARY_instance = Unit_getInstance()
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    AnnotationRetention_RUNTIME_instance = Unit_getInstance()

class AnnotationRetention(Enum):
    def __init__(self):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrEnumConstructorCallImpl
    
    def _get_name__0_k_(self):
        pass
    
    def _get_ordinal__0_k_(self):
        pass
    
    def compareTo_rvtl42_k_(self, other):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class Repeatable(Annotation):
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

def getProgressionLastElement_1(start, end, step):
    if step > 0:
        tmp = (end) if (start >= end) else ((((end - differenceModulo_1(end, start, step)) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
    elif step < 0:
        tmp = (end) if (start <= end) else ((((end + differenceModulo_1(start, end, ((-step + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
    else:
        raise IllegalArgumentException_init__Create__0('Step is zero.')
    
    return tmp

def getProgressionLastElement_2(start, end, step):
    if step.compareTo_wiekkq_k_(0) > 0:
        tmp = (end) if (start.compareTo_wiekkq_k_(end) >= 0) else ((((end - differenceModulo_2(end, start, step)) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000)
    elif step.compareTo_wiekkq_k_(0) < 0:
        tmp = (end) if (start.compareTo_wiekkq_k_(end) <= 0) else ((((end + differenceModulo_2(start, end, ((-step + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000)) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000)
    else:
        raise IllegalArgumentException_init__Create__0('Step is zero.')
    
    return tmp

def differenceModulo_1(a, b, c):
    return mod((((mod(a, c) - mod(b, c)) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000, c)

def differenceModulo_2(a, b, c):
    return mod_0((((mod_0(a, c) - mod_0(b, c)) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000, c)

def mod(a, b):
    mod = a % b
    return (mod) if (mod >= 0) else ((((mod + b) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)

def mod_0(a, b):
    mod = a.rem_wiekkq_k_(b)
    return (mod) if (mod.compareTo_wiekkq_k_(0) >= 0) else ((((mod + b) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000)

class ByteCompanionObject_0(Any):
    def __init__(self):
        global ByteCompanionObject_instance
        ByteCompanionObject_instance = self
        self.MIN_VALUE = -128
        self.MAX_VALUE = 127
        self.SIZE_BYTES = 1
        self.SIZE_BITS = 8
    
    def _get_MIN_VALUE__0_k_(self):
        return self.MIN_VALUE
    
    def _get_MAX_VALUE__0_k_(self):
        return self.MAX_VALUE
    
    def _get_SIZE_BYTES__0_k_(self):
        return self.SIZE_BYTES
    
    def _get_SIZE_BITS__0_k_(self):
        return self.SIZE_BITS
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

ByteCompanionObject_instance = None
def ByteCompanionObject_getInstance():
    if ByteCompanionObject_instance == None:
        ByteCompanionObject_0()
    
    return ByteCompanionObject_instance

class ShortCompanionObject_0(Any):
    def __init__(self):
        global ShortCompanionObject_instance
        ShortCompanionObject_instance = self
        self.MIN_VALUE = -32768
        self.MAX_VALUE = 32767
        self.SIZE_BYTES = 2
        self.SIZE_BITS = 16
    
    def _get_MIN_VALUE__0_k_(self):
        return self.MIN_VALUE
    
    def _get_MAX_VALUE__0_k_(self):
        return self.MAX_VALUE
    
    def _get_SIZE_BYTES__0_k_(self):
        return self.SIZE_BYTES
    
    def _get_SIZE_BITS__0_k_(self):
        return self.SIZE_BITS
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

ShortCompanionObject_instance = None
def ShortCompanionObject_getInstance():
    if ShortCompanionObject_instance == None:
        ShortCompanionObject_0()
    
    return ShortCompanionObject_instance

class IntCompanionObject_0(Any):
    def __init__(self):
        global IntCompanionObject_instance
        IntCompanionObject_instance = self
        self.MIN_VALUE = -2147483648
        self.MAX_VALUE = 2147483647
        self.SIZE_BYTES = 4
        self.SIZE_BITS = 32
    
    def _get_MIN_VALUE__0_k_(self):
        return self.MIN_VALUE
    
    def _get_MAX_VALUE__0_k_(self):
        return self.MAX_VALUE
    
    def _get_SIZE_BYTES__0_k_(self):
        return self.SIZE_BYTES
    
    def _get_SIZE_BITS__0_k_(self):
        return self.SIZE_BITS
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

IntCompanionObject_instance = None
def IntCompanionObject_getInstance():
    if IntCompanionObject_instance == None:
        IntCompanionObject_0()
    
    return IntCompanionObject_instance

class FloatCompanionObject_0(Any):
    def __init__(self):
        global FloatCompanionObject_instance
        FloatCompanionObject_instance = self
        self.MIN_VALUE = 1.4E-45
        self.MAX_VALUE = 3.4028235E38
        self.POSITIVE_INFINITY = Infinity
        self.NEGATIVE_INFINITY = -Infinity
        self.NaN = NaN
        self.SIZE_BYTES = 4
        self.SIZE_BITS = 32
    
    def _get_MIN_VALUE__0_k_(self):
        return self.MIN_VALUE
    
    def _get_MAX_VALUE__0_k_(self):
        return self.MAX_VALUE
    
    def _get_POSITIVE_INFINITY__0_k_(self):
        return self.POSITIVE_INFINITY
    
    def _get_NEGATIVE_INFINITY__0_k_(self):
        return self.NEGATIVE_INFINITY
    
    def _get_NaN__0_k_(self):
        return self.NaN
    
    def _get_SIZE_BYTES__0_k_(self):
        return self.SIZE_BYTES
    
    def _get_SIZE_BITS__0_k_(self):
        return self.SIZE_BITS
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

FloatCompanionObject_instance = None
def FloatCompanionObject_getInstance():
    if FloatCompanionObject_instance == None:
        FloatCompanionObject_0()
    
    return FloatCompanionObject_instance

class DoubleCompanionObject_0(Any):
    def __init__(self):
        global DoubleCompanionObject_instance
        DoubleCompanionObject_instance = self
        self.MIN_VALUE = 4.9E-324
        self.MAX_VALUE = 1.7976931348623157E308
        self.POSITIVE_INFINITY = Infinity
        self.NEGATIVE_INFINITY = -Infinity
        self.NaN = NaN
        self.SIZE_BYTES = 8
        self.SIZE_BITS = 64
    
    def _get_MIN_VALUE__0_k_(self):
        return self.MIN_VALUE
    
    def _get_MAX_VALUE__0_k_(self):
        return self.MAX_VALUE
    
    def _get_POSITIVE_INFINITY__0_k_(self):
        return self.POSITIVE_INFINITY
    
    def _get_NEGATIVE_INFINITY__0_k_(self):
        return self.NEGATIVE_INFINITY
    
    def _get_NaN__0_k_(self):
        return self.NaN
    
    def _get_SIZE_BYTES__0_k_(self):
        return self.SIZE_BYTES
    
    def _get_SIZE_BITS__0_k_(self):
        return self.SIZE_BITS
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

DoubleCompanionObject_instance = None
def DoubleCompanionObject_getInstance():
    if DoubleCompanionObject_instance == None:
        DoubleCompanionObject_0()
    
    return DoubleCompanionObject_instance

class StringCompanionObject(Any):
    def __init__(self):
        global StringCompanionObject_instance
        StringCompanionObject_instance = self
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

StringCompanionObject_instance = None
def StringCompanionObject_getInstance():
    if StringCompanionObject_instance == None:
        StringCompanionObject()
    
    return StringCompanionObject_instance

class BooleanCompanionObject(Any):
    def __init__(self):
        global BooleanCompanionObject_instance
        BooleanCompanionObject_instance = self
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

BooleanCompanionObject_instance = None
def BooleanCompanionObject_getInstance():
    if BooleanCompanionObject_instance == None:
        BooleanCompanionObject()
    
    return BooleanCompanionObject_instance

class Comparator(Any):
    def compare(self, a, b):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class JsName(Annotation):
    def __init__(self, name):
        pass
    
    def _get_name__0_k_(self):
        return self.name
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def toTypedArray(self):
    return copyToArray_0(self)

def copyToArray_0(collection):
    return (unsafeCast(asDynamic(collection).toArray())) if (asDynamic(collection).toArray is not undefined) else (unsafeCast_0(copyToArrayImpl_0(collection)))

def copyToArrayImpl_0(collection):
    array = emptyArray()
    iterator = collection.iterator_0_k_()
    while iterator.hasNext_0_k_():
        asDynamic(array).push(iterator.next_0_k_())
    
    return array

def arrayCopy_0(source, destination, destinationOffset, startIndex, endIndex):
    Companion_getInstance().checkRangeIndexes_zd700_k_(startIndex, endIndex, len(source))
    rangeSize = (((endIndex - startIndex) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
    Companion_getInstance().checkRangeIndexes_zd700_k_(destinationOffset, (((destinationOffset + rangeSize) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000, len(destination))
    if js('ArrayBuffer').isView(destination) and js('ArrayBuffer').isView(source):
        subrange = asDynamic(source).subarray(startIndex, endIndex)
        asDynamic(destination).set(subrange, destinationOffset)
    elif (True) if (not (source is destination)) else (destinationOffset <= startIndex):
        tmp0_iterator = until(0, rangeSize).iterator_0_k_()
        while tmp0_iterator.hasNext_0_k_():
            index = tmp0_iterator.next_0_k_()
            destination.__setitem__((((destinationOffset + index) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000, source[(((startIndex + index) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000])
        
    else:
        tmp1_iterator = downTo((((rangeSize - 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000, 0).iterator_0_k_()
        while tmp1_iterator.hasNext_0_k_():
            index = tmp1_iterator.next_0_k_()
            destination.__setitem__((((destinationOffset + index) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000, source[(((startIndex + index) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000])
        
    

def copyToArrayImpl_1(collection, array):
    if len(array) < collection._get_size__0_k_():
        return unsafeCast_0(copyToArrayImpl_0(collection))
    
    iterator = collection.iterator_0_k_()
    index = 0
    while iterator.hasNext_0_k_():
        tmp0 = index
        index = (((tmp0 + 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
        array.__setitem__(tmp0, unsafeCast_0(iterator.next_0_k_()))
    
    if index < len(array):
        array.__setitem__(index, unsafeCast_0(None))
    
    return array

class MutableCollection:
    pass

class AbstractMutableCollection(AbstractCollection, MutableCollection):
    def __init__(self):
        AbstractCollection.__init__(self)
    
    def add_2bq_k_(self, element):
        pass
    
    def remove_2bq_k_(self, element):
        self.checkIsMutable_sv8swh_k_()
        iterator = self.iterator_0_k_()
        while iterator.hasNext_0_k_():
            if iterator.next_0_k_() == element:
                iterator.remove_sv8swh_k_()
                return True
            
        
        return False
    
    def addAll_dxd4eo_k_(self, elements):
        self.checkIsMutable_sv8swh_k_()
        modified = False
        tmp0_iterator = elements.iterator_0_k_()
        while tmp0_iterator.hasNext_0_k_():
            element = tmp0_iterator.next_0_k_()
            if self.add_2bq_k_(element):
                modified = True
            
        
        return modified
    
    def removeAll_dxd4eo_k_(self, elements):
        self.checkIsMutable_sv8swh_k_()
        return removeAll_0((kotlin_collections_MutableIterable_E_(self)) if (isInterface(self, MutableIterable)) else (THROW_CCE()), lambda it: elements.contains_2bq_k_(it))
    
    def retainAll_dxd4eo_k_(self, elements):
        self.checkIsMutable_sv8swh_k_()
        return removeAll_0((kotlin_collections_MutableIterable_E_(self)) if (isInterface(self, MutableIterable)) else (THROW_CCE()), lambda it: not elements.contains_2bq_k_(it))
    
    def clear_sv8swh_k_(self):
        self.checkIsMutable_sv8swh_k_()
        iterator = self.iterator_0_k_()
        while iterator.hasNext_0_k_():
            iterator.next_0_k_()
            Unit_getInstance()
            iterator.remove_sv8swh_k_()
        
    
    def toJSON(self):
        return self.toArray()
    
    def checkIsMutable_sv8swh_k_(self):
        pass
    
    def _get_size__0_k_(self):
        pass
    
    def iterator_0_k_(self):
        pass
    
    def contains_2bq_k_(self, element):
        pass
    
    def containsAll_dxd4eo_k_(self, elements):
        pass
    
    def isEmpty_0_k_(self):
        pass
    
    def toString(self):
        pass
    
    def toArray(self):
        pass
    
    def toArray_gjotr5_k_(self, array):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    

class IteratorImpl_0(MutableIterator):
    def __init__(self):
        self.index = 0
        self.last = -1
    
    def _set_index__majfzk_k_(self, _set___):
        self.index = _set___
    
    def _get_index__0_k_(self):
        return self.index
    
    def _set_last__majfzk_k_(self, _set___):
        self.last = _set___
    
    def _get_last__0_k_(self):
        return self.last
    
    def hasNext_0_k_(self):
        return self._get_index__0_k_() < self._get_size__0_k_()
    
    def next_0_k_(self):
        if not self.hasNext_0_k_():
            raise NoSuchElementException_init__Create_()
        
        tmp0_this = self
        tmp1 = tmp0_this._get_index__0_k_()
        tmp0_this._set_index__majfzk_k_((((tmp1 + 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
        self._set_last__majfzk_k_(tmp1)
        return self.get_ha5a7z_k_(self._get_last__0_k_())
    
    def remove_sv8swh_k_(self):
        check_0(not (self._get_last__0_k_() == -1), lambda : 'Call next() or previous() before removing element from the iterator.')
        self.removeAt_ha5a7z_k_(self._get_last__0_k_())
        Unit_getInstance()
        self._set_index__majfzk_k_(self._get_last__0_k_())
        self._set_last__majfzk_k_(-1)
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class ListIteratorImpl_0(IteratorImpl_0, MutableListIterator):
    def __init__(self, index):
        IteratorImpl_0.__init__(self)
        Companion_getInstance().checkPositionIndex_rvwcgf_k_(index, self._get_size__0_k_())
        self._set_index__majfzk_k_(index)
    
    def hasPrevious_0_k_(self):
        return self._get_index__0_k_() > 0
    
    def nextIndex_0_k_(self):
        return self._get_index__0_k_()
    
    def previous_0_k_(self):
        if not self.hasPrevious_0_k_():
            raise NoSuchElementException_init__Create_()
        
        tmp0_this = self
        tmp0_this._set_index__majfzk_k_((((tmp0_this._get_index__0_k_() - 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
        self._set_last__majfzk_k_(tmp0_this._get_index__0_k_())
        return self.get_ha5a7z_k_(self._get_last__0_k_())
    
    def previousIndex_0_k_(self):
        return (((self._get_index__0_k_() - 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
    
    def add_jxzaet_k_(self, element):
        self.add_vz2mgm_k_(self._get_index__0_k_(), element)
        tmp0_this = self
        tmp1 = tmp0_this._get_index__0_k_()
        tmp0_this._set_index__majfzk_k_((((tmp1 + 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
        Unit_getInstance()
        self._set_last__majfzk_k_(-1)
    
    def set_jxzaet_k_(self, element):
        check_0(not (self._get_last__0_k_() == -1), lambda : 'Call next() or previous() before updating element value with the iterator.')
        self.set_ddb1qf_k_(self._get_last__0_k_(), element)
        Unit_getInstance()
    
    def _set_index__majfzk_k_(self, _set___):
        pass
    
    def _get_index__0_k_(self):
        pass
    
    def _set_last__majfzk_k_(self, _set___):
        pass
    
    def _get_last__0_k_(self):
        pass
    
    def hasNext_0_k_(self):
        pass
    
    def next_0_k_(self):
        pass
    
    def remove_sv8swh_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class AbstractMutableList:
    pass

class SubList_0(AbstractMutableList, RandomAccess):
    def __init__(self, list, fromIndex, toIndex):
        AbstractMutableList.__init__(self)
        self.list = list
        self.fromIndex = fromIndex
        self._size = 0
        Companion_getInstance().checkRangeIndexes_zd700_k_(self._get_fromIndex__0_k_(), toIndex, self._get_list__0_k_()._get_size__0_k_())
        self._set__size__majfzk_k_((((toIndex - self._get_fromIndex__0_k_()) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
    
    def _get_list__0_k_(self):
        return self.list
    
    def _get_fromIndex__0_k_(self):
        return self.fromIndex
    
    def _set__size__majfzk_k_(self, _set___):
        self._size = _set___
    
    def _get__size__0_k_(self):
        return self._size
    
    def add_vz2mgm_k_(self, index, element):
        Companion_getInstance().checkPositionIndex_rvwcgf_k_(index, self._get__size__0_k_())
        self._get_list__0_k_().add_vz2mgm_k_((((self._get_fromIndex__0_k_() + index) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000, element)
        tmp0_this = self
        tmp1 = tmp0_this._get__size__0_k_()
        tmp0_this._set__size__majfzk_k_((((tmp1 + 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
        Unit_getInstance()
    
    def get_ha5a7z_k_(self, index):
        Companion_getInstance().checkElementIndex_rvwcgf_k_(index, self._get__size__0_k_())
        return self._get_list__0_k_().get_ha5a7z_k_((((self._get_fromIndex__0_k_() + index) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
    
    def removeAt_ha5a7z_k_(self, index):
        Companion_getInstance().checkElementIndex_rvwcgf_k_(index, self._get__size__0_k_())
        result = self._get_list__0_k_().removeAt_ha5a7z_k_((((self._get_fromIndex__0_k_() + index) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
        tmp0_this = self
        tmp1 = tmp0_this._get__size__0_k_()
        tmp0_this._set__size__majfzk_k_((((tmp1 - 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
        Unit_getInstance()
        return result
    
    def set_ddb1qf_k_(self, index, element):
        Companion_getInstance().checkElementIndex_rvwcgf_k_(index, self._get__size__0_k_())
        return self._get_list__0_k_().set_ddb1qf_k_((((self._get_fromIndex__0_k_() + index) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000, element)
    
    def _get_size__0_k_(self):
        return self._get__size__0_k_()
    
    def checkIsMutable_sv8swh_k_(self):
        return self._get_list__0_k_().checkIsMutable_sv8swh_k_()
    
    def _set_modCount__majfzk_k_(self, _set___):
        pass
    
    def _get_modCount__0_k_(self):
        pass
    
    def add_2bq_k_(self, element):
        pass
    
    def addAll_xggsjz_k_(self, index, elements):
        pass
    
    def addAll_dxd4eo_k_(self, elements):
        pass
    
    def clear_sv8swh_k_(self):
        pass
    
    def removeAll_dxd4eo_k_(self, elements):
        pass
    
    def retainAll_dxd4eo_k_(self, elements):
        pass
    
    def iterator_0_k_(self):
        pass
    
    def contains_2bq_k_(self, element):
        pass
    
    def indexOf_2bq_k_(self, element):
        pass
    
    def lastIndexOf_2bq_k_(self, element):
        pass
    
    def listIterator_0_k_(self):
        pass
    
    def listIterator_ha5a7z_k_(self, index):
        pass
    
    def subList_27zxwg_k_(self, fromIndex, toIndex):
        pass
    
    def removeRange_rvwcgf_k_(self, fromIndex, toIndex):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def remove_2bq_k_(self, element):
        pass
    
    def toJSON(self):
        pass
    
    def containsAll_dxd4eo_k_(self, elements):
        pass
    
    def isEmpty_0_k_(self):
        pass
    
    def toString(self):
        pass
    
    def toArray(self):
        pass
    
    def toArray_gjotr5_k_(self, array):
        pass
    

class MutableList:
    pass

class AbstractMutableList(AbstractMutableCollection, MutableList):
    def __init__(self):
        AbstractMutableCollection.__init__(self)
        self.modCount = 0
    
    def _set_modCount__majfzk_k_(self, _set___):
        self.modCount = _set___
    
    def _get_modCount__0_k_(self):
        return self.modCount
    
    def add_vz2mgm_k_(self, index, element):
        pass
    
    def removeAt_ha5a7z_k_(self, index):
        pass
    
    def set_ddb1qf_k_(self, index, element):
        pass
    
    def add_2bq_k_(self, element):
        self.checkIsMutable_sv8swh_k_()
        self.add_vz2mgm_k_(self._get_size__0_k_(), element)
        return True
    
    def addAll_xggsjz_k_(self, index, elements):
        Companion_getInstance().checkPositionIndex_rvwcgf_k_(index, self._get_size__0_k_())
        self.checkIsMutable_sv8swh_k_()
        _index = index
        changed = False
        tmp0_iterator = elements.iterator_0_k_()
        while tmp0_iterator.hasNext_0_k_():
            e = tmp0_iterator.next_0_k_()
            tmp1 = _index
            _index = (((tmp1 + 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
            self.add_vz2mgm_k_(tmp1, e)
            changed = True
        
        return changed
    
    def clear_sv8swh_k_(self):
        self.checkIsMutable_sv8swh_k_()
        self.removeRange_rvwcgf_k_(0, self._get_size__0_k_())
    
    def removeAll_dxd4eo_k_(self, elements):
        self.checkIsMutable_sv8swh_k_()
        return removeAll(self, lambda it: elements.contains_2bq_k_(it))
    
    def retainAll_dxd4eo_k_(self, elements):
        self.checkIsMutable_sv8swh_k_()
        return removeAll(self, lambda it: not elements.contains_2bq_k_(it))
    
    def iterator_0_k_(self):
        return IteratorImpl_0()
    
    def contains_2bq_k_(self, element):
        return self.indexOf_2bq_k_(element) >= 0
    
    def indexOf_2bq_k_(self, element):
        tmp0_iterator = numberRangeToNumber(0, _get_lastIndex__4(self)).iterator_0_k_()
        while tmp0_iterator.hasNext_0_k_():
            index = tmp0_iterator.next_0_k_()
            if self.get_ha5a7z_k_(index) == element:
                return index
            
        
        return -1
    
    def lastIndexOf_2bq_k_(self, element):
        tmp0_iterator = downTo(_get_lastIndex__4(self), 0).iterator_0_k_()
        while tmp0_iterator.hasNext_0_k_():
            index = tmp0_iterator.next_0_k_()
            if self.get_ha5a7z_k_(index) == element:
                return index
            
        
        return -1
    
    def listIterator_0_k_(self):
        return self.listIterator_ha5a7z_k_(0)
    
    def listIterator_ha5a7z_k_(self, index):
        return ListIteratorImpl_0(index)
    
    def subList_27zxwg_k_(self, fromIndex, toIndex):
        return SubList_0(self, fromIndex, toIndex)
    
    def removeRange_rvwcgf_k_(self, fromIndex, toIndex):
        iterator = self.listIterator_ha5a7z_k_(fromIndex)
        def complexFunction_x3__Expr__Expr__Expr__0(it):
            iterator.next_0_k_()
            Unit_getInstance()
            iterator.remove_sv8swh_k_()
        
        repeat((((toIndex - fromIndex) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000, complexFunction_x3__Expr__Expr__Expr__0)
    
    def equals(self, other):
        if other is self:
            return True
        
        if not ((isInterface(other, List)) if (not (other == None)) else (False)):
            return False
        
        return Companion_getInstance().orderedEquals_tuq55s_k_(self, kotlin_collections_Collection___(other))
    
    def hashCode(self):
        return Companion_getInstance().orderedHashCode_dxd51x_k_(self)
    
    def remove_2bq_k_(self, element):
        pass
    
    def addAll_dxd4eo_k_(self, elements):
        pass
    
    def toJSON(self):
        pass
    
    def checkIsMutable_sv8swh_k_(self):
        pass
    
    def _get_size__0_k_(self):
        pass
    
    def containsAll_dxd4eo_k_(self, elements):
        pass
    
    def isEmpty_0_k_(self):
        pass
    
    def toString(self):
        pass
    
    def toArray(self):
        pass
    
    def toArray_gjotr5_k_(self, array):
        pass
    
    def get_ha5a7z_k_(self, index):
        pass
    

def ArrayList_init__Init_(_this):
    ArrayList.__init__(_this, emptyArray())
    return _this

def ArrayList_init__Create_():
    return ArrayList_init__Init_(ArrayList.__new__(ArrayList))

def ArrayList_init__Init__0(initialCapacity, _this):
    ArrayList.__init__(_this, emptyArray())
    return _this

def ArrayList_init__Create__0(initialCapacity):
    return ArrayList_init__Init__0(initialCapacity, ArrayList.__new__(ArrayList))

def ArrayList_init__Init__1(elements, _this):
    ArrayList.__init__(_this, toTypedArray(elements))
    return _this

def ArrayList_init__Create__1(elements):
    return ArrayList_init__Init__1(elements, ArrayList.__new__(ArrayList))

class ArrayList(AbstractMutableList, MutableList, RandomAccess):
    def __init__(self, array):
        AbstractMutableList.__init__(self)
        self.array = array
        self.isReadOnly = False
    
    def _set_array__1fckf2_k_(self, _set___):
        self.array = _set___
    
    def _get_array__0_k_(self):
        return self.array
    
    def _set_isReadOnly__rpwsgn_k_(self, _set___):
        self.isReadOnly = _set___
    
    def _get_isReadOnly__0_k_(self):
        return self.isReadOnly
    
    def build_0_k_(self):
        self.checkIsMutable_sv8swh_k_()
        self._set_isReadOnly__rpwsgn_k_(True)
        return self
    
    def trimToSize_sv8swh_k_(self):
        pass
    
    def ensureCapacity_majfzk_k_(self, minCapacity):
        pass
    
    def _get_size__0_k_(self):
        return len(self._get_array__0_k_())
    
    def get_ha5a7z_k_(self, index):
        tmp = self._get_array__0_k_()[self.rangeCheck_ha5a7z_k_(index)]
        return (E(tmp)) if ((True) if (tmp == None) else (isObject(tmp))) else (THROW_CCE())
    
    def set_ddb1qf_k_(self, index, element):
        self.checkIsMutable_sv8swh_k_()
        self.rangeCheck_ha5a7z_k_(index)
        Unit_getInstance()
        def complexFunction_x1__Expr__0(_this_apply):
            self._get_array__0_k_().__setitem__(index, element)
        
        tmp = apply(self._get_array__0_k_()[index], complexFunction_x1__Expr__0)
        return (E(tmp)) if ((True) if (tmp == None) else (isObject(tmp))) else (THROW_CCE())
    
    def add_2bq_k_(self, element):
        self.checkIsMutable_sv8swh_k_()
        asDynamic(self._get_array__0_k_()).push(element)
        tmp0_this = self
        tmp1 = tmp0_this._get_modCount__0_k_()
        tmp0_this._set_modCount__majfzk_k_((((tmp1 + 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
        Unit_getInstance()
        return True
    
    def add_vz2mgm_k_(self, index, element):
        self.checkIsMutable_sv8swh_k_()
        asDynamic(self._get_array__0_k_()).splice(self.insertionRangeCheck_ha5a7z_k_(index), 0, element)
        tmp0_this = self
        tmp1 = tmp0_this._get_modCount__0_k_()
        tmp0_this._set_modCount__majfzk_k_((((tmp1 + 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
        Unit_getInstance()
    
    def addAll_dxd4eo_k_(self, elements):
        self.checkIsMutable_sv8swh_k_()
        if elements.isEmpty_0_k_():
            return False
        
        tmp0_this = self
        tmp0_this._set_array__1fckf2_k_(plus_0(tmp0_this._get_array__0_k_(), toTypedArray(elements)))
        tmp1_this = self
        tmp2 = tmp1_this._get_modCount__0_k_()
        tmp1_this._set_modCount__majfzk_k_((((tmp2 + 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
        Unit_getInstance()
        return True
    
    def addAll_xggsjz_k_(self, index, elements):
        self.checkIsMutable_sv8swh_k_()
        self.insertionRangeCheck_ha5a7z_k_(index)
        Unit_getInstance()
        if index == self._get_size__0_k_():
            return self.addAll_dxd4eo_k_(elements)
        
        if elements.isEmpty_0_k_():
            return False
        
        tmp0_subject = index
        if tmp0_subject == self._get_size__0_k_():
            return self.addAll_dxd4eo_k_(elements)
        elif tmp0_subject == 0:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCallImpl
        else:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCallImpl
        
        tmp1_this = self
        tmp2 = tmp1_this._get_modCount__0_k_()
        tmp1_this._set_modCount__majfzk_k_((((tmp2 + 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
        Unit_getInstance()
        return True
    
    def removeAt_ha5a7z_k_(self, index):
        self.checkIsMutable_sv8swh_k_()
        self.rangeCheck_ha5a7z_k_(index)
        Unit_getInstance()
        tmp0_this = self
        tmp1 = tmp0_this._get_modCount__0_k_()
        tmp0_this._set_modCount__majfzk_k_((((tmp1 + 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
        Unit_getInstance()
        return (E(asDynamic(self._get_array__0_k_()).pop())) if (index == _get_lastIndex__4(self)) else (E(asDynamic(self._get_array__0_k_()).splice(index, 1)[0]))
    
    def remove_2bq_k_(self, element):
        self.checkIsMutable_sv8swh_k_()
        tmp0_iterator = _get_indices__3(self._get_array__0_k_()).iterator_0_k_()
        while tmp0_iterator.hasNext_0_k_():
            index = tmp0_iterator.next_0_k_()
            if self._get_array__0_k_()[index] == element:
                asDynamic(self._get_array__0_k_()).splice(index, 1)
                tmp1_this = self
                tmp2 = tmp1_this._get_modCount__0_k_()
                tmp1_this._set_modCount__majfzk_k_((((tmp2 + 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
                Unit_getInstance()
                return True
            
        
        return False
    
    def removeRange_rvwcgf_k_(self, fromIndex, toIndex):
        self.checkIsMutable_sv8swh_k_()
        tmp0_this = self
        tmp1 = tmp0_this._get_modCount__0_k_()
        tmp0_this._set_modCount__majfzk_k_((((tmp1 + 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
        Unit_getInstance()
        asDynamic(self._get_array__0_k_()).splice(fromIndex, (((toIndex - fromIndex) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
    
    def clear_sv8swh_k_(self):
        self.checkIsMutable_sv8swh_k_()
        self._set_array__1fckf2_k_(emptyArray())
        tmp0_this = self
        tmp1 = tmp0_this._get_modCount__0_k_()
        tmp0_this._set_modCount__majfzk_k_((((tmp1 + 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
        Unit_getInstance()
    
    def indexOf_2bq_k_(self, element):
        return indexOf_3(self._get_array__0_k_(), element)
    
    def lastIndexOf_2bq_k_(self, element):
        return lastIndexOf(self._get_array__0_k_(), element)
    
    def toString(self):
        return arrayToString(self._get_array__0_k_())
    
    def toArray_gjotr5_k_(self, array):
        if len(array) < self._get_size__0_k_():
            tmp = self.toArray_0_k_()
            return (kotlin_Array_T_(tmp)) if (isArray(tmp)) else (THROW_CCE())
        
        tmp = self._get_array__0_k_()
        copyInto((kotlin_Array_T_(tmp)) if (isArray(tmp)) else (THROW_CCE()), array, translateCallArguments_1, translateCallArguments_2, translateCallArguments_3)
        Unit_getInstance()
        if len(array) > self._get_size__0_k_():
            tmp = self._get_size__0_k_()
            array.__setitem__(tmp, (T(None)) if ((True) if (None == None) else (isObject(None))) else (THROW_CCE()))
        
        return array
    
    def toArray_0_k_(self):
        return kotlin_Array_kotlin_Any__(js('[]').slice.call(self._get_array__0_k_()))
    
    def checkIsMutable_sv8swh_k_(self):
        if self._get_isReadOnly__0_k_():
            raise UnsupportedOperationException_init__Create_()
        
    
    def rangeCheck_ha5a7z_k_(self, index):
        def complexFunction_x1__Expr__0(_this_apply):
            Companion_getInstance().checkElementIndex_rvwcgf_k_(index, self._get_size__0_k_())
        
        return apply(index, complexFunction_x1__Expr__0)
    
    def insertionRangeCheck_ha5a7z_k_(self, index):
        def complexFunction_x1__Expr__0(_this_apply):
            Companion_getInstance().checkPositionIndex_rvwcgf_k_(index, self._get_size__0_k_())
        
        return apply(index, complexFunction_x1__Expr__0)
    
    def _set_modCount__majfzk_k_(self, _set___):
        pass
    
    def _get_modCount__0_k_(self):
        pass
    
    def removeAll_dxd4eo_k_(self, elements):
        pass
    
    def retainAll_dxd4eo_k_(self, elements):
        pass
    
    def iterator_0_k_(self):
        pass
    
    def contains_2bq_k_(self, element):
        pass
    
    def listIterator_0_k_(self):
        pass
    
    def listIterator_ha5a7z_k_(self, index):
        pass
    
    def subList_27zxwg_k_(self, fromIndex, toIndex):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toJSON(self):
        pass
    
    def containsAll_dxd4eo_k_(self, elements):
        pass
    
    def isEmpty_0_k_(self):
        pass
    

def _set__stableSortingIsSupported_(_set___):
    global _stableSortingIsSupported
    _stableSortingIsSupported = _set___

def _get__stableSortingIsSupported_():
    return _stableSortingIsSupported

_stableSortingIsSupported = None
class RandomAccess(Any):
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def _set_output_(_set___):
    global output
    output = _set___

def _get_output_():
    return output

output = None
class BaseOutput(Any):
    def __init__(self):
        pass
    
    def println_sv8swh_k_(self):
        self.print_qi8yb4_k_('\n')
    
    def println_qi8yb4_k_(self, message):
        self.print_qi8yb4_k_(message)
        self.println_sv8swh_k_()
    
    def print_qi8yb4_k_(self, message):
        pass
    
    def flush_sv8swh_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class NodeJsOutput_0(BaseOutput):
    def __init__(self, outputStream):
        BaseOutput.__init__(self)
        self.outputStream = outputStream
    
    def _get_outputStream__0_k_(self):
        return self.outputStream
    
    def print_qi8yb4_k_(self, message):
        messageString = String_0(message)
        self._get_outputStream__0_k_().write(messageString)
    
    def println_sv8swh_k_(self):
        pass
    
    def println_qi8yb4_k_(self, message):
        pass
    
    def flush_sv8swh_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class BufferedOutput_0:
    pass

class BufferedOutputToConsoleLog_0(BufferedOutput_0):
    def __init__(self):
        BufferedOutput_0.__init__(self)
    
    def print_qi8yb4_k_(self, message):
        s = String_0(message)
        i = nativeLastIndexOf(s, '\n', 0)
        if i >= 0:
            tmp0_this = self
            tmp0_this._set_buffer__a4enbm_k_(tmp0_this._get_buffer__0_k_() + substring(s, 0, i))
            self.flush_sv8swh_k_()
            s = substring_0(s, (((i + 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
        
        tmp1_this = self
        tmp1_this._set_buffer__a4enbm_k_(tmp1_this._get_buffer__0_k_() + s)
    
    def flush_sv8swh_k_(self):
        console.log(*(self._get_buffer__0_k_(),))
        self._set_buffer__a4enbm_k_('')
    
    def _set_buffer__a4enbm_k_(self, _set___):
        pass
    
    def _get_buffer__0_k_(self):
        pass
    
    def println_sv8swh_k_(self):
        pass
    
    def println_qi8yb4_k_(self, message):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def String_0(value):
    return kotlin_String(js('String')(value))

class BufferedOutput_0(BaseOutput):
    def __init__(self):
        BaseOutput.__init__(self)
        self.buffer = ''
    
    def _set_buffer__a4enbm_k_(self, _set___):
        self.buffer = _set___
    
    def _get_buffer__0_k_(self):
        return self.buffer
    
    def print_qi8yb4_k_(self, message):
        tmp0_this = self
        tmp0_this._set_buffer__a4enbm_k_(tmp0_this._get_buffer__0_k_() + String_0(message))
    
    def flush_sv8swh_k_(self):
        self._set_buffer__a4enbm_k_('')
    
    def println_sv8swh_k_(self):
        pass
    
    def println_qi8yb4_k_(self, message):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def println(message):
    _get_output_().println_qi8yb4_k_(message)

def _get_EmptyContinuation_():
    return EmptyContinuation

EmptyContinuation = None
def asDynamic(self):
    return self

def unsafeCast(self):
    return T(self)

def unsafeCast_0(self):
    return T(asDynamic(self))

class Serializable(Any):
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def pow(self, n):
    return JsMath.pow(self, kotlin_Double(n))

def isNaN_0(self):
    return not (self == self)

def _get_INV_2_26_():
    return INV_2_26

INV_2_26 = None
def _get_INV_2_53_():
    return INV_2_53

INV_2_53 = None
def _get_js_(self):
    return ((kotlin_reflect_js_internal_KClassImpl_T_(self)) if (isinstance(self, KClassImpl)) else (THROW_CCE()))._get_jClass__0_k_()

class KCallable(Any):
    def _get_name__0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class KClass(KClassifier):
    def _get_simpleName__0_k_(self):
        pass
    
    def _get_qualifiedName__0_k_(self):
        pass
    
    def isInstance_wi7j7l_k_(self, value):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class KClassImpl(KClass):
    def __init__(self, jClass):
        self.jClass = jClass
    
    def _get_jClass__0_k_(self):
        return self.jClass
    
    def _get_qualifiedName__0_k_(self):
        return TODO()
    
    def equals(self, other):
        if isinstance(other, KClassImpl):
            tmp = self._get_jClass__0_k_() == kotlin_reflect_js_internal_KClassImpl___(other)._get_jClass__0_k_()
        elif True:
            tmp = False
        
        return tmp
    
    def hashCode(self):
        tmp0_safe_receiver = self._get_simpleName__0_k_()
        tmp1_elvis_lhs = (None) if (tmp0_safe_receiver == None) else (getStringHashCode(tmp0_safe_receiver))
        return (0) if (tmp1_elvis_lhs == None) else (tmp1_elvis_lhs)
    
    def toString(self):
        return str('class ') + str(self._get_simpleName__0_k_())
    
    def _get_simpleName__0_k_(self):
        pass
    
    def isInstance_wi7j7l_k_(self, value):
        pass
    

class PrimitiveKClassImpl(KClassImpl):
    def __init__(self, jClass, givenSimpleName, isInstanceFunction):
        KClassImpl.__init__(self, jClass)
        self.givenSimpleName = givenSimpleName
        self.isInstanceFunction = isInstanceFunction
    
    def _get_givenSimpleName__0_k_(self):
        return self.givenSimpleName
    
    def _get_isInstanceFunction__0_k_(self):
        return self.isInstanceFunction
    
    def equals(self, other):
        if not isinstance(other, PrimitiveKClassImpl):
            return False
        
        return (self._get_givenSimpleName__0_k_() == kotlin_reflect_js_internal_PrimitiveKClassImpl___(other)._get_givenSimpleName__0_k_()) if (self.equals(other)) else (False)
    
    def _get_simpleName__0_k_(self):
        return self._get_givenSimpleName__0_k_()
    
    def isInstance_wi7j7l_k_(self, value):
        return self._get_isInstanceFunction__0_k_()(value)
    
    def _get_jClass__0_k_(self):
        pass
    
    def _get_qualifiedName__0_k_(self):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class NothingKClassImpl(KClassImpl):
    def __init__(self):
        global NothingKClassImpl_instance
        NothingKClassImpl_instance = self
        KClassImpl.__init__(self, kotlin_js_JsClass_kotlin_Nothing_(js('Object')))
        self.simpleName = 'Nothing'
    
    def _get_simpleName__0_k_(self):
        return self.simpleName
    
    def isInstance_wi7j7l_k_(self, value):
        return False
    
    def _get_jClass__0_k_(self):
        raise UnsupportedOperationException_init__Create__0('There\'s no native JS class for Nothing type')
    
    def equals(self, other):
        return other is self
    
    def hashCode(self):
        return 0
    
    def _get_qualifiedName__0_k_(self):
        pass
    
    def toString(self):
        pass
    

NothingKClassImpl_instance = None
def NothingKClassImpl_getInstance():
    if NothingKClassImpl_instance == None:
        NothingKClassImpl()
    
    return NothingKClassImpl_instance

class ErrorKClass(KClass):
    def __init__(self):
        pass
    
    def _get_simpleName__0_k_(self):
        return error('Unknown simpleName for ErrorKClass')
    
    def _get_qualifiedName__0_k_(self):
        return error('Unknown qualifiedName for ErrorKClass')
    
    def isInstance_wi7j7l_k_(self, value):
        return error('Can\'s check isInstance on ErrorKClass')
    
    def equals(self, other):
        return other is self
    
    def hashCode(self):
        return 0
    
    def toString(self):
        pass
    

class SimpleKClassImpl(KClassImpl):
    def __init__(self, jClass):
        KClassImpl.__init__(self, jClass)
        tmp = self
        tmp0_safe_receiver = asDynamic(jClass)._metadata_
        tmp.simpleName = unsafeCast((None) if (tmp0_safe_receiver == None) else (tmp0_safe_receiver.simpleName))
    
    def _get_simpleName__0_k_(self):
        return self.simpleName
    
    def isInstance_wi7j7l_k_(self, value):
        return jsIsType(value, self._get_jClass__0_k_())
    
    def _get_jClass__0_k_(self):
        pass
    
    def _get_qualifiedName__0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class Function:
    pass

class KFunction(KCallable, Function):
    def _get_name__0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class KProperty(KCallable):
    def _get_name__0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class KProperty0(KProperty):
    def get_0_k_(self):
        pass
    
    def _get_name__0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def invoke_0_k_(self):
        pass
    

class KProperty1(KProperty):
    def get_2c5_k_(self, receiver):
        pass
    
    def _get_name__0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def invoke_2c5_k_(self, p1):
        pass
    

class KProperty2(KProperty):
    def get_1q4i3_k_(self, receiver1, receiver2):
        pass
    
    def _get_name__0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def invoke_1q4i3_k_(self, p1, p2):
        pass
    

class KMutableProperty:
    pass

class KMutableProperty0(KProperty0, KMutableProperty):
    def set_prcxve_k_(self, value):
        pass
    
    def get_0_k_(self):
        pass
    
    def _get_name__0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def invoke_0_k_(self):
        pass
    

class KMutableProperty(KProperty):
    def _get_name__0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class KMutableProperty1(KProperty1, KMutableProperty):
    def set_5l00ez_k_(self, receiver, value):
        pass
    
    def get_2c5_k_(self, receiver):
        pass
    
    def _get_name__0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def invoke_2c5_k_(self, p1):
        pass
    

class KMutableProperty2(KProperty2, KMutableProperty):
    def set_kx3mz5_k_(self, receiver1, receiver2, value):
        pass
    
    def get_1q4i3_k_(self, receiver1, receiver2):
        pass
    
    def _get_name__0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def invoke_1q4i3_k_(self, p1, p2):
        pass
    

class KType(Any):
    def _get_classifier__0_k_(self):
        pass
    
    def _get_arguments__0_k_(self):
        pass
    
    def _get_isMarkedNullable__0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def createKType_0(classifier, arguments, isMarkedNullable):
    return KTypeImpl(classifier, asList(arguments), isMarkedNullable)

def createDynamicKType_0():
    return DynamicKType_getInstance()

def createKTypeParameter_0(name, upperBounds, variance):
    tmp0_subject = variance
    kVariance = (visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrGetEnumValueImpl) if (tmp0_subject == 'in') else ((visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrGetEnumValueImpl) if (tmp0_subject == 'out') else (visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrGetEnumValueImpl))
    return KTypeParameterImpl(name, asList(upperBounds), kVariance, False)

def getStarKTypeProjection_0():
    return Companion_getInstance_1()._get_STAR__0_k_()

def createCovariantKTypeProjection_0(type):
    return Companion_getInstance_1().covariant_573d5y_k_(type)

def createInvariantKTypeProjection_0(type):
    return Companion_getInstance_1().invariant_573d5y_k_(type)

def createContravariantKTypeProjection_0(type):
    return Companion_getInstance_1().contravariant_573d5y_k_(type)

class KTypeImpl(KType):
    def __init__(self, classifier, arguments, isMarkedNullable):
        self.classifier = classifier
        self.arguments = arguments
        self.isMarkedNullable = isMarkedNullable
    
    def _get_classifier__0_k_(self):
        return self.classifier
    
    def _get_arguments__0_k_(self):
        return self.arguments
    
    def _get_isMarkedNullable__0_k_(self):
        return self.isMarkedNullable
    
    def equals(self, other):
        if isinstance(other, KTypeImpl):
            tmp = self._get_classifier__0_k_() == kotlin_reflect_js_internal_KTypeImpl(other)._get_classifier__0_k_()
        elif True:
            tmp = False
        
        if tmp:
            tmp = self._get_arguments__0_k_() == kotlin_reflect_js_internal_KTypeImpl(other)._get_arguments__0_k_()
        elif True:
            tmp = False
        
        if tmp:
            tmp = self._get_isMarkedNullable__0_k_() == kotlin_reflect_js_internal_KTypeImpl(other)._get_isMarkedNullable__0_k_()
        elif True:
            tmp = False
        
        return tmp
    
    def hashCode(self):
        return (((imul((((imul(hashCode(self._get_classifier__0_k_()), 31) + hashCode(self._get_arguments__0_k_())) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000, 31) + (((self._get_isMarkedNullable__0_k_() + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
    
    def toString(self):
        tmp = self._get_classifier__0_k_()
        kClass = (kotlin_reflect_KClass___(tmp)) if (isInterface(tmp, KClass)) else (None)
        classifierName = (toString_0(self._get_classifier__0_k_())) if (kClass == None) else ((kClass._get_simpleName__0_k_()) if (not (kClass._get_simpleName__0_k_() == None)) else ('(non-denotable type)'))
        args = ('') if (self._get_arguments__0_k_().isEmpty_0_k_()) else (joinToString_0(self._get_arguments__0_k_(), ', ', '<', '>', translateCallArguments_3, translateCallArguments_4, lambda it: self.asString_3z6dj_k_()))
        nullable = ('?') if (self._get_isMarkedNullable__0_k_()) else ('')
        return plus(classifierName, args) + nullable
    
    def asString_3z6dj_k_(self):
        if self._get_variance__0_k_() == None:
            return '*'
        
        return prefixString(self._get_variance__0_k_()) + toString(self._get_type__0_k_())
    

def prefixString(self):
    tmp0_subject = self
    return ('') if (tmp0_subject == visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrGetEnumValueImpl) else (('in ') if (tmp0_subject == visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrGetEnumValueImpl) else (('out ') if (tmp0_subject == visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrGetEnumValueImpl) else (noWhenBranchMatchedException())))

class DynamicKType(KType):
    def __init__(self):
        global DynamicKType_instance
        DynamicKType_instance = self
        self.classifier = None
        self.arguments = emptyList()
        self.isMarkedNullable = False
    
    def _get_classifier__0_k_(self):
        return self.classifier
    
    def _get_arguments__0_k_(self):
        return self.arguments
    
    def _get_isMarkedNullable__0_k_(self):
        return self.isMarkedNullable
    
    def toString(self):
        return 'dynamic'
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    

DynamicKType_instance = None
def DynamicKType_getInstance():
    if DynamicKType_instance == None:
        DynamicKType()
    
    return DynamicKType_instance

class KTypeParameterImpl(KTypeParameter):
    def __init__(self, name, upperBounds, variance, isReified):
        self.name = name
        self.upperBounds = upperBounds
        self.variance = variance
        self.isReified = isReified
    
    def _get_name__0_k_(self):
        return self.name
    
    def _get_upperBounds__0_k_(self):
        return self.upperBounds
    
    def _get_variance__0_k_(self):
        return self.variance
    
    def _get_isReified__0_k_(self):
        return self.isReified
    
    def toString(self):
        return self._get_name__0_k_()
    
    def component1_0_k_(self):
        return self._get_name__0_k_()
    
    def component2_0_k_(self):
        return self._get_upperBounds__0_k_()
    
    def component3_0_k_(self):
        return self._get_variance__0_k_()
    
    def component4_0_k_(self):
        return self._get_isReified__0_k_()
    
    def copy_367z8c_k_(self, name, upperBounds, variance, isReified):
        return KTypeParameterImpl(name, upperBounds, variance, isReified)
    
    def hashCode(self):
        result = getStringHashCode(self._get_name__0_k_())
        result = (((imul(result, 31) + hashCode(self._get_upperBounds__0_k_())) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
        result = (((imul(result, 31) + self._get_variance__0_k_().hashCode()) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
        result = (((imul(result, 31) + (((self._get_isReified__0_k_() + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
        return result
    
    def equals(self, other):
        if self is other:
            return True
        
        if not isinstance(other, KTypeParameterImpl):
            return False
        
        tmp0_other_with_cast = (kotlin_reflect_js_internal_KTypeParameterImpl(other)) if (isinstance(other, KTypeParameterImpl)) else (THROW_CCE())
        if not (self._get_name__0_k_() == tmp0_other_with_cast._get_name__0_k_()):
            return False
        
        if not (self._get_upperBounds__0_k_() == tmp0_other_with_cast._get_upperBounds__0_k_()):
            return False
        
        if not (self._get_variance__0_k_() == tmp0_other_with_cast._get_variance__0_k_()):
            return False
        
        if not (self._get_isReified__0_k_() == tmp0_other_with_cast._get_isReified__0_k_()):
            return False
        
        return True
    

def _get_functionClasses_():
    return functionClasses

functionClasses = None
class PrimitiveClasses_0(Any):
    def __init__(self):
        global PrimitiveClasses_instance
        PrimitiveClasses_instance = self
        self.anyClass = PrimitiveKClassImpl(unsafeCast(js('Object')), 'Any', lambda it: isObject(it))
        self.numberClass = PrimitiveKClassImpl(unsafeCast(js('Number')), 'Number', lambda it: isNumber(it))
        self.nothingClass = NothingKClassImpl_getInstance()
        self.booleanClass = PrimitiveKClassImpl(unsafeCast(js('Boolean')), 'Boolean', lambda it: (jsTypeOf(it) == 'boolean') if (not (it == None)) else (False))
        self.byteClass = PrimitiveKClassImpl(unsafeCast(js('Number')), 'Byte', lambda it: (jsTypeOf(it) == 'number') if (not (it == None)) else (False))
        self.shortClass = PrimitiveKClassImpl(unsafeCast(js('Number')), 'Short', lambda it: (jsTypeOf(it) == 'number') if (not (it == None)) else (False))
        self.intClass = PrimitiveKClassImpl(unsafeCast(js('Number')), 'Int', lambda it: (jsTypeOf(it) == 'number') if (not (it == None)) else (False))
        self.floatClass = PrimitiveKClassImpl(unsafeCast(js('Number')), 'Float', lambda it: (jsTypeOf(it) == 'number') if (not (it == None)) else (False))
        self.doubleClass = PrimitiveKClassImpl(unsafeCast(js('Number')), 'Double', lambda it: (jsTypeOf(it) == 'number') if (not (it == None)) else (False))
        self.arrayClass = PrimitiveKClassImpl(unsafeCast(js('Array')), 'Array', lambda it: (isArray(it)) if (not (it == None)) else (False))
        self.stringClass = PrimitiveKClassImpl(unsafeCast(js('String')), 'String', lambda it: (jsTypeOf(it) == 'string') if (not (it == None)) else (False))
        self.throwableClass = PrimitiveKClassImpl(unsafeCast(js('Error')), 'Throwable', lambda it: isinstance(it, Error))
        self.booleanArrayClass = PrimitiveKClassImpl(unsafeCast(js('Array')), 'BooleanArray', lambda it: (isBooleanArray(it)) if (not (it == None)) else (False))
        self.charArrayClass = PrimitiveKClassImpl(unsafeCast(js('Uint16Array')), 'CharArray', lambda it: (isCharArray(it)) if (not (it == None)) else (False))
        self.byteArrayClass = PrimitiveKClassImpl(unsafeCast(js('Int8Array')), 'ByteArray', lambda it: (isByteArray(it)) if (not (it == None)) else (False))
        self.shortArrayClass = PrimitiveKClassImpl(unsafeCast(js('Int16Array')), 'ShortArray', lambda it: (isShortArray(it)) if (not (it == None)) else (False))
        self.intArrayClass = PrimitiveKClassImpl(unsafeCast(js('Int32Array')), 'IntArray', lambda it: (isIntArray(it)) if (not (it == None)) else (False))
        self.longArrayClass = PrimitiveKClassImpl(unsafeCast(js('Array')), 'LongArray', lambda it: (isLongArray(it)) if (not (it == None)) else (False))
        self.floatArrayClass = PrimitiveKClassImpl(unsafeCast(js('Float32Array')), 'FloatArray', lambda it: (isFloatArray(it)) if (not (it == None)) else (False))
        self.doubleArrayClass = PrimitiveKClassImpl(unsafeCast(js('Float64Array')), 'DoubleArray', lambda it: (isDoubleArray(it)) if (not (it == None)) else (False))
    
    def _get_anyClass__0_k_(self):
        return self.anyClass
    
    def _get_numberClass__0_k_(self):
        return self.numberClass
    
    def _get_nothingClass__0_k_(self):
        return self.nothingClass
    
    def _get_booleanClass__0_k_(self):
        return self.booleanClass
    
    def _get_byteClass__0_k_(self):
        return self.byteClass
    
    def _get_shortClass__0_k_(self):
        return self.shortClass
    
    def _get_intClass__0_k_(self):
        return self.intClass
    
    def _get_floatClass__0_k_(self):
        return self.floatClass
    
    def _get_doubleClass__0_k_(self):
        return self.doubleClass
    
    def _get_arrayClass__0_k_(self):
        return self.arrayClass
    
    def _get_stringClass__0_k_(self):
        return self.stringClass
    
    def _get_throwableClass__0_k_(self):
        return self.throwableClass
    
    def _get_booleanArrayClass__0_k_(self):
        return self.booleanArrayClass
    
    def _get_charArrayClass__0_k_(self):
        return self.charArrayClass
    
    def _get_byteArrayClass__0_k_(self):
        return self.byteArrayClass
    
    def _get_shortArrayClass__0_k_(self):
        return self.shortArrayClass
    
    def _get_intArrayClass__0_k_(self):
        return self.intArrayClass
    
    def _get_longArrayClass__0_k_(self):
        return self.longArrayClass
    
    def _get_floatArrayClass__0_k_(self):
        return self.floatArrayClass
    
    def _get_doubleArrayClass__0_k_(self):
        return self.doubleArrayClass
    
    def functionClass(self, arity):
        tmp0_elvis_lhs = _get_functionClasses_()[arity]
        def complexFunction_x4__Assign__Expr__Expr__Return__0(_this_run):
            result = PrimitiveKClassImpl(unsafeCast(js('Function')), str('Function') + str(arity), lambda it: (asDynamic(it).length is arity) if (jsTypeOf(it) is 'function') else (False))
            Unit_getInstance()
            Unexpected_operator_EQ(asDynamic(_get_functionClasses_())[arity], result)
            return result
        
        return (run_0(self, complexFunction_x4__Assign__Expr__Expr__Return__0)) if (tmp0_elvis_lhs == None) else (tmp0_elvis_lhs)
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

PrimitiveClasses_instance = None
def PrimitiveClasses_getInstance():
    if PrimitiveClasses_instance == None:
        PrimitiveClasses_0()
    
    return PrimitiveClasses_instance

def getKClass_0(jClass):
    if kotlin_Boolean(js('Array').isArray(jClass)):
        tmp = getKClassM_0(unsafeCast_0(jClass))
    else:
        tmp = getKClass1_0(unsafeCast_0(jClass))
    
    return tmp

def getKClassM_0(jClasses):
    tmp0_subject = len(jClasses)
    return (getKClass1_0(jClasses[0])) if (tmp0_subject == 1) else ((unsafeCast_0(NothingKClassImpl_getInstance())) if (tmp0_subject == 0) else (unsafeCast_0(ErrorKClass())))

def getKClass1_0(jClass):
    if jClass is js('String'):
        return unsafeCast_0(PrimitiveClasses_getInstance()._get_stringClass__0_k_())
    
    metadata = asDynamic(jClass)._metadata_
    if metadata != None:
        if metadata._kClass_ == None:
            kClass = SimpleKClassImpl(jClass)
            Unexpected_operator_EQ(metadata._kClass_, kClass)
            tmp = kClass
        else:
            tmp = metadata._kClass_
        
        tmp = kotlin_reflect_KClass_T_(tmp)
    else:
        tmp = SimpleKClassImpl(jClass)
    
    return tmp

def getKClassFromExpression_0(e):
    tmp0_subject = jsTypeOf(e)
    if tmp0_subject == 'string':
        tmp = PrimitiveClasses_getInstance()._get_stringClass__0_k_()
    elif tmp0_subject == 'number':
        tmp = (PrimitiveClasses_getInstance()._get_intClass__0_k_()) if (asDynamic(jsBitwiseOr(e, 0)) is e) else (PrimitiveClasses_getInstance()._get_doubleClass__0_k_())
    elif tmp0_subject == 'boolean':
        tmp = PrimitiveClasses_getInstance()._get_booleanClass__0_k_()
    elif tmp0_subject == 'function':
        tmp = PrimitiveClasses_getInstance().functionClass(kotlin_Int(asDynamic(e).length))
    else:
        if isBooleanArray(e):
            tmp = PrimitiveClasses_getInstance()._get_booleanArrayClass__0_k_()
        elif isCharArray(e):
            tmp = PrimitiveClasses_getInstance()._get_charArrayClass__0_k_()
        elif isByteArray(e):
            tmp = PrimitiveClasses_getInstance()._get_byteArrayClass__0_k_()
        elif isShortArray(e):
            tmp = PrimitiveClasses_getInstance()._get_shortArrayClass__0_k_()
        elif isIntArray(e):
            tmp = PrimitiveClasses_getInstance()._get_intArrayClass__0_k_()
        elif isLongArray(e):
            tmp = PrimitiveClasses_getInstance()._get_longArrayClass__0_k_()
        elif isFloatArray(e):
            tmp = PrimitiveClasses_getInstance()._get_floatArrayClass__0_k_()
        elif isDoubleArray(e):
            tmp = PrimitiveClasses_getInstance()._get_doubleArrayClass__0_k_()
        elif isInterface(e, KClass):
            tmp = visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrClassReferenceImpl
        elif isArray(e):
            tmp = PrimitiveClasses_getInstance()._get_arrayClass__0_k_()
        elif True:
            constructor = js('Object').getPrototypeOf(e).constructor
            if constructor is js('Object'):
                tmp = PrimitiveClasses_getInstance()._get_anyClass__0_k_()
            elif constructor is js('Error'):
                tmp = PrimitiveClasses_getInstance()._get_throwableClass__0_k_()
            else:
                jsClass = kotlin_js_JsClass_T_(constructor)
                tmp = getKClass1_0(jsClass)
            
            tmp = tmp
        
        tmp = tmp
    
    return unsafeCast_0(tmp)

class Appendable(Any):
    def append_wi8o78_k_(self, value):
        pass
    
    def append_v1o70a_k_(self, value):
        pass
    
    def append_n5ylwa_k_(self, value, startIndex, endIndex):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def StringBuilder_init__Init_(capacity, _this):
    StringBuilder_init__Init__1(_this)
    return _this

def StringBuilder_init__Create_(capacity):
    return StringBuilder_init__Init_(capacity, StringBuilder.__new__(StringBuilder))

def StringBuilder_init__Init__0(content, _this):
    StringBuilder.__init__(_this, toString_0(content))
    return _this

def StringBuilder_init__Create__0(content):
    return StringBuilder_init__Init__0(content, StringBuilder.__new__(StringBuilder))

def StringBuilder_init__Init__1(_this):
    StringBuilder.__init__(_this, '')
    return _this

def StringBuilder_init__Create__1():
    return StringBuilder_init__Init__1(StringBuilder.__new__(StringBuilder))

class StringBuilder(Appendable, CharSequence):
    def __init__(self, content):
        self.string = (content) if (not (content is undefined)) else ('')
    
    def _set_string__a4enbm_k_(self, _set___):
        self.string = _set___
    
    def _get_string__0_k_(self):
        return self.string
    
    def _get_length__0_k_(self):
        return kotlin_Int(asDynamic(self._get_string__0_k_()).length)
    
    def get_ha5a7z_k_(self, index):
        def complexFunction_x1__Raise__0(it):
            raise IndexOutOfBoundsException_init__Create__0((((str('index: ') + str(index)) + str(', length: ')) + str(self._get_length__0_k_())) + str('}'))
        
        return getOrElse(self._get_string__0_k_(), index, complexFunction_x1__Raise__0)
    
    def subSequence_27zxwg_k_(self, startIndex, endIndex):
        return substring(self._get_string__0_k_(), startIndex, endIndex)
    
    def append_wi8o78_k_(self, value):
        tmp0_this = self
        tmp0_this._set_string__a4enbm_k_(tmp0_this._get_string__0_k_() + value)
        return self
    
    def append_v1o70a_k_(self, value):
        tmp0_this = self
        tmp0_this._set_string__a4enbm_k_(tmp0_this._get_string__0_k_() + toString(value))
        return self
    
    def append_n5ylwa_k_(self, value, startIndex, endIndex):
        tmp0_elvis_lhs = value
        return self.appendRange_icedxh_k_(('null') if (tmp0_elvis_lhs == None) else (tmp0_elvis_lhs), startIndex, endIndex)
    
    def reverse_0_k_(self):
        reversed = ''
        index = (((len(self._get_string__0_k_()) - 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
        while index >= 0:
            tmp = self._get_string__0_k_()
            tmp0 = index
            index = (((tmp0 - 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
            low = charSequenceGet(tmp, tmp0)
            if (index >= 0) if (isLowSurrogate(low)) else (False):
                tmp = self._get_string__0_k_()
                tmp1 = index
                index = (((tmp1 - 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
                high = charSequenceGet(tmp, tmp1)
                if isHighSurrogate(high):
                    reversed = (reversed + high) + low
                else:
                    reversed = (reversed + low) + high
                
            else:
                reversed = reversed + low
            
        
        self._set_string__a4enbm_k_(reversed)
        return self
    
    def append_wi7j7l_k_(self, value):
        tmp0_this = self
        tmp0_this._set_string__a4enbm_k_(tmp0_this._get_string__0_k_() + toString(value))
        return self
    
    def append_vcj5fe_k_(self, value):
        tmp0_this = self
        tmp0_this._set_string__a4enbm_k_(tmp0_this._get_string__0_k_() + value)
        return self
    
    def append_84823_k_(self, value):
        tmp0_this = self
        tmp0_this._set_string__a4enbm_k_(tmp0_this._get_string__0_k_() + concatToString(value))
        return self
    
    def append_6wfw3l_k_(self, value):
        return self.append_uch40_k_(value)
    
    def append_uch40_k_(self, value):
        tmp0_this = self
        tmp = tmp0_this._get_string__0_k_()
        tmp1_elvis_lhs = value
        tmp0_this._set_string__a4enbm_k_(tmp + (('null') if (tmp1_elvis_lhs == None) else (tmp1_elvis_lhs)))
        return self
    
    def capacity_0_k_(self):
        return self._get_length__0_k_()
    
    def ensureCapacity_majfzk_k_(self, minimumCapacity):
        pass
    
    def indexOf_6wfw3l_k_(self, string):
        return kotlin_Int(asDynamic(self._get_string__0_k_()).indexOf(string))
    
    def indexOf_8i7b4u_k_(self, string, startIndex):
        return kotlin_Int(asDynamic(self._get_string__0_k_()).indexOf(string, startIndex))
    
    def lastIndexOf_6wfw3l_k_(self, string):
        return kotlin_Int(asDynamic(self._get_string__0_k_()).lastIndexOf(string))
    
    def lastIndexOf_8i7b4u_k_(self, string, startIndex):
        if (startIndex < 0) if (isEmpty(string)) else (False):
            return -1
        
        return kotlin_Int(asDynamic(self._get_string__0_k_()).lastIndexOf(string, startIndex))
    
    def insert_sv7uuf_k_(self, index, value):
        Companion_getInstance().checkPositionIndex_rvwcgf_k_(index, self._get_length__0_k_())
        self._set_string__a4enbm_k_((substring(self._get_string__0_k_(), 0, index) + value) + substring_0(self._get_string__0_k_(), index))
        return self
    
    def insert_259trv_k_(self, index, value):
        Companion_getInstance().checkPositionIndex_rvwcgf_k_(index, self._get_length__0_k_())
        self._set_string__a4enbm_k_((substring(self._get_string__0_k_(), 0, index) + value) + substring_0(self._get_string__0_k_(), index))
        return self
    
    def insert_n2q82c_k_(self, index, value):
        Companion_getInstance().checkPositionIndex_rvwcgf_k_(index, self._get_length__0_k_())
        self._set_string__a4enbm_k_((substring(self._get_string__0_k_(), 0, index) + concatToString(value)) + substring_0(self._get_string__0_k_(), index))
        return self
    
    def insert_59w5qx_k_(self, index, value):
        Companion_getInstance().checkPositionIndex_rvwcgf_k_(index, self._get_length__0_k_())
        self._set_string__a4enbm_k_((substring(self._get_string__0_k_(), 0, index) + toString(value)) + substring_0(self._get_string__0_k_(), index))
        return self
    
    def insert_25ayri_k_(self, index, value):
        Companion_getInstance().checkPositionIndex_rvwcgf_k_(index, self._get_length__0_k_())
        self._set_string__a4enbm_k_((substring(self._get_string__0_k_(), 0, index) + toString(value)) + substring_0(self._get_string__0_k_(), index))
        return self
    
    def insert_4wk0sg_k_(self, index, value):
        return self.insert_9z0klb_k_(index, value)
    
    def insert_9z0klb_k_(self, index, value):
        Companion_getInstance().checkPositionIndex_rvwcgf_k_(index, self._get_length__0_k_())
        tmp0_elvis_lhs = value
        toInsert = ('null') if (tmp0_elvis_lhs == None) else (tmp0_elvis_lhs)
        self._set_string__a4enbm_k_((substring(self._get_string__0_k_(), 0, index) + toInsert) + substring_0(self._get_string__0_k_(), index))
        return self
    
    def setLength_majfzk_k_(self, newLength):
        if newLength < 0:
            raise IllegalArgumentException_init__Create__0((str('Negative new length: ') + str(newLength)) + str('.'))
        
        if newLength <= self._get_length__0_k_():
            self._set_string__a4enbm_k_(substring(self._get_string__0_k_(), 0, newLength))
        else:
            tmp0_iterator = until(self._get_length__0_k_(), newLength).iterator_0_k_()
            while tmp0_iterator.hasNext_0_k_():
                i = tmp0_iterator.next_0_k_()
                tmp1_this = self
                tmp1_this._set_string__a4enbm_k_(tmp1_this._get_string__0_k_() + Char_0(0))
            
        
    
    def substring_ha5a7z_k_(self, startIndex):
        Companion_getInstance().checkPositionIndex_rvwcgf_k_(startIndex, self._get_length__0_k_())
        return substring_0(self._get_string__0_k_(), startIndex)
    
    def substring_27zxwg_k_(self, startIndex, endIndex):
        Companion_getInstance().checkBoundsIndexes_zd700_k_(startIndex, endIndex, self._get_length__0_k_())
        return substring(self._get_string__0_k_(), startIndex, endIndex)
    
    def trimToSize_sv8swh_k_(self):
        pass
    
    def toString(self):
        return self._get_string__0_k_()
    
    def clear_0_k_(self):
        self._set_string__a4enbm_k_('')
        return self
    
    def set_vljvec_k_(self, index, value):
        Companion_getInstance().checkElementIndex_rvwcgf_k_(index, self._get_length__0_k_())
        self._set_string__a4enbm_k_((substring(self._get_string__0_k_(), 0, index) + value) + substring_0(self._get_string__0_k_(), (((index + 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000))
    
    def setRange_sfallt_k_(self, startIndex, endIndex, value):
        self.checkReplaceRange_zd700_k_(startIndex, endIndex, self._get_length__0_k_())
        self._set_string__a4enbm_k_((substring(self._get_string__0_k_(), 0, startIndex) + value) + substring_0(self._get_string__0_k_(), endIndex))
        return self
    
    def checkReplaceRange_zd700_k_(self, startIndex, endIndex, length):
        if (True) if (startIndex < 0) else (startIndex > length):
            raise IndexOutOfBoundsException_init__Create__0(((str('startIndex: ') + str(startIndex)) + str(', length: ')) + str(length))
        
        if startIndex > endIndex:
            raise IllegalArgumentException_init__Create__0((((str('startIndex(') + str(startIndex)) + str(') > endIndex(')) + str(endIndex)) + str(')'))
        
    
    def deleteAt_ha5a7z_k_(self, index):
        Companion_getInstance().checkElementIndex_rvwcgf_k_(index, self._get_length__0_k_())
        self._set_string__a4enbm_k_(substring(self._get_string__0_k_(), 0, index) + substring_0(self._get_string__0_k_(), (((index + 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000))
        return self
    
    def deleteRange_27zxwg_k_(self, startIndex, endIndex):
        self.checkReplaceRange_zd700_k_(startIndex, endIndex, self._get_length__0_k_())
        self._set_string__a4enbm_k_(substring(self._get_string__0_k_(), 0, startIndex) + substring_0(self._get_string__0_k_(), endIndex))
        return self
    
    def toCharArray_tnuj0b_k_(self, destination, destinationOffset, startIndex, endIndex):
        Companion_getInstance().checkBoundsIndexes_zd700_k_(startIndex, endIndex, self._get_length__0_k_())
        Companion_getInstance().checkBoundsIndexes_zd700_k_(destinationOffset, (((((((destinationOffset + endIndex) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000) - startIndex) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000, len(destination))
        dstIndex = destinationOffset
        tmp0_iterator = until(startIndex, endIndex).iterator_0_k_()
        while tmp0_iterator.hasNext_0_k_():
            index = tmp0_iterator.next_0_k_()
            tmp1 = dstIndex
            dstIndex = (((tmp1 + 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
            destination.__setitem__(tmp1, charSequenceGet(self._get_string__0_k_(), index))
        
    
    def appendRange_4l12y3_k_(self, value, startIndex, endIndex):
        tmp0_this = self
        tmp0_this._set_string__a4enbm_k_(tmp0_this._get_string__0_k_() + concatToString_0(value, startIndex, endIndex))
        return self
    
    def appendRange_icedxh_k_(self, value, startIndex, endIndex):
        stringCsq = toString_0(value)
        Companion_getInstance().checkBoundsIndexes_zd700_k_(startIndex, endIndex, len(stringCsq))
        tmp0_this = self
        tmp0_this._set_string__a4enbm_k_(tmp0_this._get_string__0_k_() + substring(stringCsq, startIndex, endIndex))
        return self
    
    def insertRange_nw7vlg_k_(self, index, value, startIndex, endIndex):
        Companion_getInstance().checkPositionIndex_rvwcgf_k_(index, self._get_length__0_k_())
        self._set_string__a4enbm_k_((substring(self._get_string__0_k_(), 0, index) + concatToString_0(value, startIndex, endIndex)) + substring_0(self._get_string__0_k_(), index))
        return self
    
    def insertRange_nws7cq_k_(self, index, value, startIndex, endIndex):
        Companion_getInstance().checkPositionIndex_rvwcgf_k_(index, self._get_length__0_k_())
        stringCsq = toString_0(value)
        Companion_getInstance().checkBoundsIndexes_zd700_k_(startIndex, endIndex, len(stringCsq))
        self._set_string__a4enbm_k_((substring(self._get_string__0_k_(), 0, index) + substring(stringCsq, startIndex, endIndex)) + substring_0(self._get_string__0_k_(), index))
        return self
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    

def uppercaseChar(self):
    uppercase = uppercase(self)
    return (self) if (len(uppercase) > 1) else (charSequenceGet(uppercase, 0))

def lowercaseChar(self):
    return charSequenceGet(lowercase(self), 0)

def uppercase(self):
    return unsafeCast(asDynamic(self.toString()).toUpperCase())

def lowercase(self):
    return unsafeCast(asDynamic(self.toString()).toLowerCase())

def isLowSurrogate(self):
    return Companion_getInstance_17()._get_MIN_LOW_SURROGATE__0_k_().rangeTo_wi8o78_k_(Companion_getInstance_17()._get_MAX_LOW_SURROGATE__0_k_()).contains_wi8o78_k_(self)

def isHighSurrogate(self):
    return Companion_getInstance_17()._get_MIN_HIGH_SURROGATE__0_k_().rangeTo_wi8o78_k_(Companion_getInstance_17()._get_MAX_HIGH_SURROGATE__0_k_()).contains_wi8o78_k_(self)

def checkRadix(radix):
    if not numberRangeToNumber(2, 36).contains_ha5a7z_k_(radix):
        raise IllegalArgumentException_init__Create__0((str('radix ') + str(radix)) + str(' was not in valid range 2..36'))
    
    return radix

def _get_STRING_CASE_INSENSITIVE_ORDER_():
    return STRING_CASE_INSENSITIVE_ORDER

STRING_CASE_INSENSITIVE_ORDER = None
def nativeLastIndexOf(self, str, fromIndex):
    return kotlin_Int(asDynamic(self).lastIndexOf(str, fromIndex))

def substring(self, startIndex, endIndex):
    return kotlin_String(asDynamic(self).substring(startIndex, endIndex))

def substring_0(self, startIndex):
    return kotlin_String(asDynamic(self).substring(startIndex))

def compareTo(self, other, ignoreCase):
    if ignoreCase:
        n1 = len(self)
        n2 = len(other)
        min = minOf(n1, n2)
        if min == 0:
            return (((n1 - n2) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
        
        tmp0_iterator = until(0, min).iterator_0_k_()
        while tmp0_iterator.hasNext_0_k_():
            index = tmp0_iterator.next_0_k_()
            thisChar = charSequenceGet(self, index)
            otherChar = charSequenceGet(other, index)
            if not (thisChar == otherChar):
                thisChar = uppercaseChar(thisChar)
                otherChar = uppercaseChar(otherChar)
                if not (thisChar == otherChar):
                    thisChar = lowercaseChar(thisChar)
                    otherChar = lowercaseChar(otherChar)
                    if not (thisChar == otherChar):
                        return thisChar.compareTo_wi8o78_k_(otherChar)
                    
                
            
        
        return (((n1 - n2) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
    else:
        return compareTo_0(self, other)
    

def concatToString(self):
    result = ''
    tmp0_iterator = charArrayIterator(self)
    while tmp0_iterator.hasNext_0_k_():
        char = tmp0_iterator.next_0_k_()
        result = result + char
    
    return result

def concatToString_0(self, startIndex, endIndex):
    Companion_getInstance().checkBoundsIndexes_zd700_k_(startIndex, endIndex, len(self))
    result = ''
    tmp0_iterator = until(startIndex, endIndex).iterator_0_k_()
    while tmp0_iterator.hasNext_0_k_():
        index = tmp0_iterator.next_0_k_()
        result = result + self[index]
    
    return result

def toUpperCase(self):
    return kotlin_String(asDynamic(self).toUpperCase())

class sam_kotlin_Comparator_0(Comparator):
    def __init__(self, function):
        self.function = function
    
    def compare_1qgdm_k_(self, a, b):
        return self.function(a, b)
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def STRING_CASE_INSENSITIVE_ORDER_init_():
    tmp = lambda a, b: compareTo(a, b, True)
    return sam_kotlin_Comparator_0(tmp)

def _get_REPLACEMENT_BYTE_SEQUENCE_():
    return REPLACEMENT_BYTE_SEQUENCE

REPLACEMENT_BYTE_SEQUENCE = None
class Companion_18(Any):
    def __init__(self):
        global Companion_instance
        Companion_instance = self
        self.MIN_VALUE = Char_0(0)
        self.MAX_VALUE = Char_0(65535)
        self.MIN_HIGH_SURROGATE = Char_0(55296)
        self.MAX_HIGH_SURROGATE = Char_0(56319)
        self.MIN_LOW_SURROGATE = Char_0(56320)
        self.MAX_LOW_SURROGATE = Char_0(57343)
        self.MIN_SURROGATE = Char_0(55296)
        self.MAX_SURROGATE = Char_0(57343)
        self.SIZE_BYTES = 2
        self.SIZE_BITS = 16
    
    def _get_MIN_VALUE__0_k_(self):
        return self.MIN_VALUE
    
    def _get_MAX_VALUE__0_k_(self):
        return self.MAX_VALUE
    
    def _get_MIN_HIGH_SURROGATE__0_k_(self):
        return self.MIN_HIGH_SURROGATE
    
    def _get_MAX_HIGH_SURROGATE__0_k_(self):
        return self.MAX_HIGH_SURROGATE
    
    def _get_MIN_LOW_SURROGATE__0_k_(self):
        return self.MIN_LOW_SURROGATE
    
    def _get_MAX_LOW_SURROGATE__0_k_(self):
        return self.MAX_LOW_SURROGATE
    
    def _get_MIN_SURROGATE__0_k_(self):
        return self.MIN_SURROGATE
    
    def _get_MAX_SURROGATE__0_k_(self):
        return self.MAX_SURROGATE
    
    def _get_SIZE_BYTES__0_k_(self):
        return self.SIZE_BYTES
    
    def _get_SIZE_BITS__0_k_(self):
        return self.SIZE_BITS
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

Companion_instance = None
def Companion_getInstance_17():
    if Companion_instance == None:
        Companion_18()
    
    return Companion_instance

class Char_0(Comparable):
    def __init__(self, code):
        Companion_getInstance_17()
        self.value = UShort__toInt_impl(code)
    
    def _get_value__0_k_(self):
        return self.value
    
    def compareTo_wi8o78_k_(self, other):
        return (((self._get_value__0_k_() - other._get_value__0_k_()) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
    
    def plus_ha5a7z_k_(self, other):
        return numberToChar((((self._get_value__0_k_() + other) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
    
    def minus_wi8o78_k_(self, other):
        return (((self._get_value__0_k_() - other._get_value__0_k_()) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
    
    def minus_ha5a7z_k_(self, other):
        return numberToChar((((self._get_value__0_k_() - other) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
    
    def inc_0_k_(self):
        return numberToChar((((self._get_value__0_k_() + 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
    
    def dec_0_k_(self):
        return numberToChar((((self._get_value__0_k_() - 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
    
    def rangeTo_wi8o78_k_(self, other):
        return CharRange(self, other)
    
    def toByte_0_k_(self):
        return ((self._get_value__0_k_() + 0x80) & 0xff) - 0x80
    
    def toChar_0_k_(self):
        return self
    
    def toShort_0_k_(self):
        return ((self._get_value__0_k_() + 0x8000) & 0xffff) - 0x8000
    
    def toInt_0_k_(self):
        return self._get_value__0_k_()
    
    def toLong_0_k_(self):
        return self._get_value__0_k_()
    
    def toFloat_0_k_(self):
        return kotlin_Float(self._get_value__0_k_())
    
    def toDouble_0_k_(self):
        return kotlin_Double(self._get_value__0_k_())
    
    def equals(self, other):
        if other is self:
            return True
        
        if not isinstance(other, Char_0):
            return False
        
        return self._get_value__0_k_() == kotlin_Char(other)._get_value__0_k_()
    
    def hashCode(self):
        return self._get_value__0_k_()
    
    def toString(self):
        return unsafeCast(js('String').fromCharCode(self._get_value__0_k_()))
    

class Iterable(Any):
    def iterator_0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class Collection(Iterable):
    def _get_size__0_k_(self):
        pass
    
    def isEmpty_0_k_(self):
        pass
    
    def contains_2bq_k_(self, element):
        pass
    
    def iterator_0_k_(self):
        pass
    
    def containsAll_dxd4eo_k_(self, elements):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class Set(Collection):
    def _get_size__0_k_(self):
        pass
    
    def isEmpty_0_k_(self):
        pass
    
    def contains_2bq_k_(self, element):
        pass
    
    def iterator_0_k_(self):
        pass
    
    def containsAll_dxd4eo_k_(self, elements):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class List(Collection):
    def _get_size__0_k_(self):
        pass
    
    def isEmpty_0_k_(self):
        pass
    
    def contains_2bq_k_(self, element):
        pass
    
    def iterator_0_k_(self):
        pass
    
    def containsAll_dxd4eo_k_(self, elements):
        pass
    
    def get_ha5a7z_k_(self, index):
        pass
    
    def indexOf_2bq_k_(self, element):
        pass
    
    def lastIndexOf_2bq_k_(self, element):
        pass
    
    def listIterator_0_k_(self):
        pass
    
    def listIterator_ha5a7z_k_(self, index):
        pass
    
    def subList_27zxwg_k_(self, fromIndex, toIndex):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class Entry(Any):
    def _get_key__0_k_(self):
        pass
    
    def _get_value__0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class Map_0(Any):
    def _get_size__0_k_(self):
        pass
    
    def isEmpty_0_k_(self):
        pass
    
    def containsKey_2bw_k_(self, key):
        pass
    
    def containsValue_2c7_k_(self, value):
        pass
    
    def get_2bw_k_(self, key):
        pass
    
    def _get_keys__0_k_(self):
        pass
    
    def _get_values__0_k_(self):
        pass
    
    def _get_entries__0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class MutableIterable:
    pass

class MutableCollection(Collection, MutableIterable):
    def iterator_0_k_(self):
        pass
    
    def add_2bq_k_(self, element):
        pass
    
    def remove_2bq_k_(self, element):
        pass
    
    def addAll_dxd4eo_k_(self, elements):
        pass
    
    def removeAll_dxd4eo_k_(self, elements):
        pass
    
    def retainAll_dxd4eo_k_(self, elements):
        pass
    
    def clear_sv8swh_k_(self):
        pass
    
    def _get_size__0_k_(self):
        pass
    
    def isEmpty_0_k_(self):
        pass
    
    def contains_2bq_k_(self, element):
        pass
    
    def containsAll_dxd4eo_k_(self, elements):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class MutableIterable(Iterable):
    def iterator_0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class MutableSet(Set, MutableCollection):
    def iterator_0_k_(self):
        pass
    
    def add_2bq_k_(self, element):
        pass
    
    def remove_2bq_k_(self, element):
        pass
    
    def addAll_dxd4eo_k_(self, elements):
        pass
    
    def removeAll_dxd4eo_k_(self, elements):
        pass
    
    def retainAll_dxd4eo_k_(self, elements):
        pass
    
    def clear_sv8swh_k_(self):
        pass
    
    def _get_size__0_k_(self):
        pass
    
    def isEmpty_0_k_(self):
        pass
    
    def contains_2bq_k_(self, element):
        pass
    
    def containsAll_dxd4eo_k_(self, elements):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class MutableList(List, MutableCollection):
    def add_2bq_k_(self, element):
        pass
    
    def remove_2bq_k_(self, element):
        pass
    
    def addAll_dxd4eo_k_(self, elements):
        pass
    
    def addAll_xggsjz_k_(self, index, elements):
        pass
    
    def removeAll_dxd4eo_k_(self, elements):
        pass
    
    def retainAll_dxd4eo_k_(self, elements):
        pass
    
    def clear_sv8swh_k_(self):
        pass
    
    def set_ddb1qf_k_(self, index, element):
        pass
    
    def add_vz2mgm_k_(self, index, element):
        pass
    
    def removeAt_ha5a7z_k_(self, index):
        pass
    
    def listIterator_0_k_(self):
        pass
    
    def listIterator_ha5a7z_k_(self, index):
        pass
    
    def subList_27zxwg_k_(self, fromIndex, toIndex):
        pass
    
    def _get_size__0_k_(self):
        pass
    
    def isEmpty_0_k_(self):
        pass
    
    def contains_2bq_k_(self, element):
        pass
    
    def iterator_0_k_(self):
        pass
    
    def containsAll_dxd4eo_k_(self, elements):
        pass
    
    def get_ha5a7z_k_(self, index):
        pass
    
    def indexOf_2bq_k_(self, element):
        pass
    
    def lastIndexOf_2bq_k_(self, element):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class MutableEntry(Entry):
    def setValue_2c7_k_(self, newValue):
        pass
    
    def _get_key__0_k_(self):
        pass
    
    def _get_value__0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class MutableMap(Map_0):
    def put_1q9pf_k_(self, key, value):
        pass
    
    def remove_2bw_k_(self, key):
        pass
    
    def putAll_nn707j_k_(self, _from):
        pass
    
    def clear_sv8swh_k_(self):
        pass
    
    def _get_keys__0_k_(self):
        pass
    
    def _get_values__0_k_(self):
        pass
    
    def _get_entries__0_k_(self):
        pass
    
    def _get_size__0_k_(self):
        pass
    
    def isEmpty_0_k_(self):
        pass
    
    def containsKey_2bw_k_(self, key):
        pass
    
    def containsValue_2c7_k_(self, value):
        pass
    
    def get_2bw_k_(self, key):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class Companion_19(Any):
    def __init__(self):
        global Companion_instance
        Companion_instance = self
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

Companion_instance = None
def Companion_getInstance_18():
    if Companion_instance == None:
        Companion_19()
    
    return Companion_instance

class Enum(Comparable):
    def __init__(self, name, ordinal):
        Companion_getInstance_18()
        self.name = name
        self.ordinal = ordinal
    
    def _get_name__0_k_(self):
        return self.name
    
    def _get_ordinal__0_k_(self):
        return self.ordinal
    
    def compareTo_2bq_k_(self, other):
        return compareTo_0(self._get_ordinal__0_k_(), other._get_ordinal__0_k_())
    
    def equals(self, other):
        return self is other
    
    def hashCode(self):
        return identityHashCode(self)
    
    def toString(self):
        return self._get_name__0_k_()
    

def arrayOfNulls(size):
    return fillArrayVal(Array(size), None)

def byteArrayOf(*elements):
    return elements

def arrayOf(*elements):
    return unsafeCast_0(elements)

def toString(self):
    tmp0_safe_receiver = self
    tmp1_elvis_lhs = (None) if (tmp0_safe_receiver == None) else (toString_0(tmp0_safe_receiver))
    return ('null') if (tmp1_elvis_lhs == None) else (tmp1_elvis_lhs)

def plus(self, other):
    tmp2_safe_receiver = self
    tmp3_elvis_lhs = (None) if (tmp2_safe_receiver == None) else (toString_0(tmp2_safe_receiver))
    tmp = ('null') if (tmp3_elvis_lhs == None) else (tmp3_elvis_lhs)
    tmp0_safe_receiver = other
    tmp1_elvis_lhs = (None) if (tmp0_safe_receiver == None) else (toString_0(tmp0_safe_receiver))
    return tmp + (('null') if (tmp1_elvis_lhs == None) else (tmp1_elvis_lhs))

class DefaultConstructorMarker(Any):
    def __init__(self):
        global DefaultConstructorMarker_instance
        DefaultConstructorMarker_instance = self
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

DefaultConstructorMarker_instance = None
def DefaultConstructorMarker_getInstance():
    if DefaultConstructorMarker_instance == None:
        DefaultConstructorMarker()
    
    return DefaultConstructorMarker_instance

def fillArrayVal(array, initValue):
    tmp0_iterator = numberRangeToNumber(0, (((len(array) - 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000).iterator_0_k_()
    while tmp0_iterator.hasNext_0_k_():
        i = tmp0_iterator.next_0_k_()
        array.__setitem__(i, initValue)
    
    return array

def arrayIterator(array):
    return _no_name_provided__0()

def booleanArrayIterator(array):
    return _no_name_provided__1()

def charArrayIterator(array):
    return _no_name_provided__2()

def byteArrayIterator(array):
    return _no_name_provided__3()

def shortArrayIterator(array):
    return _no_name_provided__4()

def intArrayIterator(array):
    return _no_name_provided__5()

def floatArrayIterator(array):
    return _no_name_provided__6()

def longArrayIterator(array):
    return _no_name_provided__7()

def doubleArrayIterator(array):
    return _no_name_provided__8()

def booleanArray(size):
    return unsafeCast(withType('BooleanArray', fillArrayVal(Array(size), False)))

def charArray(size):
    return unsafeCast(withType('CharArray', fillArrayVal(Array(size), Char(0))))

def longArray(size):
    return unsafeCast(withType('LongArray', fillArrayVal(Array(size), 0)))

def booleanArrayOf(arr):
    return unsafeCast(withType('BooleanArray', asDynamic(arr).slice()))

def charArrayOf(arr):
    return unsafeCast(withType('CharArray', asDynamic(arr).slice()))

def longArrayOf(arr):
    return unsafeCast(withType('LongArray', asDynamic(arr).slice()))

class _no_name_provided__0(Iterator_3):
    def __init__(self):
        self.index = 0
    
    def _set_index__majfzk_k_(self, _set___):
        self.index = _set___
    
    def _get_index__0_k_(self):
        return self.index
    
    def hasNext_0_k_(self):
        return not (self._get_index__0_k_() == len(array))
    
    def next_0_k_(self):
        if not (self._get_index__0_k_() == len(array)):
            tmp0_this = self
            tmp1 = tmp0_this._get_index__0_k_()
            tmp0_this._set_index__majfzk_k_((((tmp1 + 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
            tmp = array[tmp1]
        else:
            raise NoSuchElementException_init__Create__0(str(self._get_index__0_k_()))
        
        return tmp
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class _no_name_provided__1(BooleanIterator):
    def __init__(self):
        BooleanIterator.__init__(self)
        self.index = 0
    
    def _set_index__majfzk_k_(self, _set___):
        self.index = _set___
    
    def _get_index__0_k_(self):
        return self.index
    
    def hasNext_0_k_(self):
        return not (self._get_index__0_k_() == len(array))
    
    def nextBoolean_0_k_(self):
        if not (self._get_index__0_k_() == len(array)):
            tmp0_this = self
            tmp1 = tmp0_this._get_index__0_k_()
            tmp0_this._set_index__majfzk_k_((((tmp1 + 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
            tmp = array[tmp1]
        else:
            raise NoSuchElementException_init__Create__0(str(self._get_index__0_k_()))
        
        return tmp
    
    def next_0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class _no_name_provided__2(CharIterator):
    def __init__(self):
        CharIterator.__init__(self)
        self.index = 0
    
    def _set_index__majfzk_k_(self, _set___):
        self.index = _set___
    
    def _get_index__0_k_(self):
        return self.index
    
    def hasNext_0_k_(self):
        return not (self._get_index__0_k_() == len(array))
    
    def nextChar_0_k_(self):
        if not (self._get_index__0_k_() == len(array)):
            tmp0_this = self
            tmp1 = tmp0_this._get_index__0_k_()
            tmp0_this._set_index__majfzk_k_((((tmp1 + 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
            tmp = array[tmp1]
        else:
            raise NoSuchElementException_init__Create__0(str(self._get_index__0_k_()))
        
        return tmp
    
    def next_0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class _no_name_provided__3(ByteIterator):
    def __init__(self):
        ByteIterator.__init__(self)
        self.index = 0
    
    def _set_index__majfzk_k_(self, _set___):
        self.index = _set___
    
    def _get_index__0_k_(self):
        return self.index
    
    def hasNext_0_k_(self):
        return not (self._get_index__0_k_() == len(array))
    
    def nextByte_0_k_(self):
        if not (self._get_index__0_k_() == len(array)):
            tmp0_this = self
            tmp1 = tmp0_this._get_index__0_k_()
            tmp0_this._set_index__majfzk_k_((((tmp1 + 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
            tmp = array[tmp1]
        else:
            raise NoSuchElementException_init__Create__0(str(self._get_index__0_k_()))
        
        return tmp
    
    def next_0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class _no_name_provided__4(ShortIterator):
    def __init__(self):
        ShortIterator.__init__(self)
        self.index = 0
    
    def _set_index__majfzk_k_(self, _set___):
        self.index = _set___
    
    def _get_index__0_k_(self):
        return self.index
    
    def hasNext_0_k_(self):
        return not (self._get_index__0_k_() == len(array))
    
    def nextShort_0_k_(self):
        if not (self._get_index__0_k_() == len(array)):
            tmp0_this = self
            tmp1 = tmp0_this._get_index__0_k_()
            tmp0_this._set_index__majfzk_k_((((tmp1 + 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
            tmp = array[tmp1]
        else:
            raise NoSuchElementException_init__Create__0(str(self._get_index__0_k_()))
        
        return tmp
    
    def next_0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class _no_name_provided__5(IntIterator):
    def __init__(self):
        IntIterator.__init__(self)
        self.index = 0
    
    def _set_index__majfzk_k_(self, _set___):
        self.index = _set___
    
    def _get_index__0_k_(self):
        return self.index
    
    def hasNext_0_k_(self):
        return not (self._get_index__0_k_() == len(array))
    
    def nextInt_0_k_(self):
        if not (self._get_index__0_k_() == len(array)):
            tmp0_this = self
            tmp1 = tmp0_this._get_index__0_k_()
            tmp0_this._set_index__majfzk_k_((((tmp1 + 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
            tmp = array[tmp1]
        else:
            raise NoSuchElementException_init__Create__0(str(self._get_index__0_k_()))
        
        return tmp
    
    def next_0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class _no_name_provided__6(FloatIterator):
    def __init__(self):
        FloatIterator.__init__(self)
        self.index = 0
    
    def _set_index__majfzk_k_(self, _set___):
        self.index = _set___
    
    def _get_index__0_k_(self):
        return self.index
    
    def hasNext_0_k_(self):
        return not (self._get_index__0_k_() == len(array))
    
    def nextFloat_0_k_(self):
        if not (self._get_index__0_k_() == len(array)):
            tmp0_this = self
            tmp1 = tmp0_this._get_index__0_k_()
            tmp0_this._set_index__majfzk_k_((((tmp1 + 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
            tmp = array[tmp1]
        else:
            raise NoSuchElementException_init__Create__0(str(self._get_index__0_k_()))
        
        return tmp
    
    def next_0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class _no_name_provided__7(LongIterator):
    def __init__(self):
        LongIterator.__init__(self)
        self.index = 0
    
    def _set_index__majfzk_k_(self, _set___):
        self.index = _set___
    
    def _get_index__0_k_(self):
        return self.index
    
    def hasNext_0_k_(self):
        return not (self._get_index__0_k_() == len(array))
    
    def nextLong_0_k_(self):
        if not (self._get_index__0_k_() == len(array)):
            tmp0_this = self
            tmp1 = tmp0_this._get_index__0_k_()
            tmp0_this._set_index__majfzk_k_((((tmp1 + 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
            tmp = array[tmp1]
        else:
            raise NoSuchElementException_init__Create__0(str(self._get_index__0_k_()))
        
        return tmp
    
    def next_0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class _no_name_provided__8(DoubleIterator):
    def __init__(self):
        DoubleIterator.__init__(self)
        self.index = 0
    
    def _set_index__majfzk_k_(self, _set___):
        self.index = _set___
    
    def _get_index__0_k_(self):
        return self.index
    
    def hasNext_0_k_(self):
        return not (self._get_index__0_k_() == len(array))
    
    def nextDouble_0_k_(self):
        if not (self._get_index__0_k_() == len(array)):
            tmp0_this = self
            tmp1 = tmp0_this._get_index__0_k_()
            tmp0_this._set_index__majfzk_k_((((tmp1 + 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
            tmp = array[tmp1]
        else:
            raise NoSuchElementException_init__Create__0(str(self._get_index__0_k_()))
        
        return tmp
    
    def next_0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def _get_buf_():
    return buf

buf = None
def _get_bufFloat64_():
    return bufFloat64

bufFloat64 = None
def _get_bufFloat32_():
    return bufFloat32

bufFloat32 = None
def _get_bufInt32_():
    return bufInt32

bufInt32 = None
def _get_lowIndex_():
    return lowIndex

lowIndex = None
def _get_highIndex_():
    return highIndex

highIndex = None
def getNumberHashCode(obj):
    if unsafeCast_0(jsBitwiseOr(obj, 0)) is obj:
        return ((obj + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
    
    _get_bufFloat64_().__setitem__(0, obj)
    return (((imul(_get_bufInt32_()[_get_highIndex_()], 31) + _get_bufInt32_()[_get_lowIndex_()]) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000

class DoNotIntrinsify(Annotation):
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
        tmp = Char(unsafeCast(asDynamic(a).charCodeAt(index)))
    else:
        tmp = a.get_ha5a7z_k_(index)
    
    return tmp

def isString(a):
    return jsTypeOf(a) == 'string'

def charSequenceLength(a):
    if isString(a):
        tmp = unsafeCast(asDynamic(a).length)
    else:
        tmp = a._get_length__0_k_()
    
    return tmp

def charSequenceSubSequence(a, startIndex, endIndex):
    if isString(a):
        tmp = unsafeCast(asDynamic(a).substring(startIndex, endIndex))
    else:
        tmp = a.subSequence_27zxwg_k_(startIndex, endIndex)
    
    return tmp

def arrayToString(array):
    return joinToString(array, ', ', '[', ']', translateCallArguments_3, translateCallArguments_4, lambda it: toString_0(it))

def compareTo_0(a, b):
    tmp0_subject = jsTypeOf(a)
    if tmp0_subject == 'number':
        if jsTypeOf(b) == 'number':
            tmp = doubleCompareTo(a, b)
        elif isinstance(b, Long):
            tmp = doubleCompareTo(a, kotlin_Long(b).toDouble_0_k_())
        elif True:
            tmp = primitiveCompareTo(a, b)
        
        tmp = tmp
    elif (True) if (tmp0_subject == 'string') else (tmp0_subject == 'boolean'):
        tmp = primitiveCompareTo(a, b)
    else:
        tmp = compareToDoNotIntrinsicify(kotlin_Comparable_dynamic_(a), b)
    
    return tmp

def doubleCompareTo(a, b):
    if a < b:
        tmp = -1
    elif a > b:
        tmp = 1
    elif a is b:
        if a is not 0:
            tmp = 0
        else:
            ia = asDynamic(1) / a
            if ia is asDynamic(1) / b:
                tmp = 0
            elif ia < 0:
                tmp = -1
            else:
                tmp = 1
            
            tmp = tmp
        
        tmp = tmp
    elif a is not a:
        tmp = (0) if (b is not b) else (1)
    else:
        tmp = -1
    
    return tmp

def primitiveCompareTo(a, b):
    return (-1) if (a < b) else ((1) if (a > b) else (0))

def compareToDoNotIntrinsicify(a, b):
    return a.compareTo_2c5_k_(b)

def construct(constructorType, resultType, *args):
    return kotlin_Any(js('Reflect').construct(constructorType, args, resultType))

def identityHashCode(obj):
    return getObjectHashCode(obj)

def getObjectHashCode(obj):
    if not jsIn(_get_OBJECT_HASH_CODE_PROPERTY_NAME_(), kotlin_Any(obj)):
        hash = jsBitwiseOr(js('Math').random() * _get_POW_2_32_(), 0)
        descriptor = js('new Object()')
        Unexpected_operator_EQ(descriptor.value, hash)
        Unexpected_operator_EQ(descriptor.enumerable, False)
        js('Object').defineProperty(obj, _get_OBJECT_HASH_CODE_PROPERTY_NAME_(), descriptor)
    
    return unsafeCast(obj[_get_OBJECT_HASH_CODE_PROPERTY_NAME_()])

def _get_OBJECT_HASH_CODE_PROPERTY_NAME_():
    return OBJECT_HASH_CODE_PROPERTY_NAME

OBJECT_HASH_CODE_PROPERTY_NAME = None
def _get_POW_2_32_():
    return POW_2_32

POW_2_32 = None
def toString_0(o):
    return ('null') if (o == None) else (('[...]') if (isArrayish(o)) else (unsafeCast(o.toString())))

def hashCode(obj):
    if obj == None:
        return 0
    
    tmp0_subject = jsTypeOf(obj)
    return (kotlin_Int((obj.hashCode()) if ('function' is jsTypeOf(obj.hashCode)) else (getObjectHashCode(obj)))) if (tmp0_subject == 'object') else ((getObjectHashCode(obj)) if (tmp0_subject == 'function') else ((getNumberHashCode(kotlin_Double(obj))) if (tmp0_subject == 'number') else (((1) if (unsafeCast(obj)) else (0)) if (tmp0_subject == 'boolean') else (getStringHashCode(kotlin_String(js('String')(obj)))))))

def getStringHashCode(str):
    hash = 0
    length = len(str)
    tmp0_iterator = numberRangeToNumber(0, (((length - 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000).iterator_0_k_()
    while tmp0_iterator.hasNext_0_k_():
        i = tmp0_iterator.next_0_k_()
        code = kotlin_Int(asDynamic(str).charCodeAt(i))
        hash = (((imul(hash, 31) + code) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
    
    return hash

def anyToString(o):
    return kotlin_String(js('Object').prototype.toString.call(o))

def equals(obj1, obj2):
    if obj1 == None:
        return obj2 == None
    
    if obj2 == None:
        return False
    
    if (jsTypeOf(obj1.equals) == 'function') if (jsTypeOf(obj1) == 'object') else (False):
        return kotlin_Boolean(obj1.equals(obj2))
    
    if obj1 is not obj1:
        return obj2 is not obj2
    
    if (jsTypeOf(obj2) == 'number') if (jsTypeOf(obj1) == 'number') else (False):
        return ((True) if (obj1 is not 0) else (asDynamic(1) / obj1 is asDynamic(1) / obj2)) if (obj1 is obj2) else (False)
    
    return obj1 is obj2

def boxIntrinsic(x):
    return error('Should be lowered')

def unboxIntrinsic(x):
    return error('Should be lowered')

def captureStack(instance, constructorFunction):
    if js('Error').captureStackTrace != None:
        js('Error').captureStackTrace(instance, constructorFunction)
    else:
        Unexpected_operator_EQ(asDynamic(instance).stack, js('new Error()').stack)
    

def newThrowable(message, cause):
    throwable = js('new Error()')
    if isUndefined(message):
        if isUndefined(cause):
            tmp = message
        else:
            tmp0_safe_receiver = cause
            tmp1_elvis_lhs = (None) if (tmp0_safe_receiver == None) else (tmp0_safe_receiver.toString())
            tmp = (undefined) if (tmp1_elvis_lhs == None) else (tmp1_elvis_lhs)
        
        tmp = tmp
    else:
        tmp2_elvis_lhs = message
        tmp = (undefined) if (tmp2_elvis_lhs == None) else (tmp2_elvis_lhs)
    
    Unexpected_operator_EQ(throwable.message, tmp)
    Unexpected_operator_EQ(throwable.cause, cause)
    Unexpected_operator_EQ(throwable.name, 'Throwable')
    return unsafeCast(throwable)

def isUndefined(value):
    return value is undefined

def extendThrowable(this_, message, cause):
    js('Error').call(this_)
    setPropertiesToThrowableInstance(this_, message, cause)

def setPropertiesToThrowableInstance(this_, message, cause):
    if not hasOwnPrototypeProperty(kotlin_Any(this_), 'message'):
        if message == None:
            if not (message is None):
                tmp0_safe_receiver = cause
                tmp1_elvis_lhs = (None) if (tmp0_safe_receiver == None) else (tmp0_safe_receiver.toString())
                tmp = (undefined) if (tmp1_elvis_lhs == None) else (tmp1_elvis_lhs)
            else:
                tmp = undefined
            
            tmp = tmp
        else:
            tmp = message
        
        Unexpected_operator_EQ(this_.message, tmp)
    
    if not hasOwnPrototypeProperty(kotlin_Any(this_), 'cause'):
        Unexpected_operator_EQ(this_.cause, cause)
    
    Unexpected_operator_EQ(this_.name, Companion.getPrototypeOf(this_).constructor.name)

def hasOwnPrototypeProperty(o, name):
    return unsafeCast(Companion.getPrototypeOf(o).hasOwnProperty(name))

def returnIfSuspended(argument):
    raise Exception_init__Create__0('Implemented as intrinsic')

def getContinuation():
    raise Exception_init__Create__0('Implemented as intrinsic')

def suspendCoroutineUninterceptedOrReturnJS(block):
    return returnIfSuspended(block(getContinuation()))

def getCoroutineContext():
    return getContinuation()._get_context__0_k_()

def unreachableDeclarationLog():
    asDynamic(console).trace('Unreachable declaration')

def unreachableDeclarationException():
    raise Error('Unreachable declaration')

def ensureNotNull(v):
    return (THROW_NPE()) if (v == None) else (v)

def THROW_NPE():
    raise NullPointerException_init__Create_()

def noWhenBranchMatchedException():
    raise NoWhenBranchMatchedException_init__Create_()

def THROW_CCE():
    raise ClassCastException_init__Create_()

def throwUninitializedPropertyAccessException(name):
    raise UninitializedPropertyAccessException_init__Create__0((str('lateinit property ') + str(name)) + str(' has not been initialized'))

def throwKotlinNothingValueException():
    raise KotlinNothingValueException_init__Create_()

def THROW_ISE():
    raise IllegalStateException_init__Create_()

def THROW_IAE(msg):
    raise IllegalArgumentException_init__Create__0(msg)

def jsEqeq(a, b):
    pass

class JsIntrinsic(Annotation):
    def __init__(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def jsNotEq(a, b):
    pass

def jsEqeqeq(a, b):
    pass

def jsNotEqeq(a, b):
    pass

def jsGt(a, b):
    pass

def jsGtEq(a, b):
    pass

def jsLt(a, b):
    pass

def jsLtEq(a, b):
    pass

def jsNot(a):
    pass

def jsUnaryPlus(a):
    pass

def jsUnaryMinus(a):
    pass

def jsPlus(a, b):
    pass

def jsMinus(a, b):
    pass

def jsMult(a, b):
    pass

def jsDiv(a, b):
    pass

def jsMod(a, b):
    pass

def jsOr(a, b):
    pass

def jsBitAnd(a, b):
    pass

def jsBitOr(a, b):
    pass

def jsBitXor(a, b):
    pass

def jsBitNot(a):
    pass

def jsBitShiftR(a, b):
    pass

def jsBitShiftRU(a, b):
    pass

def jsBitShiftL(a, b):
    pass

def jsInstanceOfIntrinsic(a, b):
    pass

def objectCreate():
    pass

def jsNewTarget(a):
    pass

def emptyObject(a):
    pass

def openInitializerBox(a, b):
    pass

def DefaultType():
    pass

def jsClassIntrinsic():
    pass

def unreachable():
    pass

def jsArrayLength(a):
    pass

def jsArrayGet(a, b):
    pass

def jsArraySet(a, b, c):
    pass

def arrayLiteral(a):
    pass

def int8Array(a):
    pass

def int16Array(a):
    pass

def int32Array(a):
    pass

def float32Array(a):
    pass

def float64Array(a):
    pass

def int8ArrayOf(a):
    pass

def int16ArrayOf(a):
    pass

def int32ArrayOf(a):
    pass

def float32ArrayOf(a):
    pass

def float64ArrayOf(a):
    pass

def jsBind(receiver, target):
    pass

def sharedBoxCreate(v):
    pass

def sharedBoxRead(box):
    pass

def sharedBoxWrite(box, nv):
    pass

def jsUndefined():
    pass

def emptyArray():
    return kotlin_Array_T_(js('[]'))

def enumValueOfIntrinsic(name):
    raise IllegalStateException_init__Create__0('Should be replaced by compiler')

def enumValuesIntrinsic():
    raise IllegalStateException_init__Create__0('Should be replaced by compiler')

class Companion_20(Any):
    def __init__(self):
        global Companion_instance
        Companion_instance = self
        self.MIN_VALUE = -9223372036854775808
        self.MAX_VALUE = 9223372036854775807
        self.SIZE_BYTES = 8
        self.SIZE_BITS = 64
    
    def _get_MIN_VALUE__0_k_(self):
        return self.MIN_VALUE
    
    def _get_MAX_VALUE__0_k_(self):
        return self.MAX_VALUE
    
    def _get_SIZE_BYTES__0_k_(self):
        return self.SIZE_BYTES
    
    def _get_SIZE_BITS__0_k_(self):
        return self.SIZE_BITS
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

Companion_instance = None
def Companion_getInstance_19():
    if Companion_instance == None:
        Companion_20()
    
    return Companion_instance

class Long(Number_0, Comparable):
    def __init__(self, low, high):
        Companion_getInstance_19()
        Number_0.__init__(self)
        self.low = low
        self.high = high
    
    def _get_low__0_k_(self):
        return self.low
    
    def _get_high__0_k_(self):
        return self.high
    
    def compareTo_wi8e9i_k_(self, other):
        return self.compareTo_wiekkq_k_(other)
    
    def compareTo_dip2j2_k_(self, other):
        return self.compareTo_wiekkq_k_(other)
    
    def compareTo_ha5a7z_k_(self, other):
        return self.compareTo_wiekkq_k_(other)
    
    def compareTo_wiekkq_k_(self, other):
        return compare(self, other)
    
    def compareTo_dbmacu_k_(self, other):
        return compareTo_0(self.toFloat_0_k_(), other)
    
    def compareTo_e2tf9d_k_(self, other):
        return compareTo_0(self.toDouble_0_k_(), other)
    
    def plus_wi8e9i_k_(self, other):
        return (((self + other) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000
    
    def plus_dip2j2_k_(self, other):
        return (((self + other) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000
    
    def plus_ha5a7z_k_(self, other):
        return (((self + other) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000
    
    def plus_wiekkq_k_(self, other):
        return add(self, other)
    
    def plus_dbmacu_k_(self, other):
        return self.toFloat_0_k_() + other
    
    def plus_e2tf9d_k_(self, other):
        return self.toDouble_0_k_() + other
    
    def minus_wi8e9i_k_(self, other):
        return (((self - other) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000
    
    def minus_dip2j2_k_(self, other):
        return (((self - other) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000
    
    def minus_ha5a7z_k_(self, other):
        return (((self - other) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000
    
    def minus_wiekkq_k_(self, other):
        return subtract(self, other)
    
    def minus_dbmacu_k_(self, other):
        return self.toFloat_0_k_() - other
    
    def minus_e2tf9d_k_(self, other):
        return self.toDouble_0_k_() - other
    
    def times_wi8e9i_k_(self, other):
        return (((self * other) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000
    
    def times_dip2j2_k_(self, other):
        return (((self * other) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000
    
    def times_ha5a7z_k_(self, other):
        return (((self * other) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000
    
    def times_wiekkq_k_(self, other):
        return multiply(self, other)
    
    def times_dbmacu_k_(self, other):
        return self.toFloat_0_k_() * other
    
    def times_e2tf9d_k_(self, other):
        return self.toDouble_0_k_() * other
    
    def div_wi8e9i_k_(self, other):
        return (((self // other) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000
    
    def div_dip2j2_k_(self, other):
        return (((self // other) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000
    
    def div_ha5a7z_k_(self, other):
        return (((self // other) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000
    
    def div_wiekkq_k_(self, other):
        return divide(self, other)
    
    def div_dbmacu_k_(self, other):
        return self.toFloat_0_k_() / other
    
    def div_e2tf9d_k_(self, other):
        return self.toDouble_0_k_() / other
    
    def rem_wi8e9i_k_(self, other):
        return self.rem_wiekkq_k_(other)
    
    def rem_dip2j2_k_(self, other):
        return self.rem_wiekkq_k_(other)
    
    def rem_ha5a7z_k_(self, other):
        return self.rem_wiekkq_k_(other)
    
    def rem_wiekkq_k_(self, other):
        return modulo(self, other)
    
    def rem_dbmacu_k_(self, other):
        return self.toFloat_0_k_() % other
    
    def rem_e2tf9d_k_(self, other):
        return self.toDouble_0_k_() % other
    
    def inc_0_k_(self):
        return (((self + 1) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000
    
    def dec_0_k_(self):
        return (((self - 1) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000
    
    def unaryPlus_0_k_(self):
        return self
    
    def unaryMinus_0_k_(self):
        return (((~self + 1) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000
    
    def rangeTo_wi8e9i_k_(self, other):
        return numberRangeToLong(self, other)
    
    def rangeTo_dip2j2_k_(self, other):
        return numberRangeToLong(self, other)
    
    def rangeTo_ha5a7z_k_(self, other):
        return numberRangeToLong(self, other)
    
    def rangeTo_wiekkq_k_(self, other):
        return LongRange(self, other)
    
    def shl_ha5a7z_k_(self, bitCount):
        return shiftLeft(self, bitCount)
    
    def shr_ha5a7z_k_(self, bitCount):
        return shiftRight(self, bitCount)
    
    def ushr_ha5a7z_k_(self, bitCount):
        return shiftRightUnsigned(self, bitCount)
    
    def and_wiekkq_k_(self, other):
        return Long(self._get_low__0_k_() & other._get_low__0_k_(), self._get_high__0_k_() & other._get_high__0_k_())
    
    def or_wiekkq_k_(self, other):
        return Long(self._get_low__0_k_() | other._get_low__0_k_(), self._get_high__0_k_() | other._get_high__0_k_())
    
    def xor_wiekkq_k_(self, other):
        return Long(self._get_low__0_k_() ^ other._get_low__0_k_(), self._get_high__0_k_() ^ other._get_high__0_k_())
    
    def inv_0_k_(self):
        return Long(~self._get_low__0_k_(), ~self._get_high__0_k_())
    
    def toByte_0_k_(self):
        return ((self._get_low__0_k_() + 0x80) & 0xff) - 0x80
    
    def toChar_0_k_(self):
        return numberToChar(self._get_low__0_k_())
    
    def toShort_0_k_(self):
        return ((self._get_low__0_k_() + 0x8000) & 0xffff) - 0x8000
    
    def toInt_0_k_(self):
        return self._get_low__0_k_()
    
    def toLong_0_k_(self):
        return self
    
    def toFloat_0_k_(self):
        return kotlin_Float(self.toDouble_0_k_())
    
    def toDouble_0_k_(self):
        return toNumber(self)
    
    def valueOf(self):
        return self.toDouble_0_k_()
    
    def equals(self, other):
        if isinstance(other, Long):
            tmp = equalsLong(self, kotlin_Long(other))
        elif True:
            tmp = False
        
        return tmp
    
    def hashCode(self):
        return hashCode_0(self)
    
    def toString(self):
        return toStringImpl(self, 10)
    

def _get_ZERO_():
    return ZERO

ZERO = None
def _get_ONE_():
    return ONE

ONE = None
def _get_NEG_ONE_():
    return NEG_ONE

NEG_ONE = None
def _get_MAX_VALUE_():
    return MAX_VALUE

MAX_VALUE = None
def _get_MIN_VALUE_():
    return MIN_VALUE

MIN_VALUE = None
def _get_TWO_PWR_24__():
    return TWO_PWR_24_

TWO_PWR_24_ = None
def compare(self, other):
    if equalsLong(self, other):
        return 0
    
    thisNeg = isNegative(self)
    otherNeg = isNegative(other)
    return (-1) if ((not otherNeg) if (thisNeg) else (False)) else ((1) if ((otherNeg) if (not thisNeg) else (False)) else ((-1) if (isNegative(subtract(self, other))) else (1)))

def add(self, other):
    a48 = (self._get_high__0_k_() & 0xffff_ffff) >> 16
    a32 = self._get_high__0_k_() & 65535
    a16 = (self._get_low__0_k_() & 0xffff_ffff) >> 16
    a00 = self._get_low__0_k_() & 65535
    b48 = (other._get_high__0_k_() & 0xffff_ffff) >> 16
    b32 = other._get_high__0_k_() & 65535
    b16 = (other._get_low__0_k_() & 0xffff_ffff) >> 16
    b00 = other._get_low__0_k_() & 65535
    c48 = 0
    c32 = 0
    c16 = 0
    c00 = 0
    c00 = (((c00 + ((((a00 + b00) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
    c16 = (((c16 + ((c00 & 0xffff_ffff) >> 16)) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
    c00 = c00 & 65535
    c16 = (((c16 + ((((a16 + b16) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
    c32 = (((c32 + ((c16 & 0xffff_ffff) >> 16)) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
    c16 = c16 & 65535
    c32 = (((c32 + ((((a32 + b32) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
    c48 = (((c48 + ((c32 & 0xffff_ffff) >> 16)) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
    c32 = c32 & 65535
    c48 = (((c48 + ((((a48 + b48) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
    c48 = c48 & 65535
    return Long(((((c16 << 16) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000) | c00, ((((c48 << 16) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000) | c32)

def subtract(self, other):
    return add(self, ((-other + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000)

def multiply(self, other):
    if isZero(self):
        return _get_ZERO_()
    elif isZero(other):
        return _get_ZERO_()
    
    if equalsLong(self, _get_MIN_VALUE_()):
        return (_get_MIN_VALUE_()) if (isOdd(other)) else (_get_ZERO_())
    elif equalsLong(other, _get_MIN_VALUE_()):
        return (_get_MIN_VALUE_()) if (isOdd(self)) else (_get_ZERO_())
    
    if isNegative(self):
        if isNegative(other):
            tmp = multiply(negate(self), negate(other))
        else:
            tmp = negate(multiply(negate(self), other))
        
        return tmp
    elif isNegative(other):
        return negate(multiply(self, negate(other)))
    
    if (lessThan(other, _get_TWO_PWR_24__())) if (lessThan(self, _get_TWO_PWR_24__())) else (False):
        return fromNumber(toNumber(self) * toNumber(other))
    
    a48 = (self._get_high__0_k_() & 0xffff_ffff) >> 16
    a32 = self._get_high__0_k_() & 65535
    a16 = (self._get_low__0_k_() & 0xffff_ffff) >> 16
    a00 = self._get_low__0_k_() & 65535
    b48 = (other._get_high__0_k_() & 0xffff_ffff) >> 16
    b32 = other._get_high__0_k_() & 65535
    b16 = (other._get_low__0_k_() & 0xffff_ffff) >> 16
    b00 = other._get_low__0_k_() & 65535
    c48 = 0
    c32 = 0
    c16 = 0
    c00 = 0
    c00 = (((c00 + imul(a00, b00)) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
    c16 = (((c16 + ((c00 & 0xffff_ffff) >> 16)) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
    c00 = c00 & 65535
    c16 = (((c16 + imul(a16, b00)) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
    c32 = (((c32 + ((c16 & 0xffff_ffff) >> 16)) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
    c16 = c16 & 65535
    c16 = (((c16 + imul(a00, b16)) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
    c32 = (((c32 + ((c16 & 0xffff_ffff) >> 16)) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
    c16 = c16 & 65535
    c32 = (((c32 + imul(a32, b00)) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
    c48 = (((c48 + ((c32 & 0xffff_ffff) >> 16)) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
    c32 = c32 & 65535
    c32 = (((c32 + imul(a16, b16)) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
    c48 = (((c48 + ((c32 & 0xffff_ffff) >> 16)) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
    c32 = c32 & 65535
    c32 = (((c32 + imul(a00, b32)) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
    c48 = (((c48 + ((c32 & 0xffff_ffff) >> 16)) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
    c32 = c32 & 65535
    c48 = (((c48 + ((((((((((((imul(a48, b00) + imul(a32, b16)) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000) + imul(a16, b32)) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000) + imul(a00, b48)) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
    c48 = c48 & 65535
    return Long(((((c16 << 16) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000) | c00, ((((c48 << 16) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000) | c32)

def divide(self, other):
    if isZero(other):
        raise Exception_init__Create__0('division by zero')
    elif isZero(self):
        return _get_ZERO_()
    
    if equalsLong(self, _get_MIN_VALUE_()):
        if (True) if (equalsLong(other, _get_ONE_())) else (equalsLong(other, _get_NEG_ONE_())):
            return _get_MIN_VALUE_()
        elif equalsLong(other, _get_MIN_VALUE_()):
            return _get_ONE_()
        else:
            halfThis = shiftRight(self, 1)
            approx = shiftLeft((((halfThis // other) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000, 1)
            if equalsLong(approx, _get_ZERO_()):
                return (_get_ONE_()) if (isNegative(other)) else (_get_NEG_ONE_())
            else:
                rem = subtract(self, multiply(other, approx))
                return add(approx, (((rem // other) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000)
            
        
    elif equalsLong(other, _get_MIN_VALUE_()):
        return _get_ZERO_()
    
    if isNegative(self):
        if isNegative(other):
            tmp = (((negate(self) // negate(other)) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000
        else:
            tmp = negate((((negate(self) // other) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000)
        
        return tmp
    elif isNegative(other):
        return negate((((self // negate(other)) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000)
    
    res = _get_ZERO_()
    rem = self
    while greaterThanOrEqual(rem, other):
        approxDouble = toNumber(rem) / toNumber(other)
        approx2 = JsMath.max(*(1.0, JsMath.floor(approxDouble)))
        log2 = JsMath.ceil(JsMath.log(approx2) / LN2)
        delta = (1.0) if (log2 <= kotlin_Double(48)) else (JsMath.pow(2.0, log2 - 48))
        approxRes = fromNumber(approx2)
        approxRem = multiply(approxRes, other)
        while (True) if (isNegative(approxRem)) else (greaterThan(approxRem, rem)):
            approx2 = approx2 - delta
            approxRes = fromNumber(approx2)
            approxRem = multiply(approxRes, other)
        
        if isZero(approxRes):
            approxRes = _get_ONE_()
        
        res = add(res, approxRes)
        rem = subtract(rem, approxRem)
    
    return res

def modulo(self, other):
    return subtract(self, multiply((((self // other) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000, other))

def shiftLeft(self, numBits):
    numBits = numBits & 63
    if numBits == 0:
        return self
    elif numBits < 32:
        return Long((((self._get_low__0_k_() << numBits) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000, ((((self._get_high__0_k_() << numBits) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000) | ((self._get_low__0_k_() & 0xffff_ffff) >> ((((32 - numBits) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)))
    else:
        return Long(0, (((self._get_low__0_k_() << ((((numBits - 32) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)
    

def shiftRight(self, numBits):
    numBits = numBits & 63
    if numBits == 0:
        return self
    elif numBits < 32:
        return Long(((self._get_low__0_k_() & 0xffff_ffff) >> numBits) | ((((self._get_high__0_k_() << ((((32 - numBits) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000), self._get_high__0_k_() >> numBits)
    else:
        return Long(self._get_high__0_k_() >> ((((numBits - 32) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000), (0) if (self._get_high__0_k_() >= 0) else (-1))
    

def shiftRightUnsigned(self, numBits):
    numBits = numBits & 63
    if numBits == 0:
        return self
    elif numBits < 32:
        return Long(((self._get_low__0_k_() & 0xffff_ffff) >> numBits) | ((((self._get_high__0_k_() << ((((32 - numBits) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000), (self._get_high__0_k_() & 0xffff_ffff) >> numBits)
    else:
        if numBits == 32:
            tmp = Long(self._get_high__0_k_(), 0)
        else:
            tmp = Long((self._get_high__0_k_() & 0xffff_ffff) >> ((((numBits - 32) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000), 0)
        
        return tmp
    

def toNumber(self):
    return (self._get_high__0_k_() * _get_TWO_PWR_32_DBL__()) + getLowBitsUnsigned(self)

def equalsLong(self, other):
    return (self._get_low__0_k_() == other._get_low__0_k_()) if (self._get_high__0_k_() == other._get_high__0_k_()) else (False)

def hashCode_0(l):
    return l._get_low__0_k_() ^ l._get_high__0_k_()

def toStringImpl(self, radix):
    if (True) if (radix < 2) else (36 < radix):
        raise Exception_init__Create__0(str('radix out of range: ') + str(radix))
    
    if isZero(self):
        return '0'
    
    if isNegative(self):
        if equalsLong(self, _get_MIN_VALUE_()):
            radixLong = fromInt(radix)
            div = (((self // radixLong) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000
            rem = ((subtract(multiply(div, radixLong), self) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
            return toStringImpl(div, radix) + unsafeCast(asDynamic(rem).toString(radix))
        else:
            return str('-') + str(toStringImpl(negate(self), radix))
        
    
    radixToPower = fromNumber(JsMath.pow(kotlin_Double(radix), 6.0))
    rem = self
    result = ''
    while True:
        remDiv = (((rem // radixToPower) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000
        intval = ((subtract(rem, multiply(remDiv, radixToPower)) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
        digits = unsafeCast(asDynamic(intval).toString(radix))
        rem = remDiv
        if isZero(rem):
            return digits + result
        else:
            while len(digits) < 6:
                digits = '0' + digits
            
            result = digits + result
        
    

def fromInt(value):
    return Long(value, (-1) if (value < 0) else (0))

def isNegative(self):
    return self._get_high__0_k_() < 0

def isZero(self):
    return (self._get_low__0_k_() == 0) if (self._get_high__0_k_() == 0) else (False)

def isOdd(self):
    return self._get_low__0_k_() & 1 == 1

def negate(self):
    return ((-self + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000

def lessThan(self, other):
    return compare(self, other) < 0

def fromNumber(value):
    if isNaN_0(value):
        return _get_ZERO_()
    elif value <= -_get_TWO_PWR_63_DBL__():
        return _get_MIN_VALUE_()
    elif value + 1 >= _get_TWO_PWR_63_DBL__():
        return _get_MAX_VALUE_()
    elif value < kotlin_Double(0):
        return negate(fromNumber(-value))
    else:
        twoPwr32 = _get_TWO_PWR_32_DBL__()
        return Long(jsBitwiseOr(value % twoPwr32, 0), jsBitwiseOr(value / twoPwr32, 0))
    

def greaterThan(self, other):
    return compare(self, other) > 0

def greaterThanOrEqual(self, other):
    return compare(self, other) >= 0

def getLowBitsUnsigned(self):
    return (kotlin_Double(self._get_low__0_k_())) if (self._get_low__0_k_() >= 0) else (_get_TWO_PWR_32_DBL__() + self._get_low__0_k_())

def _get_TWO_PWR_32_DBL__():
    return TWO_PWR_32_DBL_

TWO_PWR_32_DBL_ = None
def _get_TWO_PWR_63_DBL__():
    return TWO_PWR_63_DBL_

TWO_PWR_63_DBL_ = None
def imul(a_local, b_local):
    lhs = kotlin_Double(jsBitwiseAnd(a_local, js('0xffff0000'))) * kotlin_Double(jsBitwiseAnd(b_local, 65535))
    rhs = kotlin_Double(jsBitwiseAnd(a_local, 65535)) * kotlin_Double(b_local)
    return jsBitwiseOr(lhs + rhs, 0)

def withType(type, array):
    Unexpected_operator_EQ(array._type_, type)
    return array

def arrayConcat(*args):
    len = len(args)
    typed = unsafeCast(js('Array(len)'))
    tmp0_iterator = numberRangeToNumber(0, (((len - 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000).iterator_0_k_()
    while tmp0_iterator.hasNext_0_k_():
        i = tmp0_iterator.next_0_k_()
        arr = args[i]
        if not ((isArray(arr)) if (not (arr == None)) else (False)):
            typed.__setitem__(i, T(js('[]').slice.call(arr)))
        elif True:
            typed.__setitem__(i, arr)
        
    
    return T(js('[]').concat.apply(js('[]'), typed))

def primitiveArrayConcat(*args):
    size_local = 0
    tmp0_iterator = numberRangeToNumber(0, (((len(args) - 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000).iterator_0_k_()
    while tmp0_iterator.hasNext_0_k_():
        i = tmp0_iterator.next_0_k_()
        size_local = (((size_local + len(unsafeCast_0(args[i]))) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
    
    a = args[0]
    result = unsafeCast(js('new a.constructor(size_local)'))
    if asDynamic(a)._type_ != None:
        withType(kotlin_String(asDynamic(a)._type_), result)
    
    size_local = 0
    tmp1_iterator = numberRangeToNumber(0, (((len(args) - 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000).iterator_0_k_()
    while tmp1_iterator.hasNext_0_k_():
        i = tmp1_iterator.next_0_k_()
        arr = unsafeCast_0(args[i])
        tmp2_iterator = numberRangeToNumber(0, (((len(arr) - 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000).iterator_0_k_()
        while tmp2_iterator.hasNext_0_k_():
            j = tmp2_iterator.next_0_k_()
            tmp3 = size_local
            size_local = (((tmp3 + 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
            result.__setitem__(tmp3, arr[j])
        
    
    return unsafeCast_0(result)

def taggedArrayCopy(array):
    res = array.slice()
    Unexpected_operator_EQ(res._type_, array._type_)
    return unsafeCast(res)

def numberToByte(a):
    return toByte(((a + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)

def toByte(a):
    return unsafeCast(js('a << 24 >> 24'))

def numberToInt(a):
    if isinstance(a, Long):
        tmp = ((kotlin_Long(a) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
    elif True:
        tmp = doubleToInt(kotlin_Double(a))
    
    return tmp

def doubleToInt(a):
    return (2147483647) if (a > kotlin_Double(2147483647)) else ((-2147483648) if (a < kotlin_Double(-2147483648)) else (jsBitwiseOr(a, 0)))

def numberToDouble(a):
    return unsafeCast(js('+a'))

def numberToShort(a):
    return toShort(((a + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)

def toShort(a):
    return unsafeCast(js('a << 16 >> 16'))

def numberToLong(a):
    if isinstance(a, Long):
        tmp = kotlin_Long(a)
    elif True:
        tmp = fromNumber(kotlin_Double(a))
    
    return tmp

def numberToChar(a):
    return Char_0(toUShort(((a + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000))

def toLong(a):
    return fromInt(kotlin_Int(a))

def numberRangeToNumber(start, endInclusive):
    return IntRange(kotlin_Int(start), kotlin_Int(endInclusive))

def numberRangeToLong(start, endInclusive):
    return LongRange(((start + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000, kotlin_Long(endInclusive))

def _get_propertyRefClassMetadataCache_():
    return propertyRefClassMetadataCache

propertyRefClassMetadataCache = None
def metadataObject():
    return js('{ kind: \'class\', interfaces: [] }')

def getPropertyCallableRef(name, paramCount, type, getter, setter):
    Unexpected_operator_EQ(getter.get, getter)
    Unexpected_operator_EQ(getter.set, setter)
    Unexpected_operator_EQ(getter.callableName, name)
    return unsafeCast(getPropertyRefClass(getter, getKPropMetadata(paramCount, setter, type)))

def getPropertyRefClass(obj, metadata):
    Unexpected_operator_EQ(obj._metadata_, metadata)
    Unexpected_operator_EQ(obj.constructor, obj)
    return obj

def getKPropMetadata(paramCount, setter, type):
    mdata = _get_propertyRefClassMetadataCache_()[paramCount][(0) if (setter == None) else (1)]
    if mdata.interfaces.length == 0:
        mdata.interfaces.push(type)
    
    return mdata

def getLocalDelegateReference(name, type, mutable, _lambda):
    return getPropertyCallableRef(name, 0, type, _lambda, (_lambda) if (mutable) else (None))

def isArrayish(o):
    return (True) if (isJsArray(kotlin_Any(o))) else (unsafeCast(js('ArrayBuffer').isView(o)))

def isJsArray(obj):
    return unsafeCast(js('Array').isArray(obj))

def isInterface(obj, iface):
    tmp0_elvis_lhs = obj.constructor
    if tmp0_elvis_lhs == None:
        return False
    else:
        tmp = tmp0_elvis_lhs
    
    ctor = tmp
    return isInterfaceImpl(kotlin_js_Ctor(ctor), iface)

def isInterfaceImpl(ctor, iface):
    if ctor is iface:
        return True
    
    metadata = _metadata_
    if not (metadata == None):
        interfaces = interfaces
        tmp0_iterator = arrayIterator(interfaces)
        while tmp0_iterator.hasNext_0_k_():
            i = tmp0_iterator.next_0_k_()
            if isInterfaceImpl(i, iface):
                return True
            
        
    
    superPrototype = (js('Object').getPrototypeOf(prototype)) if (not (prototype == None)) else (None)
    superConstructor = (kotlin_js_Ctor_(superPrototype.constructor)) if (superPrototype != None) else (None)
    return (isInterfaceImpl(superConstructor, iface)) if (not (superConstructor == None)) else (False)

def isArray(obj):
    return (kotlin_Boolean(not asDynamic(obj)._type_)) if (isJsArray(obj)) else (False)

def isObject(obj):
    objTypeOf = jsTypeOf(obj)
    tmp0_subject = objTypeOf
    return (True) if (tmp0_subject == 'string') else ((True) if (tmp0_subject == 'number') else ((True) if (tmp0_subject == 'boolean') else ((True) if (tmp0_subject == 'function') else (jsInstanceOf(obj, js('Object'))))))

def isSuspendFunction(obj, arity):
    if jsTypeOf(obj) == 'function':
        return unsafeCast(obj._arity) is arity
    
    if (jsIn((str(Char_0(36)) + str('metadata')) + str(Char_0(36)), kotlin_Any(obj.constructor))) if (jsTypeOf(obj) == 'object') else (False):
        tmp0_safe_receiver = _metadata_
        tmp1_safe_receiver = (None) if (tmp0_safe_receiver == None) else (suspendArity)
        def complexFunction_x6__Assign__Expr__Assign__While__Expr__Return__0(it):
            result = False
            Unit_getInstance()
            tmp0_iterator = arrayIterator(it)
            while tmp0_iterator.hasNext_0_k_():
                item = tmp0_iterator.next_0_k_()
                if arity == item:
                    result = True
                    break
                
            
            Unit_getInstance()
            return result
        
        tmp2_elvis_lhs = (None) if (tmp1_safe_receiver == None) else (let_0(tmp1_safe_receiver, complexFunction_x6__Assign__Expr__Assign__While__Expr__Return__0))
        return (False) if (tmp2_elvis_lhs == None) else (tmp2_elvis_lhs)
    
    return False

def isNumber(a):
    if jsTypeOf(a) == 'number':
        tmp = True
    else:
        tmp = isinstance(a, Long)
    
    return tmp

def isComparable(value):
    type = jsTypeOf(value)
    return (True) if ((True) if ((True) if (type == 'string') else (type == 'boolean')) else (isNumber(value))) else (isInterface(value, _get_js_(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrClassReferenceImpl)))

def isCharSequence(value):
    return (True) if (jsTypeOf(value) == 'string') else (isInterface(value, _get_js_(visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrClassReferenceImpl)))

def isBooleanArray(a):
    return (a._type_ is 'BooleanArray') if (isJsArray(kotlin_Any(a))) else (False)

def isByteArray(a):
    return jsInstanceOf(a, js('Int8Array'))

def isShortArray(a):
    return jsInstanceOf(a, js('Int16Array'))

def isCharArray(a):
    return (a._type_ is 'CharArray') if (isJsArray(kotlin_Any(a))) else (False)

def isIntArray(a):
    return jsInstanceOf(a, js('Int32Array'))

def isFloatArray(a):
    return jsInstanceOf(a, js('Float32Array'))

def isLongArray(a):
    return (a._type_ is 'LongArray') if (isJsArray(kotlin_Any(a))) else (False)

def isDoubleArray(a):
    return jsInstanceOf(a, js('Float64Array'))

def jsIsType(obj, jsClass):
    if jsClass is js('Object'):
        return isObject(obj)
    
    if (True) if ((True) if (obj == None) else (jsClass == None)) else ((not (jsTypeOf(obj) == 'function')) if (not (jsTypeOf(obj) == 'object')) else (False)):
        return False
    
    if (jsInstanceOf(obj, jsClass)) if (jsTypeOf(jsClass) == 'function') else (False):
        return True
    
    proto = jsGetPrototypeOf(jsClass)
    tmp0_safe_receiver = proto
    constructor = (None) if (tmp0_safe_receiver == None) else (tmp0_safe_receiver.constructor)
    if (jsIn((str(Char_0(36)) + str('metadata')) + str(Char_0(36)), kotlin_Any(constructor))) if (constructor != None) else (False):
        metadata = constructor._metadata_
        if metadata.kind is 'object':
            return obj is jsClass
        
    
    klassMetadata = jsClass._metadata_
    if klassMetadata == None:
        return jsInstanceOf(obj, jsClass)
    
    if (obj.constructor != None) if (klassMetadata.kind is 'interface') else (False):
        return isInterfaceImpl(kotlin_js_Ctor(obj.constructor), jsClass)
    
    return False

def jsGetPrototypeOf(jsClass):
    return js('Object').getPrototypeOf(jsClass)

def asList(self):
    return ArrayList(unsafeCast_0(self))

def plus_0(self, elements):
    return kotlin_Array_T_(asDynamic(self).concat(elements))

def copyOfRange(self, fromIndex, toIndex):
    Companion_getInstance().checkRangeIndexes_zd700_k_(fromIndex, toIndex, len(self))
    return kotlin_Array_T_(asDynamic(self).slice(fromIndex, toIndex))

def copyInto(self, destination, destinationOffset, startIndex, endIndex):
    arrayCopy_0(self, destination, destinationOffset, startIndex, endIndex)
    return destination

def minOf(a, b):
    return JsMath.min(*(a, b))

class CoroutineImpl_0(Continuation):
    def __init__(self, resultContinuation):
        self.resultContinuation = resultContinuation
        self.state = 0
        self.exceptionState = 0
        self.result = None
        self.exception = None
        self.finallyPath = None
        tmp = self
        tmp0_safe_receiver = self._get_resultContinuation__0_k_()
        tmp._context = (None) if (tmp0_safe_receiver == None) else (tmp0_safe_receiver._get_context__0_k_())
        self.intercepted_ = None
    
    def _get_resultContinuation__0_k_(self):
        return self.resultContinuation
    
    def _set_state__majfzk_k_(self, _set___):
        self.state = _set___
    
    def _get_state__0_k_(self):
        return self.state
    
    def _set_exceptionState__majfzk_k_(self, _set___):
        self.exceptionState = _set___
    
    def _get_exceptionState__0_k_(self):
        return self.exceptionState
    
    def _set_result__h9nkbz_k_(self, _set___):
        self.result = _set___
    
    def _get_result__0_k_(self):
        return self.result
    
    def _set_exception__h9nkbz_k_(self, _set___):
        self.exception = _set___
    
    def _get_exception__0_k_(self):
        return self.exception
    
    def _set_finallyPath__52zbur_k_(self, _set___):
        self.finallyPath = _set___
    
    def _get_finallyPath__0_k_(self):
        return self.finallyPath
    
    def _get__context__0_k_(self):
        return self._context
    
    def _get_context__0_k_(self):
        return ensureNotNull(self._get__context__0_k_())
    
    def _set_intercepted___qgh4ze_k_(self, _set___):
        self.intercepted_ = _set___
    
    def _get_intercepted___0_k_(self):
        return self.intercepted_
    
    def intercepted_0_k_(self):
        tmp2_elvis_lhs = self._get_intercepted___0_k_()
        if tmp2_elvis_lhs == None:
            tmp0_safe_receiver = self._get_context__0_k_().get_9uvjra_k_(Key_getInstance())
            tmp1_elvis_lhs = (None) if (tmp0_safe_receiver == None) else (tmp0_safe_receiver.interceptContinuation_x4ijla_k_(self))
            def complexFunction_x1__Expr__0(it):
                self._set_intercepted___qgh4ze_k_(it)
            
            tmp = also((self) if (tmp1_elvis_lhs == None) else (tmp1_elvis_lhs), complexFunction_x1__Expr__0)
        else:
            tmp = tmp2_elvis_lhs
        
        return tmp
    
    def resumeWith_jccoe6_k_(self, result):
        current = self
        currentResult = Result__getOrNull_impl(result)
        currentException = Result__exceptionOrNull_impl(result)
        while True:
            def complexFunction_x6__If__Expr__Expr__Assign__Expr__If__0(_this_with):
                if currentException == None:
                    tmp = _this_with._set_result__h9nkbz_k_(currentResult)
                else:
                    _this_with._set_state__majfzk_k_(_this_with._get_exceptionState__0_k_())
                    tmp = _this_with._set_exception__h9nkbz_k_(currentException)
                
                visitTry_org_jetbrains_kotlin_ir_expressions_impl_IrTryImpl
                _this_with.releaseIntercepted_sv8swh_k_()
                completion = ensureNotNull(_this_with._get_resultContinuation__0_k_())
                Unit_getInstance()
                if isinstance(completion, CoroutineImpl_0):
                    current = kotlin_coroutines_CoroutineImpl(completion)
                    tmp = Unit_getInstance()
                elif True:
                    if not (currentException == None):
                        resumeWithException(completion, ensureNotNull(currentException))
                    else:
                        resume(completion, currentResult)
                    
                    return Unit_getInstance()
                
            
            with_0(current, complexFunction_x6__If__Expr__Expr__Assign__Expr__If__0)
        
    
    def releaseIntercepted_sv8swh_k_(self):
        intercepted = self._get_intercepted___0_k_()
        if (not (intercepted is self)) if (not (intercepted == None)) else (False):
            ensureNotNull(self._get_context__0_k_().get_9uvjra_k_(Key_getInstance())).releaseInterceptedContinuation_h7c6yl_k_(intercepted)
        
        self._set_intercepted___qgh4ze_k_(CompletedContinuation_getInstance())
    
    def doResume_0_k_(self):
        pass
    
    def create_s8oglw_k_(self, completion):
        raise UnsupportedOperationException_init__Create__0('create(Continuation) has not been overridden')
    
    def create_wbutx_k_(self, value, completion):
        raise UnsupportedOperationException_init__Create__0('create(Any?;Continuation) has not been overridden')
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class CompletedContinuation(Continuation):
    def __init__(self):
        global CompletedContinuation_instance
        CompletedContinuation_instance = self
    
    def _get_context__0_k_(self):
        return error('This continuation is already complete')
    
    def resumeWith_jccoe6_k_(self, result):
        error('This continuation is already complete')
    
    def toString(self):
        return 'This continuation is already complete'
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    

CompletedContinuation_instance = None
def CompletedContinuation_getInstance():
    if CompletedContinuation_instance == None:
        CompletedContinuation()
    
    return CompletedContinuation_instance

def Exception_init__Init_(_this):
    Error.__init__(_this)
    return _this

def Exception_init__Create_():
    tmp = Exception_init__Init_(Exception.__new__(Exception))
    captureStack(tmp, Exception_init__Create_)
    return tmp

def Exception_init__Init__0(message, _this):
    Error.__init__(_this, message)
    return _this

def Exception_init__Create__0(message):
    tmp = Exception_init__Init__0(message, Exception.__new__(Exception))
    captureStack(tmp, Exception_init__Create_)
    return tmp

def Exception_init__Init__1(message, cause, _this):
    Error.__init__(_this, message, cause)
    return _this

def Exception_init__Create__1(message, cause):
    tmp = Exception_init__Init__1(message, cause, Exception.__new__(Exception))
    captureStack(tmp, Exception_init__Create_)
    return tmp

def Exception_init__Init__2(cause, _this):
    Error.__init__(_this, cause)
    return _this

def Exception_init__Create__2(cause):
    tmp = Exception_init__Init__2(cause, Exception.__new__(Exception))
    captureStack(tmp, Exception_init__Create_)
    return tmp

class Error:
    pass

class Exception(Error):
    def _get_message__0_k_(self):
        pass
    
    def _get_cause__0_k_(self):
        pass
    
    def toString(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    

def Error_init__Init_(_this):
    Error.__init__(_this)
    return _this

def Error_init__Create_():
    tmp = Error_init__Init_(Error_0.__new__(Error_0))
    captureStack(tmp, Error_init__Create_)
    return tmp

def Error_init__Init__0(message, _this):
    Error.__init__(_this, message)
    return _this

def Error_init__Create__0(message):
    tmp = Error_init__Init__0(message, Error_0.__new__(Error_0))
    captureStack(tmp, Error_init__Create_)
    return tmp

def Error_init__Init__1(message, cause, _this):
    Error.__init__(_this, message, cause)
    return _this

def Error_init__Create__1(message, cause):
    tmp = Error_init__Init__1(message, cause, Error_0.__new__(Error_0))
    captureStack(tmp, Error_init__Create_)
    return tmp

def Error_init__Init__2(cause, _this):
    Error.__init__(_this, cause)
    return _this

def Error_init__Create__2(cause):
    tmp = Error_init__Init__2(cause, Error_0.__new__(Error_0))
    captureStack(tmp, Error_init__Create_)
    return tmp

class Error_0(Error):
    def _get_message__0_k_(self):
        pass
    
    def _get_cause__0_k_(self):
        pass
    
    def toString(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    

def IllegalArgumentException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    return _this

def IllegalArgumentException_init__Create_():
    tmp = IllegalArgumentException_init__Init_(IllegalArgumentException.__new__(IllegalArgumentException))
    captureStack(tmp, IllegalArgumentException_init__Create_)
    return tmp

def IllegalArgumentException_init__Init__0(message, _this):
    RuntimeException_init__Init__0(message, _this)
    return _this

def IllegalArgumentException_init__Create__0(message):
    tmp = IllegalArgumentException_init__Init__0(message, IllegalArgumentException.__new__(IllegalArgumentException))
    captureStack(tmp, IllegalArgumentException_init__Create_)
    return tmp

def IllegalArgumentException_init__Init__1(message, cause, _this):
    RuntimeException_init__Init__1(message, cause, _this)
    return _this

def IllegalArgumentException_init__Create__1(message, cause):
    tmp = IllegalArgumentException_init__Init__1(message, cause, IllegalArgumentException.__new__(IllegalArgumentException))
    captureStack(tmp, IllegalArgumentException_init__Create_)
    return tmp

def IllegalArgumentException_init__Init__2(cause, _this):
    RuntimeException_init__Init__2(cause, _this)
    return _this

def IllegalArgumentException_init__Create__2(cause):
    tmp = IllegalArgumentException_init__Init__2(cause, IllegalArgumentException.__new__(IllegalArgumentException))
    captureStack(tmp, IllegalArgumentException_init__Create_)
    return tmp

class IllegalArgumentException(RuntimeException):
    def _get_message__0_k_(self):
        pass
    
    def _get_cause__0_k_(self):
        pass
    
    def toString(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    

def NoSuchElementException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    return _this

def NoSuchElementException_init__Create_():
    tmp = NoSuchElementException_init__Init_(NoSuchElementException.__new__(NoSuchElementException))
    captureStack(tmp, NoSuchElementException_init__Create_)
    return tmp

def NoSuchElementException_init__Init__0(message, _this):
    RuntimeException_init__Init__0(message, _this)
    return _this

def NoSuchElementException_init__Create__0(message):
    tmp = NoSuchElementException_init__Init__0(message, NoSuchElementException.__new__(NoSuchElementException))
    captureStack(tmp, NoSuchElementException_init__Create_)
    return tmp

class NoSuchElementException(RuntimeException):
    def _get_message__0_k_(self):
        pass
    
    def _get_cause__0_k_(self):
        pass
    
    def toString(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    

def RuntimeException_init__Init_(_this):
    Exception_init__Init_(_this)
    return _this

def RuntimeException_init__Create_():
    tmp = RuntimeException_init__Init_(RuntimeException.__new__(RuntimeException))
    captureStack(tmp, RuntimeException_init__Create_)
    return tmp

def RuntimeException_init__Init__0(message, _this):
    Exception_init__Init__0(message, _this)
    return _this

def RuntimeException_init__Create__0(message):
    tmp = RuntimeException_init__Init__0(message, RuntimeException.__new__(RuntimeException))
    captureStack(tmp, RuntimeException_init__Create_)
    return tmp

def RuntimeException_init__Init__1(message, cause, _this):
    Exception_init__Init__1(message, cause, _this)
    return _this

def RuntimeException_init__Create__1(message, cause):
    tmp = RuntimeException_init__Init__1(message, cause, RuntimeException.__new__(RuntimeException))
    captureStack(tmp, RuntimeException_init__Create_)
    return tmp

def RuntimeException_init__Init__2(cause, _this):
    Exception_init__Init__2(cause, _this)
    return _this

def RuntimeException_init__Create__2(cause):
    tmp = RuntimeException_init__Init__2(cause, RuntimeException.__new__(RuntimeException))
    captureStack(tmp, RuntimeException_init__Create_)
    return tmp

class RuntimeException(Exception):
    def _get_message__0_k_(self):
        pass
    
    def _get_cause__0_k_(self):
        pass
    
    def toString(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    

def IllegalStateException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    return _this

def IllegalStateException_init__Create_():
    tmp = IllegalStateException_init__Init_(IllegalStateException.__new__(IllegalStateException))
    captureStack(tmp, IllegalStateException_init__Create_)
    return tmp

def IllegalStateException_init__Init__0(message, _this):
    RuntimeException_init__Init__0(message, _this)
    return _this

def IllegalStateException_init__Create__0(message):
    tmp = IllegalStateException_init__Init__0(message, IllegalStateException.__new__(IllegalStateException))
    captureStack(tmp, IllegalStateException_init__Create_)
    return tmp

def IllegalStateException_init__Init__1(message, cause, _this):
    RuntimeException_init__Init__1(message, cause, _this)
    return _this

def IllegalStateException_init__Create__1(message, cause):
    tmp = IllegalStateException_init__Init__1(message, cause, IllegalStateException.__new__(IllegalStateException))
    captureStack(tmp, IllegalStateException_init__Create_)
    return tmp

def IllegalStateException_init__Init__2(cause, _this):
    RuntimeException_init__Init__2(cause, _this)
    return _this

def IllegalStateException_init__Create__2(cause):
    tmp = IllegalStateException_init__Init__2(cause, IllegalStateException.__new__(IllegalStateException))
    captureStack(tmp, IllegalStateException_init__Create_)
    return tmp

class IllegalStateException(RuntimeException):
    def _get_message__0_k_(self):
        pass
    
    def _get_cause__0_k_(self):
        pass
    
    def toString(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    

def IndexOutOfBoundsException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    return _this

def IndexOutOfBoundsException_init__Create_():
    tmp = IndexOutOfBoundsException_init__Init_(IndexOutOfBoundsException.__new__(IndexOutOfBoundsException))
    captureStack(tmp, IndexOutOfBoundsException_init__Create_)
    return tmp

def IndexOutOfBoundsException_init__Init__0(message, _this):
    RuntimeException_init__Init__0(message, _this)
    return _this

def IndexOutOfBoundsException_init__Create__0(message):
    tmp = IndexOutOfBoundsException_init__Init__0(message, IndexOutOfBoundsException.__new__(IndexOutOfBoundsException))
    captureStack(tmp, IndexOutOfBoundsException_init__Create_)
    return tmp

class IndexOutOfBoundsException(RuntimeException):
    def _get_message__0_k_(self):
        pass
    
    def _get_cause__0_k_(self):
        pass
    
    def toString(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    

def UnsupportedOperationException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    return _this

def UnsupportedOperationException_init__Create_():
    tmp = UnsupportedOperationException_init__Init_(UnsupportedOperationException.__new__(UnsupportedOperationException))
    captureStack(tmp, UnsupportedOperationException_init__Create_)
    return tmp

def UnsupportedOperationException_init__Init__0(message, _this):
    RuntimeException_init__Init__0(message, _this)
    return _this

def UnsupportedOperationException_init__Create__0(message):
    tmp = UnsupportedOperationException_init__Init__0(message, UnsupportedOperationException.__new__(UnsupportedOperationException))
    captureStack(tmp, UnsupportedOperationException_init__Create_)
    return tmp

def UnsupportedOperationException_init__Init__1(message, cause, _this):
    RuntimeException_init__Init__1(message, cause, _this)
    return _this

def UnsupportedOperationException_init__Create__1(message, cause):
    tmp = UnsupportedOperationException_init__Init__1(message, cause, UnsupportedOperationException.__new__(UnsupportedOperationException))
    captureStack(tmp, UnsupportedOperationException_init__Create_)
    return tmp

def UnsupportedOperationException_init__Init__2(cause, _this):
    RuntimeException_init__Init__2(cause, _this)
    return _this

def UnsupportedOperationException_init__Create__2(cause):
    tmp = UnsupportedOperationException_init__Init__2(cause, UnsupportedOperationException.__new__(UnsupportedOperationException))
    captureStack(tmp, UnsupportedOperationException_init__Create_)
    return tmp

class UnsupportedOperationException(RuntimeException):
    def _get_message__0_k_(self):
        pass
    
    def _get_cause__0_k_(self):
        pass
    
    def toString(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    

def NullPointerException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    return _this

def NullPointerException_init__Create_():
    tmp = NullPointerException_init__Init_(NullPointerException.__new__(NullPointerException))
    captureStack(tmp, NullPointerException_init__Create_)
    return tmp

def NullPointerException_init__Init__0(message, _this):
    RuntimeException_init__Init__0(message, _this)
    return _this

def NullPointerException_init__Create__0(message):
    tmp = NullPointerException_init__Init__0(message, NullPointerException.__new__(NullPointerException))
    captureStack(tmp, NullPointerException_init__Create_)
    return tmp

class NullPointerException(RuntimeException):
    def _get_message__0_k_(self):
        pass
    
    def _get_cause__0_k_(self):
        pass
    
    def toString(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    

def NoWhenBranchMatchedException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    return _this

def NoWhenBranchMatchedException_init__Create_():
    tmp = NoWhenBranchMatchedException_init__Init_(NoWhenBranchMatchedException.__new__(NoWhenBranchMatchedException))
    captureStack(tmp, NoWhenBranchMatchedException_init__Create_)
    return tmp

def NoWhenBranchMatchedException_init__Init__0(message, _this):
    RuntimeException_init__Init__0(message, _this)
    return _this

def NoWhenBranchMatchedException_init__Create__0(message):
    tmp = NoWhenBranchMatchedException_init__Init__0(message, NoWhenBranchMatchedException.__new__(NoWhenBranchMatchedException))
    captureStack(tmp, NoWhenBranchMatchedException_init__Create_)
    return tmp

def NoWhenBranchMatchedException_init__Init__1(message, cause, _this):
    RuntimeException_init__Init__1(message, cause, _this)
    return _this

def NoWhenBranchMatchedException_init__Create__1(message, cause):
    tmp = NoWhenBranchMatchedException_init__Init__1(message, cause, NoWhenBranchMatchedException.__new__(NoWhenBranchMatchedException))
    captureStack(tmp, NoWhenBranchMatchedException_init__Create_)
    return tmp

def NoWhenBranchMatchedException_init__Init__2(cause, _this):
    RuntimeException_init__Init__2(cause, _this)
    return _this

def NoWhenBranchMatchedException_init__Create__2(cause):
    tmp = NoWhenBranchMatchedException_init__Init__2(cause, NoWhenBranchMatchedException.__new__(NoWhenBranchMatchedException))
    captureStack(tmp, NoWhenBranchMatchedException_init__Create_)
    return tmp

class NoWhenBranchMatchedException(RuntimeException):
    def _get_message__0_k_(self):
        pass
    
    def _get_cause__0_k_(self):
        pass
    
    def toString(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    

def ClassCastException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    return _this

def ClassCastException_init__Create_():
    tmp = ClassCastException_init__Init_(ClassCastException.__new__(ClassCastException))
    captureStack(tmp, ClassCastException_init__Create_)
    return tmp

def ClassCastException_init__Init__0(message, _this):
    RuntimeException_init__Init__0(message, _this)
    return _this

def ClassCastException_init__Create__0(message):
    tmp = ClassCastException_init__Init__0(message, ClassCastException.__new__(ClassCastException))
    captureStack(tmp, ClassCastException_init__Create_)
    return tmp

class ClassCastException(RuntimeException):
    def _get_message__0_k_(self):
        pass
    
    def _get_cause__0_k_(self):
        pass
    
    def toString(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    

def UninitializedPropertyAccessException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    return _this

def UninitializedPropertyAccessException_init__Create_():
    tmp = UninitializedPropertyAccessException_init__Init_(UninitializedPropertyAccessException.__new__(UninitializedPropertyAccessException))
    captureStack(tmp, UninitializedPropertyAccessException_init__Create_)
    return tmp

def UninitializedPropertyAccessException_init__Init__0(message, _this):
    RuntimeException_init__Init__0(message, _this)
    return _this

def UninitializedPropertyAccessException_init__Create__0(message):
    tmp = UninitializedPropertyAccessException_init__Init__0(message, UninitializedPropertyAccessException.__new__(UninitializedPropertyAccessException))
    captureStack(tmp, UninitializedPropertyAccessException_init__Create_)
    return tmp

def UninitializedPropertyAccessException_init__Init__1(message, cause, _this):
    RuntimeException_init__Init__1(message, cause, _this)
    return _this

def UninitializedPropertyAccessException_init__Create__1(message, cause):
    tmp = UninitializedPropertyAccessException_init__Init__1(message, cause, UninitializedPropertyAccessException.__new__(UninitializedPropertyAccessException))
    captureStack(tmp, UninitializedPropertyAccessException_init__Create_)
    return tmp

def UninitializedPropertyAccessException_init__Init__2(cause, _this):
    RuntimeException_init__Init__2(cause, _this)
    return _this

def UninitializedPropertyAccessException_init__Create__2(cause):
    tmp = UninitializedPropertyAccessException_init__Init__2(cause, UninitializedPropertyAccessException.__new__(UninitializedPropertyAccessException))
    captureStack(tmp, UninitializedPropertyAccessException_init__Create_)
    return tmp

class UninitializedPropertyAccessException(RuntimeException):
    def _get_message__0_k_(self):
        pass
    
    def _get_cause__0_k_(self):
        pass
    
    def toString(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    

def jsIn(lhs_hack, rhs_hack):
    return unsafeCast(js('lhs_hack in rhs_hack'))

def jsBitwiseOr(lhs_hack, rhs_hack):
    return unsafeCast(js('lhs_hack | rhs_hack'))

def jsTypeOf(value_hack):
    return unsafeCast(js('typeof value_hack'))

def jsInstanceOf(obj_hack, jsClass_hack):
    return unsafeCast(js('obj_hack instanceof jsClass_hack'))

def jsBitwiseAnd(lhs_hack, rhs_hack):
    return unsafeCast(js('lhs_hack & rhs_hack'))

def toString_1(self, radix):
    return toStringImpl(self, checkRadix(radix))

def pythonTest():
    println('Hello world')

def exampleFromAstTest():
    fruits = listOf(*('apple', 'banana', 'cherry'))
    tmp0_iterator = fruits.iterator_0_k_()
    while tmp0_iterator.hasNext_0_k_():
        x = tmp0_iterator.next_0_k_()
        println(x)
    

def isPowerOfTwo(n):
    return n & ((((n - 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000) == 0

def factorial(n):
    tmp0_subject = n <= 1
    return (1) if (tmp0_subject == True) else ((n * factorial((((n - 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)) if (tmp0_subject == False) else (noWhenBranchMatchedException()))

def numberOfCombinations(n, k):
    return (((factorial(n) // ((((factorial(k) * factorial((((n - k) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000)) + 0x8000_0000_0000_0000) & 0xffff_ffff_ffff_ffff) - 0x8000_0000_0000_0000

def sumOverflowDemo(a, b):
    return (((a + b) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000

def execute20(f):
    return f(20)

def execute20Doubled():
    return execute20(lambda it: (((it + it) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000)

def lambdaAndCapturing():
    capt = 0
    def complexFunction_x2__Assign__Return__0():
        capt = (((capt + 1) + 0x8000_0000) & 0xffff_ffff) - 0x8000_0000
        return capt
    
    l = complexFunction_x2__Assign__Return__0
    return l()

def a(a1, *a2):
    pass

def b():
    a(1, *(2, 3))

def newCode():
    def complexFunction_x1__Expr__0(x):
        println(x)
    
    forEach(map(listOf(*('apple', 'banana', 'cherry')), lambda it: toUpperCase(it)), complexFunction_x1__Expr__0)

class TestClass(Any):
    def __init__(self, classParameter):
        self.classParameter = classParameter
    
    def _get_classParameter__0_k_(self):
        return self.classParameter
    
    def getSomeString_0_k_(self):
        return 'Hello from Kotlin class!'
    
    def functionReturningClassParameter_0_k_(self):
        return self._get_classParameter__0_k_()
    
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
    return testClass.getSomeString_0_k_()

def returnParameterFromClass():
    return TestClass('paramVal').functionReturningClassParameter_0_k_()
