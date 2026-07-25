# Eigenvectors of Experts are Training-free Non-collapsing Routers

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: H1mxs9qGQX
- Authors: Giang Do; Hung Le; Truyen Tran
- Primary area: deep_learning->everything_else
- Keywords: Sparse Mixture of Experts;Eigenvectors;Training-free;Non-collapsing router
- Source URL: https://openreview.net/forum?id=H1mxs9qGQX
- PDF URL: https://openreview.net/pdf?id=H1mxs9qGQX

## Abstract

Sparse Mixture of Experts (SMoE) architectures improve the training efficiency of Large Language Models (LLMs) by routing input tokens to a selected subset of specialized experts. Despite their remarkable success, both training and inference in SMoE models suffer from the *expert collapse* issue (Chi et al., 2022a), which degrades model performance. Prior studies primarily focus on improving the router; however, such methods rely on training from scratch or fine-tuning, which requires high computational and data-processing costs. Furthermore, we demonstrate that, despite these efforts, the issue persists when advancing well-pretrained SMoE models, as evidenced by both theoretical and empirical results. To fill that gap, we analyze the advanced SMoE models and observe that the eigenvectors of expert weight matrices encode rich semantic information, pointing to an effective alternative to conventional routing strategies. Building on this insight, we propose **Singular Value Decomposition SMoE (SSMoE)**, a novel and *training-free* framework that leverages spectral properties of the expert weights to address the collapse issue and enhance model performance. Extensive experiments across diverse language and vision tasks, under both clean and corrupt data settings, demonstrate the strong generalization and robustness of SSMoE. Our findings highlight how a deeper understanding of model internals can guide the development of more effective SMoE architectures.

## One-Sentence Claim

SSMoE uses expert-weight eigenvectors as a training-free routing signal to reduce expert collapse and improve sparse Mixture-of-Experts robustness.

## Problem

Sparse MoE models can collapse onto a subset of experts during training or inference, and most router fixes require retraining or fine-tuning that is expensive for already-pretrained large models.

## Core Contribution

The paper reframes routing as something that can be derived from existing expert internals, claiming that spectral structure in expert weight matrices encodes semantic information useful for non-collapsing routing.

## Method

The proposed Singular Value Decomposition SMoE framework analyzes expert weight matrices and leverages their spectral/eigenvector properties to route tokens without additional training. The routing design is meant to avoid conventional learned-router collapse while preserving pretrained expert capabilities.

## Experiments and Evidence

The abstract reports theoretical and empirical evidence that expert collapse persists in advanced pretrained SMoE models, then claims extensive language and vision experiments under clean and corrupted data show stronger generalization and robustness for SSMoE.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: which MoE backbones were tested, how eigenvector routing is computed at inference time, latency/memory overhead, load-balancing metrics, and whether gains persist at frontier LLM scale.

## Deep Themes

- Model internals as reusable structure rather than opaque parameters.
- Training-free adaptation for expensive foundation architectures.
- Spectral geometry as a practical interpretability and control tool.

## Subthemes

- Sparse Mixture of Experts.
- Expert collapse.
- SVD/eigenvector routing.
- Robustness under corruption.
- Language and vision transfer.
- Post-hoc architecture improvement.

## Connections to Other Papers

Connects to SVD interpretability, FAC Synthesis, and other internal-representation papers that use latent model structure as a control surface. It also aligns with efficiency papers that extract more capability from fixed pretrained systems instead of full retraining.

## Notes for Cross-Paper Synthesis

SSMoE strengthens a recurring pattern: mature models contain latent organization that can be operationalized directly, turning interpretability signals into deployment-time mechanisms.
