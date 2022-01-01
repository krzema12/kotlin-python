/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.cli.common.arguments

import org.jetbrains.kotlin.cli.common.arguments.K2JsArgumentConstants.*
import org.jetbrains.kotlin.cli.common.messages.MessageCollector
import org.jetbrains.kotlin.config.LanguageFeature
import org.jetbrains.kotlin.config.LanguageVersionSettings

class K2PyCompilerArguments : CommonCompilerArguments() {
    companion object {
        @JvmStatic private val serialVersionUID = 0L
    }

    @GradleOption(DefaultValues.StringNullDefault::class)
    @Argument(value = "-output", valueDescription = "<filepath>", description = "Destination *.js file for the compilation result")
    var outputFile: String? by NullableStringFreezableVar(null)

    @Argument(
            value = "-libraries",
            valueDescription = "<path>",
            description = "Paths to Kotlin libraries with .meta.js and .kjsm files, separated by system path separator"
    )
    var libraries: String? by NullableStringFreezableVar(null)

    @Argument(
        value = "-Xrepositories",
        valueDescription = "<path>",
        description = "Paths to additional places where libraries could be found"
    )
    var repositries: String? by NullableStringFreezableVar(null)

    @GradleOption(DefaultValues.JsMain::class)
    @Argument(
        value = "-main",
        valueDescription = "{$CALL|$NO_CALL}",
        description = "Define whether the `main` function should be called upon execution")
    var main: String? by NullableStringFreezableVar(null)

    @Argument(
            value = "-output-prefix",
            valueDescription = "<path>",
            description = "Add the content of the specified file to the beginning of output file"
    )
    var outputPrefix: String? by NullableStringFreezableVar(null)

    @Argument(
            value = "-output-postfix",
            valueDescription = "<path>",
            description = "Add the content of the specified file to the end of output file"
    )
    var outputPostfix: String? by NullableStringFreezableVar(null)

    // Advanced options

    @Argument(
        value = "-Xir-produce-klib-dir",
        description = "Generate unpacked KLIB into parent directory of output JS file.\n" +
                "In combination with -meta-info generates both IR and pre-IR versions of library."
    )
    var irProduceKlibDir: Boolean by FreezableVar(false)

    @Argument(
        value = "-Xir-produce-klib-file",
        description = "Generate packed klib into file specified by -output. Disables pre-IR backend"
    )
    var irProduceKlibFile: Boolean by FreezableVar(false)

    @Argument(value = "-Xir-produce-js", description = "Generates JS file using IR backend. Also disables pre-IR backend")
    var irProduceJs: Boolean by FreezableVar(false)

    @Argument(value = "-Xir-dce", description = "Perform experimental dead code elimination")
    var irDce: Boolean by FreezableVar(false)

    @Argument(
        value = "-Xir-dce-runtime-diagnostic",
        valueDescription = "{$RUNTIME_DIAGNOSTIC_LOG|$RUNTIME_DIAGNOSTIC_EXCEPTION}",
        description = "Enable runtime diagnostics when performing DCE instead of removing declarations"
    )
    var irDceRuntimeDiagnostic: String? by NullableStringFreezableVar(null)

    @Argument(value = "-Xir-dce-driven", description = "Perform a more experimental faster dead code elimination")
    var irDceDriven: Boolean by FreezableVar(false)

    @Argument(value = "-Xir-dce-print-reachability-info", description = "Print declarations' reachability info to stdout during performing DCE")
    var irDcePrintReachabilityInfo: Boolean by FreezableVar(false)

    @Argument(value = "-Xir-property-lazy-initialization", description = "Perform lazy initialization for properties")
    var irPropertyLazyInitialization: Boolean by FreezableVar(false)

    @Argument(
        value = "-Xir-module-name",
        valueDescription = "<name>",
        description = "Specify a compilation module name for IR backend"
    )
    var irModuleName: String? by NullableStringFreezableVar(null)

    @Argument(value = "-Xir-legacy-property-access", description = "Force property access via JS properties (requires -Xir-export-all)")
    var irLegacyPropertyAccess: Boolean by FreezableVar(false)

    @Argument(value = "-Xir-per-module-output-name", description = "Adds a custom output name to the splitted js files")
    var irPerModuleOutputName: String? by NullableStringFreezableVar(null)

    @Argument(
        value = "-Xinclude",
        valueDescription = "<path>",
        description = "A path to an intermediate library that should be processed in the same manner as source files."
    )
    var includes: String? by NullableStringFreezableVar(null)

    @Argument(
        value = "-Xcache-directories",
        valueDescription = "<path>",
        description = "A path to cache directories"
    )
    var cacheDirectories: String? by NullableStringFreezableVar(null)

    @Argument(value = "-Xir-build-cache", description = "Use compiler to build cache")
    var irBuildCache: Boolean by FreezableVar(false)

    @GradleOption(DefaultValues.BooleanFalseDefault::class)
    @Argument(value = "-Xfriend-modules-disabled", description = "Disable internal declaration export")
    var friendModulesDisabled: Boolean by FreezableVar(false)

    @Argument(
            value = "-Xfriend-modules",
            valueDescription = "<path>",
            description = "Paths to friend modules"
    )
    var friendModules: String? by NullableStringFreezableVar(null)

    @Argument(
        value = "-Xenable-extension-functions-in-externals",
        description = "Enable extensions functions members in external interfaces"
    )
    var extensionFunctionsInExternals: Boolean by FreezableVar(false)

    @Argument(value = "-Xfake-override-validator", description = "Enable IR fake override validator")
    var fakeOverrideValidator: Boolean by FreezableVar(false)

    @Argument(value = "-Xerror-tolerance-policy", description = "Set up error tolerance policy (NONE, SEMANTIC, SYNTAX, ALL)")
    var errorTolerancePolicy: String? by NullableStringFreezableVar(null)

    override fun checkIrSupport(languageVersionSettings: LanguageVersionSettings, collector: MessageCollector) {
        // Python backend is IR-based, so IR is supported. Just do nothing.
    }

    override fun configureLanguageFeatures(collector: MessageCollector): MutableMap<LanguageFeature, LanguageFeature.State> {
        return super.configureLanguageFeatures(collector).apply {
            if (extensionFunctionsInExternals) {
                this[LanguageFeature.JsEnableExtensionFunctionInExternals] = LanguageFeature.State.ENABLED
            }
        }
    }
}
