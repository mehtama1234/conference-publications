# P-GenRM: Personalized Generative Reward Model with Test-time User-based Scaling

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: hXNApWLBZG
- Authors: Pinyi Zhang; Ting-En Lin; Yuchuan Wu; Jingyang Chen; Zongqi Wang; Hua Yang; Xu Ze; Fei Huang; Yongbin Li; Kai Zhang
- Primary area: alignment, fairness, safety, privacy, and societal considerations
- Keywords: personalizd alignment;generative reward model;test-time user-based scaling
- Source URL: https://openreview.net/forum?id=hXNApWLBZG
- PDF URL: https://openreview.net/pdf?id=hXNApWLBZG

## Abstract

Personalized alignment of large language models seeks to adapt responses to individual user preferences, typically via reinforcement learning. A key challenge is obtaining accurate, user-specific reward signals in open-ended scenarios. Existing personalized reward models face two persistent limitations: (1) oversimplifying diverse, scenario-specific preferences into a small, fixed set of evaluation principles, and (2) struggling with generalization to new users with limited feedback. To this end, we propose **P-GenRM**, the first **P**ersonalized **Gen**erative **R**eward **M**odel with test-time user-based scaling. P-GenRM transforms preference signals into structured evaluation chains that derive adaptive personas and scoring rubrics across various scenarios. It further clusters users into User Prototypes and introduces a dual-granularity scaling mechanism: at the individual level, it adaptively scales and aggregates each user’s scoring scheme; at the prototype level, it incorporates preferences from similar users. This design mitigates noise in inferred preferences and enhances generalization to unseen users through prototype-based transfer. Empirical results show that  P-GenRM achieves state-of-the-art results on widely-used personalized reward model benchmarks, with an average improvement of ~2.31\%, and demonstrates strong generalization on an out-of-distribution dataset. Notably, Test-time User-based scaling provides an additional ~3\% boost, demonstrating stronger personalized alignment with test-time scalability.

## One-Sentence Claim

P-GenRM personalizes reward modeling by generating adaptive personas and rubrics, then scaling preferences at test time using individual users and similar-user prototypes.

## Problem

Personalized alignment needs reward signals that reflect individual user preferences in open-ended scenarios.

Existing personalized reward models often compress diverse preferences into fixed evaluation principles and generalize poorly to new users with limited feedback.

## Core Contribution

The paper introduces P-GenRM, a personalized generative reward model with test-time user-based scaling.

It converts preference signals into structured evaluation chains that produce adaptive personas and scoring rubrics, then uses user prototypes and dual-granularity scaling for personalization.

## Method

At the individual level, P-GenRM adaptively scales and aggregates a user's scoring scheme.

At the prototype level, it clusters users and transfers preferences from similar users, reducing noise in sparse individual feedback and improving generalization to unseen users.

## Experiments and Evidence

The abstract reports state-of-the-art results on personalized reward-model benchmarks, with about 2.31 percent average improvement.

Test-time user-based scaling adds roughly another 3 percent and the method generalizes strongly on an out-of-distribution dataset.

## Limits and Failure Modes

User clustering can misrepresent minority preferences or sensitive attributes, and test-time personalization can overfit noisy feedback. Generative rubrics may also encode model biases.

Because this note is abstract-only, details still need checking: benchmark datasets, feedback format, user-prototype construction, scaling mechanism, privacy handling, and OOD setup.

## Deep Themes

- Personalized alignment: reward models adapt to individual users rather than one global preference.
- Generative rubrics: reward evaluation becomes a structured reasoning process with personas and criteria.
- Prototype-based transfer: similar users provide priors for low-feedback personalization.
- Test-time reward scaling: alignment behavior adapts at inference/evaluation time without full retraining.

## Subthemes

- Personalized reward models.
- User prototypes.
- Test-time scaling.
- Structured evaluation chains.

## Connections to Other Papers

This connects to EigenBench, SafeDPO, SSPO, TI-DPO, and value-alignment measurement papers.

It also relates to recommendation/social-learning work because user preference modeling changes downstream information mediation.

## Notes for Cross-Paper Synthesis

P-GenRM adds a personalization theme: alignment is moving from population-average preference to user-conditional reward modeling with prototype transfer.
