#!/usr/bin/env kotlin

@file:DependsOn("it.krzeminski:github-actions-kotlin-dsl:0.10.0")
@file:Import("Common.main.kts")

import it.krzeminski.githubactions.actions.actions.CheckoutV2
import it.krzeminski.githubactions.actions.actions.CheckoutV2.FetchDepth.Infinite
import it.krzeminski.githubactions.actions.actions.DownloadArtifactV2
import it.krzeminski.githubactions.actions.actions.UploadArtifactV2
import it.krzeminski.githubactions.domain.RunnerType.UbuntuLatest
import it.krzeminski.githubactions.domain.triggers.WorkflowDispatch
import it.krzeminski.githubactions.dsl.workflow
import it.krzeminski.githubactions.yaml.toYaml
import java.nio.file.Paths

val generateReportsWorkflow = workflow(
    name = "Generate reports",
    on = listOf(WorkflowDispatch()),
    sourceFile = Paths.get(".github/workflows/_generate_workflows.main.kts"),
    targetFile = Paths.get(".github/workflows/generate_reports.yml"),
) {
    val generateReports = job(
        name = "generate_reports",
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
            name = "Build",
            command = gradle("dist"),
        )

        run(
            name = "Compile python.kt to Python",
            command = """
                dist/kotlinc/bin/kotlinc-py \
                -libraries dist/kotlinc/lib/kotlin-stdlib-py-js.klib \
                -Xir-produce-py \
                -output python/experiments/generated/out_ir.py \
                python/experiments/python.kt
            """.trimIndent(),
            condition = "\${{ matrix.testTask == 'pythonTest' }}",
        )
        run(
            name = "Compile python.kt to JavaScript",
            command = """
                dist/kotlinc/bin/kotlinc-js \
                -libraries dist/kotlinc/lib/kotlin-stdlib-js.jar \
                -Xir-produce-js \
                -Xir-property-lazy-initialization \
                -output python/experiments/generated/out-ir.js \
                python/experiments/python.kt
            """.trimIndent(),
            condition = "\${{ matrix.testTask == 'pythonTest' }}",
        )

        run(
            name = "Generate stats about missing IR mapping",
            command = """
                less python/experiments/generated/out_ir.py \
                | grep -Po "visit[a-zA-Z0-9_]+" \
                | sort \
                | uniq -c \
                | sort -nr \
                > python/experiments/generated/missing.txt
            """.trimIndent(),
            condition = "\${{ matrix.testTask == 'pythonTest' }}",
        )

        run(
            name = "Run end-to-end tests",
            command = withJavaConfigured("python/e2e-tests/run.sh"),
            condition = "\${{ matrix.testTask == 'pythonTest' }}", // TODO: run e2e tests for MicroPython too (#85)
        )

        run(
            name = "Run box tests (succeed even if they fail)",
            command = "${gradle(":python:box.tests:\${{ matrix.testTask }}")} || true",
        )
        run(
            name = "Generate box tests reports",
            command = "python/experiments/generate-box-tests-reports.main.kts --test-task=\${{ matrix.testTask }}",
        )

        uses(
            name = "Upload common artifact",
            action = UploadArtifactV2(
                name = "common-artifact",
                path = listOf(
                    "python/box.tests/reports/git-history-plot.svg",
                    "python/experiments/generated",
                )
            ),
            condition = "\${{ matrix.testTask == 'pythonTest' }}",
        )
        uses(
            name = "Upload \${{ matrix.testTask }} artifact",
            action = UploadArtifactV2(
                name = "\${{ matrix.testTask }}-artifact",
                path = listOf("python/box.tests/reports/\${{ matrix.testTask }}"),
            )
        )
    }

    job(
        name = "update_reports",
        needs = listOf(generateReports),
        runsOn = UbuntuLatest,
    ) {
        uses(
            name = "Check out",
            action = CheckoutV2(),
        )

        uses(
            name = "Download common artifact",
            action = DownloadArtifactV2(
                name = "common-artifact",
                path = "python",
            )
        )
        uses(
            name = "Download pythonTest artifact",
            action = DownloadArtifactV2(
                name = "pythonTest-artifact",
                path = "python/box.tests/reports/pythonTest",
            )
        )
        uses(
            name = "Download microPythonTest artifact",
            action = DownloadArtifactV2(
                name = "microPythonTest-artifact",
                path = "python/box.tests/reports/microPythonTest",
            )
        )

        run(
            name = "Commit and push",
            command = """
                git config --global user.email "<>"
                git config --global user.name "GitHub Actions Bot"
                git add python/box.tests/reports python/experiments
                git commit --allow-empty -m "Generate reports for ${'$'}GITHUB_SHA"  # an empty commit explicitly shows that reports are up-to-date
                git push
            """.trimIndent()
        )
    }
}

