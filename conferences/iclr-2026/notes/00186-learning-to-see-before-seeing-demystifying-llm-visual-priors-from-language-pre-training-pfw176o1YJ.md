# Learning to See Before Seeing: Demystifying LLM Visual Priors from Language Pre-training

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: pfw176o1YJ
- Authors: Junlin Han; Shengbang Tong; David Fan; Yufan Ren; Koustuv Sinha; Philip Torr; Filippos Kokkinos
- Primary area: foundation or frontier models, including LLMs
- Keywords: LLM pre-training;MLLMs;multi-modality
- Source URL: https://openreview.net/forum?id=pfw176o1YJ
- PDF URL: https://openreview.net/pdf?id=pfw176o1YJ

## Abstract

Large Language Models (LLMs), despite being trained on text alone, surprisingly develop rich visual priors. These priors allow latent visual capabilities to be unlocked for vision tasks with a relatively small amount of multimodal data, and to perform symbolic visual generation tasks without ever having seen an image. Through systematic analysis, we reveal that visual priors—the implicit, emergent knowledge about the visual world acquired during language pre-training—are composed of separable perception and reasoning priors with unique scaling trends and origins. We show that an LLM's latent visual reasoning ability is predominantly developed by pre-training on reasoning-centric data (\eg, code, math, academia) and scales progressively. This reasoning prior acquired from language pre-training is transferable and universally applicable to visual reasoning. In contrast, the perception prior emerges more diffusely from broad corpora, and perception ability is more sensitive to the vision encoder and visual instruction tuning data. In parallel, text describing the visual world proves crucial, though its performance impact saturates rapidly. Leveraging these insights, we propose a data-centric recipe for pre-training vision-aware LLMs and verify it in 1T token scale pre-training.  Our findings are grounded in over 100 controlled experiments consuming 500,000 GPU-hours, spanning the full MLLM construction pipeline—from LLM pre-training to visual alignment and supervised multimodal fine-tuning—across five model scales, a wide range of data categories and mixtures, and multiple adaptation setups. Along with our main findings, we also propose and investigate several hypotheses, and introduce a Multi-Level Existence Bench (MLE-Bench) to facilitate future research. Together, this work provides a new way of deliberately cultivating visual priors from language pre-training, paving the way for the next generation of multimodal LLMs.

We recommend a visit to our anonymous project page (https://anonymouspaperweb.github.io/lsbs/) for an interactive reading.

## One-Sentence Claim

Text-only LLM pretraining builds separable visual reasoning and perception priors, and reasoning-centric text data is especially important for transferable visual reasoning in later MLLMs.

## Problem

MLLMs often acquire visual capabilities with relatively modest multimodal data, suggesting that text-only pretraining already encodes visual priors. But the origins, scaling behavior, and separability of those priors are unclear, making multimodal pretraining data choices hard to reason about.

## Core Contribution

The paper systematically decomposes LLM visual priors into perception and reasoning priors, identifies their different data origins and scaling trends, proposes a data-centric recipe for vision-aware LLM pretraining, and introduces MLE-Bench.

## Method

The authors run controlled experiments across the MLLM construction pipeline: text pretraining data mixtures, visual alignment, and supervised multimodal fine-tuning. They vary model scale, data category, and adaptation setup to test which text sources cultivate visual reasoning versus perception.

## Experiments and Evidence

The abstract reports more than 100 controlled experiments consuming 500,000 GPU-hours, across five model scales, plus a 1T-token pretraining verification. It finds that reasoning-centric data such as code, math, and academic text drives latent visual reasoning priors, while perception priors emerge more diffusely and depend more on the vision encoder and multimodal instruction data.

## Limits and Failure Modes

The separation between visual reasoning and perception priors may depend on benchmark design and probe tasks. Text describing visual content saturating quickly may not hold for specialized domains. Full-text review should check dataset taxonomies, MLE-Bench construction, adaptation setups, causal claims, and whether visual priors are measured independently of vision encoder quality.

## Deep Themes

- Text pretraining as multimodal prior formation.
- Separable perception and reasoning priors.
- Data-centric MLLM construction.
- Controlled pretraining studies at large scale.

## Subthemes

- Reasoning-centric text for visual reasoning.
- Visual-world descriptions and saturation.
- Vision encoder sensitivity.
- MLE-Bench.
- Symbolic visual generation without image exposure.

## Connections to Other Papers

Connects to Vid-LLM, PRISM, MASK, and multimodal reward/evaluation papers through cross-modal transfer, and to Common Corpus/data-recipe papers through the role of pretraining composition in downstream capabilities.

## Notes for Cross-Paper Synthesis

This paper strengthens the corpus theme that capabilities can be latent in pretraining data long before they are activated by modality-specific fine-tuning. Data mixture is an architectural choice in practice.
