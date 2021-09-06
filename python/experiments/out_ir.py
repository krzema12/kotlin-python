def fold(initial, operation):
    accumulator = initial
    indexedObject = self
    inductionVariable = 0
    last = len(indexedObject)
    while inductionVariable < last:
        element = indexedObject[inductionVariable]
        inductionVariable = (inductionVariable + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
        accumulator = operation(accumulator, element)
    
    return accumulator

def _get_indices_():
    return IntRange(0, _get_lastIndex_())

def indexOf(element):
    if element == None:
        inductionVariable = 0
        last = (len(self) - 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
        if inductionVariable <= last:
            while True:
                index = inductionVariable
                inductionVariable = (inductionVariable + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
                if self[index] == None:
                    return index
                
                if inductionVariable <= last:
                    break
                
            
        
    else:
        inductionVariable = 0
        last = (len(self) - 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
        if inductionVariable <= last:
            while True:
                index = inductionVariable
                inductionVariable = (inductionVariable + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
                if element == self[index]:
                    return index
                
                if inductionVariable <= last:
                    break
                
            
        
    
    return -1

def lastIndexOf(element):
    if element == None:
        inductionVariable = (len(self) - 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
        if 0 <= inductionVariable:
            while True:
                index = inductionVariable
                inductionVariable = (inductionVariable + -1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
                if self[index] == None:
                    return index
                
                if 0 <= inductionVariable:
                    break
                
            
        
    else:
        inductionVariable = (len(self) - 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
        if 0 <= inductionVariable:
            while True:
                index = inductionVariable
                inductionVariable = (inductionVariable + -1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
                if element == self[index]:
                    return index
                
                if 0 <= inductionVariable:
                    break
                
            
        
    
    return -1

def _get_lastIndex_():
    return (len(self) - 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)

def joinToString(separator, prefix, postfix, limit, truncated, transform):
    return joinTo(StringBuilder_init__Create__1(), separator, prefix, postfix, limit, truncated, transform).toString()

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
    buffer.append_v1o70a_k_(prefix)
    Unit_getInstance()
    count = 0
    indexedObject = self
    inductionVariable = 0
    last = len(indexedObject)
    while inductionVariable < last:
        element = indexedObject[inductionVariable]
        inductionVariable = (inductionVariable + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
        count = (count + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
        if count > 1:
            buffer.append_v1o70a_k_(separator)
            Unit_getInstance()
        
        if (True) if (limit < 0) else (count <= limit):
            appendElement(element, transform)
        else:
            break
        
    
    if (count > limit) if (limit >= 0) else (False):
        buffer.append_v1o70a_k_(truncated)
        Unit_getInstance()
    
    buffer.append_v1o70a_k_(postfix)
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

def contains(element):
    return indexOf_0(element) >= 0

def indexOf_0(element):
    inductionVariable = 0
    last = (len(self) - 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
    if inductionVariable <= last:
        while True:
            index = inductionVariable
            inductionVariable = (inductionVariable + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
            if element == self[index]:
                return index
            
            if inductionVariable <= last:
                break
            
        
    
    return -1

def _get_indices__0():
    return IntRange(0, _get_lastIndex__0())

def _get_lastIndex__0():
    return (len(self) - 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)

def contains_0(element):
    return indexOf_1(element) >= 0

def indexOf_1(element):
    inductionVariable = 0
    last = (len(self) - 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
    if inductionVariable <= last:
        while True:
            index = inductionVariable
            inductionVariable = (inductionVariable + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
            if element == self[index]:
                return index
            
            if inductionVariable <= last:
                break
            
        
    
    return -1

def _get_indices__1():
    return IntRange(0, _get_lastIndex__1())

def _get_lastIndex__1():
    return (len(self) - 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)

def contains_1(element):
    return indexOf_2(element) >= 0

def indexOf_2(element):
    inductionVariable = 0
    last = (len(self) - 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
    if inductionVariable <= last:
        while True:
            index = inductionVariable
            inductionVariable = (inductionVariable + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
            if element == self[index]:
                return index
            
            if inductionVariable <= last:
                break
            
        
    
    return -1

def _get_indices__2():
    return IntRange(0, _get_lastIndex__2())

def _get_lastIndex__2():
    return (len(self) - 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)

def contains_2(element):
    return indexOf_3(element) >= 0

def indexOf_3(element):
    inductionVariable = 0
    last = (len(self) - 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
    if inductionVariable <= last:
        while True:
            index = inductionVariable
            inductionVariable = (inductionVariable + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
            if element == self[index]:
                return index
            
            if inductionVariable <= last:
                break
            
        
    
    return -1

def _get_indices__3():
    return IntRange(0, _get_lastIndex__3())

def _get_lastIndex__3():
    return (len(self) - 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)

def indexOfFirst(predicate):
    index = 0
    tmp0_iterator = self.iterator_0_k_()
    while tmp0_iterator.hasNext_0_k_():
        item = tmp0_iterator.next_0_k_()
        if predicate(item):
            return index
        
        tmp1 = index
        index = (tmp1 + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
        Unit_getInstance()
    
    return -1

def indexOfLast(predicate):
    iterator = self.listIterator_ha5a7z_k_(self._get_size__0_k_())
    while iterator.hasPrevious_0_k_():
        if predicate(iterator.previous_0_k_()):
            return iterator.nextIndex_0_k_()
        
    
    return -1

def any(predicate):
    if isInterface(self, jsClass()):
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

def all(predicate):
    if isInterface(self, jsClass()):
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

def joinToString_0(separator, prefix, postfix, limit, truncated, transform):
    return joinTo_0(StringBuilder_init__Create__1(), separator, prefix, postfix, limit, truncated, transform).toString()

def joinToString_default_0(separator, prefix, postfix, limit, truncated, transform, _mask0, _handler):
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
    
    return joinToString_0(kotlin_CharSequence(separator), kotlin_CharSequence(prefix), kotlin_CharSequence(postfix), limit, kotlin_CharSequence(truncated), transform)

def joinTo_0(buffer, separator, prefix, postfix, limit, truncated, transform):
    buffer.append_v1o70a_k_(prefix)
    Unit_getInstance()
    count = 0
    tmp0_iterator = self.iterator_0_k_()
    while tmp0_iterator.hasNext_0_k_():
        element = tmp0_iterator.next_0_k_()
        count = (count + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
        if count > 1:
            buffer.append_v1o70a_k_(separator)
            Unit_getInstance()
        
        if (True) if (limit < 0) else (count <= limit):
            appendElement(element, transform)
        else:
            break
        
    
    if (count > limit) if (limit >= 0) else (False):
        buffer.append_v1o70a_k_(truncated)
        Unit_getInstance()
    
    buffer.append_v1o70a_k_(postfix)
    Unit_getInstance()
    return buffer

def joinTo_default_0(buffer, separator, prefix, postfix, limit, truncated, transform, _mask0, _handler):
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
    
    return joinTo_0(buffer, kotlin_CharSequence(separator), kotlin_CharSequence(prefix), kotlin_CharSequence(postfix), limit, kotlin_CharSequence(truncated), transform)

def forEach(action):
    tmp0_iterator = self.iterator_0_k_()
    while tmp0_iterator.hasNext_0_k_():
        element = tmp0_iterator.next_0_k_()
        action(element)
    

def map(transform):
    tmp0_mapTo_0 = ArrayList_init__Create__0(collectionSizeOrDefault(10))
    tmp0_iterator_1 = self.iterator_0_k_()
    while tmp0_iterator_1.hasNext_0_k_():
        item_2 = tmp0_iterator_1.next_0_k_()
        tmp0_mapTo_0.add_2bq_k_(transform(item_2))
        Unit_getInstance()
    
    return tmp0_mapTo_0

def mapTo(destination, transform):
    tmp0_iterator = self.iterator_0_k_()
    while tmp0_iterator.hasNext_0_k_():
        item = tmp0_iterator.next_0_k_()
        destination.add_2bq_k_(transform(item))
        Unit_getInstance()
    
    return destination

def downTo(to):
    return Companion_getInstance_11().fromClosedRange_fcwjfj_k_(self, to, -1)

def until(to):
    if to <= IntCompanionObject_getInstance().MIN_VALUE:
        return Companion_getInstance_14().EMPTY
    
    return numberRangeToNumber(self, (to - 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))

def reversed():
    return Companion_getInstance_11().fromClosedRange_fcwjfj_k_(self.last, self.first, (-self.step).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))

def getOrElse(index, defaultValue):
    return (charSequenceGet(self, index)) if ((index <= _get_lastIndex__5()) if (index >= 0) else (False)) else (defaultValue(index))

def KotlinNothingValueException_init__Init_(_this):
    RuntimeException_init__Init_(_this)
    super()
    return _this

def KotlinNothingValueException_init__Create_():
    tmp = KotlinNothingValueException_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def KotlinNothingValueException_init__Init__0(message, _this):
    RuntimeException_init__Init__0(message, _this)
    super()
    return _this

def KotlinNothingValueException_init__Create__0(message):
    tmp = KotlinNothingValueException_init__Init__0(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def KotlinNothingValueException_init__Init__1(message, cause, _this):
    RuntimeException_init__Init__1(message, cause, _this)
    super()
    return _this

def KotlinNothingValueException_init__Create__1(message, cause):
    tmp = KotlinNothingValueException_init__Init__1(message, cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def KotlinNothingValueException_init__Init__2(cause, _this):
    RuntimeException_init__Init__2(cause, _this)
    super()
    return _this

def KotlinNothingValueException_init__Create__2(cause):
    tmp = KotlinNothingValueException_init__Init__2(cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

class KotlinNothingValueException:
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
    
    def __init__(self):
        captureStack(self, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    

def _get_code_():
    return self.toInt_0_k_()

def Char(code):
    Companion_getInstance_17()
    tmp0__get_code__0 = Char_0(0)
    if code < tmp0__get_code__0.toInt_0_k_():
        tmp = True
    elif True:
        Companion_getInstance_17()
        tmp1__get_code__0 = Char_0(65535)
        tmp = code > tmp1__get_code__0.toInt_0_k_()
    
    if tmp:
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

class Experimental:
    def __init__(self, level):
        self.level = level
    
    def _get_level__0_k_(self):
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
    
    def _get_markerClass__0_k_(self):
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
    Level_WARNING_instance = Level_0('WARNING', 0)
    Level_ERROR_instance = Level_0('ERROR', 1)

def RequiresOptIn_init__Init_(message, level, _mask0, _marker, _this):
    if not (_mask0 & 1 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    if not (_mask0 & 2 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    super(message, level)
    return _this

def RequiresOptIn_init__Create_(message, level, _mask0, _marker):
    return RequiresOptIn_init__Init_(message, level, _mask0, _marker, Object_create())

class Level_0:
    def __init__(self, name, ordinal):
        super(name, ordinal)
    
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

class RequiresOptIn:
    def __init__(self, message, level):
        self.message = message
        self.level = level
    
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
    

class OptIn:
    def __init__(self, *markerClass):
        self.markerClass = markerClass
    
    def _get_markerClass__0_k_(self):
        return self.markerClass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class AbstractCollection:
    def __init__(self):
        pass
    
    def _get_size__0_k_(self):
        pass
    
    def iterator_0_k_(self):
        pass
    
    def contains_2bq_k_(self, element):
        while True:
            if isInterface(self, jsClass()):
                tmp = kotlin_collections_Collection_kotlin_Any__(self).isEmpty_0_k_()
            elif True:
                tmp = False
            
            if tmp:
                tmp_ret_0 = False
                break
            
            tmp0_iterator_1 = self.iterator_0_k_()
            while tmp0_iterator_1.hasNext_0_k_():
                element_2 = tmp0_iterator_1.next_0_k_()
                if element_2 == element:
                    tmp_ret_0 = True
                    break
                
            
            tmp_ret_0 = False
            if False:
                break
            
        
        return tmp_ret_0
    
    def containsAll_dxd4eo_k_(self, elements):
        while True:
            if isInterface(elements, jsClass()):
                tmp = kotlin_collections_Collection_kotlin_Any__(elements).isEmpty_0_k_()
            elif True:
                tmp = False
            
            if tmp:
                tmp_ret_0 = True
                break
            
            tmp0_iterator_1 = elements.iterator_0_k_()
            while tmp0_iterator_1.hasNext_0_k_():
                element_2 = tmp0_iterator_1.next_0_k_()
                if not self.contains_2bq_k_(element_2):
                    tmp_ret_0 = False
                    break
                
            
            tmp_ret_0 = True
            if False:
                break
            
        
        return tmp_ret_0
    
    def isEmpty_0_k_(self):
        return self._get_size__0_k_() == 0
    
    def toString(self):
        return joinToString_default_0(', ', '[', ']', 0, None, lambda it: ('(this Collection)') if (it is self) else (toString()), 24, None)
    
    def toArray(self):
        return copyToArrayImpl_0(self)
    
    def toArray_gjotr5_k_(self, array):
        return copyToArrayImpl_1(self, array)
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    

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
        Companion_getInstance().checkRangeIndexes_zd700_k_(self.fromIndex, toIndex, self.list._get_size__0_k_())
        self._size = (toIndex - self.fromIndex).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
    
    def get_ha5a7z_k_(self, index):
        Companion_getInstance().checkElementIndex_rvwcgf_k_(index, self._size)
        return self.list.get_ha5a7z_k_((self.fromIndex + index).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))
    
    def _get_size__0_k_(self):
        return self._size
    
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
    

class IteratorImpl:
    def __init__(self, _outer):
        self._this = _outer
        self.index = 0
    
    def _set_index__majfzk_k_(self, _set___):
        self.index = _set___
    
    def _get_index__0_k_(self):
        return self.index
    
    def hasNext_0_k_(self):
        return self.index < self._this._get_size__0_k_()
    
    def next_0_k_(self):
        if not self.hasNext_0_k_():
            raise NoSuchElementException_init__Create_()
        
        tmp0_this = self
        tmp1 = tmp0_this.index
        tmp0_this.index = (tmp1 + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
        return self._this.get_ha5a7z_k_(tmp1)
    
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
        Companion_getInstance().checkPositionIndex_rvwcgf_k_(index, self._this._get_size__0_k_())
        self._set_index__majfzk_k_(index)
    
    def hasPrevious_0_k_(self):
        return self._get_index__0_k_() > 0
    
    def nextIndex_0_k_(self):
        return self._get_index__0_k_()
    
    def previous_0_k_(self):
        if not self.hasPrevious_0_k_():
            raise NoSuchElementException_init__Create_()
        
        tmp0_this = self
        tmp0_this._set_index__majfzk_k_((tmp0_this._get_index__0_k_() - 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))
        return self._this.get_ha5a7z_k_(tmp0_this._get_index__0_k_())
    
    def previousIndex_0_k_(self):
        return (self._get_index__0_k_() - 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
    
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
    

class Companion_0:
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
            hashCode = (tmp + ((0) if (tmp2_elvis_lhs == None) else (tmp2_elvis_lhs))).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
        
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

class AbstractList:
    def __init__(self):
        Companion_getInstance()
        super()
    
    def _get_size__0_k_(self):
        pass
    
    def get_ha5a7z_k_(self, index):
        pass
    
    def iterator_0_k_(self):
        return IteratorImpl(self)
    
    def indexOf_2bq_k_(self, element):
        while True:
            index_1 = 0
            tmp0_iterator_2 = self.iterator_0_k_()
            while tmp0_iterator_2.hasNext_0_k_():
                item_3 = tmp0_iterator_2.next_0_k_()
                if item_3 == element:
                    tmp_ret_0 = index_1
                    break
                
                tmp1_4 = index_1
                index_1 = (tmp1_4 + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
                Unit_getInstance()
            
            tmp_ret_0 = -1
            if False:
                break
            
        
        return tmp_ret_0
    
    def lastIndexOf_2bq_k_(self, element):
        while True:
            iterator_1 = self.listIterator_ha5a7z_k_(self._get_size__0_k_())
            while iterator_1.hasPrevious_0_k_():
                tmp0__anonymous__2 = iterator_1.previous_0_k_()
                if tmp0__anonymous__2 == element:
                    tmp_ret_0 = iterator_1.nextIndex_0_k_()
                    break
                
            
            tmp_ret_0 = -1
            if False:
                break
            
        
        return tmp_ret_0
    
    def listIterator_0_k_(self):
        return ListIteratorImpl(self, 0)
    
    def listIterator_ha5a7z_k_(self, index):
        return ListIteratorImpl(self, index)
    
    def subList_27zxwg_k_(self, fromIndex, toIndex):
        return SubList(self, fromIndex, toIndex)
    
    def equals(self, other):
        if other is self:
            return True
        
        if not ((isInterface(other, jsClass())) if (not (other == None)) else (False)):
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
    return (asList()) if (len(elements) > 0) else (emptyList())

def emptyList():
    return EmptyList_getInstance()

def _get_serialVersionUID_(_this):
    return _this.serialVersionUID

def readResolve(_this):
    return EmptyList_getInstance()

class EmptyList:
    def __init__(self):
        global EmptyList_instance
        EmptyList_instance = self
        self.serialVersionUID = -7390468764508069838
    
    def equals(self, other):
        if (isInterface(other, jsClass())) if (not (other == None)) else (False):
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
    
    def contains_2bq_k_(self, element):
        if not False:
            return False
        
        if False:
            tmp = kotlin_Nothing(element)
        elif True:
            tmp = THROW_CCE()
        
        return self.contains_5jd3j5_k_(tmp)
    
    def containsAll_lwol4p_k_(self, elements):
        return elements.isEmpty_0_k_()
    
    def containsAll_dxd4eo_k_(self, elements):
        return self.containsAll_lwol4p_k_(elements)
    
    def get_ha5a7z_k_(self, index):
        raise IndexOutOfBoundsException_init__Create__0((str('Empty list doesn\'t contain element at index ') + str(index)) + str('.'))
    
    def indexOf_5jd3j5_k_(self, element):
        return -1
    
    def indexOf_2bq_k_(self, element):
        if not False:
            return -1
        
        if False:
            tmp = kotlin_Nothing(element)
        elif True:
            tmp = THROW_CCE()
        
        return self.indexOf_5jd3j5_k_(tmp)
    
    def lastIndexOf_5jd3j5_k_(self, element):
        return -1
    
    def lastIndexOf_2bq_k_(self, element):
        if not False:
            return -1
        
        if False:
            tmp = kotlin_Nothing(element)
        elif True:
            tmp = THROW_CCE()
        
        return self.lastIndexOf_5jd3j5_k_(tmp)
    
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
    

EmptyList_instance = None
def EmptyList_getInstance():
    if EmptyList_instance == None:
        EmptyList()
    
    return EmptyList_instance

class EmptyIterator:
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

def _get_lastIndex__4():
    return (self._get_size__0_k_() - 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)

def collectionSizeOrDefault(default):
    if isInterface(self, jsClass()):
        tmp = kotlin_collections_Collection_kotlin_Any__(self)._get_size__0_k_()
    elif True:
        tmp = default
    
    return tmp

def removeAll(predicate):
    return filterInPlace(predicate, True)

def removeAll_0(predicate):
    return filterInPlace_0(predicate, True)

def filterInPlace(predicate, predicateResultToRemove):
    if not isInterface(self, jsClass()):
        return filterInPlace_0(predicate, predicateResultToRemove)
    
    writeIndex = 0
    inductionVariable = 0
    last = _get_lastIndex__4()
    if inductionVariable <= last:
        while True:
            readIndex = inductionVariable
            inductionVariable = (inductionVariable + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
            element = self.get_ha5a7z_k_(readIndex)
            if predicate(element) == predicateResultToRemove:
                continue
            
            if not (writeIndex == readIndex):
                self.set_ddb1qf_k_(writeIndex, element)
                Unit_getInstance()
            
            tmp1 = writeIndex
            writeIndex = (tmp1 + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
            Unit_getInstance()
            if not (readIndex == last):
                break
            
        
    
    if writeIndex < self._get_size__0_k_():
        inductionVariable = _get_lastIndex__4()
        if writeIndex <= inductionVariable:
            while True:
                removeIndex = inductionVariable
                inductionVariable = (inductionVariable + -1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
                self.removeAt_ha5a7z_k_(removeIndex)
                Unit_getInstance()
                if not (removeIndex == writeIndex):
                    break
                
            
        
        return True
    else:
        return False
    

def filterInPlace_0(predicate, predicateResultToRemove):
    result = False
    tmp0_with_0 = self.iterator_0_k_()
    while tmp0_with_0.hasNext_0_k_():
        if predicate(tmp0_with_0.next_0_k_()) == predicateResultToRemove:
            tmp0_with_0.remove_sv8swh_k_()
            result = True
        
    
    return result

class Sequence:
    def iterator_0_k_(self):
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
    def returns_0_k_(self):
        pass
    
    def returns_wi7j7l_k_(self, value):
        pass
    
    def returnsNotNull_0_k_(self):
        pass
    
    def callsInPlace_x6l8zl_k_(self, _lambda, kind):
        pass
    
    def callsInPlace_default_i7jixu_k_(self, _lambda, kind, _mask0, _handler):
        if not (_mask0 & 2 == 0):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
        
        return (self.callsInPlace_x6l8zl_k_(_lambda, kotlin_contracts_InvocationKind(kind))) if (_handler == None) else (kotlin_Function2_kotlin_Function2_kotlin_Function2_kotlin_Function2_(_handler)(_lambda, kind))
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def __init__(self):
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
    InvocationKind_AT_MOST_ONCE_instance = InvocationKind('AT_MOST_ONCE', 0)
    InvocationKind_AT_LEAST_ONCE_instance = InvocationKind('AT_LEAST_ONCE', 1)
    InvocationKind_EXACTLY_ONCE_instance = InvocationKind('EXACTLY_ONCE', 2)
    InvocationKind_UNKNOWN_instance = InvocationKind('UNKNOWN', 3)

class InvocationKind:
    def __init__(self, name, ordinal):
        super(name, ordinal)
    
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
    def implies_vcj5fe_k_(self, booleanExpression):
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
    def implies_vcj5fe_k_(self, booleanExpression):
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
    def implies_vcj5fe_k_(self, booleanExpression):
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
    
    def __init__(self):
        pass
    

def Continuation_0(context, resumeWith):
    return _no_name_provided_(context, resumeWith)

def resumeWithException(exception):
    tmp0_failure_0 = Companion_getInstance_2()
    return self.resumeWith_bnunh2_k_(_Result___init__impl_(createFailure(exception)))

def resume(value):
    tmp0_success_0 = Companion_getInstance_2()
    return self.resumeWith_bnunh2_k_(_Result___init__impl_(value))

def _get_coroutineContext_():
    raise NotImplementedError('Implemented as intrinsic')

class _no_name_provided_:
    def __init__(self, _context, _resumeWith):
        self._context = _context
        self._resumeWith = _resumeWith
    
    def _get_context__0_k_(self):
        return self._context
    
    def resumeWith_bnunh2_k_(self, result):
        return self._resumeWith(boxIntrinsic(result))
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class Key:
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

class ContinuationInterceptor:
    def interceptContinuation_x4ijla_k_(self, continuation):
        pass
    
    def releaseInterceptedContinuation_h7c6yl_k_(self, continuation):
        pass
    
    def get_9uvjra_k_(self, key):
        if visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
            if kotlin_coroutines_AbstractCoroutineContextKey_____(key).isSubKey_djuxjq_k_(self._get_key__0_k_()):
                tmp = kotlin_coroutines_AbstractCoroutineContextKey_____(key).tryCast_k332zt_k_(self)
                tmp = (E(tmp)) if ((isInterface(tmp, jsClass())) if (not (tmp == None)) else (False)) else (None)
            else:
                tmp = None
            
            return tmp
        
        if Key_getInstance() is key:
            tmp = (E(self)) if (isInterface(self, jsClass())) else (THROW_CCE())
        else:
            tmp = None
        
        return tmp
    
    def minusKey_djuxjq_k_(self, key):
        if visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
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
    
    def __init__(self):
        Key_getInstance()
    

class Key_0:
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def __init__(self):
        pass
    

class Element:
    def _get_key__0_k_(self):
        pass
    
    def get_9uvjra_k_(self, key):
        if self._get_key__0_k_() == key:
            tmp = (E(self)) if (isInterface(self, jsClass())) else (THROW_CCE())
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
    
    def __init__(self):
        pass
    

class CoroutineContext:
    def get_9uvjra_k_(self, key):
        pass
    
    def fold_cq605b_k_(self, initial, operation):
        pass
    
    def plus_d7pszg_k_(self, context):
        return (self) if (context is EmptyCoroutineContext_getInstance()) else (context.fold_cq605b_k_(self, lambda acc, element: visitExpressionFunctionBodyStatements_x4__Assign__Expr__If__Return_))
    
    def minusKey_djuxjq_k_(self, key):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def __init__(self):
        pass
    

def _get_serialVersionUID__0(_this):
    return _this.serialVersionUID

def readResolve_0(_this):
    return EmptyCoroutineContext_getInstance()

class EmptyCoroutineContext:
    def __init__(self):
        global EmptyCoroutineContext_instance
        EmptyCoroutineContext_instance = self
        self.serialVersionUID = 0
    
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

def _get_serialVersionUID__1(_this):
    return _this.serialVersionUID

class Companion_1:
    def __init__(self):
        global Companion_instance
        Companion_instance = self
        self.serialVersionUID = 0
    
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

def readResolve_1(_this):
    tmp0_fold_0 = _this.elements
    tmp1_fold_0 = EmptyCoroutineContext_getInstance()
    accumulator_1 = tmp1_fold_0
    indexedObject = tmp0_fold_0
    inductionVariable = 0
    last = len(indexedObject)
    while inductionVariable < last:
        element_3 = indexedObject[inductionVariable]
        inductionVariable = (inductionVariable + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
        accumulator_1 = accumulator_1.plus_d7pszg_k_(element_3)
    
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
        tmp0_elvis_lhs = (kotlin_coroutines_CombinedContext(tmp)) if (visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean) else (None)
        if tmp0_elvis_lhs == None:
            return size
        else:
            tmp = tmp0_elvis_lhs
        
        cur = tmp
        tmp1 = size
        size = (tmp1 + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
        Unit_getInstance()
    

def contains_3(_this, element):
    return _this.get_9uvjra_k_(element._get_key__0_k_()) == element

def containsAll(_this, context):
    cur = context
    while True:
        if not contains_3(_this, cur.element):
            return False
        
        next = cur.left
        if visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
            cur = kotlin_coroutines_CombinedContext(next)
        elif True:
            return contains_3(_this, (kotlin_coroutines_Element(next)) if (isInterface(next, jsClass())) else (THROW_CCE()))
        
    

def writeReplace(_this):
    n = size(_this)
    elements = fillArrayVal(Array(n), None)
    index = _sharedBox_create(0)
    _this.fold_cq605b_k_(Unit_getInstance(), lambda _anonymous_parameter_0_, element: visitExpressionFunctionBodyStatements_x3__Assign__Expr__Expr_)
    tmp0_check_0 = _sharedBox_read(index) == n
    if not tmp0_check_0:
        message_2 = 'Check failed.'
        raise IllegalStateException_init__Create__0(toString_0(message_2))
    
    return Serialized((kotlin_Array_kotlin_coroutines_CoroutineContext_(elements)) if (isArray(elements)) else (THROW_CCE()))

class Serialized:
    def __init__(self, elements):
        Companion_getInstance_0()
        self.elements = elements
    
    def _get_elements__0_k_(self):
        return self.elements
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class CombinedContext:
    def __init__(self, left, element):
        self.left = left
        self.element = element
    
    def get_9uvjra_k_(self, key):
        cur = self
        while True:
            tmp0_safe_receiver = cur.element.get_9uvjra_k_(key)
            if tmp0_safe_receiver == None:
                visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstImpl
            else:
                return tmp0_safe_receiver
            
            Unit_getInstance()
            next = cur.left
            if visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
                cur = kotlin_coroutines_CombinedContext(next)
            elif True:
                return next.get_9uvjra_k_(key)
            
        
    
    def fold_cq605b_k_(self, initial, operation):
        return operation(self.left.fold_cq605b_k_(initial, operation), self.element)
    
    def minusKey_djuxjq_k_(self, key):
        tmp0_safe_receiver = self.element.get_9uvjra_k_(key)
        if tmp0_safe_receiver == None:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrConstImpl
        else:
            return self.left
        
        Unit_getInstance()
        newLeft = self.left.minusKey_djuxjq_k_(key)
        return (self) if (newLeft is self.left) else ((self.element) if (newLeft is EmptyCoroutineContext_getInstance()) else (CombinedContext(newLeft, self.element)))
    
    def equals(self, other):
        if self is other:
            tmp = True
        else:
            if visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
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
        return (hashCode(self.left) + hashCode(self.element)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
    
    def toString(self):
        return ('[' + self.fold_cq605b_k_('', lambda acc, element: visitExpressionFunctionBodyStatements_x2__If__Return_)) + ']'
    
    def plus_d7pszg_k_(self, context):
        pass
    

def _get_safeCast_(_this):
    return _this.safeCast

def _get_topmostKey_(_this):
    return _this.topmostKey

class AbstractCoroutineContextKey:
    def __init__(self, baseKey, safeCast):
        self.safeCast = safeCast
        tmp = self
        if visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
            tmp = kotlin_coroutines_AbstractCoroutineContextKey_____(baseKey).topmostKey
        elif True:
            tmp = baseKey
        
        tmp.topmostKey = tmp
    
    def tryCast_k332zt_k_(self, element):
        return self.safeCast(element)
    
    def isSubKey_djuxjq_k_(self, key):
        return (True) if (key is self) else (self.topmostKey is key)
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def _get_COROUTINE_SUSPENDED_():
    return CoroutineSingletons_COROUTINE_SUSPENDED_getInstance()

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
    CoroutineSingletons_COROUTINE_SUSPENDED_instance = CoroutineSingletons('COROUTINE_SUSPENDED', 0)
    CoroutineSingletons_UNDECIDED_instance = CoroutineSingletons('UNDECIDED', 1)
    CoroutineSingletons_RESUMED_instance = CoroutineSingletons('RESUMED', 2)

class CoroutineSingletons:
    def __init__(self, name, ordinal):
        super(name, ordinal)
    
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

def _and(other):
    return (self & other).__add__(0x8000).__and__(0xffff).__sub__(0x8000)

def _or(other):
    return (self | other).__add__(0x8000).__and__(0xffff).__sub__(0x8000)

def xor(other):
    return (self ^ other).__add__(0x8000).__and__(0xffff).__sub__(0x8000)

def inv():
    return (~self).__add__(0x8000).__and__(0xffff).__sub__(0x8000)

def and_0(other):
    return (self & other).__add__(0x80).__and__(0xff).__sub__(0x80)

def or_0(other):
    return (self | other).__add__(0x80).__and__(0xff).__sub__(0x80)

def xor_0(other):
    return (self ^ other).__add__(0x80).__and__(0xff).__sub__(0x80)

def inv_0():
    return (~self).__add__(0x80).__and__(0xff).__sub__(0x80)

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
    RequireKotlinVersionKind_LANGUAGE_VERSION_instance = RequireKotlinVersionKind('LANGUAGE_VERSION', 0)
    RequireKotlinVersionKind_COMPILER_VERSION_instance = RequireKotlinVersionKind('COMPILER_VERSION', 1)
    RequireKotlinVersionKind_API_VERSION_instance = RequireKotlinVersionKind('API_VERSION', 2)

class RequireKotlinVersionKind:
    def __init__(self, name, ordinal):
        super(name, ordinal)
    
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
    

class HidesMembers:
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
    
    def __init__(self):
        pass
    

class Companion_2:
    def __init__(self):
        global Companion_instance
        Companion_instance = self
        self.star = KTypeProjection(None, None)
    
    def _get_star__0_k_(self):
        return self.star
    
    def _get_STAR__0_k_(self):
        return self.star
    
    def invariant_573d5y_k_(self, type):
        return KTypeProjection(KVariance_INVARIANT_getInstance(), type)
    
    def contravariant_573d5y_k_(self, type):
        return KTypeProjection(KVariance_IN_getInstance(), type)
    
    def covariant_573d5y_k_(self, type):
        return KTypeProjection(KVariance_OUT_getInstance(), type)
    
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

class KTypeProjection:
    def __init__(self, variance, type):
        Companion_getInstance_1()
        self.variance = variance
        self.type = type
        tmp0_require_0 = self.variance == None == self.type == None
        if not tmp0_require_0:
            message_2 = ('Star projection must have no type specified.') if (self.variance == None) else ((str('The projection variance ') + str(self.variance)) + str(' requires type to be specified.'))
            raise IllegalArgumentException_init__Create__0(toString_0(message_2))
        
    
    def _get_variance__0_k_(self):
        return self.variance
    
    def _get_type__0_k_(self):
        return self.type
    
    def toString(self):
        tmp0_subject = self.variance
        if tmp0_subject == None:
            tmp = '*'
        elif tmp0_subject == KVariance_INVARIANT_getInstance():
            tmp = toString()
        elif tmp0_subject == KVariance_IN_getInstance():
            tmp = str('in ') + str(self.type)
        elif tmp0_subject == KVariance_OUT_getInstance():
            tmp = str('out ') + str(self.type)
        else:
            noWhenBranchMatchedException()
        
        return tmp
    
    def component1_0_k_(self):
        return self.variance
    
    def component2_0_k_(self):
        return self.type
    
    def copy_fey4rp_k_(self, variance, type):
        return KTypeProjection(variance, type)
    
    def copy_default_jp35qf_k_(self, variance, type, _mask0, _handler):
        if not (_mask0 & 1 == 0):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
        
        if not (_mask0 & 2 == 0):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
        
        return self.copy_fey4rp_k_(variance, type)
    
    def hashCode(self):
        result = (0) if (self.variance == None) else (self.variance.hashCode())
        result = (imul(result, 31) + ((0) if (self.type == None) else (hashCode(self.type)))).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
        return result
    
    def equals(self, other):
        if self is other:
            return True
        
        if not visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
            return False
        
        tmp0_other_with_cast = (kotlin_reflect_KTypeProjection(other)) if (visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean) else (THROW_CCE())
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
    KVariance_INVARIANT_instance = KVariance('INVARIANT', 0)
    KVariance_IN_instance = KVariance('IN', 1)
    KVariance_OUT_instance = KVariance('OUT', 2)

class KVariance:
    def __init__(self, name, ordinal):
        super(name, ordinal)
    
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

def appendElement(element, transform):
    if not (transform == None):
        self.append_v1o70a_k_(transform(element))
        Unit_getInstance()
    elif (True) if (element == None) else (isCharSequence(element)):
        self.append_v1o70a_k_(kotlin_CharSequence_(element))
        Unit_getInstance()
    elif visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
        self.append_wi8o78_k_(kotlin_Char(element))
        Unit_getInstance()
    elif True:
        self.append_v1o70a_k_(toString())
        Unit_getInstance()
    

def isEmpty():
    return charSequenceLength(self) == 0

def _get_lastIndex__5():
    return (charSequenceLength(self) - 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)

def _get_UNDEFINED_RESULT_():
    return UNDEFINED_RESULT

UNDEFINED_RESULT = None
def UNDEFINED_RESULT_init_():
    tmp0_success_0 = Companion_getInstance_2()
    tmp1_success_0 = _get_COROUTINE_SUSPENDED_()
    return _Result___init__impl_(tmp1_success_0)

def check(value):
    if not value:
        message_2 = 'Check failed.'
        raise IllegalStateException_init__Create__0(toString_0(message_2))
    

def check_0(value, lazyMessage):
    if not value:
        message = lazyMessage()
        raise IllegalStateException_init__Create__0(toString_0(message))
    

def error(message):
    raise IllegalStateException_init__Create__0(toString_0(message))

def require_0(value, lazyMessage):
    if not value:
        message = lazyMessage()
        raise IllegalArgumentException_init__Create__0(toString_0(message))
    

def _Result___init__impl_(value):
    return kotlin_Result_T_(value)

def _Result___get_value__impl_(this):
    return this.value

def _Result___get_isSuccess__impl_(this):
    tmp = _Result___get_value__impl_(this)
    return not visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean

def _Result___get_isFailure__impl_(this):
    tmp = _Result___get_value__impl_(this)
    return visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean

def Result__getOrNull_impl(this):
    if _Result___get_isFailure__impl_(this):
        tmp = None
    else:
        tmp = _Result___get_value__impl_(this)
        tmp = (T(tmp)) if ((True) if (tmp == None) else (isObject(tmp))) else (THROW_CCE())
    
    return tmp

def Result__exceptionOrNull_impl(this):
    tmp0_subject = _Result___get_value__impl_(this)
    if visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
        tmp = kotlin_Failure(_Result___get_value__impl_(this)).exception
    elif True:
        tmp = None
    
    return tmp

def Result__toString_impl(this):
    tmp0_subject = _Result___get_value__impl_(this)
    if visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
        tmp = toString_0(_Result___get_value__impl_(this))
    elif True:
        tmp = (str('Success(') + str(_Result___get_value__impl_(this))) + str(')')
    
    return tmp

class Companion_3:
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

class Failure:
    def __init__(self, exception):
        self.exception = exception
    
    def _get_exception__0_k_(self):
        return self.exception
    
    def equals(self, other):
        if visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
            tmp = self.exception == kotlin_Failure(other).exception
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
    if not visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
        return False
    
    tmp0_other_with_cast = (unboxIntrinsic(other)) if (visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean) else (THROW_CCE())
    if not (this.value == tmp0_other_with_cast.value):
        return False
    
    return True

class Result:
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

def getOrThrow():
    throwOnFailure()
    tmp = _Result___get_value__impl_(self)
    return (T(tmp)) if ((True) if (tmp == None) else (isObject(tmp))) else (THROW_CCE())

def throwOnFailure():
    tmp = _Result___get_value__impl_(self)
    if visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
        raise kotlin_Failure(_Result___get_value__impl_(self)).exception
    

def run(block):
    return block()

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
        Error_init__Init__0(message, self)
        captureStack(self, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    
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
    

def let_0(block):
    return block(self)

def apply(block):
    block(self)
    return self

def repeat(times, action):
    inductionVariable = 0
    if inductionVariable < times:
        while True:
            index = inductionVariable
            inductionVariable = (inductionVariable + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
            action(index)
            if inductionVariable < times:
                break
            
        
    

def with_0(receiver, block):
    return block(receiver)

def also(block):
    block(self)
    return self

def run_0(block):
    return block(self)

def _UByte___init__impl_(data):
    return kotlin_UByte(data)

def _UByte___get_data__impl_(this):
    return this.data

class Companion_4:
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
    tmp = _UByte___get_data__impl_(this) & 255
    return compareTo_0(tmp, _UByte___get_data__impl_(other) & 255)

def UByte__compareTo_impl_0(this, other):
    tmp = unboxIntrinsic(this)
    return UByte__compareTo_impl(tmp, (unboxIntrinsic(other)) if (visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean) else (THROW_CCE()))

def UByte__compareTo_impl_1(this, other):
    tmp = _UByte___get_data__impl_(this) & 255
    return compareTo_0(tmp, _UShort___get_data__impl_(other) & 65535)

def UByte__compareTo_impl_2(this, other):
    tmp0_compareTo_0 = _UInt___init__impl_(_UByte___get_data__impl_(this) & 255)
    return uintCompare(_UInt___get_data__impl_(tmp0_compareTo_0), _UInt___get_data__impl_(other))

def UByte__compareTo_impl_3(this, other):
    tmp0_compareTo_0 = _ULong___init__impl_((_UByte___get_data__impl_(this) & 255).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    return ulongCompare(_ULong___get_data__impl_(tmp0_compareTo_0), _ULong___get_data__impl_(other))

def UByte__plus_impl(this, other):
    tmp0_plus_0 = _UInt___init__impl_(_UByte___get_data__impl_(this) & 255)
    tmp1_plus_0 = _UInt___init__impl_(_UByte___get_data__impl_(other) & 255)
    return _UInt___init__impl_((_UInt___get_data__impl_(tmp0_plus_0) + _UInt___get_data__impl_(tmp1_plus_0)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))

def UByte__plus_impl_0(this, other):
    tmp0_plus_0 = _UInt___init__impl_(_UByte___get_data__impl_(this) & 255)
    tmp1_plus_0 = _UInt___init__impl_(_UShort___get_data__impl_(other) & 65535)
    return _UInt___init__impl_((_UInt___get_data__impl_(tmp0_plus_0) + _UInt___get_data__impl_(tmp1_plus_0)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))

def UByte__plus_impl_1(this, other):
    tmp0_plus_0 = _UInt___init__impl_(_UByte___get_data__impl_(this) & 255)
    return _UInt___init__impl_((_UInt___get_data__impl_(tmp0_plus_0) + _UInt___get_data__impl_(other)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))

def UByte__plus_impl_2(this, other):
    tmp0_plus_0 = _ULong___init__impl_((_UByte___get_data__impl_(this) & 255).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    return _ULong___init__impl_((_ULong___get_data__impl_(tmp0_plus_0) + _ULong___get_data__impl_(other)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))

def UByte__minus_impl(this, other):
    tmp0_minus_0 = _UInt___init__impl_(_UByte___get_data__impl_(this) & 255)
    tmp1_minus_0 = _UInt___init__impl_(_UByte___get_data__impl_(other) & 255)
    return _UInt___init__impl_((_UInt___get_data__impl_(tmp0_minus_0) - _UInt___get_data__impl_(tmp1_minus_0)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))

def UByte__minus_impl_0(this, other):
    tmp0_minus_0 = _UInt___init__impl_(_UByte___get_data__impl_(this) & 255)
    tmp1_minus_0 = _UInt___init__impl_(_UShort___get_data__impl_(other) & 65535)
    return _UInt___init__impl_((_UInt___get_data__impl_(tmp0_minus_0) - _UInt___get_data__impl_(tmp1_minus_0)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))

def UByte__minus_impl_1(this, other):
    tmp0_minus_0 = _UInt___init__impl_(_UByte___get_data__impl_(this) & 255)
    return _UInt___init__impl_((_UInt___get_data__impl_(tmp0_minus_0) - _UInt___get_data__impl_(other)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))

def UByte__minus_impl_2(this, other):
    tmp0_minus_0 = _ULong___init__impl_((_UByte___get_data__impl_(this) & 255).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    return _ULong___init__impl_((_ULong___get_data__impl_(tmp0_minus_0) - _ULong___get_data__impl_(other)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))

def UByte__times_impl(this, other):
    tmp0_times_0 = _UInt___init__impl_(_UByte___get_data__impl_(this) & 255)
    tmp1_times_0 = _UInt___init__impl_(_UByte___get_data__impl_(other) & 255)
    return _UInt___init__impl_(imul(_UInt___get_data__impl_(tmp0_times_0), _UInt___get_data__impl_(tmp1_times_0)))

def UByte__times_impl_0(this, other):
    tmp0_times_0 = _UInt___init__impl_(_UByte___get_data__impl_(this) & 255)
    tmp1_times_0 = _UInt___init__impl_(_UShort___get_data__impl_(other) & 65535)
    return _UInt___init__impl_(imul(_UInt___get_data__impl_(tmp0_times_0), _UInt___get_data__impl_(tmp1_times_0)))

def UByte__times_impl_1(this, other):
    tmp0_times_0 = _UInt___init__impl_(_UByte___get_data__impl_(this) & 255)
    return _UInt___init__impl_(imul(_UInt___get_data__impl_(tmp0_times_0), _UInt___get_data__impl_(other)))

def UByte__times_impl_2(this, other):
    tmp0_times_0 = _ULong___init__impl_((_UByte___get_data__impl_(this) & 255).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    return _ULong___init__impl_((_ULong___get_data__impl_(tmp0_times_0) * _ULong___get_data__impl_(other)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))

def UByte__div_impl(this, other):
    tmp0_div_0 = _UInt___init__impl_(_UByte___get_data__impl_(this) & 255)
    tmp1_div_0 = _UInt___init__impl_(_UByte___get_data__impl_(other) & 255)
    return uintDivide(tmp0_div_0, tmp1_div_0)

def UByte__div_impl_0(this, other):
    tmp0_div_0 = _UInt___init__impl_(_UByte___get_data__impl_(this) & 255)
    tmp1_div_0 = _UInt___init__impl_(_UShort___get_data__impl_(other) & 65535)
    return uintDivide(tmp0_div_0, tmp1_div_0)

def UByte__div_impl_1(this, other):
    tmp0_div_0 = _UInt___init__impl_(_UByte___get_data__impl_(this) & 255)
    return uintDivide(tmp0_div_0, other)

def UByte__div_impl_2(this, other):
    tmp0_div_0 = _ULong___init__impl_((_UByte___get_data__impl_(this) & 255).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    return ulongDivide(tmp0_div_0, other)

def UByte__rem_impl(this, other):
    tmp0_rem_0 = _UInt___init__impl_(_UByte___get_data__impl_(this) & 255)
    tmp1_rem_0 = _UInt___init__impl_(_UByte___get_data__impl_(other) & 255)
    return uintRemainder(tmp0_rem_0, tmp1_rem_0)

def UByte__rem_impl_0(this, other):
    tmp0_rem_0 = _UInt___init__impl_(_UByte___get_data__impl_(this) & 255)
    tmp1_rem_0 = _UInt___init__impl_(_UShort___get_data__impl_(other) & 65535)
    return uintRemainder(tmp0_rem_0, tmp1_rem_0)

def UByte__rem_impl_1(this, other):
    tmp0_rem_0 = _UInt___init__impl_(_UByte___get_data__impl_(this) & 255)
    return uintRemainder(tmp0_rem_0, other)

def UByte__rem_impl_2(this, other):
    tmp0_rem_0 = _ULong___init__impl_((_UByte___get_data__impl_(this) & 255).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    return ulongRemainder(tmp0_rem_0, other)

def UByte__floorDiv_impl(this, other):
    tmp0_floorDiv_0 = _UInt___init__impl_(_UByte___get_data__impl_(this) & 255)
    tmp1_floorDiv_0 = _UInt___init__impl_(_UByte___get_data__impl_(other) & 255)
    return uintDivide(tmp0_floorDiv_0, tmp1_floorDiv_0)

def UByte__floorDiv_impl_0(this, other):
    tmp0_floorDiv_0 = _UInt___init__impl_(_UByte___get_data__impl_(this) & 255)
    tmp1_floorDiv_0 = _UInt___init__impl_(_UShort___get_data__impl_(other) & 65535)
    return uintDivide(tmp0_floorDiv_0, tmp1_floorDiv_0)

def UByte__floorDiv_impl_1(this, other):
    tmp0_floorDiv_0 = _UInt___init__impl_(_UByte___get_data__impl_(this) & 255)
    return uintDivide(tmp0_floorDiv_0, other)

def UByte__floorDiv_impl_2(this, other):
    tmp0_floorDiv_0 = _ULong___init__impl_((_UByte___get_data__impl_(this) & 255).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    return ulongDivide(tmp0_floorDiv_0, other)

def UByte__mod_impl(this, other):
    tmp0_mod_0 = _UInt___init__impl_(_UByte___get_data__impl_(this) & 255)
    tmp1_mod_0 = _UInt___init__impl_(_UByte___get_data__impl_(other) & 255)
    tmp3_toUByte_0 = uintRemainder(tmp0_mod_0, tmp1_mod_0)
    tmp2_toUByte_0 = _UInt___get_data__impl_(tmp3_toUByte_0)
    return _UByte___init__impl_(tmp2_toUByte_0.__add__(0x80).__and__(0xff).__sub__(0x80))

def UByte__mod_impl_0(this, other):
    tmp0_mod_0 = _UInt___init__impl_(_UByte___get_data__impl_(this) & 255)
    tmp1_mod_0 = _UInt___init__impl_(_UShort___get_data__impl_(other) & 65535)
    tmp3_toUShort_0 = uintRemainder(tmp0_mod_0, tmp1_mod_0)
    tmp2_toUShort_0 = _UInt___get_data__impl_(tmp3_toUShort_0)
    return _UShort___init__impl_(tmp2_toUShort_0.__add__(0x8000).__and__(0xffff).__sub__(0x8000))

def UByte__mod_impl_1(this, other):
    tmp0_mod_0 = _UInt___init__impl_(_UByte___get_data__impl_(this) & 255)
    return uintRemainder(tmp0_mod_0, other)

def UByte__mod_impl_2(this, other):
    tmp0_mod_0 = _ULong___init__impl_((_UByte___get_data__impl_(this) & 255).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    return ulongRemainder(tmp0_mod_0, other)

def UByte__inc_impl(this):
    return _UByte___init__impl_((_UByte___get_data__impl_(this) + 1).__add__(0x80).__and__(0xff).__sub__(0x80))

def UByte__dec_impl(this):
    return _UByte___init__impl_((_UByte___get_data__impl_(this) - 1).__add__(0x80).__and__(0xff).__sub__(0x80))

def UByte__rangeTo_impl(this, other):
    tmp = _UInt___init__impl_(_UByte___get_data__impl_(this) & 255)
    return UIntRange(tmp, _UInt___init__impl_(_UByte___get_data__impl_(other) & 255))

def UByte__and_impl(this, other):
    tmp0_and_0 = _UByte___get_data__impl_(this)
    tmp1_and_0 = _UByte___get_data__impl_(other)
    return _UByte___init__impl_((tmp0_and_0 & tmp1_and_0).__add__(0x80).__and__(0xff).__sub__(0x80))

def UByte__or_impl(this, other):
    tmp0_or_0 = _UByte___get_data__impl_(this)
    tmp1_or_0 = _UByte___get_data__impl_(other)
    return _UByte___init__impl_((tmp0_or_0 | tmp1_or_0).__add__(0x80).__and__(0xff).__sub__(0x80))

def UByte__xor_impl(this, other):
    tmp0_xor_0 = _UByte___get_data__impl_(this)
    tmp1_xor_0 = _UByte___get_data__impl_(other)
    return _UByte___init__impl_((tmp0_xor_0 ^ tmp1_xor_0).__add__(0x80).__and__(0xff).__sub__(0x80))

def UByte__inv_impl(this):
    tmp0_inv_0 = _UByte___get_data__impl_(this)
    return _UByte___init__impl_((~tmp0_inv_0).__add__(0x80).__and__(0xff).__sub__(0x80))

def UByte__toByte_impl(this):
    return _UByte___get_data__impl_(this)

def UByte__toShort_impl(this):
    tmp0_and_0 = _UByte___get_data__impl_(this)
    return (tmp0_and_0 & 255).__add__(0x8000).__and__(0xffff).__sub__(0x8000)

def UByte__toInt_impl(this):
    return _UByte___get_data__impl_(this) & 255

def UByte__toLong_impl(this):
    return (_UByte___get_data__impl_(this) & 255).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)

def UByte__toUByte_impl(this):
    return this

def UByte__toUShort_impl(this):
    tmp0_and_0 = _UByte___get_data__impl_(this)
    return _UShort___init__impl_((tmp0_and_0 & 255).__add__(0x8000).__and__(0xffff).__sub__(0x8000))

def UByte__toUInt_impl(this):
    return _UInt___init__impl_(_UByte___get_data__impl_(this) & 255)

def UByte__toULong_impl(this):
    return _ULong___init__impl_((_UByte___get_data__impl_(this) & 255).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))

def UByte__toFloat_impl(this):
    return kotlin_Float(_UByte___get_data__impl_(this) & 255)

def UByte__toDouble_impl(this):
    return kotlin_Double(_UByte___get_data__impl_(this) & 255)

def UByte__toString_impl(this):
    return (_UByte___get_data__impl_(this) & 255).toString()

def UByte__hashCode_impl(this):
    return this.data

def UByte__equals_impl(this, other):
    if not visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
        return False
    
    tmp0_other_with_cast = (unboxIntrinsic(other)) if (visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean) else (THROW_CCE())
    if not (this.data == tmp0_other_with_cast.data):
        return False
    
    return True

class UByte:
    def __init__(self, data):
        Companion_getInstance_3()
        self.data = data
    
    def compareTo_dj4lnz_k_(self, other):
        return UByte__compareTo_impl(unboxIntrinsic(self), other)
    
    def compareTo_2c5_k_(self, other):
        return UByte__compareTo_impl_0(self, other)
    
    def toString(self):
        return UByte__toString_impl(unboxIntrinsic(self))
    
    def hashCode(self):
        return UByte__hashCode_impl(unboxIntrinsic(self))
    
    def equals(self, other):
        return UByte__equals_impl(unboxIntrinsic(self), other)
    

def toUByte():
    return _UByte___init__impl_(self.__add__(0x80).__and__(0xff).__sub__(0x80))

def toUByte_0():
    return _UByte___init__impl_(self.__add__(0x80).__and__(0xff).__sub__(0x80))

def toUByte_1():
    return _UByte___init__impl_(self.__add__(0x80).__and__(0xff).__sub__(0x80))

def toUByte_2():
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

def _UByteArray___init__impl__0(size):
    tmp = _UByteArray___init__impl_(visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_int8Array_visibility_public_modality_FINAL_____arg0_kotlin_Any___returnType_kotlin_Any_)
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
    
    def hasNext_0_k_(self):
        return self.index < len(self.array)
    
    def nextUByte_sh428i_k_(self):
        if self.index < len(self.array):
            tmp0_this = self
            tmp1 = tmp0_this.index
            tmp0_this.index = (tmp1 + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
            tmp0_toUByte_0 = self.array[tmp1]
            tmp = _UByte___init__impl_(tmp0_toUByte_0)
        else:
            raise NoSuchElementException_init__Create__0(self.index.toString())
        
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
    if not visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
        return False
    
    tmp = _UByteArray___get_storage__impl_(this)
    return contains(_UByte___get_data__impl_(element))

def UByteArray__contains_impl_0(this, element):
    if not visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
        return False
    
    tmp = unboxIntrinsic(this)
    return UByteArray__contains_impl(tmp, (unboxIntrinsic(element)) if (visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean) else (THROW_CCE()))

def UByteArray__containsAll_impl(this, elements):
    while True:
        tmp0_all_0 = (kotlin_collections_Collection___(elements)) if (isInterface(elements, jsClass())) else (THROW_CCE())
        if isInterface(tmp0_all_0, jsClass()):
            tmp = kotlin_collections_Collection_kotlin_Any__(tmp0_all_0).isEmpty_0_k_()
        elif True:
            tmp = False
        
        if tmp:
            tmp_ret_0 = True
            break
        
        tmp0_iterator_1 = tmp0_all_0.iterator_0_k_()
        while tmp0_iterator_1.hasNext_0_k_():
            element_2 = tmp0_iterator_1.next_0_k_()
            if visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
                tmp = _UByteArray___get_storage__impl_(this)
                tmp0_toByte_0_4 = unboxIntrinsic(element_2)
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

def UByteArray__containsAll_impl_0(this, elements):
    return UByteArray__containsAll_impl(unboxIntrinsic(this), elements)

def UByteArray__isEmpty_impl(this):
    return len(_UByteArray___get_storage__impl_(this)) == 0

def UByteArray__toString_impl(this):
    return (str('UByteArray(storage=') + str(toString_0(this.storage))) + str(')')

def UByteArray__hashCode_impl(this):
    return hashCode(this.storage)

def UByteArray__equals_impl(this, other):
    if not visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
        return False
    
    tmp0_other_with_cast = (unboxIntrinsic(other)) if (visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean) else (THROW_CCE())
    if not (this.storage == tmp0_other_with_cast.storage):
        return False
    
    return True

class UByteArray:
    def __init__(self, storage):
        self.storage = storage
    
    def _get_size__0_k_(self):
        return _UByteArray___get_size__impl_(unboxIntrinsic(self))
    
    def iterator_0_k_(self):
        return UByteArray__iterator_impl(unboxIntrinsic(self))
    
    def contains_dj4lnz_k_(self, element):
        return UByteArray__contains_impl(unboxIntrinsic(self), element)
    
    def contains_2bq_k_(self, element):
        return UByteArray__contains_impl_0(self, element)
    
    def containsAll_wji8mv_k_(self, elements):
        return UByteArray__containsAll_impl(unboxIntrinsic(self), elements)
    
    def containsAll_dxd4eo_k_(self, elements):
        return UByteArray__containsAll_impl_0(self, elements)
    
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

class Companion_5:
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
    tmp0_compareTo_0 = _UInt___init__impl_(_UByte___get_data__impl_(other) & 255)
    return uintCompare(_UInt___get_data__impl_(this), _UInt___get_data__impl_(tmp0_compareTo_0))

def UInt__compareTo_impl_0(this, other):
    tmp0_compareTo_0 = _UInt___init__impl_(_UShort___get_data__impl_(other) & 65535)
    return uintCompare(_UInt___get_data__impl_(this), _UInt___get_data__impl_(tmp0_compareTo_0))

def UInt__compareTo_impl_1(this, other):
    return uintCompare(_UInt___get_data__impl_(this), _UInt___get_data__impl_(other))

def UInt__compareTo_impl_2(this, other):
    tmp = unboxIntrinsic(this)
    return UInt__compareTo_impl_1(tmp, (unboxIntrinsic(other)) if (visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean) else (THROW_CCE()))

def UInt__compareTo_impl_3(this, other):
    tmp0_compareTo_0 = _ULong___init__impl_((_UInt___get_data__impl_(this) & 4294967295).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    return ulongCompare(_ULong___get_data__impl_(tmp0_compareTo_0), _ULong___get_data__impl_(other))

def UInt__plus_impl(this, other):
    tmp0_plus_0 = _UInt___init__impl_(_UByte___get_data__impl_(other) & 255)
    return _UInt___init__impl_((_UInt___get_data__impl_(this) + _UInt___get_data__impl_(tmp0_plus_0)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))

def UInt__plus_impl_0(this, other):
    tmp0_plus_0 = _UInt___init__impl_(_UShort___get_data__impl_(other) & 65535)
    return _UInt___init__impl_((_UInt___get_data__impl_(this) + _UInt___get_data__impl_(tmp0_plus_0)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))

def UInt__plus_impl_1(this, other):
    return _UInt___init__impl_((_UInt___get_data__impl_(this) + _UInt___get_data__impl_(other)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))

def UInt__plus_impl_2(this, other):
    tmp0_plus_0 = _ULong___init__impl_((_UInt___get_data__impl_(this) & 4294967295).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    return _ULong___init__impl_((_ULong___get_data__impl_(tmp0_plus_0) + _ULong___get_data__impl_(other)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))

def UInt__minus_impl(this, other):
    tmp0_minus_0 = _UInt___init__impl_(_UByte___get_data__impl_(other) & 255)
    return _UInt___init__impl_((_UInt___get_data__impl_(this) - _UInt___get_data__impl_(tmp0_minus_0)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))

def UInt__minus_impl_0(this, other):
    tmp0_minus_0 = _UInt___init__impl_(_UShort___get_data__impl_(other) & 65535)
    return _UInt___init__impl_((_UInt___get_data__impl_(this) - _UInt___get_data__impl_(tmp0_minus_0)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))

def UInt__minus_impl_1(this, other):
    return _UInt___init__impl_((_UInt___get_data__impl_(this) - _UInt___get_data__impl_(other)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))

def UInt__minus_impl_2(this, other):
    tmp0_minus_0 = _ULong___init__impl_((_UInt___get_data__impl_(this) & 4294967295).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    return _ULong___init__impl_((_ULong___get_data__impl_(tmp0_minus_0) - _ULong___get_data__impl_(other)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))

def UInt__times_impl(this, other):
    tmp0_times_0 = _UInt___init__impl_(_UByte___get_data__impl_(other) & 255)
    return _UInt___init__impl_(imul(_UInt___get_data__impl_(this), _UInt___get_data__impl_(tmp0_times_0)))

def UInt__times_impl_0(this, other):
    tmp0_times_0 = _UInt___init__impl_(_UShort___get_data__impl_(other) & 65535)
    return _UInt___init__impl_(imul(_UInt___get_data__impl_(this), _UInt___get_data__impl_(tmp0_times_0)))

def UInt__times_impl_1(this, other):
    return _UInt___init__impl_(imul(_UInt___get_data__impl_(this), _UInt___get_data__impl_(other)))

def UInt__times_impl_2(this, other):
    tmp0_times_0 = _ULong___init__impl_((_UInt___get_data__impl_(this) & 4294967295).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    return _ULong___init__impl_((_ULong___get_data__impl_(tmp0_times_0) * _ULong___get_data__impl_(other)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))

def UInt__div_impl(this, other):
    tmp0_div_0 = _UInt___init__impl_(_UByte___get_data__impl_(other) & 255)
    return uintDivide(this, tmp0_div_0)

def UInt__div_impl_0(this, other):
    tmp0_div_0 = _UInt___init__impl_(_UShort___get_data__impl_(other) & 65535)
    return uintDivide(this, tmp0_div_0)

def UInt__div_impl_1(this, other):
    return uintDivide(this, other)

def UInt__div_impl_2(this, other):
    tmp0_div_0 = _ULong___init__impl_((_UInt___get_data__impl_(this) & 4294967295).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    return ulongDivide(tmp0_div_0, other)

def UInt__rem_impl(this, other):
    tmp0_rem_0 = _UInt___init__impl_(_UByte___get_data__impl_(other) & 255)
    return uintRemainder(this, tmp0_rem_0)

def UInt__rem_impl_0(this, other):
    tmp0_rem_0 = _UInt___init__impl_(_UShort___get_data__impl_(other) & 65535)
    return uintRemainder(this, tmp0_rem_0)

def UInt__rem_impl_1(this, other):
    return uintRemainder(this, other)

def UInt__rem_impl_2(this, other):
    tmp0_rem_0 = _ULong___init__impl_((_UInt___get_data__impl_(this) & 4294967295).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    return ulongRemainder(tmp0_rem_0, other)

def UInt__floorDiv_impl(this, other):
    tmp0_floorDiv_0 = _UInt___init__impl_(_UByte___get_data__impl_(other) & 255)
    return uintDivide(this, tmp0_floorDiv_0)

def UInt__floorDiv_impl_0(this, other):
    tmp0_floorDiv_0 = _UInt___init__impl_(_UShort___get_data__impl_(other) & 65535)
    return uintDivide(this, tmp0_floorDiv_0)

def UInt__floorDiv_impl_1(this, other):
    return uintDivide(this, other)

def UInt__floorDiv_impl_2(this, other):
    tmp0_floorDiv_0 = _ULong___init__impl_((_UInt___get_data__impl_(this) & 4294967295).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    return ulongDivide(tmp0_floorDiv_0, other)

def UInt__mod_impl(this, other):
    tmp0_mod_0 = _UInt___init__impl_(_UByte___get_data__impl_(other) & 255)
    tmp2_toUByte_0 = uintRemainder(this, tmp0_mod_0)
    tmp1_toUByte_0 = _UInt___get_data__impl_(tmp2_toUByte_0)
    return _UByte___init__impl_(tmp1_toUByte_0.__add__(0x80).__and__(0xff).__sub__(0x80))

def UInt__mod_impl_0(this, other):
    tmp0_mod_0 = _UInt___init__impl_(_UShort___get_data__impl_(other) & 65535)
    tmp2_toUShort_0 = uintRemainder(this, tmp0_mod_0)
    tmp1_toUShort_0 = _UInt___get_data__impl_(tmp2_toUShort_0)
    return _UShort___init__impl_(tmp1_toUShort_0.__add__(0x8000).__and__(0xffff).__sub__(0x8000))

def UInt__mod_impl_1(this, other):
    return uintRemainder(this, other)

def UInt__mod_impl_2(this, other):
    tmp0_mod_0 = _ULong___init__impl_((_UInt___get_data__impl_(this) & 4294967295).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    return ulongRemainder(tmp0_mod_0, other)

def UInt__inc_impl(this):
    return _UInt___init__impl_((_UInt___get_data__impl_(this) + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))

def UInt__dec_impl(this):
    return _UInt___init__impl_((_UInt___get_data__impl_(this) - 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))

def UInt__rangeTo_impl(this, other):
    return UIntRange(this, other)

def UInt__shl_impl(this, bitCount):
    return _UInt___init__impl_((_UInt___get_data__impl_(this) << bitCount).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))

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
    return _UInt___get_data__impl_(this).__add__(0x80).__and__(0xff).__sub__(0x80)

def UInt__toShort_impl(this):
    return _UInt___get_data__impl_(this).__add__(0x8000).__and__(0xffff).__sub__(0x8000)

def UInt__toInt_impl(this):
    return _UInt___get_data__impl_(this)

def UInt__toLong_impl(this):
    return (_UInt___get_data__impl_(this) & 4294967295).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)

def UInt__toUByte_impl(this):
    tmp0_toUByte_0 = _UInt___get_data__impl_(this)
    return _UByte___init__impl_(tmp0_toUByte_0.__add__(0x80).__and__(0xff).__sub__(0x80))

def UInt__toUShort_impl(this):
    tmp0_toUShort_0 = _UInt___get_data__impl_(this)
    return _UShort___init__impl_(tmp0_toUShort_0.__add__(0x8000).__and__(0xffff).__sub__(0x8000))

def UInt__toUInt_impl(this):
    return this

def UInt__toULong_impl(this):
    return _ULong___init__impl_((_UInt___get_data__impl_(this) & 4294967295).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))

def UInt__toFloat_impl(this):
    return kotlin_Float(uintToDouble(_UInt___get_data__impl_(this)))

def UInt__toDouble_impl(this):
    return uintToDouble(_UInt___get_data__impl_(this))

def UInt__toString_impl(this):
    return (_UInt___get_data__impl_(this) & 4294967295).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000).toString()

def UInt__hashCode_impl(this):
    return this.data

def UInt__equals_impl(this, other):
    if not visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
        return False
    
    tmp0_other_with_cast = (unboxIntrinsic(other)) if (visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean) else (THROW_CCE())
    if not (this.data == tmp0_other_with_cast.data):
        return False
    
    return True

class UInt:
    def __init__(self, data):
        Companion_getInstance_4()
        self.data = data
    
    def compareTo_wijjag_k_(self, other):
        return UInt__compareTo_impl_1(unboxIntrinsic(self), other)
    
    def compareTo_2c5_k_(self, other):
        return UInt__compareTo_impl_2(self, other)
    
    def toString(self):
        return UInt__toString_impl(unboxIntrinsic(self))
    
    def hashCode(self):
        return UInt__hashCode_impl(unboxIntrinsic(self))
    
    def equals(self, other):
        return UInt__equals_impl(unboxIntrinsic(self), other)
    

def toUInt():
    return _UInt___init__impl_(self.__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))

def toUInt_0():
    return _UInt___init__impl_(self)

def toUInt_1():
    return _UInt___init__impl_(self)

def toUInt_2():
    return doubleToUInt(self)

def toUInt_3():
    return doubleToUInt(kotlin_Double(self))

def toUInt_4():
    return _UInt___init__impl_(self)

def _get_array__0(_this):
    return _this.array

def _set_index__0(_this, _set___):
    _this.index = _set___

def _get_index__0(_this):
    return _this.index

def _UIntArray___init__impl_(storage):
    return kotlin_UIntArray(storage)

def _UIntArray___get_storage__impl_(this):
    return this.storage

def _UIntArray___init__impl__0(size):
    tmp = _UIntArray___init__impl_(visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_int32Array_visibility_public_modality_FINAL_____arg0_kotlin_Any___returnType_kotlin_Any_)
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
    return Iterator_0(_UIntArray___get_storage__impl_(this))

class Iterator_0:
    def __init__(self, array):
        super()
        self.array = array
        self.index = 0
    
    def hasNext_0_k_(self):
        return self.index < len(self.array)
    
    def nextUInt_sv9k7v_k_(self):
        if self.index < len(self.array):
            tmp0_this = self
            tmp1 = tmp0_this.index
            tmp0_this.index = (tmp1 + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
            tmp0_toUInt_0 = self.array[tmp1]
            tmp = _UInt___init__impl_(tmp0_toUInt_0)
        else:
            raise NoSuchElementException_init__Create__0(self.index.toString())
        
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
    if not visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
        return False
    
    tmp = _UIntArray___get_storage__impl_(this)
    return contains_1(_UInt___get_data__impl_(element))

def UIntArray__contains_impl_0(this, element):
    if not visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
        return False
    
    tmp = unboxIntrinsic(this)
    return UIntArray__contains_impl(tmp, (unboxIntrinsic(element)) if (visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean) else (THROW_CCE()))

def UIntArray__containsAll_impl(this, elements):
    while True:
        tmp0_all_0 = (kotlin_collections_Collection___(elements)) if (isInterface(elements, jsClass())) else (THROW_CCE())
        if isInterface(tmp0_all_0, jsClass()):
            tmp = kotlin_collections_Collection_kotlin_Any__(tmp0_all_0).isEmpty_0_k_()
        elif True:
            tmp = False
        
        if tmp:
            tmp_ret_0 = True
            break
        
        tmp0_iterator_1 = tmp0_all_0.iterator_0_k_()
        while tmp0_iterator_1.hasNext_0_k_():
            element_2 = tmp0_iterator_1.next_0_k_()
            if visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
                tmp = _UIntArray___get_storage__impl_(this)
                tmp0_toInt_0_4 = unboxIntrinsic(element_2)
                tmp = contains_1(_UInt___get_data__impl_(tmp0_toInt_0_4))
            elif True:
                tmp = False
            
            if not tmp:
                tmp_ret_0 = False
                break
            
        
        tmp_ret_0 = True
        if False:
            break
        
    
    return tmp_ret_0

def UIntArray__containsAll_impl_0(this, elements):
    return UIntArray__containsAll_impl(unboxIntrinsic(this), elements)

def UIntArray__isEmpty_impl(this):
    return len(_UIntArray___get_storage__impl_(this)) == 0

def UIntArray__toString_impl(this):
    return (str('UIntArray(storage=') + str(toString_0(this.storage))) + str(')')

def UIntArray__hashCode_impl(this):
    return hashCode(this.storage)

def UIntArray__equals_impl(this, other):
    if not visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
        return False
    
    tmp0_other_with_cast = (unboxIntrinsic(other)) if (visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean) else (THROW_CCE())
    if not (this.storage == tmp0_other_with_cast.storage):
        return False
    
    return True

class UIntArray:
    def __init__(self, storage):
        self.storage = storage
    
    def _get_size__0_k_(self):
        return _UIntArray___get_size__impl_(unboxIntrinsic(self))
    
    def iterator_0_k_(self):
        return UIntArray__iterator_impl(unboxIntrinsic(self))
    
    def contains_wijjag_k_(self, element):
        return UIntArray__contains_impl(unboxIntrinsic(self), element)
    
    def contains_2bq_k_(self, element):
        return UIntArray__contains_impl_0(self, element)
    
    def containsAll_sjraxa_k_(self, elements):
        return UIntArray__containsAll_impl(unboxIntrinsic(self), elements)
    
    def containsAll_dxd4eo_k_(self, elements):
        return UIntArray__containsAll_impl_0(self, elements)
    
    def isEmpty_0_k_(self):
        return UIntArray__isEmpty_impl(unboxIntrinsic(self))
    
    def toString(self):
        return UIntArray__toString_impl(unboxIntrinsic(self))
    
    def hashCode(self):
        return UIntArray__hashCode_impl(unboxIntrinsic(self))
    
    def equals(self, other):
        return UIntArray__equals_impl(unboxIntrinsic(self), other)
    

class Companion_6:
    def __init__(self):
        global Companion_instance
        Companion_instance = self
        tmp = self
        Companion_getInstance_4()
        tmp = _UInt___init__impl_(-1)
        Companion_getInstance_4()
        tmp.EMPTY = UIntRange(tmp, _UInt___init__impl_(0))
    
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

class UIntRange:
    def __init__(self, start, endInclusive):
        Companion_getInstance_5()
        super(start, endInclusive, 1)
    
    def _get_start__sv9k7v_k_(self):
        return self._get_first__sv9k7v_k_()
    
    def _get_start__0_k_(self):
        return boxIntrinsic(self._get_start__sv9k7v_k_())
    
    def _get_endInclusive__sv9k7v_k_(self):
        return self._get_last__sv9k7v_k_()
    
    def _get_endInclusive__0_k_(self):
        return boxIntrinsic(self._get_endInclusive__sv9k7v_k_())
    
    def contains_wijjag_k_(self, value):
        tmp0_compareTo_0 = self._get_first__sv9k7v_k_()
        if uintCompare(_UInt___get_data__impl_(tmp0_compareTo_0), _UInt___get_data__impl_(value)) <= 0:
            tmp1_compareTo_0 = self._get_last__sv9k7v_k_()
            tmp = uintCompare(_UInt___get_data__impl_(value), _UInt___get_data__impl_(tmp1_compareTo_0)) <= 0
        elif True:
            tmp = False
        
        return tmp
    
    def contains_2c5_k_(self, value):
        return self.contains_wijjag_k_((unboxIntrinsic(value)) if (visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean) else (THROW_CCE()))
    
    def isEmpty_0_k_(self):
        tmp0_compareTo_0 = self._get_first__sv9k7v_k_()
        tmp1_compareTo_0 = self._get_last__sv9k7v_k_()
        return uintCompare(_UInt___get_data__impl_(tmp0_compareTo_0), _UInt___get_data__impl_(tmp1_compareTo_0)) > 0
    
    def equals(self, other):
        if visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
            tmp = (True) if ((kotlin_ranges_UIntRange(other).isEmpty_0_k_()) if (self.isEmpty_0_k_()) else (False)) else ((boxIntrinsic(self._get_last__sv9k7v_k_()) == boxIntrinsic(kotlin_ranges_UIntRange(other)._get_last__sv9k7v_k_())) if (boxIntrinsic(self._get_first__sv9k7v_k_()) == boxIntrinsic(kotlin_ranges_UIntRange(other)._get_first__sv9k7v_k_())) else (False))
        elif True:
            tmp = False
        
        return tmp
    
    def hashCode(self):
        if self.isEmpty_0_k_():
            tmp = -1
        else:
            tmp0_toInt_0 = self._get_first__sv9k7v_k_()
            tmp = imul(31, _UInt___get_data__impl_(tmp0_toInt_0))
            tmp1_toInt_0 = self._get_last__sv9k7v_k_()
            tmp = (tmp + _UInt___get_data__impl_(tmp1_toInt_0)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
        
        return tmp
    
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
    

class Companion_7:
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

class UIntProgression:
    def __init__(self, start, endInclusive, step):
        Companion_getInstance_6()
        if step == 0:
            raise IllegalArgumentException_init__Create__0('Step must be non-zero.')
        
        if step == IntCompanionObject_getInstance().MIN_VALUE:
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
        return UIntProgressionIterator(self.first, self.last, self.step)
    
    def isEmpty_0_k_(self):
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
        if visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
            tmp = (True) if ((kotlin_ranges_UIntProgression(other).isEmpty_0_k_()) if (self.isEmpty_0_k_()) else (False)) else ((self.step == kotlin_ranges_UIntProgression(other).step) if ((boxIntrinsic(self.last) == boxIntrinsic(kotlin_ranges_UIntProgression(other).last)) if (boxIntrinsic(self.first) == boxIntrinsic(kotlin_ranges_UIntProgression(other).first)) else (False)) else (False))
        elif True:
            tmp = False
        
        return tmp
    
    def hashCode(self):
        if self.isEmpty_0_k_():
            tmp = -1
        else:
            tmp0_toInt_0 = self.first
            tmp = imul(31, _UInt___get_data__impl_(tmp0_toInt_0))
            tmp1_toInt_0 = self.last
            tmp = (imul(31, (tmp + _UInt___get_data__impl_(tmp1_toInt_0)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)) + self.step).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
        
        return tmp
    
    def toString(self):
        return ((((str(boxIntrinsic(self.first)) + str('..')) + str(boxIntrinsic(self.last))) + str(' step ')) + str(self.step)) if (self.step > 0) else ((((str(boxIntrinsic(self.first)) + str(' downTo ')) + str(boxIntrinsic(self.last))) + str(' step ')) + str((-self.step).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)))
    

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
    
    def hasNext_0_k_(self):
        return self.hasNext
    
    def nextUInt_sv9k7v_k_(self):
        value = self.next
        if boxIntrinsic(value) == boxIntrinsic(self.finalElement):
            if not self.hasNext:
                raise NoSuchElementException_init__Create_()
            
            self.hasNext = False
        else:
            tmp0_this = self
            tmp = tmp0_this
            tmp0_plus_0 = tmp0_this.next
            tmp1_plus_0 = self.step
            tmp.next = _UInt___init__impl_((_UInt___get_data__impl_(tmp0_plus_0) + _UInt___get_data__impl_(tmp1_plus_0)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))
        
        return value
    
    def next_sv9k7v_k_(self):
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
    
    def next_sv9k7v_k_(self):
        return self.nextUInt_sv9k7v_k_()
    
    def next_0_k_(self):
        return boxIntrinsic(self.next_sv9k7v_k_())
    
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
    

class ULongIterator:
    def __init__(self):
        pass
    
    def next_sha8jq_k_(self):
        return self.nextULong_sha8jq_k_()
    
    def next_0_k_(self):
        return boxIntrinsic(self.next_sha8jq_k_())
    
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
    

class UByteIterator:
    def __init__(self):
        pass
    
    def next_sh428i_k_(self):
        return self.nextUByte_sh428i_k_()
    
    def next_0_k_(self):
        return boxIntrinsic(self.next_sh428i_k_())
    
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
    

class UShortIterator:
    def __init__(self):
        pass
    
    def next_um6tma_k_(self):
        return self.nextUShort_um6tma_k_()
    
    def next_0_k_(self):
        return boxIntrinsic(self.next_um6tma_k_())
    
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

class Companion_8:
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
    tmp0_compareTo_0 = _ULong___init__impl_((_UByte___get_data__impl_(other) & 255).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    return ulongCompare(_ULong___get_data__impl_(this), _ULong___get_data__impl_(tmp0_compareTo_0))

def ULong__compareTo_impl_0(this, other):
    tmp0_compareTo_0 = _ULong___init__impl_((_UShort___get_data__impl_(other) & 65535).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    return ulongCompare(_ULong___get_data__impl_(this), _ULong___get_data__impl_(tmp0_compareTo_0))

def ULong__compareTo_impl_1(this, other):
    tmp0_compareTo_0 = _ULong___init__impl_((_UInt___get_data__impl_(other) & 4294967295).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    return ulongCompare(_ULong___get_data__impl_(this), _ULong___get_data__impl_(tmp0_compareTo_0))

def ULong__compareTo_impl_2(this, other):
    return ulongCompare(_ULong___get_data__impl_(this), _ULong___get_data__impl_(other))

def ULong__compareTo_impl_3(this, other):
    tmp = unboxIntrinsic(this)
    return ULong__compareTo_impl_2(tmp, (unboxIntrinsic(other)) if (visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean) else (THROW_CCE()))

def ULong__plus_impl(this, other):
    tmp0_plus_0 = _ULong___init__impl_((_UByte___get_data__impl_(other) & 255).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    return _ULong___init__impl_((_ULong___get_data__impl_(this) + _ULong___get_data__impl_(tmp0_plus_0)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))

def ULong__plus_impl_0(this, other):
    tmp0_plus_0 = _ULong___init__impl_((_UShort___get_data__impl_(other) & 65535).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    return _ULong___init__impl_((_ULong___get_data__impl_(this) + _ULong___get_data__impl_(tmp0_plus_0)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))

def ULong__plus_impl_1(this, other):
    tmp0_plus_0 = _ULong___init__impl_((_UInt___get_data__impl_(other) & 4294967295).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    return _ULong___init__impl_((_ULong___get_data__impl_(this) + _ULong___get_data__impl_(tmp0_plus_0)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))

def ULong__plus_impl_2(this, other):
    return _ULong___init__impl_((_ULong___get_data__impl_(this) + _ULong___get_data__impl_(other)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))

def ULong__minus_impl(this, other):
    tmp0_minus_0 = _ULong___init__impl_((_UByte___get_data__impl_(other) & 255).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    return _ULong___init__impl_((_ULong___get_data__impl_(this) - _ULong___get_data__impl_(tmp0_minus_0)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))

def ULong__minus_impl_0(this, other):
    tmp0_minus_0 = _ULong___init__impl_((_UShort___get_data__impl_(other) & 65535).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    return _ULong___init__impl_((_ULong___get_data__impl_(this) - _ULong___get_data__impl_(tmp0_minus_0)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))

def ULong__minus_impl_1(this, other):
    tmp0_minus_0 = _ULong___init__impl_((_UInt___get_data__impl_(other) & 4294967295).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    return _ULong___init__impl_((_ULong___get_data__impl_(this) - _ULong___get_data__impl_(tmp0_minus_0)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))

def ULong__minus_impl_2(this, other):
    return _ULong___init__impl_((_ULong___get_data__impl_(this) - _ULong___get_data__impl_(other)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))

def ULong__times_impl(this, other):
    tmp0_times_0 = _ULong___init__impl_((_UByte___get_data__impl_(other) & 255).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    return _ULong___init__impl_((_ULong___get_data__impl_(this) * _ULong___get_data__impl_(tmp0_times_0)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))

def ULong__times_impl_0(this, other):
    tmp0_times_0 = _ULong___init__impl_((_UShort___get_data__impl_(other) & 65535).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    return _ULong___init__impl_((_ULong___get_data__impl_(this) * _ULong___get_data__impl_(tmp0_times_0)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))

def ULong__times_impl_1(this, other):
    tmp0_times_0 = _ULong___init__impl_((_UInt___get_data__impl_(other) & 4294967295).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    return _ULong___init__impl_((_ULong___get_data__impl_(this) * _ULong___get_data__impl_(tmp0_times_0)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))

def ULong__times_impl_2(this, other):
    return _ULong___init__impl_((_ULong___get_data__impl_(this) * _ULong___get_data__impl_(other)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))

def ULong__div_impl(this, other):
    tmp0_div_0 = _ULong___init__impl_((_UByte___get_data__impl_(other) & 255).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    return ulongDivide(this, tmp0_div_0)

def ULong__div_impl_0(this, other):
    tmp0_div_0 = _ULong___init__impl_((_UShort___get_data__impl_(other) & 65535).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    return ulongDivide(this, tmp0_div_0)

def ULong__div_impl_1(this, other):
    tmp0_div_0 = _ULong___init__impl_((_UInt___get_data__impl_(other) & 4294967295).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    return ulongDivide(this, tmp0_div_0)

def ULong__div_impl_2(this, other):
    return ulongDivide(this, other)

def ULong__rem_impl(this, other):
    tmp0_rem_0 = _ULong___init__impl_((_UByte___get_data__impl_(other) & 255).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    return ulongRemainder(this, tmp0_rem_0)

def ULong__rem_impl_0(this, other):
    tmp0_rem_0 = _ULong___init__impl_((_UShort___get_data__impl_(other) & 65535).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    return ulongRemainder(this, tmp0_rem_0)

def ULong__rem_impl_1(this, other):
    tmp0_rem_0 = _ULong___init__impl_((_UInt___get_data__impl_(other) & 4294967295).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    return ulongRemainder(this, tmp0_rem_0)

def ULong__rem_impl_2(this, other):
    return ulongRemainder(this, other)

def ULong__floorDiv_impl(this, other):
    tmp0_floorDiv_0 = _ULong___init__impl_((_UByte___get_data__impl_(other) & 255).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    return ulongDivide(this, tmp0_floorDiv_0)

def ULong__floorDiv_impl_0(this, other):
    tmp0_floorDiv_0 = _ULong___init__impl_((_UShort___get_data__impl_(other) & 65535).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    return ulongDivide(this, tmp0_floorDiv_0)

def ULong__floorDiv_impl_1(this, other):
    tmp0_floorDiv_0 = _ULong___init__impl_((_UInt___get_data__impl_(other) & 4294967295).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    return ulongDivide(this, tmp0_floorDiv_0)

def ULong__floorDiv_impl_2(this, other):
    return ulongDivide(this, other)

def ULong__mod_impl(this, other):
    tmp0_mod_0 = _ULong___init__impl_((_UByte___get_data__impl_(other) & 255).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    tmp2_toUByte_0 = ulongRemainder(this, tmp0_mod_0)
    tmp1_toUByte_0 = _ULong___get_data__impl_(tmp2_toUByte_0)
    return _UByte___init__impl_(tmp1_toUByte_0.__add__(0x80).__and__(0xff).__sub__(0x80))

def ULong__mod_impl_0(this, other):
    tmp0_mod_0 = _ULong___init__impl_((_UShort___get_data__impl_(other) & 65535).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    tmp2_toUShort_0 = ulongRemainder(this, tmp0_mod_0)
    tmp1_toUShort_0 = _ULong___get_data__impl_(tmp2_toUShort_0)
    return _UShort___init__impl_(tmp1_toUShort_0.__add__(0x8000).__and__(0xffff).__sub__(0x8000))

def ULong__mod_impl_1(this, other):
    tmp0_mod_0 = _ULong___init__impl_((_UInt___get_data__impl_(other) & 4294967295).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    tmp2_toUInt_0 = ulongRemainder(this, tmp0_mod_0)
    tmp1_toUInt_0 = _ULong___get_data__impl_(tmp2_toUInt_0)
    return _UInt___init__impl_(tmp1_toUInt_0.__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))

def ULong__mod_impl_2(this, other):
    return ulongRemainder(this, other)

def ULong__inc_impl(this):
    return _ULong___init__impl_((_ULong___get_data__impl_(this) + 1).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))

def ULong__dec_impl(this):
    return _ULong___init__impl_((_ULong___get_data__impl_(this) - 1).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))

def ULong__rangeTo_impl(this, other):
    return ULongRange(this, other)

def ULong__shl_impl(this, bitCount):
    return _ULong___init__impl_((_ULong___get_data__impl_(this) << bitCount).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))

def ULong__shr_impl(this, bitCount):
    return _ULong___init__impl_(((_ULong___get_data__impl_(this) & 0xffff_ffff_ffff_ffff) >> bitCount).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))

def ULong__and_impl(this, other):
    return _ULong___init__impl_((_ULong___get_data__impl_(this) & _ULong___get_data__impl_(other)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))

def ULong__or_impl(this, other):
    return _ULong___init__impl_((_ULong___get_data__impl_(this) | _ULong___get_data__impl_(other)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))

def ULong__xor_impl(this, other):
    return _ULong___init__impl_((_ULong___get_data__impl_(this) ^ _ULong___get_data__impl_(other)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))

def ULong__inv_impl(this):
    return _ULong___init__impl_(~_ULong___get_data__impl_(this))

def ULong__toByte_impl(this):
    return _ULong___get_data__impl_(this).__add__(0x80).__and__(0xff).__sub__(0x80)

def ULong__toShort_impl(this):
    return _ULong___get_data__impl_(this).__add__(0x8000).__and__(0xffff).__sub__(0x8000)

def ULong__toInt_impl(this):
    return _ULong___get_data__impl_(this).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)

def ULong__toLong_impl(this):
    return _ULong___get_data__impl_(this)

def ULong__toUByte_impl(this):
    tmp0_toUByte_0 = _ULong___get_data__impl_(this)
    return _UByte___init__impl_(tmp0_toUByte_0.__add__(0x80).__and__(0xff).__sub__(0x80))

def ULong__toUShort_impl(this):
    tmp0_toUShort_0 = _ULong___get_data__impl_(this)
    return _UShort___init__impl_(tmp0_toUShort_0.__add__(0x8000).__and__(0xffff).__sub__(0x8000))

def ULong__toUInt_impl(this):
    tmp0_toUInt_0 = _ULong___get_data__impl_(this)
    return _UInt___init__impl_(tmp0_toUInt_0.__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))

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
    if not visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
        return False
    
    tmp0_other_with_cast = (unboxIntrinsic(other)) if (visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean) else (THROW_CCE())
    if not (this.data == tmp0_other_with_cast.data):
        return False
    
    return True

class ULong:
    def __init__(self, data):
        Companion_getInstance_7()
        self.data = data
    
    def compareTo_djarz7_k_(self, other):
        return ULong__compareTo_impl_2(unboxIntrinsic(self), other)
    
    def compareTo_2c5_k_(self, other):
        return ULong__compareTo_impl_3(self, other)
    
    def toString(self):
        return ULong__toString_impl(unboxIntrinsic(self))
    
    def hashCode(self):
        return ULong__hashCode_impl(unboxIntrinsic(self))
    
    def equals(self, other):
        return ULong__equals_impl(unboxIntrinsic(self), other)
    

def toULong():
    return _ULong___init__impl_(self)

def toULong_0():
    return _ULong___init__impl_(self)

def toULong_1():
    return doubleToULong(self)

def toULong_2():
    return doubleToULong(kotlin_Double(self))

def toULong_3():
    return _ULong___init__impl_(self)

def toULong_4():
    return _ULong___init__impl_(self)

def _get_array__1(_this):
    return _this.array

def _set_index__1(_this, _set___):
    _this.index = _set___

def _get_index__1(_this):
    return _this.index

def _ULongArray___init__impl_(storage):
    return kotlin_ULongArray(storage)

def _ULongArray___get_storage__impl_(this):
    return this.storage

def _ULongArray___init__impl__0(size):
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
    return Iterator_1(_ULongArray___get_storage__impl_(this))

class Iterator_1:
    def __init__(self, array):
        super()
        self.array = array
        self.index = 0
    
    def hasNext_0_k_(self):
        return self.index < len(self.array)
    
    def nextULong_sha8jq_k_(self):
        if self.index < len(self.array):
            tmp0_this = self
            tmp1 = tmp0_this.index
            tmp0_this.index = (tmp1 + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
            tmp0_toULong_0 = self.array[tmp1]
            tmp = _ULong___init__impl_(tmp0_toULong_0)
        else:
            raise NoSuchElementException_init__Create__0(self.index.toString())
        
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
    if not visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
        return False
    
    tmp = _ULongArray___get_storage__impl_(this)
    return contains_2(_ULong___get_data__impl_(element))

def ULongArray__contains_impl_0(this, element):
    if not visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
        return False
    
    tmp = unboxIntrinsic(this)
    return ULongArray__contains_impl(tmp, (unboxIntrinsic(element)) if (visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean) else (THROW_CCE()))

def ULongArray__containsAll_impl(this, elements):
    while True:
        tmp0_all_0 = (kotlin_collections_Collection___(elements)) if (isInterface(elements, jsClass())) else (THROW_CCE())
        if isInterface(tmp0_all_0, jsClass()):
            tmp = kotlin_collections_Collection_kotlin_Any__(tmp0_all_0).isEmpty_0_k_()
        elif True:
            tmp = False
        
        if tmp:
            tmp_ret_0 = True
            break
        
        tmp0_iterator_1 = tmp0_all_0.iterator_0_k_()
        while tmp0_iterator_1.hasNext_0_k_():
            element_2 = tmp0_iterator_1.next_0_k_()
            if visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
                tmp = _ULongArray___get_storage__impl_(this)
                tmp0_toLong_0_4 = unboxIntrinsic(element_2)
                tmp = contains_2(_ULong___get_data__impl_(tmp0_toLong_0_4))
            elif True:
                tmp = False
            
            if not tmp:
                tmp_ret_0 = False
                break
            
        
        tmp_ret_0 = True
        if False:
            break
        
    
    return tmp_ret_0

def ULongArray__containsAll_impl_0(this, elements):
    return ULongArray__containsAll_impl(unboxIntrinsic(this), elements)

def ULongArray__isEmpty_impl(this):
    return len(_ULongArray___get_storage__impl_(this)) == 0

def ULongArray__toString_impl(this):
    return (str('ULongArray(storage=') + str(toString_0(this.storage))) + str(')')

def ULongArray__hashCode_impl(this):
    return hashCode(this.storage)

def ULongArray__equals_impl(this, other):
    if not visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
        return False
    
    tmp0_other_with_cast = (unboxIntrinsic(other)) if (visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean) else (THROW_CCE())
    if not (this.storage == tmp0_other_with_cast.storage):
        return False
    
    return True

class ULongArray:
    def __init__(self, storage):
        self.storage = storage
    
    def _get_size__0_k_(self):
        return _ULongArray___get_size__impl_(unboxIntrinsic(self))
    
    def iterator_0_k_(self):
        return ULongArray__iterator_impl(unboxIntrinsic(self))
    
    def contains_djarz7_k_(self, element):
        return ULongArray__contains_impl(unboxIntrinsic(self), element)
    
    def contains_2bq_k_(self, element):
        return ULongArray__contains_impl_0(self, element)
    
    def containsAll_wotoar_k_(self, elements):
        return ULongArray__containsAll_impl(unboxIntrinsic(self), elements)
    
    def containsAll_dxd4eo_k_(self, elements):
        return ULongArray__containsAll_impl_0(self, elements)
    
    def isEmpty_0_k_(self):
        return ULongArray__isEmpty_impl(unboxIntrinsic(self))
    
    def toString(self):
        return ULongArray__toString_impl(unboxIntrinsic(self))
    
    def hashCode(self):
        return ULongArray__hashCode_impl(unboxIntrinsic(self))
    
    def equals(self, other):
        return ULongArray__equals_impl(unboxIntrinsic(self), other)
    

class Companion_9:
    def __init__(self):
        global Companion_instance
        Companion_instance = self
        tmp = self
        Companion_getInstance_7()
        tmp = _ULong___init__impl_(Long(-1, -1))
        Companion_getInstance_7()
        tmp.EMPTY = ULongRange(tmp, _ULong___init__impl_(Long(0, 0)))
    
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

class ULongRange:
    def __init__(self, start, endInclusive):
        Companion_getInstance_8()
        super(start, endInclusive, 1)
    
    def _get_start__sha8jq_k_(self):
        return self._get_first__sha8jq_k_()
    
    def _get_start__0_k_(self):
        return boxIntrinsic(self._get_start__sha8jq_k_())
    
    def _get_endInclusive__sha8jq_k_(self):
        return self._get_last__sha8jq_k_()
    
    def _get_endInclusive__0_k_(self):
        return boxIntrinsic(self._get_endInclusive__sha8jq_k_())
    
    def contains_djarz7_k_(self, value):
        tmp0_compareTo_0 = self._get_first__sha8jq_k_()
        if ulongCompare(_ULong___get_data__impl_(tmp0_compareTo_0), _ULong___get_data__impl_(value)) <= 0:
            tmp1_compareTo_0 = self._get_last__sha8jq_k_()
            tmp = ulongCompare(_ULong___get_data__impl_(value), _ULong___get_data__impl_(tmp1_compareTo_0)) <= 0
        elif True:
            tmp = False
        
        return tmp
    
    def contains_2c5_k_(self, value):
        return self.contains_djarz7_k_((unboxIntrinsic(value)) if (visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean) else (THROW_CCE()))
    
    def isEmpty_0_k_(self):
        tmp0_compareTo_0 = self._get_first__sha8jq_k_()
        tmp1_compareTo_0 = self._get_last__sha8jq_k_()
        return ulongCompare(_ULong___get_data__impl_(tmp0_compareTo_0), _ULong___get_data__impl_(tmp1_compareTo_0)) > 0
    
    def equals(self, other):
        if visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
            tmp = (True) if ((kotlin_ranges_ULongRange(other).isEmpty_0_k_()) if (self.isEmpty_0_k_()) else (False)) else ((boxIntrinsic(self._get_last__sha8jq_k_()) == boxIntrinsic(kotlin_ranges_ULongRange(other)._get_last__sha8jq_k_())) if (boxIntrinsic(self._get_first__sha8jq_k_()) == boxIntrinsic(kotlin_ranges_ULongRange(other)._get_first__sha8jq_k_())) else (False))
        elif True:
            tmp = False
        
        return tmp
    
    def hashCode(self):
        if self.isEmpty_0_k_():
            tmp = -1
        else:
            tmp1_xor_0 = self._get_first__sha8jq_k_()
            tmp0_shr_0 = self._get_first__sha8jq_k_()
            tmp2_xor_0 = _ULong___init__impl_(((_ULong___get_data__impl_(tmp0_shr_0) & 0xffff_ffff_ffff_ffff) >> 32).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
            tmp3_toInt_0 = _ULong___init__impl_((_ULong___get_data__impl_(tmp1_xor_0) ^ _ULong___get_data__impl_(tmp2_xor_0)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
            tmp = imul(31, _ULong___get_data__impl_(tmp3_toInt_0).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))
            tmp5_xor_0 = self._get_last__sha8jq_k_()
            tmp4_shr_0 = self._get_last__sha8jq_k_()
            tmp6_xor_0 = _ULong___init__impl_(((_ULong___get_data__impl_(tmp4_shr_0) & 0xffff_ffff_ffff_ffff) >> 32).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
            tmp7_toInt_0 = _ULong___init__impl_((_ULong___get_data__impl_(tmp5_xor_0) ^ _ULong___get_data__impl_(tmp6_xor_0)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
            tmp = (tmp + _ULong___get_data__impl_(tmp7_toInt_0).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
        
        return tmp
    
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
    

class Companion_10:
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

class ULongProgression:
    def __init__(self, start, endInclusive, step):
        Companion_getInstance_9()
        if step == 0:
            raise IllegalArgumentException_init__Create__0('Step must be non-zero.')
        
        Companion_getInstance_19()
        if step == -9223372036854775808:
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
        return ULongProgressionIterator(self.first, self.last, self.step)
    
    def isEmpty_0_k_(self):
        if self.step.compareTo_wiekkq_k_(0) > 0:
            tmp0_compareTo_0 = self.first
            tmp1_compareTo_0 = self.last
            tmp = ulongCompare(_ULong___get_data__impl_(tmp0_compareTo_0), _ULong___get_data__impl_(tmp1_compareTo_0)) > 0
        else:
            tmp2_compareTo_0 = self.first
            tmp3_compareTo_0 = self.last
            tmp = ulongCompare(_ULong___get_data__impl_(tmp2_compareTo_0), _ULong___get_data__impl_(tmp3_compareTo_0)) < 0
        
        return tmp
    
    def equals(self, other):
        if visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
            tmp = (True) if ((kotlin_ranges_ULongProgression(other).isEmpty_0_k_()) if (self.isEmpty_0_k_()) else (False)) else ((self.step == kotlin_ranges_ULongProgression(other).step) if ((boxIntrinsic(self.last) == boxIntrinsic(kotlin_ranges_ULongProgression(other).last)) if (boxIntrinsic(self.first) == boxIntrinsic(kotlin_ranges_ULongProgression(other).first)) else (False)) else (False))
        elif True:
            tmp = False
        
        return tmp
    
    def hashCode(self):
        if self.isEmpty_0_k_():
            tmp = -1
        else:
            tmp1_xor_0 = self.first
            tmp0_shr_0 = self.first
            tmp2_xor_0 = _ULong___init__impl_(((_ULong___get_data__impl_(tmp0_shr_0) & 0xffff_ffff_ffff_ffff) >> 32).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
            tmp3_toInt_0 = _ULong___init__impl_((_ULong___get_data__impl_(tmp1_xor_0) ^ _ULong___get_data__impl_(tmp2_xor_0)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
            tmp = imul(31, _ULong___get_data__impl_(tmp3_toInt_0).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))
            tmp5_xor_0 = self.last
            tmp4_shr_0 = self.last
            tmp6_xor_0 = _ULong___init__impl_(((_ULong___get_data__impl_(tmp4_shr_0) & 0xffff_ffff_ffff_ffff) >> 32).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
            tmp7_toInt_0 = _ULong___init__impl_((_ULong___get_data__impl_(tmp5_xor_0) ^ _ULong___get_data__impl_(tmp6_xor_0)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
            tmp = (imul(31, (tmp + _ULong___get_data__impl_(tmp7_toInt_0).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)) + (self.step ^ ((self.step & 0xffff_ffff_ffff_ffff) >> 32).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
        
        return tmp
    
    def toString(self):
        return ((((str(boxIntrinsic(self.first)) + str('..')) + str(boxIntrinsic(self.last))) + str(' step ')) + str(self.step)) if (self.step.compareTo_wiekkq_k_(0) > 0) else ((((str(boxIntrinsic(self.first)) + str(' downTo ')) + str(boxIntrinsic(self.last))) + str(' step ')) + str((-self.step).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)))
    

def _get_finalElement__0(_this):
    return _this.finalElement

def _set_hasNext__0(_this, _set___):
    _this.hasNext = _set___

def _get_hasNext__0(_this):
    return _this.hasNext

def _get_step__0(_this):
    return _this.step

def _set_next__0(_this, _set___):
    _this.next = _set___

def _get_next__0(_this):
    return _this.next

class ULongProgressionIterator:
    def __init__(self, first, last, step):
        super()
        self.finalElement = last
        tmp = self
        if step.compareTo_wiekkq_k_(0) > 0:
            tmp = ulongCompare(_ULong___get_data__impl_(first), _ULong___get_data__impl_(last)) <= 0
        else:
            tmp = ulongCompare(_ULong___get_data__impl_(first), _ULong___get_data__impl_(last)) >= 0
        
        tmp.hasNext = tmp
        tmp = self
        tmp.step = _ULong___init__impl_(step)
        self.next = (first) if (self.hasNext) else (self.finalElement)
    
    def hasNext_0_k_(self):
        return self.hasNext
    
    def nextULong_sha8jq_k_(self):
        value = self.next
        if boxIntrinsic(value) == boxIntrinsic(self.finalElement):
            if not self.hasNext:
                raise NoSuchElementException_init__Create_()
            
            self.hasNext = False
        else:
            tmp0_this = self
            tmp = tmp0_this
            tmp0_plus_0 = tmp0_this.next
            tmp1_plus_0 = self.step
            tmp.next = _ULong___init__impl_((_ULong___get_data__impl_(tmp0_plus_0) + _ULong___get_data__impl_(tmp1_plus_0)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
        
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
        if uintCompare(_UInt___get_data__impl_(start), _UInt___get_data__impl_(end)) >= 0:
            tmp = end
        elif True:
            tmp0_minus_0 = differenceModulo(end, start, _UInt___init__impl_(step))
            tmp = _UInt___init__impl_((_UInt___get_data__impl_(end) - _UInt___get_data__impl_(tmp0_minus_0)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))
        
        tmp = tmp
    elif step < 0:
        if uintCompare(_UInt___get_data__impl_(start), _UInt___get_data__impl_(end)) <= 0:
            tmp = end
        elif True:
            tmp1_toUInt_0 = (-step).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
            tmp2_plus_0 = differenceModulo(start, end, _UInt___init__impl_(tmp1_toUInt_0))
            tmp = _UInt___init__impl_((_UInt___get_data__impl_(end) + _UInt___get_data__impl_(tmp2_plus_0)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))
        
        tmp = tmp
    else:
        raise IllegalArgumentException_init__Create__0('Step is zero.')
    
    return tmp

def getProgressionLastElement_0(start, end, step):
    if step.compareTo_wiekkq_k_(0) > 0:
        if ulongCompare(_ULong___get_data__impl_(start), _ULong___get_data__impl_(end)) >= 0:
            tmp = end
        elif True:
            tmp0_minus_0 = differenceModulo_0(end, start, _ULong___init__impl_(step))
            tmp = _ULong___init__impl_((_ULong___get_data__impl_(end) - _ULong___get_data__impl_(tmp0_minus_0)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
        
        tmp = tmp
    elif step.compareTo_wiekkq_k_(0) < 0:
        if ulongCompare(_ULong___get_data__impl_(start), _ULong___get_data__impl_(end)) <= 0:
            tmp = end
        elif True:
            tmp1_toULong_0 = (-step).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)
            tmp2_plus_0 = differenceModulo_0(start, end, _ULong___init__impl_(tmp1_toULong_0))
            tmp = _ULong___init__impl_((_ULong___get_data__impl_(end) + _ULong___get_data__impl_(tmp2_plus_0)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
        
        tmp = tmp
    else:
        raise IllegalArgumentException_init__Create__0('Step is zero.')
    
    return tmp

def differenceModulo(a, b, c):
    ac = uintRemainder(a, c)
    bc = uintRemainder(b, c)
    if uintCompare(_UInt___get_data__impl_(ac), _UInt___get_data__impl_(bc)) >= 0:
        tmp = _UInt___init__impl_((_UInt___get_data__impl_(ac) - _UInt___get_data__impl_(bc)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))
    elif True:
        tmp0_plus_0 = _UInt___init__impl_((_UInt___get_data__impl_(ac) - _UInt___get_data__impl_(bc)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))
        tmp = _UInt___init__impl_((_UInt___get_data__impl_(tmp0_plus_0) + _UInt___get_data__impl_(c)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))
    
    return tmp

def differenceModulo_0(a, b, c):
    ac = ulongRemainder(a, c)
    bc = ulongRemainder(b, c)
    if ulongCompare(_ULong___get_data__impl_(ac), _ULong___get_data__impl_(bc)) >= 0:
        tmp = _ULong___init__impl_((_ULong___get_data__impl_(ac) - _ULong___get_data__impl_(bc)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    elif True:
        tmp0_plus_0 = _ULong___init__impl_((_ULong___get_data__impl_(ac) - _ULong___get_data__impl_(bc)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
        tmp = _ULong___init__impl_((_ULong___get_data__impl_(tmp0_plus_0) + _ULong___get_data__impl_(c)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    
    return tmp

def _UShort___init__impl_(data):
    return kotlin_UShort(data)

def _UShort___get_data__impl_(this):
    return this.data

class Companion_11:
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
    tmp = _UShort___get_data__impl_(this) & 65535
    return compareTo_0(tmp, _UByte___get_data__impl_(other) & 255)

def UShort__compareTo_impl_0(this, other):
    tmp = _UShort___get_data__impl_(this) & 65535
    return compareTo_0(tmp, _UShort___get_data__impl_(other) & 65535)

def UShort__compareTo_impl_1(this, other):
    tmp = unboxIntrinsic(this)
    return UShort__compareTo_impl_0(tmp, (unboxIntrinsic(other)) if (visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean) else (THROW_CCE()))

def UShort__compareTo_impl_2(this, other):
    tmp0_compareTo_0 = _UInt___init__impl_(_UShort___get_data__impl_(this) & 65535)
    return uintCompare(_UInt___get_data__impl_(tmp0_compareTo_0), _UInt___get_data__impl_(other))

def UShort__compareTo_impl_3(this, other):
    tmp0_compareTo_0 = _ULong___init__impl_((_UShort___get_data__impl_(this) & 65535).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    return ulongCompare(_ULong___get_data__impl_(tmp0_compareTo_0), _ULong___get_data__impl_(other))

def UShort__plus_impl(this, other):
    tmp0_plus_0 = _UInt___init__impl_(_UShort___get_data__impl_(this) & 65535)
    tmp1_plus_0 = _UInt___init__impl_(_UByte___get_data__impl_(other) & 255)
    return _UInt___init__impl_((_UInt___get_data__impl_(tmp0_plus_0) + _UInt___get_data__impl_(tmp1_plus_0)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))

def UShort__plus_impl_0(this, other):
    tmp0_plus_0 = _UInt___init__impl_(_UShort___get_data__impl_(this) & 65535)
    tmp1_plus_0 = _UInt___init__impl_(_UShort___get_data__impl_(other) & 65535)
    return _UInt___init__impl_((_UInt___get_data__impl_(tmp0_plus_0) + _UInt___get_data__impl_(tmp1_plus_0)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))

def UShort__plus_impl_1(this, other):
    tmp0_plus_0 = _UInt___init__impl_(_UShort___get_data__impl_(this) & 65535)
    return _UInt___init__impl_((_UInt___get_data__impl_(tmp0_plus_0) + _UInt___get_data__impl_(other)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))

def UShort__plus_impl_2(this, other):
    tmp0_plus_0 = _ULong___init__impl_((_UShort___get_data__impl_(this) & 65535).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    return _ULong___init__impl_((_ULong___get_data__impl_(tmp0_plus_0) + _ULong___get_data__impl_(other)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))

def UShort__minus_impl(this, other):
    tmp0_minus_0 = _UInt___init__impl_(_UShort___get_data__impl_(this) & 65535)
    tmp1_minus_0 = _UInt___init__impl_(_UByte___get_data__impl_(other) & 255)
    return _UInt___init__impl_((_UInt___get_data__impl_(tmp0_minus_0) - _UInt___get_data__impl_(tmp1_minus_0)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))

def UShort__minus_impl_0(this, other):
    tmp0_minus_0 = _UInt___init__impl_(_UShort___get_data__impl_(this) & 65535)
    tmp1_minus_0 = _UInt___init__impl_(_UShort___get_data__impl_(other) & 65535)
    return _UInt___init__impl_((_UInt___get_data__impl_(tmp0_minus_0) - _UInt___get_data__impl_(tmp1_minus_0)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))

def UShort__minus_impl_1(this, other):
    tmp0_minus_0 = _UInt___init__impl_(_UShort___get_data__impl_(this) & 65535)
    return _UInt___init__impl_((_UInt___get_data__impl_(tmp0_minus_0) - _UInt___get_data__impl_(other)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))

def UShort__minus_impl_2(this, other):
    tmp0_minus_0 = _ULong___init__impl_((_UShort___get_data__impl_(this) & 65535).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    return _ULong___init__impl_((_ULong___get_data__impl_(tmp0_minus_0) - _ULong___get_data__impl_(other)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))

def UShort__times_impl(this, other):
    tmp0_times_0 = _UInt___init__impl_(_UShort___get_data__impl_(this) & 65535)
    tmp1_times_0 = _UInt___init__impl_(_UByte___get_data__impl_(other) & 255)
    return _UInt___init__impl_(imul(_UInt___get_data__impl_(tmp0_times_0), _UInt___get_data__impl_(tmp1_times_0)))

def UShort__times_impl_0(this, other):
    tmp0_times_0 = _UInt___init__impl_(_UShort___get_data__impl_(this) & 65535)
    tmp1_times_0 = _UInt___init__impl_(_UShort___get_data__impl_(other) & 65535)
    return _UInt___init__impl_(imul(_UInt___get_data__impl_(tmp0_times_0), _UInt___get_data__impl_(tmp1_times_0)))

def UShort__times_impl_1(this, other):
    tmp0_times_0 = _UInt___init__impl_(_UShort___get_data__impl_(this) & 65535)
    return _UInt___init__impl_(imul(_UInt___get_data__impl_(tmp0_times_0), _UInt___get_data__impl_(other)))

def UShort__times_impl_2(this, other):
    tmp0_times_0 = _ULong___init__impl_((_UShort___get_data__impl_(this) & 65535).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    return _ULong___init__impl_((_ULong___get_data__impl_(tmp0_times_0) * _ULong___get_data__impl_(other)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))

def UShort__div_impl(this, other):
    tmp0_div_0 = _UInt___init__impl_(_UShort___get_data__impl_(this) & 65535)
    tmp1_div_0 = _UInt___init__impl_(_UByte___get_data__impl_(other) & 255)
    return uintDivide(tmp0_div_0, tmp1_div_0)

def UShort__div_impl_0(this, other):
    tmp0_div_0 = _UInt___init__impl_(_UShort___get_data__impl_(this) & 65535)
    tmp1_div_0 = _UInt___init__impl_(_UShort___get_data__impl_(other) & 65535)
    return uintDivide(tmp0_div_0, tmp1_div_0)

def UShort__div_impl_1(this, other):
    tmp0_div_0 = _UInt___init__impl_(_UShort___get_data__impl_(this) & 65535)
    return uintDivide(tmp0_div_0, other)

def UShort__div_impl_2(this, other):
    tmp0_div_0 = _ULong___init__impl_((_UShort___get_data__impl_(this) & 65535).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    return ulongDivide(tmp0_div_0, other)

def UShort__rem_impl(this, other):
    tmp0_rem_0 = _UInt___init__impl_(_UShort___get_data__impl_(this) & 65535)
    tmp1_rem_0 = _UInt___init__impl_(_UByte___get_data__impl_(other) & 255)
    return uintRemainder(tmp0_rem_0, tmp1_rem_0)

def UShort__rem_impl_0(this, other):
    tmp0_rem_0 = _UInt___init__impl_(_UShort___get_data__impl_(this) & 65535)
    tmp1_rem_0 = _UInt___init__impl_(_UShort___get_data__impl_(other) & 65535)
    return uintRemainder(tmp0_rem_0, tmp1_rem_0)

def UShort__rem_impl_1(this, other):
    tmp0_rem_0 = _UInt___init__impl_(_UShort___get_data__impl_(this) & 65535)
    return uintRemainder(tmp0_rem_0, other)

def UShort__rem_impl_2(this, other):
    tmp0_rem_0 = _ULong___init__impl_((_UShort___get_data__impl_(this) & 65535).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    return ulongRemainder(tmp0_rem_0, other)

def UShort__floorDiv_impl(this, other):
    tmp0_floorDiv_0 = _UInt___init__impl_(_UShort___get_data__impl_(this) & 65535)
    tmp1_floorDiv_0 = _UInt___init__impl_(_UByte___get_data__impl_(other) & 255)
    return uintDivide(tmp0_floorDiv_0, tmp1_floorDiv_0)

def UShort__floorDiv_impl_0(this, other):
    tmp0_floorDiv_0 = _UInt___init__impl_(_UShort___get_data__impl_(this) & 65535)
    tmp1_floorDiv_0 = _UInt___init__impl_(_UShort___get_data__impl_(other) & 65535)
    return uintDivide(tmp0_floorDiv_0, tmp1_floorDiv_0)

def UShort__floorDiv_impl_1(this, other):
    tmp0_floorDiv_0 = _UInt___init__impl_(_UShort___get_data__impl_(this) & 65535)
    return uintDivide(tmp0_floorDiv_0, other)

def UShort__floorDiv_impl_2(this, other):
    tmp0_floorDiv_0 = _ULong___init__impl_((_UShort___get_data__impl_(this) & 65535).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    return ulongDivide(tmp0_floorDiv_0, other)

def UShort__mod_impl(this, other):
    tmp0_mod_0 = _UInt___init__impl_(_UShort___get_data__impl_(this) & 65535)
    tmp1_mod_0 = _UInt___init__impl_(_UByte___get_data__impl_(other) & 255)
    tmp2_toUByte_0 = uintRemainder(tmp0_mod_0, tmp1_mod_0)
    tmp0_toUByte_0_1 = _UInt___get_data__impl_(tmp2_toUByte_0)
    return _UByte___init__impl_(tmp0_toUByte_0_1.__add__(0x80).__and__(0xff).__sub__(0x80))

def UShort__mod_impl_0(this, other):
    tmp0_mod_0 = _UInt___init__impl_(_UShort___get_data__impl_(this) & 65535)
    tmp1_mod_0 = _UInt___init__impl_(_UShort___get_data__impl_(other) & 65535)
    tmp2_toUShort_0 = uintRemainder(tmp0_mod_0, tmp1_mod_0)
    tmp0_toUShort_0_1 = _UInt___get_data__impl_(tmp2_toUShort_0)
    return _UShort___init__impl_(tmp0_toUShort_0_1.__add__(0x8000).__and__(0xffff).__sub__(0x8000))

def UShort__mod_impl_1(this, other):
    tmp0_mod_0 = _UInt___init__impl_(_UShort___get_data__impl_(this) & 65535)
    return uintRemainder(tmp0_mod_0, other)

def UShort__mod_impl_2(this, other):
    tmp0_mod_0 = _ULong___init__impl_((_UShort___get_data__impl_(this) & 65535).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    return ulongRemainder(tmp0_mod_0, other)

def UShort__inc_impl(this):
    return _UShort___init__impl_((_UShort___get_data__impl_(this) + 1).__add__(0x8000).__and__(0xffff).__sub__(0x8000))

def UShort__dec_impl(this):
    return _UShort___init__impl_((_UShort___get_data__impl_(this) - 1).__add__(0x8000).__and__(0xffff).__sub__(0x8000))

def UShort__rangeTo_impl(this, other):
    tmp = _UInt___init__impl_(_UShort___get_data__impl_(this) & 65535)
    return UIntRange(tmp, _UInt___init__impl_(_UShort___get_data__impl_(other) & 65535))

def UShort__and_impl(this, other):
    tmp0_and_0 = _UShort___get_data__impl_(this)
    tmp1_and_0 = _UShort___get_data__impl_(other)
    return _UShort___init__impl_((tmp0_and_0 & tmp1_and_0).__add__(0x8000).__and__(0xffff).__sub__(0x8000))

def UShort__or_impl(this, other):
    tmp0_or_0 = _UShort___get_data__impl_(this)
    tmp1_or_0 = _UShort___get_data__impl_(other)
    return _UShort___init__impl_((tmp0_or_0 | tmp1_or_0).__add__(0x8000).__and__(0xffff).__sub__(0x8000))

def UShort__xor_impl(this, other):
    tmp0_xor_0 = _UShort___get_data__impl_(this)
    tmp1_xor_0 = _UShort___get_data__impl_(other)
    return _UShort___init__impl_((tmp0_xor_0 ^ tmp1_xor_0).__add__(0x8000).__and__(0xffff).__sub__(0x8000))

def UShort__inv_impl(this):
    tmp0_inv_0 = _UShort___get_data__impl_(this)
    return _UShort___init__impl_((~tmp0_inv_0).__add__(0x8000).__and__(0xffff).__sub__(0x8000))

def UShort__toByte_impl(this):
    return _UShort___get_data__impl_(this).__add__(0x80).__and__(0xff).__sub__(0x80)

def UShort__toShort_impl(this):
    return _UShort___get_data__impl_(this)

def UShort__toInt_impl(this):
    return _UShort___get_data__impl_(this) & 65535

def UShort__toLong_impl(this):
    return (_UShort___get_data__impl_(this) & 65535).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)

def UShort__toUByte_impl(this):
    tmp0_toUByte_0 = _UShort___get_data__impl_(this)
    return _UByte___init__impl_(tmp0_toUByte_0.__add__(0x80).__and__(0xff).__sub__(0x80))

def UShort__toUShort_impl(this):
    return this

def UShort__toUInt_impl(this):
    return _UInt___init__impl_(_UShort___get_data__impl_(this) & 65535)

def UShort__toULong_impl(this):
    return _ULong___init__impl_((_UShort___get_data__impl_(this) & 65535).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))

def UShort__toFloat_impl(this):
    return kotlin_Float(_UShort___get_data__impl_(this) & 65535)

def UShort__toDouble_impl(this):
    return kotlin_Double(_UShort___get_data__impl_(this) & 65535)

def UShort__toString_impl(this):
    return (_UShort___get_data__impl_(this) & 65535).toString()

def UShort__hashCode_impl(this):
    return this.data

def UShort__equals_impl(this, other):
    if not visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
        return False
    
    tmp0_other_with_cast = (unboxIntrinsic(other)) if (visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean) else (THROW_CCE())
    if not (this.data == tmp0_other_with_cast.data):
        return False
    
    return True

class UShort:
    def __init__(self, data):
        Companion_getInstance_10()
        self.data = data
    
    def compareTo_6go47f_k_(self, other):
        return UShort__compareTo_impl_0(unboxIntrinsic(self), other)
    
    def compareTo_2c5_k_(self, other):
        return UShort__compareTo_impl_1(self, other)
    
    def toString(self):
        return UShort__toString_impl(unboxIntrinsic(self))
    
    def hashCode(self):
        return UShort__hashCode_impl(unboxIntrinsic(self))
    
    def equals(self, other):
        return UShort__equals_impl(unboxIntrinsic(self), other)
    

def toUShort():
    return _UShort___init__impl_(self.__add__(0x8000).__and__(0xffff).__sub__(0x8000))

def toUShort_0():
    return _UShort___init__impl_(self.__add__(0x8000).__and__(0xffff).__sub__(0x8000))

def toUShort_1():
    return _UShort___init__impl_(self)

def _get_array__2(_this):
    return _this.array

def _set_index__2(_this, _set___):
    _this.index = _set___

def _get_index__2(_this):
    return _this.index

def _UShortArray___init__impl_(storage):
    return kotlin_UShortArray(storage)

def _UShortArray___get_storage__impl_(this):
    return this.storage

def _UShortArray___init__impl__0(size):
    tmp = _UShortArray___init__impl_(visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_int16Array_visibility_public_modality_FINAL_____arg0_kotlin_Any___returnType_kotlin_Any_)
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
    return Iterator_2(_UShortArray___get_storage__impl_(this))

class Iterator_2:
    def __init__(self, array):
        super()
        self.array = array
        self.index = 0
    
    def hasNext_0_k_(self):
        return self.index < len(self.array)
    
    def nextUShort_um6tma_k_(self):
        if self.index < len(self.array):
            tmp0_this = self
            tmp1 = tmp0_this.index
            tmp0_this.index = (tmp1 + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
            tmp0_toUShort_0 = self.array[tmp1]
            tmp = _UShort___init__impl_(tmp0_toUShort_0)
        else:
            raise NoSuchElementException_init__Create__0(self.index.toString())
        
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
    if not visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
        return False
    
    tmp = _UShortArray___get_storage__impl_(this)
    return contains_0(_UShort___get_data__impl_(element))

def UShortArray__contains_impl_0(this, element):
    if not visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
        return False
    
    tmp = unboxIntrinsic(this)
    return UShortArray__contains_impl(tmp, (unboxIntrinsic(element)) if (visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean) else (THROW_CCE()))

def UShortArray__containsAll_impl(this, elements):
    while True:
        tmp0_all_0 = (kotlin_collections_Collection___(elements)) if (isInterface(elements, jsClass())) else (THROW_CCE())
        if isInterface(tmp0_all_0, jsClass()):
            tmp = kotlin_collections_Collection_kotlin_Any__(tmp0_all_0).isEmpty_0_k_()
        elif True:
            tmp = False
        
        if tmp:
            tmp_ret_0 = True
            break
        
        tmp0_iterator_1 = tmp0_all_0.iterator_0_k_()
        while tmp0_iterator_1.hasNext_0_k_():
            element_2 = tmp0_iterator_1.next_0_k_()
            if visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
                tmp = _UShortArray___get_storage__impl_(this)
                tmp0_toShort_0_4 = unboxIntrinsic(element_2)
                tmp = contains_0(_UShort___get_data__impl_(tmp0_toShort_0_4))
            elif True:
                tmp = False
            
            if not tmp:
                tmp_ret_0 = False
                break
            
        
        tmp_ret_0 = True
        if False:
            break
        
    
    return tmp_ret_0

def UShortArray__containsAll_impl_0(this, elements):
    return UShortArray__containsAll_impl(unboxIntrinsic(this), elements)

def UShortArray__isEmpty_impl(this):
    return len(_UShortArray___get_storage__impl_(this)) == 0

def UShortArray__toString_impl(this):
    return (str('UShortArray(storage=') + str(toString_0(this.storage))) + str(')')

def UShortArray__hashCode_impl(this):
    return hashCode(this.storage)

def UShortArray__equals_impl(this, other):
    if not visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
        return False
    
    tmp0_other_with_cast = (unboxIntrinsic(other)) if (visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean) else (THROW_CCE())
    if not (this.storage == tmp0_other_with_cast.storage):
        return False
    
    return True

class UShortArray:
    def __init__(self, storage):
        self.storage = storage
    
    def _get_size__0_k_(self):
        return _UShortArray___get_size__impl_(unboxIntrinsic(self))
    
    def iterator_0_k_(self):
        return UShortArray__iterator_impl(unboxIntrinsic(self))
    
    def contains_6go47f_k_(self, element):
        return UShortArray__contains_impl(unboxIntrinsic(self), element)
    
    def contains_2bq_k_(self, element):
        return UShortArray__contains_impl_0(self, element)
    
    def containsAll_m5guox_k_(self, elements):
        return UShortArray__containsAll_impl(unboxIntrinsic(self), elements)
    
    def containsAll_dxd4eo_k_(self, elements):
        return UShortArray__containsAll_impl_0(self, elements)
    
    def isEmpty_0_k_(self):
        return UShortArray__isEmpty_impl(unboxIntrinsic(self))
    
    def toString(self):
        return UShortArray__toString_impl(unboxIntrinsic(self))
    
    def hashCode(self):
        return UShortArray__hashCode_impl(unboxIntrinsic(self))
    
    def equals(self, other):
        return UShortArray__equals_impl(unboxIntrinsic(self), other)
    

def uintCompare(v1, v2):
    return compareTo_0(v1 ^ IntCompanionObject_getInstance().MIN_VALUE, v2 ^ IntCompanionObject_getInstance().MIN_VALUE)

def uintDivide(v1, v2):
    tmp = (_UInt___get_data__impl_(v1) & 4294967295).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)
    tmp0_toUInt_0 = (tmp // (_UInt___get_data__impl_(v2) & 4294967295).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)
    return _UInt___init__impl_(tmp0_toUInt_0.__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))

def uintRemainder(v1, v2):
    tmp = (_UInt___get_data__impl_(v1) & 4294967295).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)
    tmp0_toUInt_0 = tmp.rem_wiekkq_k_((_UInt___get_data__impl_(v2) & 4294967295).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    return _UInt___init__impl_(tmp0_toUInt_0.__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))

def uintToDouble(v):
    return kotlin_Double(v & IntCompanionObject_getInstance().MAX_VALUE) + (kotlin_Double((((v & 0xffff_ffff) >> 31) << 30).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)) * 2)

def ulongCompare(v1, v2):
    Companion_getInstance_19()
    tmp = (v1 ^ -9223372036854775808).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)
    Companion_getInstance_19()
    return tmp.compareTo_wiekkq_k_((v2 ^ -9223372036854775808).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))

def ulongDivide(v1, v2):
    dividend = _ULong___get_data__impl_(v1)
    divisor = _ULong___get_data__impl_(v2)
    if divisor.compareTo_wiekkq_k_(0) < 0:
        if ulongCompare(_ULong___get_data__impl_(v1), _ULong___get_data__impl_(v2)) < 0:
            tmp = _ULong___init__impl_(0)
        elif True:
            tmp = _ULong___init__impl_(1)
        
        return tmp
    
    if dividend.compareTo_wiekkq_k_(0) >= 0:
        return _ULong___init__impl_((dividend // divisor).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    
    quotient = ((((dividend & 0xffff_ffff_ffff_ffff) >> 1).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000) // divisor).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000) << 1).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)
    rem = (dividend - (quotient * divisor).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)
    tmp0_compareTo_0 = _ULong___init__impl_(rem)
    tmp1_compareTo_0 = _ULong___init__impl_(divisor)
    if ulongCompare(_ULong___get_data__impl_(tmp0_compareTo_0), _ULong___get_data__impl_(tmp1_compareTo_0)) >= 0:
        tmp = 1
    elif True:
        tmp = 0
    
    tmp2_plus_0 = tmp
    return _ULong___init__impl_((quotient + tmp2_plus_0).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))

def ulongRemainder(v1, v2):
    dividend = _ULong___get_data__impl_(v1)
    divisor = _ULong___get_data__impl_(v2)
    if divisor.compareTo_wiekkq_k_(0) < 0:
        if ulongCompare(_ULong___get_data__impl_(v1), _ULong___get_data__impl_(v2)) < 0:
            tmp = v1
        elif True:
            tmp = _ULong___init__impl_((_ULong___get_data__impl_(v1) - _ULong___get_data__impl_(v2)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
        
        return tmp
    
    if dividend.compareTo_wiekkq_k_(0) >= 0:
        return _ULong___init__impl_(dividend.rem_wiekkq_k_(divisor))
    
    quotient = ((((dividend & 0xffff_ffff_ffff_ffff) >> 1).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000) // divisor).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000) << 1).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)
    rem = (dividend - (quotient * divisor).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)
    tmp0_compareTo_0 = _ULong___init__impl_(rem)
    tmp1_compareTo_0 = _ULong___init__impl_(divisor)
    if ulongCompare(_ULong___get_data__impl_(tmp0_compareTo_0), _ULong___get_data__impl_(tmp1_compareTo_0)) >= 0:
        tmp = divisor
    elif True:
        tmp = 0
    
    return _ULong___init__impl_((rem - tmp).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))

def ulongToDouble(v):
    return (((v & 0xffff_ffff_ffff_ffff) >> 11).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000).toDouble_0_k_() * 2048) + (v & 2047).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000).toDouble_0_k_()

def ulongToString(v):
    return ulongToString_0(v, 10)

def ulongToString_0(v, base):
    if v.compareTo_wiekkq_k_(0) >= 0:
        return toString_1(base)
    
    tmp0_div_0 = ((v & 0xffff_ffff_ffff_ffff) >> 1).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)
    quotient = ((tmp0_div_0 // base).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000) << 1).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)
    tmp1_times_0 = quotient
    rem = (v - (tmp1_times_0 * base).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)
    if rem.compareTo_wiekkq_k_(base) >= 0:
        tmp2_minus_0 = rem
        rem = (tmp2_minus_0 - base).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)
        tmp3_plus_0 = quotient
        quotient = (tmp3_plus_0 + 1).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)
    
    return toString_1(base) + toString_1(base)

def doubleToUInt(v):
    if isNaN_0():
        tmp = _UInt___init__impl_(0)
    else:
        Companion_getInstance_4()
        tmp0_toDouble_0 = _UInt___init__impl_(0)
        if v <= uintToDouble(_UInt___get_data__impl_(tmp0_toDouble_0)):
            Companion_getInstance_4()
            tmp = _UInt___init__impl_(0)
        else:
            Companion_getInstance_4()
            tmp1_toDouble_0 = _UInt___init__impl_(-1)
            if v >= uintToDouble(_UInt___get_data__impl_(tmp1_toDouble_0)):
                Companion_getInstance_4()
                tmp = _UInt___init__impl_(-1)
            elif v <= kotlin_Double(IntCompanionObject_getInstance().MAX_VALUE):
                tmp2_toUInt_0 = v.__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
                tmp = _UInt___init__impl_(tmp2_toUInt_0)
            elif True:
                tmp3_toUInt_0 = (v - IntCompanionObject_getInstance().MAX_VALUE).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
                tmp5_plus_0 = _UInt___init__impl_(tmp3_toUInt_0)
                tmp4_toUInt_0 = IntCompanionObject_getInstance().MAX_VALUE
                tmp6_plus_0 = _UInt___init__impl_(tmp4_toUInt_0)
                tmp = _UInt___init__impl_((_UInt___get_data__impl_(tmp5_plus_0) + _UInt___get_data__impl_(tmp6_plus_0)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))
            
        
    
    return tmp

def doubleToULong(v):
    if isNaN_0():
        tmp = _ULong___init__impl_(Long(0, 0))
    else:
        Companion_getInstance_7()
        tmp0_toDouble_0 = _ULong___init__impl_(Long(0, 0))
        if v <= ulongToDouble(_ULong___get_data__impl_(tmp0_toDouble_0)):
            Companion_getInstance_7()
            tmp = _ULong___init__impl_(Long(0, 0))
        else:
            Companion_getInstance_7()
            tmp1_toDouble_0 = _ULong___init__impl_(Long(-1, -1))
            if v >= ulongToDouble(_ULong___get_data__impl_(tmp1_toDouble_0)):
                Companion_getInstance_7()
                tmp = _ULong___init__impl_(Long(-1, -1))
            else:
                Companion_getInstance_19()
                if v < (9223372036854775807).toDouble_0_k_():
                    tmp2_toULong_0 = v.__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)
                    tmp = _ULong___init__impl_(tmp2_toULong_0)
                elif True:
                    tmp3_toULong_0 = (v - 9.223372036854776E18).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)
                    tmp4_plus_0 = _ULong___init__impl_(tmp3_toULong_0)
                    tmp = _ULong___init__impl_((_ULong___get_data__impl_(tmp4_plus_0) + _ULong___get_data__impl_(_ULong___init__impl_(Long(0, -2147483648)))).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
                
            
        
    
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
    
    def __init__(self):
        pass
    

class Comparable:
    def compareTo_2c5_k_(self, other):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    
    def __init__(self):
        pass
    

class Iterator_3:
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
    
    def __init__(self):
        pass
    

class ListIterator:
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
    
    def __init__(self):
        pass
    

class MutableIterator:
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
    
    def __init__(self):
        pass
    

class MutableListIterator:
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
    
    def __init__(self):
        pass
    

class Number_0:
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
    

class SinceKotlin:
    def __init__(self, version):
        self.version = version
    
    def _get_version__0_k_(self):
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
    DeprecationLevel_WARNING_instance = DeprecationLevel('WARNING', 0)
    DeprecationLevel_ERROR_instance = DeprecationLevel('ERROR', 1)
    DeprecationLevel_HIDDEN_instance = DeprecationLevel('HIDDEN', 2)

class DeprecationLevel:
    def __init__(self, name, ordinal):
        super(name, ordinal)
    
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
    
    def _get_name__0_k_(self):
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
    

class ReplaceWith:
    def __init__(self, expression, *imports):
        self.expression = expression
        self.imports = imports
    
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
    

class IntIterator:
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
    

class DoubleIterator:
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
    

class FloatIterator:
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
    

class LongIterator:
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
    

class CharIterator:
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
    

class BooleanIterator:
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
    

class ShortIterator:
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
    

def _get_finalElement__1(_this):
    return _this.finalElement

def _set_hasNext__1(_this, _set___):
    _this.hasNext = _set___

def _get_hasNext__1(_this):
    return _this.hasNext

def _set_next__1(_this, _set___):
    _this.next = _set___

def _get_next__1(_this):
    return _this.next

class IntProgressionIterator:
    def __init__(self, first, last, step):
        super()
        self.step = step
        self.finalElement = last
        self.hasNext = (first <= last) if (self.step > 0) else (first >= last)
        self.next = (first) if (self.hasNext) else (self.finalElement)
    
    def _get_step__0_k_(self):
        return self.step
    
    def hasNext_0_k_(self):
        return self.hasNext
    
    def nextInt_0_k_(self):
        value = self.next
        if value == self.finalElement:
            if not self.hasNext:
                raise NoSuchElementException_init__Create_()
            
            self.hasNext = False
        else:
            tmp0_this = self
            tmp0_this.next = (tmp0_this.next + self.step).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
        
        return value
    
    def next_0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def _get_finalElement__2(_this):
    return _this.finalElement

def _set_hasNext__2(_this, _set___):
    _this.hasNext = _set___

def _get_hasNext__2(_this):
    return _this.hasNext

def _set_next__2(_this, _set___):
    _this.next = _set___

def _get_next__2(_this):
    return _this.next

class LongProgressionIterator:
    def __init__(self, first, last, step):
        super()
        self.step = step
        self.finalElement = last
        self.hasNext = (first.compareTo_wiekkq_k_(last) <= 0) if (self.step.compareTo_wiekkq_k_(0) > 0) else (first.compareTo_wiekkq_k_(last) >= 0)
        self.next = (first) if (self.hasNext) else (self.finalElement)
    
    def _get_step__0_k_(self):
        return self.step
    
    def hasNext_0_k_(self):
        return self.hasNext
    
    def nextLong_0_k_(self):
        value = self.next
        if value == self.finalElement:
            if not self.hasNext:
                raise NoSuchElementException_init__Create_()
            
            self.hasNext = False
        else:
            tmp0_this = self
            tmp0_this.next = (tmp0_this.next + self.step).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)
        
        return value
    
    def next_0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def _get_finalElement__3(_this):
    return _this.finalElement

def _set_hasNext__3(_this, _set___):
    _this.hasNext = _set___

def _get_hasNext__3(_this):
    return _this.hasNext

def _set_next__3(_this, _set___):
    _this.next = _set___

def _get_next__3(_this):
    return _this.next

class CharProgressionIterator:
    def __init__(self, first, last, step):
        super()
        self.step = step
        tmp = self
        tmp.finalElement = last.toInt_0_k_()
        self.hasNext = (first.compareTo_wi8o78_k_(last) <= 0) if (self.step > 0) else (first.compareTo_wi8o78_k_(last) >= 0)
        tmp = self
        if self.hasNext:
            tmp = first.toInt_0_k_()
        else:
            tmp = self.finalElement
        
        tmp.next = tmp
    
    def _get_step__0_k_(self):
        return self.step
    
    def hasNext_0_k_(self):
        return self.hasNext
    
    def nextChar_0_k_(self):
        value = self.next
        if value == self.finalElement:
            if not self.hasNext:
                raise NoSuchElementException_init__Create_()
            
            self.hasNext = False
        else:
            tmp0_this = self
            tmp0_this.next = (tmp0_this.next + self.step).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
        
        return numberToChar(value)
    
    def next_0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class Companion_12:
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

class IntProgression:
    def __init__(self, start, endInclusive, step):
        Companion_getInstance_11()
        if step == 0:
            raise IllegalArgumentException_init__Create__0('Step must be non-zero.')
        
        if step == IntCompanionObject_getInstance().MIN_VALUE:
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
        return IntProgressionIterator(self.first, self.last, self.step)
    
    def isEmpty_0_k_(self):
        return (self.first > self.last) if (self.step > 0) else (self.first < self.last)
    
    def equals(self, other):
        if visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
            tmp = (True) if ((kotlin_ranges_IntProgression(other).isEmpty_0_k_()) if (self.isEmpty_0_k_()) else (False)) else ((self.step == kotlin_ranges_IntProgression(other).step) if ((self.last == kotlin_ranges_IntProgression(other).last) if (self.first == kotlin_ranges_IntProgression(other).first) else (False)) else (False))
        elif True:
            tmp = False
        
        return tmp
    
    def hashCode(self):
        return (-1) if (self.isEmpty_0_k_()) else ((imul(31, (imul(31, self.first) + self.last).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)) + self.step).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))
    
    def toString(self):
        return ((((str(self.first) + str('..')) + str(self.last)) + str(' step ')) + str(self.step)) if (self.step > 0) else ((((str(self.first) + str(' downTo ')) + str(self.last)) + str(' step ')) + str((-self.step).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)))
    

class Companion_13:
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
def Companion_getInstance_12():
    if Companion_instance == None:
        Companion_13()
    
    return Companion_instance

class LongProgression:
    def __init__(self, start, endInclusive, step):
        Companion_getInstance_12()
        if step == 0:
            raise IllegalArgumentException_init__Create__0('Step must be non-zero.')
        
        Companion_getInstance_19()
        if step == -9223372036854775808:
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
        return LongProgressionIterator(self.first, self.last, self.step)
    
    def isEmpty_0_k_(self):
        return (self.first.compareTo_wiekkq_k_(self.last) > 0) if (self.step.compareTo_wiekkq_k_(0) > 0) else (self.first.compareTo_wiekkq_k_(self.last) < 0)
    
    def equals(self, other):
        if visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
            tmp = (True) if ((kotlin_ranges_LongProgression(other).isEmpty_0_k_()) if (self.isEmpty_0_k_()) else (False)) else ((self.step == kotlin_ranges_LongProgression(other).step) if ((self.last == kotlin_ranges_LongProgression(other).last) if (self.first == kotlin_ranges_LongProgression(other).first) else (False)) else (False))
        elif True:
            tmp = False
        
        return tmp
    
    def hashCode(self):
        return (-1) if (self.isEmpty_0_k_()) else (((31 * ((31 * (self.first ^ ((self.first & 0xffff_ffff_ffff_ffff) >> 32).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)) + (self.last ^ ((self.last & 0xffff_ffff_ffff_ffff) >> 32).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)) + (self.step ^ ((self.step & 0xffff_ffff_ffff_ffff) >> 32).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))
    
    def toString(self):
        return ((((str(self.first) + str('..')) + str(self.last)) + str(' step ')) + str(self.step)) if (self.step.compareTo_wiekkq_k_(0) > 0) else ((((str(self.first) + str(' downTo ')) + str(self.last)) + str(' step ')) + str((-self.step).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)))
    

class Companion_14:
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
def Companion_getInstance_13():
    if Companion_instance == None:
        Companion_14()
    
    return Companion_instance

class CharProgression:
    def __init__(self, start, endInclusive, step):
        Companion_getInstance_13()
        if step == 0:
            raise IllegalArgumentException_init__Create__0('Step must be non-zero.')
        
        if step == IntCompanionObject_getInstance().MIN_VALUE:
            raise IllegalArgumentException_init__Create__0('Step must be greater than Int.MIN_VALUE to avoid overflow on negation.')
        
        self.first = start
        tmp = self
        tmp = start.toInt_0_k_()
        tmp.last = numberToChar(getProgressionLastElement_1(tmp, endInclusive.toInt_0_k_(), step))
        self.step = step
    
    def _get_first__0_k_(self):
        return self.first
    
    def _get_last__0_k_(self):
        return self.last
    
    def _get_step__0_k_(self):
        return self.step
    
    def iterator_0_k_(self):
        return CharProgressionIterator(self.first, self.last, self.step)
    
    def isEmpty_0_k_(self):
        return (self.first.compareTo_wi8o78_k_(self.last) > 0) if (self.step > 0) else (self.first.compareTo_wi8o78_k_(self.last) < 0)
    
    def equals(self, other):
        if visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
            tmp = (True) if ((kotlin_ranges_CharProgression(other).isEmpty_0_k_()) if (self.isEmpty_0_k_()) else (False)) else ((self.step == kotlin_ranges_CharProgression(other).step) if ((self.last == kotlin_ranges_CharProgression(other).last) if (self.first == kotlin_ranges_CharProgression(other).first) else (False)) else (False))
        elif True:
            tmp = False
        
        return tmp
    
    def hashCode(self):
        if self.isEmpty_0_k_():
            tmp = -1
        else:
            tmp0__get_code__0 = self.first
            tmp = imul(31, tmp0__get_code__0.toInt_0_k_())
            tmp1__get_code__0 = self.last
            tmp = (imul(31, (tmp + tmp1__get_code__0.toInt_0_k_()).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)) + self.step).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
        
        return tmp
    
    def toString(self):
        return ((((str(self.first) + str('..')) + str(self.last)) + str(' step ')) + str(self.step)) if (self.step > 0) else ((((str(self.first) + str(' downTo ')) + str(self.last)) + str(' step ')) + str((-self.step).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)))
    

class ClosedRange:
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
    
    def __init__(self):
        pass
    

class Companion_15:
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

class IntRange:
    def __init__(self, start, endInclusive):
        Companion_getInstance_14()
        super(start, endInclusive, 1)
    
    def _get_start__0_k_(self):
        return self._get_first__0_k_()
    
    def _get_endInclusive__0_k_(self):
        return self._get_last__0_k_()
    
    def contains_ha5a7z_k_(self, value):
        return (value <= self._get_last__0_k_()) if (self._get_first__0_k_() <= value) else (False)
    
    def contains_2c5_k_(self, value):
        return self.contains_ha5a7z_k_((kotlin_Int(value)) if (jsTypeOf(value) == 'number') else (THROW_CCE()))
    
    def isEmpty_0_k_(self):
        return self._get_first__0_k_() > self._get_last__0_k_()
    
    def equals(self, other):
        if visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
            tmp = (True) if ((kotlin_ranges_IntRange(other).isEmpty_0_k_()) if (self.isEmpty_0_k_()) else (False)) else ((self._get_last__0_k_() == kotlin_ranges_IntRange(other)._get_last__0_k_()) if (self._get_first__0_k_() == kotlin_ranges_IntRange(other)._get_first__0_k_()) else (False))
        elif True:
            tmp = False
        
        return tmp
    
    def hashCode(self):
        return (-1) if (self.isEmpty_0_k_()) else ((imul(31, self._get_first__0_k_()) + self._get_last__0_k_()).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))
    
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
    

class Companion_16:
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
def Companion_getInstance_15():
    if Companion_instance == None:
        Companion_16()
    
    return Companion_instance

class LongRange:
    def __init__(self, start, endInclusive):
        Companion_getInstance_15()
        super(start, endInclusive, 1)
    
    def _get_start__0_k_(self):
        return self._get_first__0_k_()
    
    def _get_endInclusive__0_k_(self):
        return self._get_last__0_k_()
    
    def contains_wiekkq_k_(self, value):
        return (value.compareTo_wiekkq_k_(self._get_last__0_k_()) <= 0) if (self._get_first__0_k_().compareTo_wiekkq_k_(value) <= 0) else (False)
    
    def contains_2c5_k_(self, value):
        return self.contains_wiekkq_k_((kotlin_Long(value)) if (visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean) else (THROW_CCE()))
    
    def isEmpty_0_k_(self):
        return self._get_first__0_k_().compareTo_wiekkq_k_(self._get_last__0_k_()) > 0
    
    def equals(self, other):
        if visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
            tmp = (True) if ((kotlin_ranges_LongRange(other).isEmpty_0_k_()) if (self.isEmpty_0_k_()) else (False)) else ((self._get_last__0_k_() == kotlin_ranges_LongRange(other)._get_last__0_k_()) if (self._get_first__0_k_() == kotlin_ranges_LongRange(other)._get_first__0_k_()) else (False))
        elif True:
            tmp = False
        
        return tmp
    
    def hashCode(self):
        return (-1) if (self.isEmpty_0_k_()) else (((31 * (self._get_first__0_k_() ^ ((self._get_first__0_k_() & 0xffff_ffff_ffff_ffff) >> 32).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)) + (self._get_last__0_k_() ^ ((self._get_last__0_k_() & 0xffff_ffff_ffff_ffff) >> 32).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))
    
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
    

class Companion_17:
    def __init__(self):
        global Companion_instance
        Companion_instance = self
        self.EMPTY = CharRange(Char_0(1), Char_0(0))
    
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

class CharRange:
    def __init__(self, start, endInclusive):
        Companion_getInstance_16()
        super(start, endInclusive, 1)
    
    def _get_start__0_k_(self):
        return self._get_first__0_k_()
    
    def _get_endInclusive__0_k_(self):
        return self._get_last__0_k_()
    
    def contains_wi8o78_k_(self, value):
        return (value.compareTo_wi8o78_k_(self._get_last__0_k_()) <= 0) if (self._get_first__0_k_().compareTo_wi8o78_k_(value) <= 0) else (False)
    
    def contains_2c5_k_(self, value):
        return self.contains_wi8o78_k_((kotlin_Char(value)) if (visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean) else (THROW_CCE()))
    
    def isEmpty_0_k_(self):
        return self._get_first__0_k_().compareTo_wi8o78_k_(self._get_last__0_k_()) > 0
    
    def equals(self, other):
        if visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
            tmp = (True) if ((kotlin_ranges_CharRange(other).isEmpty_0_k_()) if (self.isEmpty_0_k_()) else (False)) else ((self._get_last__0_k_() == kotlin_ranges_CharRange(other)._get_last__0_k_()) if (self._get_first__0_k_() == kotlin_ranges_CharRange(other)._get_first__0_k_()) else (False))
        elif True:
            tmp = False
        
        return tmp
    
    def hashCode(self):
        if self.isEmpty_0_k_():
            tmp = -1
        else:
            tmp0__get_code__0 = self._get_first__0_k_()
            tmp = imul(31, tmp0__get_code__0.toInt_0_k_())
            tmp1__get_code__0 = self._get_last__0_k_()
            tmp = (tmp + tmp1__get_code__0.toInt_0_k_()).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
        
        return tmp
    
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
    

class Unit:
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

class Target:
    def __init__(self, *allowedTargets):
        self.allowedTargets = allowedTargets
    
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
    AnnotationRetention_SOURCE_instance = AnnotationRetention('SOURCE', 0)
    AnnotationRetention_BINARY_instance = AnnotationRetention('BINARY', 1)
    AnnotationRetention_RUNTIME_instance = AnnotationRetention('RUNTIME', 2)

class AnnotationRetention:
    def __init__(self, name, ordinal):
        super(name, ordinal)
    
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

def getProgressionLastElement_1(start, end, step):
    if step > 0:
        tmp = (end) if (start >= end) else ((end - differenceModulo_1(end, start, step)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))
    elif step < 0:
        tmp = (end) if (start <= end) else ((end + differenceModulo_1(start, end, (-step).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))
    else:
        raise IllegalArgumentException_init__Create__0('Step is zero.')
    
    return tmp

def getProgressionLastElement_2(start, end, step):
    if step.compareTo_wiekkq_k_(0) > 0:
        tmp = (end) if (start.compareTo_wiekkq_k_(end) >= 0) else ((end - differenceModulo_2(end, start, step)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    elif step.compareTo_wiekkq_k_(0) < 0:
        tmp = (end) if (start.compareTo_wiekkq_k_(end) <= 0) else ((end + differenceModulo_2(start, end, (-step).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
    else:
        raise IllegalArgumentException_init__Create__0('Step is zero.')
    
    return tmp

def differenceModulo_1(a, b, c):
    return mod((mod(a, c) - mod(b, c)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000), c)

def differenceModulo_2(a, b, c):
    return mod_0((mod_0(a, c) - mod_0(b, c)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000), c)

def mod(a, b):
    mod = a % b
    return (mod) if (mod >= 0) else ((mod + b).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))

def mod_0(a, b):
    mod = a.rem_wiekkq_k_(b)
    return (mod) if (mod.compareTo_wiekkq_k_(0) >= 0) else ((mod + b).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))

class ByteCompanionObject_0:
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

class ShortCompanionObject_0:
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

class IntCompanionObject_0:
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

class FloatCompanionObject_0:
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

class DoubleCompanionObject_0:
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

class StringCompanionObject:
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

class BooleanCompanionObject:
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
    
    def _get_name__0_k_(self):
        return self.name
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def toTypedArray():
    return copyToArray_0(self)

def copyToArray_0(collection):
    if EXCLEQEQ(toArray(collection), undefined):
        tmp0_unsafeCast_0 = INVOKE(toArray(collection))
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
    elif True:
        tmp1_unsafeCast_0 = copyToArrayImpl_0(collection)
        tmp = kotlin_Any_(tmp1_unsafeCast_0)
    
    return tmp

def copyToArrayImpl_0(collection):
    array = kotlin_Array_kotlin_Any__(js('[]'))
    iterator = collection.iterator_0_k_()
    while iterator.hasNext_0_k_():
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    
    return array

def arrayCopy_0(source, destination, destinationOffset, startIndex, endIndex):
    Companion_getInstance().checkRangeIndexes_zd700_k_(startIndex, endIndex, len(source))
    rangeSize = (endIndex - startIndex).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
    Companion_getInstance().checkRangeIndexes_zd700_k_(destinationOffset, (destinationOffset + rangeSize).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000), len(destination))
    if ANDAND(INVOKE(isView(js('ArrayBuffer')), destination), INVOKE(isView(js('ArrayBuffer')), source)):
        subrange = INVOKE(subarray(source), startIndex, endIndex)
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    elif (True) if (not (source is destination)) else (destinationOffset <= startIndex):
        inductionVariable = 0
        if inductionVariable < rangeSize:
            while True:
                index = inductionVariable
                inductionVariable = (inductionVariable + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
                destination.__setitem__((destinationOffset + index).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000), source[(startIndex + index).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)])
                if inductionVariable < rangeSize:
                    break
                
            
        
    else:
        inductionVariable = (rangeSize - 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
        if 0 <= inductionVariable:
            while True:
                index = inductionVariable
                inductionVariable = (inductionVariable + -1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
                destination.__setitem__((destinationOffset + index).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000), source[(startIndex + index).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)])
                if 0 <= inductionVariable:
                    break
                
            
        
    

def copyToArrayImpl_1(collection, array):
    if len(array) < collection._get_size__0_k_():
        tmp0_unsafeCast_0 = copyToArrayImpl_0(collection)
        return kotlin_Any_(tmp0_unsafeCast_0)
    
    iterator = collection.iterator_0_k_()
    index = 0
    while iterator.hasNext_0_k_():
        tmp0 = index
        index = (tmp0 + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
        tmp1_unsafeCast_0 = iterator.next_0_k_()
        array.__setitem__(tmp0, kotlin_Any_(tmp1_unsafeCast_0))
    
    if index < len(array):
        tmp = index
        array.__setitem__(tmp, kotlin_Any_(None))
    
    return array

class AbstractMutableCollection:
    def __init__(self):
        super()
    
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
                visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
            
        
        return modified
    
    def removeAll_dxd4eo_k_(self, elements):
        self.checkIsMutable_sv8swh_k_()
        return removeAll_0(lambda it: elements.contains_2bq_k_(it))
    
    def retainAll_dxd4eo_k_(self, elements):
        self.checkIsMutable_sv8swh_k_()
        return removeAll_0(lambda it: not elements.contains_2bq_k_(it))
    
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
    

def _get_list__0(_this):
    return _this.list

def _get_fromIndex__0(_this):
    return _this.fromIndex

def _set__size__0(_this, _set___):
    _this._size = _set___

def _get__size__0(_this):
    return _this._size

class IteratorImpl_0:
    def __init__(self, _outer):
        self._this = _outer
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
        return self.index < self._this._get_size__0_k_()
    
    def next_0_k_(self):
        if not self.hasNext_0_k_():
            raise NoSuchElementException_init__Create_()
        
        tmp = self
        tmp0_this = self
        tmp1 = tmp0_this.index
        tmp0_this.index = (tmp1 + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
        tmp.last = tmp1
        return self._this.get_ha5a7z_k_(self.last)
    
    def remove_sv8swh_k_(self):
        tmp0_check_0 = not (self.last == -1)
        if not tmp0_check_0:
            message_1 = 'Call next() or previous() before removing element from the iterator.'
            raise IllegalStateException_init__Create__0(toString_0(message_1))
        
        self._this.removeAt_ha5a7z_k_(self.last)
        Unit_getInstance()
        self.index = self.last
        self.last = -1
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class ListIteratorImpl_0:
    def __init__(self, _outer, index):
        self._this = _outer
        super(_outer)
        Companion_getInstance().checkPositionIndex_rvwcgf_k_(index, self._this._get_size__0_k_())
        self._set_index__majfzk_k_(index)
    
    def hasPrevious_0_k_(self):
        return self._get_index__0_k_() > 0
    
    def nextIndex_0_k_(self):
        return self._get_index__0_k_()
    
    def previous_0_k_(self):
        if not self.hasPrevious_0_k_():
            raise NoSuchElementException_init__Create_()
        
        tmp0_this = self
        tmp0_this._set_index__majfzk_k_((tmp0_this._get_index__0_k_() - 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))
        self._set_last__majfzk_k_(tmp0_this._get_index__0_k_())
        return self._this.get_ha5a7z_k_(self._get_last__0_k_())
    
    def previousIndex_0_k_(self):
        return (self._get_index__0_k_() - 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
    
    def add_jxzaet_k_(self, element):
        self._this.add_vz2mgm_k_(self._get_index__0_k_(), element)
        tmp0_this = self
        tmp1 = tmp0_this._get_index__0_k_()
        tmp0_this._set_index__majfzk_k_((tmp1 + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))
        Unit_getInstance()
        self._set_last__majfzk_k_(-1)
    
    def add_iav7o_k_(self, element):
        return self.add_jxzaet_k_((E(element)) if ((True) if (element == None) else (isObject(element))) else (THROW_CCE()))
    
    def set_jxzaet_k_(self, element):
        tmp0_check_0 = not (self._get_last__0_k_() == -1)
        if not tmp0_check_0:
            message_1 = 'Call next() or previous() before updating element value with the iterator.'
            raise IllegalStateException_init__Create__0(toString_0(message_1))
        
        self._this.set_ddb1qf_k_(self._get_last__0_k_(), element)
        Unit_getInstance()
    
    def set_iav7o_k_(self, element):
        return self.set_jxzaet_k_((E(element)) if ((True) if (element == None) else (isObject(element))) else (THROW_CCE()))
    
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
    

class SubList_0:
    def __init__(self, list, fromIndex, toIndex):
        super()
        self.list = list
        self.fromIndex = fromIndex
        self._size = 0
        Companion_getInstance().checkRangeIndexes_zd700_k_(self.fromIndex, toIndex, self.list._get_size__0_k_())
        self._size = (toIndex - self.fromIndex).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
    
    def add_vz2mgm_k_(self, index, element):
        Companion_getInstance().checkPositionIndex_rvwcgf_k_(index, self._size)
        self.list.add_vz2mgm_k_((self.fromIndex + index).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000), element)
        tmp0_this = self
        tmp1 = tmp0_this._size
        tmp0_this._size = (tmp1 + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
        Unit_getInstance()
    
    def get_ha5a7z_k_(self, index):
        Companion_getInstance().checkElementIndex_rvwcgf_k_(index, self._size)
        return self.list.get_ha5a7z_k_((self.fromIndex + index).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))
    
    def removeAt_ha5a7z_k_(self, index):
        Companion_getInstance().checkElementIndex_rvwcgf_k_(index, self._size)
        result = self.list.removeAt_ha5a7z_k_((self.fromIndex + index).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))
        tmp0_this = self
        tmp1 = tmp0_this._size
        tmp0_this._size = (tmp1 - 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
        Unit_getInstance()
        return result
    
    def set_ddb1qf_k_(self, index, element):
        Companion_getInstance().checkElementIndex_rvwcgf_k_(index, self._size)
        return self.list.set_ddb1qf_k_((self.fromIndex + index).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000), element)
    
    def _get_size__0_k_(self):
        return self._size
    
    def checkIsMutable_sv8swh_k_(self):
        return self.list.checkIsMutable_sv8swh_k_()
    
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
    

class AbstractMutableList:
    def __init__(self):
        super()
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
        self.checkIsMutable_sv8swh_k_()
        _index = index
        changed = False
        tmp0_iterator = elements.iterator_0_k_()
        while tmp0_iterator.hasNext_0_k_():
            e = tmp0_iterator.next_0_k_()
            tmp1 = _index
            _index = (tmp1 + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
            self.add_vz2mgm_k_(tmp1, e)
            changed = True
        
        return changed
    
    def clear_sv8swh_k_(self):
        self.checkIsMutable_sv8swh_k_()
        self.removeRange_rvwcgf_k_(0, self._get_size__0_k_())
    
    def removeAll_dxd4eo_k_(self, elements):
        self.checkIsMutable_sv8swh_k_()
        return removeAll(lambda it: elements.contains_2bq_k_(it))
    
    def retainAll_dxd4eo_k_(self, elements):
        self.checkIsMutable_sv8swh_k_()
        return removeAll(lambda it: not elements.contains_2bq_k_(it))
    
    def iterator_0_k_(self):
        return IteratorImpl_0(self)
    
    def contains_2bq_k_(self, element):
        return self.indexOf_2bq_k_(element) >= 0
    
    def indexOf_2bq_k_(self, element):
        inductionVariable = 0
        last = _get_lastIndex__4()
        if inductionVariable <= last:
            while True:
                index = inductionVariable
                inductionVariable = (inductionVariable + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
                if self.get_ha5a7z_k_(index) == element:
                    return index
                
                if not (index == last):
                    break
                
            
        
        return -1
    
    def lastIndexOf_2bq_k_(self, element):
        inductionVariable = _get_lastIndex__4()
        if 0 <= inductionVariable:
            while True:
                index = inductionVariable
                inductionVariable = (inductionVariable + -1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
                if self.get_ha5a7z_k_(index) == element:
                    return index
                
                if 0 <= inductionVariable:
                    break
                
            
        
        return -1
    
    def listIterator_0_k_(self):
        return self.listIterator_ha5a7z_k_(0)
    
    def listIterator_ha5a7z_k_(self, index):
        return ListIteratorImpl_0(self, index)
    
    def subList_27zxwg_k_(self, fromIndex, toIndex):
        return SubList_0(self, fromIndex, toIndex)
    
    def removeRange_rvwcgf_k_(self, fromIndex, toIndex):
        iterator = self.listIterator_ha5a7z_k_(fromIndex)
        tmp0_repeat_0 = (toIndex - fromIndex).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
        inductionVariable = 0
        if inductionVariable < tmp0_repeat_0:
            while True:
                index_2 = inductionVariable
                inductionVariable = (inductionVariable + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
                iterator.next_0_k_()
                Unit_getInstance()
                iterator.remove_sv8swh_k_()
                if inductionVariable < tmp0_repeat_0:
                    break
                
            
        
    
    def equals(self, other):
        if other is self:
            return True
        
        if not ((isInterface(other, jsClass())) if (not (other == None)) else (False)):
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
    

def _set_array_(_this, _set___):
    _this.array = _set___

def _get_array__3(_this):
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

def ArrayList_init__Init__0(initialCapacity, _this):
    super(kotlin_Array_kotlin_Any__(js('[]')))
    return _this

def ArrayList_init__Create__0(initialCapacity):
    return ArrayList_init__Init__0(initialCapacity, Object_create())

def ArrayList_init__Init__1(initialCapacity, _mask0, _marker, _this):
    if not (_mask0 & 1 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    ArrayList_init__Init__0(initialCapacity, _this)
    return _this

def ArrayList_init__Create__1(initialCapacity, _mask0, _marker):
    return ArrayList_init__Init__1(initialCapacity, _mask0, _marker, Object_create())

def ArrayList_init__Init__2(elements, _this):
    super(copyToArray_0(elements))
    return _this

def ArrayList_init__Create__2(elements):
    return ArrayList_init__Init__2(elements, Object_create())

def rangeCheck(_this, index):
    Companion_getInstance().checkElementIndex_rvwcgf_k_(index, _this._get_size__0_k_())
    return index

def insertionRangeCheck(_this, index):
    Companion_getInstance().checkPositionIndex_rvwcgf_k_(index, _this._get_size__0_k_())
    return index

class ArrayList:
    def __init__(self, array):
        super()
        self.array = array
        self.isReadOnly = False
    
    def build_0_k_(self):
        self.checkIsMutable_sv8swh_k_()
        self.isReadOnly = True
        return self
    
    def trimToSize_sv8swh_k_(self):
        pass
    
    def ensureCapacity_majfzk_k_(self, minCapacity):
        pass
    
    def _get_size__0_k_(self):
        return len(self.array)
    
    def get_ha5a7z_k_(self, index):
        tmp = self.array[rangeCheck(self, index)]
        return (E(tmp)) if ((True) if (tmp == None) else (isObject(tmp))) else (THROW_CCE())
    
    def set_ddb1qf_k_(self, index, element):
        self.checkIsMutable_sv8swh_k_()
        rangeCheck(self, index)
        Unit_getInstance()
        tmp0_apply_0 = self.array[index]
        self.array.__setitem__(index, element)
        tmp = tmp0_apply_0
        return (E(tmp)) if ((True) if (tmp == None) else (isObject(tmp))) else (THROW_CCE())
    
    def add_2bq_k_(self, element):
        self.checkIsMutable_sv8swh_k_()
        tmp0_asDynamic_0 = self.array
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
        tmp0_this = self
        tmp1 = tmp0_this._get_modCount__0_k_()
        tmp0_this._set_modCount__majfzk_k_((tmp1 + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))
        Unit_getInstance()
        return True
    
    def add_vz2mgm_k_(self, index, element):
        self.checkIsMutable_sv8swh_k_()
        tmp0_asDynamic_0 = self.array
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
        tmp0_this = self
        tmp1 = tmp0_this._get_modCount__0_k_()
        tmp0_this._set_modCount__majfzk_k_((tmp1 + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))
        Unit_getInstance()
    
    def addAll_dxd4eo_k_(self, elements):
        self.checkIsMutable_sv8swh_k_()
        if elements.isEmpty_0_k_():
            return False
        
        tmp0_this = self
        tmp = tmp0_this
        tmp0_plus_0 = tmp0_this.array
        tmp1_plus_0 = copyToArray_0(elements)
        tmp.array = kotlin_Array_kotlin_Any__(INVOKE(concat(tmp0_plus_0), tmp1_plus_0))
        tmp1_this = self
        tmp2 = tmp1_this._get_modCount__0_k_()
        tmp1_this._set_modCount__majfzk_k_((tmp2 + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))
        Unit_getInstance()
        return True
    
    def addAll_xggsjz_k_(self, index, elements):
        self.checkIsMutable_sv8swh_k_()
        insertionRangeCheck(self, index)
        Unit_getInstance()
        if index == self._get_size__0_k_():
            return self.addAll_dxd4eo_k_(elements)
        
        if elements.isEmpty_0_k_():
            return False
        
        tmp0_subject = index
        if tmp0_subject == self._get_size__0_k_():
            return self.addAll_dxd4eo_k_(elements)
        elif tmp0_subject == 0:
            tmp = self
            tmp0_plus_0 = copyToArray_0(elements)
            tmp1_plus_0 = self.array
            tmp.array = kotlin_Array_kotlin_Any__(INVOKE(concat(tmp0_plus_0), tmp1_plus_0))
        else:
            tmp = self
            tmp2_asDynamic_0 = copyOfRange(0, index)
            tmp.array = kotlin_Array_kotlin_Any__(INVOKE(concat(tmp2_asDynamic_0), copyToArray_0(elements), copyOfRange(index, self._get_size__0_k_())))
        
        tmp1_this = self
        tmp2 = tmp1_this._get_modCount__0_k_()
        tmp1_this._set_modCount__majfzk_k_((tmp2 + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))
        Unit_getInstance()
        return True
    
    def removeAt_ha5a7z_k_(self, index):
        self.checkIsMutable_sv8swh_k_()
        rangeCheck(self, index)
        Unit_getInstance()
        tmp0_this = self
        tmp1 = tmp0_this._get_modCount__0_k_()
        tmp0_this._set_modCount__majfzk_k_((tmp1 + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))
        Unit_getInstance()
        if index == _get_lastIndex__4():
            tmp0_asDynamic_0 = self.array
            tmp = E(INVOKE(pop(tmp0_asDynamic_0)))
        else:
            tmp1_asDynamic_0 = self.array
            tmp = E(ARRAY_ACCESS(INVOKE(splice(tmp1_asDynamic_0), index, 1), 0))
        
        return tmp
    
    def remove_2bq_k_(self, element):
        self.checkIsMutable_sv8swh_k_()
        inductionVariable = 0
        last = (len(self.array) - 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
        if inductionVariable <= last:
            while True:
                index = inductionVariable
                inductionVariable = (inductionVariable + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
                if self.array[index] == element:
                    tmp0_asDynamic_0 = self.array
                    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
                    tmp1_this = self
                    tmp2 = tmp1_this._get_modCount__0_k_()
                    tmp1_this._set_modCount__majfzk_k_((tmp2 + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))
                    Unit_getInstance()
                    return True
                
                if inductionVariable <= last:
                    break
                
            
        
        return False
    
    def removeRange_rvwcgf_k_(self, fromIndex, toIndex):
        self.checkIsMutable_sv8swh_k_()
        tmp0_this = self
        tmp1 = tmp0_this._get_modCount__0_k_()
        tmp0_this._set_modCount__majfzk_k_((tmp1 + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))
        Unit_getInstance()
        tmp0_asDynamic_0 = self.array
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    
    def clear_sv8swh_k_(self):
        self.checkIsMutable_sv8swh_k_()
        tmp = self
        tmp.array = kotlin_Array_kotlin_Any__(js('[]'))
        tmp0_this = self
        tmp1 = tmp0_this._get_modCount__0_k_()
        tmp0_this._set_modCount__majfzk_k_((tmp1 + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))
        Unit_getInstance()
    
    def indexOf_2bq_k_(self, element):
        return indexOf(element)
    
    def lastIndexOf_2bq_k_(self, element):
        return lastIndexOf(element)
    
    def toString(self):
        return arrayToString(self.array)
    
    def toArray_gjotr5_k_(self, array):
        if len(array) < self._get_size__0_k_():
            tmp = self.toArray_0_k_()
            return (kotlin_Array_T_(tmp)) if (isArray(tmp)) else (THROW_CCE())
        
        tmp = self.array
        tmp0_copyInto_0 = (kotlin_Array_T_(tmp)) if (isArray(tmp)) else (THROW_CCE())
        tmp1_copyInto_0 = len(tmp0_copyInto_0)
        arrayCopy_0(tmp0_copyInto_0, array, 0, 0, tmp1_copyInto_0)
        Unit_getInstance()
        if len(array) > self._get_size__0_k_():
            tmp = self._get_size__0_k_()
            array.__setitem__(tmp, (T(None)) if ((True) if (None == None) else (isObject(None))) else (THROW_CCE()))
        
        return array
    
    def toArray_0_k_(self):
        return kotlin_Array_kotlin_Any__(INVOKE(call(slice(js('[]'))), self.array))
    
    def toArray(self):
        return self.toArray_0_k_()
    
    def checkIsMutable_sv8swh_k_(self):
        if self.isReadOnly:
            raise UnsupportedOperationException_init__Create_()
        
    
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
    global output
    output = _set___

def _get_output_():
    return output

output = None
class BaseOutput:
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
    

class NodeJsOutput_0:
    def __init__(self, outputStream):
        super()
        self.outputStream = outputStream
    
    def _get_outputStream__0_k_(self):
        return self.outputStream
    
    def print_qi8yb4_k_(self, message):
        messageString = kotlin_String(INVOKE(js('String'), message))
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    
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
    

class BufferedOutputToConsoleLog_0:
    def __init__(self):
        super()
    
    def print_qi8yb4_k_(self, message):
        s = kotlin_String(INVOKE(js('String'), message))
        tmp0_nativeLastIndexOf_0 = s
        i = kotlin_Int(INVOKE(lastIndexOf(tmp0_nativeLastIndexOf_0), '\n', 0))
        if i >= 0:
            tmp0_this = self
            tmp = tmp0_this._get_buffer__0_k_()
            tmp1_substring_0 = s
            tmp0_this._set_buffer__a4enbm_k_(tmp + kotlin_String(INVOKE(substring(tmp1_substring_0), 0, i)))
            self.flush_sv8swh_k_()
            tmp2_substring_0 = s
            tmp3_substring_0 = (i + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
            s = kotlin_String(INVOKE(substring(tmp2_substring_0), tmp3_substring_0))
        
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
    return kotlin_String(INVOKE(js('String'), value))

class BufferedOutput_0:
    def __init__(self):
        super()
        self.buffer = ''
    
    def _set_buffer__a4enbm_k_(self, _set___):
        self.buffer = _set___
    
    def _get_buffer__0_k_(self):
        return self.buffer
    
    def print_qi8yb4_k_(self, message):
        tmp0_this = self
        tmp = tmp0_this
        tmp = tmp0_this.buffer
        tmp.buffer = tmp + kotlin_String(INVOKE(js('String'), message))
    
    def flush_sv8swh_k_(self):
        self.buffer = ''
    
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
    output.println_qi8yb4_k_(message)

def output_init_():
    isNode_2 = kotlin_Boolean(js('typeof process !== \'undefined\' && process.versions && !!process.versions.node'))
    return (NodeJsOutput_0(js('process.stdout'))) if (isNode_2) else (BufferedOutputToConsoleLog_0())

def _get_EmptyContinuation_():
    return EmptyContinuation

EmptyContinuation = None
class _no_name_provided__1:
    def __init__(self, _tmp0_Continuation_0):
        self._tmp0_Continuation_0 = _tmp0_Continuation_0
    
    def _get_context__2_0_k_(self):
        return self._tmp0_Continuation_0
    
    def _get_context__0_k_(self):
        return self._get_context__2_0_k_()
    
    def resumeWith_3_jccoe6_k_(self, result):
        throwOnFailure()
        tmp = _Result___get_value__impl_(result)
        if (True) if (tmp == None) else (isObject(tmp)):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrTypeOperatorCallImpl
        else:
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrCallImpl
        
        return Unit_getInstance()
    
    def resumeWith_bnunh2_k_(self, result):
        return self.resumeWith_3_jccoe6_k_(result)
    
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

def unsafeCast_0():
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

def isNaN_0():
    return not (self == self)

def _get_INV_2_26_():
    return INV_2_26

INV_2_26 = None
def _get_INV_2_53_():
    return INV_2_53

INV_2_53 = None
def INV_2_26_init_():
    return visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl.pow(2.0, -26.0)

def INV_2_53_init_():
    return visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl.pow(2.0, -53.0)

def _get_js_():
    return ((kotlin_reflect_js_internal_KClassImpl_T_(self)) if (visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean) else (THROW_CCE()))._get_jClass__0_k_()

class KCallable:
    def _get_name__0_k_(self):
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
    
    def __init__(self):
        pass
    

class KClassImpl:
    def __init__(self, jClass):
        self.jClass = jClass
    
    def _get_jClass__0_k_(self):
        return self.jClass
    
    def _get_qualifiedName__0_k_(self):
        raise NotImplementedError_init__Create_(None, 1, None)
    
    def equals(self, other):
        if visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
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
        if not visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
            return False
        
        return (self.givenSimpleName == kotlin_reflect_js_internal_PrimitiveKClassImpl___(other).givenSimpleName) if (self.equals(other)) else (False)
    
    def _get_simpleName__0_k_(self):
        return self.givenSimpleName
    
    def isInstance_wi7j7l_k_(self, value):
        return self.isInstanceFunction(value)
    
    def _get_jClass__0_k_(self):
        pass
    
    def _get_qualifiedName__0_k_(self):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class NothingKClassImpl:
    def __init__(self):
        global NothingKClassImpl_instance
        NothingKClassImpl_instance = self
        super(kotlin_js_JsClass_kotlin_Nothing_(js('Object')))
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

class ErrorKClass:
    def __init__(self):
        pass
    
    def _get_simpleName__0_k_(self):
        raise IllegalStateException_init__Create__0('Unknown simpleName for ErrorKClass')
    
    def _get_qualifiedName__0_k_(self):
        raise IllegalStateException_init__Create__0('Unknown qualifiedName for ErrorKClass')
    
    def isInstance_wi7j7l_k_(self, value):
        raise IllegalStateException_init__Create__0('Can\'s check isInstance on ErrorKClass')
    
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
    

class KFunction:
    def _get_name__0_k_(self):
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
    def _get_name__0_k_(self):
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
    
    def __init__(self):
        pass
    

class KProperty1:
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
    
    def __init__(self):
        pass
    

class KProperty2:
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
    
    def __init__(self):
        pass
    

class KMutableProperty0:
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
    
    def __init__(self):
        pass
    

class KMutableProperty:
    def _get_name__0_k_(self):
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
    
    def __init__(self):
        pass
    

class KMutableProperty2:
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
    
    def __init__(self):
        pass
    

class KType:
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
    
    def __init__(self):
        pass
    

def createKType_0(classifier, arguments, isMarkedNullable):
    return KTypeImpl(classifier, asList(), isMarkedNullable)

def createDynamicKType_0():
    return DynamicKType_getInstance()

def createKTypeParameter_0(name, upperBounds, variance):
    tmp0_subject = variance
    kVariance = (KVariance_IN_getInstance()) if (tmp0_subject == 'in') else ((KVariance_OUT_getInstance()) if (tmp0_subject == 'out') else (KVariance_INVARIANT_getInstance()))
    return KTypeParameterImpl(name, asList(), kVariance, False)

def getStarKTypeProjection_0():
    return Companion_getInstance_1()._get_STAR__0_k_()

def createCovariantKTypeProjection_0(type):
    return Companion_getInstance_1().covariant_573d5y_k_(type)

def createInvariantKTypeProjection_0(type):
    return Companion_getInstance_1().invariant_573d5y_k_(type)

def createContravariantKTypeProjection_0(type):
    return Companion_getInstance_1().contravariant_573d5y_k_(type)

def asString(_this):
    if self.variance == None:
        return '*'
    
    return prefixString() + toString()

class KTypeImpl:
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
        if visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
            tmp = self.classifier == kotlin_reflect_js_internal_KTypeImpl(other).classifier
        elif True:
            tmp = False
        
        if tmp:
            tmp = self.arguments == kotlin_reflect_js_internal_KTypeImpl(other).arguments
        elif True:
            tmp = False
        
        if tmp:
            tmp = self.isMarkedNullable == kotlin_reflect_js_internal_KTypeImpl(other).isMarkedNullable
        elif True:
            tmp = False
        
        return tmp
    
    def hashCode(self):
        return (imul((imul(hashCode(self.classifier), 31) + hashCode(self.arguments)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000), 31) + self.isMarkedNullable.__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
    
    def toString(self):
        tmp = self.classifier
        kClass = (kotlin_reflect_KClass___(tmp)) if (isInterface(tmp, jsClass())) else (None)
        classifierName = (toString_0(self.classifier)) if (kClass == None) else ((kClass._get_simpleName__0_k_()) if (not (kClass._get_simpleName__0_k_() == None)) else ('(non-denotable type)'))
        if self.arguments.isEmpty_0_k_():
            tmp = ''
        else:
            tmp = joinToString_default_0(', ', '<', '>', 0, None, lambda it: asString(self), 24, None)
        
        args = tmp
        nullable = ('?') if (self.isMarkedNullable) else ('')
        return plus(args) + nullable
    

def prefixString():
    tmp0_subject = self
    if tmp0_subject == KVariance_INVARIANT_getInstance():
        tmp = ''
    elif tmp0_subject == KVariance_IN_getInstance():
        tmp = 'in '
    elif tmp0_subject == KVariance_OUT_getInstance():
        tmp = 'out '
    else:
        noWhenBranchMatchedException()
    
    return tmp

class DynamicKType:
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

class KTypeParameterImpl:
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
        return self.name
    
    def component1_0_k_(self):
        return self.name
    
    def component2_0_k_(self):
        return self.upperBounds
    
    def component3_0_k_(self):
        return self.variance
    
    def component4_0_k_(self):
        return self.isReified
    
    def copy_367z8c_k_(self, name, upperBounds, variance, isReified):
        return KTypeParameterImpl(name, upperBounds, variance, isReified)
    
    def copy_default_dg98nz_k_(self, name, upperBounds, variance, isReified, _mask0, _handler):
        if not (_mask0 & 1 == 0):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
        
        if not (_mask0 & 2 == 0):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
        
        if not (_mask0 & 4 == 0):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
        
        if not (_mask0 & 8 == 0):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
        
        return self.copy_367z8c_k_(kotlin_String(name), kotlin_collections_List_kotlin_reflect_KType_(upperBounds), kotlin_reflect_KVariance(variance), isReified)
    
    def hashCode(self):
        result = getStringHashCode(self.name)
        result = (imul(result, 31) + hashCode(self.upperBounds)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
        result = (imul(result, 31) + self.variance.hashCode()).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
        result = (imul(result, 31) + self.isReified.__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
        return result
    
    def equals(self, other):
        if self is other:
            return True
        
        if not visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
            return False
        
        tmp0_other_with_cast = (kotlin_reflect_js_internal_KTypeParameterImpl(other)) if (visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean) else (THROW_CCE())
        if not (self.name == tmp0_other_with_cast.name):
            return False
        
        if not (self.upperBounds == tmp0_other_with_cast.upperBounds):
            return False
        
        if not (self.variance == tmp0_other_with_cast.variance):
            return False
        
        if not (self.isReified == tmp0_other_with_cast.isReified):
            return False
        
        return True
    

def _get_functionClasses_():
    return functionClasses

functionClasses = None
class PrimitiveClasses_0:
    def __init__(self):
        global PrimitiveClasses_instance
        PrimitiveClasses_instance = self
        tmp = self
        tmp0_unsafeCast_0 = js('Object')
        tmp.anyClass = PrimitiveKClassImpl(kotlin_Any_(tmp0_unsafeCast_0), 'Any', lambda it: isObject(it))
        tmp = self
        tmp0_unsafeCast_0 = js('Number')
        tmp.numberClass = PrimitiveKClassImpl(kotlin_Any_(tmp0_unsafeCast_0), 'Number', lambda it: isNumber(it))
        self.nothingClass = NothingKClassImpl_getInstance()
        tmp = self
        tmp0_unsafeCast_0 = js('Boolean')
        tmp.booleanClass = PrimitiveKClassImpl(kotlin_Any_(tmp0_unsafeCast_0), 'Boolean', lambda it: (jsTypeOf(it) == 'boolean') if (not (it == None)) else (False))
        tmp = self
        tmp0_unsafeCast_0 = js('Number')
        tmp.byteClass = PrimitiveKClassImpl(kotlin_Any_(tmp0_unsafeCast_0), 'Byte', lambda it: (jsTypeOf(it) == 'number') if (not (it == None)) else (False))
        tmp = self
        tmp0_unsafeCast_0 = js('Number')
        tmp.shortClass = PrimitiveKClassImpl(kotlin_Any_(tmp0_unsafeCast_0), 'Short', lambda it: (jsTypeOf(it) == 'number') if (not (it == None)) else (False))
        tmp = self
        tmp0_unsafeCast_0 = js('Number')
        tmp.intClass = PrimitiveKClassImpl(kotlin_Any_(tmp0_unsafeCast_0), 'Int', lambda it: (jsTypeOf(it) == 'number') if (not (it == None)) else (False))
        tmp = self
        tmp0_unsafeCast_0 = js('Number')
        tmp.floatClass = PrimitiveKClassImpl(kotlin_Any_(tmp0_unsafeCast_0), 'Float', lambda it: (jsTypeOf(it) == 'number') if (not (it == None)) else (False))
        tmp = self
        tmp0_unsafeCast_0 = js('Number')
        tmp.doubleClass = PrimitiveKClassImpl(kotlin_Any_(tmp0_unsafeCast_0), 'Double', lambda it: (jsTypeOf(it) == 'number') if (not (it == None)) else (False))
        tmp = self
        tmp0_unsafeCast_0 = js('Array')
        tmp.arrayClass = PrimitiveKClassImpl(kotlin_Any_(tmp0_unsafeCast_0), 'Array', lambda it: (isArray(it)) if (not (it == None)) else (False))
        tmp = self
        tmp0_unsafeCast_0 = js('String')
        tmp.stringClass = PrimitiveKClassImpl(kotlin_Any_(tmp0_unsafeCast_0), 'String', lambda it: (jsTypeOf(it) == 'string') if (not (it == None)) else (False))
        tmp = self
        tmp0_unsafeCast_0 = js('Error')
        tmp.throwableClass = PrimitiveKClassImpl(kotlin_Any_(tmp0_unsafeCast_0), 'Throwable', lambda it: visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean)
        tmp = self
        tmp0_unsafeCast_0 = js('Array')
        tmp.booleanArrayClass = PrimitiveKClassImpl(kotlin_Any_(tmp0_unsafeCast_0), 'BooleanArray', lambda it: (isBooleanArray(it)) if (not (it == None)) else (False))
        tmp = self
        tmp0_unsafeCast_0 = js('Uint16Array')
        tmp.charArrayClass = PrimitiveKClassImpl(kotlin_Any_(tmp0_unsafeCast_0), 'CharArray', lambda it: (isCharArray(it)) if (not (it == None)) else (False))
        tmp = self
        tmp0_unsafeCast_0 = js('Int8Array')
        tmp.byteArrayClass = PrimitiveKClassImpl(kotlin_Any_(tmp0_unsafeCast_0), 'ByteArray', lambda it: (isByteArray(it)) if (not (it == None)) else (False))
        tmp = self
        tmp0_unsafeCast_0 = js('Int16Array')
        tmp.shortArrayClass = PrimitiveKClassImpl(kotlin_Any_(tmp0_unsafeCast_0), 'ShortArray', lambda it: (isShortArray(it)) if (not (it == None)) else (False))
        tmp = self
        tmp0_unsafeCast_0 = js('Int32Array')
        tmp.intArrayClass = PrimitiveKClassImpl(kotlin_Any_(tmp0_unsafeCast_0), 'IntArray', lambda it: (isIntArray(it)) if (not (it == None)) else (False))
        tmp = self
        tmp0_unsafeCast_0 = js('Array')
        tmp.longArrayClass = PrimitiveKClassImpl(kotlin_Any_(tmp0_unsafeCast_0), 'LongArray', lambda it: (isLongArray(it)) if (not (it == None)) else (False))
        tmp = self
        tmp0_unsafeCast_0 = js('Float32Array')
        tmp.floatArrayClass = PrimitiveKClassImpl(kotlin_Any_(tmp0_unsafeCast_0), 'FloatArray', lambda it: (isFloatArray(it)) if (not (it == None)) else (False))
        tmp = self
        tmp0_unsafeCast_0 = js('Float64Array')
        tmp.doubleArrayClass = PrimitiveKClassImpl(kotlin_Any_(tmp0_unsafeCast_0), 'DoubleArray', lambda it: (isDoubleArray(it)) if (not (it == None)) else (False))
    
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
        tmp0_elvis_lhs = functionClasses[arity]
        if tmp0_elvis_lhs == None:
            tmp0_unsafeCast_0_3 = js('Function')
            result_2 = PrimitiveKClassImpl(kotlin_Any_(tmp0_unsafeCast_0_3), str('Function') + str(arity), lambda it: visitExpressionFunctionBodyStatements_x2__If__Return_)
            tmp1_asDynamic_0_5 = functionClasses
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
    

PrimitiveClasses_instance = None
def PrimitiveClasses_getInstance():
    if PrimitiveClasses_instance == None:
        PrimitiveClasses_0()
    
    return PrimitiveClasses_instance

def functionClasses_init_():
    return fillArrayVal(Array(0), None)

def getKClass_0(jClass):
    if kotlin_Boolean(INVOKE(isArray(js('Array')), jClass)):
        tmp = getKClassM_0(kotlin_Any_(jClass))
    else:
        tmp = getKClass1_0(kotlin_Any_(jClass))
    
    return tmp

def getKClassM_0(jClasses):
    tmp0_subject = len(jClasses)
    if tmp0_subject == 1:
        tmp = getKClass1_0(jClasses[0])
    elif tmp0_subject == 0:
        tmp0_unsafeCast_0 = NothingKClassImpl_getInstance()
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
    else:
        tmp1_unsafeCast_0 = ErrorKClass()
        tmp = kotlin_Any_(tmp1_unsafeCast_0)
    
    return tmp

def getKClass1_0(jClass):
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

def getKClassFromExpression_0(e):
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
            tmp = getKClass_0(jsClass())
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
                tmp = getKClass1_0(jsClass)
            
            tmp = tmp
        
        tmp = tmp
    
    tmp1_unsafeCast_0 = tmp
    return kotlin_Any_(tmp1_unsafeCast_0)

class Appendable:
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
    
    def __init__(self):
        pass
    

def StringBuilder_init__Init_(capacity, _this):
    StringBuilder_init__Init__1(_this)
    return _this

def StringBuilder_init__Create_(capacity):
    return StringBuilder_init__Init_(capacity, Object_create())

def StringBuilder_init__Init__0(content, _this):
    super(toString_0(content))
    return _this

def StringBuilder_init__Create__0(content):
    return StringBuilder_init__Init__0(content, Object_create())

def StringBuilder_init__Init__1(_this):
    super('')
    return _this

def StringBuilder_init__Create__1():
    return StringBuilder_init__Init__1(Object_create())

def _set_string_(_this, _set___):
    _this.string = _set___

def _get_string_(_this):
    return _this.string

def checkReplaceRange(_this, startIndex, endIndex, length):
    if (True) if (startIndex < 0) else (startIndex > length):
        raise IndexOutOfBoundsException_init__Create__0(((str('startIndex: ') + str(startIndex)) + str(', length: ')) + str(length))
    
    if startIndex > endIndex:
        raise IllegalArgumentException_init__Create__0((((str('startIndex(') + str(startIndex)) + str(') > endIndex(')) + str(endIndex)) + str(')'))
    

class StringBuilder:
    def __init__(self, content):
        self.string = (content) if (not (content is undefined)) else ('')
    
    def _get_length__0_k_(self):
        tmp0_asDynamic_0 = self.string
        return kotlin_Int(length(tmp0_asDynamic_0))
    
    def get_ha5a7z_k_(self, index):
        tmp0_getOrElse_0 = self.string
        if (index <= _get_lastIndex__5()) if (index >= 0) else (False):
            tmp = charSequenceGet(tmp0_getOrElse_0, index)
        else:
            raise IndexOutOfBoundsException_init__Create__0((((str('index: ') + str(index)) + str(', length: ')) + str(self._get_length__0_k_())) + str('}'))
        
        return tmp
    
    def subSequence_27zxwg_k_(self, startIndex, endIndex):
        tmp0_substring_0 = self.string
        return kotlin_String(INVOKE(substring(tmp0_substring_0), startIndex, endIndex))
    
    def append_wi8o78_k_(self, value):
        tmp0_this = self
        tmp0_this.string = tmp0_this.string + value
        return self
    
    def append_v1o70a_k_(self, value):
        tmp0_this = self
        tmp0_this.string = tmp0_this.string + toString()
        return self
    
    def append_n5ylwa_k_(self, value, startIndex, endIndex):
        tmp0_elvis_lhs = value
        return self.appendRange_icedxh_k_(('null') if (tmp0_elvis_lhs == None) else (tmp0_elvis_lhs), startIndex, endIndex)
    
    def reverse_0_k_(self):
        reversed = ''
        index = (len(self.string) - 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
        while index >= 0:
            tmp = self.string
            tmp0 = index
            index = (tmp0 - 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
            low = charSequenceGet(tmp, tmp0)
            if (index >= 0) if (isLowSurrogate()) else (False):
                tmp = self.string
                tmp1 = index
                index = (tmp1 - 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
                high = charSequenceGet(tmp, tmp1)
                if isHighSurrogate():
                    reversed = (reversed + high) + low
                else:
                    reversed = (reversed + low) + high
                
            else:
                reversed = reversed + low
            
        
        self.string = reversed
        return self
    
    def append_wi7j7l_k_(self, value):
        tmp0_this = self
        tmp0_this.string = tmp0_this.string + toString()
        return self
    
    def append_vcj5fe_k_(self, value):
        tmp0_this = self
        tmp0_this.string = tmp0_this.string + value
        return self
    
    def append_84823_k_(self, value):
        tmp0_this = self
        tmp0_this.string = tmp0_this.string + concatToString()
        return self
    
    def append_6wfw3l_k_(self, value):
        return self.append_uch40_k_(value)
    
    def append_uch40_k_(self, value):
        tmp0_this = self
        tmp = tmp0_this
        tmp = tmp0_this.string
        tmp1_elvis_lhs = value
        tmp.string = tmp + (('null') if (tmp1_elvis_lhs == None) else (tmp1_elvis_lhs))
        return self
    
    def capacity_0_k_(self):
        return self._get_length__0_k_()
    
    def ensureCapacity_majfzk_k_(self, minimumCapacity):
        pass
    
    def indexOf_6wfw3l_k_(self, string):
        tmp0_asDynamic_0 = self.string
        return kotlin_Int(INVOKE(indexOf(tmp0_asDynamic_0), string))
    
    def indexOf_8i7b4u_k_(self, string, startIndex):
        tmp0_asDynamic_0 = self.string
        return kotlin_Int(INVOKE(indexOf(tmp0_asDynamic_0), string, startIndex))
    
    def lastIndexOf_6wfw3l_k_(self, string):
        tmp0_asDynamic_0 = self.string
        return kotlin_Int(INVOKE(lastIndexOf(tmp0_asDynamic_0), string))
    
    def lastIndexOf_8i7b4u_k_(self, string, startIndex):
        if charSequenceLength(string) == 0:
            tmp = startIndex < 0
        elif True:
            tmp = False
        
        if tmp:
            return -1
        
        tmp0_asDynamic_0 = self.string
        return kotlin_Int(INVOKE(lastIndexOf(tmp0_asDynamic_0), string, startIndex))
    
    def insert_sv7uuf_k_(self, index, value):
        Companion_getInstance().checkPositionIndex_rvwcgf_k_(index, self._get_length__0_k_())
        tmp = self
        tmp0_substring_0 = self.string
        tmp = kotlin_String(INVOKE(substring(tmp0_substring_0), 0, index)) + value
        tmp1_substring_0 = self.string
        tmp.string = tmp + kotlin_String(INVOKE(substring(tmp1_substring_0), index))
        return self
    
    def insert_259trv_k_(self, index, value):
        Companion_getInstance().checkPositionIndex_rvwcgf_k_(index, self._get_length__0_k_())
        tmp = self
        tmp0_substring_0 = self.string
        tmp = kotlin_String(INVOKE(substring(tmp0_substring_0), 0, index)) + value
        tmp1_substring_0 = self.string
        tmp.string = tmp + kotlin_String(INVOKE(substring(tmp1_substring_0), index))
        return self
    
    def insert_n2q82c_k_(self, index, value):
        Companion_getInstance().checkPositionIndex_rvwcgf_k_(index, self._get_length__0_k_())
        tmp = self
        tmp0_substring_0 = self.string
        tmp = kotlin_String(INVOKE(substring(tmp0_substring_0), 0, index)) + concatToString()
        tmp1_substring_0 = self.string
        tmp.string = tmp + kotlin_String(INVOKE(substring(tmp1_substring_0), index))
        return self
    
    def insert_59w5qx_k_(self, index, value):
        Companion_getInstance().checkPositionIndex_rvwcgf_k_(index, self._get_length__0_k_())
        tmp = self
        tmp0_substring_0 = self.string
        tmp = kotlin_String(INVOKE(substring(tmp0_substring_0), 0, index)) + toString()
        tmp1_substring_0 = self.string
        tmp.string = tmp + kotlin_String(INVOKE(substring(tmp1_substring_0), index))
        return self
    
    def insert_25ayri_k_(self, index, value):
        Companion_getInstance().checkPositionIndex_rvwcgf_k_(index, self._get_length__0_k_())
        tmp = self
        tmp0_substring_0 = self.string
        tmp = kotlin_String(INVOKE(substring(tmp0_substring_0), 0, index)) + toString()
        tmp1_substring_0 = self.string
        tmp.string = tmp + kotlin_String(INVOKE(substring(tmp1_substring_0), index))
        return self
    
    def insert_4wk0sg_k_(self, index, value):
        return self.insert_9z0klb_k_(index, value)
    
    def insert_9z0klb_k_(self, index, value):
        Companion_getInstance().checkPositionIndex_rvwcgf_k_(index, self._get_length__0_k_())
        tmp0_elvis_lhs = value
        toInsert = ('null') if (tmp0_elvis_lhs == None) else (tmp0_elvis_lhs)
        tmp = self
        tmp0_substring_0 = self.string
        tmp = kotlin_String(INVOKE(substring(tmp0_substring_0), 0, index)) + toInsert
        tmp1_substring_0 = self.string
        tmp.string = tmp + kotlin_String(INVOKE(substring(tmp1_substring_0), index))
        return self
    
    def setLength_majfzk_k_(self, newLength):
        if newLength < 0:
            raise IllegalArgumentException_init__Create__0((str('Negative new length: ') + str(newLength)) + str('.'))
        
        if newLength <= self._get_length__0_k_():
            tmp = self
            tmp0_substring_0 = self.string
            tmp.string = kotlin_String(INVOKE(substring(tmp0_substring_0), 0, newLength))
        else:
            inductionVariable = self._get_length__0_k_()
            if inductionVariable < newLength:
                while True:
                    i = inductionVariable
                    inductionVariable = (inductionVariable + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
                    tmp1_this = self
                    tmp1_this.string = tmp1_this.string + Char_0(0)
                    if inductionVariable < newLength:
                        break
                    
                
            
        
    
    def substring_ha5a7z_k_(self, startIndex):
        Companion_getInstance().checkPositionIndex_rvwcgf_k_(startIndex, self._get_length__0_k_())
        tmp0_substring_0 = self.string
        return kotlin_String(INVOKE(substring(tmp0_substring_0), startIndex))
    
    def substring_27zxwg_k_(self, startIndex, endIndex):
        Companion_getInstance().checkBoundsIndexes_zd700_k_(startIndex, endIndex, self._get_length__0_k_())
        tmp0_substring_0 = self.string
        return kotlin_String(INVOKE(substring(tmp0_substring_0), startIndex, endIndex))
    
    def trimToSize_sv8swh_k_(self):
        pass
    
    def toString(self):
        return self.string
    
    def clear_0_k_(self):
        self.string = ''
        return self
    
    def set_vljvec_k_(self, index, value):
        Companion_getInstance().checkElementIndex_rvwcgf_k_(index, self._get_length__0_k_())
        tmp = self
        tmp0_substring_0 = self.string
        tmp = kotlin_String(INVOKE(substring(tmp0_substring_0), 0, index)) + value
        tmp1_substring_0 = self.string
        tmp2_substring_0 = (index + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
        tmp.string = tmp + kotlin_String(INVOKE(substring(tmp1_substring_0), tmp2_substring_0))
    
    def setRange_sfallt_k_(self, startIndex, endIndex, value):
        checkReplaceRange(self, startIndex, endIndex, self._get_length__0_k_())
        tmp = self
        tmp0_substring_0 = self.string
        tmp = kotlin_String(INVOKE(substring(tmp0_substring_0), 0, startIndex)) + value
        tmp1_substring_0 = self.string
        tmp.string = tmp + kotlin_String(INVOKE(substring(tmp1_substring_0), endIndex))
        return self
    
    def deleteAt_ha5a7z_k_(self, index):
        Companion_getInstance().checkElementIndex_rvwcgf_k_(index, self._get_length__0_k_())
        tmp = self
        tmp0_substring_0 = self.string
        tmp = kotlin_String(INVOKE(substring(tmp0_substring_0), 0, index))
        tmp1_substring_0 = self.string
        tmp2_substring_0 = (index + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
        tmp.string = tmp + kotlin_String(INVOKE(substring(tmp1_substring_0), tmp2_substring_0))
        return self
    
    def deleteRange_27zxwg_k_(self, startIndex, endIndex):
        checkReplaceRange(self, startIndex, endIndex, self._get_length__0_k_())
        tmp = self
        tmp0_substring_0 = self.string
        tmp = kotlin_String(INVOKE(substring(tmp0_substring_0), 0, startIndex))
        tmp1_substring_0 = self.string
        tmp.string = tmp + kotlin_String(INVOKE(substring(tmp1_substring_0), endIndex))
        return self
    
    def toCharArray_tnuj0b_k_(self, destination, destinationOffset, startIndex, endIndex):
        Companion_getInstance().checkBoundsIndexes_zd700_k_(startIndex, endIndex, self._get_length__0_k_())
        Companion_getInstance().checkBoundsIndexes_zd700_k_(destinationOffset, ((destinationOffset + endIndex).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000) - startIndex).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000), len(destination))
        dstIndex = destinationOffset
        inductionVariable = startIndex
        if inductionVariable < endIndex:
            while True:
                index = inductionVariable
                inductionVariable = (inductionVariable + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
                tmp1 = dstIndex
                dstIndex = (tmp1 + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
                destination.__setitem__(tmp1, charSequenceGet(self.string, index))
                if inductionVariable < endIndex:
                    break
                
            
        
    
    def toCharArray_default_pd3mhx_k_(self, destination, destinationOffset, startIndex, endIndex, _mask0, _handler):
        if not (_mask0 & 2 == 0):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
        
        if not (_mask0 & 4 == 0):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
        
        if not (_mask0 & 8 == 0):
            visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
        
        return self.toCharArray_tnuj0b_k_(destination, destinationOffset, startIndex, endIndex)
    
    def appendRange_4l12y3_k_(self, value, startIndex, endIndex):
        tmp0_this = self
        tmp0_this.string = tmp0_this.string + concatToString_0(startIndex, endIndex)
        return self
    
    def appendRange_icedxh_k_(self, value, startIndex, endIndex):
        stringCsq = toString_0(value)
        Companion_getInstance().checkBoundsIndexes_zd700_k_(startIndex, endIndex, len(stringCsq))
        tmp0_this = self
        tmp = tmp0_this
        tmp = tmp0_this.string
        tmp.string = tmp + kotlin_String(INVOKE(substring(stringCsq), startIndex, endIndex))
        return self
    
    def insertRange_nw7vlg_k_(self, index, value, startIndex, endIndex):
        Companion_getInstance().checkPositionIndex_rvwcgf_k_(index, self._get_length__0_k_())
        tmp = self
        tmp0_substring_0 = self.string
        tmp = kotlin_String(INVOKE(substring(tmp0_substring_0), 0, index)) + concatToString_0(startIndex, endIndex)
        tmp1_substring_0 = self.string
        tmp.string = tmp + kotlin_String(INVOKE(substring(tmp1_substring_0), index))
        return self
    
    def insertRange_nws7cq_k_(self, index, value, startIndex, endIndex):
        Companion_getInstance().checkPositionIndex_rvwcgf_k_(index, self._get_length__0_k_())
        stringCsq = toString_0(value)
        Companion_getInstance().checkBoundsIndexes_zd700_k_(startIndex, endIndex, len(stringCsq))
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
    Companion_getInstance_17()
    containsLower = Char_0(56320)
    Companion_getInstance_17()
    if self <= Char_0(57343):
        tmp = containsLower <= self
    elif True:
        tmp = False
    
    return tmp

def isHighSurrogate():
    Companion_getInstance_17()
    containsLower = Char_0(55296)
    Companion_getInstance_17()
    if self <= Char_0(56319):
        tmp = containsLower <= self
    elif True:
        tmp = False
    
    return tmp

def checkRadix(radix):
    if not ((radix <= 36) if (2 <= radix) else (False)):
        raise IllegalArgumentException_init__Create__0((str('radix ') + str(radix)) + str(' was not in valid range 2..36'))
    
    return radix

def _get_STRING_CASE_INSENSITIVE_ORDER_():
    return STRING_CASE_INSENSITIVE_ORDER

STRING_CASE_INSENSITIVE_ORDER = None
def nativeLastIndexOf(str, fromIndex):
    return kotlin_Int(INVOKE(lastIndexOf(self), str, fromIndex))

def substring(startIndex, endIndex):
    return kotlin_String(INVOKE(substring(self), startIndex, endIndex))

def substring_0(startIndex):
    return kotlin_String(INVOKE(substring(self), startIndex))

def compareTo(other, ignoreCase):
    if ignoreCase:
        n1 = len(self)
        n2 = len(other)
        min = visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl.min(*(n1, n2))
        if min == 0:
            return (n1 - n2).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
        
        start = 0
        while True:
            tmp0_minOf_0 = (start + 16).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
            end = visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl.min(*(tmp0_minOf_0, min))
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
                        return compareTo_0(s1, s2)
                    
                
            
            if end == min:
                break
            
            start = end
        
        return (n1 - n2).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
    else:
        return compareTo_0(self, other)
    

def compareTo_default(other, ignoreCase, _mask0, _handler):
    if not (_mask0 & 2 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    return compareTo(other, ignoreCase)

def uppercase():
    return kotlin_String(INVOKE(toUpperCase(self)))

def lowercase():
    return kotlin_String(INVOKE(toLowerCase(self)))

def concatToString():
    result = ''
    indexedObject = self
    inductionVariable = 0
    last = len(indexedObject)
    while inductionVariable < last:
        char = indexedObject[inductionVariable]
        inductionVariable = (inductionVariable + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
        result = result + char
    
    return result

def concatToString_0(startIndex, endIndex):
    Companion_getInstance().checkBoundsIndexes_zd700_k_(startIndex, endIndex, len(self))
    result = ''
    inductionVariable = startIndex
    if inductionVariable < endIndex:
        while True:
            index = inductionVariable
            inductionVariable = (inductionVariable + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
            result = result + self[index]
            if inductionVariable < endIndex:
                break
            
        
    
    return result

def concatToString_default(startIndex, endIndex, _mask0, _handler):
    if not (_mask0 & 1 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    if not (_mask0 & 2 == 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrSetValueImpl
    
    return concatToString_0(startIndex, endIndex)

def toUpperCase():
    return kotlin_String(INVOKE(toUpperCase(self)))

class sam_kotlin_Comparator_0:
    def __init__(self, function):
        self.function = function
    
    def compare_1qgdm_k_(self, a, b):
        return self.function(a, b)
    
    def compare(self, a, b):
        return self.compare_1qgdm_k_(a, b)
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def STRING_CASE_INSENSITIVE_ORDER_init_():
    tmp = lambda a, b: compareTo(b, True)
    return sam_kotlin_Comparator_0(tmp)

def _get_REPLACEMENT_BYTE_SEQUENCE_():
    return REPLACEMENT_BYTE_SEQUENCE

REPLACEMENT_BYTE_SEQUENCE = None
def REPLACEMENT_BYTE_SEQUENCE_init_():
    tmp0_byteArrayOf_0 = (-17, -65, -67)
    return tmp0_byteArrayOf_0

def _get_value_(_this):
    return _this.value

class Companion_18:
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

class Char_0:
    def __init__(self, code):
        Companion_getInstance_17()
        tmp = self
        tmp.value = _UShort___get_data__impl_(code) & 65535
    
    def compareTo_wi8o78_k_(self, other):
        return (self.value - other.value).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
    
    def compareTo_2c5_k_(self, other):
        return self.compareTo_wi8o78_k_((kotlin_Char(other)) if (visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean) else (THROW_CCE()))
    
    def plus_ha5a7z_k_(self, other):
        return numberToChar((self.value + other).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))
    
    def minus_wi8o78_k_(self, other):
        return (self.value - other.value).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
    
    def minus_ha5a7z_k_(self, other):
        return numberToChar((self.value - other).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))
    
    def inc_0_k_(self):
        return numberToChar((self.value + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))
    
    def dec_0_k_(self):
        return numberToChar((self.value - 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))
    
    def rangeTo_wi8o78_k_(self, other):
        return CharRange(self, other)
    
    def toByte_0_k_(self):
        return self.value.__add__(0x80).__and__(0xff).__sub__(0x80)
    
    def toChar_0_k_(self):
        return self
    
    def toShort_0_k_(self):
        return self.value.__add__(0x8000).__and__(0xffff).__sub__(0x8000)
    
    def toInt_0_k_(self):
        return self.value
    
    def toLong_0_k_(self):
        return self.value
    
    def toFloat_0_k_(self):
        return kotlin_Float(self.value)
    
    def toDouble_0_k_(self):
        return kotlin_Double(self.value)
    
    def equals(self, other):
        if other is self:
            return True
        
        if not visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
            return False
        
        return self.value == kotlin_Char(other).value
    
    def hashCode(self):
        return self.value
    
    def toString(self):
        tmp0_unsafeCast_0 = INVOKE(fromCharCode(js('String')), self.value)
        return kotlin_Any_(tmp0_unsafeCast_0)
    

class Iterable:
    def iterator_0_k_(self):
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
    
    def __init__(self):
        pass
    

class List:
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
    
    def __init__(self):
        pass
    

class MutableList:
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
    
    def __init__(self):
        pass
    

class MutableCollection:
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
    
    def __init__(self):
        pass
    

class MutableIterable:
    def iterator_0_k_(self):
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
    
    def __init__(self):
        pass
    

class Entry:
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
    
    def __init__(self):
        pass
    

class Map_0:
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
    
    def __init__(self):
        pass
    

class MutableSet:
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
    
    def __init__(self):
        pass
    

class MutableEntry:
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
    
    def __init__(self):
        pass
    

class MutableMap:
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
    
    def __init__(self):
        pass
    

class Companion_19:
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

class Enum:
    def __init__(self, name, ordinal):
        Companion_getInstance_18()
        self.name = name
        self.ordinal = ordinal
    
    def _get_name__0_k_(self):
        return self.name
    
    def _get_ordinal__0_k_(self):
        return self.ordinal
    
    def compareTo_2bq_k_(self, other):
        return compareTo_0(self.ordinal, other.ordinal)
    
    def compareTo_2c5_k_(self, other):
        return self.compareTo_2bq_k_((E(other)) if (visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean) else (THROW_CCE()))
    
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

def toString():
    tmp0_safe_receiver = self
    tmp1_elvis_lhs = (None) if (tmp0_safe_receiver == None) else (toString_0(tmp0_safe_receiver))
    return ('null') if (tmp1_elvis_lhs == None) else (tmp1_elvis_lhs)

def plus(other):
    tmp2_safe_receiver = self
    tmp3_elvis_lhs = (None) if (tmp2_safe_receiver == None) else (toString_0(tmp2_safe_receiver))
    tmp = ('null') if (tmp3_elvis_lhs == None) else (tmp3_elvis_lhs)
    tmp0_safe_receiver = other
    tmp1_elvis_lhs = (None) if (tmp0_safe_receiver == None) else (toString_0(tmp0_safe_receiver))
    return tmp + (('null') if (tmp1_elvis_lhs == None) else (tmp1_elvis_lhs))

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
    inductionVariable = 0
    last = (len(array) - 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
    if inductionVariable <= last:
        while True:
            i = inductionVariable
            inductionVariable = (inductionVariable + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
            array.__setitem__(i, initValue)
            if not (i == last):
                break
            
        
    
    return array

def arrayWithFun(size, init):
    tmp0_fillArrayFun_0 = Array(size)
    result_1 = kotlin_Any_(tmp0_fillArrayFun_0)
    i_2 = 0
    while not (i_2 == len(result_1)):
        result_1.__setitem__(i_2, init(i_2))
        i_2 = (i_2 + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
        Unit_getInstance()
    
    return result_1

def fillArrayFun(array, init):
    result = kotlin_Any_(array)
    i = 0
    while not (i == len(result)):
        result.__setitem__(i, init(i))
        i = (i + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
        Unit_getInstance()
    
    return result

def arrayIterator(array):
    return _no_name_provided__0(array)

def booleanArrayIterator(array):
    return _no_name_provided__2(array)

def charArrayIterator(array):
    return _no_name_provided__3(array)

def byteArrayIterator(array):
    return _no_name_provided__4(array)

def shortArrayIterator(array):
    return _no_name_provided__5(array)

def intArrayIterator(array):
    return _no_name_provided__6(array)

def floatArrayIterator(array):
    return _no_name_provided__7(array)

def longArrayIterator(array):
    return _no_name_provided__8(array)

def doubleArrayIterator(array):
    return _no_name_provided__9(array)

def booleanArray(size):
    tmp0_withType_0 = fillArrayVal(Array(size), False)
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    tmp1_unsafeCast_0 = tmp0_withType_0
    return kotlin_Any_(tmp1_unsafeCast_0)

def charArray(size):
    tmp = Array(size)
    Companion_getInstance_17()
    tmp0__get_code__0_1 = Char_0(0)
    if 0 < tmp0__get_code__0_1.toInt_0_k_():
        tmp = True
    elif True:
        Companion_getInstance_17()
        tmp1__get_code__0_2 = Char_0(65535)
        tmp = 0 > tmp1__get_code__0_2.toInt_0_k_()
    
    if tmp:
        raise IllegalArgumentException_init__Create__0('Invalid Char code: 0')
    
    tmp0_withType_0 = fillArrayVal(tmp, Char_0(0))
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    tmp1_unsafeCast_0 = tmp0_withType_0
    return kotlin_Any_(tmp1_unsafeCast_0)

def longArray(size):
    tmp0_withType_0 = fillArrayVal(Array(size), 0)
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    tmp1_unsafeCast_0 = tmp0_withType_0
    return kotlin_Any_(tmp1_unsafeCast_0)

def booleanArrayOf_0(arr):
    tmp0_withType_0 = INVOKE(slice(arr))
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    tmp1_unsafeCast_0 = tmp0_withType_0
    return kotlin_Any_(tmp1_unsafeCast_0)

def charArrayOf_0(arr):
    tmp0_withType_0 = INVOKE(slice(arr))
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    tmp1_unsafeCast_0 = tmp0_withType_0
    return kotlin_Any_(tmp1_unsafeCast_0)

def longArrayOf_0(arr):
    tmp0_withType_0 = INVOKE(slice(arr))
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    tmp1_unsafeCast_0 = tmp0_withType_0
    return kotlin_Any_(tmp1_unsafeCast_0)

class _no_name_provided__0:
    def __init__(self, _array):
        self._array = _array
        self.index = 0
    
    def _set_index__majfzk_k_(self, _set___):
        self.index = _set___
    
    def _get_index__0_k_(self):
        return self.index
    
    def hasNext_0_k_(self):
        return not (self.index == len(self._array))
    
    def next_0_k_(self):
        if not (self.index == len(self._array)):
            tmp0_this = self
            tmp1 = tmp0_this.index
            tmp0_this.index = (tmp1 + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
            tmp = self._array[tmp1]
        else:
            raise NoSuchElementException_init__Create__0(str(self.index))
        
        return tmp
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class _no_name_provided__2:
    def __init__(self, _array):
        self._array = _array
        super()
        self.index = 0
    
    def _set_index__majfzk_k_(self, _set___):
        self.index = _set___
    
    def _get_index__0_k_(self):
        return self.index
    
    def hasNext_0_k_(self):
        return not (self.index == len(self._array))
    
    def nextBoolean_0_k_(self):
        if not (self.index == len(self._array)):
            tmp0_this = self
            tmp1 = tmp0_this.index
            tmp0_this.index = (tmp1 + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
            tmp = self._array[tmp1]
        else:
            raise NoSuchElementException_init__Create__0(str(self.index))
        
        return tmp
    
    def next_0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class _no_name_provided__3:
    def __init__(self, _array):
        self._array = _array
        super()
        self.index = 0
    
    def _set_index__majfzk_k_(self, _set___):
        self.index = _set___
    
    def _get_index__0_k_(self):
        return self.index
    
    def hasNext_0_k_(self):
        return not (self.index == len(self._array))
    
    def nextChar_0_k_(self):
        if not (self.index == len(self._array)):
            tmp0_this = self
            tmp1 = tmp0_this.index
            tmp0_this.index = (tmp1 + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
            tmp = self._array[tmp1]
        else:
            raise NoSuchElementException_init__Create__0(str(self.index))
        
        return tmp
    
    def next_0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class _no_name_provided__4:
    def __init__(self, _array):
        self._array = _array
        super()
        self.index = 0
    
    def _set_index__majfzk_k_(self, _set___):
        self.index = _set___
    
    def _get_index__0_k_(self):
        return self.index
    
    def hasNext_0_k_(self):
        return not (self.index == len(self._array))
    
    def nextByte_0_k_(self):
        if not (self.index == len(self._array)):
            tmp0_this = self
            tmp1 = tmp0_this.index
            tmp0_this.index = (tmp1 + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
            tmp = self._array[tmp1]
        else:
            raise NoSuchElementException_init__Create__0(str(self.index))
        
        return tmp
    
    def next_0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class _no_name_provided__5:
    def __init__(self, _array):
        self._array = _array
        super()
        self.index = 0
    
    def _set_index__majfzk_k_(self, _set___):
        self.index = _set___
    
    def _get_index__0_k_(self):
        return self.index
    
    def hasNext_0_k_(self):
        return not (self.index == len(self._array))
    
    def nextShort_0_k_(self):
        if not (self.index == len(self._array)):
            tmp0_this = self
            tmp1 = tmp0_this.index
            tmp0_this.index = (tmp1 + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
            tmp = self._array[tmp1]
        else:
            raise NoSuchElementException_init__Create__0(str(self.index))
        
        return tmp
    
    def next_0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class _no_name_provided__6:
    def __init__(self, _array):
        self._array = _array
        super()
        self.index = 0
    
    def _set_index__majfzk_k_(self, _set___):
        self.index = _set___
    
    def _get_index__0_k_(self):
        return self.index
    
    def hasNext_0_k_(self):
        return not (self.index == len(self._array))
    
    def nextInt_0_k_(self):
        if not (self.index == len(self._array)):
            tmp0_this = self
            tmp1 = tmp0_this.index
            tmp0_this.index = (tmp1 + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
            tmp = self._array[tmp1]
        else:
            raise NoSuchElementException_init__Create__0(str(self.index))
        
        return tmp
    
    def next_0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class _no_name_provided__7:
    def __init__(self, _array):
        self._array = _array
        super()
        self.index = 0
    
    def _set_index__majfzk_k_(self, _set___):
        self.index = _set___
    
    def _get_index__0_k_(self):
        return self.index
    
    def hasNext_0_k_(self):
        return not (self.index == len(self._array))
    
    def nextFloat_0_k_(self):
        if not (self.index == len(self._array)):
            tmp0_this = self
            tmp1 = tmp0_this.index
            tmp0_this.index = (tmp1 + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
            tmp = self._array[tmp1]
        else:
            raise NoSuchElementException_init__Create__0(str(self.index))
        
        return tmp
    
    def next_0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class _no_name_provided__8:
    def __init__(self, _array):
        self._array = _array
        super()
        self.index = 0
    
    def _set_index__majfzk_k_(self, _set___):
        self.index = _set___
    
    def _get_index__0_k_(self):
        return self.index
    
    def hasNext_0_k_(self):
        return not (self.index == len(self._array))
    
    def nextLong_0_k_(self):
        if not (self.index == len(self._array)):
            tmp0_this = self
            tmp1 = tmp0_this.index
            tmp0_this.index = (tmp1 + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
            tmp = self._array[tmp1]
        else:
            raise NoSuchElementException_init__Create__0(str(self.index))
        
        return tmp
    
    def next_0_k_(self):
        pass
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

class _no_name_provided__9:
    def __init__(self, _array):
        self._array = _array
        super()
        self.index = 0
    
    def _set_index__majfzk_k_(self, _set___):
        self.index = _set___
    
    def _get_index__0_k_(self):
        return self.index
    
    def hasNext_0_k_(self):
        return not (self.index == len(self._array))
    
    def nextDouble_0_k_(self):
        if not (self.index == len(self._array)):
            tmp0_this = self
            tmp1 = tmp0_this.index
            tmp0_this.index = (tmp1 + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
            tmp = self._array[tmp1]
        else:
            raise NoSuchElementException_init__Create__0(str(self.index))
        
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
    tmp0_unsafeCast_0 = jsBitwiseOr(obj, 0)
    if kotlin_Any_(tmp0_unsafeCast_0) is obj:
        return obj.__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
    
    bufFloat64.__setitem__(0, obj)
    return (imul(bufInt32[highIndex], 31) + bufInt32[lowIndex]).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)

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
    bufFloat64.__setitem__(0, -1.0)
    return (1) if (not (bufInt32[0] == 0)) else (0)

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
        Companion_getInstance_17()
        tmp0__get_code__0_1 = Char_0(0)
        if tmp1_Char_0 < tmp0__get_code__0_1.toInt_0_k_():
            tmp = True
        elif True:
            Companion_getInstance_17()
            tmp1__get_code__0_2 = Char_0(65535)
            tmp = tmp1_Char_0 > tmp1__get_code__0_2.toInt_0_k_()
        
        if tmp:
            raise IllegalArgumentException_init__Create__0(str('Invalid Char code: ') + str(tmp1_Char_0))
        
        tmp = numberToChar(tmp1_Char_0)
    else:
        tmp = a.get_ha5a7z_k_(index)
    
    return tmp

def isString(a):
    return jsTypeOf(a) == 'string'

def charSequenceLength(a):
    if isString(a):
        tmp0_unsafeCast_0 = length(a)
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
    else:
        tmp = a._get_length__0_k_()
    
    return tmp

def charSequenceSubSequence(a, startIndex, endIndex):
    if isString(a):
        tmp0_unsafeCast_0 = INVOKE(substring(a), startIndex, endIndex)
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
    else:
        tmp = a.subSequence_27zxwg_k_(startIndex, endIndex)
    
    return tmp

def arrayToString(array):
    return joinToString_default(', ', '[', ']', 0, None, lambda it: toString_0(it), 24, None)

def compareTo_0(a, b):
    tmp0_subject = jsTypeOf(a)
    if tmp0_subject == 'number':
        if jsTypeOf(b) == 'number':
            tmp = doubleCompareTo(a, b)
        elif visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
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
    return a.compareTo_2c5_k_(b)

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

OBJECT_HASH_CODE_PROPERTY_NAME = None
def _get_POW_2_32_():
    return POW_2_32

POW_2_32 = None
def toString_0(o):
    if EQEQ(o, None):
        tmp = 'null'
    elif isArrayish(o):
        tmp = '[...]'
    else:
        tmp0_unsafeCast_0 = INVOKE(toString(o))
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
    
    return tmp

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
    last = (length - 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
    if inductionVariable <= last:
        while True:
            i = inductionVariable
            inductionVariable = (inductionVariable + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
            code = kotlin_Int(INVOKE(charCodeAt(str), i))
            hash = (imul(hash, 31) + code).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
            if not (i == last):
                break
            
        
    
    return hash

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
    raise IllegalStateException_init__Create__0('Should be lowered')

def unboxIntrinsic(x):
    raise IllegalStateException_init__Create__0('Should be lowered')

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
            tmp = (undefined) if (tmp1_elvis_lhs == None) else (tmp1_elvis_lhs)
        
        tmp = tmp
    else:
        tmp2_elvis_lhs = message
        tmp = (undefined) if (tmp2_elvis_lhs == None) else (tmp2_elvis_lhs)
    
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    return kotlin_Any_(throwable)

def isUndefined(value):
    return EQEQEQ(value, undefined)

def extendThrowable(this_, message, cause):
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
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
        
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    
    if not hasOwnPrototypeProperty(kotlin_Any(this_), 'cause'):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl

def hasOwnPrototypeProperty(o, name):
    tmp0_unsafeCast_0 = INVOKE(hasOwnProperty(visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl.getPrototypeOf(o)), name)
    return kotlin_Any_(tmp0_unsafeCast_0)

def getContinuation():
    raise Exception_init__Create__0('Implemented as intrinsic')

def returnIfSuspended(argument):
    raise Exception_init__Create__0('Implemented as intrinsic')

def suspendCoroutineUninterceptedOrReturnJS(block):
    return block(getContinuation())

def getCoroutineContext():
    return getContinuation()._get_context__0_k_()

def unreachableDeclarationLog():
    tmp0_asDynamic_0 = console
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl

def unreachableDeclarationException():
    raise Error('Unreachable declaration')

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
    raise UninitializedPropertyAccessException_init__Create__0((str('lateinit property ') + str(name)) + str(' has not been initialized'))

def throwKotlinNothingValueException():
    raise KotlinNothingValueException_init__Create_()

def THROW_ISE():
    raise IllegalStateException_init__Create_()

def THROW_IAE(msg):
    raise IllegalArgumentException_init__Create__0(msg)

def emptyArray():
    return kotlin_Array_T_(js('[]'))

class JsFun:
    def __init__(self, code):
        self.code = code
    
    def _get_code__0_k_(self):
        return self.code
    
    def equals(self, other):
        pass
    
    def hashCode(self):
        pass
    
    def toString(self):
        pass
    

def enumValueOfIntrinsic(name):
    raise IllegalStateException_init__Create__0('Should be replaced by compiler')

def enumValuesIntrinsic():
    raise IllegalStateException_init__Create__0('Should be replaced by compiler')

class Companion_20:
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

class Long:
    def __init__(self, low, high):
        Companion_getInstance_19()
        super()
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
        return compare(other)
    
    def compareTo_2c5_k_(self, other):
        return self.compareTo_wiekkq_k_((kotlin_Long(other)) if (visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean) else (THROW_CCE()))
    
    def compareTo_dbmacu_k_(self, other):
        return compareTo_0(self.toFloat_0_k_(), other)
    
    def compareTo_e2tf9d_k_(self, other):
        return compareTo_0(self.toDouble_0_k_(), other)
    
    def plus_wi8e9i_k_(self, other):
        return (self + other).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)
    
    def plus_dip2j2_k_(self, other):
        return (self + other).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)
    
    def plus_ha5a7z_k_(self, other):
        return (self + other).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)
    
    def plus_wiekkq_k_(self, other):
        return add(other)
    
    def plus_dbmacu_k_(self, other):
        return self.toFloat_0_k_() + other
    
    def plus_e2tf9d_k_(self, other):
        return self.toDouble_0_k_() + other
    
    def minus_wi8e9i_k_(self, other):
        return (self - other).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)
    
    def minus_dip2j2_k_(self, other):
        return (self - other).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)
    
    def minus_ha5a7z_k_(self, other):
        return (self - other).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)
    
    def minus_wiekkq_k_(self, other):
        return subtract(other)
    
    def minus_dbmacu_k_(self, other):
        return self.toFloat_0_k_() - other
    
    def minus_e2tf9d_k_(self, other):
        return self.toDouble_0_k_() - other
    
    def times_wi8e9i_k_(self, other):
        return (self * other).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)
    
    def times_dip2j2_k_(self, other):
        return (self * other).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)
    
    def times_ha5a7z_k_(self, other):
        return (self * other).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)
    
    def times_wiekkq_k_(self, other):
        return multiply(other)
    
    def times_dbmacu_k_(self, other):
        return self.toFloat_0_k_() * other
    
    def times_e2tf9d_k_(self, other):
        return self.toDouble_0_k_() * other
    
    def div_wi8e9i_k_(self, other):
        return (self // other).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)
    
    def div_dip2j2_k_(self, other):
        return (self // other).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)
    
    def div_ha5a7z_k_(self, other):
        return (self // other).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)
    
    def div_wiekkq_k_(self, other):
        return divide(other)
    
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
        return modulo(other)
    
    def rem_dbmacu_k_(self, other):
        return self.toFloat_0_k_() % other
    
    def rem_e2tf9d_k_(self, other):
        return self.toDouble_0_k_() % other
    
    def inc_0_k_(self):
        return (self + 1).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)
    
    def dec_0_k_(self):
        return (self - 1).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)
    
    def unaryPlus_0_k_(self):
        return self
    
    def unaryMinus_0_k_(self):
        return (~self + 1).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)
    
    def rangeTo_wi8e9i_k_(self, other):
        return numberRangeToLong(self, other)
    
    def rangeTo_dip2j2_k_(self, other):
        return numberRangeToLong(self, other)
    
    def rangeTo_ha5a7z_k_(self, other):
        return numberRangeToLong(self, other)
    
    def rangeTo_wiekkq_k_(self, other):
        return LongRange(self, other)
    
    def shl_ha5a7z_k_(self, bitCount):
        return shiftLeft(bitCount)
    
    def shr_ha5a7z_k_(self, bitCount):
        return shiftRight(bitCount)
    
    def ushr_ha5a7z_k_(self, bitCount):
        return shiftRightUnsigned(bitCount)
    
    def and_wiekkq_k_(self, other):
        return Long(self.low & other.low, self.high & other.high)
    
    def or_wiekkq_k_(self, other):
        return Long(self.low | other.low, self.high | other.high)
    
    def xor_wiekkq_k_(self, other):
        return Long(self.low ^ other.low, self.high ^ other.high)
    
    def inv_0_k_(self):
        return Long(~self.low, ~self.high)
    
    def toByte_0_k_(self):
        return self.low.__add__(0x80).__and__(0xff).__sub__(0x80)
    
    def toChar_0_k_(self):
        return numberToChar(self.low)
    
    def toShort_0_k_(self):
        return self.low.__add__(0x8000).__and__(0xffff).__sub__(0x8000)
    
    def toInt_0_k_(self):
        return self.low
    
    def toLong_0_k_(self):
        return self
    
    def toFloat_0_k_(self):
        return kotlin_Float(self.toDouble_0_k_())
    
    def toDouble_0_k_(self):
        return toNumber()
    
    def valueOf(self):
        return self.toDouble_0_k_()
    
    def equals(self, other):
        if visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
            tmp = equalsLong(kotlin_Long(other))
        elif True:
            tmp = False
        
        return tmp
    
    def hashCode(self):
        return hashCode_0(self)
    
    def toString(self):
        return toStringImpl(10)
    

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
def compare(other):
    if equalsLong(other):
        return 0
    
    thisNeg = isNegative()
    otherNeg = isNegative()
    return (-1) if ((not otherNeg) if (thisNeg) else (False)) else ((1) if ((otherNeg) if (not thisNeg) else (False)) else ((-1) if (isNegative()) else (1)))

def add(other):
    a48 = (self.high & 0xffff_ffff) >> 16
    a32 = self.high & 65535
    a16 = (self.low & 0xffff_ffff) >> 16
    a00 = self.low & 65535
    b48 = (other.high & 0xffff_ffff) >> 16
    b32 = other.high & 65535
    b16 = (other.low & 0xffff_ffff) >> 16
    b00 = other.low & 65535
    c48 = 0
    c32 = 0
    c16 = 0
    c00 = 0
    c00 = (c00 + (a00 + b00).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
    c16 = (c16 + ((c00 & 0xffff_ffff) >> 16)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
    c00 = c00 & 65535
    c16 = (c16 + (a16 + b16).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
    c32 = (c32 + ((c16 & 0xffff_ffff) >> 16)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
    c16 = c16 & 65535
    c32 = (c32 + (a32 + b32).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
    c48 = (c48 + ((c32 & 0xffff_ffff) >> 16)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
    c32 = c32 & 65535
    c48 = (c48 + (a48 + b48).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
    c48 = c48 & 65535
    return Long((c16 << 16).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000) | c00, (c48 << 16).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000) | c32)

def subtract(other):
    return add((-other).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))

def multiply(other):
    if isZero():
        return ZERO
    elif isZero():
        return ZERO
    
    if equalsLong(MIN_VALUE):
        return (MIN_VALUE) if (isOdd()) else (ZERO)
    elif equalsLong(MIN_VALUE):
        return (MIN_VALUE) if (isOdd()) else (ZERO)
    
    if isNegative():
        if isNegative():
            tmp = multiply(negate())
        else:
            tmp = negate()
        
        return tmp
    elif isNegative():
        return negate()
    
    if (lessThan(TWO_PWR_24_)) if (lessThan(TWO_PWR_24_)) else (False):
        return fromNumber(toNumber() * toNumber())
    
    a48 = (self.high & 0xffff_ffff) >> 16
    a32 = self.high & 65535
    a16 = (self.low & 0xffff_ffff) >> 16
    a00 = self.low & 65535
    b48 = (other.high & 0xffff_ffff) >> 16
    b32 = other.high & 65535
    b16 = (other.low & 0xffff_ffff) >> 16
    b00 = other.low & 65535
    c48 = 0
    c32 = 0
    c16 = 0
    c00 = 0
    c00 = (c00 + imul(a00, b00)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
    c16 = (c16 + ((c00 & 0xffff_ffff) >> 16)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
    c00 = c00 & 65535
    c16 = (c16 + imul(a16, b00)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
    c32 = (c32 + ((c16 & 0xffff_ffff) >> 16)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
    c16 = c16 & 65535
    c16 = (c16 + imul(a00, b16)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
    c32 = (c32 + ((c16 & 0xffff_ffff) >> 16)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
    c16 = c16 & 65535
    c32 = (c32 + imul(a32, b00)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
    c48 = (c48 + ((c32 & 0xffff_ffff) >> 16)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
    c32 = c32 & 65535
    c32 = (c32 + imul(a16, b16)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
    c48 = (c48 + ((c32 & 0xffff_ffff) >> 16)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
    c32 = c32 & 65535
    c32 = (c32 + imul(a00, b32)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
    c48 = (c48 + ((c32 & 0xffff_ffff) >> 16)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
    c32 = c32 & 65535
    c48 = (c48 + (((imul(a48, b00) + imul(a32, b16)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000) + imul(a16, b32)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000) + imul(a00, b48)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
    c48 = c48 & 65535
    return Long((c16 << 16).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000) | c00, (c48 << 16).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000) | c32)

def divide(other):
    if isZero():
        raise Exception_init__Create__0('division by zero')
    elif isZero():
        return ZERO
    
    if equalsLong(MIN_VALUE):
        if (True) if (equalsLong(ONE)) else (equalsLong(NEG_ONE)):
            return MIN_VALUE
        elif equalsLong(MIN_VALUE):
            return ONE
        else:
            halfThis = shiftRight(1)
            approx = shiftLeft(1)
            if equalsLong(ZERO):
                return (ONE) if (isNegative()) else (NEG_ONE)
            else:
                rem = subtract(multiply(approx))
                return add((rem // other).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000))
            
        
    elif equalsLong(MIN_VALUE):
        return ZERO
    
    if isNegative():
        if isNegative():
            tmp = (negate() // negate()).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)
        else:
            tmp = negate()
        
        return tmp
    elif isNegative():
        return negate()
    
    res = ZERO
    rem = self
    while greaterThanOrEqual(other):
        approxDouble = toNumber() / toNumber()
        approx2 = visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl.max(*(1.0, visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl.floor(approxDouble)))
        log2 = visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl.ceil(visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl.log(approx2) / LN2)
        delta = (1.0) if (log2 <= 48.0) else (visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl.pow(2.0, log2 - 48))
        approxRes = fromNumber(approx2)
        approxRem = multiply(other)
        while (True) if (isNegative()) else (greaterThan(rem)):
            approx2 = approx2 - delta
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
    numBits = numBits & 63
    if numBits == 0:
        return self
    elif numBits < 32:
        return Long((self.low << numBits).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000), (self.high << numBits).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000) | ((self.low & 0xffff_ffff) >> (32 - numBits).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)))
    else:
        return Long(0, (self.low << (numBits - 32).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))
    

def shiftRight(numBits):
    numBits = numBits & 63
    if numBits == 0:
        return self
    elif numBits < 32:
        return Long(((self.low & 0xffff_ffff) >> numBits) | (self.high << (32 - numBits).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000), self.high >> numBits)
    else:
        return Long(self.high >> (numBits - 32).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000), (0) if (self.high >= 0) else (-1))
    

def shiftRightUnsigned(numBits):
    numBits = numBits & 63
    if numBits == 0:
        return self
    elif numBits < 32:
        return Long(((self.low & 0xffff_ffff) >> numBits) | (self.high << (32 - numBits).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000), (self.high & 0xffff_ffff) >> numBits)
    else:
        if numBits == 32:
            tmp = Long(self.high, 0)
        else:
            tmp = Long((self.high & 0xffff_ffff) >> (numBits - 32).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000), 0)
        
        return tmp
    

def toNumber():
    return (self.high * 4.294967296E9) + getLowBitsUnsigned()

def equalsLong(other):
    return (self.low == other.low) if (self.high == other.high) else (False)

def hashCode_0(l):
    return l.low ^ l.high

def toStringImpl(radix):
    if (True) if (radix < 2) else (36 < radix):
        raise Exception_init__Create__0(str('radix out of range: ') + str(radix))
    
    if isZero():
        return '0'
    
    if isNegative():
        if equalsLong(MIN_VALUE):
            radixLong = fromInt(radix)
            div = (self // radixLong).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)
            rem = subtract(self).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
            tmp = toStringImpl(radix)
            tmp0_unsafeCast_0 = INVOKE(toString(rem), radix)
            return tmp + kotlin_Any_(tmp0_unsafeCast_0)
        else:
            return str('-') + str(toStringImpl(radix))
        
    
    radixToPower = fromNumber(visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl.pow(kotlin_Double(radix), 6.0))
    rem = self
    result = ''
    while True:
        remDiv = (rem // radixToPower).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)
        intval = subtract(multiply(radixToPower)).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
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
    return Long(value, (-1) if (value < 0) else (0))

def isNegative():
    return self.high < 0

def isZero():
    return (self.low == 0) if (self.high == 0) else (False)

def isOdd():
    return self.low & 1 == 1

def negate():
    return (-self).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)

def lessThan(other):
    return compare(other) < 0

def fromNumber(value):
    if isNaN_0():
        return ZERO
    elif value <= -9.223372036854776E18:
        return MIN_VALUE
    elif value + 1 >= 9.223372036854776E18:
        return MAX_VALUE
    elif value < 0.0:
        return negate()
    else:
        twoPwr32 = 4.294967296E9
        return Long(jsBitwiseOr(value % twoPwr32, 0), jsBitwiseOr(value / twoPwr32, 0))
    

def greaterThan(other):
    return compare(other) > 0

def greaterThanOrEqual(other):
    return compare(other) >= 0

def getLowBitsUnsigned():
    return (kotlin_Double(self.low)) if (self.low >= 0) else (4.294967296E9 + self.low)

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
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    return array

def arrayConcat(*args):
    len = len(args)
    tmp0_unsafeCast_0 = js('Array(len)')
    typed = kotlin_Any_(tmp0_unsafeCast_0)
    inductionVariable = 0
    last = (len - 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
    if inductionVariable <= last:
        while True:
            i = inductionVariable
            inductionVariable = (inductionVariable + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
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
    last = (len(args) - 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
    if inductionVariable <= last:
        while True:
            i = inductionVariable
            inductionVariable = (inductionVariable + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
            tmp = size_local
            tmp0_unsafeCast_0 = args[i]
            size_local = (tmp + len(kotlin_Any_(tmp0_unsafeCast_0))).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
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
    last = (len(args) - 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
    if inductionVariable <= last:
        while True:
            i = inductionVariable
            inductionVariable = (inductionVariable + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
            tmp3_unsafeCast_0 = args[i]
            arr = kotlin_Any_(tmp3_unsafeCast_0)
            inductionVariable = 0
            last = (len(arr) - 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
            if inductionVariable <= last:
                while True:
                    j = inductionVariable
                    inductionVariable = (inductionVariable + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
                    tmp3 = size_local
                    size_local = (tmp3 + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
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
    return toByte(a.__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))

def toByte(a):
    tmp0_unsafeCast_0 = js('a << 24 >> 24')
    return kotlin_Any_(tmp0_unsafeCast_0)

def numberToInt(a):
    if visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
        tmp = kotlin_Long(a).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
    elif True:
        tmp = doubleToInt(kotlin_Double(a))
    
    return tmp

def doubleToInt(a):
    return (2147483647) if (a > 2.147483647E9) else ((-2147483648) if (a < -2.147483648E9) else (jsBitwiseOr(a, 0)))

def numberToDouble(a):
    tmp0_unsafeCast_0 = js('+a')
    return kotlin_Any_(tmp0_unsafeCast_0)

def numberToShort(a):
    return toShort(a.__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))

def toShort(a):
    tmp0_unsafeCast_0 = js('a << 16 >> 16')
    return kotlin_Any_(tmp0_unsafeCast_0)

def numberToLong(a):
    if visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
        tmp = kotlin_Long(a)
    elif True:
        tmp = fromNumber(kotlin_Double(a))
    
    return tmp

def numberToChar(a):
    tmp0_toUShort_0 = a.__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
    return Char_0(_UShort___init__impl_(tmp0_toUShort_0.__add__(0x8000).__and__(0xffff).__sub__(0x8000)))

def toLong(a):
    return fromInt(kotlin_Int(a))

def numberRangeToNumber(start, endInclusive):
    return IntRange(kotlin_Int(start), kotlin_Int(endInclusive))

def numberRangeToLong(start, endInclusive):
    return LongRange(start.__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000), kotlin_Long(endInclusive))

def _get_propertyRefClassMetadataCache_():
    return propertyRefClassMetadataCache

propertyRefClassMetadataCache = None
def metadataObject():
    return js('{ kind: \'class\', interfaces: [] }')

def getPropertyCallableRef(name, paramCount, type, getter, setter):
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    tmp0_unsafeCast_0 = getPropertyRefClass(getter, getKPropMetadata(paramCount, setter, type))
    return kotlin_Any_(tmp0_unsafeCast_0)

def getPropertyRefClass(obj, metadata):
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    return obj

def getKPropMetadata(paramCount, setter, type):
    mdata = propertyRefClassMetadataCache[paramCount][(0) if (setter == None) else (1)]
    if EQEQ(length(interfaces(mdata)), 0):
        visitExpression_other__inToPyStatementTransformer_org_jetbrains_kotlin_ir_expressions_impl_IrDynamicOperatorExpressionImpl
    
    return mdata

def getLocalDelegateReference(name, type, mutable, _lambda):
    return getPropertyCallableRef(name, 0, type, _lambda, (_lambda) if (mutable) else (None))

def propertyRefClassMetadataCache_init_():
    tmp = js('{ kind: \'class\', interfaces: [] }')
    tmp0_arrayOf_0 = (tmp, js('{ kind: \'class\', interfaces: [] }'))
    tmp = js('{ kind: \'class\', interfaces: [] }')
    tmp1_arrayOf_0 = (tmp, js('{ kind: \'class\', interfaces: [] }'))
    tmp = js('{ kind: \'class\', interfaces: [] }')
    tmp2_arrayOf_0 = (tmp, js('{ kind: \'class\', interfaces: [] }'))
    tmp3_arrayOf_0 = (kotlin_Any_(tmp0_arrayOf_0), kotlin_Any_(tmp1_arrayOf_0), kotlin_Any_(tmp2_arrayOf_0))
    return kotlin_Any_(tmp3_arrayOf_0)

def isArrayish(o):
    if isJsArray(kotlin_Any(o)):
        tmp = True
    else:
        tmp0_unsafeCast_0 = INVOKE(isView(js('ArrayBuffer')), o)
        tmp = kotlin_Any_(tmp0_unsafeCast_0)
    
    return tmp

def isJsArray(obj):
    tmp0_unsafeCast_0 = INVOKE(isArray(js('Array')), obj)
    return kotlin_Any_(tmp0_unsafeCast_0)

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
    
    metadata = _metadata_
    if not (metadata == None):
        interfaces = interfaces
        indexedObject = interfaces
        inductionVariable = 0
        last = len(indexedObject)
        while inductionVariable < last:
            i = indexedObject[inductionVariable]
            inductionVariable = (inductionVariable + 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)
            if isInterfaceImpl(i, iface):
                return True
            
        
    
    superPrototype = (INVOKE(getPrototypeOf(js('Object')), prototype)) if (not (prototype == None)) else (None)
    superConstructor = (kotlin_js_Ctor_(constructor(superPrototype))) if (EXCLEQ(superPrototype, None)) else (None)
    return (isInterfaceImpl(superConstructor, iface)) if (not (superConstructor == None)) else (False)

def isArray(obj):
    if isJsArray(obj):
        tmp = kotlin_Boolean(EXCL(_type_(obj)))
    else:
        tmp = False
    
    return tmp

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
        tmp = visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean
    
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

def plus_0(elements):
    return kotlin_Array_T_(INVOKE(concat(self), elements))

def copyOfRange(fromIndex, toIndex):
    Companion_getInstance().checkRangeIndexes_zd700_k_(fromIndex, toIndex, len(self))
    return kotlin_Array_T_(INVOKE(slice(self), fromIndex, toIndex))

def copyInto(destination, destinationOffset, startIndex, endIndex):
    arrayCopy_0(self, destination, destinationOffset, startIndex, endIndex)
    return destination

def minOf(a, b):
    return visitGetObjectValue_org_jetbrains_kotlin_ir_expressions_impl_IrGetObjectValueImpl.min(*(a, b))

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
        ensureNotNull(_this._get_context__0_k_().get_9uvjra_k_(Key_getInstance())).releaseInterceptedContinuation_h7c6yl_k_(intercepted)
    
    _this.intercepted_ = CompletedContinuation_getInstance()

class CoroutineImpl_0:
    def __init__(self, resultContinuation):
        self.resultContinuation = resultContinuation
        self.state = 0
        self.exceptionState = 0
        self.result = None
        self.exception = None
        self.finallyPath = None
        tmp = self
        tmp0_safe_receiver = self.resultContinuation
        tmp._context = (None) if (tmp0_safe_receiver == None) else (tmp0_safe_receiver._get_context__0_k_())
        self.intercepted_ = None
    
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
    
    def _get_context__0_k_(self):
        return ensureNotNull(self._context)
    
    def intercepted_0_k_(self):
        tmp2_elvis_lhs = self.intercepted_
        if tmp2_elvis_lhs == None:
            tmp0_safe_receiver = self._get_context__0_k_().get_9uvjra_k_(Key_getInstance())
            tmp1_elvis_lhs = (None) if (tmp0_safe_receiver == None) else (tmp0_safe_receiver.interceptContinuation_x4ijla_k_(self))
            tmp0_also_0 = (self) if (tmp1_elvis_lhs == None) else (tmp1_elvis_lhs)
            self.intercepted_ = tmp0_also_0
            tmp = tmp0_also_0
        else:
            tmp = tmp2_elvis_lhs
        
        return tmp
    
    def resumeWith_jccoe6_k_(self, result):
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
            if visitCall_getNameForStaticFunction_Can_t_find_name_for_declaration_FUN_OPERATOR_name_jsInstanceOf_visibility_public_modality_FINAL_____arg0_kotlin_Any___arg1_kotlin_Any___returnType_kotlin_Boolean:
                current = kotlin_coroutines_CoroutineImpl(completion_4)
            elif True:
                if not (currentException == None):
                    tmp0_resumeWithException_0_5 = ensureNotNull(currentException)
                    tmp0_failure_0_1_6 = Companion_getInstance_2()
                    completion_4.resumeWith_bnunh2_k_(_Result___init__impl_(createFailure(tmp0_resumeWithException_0_5)))
                else:
                    tmp1_resume_0_7 = currentResult
                    tmp0_success_0_1_8 = Companion_getInstance_2()
                    completion_4.resumeWith_bnunh2_k_(_Result___init__impl_(tmp1_resume_0_7))
                
                return Unit_getInstance()
            
        
    
    def resumeWith_bnunh2_k_(self, result):
        return self.resumeWith_jccoe6_k_(result)
    
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
    

class CompletedContinuation:
    def __init__(self):
        global CompletedContinuation_instance
        CompletedContinuation_instance = self
    
    def _get_context__0_k_(self):
        raise IllegalStateException_init__Create__0('This continuation is already complete')
    
    def resumeWith_jccoe6_k_(self, result):
        raise IllegalStateException_init__Create__0('This continuation is already complete')
    
    def resumeWith_bnunh2_k_(self, result):
        return self.resumeWith_jccoe6_k_(result)
    
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
    extendThrowable(_this, _undefined(), _undefined())
    super()
    return _this

def Exception_init__Create_():
    tmp = Exception_init__Init_(Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def Exception_init__Init__0(message, _this):
    extendThrowable(_this, message, _undefined())
    super()
    return _this

def Exception_init__Create__0(message):
    tmp = Exception_init__Init__0(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def Exception_init__Init__1(message, cause, _this):
    extendThrowable(_this, message, cause)
    super()
    return _this

def Exception_init__Create__1(message, cause):
    tmp = Exception_init__Init__1(message, cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def Exception_init__Init__2(cause, _this):
    extendThrowable(_this, _undefined(), cause)
    super()
    return _this

def Exception_init__Create__2(cause):
    tmp = Exception_init__Init__2(cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

class Exception:
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

def Error_init__Init__0(message, _this):
    extendThrowable(_this, message, _undefined())
    super()
    return _this

def Error_init__Create__0(message):
    tmp = Error_init__Init__0(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def Error_init__Init__1(message, cause, _this):
    extendThrowable(_this, message, cause)
    super()
    return _this

def Error_init__Create__1(message, cause):
    tmp = Error_init__Init__1(message, cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def Error_init__Init__2(cause, _this):
    extendThrowable(_this, _undefined(), cause)
    super()
    return _this

def Error_init__Create__2(cause):
    tmp = Error_init__Init__2(cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

class Error_0:
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

def IllegalArgumentException_init__Init__0(message, _this):
    RuntimeException_init__Init__0(message, _this)
    super()
    return _this

def IllegalArgumentException_init__Create__0(message):
    tmp = IllegalArgumentException_init__Init__0(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def IllegalArgumentException_init__Init__1(message, cause, _this):
    RuntimeException_init__Init__1(message, cause, _this)
    super()
    return _this

def IllegalArgumentException_init__Create__1(message, cause):
    tmp = IllegalArgumentException_init__Init__1(message, cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def IllegalArgumentException_init__Init__2(cause, _this):
    RuntimeException_init__Init__2(cause, _this)
    super()
    return _this

def IllegalArgumentException_init__Create__2(cause):
    tmp = IllegalArgumentException_init__Init__2(cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

class IllegalArgumentException:
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

def RuntimeException_init__Init__0(message, _this):
    Exception_init__Init__0(message, _this)
    super()
    return _this

def RuntimeException_init__Create__0(message):
    tmp = RuntimeException_init__Init__0(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def RuntimeException_init__Init__1(message, cause, _this):
    Exception_init__Init__1(message, cause, _this)
    super()
    return _this

def RuntimeException_init__Create__1(message, cause):
    tmp = RuntimeException_init__Init__1(message, cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def RuntimeException_init__Init__2(cause, _this):
    Exception_init__Init__2(cause, _this)
    super()
    return _this

def RuntimeException_init__Create__2(cause):
    tmp = RuntimeException_init__Init__2(cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

class RuntimeException:
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

def NoSuchElementException_init__Init__0(message, _this):
    RuntimeException_init__Init__0(message, _this)
    super()
    return _this

def NoSuchElementException_init__Create__0(message):
    tmp = NoSuchElementException_init__Init__0(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

class NoSuchElementException:
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

def IllegalStateException_init__Init__0(message, _this):
    RuntimeException_init__Init__0(message, _this)
    super()
    return _this

def IllegalStateException_init__Create__0(message):
    tmp = IllegalStateException_init__Init__0(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def IllegalStateException_init__Init__1(message, cause, _this):
    RuntimeException_init__Init__1(message, cause, _this)
    super()
    return _this

def IllegalStateException_init__Create__1(message, cause):
    tmp = IllegalStateException_init__Init__1(message, cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def IllegalStateException_init__Init__2(cause, _this):
    RuntimeException_init__Init__2(cause, _this)
    super()
    return _this

def IllegalStateException_init__Create__2(cause):
    tmp = IllegalStateException_init__Init__2(cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

class IllegalStateException:
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

def IndexOutOfBoundsException_init__Init__0(message, _this):
    RuntimeException_init__Init__0(message, _this)
    super()
    return _this

def IndexOutOfBoundsException_init__Create__0(message):
    tmp = IndexOutOfBoundsException_init__Init__0(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

class IndexOutOfBoundsException:
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

def UnsupportedOperationException_init__Init__0(message, _this):
    RuntimeException_init__Init__0(message, _this)
    super()
    return _this

def UnsupportedOperationException_init__Create__0(message):
    tmp = UnsupportedOperationException_init__Init__0(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def UnsupportedOperationException_init__Init__1(message, cause, _this):
    RuntimeException_init__Init__1(message, cause, _this)
    super()
    return _this

def UnsupportedOperationException_init__Create__1(message, cause):
    tmp = UnsupportedOperationException_init__Init__1(message, cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def UnsupportedOperationException_init__Init__2(cause, _this):
    RuntimeException_init__Init__2(cause, _this)
    super()
    return _this

def UnsupportedOperationException_init__Create__2(cause):
    tmp = UnsupportedOperationException_init__Init__2(cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

class UnsupportedOperationException:
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

def NullPointerException_init__Init__0(message, _this):
    RuntimeException_init__Init__0(message, _this)
    super()
    return _this

def NullPointerException_init__Create__0(message):
    tmp = NullPointerException_init__Init__0(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

class NullPointerException:
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

def NoWhenBranchMatchedException_init__Init__0(message, _this):
    RuntimeException_init__Init__0(message, _this)
    super()
    return _this

def NoWhenBranchMatchedException_init__Create__0(message):
    tmp = NoWhenBranchMatchedException_init__Init__0(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def NoWhenBranchMatchedException_init__Init__1(message, cause, _this):
    RuntimeException_init__Init__1(message, cause, _this)
    super()
    return _this

def NoWhenBranchMatchedException_init__Create__1(message, cause):
    tmp = NoWhenBranchMatchedException_init__Init__1(message, cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def NoWhenBranchMatchedException_init__Init__2(cause, _this):
    RuntimeException_init__Init__2(cause, _this)
    super()
    return _this

def NoWhenBranchMatchedException_init__Create__2(cause):
    tmp = NoWhenBranchMatchedException_init__Init__2(cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

class NoWhenBranchMatchedException:
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

def ClassCastException_init__Init__0(message, _this):
    RuntimeException_init__Init__0(message, _this)
    super()
    return _this

def ClassCastException_init__Create__0(message):
    tmp = ClassCastException_init__Init__0(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

class ClassCastException:
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

def UninitializedPropertyAccessException_init__Init__0(message, _this):
    RuntimeException_init__Init__0(message, _this)
    super()
    return _this

def UninitializedPropertyAccessException_init__Create__0(message):
    tmp = UninitializedPropertyAccessException_init__Init__0(message, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def UninitializedPropertyAccessException_init__Init__1(message, cause, _this):
    RuntimeException_init__Init__1(message, cause, _this)
    super()
    return _this

def UninitializedPropertyAccessException_init__Create__1(message, cause):
    tmp = UninitializedPropertyAccessException_init__Init__1(message, cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

def UninitializedPropertyAccessException_init__Init__2(cause, _this):
    RuntimeException_init__Init__2(cause, _this)
    super()
    return _this

def UninitializedPropertyAccessException_init__Create__2(cause):
    tmp = UninitializedPropertyAccessException_init__Init__2(cause, Object_create())
    captureStack(tmp, visitExpression_other_org_jetbrains_kotlin_ir_expressions_impl_IrRawFunctionReferenceImpl)
    return tmp

class UninitializedPropertyAccessException:
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

def toString_1(radix):
    return toStringImpl(checkRadix(radix))

def pythonTest():
    println('Hello world')

def exampleFromAstTest():
    fruits = listOf(*('apple', 'banana', 'cherry'))
    tmp0_iterator = fruits.iterator_0_k_()
    while tmp0_iterator.hasNext_0_k_():
        x = tmp0_iterator.next_0_k_()
        println(x)
    

def isPowerOfTwo(n):
    return n & (n - 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000) == 0

def factorial(n):
    tmp0_subject = n <= 1
    if tmp0_subject == True:
        tmp = 1
    elif tmp0_subject == False:
        tmp = n * factorial((n - 1).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))
    else:
        noWhenBranchMatchedException()
    
    return tmp

def numberOfCombinations(n, k):
    return (factorial(n) // (factorial(k) * factorial((n - k).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)).__add__(0x8000_0000_0000_0000).__and__(0xffff_ffff_ffff_ffff).__sub__(0x8000_0000_0000_0000)

def sumOverflowDemo(a, b):
    return (a + b).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000)

def execute20(f):
    return f(20)

def execute20Doubled():
    return execute20(lambda it: (it + it).__add__(0x8000_0000).__and__(0xffff_ffff).__sub__(0x8000_0000))

def a(a1, *a2):
    pass

def b():
    a(1, *(2, 3))

def newCode():
    tmp0_map_0 = listOf(*('apple', 'banana', 'cherry'))
    tmp0_mapTo_0_1 = ArrayList_init__Create__0(collectionSizeOrDefault(10))
    tmp0_iterator_1_2 = tmp0_map_0.iterator_0_k_()
    while tmp0_iterator_1_2.hasNext_0_k_():
        item_2_3 = tmp0_iterator_1_2.next_0_k_()
        tmp0_mapTo_0_1.add_2bq_k_(kotlin_String(INVOKE(toUpperCase(item_2_3))))
        Unit_getInstance()
    
    tmp1_forEach_0 = tmp0_mapTo_0_1
    tmp0_iterator_1 = tmp1_forEach_0.iterator_0_k_()
    while tmp0_iterator_1.hasNext_0_k_():
        element_2 = tmp0_iterator_1.next_0_k_()
        println(element_2)
    

class TestClass:
    def __init__(self, classParameter):
        self.classParameter = classParameter
    
    def _get_classParameter__0_k_(self):
        return self.classParameter
    
    def getSomeString_0_k_(self):
        return 'Hello from Kotlin class!'
    
    def functionReturningClassParameter_0_k_(self):
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
    return testClass.getSomeString_0_k_()

def returnParameterFromClass():
    return TestClass('paramVal').functionReturningClassParameter_0_k_()
