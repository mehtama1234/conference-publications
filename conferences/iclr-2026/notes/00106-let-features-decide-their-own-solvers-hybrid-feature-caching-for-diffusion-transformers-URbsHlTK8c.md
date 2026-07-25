# Let Features Decide Their Own Solvers: Hybrid Feature Caching for Diffusion Transformers

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: URbsHlTK8c
- Authors: Shikang Zheng; Guantao Chen; Qinming Zhou; Yuqi Lin; Lixuan He; Chang Zou; Peiliang Cai; Jiacheng Liu; Linfeng Zhang
- Primary area: generative models
- Keywords: Efficient ML;Diffusion Transformer Acceleration;Feature Caching
- Source URL: https://openreview.net/forum?id=URbsHlTK8c
- PDF URL: https://openreview.net/pdf?id=URbsHlTK8c

## Abstract

Diffusion Transformers (DiTs) offer state-of-the-art fidelity in image and video synthesis, but their iterative sampling process remains a major bottleneck due to the high cost of transformer forward passes at each timestep. To mitigate this, feature caching has emerged as a training-free acceleration technique that reuses or forecasts hidden representations. However, existing methods often apply a uniform caching strategy across all feature dimensions, ignoring their heterogeneous dynamic behaviors. Therefore, we adopt a new perspective by modeling hidden feature evolution as a mixture of ODEs across dimensions, and introduce \textbf{HyCa}, a Hybrid ODE solver inspired caching framework that applies dimension-wise caching strategies. HyCa achieves near-lossless acceleration across diverse domains and models, including 5.56$\times$ speedup on FLUX and HunyuanVideo, 6.24$\times$ speedup on Qwen-Image and Qwen-Image-Edit without retraining. \emph{Our code is in supplementary material and will be released on Github.}

## One-Sentence Claim

HyCa accelerates diffusion transformers by assigning hidden-feature dimensions different ODE-solver-inspired caching strategies according to their heterogeneous dynamics.

## Problem

Diffusion Transformers achieve high image and video fidelity, but iterative sampling requires many expensive transformer forward passes.

Feature caching can speed sampling by reusing or forecasting hidden states, but existing methods often apply one uniform policy across all feature dimensions, ignoring that dimensions evolve differently over timesteps.

## Core Contribution

The paper introduces HyCa, a hybrid feature-caching framework for DiT acceleration.

Its main conceptual move is to model hidden feature evolution as a mixture of ODEs across dimensions and let each dimension use an appropriate caching/solver strategy.

## Method

HyCa treats feature dimensions as having distinct temporal dynamics during diffusion sampling.

Instead of reusing all hidden features with the same rule, it applies dimension-wise caching strategies inspired by hybrid ODE solvers, allowing stable dimensions to be reused more aggressively while dynamic dimensions receive more accurate updates.

## Experiments and Evidence

The abstract reports near-lossless acceleration across domains and models.

HyCa achieves 5.56x speedup on FLUX and HunyuanVideo and 6.24x speedup on Qwen-Image and Qwen-Image-Edit without retraining.

## Limits and Failure Modes

Dimension-wise caching may depend on stable feature-dynamics estimates and could fail for prompts or timesteps where usually stable dimensions abruptly change. Reported speedups need quality, memory, and overhead accounting.

Because this note is abstract-only, details still need checking: ODE mixture formulation, solver choices, feature grouping, quality metrics, exact sampling steps, and whether artifacts appear in video temporal consistency.

## Deep Themes

- Feature-level adaptive acceleration: hidden dimensions are treated as heterogeneous dynamical processes.
- Training-free DiT serving: sampling speed is improved without retraining the generator.
- Solver choice as representation policy: cache decisions become local numerical-method choices.
- Near-lossless generative efficiency: acceleration must preserve image/video fidelity.

## Subthemes

- Diffusion Transformer acceleration.
- Feature caching.
- Hybrid ODE solvers.
- Dimension-wise hidden dynamics.

## Connections to Other Papers

This connects to DCFold, DiffusionNFT, NextStep-1, InfoTok, and FlashVID through efficient generative-model inference.

It also relates to ThinKV and EntroKV because both allocate memory or reuse budget according to internal feature behavior.

## Notes for Cross-Paper Synthesis

HyCa adds a fine-grained efficiency pattern: model internals are not uniformly dynamic, so acceleration should operate at the feature or dimension level.
