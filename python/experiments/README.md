## Generating with classic backend

```
dist/kotlinc/bin/kotlinc-js -output python/experiments/out.js python/experiments/python.kt
```

## Generating with IR backend

```
dist/kotlinc/bin/kotlinc-js -libraries dist/kotlinc/lib/kotlin-stdlib-js.jar -Xir-produce-js -output python/experiments/out-ir.js python/experiments/python.kt
```
