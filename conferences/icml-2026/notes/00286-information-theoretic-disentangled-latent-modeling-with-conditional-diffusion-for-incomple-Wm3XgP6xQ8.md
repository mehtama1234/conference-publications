# Information-Theoretic Disentangled Latent Modeling with Conditional Diffusion for Incomplete Multi-View Clustering

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: Wm3XgP6xQ8
- Authors: Wenlan Chen; Lu Gao; Daoyuan Wang; Cheng Liang; Fei Guo
- Primary area: general_machine_learning->clustering
- Keywords: Multi-view clustering;Information bottleneck;Conditional diffusion
- Source URL: https://openreview.net/forum?id=Wm3XgP6xQ8
- PDF URL: https://openreview.net/pdf?id=Wm3XgP6xQ8

## Abstract

Incomplete multi-view clustering is challenging due to view missingness and the entanglement of shared semantics with view-specific factors in latent representations. Existing methods often rely on heuristic fusion or direct completion strategies, which suffer from error propagation and unreliable generation under missing views. In this paper, we propose an **I**nformation-guided **D**isentangled latent modeling framework with **C**onditional **D**iffusion for incomplete multi-view clustering (IDCD). Specifically, we first encode each view into a latent representation that is variationally decomposed into a view-wise semantic latent and a view-specific factor. Information-theoretic objectives are introduced to guide the disentanglement of view-wise latents, preserving essential multi-view information while reducing the dependency between semantic and view-specific factors and encouraging cross-view semantic consistency. Besides, we aggregate the semantic latents via a mixture of Wasserstein distributions to obtain a unified global representation, where we impose a Gaussian mixture prior to explicitly couple representation learning with clustering. Based on the learned disentangled latent space, a conditional diffusion model guided by both the global semantic latent and view-specific factors is employed to generate missing views in a consistent manner. Extensive experiments on benchmark datasets demonstrate superior clustering performance and robust missing-view generation compared to state-of-the-art methods.

## One-Sentence Claim

IDCD improves incomplete multi-view clustering by disentangling shared semantic latents from view-specific factors and using conditional diffusion to generate missing views consistently.

## Problem

Incomplete multi-view clustering must cluster samples when some views are missing. Existing fusion or direct-completion methods can entangle shared semantics with view-specific artifacts, causing error propagation and unreliable generation when views are absent.

The paper asks for a latent representation that separates what is common across views from what is view-specific, while still enabling robust missing-view generation and clustering.

## Core Contribution

The paper proposes IDCD, an information-guided disentangled latent modeling framework with conditional diffusion. It decomposes each view into a semantic latent and a view-specific factor, uses information-theoretic objectives to reduce unwanted dependence while preserving multi-view information, aggregates semantic latents with a mixture of Wasserstein distributions, and couples representation learning with clustering through a Gaussian mixture prior.

It then uses conditional diffusion guided by global semantic and view-specific latents to generate missing views.

## Method

IDCD first variationally encodes each view into separated latent components. Information objectives encourage cross-view semantic consistency and disentanglement between semantic and view-specific factors. A mixture of Wasserstein distributions aggregates semantics into a global representation, while a Gaussian mixture prior aligns that representation with cluster structure.

Conditional diffusion fills in missing views using the learned latent factors rather than directly imputing from raw fused features.

## Experiments and Evidence

Evidence reported in the abstract:

- Extensive benchmark experiments.
- Superior clustering performance compared with state-of-the-art methods.
- Robust missing-view generation.
- Information-theoretic disentanglement objectives.
- Explicit clustering coupling via Gaussian mixture prior.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: datasets, missingness patterns, objective terms, diffusion architecture, and clustering metrics.

## Limits and Failure Modes

- Disentanglement objectives may rely on assumptions that are hard to verify.
- Conditional diffusion could hallucinate plausible but cluster-misleading missing views.
- Wasserstein mixture aggregation may add computational cost.
- Performance may depend strongly on whether missingness is random or structured.

## Deep Themes

**Missing data needs semantic-factor separation.** Robust completion requires knowing what is shared across views and what belongs only to one modality.

**Generative completion and clustering are being coupled.** Missing-view generation is not a preprocessing step; it is tied to latent cluster structure.

**Information-theoretic constraints guide representation geometry.** The objective shapes what information is retained, discarded, and aligned.

## Subthemes

- Incomplete multi-view clustering.
- Semantic versus view-specific latent factors.
- Mixture of Wasserstein distributions.
- Gaussian mixture clustering prior.
- Conditional diffusion for missing views.

## Connections to Other Papers

Connects to HAMC, TESS, DLMR, and DISCO through reliable multi-view or multimodal representation under uncertainty. It also links to manifold and geometry papers because aggregation and clustering are explicitly distributional.

## Notes for Cross-Paper Synthesis

IDCD contributes to the theme that missing or noisy modalities should be handled through structured latent decomposition rather than blunt fusion or direct imputation.
