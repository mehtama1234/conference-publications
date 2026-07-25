# HypoSpace: A Diagnostic Benchmark for Set-Valued Hypothesis Generation under Underdetermination and Sublinear Coverage Bounds

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: QpjtK65JHO
- Authors: Tingting Chen; Beibei Lin; Zifeng Yuan; Qiran Zou; Hongyu He; Anirudh Goyal; Yew-Soon Ong; Dianbo Liu
- Primary area: probabilistic_methods->monte_carlo_and_sampling_methods
- Keywords: Underdetermination;Set-Value Generation;Hypothesis;Diagnosis for creativity; Scientific discovery;Sublinear Coverage Bounds
- Source URL: https://openreview.net/forum?id=QpjtK65JHO
- PDF URL: https://openreview.net/pdf?id=QpjtK65JHO

## Abstract

Many scientific problems are underdetermined: multiple distinct hypotheses are equally consistent with the same observations. In such settings, effective inference requires not only producing valid explanations, but also systematically exploring and covering the admissible hypothesis set. We introduce HypoSpace, a benchmark that treats large language models (LLMs) as samplers over finite hypothesis spaces and evaluates them on three metrics: Validity, Uniqueness, and Recovery. HypoSpace spans three structured domains (causal graph inference, gravity-constrained 3D voxel reconstruction, and Boolean genetic interaction modeling) with deterministic validators and exactly enumerable solution spaces, plus real-world anchored case studies. Empirically, HypoSpace reveals a capability- and scale-dependent coverage failure: models can maintain high Validity while exhibiting reduced Uniqueness and Recovery as admissible hypothesis spaces become larger or more combinatorial. We further show that the analysis on stratified decoding partially mitigates this collapse, demonstrating HypoSpace's utility as a diagnostic benchmark for set-valued inference. Code is available at: https://github.com/CTT-Pavilion/_HypoSpace.

## One-Sentence Claim

HypoSpace evaluates LLMs as samplers over finite hypothesis spaces, showing they can generate valid hypotheses while failing to cover diverse admissible explanations under underdetermination.

## Problem

Scientific problems often have many valid hypotheses consistent with the same observations, so evaluation must measure coverage of the admissible set rather than a single correct answer.

## Core Contribution

The paper introduces a benchmark with enumerable solution spaces, deterministic validators, and metrics for Validity, Uniqueness, and Recovery across structured scientific domains.

## Method

HypoSpace spans causal graph inference, gravity-constrained 3D voxel reconstruction, and Boolean genetic interaction modeling. It treats LLM outputs as samples and measures whether they are valid, nonduplicate, and recover the full hypothesis set; stratified decoding is analyzed as a partial mitigation.

## Experiments and Evidence

The abstract reports capability- and scale-dependent coverage failure: models maintain high validity but lose uniqueness and recovery as hypothesis spaces become larger or more combinatorial.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: exact domains, validator implementation, model set, decoding strategies, real-world case studies, and whether finite enumerability limits benchmark realism.

## Deep Themes

- Underdetermined science needs set-valued generation and coverage metrics.
- Validity alone can hide mode collapse over hypotheses.
- LLMs can be evaluated as samplers, not only answer predictors.

## Subthemes

- Hypothesis generation.
- Underdetermination.
- Set-valued inference.
- Scientific discovery.
- Coverage bounds.
- Stratified decoding.

## Connections to Other Papers

Connects to Stable-GFN, SRMC, and sampling/diversity papers through coverage of multimodal solution spaces, and to scientific-discovery benchmarks through deterministic validation.

## Notes for Cross-Paper Synthesis

HypoSpace adds a scientific-coverage theme: in underdetermined domains, the failure mode is not invalid answers but repeatedly sampling only a small part of the valid hypothesis space.
