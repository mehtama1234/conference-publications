# DR-Submodular Maximization with Stochastic Biased Gradients: Classical and Quantum Gradient Algorithms

## Metadata

- Conference: iclr-2026
- Status: Poster
- OpenReview ID: 0CZAimzcVr
- Authors: Shengminjie Chen; Xiaoming Sun; Wenguo Yang; Jialin Zhang; Zihan Zhao
- Primary area: optimization
- Keywords: DR-submodular Maximization;Stochastic Biased Gradients;Zero-Order Optimization;Quantum Gradient Estimation;Approximation Algorithms
- Source URL: https://openreview.net/forum?id=0CZAimzcVr
- PDF URL: https://openreview.net/pdf?id=0CZAimzcVr

## Abstract

In this work, we investigate DR-submodular maximization using stochastic biased gradients, which is a more realistic but challenging setting than stochastic unbiased gradients. We first generalize the Lyapunov framework to incorporate biased stochastic gradients, characterizing the adverse impacts of bias and noise. Leveraging this framework, we consider not only conventional constraints but also a novel constraint class: convex sets with a largest element, which naturally arises in applications such as resource allocations. For this constraint, we propose an $1/e$ approximation algorithm for non-monotone DR-submodular maximization, surpassing the hardness result $1/4$ for general convex constraints. As a direct application of stochastic biased gradients, we consider zero-order DR-submodular maximization and introduce both classical and quantum gradient estimation algorithms. In each constraint we consider, while retaining the same approximation ratio, the iteration complexity of our classical zero-order algorithms is $O(\epsilon^{-3})$, matching that of stochastic unbiased gradients; our quantum zero-order algorithms reach $O(\epsilon^{-1})$ iteration complexity, on par with classical first-order algorithms, demonstrating quantum acceleration and validated in numerical experiments.

## One-Sentence Claim

The paper develops classical and quantum algorithms for DR-submodular maximization with stochastic biased gradients, including improved approximation for convex sets with a largest element.

## Problem

Many DR-submodular optimization settings have stochastic gradient estimates that are biased rather than unbiased, which makes standard analyses too optimistic. Practical applications such as resource allocation also involve constraint classes that are more structured than general convex sets.

## Core Contribution

The paper generalizes a Lyapunov analysis framework to biased stochastic gradients, proposes a `1/e` approximation algorithm for non-monotone DR-submodular maximization over convex sets with a largest element, and develops classical and quantum zero-order gradient-estimation algorithms.

## Method

The method characterizes how bias and noise affect convergence through a modified Lyapunov framework. It then designs algorithms for several constraint classes, including the largest-element convex-set case, and applies the biased-gradient framework to zero-order optimization with classical and quantum gradient estimators.

## Experiments and Evidence

The abstract reports approximation guarantees and iteration complexity results. Classical zero-order algorithms achieve `O(epsilon^-3)` iteration complexity while retaining approximation ratios, matching stochastic unbiased-gradient complexity; quantum zero-order algorithms achieve `O(epsilon^-1)`, comparable to classical first-order methods. Numerical experiments validate the quantum acceleration claim.

## Limits and Failure Modes

This note is abstract/metadata-only. Full-text review should inspect oracle assumptions, bias bounds, constants, quantum access model, practical implementability of quantum gradient estimation, and examples of convex sets with largest elements. Quantum speedups may rely on assumptions unavailable in near-term hardware.

## Deep Themes

- Biased-gradient optimization theory.
- DR-submodular maximization.
- Approximation algorithms under structured constraints.
- Quantum acceleration for zero-order methods.

## Subthemes

- Lyapunov framework.
- Convex sets with largest element.
- Non-monotone submodularity.
- Classical zero-order gradients.
- Quantum gradient estimation.

## Connections to Other Papers

Connects to Track-and-Stop and global merging through finite-regime optimization guarantees, to NEXCO through constrained combinatorial optimization, and to scientific/quantum modeling notes through quantum algorithmic structure.

## Notes for Cross-Paper Synthesis

This paper adds an optimization-theory version of realism: gradient estimates are biased in many practical settings. Guarantees become more useful when they model the actual noise and bias in the oracle.
