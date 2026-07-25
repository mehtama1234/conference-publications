# Prescriptive Scaling Reveals the Evolution of Language Model Capabilities

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: IkjsHRpuYY
- Authors: Hanlin Zhang; Jikai Jin; Vasilis Syrgkanis; Sham M. Kakade
- Primary area: general_machine_learning->evaluation
- Keywords: Scaling Laws;Observational Studies;Evaluation;Validity
- Source URL: https://openreview.net/forum?id=IkjsHRpuYY
- PDF URL: https://openreview.net/pdf?id=IkjsHRpuYY

## Abstract

Machine learning model performance arises from competition and application. For deployment, we consider the prescriptive scaling laws: given a pre-training compute budget, what downstream accuracy is attainable with contemporary post-training practice, and how stable is that mapping as the field evolves? Using large-scale observational evaluations with 5k observational and 2k newly sampled data on model performance, we estimate capability boundaries—high conditional quantiles of benchmark scores as a function of log pre-training FLOPs, via smoothed quantile regression with a monotone, saturating sigmoid parameterization. We validate the temporal reliability by fitting on earlier model generations and evaluating on later releases. Across various tasks, the estimated boundaries are mostly stable, with the exception of math reasoning that exhibits a consistently advancing boundary over time. We then extend our approach to analyze task-dependent saturation and to probe contamination-related shifts on math reasoning tasks. Finally, we introduce an efficient algorithm that recovers near-full-data frontiers using roughly 20% of evaluation budget. Together, our work releases the Proteus-2k, the latest model performance evaluation dataset, and introduces a practical methodology for translating compute budgets into reliable performance expectations and for monitoring when capability boundaries move.

## One-Sentence Claim

Prescriptive scaling laws estimate attainable downstream accuracy from pretraining compute under contemporary post-training practice and track when capability boundaries shift over time.

## Problem

Traditional scaling views do not directly answer deployment questions about what performance to expect from a compute budget after current post-training, nor whether that mapping remains stable as the field changes.

## Core Contribution

The paper introduces a methodology for estimating high-quantile capability frontiers with smoothed monotone saturating quantile regression, validates temporal reliability, releases Proteus-2k, and proposes a lower-budget frontier-estimation algorithm.

## Method

Using 5k observational and 2k newly sampled model-performance data points, the authors fit conditional benchmark-score quantiles as functions of log pretraining FLOPs, test fits from earlier model generations on later releases, analyze task saturation and contamination shifts, and recover near-full-data frontiers with about 20% of evaluation budget.

## Experiments and Evidence

The abstract reports mostly stable capability boundaries across tasks, except math reasoning where the boundary consistently advances, plus efficient frontier recovery using roughly one fifth of the evaluation data.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: model/sample coverage, benchmark selection, post-training heterogeneity, contamination probes, confidence intervals, and how "contemporary practice" is operationalized.

## Deep Themes

- Evaluation as frontier estimation rather than leaderboard point comparison.
- Compute-to-capability mappings are empirical objects that can drift.
- Math reasoning appears unusually sensitive to advancing post-training practice.

## Subthemes

- Scaling laws.
- Observational evaluation.
- Quantile regression.
- Capability boundaries.
- Benchmark saturation.
- Contamination shifts.

## Connections to Other Papers

Connects to evaluation and benchmark papers, especially those tracking reasoning, contamination, and capability shifts. It also complements test-time and post-training papers by asking how those practices change expected performance at a given compute scale.

## Notes for Cross-Paper Synthesis

This paper gives the corpus a meta-evaluation lens: capability should be measured as a moving frontier conditioned on compute, post-training practice, task domain, and time.
