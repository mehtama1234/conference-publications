# A Causal Decomposition Approach for Fair Contextual Multi-Armed Bandits

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: kHEL0GD175
- Authors: Jiajun Chen; Jin Tian; Christopher John Quinn
- Primary area: general_machine_learning->online_learning_active_learning_and_bandits
- Keywords: sequential decision-making;causality;fairness
- Source URL: https://openreview.net/forum?id=kHEL0GD175
- PDF URL: https://openreview.net/pdf?id=kHEL0GD175

## Abstract

Counterfactual reasoning is one of the fundamental facets of human cognition, involved in various tasks such as explanation, credit assignment, blame, and responsibility. It describes the queries what would have happened had some intervention been performed given that something else, corresponding to Layer 3 of the Pearl Causal Hierarchy.  In this project, we examine a specific type of counterfactual quantities, called counterfactual direct (Ctf-DE), indirect (Ctf-IE), and spurious (Ctf-SE) effects for quantifying fairness in a sequential decision-making framework. Building on these measures, we formulate an online causally-fair learning problem with multiple long-term constraints and study it in both non-parametric contextual bandits and parametric logistic bandits settings. We achieve sublinear regret and violations bounds for both bandits settings with roundwise counterfactual fairness constraints (that are a priori unknown) without Slater's condition. For logistic bandits, our method achieves $\mathcal{O}(1)$ per-round time complexity using an online mirror descent estimator, yielding an efficient algorithm.

## One-Sentence Claim

Causal direct, indirect, and spurious effects can define roundwise fairness constraints for contextual bandits while still allowing sublinear regret and constraint violation.

## Problem

Sequential decision systems must balance reward with fairness, but fairness in bandits is difficult because counterfactual quantities are usually unknown online. Standard fairness constraints can also conflate direct, indirect, and spurious causal pathways.

The paper asks how to enforce counterfactual fairness constraints in contextual bandits without knowing those constraints in advance.

## Core Contribution

The paper uses counterfactual direct effects, indirect effects, and spurious effects to quantify fairness in sequential decision-making. It formulates an online causally fair learning problem with multiple long-term constraints.

It studies both non-parametric contextual bandits and parametric logistic bandits, proving sublinear regret and violation bounds for roundwise counterfactual fairness constraints without Slater's condition.

## Method

The framework decomposes fairness into causal effect components and treats them as long-term constraints in online learning. For logistic bandits, it uses an online mirror descent estimator to achieve O(1) per-round time complexity.

The algorithm must learn rewards while estimating or controlling unknown causal-fairness constraints over time.

## Experiments and Evidence

Evidence reported in the abstract:

- Counterfactual direct, indirect, and spurious effects used as fairness quantities.
- Online learning with multiple long-term constraints.
- Sublinear regret and constraint-violation bounds in non-parametric contextual bandits.
- Sublinear regret and constraint-violation bounds in logistic bandits.
- No Slater's condition required.
- O(1) per-round time for logistic bandits via online mirror descent estimator.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: causal graph assumptions, fairness estimability, regret rates, and empirical setup.

## Limits and Failure Modes

- Counterfactual effects require causal assumptions that may be hard to validate.
- Fairness constraints may be misspecified if latent confounding is unmodeled.
- Long-term constraint satisfaction may still allow short-term unfair decisions.
- Online estimation of causal quantities can be fragile under sparse contexts or rare groups.

## Deep Themes

**Fairness is causal, not only statistical.** The method separates direct, indirect, and spurious pathways.

**Constraints can be learned online.** The paper treats fairness quantities as unknown but controllable over time.

**Efficiency matters for deployed fairness.** O(1) per-round logistic-bandit updates make the framework closer to practical sequential decision systems.

## Subthemes

- Counterfactual fairness in bandits.
- Direct/indirect/spurious effect decomposition.
- Long-term online constraints.
- Logistic contextual bandits.
- No-Slater regret and violation analysis.

## Connections to Other Papers

Connects to DiCoLa, Unpaired Causal IV, OU Identifiability, and style-conditioned offline RL. It adds a fairness-specific instance of causal decomposition for sequential control.

## Notes for Cross-Paper Synthesis

This paper extends the causal-evidence theme into online decisions: fairness constraints become dynamic causal quantities that must be estimated and enforced while learning.
