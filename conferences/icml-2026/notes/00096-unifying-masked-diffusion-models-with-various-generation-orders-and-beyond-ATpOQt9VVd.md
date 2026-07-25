# Unifying Masked Diffusion Models with Various Generation Orders and Beyond

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: ATpOQt9VVd
- Authors: Chunsan Hong; Sanghyun Lee; Jong Chul Ye
- Primary area: deep_learning->generative_models_and_autoencoders
- Keywords: diffusion language models;diffusion models;masked diffusion models
- Source URL: https://openreview.net/forum?id=ATpOQt9VVd
- PDF URL: https://openreview.net/pdf?id=ATpOQt9VVd

## Abstract

Masked diffusion models (MDMs) are a potential alternative to autoregressive models (ARMs) for language generation, but generation quality depends critically on the generation order. Prior work either hard-codes an ordering (e.g., blockwise left-to-right) or learns an ordering policy for a pretrained MDM, which incurs extra cost and can yield suboptimal solutions due to the two-stage optimization. Motivated by this, we propose order-expressive masked diffusion model (OeMDM) for a broad class of diffusion generative processes with various generation orders, enabling the interpretation of MDM, ARM, and block diffusion in a single framework. Furthermore, building on OeMDM, we introduce learnable-order masked diffusion model (LoMDM), which jointly learns the generation ordering and diffusion backbone through a single objective from scratch, enabling the diffusion model to generate text in context-dependent ordering. Empirically, we confirm that LoMDM outperforms various discrete diffusion models across multiple language modeling benchmarks.

## One-Sentence Claim

OeMDM unifies masked diffusion, autoregressive, and block diffusion generation orders, while LoMDM jointly learns context-dependent generation order and diffusion backbone.

## Problem

Masked diffusion language models depend heavily on generation order, but prior methods either hard-code orders or learn ordering policies in a separate stage after pretraining.

## Core Contribution

The paper proposes order-expressive masked diffusion models as a unified framework for multiple generation orders, then introduces learnable-order masked diffusion models trained from scratch with one objective.

## Method

OeMDM defines a broad class of diffusion generative processes parameterized by generation order, making MDMs, ARMs, and block diffusion interpretable in one framework. LoMDM learns both ordering and model parameters jointly, allowing context-dependent token generation order.

## Experiments and Evidence

The abstract reports that LoMDM outperforms multiple discrete diffusion models across language modeling benchmarks.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition is deferred after repeated rate-limit failures. Details still need checking: ordering parameterization, training stability, benchmark suite, inference cost, and comparison to strong autoregressive baselines.

## Deep Themes

- Generation order is a learnable modeling choice, not merely a decoding convention.
- Diffusion and autoregressive language models can be unified by process structure.
- Context-dependent ordering may be a capability lever for non-AR generation.

## Subthemes

- Masked diffusion language models.
- Generation order.
- Discrete diffusion.
- Autoregressive unification.
- Learnable ordering.
- Text generation.

## Connections to Other Papers

Connects to Flex-Forcing, diffusion solver papers, and generative-model unification work through the idea that generation process design controls capability.

## Notes for Cross-Paper Synthesis

This paper adds a generation-process theme: the order in which a model generates tokens is part of the learned system, not a fixed wrapper around it.
