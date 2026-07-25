# Reassessing Layer Pruning in LLMs: New Insights and Methods

## Metadata

- Conference: iclr-2026
- Status: Poster
- OpenReview ID: 04Tfwy3LLC
- Authors: Yao Lu; Hao Cheng; Yujie Fang; Zeyu Wang; Jiaheng Wei; Dongwei Xu; Qi Xuan; Zhaowei Zhu
- Primary area: foundation or frontier models, including LLMs
- Keywords: Large Language Model;Layer Pruning;Model Compression
- Source URL: https://openreview.net/forum?id=04Tfwy3LLC
- PDF URL: https://openreview.net/pdf?id=04Tfwy3LLC

## Abstract

Although large language models (LLMs) have achieved remarkable success across various domains, their considerable scale necessitates substantial computational resources, posing significant challenges for deployment in resource-constrained environments. Layer pruning, as a simple yet effective compression method, removes layers of a model directly, reducing computational overhead. However, what are the best practices for layer pruning in LLMs? Are sophisticated layer selection metrics truly effective? Does the LoRA (Low-Rank Approximation) family, widely regarded as a leading method for pruned model fine-tuning, truly meet expectations when applied to post-pruning fine-tuning? To answer these questions, we dedicate thousands of GPU hours to benchmarking layer pruning in LLMs and gaining insights across multiple dimensions. Our results demonstrate that a simple approach, i.e., pruning the final layers followed by fine-tuning the lm\_head and the remaining last three layers, yields remarkably strong performance. These pruning strategies are further supported by theoretical analyses based on the gradient flow. Following this guide, our method surpasses existing state-of-the-art pruning methods by $5.62\%$–$17.27\%$ on Llama-3.1-8B-It, by $2.36\%$–$19.45\%$ on Llama-3-8B and by $4.34\%$–$9.59\%$ on Llama-3-70B. The code is available at at https://github.com/yaolu-zjut/Navigation_LLM_layer_pruning.

## One-Sentence Claim

A large benchmark of LLM layer pruning finds that simple final-layer pruning plus targeted fine-tuning can beat more sophisticated selection metrics and LoRA-style recovery strategies.

## Problem

LLMs are expensive to deploy, and layer pruning is a direct compression method, but best practices are unclear. The field needs evidence on whether complex layer-selection criteria help and whether common post-pruning LoRA-family fine-tuning is actually the best recovery strategy.

## Core Contribution

The paper contributes a large empirical reassessment of LLM layer pruning backed by gradient-flow theory. It identifies a simple recipe: prune final layers, then fine-tune the language-model head and remaining last three layers.

## Method

The study benchmarks layer-pruning choices over thousands of GPU hours, comparing layer selection metrics and post-pruning fine-tuning strategies. The recommended method removes final layers and applies focused fine-tuning to the output head plus the last three retained layers, with theoretical support from gradient-flow analysis.

## Experiments and Evidence

The abstract reports improvements over prior pruning methods by 5.62%-17.27% on Llama-3.1-8B-It, 2.36%-19.45% on Llama-3-8B, and 4.34%-9.59% on Llama-3-70B. Code is reported available at the listed GitHub repository.

## Limits and Failure Modes

This note is abstract/metadata-only. Full-text review should inspect task suites, pruning ratios, fine-tuning budgets, baseline fairness, latency/memory gains, and whether final-layer pruning holds for reasoning-heavy, multilingual, coding, or long-context tasks. Simple recipes can overfit to the evaluated model families.

## Deep Themes

- Empirical reassessment of compression folklore.
- Layer pruning for deployable LLMs.
- Simple baselines beating sophisticated heuristics.
- Gradient-flow explanation of pruning recovery.

## Subthemes

- Final-layer pruning.
- Post-pruning fine-tuning.
- Llama-3 family.
- LoRA-family limitations.
- Resource-constrained deployment.

## Connections to Other Papers

Connects to PGM, Polar Express, and MotionStream through efficiency as a capability enabler, and to Capacity Manipulation through low-rank or capacity-allocation interventions that reshape how model resources are used.

## Notes for Cross-Paper Synthesis

This paper is another case where careful benchmarking overturns method complexity. The corpus pattern is that deployment efficiency often depends on identifying which simple intervention preserves the most useful computation.
