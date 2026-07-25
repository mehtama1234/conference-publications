# Expressivity-Efficiency Tradeoffs for Hybrid Sequence Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 82EJxJzG6r
- Authors: John Cooper; Ilias Diakonikolas; Mingchen Ma; Frederic Sala
- Primary area: general_machine_learning
- Keywords: hybrid models;expressivity;model efficiency
- Source URL: https://openreview.net/forum?id=82EJxJzG6r
- PDF URL: https://openreview.net/pdf?id=82EJxJzG6r

## Abstract

Hybrid sequence models—combining Transformer and state-space model layers—seek to gain the expressive versatility of attention as well as the computational efficiency of state-space model layers. Despite burgeoning interest in hybrid models, we lack a basic understanding of the settings where—and underlying mechanisms through which—they offer benefits over their constituent models. In this paper, we study this question, focusing on a broad family of core synthetic tasks. For this family of tasks, we prove the existence of fundamental limitations for non-hybrid models. Specifically, any Transformer or state-space model that solves the underlying task requires either a large number of parameters or a large working memory. On the other hand, for two prototypical tasks within this family—namely selective copying and associative recall—we construct hybrid models of small size and working memory that provably solve these tasks, thus achieving the best of both worlds. Our experimental evaluation empirically validates our theoretical findings. Importantly, going beyond the settings in our theoretical analysis, we empirically show that learned—rather than constructed—hybrids outperform non-hybrid models with up to $6 \times$ as many parameters. We additionally demonstrate that hybrid models exhibit stronger length generalization and out-of-distribution robustness than non-hybrids.

## One-Sentence Claim

Hybrid sequence models can provably solve some synthetic sequence tasks with fewer parameters and less working memory than pure Transformer or pure SSM architectures.

## Problem

Hybrid Transformer/SSM models are empirically popular, but it is unclear when the mixture gives real advantages over its components rather than just engineering convenience.

## Core Contribution

The paper identifies task families where pure Transformers or pure SSMs face fundamental parameter or memory lower bounds, then constructs small hybrid models that avoid both bottlenecks.

## Method

The theoretical analysis studies function-composition sequence tasks and proves limitations for non-hybrid architectures under input-independent memory and working-memory measures. It then constructs shallow hybrids combining Mamba-style SSM layers with attention layers for selective copying and associative recall with decoding.

## Experiments and Evidence

The abstract reports empirical validation on synthetic tasks, with learned hybrids outperforming non-hybrid models with up to 6x as many parameters, stronger length generalization, and better out-of-distribution robustness.

## Full-Text Upgrade

The full text makes the tradeoff precise: pure SSMs can require parameter counts scaling with task size, while pure Transformers can require working memory scaling with context length. For selective copying, the paper constructs a two-layer Mamba-plus-attention hybrid with polylogarithmic model size and much smaller working memory. For associative recall with decoding, it constructs a three-layer hybrid with one Mamba layer and two attention layers.

Empirically, the full text extends beyond the constructed setting to multi-key associative recall and needle-in-a-haystack variants. It reports that hybrids can match or beat pure models with roughly 6x fewer parameters and can outperform pure Transformers by around 10% on longer sequences after training on short examples, with some OOD tests showing over 15% higher performance than either pure baseline.

## Limits and Failure Modes

Limits to watch: the strongest theory applies to stylized synthetic tasks; practical hybrid gains depend on layer allocation and training recipe; and the paper does not by itself prove that every real long-context workload has the same separable memory/parameter structure.

## Deep Themes

- Architectural mixtures can be theoretically justified by separating memory roles.
- Efficiency is not only fewer FLOPs; it is matching architecture to task structure.
- Hybrid models may encode different algorithmic primitives in different layers.

## Subthemes

- Transformer/SSM hybrids.
- Expressivity-efficiency tradeoffs.
- Working memory lower bounds.
- Selective copying.
- Associative recall.
- Length generalization.

## Connections to Other Papers

Connects to long-context and efficient-inference papers through the recurring question of what architectural substrate should store what kind of information. It also links to TACO and compression work through efficiency as a structural design problem rather than a purely post-hoc pruning problem.

## Notes for Cross-Paper Synthesis

This paper strengthens the theme that modern model efficiency is becoming architectural and task-structural: the right hybrid can be smaller because its components divide computational roles.
