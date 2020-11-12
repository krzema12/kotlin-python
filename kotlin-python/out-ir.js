this['out-ir'] = def (_) :
  'use strict'
  Exception.prototype = Object.create(Error.prototype)
  Exception.prototype.constructor = Exception
  RuntimeException.prototype = Object.create(Exception.prototype)
  RuntimeException.prototype.constructor = RuntimeException
  KotlinNothingValueException.prototype = Object.create(RuntimeException.prototype)
  KotlinNothingValueException.prototype.constructor = KotlinNothingValueException
  Level.prototype = Object.create(Enum.prototype)
  Level.prototype.constructor = Level
  Level_0.prototype = Object.create(Enum.prototype)
  Level_0.prototype.constructor = Level_0
  AbstractList.prototype = Object.create(AbstractCollection.prototype)
  AbstractList.prototype.constructor = AbstractList
  SubList.prototype = Object.create(AbstractList.prototype)
  SubList.prototype.constructor = SubList
  ListIteratorImpl.prototype = Object.create(IteratorImpl.prototype)
  ListIteratorImpl.prototype.constructor = ListIteratorImpl
  InvocationKind.prototype = Object.create(Enum.prototype)
  InvocationKind.prototype.constructor = InvocationKind
  CoroutineSingletons.prototype = Object.create(Enum.prototype)
  CoroutineSingletons.prototype.constructor = CoroutineSingletons
  RequireKotlinVersionKind.prototype = Object.create(Enum.prototype)
  RequireKotlinVersionKind.prototype.constructor = RequireKotlinVersionKind
  KVariance.prototype = Object.create(Enum.prototype)
  KVariance.prototype.constructor = KVariance
  Error_0.prototype = Object.create(Error.prototype)
  Error_0.prototype.constructor = Error_0
  NotImplementedError.prototype = Object.create(Error_0.prototype)
  NotImplementedError.prototype.constructor = NotImplementedError
  Iterator.prototype = Object.create(UByteIterator.prototype)
  Iterator.prototype.constructor = Iterator
  Iterator_0.prototype = Object.create(UIntIterator.prototype)
  Iterator_0.prototype.constructor = Iterator_0
  UIntRange.prototype = Object.create(UIntProgression.prototype)
  UIntRange.prototype.constructor = UIntRange
  UIntProgressionIterator.prototype = Object.create(UIntIterator.prototype)
  UIntProgressionIterator.prototype.constructor = UIntProgressionIterator
  Iterator_1.prototype = Object.create(ULongIterator.prototype)
  Iterator_1.prototype.constructor = Iterator_1
  ULongRange.prototype = Object.create(ULongProgression.prototype)
  ULongRange.prototype.constructor = ULongRange
  ULongProgressionIterator.prototype = Object.create(ULongIterator.prototype)
  ULongProgressionIterator.prototype.constructor = ULongProgressionIterator
  Iterator_2.prototype = Object.create(UShortIterator.prototype)
  Iterator_2.prototype.constructor = Iterator_2
  DeprecationLevel.prototype = Object.create(Enum.prototype)
  DeprecationLevel.prototype.constructor = DeprecationLevel
  IntProgressionIterator.prototype = Object.create(IntIterator.prototype)
  IntProgressionIterator.prototype.constructor = IntProgressionIterator
  LongProgressionIterator.prototype = Object.create(LongIterator.prototype)
  LongProgressionIterator.prototype.constructor = LongProgressionIterator
  CharProgressionIterator.prototype = Object.create(CharIterator.prototype)
  CharProgressionIterator.prototype.constructor = CharProgressionIterator
  IntRange.prototype = Object.create(IntProgression.prototype)
  IntRange.prototype.constructor = IntRange
  LongRange.prototype = Object.create(LongProgression.prototype)
  LongRange.prototype.constructor = LongRange
  CharRange.prototype = Object.create(CharProgression.prototype)
  CharRange.prototype.constructor = CharRange
  AnnotationTarget.prototype = Object.create(Enum.prototype)
  AnnotationTarget.prototype.constructor = AnnotationTarget
  AnnotationRetention.prototype = Object.create(Enum.prototype)
  AnnotationRetention.prototype.constructor = AnnotationRetention
  AbstractMutableCollection.prototype = Object.create(AbstractCollection.prototype)
  AbstractMutableCollection.prototype.constructor = AbstractMutableCollection
  ListIteratorImpl_0.prototype = Object.create(IteratorImpl_0.prototype)
  ListIteratorImpl_0.prototype.constructor = ListIteratorImpl_0
  AbstractMutableList.prototype = Object.create(AbstractMutableCollection.prototype)
  AbstractMutableList.prototype.constructor = AbstractMutableList
  SubList_0.prototype = Object.create(AbstractMutableList.prototype)
  SubList_0.prototype.constructor = SubList_0
  ArrayList.prototype = Object.create(AbstractMutableList.prototype)
  ArrayList.prototype.constructor = ArrayList
  NodeJsOutput_0.prototype = Object.create(BaseOutput.prototype)
  NodeJsOutput_0.prototype.constructor = NodeJsOutput_0
  BufferedOutput_0.prototype = Object.create(BaseOutput.prototype)
  BufferedOutput_0.prototype.constructor = BufferedOutput_0
  BufferedOutputToConsoleLog_0.prototype = Object.create(BufferedOutput_0.prototype)
  BufferedOutputToConsoleLog_0.prototype.constructor = BufferedOutputToConsoleLog_0
  PrimitiveKClassImpl.prototype = Object.create(KClassImpl.prototype)
  PrimitiveKClassImpl.prototype.constructor = PrimitiveKClassImpl
  NothingKClassImpl.prototype = Object.create(KClassImpl.prototype)
  NothingKClassImpl.prototype.constructor = NothingKClassImpl
  SimpleKClassImpl.prototype = Object.create(KClassImpl.prototype)
  SimpleKClassImpl.prototype.constructor = SimpleKClassImpl
  _no_name_provided__31.prototype = Object.create(BooleanIterator.prototype)
  _no_name_provided__31.prototype.constructor = _no_name_provided__31
  _no_name_provided__32.prototype = Object.create(CharIterator.prototype)
  _no_name_provided__32.prototype.constructor = _no_name_provided__32
  _no_name_provided__33.prototype = Object.create(ByteIterator.prototype)
  _no_name_provided__33.prototype.constructor = _no_name_provided__33
  _no_name_provided__34.prototype = Object.create(ShortIterator.prototype)
  _no_name_provided__34.prototype.constructor = _no_name_provided__34
  _no_name_provided__35.prototype = Object.create(IntIterator.prototype)
  _no_name_provided__35.prototype.constructor = _no_name_provided__35
  _no_name_provided__36.prototype = Object.create(FloatIterator.prototype)
  _no_name_provided__36.prototype.constructor = _no_name_provided__36
  _no_name_provided__37.prototype = Object.create(LongIterator.prototype)
  _no_name_provided__37.prototype.constructor = _no_name_provided__37
  _no_name_provided__38.prototype = Object.create(DoubleIterator.prototype)
  _no_name_provided__38.prototype.constructor = _no_name_provided__38
  Long.prototype = Object.create(Number_0.prototype)
  Long.prototype.constructor = Long
  IllegalArgumentException.prototype = Object.create(RuntimeException.prototype)
  IllegalArgumentException.prototype.constructor = IllegalArgumentException
  NoSuchElementException.prototype = Object.create(RuntimeException.prototype)
  NoSuchElementException.prototype.constructor = NoSuchElementException
  IllegalStateException.prototype = Object.create(RuntimeException.prototype)
  IllegalStateException.prototype.constructor = IllegalStateException
  UnsupportedOperationException.prototype = Object.create(RuntimeException.prototype)
  UnsupportedOperationException.prototype.constructor = UnsupportedOperationException
  NullPointerException.prototype = Object.create(RuntimeException.prototype)
  NullPointerException.prototype.constructor = NullPointerException
  IndexOutOfBoundsException.prototype = Object.create(RuntimeException.prototype)
  IndexOutOfBoundsException.prototype.constructor = IndexOutOfBoundsException
  NoWhenBranchMatchedException.prototype = Object.create(RuntimeException.prototype)
  NoWhenBranchMatchedException.prototype.constructor = NoWhenBranchMatchedException
  ClassCastException.prototype = Object.create(RuntimeException.prototype)
  ClassCastException.prototype.constructor = ClassCastException
  UninitializedPropertyAccessException.prototype = Object.create(RuntimeException.prototype)
  UninitializedPropertyAccessException.prototype.constructor = UninitializedPropertyAccessException
  def fold(_this_, initial, operation) :
     accumulator = initial
     indexedObject = _this_
     inductionVariable = 0
     last = indexedObject.length
    while (inductionVariable < last) :
       element = indexedObject[inductionVariable]
      inductionVariable = inductionVariable + 1 | 0
      accumulator = operation(accumulator, element)

    return accumulator

  def contains(_this_, element) :
    return indexOf(_this_, element) >= 0

  def indexOf(_this_, element) :
     inductionVariable = 0
     last = _this_.length - 1 | 0
    if (inductionVariable <= last)
      do :
         index = inductionVariable
        inductionVariable = inductionVariable + 1 | 0
        if (element === _this_[index]) :
          return index

       while (inductionVariable <= last)
    return -1

  def _get_indices_(_this_) :
    return new IntRange(0, _get_lastIndex_(_this_))

  def _get_lastIndex_(_this_) :
    return _this_.length - 1 | 0

  def contains_0(_this_, element) :
    return indexOf_0(_this_, element) >= 0

  def indexOf_0(_this_, element) :
     inductionVariable = 0
     last = _this_.length - 1 | 0
    if (inductionVariable <= last)
      do :
         index = inductionVariable
        inductionVariable = inductionVariable + 1 | 0
        if (element === _this_[index]) :
          return index

       while (inductionVariable <= last)
    return -1

  def _get_indices__0(_this_) :
    return new IntRange(0, _get_lastIndex__0(_this_))

  def _get_lastIndex__0(_this_) :
    return _this_.length - 1 | 0

  def contains_1(_this_, element) :
    return indexOf_1(_this_, element) >= 0

  def indexOf_1(_this_, element) :
     inductionVariable = 0
     last = _this_.length - 1 | 0
    if (inductionVariable <= last)
      do :
         index = inductionVariable
        inductionVariable = inductionVariable + 1 | 0
        if (element === _this_[index]) :
          return index

       while (inductionVariable <= last)
    return -1

  def _get_indices__1(_this_) :
    return new IntRange(0, _get_lastIndex__1(_this_))

  def _get_lastIndex__1(_this_) :
    return _this_.length - 1 | 0

  def contains_2(_this_, element) :
    return indexOf_2(_this_, element) >= 0

  def indexOf_2(_this_, element) :
     inductionVariable = 0
     last = _this_.length - 1 | 0
    if (inductionVariable <= last)
      do :
         index = inductionVariable
        inductionVariable = inductionVariable + 1 | 0
        if (element.equals(_this_[index])) :
          return index

       while (inductionVariable <= last)
    return -1

  def _get_indices__2(_this_) :
    return new IntRange(0, _get_lastIndex__2(_this_))

  def _get_lastIndex__2(_this_) :
    return _this_.length - 1 | 0

  def _get_indices__3(_this_) :
    return new IntRange(0, _get_lastIndex__3(_this_))

  def indexOf_3(_this_, element) :
    if (element == null) :
       inductionVariable = 0
       last = _this_.length - 1 | 0
      if (inductionVariable <= last)
        do :
           index = inductionVariable
          inductionVariable = inductionVariable + 1 | 0
          if (_this_[index] == null) :
            return index

         while (inductionVariable <= last)
     else :
       inductionVariable_0 = 0
       last_0 = _this_.length - 1 | 0
      if (inductionVariable_0 <= last_0)
        do :
           index_0 = inductionVariable_0
          inductionVariable_0 = inductionVariable_0 + 1 | 0
          if (equals(element, _this_[index_0])) :
            return index_0

         while (inductionVariable_0 <= last_0)

    return -1

  def lastIndexOf(_this_, element) :
    if (element == null) :
       inductionVariable = _this_.length - 1 | 0
      if (0 <= inductionVariable)
        do :
           index = inductionVariable
          inductionVariable = inductionVariable + -1 | 0
          if (_this_[index] == null) :
            return index

         while (0 <= inductionVariable)
     else :
       inductionVariable_0 = _this_.length - 1 | 0
      if (0 <= inductionVariable_0)
        do :
           index_0 = inductionVariable_0
          inductionVariable_0 = inductionVariable_0 + -1 | 0
          if (equals(element, _this_[index_0])) :
            return index_0

         while (0 <= inductionVariable_0)

    return -1

  def _get_lastIndex__3(_this_) :
    return _this_.length - 1 | 0

  def joinToString(_this_, separator, prefix, postfix, limit, truncated, transform) :
    return joinTo(_this_, StringBuilder_init_$Create$_1(), separator, prefix, postfix, limit, truncated, transform).toString()

  def joinToString$default(_this_, separator, prefix, postfix, limit, truncated, transform, $mask0, $handler) :
    if (!(($mask0 & 1) === 0))
      separator = ', '
    if (!(($mask0 & 2) === 0))
      prefix = ''
    if (!(($mask0 & 4) === 0))
      postfix = ''
    if (!(($mask0 & 8) === 0))
      limit = -1
    if (!(($mask0 & 16) === 0))
      truncated = '...'
    if (!(($mask0 & 32) === 0))
      transform = null
    return joinToString(_this_, separator, prefix, postfix, limit, truncated, transform)

  def joinTo(_this_, buffer, separator, prefix, postfix, limit, truncated, transform) :
    buffer.append_3(prefix)
    Unit_getInstance()
     count = 0
     indexedObject = _this_
     inductionVariable = 0
     last = indexedObject.length
    $l$break: while (inductionVariable < last) :
       element = indexedObject[inductionVariable]
      inductionVariable = inductionVariable + 1 | 0
      count = count + 1 | 0
      if (count > 1) :
        buffer.append_3(separator)
        Unit_getInstance()
       else :

      if (limit < 0 ? true : count <= limit) :
        appendElement(buffer, element, transform)
       else
        break $l$break

    if (limit >= 0 ? count > limit : false) :
      buffer.append_3(truncated)
      Unit_getInstance()
    buffer.append_3(postfix)
    Unit_getInstance()
    return buffer

  def joinTo$default(_this_, buffer, separator, prefix, postfix, limit, truncated, transform, $mask0, $handler) :
    if (!(($mask0 & 2) === 0))
      separator = ', '
    if (!(($mask0 & 4) === 0))
      prefix = ''
    if (!(($mask0 & 8) === 0))
      postfix = ''
    if (!(($mask0 & 16) === 0))
      limit = -1
    if (!(($mask0 & 32) === 0))
      truncated = '...'
    if (!(($mask0 & 64) === 0))
      transform = null
    return joinTo(_this_, buffer, separator, prefix, postfix, limit, truncated, transform)

  def all(_this_, predicate) :
     tmp
    if (isInterface(_this_, Collection)) :
      tmp = _this_.isEmpty_29()
     else :
      :
        tmp = false


    if (tmp)
      return true;
    else :

     tmp0_iterator = _this_.iterator_38()
    while (tmp0_iterator.hasNext_37()) :
       element = tmp0_iterator.next_41()
      if (!predicate(element))
        return false

    return true

  def joinToString_0(_this_, separator, prefix, postfix, limit, truncated, transform) :
    return joinTo_0(_this_, StringBuilder_init_$Create$_1(), separator, prefix, postfix, limit, truncated, transform).toString()

  def joinToString$default_0(_this_, separator, prefix, postfix, limit, truncated, transform, $mask0, $handler) :
    if (!(($mask0 & 1) === 0))
      separator = ', '
    if (!(($mask0 & 2) === 0))
      prefix = ''
    if (!(($mask0 & 4) === 0))
      postfix = ''
    if (!(($mask0 & 8) === 0))
      limit = -1
    if (!(($mask0 & 16) === 0))
      truncated = '...'
    if (!(($mask0 & 32) === 0))
      transform = null
    return joinToString_0(_this_, separator, prefix, postfix, limit, truncated, transform)

  def joinTo_0(_this_, buffer, separator, prefix, postfix, limit, truncated, transform) :
    buffer.append_3(prefix)
    Unit_getInstance()
     count = 0
     tmp0_iterator = _this_.iterator_38()
    $l$break: while (tmp0_iterator.hasNext_37()) :
       element = tmp0_iterator.next_41()
      count = count + 1 | 0
      if (count > 1) :
        buffer.append_3(separator)
        Unit_getInstance()
       else :

      if (limit < 0 ? true : count <= limit) :
        appendElement(buffer, element, transform)
       else
        break $l$break

    if (limit >= 0 ? count > limit : false) :
      buffer.append_3(truncated)
      Unit_getInstance()
    buffer.append_3(postfix)
    Unit_getInstance()
    return buffer

  def joinTo$default_0(_this_, buffer, separator, prefix, postfix, limit, truncated, transform, $mask0, $handler) :
    if (!(($mask0 & 2) === 0))
      separator = ', '
    if (!(($mask0 & 4) === 0))
      prefix = ''
    if (!(($mask0 & 8) === 0))
      postfix = ''
    if (!(($mask0 & 16) === 0))
      limit = -1
    if (!(($mask0 & 32) === 0))
      truncated = '...'
    if (!(($mask0 & 64) === 0))
      transform = null
    return joinTo_0(_this_, buffer, separator, prefix, postfix, limit, truncated, transform)

  def indexOfFirst(_this_, predicate) :
     index = 0
     tmp0_iterator = _this_.iterator_38()
    while (tmp0_iterator.hasNext_37()) :
       item = tmp0_iterator.next_41()
      if (predicate(item))
        return index
       tmp1 = index
      index = tmp1 + 1 | 0
      Unit_getInstance()

    return -1

  def indexOfLast(_this_, predicate) :
     iterator = _this_.listIterator_14(_this_._get_size__18())
    while (iterator.hasPrevious_3()) :
      if (predicate(iterator.previous_3())) :
        return iterator.nextIndex_3()

    return -1

  def any(_this_, predicate) :
     tmp
    if (isInterface(_this_, Collection)) :
      tmp = _this_.isEmpty_29()
     else :
      :
        tmp = false


    if (tmp)
      return false;
    else :

     tmp0_iterator = _this_.iterator_38()
    while (tmp0_iterator.hasNext_37()) :
       element = tmp0_iterator.next_41()
      if (predicate(element))
        return true

    return false

  def until(_this_, to) :
    if (to <= IntCompanionObject_getInstance()._MIN_VALUE_5)
      return Companion_getInstance_14()._EMPTY_1
    return numberRangeToNumber(_this_, to - 1 | 0)

  def downTo(_this_, to) :
    return Companion_getInstance_11().fromClosedRange_1(_this_, to, -1)

  def reversed(_this_) :
    return Companion_getInstance_11().fromClosedRange_1(_this_._last_1, _this_._first_1, -_this_._step_6 | 0)

  def getOrElse(_this_, index, defaultValue) :
    return (index >= 0 ? index <= _get_lastIndex__5(_this_) : false) ? charSequenceGet(_this_, index) : defaultValue(index)

  def KotlinNothingValueException_init_$Init$($this) :
    RuntimeException_init_$Init$($this)
    KotlinNothingValueException.call($this)
    return $this

  def KotlinNothingValueException_init_$Create$() :
     tmp = KotlinNothingValueException_init_$Init$(Object.create(KotlinNothingValueException.prototype))
    captureStack(tmp, KotlinNothingValueException_init_$Create$)
    return tmp

  def KotlinNothingValueException_init_$Init$_0(message, $this) :
    RuntimeException_init_$Init$_0(message, $this)
    KotlinNothingValueException.call($this)
    return $this

  def KotlinNothingValueException_init_$Create$_0(message) :
     tmp = KotlinNothingValueException_init_$Init$_0(message, Object.create(KotlinNothingValueException.prototype))
    captureStack(tmp, KotlinNothingValueException_init_$Create$_0)
    return tmp

  def KotlinNothingValueException_init_$Init$_1(message, cause, $this) :
    RuntimeException_init_$Init$_1(message, cause, $this)
    KotlinNothingValueException.call($this)
    return $this

  def KotlinNothingValueException_init_$Create$_1(message, cause) :
     tmp = KotlinNothingValueException_init_$Init$_1(message, cause, Object.create(KotlinNothingValueException.prototype))
    captureStack(tmp, KotlinNothingValueException_init_$Create$_1)
    return tmp

  def KotlinNothingValueException_init_$Init$_2(cause, $this) :
    RuntimeException_init_$Init$_2(cause, $this)
    KotlinNothingValueException.call($this)
    return $this

  def KotlinNothingValueException_init_$Create$_2(cause) :
     tmp = KotlinNothingValueException_init_$Init$_2(cause, Object.create(KotlinNothingValueException.prototype))
    captureStack(tmp, KotlinNothingValueException_init_$Create$_2)
    return tmp

  def KotlinNothingValueException() :
    captureStack(this, KotlinNothingValueException)

  KotlinNothingValueException.$metadata$ = {
    simpleName: 'KotlinNothingValueException',
    kind: 'class',
    interfaces: []

   Level_WARNING_instance
   Level_ERROR_instance
  def values() :
    return [Level_WARNING_getInstance(), Level_ERROR_getInstance()]

  def valueOf(value) :
    switch (value) :
      case 'WARNING':
        return Level_WARNING_getInstance();
      case 'ERROR':
        return Level_ERROR_getInstance();
      default:return THROW_ISE();


   Level_entriesInitialized
  def Level_initEntries() :
    if (Level_entriesInitialized)
      return Unit_getInstance()
    Level_entriesInitialized = true
    Level_WARNING_instance = new Level('WARNING', 0)
    Level_ERROR_instance = new Level('ERROR', 1)

  def Experimental_init_$Init$(level, $mask0, $marker, $this) :
    if (!(($mask0 & 1) === 0))
      level = Level_ERROR_getInstance()
    Experimental.call($this, level)
    return $this

  def Experimental_init_$Create$(level, $mask0, $marker) :
    return Experimental_init_$Init$(level, $mask0, $marker, Object.create(Experimental.prototype))

  def Level(name, ordinal) :
    Enum.call(this, name, ordinal)

  Level.$metadata$ = {
    simpleName: 'Level',
    kind: 'class',
    interfaces: []

  def Level_WARNING_getInstance() :
    Level_initEntries()
    return Level_WARNING_instance

  def Level_ERROR_getInstance() :
    Level_initEntries()
    return Level_ERROR_instance

  def Experimental(level) :
    this._level = level

  Experimental.prototype._get_level__2 = def () :
    return this._level

  Experimental.$metadata$ = {
    simpleName: 'Experimental',
    kind: 'class',
    interfaces: [Annotation]

  def WasExperimental(markerClass) :
    this._markerClass = markerClass

  WasExperimental.prototype._get_markerClass__0 = def () :
    return this._markerClass

  WasExperimental.$metadata$ = {
    simpleName: 'WasExperimental',
    kind: 'class',
    interfaces: [Annotation]

  def ExperimentalStdlibApi() :

  ExperimentalStdlibApi.$metadata$ = {
    simpleName: 'ExperimentalStdlibApi',
    kind: 'class',
    interfaces: [Annotation]

  def OptionalExpectation() :

  OptionalExpectation.$metadata$ = {
    simpleName: 'OptionalExpectation',
    kind: 'class',
    interfaces: [Annotation]

  def ExperimentalMultiplatform() :

  ExperimentalMultiplatform.$metadata$ = {
    simpleName: 'ExperimentalMultiplatform',
    kind: 'class',
    interfaces: [Annotation]

   Level_WARNING_instance_0
   Level_ERROR_instance_0
  def values_0() :
    return [Level_WARNING_getInstance_0(), Level_ERROR_getInstance_0()]

  def valueOf_0(value) :
    switch (value) :
      case 'WARNING':
        return Level_WARNING_getInstance_0();
      case 'ERROR':
        return Level_ERROR_getInstance_0();
      default:return THROW_ISE();


   Level_entriesInitialized_0
  def Level_initEntries_0() :
    if (Level_entriesInitialized_0)
      return Unit_getInstance()
    Level_entriesInitialized_0 = true
    Level_WARNING_instance_0 = new Level_0('WARNING', 0)
    Level_ERROR_instance_0 = new Level_0('ERROR', 1)

  def RequiresOptIn_init_$Init$(message, level, $mask0, $marker, $this) :
    if (!(($mask0 & 1) === 0))
      message = ''
    if (!(($mask0 & 2) === 0))
      level = Level_ERROR_getInstance_0()
    RequiresOptIn.call($this, message, level)
    return $this

  def RequiresOptIn_init_$Create$(message, level, $mask0, $marker) :
    return RequiresOptIn_init_$Init$(message, level, $mask0, $marker, Object.create(RequiresOptIn.prototype))

  def Level_0(name, ordinal) :
    Enum.call(this, name, ordinal)

  Level_0.$metadata$ = {
    simpleName: 'Level',
    kind: 'class',
    interfaces: []

  def Level_WARNING_getInstance_0() :
    Level_initEntries_0()
    return Level_WARNING_instance_0

  def Level_ERROR_getInstance_0() :
    Level_initEntries_0()
    return Level_ERROR_instance_0

  def RequiresOptIn(message, level) :
    this._message = message
    this._level_0 = level

  RequiresOptIn.prototype._get_message__15 = def () :
    return this._message

  RequiresOptIn.prototype._get_level__2 = def () :
    return this._level_0

  RequiresOptIn.$metadata$ = {
    simpleName: 'RequiresOptIn',
    kind: 'class',
    interfaces: [Annotation]

  def OptIn(markerClass) :
    this._markerClass_0 = markerClass

  OptIn.prototype._get_markerClass__0 = def () :
    return this._markerClass_0

  OptIn.$metadata$ = {
    simpleName: 'OptIn',
    kind: 'class',
    interfaces: [Annotation]

  def _no_name_provided_(this$0) :
    this._this$0 = this$0

  _no_name_provided_.prototype.invoke_13 = def (it) :
    return it === this._this$0 ? '(this Collection)' : toString(it)

  _no_name_provided_.prototype.invoke_66 = def (p1) :
    return this.invoke_13((p1 == null ? true : isObject(p1)) ? p1 : THROW_CCE())

  _no_name_provided_.$metadata$ = {
    kind: 'class',
    interfaces: []

  def AbstractCollection() :

  AbstractCollection.prototype.contains_32 = def (element) :
     tmp$ret$0
    l$ret$1: do :
       tmp
      if (isInterface(this, Collection)) :
        tmp = this.isEmpty_29()
       else :
        :
          tmp = false


      if (tmp) :
        tmp$ret$0 = false
        break l$ret$1
       else :

       tmp0_iterator_1 = this.iterator_38()
      while (tmp0_iterator_1.hasNext_37()) :
         element_2 = tmp0_iterator_1.next_41()
        if (equals(element_2, element)) :
          tmp$ret$0 = true
          break l$ret$1
         else :


      tmp$ret$0 = false

     while (false)
    return tmp$ret$0

  AbstractCollection.prototype.containsAll_21 = def (elements) :
     tmp$ret$0
    l$ret$1: do :
       tmp
      if (isInterface(elements, Collection)) :
        tmp = elements.isEmpty_29()
       else :
        :
          tmp = false


      if (tmp) :
        tmp$ret$0 = true
        break l$ret$1
       else :

       tmp0_iterator_1 = elements.iterator_38()
      while (tmp0_iterator_1.hasNext_37()) :
         element_2 = tmp0_iterator_1.next_41()
        if (!this.contains_32(element_2)) :
          tmp$ret$0 = false
          break l$ret$1
         else :


      tmp$ret$0 = true

     while (false)
    return tmp$ret$0

  AbstractCollection.prototype.isEmpty_29 = def () :
    return this._get_size__18() === 0

  AbstractCollection.prototype.toString = def () :
    return joinToString$default_0(this, ', ', '[', ']', 0, null, _no_name_provided_$factory(this), 24, null)

  AbstractCollection.prototype.toArray = def () :
    return copyToArrayImpl_0(this)

  AbstractCollection.prototype.toArray_7 = def (array) :
    return copyToArrayImpl_1(this, array)

  AbstractCollection.$metadata$ = {
    simpleName: 'AbstractCollection',
    kind: 'class',
    interfaces: [Collection]

  def _no_name_provided_$factory(this$0) :
     i = new _no_name_provided_(this$0)
    return def (p1) :
      return i.invoke_13(p1)


  def _get_list_($this) :
    return $this._list

  def _get_fromIndex_($this) :
    return $this._fromIndex

  def _set__size_($this, _set___) :
    $this.__size = _set___

  def _get__size_($this) :
    return $this.__size

  def SubList(list, fromIndex, toIndex) :
    AbstractList.call(this)
    this._list = list
    this._fromIndex = fromIndex
    this.__size = 0
    Companion_getInstance().checkRangeIndexes(this._fromIndex, toIndex, this._list._get_size__18())
    this.__size = toIndex - this._fromIndex | 0

  SubList.prototype.get_31 = def (index) :
    Companion_getInstance().checkElementIndex(index, this.__size)
    return this._list.get_31(this._fromIndex + index | 0)

  SubList.prototype._get_size__18 = def () :
    return this.__size

  SubList.$metadata$ = {
    simpleName: 'SubList',
    kind: 'class',
    interfaces: [RandomAccess]

  def IteratorImpl($outer) :
    this._$this = $outer
    this._index = 0

  IteratorImpl.prototype._set_index__11 = def (_set___) :
    this._index = _set___

  IteratorImpl.prototype._get_index__11 = def () :
    return this._index

  IteratorImpl.prototype.hasNext_37 = def () :
    return this._index < this._$this._get_size__18()

  IteratorImpl.prototype.next_41 = def () :
    if (!this.hasNext_37())
      throw NoSuchElementException_init_$Create$()
     tmp0_this = this
     tmp1 = tmp0_this._index
    tmp0_this._index = tmp1 + 1 | 0
    return this._$this.get_31(tmp1)

  IteratorImpl.$metadata$ = {
    simpleName: 'IteratorImpl',
    kind: 'class',
    interfaces: [Iterator_3]

  def ListIteratorImpl($outer, index) :
    this._$this_0 = $outer
    IteratorImpl.call(this, $outer)
    Companion_getInstance().checkPositionIndex(index, this._$this_0._get_size__18())
    this._set_index__11(index)

  ListIteratorImpl.prototype.hasPrevious_3 = def () :
    return this._get_index__11() > 0

  ListIteratorImpl.prototype.nextIndex_3 = def () :
    return this._get_index__11()

  ListIteratorImpl.prototype.previous_3 = def () :
    if (!this.hasPrevious_3())
      throw NoSuchElementException_init_$Create$()
     tmp0_this = this
    tmp0_this._set_index__11(tmp0_this._get_index__11() - 1 | 0)
    return this._$this_0.get_31(tmp0_this._get_index__11())

  ListIteratorImpl.prototype.previousIndex_3 = def () :
    return this._get_index__11() - 1 | 0

  ListIteratorImpl.$metadata$ = {
    simpleName: 'ListIteratorImpl',
    kind: 'class',
    interfaces: [ListIterator]

  def Companion_0() :
    Companion_instance = this

  Companion_0.prototype.checkElementIndex = def (index, size_0) :
    if (index < 0 ? true : index >= size_0) :
      throw IndexOutOfBoundsException_init_$Create$_0('' + 'index: ' + index + ', size: ' + size_0)

  Companion_0.prototype.checkPositionIndex = def (index, size_0) :
    if (index < 0 ? true : index > size_0) :
      throw IndexOutOfBoundsException_init_$Create$_0('' + 'index: ' + index + ', size: ' + size_0)

  Companion_0.prototype.checkRangeIndexes = def (fromIndex, toIndex, size_0) :
    if (fromIndex < 0 ? true : toIndex > size_0) :
      throw IndexOutOfBoundsException_init_$Create$_0('' + 'fromIndex: ' + fromIndex + ', toIndex: ' + toIndex + ', size: ' + size_0)
    if (fromIndex > toIndex) :
      throw IllegalArgumentException_init_$Create$_0('' + 'fromIndex: ' + fromIndex + ' > toIndex: ' + toIndex)

  Companion_0.prototype.checkBoundsIndexes = def (startIndex, endIndex, size_0) :
    if (startIndex < 0 ? true : endIndex > size_0) :
      throw IndexOutOfBoundsException_init_$Create$_0('' + 'startIndex: ' + startIndex + ', endIndex: ' + endIndex + ', size: ' + size_0)
    if (startIndex > endIndex) :
      throw IllegalArgumentException_init_$Create$_0('' + 'startIndex: ' + startIndex + ' > endIndex: ' + endIndex)

  Companion_0.prototype.orderedHashCode = def (c) :
     hashCode_1 = 1
     tmp0_iterator = c.iterator_38()
    while (tmp0_iterator.hasNext_37()) :
       e = tmp0_iterator.next_41()
       tmp = imul(31, hashCode_1)
       tmp1_safe_receiver = e
       tmp2_elvis_lhs = tmp1_safe_receiver == null ? null : hashCode(tmp1_safe_receiver)
      hashCode_1 = tmp + (tmp2_elvis_lhs == null ? 0 : tmp2_elvis_lhs) | 0

    return hashCode_1

  Companion_0.prototype.orderedEquals = def (c, other) :
    if (!(c._get_size__18() === other._get_size__18()))
      return false
     otherIterator = other.iterator_38()
     tmp0_iterator = c.iterator_38()
    while (tmp0_iterator.hasNext_37()) :
       elem = tmp0_iterator.next_41()
       elemOther = otherIterator.next_41()
      if (!equals(elem, elemOther)) :
        return false

    return true

  Companion_0.$metadata$ = {
    simpleName: 'Companion',
    kind: 'object',
    interfaces: []

   Companion_instance
  def Companion_getInstance() :
    if (Companion_instance == null)
      new Companion_0()
    return Companion_instance

  def AbstractList() :
    Companion_getInstance()
    AbstractCollection.call(this)

  AbstractList.prototype.iterator_38 = def () :
    return new IteratorImpl(this)

  AbstractList.prototype.indexOf_9 = def (element) :
     tmp$ret$0
    l$ret$1: do :
       index_1 = 0
       tmp0_iterator_2 = this.iterator_38()
      while (tmp0_iterator_2.hasNext_37()) :
         item_3 = tmp0_iterator_2.next_41()
        if (equals(item_3, element)) :
          tmp$ret$0 = index_1
          break l$ret$1
         else :

         tmp1_4 = index_1
        index_1 = tmp1_4 + 1 | 0
        Unit_getInstance()

      tmp$ret$0 = -1

     while (false)
    return tmp$ret$0

  AbstractList.prototype.lastIndexOf_9 = def (element) :
     tmp$ret$0
    l$ret$1: do :
       iterator_1 = this.listIterator_14(this._get_size__18())
      while (iterator_1.hasPrevious_3()) :
         tmp0__anonymous__2 = iterator_1.previous_3()
        if (equals(tmp0__anonymous__2, element)) :
          tmp$ret$0 = iterator_1.nextIndex_3()
          break l$ret$1
         else :


      tmp$ret$0 = -1

     while (false)
    return tmp$ret$0

  AbstractList.prototype.listIterator_13 = def () :
    return new ListIteratorImpl(this, 0)

  AbstractList.prototype.listIterator_14 = def (index) :
    return new ListIteratorImpl(this, index)

  AbstractList.prototype.subList_6 = def (fromIndex, toIndex) :
    return new SubList(this, fromIndex, toIndex)

  AbstractList.prototype.equals = def (other) :
    if (other === this)
      return true
    if (!(!(other == null) ? isInterface(other, List) : false))
      return false;
    else :

    return Companion_getInstance().orderedEquals(this, other)

  AbstractList.prototype.hashCode = def () :
    return Companion_getInstance().orderedHashCode(this)

  AbstractList.$metadata$ = {
    simpleName: 'AbstractList',
    kind: 'class',
    interfaces: [List]

  def _get_lastIndex__4(_this_) :
    return _this_._get_size__18() - 1 | 0

  def emptyList() :
    return EmptyList_getInstance()

  def _get_serialVersionUID_($this) :
    return $this._serialVersionUID

  def readResolve($this) :
    return EmptyList_getInstance()

  def EmptyList() :
    EmptyList_instance = this
    this._serialVersionUID = new Long(-1478467534, -1720727600)

  EmptyList.prototype.equals = def (other) :
     tmp
    if (!(other == null) ? isInterface(other, List) : false) :
      tmp = other.isEmpty_29()
     else :
      :
        tmp = false


    return tmp

  EmptyList.prototype.hashCode = def () :
    return 1

  EmptyList.prototype.toString = def () :
    return '[]'

  EmptyList.prototype._get_size__18 = def () :
    return 0

  EmptyList.prototype.isEmpty_29 = def () :
    return true

  EmptyList.prototype.contains_2 = def (element) :
    return false

  EmptyList.prototype.contains_32 = def (element) :
    if (!false)
      return false;
    else :

     tmp
    if (false) :
      tmp = element
     else :
      :
        tmp = THROW_CCE()


    return this.contains_2(tmp)

  EmptyList.prototype.containsAll_2 = def (elements) :
    return elements.isEmpty_29()

  EmptyList.prototype.containsAll_21 = def (elements) :
    return this.containsAll_2(elements)

  EmptyList.prototype.get_31 = def (index) :
    throw IndexOutOfBoundsException_init_$Create$_0('' + "Empty list doesn't contain element at index " + index + '.')

  EmptyList.prototype.indexOf_1 = def (element) :
    return -1

  EmptyList.prototype.indexOf_9 = def (element) :
    if (!false)
      return -1;
    else :

     tmp
    if (false) :
      tmp = element
     else :
      :
        tmp = THROW_CCE()


    return this.indexOf_1(tmp)

  EmptyList.prototype.lastIndexOf_1 = def (element) :
    return -1

  EmptyList.prototype.lastIndexOf_9 = def (element) :
    if (!false)
      return -1;
    else :

     tmp
    if (false) :
      tmp = element
     else :
      :
        tmp = THROW_CCE()


    return this.lastIndexOf_1(tmp)

  EmptyList.prototype.iterator_38 = def () :
    return EmptyIterator_getInstance()

  EmptyList.prototype.listIterator_13 = def () :
    return EmptyIterator_getInstance()

  EmptyList.prototype.listIterator_14 = def (index) :
    if (!(index === 0))
      throw IndexOutOfBoundsException_init_$Create$_0('' + 'Index: ' + index)
    return EmptyIterator_getInstance()

  EmptyList.prototype.subList_6 = def (fromIndex, toIndex) :
    if (fromIndex === 0 ? toIndex === 0 : false)
      return this
    throw IndexOutOfBoundsException_init_$Create$_0('' + 'fromIndex: ' + fromIndex + ', toIndex: ' + toIndex)

  EmptyList.$metadata$ = {
    simpleName: 'EmptyList',
    kind: 'object',
    interfaces: [List, Serializable, RandomAccess]

   EmptyList_instance
  def EmptyList_getInstance() :
    if (EmptyList_instance == null)
      new EmptyList()
    return EmptyList_instance

  def EmptyIterator() :
    EmptyIterator_instance = this

  EmptyIterator.prototype.hasNext_37 = def () :
    return false

  EmptyIterator.prototype.hasPrevious_3 = def () :
    return false

  EmptyIterator.prototype.nextIndex_3 = def () :
    return 0

  EmptyIterator.prototype.previousIndex_3 = def () :
    return -1

  EmptyIterator.prototype.next_41 = def () :
    throw NoSuchElementException_init_$Create$()

  EmptyIterator.prototype.previous_3 = def () :
    throw NoSuchElementException_init_$Create$()

  EmptyIterator.$metadata$ = {
    simpleName: 'EmptyIterator',
    kind: 'object',
    interfaces: [ListIterator]

   EmptyIterator_instance
  def EmptyIterator_getInstance() :
    if (EmptyIterator_instance == null)
      new EmptyIterator()
    return EmptyIterator_instance

  def removeAll(_this_, predicate) :
    return filterInPlace(_this_, predicate, true)

  def removeAll_0(_this_, predicate) :
    return filterInPlace_0(_this_, predicate, true)

  def filterInPlace(_this_, predicate, predicateResultToRemove) :
    if (!isInterface(_this_, RandomAccess)) :
      return filterInPlace_0(isInterface(_this_, MutableIterable) ? _this_ : THROW_CCE(), predicate, predicateResultToRemove)
     else :

     writeIndex = 0
     inductionVariable = 0
     last = _get_lastIndex__4(_this_)
    if (inductionVariable <= last)
      do :
         readIndex = inductionVariable
        inductionVariable = inductionVariable + 1 | 0
         element = _this_.get_31(readIndex)
        if (predicate(element) === predicateResultToRemove)
          continue
        if (!(writeIndex === readIndex)) :
          _this_.set_9(writeIndex, element)
          Unit_getInstance()
         tmp1 = writeIndex
        writeIndex = tmp1 + 1 | 0
        Unit_getInstance()

       while (!(readIndex === last))
    if (writeIndex < _this_._get_size__18()) :
       inductionVariable_0 = _get_lastIndex__4(_this_)
      if (writeIndex <= inductionVariable_0)
        do :
           removeIndex = inductionVariable_0
          inductionVariable_0 = inductionVariable_0 + -1 | 0
          _this_.removeAt_2(removeIndex)
          Unit_getInstance()

         while (!(removeIndex === writeIndex))
      return true
     else :
      return false


  def filterInPlace_0(_this_, predicate, predicateResultToRemove) :
     result = false
     tmp0_with_0 = _this_.iterator_38()
    while (tmp0_with_0.hasNext_37())
      if (predicate(tmp0_with_0.next_41()) === predicateResultToRemove) :
        tmp0_with_0.remove_3()
        result = true
    return result

  def Sequence() :

  Sequence.$metadata$ = {
    simpleName: 'Sequence',
    kind: 'interface',
    interfaces: []

  def contract(builder) :

  ContractBuilder.prototype.callsInPlace$default = def (lambda, kind, $mask0, $handler) :
    if (!(($mask0 & 2) === 0))
      kind = InvocationKind_UNKNOWN_getInstance()
    return $handler == null ? this.callsInPlace(lambda, kind) : $handler(lambda, kind)

  def ContractBuilder() :

  ContractBuilder.$metadata$ = {
    simpleName: 'ContractBuilder',
    kind: 'interface',
    interfaces: []

   InvocationKind_AT_MOST_ONCE_instance
   InvocationKind_AT_LEAST_ONCE_instance
   InvocationKind_EXACTLY_ONCE_instance
   InvocationKind_UNKNOWN_instance
  def values_1() :
    return [InvocationKind_AT_MOST_ONCE_getInstance(), InvocationKind_AT_LEAST_ONCE_getInstance(), InvocationKind_EXACTLY_ONCE_getInstance(), InvocationKind_UNKNOWN_getInstance()]

  def valueOf_1(value) :
    switch (value) :
      case 'AT_MOST_ONCE':
        return InvocationKind_AT_MOST_ONCE_getInstance();
      case 'AT_LEAST_ONCE':
        return InvocationKind_AT_LEAST_ONCE_getInstance();
      case 'EXACTLY_ONCE':
        return InvocationKind_EXACTLY_ONCE_getInstance();
      case 'UNKNOWN':
        return InvocationKind_UNKNOWN_getInstance();
      default:return THROW_ISE();


   InvocationKind_entriesInitialized
  def InvocationKind_initEntries() :
    if (InvocationKind_entriesInitialized)
      return Unit_getInstance()
    InvocationKind_entriesInitialized = true
    InvocationKind_AT_MOST_ONCE_instance = new InvocationKind('AT_MOST_ONCE', 0)
    InvocationKind_AT_LEAST_ONCE_instance = new InvocationKind('AT_LEAST_ONCE', 1)
    InvocationKind_EXACTLY_ONCE_instance = new InvocationKind('EXACTLY_ONCE', 2)
    InvocationKind_UNKNOWN_instance = new InvocationKind('UNKNOWN', 3)

  def InvocationKind(name, ordinal) :
    Enum.call(this, name, ordinal)

  InvocationKind.$metadata$ = {
    simpleName: 'InvocationKind',
    kind: 'class',
    interfaces: []

  def ExperimentalContracts() :

  ExperimentalContracts.$metadata$ = {
    simpleName: 'ExperimentalContracts',
    kind: 'class',
    interfaces: [Annotation]

  def InvocationKind_AT_MOST_ONCE_getInstance() :
    InvocationKind_initEntries()
    return InvocationKind_AT_MOST_ONCE_instance

  def InvocationKind_AT_LEAST_ONCE_getInstance() :
    InvocationKind_initEntries()
    return InvocationKind_AT_LEAST_ONCE_instance

  def InvocationKind_EXACTLY_ONCE_getInstance() :
    InvocationKind_initEntries()
    return InvocationKind_EXACTLY_ONCE_instance

  def InvocationKind_UNKNOWN_getInstance() :
    InvocationKind_initEntries()
    return InvocationKind_UNKNOWN_instance

  def CallsInPlace() :

  CallsInPlace.$metadata$ = {
    simpleName: 'CallsInPlace',
    kind: 'interface',
    interfaces: [Effect]

  def Returns() :

  Returns.$metadata$ = {
    simpleName: 'Returns',
    kind: 'interface',
    interfaces: [SimpleEffect]

  def ReturnsNotNull() :

  ReturnsNotNull.$metadata$ = {
    simpleName: 'ReturnsNotNull',
    kind: 'interface',
    interfaces: [SimpleEffect]

  def Effect() :

  Effect.$metadata$ = {
    simpleName: 'Effect',
    kind: 'interface',
    interfaces: []

  def SimpleEffect() :

  SimpleEffect.$metadata$ = {
    simpleName: 'SimpleEffect',
    kind: 'interface',
    interfaces: [Effect]

  def ConditionalEffect() :

  ConditionalEffect.$metadata$ = {
    simpleName: 'ConditionalEffect',
    kind: 'interface',
    interfaces: [Effect]

  def Continuation() :

  Continuation.$metadata$ = {
    simpleName: 'Continuation',
    kind: 'interface',
    interfaces: []

  def Continuation_0(context, resumeWith) :
    return new _no_name_provided__0(context, resumeWith)

  def resumeWithException(_this_, exception) :
     tmp0_failure_0 = Companion_getInstance_2()
    return _this_.resumeWith_6(createFailure(exception))

  def resume(_this_, value) :
     tmp0_success_0 = Companion_getInstance_2()
    return _this_.resumeWith_6(value)

  def _get_coroutineContext_() :
    throw new NotImplementedError('Implemented as intrinsic')

  def _no_name_provided__0($context, $resumeWith) :
    this._$context = $context
    this._$resumeWith = $resumeWith

  _no_name_provided__0.prototype._get_context__4 = def () :
    return this._$context

  _no_name_provided__0.prototype.resumeWith_6 = def (result) :
    return this._$resumeWith(new Result(result))

  _no_name_provided__0.$metadata$ = {
    kind: 'class',
    interfaces: [Continuation]

  def Key() :
    Key_instance = this

  Key.$metadata$ = {
    simpleName: 'Key',
    kind: 'object',
    interfaces: [Key_0]

   Key_instance
  def Key_getInstance() :
    if (Key_instance == null)
      new Key()
    return Key_instance

  ContinuationInterceptor.prototype.releaseInterceptedContinuation = def (continuation) :

  ContinuationInterceptor.prototype.get_6 = def (key) :
    if (key instanceof AbstractCoroutineContextKey) :
       tmp
      if (key.isSubKey(this._get_key__2())) :
         tmp_0 = key.tryCast(this)
        tmp = (!(tmp_0 == null) ? isInterface(tmp_0, Element) : false) ? tmp_0 : null
       else :
        tmp = null

      return tmp
     else :

     tmp_1
    if (Key_getInstance() === key) :
      tmp_1 = isInterface(this, Element) ? this : THROW_CCE()
     else :
      tmp_1 = null

    return tmp_1

  ContinuationInterceptor.prototype.minusKey_3 = def (key) :
    if (key instanceof AbstractCoroutineContextKey) :
      return (key.isSubKey(this._get_key__2()) ? !(key.tryCast(this) == null) : false) ? EmptyCoroutineContext_getInstance() : this
     else :

    return Key_getInstance() === key ? EmptyCoroutineContext_getInstance() : this

  def ContinuationInterceptor() :
    Key_getInstance()

  ContinuationInterceptor.$metadata$ = {
    simpleName: 'ContinuationInterceptor',
    kind: 'interface',
    interfaces: [Element]

  def Key_0() :

  Key_0.$metadata$ = {
    simpleName: 'Key',
    kind: 'interface',
    interfaces: []

  Element.prototype.get_6 = def (key) :
     tmp
    if (equals(this._get_key__2(), key)) :
      tmp = isInterface(this, Element) ? this : THROW_CCE()
     else :
      tmp = null

    return tmp

  Element.prototype.fold_3 = def (initial, operation) :
    return operation(initial, this)

  Element.prototype.minusKey_3 = def (key) :
    return equals(this._get_key__2(), key) ? EmptyCoroutineContext_getInstance() : this

  def Element() :

  Element.$metadata$ = {
    simpleName: 'Element',
    kind: 'interface',
    interfaces: [CoroutineContext]

  def _no_name_provided__1() :

  _no_name_provided__1.prototype.invoke_1 = def (acc, element) :
     removed = acc.minusKey_3(element._get_key__2())
     tmp
    if (removed === EmptyCoroutineContext_getInstance()) :
      tmp = element
     else :
       interceptor = removed.get_6(Key_getInstance())
       tmp_0
      if (interceptor == null) :
        tmp_0 = new CombinedContext(removed, element)
       else :
         left = removed.minusKey_3(Key_getInstance())
        tmp_0 = left === EmptyCoroutineContext_getInstance() ? new CombinedContext(element, interceptor) : new CombinedContext(new CombinedContext(left, element), interceptor)

      tmp = tmp_0

    return tmp

  _no_name_provided__1.prototype.invoke_64 = def (p1, p2) :
     tmp = (!(p1 == null) ? isInterface(p1, CoroutineContext) : false) ? p1 : THROW_CCE()
    return this.invoke_1(tmp, (!(p2 == null) ? isInterface(p2, Element) : false) ? p2 : THROW_CCE())

  _no_name_provided__1.$metadata$ = {
    kind: 'class',
    interfaces: []

  CoroutineContext.prototype.plus_3 = def (context) :
     tmp
    if (context === EmptyCoroutineContext_getInstance()) :
      tmp = this
     else :
      tmp = context.fold_3(this, _no_name_provided_$factory_0())

    return tmp

  def CoroutineContext() :

  CoroutineContext.$metadata$ = {
    simpleName: 'CoroutineContext',
    kind: 'interface',
    interfaces: []

  def _no_name_provided_$factory_0() :
     i = new _no_name_provided__1()
    return def (p1, p2) :
      return i.invoke_1(p1, p2)


  def _get_serialVersionUID__0($this) :
    return $this._serialVersionUID_0

  def readResolve_0($this) :
    return EmptyCoroutineContext_getInstance()

  def EmptyCoroutineContext() :
    EmptyCoroutineContext_instance = this
    this._serialVersionUID_0 = new Long(0, 0)

  EmptyCoroutineContext.prototype.get_6 = def (key) :
    return null

  EmptyCoroutineContext.prototype.fold_3 = def (initial, operation) :
    return initial

  EmptyCoroutineContext.prototype.plus_3 = def (context) :
    return context

  EmptyCoroutineContext.prototype.minusKey_3 = def (key) :
    return this

  EmptyCoroutineContext.prototype.hashCode = def () :
    return 0

  EmptyCoroutineContext.prototype.toString = def () :
    return 'EmptyCoroutineContext'

  EmptyCoroutineContext.$metadata$ = {
    simpleName: 'EmptyCoroutineContext',
    kind: 'object',
    interfaces: [CoroutineContext, Serializable]

   EmptyCoroutineContext_instance
  def EmptyCoroutineContext_getInstance() :
    if (EmptyCoroutineContext_instance == null)
      new EmptyCoroutineContext()
    return EmptyCoroutineContext_instance

  def _get_serialVersionUID__1($this) :
    return $this._serialVersionUID_1

  def Companion_1() :
    Companion_instance_0 = this
    this._serialVersionUID_1 = new Long(0, 0)

  Companion_1.$metadata$ = {
    simpleName: 'Companion',
    kind: 'object',
    interfaces: []

   Companion_instance_0
  def Companion_getInstance_0() :
    if (Companion_instance_0 == null)
      new Companion_1()
    return Companion_instance_0

  def readResolve_1($this) :
     tmp0_fold_0 = $this._elements
     tmp1_fold_0 = EmptyCoroutineContext_getInstance()
     accumulator_1 = tmp1_fold_0
     indexedObject = tmp0_fold_0
     inductionVariable = 0
     last = indexedObject.length
    while (inductionVariable < last) :
       element_3 = indexedObject[inductionVariable]
      inductionVariable = inductionVariable + 1 | 0
      accumulator_1 = accumulator_1.plus_3(element_3)

    return accumulator_1

  def _get_left_($this) :
    return $this._left

  def _get_element_($this) :
    return $this._element

  def size($this) :
     cur = $this
     size_0 = 2
    while (true) :
       tmp = cur._left
       tmp0_elvis_lhs = tmp instanceof CombinedContext ? tmp : null
       tmp_0
      if (tmp0_elvis_lhs == null) :
        return size_0
       else :
        tmp_0 = tmp0_elvis_lhs

      cur = tmp_0
       tmp1 = size_0
      size_0 = tmp1 + 1 | 0
      Unit_getInstance()


  def contains_3($this, element) :
    return equals($this.get_6(element._get_key__2()), element)

  def containsAll($this, context) :
     cur = context
    while (true) :
      if (!contains_3($this, cur._element))
        return false
       next = cur._left
      if (next instanceof CombinedContext) :
        cur = next
       else :
        :
          return contains_3($this, isInterface(next, Element) ? next : THROW_CCE())




  def writeReplace($this) :
     n = size($this)
     elements = fillArrayVal(Array(n), null)
     index = {_v: 0
    $this.fold_3(Unit_getInstance(), _no_name_provided_$factory_2(elements, index))
     tmp0_check_0 = index._v === n
    if (!tmp0_check_0) :
       message_2 = 'Check failed.'
      throw IllegalStateException_init_$Create$_0(toString_0(message_2))
    return new Serialized(isArray(elements) ? elements : THROW_CCE())

  def Serialized(elements) :
    Companion_getInstance_0()
    this._elements = elements

  Serialized.prototype._get_elements_ = def () :
    return this._elements

  Serialized.$metadata$ = {
    simpleName: 'Serialized',
    kind: 'class',
    interfaces: [Serializable]

  def _no_name_provided__2() :

  _no_name_provided__2.prototype.invoke_3 = def (acc, element) :
     tmp
    if (charSequenceLength(acc) === 0) :
      tmp = toString_0(element)
     else :
      :
        tmp = '' + acc + ', ' + element


    return tmp

  _no_name_provided__2.prototype.invoke_64 = def (p1, p2) :
     tmp = (!(p1 == null) ? typeof p1 === 'string' : false) ? p1 : THROW_CCE()
    return this.invoke_3(tmp, (!(p2 == null) ? isInterface(p2, Element) : false) ? p2 : THROW_CCE())

  _no_name_provided__2.$metadata$ = {
    kind: 'class',
    interfaces: []

  def _no_name_provided__3($elements, $index) :
    this._$elements = $elements
    this._$index = $index

  _no_name_provided__3.prototype.invoke_5 = def (_anonymous_parameter_0_, element) :
     tmp0 = this._$index._v
    this._$index._v = tmp0 + 1 | 0
    this._$elements[tmp0] = element

  _no_name_provided__3.prototype.invoke_64 = def (p1, p2) :
     tmp = p1 instanceof Unit ? p1 : THROW_CCE()
    this.invoke_5(tmp, (!(p2 == null) ? isInterface(p2, Element) : false) ? p2 : THROW_CCE())
    return Unit_getInstance()

  _no_name_provided__3.$metadata$ = {
    kind: 'class',
    interfaces: []

  def CombinedContext(left, element) :
    this._left = left
    this._element = element

  CombinedContext.prototype.get_6 = def (key) :
     cur = this
    while (true) :
       tmp0_safe_receiver = cur._element.get_6(key)
      if (tmp0_safe_receiver == null)
        null;
      else :
        return tmp0_safe_receiver

      Unit_getInstance()
       next = cur._left
      if (next instanceof CombinedContext) :
        cur = next
       else :
        :
          return next.get_6(key)




  CombinedContext.prototype.fold_3 = def (initial, operation) :
    return operation(this._left.fold_3(initial, operation), this._element)

  CombinedContext.prototype.minusKey_3 = def (key) :
     tmp0_safe_receiver = this._element.get_6(key)
    if (tmp0_safe_receiver == null)
      null;
    else :
      return this._left

    Unit_getInstance()
     newLeft = this._left.minusKey_3(key)
    return newLeft === this._left ? this : newLeft === EmptyCoroutineContext_getInstance() ? this._element : new CombinedContext(newLeft, this._element)

  CombinedContext.prototype.equals = def (other) :
     tmp
    if (this === other) :
      tmp = true
     else :
       tmp_0
       tmp_1
      if (other instanceof CombinedContext) :
        tmp_1 = size(other) === size(this)
       else :
        :
          tmp_1 = false


      if (tmp_1) :
        tmp_0 = containsAll(other, this)
       else :
        :
          tmp_0 = false


      tmp = tmp_0

    return tmp

  CombinedContext.prototype.hashCode = def () :
    return hashCode(this._left) + hashCode(this._element) | 0

  CombinedContext.prototype.toString = def () :
    return '[' + this.fold_3('', _no_name_provided_$factory_1()) + ']'

  CombinedContext.$metadata$ = {
    simpleName: 'CombinedContext',
    kind: 'class',
    interfaces: [CoroutineContext, Serializable]

  def _get_safeCast_($this) :
    return $this._safeCast

  def _get_topmostKey_($this) :
    return $this._topmostKey

  def AbstractCoroutineContextKey(baseKey, safeCast) :
    this._safeCast = safeCast
     tmp = this
     tmp_0
    if (baseKey instanceof AbstractCoroutineContextKey) :
      tmp_0 = baseKey._topmostKey
     else :
      :
        tmp_0 = baseKey


    tmp._topmostKey = tmp_0

  AbstractCoroutineContextKey.prototype.tryCast = def (element) :
    return this._safeCast(element)

  AbstractCoroutineContextKey.prototype.isSubKey = def (key) :
    return key === this ? true : this._topmostKey === key

  AbstractCoroutineContextKey.$metadata$ = {
    simpleName: 'AbstractCoroutineContextKey',
    kind: 'class',
    interfaces: [Key_0]

  def _no_name_provided_$factory_1() :
     i = new _no_name_provided__2()
    return def (p1, p2) :
      return i.invoke_3(p1, p2)


  def _no_name_provided_$factory_2($elements, $index) :
     i = new _no_name_provided__3($elements, $index)
    return def (p1, p2) :
      i.invoke_5(p1, p2)
      return Unit_getInstance()


  def _get_COROUTINE_SUSPENDED_() :
    return CoroutineSingletons_COROUTINE_SUSPENDED_getInstance()

   CoroutineSingletons_COROUTINE_SUSPENDED_instance
   CoroutineSingletons_UNDECIDED_instance
   CoroutineSingletons_RESUMED_instance
  def values_2() :
    return [CoroutineSingletons_COROUTINE_SUSPENDED_getInstance(), CoroutineSingletons_UNDECIDED_getInstance(), CoroutineSingletons_RESUMED_getInstance()]

  def valueOf_2(value) :
    switch (value) :
      case 'COROUTINE_SUSPENDED':
        return CoroutineSingletons_COROUTINE_SUSPENDED_getInstance();
      case 'UNDECIDED':
        return CoroutineSingletons_UNDECIDED_getInstance();
      case 'RESUMED':
        return CoroutineSingletons_RESUMED_getInstance();
      default:return THROW_ISE();


   CoroutineSingletons_entriesInitialized
  def CoroutineSingletons_initEntries() :
    if (CoroutineSingletons_entriesInitialized)
      return Unit_getInstance()
    CoroutineSingletons_entriesInitialized = true
    CoroutineSingletons_COROUTINE_SUSPENDED_instance = new CoroutineSingletons('COROUTINE_SUSPENDED', 0)
    CoroutineSingletons_UNDECIDED_instance = new CoroutineSingletons('UNDECIDED', 1)
    CoroutineSingletons_RESUMED_instance = new CoroutineSingletons('RESUMED', 2)

  def CoroutineSingletons(name, ordinal) :
    Enum.call(this, name, ordinal)

  CoroutineSingletons.$metadata$ = {
    simpleName: 'CoroutineSingletons',
    kind: 'class',
    interfaces: []

  def CoroutineSingletons_COROUTINE_SUSPENDED_getInstance() :
    CoroutineSingletons_initEntries()
    return CoroutineSingletons_COROUTINE_SUSPENDED_instance

  def CoroutineSingletons_UNDECIDED_getInstance() :
    CoroutineSingletons_initEntries()
    return CoroutineSingletons_UNDECIDED_instance

  def CoroutineSingletons_RESUMED_getInstance() :
    CoroutineSingletons_initEntries()
    return CoroutineSingletons_RESUMED_instance

  def and(_this_, other) :
    return toByte(_this_ & other)

  def or(_this_, other) :
    return toByte(_this_ | other)

  def xor(_this_, other) :
    return toByte(_this_ ^ other)

  def inv(_this_) :
    return toByte(~_this_)

  def and_0(_this_, other) :
    return toShort(_this_ & other)

  def or_0(_this_, other) :
    return toShort(_this_ | other)

  def xor_0(_this_, other) :
    return toShort(_this_ ^ other)

  def inv_0(_this_) :
    return toShort(~_this_)

  def ExperimentalTypeInference() :

  ExperimentalTypeInference.$metadata$ = {
    simpleName: 'ExperimentalTypeInference',
    kind: 'class',
    interfaces: [Annotation]

  def RequireKotlin_init_$Init$(version, message, level, versionKind, errorCode, $mask0, $marker, $this) :
    if (!(($mask0 & 2) === 0))
      message = ''
    if (!(($mask0 & 4) === 0))
      level = DeprecationLevel_ERROR_getInstance()
    if (!(($mask0 & 8) === 0))
      versionKind = RequireKotlinVersionKind_LANGUAGE_VERSION_getInstance()
    if (!(($mask0 & 16) === 0))
      errorCode = -1
    RequireKotlin.call($this, version, message, level, versionKind, errorCode)
    return $this

  def RequireKotlin_init_$Create$(version, message, level, versionKind, errorCode, $mask0, $marker) :
    return RequireKotlin_init_$Init$(version, message, level, versionKind, errorCode, $mask0, $marker, Object.create(RequireKotlin.prototype))

  def RequireKotlin(version, message, level, versionKind, errorCode) :
    this._version = version
    this._message_0 = message
    this._level_1 = level
    this._versionKind = versionKind
    this._errorCode = errorCode

  RequireKotlin.prototype._get_version__0 = def () :
    return this._version

  RequireKotlin.prototype._get_message__15 = def () :
    return this._message_0

  RequireKotlin.prototype._get_level__2 = def () :
    return this._level_1

  RequireKotlin.prototype._get_versionKind_ = def () :
    return this._versionKind

  RequireKotlin.prototype._get_errorCode_ = def () :
    return this._errorCode

  RequireKotlin.$metadata$ = {
    simpleName: 'RequireKotlin',
    kind: 'class',
    interfaces: [Annotation]

   RequireKotlinVersionKind_LANGUAGE_VERSION_instance
   RequireKotlinVersionKind_COMPILER_VERSION_instance
   RequireKotlinVersionKind_API_VERSION_instance
  def values_3() :
    return [RequireKotlinVersionKind_LANGUAGE_VERSION_getInstance(), RequireKotlinVersionKind_COMPILER_VERSION_getInstance(), RequireKotlinVersionKind_API_VERSION_getInstance()]

  def valueOf_3(value) :
    switch (value) :
      case 'LANGUAGE_VERSION':
        return RequireKotlinVersionKind_LANGUAGE_VERSION_getInstance();
      case 'COMPILER_VERSION':
        return RequireKotlinVersionKind_COMPILER_VERSION_getInstance();
      case 'API_VERSION':
        return RequireKotlinVersionKind_API_VERSION_getInstance();
      default:return THROW_ISE();


   RequireKotlinVersionKind_entriesInitialized
  def RequireKotlinVersionKind_initEntries() :
    if (RequireKotlinVersionKind_entriesInitialized)
      return Unit_getInstance()
    RequireKotlinVersionKind_entriesInitialized = true
    RequireKotlinVersionKind_LANGUAGE_VERSION_instance = new RequireKotlinVersionKind('LANGUAGE_VERSION', 0)
    RequireKotlinVersionKind_COMPILER_VERSION_instance = new RequireKotlinVersionKind('COMPILER_VERSION', 1)
    RequireKotlinVersionKind_API_VERSION_instance = new RequireKotlinVersionKind('API_VERSION', 2)

  def RequireKotlinVersionKind(name, ordinal) :
    Enum.call(this, name, ordinal)

  RequireKotlinVersionKind.$metadata$ = {
    simpleName: 'RequireKotlinVersionKind',
    kind: 'class',
    interfaces: []

  def InlineOnly() :

  InlineOnly.$metadata$ = {
    simpleName: 'InlineOnly',
    kind: 'class',
    interfaces: [Annotation]

  def NoInfer() :

  NoInfer.$metadata$ = {
    simpleName: 'NoInfer',
    kind: 'class',
    interfaces: [Annotation]

  def DynamicExtension() :

  DynamicExtension.$metadata$ = {
    simpleName: 'DynamicExtension',
    kind: 'class',
    interfaces: [Annotation]

  def ContractsDsl() :

  ContractsDsl.$metadata$ = {
    simpleName: 'ContractsDsl',
    kind: 'class',
    interfaces: [Annotation]

  def OnlyInputTypes() :

  OnlyInputTypes.$metadata$ = {
    simpleName: 'OnlyInputTypes',
    kind: 'class',
    interfaces: [Annotation]

  def RequireKotlinVersionKind_LANGUAGE_VERSION_getInstance() :
    RequireKotlinVersionKind_initEntries()
    return RequireKotlinVersionKind_LANGUAGE_VERSION_instance

  def RequireKotlinVersionKind_COMPILER_VERSION_getInstance() :
    RequireKotlinVersionKind_initEntries()
    return RequireKotlinVersionKind_COMPILER_VERSION_instance

  def RequireKotlinVersionKind_API_VERSION_getInstance() :
    RequireKotlinVersionKind_initEntries()
    return RequireKotlinVersionKind_API_VERSION_instance

  def KClassifier() :

  KClassifier.$metadata$ = {
    simpleName: 'KClassifier',
    kind: 'interface',
    interfaces: []

  def KTypeParameter() :

  KTypeParameter.$metadata$ = {
    simpleName: 'KTypeParameter',
    kind: 'interface',
    interfaces: [KClassifier]

  def Companion_2() :
    Companion_instance_1 = this
    this._star = new KTypeProjection(null, null)

  Companion_2.prototype._get_star_ = def () :
    return this._star

  Companion_2.prototype._get_STAR_ = def () :
    return this._star

  Companion_2.prototype.invariant = def (type) :
    return new KTypeProjection(KVariance_INVARIANT_getInstance(), type)

  Companion_2.prototype.contravariant = def (type) :
    return new KTypeProjection(KVariance_IN_getInstance(), type)

  Companion_2.prototype.covariant = def (type) :
    return new KTypeProjection(KVariance_OUT_getInstance(), type)

  Companion_2.$metadata$ = {
    simpleName: 'Companion',
    kind: 'object',
    interfaces: []

   Companion_instance_1
  def Companion_getInstance_1() :
    if (Companion_instance_1 == null)
      new Companion_2()
    return Companion_instance_1

  def KTypeProjection(variance, type) :
    Companion_getInstance_1()
    this._variance = variance
    this._type = type
     tmp0_require_0 = this._variance == null === (this._type == null)
    if (!tmp0_require_0) :
       message_2 = this._variance == null ? 'Star projection must have no type specified.' : '' + 'The projection variance ' + this._variance + ' requires type to be specified.'
      throw IllegalArgumentException_init_$Create$_0(toString_0(message_2))

  KTypeProjection.prototype._get_variance__1 = def () :
    return this._variance

  KTypeProjection.prototype._get_type_ = def () :
    return this._type

  KTypeProjection.prototype.toString = def () :
     tmp0_subject = this._variance
     tmp
    if (tmp0_subject == null) :
      tmp = '*'
     else if (equals(tmp0_subject, KVariance_INVARIANT_getInstance())) :
      tmp = toString(this._type)
     else if (equals(tmp0_subject, KVariance_IN_getInstance())) :
      tmp = '' + 'in ' + this._type
     else if (equals(tmp0_subject, KVariance_OUT_getInstance())) :
      tmp = '' + 'out ' + this._type
     else :
      noWhenBranchMatchedException()

    return tmp

  KTypeProjection.prototype.component1_0 = def () :
    return this._variance

  KTypeProjection.prototype.component2_0 = def () :
    return this._type

  KTypeProjection.prototype.copy = def (variance, type) :
    return new KTypeProjection(variance, type)

  KTypeProjection.prototype.copy$default = def (variance, type, $mask0, $handler) :
    if (!(($mask0 & 1) === 0))
      variance = this._variance
    if (!(($mask0 & 2) === 0))
      type = this._type
    return this.copy(variance, type)

  KTypeProjection.prototype.hashCode = def () :
     result = this._variance == null ? 0 : this._variance.hashCode()
    result = imul(result, 31) + (this._type == null ? 0 : hashCode(this._type)) | 0
    return result

  KTypeProjection.prototype.equals = def (other) :
    if (this === other)
      return true
    if (!(other instanceof KTypeProjection))
      return false;
    else :

     tmp0_other_with_cast = other instanceof KTypeProjection ? other : THROW_CCE()
    if (!equals(this._variance, tmp0_other_with_cast._variance))
      return false
    if (!equals(this._type, tmp0_other_with_cast._type))
      return false
    return true

  KTypeProjection.$metadata$ = {
    simpleName: 'KTypeProjection',
    kind: 'class',
    interfaces: []

   KVariance_INVARIANT_instance
   KVariance_IN_instance
   KVariance_OUT_instance
  def values_4() :
    return [KVariance_INVARIANT_getInstance(), KVariance_IN_getInstance(), KVariance_OUT_getInstance()]

  def valueOf_4(value) :
    switch (value) :
      case 'INVARIANT':
        return KVariance_INVARIANT_getInstance();
      case 'IN':
        return KVariance_IN_getInstance();
      case 'OUT':
        return KVariance_OUT_getInstance();
      default:return THROW_ISE();


   KVariance_entriesInitialized
  def KVariance_initEntries() :
    if (KVariance_entriesInitialized)
      return Unit_getInstance()
    KVariance_entriesInitialized = true
    KVariance_INVARIANT_instance = new KVariance('INVARIANT', 0)
    KVariance_IN_instance = new KVariance('IN', 1)
    KVariance_OUT_instance = new KVariance('OUT', 2)

  def KVariance(name, ordinal) :
    Enum.call(this, name, ordinal)

  KVariance.$metadata$ = {
    simpleName: 'KVariance',
    kind: 'class',
    interfaces: []

  def KVariance_INVARIANT_getInstance() :
    KVariance_initEntries()
    return KVariance_INVARIANT_instance

  def KVariance_IN_getInstance() :
    KVariance_initEntries()
    return KVariance_IN_instance

  def KVariance_OUT_getInstance() :
    KVariance_initEntries()
    return KVariance_OUT_instance

  def appendElement(_this_, element, transform) :
    if (!(transform == null)) :
      _this_.append_3(transform(element))
      Unit_getInstance()
     else :
      if (element == null ? true : isCharSequence(element)) :
        _this_.append_3(element)
        Unit_getInstance()
       else :
        if (element instanceof Char) :
          _this_.append_2(element)
          Unit_getInstance()
         else :
          :
            _this_.append_3(toString(element))
            Unit_getInstance()





  def isEmpty(_this_) :
    return charSequenceLength(_this_) === 0

  def _get_lastIndex__5(_this_) :
    return charSequenceLength(_this_) - 1 | 0

  def _get_UNDEFINED_RESULT_() :
    return UNDEFINED_RESULT

   UNDEFINED_RESULT
  def UNDEFINED_RESULT$init$() :
     tmp0_success_0 = Companion_getInstance_2()
     tmp1_success_0 = _get_COROUTINE_SUSPENDED_()
    return tmp1_success_0

  def check(value) :
    if (!value) :
       message_2 = 'Check failed.'
      throw IllegalStateException_init_$Create$_0(toString_0(message_2))

  def check_0(value, lazyMessage) :
    if (!value) :
       message = lazyMessage()
      throw IllegalStateException_init_$Create$_0(toString_0(message))

  def error(message) :
    throw IllegalStateException_init_$Create$_0(toString_0(message))

  def require_0(value, lazyMessage) :
    if (!value) :
       message = lazyMessage()
      throw IllegalArgumentException_init_$Create$_0(toString_0(message))

  def _Result___get_value__impl_(this_0) :
    return this_0

  def _Result___get_isSuccess__impl_(this_0) :
     tmp = _Result___get_value__impl_(this_0)
    return !(tmp instanceof Failure)

  def _Result___get_isFailure__impl_(this_0) :
     tmp = _Result___get_value__impl_(this_0)
    return tmp instanceof Failure

  def Result__getOrNull_impl(this_0) :
     tmp
    if (_Result___get_isFailure__impl_(this_0)) :
      tmp = null
     else :
       tmp_0 = _Result___get_value__impl_(this_0)
      tmp = (tmp_0 == null ? true : isObject(tmp_0)) ? tmp_0 : THROW_CCE()

    return tmp

  def Result__exceptionOrNull_impl(this_0) :
     tmp0_subject = _Result___get_value__impl_(this_0)
     tmp
    if (tmp0_subject instanceof Failure) :
      tmp = _Result___get_value__impl_(this_0)._exception
     else :
      :
        tmp = null


    return tmp

  def Result__toString_impl(this_0) :
     tmp0_subject = _Result___get_value__impl_(this_0)
     tmp
    if (tmp0_subject instanceof Failure) :
      tmp = toString_0(_Result___get_value__impl_(this_0))
     else :
      :
        tmp = '' + 'Success(' + _Result___get_value__impl_(this_0) + ')'


    return tmp

  def Companion_3() :
    Companion_instance_2 = this

  Companion_3.prototype.success = def (value) :
    return value

  Companion_3.prototype.failure = def (exception) :
    return createFailure(exception)

  Companion_3.$metadata$ = {
    simpleName: 'Companion',
    kind: 'object',
    interfaces: []

   Companion_instance_2
  def Companion_getInstance_2() :
    if (Companion_instance_2 == null)
      new Companion_3()
    return Companion_instance_2

  def Failure(exception) :
    this._exception = exception

  Failure.prototype._get_exception__0 = def () :
    return this._exception

  Failure.prototype.equals = def (other) :
     tmp
    if (other instanceof Failure) :
      tmp = equals(this._exception, other._exception)
     else :
      :
        tmp = false


    return tmp

  Failure.prototype.hashCode = def () :
    return hashCode(this._exception)

  Failure.prototype.toString = def () :
    return '' + 'Failure(' + this._exception + ')'

  Failure.$metadata$ = {
    simpleName: 'Failure',
    kind: 'class',
    interfaces: [Serializable]

  def Result__hashCode_impl(this_0) :
    return this_0 == null ? 0 : hashCode(this_0)

  def Result__equals_impl(this_0, other) :
    if (!(other instanceof Result))
      return false;
    else :

     tmp0_other_with_cast = other instanceof Result ? other._value : THROW_CCE()
    if (!equals(this_0, tmp0_other_with_cast))
      return false
    return true

  def Result(value) :
    Companion_getInstance_2()
    this._value = value

  Result.prototype.toString = def () :
    return Result__toString_impl(this._value)

  Result.prototype.hashCode = def () :
    return Result__hashCode_impl(this._value)

  Result.prototype.equals = def (other) :
    return Result__equals_impl(this._value, other)

  Result.$metadata$ = {
    simpleName: 'Result',
    kind: 'class',
    interfaces: [Serializable]

  def createFailure(exception) :
    return new Failure(exception)

  def getOrThrow(_this_) :
    throwOnFailure(_this_)
     tmp = _Result___get_value__impl_(_this_)
    return (tmp == null ? true : isObject(tmp)) ? tmp : THROW_CCE()

  def throwOnFailure(_this_) :
     tmp = _Result___get_value__impl_(_this_)
    if (tmp instanceof Failure)
      throw _Result___get_value__impl_(_this_)._exception;
    else :


  def run(block) :
    return block()

  def TODO() :
    throw NotImplementedError_init_$Create$(null, 1, null)

  def NotImplementedError_init_$Init$(message, $mask0, $marker, $this) :
    if (!(($mask0 & 1) === 0))
      message = 'An operation is not implemented.'
    NotImplementedError.call($this, message)
    return $this

  def NotImplementedError_init_$Create$(message, $mask0, $marker) :
     tmp = NotImplementedError_init_$Init$(message, $mask0, $marker, Object.create(NotImplementedError.prototype))
    captureStack(tmp, NotImplementedError_init_$Create$)
    return tmp

  def NotImplementedError(message) :
    Error_init_$Init$_0(message, this)
    captureStack(this, NotImplementedError)

  NotImplementedError.$metadata$ = {
    simpleName: 'NotImplementedError',
    kind: 'class',
    interfaces: []

  def let_0(_this_, block) :
    return block(_this_)

  def also(_this_, block) :
    block(_this_)
    return _this_

  def with_0(receiver, block) :
    return block(receiver)

  def run_0(_this_, block) :
    return block(_this_)

  def apply(_this_, block) :
    block(_this_)
    return _this_

  def repeat(times, action) :
     inductionVariable = 0
    if (inductionVariable < times)
      do :
         index = inductionVariable
        inductionVariable = inductionVariable + 1 | 0
        action(index)

       while (inductionVariable < times)

  def _UByte___get_data__impl_(this_0) :
    return this_0

  def Companion_4() :
    Companion_instance_3 = this
    this._MIN_VALUE = 0
    this._MAX_VALUE = -1
    this._SIZE_BYTES = 1
    this._SIZE_BITS = 8

  Companion_4.prototype._get_MIN_VALUE_ = def () :
    return this._MIN_VALUE

  Companion_4.prototype._get_MAX_VALUE_ = def () :
    return this._MAX_VALUE

  Companion_4.prototype._get_SIZE_BYTES__9 = def () :
    return this._SIZE_BYTES

  Companion_4.prototype._get_SIZE_BITS__9 = def () :
    return this._SIZE_BITS

  Companion_4.$metadata$ = {
    simpleName: 'Companion',
    kind: 'object',
    interfaces: []

   Companion_instance_3
  def Companion_getInstance_3() :
    if (Companion_instance_3 == null)
      new Companion_4()
    return Companion_instance_3

  def UByte__compareTo_impl(this_0, other) :
     tmp = _UByte___get_data__impl_(this_0) & 255
    return compareTo_0(tmp, _UByte___get_data__impl_(other) & 255)

  def UByte__compareTo_impl_0(this_0, other) :
     tmp = this_0._data
    return UByte__compareTo_impl(tmp, other instanceof UByte ? other._data : THROW_CCE())

  def UByte__compareTo_impl_1(this_0, other) :
     tmp = _UByte___get_data__impl_(this_0) & 255
    return compareTo_0(tmp, _UShort___get_data__impl_(other) & 65535)

  def UByte__compareTo_impl_2(this_0, other) :
     tmp0_compareTo_0 = _UByte___get_data__impl_(this_0) & 255
    return uintCompare(_UInt___get_data__impl_(tmp0_compareTo_0), _UInt___get_data__impl_(other))

  def UByte__compareTo_impl_3(this_0, other) :
     tmp0_compareTo_0 = toLong(_UByte___get_data__impl_(this_0)).and(new Long(255, 0))
    return ulongCompare(_ULong___get_data__impl_(tmp0_compareTo_0), _ULong___get_data__impl_(other))

  def UByte__plus_impl(this_0, other) :
     tmp0_plus_0 = _UByte___get_data__impl_(this_0) & 255
     tmp1_plus_0 = _UByte___get_data__impl_(other) & 255
    return _UInt___get_data__impl_(tmp0_plus_0) + _UInt___get_data__impl_(tmp1_plus_0) | 0

  def UByte__plus_impl_0(this_0, other) :
     tmp0_plus_0 = _UByte___get_data__impl_(this_0) & 255
     tmp1_plus_0 = _UShort___get_data__impl_(other) & 65535
    return _UInt___get_data__impl_(tmp0_plus_0) + _UInt___get_data__impl_(tmp1_plus_0) | 0

  def UByte__plus_impl_1(this_0, other) :
     tmp0_plus_0 = _UByte___get_data__impl_(this_0) & 255
    return _UInt___get_data__impl_(tmp0_plus_0) + _UInt___get_data__impl_(other) | 0

  def UByte__plus_impl_2(this_0, other) :
     tmp0_plus_0 = toLong(_UByte___get_data__impl_(this_0)).and(new Long(255, 0))
    return _ULong___get_data__impl_(tmp0_plus_0).plus_38(_ULong___get_data__impl_(other))

  def UByte__minus_impl(this_0, other) :
     tmp0_minus_0 = _UByte___get_data__impl_(this_0) & 255
     tmp1_minus_0 = _UByte___get_data__impl_(other) & 255
    return _UInt___get_data__impl_(tmp0_minus_0) - _UInt___get_data__impl_(tmp1_minus_0) | 0

  def UByte__minus_impl_0(this_0, other) :
     tmp0_minus_0 = _UByte___get_data__impl_(this_0) & 255
     tmp1_minus_0 = _UShort___get_data__impl_(other) & 65535
    return _UInt___get_data__impl_(tmp0_minus_0) - _UInt___get_data__impl_(tmp1_minus_0) | 0

  def UByte__minus_impl_1(this_0, other) :
     tmp0_minus_0 = _UByte___get_data__impl_(this_0) & 255
    return _UInt___get_data__impl_(tmp0_minus_0) - _UInt___get_data__impl_(other) | 0

  def UByte__minus_impl_2(this_0, other) :
     tmp0_minus_0 = toLong(_UByte___get_data__impl_(this_0)).and(new Long(255, 0))
    return _ULong___get_data__impl_(tmp0_minus_0).minus_34(_ULong___get_data__impl_(other))

  def UByte__times_impl(this_0, other) :
     tmp0_times_0 = _UByte___get_data__impl_(this_0) & 255
     tmp1_times_0 = _UByte___get_data__impl_(other) & 255
    return imul(_UInt___get_data__impl_(tmp0_times_0), _UInt___get_data__impl_(tmp1_times_0))

  def UByte__times_impl_0(this_0, other) :
     tmp0_times_0 = _UByte___get_data__impl_(this_0) & 255
     tmp1_times_0 = _UShort___get_data__impl_(other) & 65535
    return imul(_UInt___get_data__impl_(tmp0_times_0), _UInt___get_data__impl_(tmp1_times_0))

  def UByte__times_impl_1(this_0, other) :
     tmp0_times_0 = _UByte___get_data__impl_(this_0) & 255
    return imul(_UInt___get_data__impl_(tmp0_times_0), _UInt___get_data__impl_(other))

  def UByte__times_impl_2(this_0, other) :
     tmp0_times_0 = toLong(_UByte___get_data__impl_(this_0)).and(new Long(255, 0))
    return _ULong___get_data__impl_(tmp0_times_0).times_32(_ULong___get_data__impl_(other))

  def UByte__div_impl(this_0, other) :
     tmp0_div_0 = _UByte___get_data__impl_(this_0) & 255
     tmp1_div_0 = _UByte___get_data__impl_(other) & 255
    return uintDivide(tmp0_div_0, tmp1_div_0)

  def UByte__div_impl_0(this_0, other) :
     tmp0_div_0 = _UByte___get_data__impl_(this_0) & 255
     tmp1_div_0 = _UShort___get_data__impl_(other) & 65535
    return uintDivide(tmp0_div_0, tmp1_div_0)

  def UByte__div_impl_1(this_0, other) :
     tmp0_div_0 = _UByte___get_data__impl_(this_0) & 255
    return uintDivide(tmp0_div_0, other)

  def UByte__div_impl_2(this_0, other) :
     tmp0_div_0 = toLong(_UByte___get_data__impl_(this_0)).and(new Long(255, 0))
    return ulongDivide(tmp0_div_0, other)

  def UByte__rem_impl(this_0, other) :
     tmp0_rem_0 = _UByte___get_data__impl_(this_0) & 255
     tmp1_rem_0 = _UByte___get_data__impl_(other) & 255
    return uintRemainder(tmp0_rem_0, tmp1_rem_0)

  def UByte__rem_impl_0(this_0, other) :
     tmp0_rem_0 = _UByte___get_data__impl_(this_0) & 255
     tmp1_rem_0 = _UShort___get_data__impl_(other) & 65535
    return uintRemainder(tmp0_rem_0, tmp1_rem_0)

  def UByte__rem_impl_1(this_0, other) :
     tmp0_rem_0 = _UByte___get_data__impl_(this_0) & 255
    return uintRemainder(tmp0_rem_0, other)

  def UByte__rem_impl_2(this_0, other) :
     tmp0_rem_0 = toLong(_UByte___get_data__impl_(this_0)).and(new Long(255, 0))
    return ulongRemainder(tmp0_rem_0, other)

  def UByte__inc_impl(this_0) :
    return numberToByte(_UByte___get_data__impl_(this_0) + 1)

  def UByte__dec_impl(this_0) :
    return numberToByte(_UByte___get_data__impl_(this_0) - 1)

  def UByte__rangeTo_impl(this_0, other) :
     tmp = _UByte___get_data__impl_(this_0) & 255
    return new UIntRange(tmp, _UByte___get_data__impl_(other) & 255)

  def UByte__and_impl(this_0, other) :
     tmp0_and_0 = _UByte___get_data__impl_(this_0)
     tmp1_and_0 = _UByte___get_data__impl_(other)
    return toByte(tmp0_and_0 & tmp1_and_0)

  def UByte__or_impl(this_0, other) :
     tmp0_or_0 = _UByte___get_data__impl_(this_0)
     tmp1_or_0 = _UByte___get_data__impl_(other)
    return toByte(tmp0_or_0 | tmp1_or_0)

  def UByte__xor_impl(this_0, other) :
     tmp0_xor_0 = _UByte___get_data__impl_(this_0)
     tmp1_xor_0 = _UByte___get_data__impl_(other)
    return toByte(tmp0_xor_0 ^ tmp1_xor_0)

  def UByte__inv_impl(this_0) :
     tmp0_inv_0 = _UByte___get_data__impl_(this_0)
    return toByte(~tmp0_inv_0)

  def UByte__toByte_impl(this_0) :
    return _UByte___get_data__impl_(this_0)

  def UByte__toShort_impl(this_0) :
     tmp0_and_0 = _UByte___get_data__impl_(this_0)
     tmp1_and_0 = 255
    return toShort(tmp0_and_0 & tmp1_and_0)

  def UByte__toInt_impl(this_0) :
    return _UByte___get_data__impl_(this_0) & 255

  def UByte__toLong_impl(this_0) :
    return toLong(_UByte___get_data__impl_(this_0)).and(new Long(255, 0))

  def UByte__toUByte_impl(this_0) :
    return this_0

  def UByte__toUShort_impl(this_0) :
     tmp0_and_0 = _UByte___get_data__impl_(this_0)
     tmp1_and_0 = 255
    return toShort(tmp0_and_0 & tmp1_and_0)

  def UByte__toUInt_impl(this_0) :
    return _UByte___get_data__impl_(this_0) & 255

  def UByte__toULong_impl(this_0) :
    return toLong(_UByte___get_data__impl_(this_0)).and(new Long(255, 0))

  def UByte__toFloat_impl(this_0) :
    return _UByte___get_data__impl_(this_0) & 255

  def UByte__toDouble_impl(this_0) :
    return _UByte___get_data__impl_(this_0) & 255

  def UByte__toString_impl(this_0) :
    return (_UByte___get_data__impl_(this_0) & 255).toString()

  def UByte__hashCode_impl(this_0) :
    return this_0

  def UByte__equals_impl(this_0, other) :
    if (!(other instanceof UByte))
      return false;
    else :

     tmp0_other_with_cast = other instanceof UByte ? other._data : THROW_CCE()
    if (!(this_0 === tmp0_other_with_cast))
      return false
    return true

  def UByte(data) :
    Companion_getInstance_3()
    this._data = data

  UByte.prototype.compareTo_5 = def (other) :
    return UByte__compareTo_impl(this._data, other)

  UByte.prototype.compareTo_25 = def (other) :
    return UByte__compareTo_impl_0(this, other)

  UByte.prototype.toString = def () :
    return UByte__toString_impl(this._data)

  UByte.prototype.hashCode = def () :
    return UByte__hashCode_impl(this._data)

  UByte.prototype.equals = def (other) :
    return UByte__equals_impl(this._data, other)

  UByte.$metadata$ = {
    simpleName: 'UByte',
    kind: 'class',
    interfaces: [Comparable]

  def toUByte(_this_) :
    return toByte(_this_)

  def toUByte_0(_this_) :
    return toByte(_this_)

  def toUByte_1(_this_) :
    return _this_.toByte_6()

  def toUByte_2(_this_) :
    return _this_

  def _get_array_($this) :
    return $this._array

  def _set_index_($this, _set___) :
    $this._index_0 = _set___

  def _get_index_($this) :
    return $this._index_0

  def _UByteArray___get_storage__impl_(this_0) :
    return this_0

  def _UByteArray___init__impl_(size_0) :
     tmp = new Int8Array(size_0)
    return tmp

  def UByteArray__get_impl(this_0, index) :
     tmp0_toUByte_0 = _UByteArray___get_storage__impl_(this_0)[index]
    return tmp0_toUByte_0

  def UByteArray__set_impl(this_0, index, value) :
     tmp = _UByteArray___get_storage__impl_(this_0)
    tmp[index] = _UByte___get_data__impl_(value)

  def _UByteArray___get_size__impl_(this_0) :
    return _UByteArray___get_storage__impl_(this_0).length

  def UByteArray__iterator_impl(this_0) :
    return new Iterator(_UByteArray___get_storage__impl_(this_0))

  def Iterator(array) :
    UByteIterator.call(this)
    this._array = array
    this._index_0 = 0

  Iterator.prototype.hasNext_37 = def () :
    return this._index_0 < this._array.length

  Iterator.prototype.nextUByte_0 = def () :
     tmp
    if (this._index_0 < this._array.length) :
       tmp0_this = this
       tmp1 = tmp0_this._index_0
      tmp0_this._index_0 = tmp1 + 1 | 0
       tmp0_toUByte_0 = this._array[tmp1]
      tmp = tmp0_toUByte_0
     else :
      throw NoSuchElementException_init_$Create$_0(this._index_0.toString())

    return tmp

  Iterator.$metadata$ = {
    simpleName: 'Iterator',
    kind: 'class',
    interfaces: []

  def UByteArray__contains_impl(this_0, element) :
     tmp = isObject(new UByte(element)) ? new UByte(element) : THROW_CCE()
    if (!(tmp instanceof UByte))
      return false;
    else :

     tmp_0 = _UByteArray___get_storage__impl_(this_0)
    return contains(tmp_0, _UByte___get_data__impl_(element))

  def UByteArray__contains_impl_0(this_0, element) :
    if (!(element instanceof UByte))
      return false;
    else :

     tmp = this_0._storage
    return UByteArray__contains_impl(tmp, element instanceof UByte ? element._data : THROW_CCE())

  def UByteArray__containsAll_impl(this_0, elements) :
     tmp$ret$0
    l$ret$1: do :
       tmp0_all_0 = isInterface(elements, Collection) ? elements : THROW_CCE()
       tmp
      if (isInterface(tmp0_all_0, Collection)) :
        tmp = tmp0_all_0.isEmpty_29()
       else :
        :
          tmp = false


      if (tmp) :
        tmp$ret$0 = true
        break l$ret$1
       else :

       tmp0_iterator_1 = tmp0_all_0.iterator_38()
      while (tmp0_iterator_1.hasNext_37()) :
         element_2 = tmp0_iterator_1.next_41()
         tmp_0
        if (element_2 instanceof UByte) :
           tmp_1 = _UByteArray___get_storage__impl_(this_0)
           tmp0_toByte_0_4 = element_2._data
          tmp_0 = contains(tmp_1, _UByte___get_data__impl_(tmp0_toByte_0_4))
         else :
          :
            tmp_0 = false


        if (!tmp_0) :
          tmp$ret$0 = false
          break l$ret$1
         else :


      tmp$ret$0 = true

     while (false)
    return tmp$ret$0

  def UByteArray__containsAll_impl_0(this_0, elements) :
    return UByteArray__containsAll_impl(this_0._storage, elements)

  def UByteArray__isEmpty_impl(this_0) :
    return _UByteArray___get_storage__impl_(this_0).length === 0

  def UByteArray__toString_impl(this_0) :
    return '' + 'UByteArray(storage=' + toString_0(this_0) + ')'

  def UByteArray__hashCode_impl(this_0) :
    return hashCode(this_0)

  def UByteArray__equals_impl(this_0, other) :
    if (!(other instanceof UByteArray))
      return false;
    else :

     tmp0_other_with_cast = other instanceof UByteArray ? other._storage : THROW_CCE()
    if (!equals(this_0, tmp0_other_with_cast))
      return false
    return true

  def UByteArray(storage) :
    this._storage = storage

  UByteArray.prototype._get_size__18 = def () :
    return _UByteArray___get_size__impl_(this._storage)

  UByteArray.prototype.iterator_38 = def () :
    return UByteArray__iterator_impl(this._storage)

  UByteArray.prototype.contains_4 = def (element) :
    return UByteArray__contains_impl(this._storage, element)

  UByteArray.prototype.contains_32 = def (element) :
    return UByteArray__contains_impl_0(this, element)

  UByteArray.prototype.containsAll_4 = def (elements) :
    return UByteArray__containsAll_impl(this._storage, elements)

  UByteArray.prototype.containsAll_21 = def (elements) :
    return UByteArray__containsAll_impl_0(this, elements)

  UByteArray.prototype.isEmpty_29 = def () :
    return UByteArray__isEmpty_impl(this._storage)

  UByteArray.prototype.toString = def () :
    return UByteArray__toString_impl(this._storage)

  UByteArray.prototype.hashCode = def () :
    return UByteArray__hashCode_impl(this._storage)

  UByteArray.prototype.equals = def (other) :
    return UByteArray__equals_impl(this._storage, other)

  UByteArray.$metadata$ = {
    simpleName: 'UByteArray',
    kind: 'class',
    interfaces: [Collection]

  def _UInt___get_data__impl_(this_0) :
    return this_0

  def Companion_5() :
    Companion_instance_4 = this
    this._MIN_VALUE_0 = 0
    this._MAX_VALUE_0 = -1
    this._SIZE_BYTES_0 = 4
    this._SIZE_BITS_0 = 32

  Companion_5.prototype._get_MIN_VALUE__0 = def () :
    return this._MIN_VALUE_0

  Companion_5.prototype._get_MAX_VALUE__0 = def () :
    return this._MAX_VALUE_0

  Companion_5.prototype._get_SIZE_BYTES__9 = def () :
    return this._SIZE_BYTES_0

  Companion_5.prototype._get_SIZE_BITS__9 = def () :
    return this._SIZE_BITS_0

  Companion_5.$metadata$ = {
    simpleName: 'Companion',
    kind: 'object',
    interfaces: []

   Companion_instance_4
  def Companion_getInstance_4() :
    if (Companion_instance_4 == null)
      new Companion_5()
    return Companion_instance_4

  def UInt__compareTo_impl(this_0, other) :
     tmp0_compareTo_0 = _UByte___get_data__impl_(other) & 255
    return uintCompare(_UInt___get_data__impl_(this_0), _UInt___get_data__impl_(tmp0_compareTo_0))

  def UInt__compareTo_impl_0(this_0, other) :
     tmp0_compareTo_0 = _UShort___get_data__impl_(other) & 65535
    return uintCompare(_UInt___get_data__impl_(this_0), _UInt___get_data__impl_(tmp0_compareTo_0))

  def UInt__compareTo_impl_1(this_0, other) :
    return uintCompare(_UInt___get_data__impl_(this_0), _UInt___get_data__impl_(other))

  def UInt__compareTo_impl_2(this_0, other) :
     tmp = this_0._data_0
    return UInt__compareTo_impl_1(tmp, other instanceof UInt ? other._data_0 : THROW_CCE())

  def UInt__compareTo_impl_3(this_0, other) :
     tmp0_compareTo_0 = toLong(_UInt___get_data__impl_(this_0)).and(new Long(-1, 0))
    return ulongCompare(_ULong___get_data__impl_(tmp0_compareTo_0), _ULong___get_data__impl_(other))

  def UInt__plus_impl(this_0, other) :
     tmp0_plus_0 = _UByte___get_data__impl_(other) & 255
    return _UInt___get_data__impl_(this_0) + _UInt___get_data__impl_(tmp0_plus_0) | 0

  def UInt__plus_impl_0(this_0, other) :
     tmp0_plus_0 = _UShort___get_data__impl_(other) & 65535
    return _UInt___get_data__impl_(this_0) + _UInt___get_data__impl_(tmp0_plus_0) | 0

  def UInt__plus_impl_1(this_0, other) :
    return _UInt___get_data__impl_(this_0) + _UInt___get_data__impl_(other) | 0

  def UInt__plus_impl_2(this_0, other) :
     tmp0_plus_0 = toLong(_UInt___get_data__impl_(this_0)).and(new Long(-1, 0))
    return _ULong___get_data__impl_(tmp0_plus_0).plus_38(_ULong___get_data__impl_(other))

  def UInt__minus_impl(this_0, other) :
     tmp0_minus_0 = _UByte___get_data__impl_(other) & 255
    return _UInt___get_data__impl_(this_0) - _UInt___get_data__impl_(tmp0_minus_0) | 0

  def UInt__minus_impl_0(this_0, other) :
     tmp0_minus_0 = _UShort___get_data__impl_(other) & 65535
    return _UInt___get_data__impl_(this_0) - _UInt___get_data__impl_(tmp0_minus_0) | 0

  def UInt__minus_impl_1(this_0, other) :
    return _UInt___get_data__impl_(this_0) - _UInt___get_data__impl_(other) | 0

  def UInt__minus_impl_2(this_0, other) :
     tmp0_minus_0 = toLong(_UInt___get_data__impl_(this_0)).and(new Long(-1, 0))
    return _ULong___get_data__impl_(tmp0_minus_0).minus_34(_ULong___get_data__impl_(other))

  def UInt__times_impl(this_0, other) :
     tmp0_times_0 = _UByte___get_data__impl_(other) & 255
    return imul(_UInt___get_data__impl_(this_0), _UInt___get_data__impl_(tmp0_times_0))

  def UInt__times_impl_0(this_0, other) :
     tmp0_times_0 = _UShort___get_data__impl_(other) & 65535
    return imul(_UInt___get_data__impl_(this_0), _UInt___get_data__impl_(tmp0_times_0))

  def UInt__times_impl_1(this_0, other) :
    return imul(_UInt___get_data__impl_(this_0), _UInt___get_data__impl_(other))

  def UInt__times_impl_2(this_0, other) :
     tmp0_times_0 = toLong(_UInt___get_data__impl_(this_0)).and(new Long(-1, 0))
    return _ULong___get_data__impl_(tmp0_times_0).times_32(_ULong___get_data__impl_(other))

  def UInt__div_impl(this_0, other) :
     tmp0_div_0 = _UByte___get_data__impl_(other) & 255
    return uintDivide(this_0, tmp0_div_0)

  def UInt__div_impl_0(this_0, other) :
     tmp0_div_0 = _UShort___get_data__impl_(other) & 65535
    return uintDivide(this_0, tmp0_div_0)

  def UInt__div_impl_1(this_0, other) :
    return uintDivide(this_0, other)

  def UInt__div_impl_2(this_0, other) :
     tmp0_div_0 = toLong(_UInt___get_data__impl_(this_0)).and(new Long(-1, 0))
    return ulongDivide(tmp0_div_0, other)

  def UInt__rem_impl(this_0, other) :
     tmp0_rem_0 = _UByte___get_data__impl_(other) & 255
    return uintRemainder(this_0, tmp0_rem_0)

  def UInt__rem_impl_0(this_0, other) :
     tmp0_rem_0 = _UShort___get_data__impl_(other) & 65535
    return uintRemainder(this_0, tmp0_rem_0)

  def UInt__rem_impl_1(this_0, other) :
    return uintRemainder(this_0, other)

  def UInt__rem_impl_2(this_0, other) :
     tmp0_rem_0 = toLong(_UInt___get_data__impl_(this_0)).and(new Long(-1, 0))
    return ulongRemainder(tmp0_rem_0, other)

  def UInt__inc_impl(this_0) :
    return _UInt___get_data__impl_(this_0) + 1 | 0

  def UInt__dec_impl(this_0) :
    return _UInt___get_data__impl_(this_0) - 1 | 0

  def UInt__rangeTo_impl(this_0, other) :
    return new UIntRange(this_0, other)

  def UInt__shl_impl(this_0, bitCount) :
    return _UInt___get_data__impl_(this_0) << bitCount

  def UInt__shr_impl(this_0, bitCount) :
    return _UInt___get_data__impl_(this_0) >>> bitCount

  def UInt__and_impl(this_0, other) :
    return _UInt___get_data__impl_(this_0) & _UInt___get_data__impl_(other)

  def UInt__or_impl(this_0, other) :
    return _UInt___get_data__impl_(this_0) | _UInt___get_data__impl_(other)

  def UInt__xor_impl(this_0, other) :
    return _UInt___get_data__impl_(this_0) ^ _UInt___get_data__impl_(other)

  def UInt__inv_impl(this_0) :
    return ~_UInt___get_data__impl_(this_0)

  def UInt__toByte_impl(this_0) :
    return toByte(_UInt___get_data__impl_(this_0))

  def UInt__toShort_impl(this_0) :
    return toShort(_UInt___get_data__impl_(this_0))

  def UInt__toInt_impl(this_0) :
    return _UInt___get_data__impl_(this_0)

  def UInt__toLong_impl(this_0) :
    return toLong(_UInt___get_data__impl_(this_0)).and(new Long(-1, 0))

  def UInt__toUByte_impl(this_0) :
     tmp0_toUByte_0 = _UInt___get_data__impl_(this_0)
    return toByte(tmp0_toUByte_0)

  def UInt__toUShort_impl(this_0) :
     tmp0_toUShort_0 = _UInt___get_data__impl_(this_0)
    return toShort(tmp0_toUShort_0)

  def UInt__toUInt_impl(this_0) :
    return this_0

  def UInt__toULong_impl(this_0) :
    return toLong(_UInt___get_data__impl_(this_0)).and(new Long(-1, 0))

  def UInt__toFloat_impl(this_0) :
    return uintToDouble(_UInt___get_data__impl_(this_0))

  def UInt__toDouble_impl(this_0) :
    return uintToDouble(_UInt___get_data__impl_(this_0))

  def UInt__toString_impl(this_0) :
    return toLong(_UInt___get_data__impl_(this_0)).and(new Long(-1, 0)).toString()

  def UInt__hashCode_impl(this_0) :
    return this_0

  def UInt__equals_impl(this_0, other) :
    if (!(other instanceof UInt))
      return false;
    else :

     tmp0_other_with_cast = other instanceof UInt ? other._data_0 : THROW_CCE()
    if (!(this_0 === tmp0_other_with_cast))
      return false
    return true

  def UInt(data) :
    Companion_getInstance_4()
    this._data_0 = data

  UInt.prototype.compareTo_7 = def (other) :
    return UInt__compareTo_impl_1(this._data_0, other)

  UInt.prototype.compareTo_25 = def (other) :
    return UInt__compareTo_impl_2(this, other)

  UInt.prototype.toString = def () :
    return UInt__toString_impl(this._data_0)

  UInt.prototype.hashCode = def () :
    return UInt__hashCode_impl(this._data_0)

  UInt.prototype.equals = def (other) :
    return UInt__equals_impl(this._data_0, other)

  UInt.$metadata$ = {
    simpleName: 'UInt',
    kind: 'class',
    interfaces: [Comparable]

  def toUInt(_this_) :
    return _this_.toInt_6()

  def toUInt_0(_this_) :
    return _this_

  def toUInt_1(_this_) :
    return _this_

  def toUInt_2(_this_) :
    return doubleToUInt(_this_)

  def toUInt_3(_this_) :
    return doubleToUInt(_this_)

  def toUInt_4(_this_) :
    return _this_

  def _get_array__0($this) :
    return $this._array_0

  def _set_index__0($this, _set___) :
    $this._index_1 = _set___

  def _get_index__0($this) :
    return $this._index_1

  def _UIntArray___get_storage__impl_(this_0) :
    return this_0

  def _UIntArray___init__impl_(size_0) :
     tmp = new Int32Array(size_0)
    return tmp

  def UIntArray__get_impl(this_0, index) :
     tmp0_toUInt_0 = _UIntArray___get_storage__impl_(this_0)[index]
    return tmp0_toUInt_0

  def UIntArray__set_impl(this_0, index, value) :
     tmp = _UIntArray___get_storage__impl_(this_0)
    tmp[index] = _UInt___get_data__impl_(value)

  def _UIntArray___get_size__impl_(this_0) :
    return _UIntArray___get_storage__impl_(this_0).length

  def UIntArray__iterator_impl(this_0) :
    return new Iterator_0(_UIntArray___get_storage__impl_(this_0))

  def Iterator_0(array) :
    UIntIterator.call(this)
    this._array_0 = array
    this._index_1 = 0

  Iterator_0.prototype.hasNext_37 = def () :
    return this._index_1 < this._array_0.length

  Iterator_0.prototype.nextUInt_1 = def () :
     tmp
    if (this._index_1 < this._array_0.length) :
       tmp0_this = this
       tmp1 = tmp0_this._index_1
      tmp0_this._index_1 = tmp1 + 1 | 0
       tmp0_toUInt_0 = this._array_0[tmp1]
      tmp = tmp0_toUInt_0
     else :
      throw NoSuchElementException_init_$Create$_0(this._index_1.toString())

    return tmp

  Iterator_0.$metadata$ = {
    simpleName: 'Iterator',
    kind: 'class',
    interfaces: []

  def UIntArray__contains_impl(this_0, element) :
     tmp = isObject(new UInt(element)) ? new UInt(element) : THROW_CCE()
    if (!(tmp instanceof UInt))
      return false;
    else :

     tmp_0 = _UIntArray___get_storage__impl_(this_0)
    return contains_1(tmp_0, _UInt___get_data__impl_(element))

  def UIntArray__contains_impl_0(this_0, element) :
    if (!(element instanceof UInt))
      return false;
    else :

     tmp = this_0._storage_0
    return UIntArray__contains_impl(tmp, element instanceof UInt ? element._data_0 : THROW_CCE())

  def UIntArray__containsAll_impl(this_0, elements) :
     tmp$ret$0
    l$ret$1: do :
       tmp0_all_0 = isInterface(elements, Collection) ? elements : THROW_CCE()
       tmp
      if (isInterface(tmp0_all_0, Collection)) :
        tmp = tmp0_all_0.isEmpty_29()
       else :
        :
          tmp = false


      if (tmp) :
        tmp$ret$0 = true
        break l$ret$1
       else :

       tmp0_iterator_1 = tmp0_all_0.iterator_38()
      while (tmp0_iterator_1.hasNext_37()) :
         element_2 = tmp0_iterator_1.next_41()
         tmp_0
        if (element_2 instanceof UInt) :
           tmp_1 = _UIntArray___get_storage__impl_(this_0)
           tmp0_toInt_0_4 = element_2._data_0
          tmp_0 = contains_1(tmp_1, _UInt___get_data__impl_(tmp0_toInt_0_4))
         else :
          :
            tmp_0 = false


        if (!tmp_0) :
          tmp$ret$0 = false
          break l$ret$1
         else :


      tmp$ret$0 = true

     while (false)
    return tmp$ret$0

  def UIntArray__containsAll_impl_0(this_0, elements) :
    return UIntArray__containsAll_impl(this_0._storage_0, elements)

  def UIntArray__isEmpty_impl(this_0) :
    return _UIntArray___get_storage__impl_(this_0).length === 0

  def UIntArray__toString_impl(this_0) :
    return '' + 'UIntArray(storage=' + toString_0(this_0) + ')'

  def UIntArray__hashCode_impl(this_0) :
    return hashCode(this_0)

  def UIntArray__equals_impl(this_0, other) :
    if (!(other instanceof UIntArray))
      return false;
    else :

     tmp0_other_with_cast = other instanceof UIntArray ? other._storage_0 : THROW_CCE()
    if (!equals(this_0, tmp0_other_with_cast))
      return false
    return true

  def UIntArray(storage) :
    this._storage_0 = storage

  UIntArray.prototype._get_size__18 = def () :
    return _UIntArray___get_size__impl_(this._storage_0)

  UIntArray.prototype.iterator_38 = def () :
    return UIntArray__iterator_impl(this._storage_0)

  UIntArray.prototype.contains_8 = def (element) :
    return UIntArray__contains_impl(this._storage_0, element)

  UIntArray.prototype.contains_32 = def (element) :
    return UIntArray__contains_impl_0(this, element)

  UIntArray.prototype.containsAll_6 = def (elements) :
    return UIntArray__containsAll_impl(this._storage_0, elements)

  UIntArray.prototype.containsAll_21 = def (elements) :
    return UIntArray__containsAll_impl_0(this, elements)

  UIntArray.prototype.isEmpty_29 = def () :
    return UIntArray__isEmpty_impl(this._storage_0)

  UIntArray.prototype.toString = def () :
    return UIntArray__toString_impl(this._storage_0)

  UIntArray.prototype.hashCode = def () :
    return UIntArray__hashCode_impl(this._storage_0)

  UIntArray.prototype.equals = def (other) :
    return UIntArray__equals_impl(this._storage_0, other)

  UIntArray.$metadata$ = {
    simpleName: 'UIntArray',
    kind: 'class',
    interfaces: [Collection]

  def Companion_6() :
    Companion_instance_5 = this
    this._EMPTY = new UIntRange(-1, 0)

  Companion_6.prototype._get_EMPTY__3 = def () :
    return this._EMPTY

  Companion_6.$metadata$ = {
    simpleName: 'Companion',
    kind: 'object',
    interfaces: []

   Companion_instance_5
  def Companion_getInstance_5() :
    if (Companion_instance_5 == null)
      new Companion_6()
    return Companion_instance_5

  def UIntRange(start, endInclusive) :
    Companion_getInstance_5()
    UIntProgression.call(this, start, endInclusive, 1)

  UIntRange.prototype._get_start_ = def () :
    return this._get_first__0()

  UIntRange.prototype._get_start__6 = def () :
    return new UInt(this._get_start_())

  UIntRange.prototype._get_endInclusive_ = def () :
    return this._get_last__0()

  UIntRange.prototype._get_endInclusive__6 = def () :
    return new UInt(this._get_endInclusive_())

  UIntRange.prototype.contains_8 = def (value) :
     tmp
     tmp0_compareTo_0 = this._get_first__0()
    if (uintCompare(_UInt___get_data__impl_(tmp0_compareTo_0), _UInt___get_data__impl_(value)) <= 0) :
       tmp1_compareTo_0 = this._get_last__0()
      tmp = uintCompare(_UInt___get_data__impl_(value), _UInt___get_data__impl_(tmp1_compareTo_0)) <= 0
     else :
      :
        tmp = false


    return tmp

  UIntRange.prototype.contains_22 = def (value) :
    return this.contains_8(value instanceof UInt ? value._data_0 : THROW_CCE())

  UIntRange.prototype.isEmpty_29 = def () :
     tmp0_compareTo_0 = this._get_first__0()
     tmp1_compareTo_0 = this._get_last__0()
    return uintCompare(_UInt___get_data__impl_(tmp0_compareTo_0), _UInt___get_data__impl_(tmp1_compareTo_0)) > 0

  UIntRange.prototype.equals = def (other) :
     tmp
    if (other instanceof UIntRange) :
      tmp = (this.isEmpty_29() ? other.isEmpty_29() : false) ? true : equals(new UInt(this._get_first__0()), new UInt(other._get_first__0())) ? equals(new UInt(this._get_last__0()), new UInt(other._get_last__0())) : false
     else :
      :
        tmp = false


    return tmp

  UIntRange.prototype.hashCode = def () :
     tmp
    if (this.isEmpty_29()) :
      tmp = -1
     else :
       tmp0_toInt_0 = this._get_first__0()
       tmp_0 = imul(31, _UInt___get_data__impl_(tmp0_toInt_0))
       tmp1_toInt_0 = this._get_last__0()
      tmp = tmp_0 + _UInt___get_data__impl_(tmp1_toInt_0) | 0

    return tmp

  UIntRange.prototype.toString = def () :
    return '' + new UInt(this._get_first__0()) + '..' + new UInt(this._get_last__0())

  UIntRange.$metadata$ = {
    simpleName: 'UIntRange',
    kind: 'class',
    interfaces: [ClosedRange]

  def Companion_7() :
    Companion_instance_6 = this

  Companion_7.prototype.fromClosedRange = def (rangeStart, rangeEnd, step) :
    return new UIntProgression(rangeStart, rangeEnd, step)

  Companion_7.$metadata$ = {
    simpleName: 'Companion',
    kind: 'object',
    interfaces: []

   Companion_instance_6
  def Companion_getInstance_6() :
    if (Companion_instance_6 == null)
      new Companion_7()
    return Companion_instance_6

  def UIntProgression(start, endInclusive, step) :
    Companion_getInstance_6()
    if (step === 0)
      throw IllegalArgumentException_init_$Create$_0('Step must be non-zero.')
    if (step === IntCompanionObject_getInstance()._MIN_VALUE_5)
      throw IllegalArgumentException_init_$Create$_0('Step must be greater than Int.MIN_VALUE to avoid overflow on negation.')
    this._first = start
    this._last = getProgressionLastElement(start, endInclusive, step)
    this._step = step

  UIntProgression.prototype._get_first__0 = def () :
    return this._first

  UIntProgression.prototype._get_last__0 = def () :
    return this._last

  UIntProgression.prototype._get_step__11 = def () :
    return this._step

  UIntProgression.prototype.iterator_38 = def () :
    return new UIntProgressionIterator(this._first, this._last, this._step)

  UIntProgression.prototype.isEmpty_29 = def () :
     tmp
    if (this._step > 0) :
       tmp0_compareTo_0 = this._first
       tmp1_compareTo_0 = this._last
      tmp = uintCompare(_UInt___get_data__impl_(tmp0_compareTo_0), _UInt___get_data__impl_(tmp1_compareTo_0)) > 0
     else :
       tmp2_compareTo_0 = this._first
       tmp3_compareTo_0 = this._last
      tmp = uintCompare(_UInt___get_data__impl_(tmp2_compareTo_0), _UInt___get_data__impl_(tmp3_compareTo_0)) < 0

    return tmp

  UIntProgression.prototype.equals = def (other) :
     tmp
    if (other instanceof UIntProgression) :
      tmp = (this.isEmpty_29() ? other.isEmpty_29() : false) ? true : (equals(new UInt(this._first), new UInt(other._first)) ? equals(new UInt(this._last), new UInt(other._last)) : false) ? this._step === other._step : false
     else :
      :
        tmp = false


    return tmp

  UIntProgression.prototype.hashCode = def () :
     tmp
    if (this.isEmpty_29()) :
      tmp = -1
     else :
       tmp0_toInt_0 = this._first
       tmp_0 = imul(31, _UInt___get_data__impl_(tmp0_toInt_0))
       tmp1_toInt_0 = this._last
      tmp = imul(31, tmp_0 + _UInt___get_data__impl_(tmp1_toInt_0) | 0) + this._step | 0

    return tmp

  UIntProgression.prototype.toString = def () :
    return this._step > 0 ? '' + new UInt(this._first) + '..' + new UInt(this._last) + ' step ' + this._step : '' + new UInt(this._first) + ' downTo ' + new UInt(this._last) + ' step ' + (-this._step | 0)

  UIntProgression.$metadata$ = {
    simpleName: 'UIntProgression',
    kind: 'class',
    interfaces: [Iterable]

  def _get_finalElement_($this) :
    return $this._finalElement

  def _set_hasNext_($this, _set___) :
    $this._hasNext = _set___

  def _get_hasNext_($this) :
    return $this._hasNext

  def _get_step_($this) :
    return $this._step_0

  def _set_next_($this, _set___) :
    $this._next = _set___

  def _get_next_($this) :
    return $this._next

  def UIntProgressionIterator(first, last, step) :
    UIntIterator.call(this)
    this._finalElement = last
     tmp = this
     tmp_0
    if (step > 0) :
      tmp_0 = uintCompare(_UInt___get_data__impl_(first), _UInt___get_data__impl_(last)) <= 0
     else :
      tmp_0 = uintCompare(_UInt___get_data__impl_(first), _UInt___get_data__impl_(last)) >= 0

    tmp._hasNext = tmp_0
     tmp_1 = this
    tmp_1._step_0 = step
    this._next = this._hasNext ? first : this._finalElement

  UIntProgressionIterator.prototype.hasNext_37 = def () :
    return this._hasNext

  UIntProgressionIterator.prototype.nextUInt_1 = def () :
     value = this._next
    if (equals(new UInt(value), new UInt(this._finalElement))) :
      if (!this._hasNext)
        throw NoSuchElementException_init_$Create$()
      this._hasNext = false
     else :
       tmp0_this = this
       tmp = tmp0_this
       tmp0_plus_0 = tmp0_this._next
       tmp1_plus_0 = this._step_0
      tmp._next = _UInt___get_data__impl_(tmp0_plus_0) + _UInt___get_data__impl_(tmp1_plus_0) | 0

    return value

  UIntProgressionIterator.$metadata$ = {
    simpleName: 'UIntProgressionIterator',
    kind: 'class',
    interfaces: []

  def UIntIterator() :

  UIntIterator.prototype.next_5 = def () :
    return this.nextUInt_1()

  UIntIterator.prototype.next_41 = def () :
    return new UInt(this.next_5())

  UIntIterator.$metadata$ = {
    simpleName: 'UIntIterator',
    kind: 'class',
    interfaces: [Iterator_3]

  def ULongIterator() :

  ULongIterator.prototype.next_14 = def () :
    return this.nextULong_1()

  ULongIterator.prototype.next_41 = def () :
    return new ULong(this.next_14())

  ULongIterator.$metadata$ = {
    simpleName: 'ULongIterator',
    kind: 'class',
    interfaces: [Iterator_3]

  def UByteIterator() :

  UByteIterator.prototype.next_9 = def () :
    return this.nextUByte_0()

  UByteIterator.prototype.next_41 = def () :
    return new UByte(this.next_9())

  UByteIterator.$metadata$ = {
    simpleName: 'UByteIterator',
    kind: 'class',
    interfaces: [Iterator_3]

  def UShortIterator() :

  UShortIterator.prototype.next_15 = def () :
    return this.nextUShort_0()

  UShortIterator.prototype.next_41 = def () :
    return new UShort(this.next_15())

  UShortIterator.$metadata$ = {
    simpleName: 'UShortIterator',
    kind: 'class',
    interfaces: [Iterator_3]

  def _ULong___get_data__impl_(this_0) :
    return this_0

  def Companion_8() :
    Companion_instance_7 = this
    this._MIN_VALUE_1 = new Long(0, 0)
    this._MAX_VALUE_1 = new Long(-1, -1)
    this._SIZE_BYTES_1 = 8
    this._SIZE_BITS_1 = 64

  Companion_8.prototype._get_MIN_VALUE__1 = def () :
    return this._MIN_VALUE_1

  Companion_8.prototype._get_MAX_VALUE__1 = def () :
    return this._MAX_VALUE_1

  Companion_8.prototype._get_SIZE_BYTES__9 = def () :
    return this._SIZE_BYTES_1

  Companion_8.prototype._get_SIZE_BITS__9 = def () :
    return this._SIZE_BITS_1

  Companion_8.$metadata$ = {
    simpleName: 'Companion',
    kind: 'object',
    interfaces: []

   Companion_instance_7
  def Companion_getInstance_7() :
    if (Companion_instance_7 == null)
      new Companion_8()
    return Companion_instance_7

  def ULong__compareTo_impl(this_0, other) :
     tmp0_compareTo_0 = toLong(_UByte___get_data__impl_(other)).and(new Long(255, 0))
    return ulongCompare(_ULong___get_data__impl_(this_0), _ULong___get_data__impl_(tmp0_compareTo_0))

  def ULong__compareTo_impl_0(this_0, other) :
     tmp0_compareTo_0 = toLong(_UShort___get_data__impl_(other)).and(new Long(65535, 0))
    return ulongCompare(_ULong___get_data__impl_(this_0), _ULong___get_data__impl_(tmp0_compareTo_0))

  def ULong__compareTo_impl_1(this_0, other) :
     tmp0_compareTo_0 = toLong(_UInt___get_data__impl_(other)).and(new Long(-1, 0))
    return ulongCompare(_ULong___get_data__impl_(this_0), _ULong___get_data__impl_(tmp0_compareTo_0))

  def ULong__compareTo_impl_2(this_0, other) :
    return ulongCompare(_ULong___get_data__impl_(this_0), _ULong___get_data__impl_(other))

  def ULong__compareTo_impl_3(this_0, other) :
     tmp = this_0._data_1
    return ULong__compareTo_impl_2(tmp, other instanceof ULong ? other._data_1 : THROW_CCE())

  def ULong__plus_impl(this_0, other) :
     tmp0_plus_0 = toLong(_UByte___get_data__impl_(other)).and(new Long(255, 0))
    return _ULong___get_data__impl_(this_0).plus_38(_ULong___get_data__impl_(tmp0_plus_0))

  def ULong__plus_impl_0(this_0, other) :
     tmp0_plus_0 = toLong(_UShort___get_data__impl_(other)).and(new Long(65535, 0))
    return _ULong___get_data__impl_(this_0).plus_38(_ULong___get_data__impl_(tmp0_plus_0))

  def ULong__plus_impl_1(this_0, other) :
     tmp0_plus_0 = toLong(_UInt___get_data__impl_(other)).and(new Long(-1, 0))
    return _ULong___get_data__impl_(this_0).plus_38(_ULong___get_data__impl_(tmp0_plus_0))

  def ULong__plus_impl_2(this_0, other) :
    return _ULong___get_data__impl_(this_0).plus_38(_ULong___get_data__impl_(other))

  def ULong__minus_impl(this_0, other) :
     tmp0_minus_0 = toLong(_UByte___get_data__impl_(other)).and(new Long(255, 0))
    return _ULong___get_data__impl_(this_0).minus_34(_ULong___get_data__impl_(tmp0_minus_0))

  def ULong__minus_impl_0(this_0, other) :
     tmp0_minus_0 = toLong(_UShort___get_data__impl_(other)).and(new Long(65535, 0))
    return _ULong___get_data__impl_(this_0).minus_34(_ULong___get_data__impl_(tmp0_minus_0))

  def ULong__minus_impl_1(this_0, other) :
     tmp0_minus_0 = toLong(_UInt___get_data__impl_(other)).and(new Long(-1, 0))
    return _ULong___get_data__impl_(this_0).minus_34(_ULong___get_data__impl_(tmp0_minus_0))

  def ULong__minus_impl_2(this_0, other) :
    return _ULong___get_data__impl_(this_0).minus_34(_ULong___get_data__impl_(other))

  def ULong__times_impl(this_0, other) :
     tmp0_times_0 = toLong(_UByte___get_data__impl_(other)).and(new Long(255, 0))
    return _ULong___get_data__impl_(this_0).times_32(_ULong___get_data__impl_(tmp0_times_0))

  def ULong__times_impl_0(this_0, other) :
     tmp0_times_0 = toLong(_UShort___get_data__impl_(other)).and(new Long(65535, 0))
    return _ULong___get_data__impl_(this_0).times_32(_ULong___get_data__impl_(tmp0_times_0))

  def ULong__times_impl_1(this_0, other) :
     tmp0_times_0 = toLong(_UInt___get_data__impl_(other)).and(new Long(-1, 0))
    return _ULong___get_data__impl_(this_0).times_32(_ULong___get_data__impl_(tmp0_times_0))

  def ULong__times_impl_2(this_0, other) :
    return _ULong___get_data__impl_(this_0).times_32(_ULong___get_data__impl_(other))

  def ULong__div_impl(this_0, other) :
     tmp0_div_0 = toLong(_UByte___get_data__impl_(other)).and(new Long(255, 0))
    return ulongDivide(this_0, tmp0_div_0)

  def ULong__div_impl_0(this_0, other) :
     tmp0_div_0 = toLong(_UShort___get_data__impl_(other)).and(new Long(65535, 0))
    return ulongDivide(this_0, tmp0_div_0)

  def ULong__div_impl_1(this_0, other) :
     tmp0_div_0 = toLong(_UInt___get_data__impl_(other)).and(new Long(-1, 0))
    return ulongDivide(this_0, tmp0_div_0)

  def ULong__div_impl_2(this_0, other) :
    return ulongDivide(this_0, other)

  def ULong__rem_impl(this_0, other) :
     tmp0_rem_0 = toLong(_UByte___get_data__impl_(other)).and(new Long(255, 0))
    return ulongRemainder(this_0, tmp0_rem_0)

  def ULong__rem_impl_0(this_0, other) :
     tmp0_rem_0 = toLong(_UShort___get_data__impl_(other)).and(new Long(65535, 0))
    return ulongRemainder(this_0, tmp0_rem_0)

  def ULong__rem_impl_1(this_0, other) :
     tmp0_rem_0 = toLong(_UInt___get_data__impl_(other)).and(new Long(-1, 0))
    return ulongRemainder(this_0, tmp0_rem_0)

  def ULong__rem_impl_2(this_0, other) :
    return ulongRemainder(this_0, other)

  def ULong__inc_impl(this_0) :
    return _ULong___get_data__impl_(this_0).inc_5()

  def ULong__dec_impl(this_0) :
    return _ULong___get_data__impl_(this_0).dec_5()

  def ULong__rangeTo_impl(this_0, other) :
    return new ULongRange(this_0, other)

  def ULong__shl_impl(this_0, bitCount) :
    return _ULong___get_data__impl_(this_0).shl_0(bitCount)

  def ULong__shr_impl(this_0, bitCount) :
    return _ULong___get_data__impl_(this_0).ushr_0(bitCount)

  def ULong__and_impl(this_0, other) :
    return _ULong___get_data__impl_(this_0).and(_ULong___get_data__impl_(other))

  def ULong__or_impl(this_0, other) :
    return _ULong___get_data__impl_(this_0).or(_ULong___get_data__impl_(other))

  def ULong__xor_impl(this_0, other) :
    return _ULong___get_data__impl_(this_0).xor(_ULong___get_data__impl_(other))

  def ULong__inv_impl(this_0) :
    return _ULong___get_data__impl_(this_0).inv_0()

  def ULong__toByte_impl(this_0) :
    return _ULong___get_data__impl_(this_0).toByte_6()

  def ULong__toShort_impl(this_0) :
    return _ULong___get_data__impl_(this_0).toShort_6()

  def ULong__toInt_impl(this_0) :
    return _ULong___get_data__impl_(this_0).toInt_6()

  def ULong__toLong_impl(this_0) :
    return _ULong___get_data__impl_(this_0)

  def ULong__toUByte_impl(this_0) :
     tmp0_toUByte_0 = _ULong___get_data__impl_(this_0)
    return tmp0_toUByte_0.toByte_6()

  def ULong__toUShort_impl(this_0) :
     tmp0_toUShort_0 = _ULong___get_data__impl_(this_0)
    return tmp0_toUShort_0.toShort_6()

  def ULong__toUInt_impl(this_0) :
     tmp0_toUInt_0 = _ULong___get_data__impl_(this_0)
    return tmp0_toUInt_0.toInt_6()

  def ULong__toULong_impl(this_0) :
    return this_0

  def ULong__toFloat_impl(this_0) :
    return ulongToDouble(_ULong___get_data__impl_(this_0))

  def ULong__toDouble_impl(this_0) :
    return ulongToDouble(_ULong___get_data__impl_(this_0))

  def ULong__toString_impl(this_0) :
    return ulongToString(_ULong___get_data__impl_(this_0))

  def ULong__hashCode_impl(this_0) :
    return this_0.hashCode()

  def ULong__equals_impl(this_0, other) :
    if (!(other instanceof ULong))
      return false;
    else :

     tmp0_other_with_cast = other instanceof ULong ? other._data_1 : THROW_CCE()
    if (!this_0.equals(tmp0_other_with_cast))
      return false
    return true

  def ULong(data) :
    Companion_getInstance_7()
    this._data_1 = data

  ULong.prototype.compareTo_9 = def (other) :
    return ULong__compareTo_impl_2(this._data_1, other)

  ULong.prototype.compareTo_25 = def (other) :
    return ULong__compareTo_impl_3(this, other)

  ULong.prototype.toString = def () :
    return ULong__toString_impl(this._data_1)

  ULong.prototype.hashCode = def () :
    return ULong__hashCode_impl(this._data_1)

  ULong.prototype.equals = def (other) :
    return ULong__equals_impl(this._data_1, other)

  ULong.$metadata$ = {
    simpleName: 'ULong',
    kind: 'class',
    interfaces: [Comparable]

  def toULong(_this_) :
    return _this_

  def toULong_0(_this_) :
    return toLong(_this_)

  def toULong_1(_this_) :
    return doubleToULong(_this_)

  def toULong_2(_this_) :
    return doubleToULong(_this_)

  def toULong_3(_this_) :
    return toLong(_this_)

  def toULong_4(_this_) :
    return toLong(_this_)

  def _get_array__1($this) :
    return $this._array_1

  def _set_index__1($this, _set___) :
    $this._index_2 = _set___

  def _get_index__1($this) :
    return $this._index_2

  def _ULongArray___get_storage__impl_(this_0) :
    return this_0

  def _ULongArray___init__impl_(size_0) :
     tmp = longArray(size_0)
    return tmp

  def ULongArray__get_impl(this_0, index) :
     tmp0_toULong_0 = _ULongArray___get_storage__impl_(this_0)[index]
    return tmp0_toULong_0

  def ULongArray__set_impl(this_0, index, value) :
     tmp = _ULongArray___get_storage__impl_(this_0)
    tmp[index] = _ULong___get_data__impl_(value)

  def _ULongArray___get_size__impl_(this_0) :
    return _ULongArray___get_storage__impl_(this_0).length

  def ULongArray__iterator_impl(this_0) :
    return new Iterator_1(_ULongArray___get_storage__impl_(this_0))

  def Iterator_1(array) :
    ULongIterator.call(this)
    this._array_1 = array
    this._index_2 = 0

  Iterator_1.prototype.hasNext_37 = def () :
    return this._index_2 < this._array_1.length

  Iterator_1.prototype.nextULong_1 = def () :
     tmp
    if (this._index_2 < this._array_1.length) :
       tmp0_this = this
       tmp1 = tmp0_this._index_2
      tmp0_this._index_2 = tmp1 + 1 | 0
       tmp0_toULong_0 = this._array_1[tmp1]
      tmp = tmp0_toULong_0
     else :
      throw NoSuchElementException_init_$Create$_0(this._index_2.toString())

    return tmp

  Iterator_1.$metadata$ = {
    simpleName: 'Iterator',
    kind: 'class',
    interfaces: []

  def ULongArray__contains_impl(this_0, element) :
     tmp = isObject(new ULong(element)) ? new ULong(element) : THROW_CCE()
    if (!(tmp instanceof ULong))
      return false;
    else :

     tmp_0 = _ULongArray___get_storage__impl_(this_0)
    return contains_2(tmp_0, _ULong___get_data__impl_(element))

  def ULongArray__contains_impl_0(this_0, element) :
    if (!(element instanceof ULong))
      return false;
    else :

     tmp = this_0._storage_1
    return ULongArray__contains_impl(tmp, element instanceof ULong ? element._data_1 : THROW_CCE())

  def ULongArray__containsAll_impl(this_0, elements) :
     tmp$ret$0
    l$ret$1: do :
       tmp0_all_0 = isInterface(elements, Collection) ? elements : THROW_CCE()
       tmp
      if (isInterface(tmp0_all_0, Collection)) :
        tmp = tmp0_all_0.isEmpty_29()
       else :
        :
          tmp = false


      if (tmp) :
        tmp$ret$0 = true
        break l$ret$1
       else :

       tmp0_iterator_1 = tmp0_all_0.iterator_38()
      while (tmp0_iterator_1.hasNext_37()) :
         element_2 = tmp0_iterator_1.next_41()
         tmp_0
        if (element_2 instanceof ULong) :
           tmp_1 = _ULongArray___get_storage__impl_(this_0)
           tmp0_toLong_0_4 = element_2._data_1
          tmp_0 = contains_2(tmp_1, _ULong___get_data__impl_(tmp0_toLong_0_4))
         else :
          :
            tmp_0 = false


        if (!tmp_0) :
          tmp$ret$0 = false
          break l$ret$1
         else :


      tmp$ret$0 = true

     while (false)
    return tmp$ret$0

  def ULongArray__containsAll_impl_0(this_0, elements) :
    return ULongArray__containsAll_impl(this_0._storage_1, elements)

  def ULongArray__isEmpty_impl(this_0) :
    return _ULongArray___get_storage__impl_(this_0).length === 0

  def ULongArray__toString_impl(this_0) :
    return '' + 'ULongArray(storage=' + toString_0(this_0) + ')'

  def ULongArray__hashCode_impl(this_0) :
    return hashCode(this_0)

  def ULongArray__equals_impl(this_0, other) :
    if (!(other instanceof ULongArray))
      return false;
    else :

     tmp0_other_with_cast = other instanceof ULongArray ? other._storage_1 : THROW_CCE()
    if (!equals(this_0, tmp0_other_with_cast))
      return false
    return true

  def ULongArray(storage) :
    this._storage_1 = storage

  ULongArray.prototype._get_size__18 = def () :
    return _ULongArray___get_size__impl_(this._storage_1)

  ULongArray.prototype.iterator_38 = def () :
    return ULongArray__iterator_impl(this._storage_1)

  ULongArray.prototype.contains_12 = def (element) :
    return ULongArray__contains_impl(this._storage_1, element)

  ULongArray.prototype.contains_32 = def (element) :
    return ULongArray__contains_impl_0(this, element)

  ULongArray.prototype.containsAll_8 = def (elements) :
    return ULongArray__containsAll_impl(this._storage_1, elements)

  ULongArray.prototype.containsAll_21 = def (elements) :
    return ULongArray__containsAll_impl_0(this, elements)

  ULongArray.prototype.isEmpty_29 = def () :
    return ULongArray__isEmpty_impl(this._storage_1)

  ULongArray.prototype.toString = def () :
    return ULongArray__toString_impl(this._storage_1)

  ULongArray.prototype.hashCode = def () :
    return ULongArray__hashCode_impl(this._storage_1)

  ULongArray.prototype.equals = def (other) :
    return ULongArray__equals_impl(this._storage_1, other)

  ULongArray.$metadata$ = {
    simpleName: 'ULongArray',
    kind: 'class',
    interfaces: [Collection]

  def Companion_9() :
    Companion_instance_8 = this
    this._EMPTY_0 = new ULongRange(new Long(-1, -1), new Long(0, 0))

  Companion_9.prototype._get_EMPTY__3 = def () :
    return this._EMPTY_0

  Companion_9.$metadata$ = {
    simpleName: 'Companion',
    kind: 'object',
    interfaces: []

   Companion_instance_8
  def Companion_getInstance_8() :
    if (Companion_instance_8 == null)
      new Companion_9()
    return Companion_instance_8

  def ULongRange(start, endInclusive) :
    Companion_getInstance_8()
    ULongProgression.call(this, start, endInclusive, new Long(1, 0))

  ULongRange.prototype._get_start__1 = def () :
    return this._get_first__2()

  ULongRange.prototype._get_start__6 = def () :
    return new ULong(this._get_start__1())

  ULongRange.prototype._get_endInclusive__1 = def () :
    return this._get_last__2()

  ULongRange.prototype._get_endInclusive__6 = def () :
    return new ULong(this._get_endInclusive__1())

  ULongRange.prototype.contains_12 = def (value) :
     tmp
     tmp0_compareTo_0 = this._get_first__2()
    if (ulongCompare(_ULong___get_data__impl_(tmp0_compareTo_0), _ULong___get_data__impl_(value)) <= 0) :
       tmp1_compareTo_0 = this._get_last__2()
      tmp = ulongCompare(_ULong___get_data__impl_(value), _ULong___get_data__impl_(tmp1_compareTo_0)) <= 0
     else :
      :
        tmp = false


    return tmp

  ULongRange.prototype.contains_22 = def (value) :
    return this.contains_12(value instanceof ULong ? value._data_1 : THROW_CCE())

  ULongRange.prototype.isEmpty_29 = def () :
     tmp0_compareTo_0 = this._get_first__2()
     tmp1_compareTo_0 = this._get_last__2()
    return ulongCompare(_ULong___get_data__impl_(tmp0_compareTo_0), _ULong___get_data__impl_(tmp1_compareTo_0)) > 0

  ULongRange.prototype.equals = def (other) :
     tmp
    if (other instanceof ULongRange) :
      tmp = (this.isEmpty_29() ? other.isEmpty_29() : false) ? true : equals(new ULong(this._get_first__2()), new ULong(other._get_first__2())) ? equals(new ULong(this._get_last__2()), new ULong(other._get_last__2())) : false
     else :
      :
        tmp = false


    return tmp

  ULongRange.prototype.hashCode = def () :
     tmp
    if (this.isEmpty_29()) :
      tmp = -1
     else :
       tmp2_xor_0 = this._get_first__2()
       tmp0_shr_0 = this._get_first__2()
       tmp1_shr_0 = 32
       tmp3_xor_0 = _ULong___get_data__impl_(tmp0_shr_0).ushr_0(tmp1_shr_0)
       tmp4_toInt_0 = _ULong___get_data__impl_(tmp2_xor_0).xor(_ULong___get_data__impl_(tmp3_xor_0))
       tmp_0 = imul(31, _ULong___get_data__impl_(tmp4_toInt_0).toInt_6())
       tmp7_xor_0 = this._get_last__2()
       tmp5_shr_0 = this._get_last__2()
       tmp6_shr_0 = 32
       tmp8_xor_0 = _ULong___get_data__impl_(tmp5_shr_0).ushr_0(tmp6_shr_0)
       tmp9_toInt_0 = _ULong___get_data__impl_(tmp7_xor_0).xor(_ULong___get_data__impl_(tmp8_xor_0))
      tmp = tmp_0 + _ULong___get_data__impl_(tmp9_toInt_0).toInt_6() | 0

    return tmp

  ULongRange.prototype.toString = def () :
    return '' + new ULong(this._get_first__2()) + '..' + new ULong(this._get_last__2())

  ULongRange.$metadata$ = {
    simpleName: 'ULongRange',
    kind: 'class',
    interfaces: [ClosedRange]

  def Companion_10() :
    Companion_instance_9 = this

  Companion_10.prototype.fromClosedRange_0 = def (rangeStart, rangeEnd, step) :
    return new ULongProgression(rangeStart, rangeEnd, step)

  Companion_10.$metadata$ = {
    simpleName: 'Companion',
    kind: 'object',
    interfaces: []

   Companion_instance_9
  def Companion_getInstance_9() :
    if (Companion_instance_9 == null)
      new Companion_10()
    return Companion_instance_9

  def ULongProgression(start, endInclusive, step) :
    Companion_getInstance_9()
    if (step.equals(new Long(0, 0)))
      throw IllegalArgumentException_init_$Create$_0('Step must be non-zero.')
    if (step.equals(new Long(0, -2147483648)))
      throw IllegalArgumentException_init_$Create$_0('Step must be greater than Long.MIN_VALUE to avoid overflow on negation.')
    this._first_0 = start
    this._last_0 = getProgressionLastElement_0(start, endInclusive, step)
    this._step_1 = step

  ULongProgression.prototype._get_first__2 = def () :
    return this._first_0

  ULongProgression.prototype._get_last__2 = def () :
    return this._last_0

  ULongProgression.prototype._get_step__11 = def () :
    return this._step_1

  ULongProgression.prototype.iterator_38 = def () :
    return new ULongProgressionIterator(this._first_0, this._last_0, this._step_1)

  ULongProgression.prototype.isEmpty_29 = def () :
     tmp
    if (this._step_1.compareTo_56(new Long(0, 0)) > 0) :
       tmp0_compareTo_0 = this._first_0
       tmp1_compareTo_0 = this._last_0
      tmp = ulongCompare(_ULong___get_data__impl_(tmp0_compareTo_0), _ULong___get_data__impl_(tmp1_compareTo_0)) > 0
     else :
       tmp2_compareTo_0 = this._first_0
       tmp3_compareTo_0 = this._last_0
      tmp = ulongCompare(_ULong___get_data__impl_(tmp2_compareTo_0), _ULong___get_data__impl_(tmp3_compareTo_0)) < 0

    return tmp

  ULongProgression.prototype.equals = def (other) :
     tmp
    if (other instanceof ULongProgression) :
      tmp = (this.isEmpty_29() ? other.isEmpty_29() : false) ? true : (equals(new ULong(this._first_0), new ULong(other._first_0)) ? equals(new ULong(this._last_0), new ULong(other._last_0)) : false) ? this._step_1.equals(other._step_1) : false
     else :
      :
        tmp = false


    return tmp

  ULongProgression.prototype.hashCode = def () :
     tmp
    if (this.isEmpty_29()) :
      tmp = -1
     else :
       tmp2_xor_0 = this._first_0
       tmp0_shr_0 = this._first_0
       tmp1_shr_0 = 32
       tmp3_xor_0 = _ULong___get_data__impl_(tmp0_shr_0).ushr_0(tmp1_shr_0)
       tmp4_toInt_0 = _ULong___get_data__impl_(tmp2_xor_0).xor(_ULong___get_data__impl_(tmp3_xor_0))
       tmp_0 = imul(31, _ULong___get_data__impl_(tmp4_toInt_0).toInt_6())
       tmp7_xor_0 = this._last_0
       tmp5_shr_0 = this._last_0
       tmp6_shr_0 = 32
       tmp8_xor_0 = _ULong___get_data__impl_(tmp5_shr_0).ushr_0(tmp6_shr_0)
       tmp9_toInt_0 = _ULong___get_data__impl_(tmp7_xor_0).xor(_ULong___get_data__impl_(tmp8_xor_0))
      tmp = imul(31, tmp_0 + _ULong___get_data__impl_(tmp9_toInt_0).toInt_6() | 0) + this._step_1.xor(this._step_1.ushr_0(32)).toInt_6() | 0

    return tmp

  ULongProgression.prototype.toString = def () :
    return this._step_1.compareTo_56(new Long(0, 0)) > 0 ? '' + new ULong(this._first_0) + '..' + new ULong(this._last_0) + ' step ' + this._step_1 : '' + new ULong(this._first_0) + ' downTo ' + new ULong(this._last_0) + ' step ' + this._step_1.unaryMinus_4()

  ULongProgression.$metadata$ = {
    simpleName: 'ULongProgression',
    kind: 'class',
    interfaces: [Iterable]

  def _get_finalElement__0($this) :
    return $this._finalElement_0

  def _set_hasNext__0($this, _set___) :
    $this._hasNext_0 = _set___

  def _get_hasNext__0($this) :
    return $this._hasNext_0

  def _get_step__0($this) :
    return $this._step_2

  def _set_next__0($this, _set___) :
    $this._next_0 = _set___

  def _get_next__0($this) :
    return $this._next_0

  def ULongProgressionIterator(first, last, step) :
    ULongIterator.call(this)
    this._finalElement_0 = last
     tmp = this
     tmp_0
    if (step.compareTo_56(new Long(0, 0)) > 0) :
      tmp_0 = ulongCompare(_ULong___get_data__impl_(first), _ULong___get_data__impl_(last)) <= 0
     else :
      tmp_0 = ulongCompare(_ULong___get_data__impl_(first), _ULong___get_data__impl_(last)) >= 0

    tmp._hasNext_0 = tmp_0
     tmp_1 = this
    tmp_1._step_2 = step
    this._next_0 = this._hasNext_0 ? first : this._finalElement_0

  ULongProgressionIterator.prototype.hasNext_37 = def () :
    return this._hasNext_0

  ULongProgressionIterator.prototype.nextULong_1 = def () :
     value = this._next_0
    if (equals(new ULong(value), new ULong(this._finalElement_0))) :
      if (!this._hasNext_0)
        throw NoSuchElementException_init_$Create$()
      this._hasNext_0 = false
     else :
       tmp0_this = this
       tmp = tmp0_this
       tmp0_plus_0 = tmp0_this._next_0
       tmp1_plus_0 = this._step_2
      tmp._next_0 = _ULong___get_data__impl_(tmp0_plus_0).plus_38(_ULong___get_data__impl_(tmp1_plus_0))

    return value

  ULongProgressionIterator.$metadata$ = {
    simpleName: 'ULongProgressionIterator',
    kind: 'class',
    interfaces: []

  def getProgressionLastElement(start, end, step) :
     tmp
    if (step > 0) :
       tmp_0
      if (uintCompare(_UInt___get_data__impl_(start), _UInt___get_data__impl_(end)) >= 0) :
        tmp_0 = end
       else :
        :
           tmp0_minus_0 = differenceModulo(end, start, step)
          tmp_0 = _UInt___get_data__impl_(end) - _UInt___get_data__impl_(tmp0_minus_0) | 0


      tmp = tmp_0
     else if (step < 0) :
       tmp_1
      if (uintCompare(_UInt___get_data__impl_(start), _UInt___get_data__impl_(end)) <= 0) :
        tmp_1 = end
       else :
        :
           tmp1_toUInt_0 = -step | 0
           tmp2_plus_0 = differenceModulo(start, end, tmp1_toUInt_0)
          tmp_1 = _UInt___get_data__impl_(end) + _UInt___get_data__impl_(tmp2_plus_0) | 0


      tmp = tmp_1
     else :
      throw IllegalArgumentException_init_$Create$_0('Step is zero.')

    return tmp

  def getProgressionLastElement_0(start, end, step) :
     tmp
    if (step.compareTo_56(new Long(0, 0)) > 0) :
       tmp_0
      if (ulongCompare(_ULong___get_data__impl_(start), _ULong___get_data__impl_(end)) >= 0) :
        tmp_0 = end
       else :
        :
           tmp0_minus_0 = differenceModulo_0(end, start, step)
          tmp_0 = _ULong___get_data__impl_(end).minus_34(_ULong___get_data__impl_(tmp0_minus_0))


      tmp = tmp_0
     else if (step.compareTo_56(new Long(0, 0)) < 0) :
       tmp_1
      if (ulongCompare(_ULong___get_data__impl_(start), _ULong___get_data__impl_(end)) <= 0) :
        tmp_1 = end
       else :
        :
           tmp1_toULong_0 = step.unaryMinus_4()
           tmp2_plus_0 = differenceModulo_0(start, end, tmp1_toULong_0)
          tmp_1 = _ULong___get_data__impl_(end).plus_38(_ULong___get_data__impl_(tmp2_plus_0))


      tmp = tmp_1
     else :
      throw IllegalArgumentException_init_$Create$_0('Step is zero.')

    return tmp

  def differenceModulo(a, b, c) :
     ac = uintRemainder(a, c)
     bc = uintRemainder(b, c)
     tmp
    if (uintCompare(_UInt___get_data__impl_(ac), _UInt___get_data__impl_(bc)) >= 0) :
      tmp = _UInt___get_data__impl_(ac) - _UInt___get_data__impl_(bc) | 0
     else :
      :
         tmp0_plus_0 = _UInt___get_data__impl_(ac) - _UInt___get_data__impl_(bc) | 0
        tmp = _UInt___get_data__impl_(tmp0_plus_0) + _UInt___get_data__impl_(c) | 0


    return tmp

  def differenceModulo_0(a, b, c) :
     ac = ulongRemainder(a, c)
     bc = ulongRemainder(b, c)
     tmp
    if (ulongCompare(_ULong___get_data__impl_(ac), _ULong___get_data__impl_(bc)) >= 0) :
      tmp = _ULong___get_data__impl_(ac).minus_34(_ULong___get_data__impl_(bc))
     else :
      :
         tmp0_plus_0 = _ULong___get_data__impl_(ac).minus_34(_ULong___get_data__impl_(bc))
        tmp = _ULong___get_data__impl_(tmp0_plus_0).plus_38(_ULong___get_data__impl_(c))


    return tmp

  def _UShort___get_data__impl_(this_0) :
    return this_0

  def Companion_11() :
    Companion_instance_10 = this
    this._MIN_VALUE_2 = 0
    this._MAX_VALUE_2 = -1
    this._SIZE_BYTES_2 = 2
    this._SIZE_BITS_2 = 16

  Companion_11.prototype._get_MIN_VALUE__2 = def () :
    return this._MIN_VALUE_2

  Companion_11.prototype._get_MAX_VALUE__2 = def () :
    return this._MAX_VALUE_2

  Companion_11.prototype._get_SIZE_BYTES__9 = def () :
    return this._SIZE_BYTES_2

  Companion_11.prototype._get_SIZE_BITS__9 = def () :
    return this._SIZE_BITS_2

  Companion_11.$metadata$ = {
    simpleName: 'Companion',
    kind: 'object',
    interfaces: []

   Companion_instance_10
  def Companion_getInstance_10() :
    if (Companion_instance_10 == null)
      new Companion_11()
    return Companion_instance_10

  def UShort__compareTo_impl(this_0, other) :
     tmp = _UShort___get_data__impl_(this_0) & 65535
    return compareTo_0(tmp, _UByte___get_data__impl_(other) & 255)

  def UShort__compareTo_impl_0(this_0, other) :
     tmp = _UShort___get_data__impl_(this_0) & 65535
    return compareTo_0(tmp, _UShort___get_data__impl_(other) & 65535)

  def UShort__compareTo_impl_1(this_0, other) :
     tmp = this_0._data_2
    return UShort__compareTo_impl_0(tmp, other instanceof UShort ? other._data_2 : THROW_CCE())

  def UShort__compareTo_impl_2(this_0, other) :
     tmp0_compareTo_0 = _UShort___get_data__impl_(this_0) & 65535
    return uintCompare(_UInt___get_data__impl_(tmp0_compareTo_0), _UInt___get_data__impl_(other))

  def UShort__compareTo_impl_3(this_0, other) :
     tmp0_compareTo_0 = toLong(_UShort___get_data__impl_(this_0)).and(new Long(65535, 0))
    return ulongCompare(_ULong___get_data__impl_(tmp0_compareTo_0), _ULong___get_data__impl_(other))

  def UShort__plus_impl(this_0, other) :
     tmp0_plus_0 = _UShort___get_data__impl_(this_0) & 65535
     tmp1_plus_0 = _UByte___get_data__impl_(other) & 255
    return _UInt___get_data__impl_(tmp0_plus_0) + _UInt___get_data__impl_(tmp1_plus_0) | 0

  def UShort__plus_impl_0(this_0, other) :
     tmp0_plus_0 = _UShort___get_data__impl_(this_0) & 65535
     tmp1_plus_0 = _UShort___get_data__impl_(other) & 65535
    return _UInt___get_data__impl_(tmp0_plus_0) + _UInt___get_data__impl_(tmp1_plus_0) | 0

  def UShort__plus_impl_1(this_0, other) :
     tmp0_plus_0 = _UShort___get_data__impl_(this_0) & 65535
    return _UInt___get_data__impl_(tmp0_plus_0) + _UInt___get_data__impl_(other) | 0

  def UShort__plus_impl_2(this_0, other) :
     tmp0_plus_0 = toLong(_UShort___get_data__impl_(this_0)).and(new Long(65535, 0))
    return _ULong___get_data__impl_(tmp0_plus_0).plus_38(_ULong___get_data__impl_(other))

  def UShort__minus_impl(this_0, other) :
     tmp0_minus_0 = _UShort___get_data__impl_(this_0) & 65535
     tmp1_minus_0 = _UByte___get_data__impl_(other) & 255
    return _UInt___get_data__impl_(tmp0_minus_0) - _UInt___get_data__impl_(tmp1_minus_0) | 0

  def UShort__minus_impl_0(this_0, other) :
     tmp0_minus_0 = _UShort___get_data__impl_(this_0) & 65535
     tmp1_minus_0 = _UShort___get_data__impl_(other) & 65535
    return _UInt___get_data__impl_(tmp0_minus_0) - _UInt___get_data__impl_(tmp1_minus_0) | 0

  def UShort__minus_impl_1(this_0, other) :
     tmp0_minus_0 = _UShort___get_data__impl_(this_0) & 65535
    return _UInt___get_data__impl_(tmp0_minus_0) - _UInt___get_data__impl_(other) | 0

  def UShort__minus_impl_2(this_0, other) :
     tmp0_minus_0 = toLong(_UShort___get_data__impl_(this_0)).and(new Long(65535, 0))
    return _ULong___get_data__impl_(tmp0_minus_0).minus_34(_ULong___get_data__impl_(other))

  def UShort__times_impl(this_0, other) :
     tmp0_times_0 = _UShort___get_data__impl_(this_0) & 65535
     tmp1_times_0 = _UByte___get_data__impl_(other) & 255
    return imul(_UInt___get_data__impl_(tmp0_times_0), _UInt___get_data__impl_(tmp1_times_0))

  def UShort__times_impl_0(this_0, other) :
     tmp0_times_0 = _UShort___get_data__impl_(this_0) & 65535
     tmp1_times_0 = _UShort___get_data__impl_(other) & 65535
    return imul(_UInt___get_data__impl_(tmp0_times_0), _UInt___get_data__impl_(tmp1_times_0))

  def UShort__times_impl_1(this_0, other) :
     tmp0_times_0 = _UShort___get_data__impl_(this_0) & 65535
    return imul(_UInt___get_data__impl_(tmp0_times_0), _UInt___get_data__impl_(other))

  def UShort__times_impl_2(this_0, other) :
     tmp0_times_0 = toLong(_UShort___get_data__impl_(this_0)).and(new Long(65535, 0))
    return _ULong___get_data__impl_(tmp0_times_0).times_32(_ULong___get_data__impl_(other))

  def UShort__div_impl(this_0, other) :
     tmp0_div_0 = _UShort___get_data__impl_(this_0) & 65535
     tmp1_div_0 = _UByte___get_data__impl_(other) & 255
    return uintDivide(tmp0_div_0, tmp1_div_0)

  def UShort__div_impl_0(this_0, other) :
     tmp0_div_0 = _UShort___get_data__impl_(this_0) & 65535
     tmp1_div_0 = _UShort___get_data__impl_(other) & 65535
    return uintDivide(tmp0_div_0, tmp1_div_0)

  def UShort__div_impl_1(this_0, other) :
     tmp0_div_0 = _UShort___get_data__impl_(this_0) & 65535
    return uintDivide(tmp0_div_0, other)

  def UShort__div_impl_2(this_0, other) :
     tmp0_div_0 = toLong(_UShort___get_data__impl_(this_0)).and(new Long(65535, 0))
    return ulongDivide(tmp0_div_0, other)

  def UShort__rem_impl(this_0, other) :
     tmp0_rem_0 = _UShort___get_data__impl_(this_0) & 65535
     tmp1_rem_0 = _UByte___get_data__impl_(other) & 255
    return uintRemainder(tmp0_rem_0, tmp1_rem_0)

  def UShort__rem_impl_0(this_0, other) :
     tmp0_rem_0 = _UShort___get_data__impl_(this_0) & 65535
     tmp1_rem_0 = _UShort___get_data__impl_(other) & 65535
    return uintRemainder(tmp0_rem_0, tmp1_rem_0)

  def UShort__rem_impl_1(this_0, other) :
     tmp0_rem_0 = _UShort___get_data__impl_(this_0) & 65535
    return uintRemainder(tmp0_rem_0, other)

  def UShort__rem_impl_2(this_0, other) :
     tmp0_rem_0 = toLong(_UShort___get_data__impl_(this_0)).and(new Long(65535, 0))
    return ulongRemainder(tmp0_rem_0, other)

  def UShort__inc_impl(this_0) :
    return numberToShort(_UShort___get_data__impl_(this_0) + 1)

  def UShort__dec_impl(this_0) :
    return numberToShort(_UShort___get_data__impl_(this_0) - 1)

  def UShort__rangeTo_impl(this_0, other) :
     tmp = _UShort___get_data__impl_(this_0) & 65535
    return new UIntRange(tmp, _UShort___get_data__impl_(other) & 65535)

  def UShort__and_impl(this_0, other) :
     tmp0_and_0 = _UShort___get_data__impl_(this_0)
     tmp1_and_0 = _UShort___get_data__impl_(other)
    return toShort(tmp0_and_0 & tmp1_and_0)

  def UShort__or_impl(this_0, other) :
     tmp0_or_0 = _UShort___get_data__impl_(this_0)
     tmp1_or_0 = _UShort___get_data__impl_(other)
    return toShort(tmp0_or_0 | tmp1_or_0)

  def UShort__xor_impl(this_0, other) :
     tmp0_xor_0 = _UShort___get_data__impl_(this_0)
     tmp1_xor_0 = _UShort___get_data__impl_(other)
    return toShort(tmp0_xor_0 ^ tmp1_xor_0)

  def UShort__inv_impl(this_0) :
     tmp0_inv_0 = _UShort___get_data__impl_(this_0)
    return toShort(~tmp0_inv_0)

  def UShort__toByte_impl(this_0) :
    return toByte(_UShort___get_data__impl_(this_0))

  def UShort__toShort_impl(this_0) :
    return _UShort___get_data__impl_(this_0)

  def UShort__toInt_impl(this_0) :
    return _UShort___get_data__impl_(this_0) & 65535

  def UShort__toLong_impl(this_0) :
    return toLong(_UShort___get_data__impl_(this_0)).and(new Long(65535, 0))

  def UShort__toUByte_impl(this_0) :
     tmp0_toUByte_0 = _UShort___get_data__impl_(this_0)
    return toByte(tmp0_toUByte_0)

  def UShort__toUShort_impl(this_0) :
    return this_0

  def UShort__toUInt_impl(this_0) :
    return _UShort___get_data__impl_(this_0) & 65535

  def UShort__toULong_impl(this_0) :
    return toLong(_UShort___get_data__impl_(this_0)).and(new Long(65535, 0))

  def UShort__toFloat_impl(this_0) :
    return _UShort___get_data__impl_(this_0) & 65535

  def UShort__toDouble_impl(this_0) :
    return _UShort___get_data__impl_(this_0) & 65535

  def UShort__toString_impl(this_0) :
    return (_UShort___get_data__impl_(this_0) & 65535).toString()

  def UShort__hashCode_impl(this_0) :
    return this_0

  def UShort__equals_impl(this_0, other) :
    if (!(other instanceof UShort))
      return false;
    else :

     tmp0_other_with_cast = other instanceof UShort ? other._data_2 : THROW_CCE()
    if (!(this_0 === tmp0_other_with_cast))
      return false
    return true

  def UShort(data) :
    Companion_getInstance_10()
    this._data_2 = data

  UShort.prototype.compareTo_11 = def (other) :
    return UShort__compareTo_impl_0(this._data_2, other)

  UShort.prototype.compareTo_25 = def (other) :
    return UShort__compareTo_impl_1(this, other)

  UShort.prototype.toString = def () :
    return UShort__toString_impl(this._data_2)

  UShort.prototype.hashCode = def () :
    return UShort__hashCode_impl(this._data_2)

  UShort.prototype.equals = def (other) :
    return UShort__equals_impl(this._data_2, other)

  UShort.$metadata$ = {
    simpleName: 'UShort',
    kind: 'class',
    interfaces: [Comparable]

  def toUShort(_this_) :
    return toShort(_this_)

  def toUShort_0(_this_) :
    return _this_.toShort_6()

  def toUShort_1(_this_) :
    return _this_

  def _get_array__2($this) :
    return $this._array_2

  def _set_index__2($this, _set___) :
    $this._index_3 = _set___

  def _get_index__2($this) :
    return $this._index_3

  def _UShortArray___get_storage__impl_(this_0) :
    return this_0

  def _UShortArray___init__impl_(size_0) :
     tmp = new Int16Array(size_0)
    return tmp

  def UShortArray__get_impl(this_0, index) :
     tmp0_toUShort_0 = _UShortArray___get_storage__impl_(this_0)[index]
    return tmp0_toUShort_0

  def UShortArray__set_impl(this_0, index, value) :
     tmp = _UShortArray___get_storage__impl_(this_0)
    tmp[index] = _UShort___get_data__impl_(value)

  def _UShortArray___get_size__impl_(this_0) :
    return _UShortArray___get_storage__impl_(this_0).length

  def UShortArray__iterator_impl(this_0) :
    return new Iterator_2(_UShortArray___get_storage__impl_(this_0))

  def Iterator_2(array) :
    UShortIterator.call(this)
    this._array_2 = array
    this._index_3 = 0

  Iterator_2.prototype.hasNext_37 = def () :
    return this._index_3 < this._array_2.length

  Iterator_2.prototype.nextUShort_0 = def () :
     tmp
    if (this._index_3 < this._array_2.length) :
       tmp0_this = this
       tmp1 = tmp0_this._index_3
      tmp0_this._index_3 = tmp1 + 1 | 0
       tmp0_toUShort_0 = this._array_2[tmp1]
      tmp = tmp0_toUShort_0
     else :
      throw NoSuchElementException_init_$Create$_0(this._index_3.toString())

    return tmp

  Iterator_2.$metadata$ = {
    simpleName: 'Iterator',
    kind: 'class',
    interfaces: []

  def UShortArray__contains_impl(this_0, element) :
     tmp = isObject(new UShort(element)) ? new UShort(element) : THROW_CCE()
    if (!(tmp instanceof UShort))
      return false;
    else :

     tmp_0 = _UShortArray___get_storage__impl_(this_0)
    return contains_0(tmp_0, _UShort___get_data__impl_(element))

  def UShortArray__contains_impl_0(this_0, element) :
    if (!(element instanceof UShort))
      return false;
    else :

     tmp = this_0._storage_2
    return UShortArray__contains_impl(tmp, element instanceof UShort ? element._data_2 : THROW_CCE())

  def UShortArray__containsAll_impl(this_0, elements) :
     tmp$ret$0
    l$ret$1: do :
       tmp0_all_0 = isInterface(elements, Collection) ? elements : THROW_CCE()
       tmp
      if (isInterface(tmp0_all_0, Collection)) :
        tmp = tmp0_all_0.isEmpty_29()
       else :
        :
          tmp = false


      if (tmp) :
        tmp$ret$0 = true
        break l$ret$1
       else :

       tmp0_iterator_1 = tmp0_all_0.iterator_38()
      while (tmp0_iterator_1.hasNext_37()) :
         element_2 = tmp0_iterator_1.next_41()
         tmp_0
        if (element_2 instanceof UShort) :
           tmp_1 = _UShortArray___get_storage__impl_(this_0)
           tmp0_toShort_0_4 = element_2._data_2
          tmp_0 = contains_0(tmp_1, _UShort___get_data__impl_(tmp0_toShort_0_4))
         else :
          :
            tmp_0 = false


        if (!tmp_0) :
          tmp$ret$0 = false
          break l$ret$1
         else :


      tmp$ret$0 = true

     while (false)
    return tmp$ret$0

  def UShortArray__containsAll_impl_0(this_0, elements) :
    return UShortArray__containsAll_impl(this_0._storage_2, elements)

  def UShortArray__isEmpty_impl(this_0) :
    return _UShortArray___get_storage__impl_(this_0).length === 0

  def UShortArray__toString_impl(this_0) :
    return '' + 'UShortArray(storage=' + toString_0(this_0) + ')'

  def UShortArray__hashCode_impl(this_0) :
    return hashCode(this_0)

  def UShortArray__equals_impl(this_0, other) :
    if (!(other instanceof UShortArray))
      return false;
    else :

     tmp0_other_with_cast = other instanceof UShortArray ? other._storage_2 : THROW_CCE()
    if (!equals(this_0, tmp0_other_with_cast))
      return false
    return true

  def UShortArray(storage) :
    this._storage_2 = storage

  UShortArray.prototype._get_size__18 = def () :
    return _UShortArray___get_size__impl_(this._storage_2)

  UShortArray.prototype.iterator_38 = def () :
    return UShortArray__iterator_impl(this._storage_2)

  UShortArray.prototype.contains_14 = def (element) :
    return UShortArray__contains_impl(this._storage_2, element)

  UShortArray.prototype.contains_32 = def (element) :
    return UShortArray__contains_impl_0(this, element)

  UShortArray.prototype.containsAll_10 = def (elements) :
    return UShortArray__containsAll_impl(this._storage_2, elements)

  UShortArray.prototype.containsAll_21 = def (elements) :
    return UShortArray__containsAll_impl_0(this, elements)

  UShortArray.prototype.isEmpty_29 = def () :
    return UShortArray__isEmpty_impl(this._storage_2)

  UShortArray.prototype.toString = def () :
    return UShortArray__toString_impl(this._storage_2)

  UShortArray.prototype.hashCode = def () :
    return UShortArray__hashCode_impl(this._storage_2)

  UShortArray.prototype.equals = def (other) :
    return UShortArray__equals_impl(this._storage_2, other)

  UShortArray.$metadata$ = {
    simpleName: 'UShortArray',
    kind: 'class',
    interfaces: [Collection]

  def uintCompare(v1, v2) :
    return compareTo_0(v1 ^ IntCompanionObject_getInstance()._MIN_VALUE_5, v2 ^ IntCompanionObject_getInstance()._MIN_VALUE_5)

  def uintDivide(v1, v2) :
     tmp = toLong(_UInt___get_data__impl_(v1)).and(new Long(-1, 0))
     tmp0_toUInt_0 = tmp.div_32(toLong(_UInt___get_data__impl_(v2)).and(new Long(-1, 0)))
    return tmp0_toUInt_0.toInt_6()

  def uintRemainder(v1, v2) :
     tmp = toLong(_UInt___get_data__impl_(v1)).and(new Long(-1, 0))
     tmp0_toUInt_0 = tmp.rem_32(toLong(_UInt___get_data__impl_(v2)).and(new Long(-1, 0)))
    return tmp0_toUInt_0.toInt_6()

  def uintToDouble(v) :
    return (v & IntCompanionObject_getInstance()._MAX_VALUE_5) + (v >>> 31 << 30) * 2

  def ulongCompare(v1, v2) :
    return v1.xor(new Long(0, -2147483648)).compareTo_56(v2.xor(new Long(0, -2147483648)))

  def ulongDivide(v1, v2) :
     dividend = _ULong___get_data__impl_(v1)
     divisor = _ULong___get_data__impl_(v2)
    if (divisor.compareTo_56(new Long(0, 0)) < 0) :
       tmp
      if (ulongCompare(_ULong___get_data__impl_(v1), _ULong___get_data__impl_(v2)) < 0) :
        tmp = new Long(0, 0)
       else :
        :
          tmp = new Long(1, 0)


      return tmp
    if (dividend.compareTo_56(new Long(0, 0)) >= 0) :
      return dividend.div_32(divisor)
     quotient = dividend.ushr_0(1).div_32(divisor).shl_0(1)
     rem = dividend.minus_34(quotient.times_32(divisor))
     tmp_0
     tmp0_compareTo_0 = rem
     tmp1_compareTo_0 = divisor
    if (ulongCompare(_ULong___get_data__impl_(tmp0_compareTo_0), _ULong___get_data__impl_(tmp1_compareTo_0)) >= 0) :
      tmp_0 = 1
     else :
      :
        tmp_0 = 0


     tmp2_plus_0 = tmp_0
    return quotient.plus_38(toLong(tmp2_plus_0))

  def ulongRemainder(v1, v2) :
     dividend = _ULong___get_data__impl_(v1)
     divisor = _ULong___get_data__impl_(v2)
    if (divisor.compareTo_56(new Long(0, 0)) < 0) :
       tmp
      if (ulongCompare(_ULong___get_data__impl_(v1), _ULong___get_data__impl_(v2)) < 0) :
        tmp = v1
       else :
        :
          tmp = _ULong___get_data__impl_(v1).minus_34(_ULong___get_data__impl_(v2))


      return tmp
    if (dividend.compareTo_56(new Long(0, 0)) >= 0) :
      return dividend.rem_32(divisor)
     quotient = dividend.ushr_0(1).div_32(divisor).shl_0(1)
     rem = dividend.minus_34(quotient.times_32(divisor))
     tmp_0
     tmp0_compareTo_0 = rem
     tmp1_compareTo_0 = divisor
    if (ulongCompare(_ULong___get_data__impl_(tmp0_compareTo_0), _ULong___get_data__impl_(tmp1_compareTo_0)) >= 0) :
      tmp_0 = divisor
     else :
      :
        tmp_0 = new Long(0, 0)


    return rem.minus_34(tmp_0)

  def ulongToDouble(v) :
    return v.ushr_0(11).toDouble_6() * 2048 + v.and(new Long(2047, 0)).toDouble_6()

  def ulongToString(v) :
    return ulongToString_0(v, 10)

  def ulongToString_0(v, base) :
    if (v.compareTo_56(new Long(0, 0)) >= 0)
      return toString_1(v, base)
     tmp0_div_0 = v.ushr_0(1)
     quotient = tmp0_div_0.div_32(toLong(base)).shl_0(1)
     tmp1_times_0 = quotient
     rem = v.minus_34(tmp1_times_0.times_32(toLong(base)))
    if (rem.compareTo_56(toLong(base)) >= 0) :
       tmp2_minus_0 = rem
      rem = tmp2_minus_0.minus_34(toLong(base))
       tmp3_plus_0 = quotient
       tmp4_plus_0 = 1
      quotient = tmp3_plus_0.plus_38(toLong(tmp4_plus_0))
    return toString_1(quotient, base) + toString_1(rem, base)

  def doubleToUInt(v) :
     tmp
    if (isNaN_0(v)) :
      tmp = 0
     else :
       tmp0_toDouble_0 = 0
      if (v <= uintToDouble(_UInt___get_data__impl_(tmp0_toDouble_0))) :
        tmp = 0
       else :
         tmp1_toDouble_0 = -1
        if (v >= uintToDouble(_UInt___get_data__impl_(tmp1_toDouble_0))) :
          tmp = -1
         else :
          if (v <= IntCompanionObject_getInstance()._MAX_VALUE_5) :
             tmp2_toUInt_0 = numberToInt(v)
            tmp = tmp2_toUInt_0
           else :
            :
               tmp3_toUInt_0 = numberToInt(v - IntCompanionObject_getInstance()._MAX_VALUE_5)
               tmp5_plus_0 = tmp3_toUInt_0
               tmp4_toUInt_0 = IntCompanionObject_getInstance()._MAX_VALUE_5
               tmp6_plus_0 = tmp4_toUInt_0
              tmp = _UInt___get_data__impl_(tmp5_plus_0) + _UInt___get_data__impl_(tmp6_plus_0) | 0





    return tmp

  def doubleToULong(v) :
     tmp
    if (isNaN_0(v)) :
      tmp = new Long(0, 0)
     else :
       tmp0_toDouble_0 = new Long(0, 0)
      if (v <= ulongToDouble(_ULong___get_data__impl_(tmp0_toDouble_0))) :
        tmp = new Long(0, 0)
       else :
         tmp1_toDouble_0 = new Long(-1, -1)
        if (v >= ulongToDouble(_ULong___get_data__impl_(tmp1_toDouble_0))) :
          tmp = new Long(-1, -1)
         else :
          if (v < 9.223372036854776E18) :
             tmp2_toULong_0 = numberToLong(v)
            tmp = tmp2_toULong_0
           else :
            :
               tmp3_toULong_0 = numberToLong(v - 9.223372036854776E18)
               tmp4_plus_0 = tmp3_toULong_0
               tmp5_plus_0 = new Long(0, -2147483648)
              tmp = _ULong___get_data__impl_(tmp4_plus_0).plus_38(_ULong___get_data__impl_(tmp5_plus_0))





    return tmp

  def ExperimentalUnsignedTypes() :

  ExperimentalUnsignedTypes.$metadata$ = {
    simpleName: 'ExperimentalUnsignedTypes',
    kind: 'class',
    interfaces: [Annotation]

  def Annotation() :

  Annotation.$metadata$ = {
    simpleName: 'Annotation',
    kind: 'interface',
    interfaces: []

  def CharSequence() :

  CharSequence.$metadata$ = {
    simpleName: 'CharSequence',
    kind: 'interface',
    interfaces: []

  def Comparable() :

  Comparable.$metadata$ = {
    simpleName: 'Comparable',
    kind: 'interface',
    interfaces: []

  def Iterator_3() :

  Iterator_3.$metadata$ = {
    simpleName: 'Iterator',
    kind: 'interface',
    interfaces: []

  def ListIterator() :

  ListIterator.$metadata$ = {
    simpleName: 'ListIterator',
    kind: 'interface',
    interfaces: [Iterator_3]

  def MutableIterator() :

  MutableIterator.$metadata$ = {
    simpleName: 'MutableIterator',
    kind: 'interface',
    interfaces: [Iterator_3]

  def MutableListIterator() :

  MutableListIterator.$metadata$ = {
    simpleName: 'MutableListIterator',
    kind: 'interface',
    interfaces: [ListIterator, MutableIterator]

  def Number_0() :

  Number_0.$metadata$ = {
    simpleName: 'Number',
    kind: 'class',
    interfaces: []

  def SinceKotlin(version) :
    this._version_0 = version

  SinceKotlin.prototype._get_version__0 = def () :
    return this._version_0

  SinceKotlin.$metadata$ = {
    simpleName: 'SinceKotlin',
    kind: 'class',
    interfaces: [Annotation]

  def Suppress(names) :
    this._names = names

  Suppress.prototype._get_names_ = def () :
    return this._names

  Suppress.$metadata$ = {
    simpleName: 'Suppress',
    kind: 'class',
    interfaces: [Annotation]

   DeprecationLevel_WARNING_instance
   DeprecationLevel_ERROR_instance
   DeprecationLevel_HIDDEN_instance
  def values_5() :
    return [DeprecationLevel_WARNING_getInstance(), DeprecationLevel_ERROR_getInstance(), DeprecationLevel_HIDDEN_getInstance()]

  def valueOf_5(value) :
    switch (value) :
      case 'WARNING':
        return DeprecationLevel_WARNING_getInstance();
      case 'ERROR':
        return DeprecationLevel_ERROR_getInstance();
      case 'HIDDEN':
        return DeprecationLevel_HIDDEN_getInstance();
      default:return THROW_ISE();


   DeprecationLevel_entriesInitialized
  def DeprecationLevel_initEntries() :
    if (DeprecationLevel_entriesInitialized)
      return Unit_getInstance()
    DeprecationLevel_entriesInitialized = true
    DeprecationLevel_WARNING_instance = new DeprecationLevel('WARNING', 0)
    DeprecationLevel_ERROR_instance = new DeprecationLevel('ERROR', 1)
    DeprecationLevel_HIDDEN_instance = new DeprecationLevel('HIDDEN', 2)

  def DeprecationLevel(name, ordinal) :
    Enum.call(this, name, ordinal)

  DeprecationLevel.$metadata$ = {
    simpleName: 'DeprecationLevel',
    kind: 'class',
    interfaces: []

  def PublishedApi() :

  PublishedApi.$metadata$ = {
    simpleName: 'PublishedApi',
    kind: 'class',
    interfaces: [Annotation]

  def ParameterName(name) :
    this._name = name

  ParameterName.prototype._get_name__22 = def () :
    return this._name

  ParameterName.$metadata$ = {
    simpleName: 'ParameterName',
    kind: 'class',
    interfaces: [Annotation]

  def Deprecated_init_$Init$(message, replaceWith, level, $mask0, $marker, $this) :
    if (!(($mask0 & 2) === 0))
      replaceWith = new ReplaceWith('', [])
    if (!(($mask0 & 4) === 0))
      level = DeprecationLevel_WARNING_getInstance()
    Deprecated.call($this, message, replaceWith, level)
    return $this

  def Deprecated_init_$Create$(message, replaceWith, level, $mask0, $marker) :
    return Deprecated_init_$Init$(message, replaceWith, level, $mask0, $marker, Object.create(Deprecated.prototype))

  def Deprecated(message, replaceWith, level) :
    this._message_1 = message
    this._replaceWith = replaceWith
    this._level_2 = level

  Deprecated.prototype._get_message__15 = def () :
    return this._message_1

  Deprecated.prototype._get_replaceWith_ = def () :
    return this._replaceWith

  Deprecated.prototype._get_level__2 = def () :
    return this._level_2

  Deprecated.$metadata$ = {
    simpleName: 'Deprecated',
    kind: 'class',
    interfaces: [Annotation]

  def ReplaceWith(expression, imports) :
    this._expression = expression
    this._imports = imports

  ReplaceWith.prototype._get_expression_ = def () :
    return this._expression

  ReplaceWith.prototype._get_imports_ = def () :
    return this._imports

  ReplaceWith.$metadata$ = {
    simpleName: 'ReplaceWith',
    kind: 'class',
    interfaces: [Annotation]

  def ExtensionFunctionType() :

  ExtensionFunctionType.$metadata$ = {
    simpleName: 'ExtensionFunctionType',
    kind: 'class',
    interfaces: [Annotation]

  def UnsafeVariance() :

  UnsafeVariance.$metadata$ = {
    simpleName: 'UnsafeVariance',
    kind: 'class',
    interfaces: [Annotation]

  def DeprecationLevel_WARNING_getInstance() :
    DeprecationLevel_initEntries()
    return DeprecationLevel_WARNING_instance

  def DeprecationLevel_ERROR_getInstance() :
    DeprecationLevel_initEntries()
    return DeprecationLevel_ERROR_instance

  def DeprecationLevel_HIDDEN_getInstance() :
    DeprecationLevel_initEntries()
    return DeprecationLevel_HIDDEN_instance

  def ByteIterator() :

  ByteIterator.prototype.next_41 = def () :
    return this.nextByte_0()

  ByteIterator.$metadata$ = {
    simpleName: 'ByteIterator',
    kind: 'class',
    interfaces: [Iterator_3]

  def IntIterator() :

  IntIterator.prototype.next_41 = def () :
    return this.nextInt_1()

  IntIterator.$metadata$ = {
    simpleName: 'IntIterator',
    kind: 'class',
    interfaces: [Iterator_3]

  def DoubleIterator() :

  DoubleIterator.prototype.next_41 = def () :
    return this.nextDouble_0()

  DoubleIterator.$metadata$ = {
    simpleName: 'DoubleIterator',
    kind: 'class',
    interfaces: [Iterator_3]

  def FloatIterator() :

  FloatIterator.prototype.next_41 = def () :
    return this.nextFloat_0()

  FloatIterator.$metadata$ = {
    simpleName: 'FloatIterator',
    kind: 'class',
    interfaces: [Iterator_3]

  def LongIterator() :

  LongIterator.prototype.next_41 = def () :
    return this.nextLong_1()

  LongIterator.$metadata$ = {
    simpleName: 'LongIterator',
    kind: 'class',
    interfaces: [Iterator_3]

  def CharIterator() :

  CharIterator.prototype.next_41 = def () :
    return this.nextChar_1()

  CharIterator.$metadata$ = {
    simpleName: 'CharIterator',
    kind: 'class',
    interfaces: [Iterator_3]

  def BooleanIterator() :

  BooleanIterator.prototype.next_41 = def () :
    return this.nextBoolean_0()

  BooleanIterator.$metadata$ = {
    simpleName: 'BooleanIterator',
    kind: 'class',
    interfaces: [Iterator_3]

  def ShortIterator() :

  ShortIterator.prototype.next_41 = def () :
    return this.nextShort_0()

  ShortIterator.$metadata$ = {
    simpleName: 'ShortIterator',
    kind: 'class',
    interfaces: [Iterator_3]

  def _get_finalElement__1($this) :
    return $this._finalElement_1

  def _set_hasNext__1($this, _set___) :
    $this._hasNext_1 = _set___

  def _get_hasNext__1($this) :
    return $this._hasNext_1

  def _set_next__1($this, _set___) :
    $this._next_1 = _set___

  def _get_next__1($this) :
    return $this._next_1

  def IntProgressionIterator(first, last, step) :
    IntIterator.call(this)
    this._step_3 = step
    this._finalElement_1 = last
    this._hasNext_1 = this._step_3 > 0 ? first <= last : first >= last
    this._next_1 = this._hasNext_1 ? first : this._finalElement_1

  IntProgressionIterator.prototype._get_step__11 = def () :
    return this._step_3

  IntProgressionIterator.prototype.hasNext_37 = def () :
    return this._hasNext_1

  IntProgressionIterator.prototype.nextInt_1 = def () :
     value = this._next_1
    if (value === this._finalElement_1) :
      if (!this._hasNext_1)
        throw NoSuchElementException_init_$Create$()
      this._hasNext_1 = false
     else :
       tmp0_this = this
      tmp0_this._next_1 = tmp0_this._next_1 + this._step_3 | 0

    return value

  IntProgressionIterator.$metadata$ = {
    simpleName: 'IntProgressionIterator',
    kind: 'class',
    interfaces: []

  def _get_finalElement__2($this) :
    return $this._finalElement_2

  def _set_hasNext__2($this, _set___) :
    $this._hasNext_2 = _set___

  def _get_hasNext__2($this) :
    return $this._hasNext_2

  def _set_next__2($this, _set___) :
    $this._next_2 = _set___

  def _get_next__2($this) :
    return $this._next_2

  def LongProgressionIterator(first, last, step) :
    LongIterator.call(this)
    this._step_4 = step
    this._finalElement_2 = last
    this._hasNext_2 = this._step_4.compareTo_56(new Long(0, 0)) > 0 ? first.compareTo_56(last) <= 0 : first.compareTo_56(last) >= 0
    this._next_2 = this._hasNext_2 ? first : this._finalElement_2

  LongProgressionIterator.prototype._get_step__11 = def () :
    return this._step_4

  LongProgressionIterator.prototype.hasNext_37 = def () :
    return this._hasNext_2

  LongProgressionIterator.prototype.nextLong_1 = def () :
     value = this._next_2
    if (value.equals(this._finalElement_2)) :
      if (!this._hasNext_2)
        throw NoSuchElementException_init_$Create$()
      this._hasNext_2 = false
     else :
       tmp0_this = this
      tmp0_this._next_2 = tmp0_this._next_2.plus_38(this._step_4)

    return value

  LongProgressionIterator.$metadata$ = {
    simpleName: 'LongProgressionIterator',
    kind: 'class',
    interfaces: []

  def _get_finalElement__3($this) :
    return $this._finalElement_3

  def _set_hasNext__3($this, _set___) :
    $this._hasNext_3 = _set___

  def _get_hasNext__3($this) :
    return $this._hasNext_3

  def _set_next__3($this, _set___) :
    $this._next_3 = _set___

  def _get_next__3($this) :
    return $this._next_3

  def CharProgressionIterator(first, last, step) :
    CharIterator.call(this)
    this._step_5 = step
    this._finalElement_3 = last.toInt_6()
    this._hasNext_3 = this._step_5 > 0 ? first.compareTo_17(last) <= 0 : first.compareTo_17(last) >= 0
    this._next_3 = this._hasNext_3 ? first.toInt_6() : this._finalElement_3

  CharProgressionIterator.prototype._get_step__11 = def () :
    return this._step_5

  CharProgressionIterator.prototype.hasNext_37 = def () :
    return this._hasNext_3

  CharProgressionIterator.prototype.nextChar_1 = def () :
     value = this._next_3
    if (value === this._finalElement_3) :
      if (!this._hasNext_3)
        throw NoSuchElementException_init_$Create$()
      this._hasNext_3 = false
     else :
       tmp0_this = this
      tmp0_this._next_3 = tmp0_this._next_3 + this._step_5 | 0

    return numberToChar(value)

  CharProgressionIterator.$metadata$ = {
    simpleName: 'CharProgressionIterator',
    kind: 'class',
    interfaces: []

  def Companion_12() :
    Companion_instance_11 = this

  Companion_12.prototype.fromClosedRange_1 = def (rangeStart, rangeEnd, step) :
    return new IntProgression(rangeStart, rangeEnd, step)

  Companion_12.$metadata$ = {
    simpleName: 'Companion',
    kind: 'object',
    interfaces: []

   Companion_instance_11
  def Companion_getInstance_11() :
    if (Companion_instance_11 == null)
      new Companion_12()
    return Companion_instance_11

  def IntProgression(start, endInclusive, step) :
    Companion_getInstance_11()
    if (step === 0)
      throw IllegalArgumentException_init_$Create$_0('Step must be non-zero.')
    if (step === IntCompanionObject_getInstance()._MIN_VALUE_5)
      throw IllegalArgumentException_init_$Create$_0('Step must be greater than Int.MIN_VALUE to avoid overflow on negation.')
    this._first_1 = start
    this._last_1 = getProgressionLastElement_1(start, endInclusive, step)
    this._step_6 = step

  IntProgression.prototype._get_first__8 = def () :
    return this._first_1

  IntProgression.prototype._get_last__10 = def () :
    return this._last_1

  IntProgression.prototype._get_step__11 = def () :
    return this._step_6

  IntProgression.prototype.iterator_38 = def () :
    return new IntProgressionIterator(this._first_1, this._last_1, this._step_6)

  IntProgression.prototype.isEmpty_29 = def () :
    return this._step_6 > 0 ? this._first_1 > this._last_1 : this._first_1 < this._last_1

  IntProgression.prototype.equals = def (other) :
     tmp
    if (other instanceof IntProgression) :
      tmp = (this.isEmpty_29() ? other.isEmpty_29() : false) ? true : (this._first_1 === other._first_1 ? this._last_1 === other._last_1 : false) ? this._step_6 === other._step_6 : false
     else :
      :
        tmp = false


    return tmp

  IntProgression.prototype.hashCode = def () :
    return this.isEmpty_29() ? -1 : imul(31, imul(31, this._first_1) + this._last_1 | 0) + this._step_6 | 0

  IntProgression.prototype.toString = def () :
    return this._step_6 > 0 ? '' + this._first_1 + '..' + this._last_1 + ' step ' + this._step_6 : '' + this._first_1 + ' downTo ' + this._last_1 + ' step ' + (-this._step_6 | 0)

  IntProgression.$metadata$ = {
    simpleName: 'IntProgression',
    kind: 'class',
    interfaces: [Iterable]

  def Companion_13() :
    Companion_instance_12 = this

  Companion_13.prototype.fromClosedRange_2 = def (rangeStart, rangeEnd, step) :
    return new LongProgression(rangeStart, rangeEnd, step)

  Companion_13.$metadata$ = {
    simpleName: 'Companion',
    kind: 'object',
    interfaces: []

   Companion_instance_12
  def Companion_getInstance_12() :
    if (Companion_instance_12 == null)
      new Companion_13()
    return Companion_instance_12

  def LongProgression(start, endInclusive, step) :
    Companion_getInstance_12()
    if (step.equals(new Long(0, 0)))
      throw IllegalArgumentException_init_$Create$_0('Step must be non-zero.')
    if (step.equals(new Long(0, -2147483648)))
      throw IllegalArgumentException_init_$Create$_0('Step must be greater than Long.MIN_VALUE to avoid overflow on negation.')
    this._first_2 = start
    this._last_2 = getProgressionLastElement_2(start.toLong_6(), endInclusive.toLong_6(), step).toLong_6()
    this._step_7 = step

  LongProgression.prototype._get_first__8 = def () :
    return this._first_2

  LongProgression.prototype._get_last__10 = def () :
    return this._last_2

  LongProgression.prototype._get_step__11 = def () :
    return this._step_7

  LongProgression.prototype.iterator_38 = def () :
    return new LongProgressionIterator(this._first_2, this._last_2, this._step_7)

  LongProgression.prototype.isEmpty_29 = def () :
    return this._step_7.compareTo_56(new Long(0, 0)) > 0 ? this._first_2.compareTo_56(this._last_2) > 0 : this._first_2.compareTo_56(this._last_2) < 0

  LongProgression.prototype.equals = def (other) :
     tmp
    if (other instanceof LongProgression) :
      tmp = (this.isEmpty_29() ? other.isEmpty_29() : false) ? true : (this._first_2.equals(other._first_2) ? this._last_2.equals(other._last_2) : false) ? this._step_7.equals(other._step_7) : false
     else :
      :
        tmp = false


    return tmp

  LongProgression.prototype.hashCode = def () :
    return this.isEmpty_29() ? -1 : numberToLong(31).times_32(numberToLong(31).times_32(this._first_2.xor(this._first_2.ushr_0(32))).plus_38(this._last_2.xor(this._last_2.ushr_0(32)))).plus_38(this._step_7.xor(this._step_7.ushr_0(32))).toInt_6()

  LongProgression.prototype.toString = def () :
    return this._step_7.compareTo_56(new Long(0, 0)) > 0 ? '' + this._first_2 + '..' + this._last_2 + ' step ' + this._step_7 : '' + this._first_2 + ' downTo ' + this._last_2 + ' step ' + this._step_7.unaryMinus_4()

  LongProgression.$metadata$ = {
    simpleName: 'LongProgression',
    kind: 'class',
    interfaces: [Iterable]

  def Companion_14() :
    Companion_instance_13 = this

  Companion_14.prototype.fromClosedRange_3 = def (rangeStart, rangeEnd, step) :
    return new CharProgression(rangeStart, rangeEnd, step)

  Companion_14.$metadata$ = {
    simpleName: 'Companion',
    kind: 'object',
    interfaces: []

   Companion_instance_13
  def Companion_getInstance_13() :
    if (Companion_instance_13 == null)
      new Companion_14()
    return Companion_instance_13

  def CharProgression(start, endInclusive, step) :
    Companion_getInstance_13()
    if (step === 0)
      throw IllegalArgumentException_init_$Create$_0('Step must be non-zero.')
    if (step === IntCompanionObject_getInstance()._MIN_VALUE_5)
      throw IllegalArgumentException_init_$Create$_0('Step must be greater than Int.MIN_VALUE to avoid overflow on negation.')
    this._first_3 = start
    this._last_3 = numberToChar(getProgressionLastElement_1(start.toInt_6(), endInclusive.toInt_6(), step))
    this._step_8 = step

  CharProgression.prototype._get_first__8 = def () :
    return this._first_3

  CharProgression.prototype._get_last__10 = def () :
    return this._last_3

  CharProgression.prototype._get_step__11 = def () :
    return this._step_8

  CharProgression.prototype.iterator_38 = def () :
    return new CharProgressionIterator(this._first_3, this._last_3, this._step_8)

  CharProgression.prototype.isEmpty_29 = def () :
    return this._step_8 > 0 ? this._first_3.compareTo_17(this._last_3) > 0 : this._first_3.compareTo_17(this._last_3) < 0

  CharProgression.prototype.equals = def (other) :
     tmp
    if (other instanceof CharProgression) :
      tmp = (this.isEmpty_29() ? other.isEmpty_29() : false) ? true : (this._first_3.equals(other._first_3) ? this._last_3.equals(other._last_3) : false) ? this._step_8 === other._step_8 : false
     else :
      :
        tmp = false


    return tmp

  CharProgression.prototype.hashCode = def () :
    return this.isEmpty_29() ? -1 : imul(31, imul(31, this._first_3.toInt_6()) + this._last_3.toInt_6() | 0) + this._step_8 | 0

  CharProgression.prototype.toString = def () :
    return this._step_8 > 0 ? '' + this._first_3 + '..' + this._last_3 + ' step ' + this._step_8 : '' + this._first_3 + ' downTo ' + this._last_3 + ' step ' + (-this._step_8 | 0)

  CharProgression.$metadata$ = {
    simpleName: 'CharProgression',
    kind: 'class',
    interfaces: [Iterable]

  ClosedRange.prototype.contains_22 = def (value) :
    return compareTo_0(value, this._get_start__6()) >= 0 ? compareTo_0(value, this._get_endInclusive__6()) <= 0 : false

  ClosedRange.prototype.isEmpty_29 = def () :
    return compareTo_0(this._get_start__6(), this._get_endInclusive__6()) > 0

  def ClosedRange() :

  ClosedRange.$metadata$ = {
    simpleName: 'ClosedRange',
    kind: 'interface',
    interfaces: []

  def Companion_15() :
    Companion_instance_14 = this
    this._EMPTY_1 = new IntRange(1, 0)

  Companion_15.prototype._get_EMPTY__3 = def () :
    return this._EMPTY_1

  Companion_15.$metadata$ = {
    simpleName: 'Companion',
    kind: 'object',
    interfaces: []

   Companion_instance_14
  def Companion_getInstance_14() :
    if (Companion_instance_14 == null)
      new Companion_15()
    return Companion_instance_14

  def IntRange(start, endInclusive) :
    Companion_getInstance_14()
    IntProgression.call(this, start, endInclusive, 1)

  IntRange.prototype._get_start__6 = def () :
    return this._get_first__8()

  IntRange.prototype._get_endInclusive__6 = def () :
    return this._get_last__10()

  IntRange.prototype.contains_17 = def (value) :
    return this._get_first__8() <= value ? value <= this._get_last__10() : false

  IntRange.prototype.contains_22 = def (value) :
    return this.contains_17(typeof value === 'number' ? value : THROW_CCE())

  IntRange.prototype.isEmpty_29 = def () :
    return this._get_first__8() > this._get_last__10()

  IntRange.prototype.equals = def (other) :
     tmp
    if (other instanceof IntRange) :
      tmp = (this.isEmpty_29() ? other.isEmpty_29() : false) ? true : this._get_first__8() === other._get_first__8() ? this._get_last__10() === other._get_last__10() : false
     else :
      :
        tmp = false


    return tmp

  IntRange.prototype.hashCode = def () :
    return this.isEmpty_29() ? -1 : imul(31, this._get_first__8()) + this._get_last__10() | 0

  IntRange.prototype.toString = def () :
    return '' + this._get_first__8() + '..' + this._get_last__10()

  IntRange.$metadata$ = {
    simpleName: 'IntRange',
    kind: 'class',
    interfaces: [ClosedRange]

  def Companion_16() :
    Companion_instance_15 = this
    this._EMPTY_2 = new LongRange(new Long(1, 0), new Long(0, 0))

  Companion_16.prototype._get_EMPTY__3 = def () :
    return this._EMPTY_2

  Companion_16.$metadata$ = {
    simpleName: 'Companion',
    kind: 'object',
    interfaces: []

   Companion_instance_15
  def Companion_getInstance_15() :
    if (Companion_instance_15 == null)
      new Companion_16()
    return Companion_instance_15

  def LongRange(start, endInclusive) :
    Companion_getInstance_15()
    LongProgression.call(this, start, endInclusive, new Long(1, 0))

  LongRange.prototype._get_start__6 = def () :
    return this._get_first__8()

  LongRange.prototype._get_endInclusive__6 = def () :
    return this._get_last__10()

  LongRange.prototype.contains_19 = def (value) :
    return this._get_first__8().compareTo_56(value) <= 0 ? value.compareTo_56(this._get_last__10()) <= 0 : false

  LongRange.prototype.contains_22 = def (value) :
    return this.contains_19(value instanceof Long ? value : THROW_CCE())

  LongRange.prototype.isEmpty_29 = def () :
    return this._get_first__8().compareTo_56(this._get_last__10()) > 0

  LongRange.prototype.equals = def (other) :
     tmp
    if (other instanceof LongRange) :
      tmp = (this.isEmpty_29() ? other.isEmpty_29() : false) ? true : this._get_first__8().equals(other._get_first__8()) ? this._get_last__10().equals(other._get_last__10()) : false
     else :
      :
        tmp = false


    return tmp

  LongRange.prototype.hashCode = def () :
    return this.isEmpty_29() ? -1 : numberToLong(31).times_32(this._get_first__8().xor(this._get_first__8().ushr_0(32))).plus_38(this._get_last__10().xor(this._get_last__10().ushr_0(32))).toInt_6()

  LongRange.prototype.toString = def () :
    return '' + this._get_first__8() + '..' + this._get_last__10()

  LongRange.$metadata$ = {
    simpleName: 'LongRange',
    kind: 'class',
    interfaces: [ClosedRange]

  def Companion_17() :
    Companion_instance_16 = this
    this._EMPTY_3 = new CharRange(new Char(1), new Char(0))

  Companion_17.prototype._get_EMPTY__3 = def () :
    return this._EMPTY_3

  Companion_17.$metadata$ = {
    simpleName: 'Companion',
    kind: 'object',
    interfaces: []

   Companion_instance_16
  def Companion_getInstance_16() :
    if (Companion_instance_16 == null)
      new Companion_17()
    return Companion_instance_16

  def CharRange(start, endInclusive) :
    Companion_getInstance_16()
    CharProgression.call(this, start, endInclusive, 1)

  CharRange.prototype._get_start__6 = def () :
    return this._get_first__8()

  CharRange.prototype._get_endInclusive__6 = def () :
    return this._get_last__10()

  CharRange.prototype.contains_21 = def (value) :
    return this._get_first__8().compareTo_17(value) <= 0 ? value.compareTo_17(this._get_last__10()) <= 0 : false

  CharRange.prototype.contains_22 = def (value) :
    return this.contains_21(value instanceof Char ? value : THROW_CCE())

  CharRange.prototype.isEmpty_29 = def () :
    return this._get_first__8().compareTo_17(this._get_last__10()) > 0

  CharRange.prototype.equals = def (other) :
     tmp
    if (other instanceof CharRange) :
      tmp = (this.isEmpty_29() ? other.isEmpty_29() : false) ? true : this._get_first__8().equals(other._get_first__8()) ? this._get_last__10().equals(other._get_last__10()) : false
     else :
      :
        tmp = false


    return tmp

  CharRange.prototype.hashCode = def () :
    return this.isEmpty_29() ? -1 : imul(31, this._get_first__8().toInt_6()) + this._get_last__10().toInt_6() | 0

  CharRange.prototype.toString = def () :
    return '' + this._get_first__8() + '..' + this._get_last__10()

  CharRange.$metadata$ = {
    simpleName: 'CharRange',
    kind: 'class',
    interfaces: [ClosedRange]

  def Unit() :
    Unit_instance = this

  Unit.prototype.toString = def () :
    return 'kotlin.Unit'

  Unit.$metadata$ = {
    simpleName: 'Unit',
    kind: 'object',
    interfaces: []

   Unit_instance
  def Unit_getInstance() :
    if (Unit_instance == null)
      new Unit()
    return Unit_instance

  def Target(allowedTargets) :
    this._allowedTargets = allowedTargets

  Target.prototype._get_allowedTargets_ = def () :
    return this._allowedTargets

  Target.$metadata$ = {
    simpleName: 'Target',
    kind: 'class',
    interfaces: [Annotation]

   AnnotationTarget_CLASS_instance
   AnnotationTarget_ANNOTATION_CLASS_instance
   AnnotationTarget_TYPE_PARAMETER_instance
   AnnotationTarget_PROPERTY_instance
   AnnotationTarget_FIELD_instance
   AnnotationTarget_LOCAL_VARIABLE_instance
   AnnotationTarget_VALUE_PARAMETER_instance
   AnnotationTarget_CONSTRUCTOR_instance
   AnnotationTarget_FUNCTION_instance
   AnnotationTarget_PROPERTY_GETTER_instance
   AnnotationTarget_PROPERTY_SETTER_instance
   AnnotationTarget_TYPE_instance
   AnnotationTarget_EXPRESSION_instance
   AnnotationTarget_FILE_instance
   AnnotationTarget_TYPEALIAS_instance
  def values_6() :
    return [AnnotationTarget_CLASS_getInstance(), AnnotationTarget_ANNOTATION_CLASS_getInstance(), AnnotationTarget_TYPE_PARAMETER_getInstance(), AnnotationTarget_PROPERTY_getInstance(), AnnotationTarget_FIELD_getInstance(), AnnotationTarget_LOCAL_VARIABLE_getInstance(), AnnotationTarget_VALUE_PARAMETER_getInstance(), AnnotationTarget_CONSTRUCTOR_getInstance(), AnnotationTarget_FUNCTION_getInstance(), AnnotationTarget_PROPERTY_GETTER_getInstance(), AnnotationTarget_PROPERTY_SETTER_getInstance(), AnnotationTarget_TYPE_getInstance(), AnnotationTarget_EXPRESSION_getInstance(), AnnotationTarget_FILE_getInstance(), AnnotationTarget_TYPEALIAS_getInstance()]

  def valueOf_6(value) :
    switch (value) :
      case 'CLASS':
        return AnnotationTarget_CLASS_getInstance();
      case 'ANNOTATION_CLASS':
        return AnnotationTarget_ANNOTATION_CLASS_getInstance();
      case 'TYPE_PARAMETER':
        return AnnotationTarget_TYPE_PARAMETER_getInstance();
      case 'PROPERTY':
        return AnnotationTarget_PROPERTY_getInstance();
      case 'FIELD':
        return AnnotationTarget_FIELD_getInstance();
      case 'LOCAL_VARIABLE':
        return AnnotationTarget_LOCAL_VARIABLE_getInstance();
      case 'VALUE_PARAMETER':
        return AnnotationTarget_VALUE_PARAMETER_getInstance();
      case 'CONSTRUCTOR':
        return AnnotationTarget_CONSTRUCTOR_getInstance();
      case 'FUNCTION':
        return AnnotationTarget_FUNCTION_getInstance();
      case 'PROPERTY_GETTER':
        return AnnotationTarget_PROPERTY_GETTER_getInstance();
      case 'PROPERTY_SETTER':
        return AnnotationTarget_PROPERTY_SETTER_getInstance();
      case 'TYPE':
        return AnnotationTarget_TYPE_getInstance();
      case 'EXPRESSION':
        return AnnotationTarget_EXPRESSION_getInstance();
      case 'FILE':
        return AnnotationTarget_FILE_getInstance();
      case 'TYPEALIAS':
        return AnnotationTarget_TYPEALIAS_getInstance();
      default:return THROW_ISE();


   AnnotationTarget_entriesInitialized
  def AnnotationTarget_initEntries() :
    if (AnnotationTarget_entriesInitialized)
      return Unit_getInstance()
    AnnotationTarget_entriesInitialized = true
    AnnotationTarget_CLASS_instance = new AnnotationTarget('CLASS', 0)
    AnnotationTarget_ANNOTATION_CLASS_instance = new AnnotationTarget('ANNOTATION_CLASS', 1)
    AnnotationTarget_TYPE_PARAMETER_instance = new AnnotationTarget('TYPE_PARAMETER', 2)
    AnnotationTarget_PROPERTY_instance = new AnnotationTarget('PROPERTY', 3)
    AnnotationTarget_FIELD_instance = new AnnotationTarget('FIELD', 4)
    AnnotationTarget_LOCAL_VARIABLE_instance = new AnnotationTarget('LOCAL_VARIABLE', 5)
    AnnotationTarget_VALUE_PARAMETER_instance = new AnnotationTarget('VALUE_PARAMETER', 6)
    AnnotationTarget_CONSTRUCTOR_instance = new AnnotationTarget('CONSTRUCTOR', 7)
    AnnotationTarget_FUNCTION_instance = new AnnotationTarget('FUNCTION', 8)
    AnnotationTarget_PROPERTY_GETTER_instance = new AnnotationTarget('PROPERTY_GETTER', 9)
    AnnotationTarget_PROPERTY_SETTER_instance = new AnnotationTarget('PROPERTY_SETTER', 10)
    AnnotationTarget_TYPE_instance = new AnnotationTarget('TYPE', 11)
    AnnotationTarget_EXPRESSION_instance = new AnnotationTarget('EXPRESSION', 12)
    AnnotationTarget_FILE_instance = new AnnotationTarget('FILE', 13)
    AnnotationTarget_TYPEALIAS_instance = new AnnotationTarget('TYPEALIAS', 14)

  def AnnotationTarget(name, ordinal) :
    Enum.call(this, name, ordinal)

  AnnotationTarget.$metadata$ = {
    simpleName: 'AnnotationTarget',
    kind: 'class',
    interfaces: []

  def MustBeDocumented() :

  MustBeDocumented.$metadata$ = {
    simpleName: 'MustBeDocumented',
    kind: 'class',
    interfaces: [Annotation]

  def Retention_init_$Init$(value, $mask0, $marker, $this) :
    if (!(($mask0 & 1) === 0))
      value = AnnotationRetention_RUNTIME_getInstance()
    Retention.call($this, value)
    return $this

  def Retention_init_$Create$(value, $mask0, $marker) :
    return Retention_init_$Init$(value, $mask0, $marker, Object.create(Retention.prototype))

  def Retention(value) :
    this._value_0 = value

  Retention.prototype._get_value__1 = def () :
    return this._value_0

  Retention.$metadata$ = {
    simpleName: 'Retention',
    kind: 'class',
    interfaces: [Annotation]

   AnnotationRetention_SOURCE_instance
   AnnotationRetention_BINARY_instance
   AnnotationRetention_RUNTIME_instance
  def values_7() :
    return [AnnotationRetention_SOURCE_getInstance(), AnnotationRetention_BINARY_getInstance(), AnnotationRetention_RUNTIME_getInstance()]

  def valueOf_7(value) :
    switch (value) :
      case 'SOURCE':
        return AnnotationRetention_SOURCE_getInstance();
      case 'BINARY':
        return AnnotationRetention_BINARY_getInstance();
      case 'RUNTIME':
        return AnnotationRetention_RUNTIME_getInstance();
      default:return THROW_ISE();


   AnnotationRetention_entriesInitialized
  def AnnotationRetention_initEntries() :
    if (AnnotationRetention_entriesInitialized)
      return Unit_getInstance()
    AnnotationRetention_entriesInitialized = true
    AnnotationRetention_SOURCE_instance = new AnnotationRetention('SOURCE', 0)
    AnnotationRetention_BINARY_instance = new AnnotationRetention('BINARY', 1)
    AnnotationRetention_RUNTIME_instance = new AnnotationRetention('RUNTIME', 2)

  def AnnotationRetention(name, ordinal) :
    Enum.call(this, name, ordinal)

  AnnotationRetention.$metadata$ = {
    simpleName: 'AnnotationRetention',
    kind: 'class',
    interfaces: []

  def Repeatable() :

  Repeatable.$metadata$ = {
    simpleName: 'Repeatable',
    kind: 'class',
    interfaces: [Annotation]

  def AnnotationTarget_CLASS_getInstance() :
    AnnotationTarget_initEntries()
    return AnnotationTarget_CLASS_instance

  def AnnotationTarget_ANNOTATION_CLASS_getInstance() :
    AnnotationTarget_initEntries()
    return AnnotationTarget_ANNOTATION_CLASS_instance

  def AnnotationTarget_TYPE_PARAMETER_getInstance() :
    AnnotationTarget_initEntries()
    return AnnotationTarget_TYPE_PARAMETER_instance

  def AnnotationTarget_PROPERTY_getInstance() :
    AnnotationTarget_initEntries()
    return AnnotationTarget_PROPERTY_instance

  def AnnotationTarget_FIELD_getInstance() :
    AnnotationTarget_initEntries()
    return AnnotationTarget_FIELD_instance

  def AnnotationTarget_LOCAL_VARIABLE_getInstance() :
    AnnotationTarget_initEntries()
    return AnnotationTarget_LOCAL_VARIABLE_instance

  def AnnotationTarget_VALUE_PARAMETER_getInstance() :
    AnnotationTarget_initEntries()
    return AnnotationTarget_VALUE_PARAMETER_instance

  def AnnotationTarget_CONSTRUCTOR_getInstance() :
    AnnotationTarget_initEntries()
    return AnnotationTarget_CONSTRUCTOR_instance

  def AnnotationTarget_FUNCTION_getInstance() :
    AnnotationTarget_initEntries()
    return AnnotationTarget_FUNCTION_instance

  def AnnotationTarget_PROPERTY_GETTER_getInstance() :
    AnnotationTarget_initEntries()
    return AnnotationTarget_PROPERTY_GETTER_instance

  def AnnotationTarget_PROPERTY_SETTER_getInstance() :
    AnnotationTarget_initEntries()
    return AnnotationTarget_PROPERTY_SETTER_instance

  def AnnotationTarget_TYPE_getInstance() :
    AnnotationTarget_initEntries()
    return AnnotationTarget_TYPE_instance

  def AnnotationTarget_EXPRESSION_getInstance() :
    AnnotationTarget_initEntries()
    return AnnotationTarget_EXPRESSION_instance

  def AnnotationTarget_FILE_getInstance() :
    AnnotationTarget_initEntries()
    return AnnotationTarget_FILE_instance

  def AnnotationTarget_TYPEALIAS_getInstance() :
    AnnotationTarget_initEntries()
    return AnnotationTarget_TYPEALIAS_instance

  def AnnotationRetention_SOURCE_getInstance() :
    AnnotationRetention_initEntries()
    return AnnotationRetention_SOURCE_instance

  def AnnotationRetention_BINARY_getInstance() :
    AnnotationRetention_initEntries()
    return AnnotationRetention_BINARY_instance

  def AnnotationRetention_RUNTIME_getInstance() :
    AnnotationRetention_initEntries()
    return AnnotationRetention_RUNTIME_instance

  def getProgressionLastElement_1(start, end, step) :
     tmp
    if (step > 0) :
      tmp = start >= end ? end : end - differenceModulo_1(end, start, step) | 0
     else if (step < 0) :
      tmp = start <= end ? end : end + differenceModulo_1(start, end, -step | 0) | 0
     else :
      throw IllegalArgumentException_init_$Create$_0('Step is zero.')

    return tmp

  def getProgressionLastElement_2(start, end, step) :
     tmp
    if (step.compareTo_56(new Long(0, 0)) > 0) :
      tmp = start.compareTo_56(end) >= 0 ? end : end.minus_34(differenceModulo_2(end, start, step))
     else if (step.compareTo_56(new Long(0, 0)) < 0) :
      tmp = start.compareTo_56(end) <= 0 ? end : end.plus_38(differenceModulo_2(start, end, step.unaryMinus_4()))
     else :
      throw IllegalArgumentException_init_$Create$_0('Step is zero.')

    return tmp

  def differenceModulo_1(a, b, c) :
    return mod(mod(a, c) - mod(b, c) | 0, c)

  def differenceModulo_2(a, b, c) :
    return mod_0(mod_0(a, c).minus_34(mod_0(b, c)), c)

  def mod(a, b) :
     mod_1 = a % b
    return mod_1 >= 0 ? mod_1 : mod_1 + b | 0

  def mod_0(a, b) :
     mod_1 = a.rem_32(b)
    return mod_1.compareTo_56(new Long(0, 0)) >= 0 ? mod_1 : mod_1.plus_38(b)

  def ByteCompanionObject_0() :
    ByteCompanionObject_instance = this
    this._MIN_VALUE_3 = -128
    this._MAX_VALUE_3 = 127
    this._SIZE_BYTES_3 = 1
    this._SIZE_BITS_3 = 8

  ByteCompanionObject_0.prototype._get_MIN_VALUE__9 = def () :
    return this._MIN_VALUE_3

  ByteCompanionObject_0.prototype._get_MAX_VALUE__9 = def () :
    return this._MAX_VALUE_3

  ByteCompanionObject_0.prototype._get_SIZE_BYTES__9 = def () :
    return this._SIZE_BYTES_3

  ByteCompanionObject_0.prototype._get_SIZE_BITS__9 = def () :
    return this._SIZE_BITS_3

  ByteCompanionObject_0.$metadata$ = {
    simpleName: 'ByteCompanionObject',
    kind: 'object',
    interfaces: []

  Object.defineProperty(ByteCompanionObject_0.prototype, 'MIN_VALUE', {
    configurable: true,
    get: ByteCompanionObject_0.prototype._get_MIN_VALUE__9
  )
  Object.defineProperty(ByteCompanionObject_0.prototype, 'MAX_VALUE', {
    configurable: true,
    get: ByteCompanionObject_0.prototype._get_MAX_VALUE__9
  )
  Object.defineProperty(ByteCompanionObject_0.prototype, 'SIZE_BYTES', {
    configurable: true,
    get: ByteCompanionObject_0.prototype._get_SIZE_BYTES__9
  )
  Object.defineProperty(ByteCompanionObject_0.prototype, 'SIZE_BITS', {
    configurable: true,
    get: ByteCompanionObject_0.prototype._get_SIZE_BITS__9
  )
   ByteCompanionObject_instance
  def ByteCompanionObject_getInstance() :
    if (ByteCompanionObject_instance == null)
      new ByteCompanionObject_0()
    return ByteCompanionObject_instance

  def ShortCompanionObject_0() :
    ShortCompanionObject_instance = this
    this._MIN_VALUE_4 = -32768
    this._MAX_VALUE_4 = 32767
    this._SIZE_BYTES_4 = 2
    this._SIZE_BITS_4 = 16

  ShortCompanionObject_0.prototype._get_MIN_VALUE__9 = def () :
    return this._MIN_VALUE_4

  ShortCompanionObject_0.prototype._get_MAX_VALUE__9 = def () :
    return this._MAX_VALUE_4

  ShortCompanionObject_0.prototype._get_SIZE_BYTES__9 = def () :
    return this._SIZE_BYTES_4

  ShortCompanionObject_0.prototype._get_SIZE_BITS__9 = def () :
    return this._SIZE_BITS_4

  ShortCompanionObject_0.$metadata$ = {
    simpleName: 'ShortCompanionObject',
    kind: 'object',
    interfaces: []

  Object.defineProperty(ShortCompanionObject_0.prototype, 'MIN_VALUE', {
    configurable: true,
    get: ShortCompanionObject_0.prototype._get_MIN_VALUE__9
  )
  Object.defineProperty(ShortCompanionObject_0.prototype, 'MAX_VALUE', {
    configurable: true,
    get: ShortCompanionObject_0.prototype._get_MAX_VALUE__9
  )
  Object.defineProperty(ShortCompanionObject_0.prototype, 'SIZE_BYTES', {
    configurable: true,
    get: ShortCompanionObject_0.prototype._get_SIZE_BYTES__9
  )
  Object.defineProperty(ShortCompanionObject_0.prototype, 'SIZE_BITS', {
    configurable: true,
    get: ShortCompanionObject_0.prototype._get_SIZE_BITS__9
  )
   ShortCompanionObject_instance
  def ShortCompanionObject_getInstance() :
    if (ShortCompanionObject_instance == null)
      new ShortCompanionObject_0()
    return ShortCompanionObject_instance

  def IntCompanionObject_0() :
    IntCompanionObject_instance = this
    this._MIN_VALUE_5 = -2147483648
    this._MAX_VALUE_5 = 2147483647
    this._SIZE_BYTES_5 = 4
    this._SIZE_BITS_5 = 32

  IntCompanionObject_0.prototype._get_MIN_VALUE__9 = def () :
    return this._MIN_VALUE_5

  IntCompanionObject_0.prototype._get_MAX_VALUE__9 = def () :
    return this._MAX_VALUE_5

  IntCompanionObject_0.prototype._get_SIZE_BYTES__9 = def () :
    return this._SIZE_BYTES_5

  IntCompanionObject_0.prototype._get_SIZE_BITS__9 = def () :
    return this._SIZE_BITS_5

  IntCompanionObject_0.$metadata$ = {
    simpleName: 'IntCompanionObject',
    kind: 'object',
    interfaces: []

  Object.defineProperty(IntCompanionObject_0.prototype, 'MIN_VALUE', {
    configurable: true,
    get: IntCompanionObject_0.prototype._get_MIN_VALUE__9
  )
  Object.defineProperty(IntCompanionObject_0.prototype, 'MAX_VALUE', {
    configurable: true,
    get: IntCompanionObject_0.prototype._get_MAX_VALUE__9
  )
  Object.defineProperty(IntCompanionObject_0.prototype, 'SIZE_BYTES', {
    configurable: true,
    get: IntCompanionObject_0.prototype._get_SIZE_BYTES__9
  )
  Object.defineProperty(IntCompanionObject_0.prototype, 'SIZE_BITS', {
    configurable: true,
    get: IntCompanionObject_0.prototype._get_SIZE_BITS__9
  )
   IntCompanionObject_instance
  def IntCompanionObject_getInstance() :
    if (IntCompanionObject_instance == null)
      new IntCompanionObject_0()
    return IntCompanionObject_instance

  def FloatCompanionObject_0() :
    FloatCompanionObject_instance = this
    this._MIN_VALUE_6 = 1.4E-45
    this._MAX_VALUE_6 = 3.4028235E38
    this._POSITIVE_INFINITY = Infinity
    this._NEGATIVE_INFINITY = -Infinity
    this._NaN = NaN
    this._SIZE_BYTES_6 = 4
    this._SIZE_BITS_6 = 32

  FloatCompanionObject_0.prototype._get_MIN_VALUE__9 = def () :
    return this._MIN_VALUE_6

  FloatCompanionObject_0.prototype._get_MAX_VALUE__9 = def () :
    return this._MAX_VALUE_6

  FloatCompanionObject_0.prototype._get_POSITIVE_INFINITY__0 = def () :
    return this._POSITIVE_INFINITY

  FloatCompanionObject_0.prototype._get_NEGATIVE_INFINITY__0 = def () :
    return this._NEGATIVE_INFINITY

  FloatCompanionObject_0.prototype._get_NaN__0 = def () :
    return this._NaN

  FloatCompanionObject_0.prototype._get_SIZE_BYTES__9 = def () :
    return this._SIZE_BYTES_6

  FloatCompanionObject_0.prototype._get_SIZE_BITS__9 = def () :
    return this._SIZE_BITS_6

  FloatCompanionObject_0.$metadata$ = {
    simpleName: 'FloatCompanionObject',
    kind: 'object',
    interfaces: []

  Object.defineProperty(FloatCompanionObject_0.prototype, 'MIN_VALUE', {
    configurable: true,
    get: FloatCompanionObject_0.prototype._get_MIN_VALUE__9
  )
  Object.defineProperty(FloatCompanionObject_0.prototype, 'MAX_VALUE', {
    configurable: true,
    get: FloatCompanionObject_0.prototype._get_MAX_VALUE__9
  )
  Object.defineProperty(FloatCompanionObject_0.prototype, 'POSITIVE_INFINITY', {
    configurable: true,
    get: FloatCompanionObject_0.prototype._get_POSITIVE_INFINITY__0
  )
  Object.defineProperty(FloatCompanionObject_0.prototype, 'NEGATIVE_INFINITY', {
    configurable: true,
    get: FloatCompanionObject_0.prototype._get_NEGATIVE_INFINITY__0
  )
  Object.defineProperty(FloatCompanionObject_0.prototype, 'NaN', {
    configurable: true,
    get: FloatCompanionObject_0.prototype._get_NaN__0
  )
  Object.defineProperty(FloatCompanionObject_0.prototype, 'SIZE_BYTES', {
    configurable: true,
    get: FloatCompanionObject_0.prototype._get_SIZE_BYTES__9
  )
  Object.defineProperty(FloatCompanionObject_0.prototype, 'SIZE_BITS', {
    configurable: true,
    get: FloatCompanionObject_0.prototype._get_SIZE_BITS__9
  )
   FloatCompanionObject_instance
  def FloatCompanionObject_getInstance() :
    if (FloatCompanionObject_instance == null)
      new FloatCompanionObject_0()
    return FloatCompanionObject_instance

  def DoubleCompanionObject_0() :
    DoubleCompanionObject_instance = this
    this._MIN_VALUE_7 = 4.9E-324
    this._MAX_VALUE_7 = 1.7976931348623157E308
    this._POSITIVE_INFINITY_0 = Infinity
    this._NEGATIVE_INFINITY_0 = -Infinity
    this._NaN_0 = NaN
    this._SIZE_BYTES_7 = 8
    this._SIZE_BITS_7 = 64

  DoubleCompanionObject_0.prototype._get_MIN_VALUE__9 = def () :
    return this._MIN_VALUE_7

  DoubleCompanionObject_0.prototype._get_MAX_VALUE__9 = def () :
    return this._MAX_VALUE_7

  DoubleCompanionObject_0.prototype._get_POSITIVE_INFINITY__0 = def () :
    return this._POSITIVE_INFINITY_0

  DoubleCompanionObject_0.prototype._get_NEGATIVE_INFINITY__0 = def () :
    return this._NEGATIVE_INFINITY_0

  DoubleCompanionObject_0.prototype._get_NaN__0 = def () :
    return this._NaN_0

  DoubleCompanionObject_0.prototype._get_SIZE_BYTES__9 = def () :
    return this._SIZE_BYTES_7

  DoubleCompanionObject_0.prototype._get_SIZE_BITS__9 = def () :
    return this._SIZE_BITS_7

  DoubleCompanionObject_0.$metadata$ = {
    simpleName: 'DoubleCompanionObject',
    kind: 'object',
    interfaces: []

  Object.defineProperty(DoubleCompanionObject_0.prototype, 'MIN_VALUE', {
    configurable: true,
    get: DoubleCompanionObject_0.prototype._get_MIN_VALUE__9
  )
  Object.defineProperty(DoubleCompanionObject_0.prototype, 'MAX_VALUE', {
    configurable: true,
    get: DoubleCompanionObject_0.prototype._get_MAX_VALUE__9
  )
  Object.defineProperty(DoubleCompanionObject_0.prototype, 'POSITIVE_INFINITY', {
    configurable: true,
    get: DoubleCompanionObject_0.prototype._get_POSITIVE_INFINITY__0
  )
  Object.defineProperty(DoubleCompanionObject_0.prototype, 'NEGATIVE_INFINITY', {
    configurable: true,
    get: DoubleCompanionObject_0.prototype._get_NEGATIVE_INFINITY__0
  )
  Object.defineProperty(DoubleCompanionObject_0.prototype, 'NaN', {
    configurable: true,
    get: DoubleCompanionObject_0.prototype._get_NaN__0
  )
  Object.defineProperty(DoubleCompanionObject_0.prototype, 'SIZE_BYTES', {
    configurable: true,
    get: DoubleCompanionObject_0.prototype._get_SIZE_BYTES__9
  )
  Object.defineProperty(DoubleCompanionObject_0.prototype, 'SIZE_BITS', {
    configurable: true,
    get: DoubleCompanionObject_0.prototype._get_SIZE_BITS__9
  )
   DoubleCompanionObject_instance
  def DoubleCompanionObject_getInstance() :
    if (DoubleCompanionObject_instance == null)
      new DoubleCompanionObject_0()
    return DoubleCompanionObject_instance

  def StringCompanionObject() :
    StringCompanionObject_instance = this

  StringCompanionObject.$metadata$ = {
    simpleName: 'StringCompanionObject',
    kind: 'object',
    interfaces: []

   StringCompanionObject_instance
  def StringCompanionObject_getInstance() :
    if (StringCompanionObject_instance == null)
      new StringCompanionObject()
    return StringCompanionObject_instance

  def BooleanCompanionObject() :
    BooleanCompanionObject_instance = this

  BooleanCompanionObject.$metadata$ = {
    simpleName: 'BooleanCompanionObject',
    kind: 'object',
    interfaces: []

   BooleanCompanionObject_instance
  def BooleanCompanionObject_getInstance() :
    if (BooleanCompanionObject_instance == null)
      new BooleanCompanionObject()
    return BooleanCompanionObject_instance

  def Comparator() :

  Comparator.$metadata$ = {
    simpleName: 'Comparator',
    kind: 'interface',
    interfaces: []

  def JsName(name) :
    this._name_0 = name

  JsName.prototype._get_name__22 = def () :
    return this._name_0

  JsName.$metadata$ = {
    simpleName: 'JsName',
    kind: 'class',
    interfaces: [Annotation]

  def toTypedArray(_this_) :
    return copyToArray_0(_this_)

  def copyToArray_0(collection) :
     tmp
    if (collection.toArray !== undefined) :
       tmp0_unsafeCast_0 = collection.toArray()
      tmp = tmp0_unsafeCast_0
     else :
      :
         tmp1_unsafeCast_0 = copyToArrayImpl_0(collection)
        tmp = tmp1_unsafeCast_0


    return tmp

  def copyToArrayImpl_0(collection) :
     array = []
     iterator = collection.iterator_38()
    while (iterator.hasNext_37()) :
      array.push(iterator.next_41())

    return array

  def copyToArrayImpl_1(collection, array) :
    if (array.length < collection._get_size__18()) :
       tmp0_unsafeCast_0 = copyToArrayImpl_0(collection)
      return tmp0_unsafeCast_0
     iterator = collection.iterator_38()
     index = 0
    while (iterator.hasNext_37()) :
       tmp0 = index
      index = tmp0 + 1 | 0
       tmp1_unsafeCast_0 = iterator.next_41()
      array[tmp0] = tmp1_unsafeCast_0

    if (index < array.length) :
       tmp = index
       tmp2_unsafeCast_0 = null
      array[tmp] = tmp2_unsafeCast_0
    return array

  def _no_name_provided__4($elements) :
    this._$elements_0 = $elements

  _no_name_provided__4.prototype.invoke_13 = def (it) :
    return this._$elements_0.contains_32(it)

  _no_name_provided__4.prototype.invoke_66 = def (p1) :
    return this.invoke_13((p1 == null ? true : isObject(p1)) ? p1 : THROW_CCE())

  _no_name_provided__4.$metadata$ = {
    kind: 'class',
    interfaces: []

  def _no_name_provided__5($elements) :
    this._$elements_1 = $elements

  _no_name_provided__5.prototype.invoke_13 = def (it) :
    return !this._$elements_1.contains_32(it)

  _no_name_provided__5.prototype.invoke_66 = def (p1) :
    return this.invoke_13((p1 == null ? true : isObject(p1)) ? p1 : THROW_CCE())

  _no_name_provided__5.$metadata$ = {
    kind: 'class',
    interfaces: []

  def AbstractMutableCollection() :
    AbstractCollection.call(this)

  AbstractMutableCollection.prototype.remove_9 = def (element) :
    this.checkIsMutable_2()
     iterator = this.iterator_38()
    while (iterator.hasNext_37()) :
      if (equals(iterator.next_41(), element)) :
        iterator.remove_3()
        return true

    return false

  AbstractMutableCollection.prototype.addAll_8 = def (elements) :
    this.checkIsMutable_2()
     modified = false
     tmp0_iterator = elements.iterator_38()
    while (tmp0_iterator.hasNext_37()) :
       element = tmp0_iterator.next_41()
      if (this.add_11(element))
        modified = true

    return modified

  AbstractMutableCollection.prototype.removeAll_5 = def (elements) :
    this.checkIsMutable_2()
     tmp = isInterface(this, MutableIterable) ? this : THROW_CCE()
    return removeAll_0(tmp, _no_name_provided_$factory_3(elements))

  AbstractMutableCollection.prototype.retainAll_5 = def (elements) :
    this.checkIsMutable_2()
     tmp = isInterface(this, MutableIterable) ? this : THROW_CCE()
    return removeAll_0(tmp, _no_name_provided_$factory_4(elements))

  AbstractMutableCollection.prototype.clear_7 = def () :
    this.checkIsMutable_2()
     iterator = this.iterator_38()
    while (iterator.hasNext_37()) :
      iterator.next_41()
      Unit_getInstance()
      iterator.remove_3()


  AbstractMutableCollection.prototype.toJSON = def () :
    return this.toArray()

  AbstractMutableCollection.prototype.checkIsMutable_2 = def () :

  AbstractMutableCollection.$metadata$ = {
    simpleName: 'AbstractMutableCollection',
    kind: 'class',
    interfaces: [MutableCollection]

  def _no_name_provided_$factory_3($elements) :
     i = new _no_name_provided__4($elements)
    return def (p1) :
      return i.invoke_13(p1)


  def _no_name_provided_$factory_4($elements) :
     i = new _no_name_provided__5($elements)
    return def (p1) :
      return i.invoke_13(p1)


  def _get_list__0($this) :
    return $this._list_0

  def _get_fromIndex__0($this) :
    return $this._fromIndex_0

  def _set__size__0($this, _set___) :
    $this.__size_0 = _set___

  def _get__size__0($this) :
    return $this.__size_0

  def IteratorImpl_0($outer) :
    this._$this_1 = $outer
    this._index_4 = 0
    this._last_4 = -1

  IteratorImpl_0.prototype._set_index__11 = def (_set___) :
    this._index_4 = _set___

  IteratorImpl_0.prototype._get_index__11 = def () :
    return this._index_4

  IteratorImpl_0.prototype._set_last__0 = def (_set___) :
    this._last_4 = _set___

  IteratorImpl_0.prototype._get_last__10 = def () :
    return this._last_4

  IteratorImpl_0.prototype.hasNext_37 = def () :
    return this._index_4 < this._$this_1._get_size__18()

  IteratorImpl_0.prototype.next_41 = def () :
    if (!this.hasNext_37())
      throw NoSuchElementException_init_$Create$()
     tmp = this
     tmp0_this = this
     tmp1 = tmp0_this._index_4
    tmp0_this._index_4 = tmp1 + 1 | 0
    tmp._last_4 = tmp1
    return this._$this_1.get_31(this._last_4)

  IteratorImpl_0.prototype.remove_3 = def () :
     tmp0_check_0 = !(this._last_4 === -1)
    if (!tmp0_check_0) :
       message_1 = 'Call next() or previous() before removing element from the iterator.'
      throw IllegalStateException_init_$Create$_0(toString_0(message_1))
    this._$this_1.removeAt_2(this._last_4)
    Unit_getInstance()
    this._index_4 = this._last_4
    this._last_4 = -1

  IteratorImpl_0.$metadata$ = {
    simpleName: 'IteratorImpl',
    kind: 'class',
    interfaces: [MutableIterator]

  def ListIteratorImpl_0($outer, index) :
    this._$this_2 = $outer
    IteratorImpl_0.call(this, $outer)
    Companion_getInstance().checkPositionIndex(index, this._$this_2._get_size__18())
    this._set_index__11(index)

  ListIteratorImpl_0.prototype.hasPrevious_3 = def () :
    return this._get_index__11() > 0

  ListIteratorImpl_0.prototype.nextIndex_3 = def () :
    return this._get_index__11()

  ListIteratorImpl_0.prototype.previous_3 = def () :
    if (!this.hasPrevious_3())
      throw NoSuchElementException_init_$Create$()
     tmp0_this = this
    tmp0_this._set_index__11(tmp0_this._get_index__11() - 1 | 0)
    this._set_last__0(tmp0_this._get_index__11())
    return this._$this_2.get_31(this._get_last__10())

  ListIteratorImpl_0.prototype.previousIndex_3 = def () :
    return this._get_index__11() - 1 | 0

  ListIteratorImpl_0.prototype.add_1 = def (element) :
    this._$this_2.add_12(this._get_index__11(), element)
     tmp0_this = this
     tmp1 = tmp0_this._get_index__11()
    tmp0_this._set_index__11(tmp1 + 1 | 0)
    Unit_getInstance()
    this._set_last__0(-1)

  ListIteratorImpl_0.prototype.add_2 = def (element) :
    return this.add_1((element == null ? true : isObject(element)) ? element : THROW_CCE())

  ListIteratorImpl_0.prototype.set_0 = def (element) :
     tmp0_check_0 = !(this._get_last__10() === -1)
    if (!tmp0_check_0) :
       message_1 = 'Call next() or previous() before updating element value with the iterator.'
      throw IllegalStateException_init_$Create$_0(toString_0(message_1))
    this._$this_2.set_9(this._get_last__10(), element)
    Unit_getInstance()

  ListIteratorImpl_0.prototype.set_1 = def (element) :
    return this.set_0((element == null ? true : isObject(element)) ? element : THROW_CCE())

  ListIteratorImpl_0.$metadata$ = {
    simpleName: 'ListIteratorImpl',
    kind: 'class',
    interfaces: [MutableListIterator]

  def SubList_0(list, fromIndex, toIndex) :
    AbstractMutableList.call(this)
    this._list_0 = list
    this._fromIndex_0 = fromIndex
    this.__size_0 = 0
    Companion_getInstance().checkRangeIndexes(this._fromIndex_0, toIndex, this._list_0._get_size__18())
    this.__size_0 = toIndex - this._fromIndex_0 | 0

  SubList_0.prototype.add_12 = def (index, element) :
    Companion_getInstance().checkPositionIndex(index, this.__size_0)
    this._list_0.add_12(this._fromIndex_0 + index | 0, element)
     tmp0_this = this
     tmp1 = tmp0_this.__size_0
    tmp0_this.__size_0 = tmp1 + 1 | 0
    Unit_getInstance()

  SubList_0.prototype.get_31 = def (index) :
    Companion_getInstance().checkElementIndex(index, this.__size_0)
    return this._list_0.get_31(this._fromIndex_0 + index | 0)

  SubList_0.prototype.removeAt_2 = def (index) :
    Companion_getInstance().checkElementIndex(index, this.__size_0)
     result = this._list_0.removeAt_2(this._fromIndex_0 + index | 0)
     tmp0_this = this
     tmp1 = tmp0_this.__size_0
    tmp0_this.__size_0 = tmp1 - 1 | 0
    Unit_getInstance()
    return result

  SubList_0.prototype.set_9 = def (index, element) :
    Companion_getInstance().checkElementIndex(index, this.__size_0)
    return this._list_0.set_9(this._fromIndex_0 + index | 0, element)

  SubList_0.prototype._get_size__18 = def () :
    return this.__size_0

  SubList_0.prototype.checkIsMutable_2 = def () :
    return this._list_0.checkIsMutable_2()

  SubList_0.$metadata$ = {
    simpleName: 'SubList',
    kind: 'class',
    interfaces: [RandomAccess]

  def _no_name_provided__6($elements) :
    this._$elements_2 = $elements

  _no_name_provided__6.prototype.invoke_13 = def (it) :
    return this._$elements_2.contains_32(it)

  _no_name_provided__6.prototype.invoke_66 = def (p1) :
    return this.invoke_13((p1 == null ? true : isObject(p1)) ? p1 : THROW_CCE())

  _no_name_provided__6.$metadata$ = {
    kind: 'class',
    interfaces: []

  def _no_name_provided__7($elements) :
    this._$elements_3 = $elements

  _no_name_provided__7.prototype.invoke_13 = def (it) :
    return !this._$elements_3.contains_32(it)

  _no_name_provided__7.prototype.invoke_66 = def (p1) :
    return this.invoke_13((p1 == null ? true : isObject(p1)) ? p1 : THROW_CCE())

  _no_name_provided__7.$metadata$ = {
    kind: 'class',
    interfaces: []

  def AbstractMutableList() :
    AbstractMutableCollection.call(this)
    this._modCount = 0

  AbstractMutableList.prototype._set_modCount__1 = def (_set___) :
    this._modCount = _set___

  AbstractMutableList.prototype._get_modCount__1 = def () :
    return this._modCount

  AbstractMutableList.prototype.add_11 = def (element) :
    this.checkIsMutable_2()
    this.add_12(this._get_size__18(), element)
    return true

  AbstractMutableList.prototype.addAll_9 = def (index, elements) :
    this.checkIsMutable_2()
     _index = index
     changed = false
     tmp0_iterator = elements.iterator_38()
    while (tmp0_iterator.hasNext_37()) :
       e = tmp0_iterator.next_41()
       tmp1 = _index
      _index = tmp1 + 1 | 0
      this.add_12(tmp1, e)
      changed = true

    return changed

  AbstractMutableList.prototype.clear_7 = def () :
    this.checkIsMutable_2()
    this.removeRange_1(0, this._get_size__18())

  AbstractMutableList.prototype.removeAll_5 = def (elements) :
    this.checkIsMutable_2()
    return removeAll(this, _no_name_provided_$factory_5(elements))

  AbstractMutableList.prototype.retainAll_5 = def (elements) :
    this.checkIsMutable_2()
    return removeAll(this, _no_name_provided_$factory_6(elements))

  AbstractMutableList.prototype.iterator_38 = def () :
    return new IteratorImpl_0(this)

  AbstractMutableList.prototype.contains_32 = def (element) :
    return this.indexOf_9(element) >= 0

  AbstractMutableList.prototype.indexOf_9 = def (element) :
     inductionVariable = 0
     last = _get_lastIndex__4(this)
    if (inductionVariable <= last)
      do :
         index = inductionVariable
        inductionVariable = inductionVariable + 1 | 0
        if (equals(this.get_31(index), element)) :
          return index

       while (!(index === last))
    return -1

  AbstractMutableList.prototype.lastIndexOf_9 = def (element) :
     inductionVariable = _get_lastIndex__4(this)
    if (0 <= inductionVariable)
      do :
         index = inductionVariable
        inductionVariable = inductionVariable + -1 | 0
        if (equals(this.get_31(index), element)) :
          return index

       while (0 <= inductionVariable)
    return -1

  AbstractMutableList.prototype.listIterator_13 = def () :
    return this.listIterator_14(0)

  AbstractMutableList.prototype.listIterator_14 = def (index) :
    return new ListIteratorImpl_0(this, index)

  AbstractMutableList.prototype.subList_6 = def (fromIndex, toIndex) :
    return new SubList_0(this, fromIndex, toIndex)

  AbstractMutableList.prototype.removeRange_1 = def (fromIndex, toIndex) :
     iterator = this.listIterator_14(fromIndex)
     tmp0_repeat_0 = toIndex - fromIndex | 0
     inductionVariable = 0
    if (inductionVariable < tmp0_repeat_0)
      do :
         index_2 = inductionVariable
        inductionVariable = inductionVariable + 1 | 0
        iterator.next_41()
        Unit_getInstance()
        iterator.remove_3()

       while (inductionVariable < tmp0_repeat_0)

  AbstractMutableList.prototype.equals = def (other) :
    if (other === this)
      return true
    if (!(!(other == null) ? isInterface(other, List) : false))
      return false;
    else :

    return Companion_getInstance().orderedEquals(this, other)

  AbstractMutableList.prototype.hashCode = def () :
    return Companion_getInstance().orderedHashCode(this)

  AbstractMutableList.$metadata$ = {
    simpleName: 'AbstractMutableList',
    kind: 'class',
    interfaces: [MutableList]

  def _no_name_provided_$factory_5($elements) :
     i = new _no_name_provided__6($elements)
    return def (p1) :
      return i.invoke_13(p1)


  def _no_name_provided_$factory_6($elements) :
     i = new _no_name_provided__7($elements)
    return def (p1) :
      return i.invoke_13(p1)


  def _set_array_($this, _set___) :
    $this._array_3 = _set___

  def _get_array__3($this) :
    return $this._array_3

  def _set_isReadOnly_($this, _set___) :
    $this._isReadOnly = _set___

  def _get_isReadOnly_($this) :
    return $this._isReadOnly

  def ArrayList_init_$Init$($this) :
    ArrayList.call($this, [])
    return $this

  def ArrayList_init_$Create$() :
    return ArrayList_init_$Init$(Object.create(ArrayList.prototype))

  def ArrayList_init_$Init$_0(initialCapacity, $this) :
    ArrayList.call($this, [])
    return $this

  def ArrayList_init_$Create$_0(initialCapacity) :
    return ArrayList_init_$Init$_0(initialCapacity, Object.create(ArrayList.prototype))

  def ArrayList_init_$Init$_1(initialCapacity, $mask0, $marker, $this) :
    if (!(($mask0 & 1) === 0))
      initialCapacity = 0
    ArrayList_init_$Init$_0(initialCapacity, $this)
    return $this

  def ArrayList_init_$Create$_1(initialCapacity, $mask0, $marker) :
    return ArrayList_init_$Init$_1(initialCapacity, $mask0, $marker, Object.create(ArrayList.prototype))

  def ArrayList_init_$Init$_2(elements, $this) :
    ArrayList.call($this, copyToArray_0(elements))
    return $this

  def ArrayList_init_$Create$_2(elements) :
    return ArrayList_init_$Init$_2(elements, Object.create(ArrayList.prototype))

  def rangeCheck($this, index) :
    Companion_getInstance().checkElementIndex(index, $this._get_size__18())
    return index

  def insertionRangeCheck($this, index) :
    Companion_getInstance().checkPositionIndex(index, $this._get_size__18())
    return index

  def ArrayList(array) :
    AbstractMutableList.call(this)
    this._array_3 = array
    this._isReadOnly = false

  ArrayList.prototype.build = def () :
    this.checkIsMutable_2()
    this._isReadOnly = true
    return this

  ArrayList.prototype.trimToSize_0 = def () :

  ArrayList.prototype.ensureCapacity_0 = def (minCapacity) :

  ArrayList.prototype._get_size__18 = def () :
    return this._array_3.length

  ArrayList.prototype.get_31 = def (index) :
     tmp = this._array_3[rangeCheck(this, index)]
    return (tmp == null ? true : isObject(tmp)) ? tmp : THROW_CCE()

  ArrayList.prototype.set_9 = def (index, element) :
    this.checkIsMutable_2()
    rangeCheck(this, index)
    Unit_getInstance()
     tmp0_apply_0 = this._array_3[index]
    this._array_3[index] = element
     tmp = tmp0_apply_0
    return (tmp == null ? true : isObject(tmp)) ? tmp : THROW_CCE()

  ArrayList.prototype.add_11 = def (element) :
    this.checkIsMutable_2()
     tmp0_asDynamic_0 = this._array_3
    tmp0_asDynamic_0.push(element)
     tmp0_this = this
     tmp1 = tmp0_this._get_modCount__1()
    tmp0_this._set_modCount__1(tmp1 + 1 | 0)
    Unit_getInstance()
    return true

  ArrayList.prototype.add_12 = def (index, element) :
    this.checkIsMutable_2()
     tmp0_asDynamic_0 = this._array_3
    tmp0_asDynamic_0.splice(insertionRangeCheck(this, index), 0, element)
     tmp0_this = this
     tmp1 = tmp0_this._get_modCount__1()
    tmp0_this._set_modCount__1(tmp1 + 1 | 0)
    Unit_getInstance()

  ArrayList.prototype.addAll_8 = def (elements) :
    this.checkIsMutable_2()
    if (elements.isEmpty_29())
      return false
     tmp0_this = this
     tmp = tmp0_this
     tmp0_plus_0 = tmp0_this._array_3
     tmp1_plus_0 = copyToArray_0(elements)
    tmp._array_3 = tmp0_plus_0.concat(tmp1_plus_0)
     tmp1_this = this
     tmp2 = tmp1_this._get_modCount__1()
    tmp1_this._set_modCount__1(tmp2 + 1 | 0)
    Unit_getInstance()
    return true

  ArrayList.prototype.addAll_9 = def (index, elements) :
    this.checkIsMutable_2()
    insertionRangeCheck(this, index)
    Unit_getInstance()
    if (index === this._get_size__18())
      return this.addAll_8(elements)
    if (elements.isEmpty_29())
      return false
     tmp0_subject = index
    if (tmp0_subject === this._get_size__18())
      return this.addAll_8(elements);
    else if (tmp0_subject === 0) :
       tmp = this
       tmp0_plus_0 = copyToArray_0(elements)
       tmp1_plus_0 = this._array_3
      tmp._array_3 = tmp0_plus_0.concat(tmp1_plus_0)
     else :
       tmp_0 = this
       tmp2_asDynamic_0 = copyOfRange(this._array_3, 0, index)
      tmp_0._array_3 = tmp2_asDynamic_0.concat(copyToArray_0(elements), copyOfRange(this._array_3, index, this._get_size__18()))

     tmp1_this = this
     tmp2 = tmp1_this._get_modCount__1()
    tmp1_this._set_modCount__1(tmp2 + 1 | 0)
    Unit_getInstance()
    return true

  ArrayList.prototype.removeAt_2 = def (index) :
    this.checkIsMutable_2()
    rangeCheck(this, index)
    Unit_getInstance()
     tmp0_this = this
     tmp1 = tmp0_this._get_modCount__1()
    tmp0_this._set_modCount__1(tmp1 + 1 | 0)
    Unit_getInstance()
     tmp
    if (index === _get_lastIndex__4(this)) :
       tmp0_asDynamic_0 = this._array_3
      tmp = tmp0_asDynamic_0.pop()
     else :
       tmp1_asDynamic_0 = this._array_3
      tmp = tmp1_asDynamic_0.splice(index, 1)[0]

    return tmp

  ArrayList.prototype.remove_9 = def (element) :
    this.checkIsMutable_2()
     inductionVariable = 0
     last = this._array_3.length - 1 | 0
    if (inductionVariable <= last)
      do :
         index = inductionVariable
        inductionVariable = inductionVariable + 1 | 0
        if (equals(this._array_3[index], element)) :
           tmp0_asDynamic_0 = this._array_3
          tmp0_asDynamic_0.splice(index, 1)
           tmp1_this = this
           tmp2 = tmp1_this._get_modCount__1()
          tmp1_this._set_modCount__1(tmp2 + 1 | 0)
          Unit_getInstance()
          return true

       while (inductionVariable <= last)
    return false

  ArrayList.prototype.removeRange_1 = def (fromIndex, toIndex) :
    this.checkIsMutable_2()
     tmp0_this = this
     tmp1 = tmp0_this._get_modCount__1()
    tmp0_this._set_modCount__1(tmp1 + 1 | 0)
    Unit_getInstance()
     tmp0_asDynamic_0 = this._array_3
    tmp0_asDynamic_0.splice(fromIndex, toIndex - fromIndex | 0)

  ArrayList.prototype.clear_7 = def () :
    this.checkIsMutable_2()
     tmp = this
    tmp._array_3 = []
     tmp0_this = this
     tmp1 = tmp0_this._get_modCount__1()
    tmp0_this._set_modCount__1(tmp1 + 1 | 0)
    Unit_getInstance()

  ArrayList.prototype.indexOf_9 = def (element) :
    return indexOf_3(this._array_3, element)

  ArrayList.prototype.lastIndexOf_9 = def (element) :
    return lastIndexOf(this._array_3, element)

  ArrayList.prototype.toString = def () :
    return arrayToString(this._array_3)

  ArrayList.prototype.toArray_6 = def () :
    return [].slice.call(this._array_3)

  ArrayList.prototype.toArray = def () :
    return this.toArray_6()

  ArrayList.prototype.checkIsMutable_2 = def () :
    if (this._isReadOnly)
      throw UnsupportedOperationException_init_$Create$()

  ArrayList.$metadata$ = {
    simpleName: 'ArrayList',
    kind: 'class',
    interfaces: [MutableList, RandomAccess]

  def _set__stableSortingIsSupported_(_set___) :
    _stableSortingIsSupported = _set___

  def _get__stableSortingIsSupported_() :
    return _stableSortingIsSupported

   _stableSortingIsSupported
  def RandomAccess() :

  RandomAccess.$metadata$ = {
    simpleName: 'RandomAccess',
    kind: 'interface',
    interfaces: []

  def _set_output_(_set___) :
    output = _set___

  def _get_output_() :
    return output

   output
  def BaseOutput() :

  BaseOutput.prototype.println_5 = def () :
    this.print_2('\n')

  BaseOutput.prototype.println_6 = def (message) :
    this.print_2(message)
    this.println_5()

  BaseOutput.prototype.flush_2 = def () :

  BaseOutput.$metadata$ = {
    simpleName: 'BaseOutput',
    kind: 'class',
    interfaces: []

  def NodeJsOutput_0(outputStream) :
    BaseOutput.call(this)
    this._outputStream = outputStream

  NodeJsOutput_0.prototype._get_outputStream_ = def () :
    return this._outputStream

  NodeJsOutput_0.prototype.print_2 = def (message) :
     messageString = String(message)
    this._outputStream.write(messageString)

  NodeJsOutput_0.$metadata$ = {
    simpleName: 'NodeJsOutput',
    kind: 'class',
    interfaces: []

  def BufferedOutputToConsoleLog_0() :
    BufferedOutput_0.call(this)

  BufferedOutputToConsoleLog_0.prototype.print_2 = def (message) :
     s = String(message)
     tmp0_nativeLastIndexOf_0 = s
     tmp1_nativeLastIndexOf_0 = '\n'
     tmp2_nativeLastIndexOf_0 = 0
     i = tmp0_nativeLastIndexOf_0.lastIndexOf(tmp1_nativeLastIndexOf_0, tmp2_nativeLastIndexOf_0)
    if (i >= 0) :
       tmp0_this = this
       tmp = tmp0_this._get_buffer__0()
       tmp3_substring_0 = s
       tmp4_substring_0 = 0
      tmp0_this._set_buffer__0(tmp + tmp3_substring_0.substring(tmp4_substring_0, i))
      this.flush_2()
       tmp5_substring_0 = s
       tmp6_substring_0 = i + 1 | 0
      s = tmp5_substring_0.substring(tmp6_substring_0)
     tmp1_this = this
    tmp1_this._set_buffer__0(tmp1_this._get_buffer__0() + s)

  BufferedOutputToConsoleLog_0.prototype.flush_2 = def () :
    (def () :
       $externalVarargReceiverTmp = console
      return $externalVarargReceiverTmp.log.apply($externalVarargReceiverTmp, [].concat([].slice.call([this._get_buffer__0()])))
    .call(this))
    this._set_buffer__0('')

  BufferedOutputToConsoleLog_0.$metadata$ = {
    simpleName: 'BufferedOutputToConsoleLog',
    kind: 'class',
    interfaces: []

  def String_0(value) :
    return String(value)

  def BufferedOutput_0() :
    BaseOutput.call(this)
    this._buffer = ''

  BufferedOutput_0.prototype._set_buffer__0 = def (_set___) :
    this._buffer = _set___

  BufferedOutput_0.prototype._get_buffer__0 = def () :
    return this._buffer

  BufferedOutput_0.prototype.print_2 = def (message) :
     tmp0_this = this
     tmp = tmp0_this
     tmp_0 = tmp0_this._buffer
    tmp._buffer = tmp_0 + String(message)

  BufferedOutput_0.prototype.flush_2 = def () :
    this._buffer = ''

  BufferedOutput_0.$metadata$ = {
    simpleName: 'BufferedOutput',
    kind: 'class',
    interfaces: []

  def println(message) :
    output.println_6(message)

  def output$init$() :
     isNode_2 = typeof process !== 'undefined' && process.versions && !!process.versions.node
    return isNode_2 ? new NodeJsOutput_0(process.stdout) : new BufferedOutputToConsoleLog_0()

  def _get_EmptyContinuation_() :
    return EmptyContinuation

   EmptyContinuation
  def _no_name_provided__1_0($tmp0_Continuation_0) :
    this._$tmp0_Continuation_0 = $tmp0_Continuation_0

  _no_name_provided__1_0.prototype._get_context__2 = def () :
    return this._$tmp0_Continuation_0

  _no_name_provided__1_0.prototype._get_context__4 = def () :
    return this._get_context__2()

  _no_name_provided__1_0.prototype.resumeWith_3 = def (result) :
    throwOnFailure(result)
     tmp = _Result___get_value__impl_(result)
    if (tmp == null ? true : isObject(tmp))
      tmp;
    else
      THROW_CCE()
    return Unit_getInstance()

  _no_name_provided__1_0.prototype.resumeWith_6 = def (result) :
    return this.resumeWith_3(result)

  _no_name_provided__1_0.$metadata$ = {
    simpleName: '<no name provided>_1',
    kind: 'class',
    interfaces: [Continuation]

  def EmptyContinuation$init$() :
     tmp0_Continuation_0 = EmptyCoroutineContext_getInstance()
    return new _no_name_provided__1_0(tmp0_Continuation_0)

  def asDynamic(_this_) :
    return _this_

  def unsafeCast(_this_) :
    return _this_

  def unsafeCast_0(_this_) :
    return _this_

  def Serializable() :

  Serializable.$metadata$ = {
    simpleName: 'Serializable',
    kind: 'interface',
    interfaces: []

  def pow(_this_, n) :
    return Math.pow(_this_, n)

  def isNaN_0(_this_) :
    return !(_this_ === _this_)

  def _get_INV_2_26_() :
    return INV_2_26

   INV_2_26
  def _get_INV_2_53_() :
    return INV_2_53

   INV_2_53
  def INV_2_26$init$() :
     tmp0_pow_0 = 2.0
     tmp1_pow_0 = -26
    return Math.pow(tmp0_pow_0, tmp1_pow_0)

  def INV_2_53$init$() :
     tmp0_pow_0 = 2.0
     tmp1_pow_0 = -53
    return Math.pow(tmp0_pow_0, tmp1_pow_0)

  def _get_js_(_this_) :
    return (_this_ instanceof KClassImpl ? _this_ : THROW_CCE())._get_jClass__2()

  def KCallable() :

  KCallable.$metadata$ = {
    simpleName: 'KCallable',
    kind: 'interface',
    interfaces: []

  def KClass() :

  KClass.$metadata$ = {
    simpleName: 'KClass',
    kind: 'interface',
    interfaces: [KClassifier]

  def KClassImpl(jClass) :
    this._jClass = jClass

  KClassImpl.prototype._get_jClass__2 = def () :
    return this._jClass

  KClassImpl.prototype._get_qualifiedName__4 = def () :
    throw NotImplementedError_init_$Create$(null, 1, null)

  KClassImpl.prototype.equals = def (other) :
     tmp
    if (other instanceof KClassImpl) :
      tmp = equals(this._get_jClass__2(), other._get_jClass__2())
     else :
      :
        tmp = false


    return tmp

  KClassImpl.prototype.hashCode = def () :
     tmp0_safe_receiver = this._get_simpleName__4()
     tmp1_elvis_lhs = tmp0_safe_receiver == null ? null : getStringHashCode(tmp0_safe_receiver)
    return tmp1_elvis_lhs == null ? 0 : tmp1_elvis_lhs

  KClassImpl.prototype.toString = def () :
    return '' + 'class ' + this._get_simpleName__4()

  KClassImpl.$metadata$ = {
    simpleName: 'KClassImpl',
    kind: 'class',
    interfaces: [KClass]

  def _get_givenSimpleName_($this) :
    return $this._givenSimpleName

  def _get_isInstanceFunction_($this) :
    return $this._isInstanceFunction

  def PrimitiveKClassImpl(jClass, givenSimpleName, isInstanceFunction) :
    KClassImpl.call(this, jClass)
    this._givenSimpleName = givenSimpleName
    this._isInstanceFunction = isInstanceFunction

  PrimitiveKClassImpl.prototype.equals = def (other) :
    if (!(other instanceof PrimitiveKClassImpl))
      return false;
    else :

    return KClassImpl.prototype.equals.call(this, other) ? this._givenSimpleName === other._givenSimpleName : false

  PrimitiveKClassImpl.prototype._get_simpleName__4 = def () :
    return this._givenSimpleName

  PrimitiveKClassImpl.prototype.isInstance_4 = def (value) :
    return this._isInstanceFunction(value)

  PrimitiveKClassImpl.$metadata$ = {
    simpleName: 'PrimitiveKClassImpl',
    kind: 'class',
    interfaces: []

  def NothingKClassImpl() :
    NothingKClassImpl_instance = this
    KClassImpl.call(this, Object)
    this._simpleName = 'Nothing'

  NothingKClassImpl.prototype._get_simpleName__4 = def () :
    return this._simpleName

  NothingKClassImpl.prototype.isInstance_4 = def (value) :
    return false

  NothingKClassImpl.prototype._get_jClass__2 = def () :
    throw UnsupportedOperationException_init_$Create$_0("There's no native JS class for Nothing type")

  NothingKClassImpl.prototype.equals = def (other) :
    return other === this

  NothingKClassImpl.prototype.hashCode = def () :
    return 0

  NothingKClassImpl.$metadata$ = {
    simpleName: 'NothingKClassImpl',
    kind: 'object',
    interfaces: []

   NothingKClassImpl_instance
  def NothingKClassImpl_getInstance() :
    if (NothingKClassImpl_instance == null)
      new NothingKClassImpl()
    return NothingKClassImpl_instance

  def ErrorKClass() :

  ErrorKClass.prototype._get_simpleName__4 = def () :
     tmp0_error_0 = 'Unknown simpleName for ErrorKClass'
    throw IllegalStateException_init_$Create$_0(toString_0(tmp0_error_0))

  ErrorKClass.prototype._get_qualifiedName__4 = def () :
     tmp0_error_0 = 'Unknown qualifiedName for ErrorKClass'
    throw IllegalStateException_init_$Create$_0(toString_0(tmp0_error_0))

  ErrorKClass.prototype.isInstance_4 = def (value) :
     tmp0_error_0 = "Can's check isInstance on ErrorKClass"
    throw IllegalStateException_init_$Create$_0(toString_0(tmp0_error_0))

  ErrorKClass.prototype.equals = def (other) :
    return other === this

  ErrorKClass.prototype.hashCode = def () :
    return 0

  ErrorKClass.$metadata$ = {
    simpleName: 'ErrorKClass',
    kind: 'class',
    interfaces: [KClass]

  def SimpleKClassImpl(jClass) :
    KClassImpl.call(this, jClass)
     tmp = this
     tmp0_safe_receiver = jClass.$metadata$
     tmp0_unsafeCast_0 = tmp0_safe_receiver == null ? null : tmp0_safe_receiver.simpleName
    tmp._simpleName_0 = tmp0_unsafeCast_0

  SimpleKClassImpl.prototype._get_simpleName__4 = def () :
    return this._simpleName_0

  SimpleKClassImpl.prototype.isInstance_4 = def (value) :
    return jsIsType(value, this._get_jClass__2())

  SimpleKClassImpl.$metadata$ = {
    simpleName: 'SimpleKClassImpl',
    kind: 'class',
    interfaces: []

  def KFunction() :

  KFunction.$metadata$ = {
    simpleName: 'KFunction',
    kind: 'interface',
    interfaces: [KCallable]

  def KProperty() :

  KProperty.$metadata$ = {
    simpleName: 'KProperty',
    kind: 'interface',
    interfaces: [KCallable]

  def KProperty0() :

  KProperty0.$metadata$ = {
    simpleName: 'KProperty0',
    kind: 'interface',
    interfaces: [KProperty]

  def KProperty1() :

  KProperty1.$metadata$ = {
    simpleName: 'KProperty1',
    kind: 'interface',
    interfaces: [KProperty]

  def KProperty2() :

  KProperty2.$metadata$ = {
    simpleName: 'KProperty2',
    kind: 'interface',
    interfaces: [KProperty]

  def KMutableProperty0() :

  KMutableProperty0.$metadata$ = {
    simpleName: 'KMutableProperty0',
    kind: 'interface',
    interfaces: [KProperty0, KMutableProperty]

  def KMutableProperty() :

  KMutableProperty.$metadata$ = {
    simpleName: 'KMutableProperty',
    kind: 'interface',
    interfaces: [KProperty]

  def KMutableProperty1() :

  KMutableProperty1.$metadata$ = {
    simpleName: 'KMutableProperty1',
    kind: 'interface',
    interfaces: [KProperty1, KMutableProperty]

  def KMutableProperty2() :

  KMutableProperty2.$metadata$ = {
    simpleName: 'KMutableProperty2',
    kind: 'interface',
    interfaces: [KProperty2, KMutableProperty]

  def KType() :

  KType.$metadata$ = {
    simpleName: 'KType',
    kind: 'interface',
    interfaces: []

  def createKType_0(classifier, arguments_0, isMarkedNullable) :
    return new KTypeImpl(classifier, asList(arguments_0), isMarkedNullable)

  def createDynamicKType_0() :
    return DynamicKType_getInstance()

  def createKTypeParameter_0(name, upperBounds, variance) :
     tmp0_subject = variance
    :
       kVariance
      switch (tmp0_subject) :
        case 'in':
          kVariance = KVariance_IN_getInstance();
          break;
        case 'out':
          kVariance = KVariance_OUT_getInstance();
          break;
        default:kVariance = KVariance_INVARIANT_getInstance();
          break;


    return new KTypeParameterImpl(name, asList(upperBounds), kVariance, false)

  def getStarKTypeProjection_0() :
    return Companion_getInstance_1()._get_STAR_()

  def createCovariantKTypeProjection_0(type) :
    return Companion_getInstance_1().covariant(type)

  def createInvariantKTypeProjection_0(type) :
    return Companion_getInstance_1().invariant(type)

  def createContravariantKTypeProjection_0(type) :
    return Companion_getInstance_1().contravariant(type)

  def asString(_this_, $this) :
    if (_this_._variance == null)
      return '*'
    return prefixString(_this_._variance) + toString(_this_._type)

  def _no_name_provided__8(this$0) :
    this._this$0_0 = this$0

  _no_name_provided__8.prototype.invoke_21 = def (it) :
    return asString(it, this._this$0_0)

  _no_name_provided__8.prototype.invoke_66 = def (p1) :
    return this.invoke_21(p1 instanceof KTypeProjection ? p1 : THROW_CCE())

  _no_name_provided__8.$metadata$ = {
    kind: 'class',
    interfaces: []

  def KTypeImpl(classifier, arguments_0, isMarkedNullable) :
    this._classifier = classifier
    this._arguments = arguments_0
    this._isMarkedNullable = isMarkedNullable

  KTypeImpl.prototype._get_classifier__1 = def () :
    return this._classifier

  KTypeImpl.prototype._get_arguments__1 = def () :
    return this._arguments

  KTypeImpl.prototype._get_isMarkedNullable__1 = def () :
    return this._isMarkedNullable

  KTypeImpl.prototype.equals = def (other) :
     tmp
     tmp_0
     tmp_1
    if (other instanceof KTypeImpl) :
      tmp_1 = equals(this._classifier, other._classifier)
     else :
      :
        tmp_1 = false


    if (tmp_1) :
      tmp_0 = equals(this._arguments, other._arguments)
     else :
      :
        tmp_0 = false


    if (tmp_0) :
      tmp = this._isMarkedNullable === other._isMarkedNullable
     else :
      :
        tmp = false


    return tmp

  KTypeImpl.prototype.hashCode = def () :
    return imul(imul(hashCode(this._classifier), 31) + hashCode(this._arguments) | 0, 31) + (this._isMarkedNullable | 0) | 0

  KTypeImpl.prototype.toString = def () :
     tmp = this._classifier
     kClass = isInterface(tmp, KClass) ? tmp : null
     classifierName = kClass == null ? toString_0(this._classifier) : !(kClass._get_simpleName__4() == null) ? kClass._get_simpleName__4() : '(non-denotable type)'
     tmp_0
    if (this._arguments.isEmpty_29()) :
      tmp_0 = ''
     else :
      tmp_0 = joinToString$default_0(this._arguments, ', ', '<', '>', 0, null, _no_name_provided_$factory_7(this), 24, null)

     args = tmp_0
     nullable = this._isMarkedNullable ? '?' : ''
    return plus(classifierName, args) + nullable

  KTypeImpl.$metadata$ = {
    simpleName: 'KTypeImpl',
    kind: 'class',
    interfaces: [KType]

  def prefixString(_this_) :
     tmp0_subject = _this_
     tmp
    if (tmp0_subject.equals(KVariance_INVARIANT_getInstance())) :
      tmp = ''
     else if (tmp0_subject.equals(KVariance_IN_getInstance())) :
      tmp = 'in '
     else if (tmp0_subject.equals(KVariance_OUT_getInstance())) :
      tmp = 'out '
     else :
      noWhenBranchMatchedException()

    return tmp

  def DynamicKType() :
    DynamicKType_instance = this
    this._classifier_0 = null
    this._arguments_0 = emptyList()
    this._isMarkedNullable_0 = false

  DynamicKType.prototype._get_classifier__1 = def () :
    return this._classifier_0

  DynamicKType.prototype._get_arguments__1 = def () :
    return this._arguments_0

  DynamicKType.prototype._get_isMarkedNullable__1 = def () :
    return this._isMarkedNullable_0

  DynamicKType.prototype.toString = def () :
    return 'dynamic'

  DynamicKType.$metadata$ = {
    simpleName: 'DynamicKType',
    kind: 'object',
    interfaces: [KType]

   DynamicKType_instance
  def DynamicKType_getInstance() :
    if (DynamicKType_instance == null)
      new DynamicKType()
    return DynamicKType_instance

  def _no_name_provided_$factory_7(this$0) :
     i = new _no_name_provided__8(this$0)
    return def (p1) :
      return i.invoke_21(p1)


  def KTypeParameterImpl(name, upperBounds, variance, isReified) :
    this._name_1 = name
    this._upperBounds = upperBounds
    this._variance_0 = variance
    this._isReified = isReified

  KTypeParameterImpl.prototype._get_name__22 = def () :
    return this._name_1

  KTypeParameterImpl.prototype._get_upperBounds__0 = def () :
    return this._upperBounds

  KTypeParameterImpl.prototype._get_variance__1 = def () :
    return this._variance_0

  KTypeParameterImpl.prototype._get_isReified__0 = def () :
    return this._isReified

  KTypeParameterImpl.prototype.toString = def () :
    return this._name_1

  KTypeParameterImpl.prototype.component1_0 = def () :
    return this._name_1

  KTypeParameterImpl.prototype.component2_0 = def () :
    return this._upperBounds

  KTypeParameterImpl.prototype.component3 = def () :
    return this._variance_0

  KTypeParameterImpl.prototype.component4 = def () :
    return this._isReified

  KTypeParameterImpl.prototype.copy_0 = def (name, upperBounds, variance, isReified) :
    return new KTypeParameterImpl(name, upperBounds, variance, isReified)

  KTypeParameterImpl.prototype.copy$default_0 = def (name, upperBounds, variance, isReified, $mask0, $handler) :
    if (!(($mask0 & 1) === 0))
      name = this._name_1
    if (!(($mask0 & 2) === 0))
      upperBounds = this._upperBounds
    if (!(($mask0 & 4) === 0))
      variance = this._variance_0
    if (!(($mask0 & 8) === 0))
      isReified = this._isReified
    return this.copy_0(name, upperBounds, variance, isReified)

  KTypeParameterImpl.prototype.hashCode = def () :
     result = getStringHashCode(this._name_1)
    result = imul(result, 31) + hashCode(this._upperBounds) | 0
    result = imul(result, 31) + this._variance_0.hashCode() | 0
    result = imul(result, 31) + (this._isReified | 0) | 0
    return result

  KTypeParameterImpl.prototype.equals = def (other) :
    if (this === other)
      return true
    if (!(other instanceof KTypeParameterImpl))
      return false;
    else :

     tmp0_other_with_cast = other instanceof KTypeParameterImpl ? other : THROW_CCE()
    if (!(this._name_1 === tmp0_other_with_cast._name_1))
      return false
    if (!equals(this._upperBounds, tmp0_other_with_cast._upperBounds))
      return false
    if (!this._variance_0.equals(tmp0_other_with_cast._variance_0))
      return false
    if (!(this._isReified === tmp0_other_with_cast._isReified))
      return false
    return true

  KTypeParameterImpl.$metadata$ = {
    simpleName: 'KTypeParameterImpl',
    kind: 'class',
    interfaces: [KTypeParameter]

  def _get_functionClasses_() :
    return functionClasses

   functionClasses
  def _no_name_provided__9() :

  _no_name_provided__9.prototype.invoke_65 = def (it) :
    return isObject(it)

  _no_name_provided__9.prototype.invoke_66 = def (p1) :
    return this.invoke_65((p1 == null ? true : isObject(p1)) ? p1 : THROW_CCE())

  _no_name_provided__9.$metadata$ = {
    kind: 'class',
    interfaces: []

  def _no_name_provided__10() :

  _no_name_provided__10.prototype.invoke_65 = def (it) :
    return isNumber(it)

  _no_name_provided__10.prototype.invoke_66 = def (p1) :
    return this.invoke_65((p1 == null ? true : isObject(p1)) ? p1 : THROW_CCE())

  _no_name_provided__10.$metadata$ = {
    kind: 'class',
    interfaces: []

  def _no_name_provided__11() :

  _no_name_provided__11.prototype.invoke_65 = def (it) :
    return !(it == null) ? typeof it === 'boolean' : false

  _no_name_provided__11.prototype.invoke_66 = def (p1) :
    return this.invoke_65((p1 == null ? true : isObject(p1)) ? p1 : THROW_CCE())

  _no_name_provided__11.$metadata$ = {
    kind: 'class',
    interfaces: []

  def _no_name_provided__12() :

  _no_name_provided__12.prototype.invoke_65 = def (it) :
    return !(it == null) ? typeof it === 'number' : false

  _no_name_provided__12.prototype.invoke_66 = def (p1) :
    return this.invoke_65((p1 == null ? true : isObject(p1)) ? p1 : THROW_CCE())

  _no_name_provided__12.$metadata$ = {
    kind: 'class',
    interfaces: []

  def _no_name_provided__13() :

  _no_name_provided__13.prototype.invoke_65 = def (it) :
    return !(it == null) ? typeof it === 'number' : false

  _no_name_provided__13.prototype.invoke_66 = def (p1) :
    return this.invoke_65((p1 == null ? true : isObject(p1)) ? p1 : THROW_CCE())

  _no_name_provided__13.$metadata$ = {
    kind: 'class',
    interfaces: []

  def _no_name_provided__14() :

  _no_name_provided__14.prototype.invoke_65 = def (it) :
    return !(it == null) ? typeof it === 'number' : false

  _no_name_provided__14.prototype.invoke_66 = def (p1) :
    return this.invoke_65((p1 == null ? true : isObject(p1)) ? p1 : THROW_CCE())

  _no_name_provided__14.$metadata$ = {
    kind: 'class',
    interfaces: []

  def _no_name_provided__15() :

  _no_name_provided__15.prototype.invoke_65 = def (it) :
    return !(it == null) ? typeof it === 'number' : false

  _no_name_provided__15.prototype.invoke_66 = def (p1) :
    return this.invoke_65((p1 == null ? true : isObject(p1)) ? p1 : THROW_CCE())

  _no_name_provided__15.$metadata$ = {
    kind: 'class',
    interfaces: []

  def _no_name_provided__16() :

  _no_name_provided__16.prototype.invoke_65 = def (it) :
    return !(it == null) ? typeof it === 'number' : false

  _no_name_provided__16.prototype.invoke_66 = def (p1) :
    return this.invoke_65((p1 == null ? true : isObject(p1)) ? p1 : THROW_CCE())

  _no_name_provided__16.$metadata$ = {
    kind: 'class',
    interfaces: []

  def _no_name_provided__17() :

  _no_name_provided__17.prototype.invoke_65 = def (it) :
    return !(it == null) ? isArray(it) : false

  _no_name_provided__17.prototype.invoke_66 = def (p1) :
    return this.invoke_65((p1 == null ? true : isObject(p1)) ? p1 : THROW_CCE())

  _no_name_provided__17.$metadata$ = {
    kind: 'class',
    interfaces: []

  def _no_name_provided__18() :

  _no_name_provided__18.prototype.invoke_65 = def (it) :
    return !(it == null) ? typeof it === 'string' : false

  _no_name_provided__18.prototype.invoke_66 = def (p1) :
    return this.invoke_65((p1 == null ? true : isObject(p1)) ? p1 : THROW_CCE())

  _no_name_provided__18.$metadata$ = {
    kind: 'class',
    interfaces: []

  def _no_name_provided__19() :

  _no_name_provided__19.prototype.invoke_65 = def (it) :
    return it instanceof Error

  _no_name_provided__19.prototype.invoke_66 = def (p1) :
    return this.invoke_65((p1 == null ? true : isObject(p1)) ? p1 : THROW_CCE())

  _no_name_provided__19.$metadata$ = {
    kind: 'class',
    interfaces: []

  def _no_name_provided__20() :

  _no_name_provided__20.prototype.invoke_65 = def (it) :
    return !(it == null) ? isBooleanArray(it) : false

  _no_name_provided__20.prototype.invoke_66 = def (p1) :
    return this.invoke_65((p1 == null ? true : isObject(p1)) ? p1 : THROW_CCE())

  _no_name_provided__20.$metadata$ = {
    kind: 'class',
    interfaces: []

  def _no_name_provided__21() :

  _no_name_provided__21.prototype.invoke_65 = def (it) :
    return !(it == null) ? isCharArray(it) : false

  _no_name_provided__21.prototype.invoke_66 = def (p1) :
    return this.invoke_65((p1 == null ? true : isObject(p1)) ? p1 : THROW_CCE())

  _no_name_provided__21.$metadata$ = {
    kind: 'class',
    interfaces: []

  def _no_name_provided__22() :

  _no_name_provided__22.prototype.invoke_65 = def (it) :
    return !(it == null) ? isByteArray(it) : false

  _no_name_provided__22.prototype.invoke_66 = def (p1) :
    return this.invoke_65((p1 == null ? true : isObject(p1)) ? p1 : THROW_CCE())

  _no_name_provided__22.$metadata$ = {
    kind: 'class',
    interfaces: []

  def _no_name_provided__23() :

  _no_name_provided__23.prototype.invoke_65 = def (it) :
    return !(it == null) ? isShortArray(it) : false

  _no_name_provided__23.prototype.invoke_66 = def (p1) :
    return this.invoke_65((p1 == null ? true : isObject(p1)) ? p1 : THROW_CCE())

  _no_name_provided__23.$metadata$ = {
    kind: 'class',
    interfaces: []

  def _no_name_provided__24() :

  _no_name_provided__24.prototype.invoke_65 = def (it) :
    return !(it == null) ? isIntArray(it) : false

  _no_name_provided__24.prototype.invoke_66 = def (p1) :
    return this.invoke_65((p1 == null ? true : isObject(p1)) ? p1 : THROW_CCE())

  _no_name_provided__24.$metadata$ = {
    kind: 'class',
    interfaces: []

  def _no_name_provided__25() :

  _no_name_provided__25.prototype.invoke_65 = def (it) :
    return !(it == null) ? isLongArray(it) : false

  _no_name_provided__25.prototype.invoke_66 = def (p1) :
    return this.invoke_65((p1 == null ? true : isObject(p1)) ? p1 : THROW_CCE())

  _no_name_provided__25.$metadata$ = {
    kind: 'class',
    interfaces: []

  def _no_name_provided__26() :

  _no_name_provided__26.prototype.invoke_65 = def (it) :
    return !(it == null) ? isFloatArray(it) : false

  _no_name_provided__26.prototype.invoke_66 = def (p1) :
    return this.invoke_65((p1 == null ? true : isObject(p1)) ? p1 : THROW_CCE())

  _no_name_provided__26.$metadata$ = {
    kind: 'class',
    interfaces: []

  def _no_name_provided__27() :

  _no_name_provided__27.prototype.invoke_65 = def (it) :
    return !(it == null) ? isDoubleArray(it) : false

  _no_name_provided__27.prototype.invoke_66 = def (p1) :
    return this.invoke_65((p1 == null ? true : isObject(p1)) ? p1 : THROW_CCE())

  _no_name_provided__27.$metadata$ = {
    kind: 'class',
    interfaces: []

  def _no_name_provided__28($arity) :
    this._$arity = $arity

  _no_name_provided__28.prototype.invoke_65 = def (it) :
     tmp
    if (typeof it === 'function') :
      tmp = it.length === this._$arity
     else :
      tmp = false

    return tmp

  _no_name_provided__28.prototype.invoke_66 = def (p1) :
    return this.invoke_65((p1 == null ? true : isObject(p1)) ? p1 : THROW_CCE())

  _no_name_provided__28.$metadata$ = {
    kind: 'class',
    interfaces: []

  def PrimitiveClasses_0() :
    PrimitiveClasses_instance = this
     tmp = this
     tmp0_unsafeCast_0 = Object
     tmp_0 = tmp0_unsafeCast_0
    tmp._anyClass = new PrimitiveKClassImpl(tmp_0, 'Any', _no_name_provided_$factory_8())
     tmp_1 = this
     tmp0_unsafeCast_0_0 = Number
     tmp_2 = tmp0_unsafeCast_0_0
    tmp_1._numberClass = new PrimitiveKClassImpl(tmp_2, 'Number', _no_name_provided_$factory_9())
    this._nothingClass = NothingKClassImpl_getInstance()
     tmp_3 = this
     tmp0_unsafeCast_0_1 = Boolean
     tmp_4 = tmp0_unsafeCast_0_1
    tmp_3._booleanClass = new PrimitiveKClassImpl(tmp_4, 'Boolean', _no_name_provided_$factory_10())
     tmp_5 = this
     tmp0_unsafeCast_0_2 = Number
     tmp_6 = tmp0_unsafeCast_0_2
    tmp_5._byteClass = new PrimitiveKClassImpl(tmp_6, 'Byte', _no_name_provided_$factory_11())
     tmp_7 = this
     tmp0_unsafeCast_0_3 = Number
     tmp_8 = tmp0_unsafeCast_0_3
    tmp_7._shortClass = new PrimitiveKClassImpl(tmp_8, 'Short', _no_name_provided_$factory_12())
     tmp_9 = this
     tmp0_unsafeCast_0_4 = Number
     tmp_10 = tmp0_unsafeCast_0_4
    tmp_9._intClass = new PrimitiveKClassImpl(tmp_10, 'Int', _no_name_provided_$factory_13())
     tmp_11 = this
     tmp0_unsafeCast_0_5 = Number
     tmp_12 = tmp0_unsafeCast_0_5
    tmp_11._floatClass = new PrimitiveKClassImpl(tmp_12, 'Float', _no_name_provided_$factory_14())
     tmp_13 = this
     tmp0_unsafeCast_0_6 = Number
     tmp_14 = tmp0_unsafeCast_0_6
    tmp_13._doubleClass = new PrimitiveKClassImpl(tmp_14, 'Double', _no_name_provided_$factory_15())
     tmp_15 = this
     tmp0_unsafeCast_0_7 = Array
     tmp_16 = tmp0_unsafeCast_0_7
    tmp_15._arrayClass = new PrimitiveKClassImpl(tmp_16, 'Array', _no_name_provided_$factory_16())
     tmp_17 = this
     tmp0_unsafeCast_0_8 = String
     tmp_18 = tmp0_unsafeCast_0_8
    tmp_17._stringClass = new PrimitiveKClassImpl(tmp_18, 'String', _no_name_provided_$factory_17())
     tmp_19 = this
     tmp0_unsafeCast_0_9 = Error
     tmp_20 = tmp0_unsafeCast_0_9
    tmp_19._throwableClass = new PrimitiveKClassImpl(tmp_20, 'Throwable', _no_name_provided_$factory_18())
     tmp_21 = this
     tmp0_unsafeCast_0_10 = Array
     tmp_22 = tmp0_unsafeCast_0_10
    tmp_21._booleanArrayClass = new PrimitiveKClassImpl(tmp_22, 'BooleanArray', _no_name_provided_$factory_19())
     tmp_23 = this
     tmp0_unsafeCast_0_11 = Uint16Array
     tmp_24 = tmp0_unsafeCast_0_11
    tmp_23._charArrayClass = new PrimitiveKClassImpl(tmp_24, 'CharArray', _no_name_provided_$factory_20())
     tmp_25 = this
     tmp0_unsafeCast_0_12 = Int8Array
     tmp_26 = tmp0_unsafeCast_0_12
    tmp_25._byteArrayClass = new PrimitiveKClassImpl(tmp_26, 'ByteArray', _no_name_provided_$factory_21())
     tmp_27 = this
     tmp0_unsafeCast_0_13 = Int16Array
     tmp_28 = tmp0_unsafeCast_0_13
    tmp_27._shortArrayClass = new PrimitiveKClassImpl(tmp_28, 'ShortArray', _no_name_provided_$factory_22())
     tmp_29 = this
     tmp0_unsafeCast_0_14 = Int32Array
     tmp_30 = tmp0_unsafeCast_0_14
    tmp_29._intArrayClass = new PrimitiveKClassImpl(tmp_30, 'IntArray', _no_name_provided_$factory_23())
     tmp_31 = this
     tmp0_unsafeCast_0_15 = Array
     tmp_32 = tmp0_unsafeCast_0_15
    tmp_31._longArrayClass = new PrimitiveKClassImpl(tmp_32, 'LongArray', _no_name_provided_$factory_24())
     tmp_33 = this
     tmp0_unsafeCast_0_16 = Float32Array
     tmp_34 = tmp0_unsafeCast_0_16
    tmp_33._floatArrayClass = new PrimitiveKClassImpl(tmp_34, 'FloatArray', _no_name_provided_$factory_25())
     tmp_35 = this
     tmp0_unsafeCast_0_17 = Float64Array
     tmp_36 = tmp0_unsafeCast_0_17
    tmp_35._doubleArrayClass = new PrimitiveKClassImpl(tmp_36, 'DoubleArray', _no_name_provided_$factory_26())

  PrimitiveClasses_0.prototype._get_anyClass_ = def () :
    return this._anyClass

  PrimitiveClasses_0.prototype._get_numberClass_ = def () :
    return this._numberClass

  PrimitiveClasses_0.prototype._get_nothingClass_ = def () :
    return this._nothingClass

  PrimitiveClasses_0.prototype._get_booleanClass_ = def () :
    return this._booleanClass

  PrimitiveClasses_0.prototype._get_byteClass_ = def () :
    return this._byteClass

  PrimitiveClasses_0.prototype._get_shortClass_ = def () :
    return this._shortClass

  PrimitiveClasses_0.prototype._get_intClass_ = def () :
    return this._intClass

  PrimitiveClasses_0.prototype._get_floatClass_ = def () :
    return this._floatClass

  PrimitiveClasses_0.prototype._get_doubleClass_ = def () :
    return this._doubleClass

  PrimitiveClasses_0.prototype._get_arrayClass_ = def () :
    return this._arrayClass

  PrimitiveClasses_0.prototype._get_stringClass_ = def () :
    return this._stringClass

  PrimitiveClasses_0.prototype._get_throwableClass_ = def () :
    return this._throwableClass

  PrimitiveClasses_0.prototype._get_booleanArrayClass_ = def () :
    return this._booleanArrayClass

  PrimitiveClasses_0.prototype._get_charArrayClass_ = def () :
    return this._charArrayClass

  PrimitiveClasses_0.prototype._get_byteArrayClass_ = def () :
    return this._byteArrayClass

  PrimitiveClasses_0.prototype._get_shortArrayClass_ = def () :
    return this._shortArrayClass

  PrimitiveClasses_0.prototype._get_intArrayClass_ = def () :
    return this._intArrayClass

  PrimitiveClasses_0.prototype._get_longArrayClass_ = def () :
    return this._longArrayClass

  PrimitiveClasses_0.prototype._get_floatArrayClass_ = def () :
    return this._floatArrayClass

  PrimitiveClasses_0.prototype._get_doubleArrayClass_ = def () :
    return this._doubleArrayClass

  PrimitiveClasses_0.prototype.functionClass = def (arity) :
     tmp0_elvis_lhs = functionClasses[arity]
     tmp
    if (tmp0_elvis_lhs == null) :
       tmp0_unsafeCast_0_3 = Function
       tmp_0 = tmp0_unsafeCast_0_3
       tmp_1 = '' + 'Function' + arity
       result_2 = new PrimitiveKClassImpl(tmp_0, tmp_1, _no_name_provided_$factory_27(arity))
       tmp1_asDynamic_0_5 = functionClasses
      tmp1_asDynamic_0_5[arity] = result_2
      tmp = result_2
     else :
      tmp = tmp0_elvis_lhs

    return tmp

  PrimitiveClasses_0.$metadata$ = {
    simpleName: 'PrimitiveClasses',
    kind: 'object',
    interfaces: []

  Object.defineProperty(PrimitiveClasses_0.prototype, 'anyClass', {
    configurable: true,
    get: PrimitiveClasses_0.prototype._get_anyClass_
  )
  Object.defineProperty(PrimitiveClasses_0.prototype, 'numberClass', {
    configurable: true,
    get: PrimitiveClasses_0.prototype._get_numberClass_
  )
  Object.defineProperty(PrimitiveClasses_0.prototype, 'nothingClass', {
    configurable: true,
    get: PrimitiveClasses_0.prototype._get_nothingClass_
  )
  Object.defineProperty(PrimitiveClasses_0.prototype, 'booleanClass', {
    configurable: true,
    get: PrimitiveClasses_0.prototype._get_booleanClass_
  )
  Object.defineProperty(PrimitiveClasses_0.prototype, 'byteClass', {
    configurable: true,
    get: PrimitiveClasses_0.prototype._get_byteClass_
  )
  Object.defineProperty(PrimitiveClasses_0.prototype, 'shortClass', {
    configurable: true,
    get: PrimitiveClasses_0.prototype._get_shortClass_
  )
  Object.defineProperty(PrimitiveClasses_0.prototype, 'intClass', {
    configurable: true,
    get: PrimitiveClasses_0.prototype._get_intClass_
  )
  Object.defineProperty(PrimitiveClasses_0.prototype, 'floatClass', {
    configurable: true,
    get: PrimitiveClasses_0.prototype._get_floatClass_
  )
  Object.defineProperty(PrimitiveClasses_0.prototype, 'doubleClass', {
    configurable: true,
    get: PrimitiveClasses_0.prototype._get_doubleClass_
  )
  Object.defineProperty(PrimitiveClasses_0.prototype, 'arrayClass', {
    configurable: true,
    get: PrimitiveClasses_0.prototype._get_arrayClass_
  )
  Object.defineProperty(PrimitiveClasses_0.prototype, 'stringClass', {
    configurable: true,
    get: PrimitiveClasses_0.prototype._get_stringClass_
  )
  Object.defineProperty(PrimitiveClasses_0.prototype, 'throwableClass', {
    configurable: true,
    get: PrimitiveClasses_0.prototype._get_throwableClass_
  )
  Object.defineProperty(PrimitiveClasses_0.prototype, 'booleanArrayClass', {
    configurable: true,
    get: PrimitiveClasses_0.prototype._get_booleanArrayClass_
  )
  Object.defineProperty(PrimitiveClasses_0.prototype, 'charArrayClass', {
    configurable: true,
    get: PrimitiveClasses_0.prototype._get_charArrayClass_
  )
  Object.defineProperty(PrimitiveClasses_0.prototype, 'byteArrayClass', {
    configurable: true,
    get: PrimitiveClasses_0.prototype._get_byteArrayClass_
  )
  Object.defineProperty(PrimitiveClasses_0.prototype, 'shortArrayClass', {
    configurable: true,
    get: PrimitiveClasses_0.prototype._get_shortArrayClass_
  )
  Object.defineProperty(PrimitiveClasses_0.prototype, 'intArrayClass', {
    configurable: true,
    get: PrimitiveClasses_0.prototype._get_intArrayClass_
  )
  Object.defineProperty(PrimitiveClasses_0.prototype, 'longArrayClass', {
    configurable: true,
    get: PrimitiveClasses_0.prototype._get_longArrayClass_
  )
  Object.defineProperty(PrimitiveClasses_0.prototype, 'floatArrayClass', {
    configurable: true,
    get: PrimitiveClasses_0.prototype._get_floatArrayClass_
  )
  Object.defineProperty(PrimitiveClasses_0.prototype, 'doubleArrayClass', {
    configurable: true,
    get: PrimitiveClasses_0.prototype._get_doubleArrayClass_
  )
   PrimitiveClasses_instance
  def PrimitiveClasses_getInstance() :
    if (PrimitiveClasses_instance == null)
      new PrimitiveClasses_0()
    return PrimitiveClasses_instance

  def _no_name_provided_$factory_8() :
     i = new _no_name_provided__9()
    return def (p1) :
      return i.invoke_65(p1)


  def _no_name_provided_$factory_9() :
     i = new _no_name_provided__10()
    return def (p1) :
      return i.invoke_65(p1)


  def _no_name_provided_$factory_10() :
     i = new _no_name_provided__11()
    return def (p1) :
      return i.invoke_65(p1)


  def _no_name_provided_$factory_11() :
     i = new _no_name_provided__12()
    return def (p1) :
      return i.invoke_65(p1)


  def _no_name_provided_$factory_12() :
     i = new _no_name_provided__13()
    return def (p1) :
      return i.invoke_65(p1)


  def _no_name_provided_$factory_13() :
     i = new _no_name_provided__14()
    return def (p1) :
      return i.invoke_65(p1)


  def _no_name_provided_$factory_14() :
     i = new _no_name_provided__15()
    return def (p1) :
      return i.invoke_65(p1)


  def _no_name_provided_$factory_15() :
     i = new _no_name_provided__16()
    return def (p1) :
      return i.invoke_65(p1)


  def _no_name_provided_$factory_16() :
     i = new _no_name_provided__17()
    return def (p1) :
      return i.invoke_65(p1)


  def _no_name_provided_$factory_17() :
     i = new _no_name_provided__18()
    return def (p1) :
      return i.invoke_65(p1)


  def _no_name_provided_$factory_18() :
     i = new _no_name_provided__19()
    return def (p1) :
      return i.invoke_65(p1)


  def _no_name_provided_$factory_19() :
     i = new _no_name_provided__20()
    return def (p1) :
      return i.invoke_65(p1)


  def _no_name_provided_$factory_20() :
     i = new _no_name_provided__21()
    return def (p1) :
      return i.invoke_65(p1)


  def _no_name_provided_$factory_21() :
     i = new _no_name_provided__22()
    return def (p1) :
      return i.invoke_65(p1)


  def _no_name_provided_$factory_22() :
     i = new _no_name_provided__23()
    return def (p1) :
      return i.invoke_65(p1)


  def _no_name_provided_$factory_23() :
     i = new _no_name_provided__24()
    return def (p1) :
      return i.invoke_65(p1)


  def _no_name_provided_$factory_24() :
     i = new _no_name_provided__25()
    return def (p1) :
      return i.invoke_65(p1)


  def _no_name_provided_$factory_25() :
     i = new _no_name_provided__26()
    return def (p1) :
      return i.invoke_65(p1)


  def _no_name_provided_$factory_26() :
     i = new _no_name_provided__27()
    return def (p1) :
      return i.invoke_65(p1)


  def _no_name_provided_$factory_27($arity) :
     i = new _no_name_provided__28($arity)
    return def (p1) :
      return i.invoke_65(p1)


  def functionClasses$init$() :
     tmp0_arrayOfNulls_0 = 0
    return fillArrayVal(Array(tmp0_arrayOfNulls_0), null)

  def getKClass_0(jClass) :
     tmp
    if (Array.isArray(jClass)) :
      tmp = getKClassM_0(jClass)
     else :
      tmp = getKClass1_0(jClass)

    return tmp

  def getKClassM_0(jClasses) :
     tmp0_subject = jClasses.length
     tmp
    switch (tmp0_subject) :
      case 1:
        tmp = getKClass1_0(jClasses[0]);
        break;
      case 0:
         tmp0_unsafeCast_0 = NothingKClassImpl_getInstance();
        tmp = tmp0_unsafeCast_0;
        break;
      default: tmp1_unsafeCast_0 = new ErrorKClass();
        tmp = tmp1_unsafeCast_0;
        break;

    return tmp

  def getKClass1_0(jClass) :
    if (jClass === String) :
       tmp0_unsafeCast_0 = PrimitiveClasses_getInstance()._stringClass
      return tmp0_unsafeCast_0
     metadata = jClass.$metadata$
     tmp
    if (metadata != null) :
       tmp_0
      if (metadata.$kClass$ == null) :
         kClass = new SimpleKClassImpl(jClass)
        metadata.$kClass$ = kClass
        tmp_0 = kClass
       else :
        tmp_0 = metadata.$kClass$

      tmp = tmp_0
     else :
      tmp = new SimpleKClassImpl(jClass)

    return tmp

  def getKClassFromExpression_0(e) :
     tmp0_subject = typeof e
     tmp
    switch (tmp0_subject) :
      case 'string':
        tmp = PrimitiveClasses_getInstance()._stringClass;
        break;
      case 'number':
         tmp_0;
         tmp0_asDynamic_0 = jsBitwiseOr(e, 0);
        if (tmp0_asDynamic_0 === e) :
          tmp_0 = PrimitiveClasses_getInstance()._intClass
         else :
          :
            tmp_0 = PrimitiveClasses_getInstance()._doubleClass



        tmp = tmp_0;
        break;
      case 'boolean':
        tmp = PrimitiveClasses_getInstance()._booleanClass;
        break;
      case 'function':
         tmp_1 = PrimitiveClasses_getInstance();
        tmp = tmp_1.functionClass(e.length);
        break;
      default: tmp_2;
        if (isBooleanArray(e)) :
          tmp_2 = PrimitiveClasses_getInstance()._booleanArrayClass
         else :
          if (isCharArray(e)) :
            tmp_2 = PrimitiveClasses_getInstance()._charArrayClass
           else :
            if (isByteArray(e)) :
              tmp_2 = PrimitiveClasses_getInstance()._byteArrayClass
             else :
              if (isShortArray(e)) :
                tmp_2 = PrimitiveClasses_getInstance()._shortArrayClass
               else :
                if (isIntArray(e)) :
                  tmp_2 = PrimitiveClasses_getInstance()._intArrayClass
                 else :
                  if (isLongArray(e)) :
                    tmp_2 = PrimitiveClasses_getInstance()._longArrayClass
                   else :
                    if (isFloatArray(e)) :
                      tmp_2 = PrimitiveClasses_getInstance()._floatArrayClass
                     else :
                      if (isDoubleArray(e)) :
                        tmp_2 = PrimitiveClasses_getInstance()._doubleArrayClass
                       else :
                        if (isInterface(e, KClass)) :
                          tmp_2 = getKClass_0(KClass)
                         else :
                          if (isArray(e)) :
                            tmp_2 = PrimitiveClasses_getInstance()._arrayClass
                           else :
                            :
                               constructor = Object.getPrototypeOf(e).constructor
                               tmp_3
                              if (constructor === Object) :
                                tmp_3 = PrimitiveClasses_getInstance()._anyClass
                               else if (constructor === Error) :
                                tmp_3 = PrimitiveClasses_getInstance()._throwableClass
                               else :
                                 jsClass_0 = constructor
                                tmp_3 = getKClass1_0(jsClass_0)

                              tmp_2 = tmp_3












        tmp = tmp_2;
        break;

     tmp1_unsafeCast_0 = tmp
    return tmp1_unsafeCast_0

  def Appendable() :

  Appendable.$metadata$ = {
    simpleName: 'Appendable',
    kind: 'interface',
    interfaces: []

  def StringBuilder_init_$Init$(capacity, $this) :
    StringBuilder_init_$Init$_1($this)
    return $this

  def StringBuilder_init_$Create$(capacity) :
    return StringBuilder_init_$Init$(capacity, Object.create(StringBuilder.prototype))

  def StringBuilder_init_$Init$_0(content, $this) :
    StringBuilder.call($this, toString_0(content))
    return $this

  def StringBuilder_init_$Create$_0(content) :
    return StringBuilder_init_$Init$_0(content, Object.create(StringBuilder.prototype))

  def StringBuilder_init_$Init$_1($this) :
    StringBuilder.call($this, '')
    return $this

  def StringBuilder_init_$Create$_1() :
    return StringBuilder_init_$Init$_1(Object.create(StringBuilder.prototype))

  def _set_string_($this, _set___) :
    $this._string = _set___

  def _get_string_($this) :
    return $this._string

  def checkReplaceRange($this, startIndex, endIndex, length) :
    if (startIndex < 0 ? true : startIndex > length) :
      throw IndexOutOfBoundsException_init_$Create$_0('' + 'startIndex: ' + startIndex + ', length: ' + length)
    if (startIndex > endIndex) :
      throw IllegalArgumentException_init_$Create$_0('' + 'startIndex(' + startIndex + ') > endIndex(' + endIndex + ')')

  def StringBuilder(content) :
    this._string = !(content === undefined) ? content : ''

  StringBuilder.prototype._get_length__0 = def () :
     tmp0_asDynamic_0 = this._string
    return tmp0_asDynamic_0.length

  StringBuilder.prototype.get_31 = def (index) :
     tmp0_getOrElse_0 = this._string
     tmp
    if (index >= 0 ? index <= _get_lastIndex__5(tmp0_getOrElse_0) : false) :
      tmp = charSequenceGet(tmp0_getOrElse_0, index)
     else :
      throw IndexOutOfBoundsException_init_$Create$_0('' + 'index: ' + index + ', length: ' + this._get_length__0() + '}')

    return tmp

  StringBuilder.prototype.subSequence_1 = def (startIndex, endIndex) :
     tmp0_substring_0 = this._string
    return tmp0_substring_0.substring(startIndex, endIndex)

  StringBuilder.prototype.append_2 = def (value) :
     tmp0_this = this
    tmp0_this._string = tmp0_this._string + value
    return this

  StringBuilder.prototype.append_3 = def (value) :
     tmp0_this = this
    tmp0_this._string = tmp0_this._string + toString(value)
    return this

  StringBuilder.prototype.append_4 = def (value, startIndex, endIndex) :
     tmp0_elvis_lhs = value
    return this.appendRange_0(tmp0_elvis_lhs == null ? 'null' : tmp0_elvis_lhs, startIndex, endIndex)

  StringBuilder.prototype.reverse = def () :
     reversed_0 = ''
     index = this._string.length - 1 | 0
    while (index >= 0) :
       tmp = this._string
       tmp0 = index
      index = tmp0 - 1 | 0
       low = charSequenceGet(tmp, tmp0)
      if (isLowSurrogate(low) ? index >= 0 : false) :
         tmp_0 = this._string
         tmp1 = index
        index = tmp1 - 1 | 0
         high = charSequenceGet(tmp_0, tmp1)
        if (isHighSurrogate(high)) :
          reversed_0 = reversed_0 + high + low
         else :
          reversed_0 = reversed_0 + low + high

       else :
        reversed_0 = reversed_0 + low


    this._string = reversed_0
    return this

  StringBuilder.prototype.append_5 = def (value) :
     tmp0_this = this
    tmp0_this._string = tmp0_this._string + toString(value)
    return this

  StringBuilder.prototype.append_6 = def (value) :
     tmp0_this = this
    tmp0_this._string = tmp0_this._string + value
    return this

  StringBuilder.prototype.append_7 = def (value) :
     tmp0_this = this
    tmp0_this._string = tmp0_this._string + concatToString(value)
    return this

  StringBuilder.prototype.append_8 = def (value) :
    return this.append_9(value)

  StringBuilder.prototype.append_9 = def (value) :
     tmp0_this = this
     tmp = tmp0_this
     tmp_0 = tmp0_this._string
     tmp1_elvis_lhs = value
    tmp._string = tmp_0 + (tmp1_elvis_lhs == null ? 'null' : tmp1_elvis_lhs)
    return this

  StringBuilder.prototype.capacity = def () :
    return this._get_length__0()

  StringBuilder.prototype.ensureCapacity_0 = def (minimumCapacity) :

  StringBuilder.prototype.indexOf_6 = def (string) :
     tmp0_asDynamic_0 = this._string
    return tmp0_asDynamic_0.indexOf(string)

  StringBuilder.prototype.indexOf_7 = def (string, startIndex) :
     tmp0_asDynamic_0 = this._string
    return tmp0_asDynamic_0.indexOf(string, startIndex)

  StringBuilder.prototype.lastIndexOf_6 = def (string) :
     tmp0_asDynamic_0 = this._string
    return tmp0_asDynamic_0.lastIndexOf(string)

  StringBuilder.prototype.lastIndexOf_7 = def (string, startIndex) :
     tmp
    if (charSequenceLength(string) === 0) :
      tmp = startIndex < 0
     else :
      :
        tmp = false


    if (tmp)
      return -1;
    else :

     tmp0_asDynamic_0 = this._string
    return tmp0_asDynamic_0.lastIndexOf(string, startIndex)

  StringBuilder.prototype.insert = def (index, value) :
    Companion_getInstance().checkPositionIndex(index, this._get_length__0())
     tmp = this
     tmp0_substring_0 = this._string
     tmp1_substring_0 = 0
     tmp_0 = tmp0_substring_0.substring(tmp1_substring_0, index) + value
     tmp2_substring_0 = this._string
    tmp._string = tmp_0 + tmp2_substring_0.substring(index)
    return this

  StringBuilder.prototype.insert_0 = def (index, value) :
    Companion_getInstance().checkPositionIndex(index, this._get_length__0())
     tmp = this
     tmp0_substring_0 = this._string
     tmp1_substring_0 = 0
     tmp_0 = tmp0_substring_0.substring(tmp1_substring_0, index) + value
     tmp2_substring_0 = this._string
    tmp._string = tmp_0 + tmp2_substring_0.substring(index)
    return this

  StringBuilder.prototype.insert_1 = def (index, value) :
    Companion_getInstance().checkPositionIndex(index, this._get_length__0())
     tmp = this
     tmp0_substring_0 = this._string
     tmp1_substring_0 = 0
     tmp_0 = tmp0_substring_0.substring(tmp1_substring_0, index) + concatToString(value)
     tmp2_substring_0 = this._string
    tmp._string = tmp_0 + tmp2_substring_0.substring(index)
    return this

  StringBuilder.prototype.insert_2 = def (index, value) :
    Companion_getInstance().checkPositionIndex(index, this._get_length__0())
     tmp = this
     tmp0_substring_0 = this._string
     tmp1_substring_0 = 0
     tmp_0 = tmp0_substring_0.substring(tmp1_substring_0, index) + toString(value)
     tmp2_substring_0 = this._string
    tmp._string = tmp_0 + tmp2_substring_0.substring(index)
    return this

  StringBuilder.prototype.insert_3 = def (index, value) :
    Companion_getInstance().checkPositionIndex(index, this._get_length__0())
     tmp = this
     tmp0_substring_0 = this._string
     tmp1_substring_0 = 0
     tmp_0 = tmp0_substring_0.substring(tmp1_substring_0, index) + toString(value)
     tmp2_substring_0 = this._string
    tmp._string = tmp_0 + tmp2_substring_0.substring(index)
    return this

  StringBuilder.prototype.insert_4 = def (index, value) :
    return this.insert_5(index, value)

  StringBuilder.prototype.insert_5 = def (index, value) :
    Companion_getInstance().checkPositionIndex(index, this._get_length__0())
     tmp0_elvis_lhs = value
     toInsert = tmp0_elvis_lhs == null ? 'null' : tmp0_elvis_lhs
     tmp = this
     tmp0_substring_0 = this._string
     tmp1_substring_0 = 0
     tmp_0 = tmp0_substring_0.substring(tmp1_substring_0, index) + toInsert
     tmp2_substring_0 = this._string
    tmp._string = tmp_0 + tmp2_substring_0.substring(index)
    return this

  StringBuilder.prototype.setLength = def (newLength) :
    if (newLength < 0) :
      throw IllegalArgumentException_init_$Create$_0('' + 'Negative new length: ' + newLength + '.')
    if (newLength <= this._get_length__0()) :
       tmp = this
       tmp0_substring_0 = this._string
       tmp1_substring_0 = 0
      tmp._string = tmp0_substring_0.substring(tmp1_substring_0, newLength)
     else :
       inductionVariable = this._get_length__0()
      if (inductionVariable < newLength)
        do :
           i = inductionVariable
          inductionVariable = inductionVariable + 1 | 0
           tmp1_this = this
          tmp1_this._string = tmp1_this._string + new Char(0)

         while (inductionVariable < newLength)


  StringBuilder.prototype.substring = def (startIndex) :
    Companion_getInstance().checkPositionIndex(startIndex, this._get_length__0())
     tmp0_substring_0 = this._string
    return tmp0_substring_0.substring(startIndex)

  StringBuilder.prototype.substring_0 = def (startIndex, endIndex) :
    Companion_getInstance().checkBoundsIndexes(startIndex, endIndex, this._get_length__0())
     tmp0_substring_0 = this._string
    return tmp0_substring_0.substring(startIndex, endIndex)

  StringBuilder.prototype.trimToSize_0 = def () :

  StringBuilder.prototype.toString = def () :
    return this._string

  StringBuilder.prototype.clear_3 = def () :
    this._string = ''
    return this

  StringBuilder.prototype.set_16 = def (index, value) :
    Companion_getInstance().checkElementIndex(index, this._get_length__0())
     tmp = this
     tmp0_substring_0 = this._string
     tmp1_substring_0 = 0
     tmp_0 = tmp0_substring_0.substring(tmp1_substring_0, index) + value
     tmp2_substring_0 = this._string
     tmp3_substring_0 = index + 1 | 0
    tmp._string = tmp_0 + tmp2_substring_0.substring(tmp3_substring_0)

  StringBuilder.prototype.setRange = def (startIndex, endIndex, value) :
    checkReplaceRange(this, startIndex, endIndex, this._get_length__0())
     tmp = this
     tmp0_substring_0 = this._string
     tmp1_substring_0 = 0
     tmp_0 = tmp0_substring_0.substring(tmp1_substring_0, startIndex) + value
     tmp2_substring_0 = this._string
    tmp._string = tmp_0 + tmp2_substring_0.substring(endIndex)
    return this

  StringBuilder.prototype.deleteAt = def (index) :
    Companion_getInstance().checkElementIndex(index, this._get_length__0())
     tmp = this
     tmp0_substring_0 = this._string
     tmp1_substring_0 = 0
     tmp_0 = tmp0_substring_0.substring(tmp1_substring_0, index)
     tmp2_substring_0 = this._string
     tmp3_substring_0 = index + 1 | 0
    tmp._string = tmp_0 + tmp2_substring_0.substring(tmp3_substring_0)
    return this

  StringBuilder.prototype.deleteRange = def (startIndex, endIndex) :
    checkReplaceRange(this, startIndex, endIndex, this._get_length__0())
     tmp = this
     tmp0_substring_0 = this._string
     tmp1_substring_0 = 0
     tmp_0 = tmp0_substring_0.substring(tmp1_substring_0, startIndex)
     tmp2_substring_0 = this._string
    tmp._string = tmp_0 + tmp2_substring_0.substring(endIndex)
    return this

  StringBuilder.prototype.toCharArray = def (destination, destinationOffset, startIndex, endIndex) :
    Companion_getInstance().checkBoundsIndexes(startIndex, endIndex, this._get_length__0())
    Companion_getInstance().checkBoundsIndexes(destinationOffset, (destinationOffset + endIndex | 0) - startIndex | 0, destination.length)
     dstIndex = destinationOffset
     inductionVariable = startIndex
    if (inductionVariable < endIndex)
      do :
         index = inductionVariable
        inductionVariable = inductionVariable + 1 | 0
         tmp1 = dstIndex
        dstIndex = tmp1 + 1 | 0
        destination[tmp1] = charSequenceGet(this._string, index)

       while (inductionVariable < endIndex)

  StringBuilder.prototype.toCharArray$default = def (destination, destinationOffset, startIndex, endIndex, $mask0, $handler) :
    if (!(($mask0 & 2) === 0))
      destinationOffset = 0
    if (!(($mask0 & 4) === 0))
      startIndex = 0
    if (!(($mask0 & 8) === 0))
      endIndex = this._get_length__0()
    return this.toCharArray(destination, destinationOffset, startIndex, endIndex)

  StringBuilder.prototype.appendRange = def (value, startIndex, endIndex) :
     tmp0_this = this
    tmp0_this._string = tmp0_this._string + concatToString_0(value, startIndex, endIndex)
    return this

  StringBuilder.prototype.appendRange_0 = def (value, startIndex, endIndex) :
     stringCsq = toString_0(value)
    Companion_getInstance().checkBoundsIndexes(startIndex, endIndex, stringCsq.length)
     tmp0_this = this
     tmp = tmp0_this
     tmp_0 = tmp0_this._string
    tmp._string = tmp_0 + stringCsq.substring(startIndex, endIndex)
    return this

  StringBuilder.prototype.insertRange = def (index, value, startIndex, endIndex) :
    Companion_getInstance().checkPositionIndex(index, this._get_length__0())
     tmp = this
     tmp0_substring_0 = this._string
     tmp1_substring_0 = 0
     tmp_0 = tmp0_substring_0.substring(tmp1_substring_0, index) + concatToString_0(value, startIndex, endIndex)
     tmp2_substring_0 = this._string
    tmp._string = tmp_0 + tmp2_substring_0.substring(index)
    return this

  StringBuilder.prototype.insertRange_0 = def (index, value, startIndex, endIndex) :
    Companion_getInstance().checkPositionIndex(index, this._get_length__0())
     stringCsq = toString_0(value)
    Companion_getInstance().checkBoundsIndexes(startIndex, endIndex, stringCsq.length)
     tmp = this
     tmp0_substring_0 = this._string
     tmp1_substring_0 = 0
     tmp_0 = tmp0_substring_0.substring(tmp1_substring_0, index)
     tmp_1 = tmp_0 + stringCsq.substring(startIndex, endIndex)
     tmp2_substring_0 = this._string
    tmp._string = tmp_1 + tmp2_substring_0.substring(index)
    return this

  StringBuilder.$metadata$ = {
    simpleName: 'StringBuilder',
    kind: 'class',
    interfaces: [Appendable, CharSequence]

  def isLowSurrogate(_this_) :
     containsLower = new Char(56320)
    return _this_ <= new Char(57343) ? containsLower <= _this_ : false

  def isHighSurrogate(_this_) :
     containsLower = new Char(55296)
    return _this_ <= new Char(56319) ? containsLower <= _this_ : false

  def checkRadix(radix) :
    if (!(2 <= radix ? radix <= 36 : false)) :
      throw IllegalArgumentException_init_$Create$_0('' + 'radix ' + radix + ' was not in valid range 2..36')
    return radix

  def _get_STRING_CASE_INSENSITIVE_ORDER_() :
    return STRING_CASE_INSENSITIVE_ORDER

   STRING_CASE_INSENSITIVE_ORDER
  def nativeLastIndexOf(_this_, str, fromIndex) :
    return _this_.lastIndexOf(str, fromIndex)

  def substring(_this_, startIndex, endIndex) :
    return _this_.substring(startIndex, endIndex)

  def substring_0(_this_, startIndex) :
    return _this_.substring(startIndex)

  def compareTo(_this_, other, ignoreCase) :
    if (ignoreCase) :
       n1 = _this_.length
       n2 = other.length
       min = def () :
         $externalVarargReceiverTmp = Math
        return $externalVarargReceiverTmp.min.apply($externalVarargReceiverTmp, [].concat([].slice.call(new Int32Array([n1, n2]))))
      .call(this)
      if (min === 0)
        return n1 - n2 | 0
       start = 0
      $l$break: while (true) :
         tmp0_minOf_0 = start + 16 | 0
         end = def () :
           $externalVarargReceiverTmp = Math
          return $externalVarargReceiverTmp.min.apply($externalVarargReceiverTmp, [].concat([].slice.call(new Int32Array([tmp0_minOf_0, min]))))
        .call(this)
         tmp1_substring_0 = start
         s1 = _this_.substring(tmp1_substring_0, end)
         tmp2_substring_0 = start
         s2 = other.substring(tmp2_substring_0, end)
        if (!(s1 === s2)) :
           tmp3_toUpperCase_0 = s1
          s1 = tmp3_toUpperCase_0.toUpperCase()
           tmp4_toUpperCase_0 = s2
          s2 = tmp4_toUpperCase_0.toUpperCase()
          if (!(s1 === s2)) :
             tmp5_toLowerCase_0 = s1
            s1 = tmp5_toLowerCase_0.toLowerCase()
             tmp6_toLowerCase_0 = s2
            s2 = tmp6_toLowerCase_0.toLowerCase()
            if (!(s1 === s2)) :
              return compareTo_0(s1, s2)
        if (end === min)
          break $l$break
        start = end

      return n1 - n2 | 0
     else :
      return compareTo_0(_this_, other)


  def compareTo$default(_this_, other, ignoreCase, $mask0, $handler) :
    if (!(($mask0 & 2) === 0))
      ignoreCase = false
    return compareTo(_this_, other, ignoreCase)

  def toUpperCase(_this_) :
    return _this_.toUpperCase()

  def toLowerCase(_this_) :
    return _this_.toLowerCase()

  def concatToString(_this_) :
     result = ''
     indexedObject = _this_
     inductionVariable = 0
     last = indexedObject.length
    while (inductionVariable < last) :
       char = indexedObject[inductionVariable]
      inductionVariable = inductionVariable + 1 | 0
      result = result + char

    return result

  def concatToString_0(_this_, startIndex, endIndex) :
    Companion_getInstance().checkBoundsIndexes(startIndex, endIndex, _this_.length)
     result = ''
     inductionVariable = startIndex
    if (inductionVariable < endIndex)
      do :
         index = inductionVariable
        inductionVariable = inductionVariable + 1 | 0
        result = result + _this_[index]

       while (inductionVariable < endIndex)
    return result

  def concatToString$default(_this_, startIndex, endIndex, $mask0, $handler) :
    if (!(($mask0 & 1) === 0))
      startIndex = 0
    if (!(($mask0 & 2) === 0))
      endIndex = _this_.length
    return concatToString_0(_this_, startIndex, endIndex)

  def sam$kotlin_Comparator$0(function_0) :
    this._function = function_0

  sam$kotlin_Comparator$0.prototype.compare_0 = def (a, b) :
    return this._function(a, b)

  sam$kotlin_Comparator$0.prototype.compare = def (a, b) :
    return this.compare_0(a, b)

  sam$kotlin_Comparator$0.$metadata$ = {
    simpleName: 'sam$kotlin_Comparator$0',
    kind: 'class',
    interfaces: [Comparator]

  def _no_name_provided__29() :

  _no_name_provided__29.prototype.invoke_63 = def (a, b) :
    return compareTo(a, b, true)

  _no_name_provided__29.prototype.invoke_64 = def (p1, p2) :
     tmp = (!(p1 == null) ? typeof p1 === 'string' : false) ? p1 : THROW_CCE()
    return this.invoke_63(tmp, (!(p2 == null) ? typeof p2 === 'string' : false) ? p2 : THROW_CCE())

  _no_name_provided__29.$metadata$ = {
    kind: 'class',
    interfaces: []

  def _no_name_provided_$factory_28() :
     i = new _no_name_provided__29()
    return def (p1, p2) :
      return i.invoke_63(p1, p2)


  def STRING_CASE_INSENSITIVE_ORDER$init$() :
     tmp = _no_name_provided_$factory_28()
    return new sam$kotlin_Comparator$0(tmp)

  def _get_REPLACEMENT_BYTE_SEQUENCE_() :
    return REPLACEMENT_BYTE_SEQUENCE

   REPLACEMENT_BYTE_SEQUENCE
  def REPLACEMENT_BYTE_SEQUENCE$init$() :
     tmp0_byteArrayOf_0 = new Int8Array([-17, -65, -67])
    return tmp0_byteArrayOf_0

  def _get_value_($this) :
    return $this._value_1

  def Companion_18() :
    Companion_instance_17 = this
    this._MIN_VALUE_8 = new Char(0)
    this._MAX_VALUE_8 = new Char(65535)
    this._MIN_HIGH_SURROGATE = new Char(55296)
    this._MAX_HIGH_SURROGATE = new Char(56319)
    this._MIN_LOW_SURROGATE = new Char(56320)
    this._MAX_LOW_SURROGATE = new Char(57343)
    this._MIN_SURROGATE = new Char(55296)
    this._MAX_SURROGATE = new Char(57343)
    this._SIZE_BYTES_8 = 2
    this._SIZE_BITS_8 = 16

  Companion_18.prototype._get_MIN_VALUE__9 = def () :
    return this._MIN_VALUE_8

  Companion_18.prototype._get_MAX_VALUE__9 = def () :
    return this._MAX_VALUE_8

  Companion_18.prototype._get_MIN_HIGH_SURROGATE_ = def () :
    return this._MIN_HIGH_SURROGATE

  Companion_18.prototype._get_MAX_HIGH_SURROGATE_ = def () :
    return this._MAX_HIGH_SURROGATE

  Companion_18.prototype._get_MIN_LOW_SURROGATE_ = def () :
    return this._MIN_LOW_SURROGATE

  Companion_18.prototype._get_MAX_LOW_SURROGATE_ = def () :
    return this._MAX_LOW_SURROGATE

  Companion_18.prototype._get_MIN_SURROGATE_ = def () :
    return this._MIN_SURROGATE

  Companion_18.prototype._get_MAX_SURROGATE_ = def () :
    return this._MAX_SURROGATE

  Companion_18.prototype._get_SIZE_BYTES__9 = def () :
    return this._SIZE_BYTES_8

  Companion_18.prototype._get_SIZE_BITS__9 = def () :
    return this._SIZE_BITS_8

  Companion_18.$metadata$ = {
    simpleName: 'Companion',
    kind: 'object',
    interfaces: []

   Companion_instance_17
  def Companion_getInstance_17() :
    if (Companion_instance_17 == null)
      new Companion_18()
    return Companion_instance_17

  def Char(value) :
    Companion_getInstance_17()
    this._value_1 = value

  Char.prototype.compareTo_17 = def (other) :
    return this._value_1 - other._value_1 | 0

  Char.prototype.compareTo_25 = def (other) :
    return this.compareTo_17(other instanceof Char ? other : THROW_CCE())

  Char.prototype.plus_37 = def (other) :
    return numberToChar(this._value_1 + other | 0)

  Char.prototype.minus = def (other) :
    return this._value_1 - other._value_1 | 0

  Char.prototype.minus_33 = def (other) :
    return numberToChar(this._value_1 - other | 0)

  Char.prototype.inc_5 = def () :
    return numberToChar(this._value_1 + 1 | 0)

  Char.prototype.dec_5 = def () :
    return numberToChar(this._value_1 - 1 | 0)

  Char.prototype.rangeTo = def (other) :
    return new CharRange(this, other)

  Char.prototype.toByte_6 = def () :
    return toByte(this._value_1)

  Char.prototype.toChar_6 = def () :
    return this

  Char.prototype.toShort_6 = def () :
    return toShort(this._value_1)

  Char.prototype.toInt_6 = def () :
    return this._value_1

  Char.prototype.toLong_6 = def () :
    return toLong(this._value_1)

  Char.prototype.toFloat_6 = def () :
    return this._value_1

  Char.prototype.toDouble_6 = def () :
    return this._value_1

  Char.prototype.equals = def (other) :
    if (other === this)
      return true
    if (!(other instanceof Char))
      return false;
    else :

    return this._value_1 === other._value_1

  Char.prototype.hashCode = def () :
    return this._value_1

  Char.prototype.toString = def () :
     tmp0_unsafeCast_0 = String.fromCharCode(this._value_1)
    return tmp0_unsafeCast_0

  Char.$metadata$ = {
    simpleName: 'Char',
    kind: 'class',
    interfaces: [Comparable]

  def Iterable() :

  Iterable.$metadata$ = {
    simpleName: 'Iterable',
    kind: 'interface',
    interfaces: []

  def Collection() :

  Collection.$metadata$ = {
    simpleName: 'Collection',
    kind: 'interface',
    interfaces: [Iterable]

  def Set() :

  Set.$metadata$ = {
    simpleName: 'Set',
    kind: 'interface',
    interfaces: [Collection]

  def List() :

  List.$metadata$ = {
    simpleName: 'List',
    kind: 'interface',
    interfaces: [Collection]

  def Entry() :

  Entry.$metadata$ = {
    simpleName: 'Entry',
    kind: 'interface',
    interfaces: []

  def Map_0() :

  Map_0.$metadata$ = {
    simpleName: 'Map',
    kind: 'interface',
    interfaces: []

  def MutableCollection() :

  MutableCollection.$metadata$ = {
    simpleName: 'MutableCollection',
    kind: 'interface',
    interfaces: [Collection, MutableIterable]

  def MutableIterable() :

  MutableIterable.$metadata$ = {
    simpleName: 'MutableIterable',
    kind: 'interface',
    interfaces: [Iterable]

  def MutableSet() :

  MutableSet.$metadata$ = {
    simpleName: 'MutableSet',
    kind: 'interface',
    interfaces: [Set, MutableCollection]

  def MutableList() :

  MutableList.$metadata$ = {
    simpleName: 'MutableList',
    kind: 'interface',
    interfaces: [List, MutableCollection]

  def MutableEntry() :

  MutableEntry.$metadata$ = {
    simpleName: 'MutableEntry',
    kind: 'interface',
    interfaces: [Entry]

  def MutableMap() :

  MutableMap.$metadata$ = {
    simpleName: 'MutableMap',
    kind: 'interface',
    interfaces: [Map_0]

  def Companion_19() :
    Companion_instance_18 = this

  Companion_19.$metadata$ = {
    simpleName: 'Companion',
    kind: 'object',
    interfaces: []

   Companion_instance_18
  def Companion_getInstance_18() :
    if (Companion_instance_18 == null)
      new Companion_19()
    return Companion_instance_18

  def Enum(name, ordinal) :
    Companion_getInstance_18()
    this._name_2 = name
    this._ordinal = ordinal

  Enum.prototype._get_name__22 = def () :
    return this._name_2

  Enum.prototype._get_ordinal__8 = def () :
    return this._ordinal

  Enum.prototype.compareTo_19 = def (other) :
    return compareTo_0(this._ordinal, other._ordinal)

  Enum.prototype.compareTo_25 = def (other) :
    return this.compareTo_19(other instanceof Enum ? other : THROW_CCE())

  Enum.prototype.equals = def (other) :
    return this === other

  Enum.prototype.hashCode = def () :
    return identityHashCode(this)

  Enum.prototype.toString = def () :
    return this._name_2

  Enum.$metadata$ = {
    simpleName: 'Enum',
    kind: 'class',
    interfaces: [Comparable]

  def byteArrayOf(elements) :
    return elements

  def arrayOf(elements) :
    return elements

  def plus(_this_, other) :
     tmp2_safe_receiver = _this_
     tmp3_elvis_lhs = tmp2_safe_receiver == null ? null : toString_0(tmp2_safe_receiver)
     tmp = tmp3_elvis_lhs == null ? 'null' : tmp3_elvis_lhs
     tmp0_safe_receiver = other
     tmp1_elvis_lhs = tmp0_safe_receiver == null ? null : toString_0(tmp0_safe_receiver)
    return tmp + (tmp1_elvis_lhs == null ? 'null' : tmp1_elvis_lhs)

  def toString(_this_) :
     tmp0_safe_receiver = _this_
     tmp1_elvis_lhs = tmp0_safe_receiver == null ? null : toString_0(tmp0_safe_receiver)
    return tmp1_elvis_lhs == null ? 'null' : tmp1_elvis_lhs

  def booleanArrayOf(elements) :
    return elements

  def charArrayOf(elements) :
    return elements

  def shortArrayOf(elements) :
    return elements

  def intArrayOf(elements) :
    return elements

  def floatArrayOf(elements) :
    return elements

  def longArrayOf(elements) :
    return elements

  def doubleArrayOf(elements) :
    return elements

  def DefaultConstructorMarker() :
    DefaultConstructorMarker_instance = this

  DefaultConstructorMarker.$metadata$ = {
    simpleName: 'DefaultConstructorMarker',
    kind: 'object',
    interfaces: []

   DefaultConstructorMarker_instance
  def DefaultConstructorMarker_getInstance() :
    if (DefaultConstructorMarker_instance == null)
      new DefaultConstructorMarker()
    return DefaultConstructorMarker_instance

  def fillArrayVal(array, initValue) :
     inductionVariable = 0
     last = array.length - 1 | 0
    if (inductionVariable <= last)
      do :
         i = inductionVariable
        inductionVariable = inductionVariable + 1 | 0
        array[i] = initValue

       while (!(i === last))
    return array

  def arrayWithFun(size_0, init) :
     tmp0_fillArrayFun_0 = Array(size_0)
     result_1 = tmp0_fillArrayFun_0
     i_2 = 0
    while (!(i_2 === result_1.length)) :
      result_1[i_2] = init(i_2)
      i_2 = i_2 + 1 | 0
      Unit_getInstance()

    return result_1

  def fillArrayFun(array, init) :
     result = array
     i = 0
    while (!(i === result.length)) :
      result[i] = init(i)
      i = i + 1 | 0
      Unit_getInstance()

    return result

  def arrayIterator(array) :
    return new _no_name_provided__30(array)

  def booleanArrayIterator(array) :
    return new _no_name_provided__31(array)

  def charArrayIterator(array) :
    return new _no_name_provided__32(array)

  def byteArrayIterator(array) :
    return new _no_name_provided__33(array)

  def shortArrayIterator(array) :
    return new _no_name_provided__34(array)

  def intArrayIterator(array) :
    return new _no_name_provided__35(array)

  def floatArrayIterator(array) :
    return new _no_name_provided__36(array)

  def longArrayIterator(array) :
    return new _no_name_provided__37(array)

  def doubleArrayIterator(array) :
    return new _no_name_provided__38(array)

  def booleanArray(size_0) :
     tmp0_withType_0 = 'BooleanArray'
     tmp1_withType_0 = fillArrayVal(Array(size_0), false)
    tmp1_withType_0.$type$ = tmp0_withType_0
     tmp2_unsafeCast_0 = tmp1_withType_0
    return tmp2_unsafeCast_0

  def charArray(size_0) :
     tmp0_withType_0 = 'CharArray'
     tmp1_withType_0 = fillArrayVal(Array(size_0), new Char(0))
    tmp1_withType_0.$type$ = tmp0_withType_0
     tmp2_unsafeCast_0 = tmp1_withType_0
    return tmp2_unsafeCast_0

  def longArray(size_0) :
     tmp0_withType_0 = 'LongArray'
     tmp1_withType_0 = fillArrayVal(Array(size_0), new Long(0, 0))
    tmp1_withType_0.$type$ = tmp0_withType_0
     tmp2_unsafeCast_0 = tmp1_withType_0
    return tmp2_unsafeCast_0

  def booleanArrayOf_0(arr) :
     tmp0_withType_0 = 'BooleanArray'
     tmp1_withType_0 = arr.slice()
    tmp1_withType_0.$type$ = tmp0_withType_0
     tmp2_unsafeCast_0 = tmp1_withType_0
    return tmp2_unsafeCast_0

  def charArrayOf_0(arr) :
     tmp0_withType_0 = 'CharArray'
     tmp1_withType_0 = arr.slice()
    tmp1_withType_0.$type$ = tmp0_withType_0
     tmp2_unsafeCast_0 = tmp1_withType_0
    return tmp2_unsafeCast_0

  def longArrayOf_0(arr) :
     tmp0_withType_0 = 'LongArray'
     tmp1_withType_0 = arr.slice()
    tmp1_withType_0.$type$ = tmp0_withType_0
     tmp2_unsafeCast_0 = tmp1_withType_0
    return tmp2_unsafeCast_0

  def _no_name_provided__30($array) :
    this._$array = $array
    this._index_5 = 0

  _no_name_provided__30.prototype._set_index__11 = def (_set___) :
    this._index_5 = _set___

  _no_name_provided__30.prototype._get_index__11 = def () :
    return this._index_5

  _no_name_provided__30.prototype.hasNext_37 = def () :
    return !(this._index_5 === this._$array.length)

  _no_name_provided__30.prototype.next_41 = def () :
     tmp
    if (!(this._index_5 === this._$array.length)) :
       tmp0_this = this
       tmp1 = tmp0_this._index_5
      tmp0_this._index_5 = tmp1 + 1 | 0
      tmp = this._$array[tmp1]
     else :
      throw NoSuchElementException_init_$Create$_0('' + this._index_5)

    return tmp

  _no_name_provided__30.$metadata$ = {
    kind: 'class',
    interfaces: [Iterator_3]

  def _no_name_provided__31($array) :
    this._$array_0 = $array
    BooleanIterator.call(this)
    this._index_6 = 0

  _no_name_provided__31.prototype._set_index__11 = def (_set___) :
    this._index_6 = _set___

  _no_name_provided__31.prototype._get_index__11 = def () :
    return this._index_6

  _no_name_provided__31.prototype.hasNext_37 = def () :
    return !(this._index_6 === this._$array_0.length)

  _no_name_provided__31.prototype.nextBoolean_0 = def () :
     tmp
    if (!(this._index_6 === this._$array_0.length)) :
       tmp0_this = this
       tmp1 = tmp0_this._index_6
      tmp0_this._index_6 = tmp1 + 1 | 0
      tmp = this._$array_0[tmp1]
     else :
      throw NoSuchElementException_init_$Create$_0('' + this._index_6)

    return tmp

  _no_name_provided__31.$metadata$ = {
    kind: 'class',
    interfaces: []

  def _no_name_provided__32($array) :
    this._$array_1 = $array
    CharIterator.call(this)
    this._index_7 = 0

  _no_name_provided__32.prototype._set_index__11 = def (_set___) :
    this._index_7 = _set___

  _no_name_provided__32.prototype._get_index__11 = def () :
    return this._index_7

  _no_name_provided__32.prototype.hasNext_37 = def () :
    return !(this._index_7 === this._$array_1.length)

  _no_name_provided__32.prototype.nextChar_1 = def () :
     tmp
    if (!(this._index_7 === this._$array_1.length)) :
       tmp0_this = this
       tmp1 = tmp0_this._index_7
      tmp0_this._index_7 = tmp1 + 1 | 0
      tmp = this._$array_1[tmp1]
     else :
      throw NoSuchElementException_init_$Create$_0('' + this._index_7)

    return tmp

  _no_name_provided__32.$metadata$ = {
    kind: 'class',
    interfaces: []

  def _no_name_provided__33($array) :
    this._$array_2 = $array
    ByteIterator.call(this)
    this._index_8 = 0

  _no_name_provided__33.prototype._set_index__11 = def (_set___) :
    this._index_8 = _set___

  _no_name_provided__33.prototype._get_index__11 = def () :
    return this._index_8

  _no_name_provided__33.prototype.hasNext_37 = def () :
    return !(this._index_8 === this._$array_2.length)

  _no_name_provided__33.prototype.nextByte_0 = def () :
     tmp
    if (!(this._index_8 === this._$array_2.length)) :
       tmp0_this = this
       tmp1 = tmp0_this._index_8
      tmp0_this._index_8 = tmp1 + 1 | 0
      tmp = this._$array_2[tmp1]
     else :
      throw NoSuchElementException_init_$Create$_0('' + this._index_8)

    return tmp

  _no_name_provided__33.$metadata$ = {
    kind: 'class',
    interfaces: []

  def _no_name_provided__34($array) :
    this._$array_3 = $array
    ShortIterator.call(this)
    this._index_9 = 0

  _no_name_provided__34.prototype._set_index__11 = def (_set___) :
    this._index_9 = _set___

  _no_name_provided__34.prototype._get_index__11 = def () :
    return this._index_9

  _no_name_provided__34.prototype.hasNext_37 = def () :
    return !(this._index_9 === this._$array_3.length)

  _no_name_provided__34.prototype.nextShort_0 = def () :
     tmp
    if (!(this._index_9 === this._$array_3.length)) :
       tmp0_this = this
       tmp1 = tmp0_this._index_9
      tmp0_this._index_9 = tmp1 + 1 | 0
      tmp = this._$array_3[tmp1]
     else :
      throw NoSuchElementException_init_$Create$_0('' + this._index_9)

    return tmp

  _no_name_provided__34.$metadata$ = {
    kind: 'class',
    interfaces: []

  def _no_name_provided__35($array) :
    this._$array_4 = $array
    IntIterator.call(this)
    this._index_10 = 0

  _no_name_provided__35.prototype._set_index__11 = def (_set___) :
    this._index_10 = _set___

  _no_name_provided__35.prototype._get_index__11 = def () :
    return this._index_10

  _no_name_provided__35.prototype.hasNext_37 = def () :
    return !(this._index_10 === this._$array_4.length)

  _no_name_provided__35.prototype.nextInt_1 = def () :
     tmp
    if (!(this._index_10 === this._$array_4.length)) :
       tmp0_this = this
       tmp1 = tmp0_this._index_10
      tmp0_this._index_10 = tmp1 + 1 | 0
      tmp = this._$array_4[tmp1]
     else :
      throw NoSuchElementException_init_$Create$_0('' + this._index_10)

    return tmp

  _no_name_provided__35.$metadata$ = {
    kind: 'class',
    interfaces: []

  def _no_name_provided__36($array) :
    this._$array_5 = $array
    FloatIterator.call(this)
    this._index_11 = 0

  _no_name_provided__36.prototype._set_index__11 = def (_set___) :
    this._index_11 = _set___

  _no_name_provided__36.prototype._get_index__11 = def () :
    return this._index_11

  _no_name_provided__36.prototype.hasNext_37 = def () :
    return !(this._index_11 === this._$array_5.length)

  _no_name_provided__36.prototype.nextFloat_0 = def () :
     tmp
    if (!(this._index_11 === this._$array_5.length)) :
       tmp0_this = this
       tmp1 = tmp0_this._index_11
      tmp0_this._index_11 = tmp1 + 1 | 0
      tmp = this._$array_5[tmp1]
     else :
      throw NoSuchElementException_init_$Create$_0('' + this._index_11)

    return tmp

  _no_name_provided__36.$metadata$ = {
    kind: 'class',
    interfaces: []

  def _no_name_provided__37($array) :
    this._$array_6 = $array
    LongIterator.call(this)
    this._index_12 = 0

  _no_name_provided__37.prototype._set_index__11 = def (_set___) :
    this._index_12 = _set___

  _no_name_provided__37.prototype._get_index__11 = def () :
    return this._index_12

  _no_name_provided__37.prototype.hasNext_37 = def () :
    return !(this._index_12 === this._$array_6.length)

  _no_name_provided__37.prototype.nextLong_1 = def () :
     tmp
    if (!(this._index_12 === this._$array_6.length)) :
       tmp0_this = this
       tmp1 = tmp0_this._index_12
      tmp0_this._index_12 = tmp1 + 1 | 0
      tmp = this._$array_6[tmp1]
     else :
      throw NoSuchElementException_init_$Create$_0('' + this._index_12)

    return tmp

  _no_name_provided__37.$metadata$ = {
    kind: 'class',
    interfaces: []

  def _no_name_provided__38($array) :
    this._$array_7 = $array
    DoubleIterator.call(this)
    this._index_13 = 0

  _no_name_provided__38.prototype._set_index__11 = def (_set___) :
    this._index_13 = _set___

  _no_name_provided__38.prototype._get_index__11 = def () :
    return this._index_13

  _no_name_provided__38.prototype.hasNext_37 = def () :
    return !(this._index_13 === this._$array_7.length)

  _no_name_provided__38.prototype.nextDouble_0 = def () :
     tmp
    if (!(this._index_13 === this._$array_7.length)) :
       tmp0_this = this
       tmp1 = tmp0_this._index_13
      tmp0_this._index_13 = tmp1 + 1 | 0
      tmp = this._$array_7[tmp1]
     else :
      throw NoSuchElementException_init_$Create$_0('' + this._index_13)

    return tmp

  _no_name_provided__38.$metadata$ = {
    kind: 'class',
    interfaces: []

  def _get_buf_() :
    return buf

   buf
  def _get_bufFloat64_() :
    return bufFloat64

   bufFloat64
  def _get_bufFloat32_() :
    return bufFloat32

   bufFloat32
  def _get_bufInt32_() :
    return bufInt32

   bufInt32
  def _get_lowIndex_() :
    return lowIndex

   lowIndex
  def _get_highIndex_() :
    return highIndex

   highIndex
  def getNumberHashCode(obj) :
     tmp0_unsafeCast_0 = jsBitwiseOr(obj, 0)
    if (tmp0_unsafeCast_0 === obj) :
      return numberToInt(obj)
     else :

    bufFloat64[0] = obj
    return imul(bufInt32[highIndex], 31) + bufInt32[lowIndex] | 0

  def bufFloat64$init$() :
     tmp0_unsafeCast_0 = new Float64Array(buf)
    return tmp0_unsafeCast_0

  def bufFloat32$init$() :
     tmp0_unsafeCast_0 = new Float32Array(buf)
    return tmp0_unsafeCast_0

  def bufInt32$init$() :
     tmp0_unsafeCast_0 = new Int32Array(buf)
    return tmp0_unsafeCast_0

  def lowIndex$init$() :
    bufFloat64[0] = -1.0
    return !(bufInt32[0] === 0) ? 1 : 0

  def DoNotIntrinsify() :

  DoNotIntrinsify.$metadata$ = {
    simpleName: 'DoNotIntrinsify',
    kind: 'class',
    interfaces: [Annotation]

  def charSequenceGet(a, index) :
     tmp
    if (isString(a)) :
       tmp0_unsafeCast_0 = a.charCodeAt(index)
      tmp = new Char(tmp0_unsafeCast_0)
     else :
      tmp = a.get_31(index)

    return tmp

  def isString(a) :
    return typeof a === 'string'

  def charSequenceLength(a) :
     tmp
    if (isString(a)) :
       tmp0_unsafeCast_0 = a.length
      tmp = tmp0_unsafeCast_0
     else :
      tmp = a._get_length__0()

    return tmp

  def charSequenceSubSequence(a, startIndex, endIndex) :
     tmp
    if (isString(a)) :
       tmp0_unsafeCast_0 = a.substring(startIndex, endIndex)
      tmp = tmp0_unsafeCast_0
     else :
      tmp = a.subSequence_1(startIndex, endIndex)

    return tmp

  def arrayToString(array) :
    return joinToString$default(array, ', ', '[', ']', 0, null, _no_name_provided_$factory_29(), 24, null)

  def _no_name_provided__39() :

  _no_name_provided__39.prototype.invoke_65 = def (it) :
    return toString_0(it)

  _no_name_provided__39.prototype.invoke_66 = def (p1) :
    return this.invoke_65((p1 == null ? true : isObject(p1)) ? p1 : THROW_CCE())

  _no_name_provided__39.$metadata$ = {
    kind: 'class',
    interfaces: []

  def _no_name_provided_$factory_29() :
     i = new _no_name_provided__39()
    return def (p1) :
      return i.invoke_65(p1)


  def compareTo_0(a, b) :
     tmp0_subject = typeof a
     tmp
    switch (tmp0_subject) :
      case 'number':
         tmp_0;
        if (typeof b === 'number') :
          tmp_0 = doubleCompareTo(a, b)
         else :
          if (b instanceof Long) :
            tmp_0 = doubleCompareTo(a, b.toDouble_6())
           else :
            :
              tmp_0 = primitiveCompareTo(a, b)




        tmp = tmp_0;
        break;
      case 'string':
      case 'boolean':
        tmp = primitiveCompareTo(a, b);
        break;
      default:tmp = compareToDoNotIntrinsicify(a, b);
        break;

    return tmp

  def doubleCompareTo(a, b) :
     tmp
    if (a < b) :
      tmp = -1
     else if (a > b) :
      tmp = 1
     else if (a === b) :
       tmp_0
      if (a !== 0) :
        tmp_0 = 0
       else :
         tmp0_asDynamic_0 = 1
         ia = tmp0_asDynamic_0 / a
         tmp_1
         tmp1_asDynamic_0 = 1
        if (ia === tmp1_asDynamic_0 / b) :
          tmp_1 = 0
         else :
          if (ia < 0) :
            tmp_1 = -1
           else :
            :
              tmp_1 = 1



        tmp_0 = tmp_1

      tmp = tmp_0
     else if (a !== a) :
      tmp = b !== b ? 0 : 1
     else :
      tmp = -1

    return tmp

  def primitiveCompareTo(a, b) :
    return a < b ? -1 : a > b ? 1 : 0

  def compareToDoNotIntrinsicify(a, b) :
    return a.compareTo_25(b)

  def construct(constructorType, resultType, args) :
    return Reflect.construct(constructorType, args, resultType)

  def identityHashCode(obj) :
    return getObjectHashCode(obj)

  def getObjectHashCode(obj) :
    if (!jsIn('kotlinHashCodeValue$', obj)) :
       hash = jsBitwiseOr(Math.random() * 4.294967296E9, 0)
       descriptor = new Object()
      descriptor.value = hash
      descriptor.enumerable = false
      Object.defineProperty(obj, 'kotlinHashCodeValue$', descriptor)
     tmp0_unsafeCast_0 = obj['kotlinHashCodeValue$']
    return tmp0_unsafeCast_0

  def _get_OBJECT_HASH_CODE_PROPERTY_NAME_() :
    return OBJECT_HASH_CODE_PROPERTY_NAME

   OBJECT_HASH_CODE_PROPERTY_NAME
  def _get_POW_2_32_() :
    return POW_2_32

   POW_2_32
  def hashCode(obj) :
    if (obj == null)
      return 0
     tmp0_subject = typeof obj
     tmp
    switch (tmp0_subject) :
      case 'object':
        tmp = 'function' === typeof obj.hashCode ? obj.hashCode() : getObjectHashCode(obj);
        break;
      case 'function':
        tmp = getObjectHashCode(obj);
        break;
      case 'number':
        tmp = getNumberHashCode(obj);
        break;
      case 'boolean':
         tmp_0;
        if (obj) :
          tmp_0 = 1
         else :
          :
            tmp_0 = 0



        tmp = tmp_0;
        break;
      default:tmp = getStringHashCode(String(obj));
        break;

    return tmp

  def getStringHashCode(str) :
     hash = 0
     length = str.length
     inductionVariable = 0
     last = length - 1 | 0
    if (inductionVariable <= last)
      do :
         i = inductionVariable
        inductionVariable = inductionVariable + 1 | 0
         code = str.charCodeAt(i)
        hash = imul(hash, 31) + code | 0

       while (!(i === last))
    return hash

  def toString_0(o) :
     tmp
    if (o == null) :
      tmp = 'null'
     else if (isArrayish(o)) :
      tmp = '[...]'
     else :
       tmp0_unsafeCast_0 = o.toString()
      tmp = tmp0_unsafeCast_0

    return tmp

  def anyToString(o) :
    return Object.prototype.toString.call(o)

  def equals(obj1, obj2) :
    if (obj1 == null) :
      return obj2 == null
    if (obj2 == null) :
      return false
    if (typeof obj1 === 'object' ? typeof obj1.equals === 'function' : false) :
      return obj1.equals(obj2)
    if (obj1 !== obj1) :
      return obj2 !== obj2
    if (typeof obj1 === 'number' ? typeof obj2 === 'number' : false) :
       tmp
      if (obj1 === obj2) :
         tmp_0
        if (obj1 !== 0) :
          tmp_0 = true
         else :
           tmp0_asDynamic_0 = 1
           tmp_1 = tmp0_asDynamic_0 / obj1
           tmp1_asDynamic_0 = 1
          tmp_0 = tmp_1 === tmp1_asDynamic_0 / obj2

        tmp = tmp_0
       else :
        tmp = false

      return tmp
    return obj1 === obj2

  def boxIntrinsic(x) :
     tmp0_error_0 = 'Should be lowered'
    throw IllegalStateException_init_$Create$_0(toString_0(tmp0_error_0))

  def unboxIntrinsic(x) :
     tmp0_error_0 = 'Should be lowered'
    throw IllegalStateException_init_$Create$_0(toString_0(tmp0_error_0))

  def captureStack(instance, constructorFunction) :
    if (Error.captureStackTrace != null) :
      Error.captureStackTrace(instance, constructorFunction)
     else :
      instance.stack = (new Error()).stack


  def newThrowable(message, cause) :
     throwable = new Error()
     tmp
    if (isUndefined(message)) :
       tmp_0
      if (isUndefined(cause)) :
        tmp_0 = message
       else :
         tmp0_safe_receiver = cause
         tmp1_elvis_lhs = tmp0_safe_receiver == null ? null : tmp0_safe_receiver.toString()
        tmp_0 = tmp1_elvis_lhs == null ? undefined : tmp1_elvis_lhs

      tmp = tmp_0
     else :
       tmp2_elvis_lhs = message
      tmp = tmp2_elvis_lhs == null ? undefined : tmp2_elvis_lhs

    throwable.message = tmp
    throwable.cause = cause
    throwable.name = 'Throwable'
    return throwable

  def isUndefined(value) :
    return value === undefined

  def extendThrowable(this_, message, cause) :
    Error.call(this_)
    setPropertiesToThrowableInstance(this_, message, cause)

  def setPropertiesToThrowableInstance(this_, message, cause) :
    if (!hasOwnPrototypeProperty(this_, 'message')) :
       tmp
      if (message == null) :
         tmp_0
        if (!(message === null)) :
           tmp0_safe_receiver = cause
           tmp1_elvis_lhs = tmp0_safe_receiver == null ? null : tmp0_safe_receiver.toString()
          tmp_0 = tmp1_elvis_lhs == null ? undefined : tmp1_elvis_lhs
         else :
          tmp_0 = undefined

        tmp = tmp_0
       else :
        tmp = message

      this_.message = tmp
    if (!hasOwnPrototypeProperty(this_, 'cause')) :
      this_.cause = cause
    this_.name = Object.getPrototypeOf(this_).constructor.name

  def hasOwnPrototypeProperty(o, name) :
     tmp0_unsafeCast_0 = Object.getPrototypeOf(o).hasOwnProperty(name)
    return tmp0_unsafeCast_0

  def getContinuation() :
    throw Exception_init_$Create$_0('Implemented as intrinsic')

  def returnIfSuspended(argument, $cont) :
    throw Exception_init_$Create$_0('Implemented as intrinsic')

  def suspendCoroutineUninterceptedOrReturnJS(block, $cont) :
    return block($cont)

  def getCoroutineContext($cont) :
    return $cont._get_context__4()

  def ensureNotNull(v) :
     tmp
    if (v == null) :
      THROW_NPE()
     else :
      tmp = v

    return tmp

  def THROW_NPE() :
    throw NullPointerException_init_$Create$()

  def noWhenBranchMatchedException() :
    throw NoWhenBranchMatchedException_init_$Create$()

  def THROW_CCE() :
    throw ClassCastException_init_$Create$()

  def throwUninitializedPropertyAccessException(name) :
    throw UninitializedPropertyAccessException_init_$Create$_0('' + 'lateinit property ' + name + ' has not been initialized')

  def throwKotlinNothingValueException() :
    throw KotlinNothingValueException_init_$Create$()

  def THROW_ISE() :
    throw IllegalStateException_init_$Create$()

  def THROW_IAE(msg) :
    throw IllegalArgumentException_init_$Create$_0(msg)

  def emptyArray() :
    return []

  def enumValueOfIntrinsic(name) :
    throw IllegalStateException_init_$Create$_0('Should be replaced by compiler')

  def enumValuesIntrinsic() :
    throw IllegalStateException_init_$Create$_0('Should be replaced by compiler')

  def Companion_20() :
    Companion_instance_19 = this
    this._MIN_VALUE_9 = new Long(0, -2147483648)
    this._MAX_VALUE_9 = new Long(-1, 2147483647)
    this._SIZE_BYTES_9 = 8
    this._SIZE_BITS_9 = 64

  Companion_20.prototype._get_MIN_VALUE__9 = def () :
    return this._MIN_VALUE_9

  Companion_20.prototype._get_MAX_VALUE__9 = def () :
    return this._MAX_VALUE_9

  Companion_20.prototype._get_SIZE_BYTES__9 = def () :
    return this._SIZE_BYTES_9

  Companion_20.prototype._get_SIZE_BITS__9 = def () :
    return this._SIZE_BITS_9

  Companion_20.$metadata$ = {
    simpleName: 'Companion',
    kind: 'object',
    interfaces: []

   Companion_instance_19
  def Companion_getInstance_19() :
    if (Companion_instance_19 == null)
      new Companion_20()
    return Companion_instance_19

  def Long(low, high) :
    Companion_getInstance_19()
    Number_0.call(this)
    this._low = low
    this._high = high

  Long.prototype._get_low_ = def () :
    return this._low

  Long.prototype._get_high_ = def () :
    return this._high

  Long.prototype.compareTo_53 = def (other) :
    return this.compareTo_56(toLong(other))

  Long.prototype.compareTo_54 = def (other) :
    return this.compareTo_56(toLong(other))

  Long.prototype.compareTo_55 = def (other) :
    return this.compareTo_56(toLong(other))

  Long.prototype.compareTo_56 = def (other) :
    return compare(this, other)

  Long.prototype.compareTo_25 = def (other) :
    return this.compareTo_56(other instanceof Long ? other : THROW_CCE())

  Long.prototype.compareTo_57 = def (other) :
    return compareTo_0(this.toFloat_6(), other)

  Long.prototype.compareTo_58 = def (other) :
    return compareTo_0(this.toDouble_6(), other)

  Long.prototype.plus_35 = def (other) :
    return this.plus_38(toLong(other))

  Long.prototype.plus_36 = def (other) :
    return this.plus_38(toLong(other))

  Long.prototype.plus_37 = def (other) :
    return this.plus_38(toLong(other))

  Long.prototype.plus_38 = def (other) :
    return add(this, other)

  Long.prototype.plus_39 = def (other) :
    return this.toFloat_6() + other

  Long.prototype.plus_40 = def (other) :
    return this.toDouble_6() + other

  Long.prototype.minus_31 = def (other) :
    return this.minus_34(toLong(other))

  Long.prototype.minus_32 = def (other) :
    return this.minus_34(toLong(other))

  Long.prototype.minus_33 = def (other) :
    return this.minus_34(toLong(other))

  Long.prototype.minus_34 = def (other) :
    return subtract(this, other)

  Long.prototype.minus_35 = def (other) :
    return this.toFloat_6() - other

  Long.prototype.minus_36 = def (other) :
    return this.toDouble_6() - other

  Long.prototype.times_29 = def (other) :
    return this.times_32(toLong(other))

  Long.prototype.times_30 = def (other) :
    return this.times_32(toLong(other))

  Long.prototype.times_31 = def (other) :
    return this.times_32(toLong(other))

  Long.prototype.times_32 = def (other) :
    return multiply(this, other)

  Long.prototype.times_33 = def (other) :
    return this.toFloat_6() * other

  Long.prototype.times_34 = def (other) :
    return this.toDouble_6() * other

  Long.prototype.div_29 = def (other) :
    return this.div_32(toLong(other))

  Long.prototype.div_30 = def (other) :
    return this.div_32(toLong(other))

  Long.prototype.div_31 = def (other) :
    return this.div_32(toLong(other))

  Long.prototype.div_32 = def (other) :
    return divide(this, other)

  Long.prototype.div_33 = def (other) :
    return this.toFloat_6() / other

  Long.prototype.div_34 = def (other) :
    return this.toDouble_6() / other

  Long.prototype.rem_29 = def (other) :
    return this.rem_32(toLong(other))

  Long.prototype.rem_30 = def (other) :
    return this.rem_32(toLong(other))

  Long.prototype.rem_31 = def (other) :
    return this.rem_32(toLong(other))

  Long.prototype.rem_32 = def (other) :
    return modulo(this, other)

  Long.prototype.rem_33 = def (other) :
    return this.toFloat_6() % other

  Long.prototype.rem_34 = def (other) :
    return this.toDouble_6() % other

  Long.prototype.inc_5 = def () :
    return this.plus_38(new Long(1, 0))

  Long.prototype.dec_5 = def () :
    return this.minus_34(new Long(1, 0))

  Long.prototype.unaryPlus_4 = def () :
    return this

  Long.prototype.unaryMinus_4 = def () :
    return this.inv_0().plus_38(new Long(1, 0))

  Long.prototype.rangeTo_12 = def (other) :
    return this.rangeTo_15(toLong(other))

  Long.prototype.rangeTo_13 = def (other) :
    return this.rangeTo_15(toLong(other))

  Long.prototype.rangeTo_14 = def (other) :
    return this.rangeTo_15(toLong(other))

  Long.prototype.rangeTo_15 = def (other) :
    return new LongRange(this, other)

  Long.prototype.shl_0 = def (bitCount) :
    return shiftLeft(this, bitCount)

  Long.prototype.shr_0 = def (bitCount) :
    return shiftRight(this, bitCount)

  Long.prototype.ushr_0 = def (bitCount) :
    return shiftRightUnsigned(this, bitCount)

  Long.prototype.and = def (other) :
    return new Long(this._low & other._low, this._high & other._high)

  Long.prototype.or = def (other) :
    return new Long(this._low | other._low, this._high | other._high)

  Long.prototype.xor = def (other) :
    return new Long(this._low ^ other._low, this._high ^ other._high)

  Long.prototype.inv_0 = def () :
    return new Long(~this._low, ~this._high)

  Long.prototype.toByte_6 = def () :
    return toByte(this._low)

  Long.prototype.toChar_6 = def () :
    return numberToChar(this._low)

  Long.prototype.toShort_6 = def () :
    return toShort(this._low)

  Long.prototype.toInt_6 = def () :
    return this._low

  Long.prototype.toLong_6 = def () :
    return this

  Long.prototype.toFloat_6 = def () :
    return this.toDouble_6()

  Long.prototype.toDouble_6 = def () :
    return toNumber(this)

  Long.prototype.valueOf = def () :
    return this.toDouble_6()

  Long.prototype.equals = def (other) :
     tmp
    if (other instanceof Long) :
      tmp = equalsLong(this, other)
     else :
      :
        tmp = false


    return tmp

  Long.prototype.hashCode = def () :
    return hashCode_0(this)

  Long.prototype.toString = def () :
    return toStringImpl(this, 10)

  Long.$metadata$ = {
    simpleName: 'Long',
    kind: 'class',
    interfaces: [Comparable]

  def _get_ZERO_() :
    return ZERO

   ZERO
  def _get_ONE_() :
    return ONE

   ONE
  def _get_NEG_ONE_() :
    return NEG_ONE

   NEG_ONE
  def _get_MAX_VALUE_() :
    return MAX_VALUE

   MAX_VALUE
  def _get_MIN_VALUE_() :
    return MIN_VALUE

   MIN_VALUE
  def _get_TWO_PWR_24__() :
    return TWO_PWR_24_

   TWO_PWR_24_
  def compare(_this_, other) :
    if (equalsLong(_this_, other)) :
      return 0
     thisNeg = isNegative(_this_)
     otherNeg = isNegative(other)
    return (thisNeg ? !otherNeg : false) ? -1 : (!thisNeg ? otherNeg : false) ? 1 : isNegative(subtract(_this_, other)) ? -1 : 1

  def add(_this_, other) :
     a48 = _this_._high >>> 16
     a32 = _this_._high & 65535
     a16 = _this_._low >>> 16
     a00 = _this_._low & 65535
     b48 = other._high >>> 16
     b32 = other._high & 65535
     b16 = other._low >>> 16
     b00 = other._low & 65535
     c48 = 0
     c32 = 0
     c16 = 0
     c00 = 0
    c00 = c00 + (a00 + b00 | 0) | 0
    c16 = c16 + (c00 >>> 16) | 0
    c00 = c00 & 65535
    c16 = c16 + (a16 + b16 | 0) | 0
    c32 = c32 + (c16 >>> 16) | 0
    c16 = c16 & 65535
    c32 = c32 + (a32 + b32 | 0) | 0
    c48 = c48 + (c32 >>> 16) | 0
    c32 = c32 & 65535
    c48 = c48 + (a48 + b48 | 0) | 0
    c48 = c48 & 65535
    return new Long(c16 << 16 | c00, c48 << 16 | c32)

  def subtract(_this_, other) :
    return add(_this_, other.unaryMinus_4())

  def multiply(_this_, other) :
    if (isZero(_this_)) :
      return ZERO
     else if (isZero(other)) :
      return ZERO
    if (equalsLong(_this_, MIN_VALUE)) :
      return isOdd(other) ? MIN_VALUE : ZERO
     else if (equalsLong(other, MIN_VALUE)) :
      return isOdd(_this_) ? MIN_VALUE : ZERO
    if (isNegative(_this_)) :
       tmp
      if (isNegative(other)) :
        tmp = multiply(negate(_this_), negate(other))
       else :
        tmp = negate(multiply(negate(_this_), other))

      return tmp
     else if (isNegative(other)) :
      return negate(multiply(_this_, negate(other)))
    if (lessThan(_this_, TWO_PWR_24_) ? lessThan(other, TWO_PWR_24_) : false) :
      return fromNumber(toNumber(_this_) * toNumber(other))
     a48 = _this_._high >>> 16
     a32 = _this_._high & 65535
     a16 = _this_._low >>> 16
     a00 = _this_._low & 65535
     b48 = other._high >>> 16
     b32 = other._high & 65535
     b16 = other._low >>> 16
     b00 = other._low & 65535
     c48 = 0
     c32 = 0
     c16 = 0
     c00 = 0
    c00 = c00 + imul(a00, b00) | 0
    c16 = c16 + (c00 >>> 16) | 0
    c00 = c00 & 65535
    c16 = c16 + imul(a16, b00) | 0
    c32 = c32 + (c16 >>> 16) | 0
    c16 = c16 & 65535
    c16 = c16 + imul(a00, b16) | 0
    c32 = c32 + (c16 >>> 16) | 0
    c16 = c16 & 65535
    c32 = c32 + imul(a32, b00) | 0
    c48 = c48 + (c32 >>> 16) | 0
    c32 = c32 & 65535
    c32 = c32 + imul(a16, b16) | 0
    c48 = c48 + (c32 >>> 16) | 0
    c32 = c32 & 65535
    c32 = c32 + imul(a00, b32) | 0
    c48 = c48 + (c32 >>> 16) | 0
    c32 = c32 & 65535
    c48 = c48 + (((imul(a48, b00) + imul(a32, b16) | 0) + imul(a16, b32) | 0) + imul(a00, b48) | 0) | 0
    c48 = c48 & 65535
    return new Long(c16 << 16 | c00, c48 << 16 | c32)

  def divide(_this_, other) :
    if (isZero(other)) :
      throw Exception_init_$Create$_0('division by zero')
     else if (isZero(_this_)) :
      return ZERO
    if (equalsLong(_this_, MIN_VALUE)) :
      if (equalsLong(other, ONE) ? true : equalsLong(other, NEG_ONE)) :
        return MIN_VALUE
       else if (equalsLong(other, MIN_VALUE)) :
        return ONE
       else :
         halfThis = shiftRight(_this_, 1)
         approx = shiftLeft(halfThis.div_32(other), 1)
        if (equalsLong(approx, ZERO)) :
          return isNegative(other) ? ONE : NEG_ONE
         else :
           rem = subtract(_this_, multiply(other, approx))
          return add(approx, rem.div_32(other))


     else if (equalsLong(other, MIN_VALUE)) :
      return ZERO
    if (isNegative(_this_)) :
       tmp
      if (isNegative(other)) :
        tmp = negate(_this_).div_32(negate(other))
       else :
        tmp = negate(negate(_this_).div_32(other))

      return tmp
     else if (isNegative(other)) :
      return negate(_this_.div_32(negate(other)))
     res = ZERO
     rem_0 = _this_
    while (greaterThanOrEqual(rem_0, other)) :
       approxDouble = toNumber(rem_0) / toNumber(other)
       approx2 = Math.max(1.0, Math.floor(approxDouble))
       log2 = Math.ceil(Math.log(approx2) / Math.LN2)
       delta = log2 <= 48.0 ? 1.0 : Math.pow(2, log2 - 48)
       approxRes = fromNumber(approx2)
       approxRem = multiply(approxRes, other)
      while (isNegative(approxRem) ? true : greaterThan(approxRem, rem_0)) :
        approx2 = approx2 - delta
        approxRes = fromNumber(approx2)
        approxRem = multiply(approxRes, other)

      if (isZero(approxRes)) :
        approxRes = ONE
      res = add(res, approxRes)
      rem_0 = subtract(rem_0, approxRem)

    return res

  def modulo(_this_, other) :
    return subtract(_this_, multiply(_this_.div_32(other), other))

  def shiftLeft(_this_, numBits) :
     numBits_0 = numBits & 63
    if (numBits_0 === 0) :
      return _this_
     else :
      if (numBits_0 < 32) :
        return new Long(_this_._low << numBits_0, _this_._high << numBits_0 | _this_._low >>> (32 - numBits_0 | 0))
       else :
        return new Long(0, _this_._low << (numBits_0 - 32 | 0))



  def shiftRight(_this_, numBits) :
     numBits_0 = numBits & 63
    if (numBits_0 === 0) :
      return _this_
     else :
      if (numBits_0 < 32) :
        return new Long(_this_._low >>> numBits_0 | _this_._high << (32 - numBits_0 | 0), _this_._high >> numBits_0)
       else :
        return new Long(_this_._high >> (numBits_0 - 32 | 0), _this_._high >= 0 ? 0 : -1)



  def shiftRightUnsigned(_this_, numBits) :
     numBits_0 = numBits & 63
    if (numBits_0 === 0) :
      return _this_
     else :
      if (numBits_0 < 32) :
        return new Long(_this_._low >>> numBits_0 | _this_._high << (32 - numBits_0 | 0), _this_._high >>> numBits_0)
       else :
         tmp
        if (numBits_0 === 32) :
          tmp = new Long(_this_._high, 0)
         else :
          tmp = new Long(_this_._high >>> (numBits_0 - 32 | 0), 0)

        return tmp



  def toNumber(_this_) :
    return _this_._high * 4.294967296E9 + getLowBitsUnsigned(_this_)

  def equalsLong(_this_, other) :
    return _this_._high === other._high ? _this_._low === other._low : false

  def hashCode_0(l) :
    return l._low ^ l._high

  def toStringImpl(_this_, radix) :
    if (radix < 2 ? true : 36 < radix) :
      throw Exception_init_$Create$_0('' + 'radix out of range: ' + radix)
    if (isZero(_this_)) :
      return '0'
    if (isNegative(_this_)) :
      if (equalsLong(_this_, MIN_VALUE)) :
         radixLong = fromInt(radix)
         div = _this_.div_32(radixLong)
         rem = subtract(multiply(div, radixLong), _this_).toInt_6()
         tmp = toStringImpl(div, radix)
         tmp0_unsafeCast_0 = rem.toString(radix)
        return tmp + tmp0_unsafeCast_0
       else :
        return '' + '-' + toStringImpl(negate(_this_), radix)

     radixToPower = fromNumber(Math.pow(radix, 6.0))
     rem_0 = _this_
     result = ''
    while (true) :
       remDiv = rem_0.div_32(radixToPower)
       intval = subtract(rem_0, multiply(remDiv, radixToPower)).toInt_6()
       tmp1_unsafeCast_0 = intval.toString(radix)
       digits = tmp1_unsafeCast_0
      rem_0 = remDiv
      if (isZero(rem_0)) :
        return digits + result
       else :
        while (digits.length < 6) :
          digits = '0' + digits

        result = digits + result



  def fromInt(value) :
    return new Long(value, value < 0 ? -1 : 0)

  def isNegative(_this_) :
    return _this_._high < 0

  def isZero(_this_) :
    return _this_._high === 0 ? _this_._low === 0 : false

  def isOdd(_this_) :
    return (_this_._low & 1) === 1

  def negate(_this_) :
    return _this_.unaryMinus_4()

  def lessThan(_this_, other) :
    return compare(_this_, other) < 0

  def fromNumber(value) :
    if (isNaN_0(value)) :
      return ZERO
     else if (value <= -9.223372036854776E18) :
      return MIN_VALUE
     else if (value + 1 >= 9.223372036854776E18) :
      return MAX_VALUE
     else if (value < 0.0) :
      return negate(fromNumber(-value))
     else :
       twoPwr32 = 4.294967296E9
      return new Long(jsBitwiseOr(value % twoPwr32, 0), jsBitwiseOr(value / twoPwr32, 0))


  def greaterThan(_this_, other) :
    return compare(_this_, other) > 0

  def greaterThanOrEqual(_this_, other) :
    return compare(_this_, other) >= 0

  def getLowBitsUnsigned(_this_) :
    return _this_._low >= 0 ? _this_._low : 4.294967296E9 + _this_._low

  def _get_TWO_PWR_32_DBL__() :
    return TWO_PWR_32_DBL_

   TWO_PWR_32_DBL_
  def _get_TWO_PWR_63_DBL__() :
    return TWO_PWR_63_DBL_

   TWO_PWR_63_DBL_
  def imul(a_local, b_local) :
     lhs = jsBitwiseAnd(a_local, 4.29490176E9) * jsBitwiseAnd(b_local, 65535)
     rhs = jsBitwiseAnd(a_local, 65535) * b_local
    return jsBitwiseOr(lhs + rhs, 0)

  def withType(type, array) :
    array.$type$ = type
    return array

  def arrayConcat(args) :
     len = args.length
     tmp0_unsafeCast_0 = Array(len)
     typed = tmp0_unsafeCast_0
     inductionVariable = 0
     last = len - 1 | 0
    if (inductionVariable <= last)
      do :
         i = inductionVariable
        inductionVariable = inductionVariable + 1 | 0
         arr = args[i]
        if (!(!(arr == null) ? isArray(arr) : false)) :
          typed[i] = [].slice.call(arr)
         else :
          :
            typed[i] = arr



       while (!(i === last))
    return [].concat.apply([], typed)

  def primitiveArrayConcat(args) :
     size_local = 0
     inductionVariable = 0
     last = args.length - 1 | 0
    if (inductionVariable <= last)
      do :
         i = inductionVariable
        inductionVariable = inductionVariable + 1 | 0
         tmp = size_local
         tmp0_unsafeCast_0 = args[i]
        size_local = tmp + tmp0_unsafeCast_0.length | 0

       while (!(i === last))
     a = args[0]
     tmp1_unsafeCast_0 = new a.constructor(size_local)
     result = tmp1_unsafeCast_0
    if (a.$type$ != null) :
       tmp2_withType_0 = a.$type$
      result.$type$ = tmp2_withType_0
     else :

    size_local = 0
     inductionVariable_0 = 0
     last_0 = args.length - 1 | 0
    if (inductionVariable_0 <= last_0)
      do :
         i_0 = inductionVariable_0
        inductionVariable_0 = inductionVariable_0 + 1 | 0
         tmp3_unsafeCast_0 = args[i_0]
         arr = tmp3_unsafeCast_0
         inductionVariable_1 = 0
         last_1 = arr.length - 1 | 0
        if (inductionVariable_1 <= last_1)
          do :
             j = inductionVariable_1
            inductionVariable_1 = inductionVariable_1 + 1 | 0
             tmp3 = size_local
            size_local = tmp3 + 1 | 0
            result[tmp3] = arr[j]

           while (!(j === last_1))

       while (!(i_0 === last_0))
    return result

  def taggedArrayCopy(array) :
     res = array.slice()
    res.$type$ = array.$type$
    return res

  def numberToByte(a) :
    return toByte(numberToInt(a))

  def toByte(a) :
     tmp0_unsafeCast_0 = a << 24 >> 24
    return tmp0_unsafeCast_0

  def numberToInt(a) :
     tmp
    if (a instanceof Long) :
      tmp = a.toInt_6()
     else :
      :
        tmp = doubleToInt(a)


    return tmp

  def doubleToInt(a) :
    return a > 2.147483647E9 ? 2147483647 : a < -2.147483648E9 ? -2147483648 : jsBitwiseOr(a, 0)

  def numberToDouble(a) :
     tmp0_unsafeCast_0 = +a
    return tmp0_unsafeCast_0

  def numberToShort(a) :
    return toShort(numberToInt(a))

  def toShort(a) :
     tmp0_unsafeCast_0 = a << 16 >> 16
    return tmp0_unsafeCast_0

  def numberToLong(a) :
     tmp
    if (a instanceof Long) :
      tmp = a
     else :
      :
        tmp = fromNumber(a)


    return tmp

  def numberToChar(a) :
    return new Char(numberToInt(a) & 65535)

  def toLong(a) :
    return fromInt(a)

  def numberRangeToNumber(start, endInclusive) :
    return new IntRange(start, endInclusive)

  def numberRangeToLong(start, endInclusive) :
    return new LongRange(numberToLong(start), endInclusive)

  def _get_propertyRefClassMetadataCache_() :
    return propertyRefClassMetadataCache

   propertyRefClassMetadataCache
  def metadataObject() :
    return {kind: 'class', interfaces: []

  def getPropertyCallableRef(name, paramCount, type, getter, setter) :
    getter.get = getter
    getter.set = setter
    getter.callableName = name
     tmp0_unsafeCast_0 = getPropertyRefClass(getter, getKPropMetadata(paramCount, setter, type))
    return tmp0_unsafeCast_0

  def getPropertyRefClass(obj, metadata) :
    obj.$metadata$ = metadata
    obj.constructor = obj
    return obj

  def getKPropMetadata(paramCount, setter, type) :
     mdata = propertyRefClassMetadataCache[paramCount][setter == null ? 0 : 1]
    if (mdata.interfaces.length == 0) :
      mdata.interfaces.push(type)
    return mdata

  def getLocalDelegateReference(name, type, mutable, lambda) :
    return getPropertyCallableRef(name, 0, type, lambda, mutable ? lambda : null)

  def propertyRefClassMetadataCache$init$() :
     tmp = {kind: 'class', interfaces: []
     tmp0_arrayOf_0 = [tmp, {kind: 'class', interfaces: []]
     tmp_0 = tmp0_arrayOf_0
     tmp_1 = {kind: 'class', interfaces: []
     tmp1_arrayOf_0 = [tmp_1, {kind: 'class', interfaces: []]
     tmp_2 = tmp1_arrayOf_0
     tmp_3 = {kind: 'class', interfaces: []
     tmp2_arrayOf_0 = [tmp_3, {kind: 'class', interfaces: []]
     tmp3_arrayOf_0 = [tmp_0, tmp_2, tmp2_arrayOf_0]
    return tmp3_arrayOf_0

  def isInterface(obj, iface) :
     tmp0_elvis_lhs = obj.constructor
     tmp
    if (tmp0_elvis_lhs == null) :
      return false
     else :
      tmp = tmp0_elvis_lhs

     ctor = tmp
    return isInterfaceImpl(ctor, iface)

  def isInterfaceImpl(ctor, iface) :
    if (ctor === iface)
      return true
     metadata = ctor.$metadata$
    if (!(metadata == null)) :
       interfaces = metadata.interfaces
       indexedObject = interfaces
       inductionVariable = 0
       last = indexedObject.length
      while (inductionVariable < last) :
         i = indexedObject[inductionVariable]
        inductionVariable = inductionVariable + 1 | 0
        if (isInterfaceImpl(i, iface)) :
          return true

     superPrototype = !(ctor.prototype == null) ? Object.getPrototypeOf(ctor.prototype) : null
     superConstructor = superPrototype != null ? superPrototype.constructor : null
    return !(superConstructor == null) ? isInterfaceImpl(superConstructor, iface) : false

  def isArray(obj) :
     tmp
    if (isJsArray(obj)) :
      tmp = !obj.$type$
     else :
      tmp = false

    return tmp

  def isJsArray(obj) :
     tmp0_unsafeCast_0 = Array.isArray(obj)
    return tmp0_unsafeCast_0

  def isObject(obj) :
     objTypeOf = typeof obj
     tmp0_subject = objTypeOf
    switch (tmp0_subject) :
      case 'string':
        return true;
      case 'number':
        return true;
      case 'boolean':
        return true;
      case 'function':
        return true;
      default:return jsInstanceOf(obj, Object);


  def isSuspendFunction(obj, arity) :
    if (typeof obj === 'function') :
       tmp0_unsafeCast_0 = obj.$arity
      return tmp0_unsafeCast_0 === arity
    return false

  def isNumber(a) :
     tmp
    if (typeof a === 'number') :
      tmp = true
     else :
      tmp = a instanceof Long

    return tmp

  def isComparable(value) :
     type = typeof value
    return ((type === 'string' ? true : type === 'boolean') ? true : isNumber(value)) ? true : isInterface(value, _get_js_(getKClass_0(Comparable)))

  def isCharSequence(value) :
    return typeof value === 'string' ? true : isInterface(value, _get_js_(getKClass_0(CharSequence)))

  def isBooleanArray(a) :
    return isJsArray(a) ? a.$type$ === 'BooleanArray' : false

  def isByteArray(a) :
    return jsInstanceOf(a, Int8Array)

  def isShortArray(a) :
    return jsInstanceOf(a, Int16Array)

  def isCharArray(a) :
    return isJsArray(a) ? a.$type$ === 'CharArray' : false

  def isIntArray(a) :
    return jsInstanceOf(a, Int32Array)

  def isFloatArray(a) :
    return jsInstanceOf(a, Float32Array)

  def isLongArray(a) :
    return isJsArray(a) ? a.$type$ === 'LongArray' : false

  def isDoubleArray(a) :
    return jsInstanceOf(a, Float64Array)

  def isArrayish(o) :
     tmp
    if (isJsArray(o)) :
      tmp = true
     else :
       tmp0_unsafeCast_0 = ArrayBuffer.isView(o)
      tmp = tmp0_unsafeCast_0

    return tmp

  def jsIsType(obj, jsClass_0) :
    if (jsClass_0 === Object) :
      return isObject(obj)
    if ((obj == null ? true : jsClass_0 == null) ? true : !(typeof obj === 'object') ? !(typeof obj === 'function') : false) :
      return false
    if (typeof jsClass_0 === 'function' ? jsInstanceOf(obj, jsClass_0) : false) :
      return true
     proto = jsGetPrototypeOf(jsClass_0)
     tmp0_safe_receiver = proto
     constructor = tmp0_safe_receiver == null ? null : tmp0_safe_receiver.constructor
    if (constructor != null ? jsIn('$metadata$', constructor) : false) :
       metadata = constructor.$metadata$
      if (metadata.kind === 'object') :
        return obj === jsClass_0
     klassMetadata = jsClass_0.$metadata$
    if (klassMetadata == null) :
      return jsInstanceOf(obj, jsClass_0)
    if (klassMetadata.kind === 'interface' ? obj.constructor != null : false) :
      return isInterfaceImpl(obj.constructor, jsClass_0)
    return false

  def jsGetPrototypeOf(jsClass_0) :
    return Object.getPrototypeOf(jsClass_0)

  def asList(_this_) :
    return new ArrayList(_this_)

  def plus_0(_this_, elements) :
    return _this_.concat(elements)

  def copyOfRange(_this_, fromIndex, toIndex) :
    Companion_getInstance().checkRangeIndexes(fromIndex, toIndex, _this_.length)
    return _this_.slice(fromIndex, toIndex)

  def minOf(a, b) :
    return def () :
       $externalVarargReceiverTmp = Math
      return $externalVarargReceiverTmp.min.apply($externalVarargReceiverTmp, [].concat([].slice.call(new Int32Array([a, b]))))
    .call(this)

  def _get_resultContinuation_($this) :
    return $this._resultContinuation

  def _get__context_($this) :
    return $this.__context

  def _set_intercepted__($this, _set___) :
    $this._intercepted_ = _set___

  def _get_intercepted__($this) :
    return $this._intercepted_

  def releaseIntercepted($this) :
     intercepted = $this._intercepted_
    if (!(intercepted == null) ? !(intercepted === $this) : false) :
      ensureNotNull($this._get_context__4().get_6(Key_getInstance())).releaseInterceptedContinuation(intercepted)
    $this._intercepted_ = CompletedContinuation_getInstance()

  def CoroutineImpl_0(resultContinuation) :
    this._resultContinuation = resultContinuation
    this._state = 0
    this._exceptionState = 0
    this._result = null
    this._exception_0 = null
    this._finallyPath = null
     tmp = this
     tmp0_safe_receiver = this._resultContinuation
    tmp.__context = tmp0_safe_receiver == null ? null : tmp0_safe_receiver._get_context__4()
    this._intercepted_ = null

  CoroutineImpl_0.prototype._set_state_ = def (_set___) :
    this._state = _set___

  CoroutineImpl_0.prototype._get_state_ = def () :
    return this._state

  CoroutineImpl_0.prototype._set_exceptionState_ = def (_set___) :
    this._exceptionState = _set___

  CoroutineImpl_0.prototype._get_exceptionState_ = def () :
    return this._exceptionState

  CoroutineImpl_0.prototype._set_result_ = def (_set___) :
    this._result = _set___

  CoroutineImpl_0.prototype._get_result_ = def () :
    return this._result

  CoroutineImpl_0.prototype._set_exception_ = def (_set___) :
    this._exception_0 = _set___

  CoroutineImpl_0.prototype._get_exception__0 = def () :
    return this._exception_0

  CoroutineImpl_0.prototype._set_finallyPath_ = def (_set___) :
    this._finallyPath = _set___

  CoroutineImpl_0.prototype._get_finallyPath_ = def () :
    return this._finallyPath

  CoroutineImpl_0.prototype._get_context__4 = def () :
    return ensureNotNull(this.__context)

  CoroutineImpl_0.prototype.intercepted = def () :
     tmp2_elvis_lhs = this._intercepted_
     tmp
    if (tmp2_elvis_lhs == null) :
       tmp0_safe_receiver = this._get_context__4().get_6(Key_getInstance())
       tmp1_elvis_lhs = tmp0_safe_receiver == null ? null : tmp0_safe_receiver.interceptContinuation(this)
       tmp0_also_0 = tmp1_elvis_lhs == null ? this : tmp1_elvis_lhs
      this._intercepted_ = tmp0_also_0
      tmp = tmp0_also_0
     else :
      tmp = tmp2_elvis_lhs

    return tmp

  CoroutineImpl_0.prototype.resumeWith_5 = def (result) :
     current = this
     tmp
    if (_Result___get_isFailure__impl_(result)) :
      tmp = null
     else :
       tmp_0 = _Result___get_value__impl_(result)
      tmp = (tmp_0 == null ? true : isObject(tmp_0)) ? tmp_0 : THROW_CCE()

     currentResult = tmp
     currentException = Result__exceptionOrNull_impl(result)
    while (true) :
       tmp0_with_0 = current
      if (currentException == null) :
        tmp0_with_0._result = currentResult
       else :
        tmp0_with_0._state = tmp0_with_0._exceptionState
        tmp0_with_0._exception_0 = currentException

      try :
         outcome_2 = tmp0_with_0.doResume()
        if (outcome_2 === _get_COROUTINE_SUSPENDED_())
          return Unit_getInstance()
        currentResult = outcome_2
        currentException = null
       catch ($p) :
        currentResult = null
        currentException = $p

      releaseIntercepted(tmp0_with_0)
       completion_4 = ensureNotNull(tmp0_with_0._resultContinuation)
      if (completion_4 instanceof CoroutineImpl_0) :
        current = completion_4
       else :
        :
          if (!(currentException == null)) :
             tmp0_resumeWithException_0_5 = ensureNotNull(currentException)
             tmp0_failure_0_1_6 = Companion_getInstance_2()
            completion_4.resumeWith_6(createFailure(tmp0_resumeWithException_0_5))
           else :
             tmp1_resume_0_7 = currentResult
             tmp0_success_0_1_8 = Companion_getInstance_2()
            completion_4.resumeWith_6(tmp1_resume_0_7)

          return Unit_getInstance()




  CoroutineImpl_0.prototype.resumeWith_6 = def (result) :
    return this.resumeWith_5(result)

  CoroutineImpl_0.prototype.create = def (completion) :
    throw UnsupportedOperationException_init_$Create$_0('create(Continuation) has not been overridden')

  CoroutineImpl_0.prototype.create_0 = def (value, completion) :
    throw UnsupportedOperationException_init_$Create$_0('create(Any?;Continuation) has not been overridden')

  CoroutineImpl_0.$metadata$ = {
    simpleName: 'CoroutineImpl',
    kind: 'class',
    interfaces: [Continuation]

  def CompletedContinuation() :
    CompletedContinuation_instance = this

  CompletedContinuation.prototype._get_context__4 = def () :
     tmp0_error_0 = 'This continuation is already complete'
    throw IllegalStateException_init_$Create$_0(toString_0(tmp0_error_0))

  CompletedContinuation.prototype.resumeWith_5 = def (result) :
     tmp0_error_0 = 'This continuation is already complete'
    throw IllegalStateException_init_$Create$_0(toString_0(tmp0_error_0))

  CompletedContinuation.prototype.resumeWith_6 = def (result) :
    return this.resumeWith_5(result)

  CompletedContinuation.prototype.toString = def () :
    return 'This continuation is already complete'

  CompletedContinuation.$metadata$ = {
    simpleName: 'CompletedContinuation',
    kind: 'object',
    interfaces: [Continuation]

   CompletedContinuation_instance
  def CompletedContinuation_getInstance() :
    if (CompletedContinuation_instance == null)
      new CompletedContinuation()
    return CompletedContinuation_instance

  def Exception_init_$Init$($this) :
    extendThrowable($this, void 1, void 1)
    Exception.call($this)
    return $this

  def Exception_init_$Create$() :
     tmp = Exception_init_$Init$(Object.create(Exception.prototype))
    captureStack(tmp, Exception_init_$Create$)
    return tmp

  def Exception_init_$Init$_0(message, $this) :
    extendThrowable($this, message, void 1)
    Exception.call($this)
    return $this

  def Exception_init_$Create$_0(message) :
     tmp = Exception_init_$Init$_0(message, Object.create(Exception.prototype))
    captureStack(tmp, Exception_init_$Create$_0)
    return tmp

  def Exception_init_$Init$_1(message, cause, $this) :
    extendThrowable($this, message, cause)
    Exception.call($this)
    return $this

  def Exception_init_$Create$_1(message, cause) :
     tmp = Exception_init_$Init$_1(message, cause, Object.create(Exception.prototype))
    captureStack(tmp, Exception_init_$Create$_1)
    return tmp

  def Exception_init_$Init$_2(cause, $this) :
    extendThrowable($this, void 1, cause)
    Exception.call($this)
    return $this

  def Exception_init_$Create$_2(cause) :
     tmp = Exception_init_$Init$_2(cause, Object.create(Exception.prototype))
    captureStack(tmp, Exception_init_$Create$_2)
    return tmp

  def Exception() :
    captureStack(this, Exception)

  Exception.$metadata$ = {
    simpleName: 'Exception',
    kind: 'class',
    interfaces: []

  def Error_init_$Init$($this) :
    extendThrowable($this, void 1, void 1)
    Error_0.call($this)
    return $this

  def Error_init_$Create$() :
     tmp = Error_init_$Init$(Object.create(Error_0.prototype))
    captureStack(tmp, Error_init_$Create$)
    return tmp

  def Error_init_$Init$_0(message, $this) :
    extendThrowable($this, message, void 1)
    Error_0.call($this)
    return $this

  def Error_init_$Create$_0(message) :
     tmp = Error_init_$Init$_0(message, Object.create(Error_0.prototype))
    captureStack(tmp, Error_init_$Create$_0)
    return tmp

  def Error_init_$Init$_1(message, cause, $this) :
    extendThrowable($this, message, cause)
    Error_0.call($this)
    return $this

  def Error_init_$Create$_1(message, cause) :
     tmp = Error_init_$Init$_1(message, cause, Object.create(Error_0.prototype))
    captureStack(tmp, Error_init_$Create$_1)
    return tmp

  def Error_init_$Init$_2(cause, $this) :
    extendThrowable($this, void 1, cause)
    Error_0.call($this)
    return $this

  def Error_init_$Create$_2(cause) :
     tmp = Error_init_$Init$_2(cause, Object.create(Error_0.prototype))
    captureStack(tmp, Error_init_$Create$_2)
    return tmp

  def Error_0() :
    captureStack(this, Error_0)

  Error_0.$metadata$ = {
    simpleName: 'Error',
    kind: 'class',
    interfaces: []

  def IllegalArgumentException_init_$Init$($this) :
    RuntimeException_init_$Init$($this)
    IllegalArgumentException.call($this)
    return $this

  def IllegalArgumentException_init_$Create$() :
     tmp = IllegalArgumentException_init_$Init$(Object.create(IllegalArgumentException.prototype))
    captureStack(tmp, IllegalArgumentException_init_$Create$)
    return tmp

  def IllegalArgumentException_init_$Init$_0(message, $this) :
    RuntimeException_init_$Init$_0(message, $this)
    IllegalArgumentException.call($this)
    return $this

  def IllegalArgumentException_init_$Create$_0(message) :
     tmp = IllegalArgumentException_init_$Init$_0(message, Object.create(IllegalArgumentException.prototype))
    captureStack(tmp, IllegalArgumentException_init_$Create$_0)
    return tmp

  def IllegalArgumentException_init_$Init$_1(message, cause, $this) :
    RuntimeException_init_$Init$_1(message, cause, $this)
    IllegalArgumentException.call($this)
    return $this

  def IllegalArgumentException_init_$Create$_1(message, cause) :
     tmp = IllegalArgumentException_init_$Init$_1(message, cause, Object.create(IllegalArgumentException.prototype))
    captureStack(tmp, IllegalArgumentException_init_$Create$_1)
    return tmp

  def IllegalArgumentException_init_$Init$_2(cause, $this) :
    RuntimeException_init_$Init$_2(cause, $this)
    IllegalArgumentException.call($this)
    return $this

  def IllegalArgumentException_init_$Create$_2(cause) :
     tmp = IllegalArgumentException_init_$Init$_2(cause, Object.create(IllegalArgumentException.prototype))
    captureStack(tmp, IllegalArgumentException_init_$Create$_2)
    return tmp

  def IllegalArgumentException() :
    captureStack(this, IllegalArgumentException)

  IllegalArgumentException.$metadata$ = {
    simpleName: 'IllegalArgumentException',
    kind: 'class',
    interfaces: []

  def RuntimeException_init_$Init$($this) :
    Exception_init_$Init$($this)
    RuntimeException.call($this)
    return $this

  def RuntimeException_init_$Create$() :
     tmp = RuntimeException_init_$Init$(Object.create(RuntimeException.prototype))
    captureStack(tmp, RuntimeException_init_$Create$)
    return tmp

  def RuntimeException_init_$Init$_0(message, $this) :
    Exception_init_$Init$_0(message, $this)
    RuntimeException.call($this)
    return $this

  def RuntimeException_init_$Create$_0(message) :
     tmp = RuntimeException_init_$Init$_0(message, Object.create(RuntimeException.prototype))
    captureStack(tmp, RuntimeException_init_$Create$_0)
    return tmp

  def RuntimeException_init_$Init$_1(message, cause, $this) :
    Exception_init_$Init$_1(message, cause, $this)
    RuntimeException.call($this)
    return $this

  def RuntimeException_init_$Create$_1(message, cause) :
     tmp = RuntimeException_init_$Init$_1(message, cause, Object.create(RuntimeException.prototype))
    captureStack(tmp, RuntimeException_init_$Create$_1)
    return tmp

  def RuntimeException_init_$Init$_2(cause, $this) :
    Exception_init_$Init$_2(cause, $this)
    RuntimeException.call($this)
    return $this

  def RuntimeException_init_$Create$_2(cause) :
     tmp = RuntimeException_init_$Init$_2(cause, Object.create(RuntimeException.prototype))
    captureStack(tmp, RuntimeException_init_$Create$_2)
    return tmp

  def RuntimeException() :
    captureStack(this, RuntimeException)

  RuntimeException.$metadata$ = {
    simpleName: 'RuntimeException',
    kind: 'class',
    interfaces: []

  def NoSuchElementException_init_$Init$($this) :
    RuntimeException_init_$Init$($this)
    NoSuchElementException.call($this)
    return $this

  def NoSuchElementException_init_$Create$() :
     tmp = NoSuchElementException_init_$Init$(Object.create(NoSuchElementException.prototype))
    captureStack(tmp, NoSuchElementException_init_$Create$)
    return tmp

  def NoSuchElementException_init_$Init$_0(message, $this) :
    RuntimeException_init_$Init$_0(message, $this)
    NoSuchElementException.call($this)
    return $this

  def NoSuchElementException_init_$Create$_0(message) :
     tmp = NoSuchElementException_init_$Init$_0(message, Object.create(NoSuchElementException.prototype))
    captureStack(tmp, NoSuchElementException_init_$Create$_0)
    return tmp

  def NoSuchElementException() :
    captureStack(this, NoSuchElementException)

  NoSuchElementException.$metadata$ = {
    simpleName: 'NoSuchElementException',
    kind: 'class',
    interfaces: []

  def IllegalStateException_init_$Init$($this) :
    RuntimeException_init_$Init$($this)
    IllegalStateException.call($this)
    return $this

  def IllegalStateException_init_$Create$() :
     tmp = IllegalStateException_init_$Init$(Object.create(IllegalStateException.prototype))
    captureStack(tmp, IllegalStateException_init_$Create$)
    return tmp

  def IllegalStateException_init_$Init$_0(message, $this) :
    RuntimeException_init_$Init$_0(message, $this)
    IllegalStateException.call($this)
    return $this

  def IllegalStateException_init_$Create$_0(message) :
     tmp = IllegalStateException_init_$Init$_0(message, Object.create(IllegalStateException.prototype))
    captureStack(tmp, IllegalStateException_init_$Create$_0)
    return tmp

  def IllegalStateException_init_$Init$_1(message, cause, $this) :
    RuntimeException_init_$Init$_1(message, cause, $this)
    IllegalStateException.call($this)
    return $this

  def IllegalStateException_init_$Create$_1(message, cause) :
     tmp = IllegalStateException_init_$Init$_1(message, cause, Object.create(IllegalStateException.prototype))
    captureStack(tmp, IllegalStateException_init_$Create$_1)
    return tmp

  def IllegalStateException_init_$Init$_2(cause, $this) :
    RuntimeException_init_$Init$_2(cause, $this)
    IllegalStateException.call($this)
    return $this

  def IllegalStateException_init_$Create$_2(cause) :
     tmp = IllegalStateException_init_$Init$_2(cause, Object.create(IllegalStateException.prototype))
    captureStack(tmp, IllegalStateException_init_$Create$_2)
    return tmp

  def IllegalStateException() :
    captureStack(this, IllegalStateException)

  IllegalStateException.$metadata$ = {
    simpleName: 'IllegalStateException',
    kind: 'class',
    interfaces: []

  def UnsupportedOperationException_init_$Init$($this) :
    RuntimeException_init_$Init$($this)
    UnsupportedOperationException.call($this)
    return $this

  def UnsupportedOperationException_init_$Create$() :
     tmp = UnsupportedOperationException_init_$Init$(Object.create(UnsupportedOperationException.prototype))
    captureStack(tmp, UnsupportedOperationException_init_$Create$)
    return tmp

  def UnsupportedOperationException_init_$Init$_0(message, $this) :
    RuntimeException_init_$Init$_0(message, $this)
    UnsupportedOperationException.call($this)
    return $this

  def UnsupportedOperationException_init_$Create$_0(message) :
     tmp = UnsupportedOperationException_init_$Init$_0(message, Object.create(UnsupportedOperationException.prototype))
    captureStack(tmp, UnsupportedOperationException_init_$Create$_0)
    return tmp

  def UnsupportedOperationException_init_$Init$_1(message, cause, $this) :
    RuntimeException_init_$Init$_1(message, cause, $this)
    UnsupportedOperationException.call($this)
    return $this

  def UnsupportedOperationException_init_$Create$_1(message, cause) :
     tmp = UnsupportedOperationException_init_$Init$_1(message, cause, Object.create(UnsupportedOperationException.prototype))
    captureStack(tmp, UnsupportedOperationException_init_$Create$_1)
    return tmp

  def UnsupportedOperationException_init_$Init$_2(cause, $this) :
    RuntimeException_init_$Init$_2(cause, $this)
    UnsupportedOperationException.call($this)
    return $this

  def UnsupportedOperationException_init_$Create$_2(cause) :
     tmp = UnsupportedOperationException_init_$Init$_2(cause, Object.create(UnsupportedOperationException.prototype))
    captureStack(tmp, UnsupportedOperationException_init_$Create$_2)
    return tmp

  def UnsupportedOperationException() :
    captureStack(this, UnsupportedOperationException)

  UnsupportedOperationException.$metadata$ = {
    simpleName: 'UnsupportedOperationException',
    kind: 'class',
    interfaces: []

  def NullPointerException_init_$Init$($this) :
    RuntimeException_init_$Init$($this)
    NullPointerException.call($this)
    return $this

  def NullPointerException_init_$Create$() :
     tmp = NullPointerException_init_$Init$(Object.create(NullPointerException.prototype))
    captureStack(tmp, NullPointerException_init_$Create$)
    return tmp

  def NullPointerException_init_$Init$_0(message, $this) :
    RuntimeException_init_$Init$_0(message, $this)
    NullPointerException.call($this)
    return $this

  def NullPointerException_init_$Create$_0(message) :
     tmp = NullPointerException_init_$Init$_0(message, Object.create(NullPointerException.prototype))
    captureStack(tmp, NullPointerException_init_$Create$_0)
    return tmp

  def NullPointerException() :
    captureStack(this, NullPointerException)

  NullPointerException.$metadata$ = {
    simpleName: 'NullPointerException',
    kind: 'class',
    interfaces: []

  def IndexOutOfBoundsException_init_$Init$($this) :
    RuntimeException_init_$Init$($this)
    IndexOutOfBoundsException.call($this)
    return $this

  def IndexOutOfBoundsException_init_$Create$() :
     tmp = IndexOutOfBoundsException_init_$Init$(Object.create(IndexOutOfBoundsException.prototype))
    captureStack(tmp, IndexOutOfBoundsException_init_$Create$)
    return tmp

  def IndexOutOfBoundsException_init_$Init$_0(message, $this) :
    RuntimeException_init_$Init$_0(message, $this)
    IndexOutOfBoundsException.call($this)
    return $this

  def IndexOutOfBoundsException_init_$Create$_0(message) :
     tmp = IndexOutOfBoundsException_init_$Init$_0(message, Object.create(IndexOutOfBoundsException.prototype))
    captureStack(tmp, IndexOutOfBoundsException_init_$Create$_0)
    return tmp

  def IndexOutOfBoundsException() :
    captureStack(this, IndexOutOfBoundsException)

  IndexOutOfBoundsException.$metadata$ = {
    simpleName: 'IndexOutOfBoundsException',
    kind: 'class',
    interfaces: []

  def NoWhenBranchMatchedException_init_$Init$($this) :
    RuntimeException_init_$Init$($this)
    NoWhenBranchMatchedException.call($this)
    return $this

  def NoWhenBranchMatchedException_init_$Create$() :
     tmp = NoWhenBranchMatchedException_init_$Init$(Object.create(NoWhenBranchMatchedException.prototype))
    captureStack(tmp, NoWhenBranchMatchedException_init_$Create$)
    return tmp

  def NoWhenBranchMatchedException_init_$Init$_0(message, $this) :
    RuntimeException_init_$Init$_0(message, $this)
    NoWhenBranchMatchedException.call($this)
    return $this

  def NoWhenBranchMatchedException_init_$Create$_0(message) :
     tmp = NoWhenBranchMatchedException_init_$Init$_0(message, Object.create(NoWhenBranchMatchedException.prototype))
    captureStack(tmp, NoWhenBranchMatchedException_init_$Create$_0)
    return tmp

  def NoWhenBranchMatchedException_init_$Init$_1(message, cause, $this) :
    RuntimeException_init_$Init$_1(message, cause, $this)
    NoWhenBranchMatchedException.call($this)
    return $this

  def NoWhenBranchMatchedException_init_$Create$_1(message, cause) :
     tmp = NoWhenBranchMatchedException_init_$Init$_1(message, cause, Object.create(NoWhenBranchMatchedException.prototype))
    captureStack(tmp, NoWhenBranchMatchedException_init_$Create$_1)
    return tmp

  def NoWhenBranchMatchedException_init_$Init$_2(cause, $this) :
    RuntimeException_init_$Init$_2(cause, $this)
    NoWhenBranchMatchedException.call($this)
    return $this

  def NoWhenBranchMatchedException_init_$Create$_2(cause) :
     tmp = NoWhenBranchMatchedException_init_$Init$_2(cause, Object.create(NoWhenBranchMatchedException.prototype))
    captureStack(tmp, NoWhenBranchMatchedException_init_$Create$_2)
    return tmp

  def NoWhenBranchMatchedException() :
    captureStack(this, NoWhenBranchMatchedException)

  NoWhenBranchMatchedException.$metadata$ = {
    simpleName: 'NoWhenBranchMatchedException',
    kind: 'class',
    interfaces: []

  def ClassCastException_init_$Init$($this) :
    RuntimeException_init_$Init$($this)
    ClassCastException.call($this)
    return $this

  def ClassCastException_init_$Create$() :
     tmp = ClassCastException_init_$Init$(Object.create(ClassCastException.prototype))
    captureStack(tmp, ClassCastException_init_$Create$)
    return tmp

  def ClassCastException_init_$Init$_0(message, $this) :
    RuntimeException_init_$Init$_0(message, $this)
    ClassCastException.call($this)
    return $this

  def ClassCastException_init_$Create$_0(message) :
     tmp = ClassCastException_init_$Init$_0(message, Object.create(ClassCastException.prototype))
    captureStack(tmp, ClassCastException_init_$Create$_0)
    return tmp

  def ClassCastException() :
    captureStack(this, ClassCastException)

  ClassCastException.$metadata$ = {
    simpleName: 'ClassCastException',
    kind: 'class',
    interfaces: []

  def UninitializedPropertyAccessException_init_$Init$($this) :
    RuntimeException_init_$Init$($this)
    UninitializedPropertyAccessException.call($this)
    return $this

  def UninitializedPropertyAccessException_init_$Create$() :
     tmp = UninitializedPropertyAccessException_init_$Init$(Object.create(UninitializedPropertyAccessException.prototype))
    captureStack(tmp, UninitializedPropertyAccessException_init_$Create$)
    return tmp

  def UninitializedPropertyAccessException_init_$Init$_0(message, $this) :
    RuntimeException_init_$Init$_0(message, $this)
    UninitializedPropertyAccessException.call($this)
    return $this

  def UninitializedPropertyAccessException_init_$Create$_0(message) :
     tmp = UninitializedPropertyAccessException_init_$Init$_0(message, Object.create(UninitializedPropertyAccessException.prototype))
    captureStack(tmp, UninitializedPropertyAccessException_init_$Create$_0)
    return tmp

  def UninitializedPropertyAccessException_init_$Init$_1(message, cause, $this) :
    RuntimeException_init_$Init$_1(message, cause, $this)
    UninitializedPropertyAccessException.call($this)
    return $this

  def UninitializedPropertyAccessException_init_$Create$_1(message, cause) :
     tmp = UninitializedPropertyAccessException_init_$Init$_1(message, cause, Object.create(UninitializedPropertyAccessException.prototype))
    captureStack(tmp, UninitializedPropertyAccessException_init_$Create$_1)
    return tmp

  def UninitializedPropertyAccessException_init_$Init$_2(cause, $this) :
    RuntimeException_init_$Init$_2(cause, $this)
    UninitializedPropertyAccessException.call($this)
    return $this

  def UninitializedPropertyAccessException_init_$Create$_2(cause) :
     tmp = UninitializedPropertyAccessException_init_$Init$_2(cause, Object.create(UninitializedPropertyAccessException.prototype))
    captureStack(tmp, UninitializedPropertyAccessException_init_$Create$_2)
    return tmp

  def UninitializedPropertyAccessException() :
    captureStack(this, UninitializedPropertyAccessException)

  UninitializedPropertyAccessException.$metadata$ = {
    simpleName: 'UninitializedPropertyAccessException',
    kind: 'class',
    interfaces: []

  def jsIn(lhs_hack, rhs_hack) :
     tmp0_unsafeCast_0 = lhs_hack in rhs_hack
    return tmp0_unsafeCast_0

  def jsBitwiseOr(lhs_hack, rhs_hack) :
     tmp0_unsafeCast_0 = lhs_hack | rhs_hack
    return tmp0_unsafeCast_0

  def jsTypeOf(value_hack) :
     tmp0_unsafeCast_0 = typeof value_hack
    return tmp0_unsafeCast_0

  def jsInstanceOf(obj_hack, jsClass_hack) :
     tmp0_unsafeCast_0 = obj_hack instanceof jsClass_hack
    return tmp0_unsafeCast_0

  def jsBitwiseAnd(lhs_hack, rhs_hack) :
     tmp0_unsafeCast_0 = lhs_hack & rhs_hack
    return tmp0_unsafeCast_0

  def toString_1(_this_, radix) :
    return toStringImpl(_this_, checkRadix(radix))

  def pythonTest() :
    println('Hello world')

  CombinedContext.prototype.plus_3 = CoroutineContext.prototype.plus_3
  UByteIterator.prototype.hasNext_37 = Iterator_3.prototype.hasNext_37
  UIntIterator.prototype.hasNext_37 = Iterator_3.prototype.hasNext_37
  ULongIterator.prototype.hasNext_37 = Iterator_3.prototype.hasNext_37
  UShortIterator.prototype.hasNext_37 = Iterator_3.prototype.hasNext_37
  ByteIterator.prototype.hasNext_37 = Iterator_3.prototype.hasNext_37
  IntIterator.prototype.hasNext_37 = Iterator_3.prototype.hasNext_37
  DoubleIterator.prototype.hasNext_37 = Iterator_3.prototype.hasNext_37
  FloatIterator.prototype.hasNext_37 = Iterator_3.prototype.hasNext_37
  LongIterator.prototype.hasNext_37 = Iterator_3.prototype.hasNext_37
  CharIterator.prototype.hasNext_37 = Iterator_3.prototype.hasNext_37
  BooleanIterator.prototype.hasNext_37 = Iterator_3.prototype.hasNext_37
  ShortIterator.prototype.hasNext_37 = Iterator_3.prototype.hasNext_37
  AbstractMutableList.prototype.get_31 = List.prototype.get_31
  KClassImpl.prototype._get_simpleName__4 = KClass.prototype._get_simpleName__4
  KClassImpl.prototype.isInstance_4 = KClass.prototype.isInstance_4
  UNDEFINED_RESULT = UNDEFINED_RESULT$init$()
  _stableSortingIsSupported = null
  output = output$init$()
  EmptyContinuation = EmptyContinuation$init$()
  INV_2_26 = INV_2_26$init$()
  INV_2_53 = INV_2_53$init$()
  functionClasses = functionClasses$init$()
  STRING_CASE_INSENSITIVE_ORDER = STRING_CASE_INSENSITIVE_ORDER$init$()
  REPLACEMENT_BYTE_SEQUENCE = REPLACEMENT_BYTE_SEQUENCE$init$()
  buf = new ArrayBuffer(8)
  bufFloat64 = bufFloat64$init$()
  bufFloat32 = bufFloat32$init$()
  bufInt32 = bufInt32$init$()
  lowIndex = lowIndex$init$()
  highIndex = 1 - lowIndex | 0
  OBJECT_HASH_CODE_PROPERTY_NAME = 'kotlinHashCodeValue$'
  POW_2_32 = 4.294967296E9
  ZERO = fromInt(0)
  ONE = fromInt(1)
  NEG_ONE = fromInt(-1)
  MAX_VALUE = new Long(-1, 2147483647)
  MIN_VALUE = new Long(0, -2147483648)
  TWO_PWR_24_ = fromInt(16777216)
  TWO_PWR_32_DBL_ = 4.294967296E9
  TWO_PWR_63_DBL_ = 9.223372036854776E18
  propertyRefClassMetadataCache = propertyRefClassMetadataCache$init$()
  return _
(typeof this['out-ir'] === 'undefined' ? { : this['out-ir'])
