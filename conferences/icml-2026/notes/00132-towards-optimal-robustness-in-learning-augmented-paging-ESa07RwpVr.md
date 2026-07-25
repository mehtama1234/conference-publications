# Towards Optimal Robustness in Learning-Augmented Paging

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: ESa07RwpVr
- Authors: Peng Chen; Hailiang Zhao; Xueyan Tang; Yixuan Wang; Shuiguang Deng
- Primary area: optimization->discrete_and_combinatorial_optimization
- Keywords: Learning-augmented Algorithms;Paging;Optimality;Robustness
- Source URL: https://openreview.net/forum?id=ESa07RwpVr
- PDF URL: https://openreview.net/pdf?id=ESa07RwpVr

## Abstract

Learning-augmented paging has been extensively studied in recent years. A key advantage over naive ML-based approaches is bounded robustness, which guarantees worst-case performance even when predictions are inaccurate, making these algorithms valuable for real-world systems. Prior work achieves robustness bounds of $2H_k + O(1)$ in the randomized setting, leaving a gap to the optimal competitive ratio $H_k$.

In this paper, we study how to close this gap. We begin by reviewing online optimality and proving a new property of the latest $H_k$-competitive algorithm, which facilitates our analysis in the learning-augmented setting. Then, we review existing learning-augmented paging algorithms and introduce a unifying primitive, the relative prediction budget, which captures the essence of establishing robustness and reveals that prior algorithms either overuse or underutilize predictions. Guided by the above analysis, we develop a new framework that achieves the best-possible robustness up to an additive constant for learning-augmented paging: $H_k + O(1)$. Experiments further demonstrate strong practical performance.

## One-Sentence Claim

A new learning-augmented paging framework reaches best-possible robustness H_k + O(1) by controlling how prediction budget is used.

## Problem

Learning-augmented paging should exploit predictions while retaining worst-case guarantees, but prior randomized methods have robustness around 2H_k + O(1), above the optimal H_k.

## Core Contribution

The paper introduces a unifying relative prediction budget primitive and uses it to close the robustness gap for learning-augmented paging.

## Method

It analyzes a latest H_k-competitive online paging algorithm, identifies a property useful for prediction-augmented robustness, and designs a framework that avoids overusing or underusing predictions.

## Experiments and Evidence

The abstract reports H_k + O(1) robustness and experiments showing strong practical performance.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: prediction model assumptions, consistency/robustness tradeoff, randomized algorithm details, and empirical cache workloads.

## Deep Themes

- Learning-augmented algorithms need optimal fallback behavior when predictions fail.
- Prediction usage itself is a budgeted resource.
- Robustness can be designed around controlled trust in ML advice.

## Subthemes

- Learning-augmented algorithms.
- Paging.
- Competitive ratio.
- Robustness.
- Prediction budget.
- Online algorithms.

## Connections to Other Papers

Connects to online conformal prediction, robust optimization, and implementation-aware theory through guarantees under unreliable learned components.

## Notes for Cross-Paper Synthesis

This paper adds to the robust-learning-augmentation theme: ML predictions can improve online systems only when their influence is explicitly budgeted.
