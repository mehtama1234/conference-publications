# Training Diffusion Language Models for Black-Box Optimization

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: Z7wI0sor6i
- Authors: Zipeng Sun; Can Chen; Ye Yuan; Haolun Wu; Jiayao Gu; Christopher Pal; Xue Liu
- Primary area: applications->chemistry_physics_and_earth_sciences
- Keywords: Diffusion Large Language Models;Offline Black-Box Optimization
- Source URL: https://openreview.net/forum?id=Z7wI0sor6i
- PDF URL: https://openreview.net/pdf?id=Z7wI0sor6i

## Abstract

We study offline black-box optimization (BBO), aiming to discover improved designs from an offline dataset of designs and labels, a problem common in robotics, DNA, and materials science with limited labeled samples. While recent work applies autoregressive LLMs to BBO by formatting tasks as natural-language prompts, their left-to-right design generation struggles to capture the strong bidirectional dependencies inherent in design problems. To address this, we propose adapting diffusion LLMs to offline BBO to leverage their bidirectional modeling capabilities. However, a domain gap exists between the natural text pre-training of diffusion LLMs and the heterogeneous signals in BBO (prompts, designs, and labels). To bridge this gap, we construct a unified prompt–-response corpus and introduce delimiter tokens to explicitly mark field boundaries for domain adaptation. We further propose a two-stage post-training framework to align the diffusion LLM generation with high-label designs. The first stage performs supervised fine-tuning on the unified dataset via masked-response prediction, and the second stage adopts reinforcement learning with rewards defined by label improvements. Our method achieves state-of-the-art results on Design-Bench under small-data settings. Code for our work is available here: https://github.com/zpointS/DiBO.

## One-Sentence Claim

Diffusion language models improve offline black-box optimization by bidirectionally modeling prompt, design, and label fields, then post-training generation toward high-label designs.

## Problem

Offline black-box optimization seeks better designs from a fixed dataset of designs and labels, common in robotics, DNA, and materials science where labels are scarce. Autoregressive LLM approaches serialize BBO tasks as natural-language prompts, but left-to-right generation can struggle with strong bidirectional dependencies among design variables.

The paper asks whether diffusion LLMs are a better fit for design optimization under small-data conditions.

## Core Contribution

The paper adapts diffusion LLMs to offline BBO. It builds a unified prompt-response corpus and adds delimiter tokens to mark boundaries among prompts, designs, and labels, bridging the gap between natural-text pretraining and heterogeneous BBO signals.

It then uses two-stage post-training: supervised fine-tuning by masked-response prediction, followed by reinforcement learning with rewards based on label improvements. The method reaches state-of-the-art on Design-Bench under small-data settings.

## Method

The model represents BBO examples as structured text with explicit field delimiters. Diffusion language modeling allows masked/bidirectional generation over the design response rather than only left-to-right generation.

SFT teaches the task format and conditional design distribution; RL shifts generation toward designs with improved labels.

## Experiments and Evidence

Evidence reported in the abstract:

- Offline BBO domains including robotics, DNA, and materials-science relevance.
- Unified prompt-response corpus with delimiter tokens.
- Two-stage post-training with masked-response SFT and label-improvement RL.
- State-of-the-art results on Design-Bench under small-data settings.
- Code release.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: Design-Bench tasks, diffusion LM base model, reward computation, oracle use, and out-of-distribution design validity.

## Limits and Failure Modes

- Offline BBO can exploit learned or benchmark oracles without producing physically valid designs.
- RL toward high labels may reduce diversity or leave the data manifold.
- Text serialization and delimiter choices may heavily influence results.
- Diffusion LMs may be slower at inference than autoregressive alternatives.

## Deep Themes

**Design problems need bidirectional dependencies.** Diffusion LMs are motivated by the fact that design variables mutually constrain each other.

**Post-training bridges modality mismatch.** Prompt/design/label corpora adapt language models to structured optimization data.

**Optimization becomes generation with reward steering.** The model proposes designs, while labels define the improvement signal.

## Subthemes

- Offline black-box optimization.
- Diffusion language models.
- Unified prompt-response design corpora.
- Masked-response prediction.
- Label-improvement RL.

## Connections to Other Papers

Connects to UDM-GRPO, TD3B, FlowOptimizer, and scientific generative design papers. It also links to Procedural Pretraining because structured delimiters and task formats act as scaffolds for adapting language models beyond ordinary text.

## Notes for Cross-Paper Synthesis

This paper reinforces that generative models for science and design need task-native serialization plus post-training objectives aligned with design improvement.
