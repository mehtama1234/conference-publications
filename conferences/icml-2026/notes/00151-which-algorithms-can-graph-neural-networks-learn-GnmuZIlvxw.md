# Which Algorithms Can Graph Neural Networks Learn?

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: GnmuZIlvxw
- Authors: Solveig Wittig; Antonis Vasileiou; Robert R Nerem; Timo Stoll; Floris Geerts; Yusu Wang; Christopher Morris
- Primary area: deep_learning->theory
- Keywords: GNNs;generalization;expressivity;algorithms;size generalization
- Source URL: https://openreview.net/forum?id=GnmuZIlvxw
- PDF URL: https://openreview.net/pdf?id=GnmuZIlvxw

## Abstract

In recent years, there has been growing interest in understanding neural architectures' ability to learn to execute discrete algorithms, a line of work often referred to as neural algorithmic reasoning. The goal is to integrate algorithmic reasoning capabilities into larger neural pipelines. Many such architectures are based on (message-passing) graph neural networks (MPNNs), owing to their permutation equivariance and ability to deal with sparsity and variable-sized inputs. However, much existing work is either largely empirical and lacks formal guarantees or it focuses solely on expressivity, leaving open the question of when and how such architectures generalize beyond a finite training set. In this work, we propose a general theoretical framework that characterizes sufficient conditions under which MPNNs can learn an algorithm from a training set of small instances and provably approximate its behavior on inputs of arbitrary size with worst-case guarantees. Our framework applies to a broad class of algorithms, including single-source shortest paths, minimum spanning trees, and general dynamic programming problems, such as the $0$-$1$ knapsack problem. In addition, we establish impossibility results for a wide range of algorithmic tasks, showing that standard MPNNs cannot learn them and derive more expressive MPNN-like architectures that overcome these limitations. Finally, we refine our analysis for the Bellman–Ford algorithm, yielding substantially smaller required training sets and significantly extending the recent work of Nerem et al., 2025 by allowing for a differentiable regularization loss. Empirical results largely support our theoretical findings.

## One-Sentence Claim

MPNNs can provably learn some graph algorithms from small instances and generalize to arbitrary sizes under sufficient conditions, while other algorithmic tasks require more expressive architectures.

## Problem

Neural algorithmic reasoning with GNNs is often empirical or expressivity-only, leaving unclear when learned graph algorithms generalize beyond finite training sets.

## Core Contribution

The paper develops a theoretical framework for size-generalizing algorithm learning with MPNNs, gives impossibility results, and derives more expressive MPNN-like architectures for hard tasks.

## Method

The framework characterizes sufficient conditions under which MPNNs trained on small examples approximate algorithms on arbitrary-size inputs with worst-case guarantees, covering shortest paths, MST, dynamic programming, and refined Bellman-Ford analysis.

## Experiments and Evidence

The abstract reports empirical results largely supporting the theoretical findings and smaller training-set requirements for Bellman-Ford under differentiable regularization.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: formal assumptions, algorithm class boundaries, architecture modifications, and benchmark construction.

## Deep Themes

- Size generalization needs formal guarantees, not only training-set accuracy.
- GNNs can learn algorithms only when architecture and task structure align.
- Impossibility results are useful for designing more expressive neural processors.

## Subthemes

- Neural algorithmic reasoning.
- MPNNs.
- Size generalization.
- Shortest paths.
- Minimum spanning trees.
- Dynamic programming.

## Connections to Other Papers

Connects to S3GNN, OSM+, algorithmic reasoning, and graph verification papers through graph models as algorithm learners.

## Notes for Cross-Paper Synthesis

This paper adds an algorithm-learnability theme: whether a neural architecture generalizes depends on the algorithmic structure it can represent and execute.
