# On the Optimization Trajectory of DeepWalk Embeddings

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: YKX6FgtL3R
- Authors: Christopher Harker; Aditya Bhaskara
- Primary area: optimization->nonconvex
- Keywords: DeepWalk node embeddings;Stochastic block models;optimization trajectory
- Source URL: https://openreview.net/forum?id=YKX6FgtL3R
- PDF URL: https://openreview.net/pdf?id=YKX6FgtL3R

## Abstract

The DeepWalk algorithm has been widely used for learning node embeddings in graphs. Combined with the idea of _negative sampling_, the DeepWalk algorithm has been shown to be implementable at scale, easily handling graphs with millions of nodes. However, theoretical guarantees on the resulting embeddings are much less understood. Recent results have studied the minimizers of the objective and have shown interesting guarantees for certain graph classes. However, the optimization _trajectory_, i.e., what happens when we start at a random initialization and run gradient descent, remains poorly understood. This is especially true for the implementation of DeepWalk using Skip-gram with negative sampling (SGNS), since the variance of the stochastic updates turns out to be very large. In this work, we make progress on this question. We show that for "small norm" initialization, under a spectral gap assumption on the graph, the DeepWalk embeddings align with the column space of a fixed low-rank matrix. For graphs generated from Stochastic Block Models with certain separation conditions, our results imply that the DeepWalk embeddings recover cluster structure. To the best of our knowledge, our results give the first analysis of the optimization trajectory of DeepWalk with negative sampling on non-trivial graph classes.

## One-Sentence Claim

DeepWalk with negative sampling can be analyzed from random initialization: under spectral-gap and small-norm conditions, embeddings align with a fixed low-rank subspace and recover SBM clusters.

## Problem

DeepWalk is widely used for scalable node embeddings, especially with Skip-gram negative sampling, but theory has focused more on objective minimizers than on the actual gradient-descent trajectory. The stochastic updates in SGNS have high variance, making trajectory analysis difficult.

The paper asks what happens from random initialization during optimization on non-trivial graph classes.

## Core Contribution

The paper gives the first analysis of the optimization trajectory of DeepWalk with negative sampling on non-trivial graph classes. For small-norm initialization and graphs with a spectral gap, embeddings align with the column space of a fixed low-rank matrix.

For stochastic block models under separation conditions, this alignment implies recovery of cluster structure.

## Method

The method studies gradient-descent dynamics of the DeepWalk/SGNS objective rather than only final optima. Spectral assumptions on the graph control the direction in which embeddings grow from small initialization, and the low-rank subspace captures graph community structure.

The SBM result specializes this trajectory analysis to a probabilistic graph model where clusters are identifiable.

## Experiments and Evidence

Evidence reported in the abstract is theoretical:

- Trajectory analysis for DeepWalk with negative sampling.
- Small-norm initialization condition.
- Spectral-gap assumption on the graph.
- Alignment with a fixed low-rank matrix.
- Cluster recovery for stochastic block models under separation.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: exact learning rates, stochastic versus deterministic updates, negative-sampling distribution, and graph assumptions.

## Limits and Failure Modes

- Small-norm initialization and spectral gaps may not capture all real graph regimes.
- SBM separation conditions may be stronger than noisy applied graphs.
- High variance in SGNS updates remains a practical concern.
- Results may describe early or idealized trajectories more cleanly than full training with heuristics.

## Deep Themes

**Optimization trajectories matter, not only minima.** The paper explains how useful graph structure emerges during training.

**Spectral graph structure guides embedding dynamics.** DeepWalk recovers clusters because its path aligns with low-rank graph subspaces.

**Scalable heuristics are receiving dynamical theory.** A long-used practical algorithm gets a mechanistic optimization account.

## Subthemes

- DeepWalk with SGNS.
- Small-norm trajectory analysis.
- Spectral-gap assumptions.
- Low-rank subspace alignment.
- SBM cluster recovery.

## Connections to Other Papers

Connects to DIGL, ENGNN, PSAHS, and graph representation papers through graph geometry and cluster structure. It also links to Diffract and language-symmetry geometry because all study how optimization or data statistics create representation subspaces.

## Notes for Cross-Paper Synthesis

DeepWalk trajectory theory adds another instance where useful representations are explained by the path through parameter space, not only by the loss objective.
