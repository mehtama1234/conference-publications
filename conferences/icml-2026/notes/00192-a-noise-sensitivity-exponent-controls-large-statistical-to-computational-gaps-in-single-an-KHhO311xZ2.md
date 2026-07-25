# A Noise Sensitivity Exponent Controls Large Statistical-to-Computational Gaps in Single- and Multi-Index Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: KHhO311xZ2
- Authors: Leonardo Defilippis; Florent Krzakala; Bruno Loureiro; Antoine Maillard
- Primary area: theory
- Keywords: Multi-index models;Approximate Message Passing;Statistical to Computational gaps;teacher student models
- Source URL: https://openreview.net/forum?id=KHhO311xZ2
- PDF URL: https://openreview.net/pdf?id=KHhO311xZ2

## Abstract

Understanding when learning is statistically possible yet computationally hard is a central challenge in high-dimensional statistics.
In this work, we investigate this question in the context of single- and multi-index models, classes of functions widely studied as benchmarks to probe the ability of machine learning methods to discover features in high-dimensional data. 
Our main contribution is to show that a Noise Sensitivity Exponent (NSE)—a simple quantity determined by the activation function—governs the existence and magnitude of statistical-to-computational gaps within a broad regime of these models.
We first establish that, in single-index models with large additive noise, the onset of a computational bottleneck is fully characterized by the NSE. We then demonstrate that the same exponent controls a statistical-computational gap in the specialization transition of large separable multi-index models, where individual components become learnable. Taken together, our results identify the NSE as a unifying property linking noise robustness, computational hardness, and feature specialization in high-dimensional learning.

## One-Sentence Claim

A Noise Sensitivity Exponent determined by the activation function governs statistical-to-computational gaps and feature-specialization transitions in single- and multi-index models.

## Problem

High-dimensional learning can be statistically possible but computationally hard, and the field needs simple quantities that predict when those gaps appear in feature-learning models.

## Core Contribution

The paper identifies NSE as a unifying property connecting noise robustness, computational bottlenecks, and specialization transitions across broad regimes of single- and multi-index models.

## Method

The authors analyze single-index models with large additive noise and separable multi-index models, showing that activation-driven noise sensitivity controls both computational hardness onset and component learnability.

## Experiments and Evidence

The abstract is theoretical. It reports characterization of computational bottlenecks in noisy single-index models and statistical-computational gaps in specialization transitions of large separable multi-index models.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: precise NSE definition, assumptions on activations and noise, algorithmic model, AMP connection, finite-size behavior, and relevance to practical neural architectures.

## Deep Themes

- Simple function-level properties can control high-dimensional learnability.
- Noise robustness and computational hardness are linked.
- Feature specialization has phase-transition structure.

## Subthemes

- Single-index models.
- Multi-index models.
- Statistical-computational gaps.
- Approximate Message Passing.
- Teacher-student learning.
- Activation functions.

## Connections to Other Papers

Connects to theory papers on representation limits, neural algorithm learning, and power-law compositional reasoning through formal explanations of when learning becomes feasible.

## Notes for Cross-Paper Synthesis

This paper adds a phase-transition perspective to the corpus: capability may depend sharply on latent exponents or structural quantities that are invisible in high-level benchmark descriptions.
