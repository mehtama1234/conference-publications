# Non-Asymptotic Analysis of (Sticky) Track-and-Stop

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: vebqP5aioj
- Authors: Riccardo Poiani; Martino Bernasconi; Andrea Celli
- Primary area: learning theory
- Keywords: Multi-Armed Bandit Theory;Pure Exploration;Fixed-Confidence
- Source URL: https://openreview.net/forum?id=vebqP5aioj
- PDF URL: https://openreview.net/pdf?id=vebqP5aioj

## Abstract

In pure exploration problems, a statistician sequentially collects information to answer a question about some stochastic and unknown environment. The probability of returning a wrong answer should not exceed a maximum risk parameter $\delta$ and good algorithms make as few queries to the environment as possible. The Track-and-Stop algorithm is a pioneering method to solve these problems. Specifically, it is well-known that it enjoys asymptotic optimality sample complexity guarantees for $\delta \to 0$ whenever the map from the environment to its correct answers is single-valued (e.g., best-arm identification with a unique optimal arm). The Sticky Track-and-Stop algorithm extends these results to settings where, for each environment, there might exist multiple correct answers (e.g., $\epsilon$-optimal arm identification). Although both methods are optimal in the asymptotic regime, their non-asymptotic guarantees remain unknown. In this work, we fill this gap and provide non-asymptotic guarantees for both algorithms.

## One-Sentence Claim

The paper provides finite-sample guarantees for Track-and-Stop and Sticky Track-and-Stop pure-exploration bandit algorithms, closing a gap left by asymptotic optimality results.

## Problem

Track-and-Stop algorithms are asymptotically optimal for fixed-confidence pure exploration as risk `delta` approaches zero, but users need non-asymptotic sample-complexity guarantees at finite confidence levels. Existing theory is especially incomplete when multiple correct answers are allowed.

## Core Contribution

The paper derives non-asymptotic guarantees for both classic Track-and-Stop and Sticky Track-and-Stop, covering single-valued answer maps such as unique best-arm identification and multi-valued settings such as epsilon-optimal arm identification.

## Method

The analysis studies fixed-confidence pure exploration where a statistician adaptively queries a stochastic environment while controlling error probability. It bounds the finite-sample behavior of Track-and-Stop allocation and stopping rules, including the sticky extension for multiple valid answers.

## Experiments and Evidence

The main evidence is theoretical: finite-risk guarantees complementing known asymptotic optimality as `delta -> 0`. The abstract does not emphasize empirical experiments.

## Limits and Failure Modes

Non-asymptotic bounds may be conservative or depend on problem-specific complexity terms. Practical performance may still hinge on implementation details and distributional assumptions. Full-text review should check exact constants, assumptions on reward distributions, multiple-answer handling, and comparison to empirical stopping behavior.

## Deep Themes

- Finite-sample theory for adaptive experimentation.
- Fixed-confidence pure exploration.
- Bandit stopping rules.
- Multiple-correct-answer identification.

## Subthemes

- Track-and-Stop.
- Sticky Track-and-Stop.
- Best-arm identification.
- Epsilon-optimal arm identification.
- Non-asymptotic sample complexity.

## Connections to Other Papers

Connects to ranking-feedback online learning and OpTI-BFM through bandit-style data collection, and to evaluation/active reasoning papers where sample efficiency under uncertainty matters.

## Notes for Cross-Paper Synthesis

This paper supplies rigorous finite-time guarantees for a recurring practical problem: how to stop collecting data once confidence is high enough. It grounds broader adaptive-evaluation and task-inference themes in bandit theory.
