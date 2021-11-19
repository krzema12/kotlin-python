
plugins {
    kotlin("jvm")
    id("jps-compatible")
}

dependencies {
    compile(project(":core:descriptors"))
    compile(project(":core:descriptors.jvm"))
    compile(project(":core:deserialization"))
    compile(project(":compiler:util"))
    compile(project(":compiler:frontend"))
    compile(project(":compiler:frontend.java"))
    compile(project(":compiler:cli"))
    compile(project(":compiler:cli-js"))
    compile(project(":kotlin-build-common"))
    compile(project(":daemon-common"))
    compileOnly(intellijCoreDep()) { includeJars("intellij-core") }

    testCompile(commonDep("junit:junit"))
    testCompile(project(":kotlin-test:kotlin-test-junit"))
    testCompile(kotlinStdlib())
    testCompile(projectTests(":kotlin-build-common"))
    testCompile(projectTests(":compiler:tests-common"))
    testCompile(intellijCoreDep()) { includeJars("intellij-core") }
    testCompile(intellijDep()) { includeJars("log4j", "jdom") }
    testRuntime(project(":kotlin-reflect"))
    testRuntime(project(":core:descriptors.runtime"))
    testRuntime(intellijDep()) { includeJars("lz4-java", "jna", rootProject = rootProject) }
}

sourceSets {
    "main" { projectDefault() }
    "test" { projectDefault() }
}

projectTest(parallel = true) {
    workingDir = rootDir
    dependsOn(":kotlin-stdlib-js-ir:packFullRuntimeKLib")
}

projectTest("testJvmICWithJdk11", parallel = true) {
    workingDir = rootDir
    filter {
        includeTestsMatching("org.jetbrains.kotlin.incremental.IncrementalJvmCompilerRunnerTestGenerated*")
    }
    javaLauncher.set(project.getToolchainLauncherFor(JdkMajorVersion.JDK_11))
}

testsJar()
