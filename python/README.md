# Python backend

The goal is to have Kotlin-Python interop, starting with being able to compile Kotlin to Python.

See discussion at https://discuss.kotlinlang.org/t/idea-python-backend/19852

## Progress

- [ ] Kotlin-Python interop
  - [ ] compile Kotlin to Python
    - [ ] describe Python AST with Kotlin
      - [ ] create a generic tool that converts [ASDL](https://www.usenix.org/legacy/publications/library/proceedings/dsl97/full_papers/wang/wang.pdf) to Kotlin entities
        - [ ] **(in progress)** create a parser of ASDL
        - [ ] create a generator of Kotlin entities from parsed ASDL
        - ...
      - [ ] convert [Python's grammar in ASDL](https://github.com/python/cpython/blob/master/Parser/Python.asdl) into AST entities
      - ...
    - [ ] translate Kotlin IR to Python AST
      - ...
    - [ ] generate Python code from Python AST
      - ...
  - [ ] use Python from Kotlin
    - ...
