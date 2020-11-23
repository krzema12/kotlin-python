# Python backend

The goal is to have Kotlin-Python interop, starting with being able to compile Kotlin to Python.

See discussion at https://discuss.kotlinlang.org/t/idea-python-backend/19852

## Progress

- [ ] Kotlin-Python interop
  - [ ] compile Kotlin to Python
    - [x] describe Python AST with Kotlin
      - [x] create a generic tool that converts [ASDL](https://www.usenix.org/legacy/publications/library/proceedings/dsl97/full_papers/wang/wang.pdf) to Kotlin entities
        - [x] create a parser of ASDL
        - [x] create a generator of Kotlin entities from parsed ASDL
        - [x] try to represent an example Python program, and fix any issues found
      - [x] convert [Python's grammar in ASDL](https://github.com/python/cpython/blob/master/Parser/Python.asdl) into AST entities
    - [ ] translate Kotlin IR to Python AST
      - [x] translate IR items present in the simple Python AST example (assignment, list, for loop, function invocation...)
      - [ ] move Python IR -> AST mapping logic to a separate module (don't piggy-back on JS stuff, like lowerings)
      - [x] make a simple `fun hello() = "hello"` function translated and executable by Python (rest of the bundle at least parses fine by Python)
      - [ ] set up box tests infra
      - [ ] translate all IR items
      - [ ] make all existing box tests pass
      - [ ] clean up before committing to master (if happens)
      - ...
    - [ ] generate Python code from Python AST
      - [x] AST items used in the simple example (unblocking end-to-end PoC)
      - [ ] all Python AST items
  - [ ] use Python from Kotlin
    - ...

## Running box tests

```
./gradlew :python:box.tests:pythonTest --tests "org.jetbrains.kotlin.python.test.ir.semantics.IrPythonCodegenBoxTestGenerated"
```

### Test stats

With no Python interpreter hooked into the tests and
* when `OK` returned from the interpreter interface: all passed
* when something else returned from the interpreter interface: **4512**/5367 failed
  (the ones that succeeded are `testAllFilesPresentIn...` tests which doesn't depend on the actual invocation of code under test)
