if (typeof kotlin === 'undefined') :
  throw new Error("krzema12 classic mod: Error loading module 'out'. Its dependency 'kotlin' was not found. Please, check whether 'kotlin' is loaded prior to 'out'.")
}var out = def (_, Kotlin) :
  'use strict'
  var println = Kotlin.kotlin.io.println_s8jyv4$
  def pythonTest() :
    println('Hello world')
  }
  _.pythonTest = pythonTest
  Kotlin.defineModule('out', _)
  return _
}(typeof out === 'undefined' ? {} : out, kotlin)
