# Half-order Fine-Tuning for Diffusion Model: A Recursive Likelihood Ratio Optimizer

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: AZ6lqcvHLX
- Authors: Tao Ren; Zishi Zhang; Jinyang Jiang; Zehao Li; Shentao Qin; Yi Zheng; Guanghao Li; Qianyou Sun; Yan Li; Jiafeng Liang; Xinping Li; Yijie Peng
- Primary area: optimization
- Keywords: perturbation-based gradient estimation;diffusion model;post-training
- Source URL: https://openreview.net/forum?id=AZ6lqcvHLX
- PDF URL: https://openreview.net/pdf?id=AZ6lqcvHLX

## Abstract

The probabilistic diffusion model (DM), generating content by inferencing through a recursive chain structure, has emerged as a powerful framework for visual generation. After pre-training on enormous data, the model needs to be properly aligned to meet requirements for downstream applications. How to efficiently align the foundation DM is a crucial task. Contemporary methods are either based on Reinforcement Learning (RL) or truncated Backpropagation (BP). However, RL and truncated BP suffer from low sample efficiency and biased gradient estimation, respectively, resulting in limited improvement or, even worse, complete training failure. To overcome the challenges, we propose the Recursive Likelihood Ratio (RLR) optimizer, a Half-Order (HO) fine-tuning paradigm for DM. The HO gradient estimator enables the computation graph rearrangement within the recursive diffusive chain, making the RLR's gradient estimator **an unbiased one with lower variance** than other methods. We theoretically investigate the bias, variance, and convergence of our method. Extensive experiments are conducted on image and video generation to validate the superiority of the RLR. Furthermore, we propose a novel prompt technique that is natural for the RLR to achieve a synergistic effect. The implementation is available at https://github.com/RTkenny/RLR-Optimizer.

## One-Sentence Claim

RLR fine-tunes diffusion models with an unbiased lower-variance half-order gradient estimator by rearranging computation through the recursive diffusion chain.

## Problem

Foundation diffusion models need downstream alignment after pretraining. Existing RL-based and truncated-backpropagation fine-tuning methods face low sample efficiency or biased gradient estimates.

These limitations can produce weak improvements or training failure, especially in recursive multi-step diffusion generation.

## Core Contribution

The paper proposes Recursive Likelihood Ratio, RLR, a Half-Order fine-tuning paradigm for diffusion models.

Its core contribution is a half-order gradient estimator that rearranges the recursive diffusion computation graph to produce an unbiased estimator with lower variance than competing approaches.

## Method

RLR uses likelihood-ratio estimation through the recursive diffusion chain. The half-order estimator is designed to avoid the bias of truncated BP while improving variance over RL-style estimators.

The paper also proposes a prompt technique that naturally interacts with RLR to produce a synergistic effect.

## Experiments and Evidence

The abstract reports theoretical analysis of bias, variance, and convergence.

It also reports extensive image and video generation experiments validating the superiority of RLR over contemporary RL or truncated-BP fine-tuning approaches.

## Limits and Failure Modes

Likelihood-ratio estimators can still be noisy, and diffusion fine-tuning may be sensitive to reward design, prompt distribution, and compute cost.

Because this note is abstract-only, details still need checking: estimator derivation, variance comparison, reward/objective setup, prompt technique, image/video datasets, and stability under long diffusion chains.

## Deep Themes

- Post-training diffusion alignment: foundation generative models need efficient downstream control.
- Bias-variance tradeoff in recursive models: gradient estimators must respect the diffusion chain.
- Half-order optimization: rearranging computation graphs creates an intermediate between RL and backprop.
- Prompt-optimizer interaction: prompting can alter optimization effectiveness, not only inference outputs.

## Subthemes

- Recursive likelihood ratio.
- Unbiased diffusion fine-tuning.
- Lower-variance gradient estimation.
- Image and video generation alignment.

## Connections to Other Papers

This connects to RealUID, Diffusion Flow Matching theory, DivIn, Reverse Flow Matching, and AGSM through diffusion/flow control and acceleration.

It also relates to RACO and preference optimization work because it targets downstream alignment of large generative models.

## Notes for Cross-Paper Synthesis

RLR adds to the diffusion post-training theme: as diffusion models become foundation models, fine-tuning requires estimators tailored to recursive generation rather than borrowed from generic RL or BP.
