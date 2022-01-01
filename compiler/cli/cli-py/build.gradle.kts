plugins {
    kotlin("jvm")
    id("jps-compatible")
}

dependencies {
    compile(project(":compiler:cli"))
    compile(project(":compiler:ir.tree.impl"))
    compile(project(":compiler:backend.py"))
    compile(project(":compiler:backend.wasm"))

    compileOnly(intellijCoreDep()) { includeJars("intellij-core") }
}

sourceSets {
    "main" { projectDefault() }
}
