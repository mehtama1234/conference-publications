# Prototype-guided Bilateral Alignment Multimodal Federated Learning

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: aNgkaEagBG
- Authors: Tianchi Liao; Lele Fu; Sheng Huang; Qing Hu; Hong-Ning Dai; Chuan Chen
- Primary area: general_machine_learning
- Keywords: Multimodal federated learning;Gromov Wasserstein Distance
- Source URL: https://openreview.net/forum?id=aNgkaEagBG
- PDF URL: https://openreview.net/pdf?id=aNgkaEagBG

## Abstract

Multimodal federated learning (MFL) has emerged as a pivotal paradigm for leveraging distributed data to enhance model performance. However, existing methods  predominantly rely on idealized assumptions of model homogeneity and balanced modality distributions, rendering them ill-suited for practical scenarios characterized by heterogeneous client architectures and severe modality imbalance. To address these challenges, we propose a \textbf{M}ultimodal \textbf{Fed}erated learning Prototype-guided Bilateral Alignment (MFedPBA) framework. MFedPBA facilitates robust knowledge synergy through a dual alignment mechanism: (i) at the feature level, it aligns heterogeneous feature spaces via a projection encoder optimized by contrastive learning and the Gromov-Wasserstein distance; (ii) at the decision level, it employs an entropy-weighted aggregation of naturally aligned logit prototypes. This novel design achieves robust MFL by jointly tackling heterogeneous feature spaces and collectively aggregating decisions.
Extensive experiments demonstrate that our method significantly outperforms state-of-the-art baselines under conditions of model heterogeneity and modality imbalance.

## One-Sentence Claim

MFedPBA makes multimodal federated learning robust to heterogeneous client models and modality imbalance by aligning feature spaces and aggregating entropy-weighted logit prototypes.

## Problem

Multimodal federated learning should learn from distributed multimodal data without centralizing it, but practical clients often differ in architecture and modality availability. Existing MFL methods commonly assume homogeneous models and balanced modalities, making them brittle in real settings.

The paper asks how to combine knowledge across clients when both feature spaces and modality distributions are heterogeneous.

## Core Contribution

The paper proposes Multimodal Federated learning Prototype-guided Bilateral Alignment, or MFedPBA. It uses dual alignment:

- Feature-level alignment through a projection encoder trained with contrastive learning and Gromov-Wasserstein distance.
- Decision-level alignment through entropy-weighted aggregation of naturally aligned logit prototypes.

This jointly handles heterogeneous feature spaces and collective decision aggregation under modality imbalance.

## Method

MFedPBA maps heterogeneous client features into a shared alignment space using projection encoders. Contrastive learning encourages semantically matching representations, while Gromov-Wasserstein distance aligns relational structure between feature spaces.

At decision level, clients contribute logit prototypes, with entropy weighting favoring more confident/reliable prototypes during aggregation.

## Experiments and Evidence

Evidence reported in the abstract:

- Experiments under model heterogeneity.
- Experiments under severe modality imbalance.
- Significant improvement over state-of-the-art MFL baselines.
- Feature-level contrastive and Gromov-Wasserstein alignment.
- Decision-level entropy-weighted logit prototype aggregation.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: datasets, modality patterns, client architectures, privacy leakage through prototypes, and communication costs.

## Limits and Failure Modes

- Prototype sharing can leak information if not privacy-protected.
- Gromov-Wasserstein alignment may be expensive or unstable for many clients.
- Entropy is an imperfect reliability signal under miscalibration.
- Severe missing modalities may leave too little cross-modal signal to align.

## Deep Themes

**Federated multimodality needs bilateral alignment.** Features and decisions both require coordination under client heterogeneity.

**Relational alignment can bridge architecture mismatch.** Gromov-Wasserstein distance aligns structure rather than coordinates.

**Confidence-weighted prototypes become collaboration currency.** Logit prototypes carry decision knowledge without sharing raw data.

## Subthemes

- Multimodal federated learning.
- Model heterogeneity.
- Modality imbalance.
- Gromov-Wasserstein feature alignment.
- Entropy-weighted logit prototypes.

## Connections to Other Papers

Connects to FedPissa, SmartFed, PRISM, IDCD, and multimodal representation papers. It also links to DIGL and FlashSinkhorn through optimal-transport geometry.

## Notes for Cross-Paper Synthesis

MFedPBA extends the federated adaptation theme from parameter subspaces to multimodal evidence spaces: collaboration requires alignment of both representations and decisions.
