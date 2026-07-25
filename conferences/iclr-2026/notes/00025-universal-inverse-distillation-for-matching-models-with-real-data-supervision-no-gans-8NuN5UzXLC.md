# Universal Inverse Distillation for Matching Models with Real-Data Supervision (No GANs)

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: 8NuN5UzXLC
- Authors: Nikita Maksimovich Kornilov; David Li; Tikhon Mavrin; Aleksei Leonov; Nikita Gushchin; Evgeny Burnaev; Iaroslav Sergeevich Koshelev; Alexander Korotin
- Primary area: generative models
- Keywords: Diffusion models;Flow Matching;Acceleration of diffusion/flow models;Distillation of diffusion/flow models
- Source URL: https://openreview.net/forum?id=8NuN5UzXLC
- PDF URL: https://openreview.net/pdf?id=8NuN5UzXLC

## Abstract

While achieving exceptional generative quality, modern diffusion, flow, and other matching models suffer from slow inference, as they require many steps of iterative generation. Recent distillation methods address this by training efficient one-step generators under the guidance of a pre-trained teacher model. However, these methods are often constrained to only one specific framework, e.g., only to diffusion or only to flow models. Furthermore, these methods are naturally data-free, and to benefit from the usage of real data, it is required to use an additional complex adversarial training with an extra discriminator model. In this paper, we present \textbf{RealUID}, a unified distillation framework for all matching models that seamlessly incorporates real data into the distillation procedure without GANs. Our \textbf{RealUID} approach offers a simple theoretical foundation that covers previous distillation methods for Flow Matching and Diffusion models, and is also extended to their modifications, such as Bridge Matching and Stochastic Interpolants.

## One-Sentence Claim

RealUID distills diffusion, flow, and other matching models into efficient generators while incorporating real-data supervision without adversarial GAN training.

## Problem

Diffusion and flow/matching models generate high-quality samples but are slow because they require many iterative steps.

Existing distillation methods can train one-step generators, but they are often tied to one modeling framework and are naturally data-free. Adding real-data supervision typically requires adversarial training with an extra discriminator.

## Core Contribution

The paper introduces RealUID, a unified inverse-distillation framework for matching models that incorporates real data without GANs.

Its theoretical foundation covers previous distillation methods for Flow Matching and Diffusion models and extends to variants such as Bridge Matching and Stochastic Interpolants.

## Method

RealUID distills a pretrained teacher matching model into a faster generator while using real data directly in the distillation procedure.

The framework is designed to be model-family agnostic across diffusion, flow matching, bridge matching, and stochastic-interpolant variants, avoiding the need for a discriminator.

## Experiments and Evidence

The abstract emphasizes theoretical unification and real-data-compatible distillation. It does not provide specific quantitative results in the local abstract.

Because this note is abstract-only, experimental details need checking from the full paper: sample quality, step count, speedup, datasets, teacher families, and comparisons against adversarial distillation baselines.

## Limits and Failure Modes

Distillation can trade diversity or fidelity for speed, and one-step generators may inherit teacher biases while losing iterative correction capacity.

Because details are absent locally, open questions include how real-data supervision is weighted, whether mode coverage improves, and whether the unified theory translates to strong empirical performance across model families.

## Deep Themes

- Unified generative distillation: diffusion and flow acceleration can share a common framework.
- Real-data supervision without GANs: distillation can use data without adversarial discriminators.
- Inference acceleration as deployment enabler: slow iterative generation remains a practical bottleneck.
- Matching-model abstraction: bridge matching and stochastic interpolants fit into a broader generative family.

## Subthemes

- One-step generator distillation.
- Diffusion and flow matching unification.
- Bridge Matching and Stochastic Interpolants.
- Non-adversarial real-data supervision.

## Connections to Other Papers

This connects to ICML's Diffusion Flow Matching theory, Reverse Flow Matching, DivIn, and MSP because flow/diffusion methods are being unified, accelerated, and used for control.

It also relates to FlashWorld and other fast generative-scene papers where speed determines whether a model is deployable.

## Notes for Cross-Paper Synthesis

RealUID adds an acceleration/unification thread: as matching models diversify, practical deployment needs distillation methods that work across the family and can still use real data.
