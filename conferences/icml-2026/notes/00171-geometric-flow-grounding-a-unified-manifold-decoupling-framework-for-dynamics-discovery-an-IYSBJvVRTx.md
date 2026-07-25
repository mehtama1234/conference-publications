# Geometric Flow Grounding: A Unified Manifold Decoupling Framework for Dynamics Discovery and Verification

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: IYSBJvVRTx
- Authors: Chang Yu; Yuxuan Luo; Yixuan Du; Yuqing Zhou; Siyuan Li; Jingbo Zhou; jiawei jiang; Zhen Lei; Stan Z. Li
- Primary area: applications->everything_else
- Keywords: Unsupervised Learning;AI for Science;Disentangled Representations
- Source URL: https://openreview.net/forum?id=IYSBJvVRTx
- PDF URL: https://openreview.net/pdf?id=IYSBJvVRTx

## Abstract

Modeling complex dynamics from observational data is fundamental to scientific discovery and artificial intelligence. However, existing approaches are often plagued by the entanglement of static state representations and instantaneous motion, leading to accumulated errors and off-manifold hallucinations where predicted trajectories violate intrinsic geometric constraints. To address this, we propose Geometric Flow Grounding, a unified framework that enforces dynamic evolution strictly along the tangent bundle of the learned data manifold via a differentiable Neural Tangent Projection Layer. By geometrically decoupling state representation from tangential dynamics, our method generalizes across diverse data regimes. In scientific discovery, GFG reduces numerical aliasing and improves long-horizon stability in sparse dynamical systems, while recovering interpretable gene regulatory motifs from single-cell data. For trustworthy AI, the projection residual provides a zero-shot metric for deepfake video detection by revealing inconsistencies with the implicit flow of pre-trained world models. Our results establish manifold-constrained projection as a universal operator for both discovering natural laws and verifying synthetic content. Code will be available at \url{https://github.com/yuchang97/GFG-public}

## One-Sentence Claim

Geometric Flow Grounding constrains learned dynamics to the tangent bundle of the data manifold, improving scientific dynamics discovery and enabling synthetic-content verification.

## Problem

Dynamics models can entangle static state representation with instantaneous motion, causing accumulated trajectory errors and off-manifold hallucinations that violate intrinsic geometric constraints.

## Core Contribution

The paper proposes a unified manifold-decoupling framework with a differentiable Neural Tangent Projection Layer, using projection both for stable dynamics modeling and as a residual signal for verification.

## Method

GFG learns a data manifold and enforces evolution along its tangent bundle, decoupling state from tangential flow. The projection residual measures inconsistency with the implicit flow of pretrained world models and can be used as a zero-shot deepfake detection signal.

## Experiments and Evidence

The abstract reports improved long-horizon stability and reduced numerical aliasing in sparse dynamical systems, recovery of interpretable gene regulatory motifs in single-cell data, and zero-shot deepfake video detection through projection residuals.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: manifold-learning assumptions, tangent projection implementation, benchmark systems, deepfake datasets, world-model dependence, and sensitivity to manifold estimation errors.

## Deep Themes

- Manifold constraints as safeguards against off-support dynamics.
- Scientific discovery and trustworthiness can share geometric operators.
- Residuals from structural constraints become verification signals.

## Subthemes

- AI for science.
- Dynamical systems.
- Tangent bundles.
- Disentangled representations.
- Single-cell gene regulation.
- Deepfake detection.

## Connections to Other Papers

Connects to CoCLD and SDEVI through continuous dynamics, and to FlowGuard/DGS-Net through internal consistency signals for detecting synthetic or unsafe content.

## Notes for Cross-Paper Synthesis

GFG extends the geometry theme into scientific verification: the same manifold constraint can stabilize prediction and reveal when generated content violates learned physical or visual flow.
