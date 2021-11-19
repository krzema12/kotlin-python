/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.fir.analysis.diagnostics

import org.jetbrains.kotlin.fir.analysis.diagnostics.impl.BaseDiagnosticReporter
import org.jetbrains.kotlin.fir.analysis.diagnostics.impl.DiagnosticReporterWithSuppress
import org.jetbrains.kotlin.fir.analysis.diagnostics.impl.SimpleDiagnosticReporter

object DiagnosticReporterFactory {
    fun createReporter(disableSuppress: Boolean = false): BaseDiagnosticReporter {
        return if (disableSuppress) {
            SimpleDiagnosticReporter()
        } else {
            DiagnosticReporterWithSuppress()
        }
    }
}