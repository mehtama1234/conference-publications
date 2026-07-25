# Non-Convex Federated Optimization under Cost-Aware Client Selection

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: FnaDv6SMd9
- Authors: Xiaowen Jiang; Anton Rodomanov; Sebastian U Stich
- Primary area: optimization
- Keywords: Client Sampling;SAGA;Second-order Similarity;Composite Gradient Method;Variance Reduction
- Source URL: https://openreview.net/forum?id=FnaDv6SMd9
- PDF URL: https://openreview.net/pdf?id=FnaDv6SMd9

## Abstract

Different federated optimization algorithms typically employ distinct client-selection strategies: some methods communicate only with a randomly sampled subset of clients at each round, while others need to periodically communicate with all clients or use a hybrid scheme that combines both strategies. However, existing metrics for comparing optimization methods typically do not distinguish between these strategies, which often incur different communication costs in practice. To address this disparity, we introduce a simple and natural model of federated optimization that quantifies communication and local computation complexities. This new model allows for several commonly used client-selection strategies and explicitly associates each with a distinct cost. Within this setting, we propose a new algorithm that achieves the best-known communication and local complexities among existing federated optimization methods for non-convex optimization. This algorithm is based on the inexact composite gradient method with a carefully constructed gradient estimator and a special procedure for solving the auxiliary subproblem at each iteration. The gradient estimator is based on SAGA, a popular variance-reduced gradient estimator. We first derive a new variance bound for it, showing that SAGA can exploit functional similarity. We then introduce the Recursive-Gradient technique as a general way to potentially improve the error bound of a given conditionally unbiased gradient estimator, including both SAGA and SVRG. By applying this technique to SAGA, we obtain a new estimator, RG-SAGA, which has an improved error bound compared to the original one.

## One-Sentence Claim

The paper improves non-convex federated optimization by explicitly pricing client-selection strategies and deriving RG-SAGA, a variance-reduced estimator that exploits functional similarity.

## Problem

Federated optimization algorithms use different client-selection strategies: random subsets, full-client communication, or hybrids. Standard complexity comparisons often ignore that these strategies have different practical communication costs.

The problem is to compare and design federated methods under a cost model that accounts for client selection, communication, and local computation.

## Core Contribution

The paper introduces a simple cost-aware model for federated optimization and proposes an algorithm with best-known communication and local complexities for non-convex optimization under that model.

It derives a new SAGA variance bound showing SAGA can exploit functional similarity, then introduces Recursive-Gradient as a general technique to improve conditionally unbiased gradient estimators, yielding RG-SAGA.

## Method

The optimization algorithm uses an inexact composite gradient method with a carefully constructed gradient estimator and a special auxiliary subproblem solver.

RG-SAGA improves on SAGA by recursively reducing estimator error while preserving the cost-aware federated communication structure.

## Experiments and Evidence

The abstract is primarily theoretical. It claims best-known communication and local complexities compared with existing federated optimization methods for non-convex optimization.

The evidence is new variance and error bounds for SAGA, SVRG-style estimators, and RG-SAGA under functional similarity.

## Limits and Failure Modes

The practical value depends on whether the cost model matches real federated systems, where availability, stragglers, privacy, and heterogeneity may dominate.

Because this note is abstract-only, details still need checking: assumptions on smoothness and similarity, exact complexity bounds, auxiliary subproblem cost, empirical validation, and robustness to non-IID clients.

## Deep Themes

- Cost-aware algorithm comparison: federated methods should be judged by realistic communication patterns.
- Client selection as design variable: sampling strategy changes both theory and deployment cost.
- Functional similarity as variance resource: related clients can reduce estimator noise.
- Recursive estimator improvement: gradient-estimator error can be systematically reduced.

## Subthemes

- Non-convex federated optimization.
- SAGA variance reduction.
- Recursive-Gradient technique.
- Communication versus local computation.

## Connections to Other Papers

This connects to MV-FGAD, SmartFed, SpineFL, and federated personalization work through distributed learning under client heterogeneity.

It also relates to optimizer-theory papers such as LoRA-Pre, SGD RLVR, and ScaleRL because it sharpens optimization comparisons with realistic cost accounting.

## Notes for Cross-Paper Synthesis

This paper adds a deployment-aware optimization theme: algorithmic complexity should price the actual communication choices made by distributed systems.
