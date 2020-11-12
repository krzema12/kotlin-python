## Generating with classic backend

```
dist/kotlinc/bin/kotlinc-js -output kotlin-python/out.js kotlin-python/python.kt
```

## Generating with IR backend

```
dist/kotlinc/bin/kotlinc-js -libraries dist/kotlinc/lib/kotlin-stdlib-js.jar -Xir-produce-js -output kotlin-python/out-ir.js kotlin-python/python.kt
```
