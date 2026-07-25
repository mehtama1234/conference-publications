# Lookahead Sample Reward Guidance for Test-Time Scaling of Diffusion Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: IbRm6gwmew
- Authors: Yeongmin Kim; Donghyeok Shin; Byeonghu Na; Minsang Park; Richard Lee Kim; Il-chul Moon
- Primary area: deep_learning->generative_models_and_autoencoders
- Keywords: Diffusion Model;Test-time Scaling;Monte Carlo method
- Source URL: https://openreview.net/forum?id=IbRm6gwmew
- PDF URL: https://openreview.net/pdf?id=IbRm6gwmew

## Abstract

Diffusion models have demonstrated strong generative performance; however, generated samples often fail to fully align with human intent. This paper studies an efficient test-time scaling method for sampling from regions with higher human-aligned reward values. Existing methods for computing the expected future reward (EFR) face important limitations: backward rollout incurs prohibitively high sampling costs, while Tweedie-based approaches, including Sequential Monte Carlo and gradient guidance, suffer from bias and inherent sampling issues. We show that the EFR at any $\mathbf{x}_t$ can be computed using only marginal samples from a pre-trained diffusion model, enabling closed-form reward guidance without neural backpropagation. To further improve efficiency, we introduce a few-step lookahead sampling and an accurate solver that guides particles toward high-reward lookahead samples. We refer to this sampling scheme as LiDAR sampling. LiDAR achieves the same GenEval performance as the latest gradient guidance method for SDXL with a 9.5× speedup. We release the code at https://github.com/aailab-kaist/Diffusion-LiDAR-Sampling.

## One-Sentence Claim

LiDAR sampling guides diffusion generation toward higher human-aligned rewards with closed-form expected-future-reward guidance and large speedups over gradient guidance.

## Problem

Diffusion samples may not align with human intent, while existing expected-future-reward guidance methods are either too expensive or biased due to backward rollouts, Tweedie approximations, SMC, or gradient guidance issues.

## Core Contribution

The paper shows that expected future reward at a diffusion state can be computed from marginal samples of a pretrained model, enabling backpropagation-free reward guidance plus efficient few-step lookahead sampling.

## Method

LiDAR sampling draws lookahead marginal samples, computes closed-form reward guidance without neural backpropagation, and uses an accurate solver to steer particles toward high-reward lookahead samples.

## Experiments and Evidence

The abstract reports matching the latest gradient-guidance GenEval performance for SDXL while achieving a 9.5x speedup.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: reward model type, marginal sample count, solver details, image-quality tradeoffs, benchmark breadth, and behavior under misaligned or adversarial rewards.

## Deep Themes

- Test-time scaling for diffusion models.
- Reward guidance without retraining or gradient backpropagation.
- Lookahead sampling as a compute-efficient alignment mechanism.

## Subthemes

- Diffusion sampling.
- Human-aligned rewards.
- Expected future reward.
- Monte Carlo methods.
- GenEval.
- SDXL guidance efficiency.

## Connections to Other Papers

Connects to Top-W and compute-bounded RL through inference-time control, and to VOTP/reward-learning papers through reward propagation under limited supervision.

## Notes for Cross-Paper Synthesis

LiDAR adds a generative-model example of test-time control: alignment can be improved by changing the sampling process, not only by retraining the base model.
