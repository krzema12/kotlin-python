#!/bin/bash
set -e

mkdir -p python/e2e-tests/out

echo "Starting end-to-end tests"

for testcaseFile in python/e2e-tests/testcases/*.kt.py.txt; do
    baseFileName=$(basename -- "$testcaseFile")
    testName="${baseFileName%%.*}"
    echo "===== Executing '$testName' ====="

    awk '/--- Kotlin code ---/,/--- Python consumer ---/' "$testcaseFile" | tail -n +2 | head -n -1 > python/e2e-tests/out/kotlin-code.kt
    awk '/--- Python consumer ---/,/--- Expected output ---/' "$testcaseFile" | tail -n +2 | head -n -1 > python/e2e-tests/out/python-consumer.py
    awk '/--- Expected output ---/,0' "$testcaseFile" | tail -n +2 > python/e2e-tests/out/expected-output.txt

    echo "  Compiling to Python..."
    dist/kotlinc/bin/kotlinc-py \
      -libraries dist/kotlinc/lib/kotlin-stdlib-js.jar \
      -Xir-produce-py \
      -output python/e2e-tests/out/compiled.py \
      python/e2e-tests/out/kotlin-code.kt

    echo "  Running Python to produce the output..."
    python3 python/e2e-tests/out/python-consumer.py > python/e2e-tests/out/output.txt

    echo "  Comparing actual and expected output..."
    diff -u python/e2e-tests/out/expected-output.txt python/e2e-tests/out/output.txt

    echo "===== Finished with '$testName' ====="
done

echo "All done"
