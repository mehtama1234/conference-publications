# Modeling Hierarchical Thinking in Large Reasoning Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: N44P3zrrgO
- Authors: G M Shahariar; Erfan Shayegani; Ali Nazari; Nael Abu-Ghazaleh
- Primary area: deep_learning->large_language_models
- Keywords: reasoning;hierarchical thinking;finite state abstraction;reasoning dynamics;activation steering;Q-value policy;representation engineering;thinking;CoT;Chain of Thought
- Source URL: https://openreview.net/forum?id=N44P3zrrgO
- PDF URL: https://openreview.net/pdf?id=N44P3zrrgO

## Abstract

Large Reasoning Models (LRMs) solve complex tasks by generating long Chain-of-Thought (CoT) sequences; however, the emergent dynamics governing reasoning trajectories are not well understood and can lead to inconsistencies and reasoning pathologies. In this work, we propose to approximate LRM's emerging hierarchical reasoning dynamics as a trajectory within a Finite State Machine (FSM) transitioning among six abstract cognitive states. We demonstrate that these states and transitions can be captured in the latent state of the model. We believe that this representation can have different applications in the interpretability and optimization of LRM models. For example, by analyzing the topology of these transitions, we identify statistical shifts in reasoning strategies that help identify effective reasoning chains from those that fail. To illustrate these potential advantages, we propose $Q$-Value guided steering, a training-free inference-time control method that treats reasoning as a planning problem. We estimate the long-horizon utility of state transitions and apply sparse, orthogonal activation steering at sentence boundaries to align the CoT generation with optimal reasoning policies. Experiments across four benchmarks (AIME25, MATH-500, GSM8k, and GPQA Diamond) using three state-of-the-art open reasoning models demonstrate that $Q$-Value steering policy achieves significant performance gains with "surgical'' efficiency, often requiring $25\times$ fewer interventions than greedy and weighted baselines, which suggests that reasoning can be effectively controlled by guiding high-level cognitive dynamics rather than micro-managing token generation. Code is available at: https://github.com/shahariar-shibli/CoT-FSM.

## One-Sentence Claim

The paper models LRM chain-of-thought as transitions among six latent cognitive states and uses Q-value-guided activation steering to improve reasoning with sparse interventions.

## Problem

Large reasoning models generate long CoT trajectories, but the high-level dynamics governing successful versus failed reasoning paths are poorly understood and can produce pathologies.

## Core Contribution

The paper approximates hierarchical reasoning as a finite-state machine captured in latent activations, uses transition topology to distinguish effective chains, and proposes training-free Q-value policy steering at sentence boundaries.

## Method

The method identifies six abstract cognitive states in model latents, estimates long-horizon utility of state transitions, and applies sparse orthogonal activation steering at sentence boundaries to align CoT generation with better reasoning policies.

## Experiments and Evidence

The abstract reports significant gains on AIME25, MATH-500, GSM8K, and GPQA Diamond across three open reasoning models, often using 25x fewer interventions than greedy or weighted steering baselines.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: state discovery procedure, intervention safety, benchmark specifics, steering overhead, failure modes under distribution shift, and whether six states are stable across model families.

## Deep Themes

- Reasoning can be controlled at high-level state-transition granularity.
- CoT dynamics resemble planning trajectories, not just token sequences.
- Sparse activation steering can improve process quality without retraining.

## Subthemes

- Large reasoning models.
- Chain-of-thought.
- Finite-state abstraction.
- Q-value policy steering.
- Activation steering.
- Reasoning dynamics.

## Connections to Other Papers

Connects to TRM, Faire, FlashTrace, and CE-Graph through process-level reasoning analysis and to test-time scaling papers through inference-time control.

## Notes for Cross-Paper Synthesis

This paper adds a high-level-control theme for reasoning: steering the sequence of cognitive states may be more efficient than intervening on every token or local step.
