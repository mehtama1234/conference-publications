# Don't Reinvent the Wheel, Just Realign the Spokes: Resource-Efficient Federated Fine-Tuning via Rank-Wise Expert Assembly

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: HdsEUNo4C4
- Authors: Yebo Wu; Jingguang Li; Zhijiang Guo; Li Li
- Primary area: general_machine_learning->transfer_multitask_and_metalearning
- Keywords: Knowledge Transfer;Large Language Models;Mixture of Experts
- Source URL: https://openreview.net/forum?id=HdsEUNo4C4
- PDF URL: https://openreview.net/pdf?id=HdsEUNo4C4

## Abstract

Federated fine-tuning presents a promising avenue for adapting Large Language Models (LLMs) to downstream tasks while preserving data privacy. However, the prohibitive computational and communication overhead of LLM adaptation inhibits its deployment on resource-constrained edge devices. In this paper, we propose SmartFed, a resource-efficient framework that circumvents expensive training from scratch by intelligently reusing knowledge embedded in existing LoRA modules. To fully exploit this potential and ensure scalability, we introduce the Mixture of Rank-Wise Experts (MoRE). MoRE decomposes LoRA modules into fine-grained rank-level experts, which are selectively activated based on input semantics and resource budgets. Furthermore, to optimize resource utilization, we propose Elastic Expert Quota Allocation (EEQA), a strategy that adaptively distributes expert capacity across parameter matrices based on their contribution to model performance. Extensive evaluations across multiple benchmarks demonstrate that SmartFed significantly outperforms state-of-the-art methods in both model performance and training efficiency. Our code is publicly available at https://github.com/benmagnifico/SmartFed.

## One-Sentence Claim

SmartFed reuses existing LoRA modules as rank-wise experts to make federated LLM fine-tuning more efficient under edge-device resource limits.

## Problem

Federated LLM adaptation promises privacy-preserving personalization, but conventional fine-tuning imposes computational and communication costs that are impractical for constrained clients.

## Core Contribution

The paper introduces Mixture of Rank-Wise Experts, which decomposes LoRA modules into fine-grained rank-level experts, and Elastic Expert Quota Allocation, which distributes capacity according to parameter-matrix contribution.

## Method

SmartFed selectively activates rank-level LoRA experts based on input semantics and resource budgets, then adaptively assigns expert quota across matrices to improve resource utilization. The design avoids training from scratch by assembling knowledge already embedded in LoRA modules.

## Experiments and Evidence

The abstract reports extensive benchmark evaluations where SmartFed improves both model performance and training efficiency over state-of-the-art federated fine-tuning methods.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: benchmark suite, client heterogeneity, communication accounting, privacy guarantees, LoRA source assumptions, and overhead of input-conditioned expert selection.

## Deep Themes

- Modular reuse as an alternative to full federated retraining.
- Resource budgets as routing constraints.
- Fine-grained adapter decomposition for privacy-preserving personalization.

## Subthemes

- Federated fine-tuning.
- LoRA modules.
- Mixture of Experts.
- Edge deployment.
- Communication efficiency.
- Rank-wise adaptation.

## Connections to Other Papers

Connects to FlatLand through federated personalization and to SSMoE through expert selection without monolithic retraining. It also links to efficiency-as-capability papers that adapt fixed resources through smarter assembly.

## Notes for Cross-Paper Synthesis

SmartFed adds an adapter-level version of the anti-retraining theme: existing modules can be decomposed and recombined under semantic and resource constraints instead of updating an entire LLM.
