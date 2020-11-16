## Generating with classic backend

```
dist/kotlinc/bin/kotlinc-js -output python/experiments/out.py python/experiments/python.kt
```

## Generating with IR backend

```
dist/kotlinc/bin/kotlinc-js -libraries dist/kotlinc/lib/kotlin-stdlib-js.jar -Xir-produce-js -output python/experiments/out-ir.py python/experiments/python.kt
```
