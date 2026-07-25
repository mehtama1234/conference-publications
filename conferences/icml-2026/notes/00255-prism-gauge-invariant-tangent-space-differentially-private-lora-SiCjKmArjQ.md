# PRISM: Gauge-Invariant Tangent-Space Differentially Private LoRA

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: SiCjKmArjQ
- Authors: Shihao Wang; Xueru Zhang
- Primary area: social_aspects->privacy
- Keywords: differential privacy;LoRA;parameter-efficient fine-tuning;invariance;matrix manifolds
- Source URL: https://openreview.net/forum?id=SiCjKmArjQ
- PDF URL: https://openreview.net/pdf?id=SiCjKmArjQ

## Abstract

Applying differential privacy (DP) via DP-SGD to Low-Rank Adaptation (LoRA) is a natural approach for privacy-preserving fine-tuning. However, LoRA's low-rank parameterization poses a fundamental challenge. In LoRA, each trainable update is represented as a low-rank matrix $Z = AB^\top$, but this factorization is inherently *non-identifiable*: many factor pairs $(A, B)$ represent the same update $Z$. As a result, applying DP-SGD directly to the factors induces *gauge-dependent* perturbations on $Z$, and we show that this naive DP-LoRA can lead to unbounded noise amplification. We propose **PRISM**, an intrinsic DP mechanism for LoRA that is gauge invariant by construction, avoids bilinear noise amplification, and admits an efficient low-dimensional noise sampler. Moreover, PRISM yields a closed-form characterization of the effective intrinsic noise induced on $Z$, enabling stable privacy–utility trade-offs through bounded, gauge-invariant perturbations. We establish standard $(\varepsilon,\delta)$-DP guarantees for PRISM and introduce a DP-aware, gauge-invariant adaptive update rule that prevents adaptive optimization from amplifying injected privacy noise, improving numerical stability in practice.

## One-Sentence Claim

PRISM makes differentially private LoRA gauge-invariant by adding bounded intrinsic tangent-space noise to the low-rank update rather than gauge-dependent factor noise.

## Problem

Naive DP-SGD on LoRA factors is unstable because the factorization Z = AB^T is non-identifiable, so equivalent gauges can induce different and even unbounded noise amplification on the actual update.

## Core Contribution

The paper proposes an intrinsic DP mechanism for LoRA with gauge-invariant perturbations, an efficient low-dimensional noise sampler, closed-form effective-noise characterization, and a DP-aware adaptive update rule.

## Method

PRISM operates on the tangent-space geometry of low-rank matrix updates rather than directly perturbing arbitrary factors, ensuring that privacy noise is bounded and invariant to equivalent LoRA parameterizations.

## Experiments and Evidence

The abstract reports standard epsilon-delta DP guarantees and practical numerical stability improvements through the gauge-invariant adaptive update rule; specific empirical benchmarks are not listed in the visible abstract.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: privacy accounting, utility benchmarks, LoRA ranks, optimizer compatibility, tangent-space computation cost, and scaling to large LLM fine-tuning.

## Deep Themes

- Privacy mechanisms must respect parameterization geometry.
- Non-identifiability can amplify noise and distort utility.
- Tangent-space perturbations give more stable privacy-utility tradeoffs for low-rank adaptation.

## Subthemes

- Differential privacy.
- LoRA.
- Gauge invariance.
- Matrix manifolds.
- Tangent-space noise.
- Parameter-efficient fine-tuning.

## Connections to Other Papers

Connects to IHM, streaming DP lower bounds, GR-LoRA, and SmartFed through privacy/utility under structured low-dimensional adaptation.

## Notes for Cross-Paper Synthesis

PRISM adds a geometry-of-privacy theme: privacy noise should be injected into the identifiable object being learned, not arbitrary coordinates of an equivalent parameterization.
