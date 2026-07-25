# Improved Dimension Dependence for Bandit Convex Optimization with Gradient Variation

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: X8evkEdMxb
- Authors: Hang Yu; Yu-Hu Yan; Peng Zhao
- Primary area: theory->online_learning_and_bandits
- Keywords: Online Learning;Bandit Convex Optimization;Two-Point Feedback;Dimension Dependence Improvement
- Source URL: https://openreview.net/forum?id=X8evkEdMxb
- PDF URL: https://openreview.net/pdf?id=X8evkEdMxb

## Abstract

Gradient-variation online learning has drawn increasing attention due to its deep connections to game theory and optimization. It has been studied extensively in the full-information setting, but is underexplored with bandit feedback. In this work, we focus on gradient variation in Bandit Convex Optimization (BCO) with two-point feedback. By proposing a refined analysis of the *non-consecutive* gradient variation, a fundamental quantity in gradient variation with bandit feedback, we improve the dimension dependence for both convex and strongly convex functions compared with the best known results (Chiang et al., 2013). Our improved analysis of the non-consecutive gradient variation also implies other favorable problem-dependent guarantees, such as gradient-variance and small-loss regret bounds. Beyond the two-point setup, we demonstrate the versatility of our technique by achieving the *first* gradient-variation bound for one-point bandit linear optimization over hyper-rectangular domains. Finally, we validate the effectiveness of our results in more challenging tasks such as dynamic and universal regret minimization, establishing the *first* gradient-variation dynamic and universal regret bounds for two-point BCO.

## One-Sentence Claim

Refined analysis of non-consecutive gradient variation improves dimension dependence and problem-dependent regret guarantees for bandit convex optimization.

## Problem

Gradient-variation bounds are important in online learning, game theory, and optimization because they exploit predictable changes in gradients. Full-information settings are well studied, but bandit feedback gives only limited function observations, making gradient variation harder to estimate and analyze.

The paper focuses on bandit convex optimization with two-point feedback and seeks better dimension dependence than classical results.

## Core Contribution

The paper introduces a refined analysis of non-consecutive gradient variation, a key quantity under bandit feedback. This improves dimension dependence for convex and strongly convex functions relative to Chiang et al. 2013.

The analysis also yields problem-dependent guarantees, including gradient-variance and small-loss regret bounds, and extends beyond two-point feedback by giving the first gradient-variation bound for one-point bandit linear optimization over hyperrectangles. It further establishes the first gradient-variation dynamic and universal regret bounds for two-point BCO.

## Method

The method is theoretical. It reworks how gradient variation is measured when feedback points are non-consecutive due to bandit sampling. By tightening this quantity, the authors improve regret analyses across multiple online-learning objectives.

The same analytical technique is then reused for one-point bandit linear optimization and dynamic/universal regret settings.

## Experiments and Evidence

Evidence reported in the abstract:

- Improved dimension dependence for convex and strongly convex two-point BCO.
- Gradient-variance and small-loss regret bounds.
- First gradient-variation bound for one-point bandit linear optimization over hyperrectangles.
- First gradient-variation dynamic and universal regret bounds for two-point BCO.
- Validation on dynamic and universal regret minimization tasks.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: exact regret rates, dimension exponents, assumptions on domains/losses, and whether validation is simulation or applied optimization.

## Limits and Failure Modes

- The gains may rely on two-point feedback, convexity, or domain assumptions.
- One-point results are stated for bandit linear optimization over hyperrectangles, not full BCO.
- Theoretical improvements may have constants that matter in finite regimes.
- Practical deployment depends on whether feedback queries are feasible.

## Deep Themes

**Sharper variation measures unlock better online guarantees.** The key is not a new model but a better accounting of gradient change under bandit feedback.

**Problem-dependent bounds are becoming more granular.** Variation, variance, small loss, dynamic regret, and universal regret expose different favorable regimes.

**Bandit feedback forces indirect geometry.** The learner must reason about gradients it cannot directly observe.

## Subthemes

- Non-consecutive gradient variation.
- Two-point bandit convex optimization.
- Dimension-dependence improvement.
- Small-loss and gradient-variance regret.
- Dynamic and universal regret.

## Connections to Other Papers

Connects to PAVE, R2VPO, and optimization-theory papers through gradient-field stability. It also links to game-theoretic work because variation-adaptive online learning often underlies equilibrium and repeated-decision analysis.

## Notes for Cross-Paper Synthesis

This paper contributes to the theory theme that better definitions of the changing environment can directly improve algorithmic guarantees.
