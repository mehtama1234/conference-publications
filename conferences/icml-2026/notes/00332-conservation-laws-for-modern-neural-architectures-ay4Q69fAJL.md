# Conservation Laws for Modern Neural Architectures

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: ay4Q69fAJL
- Authors: Viet-Hoang Tran; Vinh Khanh Bui; Tan Lai Ngoc; Nam Nguyen; Tuan Quang Dam; Tan Minh Nguyen
- Primary area: theory->deep_learning
- Keywords: conservation laws;multihead attention;mixture of experts
- Source URL: https://openreview.net/forum?id=ay4Q69fAJL
- PDF URL: https://openreview.net/pdf?id=ay4Q69fAJL

## Abstract

Understanding gradient descent dynamics is key to explaining the success of over-parameterized models, where implicit bias manifests through conservation laws in gradient flow. While such laws are well understood for linear and ReLU networks, they remain largely unexplored for modern architectures. This work develops a unified framework to characterize conservation laws for contemporary models, including feedforward networks with GELU, SiLU, and SwiGLU activations, multihead attention with sinusoidal and rotary positional encodings, and Mixture-of-Experts architectures under diverse gating designs. Our theoretical findings are supported by experiments that validate the predicted invariants.

## One-Sentence Claim

Modern architectures such as GELU/SwiGLU networks, attention with positional encodings, and MoE models exhibit gradient-flow conservation laws that characterize implicit bias.

## Problem

Conservation laws in gradient flow help explain implicit bias in overparameterized linear and ReLU networks. But modern neural architectures use smooth activations, gated blocks, attention, positional encodings, and mixture-of-experts designs where analogous invariants are less understood.

The paper asks for a unified framework that characterizes conservation laws across contemporary architectures.

## Core Contribution

The paper develops a unified theoretical framework for conservation laws in modern models. It covers feedforward networks with GELU, SiLU, and SwiGLU activations; multihead attention with sinusoidal and rotary positional encodings; and mixture-of-experts architectures under different gating designs.

Experiments validate the predicted invariants.

## Method

The method analyzes gradient-flow dynamics and identifies quantities preserved during continuous-time training. It extends implicit-bias conservation-law analysis beyond homogeneous ReLU-style settings to modern nonlinearities and architectural modules.

For attention and MoE, the framework accounts for positional encodings and gating designs as part of the invariant structure.

## Experiments and Evidence

Evidence reported in the abstract:

- Unified framework for conservation laws in modern architectures.
- Coverage of GELU, SiLU, and SwiGLU feedforward networks.
- Coverage of multihead attention with sinusoidal and rotary positional encodings.
- Coverage of MoE with diverse gating designs.
- Experimental validation of predicted invariants.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: exact invariants, gradient-flow assumptions, finite-step optimizer behavior, and experimental architectures.

## Limits and Failure Modes

- Gradient-flow conservation laws may be altered by discrete optimizers, weight decay, normalization, or adaptive methods.
- Invariants do not automatically explain generalization.
- MoE routing and gating discontinuities may require idealized assumptions.
- Empirical validation of invariants may be simpler than frontier-scale training dynamics.

## Deep Themes

**Implicit bias is encoded in training invariants.** Conservation laws reveal what gradient flow cannot change.

**Modern architecture details matter theoretically.** Activations, positional encodings, and gates change the invariant structure.

**Theory is catching up to actual LLM components.** The paper moves beyond toy ReLU networks toward attention and MoE.

## Subthemes

- Gradient-flow conservation laws.
- GELU/SiLU/SwiGLU implicit bias.
- Attention positional-encoding invariants.
- MoE gating conservation.
- Modern architecture theory.

## Connections to Other Papers

Connects to Context-Parameter Equivalence, Diffract, Neural Ricci Flow, and optimization-trajectory papers. It also links to OENN/CENN and symmetry papers because invariants reflect structural constraints on learning dynamics.

## Notes for Cross-Paper Synthesis

This paper strengthens the dynamics-theory theme: to understand modern models, track what training preserves as carefully as what it optimizes.
