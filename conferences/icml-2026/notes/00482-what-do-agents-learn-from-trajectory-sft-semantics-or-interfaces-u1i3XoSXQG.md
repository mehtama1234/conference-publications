# What Do Agents Learn from Trajectory-SFT: Semantics or Interfaces?

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: u1i3XoSXQG
- Authors: Weizheng Gu; Chengze Li; Zhuohao Yu; Mengyuan Sun; Zhibang Yang; Wei Wang; Hongrui Jia; Shikun Zhang; Wei Ye
- Primary area: deep_learning->large_language_models
- Keywords: LLM agent;agent evaluation;tool using;generalization
- Source URL: https://openreview.net/forum?id=u1i3XoSXQG
- PDF URL: https://openreview.net/pdf?id=u1i3XoSXQG

## Abstract

Large language models are increasingly evaluated as interactive agents, yet standard agent benchmarks conflate two qualitatively distinct sources of success: semantic tool-use and interface-specific interaction pattern memorization.
Because both mechanisms can yield identical task success on the original interface, benchmark scores alone are not identifiable evidence of environment-invariant capability.
We propose **PIPE**, a protocol-level evaluation augmentation for diagnosing interface reliance by minimally rewriting environment interfaces while preserving task semantics and execution behavior.
Across 16 environments from AgentBench and AgentGym and a range of open-source and API-based agents, PIPE reveals that task-specific trajectory-SFT can amplify reliance on training-time interface forms: in several environments, agents with trajectory-SFT degrade sharply under minimal interface rewrites, whereas other agents are often more stable.
We further introduce Interface Reliance (IR), a counterbalanced alias-based metric that quantifies preference for training-time interfaces, and show that interface shortcutting exhibits environment-dependent, non-monotonic training dynamics that remain invisible under standard evaluation. Our code is available at https://github.com/ChengZe2005/What-Do-Agents-Learn-from-Trajectory-SFT-Semantics-or-Interfaces-.

## One-Sentence Claim

PIPE shows that trajectory-SFT can teach agents brittle interface patterns rather than semantic tool-use competence, revealed by minimal interface rewrites that preserve task behavior.

## Problem

Agent benchmarks often report task success, but the same success can come from two different mechanisms: robust semantic tool use or memorized interaction patterns tied to the training interface. Standard scores cannot identify which mechanism was learned.

This matters because deployed tools and environments change. An agent that learned interface shortcuts can collapse under harmless renamings, layout changes, or alias substitutions even though the underlying task semantics are unchanged.

## Core Contribution

The paper introduces PIPE, a protocol-level evaluation augmentation that minimally rewrites environment interfaces while preserving task semantics and execution behavior. It also introduces Interface Reliance, a counterbalanced alias-based metric for preference toward training-time interfaces.

The core finding is that task-specific trajectory-SFT can amplify reliance on training-time interface forms. In several environments, SFT agents degrade sharply under minimal rewrites while other agents remain more stable.

## Method

PIPE constructs paired evaluations: original interfaces and minimally rewritten interfaces with the same semantics and execution behavior. By comparing performance, the protocol diagnoses whether success depends on surface forms.

Interface Reliance uses counterbalanced aliases to measure preference for known interface forms. The paper also tracks training dynamics, showing shortcut reliance can be environment-dependent and non-monotonic.

## Experiments and Evidence

The abstract reports evaluation across 16 environments from AgentBench and AgentGym, covering open-source and API-based agents. PIPE reveals sharp degradation for some trajectory-SFT agents under interface rewrites, and IR exposes shortcutting hidden by standard evaluation.

Full-paper reading should verify rewrite types, semantic preservation checks, agent list, SFT datasets, training checkpoints, and whether failures reflect parsing brittleness or deeper policy shortcutting.

## Limits and Failure Modes

Minimal interface rewrites must be carefully validated. If a rewrite subtly changes affordances or prompt clarity, degradation could be misattributed to interface reliance.

PIPE diagnoses one axis of generalization. Agents may still fail under semantic shifts, longer horizons, or tool errors even if they pass interface rewrites.

## Deep Themes

- Benchmark identifiability: task success alone does not reveal what capability was learned.
- Interface shortcutting: agents can memorize environment forms instead of tool semantics.
- Protocol-level evaluation: changing the wrapper while preserving task semantics exposes hidden brittleness.
- Non-monotonic training dynamics: more trajectory-SFT can sometimes increase shortcut reliance.

## Subthemes

- Alias-based counterbalancing gives a concrete interface-reliance metric.
- Trajectory data can overfit interaction patterns.
- Agent robustness requires environment-invariant competence.
- Standard benchmark scores can hide causal mechanism ambiguity.

## Connections to Other Papers

This paper connects strongly to MiniAppBench, Vision2Web, MAP, and AlgoVeri: all argue evaluation should exercise the real protocol rather than score superficial artifacts.

It also connects to performative misalignment because both identify evaluation confounds that can make behavioral scores misleading.

## Notes for Cross-Paper Synthesis

The synthesis point is that agent fine-tuning can overfit the interface layer. Future agent benchmarks need controlled perturbations that distinguish semantic skill from UI/API memorization.
