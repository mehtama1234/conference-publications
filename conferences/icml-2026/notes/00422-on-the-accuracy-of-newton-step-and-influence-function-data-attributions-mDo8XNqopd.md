# On the Accuracy of Newton Step and Influence Function Data Attributions

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: mDo8XNqopd
- Authors: Ittai Rubinstein; Samuel B. Hopkins
- Primary area: theory->learning_theory
- Keywords: influence functions;data attribution;Newton step;logistic regression
- Source URL: https://openreview.net/forum?id=mDo8XNqopd
- PDF URL: https://openreview.net/pdf?id=mDo8XNqopd

## Abstract

Data attribution estimates how a trained model would change if a subset of training points were removed, and is a central primitive for tasks such as interpretability, data valuation, and machine unlearning. Despite its widespread use, our theoretical understanding of key data attribution methods -- Influence Functions (IF) and a single Newton Step (NS) -- remains limited: existing guarantees heavily rely on *global* strong convexity and yield bounds with pessimistic dependence on the parameter dimension $d$ and the number of removed samples $k$.
We give a new analysis of IF and NS for convex ERM that replaces global assumptions with *local* conditions: it suffices that the loss is strongly convex and sufficiently smooth only in a neighborhood of the first Newton step.
As a concrete validation, we analyze logistic regression with Gaussian features and show that our bounds capture the correct scaling up to polylogarithmic factors, yielding matching upper and lower bounds and explaining observed regimes in which NS is markedly more accurate than IF, thereby resolving open questions raised by (Koh et al., 2019).

## One-Sentence Claim

Local curvature conditions around the first Newton step can explain when Newton-step data attribution is more accurate than influence functions, avoiding pessimistic global assumptions.

## Problem

Data attribution estimates how a trained model would change if training points were removed, supporting interpretability, valuation, and unlearning. Influence Functions and single Newton Step approximations are widely used, but theory often assumes global strong convexity and gives pessimistic dependence on dimension and removed-sample count.

The paper asks whether local conditions can give sharper, more realistic guarantees.

## Core Contribution

The paper provides a new analysis of IF and NS for convex ERM requiring strong convexity and smoothness only near the first Newton step. It validates the theory for logistic regression with Gaussian features.

The bounds match upper and lower scaling up to polylog factors and explain regimes where NS is much more accurate than IF, resolving questions from Koh et al. (2019).

## Method

The analysis localizes the approximation problem around the Newton step rather than requiring global curvature. It studies the leave-k-out parameter shift and compares the IF linear approximation with a single Newton update.

For logistic regression with Gaussian features, it derives matching upper and lower behavior to show the scaling is essentially tight.

## Experiments and Evidence

Evidence reported in the abstract:

- New local-condition analysis for IF and NS in convex ERM.
- Strong convexity and smoothness needed only near the first Newton step.
- Logistic regression with Gaussian features analyzed.
- Bounds capture correct scaling up to polylogarithmic factors.
- Matching upper and lower bounds.
- Explanation of regimes where NS is markedly more accurate than IF.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: exact local assumptions, k/d scaling, and empirical comparisons.

## Limits and Failure Modes

- Results are for convex ERM, with concrete validation in logistic regression.
- Nonconvex deep networks may violate local curvature assumptions.
- Newton steps require Hessian information that can be expensive at scale.
- Attribution accuracy may degrade for large deletions or distribution-shifting removals.

## Deep Themes

**Attribution is local sensitivity.** Global convexity is often the wrong lens for leave-out effects.

**Second-order corrections matter.** A single Newton step can capture nonlinear parameter movement missed by IF.

**Unlearning primitives need sharper theory.** Attribution guarantees underpin data removal and valuation claims.

## Subthemes

- Influence functions.
- Newton-step attribution.
- Data removal sensitivity.
- Local strong convexity.
- Logistic regression scaling.

## Connections to Other Papers

Connects to OPUS, Source Screening, Token Overcharging, and unlearning/privacy papers. It adds theoretical precision to the data-attribution/data-governance cluster.

## Notes for Cross-Paper Synthesis

This paper strengthens the attribution theme: useful data governance depends on approximations whose error is understood in the actual local regime.
