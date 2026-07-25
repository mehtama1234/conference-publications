# Manifold-Optimal Guidance: A Unified Riemannian Control View of Diffusion Guidance

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: eSxGdQ0zwG
- Authors: Zexi Jia; Pengcheng Luo; Zhengyao Fang; Jinchao Zhang; Jie Zhou
- Primary area: deep_learning->generative_models_and_autoencoders
- Keywords: Diffusion Models;Riemannian Geometry;Optimal Control;Classifier-Free Guidance
- Source URL: https://openreview.net/forum?id=eSxGdQ0zwG
- PDF URL: https://openreview.net/pdf?id=eSxGdQ0zwG

## Abstract

Classifier-Free Guidance (CFG) serves as the de facto control mechanism for conditional diffusion, yet high guidance scales notoriously induce oversaturation, texture artifacts, and structural collapse. We attribute this failure to a geometric mismatch: standard CFG performs Euclidean extrapolation in ambient space, inadvertently driving sampling trajectories off the high-density data manifold. To resolve this, we present Manifold-Optimal Guidance (MOG), a framework that reformulates guidance as a local optimal control problem. MOG yields a closed-form, geometry-aware Riemannian update that corrects off-manifold drift without requiring retraining. Leveraging this perspective, we further introduce Auto-MOG, a dynamic energy-balancing schedule that adaptively calibrates guidance strength, effectively eliminating the need for manual hyperparameter tuning. Extensive validation demonstrates that MOG yields superior fidelity and alignment compared to baselines, with virtually no added computational overhead.

## One-Sentence Claim

Manifold-Optimal Guidance reframes diffusion guidance as local Riemannian control, reducing off-manifold artifacts from standard classifier-free guidance without retraining.

## Problem

Classifier-free guidance is the standard control mechanism for conditional diffusion, but high guidance scales often produce oversaturation, texture artifacts, and structural collapse. The paper argues that this happens because Euclidean extrapolation in ambient space pushes samples away from the high-density data manifold.

The problem is therefore geometric: control should respect the local data manifold rather than amplify conditional scores in a mismatched coordinate system.

## Core Contribution

The paper introduces Manifold-Optimal Guidance, a framework that formulates guidance as a local optimal-control problem on a Riemannian manifold. It derives a closed-form geometry-aware update that corrects off-manifold drift without retraining.

It also proposes Auto-MOG, a dynamic energy-balancing schedule that adapts guidance strength and reduces manual hyperparameter tuning.

## Method

MOG replaces standard ambient-space extrapolation with a Riemannian update shaped by local manifold geometry. In control terms, guidance becomes an intervention that balances conditional alignment with staying on or near the data manifold.

Auto-MOG dynamically calibrates guidance energy during sampling, aiming to avoid both underguidance and high-scale collapse.

## Experiments and Evidence

Evidence reported in the abstract:

- Improved fidelity and alignment relative to guidance baselines.
- Mitigation of oversaturation, texture artifacts, and structural collapse.
- No retraining requirement.
- Virtually no added computational overhead.
- Automatic guidance-strength scheduling through Auto-MOG.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: manifold estimator, exact Riemannian update, benchmark suite, and overhead measurement.

## Limits and Failure Modes

- The quality of geometry-aware guidance depends on whether the local manifold approximation is reliable.
- Very high-dimensional image manifolds may violate simple local assumptions.
- "Virtually no overhead" needs validation across model sizes and samplers.
- Alignment gains may differ by prompt type, conditioning modality, and guidance scale.

## Deep Themes

**Guidance is geometry.** The paper explains diffusion artifacts as a mismatch between ambient extrapolation and data-manifold structure.

**Inference controls are becoming principled.** MOG offers a control-theoretic and Riemannian explanation for a ubiquitous heuristic.

**Automation targets the brittle knob.** Auto-MOG turns guidance scale from a manual hyperparameter into an adaptive schedule.

## Subthemes

- Riemannian diffusion guidance.
- Local optimal control.
- Off-manifold drift correction.
- Auto-calibrated guidance strength.
- Retraining-free conditional generation.

## Connections to Other Papers

Connects to KPE/KTS, Tilt Matching, PACT, Flow Sampling, Local Diffusion Composition, and Dimension-Free Diffusion Sampling. Together these papers treat sampling-time dynamics as a first-class design object.

## Notes for Cross-Paper Synthesis

MOG reinforces a deep theme across generative-model papers: many failures are trajectory geometry failures, and fixes increasingly modify the path rather than the trained model.
