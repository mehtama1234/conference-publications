# Hybrid Reinforcement: when reward is sparse, better to be dense

## Metadata

- Conference: iclr-2026
- Status: Poster
- OpenReview ID: 0CajQNVKyB
- Authors: Leitian Tao; Ilia Kulikov; Swarnadeep Saha; Tianlu Wang; Jing Xu; Sharon Li; Jason E Weston; Ping Yu
- Primary area: foundation or frontier models, including LLMs
- Keywords: Hybrid rewards for reinforcement learning
- Source URL: https://openreview.net/forum?id=0CajQNVKyB
- PDF URL: https://openreview.net/pdf?id=0CajQNVKyB

## Abstract

Post-training for reasoning in large language models has increasingly relied on verifiable rewards: deterministic checkers that provide $0$–$1$ correctness signals. While reliable, such binary feedback is brittle—many tasks admit partially correct or alternative answers that verifiers under-credit, and the resulting all-or-nothing supervision limits learning. Reward models  offer richer, continuous feedback, which can serve as a complementary supervisory signal to verifiers. We introduce HERO (Hybrid Ensemble Reward Optimization), a reinforcement learning framework that integrates sparse verifier signals with dense reward model scores in a structured way. HERO employs stratified normalization to bound reward-model scores within verifier-defined groups, preserving correctness while refining quality distinctions, and variance-aware weighting to emphasize challenging prompts where dense signals matter most. Across diverse mathematical reasoning benchmarks, HERO consistently outperforms reward model-only and verifier-only baselines, with strong gains on both verifiable and hard-to-verify tasks. Our results show that hybrid reward design retains the stability of verifiers while leveraging the nuance of reward models to advance reasoning.

## One-Sentence Claim

HERO combines sparse verifier rewards with dense reward-model scores so reasoning post-training preserves correctness while learning from nuanced partial-credit signals.

## Problem

Verifiable rewards are reliable but brittle: binary checkers under-credit partially correct, alternative, or hard-to-verify answers. Dense reward models can provide richer feedback but may be less trustworthy if used alone.

## Core Contribution

The paper introduces Hybrid Ensemble Reward Optimization, a reinforcement learning framework that structurally integrates verifier signals and reward-model scores using stratified normalization and variance-aware weighting.

## Method

HERO groups reward-model scores by verifier-defined correctness strata and normalizes them within those groups, preserving verifier correctness while ranking quality differences. Variance-aware weighting emphasizes prompts where dense signals are most useful, especially challenging or hard-to-verify cases.

## Experiments and Evidence

The abstract reports consistent improvements over reward-model-only and verifier-only baselines across diverse mathematical reasoning benchmarks, with gains on both verifiable and hard-to-verify tasks.

## Limits and Failure Modes

This note is abstract/metadata-only. Full-text review should inspect reward-model calibration, verifier coverage, normalization details, benchmark mix, and whether dense rewards introduce exploitable artifacts. Hybrid rewards can still fail when verifiers are wrong or reward models systematically prefer plausible but invalid reasoning.

## Deep Themes

- Hybrid reward design.
- Sparse verifier plus dense reward model.
- Reasoning post-training.
- Partial credit under correctness constraints.

## Subthemes

- HERO.
- Stratified normalization.
- Variance-aware weighting.
- Mathematical reasoning RL.
- Hard-to-verify tasks.

## Connections to Other Papers

Connects to THOR through step/process-level math reasoning signals, to ImageDoctor through dense structured rewards, and to MNPO/GLASS/EmotionThinker through alignment methods that enrich sparse outcome feedback.

## Notes for Cross-Paper Synthesis

HERO reinforces a major alignment pattern: neither pure verifier signals nor pure learned rewards are enough. The most useful training signal combines hard correctness anchors with dense quality gradients.
