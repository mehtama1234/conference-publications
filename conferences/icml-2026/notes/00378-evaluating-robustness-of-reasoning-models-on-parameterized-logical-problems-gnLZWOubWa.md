# Evaluating Robustness of Reasoning Models on Parameterized Logical Problems

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: gnLZWOubWa
- Authors: Naïm Es-sebbani; Esteban Marquer; Yakoub Salhi; Zied Bouraoui
- Primary area: general_machine_learning->evaluation
- Keywords: LLM-based reasoning models;parameterized 2-CNF formulas;evaluation;reasoning
- Source URL: https://openreview.net/forum?id=gnLZWOubWa
- PDF URL: https://openreview.net/pdf?id=gnLZWOubWa

## Abstract

Logic provides a controlled testbed for evaluating LLM-based reasoners, yet standard SAT-style benchmarks often conflate surface difficulty (length, wording, clause order) with the structural phenomena that actually determine satisfiability. We introduce a diagnostic benchmark for 2-SAT built from parameterized families of structured 2-CNF formulas, where satisfiability is characterized by the implication graph and can be tuned along interpretable axes. Our generators isolate distinct competencies and failure modes: (i) contradiction-cycle UNSAT cores with controllable size and imbalance, (ii) SAT instances with a prescribed fraction of free variables to control solution multiplicity, (iii) planted backbones that modulate propagation, (iv) late bridge clauses that couple otherwise monotone regions to probe sensitivity to ordering and revision, and (v) symmetry/duplication variants that test abstraction under renaming and redundant structure. We evaluate LLM-based reasoners on decision accuracy and assignment validity, and quantify robustness under semantics-preserving perturbations such as clause reordering, filler clauses, and variable renaming. Across models, we observe sharp performance transitions under targeted structural interventions even when surface statistics are held fixed, revealing brittleness regimes that are invisible to aggregate SAT accuracy.

## One-Sentence Claim

Parameterized 2-SAT families expose reasoning-model brittleness by isolating logical structure from superficial prompt statistics.

## Problem

Logic benchmarks are useful for evaluating reasoning models, but standard SAT-style tasks can conflate structural difficulty with length, wording, clause order, and other surface features. Aggregate accuracy can hide sharp failures under specific logical phenomena.

The paper asks how to build a diagnostic benchmark where satisfiability structure is controlled and perturbations preserve semantics.

## Core Contribution

The contribution is a 2-SAT diagnostic benchmark built from parameterized families of structured 2-CNF formulas. Each generator isolates a specific competence or failure mode: contradiction-cycle UNSAT cores, SAT solution multiplicity, planted backbones, late bridge clauses, and symmetry/duplication variants.

The benchmark evaluates both decision accuracy and assignment validity, then tests robustness under clause reordering, filler clauses, and variable renaming.

## Method

Because 2-SAT satisfiability is characterized by implication graphs, the benchmark controls graph-level phenomena directly. Formula generators tune interpretable axes such as UNSAT core size, free-variable fraction, propagation backbone, bridge clauses, and redundant symmetric structure.

Models are then evaluated under semantics-preserving perturbations to distinguish actual logical abstraction from brittle surface matching.

## Experiments and Evidence

Evidence reported in the abstract:

- Structured parameterized 2-CNF formula families.
- Evaluation of decision accuracy and assignment validity.
- Robustness tests under clause reordering, filler clauses, and variable renaming.
- Sharp performance transitions under targeted structural interventions.
- Brittleness regimes invisible to aggregate SAT accuracy.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: model set, generator parameters, prompt format, and exact robustness metrics.

## Limits and Failure Modes

- 2-SAT is controlled and interpretable but narrower than natural-language reasoning.
- Prompting choices can influence whether models express valid assignments.
- Structural brittleness on formulas may not map directly to real-world tasks.
- The benchmark diagnoses failures but does not by itself explain internal mechanisms.

## Deep Themes

**Evaluation should control causal difficulty variables.** The benchmark changes graph structure while holding surface statistics stable.

**Robustness is structural, not aggregate.** Models can look strong on average while failing sharply at specific logical transitions.

**Semantics-preserving perturbations reveal abstraction.** Renaming, reordering, and redundancy test whether models reason over meaning.

## Subthemes

- Parameterized 2-SAT evaluation.
- Implication-graph difficulty.
- Assignment validity.
- Semantic perturbation robustness.
- Logical brittleness transitions.

## Connections to Other Papers

Connects to Finite Test Certification, MADQA, Weak-Strong Verification, VenusBench-Mobile, and Anytime Trees. All push evaluation toward controlled diagnostics rather than one-dimensional scores.

## Notes for Cross-Paper Synthesis

This paper strengthens the evaluation theme: robust reasoning benchmarks need knobs tied to the actual latent structure of the task, not just larger collections of examples.
