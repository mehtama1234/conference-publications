# Toward Stable Value Alignment: Introducing Independent Modules for Consistent Value Guidance

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: R80JLmXXPJ
- Authors: Wenhao Chen; Sirui Sun; Shengyuan Bai; Guojie Song
- Primary area: social_aspects->alignment
- Keywords: Large Language Models;AI Alignment;Inference-time Steering
- Source URL: https://openreview.net/forum?id=R80JLmXXPJ
- PDF URL: https://openreview.net/pdf?id=R80JLmXXPJ

## Abstract

Aligning large language models (LLMs) with human values typically relies on post-training or inference-time steering that directly manipulates the backbone’s parameters or representation space. However, a critical gap exists: the model’s residual stream is highly dynamic, in which values exist as fragile, low-dimensional properties, inherently incompatible with  the stability required for consistent value expression. In this paper, we propose the Stable Value Guidance Transformer (SVGT), which addresses this gap through an independent value module incorporating two key designs: (1) *independent value modeling*, maintaining normative representations in a dedicated value space isolated from the backbone, and (2) *explicit behavioral guidance*, transducing these stable signals into learnable latent Bridge Tokens. These tokens serve as dynamic value anchors to explicitly steer the generative trajectory, ensuring robust adherence across diverse contexts without disrupting the backbone’s internal representations. Experiments across multiple backbones and safety benchmarks show that SVGT generally reduces harmful scores by over 70\% while maintaining generation fluency, demonstrating the efficacy of architecturally grounded value modeling.

## One-Sentence Claim

SVGT stabilizes LLM value alignment by modeling normative representations in an independent module and steering generation through bridge tokens rather than directly perturbing the backbone.

## Problem

Post-training and inference-time steering often manipulate the backbone residual stream, but values are fragile low-dimensional properties in a dynamic representation space, making consistent value expression unstable.

## Core Contribution

The paper proposes an independent value module plus explicit behavioral guidance through learnable latent Bridge Tokens that anchor generation without disrupting backbone internals.

## Method

SVGT stores value representations in a dedicated value space isolated from the backbone, then transduces stable value signals into bridge tokens that dynamically steer the generative trajectory across contexts.

## Experiments and Evidence

The abstract reports experiments across multiple backbones and safety benchmarks where SVGT generally reduces harmful scores by more than 70% while maintaining fluency.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: value-module training data, benchmark set, bridge-token insertion strategy, over-refusal, robustness to jailbreaks, and effects on helpfulness in ambiguous contexts.

## Deep Themes

- Value representations may need architectural separation from task representations.
- Inference-time steering can use stable external anchors instead of residual-stream manipulation.
- Alignment should preserve backbone capabilities while guiding behavior.

## Subthemes

- AI alignment.
- Inference-time steering.
- Independent value modules.
- Bridge Tokens.
- Harmful-score reduction.
- Stable normative representations.

## Connections to Other Papers

Connects to Buffer-and-Reinforce, Robust Harmful Features, RLVepsR, and causal route gating through internal safety control and steering.

## Notes for Cross-Paper Synthesis

SVGT adds an architectural isolation theme: values may be more stable when represented in a dedicated module and injected through explicit anchors rather than entangled in the residual stream.
