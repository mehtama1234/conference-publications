# HOBIT: Hardness Optimized Batch Sampling for InfoNCE Training

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: R49XZi14YH
- Authors: Himanshu Dutta; Lokesh Nagalapatti; Yashoteja Prabhu
- Primary area: deep_learning->other_representation_learning
- Keywords: information retrieval;dual encoders;hard negative mining;optimal batching
- Source URL: https://openreview.net/forum?id=R49XZi14YH
- PDF URL: https://openreview.net/pdf?id=R49XZi14YH

## Abstract

Contrastive training with  InfoNCE loss and in-batch negatives is the standard approach for learning dual-encoder models. Its effectiveness, however, critically depends on the availability of hard negatives; in their absence, learning quickly saturates. Existing methods address this via explicit hard-negative mining, which is often costly or heuristic-driven. We introduce $\mathrm{\texttt{HOBIT}}$, a principled mini-batch construction method that improves in-batch negative quality by reordering training examples at every epoch. $\mathrm{\texttt{HOBIT}}$ solves an optimization problem motivated by the InfoNCE objective to yield mini-batches such that each query in the batch is exposed to hard yet non-contradictory, informative negative examples. We show that the optimization objective is monotone and submodular which in turn leads us to a greedy algorithm that admits the standard $\mathcal{O}(1 - 1/e)$ approximation guarantee. Empirically, we show that $\mathrm{\texttt{HOBIT}}$ incurs negligible computational overhead while significantly outperforming state-of-the-art batching methods, and remains complementary to existing hard negative mining techniques.

## One-Sentence Claim

HOBIT improves InfoNCE dual-encoder training by constructing mini-batches that expose each query to hard, informative, non-contradictory in-batch negatives.

## Problem

Dual-encoder contrastive learning quickly saturates without hard negatives, while explicit hard-negative mining can be expensive or heuristic.

## Core Contribution

The paper formulates hardness-optimized batch construction as a monotone submodular optimization problem and gives a greedy algorithm with a standard 1 - 1/e approximation guarantee.

## Method

At each epoch, HOBIT reorders training examples into mini-batches that optimize an InfoNCE-motivated objective, improving in-batch negative quality while avoiding contradictory negatives.

## Experiments and Evidence

The abstract reports negligible computational overhead, significant gains over state-of-the-art batching methods, and complementarity with existing hard-negative mining techniques.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: retrieval datasets, contradiction definition, similarity computation cost, batch-size sensitivity, interaction with mined negatives, and distributed-training scalability.

## Deep Themes

- Data ordering and batching are optimization levers, not incidental training details.
- Hardness should be useful without contradicting labels.
- Submodularity can turn heuristic training-data construction into an algorithm with guarantees.

## Subthemes

- InfoNCE.
- Dual encoders.
- Hard negatives.
- Batch sampling.
- Submodular optimization.
- Information retrieval.

## Connections to Other Papers

Connects to data selection, sequential data values, and power-law curriculum papers through training distribution/order as a capability driver.

## Notes for Cross-Paper Synthesis

HOBIT adds a batch-level curation theme: the examples in a mini-batch define the contrastive task, so batch construction is part of representation learning.
