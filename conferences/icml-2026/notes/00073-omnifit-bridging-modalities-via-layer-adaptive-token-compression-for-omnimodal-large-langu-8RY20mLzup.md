# OmniFit: Bridging Modalities via Layer-Adaptive Token Compression for Omnimodal Large Language Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 8RY20mLzup
- Authors: Zining Wang; Zhihang Yuan; Yingjie Zhai; Wenshuo Li; Han Shu; Ruihao Gong; Jinyang Guo; Xianglong Liu
- Primary area: deep_learning->large_language_models
- Keywords: LLMs;token reduction;model efficiency
- Source URL: https://openreview.net/forum?id=8RY20mLzup
- PDF URL: https://openreview.net/pdf?id=8RY20mLzup

## Abstract

Emerging Omni-modal Large Language Models (OmniLLMs) enable real-time interaction across video, audio, and text but suffer from prohibitive computational costs due to the quadratic complexity of processing continuous streaming inputs. Existing token compression strategies remain suboptimal as they typically rely on biased modality-centric priors or enforce uniform retention policies, neglecting the heterogeneity across layers and the critical role of cross-modality alignment. To address these challenges, we propose OmniFit, a training-free framework that decouples interaction profiling from inference execution. OmniFit incorporates Layer-Adaptive Heterogeneity Profiling (LAHP) to dynamically allocate computational budgets based on layer-wise redundancy and modality preferences, preserving tokens according to the characteristics of each layer. Furthermore, we introduce Alignment-Rectified Token Selection (ARTS), a lightweight mechanism that efficiently identifies tokens semantically aligned with cross-modal cues. Extensive experiments on 3 model series across 10 benchmarks demonstrate that OmniFit establishes a new Pareto frontier, retaining 98\% of model performance with only 20\% token usage and achieves up to 2.31$\times$ end-to-end inference speedup and 2.5$\times$ VRAM saving, significantly outperforming state-of-the-art methods.

## One-Sentence Claim

OmniFit accelerates omnimodal LLMs by applying training-free, layer-adaptive token compression that preserves cross-modal alignment.

## Problem

Streaming video, audio, and text inputs create prohibitive quadratic token-processing cost, while existing compression methods often impose uniform retention or modality-biased priors.

## Core Contribution

The paper proposes OmniFit, a training-free framework combining Layer-Adaptive Heterogeneity Profiling with Alignment-Rectified Token Selection for omnimodal token reduction.

## Method

OmniFit profiles layer-wise redundancy and modality preferences separately from inference execution, then dynamically allocates token budgets by layer. ARTS selects tokens that remain semantically aligned with cross-modal cues.

## Experiments and Evidence

The abstract reports experiments on 3 model series and 10 benchmarks, retaining 98% of performance with 20% token usage while achieving up to 2.31x end-to-end inference speedup and 2.5x VRAM savings.

## Limits and Failure Modes

ArXiv search failed with rate-limit/service errors for this batch, so this note is abstract-only. Details still need checking: profiling cost, supported OmniLLM architectures, streaming latency behavior, and alignment-selection failure cases.

## Deep Themes

- Token compression must respect modality and layer heterogeneity.
- Efficiency work is shifting toward alignment-preserving reduction, not blind sparsification.
- Streaming multimodal systems make context cost a deployment bottleneck.

## Subthemes

- Omnimodal LLMs.
- Layer-adaptive token compression.
- Cross-modal alignment.
- Training-free acceleration.
- Streaming inputs.
- VRAM reduction.

## Connections to Other Papers

Connects to TACO, EcoVLA, LiftQuant, and TetraJet-v2 through runtime efficiency. It also links to multimodal evaluation papers because compression must preserve cross-modal semantics, not just aggregate accuracy.

## Notes for Cross-Paper Synthesis

OmniFit extends the adaptive-efficiency theme: the unit of compression is increasingly selected by semantic role, layer behavior, and modality alignment.
