# Multiplayer Nash Preference Optimization

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: x7aLhLMVn1
- Authors: Fang Wu; Xu Huang; Weihao Xuan; Zhiwei Zhang; Yijia Xiao; Guancheng Wan; Xiaomin Li; Bing Hu; Peng Xia; Jure Leskovec; Yejin Choi
- Primary area: applications to computer vision, audio, language, and other modalities
- Keywords: Preference Optimization;RLHF
- Source URL: https://openreview.net/forum?id=x7aLhLMVn1
- PDF URL: https://openreview.net/pdf?id=x7aLhLMVn1

## Abstract

Reinforcement learning from human feedback (RLHF) has emerged as the standard paradigm for aligning large language models (LLMs) with human preferences. However, reward-based methods built on the Bradley–Terry assumption struggle to capture the non-transitive and heterogeneous nature of real-world preferences. To address this, recent studies have reframed alignment as a two-player Nash game, giving rise to Nash learning from human feedback (NLHF). While this perspective has inspired algorithms such as INPO, ONPO, and EGPO with strong theoretical and empirical guarantees, they remain fundamentally restricted to two-player interactions, creating a single-opponent bias that fails to capture the full complexity of realistic preference structures. 
In this work, we introduce Multiplayer Nash Preference Optimization (MNPO), a novel framework that generalizes NLHF to the multiplayer regime. It formulates alignment as an $n$-player game, where each policy competes against a population of opponents while being regularized toward a reference model. 
Our framework establishes well-defined Nash equilibria in multiplayer settings and extends the concept of duality gap to quantify approximation quality. We demonstrate that MNPO inherits the equilibrium guarantees of two-player methods while enabling richer competitive dynamics and improved coverage of diverse preference structures. Through comprehensive empirical evaluation, we show that MNPO consistently outperforms existing NLHF baselines on instruction-following benchmarks, achieving superior alignment quality under heterogeneous annotator conditions and mixed-policy evaluation scenarios. Together, these results establish MNPO as a principled and scalable framework for aligning LLMs with complex, non-transitive human preferences.

## One-Sentence Claim

MNPO generalizes Nash-style preference optimization from two-player alignment games to multiplayer policy populations, better modeling heterogeneous and non-transitive human preferences.

## Problem

Standard RLHF often relies on Bradley-Terry-style reward modeling, which struggles with heterogeneous, non-transitive preferences. Two-player NLHF methods improve on scalar reward framing but introduce single-opponent bias, limiting their ability to represent realistic preference structures across multiple annotator groups or policy behaviors.

## Core Contribution

The paper introduces Multiplayer Nash Preference Optimization, an n-player alignment framework in which each policy competes against a population of opponents while remaining regularized toward a reference model. It establishes multiplayer Nash equilibria and extends duality-gap measurement to quantify approximation quality.

## Method

MNPO frames preference optimization as an n-player game over policies rather than a reward maximization problem or a two-player comparison. Policies are optimized against a population, with reference-model regularization preserving alignment stability. The framework uses an extended duality gap to evaluate how close learned policies are to equilibrium.

## Experiments and Evidence

The abstract reports comprehensive evaluation on instruction-following benchmarks. MNPO consistently outperforms existing NLHF baselines, especially under heterogeneous annotator conditions and mixed-policy evaluation scenarios, while inheriting equilibrium guarantees from two-player approaches.

## Limits and Failure Modes

This note is abstract/metadata-only. Full-text review should inspect computational cost as the number of players grows, how opponent populations are sampled, whether multiplayer dynamics are stable in large models, and whether benchmark heterogeneity truly approximates real preference pluralism. Equilibrium guarantees may not fully translate to noisy learned preference data.

## Deep Themes

- Preference alignment as multiplayer game.
- Non-transitive and heterogeneous human preferences.
- Equilibrium quality measurement.
- Population-based policy optimization.

## Subthemes

- RLHF.
- Nash learning from human feedback.
- Duality gap.
- Reference regularization.
- Mixed-policy evaluation.

## Connections to Other Papers

Connects to WIMHF through richer modeling of preference data, to AdAEM through probing value heterogeneity beyond static benchmarks, and to GLASS/EmotionThinker/Visual Planning through RL-style post-training shaped by nontrivial reward or evaluation structure.

## Notes for Cross-Paper Synthesis

MNPO adds a preference-theoretic version of a broad corpus pattern: single scalar objectives are often too thin. When preferences are plural and non-transitive, alignment may require population dynamics and equilibrium diagnostics rather than one reward model.
