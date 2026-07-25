# Neon: Negative Extrapolation From Self-Training Improves Image Generation

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: kpLRYtPGt3
- Authors: Sina Alemohammad; Zhangyang Wang; Richard Baraniuk
- Primary area: generative models
- Keywords: Generative Models;Self-Improvement;Weight Merging;Image Generation
- Source URL: https://openreview.net/forum?id=kpLRYtPGt3
- PDF URL: https://openreview.net/pdf?id=kpLRYtPGt3

## Abstract

Scaling generative AI models is bottlenecked by the scarcity of high-quality training data. The ease of synthesizing from a generative model suggests using (unverified) synthetic data to augment a limited corpus of real data for the purpose of fine-tuning in the hope of improving performance. Unfortunately, however, the resulting positive feedback loop leads to model autophagy disorder (MAD, aka model collapse) that results in a rapid degradation in sample quality and/or diversity. In this paper, we introduce Neon (for Negative Extrapolation frOm self-traiNing), a new learning method that turns the degradation from self-training into a powerful signal for self-improvement. Given a base model, Neon first fine-tunes it on its own self-synthesized data but then, counterintuitively, reverses its gradient updates to extrapolate away from the degraded weights.  We prove that Neon works because typical inference samplers that favor high-probability regions create a predictable anti-alignment between the synthetic and real data population gradients, which negative extrapolation corrects to better align the model with the true data distribution. Neon is remarkably easy to implement via a simple post-hoc merge that requires no new real data, works effectively with as few as 1k synthetic samples, and typically uses less than 1\% additional training compute.  We demonstrate Neon’s universality across a range of architectures (diffusion, flow matching, autoregressive, and inductive moment matching models) and datasets (ImageNet, CIFAR-10, and FFHQ). In particular, on ImageNet 256x256, Neon elevates the xAR-L model to a new state-of-the-art FID of 1.02 with only 0.36\% additional training compute.

## One-Sentence Claim

Neon turns self-training degradation into an improvement signal by fine-tuning on self-generated images, reversing the resulting weight update, and merging away from the degraded model.

## Problem

High-quality real data limits generative-model scaling, but naive synthetic self-training creates feedback loops that degrade sample quality and diversity. The challenge is extracting useful information from a model's own samples without inducing model collapse.

## Core Contribution

The paper introduces Negative Extrapolation from Self-Training, a simple post-hoc weight-merge method that uses the direction of self-training degradation as an anti-gradient. It also gives a theoretical explanation based on sampler-induced anti-alignment between synthetic and real population gradients.

## Method

Starting from a base model, Neon fine-tunes on a small set of self-synthesized samples, then reverses or extrapolates away from the resulting weight update. The method is applied as a lightweight post-hoc merge, requiring no new real data and less than 1 percent additional training compute according to the abstract.

## Experiments and Evidence

The method reportedly works with as few as 1k synthetic samples across diffusion, flow matching, autoregressive, and inductive moment matching models on ImageNet, CIFAR-10, and FFHQ. On ImageNet 256x256, it improves xAR-L to FID 1.02 with 0.36 percent extra training compute.

## Limits and Failure Modes

Negative extrapolation assumes the self-training update reliably points toward a predictable degradation direction. It may fail when synthetic samples are too diverse, too low quality, sampled with unusual guidance, or when fine-tuning noise dominates. Full-text review should check merge coefficients, sampler settings, architectures, diversity metrics, and whether repeated Neon applications remain stable.

## Deep Themes

- Synthetic data as a diagnostic signal.
- Model-collapse direction as useful negative evidence.
- Post-hoc weight merging for generative improvement.
- Low-compute self-improvement without new real data.

## Subthemes

- Negative extrapolation.
- Self-training anti-gradients.
- Sampler-induced distribution bias.
- Cross-architecture generative improvement.
- Data scarcity for image generation.

## Connections to Other Papers

Connects to data-governance and pretraining-efficiency work through high-quality data scarcity, to diffusion post-training/distillation papers through lightweight generative model improvement, and to LoRA/weight-merge themes where small parameter-space moves create useful behavioral shifts.

## Notes for Cross-Paper Synthesis

Neon reframes failure as supervision: the collapse direction from self-training tells the model which way not to move. This is a deeper example of using process diagnostics, rather than labels, to guide improvement.
