## Generating with IR backend

```
dist/kotlinc/bin/kotlinc-py -libraries dist/kotlinc/lib/kotlin-stdlib-js.jar -Xir-produce-js -output python/experiments/out_ir.py python/experiments/python.kt
```

## Generating stats about missing IR mapping

```
less python/experiments/out_ir.py  | grep -Po "visit[a-zA-Z0-9_]+" | sort | uniq -c | sort -nr > python/experiments/missing.txt
```
