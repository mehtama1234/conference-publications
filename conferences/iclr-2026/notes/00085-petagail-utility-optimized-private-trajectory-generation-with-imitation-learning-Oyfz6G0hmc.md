# PetaGAIL++: Utility Optimized Private Trajectory Generation with Imitation Learning

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: Oyfz6G0hmc
- Authors: Yingjie Ma; Bijal Bharadva; Xin Zhang; Joann Qiongna Chen
- Primary area: alignment, fairness, safety, privacy, and societal considerations
- Keywords: Differential Privacy;Imitation Learning
- Source URL: https://openreview.net/forum?id=Oyfz6G0hmc
- PDF URL: https://openreview.net/pdf?id=Oyfz6G0hmc

## Abstract

Human mobility trajectory data supports a wide range of applications, including urban planning, intelligent transportation systems, and public safety monitoring. However, large-scale, high-quality mobility datasets are difficult to obtain due to privacy concerns. Raw trajectory data may reveal sensitive user information, such as home addresses, routines, or social relationships, making it crucial to develop privacy-preserving alternatives. Recent advances in deep generative modeling have enabled synthetic trajectory generation, but existing methods either lack formal privacy guarantees or suffer from reduced utility and scalability. Differential Privacy (DP) has emerged as a rigorous framework for data protection, and recent efforts such as PATE-GAN and PATEGAIL integrate DP with generative adversarial learning. While promising, these methods struggle to generalize across diverse trajectory patterns and often incur significant utility degradation. In this work, we propose a new framework that builds on PATEGAIL by introducing a sensitivity-aware noise injection module that dynamically adjusts privacy noise based on sample-level sensitivity. This design significantly improves trajectory fidelity, downstream task performance, and scalability under strong privacy guarantees. We evaluate our method on real-world mobility datasets and demonstrate its superiority over state-of-the-art baselines in terms of privacy-utility trade-off.

## One-Sentence Claim

PetaGAIL++ improves differentially private synthetic mobility trajectory generation by injecting privacy noise according to sample-level sensitivity.

## Problem

Human mobility trajectories are valuable for urban planning, transportation, and public safety, but raw trajectories can reveal home locations, routines, social ties, and other sensitive information.

Synthetic trajectory generation can help, but prior methods often lack formal privacy guarantees or lose too much utility under differential privacy.

## Core Contribution

The paper proposes PetaGAIL++, a privacy-preserving trajectory generation framework built on PATEGAIL.

Its key addition is a sensitivity-aware noise injection module that dynamically adjusts DP noise by sample-level sensitivity, improving the privacy-utility tradeoff.

## Method

PetaGAIL++ combines imitation-learning-style generative adversarial trajectory modeling with differential privacy.

Instead of adding uniform privacy noise, it estimates or uses sample-level sensitivity to allocate noise where privacy risk is higher and preserve fidelity where less perturbation is needed.

## Experiments and Evidence

The abstract reports evaluation on real-world mobility datasets.

PetaGAIL++ outperforms state-of-the-art baselines on trajectory fidelity, downstream task performance, scalability, and privacy-utility tradeoff under strong privacy guarantees.

## Limits and Failure Modes

Sample-level sensitivity estimation must itself be reliable; underestimating sensitivity could weaken privacy, while overestimating it can reduce utility. Mobility privacy also includes linkage attacks beyond aggregate trajectory resemblance.

Because this note is abstract-only, details still need checking: DP accounting, sensitivity definition, imitation-learning objective, datasets, downstream tasks, attack evaluations, and scalability claims.

## Deep Themes

- Adaptive privacy noise: privacy mechanisms can allocate perturbation by risk rather than treating all trajectories equally.
- Synthetic data with formal guarantees: generative models are being adapted to regulated, high-sensitivity domains.
- Utility-aware privacy: downstream task performance is treated as a core metric, not an afterthought.
- Mobility as privacy stress test: trajectories expose identity through repeated spatiotemporal patterns.

## Subthemes

- Differential privacy.
- Synthetic trajectory generation.
- Imitation learning.
- Sensitivity-aware noise injection.

## Connections to Other Papers

This connects to privacy, unlearning, and data-governance papers across both conferences.

It also relates to SimuHome and agent-environment work because both involve temporally structured human activity data and real-world deployment constraints.

## Notes for Cross-Paper Synthesis

PetaGAIL++ adds a data-governance pattern: privacy-preserving generation increasingly needs adaptive mechanisms that protect sensitive cases without destroying population-level utility.
