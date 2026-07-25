# Post-Training with Policy Gradients: Optimality and the Base Model Barrier

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: nnWlTi7A7a
- Authors: Alireza Mousavi-Hosseini; Murat A Erdogdu
- Primary area: deep_learning->theory
- Keywords: post-training;policy gradient;autoregressive models;coverage;RLVR;minimax optimality;separable data
- Source URL: https://openreview.net/forum?id=nnWlTi7A7a
- PDF URL: https://openreview.net/pdf?id=nnWlTi7A7a

## Abstract

We study post-training linear autoregressive models with outcome and process rewards. Given a context $x$, the model must predict the response $y \in \mathcal{Y}^N$, a sequence of length $N$ that satisfies a $\gamma$ margin condition, an extension of the standard separability to sequences.
We prove that on test samples where the base model achieves a non-trivial likelihood $\alpha$, a variant of policy gradient (PG) can achieve likelihood $1 - \varepsilon$ with an essentially minimax optimal number of reward queries $\tilde{\mathcal{O}}((\alpha^{-1} + \varepsilon^{-1})/\gamma^2)$.
However, a barrier arises for going beyond the support of the base model.
We prove that the overall expected error after post-training with outcome rewards is governed by a property of the base model called the *Likelihood Quantile* (LQ), and that variants of PG, while minimax optimal, may require a number of reward queries exponential in $N$ to go beyond this support, regardless of the pre-training algorithm.
To overcome this barrier, we study post-training with a process reward model, and demonstrate how PG variants in this setting avoid the curse of dimensionality in $N$ via dependence on a token-level LQ.
Along the way, we prove that under the margin condition, SGD with adaptive learning rate (LR) achieves a near optimal test error for statistical learning, and PG with adaptive LR achieves a near optimal number of mistakes for online learning while being computationally efficient whenever possible, both of which may be of independent interest.

## One-Sentence Claim

Policy-gradient post-training can be minimax optimal where the base model already assigns nontrivial likelihood, but outcome rewards face an exponential barrier beyond the base model's support unless process rewards provide token-level guidance.

## Problem

Post-training with reinforcement learning is now central to improving autoregressive models, but its theoretical limits are unclear. In particular, it is not enough to ask whether policy gradients can improve a model; the key question is when reward queries can discover responses that the base model almost never produces.

The paper formalizes this as a support and coverage problem. If the base model gives low probability to correct sequences, outcome-only rewards may require searching an exponentially large sequence space.

## Core Contribution

The paper proves that, on test samples where the base model assigns nontrivial likelihood alpha to good responses, a policy-gradient variant can reach likelihood 1 - epsilon with essentially minimax-optimal reward-query complexity. It then proves a base-model barrier: going beyond the support of the base model can require exponentially many reward queries in sequence length.

It also shows how process rewards avoid this curse by replacing sequence-level coverage with token-level likelihood quantiles. The conceptual contribution is a theory of why post-training can refine capabilities already latent in the base model but struggles to create capabilities unsupported by the base distribution.

## Method

The analysis uses linear autoregressive models under a sequence margin condition. It studies outcome-reward and process-reward versions of policy gradient, introducing Likelihood Quantile as a property that governs post-training error.

For outcome rewards, the relevant quantity is whether the base model assigns enough probability to full correct responses. For process rewards, the dependence shifts toward token-level LQ, giving the learner denser guidance and avoiding exponential dependence on sequence length.

## Experiments and Evidence

This is primarily a theoretical paper. The abstract states upper bounds for policy-gradient reward-query complexity, lower/barrier results for out-of-support learning, and near-optimality claims for adaptive learning-rate SGD and PG under the margin condition.

The most important evidence is the separation between outcome and process rewards. Full-paper reading should verify assumptions behind linear autoregressive modeling, separability/margin conditions, and the exact minimax constants hidden in the tilde notation.

## Limits and Failure Modes

The theory is based on simplified linear autoregressive models and margin assumptions, so direct transfer to frontier-scale nonlinear transformers is interpretive rather than automatic. Real RLHF/RLVR pipelines also include reward-model errors, sampling heuristics, KL penalties, and multi-stage data mixtures.

Still, the support barrier is likely robust as a conceptual warning: post-training cannot efficiently optimize behavior that the base model almost never samples unless the training signal decomposes the problem.

## Deep Themes

- Base-model support as a capability boundary: post-training refines what pretraining makes reachable.
- Process supervision as search-space compression: token-level feedback avoids exponential sequence search.
- Theory of RLVR scaling: reward-query complexity becomes a core measure of post-training feasibility.
- Optimality with a caveat: PG can be minimax optimal and still limited by base distribution coverage.

## Subthemes

- Likelihood Quantile turns vague coverage into a measurable theoretical property.
- Outcome rewards are sparse over long sequences.
- Process rewards reshape exploration by rewarding partial progress.
- Adaptive learning rates appear as a bridge between statistical and online learning guarantees.

## Connections to Other Papers

This paper connects to BLL-Loss, PLAINTAIN, JustGRPO, and RAGEN-style reasoning RL papers. All probe the limits of post-training and inference-time reasoning, but this one gives a clean theoretical account of when policy-gradient improvement is possible.

It also links to OPUS and data-selection work: if the base model's support determines what post-training can reach, pretraining data and token exposure become upstream constraints on downstream alignment.

## Notes for Cross-Paper Synthesis

The cross-paper takeaway is that post-training should be understood as conditional amplification, not unconstrained capability creation. Process supervision, data selection, and base-model coverage form a single pipeline of reachability.
