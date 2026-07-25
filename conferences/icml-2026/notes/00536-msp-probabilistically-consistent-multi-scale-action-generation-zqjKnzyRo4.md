# MSP: Probabilistically Consistent Multi-Scale Action Generation

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: zqjKnzyRo4
- Authors: Zhixuan Lin; Gengqi Liu; Chao Zheng; Gao Lin; Jindong Yu; Song Gao; Fei Wang
- Primary area: applications->robotics
- Keywords: Robotic Imitation Learning;Long-horizon Manipulation;Coarse-to-fine Generation;Multi-scale Policy;Action Generation;Probabilistic Consistency
- Source URL: https://openreview.net/forum?id=zqjKnzyRo4
- PDF URL: https://openreview.net/pdf?id=zqjKnzyRo4

## Abstract

In robotic imitation learning, accurately modeling the multimodality and temporal correlations of long-horizon action sequences remains challenging. Long-horizon tasks require preserving global task intent while executing precise low-level control; otherwise, local errors can accumulate and lead to failure. While recent coarse-to-fine autoregressive models have improved action generation, they struggle to maintain consistency across hierarchies, leading to suboptimal performance in long-horizon tasks. To address these shortcomings, we propose Probabilistically Consistent Multi-Scale Action Generation (MSP), a novel coarse-to-fine approach that promotes cross-scale consistency. MSP adopts a streamlined multi-scale design by directly downsampling in a continuous latent space. A scale-wise autoregressive Transformer is used to generate semantic conditions at each scale, which guide a lightweight MeanFlow model to capture multi-scale latent distributions, enabling probabilistically consistent refinement across scales. Through extensive simulation and real-world experiments, including long-horizon, multi-task, and few-shot generalization settings, we show that MSP outperforms existing coarse-to-fine methods, achieving state-of-the-art performance with high efficiency.

## One-Sentence Claim

MSP improves long-horizon robotic imitation learning by generating actions coarse-to-fine while enforcing probabilistic consistency across temporal scales.

## Problem

Long-horizon robotic manipulation requires both global task intent and precise low-level control. If coarse plans and fine actions diverge, local errors accumulate and the task fails.

Recent coarse-to-fine autoregressive action models help with long horizons but can be inconsistent across hierarchy levels, weakening performance on long-horizon tasks.

## Core Contribution

The paper proposes Probabilistically Consistent Multi-Scale Action Generation, MSP, a coarse-to-fine action generation framework designed to maintain cross-scale consistency.

Its core contribution is a streamlined multi-scale design that downsamples in continuous latent space, uses a scale-wise autoregressive Transformer for semantic conditions, and uses a lightweight MeanFlow model to represent multi-scale latent distributions.

## Method

MSP directly downscales action sequences in continuous latent space to build multiple temporal scales. A scale-wise autoregressive Transformer generates semantic conditions for each scale.

Those conditions guide a lightweight MeanFlow model that captures latent distributions at each scale, enabling refinement that is probabilistically consistent rather than merely hierarchically conditioned.

## Experiments and Evidence

The abstract reports extensive simulation and real-world experiments.

It claims state-of-the-art performance and high efficiency across long-horizon, multi-task, and few-shot generalization settings, outperforming existing coarse-to-fine methods.

## Limits and Failure Modes

The method depends on latent downsampling preserving task-relevant temporal structure. If coarse latents discard rare but critical control details, fine-scale refinement may not recover them.

Because this note is abstract-only, details still need checking: robot platforms, task suite, action representation, latent downsampling method, MeanFlow architecture, baselines, real-world trial counts, and failure analysis on contact-rich tasks.

## Deep Themes

- Hierarchical action generation: long-horizon control needs multiple temporal scales.
- Cross-scale probabilistic consistency: coarse intent and fine control must agree distributionally.
- Continuous latent action abstraction: downsampling in latent space can simplify hierarchy construction.
- Efficient generative policies for robotics: MeanFlow-style models support fast action refinement.

## Subthemes

- Coarse-to-fine imitation learning.
- Scale-wise autoregressive Transformers.
- Multi-scale latent distributions.
- Long-horizon and few-shot robotic generalization.

## Connections to Other Papers

This connects to VectorWorld, EcoVLA, and GLANCE through embodied sequential decision making. It also relates to Reverse Flow Matching, Diffusion Flow Matching, and DivIn because flow-based generative modeling is used as a control mechanism.

It belongs with hierarchical RL and long-horizon policy papers such as SOL and H1, but focuses on imitation-learning action generation rather than reward-driven reasoning.

## Notes for Cross-Paper Synthesis

MSP adds a cross-scale consistency theme: hierarchical generation is useful only when local refinements remain probabilistically aligned with global intent.
