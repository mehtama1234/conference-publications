# The Signal is in the Steps: Local Scoring for Reasoning Data Selection

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: GcB3a6IonG
- Authors: Hoang Anh Just; Myeongseob Ko; Ruoxi Jia
- Primary area: general_machine_learning->everything_else
- Keywords: response selection;reasoning;local steps
- Source URL: https://openreview.net/forum?id=GcB3a6IonG
- PDF URL: https://openreview.net/pdf?id=GcB3a6IonG

## Abstract

Distilling long-form reasoning from teacher models into smaller students requires selecting which candidate solutions to train on. Recent work argues that one should select responses the student model assigns highest probability, i.e., favoring solutions ``natural'' to the student. However, we find that this approach works within a single teacher but fails when scaling to long reasoning traces from multiple diverse teachers. We identify a key cause: this approach scores entire solutions, but students generalize by recombining familiar reasoning steps, not by memorizing complete solutions. Full-trajectory scoring optimizes the wrong target; it rewards global fluency while the transferable signal lies in local step transitions. We propose Local Average Log Probability (LALP), which scores each reasoning step using only a small window of preceding context, measuring whether each step is justified by its immediate premises rather than whether the full response looks natural to the student. LALP enables two practical use cases: selecting the best teacher before fine-tuning and curating training data from diverse teacher pools. Across math, coding, and science reasoning tasks, LALP consistently improves accuracy when selecting the most natural solutions by a large margin.

## One-Sentence Claim

Local Average Log Probability selects reasoning data by scoring local step transitions, which better matches how students recombine reasoning than full-response naturalness.

## Problem

Selecting long reasoning traces by full-solution probability works within one teacher but fails with diverse teachers because students generalize from local steps rather than entire trajectories.

## Core Contribution

The paper identifies full-trajectory scoring as the wrong target for reasoning distillation and proposes LALP for local step-level data selection.

## Method

LALP scores each reasoning step using only a small preceding context window, measuring whether the step follows from immediate premises instead of whether the full response is globally fluent to the student.

## Experiments and Evidence

The abstract reports consistent accuracy gains across math, coding, and science reasoning when selecting teachers or curating data from diverse teacher pools.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: step segmentation, window size, teacher diversity, student model sizes, and failure on globally coherent but locally surprising insights.

## Deep Themes

- Reasoning data quality lives in local transitions, not only final answers.
- Students recombine familiar steps across teachers.
- Data selection should match the granularity of generalization.

## Subthemes

- Reasoning data selection.
- Distillation.
- Local step scoring.
- Teacher selection.
- Math/coding/science reasoning.
- Student naturalness.

## Connections to Other Papers

Connects to RGR-GRPO, DR Tulu, FAC Synthesis, data valuation, and ThreadWeaver through process-level reasoning data curation.

## Notes for Cross-Paper Synthesis

This paper reinforces the process-data theme: for reasoning models, the trainable signal is often in the step transitions rather than whole solutions.
