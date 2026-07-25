# SVD as a Fast Interpretability Method for Transformers

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 7tt8TwMjdJ
- Authors: Min Xue; Artur Andrzejak
- Primary area: social_aspects->accountability_transparency_and_interpretability
- Keywords: interpretability;transformers;mechanistic interpretability;representation learning
- Source URL: https://openreview.net/forum?id=7tt8TwMjdJ
- PDF URL: https://openreview.net/pdf?id=7tt8TwMjdJ

## Abstract

Mechanistic interpretability of Transformer models commonly relies on training auxiliary proxy models, such as Sparse Autoencoders or Cross-Layer Transcoders. While effective, these post-hoc approaches introduce approximation bias and incur substantial computational overhead. We propose an alternative, training-free interpretability framework that directly exploits the Singular Value Decomposition (SVD) of weight matrices in Transformer MLP sublayers. By operating natively on model parameters, our method improves scalability while preserving fidelity to the original weights. We show that the projection matrices of MLP sublayers admit a natural decomposition into orthogonal, interpretable rank-1 subspaces, which we term **Detector-Effector Units** (DEUs). Within each unit, a singular vector functions as a detector of input patterns and modulates a coupled effector vector that encodes output semantics. Building on this structure, we introduce **Subspace Contribution Analysis** (SCA), a diagnostic method that quantifies the direct causal contribution of individual native subspaces to model predictions. Experiments across the GPT-2 family demonstrate that our framework, **Native Network Anatomy** (NaNA), identifies dominant functional pathways with orders-of-magnitude efficiency gains over training-based interpretability baselines, while maintaining weight fidelity. Our results suggest that SVD-based analyses provide a scalable and faithful alternative to learned proxy approaches for mechanistic interpretability.

## One-Sentence Claim

SVD of Transformer MLP weights can provide fast, training-free mechanistic interpretability by decomposing native parameters into detector-effector rank-1 units.

## Problem

Mechanistic interpretability often relies on learned proxy models such as sparse autoencoders or cross-layer transcoders, which add compute cost and approximation bias.

## Core Contribution

The paper proposes Native Network Anatomy, an SVD-based framework for interpreting Transformer MLP sublayers directly from model weights, including Detector-Effector Units and Subspace Contribution Analysis.

## Method

It decomposes MLP projection matrices into orthogonal rank-1 subspaces. Within each DEU, a singular vector acts as an input-pattern detector and a coupled vector acts as an output-semantic effector; SCA estimates the causal contribution of these native subspaces to predictions.

## Experiments and Evidence

The abstract reports experiments across the GPT-2 family showing dominant functional pathways with orders-of-magnitude efficiency gains over training-based interpretability baselines while preserving weight fidelity.

## Limits and Failure Modes

No confident local PDF/arXiv match yet, so details still need checking: how DEUs are labeled, causal-intervention protocol, comparison baselines, and whether MLP SVD captures polysemantic or attention-mediated circuits.

## Deep Themes

- Interpretability can use native weight structure rather than learned proxies.
- Linear algebra decompositions may offer scalable mechanistic entry points.
- Fidelity and computational cost are becoming central interpretability criteria.

## Subthemes

- Mechanistic interpretability.
- Singular value decomposition.
- Transformer MLPs.
- Detector-Effector Units.
- Subspace Contribution Analysis.
- Training-free analysis.

## Connections to Other Papers

Connects to Base Models Know How to Reason, visual-symbolic mechanisms, and LOES through internal representation/weight geometry. It also links to spectral papers through SVD as an explanatory tool.

## Notes for Cross-Paper Synthesis

This paper adds a native-geometry interpretability theme: instead of training external explanatory models, one can sometimes read functional structure directly from model matrices.
