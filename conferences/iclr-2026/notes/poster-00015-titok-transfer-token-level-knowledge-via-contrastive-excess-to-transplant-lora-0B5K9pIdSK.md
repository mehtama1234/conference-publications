# TiTok: Transfer Token-level Knowledge via Contrastive Excess to Transplant LoRA

## Metadata

- Conference: iclr-2026
- Status: Poster
- OpenReview ID: 0B5K9pIdSK
- Authors: ChanJoo Jung; Jaehyung Kim
- Primary area: foundation or frontier models, including LLMs
- Keywords: Large Language Models;Knowledge Transfer;PEFT
- Source URL: https://openreview.net/forum?id=0B5K9pIdSK
- PDF URL: https://openreview.net/pdf?id=0B5K9pIdSK

## Abstract

Large Language Models (LLMs) are widely applied in real world scenarios, but fine-tuning them comes with significant computational and storage costs. Parameter-Efficient Fine-Tuning (PEFT) methods such as LoRA mitigate these costs, but the adapted parameters are dependent on the base model and cannot be transferred across different backbones. One way to address this issue is through knowledge distillation, but its effectiveness inherently depends on training data. Recent work such as TransLoRA avoids this by generating synthetic data, but this adds complexity because it requires training an additional discriminator model. In this paper, we propose TiTok, a new framework that enables effective LoRA Transplantation through Token-level knowledge transfer. Specifically, TiTok captures task-relevant information through a token-wise contrastive excess between a source model with and without LoRA. This excess highlights informative tokens and enables selective filtering of synthetic data, all without additional models or overhead. Through experiments on three benchmarks across multiple transfer settings, our experiments show that TiTok is consistently effective, achieving average performance gains of +4–8% compared to baselines overall.

## One-Sentence Claim

TiTok transfers LoRA adaptations across LLM backbones by using token-level contrastive excess to identify task-relevant synthetic data without training an extra discriminator.

## Problem

LoRA and other PEFT methods reduce fine-tuning cost, but their learned adapters are tied to a specific base model and usually cannot be moved across backbones. Distillation can transfer behavior but depends heavily on data, and synthetic-data approaches may add extra model-training complexity.

## Core Contribution

The paper introduces TiTok, a LoRA transplantation framework based on token-level knowledge transfer. It measures the token-wise contrastive excess between a source model with and without LoRA, using that signal to identify informative tokens and filter synthetic data without additional models or overhead.

## Method

TiTok compares token-level behavior of the source base model and its LoRA-adapted version. Tokens with high contrastive excess indicate task-relevant adaptation knowledge. This signal guides selective synthetic-data filtering for transferring the adaptation to a different backbone.

## Experiments and Evidence

The abstract reports experiments on three benchmarks across multiple transfer settings. TiTok consistently improves over baselines, with average gains of 4-8% overall.

## Limits and Failure Modes

This note is abstract/metadata-only. Full-text review should inspect backbone pairs, task types, synthetic-data generation process, contrastive-excess definition, and whether transfer works across major tokenizer, architecture, and scale differences. Token-level signals may miss global style or reasoning behaviors not localized to obvious tokens.

## Deep Themes

- Transferable parameter-efficient fine-tuning.
- Token-level adaptation diagnostics.
- Synthetic data filtering without extra discriminators.
- Adapter portability across backbones.

## Subthemes

- TiTok.
- LoRA transplantation.
- Contrastive excess.
- PEFT knowledge transfer.
- Source adapted versus source base comparison.

## Connections to Other Papers

Connects to layer pruning and Polar Express through deployment-efficiency infrastructure, to COMPACT through synthetic data filtering for data efficiency, and to WIMHF through feature-level identification of behavior-driving examples.

## Notes for Cross-Paper Synthesis

TiTok turns model adaptation into a diagnostic contrast: what changed token by token after LoRA? The broader pattern is that transferable efficiency depends on isolating the small behavioral signal that actually encodes task knowledge.
