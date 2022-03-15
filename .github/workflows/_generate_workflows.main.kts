#!/usr/bin/env kotlin
@file:DependsOn("it.krzeminski:github-actions-kotlin-dsl:0.10.0")

@file:Import("build_and_test.main.kts")
@file:Import("generate_reports.main.kts")

import it.krzeminski.githubactions.yaml.writeToFile

listOf(
    buildAndTest,
    generateReportsWorkflow
).forEach { it.writeToFile() }

