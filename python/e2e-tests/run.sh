#!/bin/bash
set -e

echo "Starting end-to-end tests"

for kotlinFile in python/e2e-tests/*.kt; do
    baseFileName=$(basename -- "$kotlinFile")
    testName="${baseFileName%.*}"
    echo "===== Executing '$testName' ====="

    echo "  Compiling to Python..."
    dist/kotlinc/bin/kotlinc-py \
      -libraries dist/kotlinc/lib/kotlin-stdlib-js.jar \
      -Xir-produce-js \
      -output python/e2e-tests/output.py \
      python/e2e-tests/$testName.kt

    echo "  Running Python to produce the output..."
    python3 python/e2e-tests/$testName.consumer.py > python/e2e-tests/output.txt

    echo "  Comparing actual and expected output..."
    diff -u python/e2e-tests/$testName.output.txt python/e2e-tests/output.txt
done

