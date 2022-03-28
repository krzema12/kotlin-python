#!/usr/bin/env kotlin

@file:DependsOn("it.krzeminski:github-actions-kotlin-dsl:0.10.0")
@file:Import("Common.main.kts")

import it.krzeminski.githubactions.actions.actions.CheckoutV2
import it.krzeminski.githubactions.actions.actions.CheckoutV2.FetchDepth.Infinite
import it.krzeminski.githubactions.domain.RunnerType.UbuntuLatest
import it.krzeminski.githubactions.domain.triggers.Push
import it.krzeminski.githubactions.domain.triggers.WorkflowDispatch
import it.krzeminski.githubactions.dsl.workflow
import java.nio.file.Paths

val buildAndTest = workflow(
    name = "Build and test",
    on = listOf(Push(), WorkflowDispatch()),
    sourceFile = Paths.get(".github/workflows/_generate_workflows.main.kts"),
    targetFile = Paths.get(".github/workflows/build_and_test.yml"),
) {
    job(
        name = "build_and_test",
        runsOn = UbuntuLatest,
        strategyMatrix = mapOf(
            "testTask" to listOf(
                "pythonTest",
                "microPythonTest",
            )
        ),
    ) {
        uses(
            name = "Fetch the whole git history (to be able to calculate some stats based on it)",
            action = CheckoutV2(fetchDepth = Infinite),
        )
        run(
            name = "Install Kotlin for scripting",
            command = "sudo snap install --classic kotlin",
        )
        run(
            name = "Install MicroPython",
            command = "sudo snap install micropython",
            condition = "\${{ matrix.testTask == 'microPythonTest' }}",
        )
        run(
            name = "Disable old Java for Kotlin",
            command = "echo \"kotlin.build.isObsoleteJdkOverrideEnabled=true\" > local.properties",
        )

        run(
            name = "Clean",
            command = gradle("clean"),
        )
        run(
            name = "Run ast tests",
            command = gradle(":python:ast:test"),
            condition = "always()",
        )
        run(
            name = "Build",
            command = gradle("dist"),
        )

        run(
            name = "Compile python.kt to Python",
            command = """
                dist/kotlinc/bin/kotlinc-py \
                -libraries dist/kotlinc/lib/kotlin-stdlib-py-js.klib \
                -Xir-produce-py \
                -output out_ir.py \
                python/experiments/python.kt
            """.trimIndent(),
            condition = "always()",
        )
        run(
            name = "Compare out_ir.py",
            command = "diff -u out_ir.py python/experiments/generated/out_ir.py",
            condition = "always()",
        )

        run(
            name = "Compile python.kt to JavaScript",
            command = """
                dist/kotlinc/bin/kotlinc-js \
                -libraries dist/kotlinc/lib/kotlin-stdlib-js.jar \
                -Xir-produce-js \
                -Xir-property-lazy-initialization \
                -output out-ir.js \
                python/experiments/python.kt
            """.trimIndent(),
            condition = "always()",
        )
        run(
            name = "Compare out-ir.js",
            command = "diff -u out-ir.js python/experiments/generated/out-ir.js",
            condition = "always()",
        )

        run(
            name = "Generate stats about missing IR mapping",
            command = """
                less python/experiments/generated/out_ir.py \
                | grep -Po "visit[a-zA-Z0-9_]+" \
                | sort \
                | uniq -c \
                | sort -nr \
                > missing.txt
            """.trimIndent(),
            condition = "always()",
        )
        run(
            name = "Compare missing.txt",
            command = "diff -u missing.txt python/experiments/generated/missing.txt",
            condition = "always()",
        )

        run(
            name = "Run end-to-end tests",
            command = withJavaConfigured("python/e2e-tests/run.sh"),
            condition = "\${{ matrix.testTask == 'pythonTest' }}", // TODO: run e2e tests for MicroPython too (#85)
        )

        run(
            name = "Run box tests (succeed even if they fail)",
            command = "${gradle(":python:box.tests:\${{ matrix.testTask }}")} || true",
            condition = "always()",
        )

        val failedTestsFile = "failed-tests.txt"
        val boxTestsReportFile = "box-tests-report.tsv"
        val failureCountFile = "failure-count.tsv"

        fun reportsFile(fileName: String) =
            "python/box.tests/reports/\${{ matrix.testTask }}/$fileName"

        run(
            name = "Generate box tests reports",
            command = """
                python/experiments/generate-box-tests-reports.main.kts \
                --test-task=${"$"}{{ matrix.testTask }} \
                --failed-tests-report-path=$failedTestsFile \
                --box-tests-report-path=$boxTestsReportFile \
                --failure-count-report-path=$failureCountFile
            """.trimIndent(),
            condition = "always()",
        )
        run(
            name = "Compare $failedTestsFile",
            command = "diff -u $failedTestsFile ${reportsFile(failedTestsFile)}",
            condition = "always()",
        )
        run(
            name = "Compare $boxTestsReportFile",
            command = "diff -u $boxTestsReportFile ${reportsFile(boxTestsReportFile)}",
            condition = "always()",
        )
        run(
            name = "Compare $failureCountFile",
            command = "diff -u $failureCountFile ${reportsFile(failureCountFile)}",
            condition = "always()",
        )
    }
}

