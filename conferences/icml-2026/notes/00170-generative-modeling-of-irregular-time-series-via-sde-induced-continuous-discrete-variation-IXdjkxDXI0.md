# Generative Modeling of Irregular Time Series via SDE-Induced Continuous-Discrete Variational Inference

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: IXdjkxDXI0
- Authors: Zexin Yuan; Qinliang Su; Junxi Xiao
- Primary area: deep_learning->sequential_models_time_series
- Keywords: irregular time series;Neural SDEs;variational inference
- Source URL: https://openreview.net/forum?id=IXdjkxDXI0
- PDF URL: https://openreview.net/pdf?id=IXdjkxDXI0

## Abstract

Irregular time series arise ubiquitously in real-world systems, where observations are sparse, asynchronous, and governed by underlying continuous-time dynamics. Existing continuous–discrete state-space models typically rely on path-based variational inference, which is computationally expensive or constrained by restrictive posterior assumptions. We propose SDEVI, a novel framework that performs variational inference directly on the joint distribution over discrete-time observations, while guaranteeing consistency with an underlying continuous process governed by a Stochastic Differential Equation(SDE). SDEVI employs a variational posterior induced by linear time-varying SDEs as a scalable inference backbone. To enable intricate dynamics modeling for real-world data, we introduce non-linear-SDE-induced variational inference and generalize our framework to the complex domain. Extensive experiments across healthcare, physics, climate, and IoT benchmarks demonstrate state-of-the-art performance on interpolation, extrapolation, regression, and classification tasks.

## One-Sentence Claim

SDEVI performs scalable variational inference for irregular time series by defining posteriors over discrete observations that remain consistent with an underlying continuous SDE process.

## Problem

Continuous-discrete state-space models for sparse asynchronous observations often use path-based variational inference, which can be expensive or limited by restrictive posterior assumptions.

## Core Contribution

The paper proposes SDE-induced variational inference over observation joint distributions, extends it to nonlinear SDE-induced inference, and generalizes the framework to the complex domain.

## Method

SDEVI uses a variational posterior induced by linear time-varying SDEs as a scalable inference backbone, then introduces nonlinear-SDE-induced variational inference for richer dynamics while preserving consistency with continuous-time generative assumptions.

## Experiments and Evidence

The abstract reports state-of-the-art results across healthcare, physics, climate, and IoT benchmarks on interpolation, extrapolation, regression, and classification.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: inference derivation, approximation quality, runtime versus path-based methods, benchmark splits, missingness mechanisms, and complex-domain use cases.

## Deep Themes

- Continuous stochastic dynamics for irregular real-world data.
- Scalable inference through observation-level variational formulations.
- Generative modeling that supports both prediction and reconstruction tasks.

## Subthemes

- Irregular time series.
- Neural SDEs.
- Variational inference.
- Continuous-discrete state-space models.
- Interpolation and extrapolation.
- Healthcare, climate, physics, and IoT.

## Connections to Other Papers

Connects directly to CoCLD through continuous-time irregular-sequence modeling and to Robust Filter Attention through stochastic-process views of sequence representation.

## Notes for Cross-Paper Synthesis

SDEVI deepens the continuous-time theme: sparse sequence data often need latent stochastic process structure, not only denser discrete sequence models.
