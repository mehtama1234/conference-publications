# Controlled LLM Training on Spectral Sphere

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 5kTn1c3vtt
- Authors: Tian Xie; Haoming Luo; Haoyu Tang; Hu Yiwen; Jason Klein Liu; Qingnan Ren; Yang Wang; Xin Zhao; Rui Yan; Bing Su; Chong Luo; Baining Guo
- Primary area: deep_learning->algorithms
- Keywords: LLM pretrain;spectral norm;steepest descent;scaling law
- Source URL: https://openreview.net/forum?id=5kTn1c3vtt
- PDF URL: https://openreview.net/pdf?id=5kTn1c3vtt

## Abstract

Scaling large models requires optimization strategies that ensure rapid convergence grounded in stability. Maximal Update Parametrization ($\boldsymbol{\mu}$P) provides a theoretical safeguard for width-invariant $\Theta(1)$ activation control, whereas emerging optimizers like Muon are only "half-aligned" with these constraints: they control updates but allow weights to drift. To address this limitation, we introduce the **Spectral Sphere Optimizer (SSO)**, which enforces strict module-wise spectral constraints on both weights and their updates. By deriving the steepest descent direction on the spectral sphere, SSO realizes a fully $\boldsymbol{\mu}$P-aligned optimization process. To enable large‑scale training, we implement SSO as an efficient parallel algorithm within Megatron. Through extensive pretraining on diverse architectures, including Dense 1.7B, MoE 8B-A1B, and 200-layer DeepNet models, SSO consistently outperforms AdamW and Muon. Furthermore, we observe significant practical stability benefits, including improved MoE router load balancing, suppressed outliers, and strictly bounded activations.

## One-Sentence Claim

Spectral Sphere Optimizer stabilizes large-scale LLM training by constraining both weights and updates on module-wise spectral spheres, aligning steepest descent with muP-style activation control.

## Problem

LLM pretraining needs fast optimization without activation drift, outliers, or instability. Muon controls update directions under the spectral norm but leaves forward weights unconstrained, making it only partially aligned with muP stability constraints.

## Core Contribution

The paper derives steepest descent on the spectral sphere, implements SSO efficiently in Megatron, and shows improved convergence and stability across dense, MoE, and very deep LLM architectures.

## Method

SSO enforces module-wise spectral constraints on both weights and updates. It projects updates into the tangent geometry of a spectral sphere and retracts weights back to the constrained manifold, with practical spectral scaling and parallel implementation details.

## Experiments and Evidence

The abstract reports pretraining gains over AdamW and Muon on Dense 1.7B, MoE 8B-A1B, and 200-layer DeepNet settings, with improved MoE router load balancing, suppressed outliers, and bounded activations.

## Full-Text Upgrade

The full text frames SSO as resolving a gap between convergence speed and muP-style stability. Muon is interpreted as steepest descent under the spectral norm for updates, but since it does not constrain weights, activations can drift. SSO identifies the spectral sphere as the geometry where both update and weight scales are controlled.

Implementation details matter: the paper includes Megatron-LM integration, spectral norm estimation, retraction to the spectral sphere, and parallelization strategies. In Dense 1.7B training, SSO reaches AdamW's validation loss in fewer steps; in MoE 8B-A1B, it improves router load balance; in 200-layer DeepNet stress tests, it suppresses instability and outliers relative to baselines.

## Limits and Failure Modes

Limits to watch: spectral norm estimation/projection adds system complexity; implementation precision affects update quality; some parameters or architecture components may remain outside full manifold constraints; and benefits need continued validation at larger frontier scales.

## Deep Themes

- Optimizer geometry is becoming a direct stability control mechanism for LLM pretraining.
- Spectral constraints can unify activation control and fast descent.
- Scaling laws and training stability depend on module-wise norm geometry, not only learning-rate schedules.

## Subthemes

- Spectral norm optimization.
- Spectral Sphere Optimizer.
- muP alignment.
- Muon optimizer.
- MoE load balancing.
- Activation outlier control.

## Connections to Other Papers

Connects to Single-Head Attention spectra, Jacobian spectra, DiReCT, and Alignment-Sensitive Minimax Rates through spectral geometry. It also links to low-precision training and LiftQuant through operational stability under deployment/training constraints.

## Notes for Cross-Paper Synthesis

SSO strengthens the spectral-control theme: spectra are not only explanatory diagnostics but design constraints for optimizers and stable scaling.
