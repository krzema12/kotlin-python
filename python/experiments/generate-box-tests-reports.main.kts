#!/usr/bin/env kotlin
@file:DependsOn("org.eclipse.jgit:org.eclipse.jgit:4.6.0.201612231935-r")
@file:DependsOn("org.jetbrains.lets-plot:lets-plot-common:2.1.0")
@file:DependsOn("org.jetbrains.lets-plot:lets-plot-kotlin-jvm:3.0.2")
@file:DependsOn("io.github.microutils:kotlin-logging:1.12.5") // To fix missing runtime dependency.

import jetbrains.datalore.plot.base.render.svg.SvgUID
import jetbrains.letsPlot.export.ggsave
import jetbrains.letsPlot.geom.geomPoint
import jetbrains.letsPlot.geom.geomStep
import jetbrains.letsPlot.ggsize
import jetbrains.letsPlot.label.ylab
import jetbrains.letsPlot.letsPlot
import jetbrains.letsPlot.scale.scaleXDateTime
import jetbrains.letsPlot.scale.scaleYContinuous
import org.eclipse.jgit.api.Git
import org.eclipse.jgit.lib.Repository
import org.eclipse.jgit.revwalk.RevTree
import org.eclipse.jgit.treewalk.TreeWalk
import java.io.File
import java.nio.file.Path
import java.nio.file.Paths
import java.time.Instant
import java.time.temporal.ChronoUnit
import java.util.*
import javax.xml.parsers.DocumentBuilderFactory
import kotlin.text.Charsets.UTF_8

fun pathFromNamedArgument(argumentName: String): Path? =
    stringFromNamedArgument(argumentName)?.let { Paths.get(it) }

fun stringFromNamedArgument(argumentName: String): String? =
    args.firstOrNull { it.startsWith("--$argumentName=") }
        ?.let { it.split("=")[1] }

val testTask: String = stringFromNamedArgument("test-task")
    ?: "pythonTest".also { println("'test-task' parameter is missing, using default 'pythonTest'") }
val targetFailedTestsReportPath: Path = pathFromNamedArgument("failed-tests-report-path")
    ?: Paths.get("python/box.tests/reports/$testTask/failed-tests.txt")
val targetBoxTestsReportPath: Path = pathFromNamedArgument("box-tests-report-path")
    ?: Paths.get("python/box.tests/reports/$testTask/box-tests-report.tsv")
val failureCountReportPath: Path = pathFromNamedArgument("failure-count-report-path")
    ?: Paths.get("python/box.tests/reports/$testTask/failure-count.tsv")
val gitHistoryPlotPath: Path = pathFromNamedArgument("git-history-plot-path")
    ?: Paths.get("python/box.tests/reports/git-history-plot.svg")

val testResults = getTestResults(Paths.get("python/box.tests/build/test-results/$testTask"))

testResults.writeFailedTestsSummary(targetFailedTestsReportPath)
testResults.writeSummaryTsvToFile(targetBoxTestsReportPath)
testResults.writeFailureCount(failureCountReportPath)
generateGitHistoryPlot(gitHistoryPlotPath)

fun List<TestResult>.writeFailedTestsSummary(targetFile: Path) = targetFile.toFile().printWriter().use { out ->
    this
        .filter { it.status is TestStatus.Failed }
        .forEach { out.println("${it.name} FAILED") }
}

fun List<TestResult>.writeSummaryTsvToFile(targetFile: Path) = targetFile.toFile().printWriter().use { out ->
    out.println(listOf(
        "Name",
        "Status",
//        "Time (s)",
        "Failure general reason",
        "Failure detailed reason",
//        "Failed Kotlin compilation time (s)",
//        "Failed Python execution time (s)",
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

        fun String.makeEasyPastableToGradle() = replace(" > ", ".")

        out.println(listOf(
            testResult.name.makeEasyPastableToGradle(),
            statusAsString,
//            testResult.timeSeconds,
            failureGeneralReason ?: "",
            failureDetailedReason?.removeVaryingParts() ?: "",
//            kotlinCompilationTime ?: "",
//            pythonExecutionTime ?: "",
        ).joinToString("\t"))
    }
}

fun List<TestResult>.writeFailureCount(targetFile: Path) = targetFile.toFile().printWriter().use { out ->
    this
        .asSequence()
        .map { it.status }
        .filterIsInstance<TestStatus.Failed>()
        .map { it.extractFailureGeneralReason()?.let { reason -> it.extractFailureDetailedReason(reason)?.removeVaryingParts() }  }
        .filter { it != null && it.isNotEmpty() }
        .groupBy { it }
        .map { (reason, list) -> reason to list.size }
        .sortedWith(
            compareBy(
                { (_, count) -> -count },
                { (reason, _) -> reason },
            )
        )
        .forEach { (reason, count) -> out.println("$count\t$reason") }
}

fun String.removeVaryingParts() =
    // The exception message is sometimes provided locally and not provided on CI, so trying to normalize it.
    (if (startsWith("java.lang.ClassCastException")) "java.lang.ClassCastException" else this)
        .replace(Regex("\\S+\\.kt"), "<path-truncated>")
        .replace(Regex("\\S+\\.py"), "<path-truncated>")
        .replace(Regex("@[a-f0-9]{1,8}"), "@...")
        .replace(Regex("0x[a-f0-9]{12}"), "[address]")
        .replace(Regex("allocating \\d+ .*"), "allocating XXX bytes")
        .replace(Regex("object at [a-f0-9]{1,12}"), "object at [address]")

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

fun generateGitHistoryPlot(gitHistoryPlotPath: Path) {
    val kotlinPythonAuthors = setOf(
        "git@krzeminski.it",
        "servbul@yandex.ru",
    )
    // E.g. incorrectly changed failed-tests.txt, back when CI didn't verify it.
    val commitsContainingIncorrectData = setOf(
        "d1a115d863cd05bea43d39a68421d240d4792ee3",
        "59a97e4199c9824d09cee1fd3437ef0de789b45d",
    )

    data class DataPoint(
        val date: Date,
        val testsAll: Int,
        val testsPassedPython: Int,
        val testsPassedMicroPython: Int?,
    )

    val git = Git.open(File("."))

    val data = git.log().call()
        .filter { it.authorIdent.emailAddress in kotlinPythonAuthors }
        .filter { it.name !in commitsContainingIncorrectData }
        .sortedBy { it.commitTime }
        .filter {
            val numberOfAllTests = git.repository.getNumberOfAllTests(it.tree)
            val numberOfAllTestsPrev = git.repository.getNumberOfAllTests(it.parents[0].tree)
            val numberOfFailedPythonTests = git.repository.getNumberOfFailedTests(it.tree, "pythonTest")
            val numberOfFailedPythonTestsPrev = git.repository.getNumberOfFailedTests(it.parents[0].tree, "pythonTest")
            val numberOfFailedMicroPythonTests = git.repository.getNumberOfFailedTests(it.tree, "microPythonTest")
            val numberOfFailedMicroPythonTestsPrev = git.repository.getNumberOfFailedTests(it.parents[0].tree, "microPythonTest")

            numberOfAllTests != numberOfAllTestsPrev || numberOfFailedPythonTests != numberOfFailedPythonTestsPrev ||
                    numberOfFailedMicroPythonTests != numberOfFailedMicroPythonTestsPrev
        }
        .groupBy { Instant.ofEpochSecond(it.commitTime.toLong()).truncatedTo(ChronoUnit.DAYS) }
        .mapNotNull { it.value.lastOrNull() }
        .mapNotNull {
            val instant = Instant.ofEpochSecond(it.commitTime.toLong())
            val numberOfFailedTestsPython = git.repository.getNumberOfFailedTests(it.tree, "pythonTest")
            val numberOfFailedTestsMicroPython = git.repository.getNumberOfFailedTests(it.tree, "microPythonTest")
            val numberOfAllTests = git.repository.getNumberOfAllTests(it.tree)
            if (numberOfAllTests != null && numberOfFailedTestsPython != null) {
                val numberOfPassedTestsPython = numberOfAllTests - numberOfFailedTestsPython
                val numberOfPassedTestsMicroPython = if (numberOfFailedTestsMicroPython != null) {
                    numberOfAllTests - numberOfFailedTestsMicroPython
                } else {
                    null
                }
                DataPoint(
                    date = Date.from(instant),
                    testsAll = numberOfAllTests,
                    testsPassedPython = numberOfPassedTestsPython,
                    testsPassedMicroPython = numberOfPassedTestsMicroPython,
                )
            } else {
                null
            }
        }

    SvgUID.setUpForTest()  // make the svg deterministic as discussed here: https://github.com/JetBrains/lets-plot/issues/492

    val dataForPlot = mapOf(
        "date" to data.map { it.date } + data.map { it.date } + data.map { it.date },
        "tests" to data.map { it.testsAll } + data.map { it.testsPassedPython } + data.map { it.testsPassedMicroPython },
        "type" to List(data.size) { "all" } + List(data.size) { "passed (Python)" } + List(data.size) { "passed (MicroPython)" },
    )
    val p = letsPlot(dataForPlot) { x = "date"; y = "tests"; color = "type" } +
            geomStep() +
            geomPoint() +
            scaleXDateTime(format = "%b %Y") +
            ylab("# of box tests") +
            scaleYContinuous(limits = Pair(0, null), expand = listOf(0)) +
            ggsize(1000, 500)
    ggsave(p, gitHistoryPlotPath.fileName.toString(), path = gitHistoryPlotPath.parent?.toString() ?: ".")
}

fun Repository.getNumberOfFailedTests(tree: RevTree, testTask: String): Int? {
    // Trying two paths, to be able to fetch number of failed tests for various file layouts that the repository had.
    val failedTestsFile = if (testTask == "pythonTest") {
        readFileAsText(tree, Paths.get("python/experiments/failed-tests.txt"))
            ?: readFileAsText(tree, Paths.get("python/box.tests/reports/pythonTest/failed-tests.txt"))
    } else {
        readFileAsText(tree, Paths.get("python/box.tests/reports/$testTask/failed-tests.txt"))
    }
    return failedTestsFile?.lines()?.size
}

fun Repository.getNumberOfAllTests(tree: RevTree): Int? {
    val readme = readFileAsText(tree, Paths.get("python/README.md")) ?: return null
    val numericResultsRegex = Regex("\\*\\*\\d+\\*\\*\\/(\\d+)")
    val (allTests) = numericResultsRegex.find(readme)?.destructured ?: return null
    return allTests.toInt()
}

/**
 * @return [null] if the file does not exist.
 */
fun Repository.readFileAsText(tree: RevTree, path: Path): String? {
    val treeWalk = TreeWalk.forPath(this, path.toString(), tree) ?: return null
    val objectId = treeWalk.getObjectId(0)
    val objectReader = newObjectReader()
    val result = objectReader.open(objectId)
    objectReader.close()
    return String(result.bytes, UTF_8)
}
