# A Recursive Decomposition Framework for Causal Structure Learning in the Presence of Latent Variables

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: jdbQzlnYll
- Authors: Zheng Li; Feng Xie; Shenglan Nie; Xichen Guo; Ruxin Wang; Hao Zhang
- Primary area: general_machine_learning->causality
- Keywords: Causal Discovery;Causal Structure Learning;Latent Variables;Divide-and-Conquer;Ancestral Graph
- Source URL: https://openreview.net/forum?id=jdbQzlnYll
- PDF URL: https://openreview.net/pdf?id=jdbQzlnYll

## Abstract

Constraint-based causal discovery is widely used for learning causal structures, but heavy reliance on conditional independence (CI) testing makes it computationally expensive in high-dimensional settings.
To mitigate this limitation, many divide-and-conquer frameworks have been proposed, but most assume causal sufficiency, i.e., no latent variables.
In this paper, we show that divide-and-conquer strategies can be theoretically generalized beyond causal sufficiency to settings with latent variables. 
Specifically, we propose a recursive decomposition framework, termed DiCoLa, that enables divide-and-conquer causal discovery in the presence of latent variables. It recursively decomposes the global learning task into smaller subproblems and integrates their solutions through a principled reconstruction step to recover the global structure.
We theoretically establish the soundness and completeness of the proposed framework. Extensive experiments on synthetic data demonstrate that our approach significantly improves computational efficiency across a range of causal discovery algorithms, while experiments on a real-world dataset further illustrate its practical effectiveness.

## One-Sentence Claim

DiCoLa extends divide-and-conquer constraint-based causal discovery to latent-variable settings with sound and complete recursive decomposition and reconstruction.

## Problem

Constraint-based causal discovery relies heavily on conditional-independence testing, which becomes computationally expensive in high-dimensional problems. Divide-and-conquer methods reduce cost, but most assume causal sufficiency and therefore do not handle latent confounders.

The paper asks whether causal structure learning can be decomposed recursively when latent variables are present.

## Core Contribution

The contribution is DiCoLa, a recursive decomposition framework for causal discovery with latent variables. It decomposes the global learning task into smaller subproblems, solves them, and reconstructs the global ancestral graph through a principled integration step.

The paper theoretically establishes soundness and completeness, showing that divide-and-conquer causal discovery is not limited to causally sufficient settings.

## Method

DiCoLa recursively partitions the causal discovery problem into substructures that can be learned with existing constraint-based algorithms. After local solutions are obtained, a reconstruction step combines them into a global structure while preserving latent-variable semantics.

The framework is intended to wrap a range of causal discovery algorithms and improve their computational efficiency.

## Experiments and Evidence

Evidence reported in the abstract:

- Theoretical soundness and completeness.
- Synthetic experiments across multiple causal discovery algorithms.
- Significant computational efficiency gains.
- Real-world dataset experiment showing practical effectiveness.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: graph assumptions, decomposition criteria, reconstruction proof, and real dataset domain.

## Limits and Failure Modes

- Constraint-based methods still depend on reliable CI tests.
- Latent-variable assumptions and ancestral-graph semantics may not cover all hidden-confounding cases.
- Decomposition can fail to help if graph structure is too densely coupled.
- Reconstruction may be sensitive to local discovery errors.

## Deep Themes

**Decomposition is a scalability strategy.** High-dimensional causal discovery becomes tractable by learning smaller pieces.

**Latent variables should not force monolithic learning.** The paper generalizes divide-and-conquer beyond causal sufficiency.

**Global structure needs principled stitching.** Reconstruction is as important as local discovery.

## Subthemes

- Latent-variable causal discovery.
- Recursive decomposition.
- Ancestral graphs.
- Conditional-independence test efficiency.
- Sound and complete reconstruction.

## Connections to Other Papers

Connects to OU Identifiability, Unpaired Causal IV, Source Screening, and Noisy Sample Compression. It strengthens the evidence-efficiency theme in causal/statistical learning.

## Notes for Cross-Paper Synthesis

DiCoLa adds a causal-systems pattern: high-dimensional structure can be recovered by decomposing the graph, but only if the recomposition step has formal guarantees.
