# LiME: Lightweight Mixture of Experts for Efficient Multimodal Multi-task Learning

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: KRSZj8z5Lr
- Authors: Md Kowsher; Haris Mansoor; Nusrat Jahan Prottasha; Ozlem Garibay; Victor Zhu; Zhengping Ji; Chen Chen
- Primary area: deep_learning->large_language_models
- Keywords: Mixture of Experts;Parameter-Efficient Fine-Tuning;Zero-Parameter Routing;Multi-Task Learning;Expert Modulation;Multimodal Learning;Lightweight Models;PEFT
- Source URL: https://openreview.net/forum?id=KRSZj8z5Lr
- PDF URL: https://openreview.net/pdf?id=KRSZj8z5Lr

## Abstract

MoE-PEFT methods combine Mixture of Experts with parameter-efficient fine-tuning for multi-task adaptation, but require separate adapters per expert—causing trainable parameters to scale linearly with expert count and limiting applicability to adapter-based architectures. We propose LiME (Lightweight Mixture of Experts), which achieves expert specialization through lightweight modulation rather than adapter replication. Instead of separate adapters, LiME uses a single shared PEFT module and modulates its output with lightweight expert vectors, reducing expert parameters while generalizing to any PEFT method. Notably, LiME introduces zero-parameter routing by leveraging existing frozen and adapted representations—eliminating learned router parameters typically required per layer. Theoretically, we prove that (i) more experts preserve more task-relevant information and (ii) modulation approximates full expert-specific PEFT with bounded error. LiME further incorporates n-gram windowed routing and adaptive expert selection (Auto Top-K) based on routing confidence. Experiments on MMT-47, a multimodal multi-task benchmark with 47 tasks spanning text, image, and video, demonstrate that LiME achieves competitive or superior performance while using up to 4× fewer trainable parameters and up to 29% faster training compared to corresponding MoE-PEFT baselines.

## One-Sentence Claim

LiME achieves efficient multimodal multi-task adaptation by using one shared PEFT module modulated by lightweight expert vectors and zero-parameter routing.

## Problem

MoE-PEFT methods usually replicate adapters per expert, causing trainable parameters to grow linearly with expert count and tying the approach to adapter-specific architectures.

## Core Contribution

The paper proposes lightweight expert modulation instead of adapter replication, proves modulation approximates full expert-specific PEFT with bounded error, and introduces routing methods that use existing frozen/adapted representations.

## Method

LiME uses a shared PEFT module whose output is modulated by expert vectors, leverages zero-parameter routing from existing representations, applies n-gram windowed routing, and selects Auto Top-K experts based on routing confidence.

## Experiments and Evidence

The abstract reports competitive or superior performance on MMT-47, a 47-task multimodal benchmark spanning text, image, and video, with up to 4x fewer trainable parameters and 29% faster training than MoE-PEFT baselines.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: backbone models, PEFT methods tested, expert counts, routing confidence calibration, task imbalance, and whether zero-parameter routing remains stable under distribution shift.

## Deep Themes

- Expert specialization need not require adapter replication.
- Frozen representations can route tasks without learned router parameters.
- Parameter efficiency and multitask flexibility can reinforce each other.

## Subthemes

- Mixture of Experts.
- PEFT.
- Multimodal multi-task learning.
- Zero-parameter routing.
- Expert modulation.
- Adaptive Top-K selection.

## Connections to Other Papers

Connects to SSMoE, SmartFed, and M-CBE through expert modularity and to multimodal adaptation papers through efficient task-specific routing.

## Notes for Cross-Paper Synthesis

LiME adds another anti-replication design pattern: keep a shared adaptable core, then specialize with cheap modulation and routing rather than full expert copies.
