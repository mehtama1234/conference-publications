# Learning to Execute Graph Algorithms Exactly with Graph Neural Networks

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: YKEmoqwkE9
- Authors: Muhammad Fetrat Qharabagh; Artur Back de Luca; George Giapitzakis; Kimon Fountoulakis
- Primary area: deep_learning->graph_neural_networks
- Keywords: Graph Neural Networks;Neural Algorithmic Reasoning;Graph Algorithms;Exact Learning
- Source URL: https://openreview.net/forum?id=YKEmoqwkE9
- PDF URL: https://openreview.net/pdf?id=YKEmoqwkE9

## Abstract

Understanding what graph neural networks can learn, especially their ability to learn to execute algorithms, remains a central theoretical challenge. In this work, we prove exact learnability results for graph algorithms under bounded-degree and finite-precision constraints. Our approach follows a two-step process. First, we train an ensemble of multi-layer perceptrons (MLPs) to execute the local instructions of a single node. Second, during inference, we use the trained MLP ensemble as the update function within a graph neural network (GNN). Leveraging Neural Tangent Kernel (NTK) theory, we show that local instructions can be learned from a small training set, enabling the complete graph algorithm to be executed during inference without error and with high probability. To illustrate the learning power of our setting, we establish a rigorous learnability result for the LOCAL model of distributed computation. We further demonstrate positive learnability results for widely studied algorithms such as message flooding, breadth-first and depth-first search, and Bellman-Ford.

## One-Sentence Claim

Under bounded-degree and finite-precision constraints, GNNs can exactly execute graph algorithms by learning local node instructions with small MLP ensembles and using them as inference-time update rules.

## Problem

Neural algorithmic reasoning asks whether neural networks can learn to execute algorithms rather than merely approximate input-output behavior. For graph algorithms, the theoretical question is especially hard because execution involves repeated local communication and exact symbolic-like state updates.

The paper asks when GNNs can provably learn exact graph algorithm execution.

## Core Contribution

The paper proves exact learnability results for graph algorithms in a bounded-degree, finite-precision setting. It separates the problem into two parts:

- Learn local instructions for a single node using an ensemble of MLPs.
- Use the trained ensemble as the update function inside a GNN during inference.

Using NTK theory, it shows local instructions can be learned from a small training set, enabling complete graph algorithms to execute without error with high probability. It gives results for the LOCAL model and algorithms including flooding, BFS, DFS, and Bellman-Ford.

## Method

The method reduces graph-algorithm learning to supervised learning of local transition rules. Once the local rule is learned, iterative GNN message passing simulates distributed computation over the graph.

NTK analysis supplies the generalization guarantee for local instruction learning, while bounded degree and finite precision keep the local state/action space tractable.

## Experiments and Evidence

Evidence reported in the abstract is mainly theoretical:

- Exact learnability under bounded-degree and finite-precision constraints.
- NTK-based proof that local instructions can be learned from small training sets.
- Rigorous result for the LOCAL distributed-computation model.
- Positive learnability results for message flooding, BFS, DFS, and Bellman-Ford.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: precise graph classes, finite-precision encoding, MLP ensemble size, error probability, and whether empirical demonstrations are included.

## Limits and Failure Modes

- Bounded degree and finite precision are strong assumptions compared with arbitrary graphs.
- Exactness depends on learning local rules perfectly enough; distribution shift in local states may break execution.
- NTK guarantees may require overparameterization or training assumptions.
- Algorithms with global branching or large state may not fit the same local-rule reduction.

## Deep Themes

**Algorithmic reasoning can be localized.** Exact global execution is obtained by learning local instructions and iterating them.

**Neural and symbolic computation meet in finite-state update rules.** GNNs become learned distributed computers under explicit constraints.

**Theory is narrowing the meaning of "learn an algorithm."** The paper distinguishes exact execution from approximate pattern matching.

## Subthemes

- Neural algorithmic reasoning.
- LOCAL model of distributed computation.
- NTK guarantees for local rule learning.
- Exact graph algorithm execution.
- Bounded-degree finite-precision assumptions.

## Connections to Other Papers

Connects to WZ-LLM and Procedural Pretraining through procedural structure as a scaffold for reasoning. It also links to ENGNN, DIGL, and graph OOD papers by studying what GNNs can express or execute under structural constraints.

## Notes for Cross-Paper Synthesis

This paper adds an exactness theme: for some algorithmic tasks, the right abstraction is not larger representation capacity but faithful learning of local transition rules.
