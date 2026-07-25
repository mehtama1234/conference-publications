# Why DPO is a Misspecified Estimator and How to Fix It

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: btEiAfnLsX
- Authors: Aditya Gopalan; Sayak Ray Chowdhury; Debangshu Banerjee
- Primary area: foundation or frontier models, including LLMs
- Keywords: Direct Preference Optimization;Reinforcement Learning;Reinforcement learning with human feedback
- Source URL: https://openreview.net/forum?id=btEiAfnLsX
- PDF URL: https://openreview.net/pdf?id=btEiAfnLsX

## Abstract

Direct alignment algorithms such as Direct Preference Optimization (DPO) fine-tune models based on preference data, using only supervised learning instead of two-stage reinforcement learning with human feedback (RLHF). We show that DPO encodes a statistical estimation problem over reward functions induced by a parametric policy class. When the true reward function that generates preferences cannot be realized via the policy class, DPO becomes misspecified, resulting in failure modes such as preference order reversal, worsening of policy reward, and high sensitivity to the input preference data distribution. On the other hand, we study the local behavior of two-stage RLHF for a parametric class and relate it to a natural gradient step in policy space.  Our fine-grained geometric characterization allows us to propose AuxDPO, which introduces additional auxiliary variables in the DPO loss function to help move towards the RLHF solution in a principled manner and mitigate the misspecification in DPO. We empirically demonstrate the superior performance of AuxDPO on didactic bandit settings as well as LLM alignment tasks.

## One-Sentence Claim

DPO can be statistically misspecified when the preference-generating reward is not realizable by the policy class; AuxDPO adds auxiliary variables to move more closely toward the RLHF solution.

## Problem

Direct preference optimization avoids two-stage RLHF by turning preference data into supervised fine-tuning, but it implicitly estimates rewards through a constrained parametric policy class.

When the true reward function cannot be represented through that policy class, DPO can reverse preference order, lower policy reward, or become highly sensitive to preference-data distribution.

## Core Contribution

The paper characterizes DPO as a misspecified statistical estimator and analyzes local two-stage RLHF behavior as a natural-gradient step in policy space.

It proposes AuxDPO, which adds auxiliary variables to the DPO loss to mitigate misspecification and better approximate the RLHF solution.

## Method

The theoretical analysis studies reward functions induced by parametric policy classes and compares DPO's estimator geometry with local RLHF dynamics.

AuxDPO modifies the loss with auxiliary variables that relax the restrictive coupling causing misspecification.

## Experiments and Evidence

The abstract reports empirical gains on didactic bandit settings and LLM alignment tasks.

AuxDPO performs better than DPO under settings designed to expose preference order reversal and reward degradation.

## Limits and Failure Modes

The practical benefit may depend on how often real preference data violates DPO's realizability assumptions. Auxiliary variables can add tuning complexity or instability.

Because this note is abstract-only, details still need checking: formal misspecification condition, AuxDPO objective, natural-gradient derivation, LLM tasks, baselines, and sensitivity analyses.

## Deep Themes

- Alignment as statistical estimation: preference tuning methods have realizability assumptions.
- Direct methods versus RLHF geometry: supervised objectives may not replicate policy-space reward improvement.
- Misspecification failure modes: preference order reversal and reward degradation expose estimator limits.
- Objective repair through auxiliary variables: small loss changes can correct deeper statistical geometry.

## Subthemes

- Direct Preference Optimization.
- RLHF.
- Natural-gradient policy update.
- AuxDPO.

## Connections to Other Papers

This connects to SafeDPO, token-importance DPO, semi-supervised preference optimization, and DPO/RLHF equivalence papers.

It also relates to TROLL because both revisit popular post-training objectives at the optimization-geometry level.

## Notes for Cross-Paper Synthesis

This paper adds a post-training-theory theme: alignment algorithms need estimator assumptions checked, not only empirical leaderboard comparisons.
