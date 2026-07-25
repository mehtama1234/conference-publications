# Asymmetric Multi-View Clustering with Hyperbolic Uncertainty Modeling

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: OTKdKRLXf7
- Authors: Yiming Wang; Qun Li; Dongxia Chang; Jie Wen; Hua Dai; Fu Xiao
- Primary area: general_machine_learning->clustering
- Keywords: Multi-view Clustering; Contrastive Learning
- Source URL: https://openreview.net/forum?id=OTKdKRLXf7
- PDF URL: https://openreview.net/pdf?id=OTKdKRLXf7

## Abstract

Deep Multi-View Clustering (MVC) aims to learn a unified semantic representation from diverse data sources without supervision. However, current approaches relying on flat Euclidean embeddings often fail to model data uncertainty, resulting in rigid alignment where high-quality views are forced to drift toward corrupted ones. To address these challenges, we propose the Hyperbolic Asymmetric Multi-view Clustering (HAMC) framework. HAMC maps view-specific features into the Poincaré ball and uses radial geometry as a confidence proxy, encouraging confident representations to occupy larger radial distances while allowing ambiguous or noisy samples to remain closer to the origin. To mitigate noise, we introduce an asymmetric view alignment mechanism, enabling reliable views to unidirectionally guide unreliable ones. Furthermore, a consensus-aware cluster learning strategy is designed to construct robust global pseudo-labels via a confidence-based screening scheme, refining the cluster structure. Extensive experiments against 13 baselines demonstrate that HAMC achieves state-of-the-art performance.

## One-Sentence Claim

HAMC improves multi-view clustering by using hyperbolic radial geometry as an uncertainty proxy and asymmetric alignment so reliable views guide corrupted ones.

## Problem

Deep multi-view clustering methods often use flat Euclidean embeddings and rigid alignment, forcing high-quality views to drift toward noisy or corrupted views.

## Core Contribution

The paper proposes Hyperbolic Asymmetric Multi-view Clustering with confidence-aware Poincare embeddings, unidirectional view alignment, and consensus-based pseudo-label refinement.

## Method

HAMC maps view-specific features into the Poincare ball, assigns confident representations larger radial distances while keeping ambiguous samples near the origin, aligns unreliable views toward reliable ones, and screens pseudo-labels by confidence for robust clustering.

## Experiments and Evidence

The abstract reports state-of-the-art performance against 13 baselines.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: datasets, corruption settings, radial-confidence calibration, sensitivity to hyperbolic curvature, pseudo-label error propagation, and runtime versus Euclidean MVC baselines.

## Deep Themes

- Geometry can encode uncertainty and confidence, not only similarity.
- Asymmetric alignment protects reliable views from noisy ones.
- Robust unsupervised learning depends on view-quality-aware consensus.

## Subthemes

- Multi-view clustering.
- Hyperbolic embeddings.
- Poincare ball.
- Contrastive learning.
- Confidence screening.
- Asymmetric view alignment.

## Connections to Other Papers

Connects to FlatLand and Riemannian metric matching through non-Euclidean geometry, and to multimodal decomposition papers that avoid forcing all sources into a symmetric alignment.

## Notes for Cross-Paper Synthesis

HAMC adds an uncertainty-aware geometry theme: representation location on a manifold can encode confidence and regulate how information flows across views.
