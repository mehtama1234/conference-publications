# MetaEmbed: Scaling Multimodal Retrieval at Test-Time with Flexible Late Interaction

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: yKDqg9HwZX
- Authors: Zilin Xiao; Qi Ma; Mengting Gu; Chun-cheng Jason Chen; Xintao Chen; Vicente Ordonez; Vijai Mohan
- Primary area: applications to computer vision, audio, language, and other modalities
- Keywords: multimodal retrieval;information retrieval
- Source URL: https://openreview.net/forum?id=yKDqg9HwZX
- PDF URL: https://openreview.net/pdf?id=yKDqg9HwZX

## Abstract

Universal multimodal embedding models have achieved great success in capturing semantic relevance between queries and candidates. However, current methods either condense queries and candidates into a single vector, potentially limiting the expressiveness for fine-grained information, or produce too many vectors that are prohibitively expensive for multi-vector retrieval. In this work, we introduce MetaEmbed, a new framework for multimodal retrieval that rethinks how multimodal embeddings are constructed and interacted with at scale. During training, a fixed number of learnable Meta Tokens are appended to the input sequence. At test-time, their last-layer contextualized representations serve as compact yet expressive multi-vector embeddings. Through the proposed Matryoshka Multi-Vector Retrieval training, MetaEmbed learns to organize information by granularity across multiple vectors. As a result, we enable test-time scaling in multimodal retrieval where users can balance retrieval quality against efficiency demands by selecting the number of tokens used for indexing and retrieval interactions. Extensive evaluations on the Massive Multimodal Embedding Benchmark (MMEB) and the Visual Document Retrieval Benchmark (ViDoRe) confirm that MetaEmbed achieves state-of-the-art retrieval performance while scaling robustly to models with 32B parameters. Code is available at https://github.com/facebookresearch/MetaEmbed.

## One-Sentence Claim

MetaEmbed enables test-time scaling for multimodal retrieval by using compact meta-token multi-vector embeddings whose number can be selected to trade retrieval quality against efficiency.

## Problem

Single-vector multimodal embeddings can be too compressed for fine-grained retrieval, while dense multi-vector representations can be too expensive for indexing and retrieval. Users need a retrieval representation that can scale quality and cost at test time.

## Core Contribution

The paper contributes MetaEmbed, which appends a fixed number of learnable Meta Tokens during training and uses their last-layer contextualized representations as compact multi-vector embeddings at test time. Matryoshka Multi-Vector Retrieval training organizes information by granularity across vectors.

## Method

Meta Tokens are appended to multimodal inputs, producing contextualized vectors that summarize information at multiple granularities. At indexing or retrieval time, users choose how many vectors participate in late interaction, allowing flexible computation/quality tradeoffs without retraining separate embedding models.

## Experiments and Evidence

The abstract reports state-of-the-art performance on the Massive Multimodal Embedding Benchmark and the Visual Document Retrieval Benchmark, with robust scaling to 32B-parameter models. It also states code is available at the MetaEmbed GitHub repository.

## Limits and Failure Modes

This note is abstract/metadata-only. Full-text review should inspect storage overhead, latency, token-count tradeoff curves, indexing implementation, benchmark task mix, and whether gains persist for out-of-domain visual documents or long-tail queries. Late interaction can improve quality while complicating serving infrastructure.

## Deep Themes

- Test-time scalable retrieval.
- Compact multi-vector multimodal embeddings.
- Granularity-aware representation learning.
- Efficiency-quality controls.

## Subthemes

- Meta Tokens.
- Matryoshka Multi-Vector Retrieval.
- Late interaction.
- MMEB.
- ViDoRe.

## Connections to Other Papers

Connects to Tool-Augmented SSMs and Visual Planning through test-time control of intermediate representations, to MotionStream through fixed-resource long-horizon efficiency, and to broader retrieval/RAG notes where embedding compression determines downstream quality.

## Notes for Cross-Paper Synthesis

MetaEmbed makes representation granularity a user-controllable test-time knob. The pattern matches other 2026 work that exposes latent compute/quality tradeoffs instead of hiding them inside a fixed representation.
