# DGS-Net: Distillation-Guided Gradient Surgery for CLIP Fine-Tuning in AI-Generated Image Detection

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: G5XGej7wNt
- Authors: Jiazhen Yan; Ziqiang Li; Fan Wang; Boyu Wang; Ziwen He; Zhangjie Fu
- Primary area: social_aspects->security
- Keywords: AIGI Detection; AI Security; Knowledge Distillation
- Source URL: https://openreview.net/forum?id=G5XGej7wNt
- PDF URL: https://openreview.net/pdf?id=G5XGej7wNt

## Abstract

The rapid progress of generative models such as GANs and diffusion models has led to the widespread proliferation of AI-generated images, raising concerns about misinformation, privacy violations, and trust erosion in digital media. Although large-scale multimodal models like CLIP offer strong transferable representations for detecting synthetic content, fine-tuning them often induces catastrophic forgetting, which degrades pre-trained priors and limits cross-domain generalization. To address this issue, we propose the Distillation-guided Gradient Surgery Network (DGS-Net), a novel framework that preserves transferable pre-trained priors while suppressing task-irrelevant components. Specifically, we introduce a gradient-space decomposition that separates harmful and beneficial descent directions during optimization. By projecting task gradients onto the orthogonal complement of harmful directions and aligning with beneficial ones distilled from a frozen CLIP encoder, DGS-Net achieves unified optimization of prior preservation and irrelevant suppression. Extensive experiments on 50 generative models demonstrate that our method outperforms state-of-the-art approaches by an average margin of 6.6%, achieving superior detection performance and generalization across diverse generation techniques.

## One-Sentence Claim

DGS-Net fine-tunes CLIP for AI-generated image detection by surgically removing harmful gradient components while preserving transferable pretrained priors through distillation.

## Problem

CLIP representations transfer well to synthetic-image detection, but fine-tuning can cause catastrophic forgetting that hurts cross-domain generalization across generators.

## Core Contribution

The paper proposes Distillation-Guided Gradient Surgery, separating beneficial and harmful descent directions during optimization using a frozen CLIP encoder.

## Method

DGS-Net decomposes gradients in gradient space, projects task gradients away from harmful directions, and aligns them with beneficial directions distilled from frozen CLIP to jointly preserve priors and suppress irrelevant components.

## Experiments and Evidence

The abstract reports experiments on 50 generative models, outperforming state-of-the-art approaches by an average 6.6% margin with better generalization across generation techniques.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: generator split design, harmful-direction definition, CLIP backbone choices, and robustness to future generators.

## Deep Themes

- Fine-tuning safety detectors must preserve broad pretrained priors.
- Gradient surgery can separate useful task adaptation from forgetting.
- Synthetic-media detection is a moving cross-generator generalization problem.

## Subthemes

- AI-generated image detection.
- CLIP fine-tuning.
- Gradient surgery.
- Knowledge distillation.
- Catastrophic forgetting.
- Security and misinformation.

## Connections to Other Papers

Connects to Concept Removal Guidance, Jailbreak Foundry, multimodal safety, and CLIP fine-tuning papers through security under generative-model proliferation.

## Notes for Cross-Paper Synthesis

DGS-Net adds a detector-adaptation theme: safety classifiers need to adapt without destroying the broad priors that make them generalize.
