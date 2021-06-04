/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.py.inline.clean

import org.jetbrains.kotlin.js.backend.ast.JsNode
import org.jetbrains.kotlin.py.inline.util.IdentitySet
import java.util.*

internal class ReferenceTracker<in Reference, RemoveCandidate : JsNode> {
    private val reachable = IdentityHashMap<Reference, Boolean>()
    private val removableCandidates = IdentityHashMap<Reference, RemoveCandidate>()
    private val referenceFromTo = IdentityHashMap<Reference, MutableSet<Reference>>()
    private val visited = IdentitySet<Reference>()

    val removable: List<RemoveCandidate>
        get() {
            return reachable
                        .filter { !it.value }
                        .map { removableCandidates[it.key]!! }
        }

    fun addCandidateForRemoval(reference: Reference, candidate: RemoveCandidate) {
        assert(!isReferenceToRemovableCandidate(reference)) { "Candidate for removal cannot be reassigned: $candidate" }

        removableCandidates.put(reference, candidate)
        reachable.put(reference, false)
    }

    fun addRemovableReference(referrer: Reference, referenced: Reference) {
        if (!isReferenceToRemovableCandidate(referenced)) return

        getReferencedBy(referrer).add(referenced)

        if (isReachable(referrer)) {
            markReachable(referenced)
        }
    }

    fun markReachable(reference: Reference) {
        if (!isReferenceToRemovableCandidate(reference)) return

        visited.add(reference)
        getReferencedBy(reference)
                .filterNot { it in visited }
                .filter { isReferenceToRemovableCandidate(it) && !isReachable(it) }
                .forEach { markReachable(it) }

        visited.remove(reference)
        reachable[reference] = true
    }

    private fun getReferencedBy(referrer: Reference): MutableSet<Reference> {
        return referenceFromTo.getOrPut(referrer, { IdentitySet<Reference>() })
    }

    fun isReferenceToRemovableCandidate(ref: Reference): Boolean {
        return removableCandidates.containsKey(ref)
    }

    private fun isReachable(ref: Reference): Boolean {
        return reachable[ref] ?: false
    }
}
