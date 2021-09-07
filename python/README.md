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
      - [ ] move backend (Python IR -> AST mapping) logic to a separate module (don't piggy-back on JS stuff, like lowerings)
      - [ ] move frontend to a separate module (don't piggy-back on JS stuff)
      - [x] make a simple `fun hello() = "hello"` function translated and executable by Python (rest of the bundle at least parses fine by Python)
      - [x] set up box tests infra
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

```shell script
./gradlew :python:box.tests:pythonTest --tests "org.jetbrains.kotlin.python.test.ir.semantics.IrPythonCodegenBoxTestGenerated"
```

To speed up tests:

```shell script
# create ramdisk where temporary test py files are generated extensively:
sudo mount -t tmpfs -o size=10G myramdisk python/py.translator/testData  # don't forget to clean this dir sometimes
sudo mount -t tmpfs -o size=10G myramdisk1 /tmp

mount | tail -n 2  # check it's mounted successfully
sudo umount python/py.translator/testData  # unmount
sudo umount /tmp  # unmount
```

Setting `maxParallelForks` isn't required anymore since now Gradle parallelism is used.

### Generating reports

Go to the repository root and call:

```
python/experiments/generate-box-tests-reports.main.kts
```

It will generate various reports and summaries:
* `box-tests-report.tsv` - for each test, some useful info are produced, in particular about the reason why it failed
* `failed-tests.txt` - one failed test per line. It provides much less data, but it's still useful because it gives
   a cleaner diff comparing to `box-tests-report.tsv` when something changes. E.g. when the failure reason changes,
   this file won't be affected for a given test - all that matters is that it still fails

### Test stats

Current status: **1709**/5787 passed

### History (newest on top)

* after supporting const statements: **1709**/5787 passed (+4)

* after supporting set value statements: **1705**/5787 passed (+20)

* after resolving some name clashes: **1685**/5787 passed (+20: +22 passed, +2 failed because no support for default arguments and extension functions, but with clashes those functions were overriden by others and tests passed)

* after adding initial support for static fields: **1665**/5787 passed (+209)

* after changing varargs a bit (due to refactoring expr transformer): **1456**/5787 passed (+1)

* after supporting simple lambdas: **1455**/5787 passed (+89)

* after supporting most integer operations: **1366**/5787 passed (+52)
  
* after supporting float constants: **1314**/5787 passed (+2)

* after supporting do-while, break, continue: **1312**/5787 passed (+14)

* after supporting string concatenation: **1298**/5787 passed (+6)

* after supporting binary ops: **1292**/5787 passed (+87)

* after supporting arrays: **1205**/5787 passed (+8)

* after supporting unary ops: **1197**/5787 passed (+53)

* after supporting return statements: **1144**/5787 passed (+4)

* after supporting when expressions: **1140**/5787 passed (+62)

* after supporting when statements: **1078**/5787 passed (+7)

* after removing empty variable declaration: **1071**/5787 passed (+3)
  
* after supporting comparison: **1068**/5787 passed (+7)

* after updating to Kotlin 1.5.21: **1061**/5787 (incomparable)

* after supporting some constructors, some inheritance...: **1042**/5368 passed (+75)

* after adding support for class methods: **967**/5368 passed (+28)

* with Python interpreter in place, no other changes to the compiler: **939**/5368 passed (+84)

* with no Python interpreter hooked into the tests and
  * when `OK` returned from the interpreter interface: all passed
  * when something else returned from the interpreter interface: **855**/5368 passed
    (the ones that succeeded are `testAllFilesPresentIn...` tests which doesn't depend on the actual invocation of code under test)
