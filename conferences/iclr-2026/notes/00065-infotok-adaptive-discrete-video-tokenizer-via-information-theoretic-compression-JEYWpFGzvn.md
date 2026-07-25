# InfoTok: Adaptive Discrete Video Tokenizer via Information-Theoretic Compression

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: JEYWpFGzvn
- Authors: Haotian Ye; Qiyuan He; Jiaqi Han; Puheng Li; Jiaojiao Fan; Zekun Hao; Fitsum Reda; Yogesh Balaji; Huayu Chen; Sheng Liu; Angela Yao; James Zou; Stefano Ermon; Haoxiang Wang; Ming-Yu Liu
- Primary area: learning theory
- Keywords: discrete tokenization;video representation;eficiency;information theory
- Source URL: https://openreview.net/forum?id=JEYWpFGzvn
- PDF URL: https://openreview.net/pdf?id=JEYWpFGzvn

## Abstract

Accurate and efficient discrete video tokenization is essential for long video sequences processing. Yet, the inherent complexity and variable information density of videos present a significant bottleneck for current tokenizers, which rigidly compress all content at a fixed rate, leading to redundancy or information loss. Drawing inspiration from Shannon's information theory, this paper introduces \alg, a principled framework for adaptive video tokenization. We rigorously prove that existing data-agnostic training methods are suboptimal in representation length, and present a novel evidence lower bound (ELBO)-based algorithm that approaches theoretical optimality. Leveraging this framework, we develop a transformer-based adaptive compressor that enables adaptive tokenization. Empirical results demonstrate state-of-the-art compression performance, saving $20\%$ tokens without influence on performance, and achieving $2.3\times$ compression rates while still outperforming prior heuristic adaptive approaches. By allocating tokens according to informational richness, \alg enables a more compressed yet accurate tokenization for video representation, offering valuable insights for future research.

## One-Sentence Claim

InfoTok adaptively allocates discrete video tokens according to information density, reducing redundancy and approaching information-theoretic optimal compression.

## Problem

Long video processing depends on efficient discrete tokenization. Fixed-rate tokenizers compress all content equally, even though videos have variable information density.

This creates either redundant tokens in simple regions or information loss in complex regions.

## Core Contribution

The paper introduces InfoTok, an information-theoretic framework for adaptive video tokenization.

It proves data-agnostic training methods are suboptimal in representation length and presents an ELBO-based algorithm that approaches theoretical optimality. It also builds a transformer-based adaptive compressor.

## Method

InfoTok formulates token allocation as an information-theoretic compression problem. The ELBO-based algorithm learns to assign more tokens to information-rich content and fewer to redundant content.

The transformer adaptive compressor implements this allocation for discrete video representation.

## Experiments and Evidence

The abstract reports state-of-the-art compression performance.

InfoTok saves 20 percent of tokens without affecting performance and achieves 2.3x compression while outperforming prior heuristic adaptive approaches.

## Limits and Failure Modes

Information density estimates may miss semantically important but visually subtle events. Adaptive token allocation can also complicate downstream models that expect fixed token grids.

Because this note is abstract-only, details still need checking: theoretical optimality statement, ELBO objective, tokenizer architecture, video benchmarks, downstream tasks, and failure modes on rare events.

## Deep Themes

- Information-aware tokenization: token budgets should follow content complexity.
- Adaptive compression for long video: fixed rates waste capacity or lose information.
- Theory-guided representation length: tokenization can be optimized with information-theoretic objectives.
- Efficient video foundation infrastructure: better tokenizers enable longer and cheaper video modeling.

## Subthemes

- Discrete video tokens.
- ELBO-based adaptive compression.
- Variable information density.
- Transformer adaptive compressor.

## Connections to Other Papers

This connects to FlashVID, EntroKV, ThinkV, and Beyond Language Modeling through adaptive token/inference efficiency.

It also relates to VibeVoice because both use efficient tokenization to make long-form generation or processing feasible.

## Notes for Cross-Paper Synthesis

InfoTok reinforces the information-adaptive compression theme: efficient multimodal models allocate representation length where the signal actually is.
