/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.cli.common.arguments

import org.jetbrains.kotlin.cli.common.arguments.K2JsArgumentConstants.CALL
import org.jetbrains.kotlin.cli.common.arguments.K2JsArgumentConstants.NO_CALL
import org.jetbrains.kotlin.cli.common.messages.MessageCollector
import org.jetbrains.kotlin.config.LanguageFeature
import org.jetbrains.kotlin.config.LanguageVersionSettings

class K2PyCompilerArguments : CommonCompilerArguments() {
    companion object {
        @JvmStatic private val serialVersionUID = 0L
    }

    @GradleOption(DefaultValues.StringNullDefault::class)
    @Argument(value = "-output", valueDescription = "<filepath>", description = "Destination *.py file for the compilation result")
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

    @Argument(value = "-Xir-produce-py", description = "Generates Python file using IR backend")
    var irProducePy: Boolean by FreezableVar(false)

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
