# Decomposed On-Policy Distillation for Vision-Language Reasoning: Steering Gradients for Visual Grounding

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: Jb1YBPqyb7
- Authors: Hee Suk Yoon; Eunseop Yoon; Jaehyun Jang; SooHwan Eom; Ji Woo Hong; Mark A. Hasegawa-Johnson; Qi Dai; Chong Luo; Chang D. Yoo
- Primary area: deep_learning->large_language_models
- Keywords: Vision Language Model;On-Policy Distillation;Reasoning
- Source URL: https://openreview.net/forum?id=Jb1YBPqyb7
- PDF URL: https://openreview.net/pdf?id=Jb1YBPqyb7

## Abstract

While on-policy distillation offers dense supervision for training small reasoning models, its optimization dynamics in the multimodal domain remain under-explored. In this work, we challenge the standard monolithic view of Vision-Language Model (VLM) distillation by mathematically decomposing the loss into two distinct components: the language prior and visual grounding. Our analysis uncovers that gradient vectors for these components are nearly orthogonal, indicating that the objective of aligning with the teacher's language distribution is geometrically independent from the objective of matching its visual perception. Consequently, standard optimization passively follows a suboptimal compromise trajectory that implicitly balances the two objectives. Hypothesizing that visual grounding constitutes the primary bottleneck for vision-language reasoning, we introduce Visual Gradient Steering (VGS), a method that dynamically reorients the update vector to prioritize the visual subspace. Experimental results on multiple distillation settings and complex multimodal benchmarks demonstrate that VGS significantly outperforms the standard monolithic formulation of on-policy distillation, achieving superior grounding with minimal training overhead.

## One-Sentence Claim

Visual Gradient Steering improves VLM distillation by decomposing teacher alignment into language-prior and visual-grounding components and prioritizing the visual subspace.

## Problem

On-policy distillation gives dense supervision for small reasoning models, but monolithic VLM distillation can follow a poor compromise between language imitation and visual grounding.

## Core Contribution

The paper mathematically decomposes the distillation loss, finds nearly orthogonal gradients for language prior and visual grounding, and introduces a gradient steering method for grounding-focused updates.

## Method

VGS dynamically reorients the optimization update vector toward the visual-grounding component instead of passively following the combined monolithic gradient, with minimal added training overhead.

## Experiments and Evidence

The abstract reports significant gains over standard on-policy distillation across multiple distillation settings and complex multimodal benchmarks, especially in grounding.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: loss decomposition derivation, how visual grounding is isolated, benchmark set, student/teacher models, overhead, and whether language fluency or general reasoning regresses.

## Deep Themes

- Multimodal optimization objectives can hide independent gradient subproblems.
- Visual grounding may be the bottleneck for VLM reasoning.
- Steering gradients turns diagnosis of loss geometry into an intervention.

## Subthemes

- Vision-language reasoning.
- On-policy distillation.
- Visual grounding.
- Gradient orthogonality.
- Small reasoning models.
- Teacher-student alignment.

## Connections to Other Papers

Connects to AGREE through gradient conflict/decomposition and to FlowGuard/3ViewSense through multimodal grounding and cross-modal consistency.

## Notes for Cross-Paper Synthesis

VGS reinforces the optimization-decomposition theme: when objectives combine semantically different skills, explicitly steering their gradient geometry can improve the capability that matters most.
