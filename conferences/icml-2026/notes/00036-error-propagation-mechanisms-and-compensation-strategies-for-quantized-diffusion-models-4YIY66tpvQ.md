# Error Propagation Mechanisms and Compensation Strategies for Quantized Diffusion Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 4YIY66tpvQ
- Authors: Songwei Liu; Chao Zeng; Chenqian Yan; Xurui Peng; XING WANG; Fangmin Chen; Xing Mei
- Primary area: deep_learning->generative_models_and_autoencoders
- Keywords: Diffusion Models;Post-training Quantization
- Source URL: https://openreview.net/forum?id=4YIY66tpvQ
- PDF URL: https://openreview.net/pdf?id=4YIY66tpvQ

## Abstract

Diffusion models have transformed image synthesis by establishing unprecedented quality and creativity benchmarks. Nevertheless, their large-scale deployment faces challenges due to computationally intensive iterative denoising processes. Although post-training quantization (PTQ) provides an effective pathway for accelerating sampling, the iterative nature of diffusion models causes stepwise quantization errors to accumulate progressively during generation, inevitably compromising output fidelity. To address this challenge, we develop a theoretical framework that mathematically formulates error propagation in Diffusion Models (DMs), deriving per-step quantization error propagation equations and establishing the first closed-form solution for cumulative error. Building on this theoretical foundation, we propose a timestep-aware cumulative error compensation scheme. Extensive experiments on multiple image datasets demonstrate that our compensation strategy effectively mitigates error propagation, significantly enhancing existing PTQ methods. Specifically, it achieves a 1.2 PSNR improvement over SVDQuant on SDXL W4A4, while incurring only an additional $<$ 0.5\% time overhead.

## One-Sentence Claim

Quantized diffusion models need timestep-aware compensation because iterative denoising causes per-step quantization errors to accumulate and degrade generation quality.

## Problem

Post-training quantization can accelerate diffusion sampling, but diffusion's iterative denoising repeatedly reuses quantized computations, so small per-step errors propagate across the sampling trajectory and compound into visible fidelity loss.

## Core Contribution

The paper derives a mathematical framework for diffusion-model quantization error propagation, including per-step propagation equations and a closed-form cumulative-error solution, then proposes a cumulative error compensation strategy.

## Method

It models how quantization error evolves across denoising timesteps and uses the resulting cumulative-error expression to design a timestep-aware compensation module that can enhance existing PTQ methods with minimal overhead.

## Experiments and Evidence

The abstract reports improvements across multiple image datasets and a 1.2 PSNR gain over SVDQuant on SDXL W4A4 with less than 0.5% extra time overhead.

## Limits and Failure Modes

No confident local PDF/arXiv match yet, so details still need checking: exact closed-form assumptions, interaction with different samplers/schedulers, whether compensation depends on calibration data, and perceptual-quality tradeoffs beyond PSNR.

## Deep Themes

- Deployment compression must account for temporal error propagation.
- Diffusion quantization differs from one-shot model quantization because sampling is iterative.
- Efficiency methods increasingly need model-dynamics-specific error theory.

## Subthemes

- Diffusion models.
- Post-training quantization.
- Quantization error propagation.
- Timestep-aware compensation.
- SDXL deployment.
- Sampling efficiency.

## Connections to Other Papers

Connects to LiftQuant, low-precision transformer training, and FOCUS/RePAIR as a compression cluster where naive efficiency changes can alter downstream behavior. It also links to IRNO through iterative-process error correction.

## Notes for Cross-Paper Synthesis

This paper adds a diffusion-specific efficiency theme: deployment optimization must model how approximation errors move through the generation trajectory, not only how large they are at one layer or step.
