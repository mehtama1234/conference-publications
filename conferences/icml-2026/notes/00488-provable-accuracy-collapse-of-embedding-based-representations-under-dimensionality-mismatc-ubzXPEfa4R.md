# Provable Accuracy Collapse of Embedding-Based Representations under Dimensionality Mismatch

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: ubzXPEfa4R
- Authors: Dionysis Arvanitakis; Vaggos Chatziafratis; Yiyuan Luo
- Primary area: theory
- Keywords: Contrastive Learning;Ordinal Embeddings;Embedding-based representations;Representation Learning;Metric Space
- Source URL: https://openreview.net/forum?id=ubzXPEfa4R
- PDF URL: https://openreview.net/pdf?id=ubzXPEfa4R

## Abstract

Embedding-based representations in Euclidean space $\mathbb{R}^d$ are a cornerstone of modern machine learning, where a major goal is to use the \emph{smallest dimension} that faithfully captures data relations. In this work, we prove sharp dimension--accuracy tradeoffs and identify a fundamental information-theoretic limitation: unless the embedding dimension $d$ is chosen close to the ground-truth dimension $D$,  accuracy undergoes a sudden collapse. Our main result shows that this phenomenon arises even in standard contrastive learning settings, where supervision is limited to a set of $m$ anchor--positive--negative triplets $(i,j,k)$ encoding distance comparisons $\mathrm{dist}(i,j) < \mathrm{dist}(i,k)$. Specifically, given triplets realizable by an unknown ground-truth embedding in $D$ dimensions, we prove that there exists constant $c < 1$, such that \emph{every embedding of dimension at most $cD$  violates almost half of the triplets}, yielding accuracy as low as a trivial one-dimensional solution that ignores the input. We complement our information-theoretic bounds with strong computational hardness results: under the Unique Games Conjecture, even if the given triplets are nearly realizable in $D=1$ dimension, no polynomial-time algorithm---\textit{regardless of its dimension}---can achieve accuracy above the trivial 50% baseline.

## One-Sentence Claim

Embedding representations face a sharp dimension-accuracy threshold: if the learned Euclidean dimension is too small relative to the true dimension, triplet accuracy collapses to near-trivial levels.

## Problem

Embedding methods aim to represent relational structure in as few dimensions as possible. In contrastive and ordinal settings, supervision often comes through triplets saying one pair is closer than another.

The key question is how much dimension is needed to faithfully preserve these relations. Practitioners often choose smaller embedding dimensions for efficiency, but the paper shows there can be a sudden information-theoretic collapse rather than graceful degradation.

## Core Contribution

The paper proves sharp dimension-accuracy tradeoffs. Given triplets realizable by an unknown D-dimensional embedding, every embedding of dimension at most cD violates almost half of the triplets for some constant c < 1.

It also proves strong computational hardness: under the Unique Games Conjecture, even nearly realizable one-dimensional triplet instances cannot be solved above the trivial 50 percent baseline by any polynomial-time algorithm, regardless of embedding dimension.

## Method

The theoretical setup studies ordinal triplet constraints of the form dist(i,j) < dist(i,k). It compares the ground-truth dimension D to candidate embedding dimension d and derives lower bounds on unavoidable triplet violations.

The hardness result uses reductions under UGC to show computational barriers separate from information-theoretic dimensionality limits.

## Experiments and Evidence

The abstract presents information-theoretic bounds and computational hardness results rather than empirical experiments. The main evidence is the proof that dimensionality mismatch can force accuracy down to near the trivial baseline.

Full-paper reading should verify constants, metric assumptions, realizability definitions, distribution of triplets, and the scope of the UGC-based hardness theorem.

## Limits and Failure Modes

Worst-case triplet bounds may be pessimistic for natural datasets with lower intrinsic dimension, noise tolerance, or task-specific structure. Practical embeddings can still work well below apparent dimensionality when only downstream ranking quality matters.

The result is a warning against underdimensioning, not a complete prescription for choosing d in real systems.

## Deep Themes

- Dimensionality as information bottleneck: too-small embeddings can lose relational structure catastrophically.
- Accuracy collapse rather than smooth tradeoff: representation compression has phase-transition behavior.
- Contrastive learning limits: triplet supervision can be impossible to satisfy under dimension mismatch.
- Hardness beyond dimension: some ordinal embedding problems are computationally hard even with enough dimension.

## Subthemes

- Ground-truth dimension D is a critical hidden parameter.
- Triplet accuracy can fall to 50 percent despite nontrivial input.
- Unique Games hardness separates efficient algorithms from realizability.
- Embedding size is a correctness parameter, not just a storage parameter.

## Connections to Other Papers

This paper connects to embedding translation, LDM, FedARC, and concept-binding work through representation geometry. It gives a negative counterpart: not every structure can be compressed into a smaller Euclidean space.

It also relates to MoE compression and sparse lottery tickets because all examine when compression preserves capability versus collapses it.

## Notes for Cross-Paper Synthesis

The synthesis point is that representation compression has hard limits. Efficiency work must ask what relational or semantic structure survives the chosen bottleneck.
