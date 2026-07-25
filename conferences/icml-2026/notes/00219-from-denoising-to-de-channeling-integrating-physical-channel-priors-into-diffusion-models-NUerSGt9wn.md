# From Denoising to De-Channeling: Integrating Physical Channel Priors into Diffusion Models for Radio Signal Understanding

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: NUerSGt9wn
- Authors: Yaoqi Liu; Jin Wang; Chunchen Wang; Hui Wang; Chuan Shi
- Primary area: deep_learning->selfsupervised_learning
- Keywords: Diffusion;Radio signal understanding;Wireless channel
- Source URL: https://openreview.net/forum?id=NUerSGt9wn
- PDF URL: https://openreview.net/pdf?id=NUerSGt9wn

## Abstract

In recent years, wireless signal recognition (WSR), which leverages artificial intelligence (AI) to identify properties of passively received radio signals, has garnered significant attention due to its broad applications, such as spectrum management. Existing WSR methods typically learn directly from received signals, which are distorted by physical wireless channel effects such as fading, and current denoising diffusion models lack de-channeling capabilities, which leads to performance degradation. Therefore, we propose PWC-Diff, a novel framework that integrates prior Physical Wireless Channels into the denoising Diffusion process. The framework employs a dedicated architecture named FusedFormer, which contains a fusion module and a self-attention module that jointly capture the temporal and spectral characteristics of the signals throughout the diffusion trajectory. By leveraging prior wireless channels, PWC-Diff learns to progressively “de-channel” the received signal and recover a representation closer to the transmitted signal. Extensive experiments on several datasets across three WSR tasks have achieved state-of-the-art (SOTA) performance, which demonstrates the rationality of our theory, and ablation experiments further illustrate the effectiveness of our proposed PWC-Diff. Code is available at https://github.com/BUPT-GAMMA/FoundWSR.

## One-Sentence Claim

PWC-Diff integrates physical wireless channel priors into diffusion models so received radio signals can be progressively de-channeled toward transmitted-signal representations.

## Problem

Wireless signal recognition methods learn from received signals distorted by fading and other channel effects, while standard denoising diffusion lacks explicit de-channeling capability.

## Core Contribution

The paper proposes a diffusion framework with physical wireless channel priors and a FusedFormer architecture that jointly captures temporal and spectral signal structure along the diffusion trajectory.

## Method

PWC-Diff injects prior channel knowledge into the denoising process, using fusion and self-attention modules to recover representations closer to transmitted signals rather than merely denoised received signals.

## Experiments and Evidence

The abstract reports state-of-the-art performance across several datasets and three wireless signal recognition tasks, with ablation studies supporting the proposed components.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: channel models, task definitions, datasets, generalization to unseen channel conditions, computational cost, and dependence on accurate physical priors.

## Deep Themes

- Physical channel priors can turn generic denoising into domain-specific inverse modeling.
- Diffusion trajectories can encode structured correction processes.
- Temporal and spectral fusion is central for radio signal understanding.

## Subthemes

- Wireless signal recognition.
- Diffusion models.
- Physical channel priors.
- De-channeling.
- Temporal-spectral attention.
- Spectrum management.

## Connections to Other Papers

Connects to scientific/physical-domain generation papers such as Modified SINNs, GFG, and weather latent modeling through explicit domain priors.

## Notes for Cross-Paper Synthesis

PWC-Diff adds a physical-prior diffusion theme: domain distortion should be modeled through the physics that produced it, not treated as generic noise.
