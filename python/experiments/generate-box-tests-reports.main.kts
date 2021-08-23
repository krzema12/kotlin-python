#!/usr/bin/env kotlin
import java.nio.file.Path
import java.nio.file.Paths
import java.util.Locale
import javax.xml.parsers.DocumentBuilderFactory

fun pathFromNamedArgument(argumentName: String): Path? =
    args.firstOrNull { it.startsWith("--$argumentName=") }
        ?.let { Paths.get(it.split("=")[1]) }

val targetFailedTestsReportPath: Path = pathFromNamedArgument("failed-tests-report-path")
    ?: Paths.get("python/experiments/failed-tests.txt")
val targetBoxTestsReportPath: Path = pathFromNamedArgument("box-tests-report-path")
    ?: Paths.get("python/experiments/box-tests-report.tsv")

val testResults = getTestResults(Paths.get("python/box.tests/build/test-results/pythonTest"))

testResults.writeFailedTestsSummary(targetFailedTestsReportPath)
testResults.writeSummaryTsvToFile(targetBoxTestsReportPath)

fun List<TestResult>.writeFailedTestsSummary(targetFile: Path) = targetFile.toFile().printWriter().use { out ->
    this
        .filter { it.status is TestStatus.Failed }
        .forEach { out.println("${it.name} FAILED") }
}

fun List<TestResult>.writeSummaryTsvToFile(targetFile: Path) = targetFile.toFile().printWriter().use { out ->
    out.println(listOf(
        "Name",
        "Status",
        "Time (s)",
        "Failure general reason",
        "Failure detailed reason",
        "Failed Kotlin compilation time (s)",
        "Failed Python execution time (s)",
    ).joinToString("\t"))
    forEach { testResult ->
        val statusAsString = when (testResult.status) {
            is TestStatus.Succeeded -> "Succeeded"
            is TestStatus.Failed -> "Failed"
        }
        val failureGeneralReason = testResult.status.extractFailureGeneralReason()

        val (failureDetailedReason, kotlinCompilationTime, pythonExecutionTime) =
            if (failureGeneralReason != null && testResult.status is TestStatus.Failed) {
                Triple(
                    testResult.status.extractFailureDetailedReason(failureGeneralReason),
                    if (failureGeneralReason == FailureGeneralReason.KotlinCompilation) testResult.status.message.extractDuration() else null,
                    if (failureGeneralReason == FailureGeneralReason.PythonExecution) testResult.status.message.extractDuration() else null,
                )
            } else Triple(null, null, null)
        out.println(listOf(
            testResult.name,
            statusAsString,
            testResult.timeSeconds,
            failureGeneralReason ?: "",
            failureDetailedReason ?: "",
            kotlinCompilationTime ?: "",
            pythonExecutionTime ?: "",
        ).joinToString("\t"))
    }
}

fun TestStatus.extractFailureGeneralReason(): FailureGeneralReason? {
    return if (this is TestStatus.Failed) {
        when {
            "Can't find compiled module for dependency" in message -> FailureGeneralReason.BoxTestsFailure
            "KotlinCompilationException" in message -> FailureGeneralReason.KotlinCompilation
            "PythonExecutionException" in message -> FailureGeneralReason.PythonExecution
            "ComparisonFailure: expected" in message -> FailureGeneralReason.AssertionFailed
            else -> FailureGeneralReason.Unknown
        }
    } else {
        null
    }
}

fun TestStatus.Failed.extractFailureDetailedReason(failureGeneralReason: FailureGeneralReason): String? {
    return when (failureGeneralReason) {
        FailureGeneralReason.BoxTestsFailure -> message.lines().first()
        FailureGeneralReason.KotlinCompilation -> stackTrace?.lines()?.firstOrNull { "Caused by:" in it }?.removePrefix("Caused by: ")
        FailureGeneralReason.PythonExecution -> message.lines().last()
        FailureGeneralReason.AssertionFailed -> message.lines().first()
        FailureGeneralReason.Unknown -> message.lines().first()
    }
}

fun String.extractDuration(): Float? {
    val match = Regex("time: (\\d+) ms").find(this)
    return match?.let {
        it.groups[1]?.value?.toFloat()?.div(1000.0f)
    }
}

enum class FailureGeneralReason {
    BoxTestsFailure,
    KotlinCompilation,
    PythonExecution,
    AssertionFailed,
    Unknown,
}

data class TestResult(
    val name: String,
    val status: TestStatus,
    val timeSeconds: Float,
)

sealed interface TestStatus {
    object Succeeded : TestStatus
    data class Failed(val message: String, val stackTrace: String?) : TestStatus
}

fun getTestResults(testReportsPath: Path): List<TestResult> =
    enumerateTestReportXMLFiles(testReportsPath)
        .flatMap { parseTestReportXMLFile(it) }
        .sortedBy { it.name }

fun enumerateTestReportXMLFiles(testReportsPath: Path): List<Path> {
    return testReportsPath.toFile()
        .listFiles { _, name -> name.lowercase(Locale.getDefault()).endsWith(".xml") }
        ?.map { it.toPath() } ?: throw RuntimeException("There was a problem with listing XML report files")
}

fun parseTestReportXMLFile(xmlFilePath: Path): List<TestResult> = sequence {
    val parsedXml = DocumentBuilderFactory.newInstance().newDocumentBuilder().parse(xmlFilePath.toFile())
    val testsuite = parsedXml.documentElement
    val testsuiteName = testsuite.attributes.getNamedItem("name").nodeValue
    val testcases = testsuite.getElementsByTagName("testcase")
    for (i in 0 until testcases.length) {
        val testcase = testcases.item(i)
        val testcaseName = testcase.attributes.getNamedItem("name").nodeValue
        val testcaseTime = testcase.attributes.getNamedItem("time").nodeValue.toFloat()
        val fullTestcaseName = "$testsuiteName > $testcaseName"

        data class TestcaseFailure(
            val message: String,
            val stackTrace: String?,
        )

        val testcaseFailures = sequence {
            for (f in 0 until testcase.childNodes.length) {
                if (testcase.childNodes.item(f).nodeName == "failure") {
                    yield(TestcaseFailure(
                        message = testcase.childNodes.item(f).attributes.getNamedItem("message").nodeValue,
                        stackTrace = testcase.childNodes.item(f).textContent))
                }
            }
        }.toList()
        assert(testcaseFailures.size <= 2) { "Testcase '$fullTestcaseName' has more than one failure!" }

        yield(
            TestResult(
                name = fullTestcaseName,
                status = if (testcaseFailures.isEmpty())
                    TestStatus.Succeeded
                else
                    TestStatus.Failed(
                        message = testcaseFailures.first().message,
                        stackTrace = testcaseFailures.first().stackTrace,
                    ),
                timeSeconds = testcaseTime,
            )
        )
    }
}.toList()

