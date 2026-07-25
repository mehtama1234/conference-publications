# SurvDiff: A Diffusion Model for Generating Synthetic Data in Survival Analysis

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: boeY2syj2r
- Authors: Marie Brockschmidt; Maresa Schröder; Stefan Feuerriegel
- Primary area: applications->health_medicine
- Keywords: Survival Analysis;Diffusion Models
- Source URL: https://openreview.net/forum?id=boeY2syj2r
- PDF URL: https://openreview.net/pdf?id=boeY2syj2r

## Abstract

Survival analysis is a cornerstone of clinical research by modeling time-to-event outcomes such as metastasis, disease relapse, or patient death. Unlike standard tabular data, survival data often come with incomplete event information due to dropout, or loss to follow-up. This poses unique challenges for synthetic data generation, where it is crucial for clinical research to faithfully reproduce both the event-time distribution and the censoring mechanism. In this paper, we propose SurvDiff, an end-to-end diffusion model specifically designed for generating synthetic data in survival analysis. SurvDiff is tailored to capture the data-generating mechanism by jointly generating mixed-type covariates, event times, and right-censoring, guided by a survival-tailored loss function. The loss encodes the time-to-event structure and directly optimizes for downstream survival tasks, which ensures that SurvDiff (i) reproduces realistic event-time distributions and (ii) preserves the censoring mechanism. Across multiple datasets, we show that SurvDiff outperforms state-of-the-art generative baselines in both distributional fidelity and survival model evaluation metrics across multiple medical datasets. To the best of our knowledge, SurvDiff is the first end-to-end diffusion model explicitly designed for generating synthetic survival data.

## One-Sentence Claim

SurvDiff is an end-to-end diffusion model for synthetic survival data that jointly generates mixed covariates, event times, and censoring while preserving time-to-event structure.

## Problem

Survival analysis models time-to-event outcomes such as relapse, metastasis, or death, but data often include right-censoring from dropout or loss to follow-up. Synthetic survival data must reproduce both event-time distributions and censoring mechanisms to be useful for clinical research.

Generic tabular generators do not directly encode these survival-specific constraints.

## Core Contribution

The paper introduces SurvDiff, described as the first end-to-end diffusion model explicitly designed for synthetic survival data. It jointly generates mixed-type covariates, event times, and right-censoring.

A survival-tailored loss encodes time-to-event structure and optimizes for downstream survival tasks, helping reproduce event-time distributions and preserve censoring mechanisms.

## Method

SurvDiff adapts diffusion generation to survival records. The model generates covariates, event times, and censoring indicators jointly, while the loss penalizes failures that would distort survival analysis objectives.

The design targets downstream survival-model utility, not only marginal tabular fidelity.

## Experiments and Evidence

Evidence reported in the abstract:

- Multiple medical datasets.
- End-to-end diffusion generation of mixed covariates, event times, and right-censoring.
- Survival-tailored loss.
- Better distributional fidelity than state-of-the-art generative baselines.
- Better survival model evaluation metrics.
- Claimed first end-to-end diffusion model for synthetic survival data.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: datasets, censoring assumptions, privacy evaluation, downstream metrics, and comparison baselines.

## Limits and Failure Modes

- Synthetic clinical data can leak privacy if not explicitly protected.
- Censoring mechanisms may differ across hospitals or studies.
- Downstream utility does not guarantee causal validity.
- Rare event tails may be hard to synthesize accurately.

## Deep Themes

**Domain-specific synthetic data needs task-native losses.** Survival data require event-time and censoring structure.

**Medical data generation must preserve missingness mechanisms.** Censoring is part of the data-generating process, not noise to ignore.

**Diffusion models are specializing into scientific table domains.** The method adapts generative modeling to clinical survival analysis.

## Subthemes

- Synthetic survival data.
- Right-censoring preservation.
- Mixed-type covariate generation.
- Survival-tailored diffusion loss.
- Downstream survival-model utility.

## Connections to Other Papers

Connects to TRECA, ROCP, medical/high-stakes decision papers, and synthetic data governance. It also links to Manifold Perturbations and Flow Sampling through domain-constrained generative modeling.

## Notes for Cross-Paper Synthesis

SurvDiff adds a clinical-data-generation theme: useful synthetic data must preserve the statistical mechanism that downstream methods rely on, including censoring and event timing.
