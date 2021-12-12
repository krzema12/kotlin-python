plugins {
    kotlin("jvm")
    id("jps-compatible")
}

dependencies {
    // todo: review the dependencies and get rid of unneeded
    testRuntime(intellijDep())

    testCompile(protobufFull())
    testCompile(projectTests(":compiler:tests-common"))
    testCompileOnly(project(":compiler:frontend"))
    testCompileOnly(project(":compiler:cli"))
    testCompileOnly(project(":compiler:util"))
    testCompileOnly(intellijCoreDep()) { includeJars("intellij-core") }
    testCompileOnly(intellijDep()) { includeJars("idea", "idea_rt", "util") }
    testCompile(project(":compiler:backend.py"))
    testCompile(project(":python:py.translator"))
    testCompile(project(":compiler:incremental-compilation-impl"))
    testCompile(commonDep("junit:junit"))
    testCompile(projectTests(":kotlin-build-common"))
    testCompile(projectTests(":generators:test-generator"))

    testCompile(intellijCoreDep()) { includeJars("intellij-core") }
    testCompile(project(":compiler:frontend"))
    testCompile(project(":compiler:cli"))
    testCompile(project(":compiler:util"))

    testRuntime(project(":kotlin-reflect"))

    testRuntime(intellijDep()) { includeJars("trove4j", "guava", "jdom", rootProject = rootProject) }

    testRuntime(kotlinStdlib())
    testRuntime(project(":kotlin-reflect"))
    testRuntime(project(":kotlin-preloader")) // it's required for ant tests
    testRuntime(project(":compiler:backend-common"))
    testRuntime(commonDep("org.fusesource.jansi", "jansi"))
}

sourceSets {
    "main" { none() }
    "test" { projectDefault() }
}

projectTest("pythonTest", parallel = true) {
    definePythonTestTask("python3.8")
}

projectTest("microPythonTest", parallel = true) {
    definePythonTestTask("micropython")
}

fun Test.definePythonTestTask(interpreterBinary: String) {
    doFirst {
        try {
            exec {
                executable = interpreterBinary
            }
        } catch (e: Throwable) {
            throw RuntimeException("There was a problem running '$interpreterBinary' binary! Please ensure it's installed.", e)
        }
    }
    dependsOn(":dist")
    workingDir = rootDir
    jvmArgs!!.removeIf { it.contains("-Xmx") }
    maxHeapSize = "3g"

    systemProperty("kotlin.py.interpreter.binary", interpreterBinary)

    dependsOn(":kotlin-stdlib-python:compileKotlin")  // todo: remove js stuff
    systemProperty("kotlin.js.full.stdlib.path", "libraries/stdlib/js-ir/build/classes/kotlin/js/main")  // todo: remove js stuff
    dependsOn(":kotlin-stdlib-js-ir-minimal-for-test:compileKotlinJs")  // todo: remove js stuff
    systemProperty("kotlin.js.reduced.stdlib.path", "libraries/stdlib/js-ir-minimal-for-test/build/classes/kotlin/js/main")  // todo: remove js stuff
    dependsOn(":kotlin-test:kotlin-test-js-ir:compileKotlinJs")  // todo: remove js stuff
    systemProperty("kotlin.js.kotlin.test.path", "libraries/kotlin.test/js-ir/build/classes/kotlin/js/main")  // todo: remove js stuff

    include("org/jetbrains/kotlin/python/test/ir/semantics/*")
}

testsJar()

val generateTests by generator("org.jetbrains.kotlin.generators.tests.GeneratePyTestsKt")
