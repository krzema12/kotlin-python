import org.jetbrains.kotlin.gradle.plugin.KotlinPlatformType
import org.jetbrains.kotlin.gradle.plugin.mpp.KotlinUsages

plugins {
    kotlin("jvm")
    id("jps-compatible")
}

val testJsRuntime by configurations.creating {  // todo: remove js stuff
    attributes {
        attribute(Usage.USAGE_ATTRIBUTE, objects.named(KotlinUsages.KOTLIN_RUNTIME))
        attribute(KotlinPlatformType.attribute, KotlinPlatformType.js)
    }
}

dependencies {
    // todo: review the dependencies and get rid of unneeded
    testRuntime(intellijDep())

    testCompile(protobufFull())
    testCompile(projectTests(":compiler:tests-common"))
    testCompileOnly(project(":compiler:frontend"))
    testCompileOnly(project(":compiler:cli"))
    testCompileOnly(project(":compiler:cli-js"))
    testCompileOnly(project(":compiler:util"))
    testCompileOnly(intellijCoreDep()) { includeJars("intellij-core") }
    testCompileOnly(intellijDep()) { includeJars("idea", "idea_rt", "util") }
    testCompile(project(":compiler:backend.py"))
    testCompile(project(":compiler:backend.wasm"))
    testCompile(project(":python:py.translator"))
    testCompile(project(":js:js.serializer"))
    testCompile(project(":js:js.dce"))
    testCompile(project(":js:js.engines"))
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
    testJsRuntime(kotlinStdlib("js"))
    if (!kotlinBuildProperties.isInJpsBuildIdeaSync) {
        testJsRuntime(project(":kotlin-test:kotlin-test-js")) // to be sure that kotlin-test-js built before tests runned
    }
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

    dependsOn(":kotlin-stdlib-js-ir:compileKotlinJs")  // todo: remove js stuff
    systemProperty("kotlin.js.full.stdlib.path", "libraries/stdlib/js-ir/build/classes/kotlin/js/main")  // todo: remove js stuff
    dependsOn(":kotlin-stdlib-js-ir-minimal-for-test:compileKotlinJs")  // todo: remove js stuff
    systemProperty("kotlin.js.reduced.stdlib.path", "libraries/stdlib/js-ir-minimal-for-test/build/classes/kotlin/js/main")  // todo: remove js stuff
    dependsOn(":kotlin-test:kotlin-test-js-ir:compileKotlinJs")  // todo: remove js stuff
    systemProperty("kotlin.js.kotlin.test.path", "libraries/kotlin.test/js-ir/build/classes/kotlin/js/main")  // todo: remove js stuff

    exclude("org/jetbrains/kotlin/python/test/wasm/semantics/*")  // todo: remove js stuff
    exclude("org/jetbrains/kotlin/python/test/es6/semantics/*")  // todo: remove js stuff

    include("org/jetbrains/kotlin/python/test/ir/semantics/*")

    jvmArgs("-da:jdk.nashorn.internal.runtime.RecompilableScriptFunctionData") // Disable assertion which fails due to a bug in nashorn (KT-23637)
}

testsJar()

val generateTests by generator("org.jetbrains.kotlin.generators.tests.GeneratePyTestsKt")
