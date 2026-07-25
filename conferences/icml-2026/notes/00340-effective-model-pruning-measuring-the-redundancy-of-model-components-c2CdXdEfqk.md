# Effective Model Pruning : Measuring the Redundancy of Model Components

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: c2CdXdEfqk
- Authors: Yixuan Wang; Dan P. Guralnik; Saiedeh Akbari; Warren Dixon
- Primary area: theory->deep_learning
- Keywords: Model Pruning
- Source URL: https://openreview.net/forum?id=c2CdXdEfqk
- PDF URL: https://openreview.net/pdf?id=c2CdXdEfqk

## Abstract

This article initiates the study of a basic question about model pruning. Given a vector s of importance scores assigned to model components, how many of the scored components could be discarded without sacrificing performance? We propose Effective Model Pruning (EMP), which derives the desired sparsity directly from the score distribution using the notion of effective sample size from particle filtering, also known as the inverse Simpson index.

Rather than prescribe a pruning criterion, EMP supplies a universal adaptive threshold derived from the distribution of the score $s$ over the model components: EMP maps $s$ to a number $N_{eff} = N_{eff} (s)$, called the effective sample size. The $N − N_{eff}$ lowest scoring components are discarded. A tight lower bound on the preserved mass fraction seff (the sum of retained normalized scores) in terms of $N_{eff}$ is derived. This process yields models with a provable upper bound on the loss change relative to the original dense
model. Numerical experiments are performed demonstrating this phenomenon across a variety of network architectures including MLPs, CNNs, Transformers, LLMs, and KAN. It is also shown that EMP addresses a rich set of pruning criteria such as weight magnitude, attention score, KAN importance score, and even feature-level signals such as image pixels.

## One-Sentence Claim

Effective Model Pruning chooses sparsity adaptively from importance-score distributions using effective sample size, yielding preserved-mass and loss-change guarantees across many component types.

## Problem

Pruning typically starts with importance scores for model components, but practitioners still need to choose how many components to remove. Fixed sparsity targets or ad hoc thresholds can under-prune or over-prune depending on the score distribution.

The paper asks how to derive the pruning amount directly from the score vector itself.

## Core Contribution

The paper introduces Effective Model Pruning. It maps the importance-score vector to an effective sample size, using the inverse Simpson index from particle filtering, then discards the N - N_eff lowest-scoring components.

It derives a tight lower bound on the preserved normalized score mass in terms of N_eff and gives a provable upper bound on loss change relative to the dense model. Experiments span MLPs, CNNs, Transformers, LLMs, KANs, and pruning criteria from weight magnitude to feature-level image pixels.

## Method

EMP normalizes importance scores and computes their concentration. If the score mass is concentrated in a small set of components, the effective sample size is small and more components can be pruned. If scores are diffuse, fewer components are removed.

This makes sparsity adaptive to redundancy implied by the importance distribution.

## Experiments and Evidence

Evidence reported in the abstract:

- Effective sample size / inverse Simpson index thresholding rule.
- Tight lower bound on preserved score mass.
- Upper bound on loss change relative to dense model.
- Experiments across MLPs, CNNs, Transformers, LLMs, and KANs.
- Applies to weight magnitude, attention score, KAN importance, and image-pixel feature signals.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: loss-bound assumptions, score normalization, fine-tuning after pruning, and benchmark results.

## Limits and Failure Modes

- Guarantees depend on the importance scores being meaningful.
- Effective sample size may not capture interactions among components.
- Pruning low-scoring components can still damage rare capabilities.
- Different architectures may require structured constraints beyond component-wise thresholds.

## Deep Themes

**Sparsity should be inferred from redundancy.** EMP lets the score distribution choose the pruning amount.

**Importance concentration is a pruning signal.** Effective sample size quantifies how many components carry meaningful mass.

**Universal pruning rules need explicit guarantees.** Preserved mass and loss-change bounds make thresholding less arbitrary.

## Subthemes

- Effective sample size for pruning.
- Inverse Simpson index.
- Adaptive sparsity threshold.
- Preserved score-mass guarantee.
- Component-agnostic pruning criteria.

## Connections to Other Papers

Connects to MACKO-SpMV, FlashOptim, ReQAT, FeatJND, and Brain Encoding Scale through compression and deployment efficiency. It also links to Diffract because both ask which model components can be removed or rewound without quality loss.

## Notes for Cross-Paper Synthesis

EMP contributes a principled thresholding layer to the efficiency theme: after scoring components, the next question is how much redundancy the score distribution proves.
