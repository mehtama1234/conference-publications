# ICML 2026 Spotlight Batch 055 Synthesis

## Scope

This synthesis covers ICML 2026 spotlight notes 271-275:

- SmoothSpike: Spiking Transformer with Learnable Hadamard Transformation
- Stabilizing the Q-Gradient Field for Policy Smoothness in Actor-Critic Methods
- Optimal Decision-Making Based on Prediction Sets
- Orthogonal Concept Erasure for Diffusion Models
- From Pixels to Tokens: A Systematic Study of Latent Action Supervision for Vision-Language-Action Models

Source depth: abstract/metadata only for all five papers. ArXiv acquisition remains deferred after repeated rate-limit/service failures; these papers should be retried later from offset 270.

## Emerging Pattern 1: Geometry-Preserving Transforms Are Practical Control Knobs

SmoothSpike uses fixed or learnable orthogonal transforms to reduce spike-saturation homogenization. OCE uses layer-wise orthogonal transformations to erase diffusion concepts while preserving magnitude and angular geometry.

Both papers use transformations whose invariants match what should be preserved. This is a recurring pattern across PRISM, ENGNN, and RECM: control the representation without corrupting arbitrary coordinate structure.

## Emerging Pattern 2: Downstream Behavior Is Governed by Internal Fields

PAVE argues policy non-smoothness comes from the critic's differential geometry, especially Q-gradient volatility relative to action curvature. SmoothSpike similarly traces language-performance gaps to pre-spike amplitude concentration.

The common move is causal localization: identify the internal field or bottleneck that creates bad output behavior, then regularize that internal source.

## Emerging Pattern 3: Uncertainty Must Be Optimized for Decisions

ROCP turns conformal prediction sets into robust decision objects. It does not stop at coverage; it builds sets that minimize minimax downstream risk under coverage constraints.

This connects to Falling Trees and Bulk-Calibrated Credal Sets. High-stakes systems need uncertainty representations that are directly aligned with the losses decision-makers face.

## Emerging Pattern 4: Safety Editing Is Becoming Fast, Geometric, and Multi-Concept

OCE targets deployment-friendly diffusion safety: closed-form orthogonal edits, preservation of non-target generation, and multi-concept erasure through subspace objectives. It continues a line of concept-erasure papers that are becoming more explicit about representation geometry and interference.

## Emerging Pattern 5: Actions Are Becoming Tokens

Latent Action Supervision shows that directly supervising VLAs with discrete latent action tokens is highly effective, while different latent formulations serve long-horizon reasoning and motor coordination differently.

This links robotics to LatentLM and behavioral-cloning work: non-text modalities and processes are increasingly converted into token-like intermediate languages.

## Cross-Batch Links

- SmoothSpike connects to WBMM, WeDLM, FeatJND, ENGNN, and OCE through efficient geometry-aware representation control.
- PAVE connects to R2VPO, RQE Actor-Critic, RelaxFlow, and Flowers through field-level views of optimization and dynamics.
- ROCP connects to Bulk-Calibrated Credal Sets, Falling Trees, DISCO, and critical-decision evaluation.
- OCE connects to GEM, AdLift, PRISM, SVGT, and safety-editing papers through fast geometry-respecting interventions.
- Latent Action Supervision connects to EcoVLA, LatentLM, Scientific Annotation BC, and DLMR through latent process interfaces.

## Deep Theme Update

Batch 055 is about making internal geometry operational: smooth spike coordinates before discretization, stabilize critic gradient fields before policies oscillate, construct prediction sets around decision loss, rotate diffusion parameters for concept erasure, and tokenize latent actions so heterogeneous robot data can share an interface.
