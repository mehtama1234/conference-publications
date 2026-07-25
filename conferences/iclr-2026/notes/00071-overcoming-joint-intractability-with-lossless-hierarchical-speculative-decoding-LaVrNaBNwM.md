# Overcoming Joint Intractability with Lossless Hierarchical Speculative Decoding

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: LaVrNaBNwM
- Authors: Yuxuan Zhou; Fei Huang; Heng Li; Fengyi Wu; Tianyu Wang; jianwei zhang; Junyang Lin; Zhi-Qi Cheng
- Primary area: foundation or frontier models, including LLMs
- Keywords: Speculative Decoding;Joint Intractability;Lossless Verification
- Source URL: https://openreview.net/forum?id=LaVrNaBNwM
- PDF URL: https://openreview.net/pdf?id=LaVrNaBNwM

## Abstract

Verification is a key bottleneck in improving inference speed while maintaining distribution fidelity in Speculative Decoding. Recent work has shown that sequence-level verification leads to a higher number of accepted tokens compared to token-wise verification. However, existing solutions often rely on surrogate approximations or are constrained by partial information, struggling with joint intractability. In this work, we propose Hierarchical Speculative Decoding (HSD), a provably lossless verification method that significantly boosts the expected number of accepted tokens and overcomes joint intractability by balancing excess and deficient mass across accessible branches. Through extensive large-scale experiments, we show that HSD consistently improves acceptance rates, especially with longer draft sequences. Its strong explainability and generality further highlight the potential for integration into a wide range of speculative decoding frameworks.

## One-Sentence Claim

Hierarchical Speculative Decoding provides provably lossless sequence-level verification that improves accepted-token counts while overcoming joint intractability.

## Problem

Speculative decoding accelerates LLM inference by drafting multiple tokens and verifying them against a target model. Token-wise verification can be conservative, while sequence-level verification can accept more tokens but faces joint intractability.

Existing sequence-level methods often depend on surrogate approximations or partial information, risking either lost distribution fidelity or limited applicability.

## Core Contribution

The paper proposes Hierarchical Speculative Decoding, a lossless verification method for speculative decoding.

Its central idea is to balance excess and deficient probability mass across accessible branches, enabling sequence-level verification without changing the target distribution.

## Method

HSD organizes verification hierarchically over draft branches. Instead of checking tokens independently or approximating the full joint distribution, it redistributes verification mass across reachable branches so accepted draft sequences preserve distribution fidelity.

The hierarchy is meant to make longer draft sequences more useful by increasing expected accepted tokens.

## Experiments and Evidence

The abstract reports extensive large-scale experiments.

HSD consistently improves acceptance rates, with especially strong gains for longer draft sequences. The authors also emphasize explainability and generality across speculative decoding frameworks.

## Limits and Failure Modes

The method still depends on draft-model quality and the overhead of hierarchical verification. If branch construction or mass balancing is expensive, speedups may shrink for smaller models or shorter outputs.

Because this note is abstract-only, details still need checking: formal losslessness proof, hierarchy construction, verification overhead, models tested, latency results, and integration constraints.

## Deep Themes

- Lossless acceleration: inference speedups are valuable only if output distribution fidelity is preserved.
- Sequence-level acceptance: verification is moving from local token checks to structured branch decisions.
- Longer draft utilization: decoding systems increasingly try to extract more work from each target-model call.
- Explainable inference algorithms: probability-mass accounting makes acceleration behavior auditable.

## Subthemes

- Speculative decoding.
- Joint intractability.
- Lossless verification.
- Branch-level probability mass balancing.

## Connections to Other Papers

This connects to p-less sampling, ThinKV, ASAG, and EntroKV through test-time efficiency controls for LLM inference.

It also relates to TileLang at the systems level: algorithmic inference acceleration must ultimately be implemented with low overhead to matter in serving.

## Notes for Cross-Paper Synthesis

HSD adds a distribution-fidelity constraint to the efficiency theme: faster inference should not silently become a different sampler.
