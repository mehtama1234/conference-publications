# Uncovering the Latent Potential of Deep Intermediate Representations

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 6up1qGJwYZ
- Authors: Arnesh Batra; Arush Gumber; Aniket Khandelwal; Jashn Khemani; Anubha Gupta
- Primary area: general_machine_learning->representation_learning
- Keywords: representation learning;layer selection;linear probes;embedding geometry;transfer learning;deep encoders;foundation models
- Source URL: https://openreview.net/forum?id=6up1qGJwYZ
- PDF URL: https://openreview.net/pdf?id=6up1qGJwYZ

## Abstract

Foundational models pretrained on huge amounts of data learn representations that evolve across depth, forming a hierarchy of embeddings with distinct semantic content and geometric structure. Contrary to the widespread practice of using only the final layer or shallow mixtures, we show that task-relevant information is distributed non-monotonically across layers and cannot be recovered by na\"ive aggregation. Through a geometric and empirical study across multiple modalities, we show that effective transfer depends on identifying which layers encode task-discriminative structure and how their embeddings are geometrically organized. We introduce Layer-wise Optimal Embedding Selection (LOES), a constructive spectral method that identifies task-discriminative subspaces by minimizing residual error under orthogonality and isotropy constraints. To align fine-tuning with this selection principle, we further propose Geometric Regularization (GeoReg), which enforces a simplicial structure on class manifolds and stabilizes representation geometry during fine-tuning. Across a wide range of architectures, depths, modalities, and data regimes, LOES consistently outperforms standard baselines, with gains that grow as model depth increases. Beyond accuracy, our method reveals how semantic factors are distributed across layers, thereby enabling cross-lingual and cross-modal interpretability analyses. Together, our results provide strong evidence that layerwise embedding geometry is not incidental but central to how deep models represent and transfer knowledge.

## One-Sentence Claim

Task-relevant information in foundation-model encoders is distributed non-monotonically across layers, so transfer improves when layerwise embedding geometry is selected and preserved rather than defaulting to the final layer.

## Problem

Transfer learning commonly uses final-layer embeddings or shallow layer mixtures, but deep encoders store different semantic and geometric information at different depths, and naive aggregation can miss task-discriminative structure.

## Core Contribution

The paper introduces Layer-wise Optimal Embedding Selection and Geometric Regularization, showing that layerwise geometry is central to representation transfer across modalities, architectures, and data regimes.

## Method

LOES is a spectral layer-selection method that identifies task-discriminative subspaces under orthogonality and isotropy constraints. GeoReg regularizes fine-tuning to preserve favorable geometric structure, including simplicial class manifolds.

## Experiments and Evidence

The abstract reports consistent improvements over standard baselines across architectures, depths, modalities, and data regimes, with gains increasing as model depth grows, plus interpretability analyses for cross-lingual and cross-modal factors.

## Full-Text Upgrade

The full text makes the mechanism concrete: LOES evaluates layerwise embeddings through residual reduction, redundancy control, and isotropy. It selects a small number of intermediate layers whose embeddings are both discriminative and geometrically well-conditioned, then fits probes or downstream heads on the selected fused representation.

GeoReg is introduced because fine-tuning can collapse the very geometry LOES selects. It penalizes spectral imbalance and encourages class-centroid/simplex structure, stabilizing representation geometry during downstream adaptation. Experiments cover classification, segmentation, and regression across models such as CLIP, ViT-style encoders, ModernBERT, and task-adapted variants; mid-depth layers are often selected, especially for large multimodal pretraining regimes.

## Limits and Failure Modes

Limits to watch: LOES uses calibration data and several geometry hyperparameters; layer-selection benefits may depend on pretraining paradigm and task; and the method analyzes existing representations rather than explaining how to train them to organize depth better from the start.

## Deep Themes

- Intermediate representations are active resources for transfer, not obsolete steps toward the final layer.
- Geometry of embeddings controls downstream accessibility of semantic factors.
- Interpretability and transfer can share the same layerwise selection machinery.

## Subthemes

- Layer selection.
- Intermediate representations.
- Spectral subspace selection.
- Embedding isotropy.
- Geometric regularization.
- Cross-modal interpretability.

## Connections to Other Papers

Connects to Base Models Know How to Reason, visual-symbolic mechanisms, and interpretability-as-intervention papers through internal representation analysis. It also links to effective span dimension and spectral papers through geometry-aware generalization.

## Notes for Cross-Paper Synthesis

This paper strengthens the representation-geometry theme: what a foundation model knows may be distributed across depth, and transfer methods need to recover the right internal layer geometry rather than assume final-layer sufficiency.
