# Ranking Time Series using a Time Warping Ideal Point Model

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 5wMBxVaTbC
- Authors: Lucas Zoroddu; Pierre Humbert; Laurent Oudre
- Primary area: applications->time_series
- Keywords: Ranking;Pairwise Comparisons;Ideal Point Model;Time Series;DTW;TWED
- Source URL: https://openreview.net/forum?id=5wMBxVaTbC
- PDF URL: https://openreview.net/pdf?id=5wMBxVaTbC

## Abstract

Expert-annotated time series datasets often suffer from low agreement, especially in medical applications where decisions rely on subjective criteria and inconsistent thresholds. Such variability degrades annotation quality and thus limits the reliability of supervised classification models. To address this, we propose to rely on a pairwise comparison-based approach, which provides a more robust alternative to individual annotation, since relative judgments are typically easier and yield higher consistency.
The problem is thus transformed into a ranking problem and we introduce an ideal point model adapted to time series data using elastic similarity measures such as Dynamic Time Warping (DTW) and Time Warp Edit Distance (TWED).
We prove Lipschitz continuity of these distances and demonstrate several convergence guarantees for this model. To facilitate gradient-based optimization, we also introduce a differentiable version of the TWED. Finally, we show through multiple experiments that our approach produces accurate and robust rankings under noisy annotation conditions.

## One-Sentence Claim

Pairwise comparison ranking with time-warping distances can produce robust time-series orderings under noisy, subjective annotations.

## Problem

Expert labels for time-series datasets, especially in medical settings, can have low agreement because annotators use subjective criteria and inconsistent thresholds, weakening supervised classifiers trained on individual labels.

## Core Contribution

The paper adapts ideal point modeling to time-series ranking using elastic similarity measures such as DTW and TWED, and introduces differentiable TWED for gradient-based optimization.

## Method

It transforms annotation into a pairwise comparison/ranking problem. Time series are compared to latent ideal points through time-warping distances, with Lipschitz and convergence guarantees supporting optimization and robustness.

## Experiments and Evidence

The abstract reports multiple experiments showing accurate and robust rankings under noisy annotation conditions.

## Limits and Failure Modes

No confident local PDF/arXiv match yet, so details still need checking: task domains, annotation protocols, exact ideal-point likelihood, differentiable TWED formulation, scaling to long series, and comparison against classification/regression baselines.

## Deep Themes

- Relative judgments can be more reliable than absolute labels.
- Annotation noise should reshape the learning problem, not only be averaged away.
- Time-series models need similarity measures that respect temporal warping.

## Subthemes

- Time-series ranking.
- Pairwise comparisons.
- Ideal point models.
- Dynamic Time Warping.
- Time Warp Edit Distance.
- Noisy medical annotation.

## Connections to Other Papers

Connects to evaluation and measurement papers, especially those replacing brittle absolute labels with richer judgment protocols. It also links to robust contextual optimization through decision-making under imperfect observed data.

## Notes for Cross-Paper Synthesis

This paper adds a measurement-design theme: when labels are subjective, reformulating annotation as pairwise ranking may produce more reliable supervision than forcing absolute categories.
