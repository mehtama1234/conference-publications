# FedPissa: Towards Federated Personalized Adaptation of Foundation Models via LoRA Subspace Mapping

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: ZEWN40uNEh
- Authors: Wenwen He; Wenke Huang; Yi Liu; Jian Liang; Xirui Li; Guansong Pang; Mang Ye
- Primary area: deep_learning->large_language_models
- Keywords: Federated Personalized Learning
- Source URL: https://openreview.net/forum?id=ZEWN40uNEh
- PDF URL: https://openreview.net/pdf?id=ZEWN40uNEh

## Abstract

LoRA efficiently adapts large pre-trained models via low-rank updates, making it a strong parameter-efficient fine-tuning (PEFT) method. When integrated with Federated Learning (FL), it enables collaborative fine-tuning across distributed clients, leveraging rich downstream data without exposing private information. However, this strategy is hindered by data heterogeneity and limits personalization performance. To address this, personalized FedLoRA approaches have been proposed and employ a dual-LoRA architecture, e.g., one branch for global knowledge and another for client-specific adaptation. Nevertheless, this dual-LoRA design introduces additional computational overhead and structural redundancy. To address this limitation, we propose FedPissa, the first framework that rethinks single-LoRA via selective aggregation and subspace decorrelation. We selectively aggregate LoRA components based on their aggregation dynamics, and further apply a decorrelated subspace projection to mitigate heterogeneous update conflicts, reducing cross-client interference and improving personalized adaptation. Experiments on texual and visual scenario show that FedPissa not only achieves up to 35\% lower communication and computation cost, but also improves superior compared to counterparts.

## One-Sentence Claim

FedPissa personalizes federated LoRA by selectively aggregating single-LoRA components and decorrelating subspaces to reduce heterogeneous client interference without dual-LoRA redundancy.

## Problem

Federated LoRA enables collaborative adaptation of foundation models without centralizing private client data. But data heterogeneity harms personalization, and dual-LoRA personalized approaches add compute, communication, and structural redundancy by maintaining separate global and client-specific branches.

The paper asks whether a single-LoRA design can support personalization efficiently.

## Core Contribution

FedPissa rethinks single-LoRA federated adaptation through selective aggregation and subspace decorrelation. It aggregates LoRA components based on their aggregation dynamics and applies decorrelated subspace projection to mitigate conflicts among heterogeneous client updates.

The claimed result is improved personalized adaptation with up to 35 percent lower communication and computation cost across textual and visual scenarios.

## Method

The method monitors LoRA component aggregation dynamics to decide which components should be shared globally. It then projects updates into decorrelated subspaces to reduce cross-client interference.

This keeps one LoRA branch while trying to separate global knowledge from client-specific variation implicitly in subspace geometry.

## Experiments and Evidence

Evidence reported in the abstract:

- First framework framed around single-LoRA selective aggregation and subspace decorrelation for personalized federated foundation-model adaptation.
- Textual and visual scenario experiments.
- Up to 35 percent lower communication and computation cost.
- Better personalization performance than counterparts.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: client heterogeneity settings, model families, LoRA rank, aggregation rule, and privacy/security guarantees.

## Limits and Failure Modes

- Federated learning still risks update leakage unless privacy mechanisms are added.
- Selective aggregation may fail under extreme non-IID clients.
- Subspace decorrelation depends on stable estimation of update conflicts.
- Reported cost savings need breakdown between communication, computation, and memory.

## Deep Themes

**Personalization can be subspace geometry.** FedPissa avoids separate adapters by separating update directions.

**Federated adaptation needs conflict control.** Client heterogeneity is managed through aggregation dynamics and decorrelation.

**Efficiency and privacy constraints shape PEFT design.** Single-LoRA personalization reduces overhead while keeping data distributed.

## Subthemes

- Federated LoRA.
- Personalized foundation-model adaptation.
- Selective component aggregation.
- Decorrelated subspace projection.
- Heterogeneous client update conflicts.

## Connections to Other Papers

Connects to PRISM, GR-LoRA, SmartFed, Diffract, and low-rank adaptation papers. It also links to data governance and privacy work because distributed data access changes both incentives and update geometry.

## Notes for Cross-Paper Synthesis

FedPissa adds to the low-rank geometry theme: personalization, privacy, and efficiency are increasingly handled by choosing which update subspaces should be shared, separated, or noised.
