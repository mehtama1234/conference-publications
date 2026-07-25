# Revela: Dense Retriever Learning via Language Modeling

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: e7pAjJZJWb
- Authors: Fengyu Cai; Tong Chen; Xinran Zhao; Sihao Chen; Hongming Zhang; Tongshuang Wu; Iryna Gurevych; Heinz Koeppl
- Primary area: unsupervised, self-supervised, semi-supervised, and supervised representation learning
- Keywords: Information Retrieval;Unsupervised Learning
- Source URL: https://openreview.net/forum?id=e7pAjJZJWb
- PDF URL: https://openreview.net/pdf?id=e7pAjJZJWb

## Abstract

Dense retrievers play a vital role in accessing external and specialized knowledge to augment language models (LMs). Training dense retrievers typically requires annotated query-document pairs, which are costly to create and scarce in specialized domains (e.g., code) or in complex settings (e.g., requiring reasoning). These practical challenges have sparked growing interest in self-supervised retriever learning.
Since LMs are trained to capture token-level dependencies through a self-supervised learning objective (i.e., next token prediction), we can analogously cast retrieval as learning dependencies among chunks of tokens. This analogy naturally leads to the question: How can we adapt self‑supervised learning objectives in the spirit of language modeling to train retrievers?

To answer this question, we introduce Revela, a unified and scalable training framework for self-supervised retriever learning via language modeling. Revela models semantic dependencies among documents by conditioning next token prediction on local and cross-document context through an in-batch attention mechanism. This attention is weighted by retriever-computed similarity scores, enabling the retriever to be optimized as part of language modeling. We evaluate Revela on domain-specific (CoIR), reasoning-intensive (BRIGHT), and general-domain (BEIR) benchmarks across various retriever backbones. Without annotated or synthetic query-document pairs, Revela surpasses larger supervised models and proprietary APIs on both CoIR and BRIGHT. It achieves BEIR's unsupervised SoTA with ~1000x less training data and 10x less compute. Performance increases with batch size and model size, highlighting Revela's scalability and its promise for self‑supervised retriever learning.

## One-Sentence Claim

Revela trains dense retrievers self-supervised by making retriever-weighted cross-document context useful for language-model next-token prediction.

## Problem

Dense retrievers are central for giving LMs access to external and specialized knowledge, but supervised query-document pairs are costly and scarce in code, specialized domains, and reasoning-heavy retrieval.

Self-supervised retriever learning needs an objective analogous to language modeling, but operating over dependencies among chunks and documents.

## Core Contribution

The paper introduces Revela, a scalable framework for self-supervised dense retriever learning via language modeling.

It models semantic dependencies among documents by conditioning next-token prediction on local and cross-document context weighted by retriever-computed similarities.

## Method

Revela uses in-batch attention over document chunks. Retriever similarity scores weight cross-document context, and the language-modeling loss optimizes the retriever because useful retrieved context improves next-token prediction.

This removes the need for annotated or synthetic query-document pairs.

## Experiments and Evidence

The abstract reports evaluations on CoIR, BRIGHT, and BEIR across multiple retriever backbones.

Without annotated or synthetic pairs, Revela beats larger supervised models and proprietary APIs on CoIR and BRIGHT, reaches unsupervised state of the art on BEIR with about 1000x less training data and 10x less compute, and scales with batch and model size.

## Limits and Failure Modes

Language-modeling usefulness may not perfectly align with downstream retrieval relevance, especially for factual QA, multi-hop reasoning, or adversarial search. Large batch scaling can also be infrastructure-heavy.

Because this note is abstract-only, details still need checking: in-batch attention implementation, retriever backbones, training corpus, benchmark protocols, compute accounting, and failure cases.

## Deep Themes

- Retrieval as language modeling: document dependencies become a self-supervised signal.
- Pair-free retriever training: useful retrieval can emerge without labeled or synthetic query pairs.
- Cross-document context as supervision: the retriever is rewarded when selected chunks improve token prediction.
- Scalable unsupervised retrieval: performance improves with batch size and model size.

## Subthemes

- Dense retrieval.
- Self-supervised learning.
- In-batch attention.
- CoIR, BRIGHT, and BEIR.

## Connections to Other Papers

This connects to Q-RAG, MC-Search, AstaBench, WAVE, and retrieval/information-access themes.

It also relates to Train-before-Test because both turn adaptation/training setup into the lens for measuring model potential.

## Notes for Cross-Paper Synthesis

Revela adds a retrieval-pretraining theme: access models can be trained from the same self-supervised principles as language models when retrieval is framed as cross-document dependency modeling.
