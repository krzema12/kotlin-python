def (_, Kotlin) :
  'use strict'
  var println = Kotlin.kotlin.io.println_s8jyv4$
  def pythonTest() :
    println('Hello world')
  }
  _.pythonTest = pythonTest
  Kotlin.defineModule('out', _)
  return _
}
