# Skill-Pro: Learning Reusable Skills from Experience via Non-Parametric PPO for LLM Agents

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 9kJQjx2B80
- Authors: Qirui Mi; Zhijian Ma; Mengyue Yang; Haoxuan Li; Yisen Wang; Haifeng Zhang; Jun Wang
- Primary area: reinforcement_learning
- Keywords: LLM Agents;Skills;Procedural Memory;Non-Parametric Optimization;Experience Reuse
- Source URL: https://openreview.net/forum?id=9kJQjx2B80
- PDF URL: https://openreview.net/pdf?id=9kJQjx2B80

## Abstract

LLM-driven agents excel at sequential decision-making but often rely on on-the-fly reasoning, re-deriving solutions even in recurring scenarios. This insufficient experience reuse leads to computational redundancy and instability. To bridge this gap, we propose **Skill-Pro**, a framework enabling agents to autonomously learn reusable procedural skills from interaction experiences without parameter updates. By formalizing a **Skill-MDP**, Skill-Pro transforms passive episodic narratives into executable Skills defined by activation, execution, and termination conditions to ensure executability. 
To achieve reliable reusability without capability degradation, we introduce **Non-Parametric PPO**, which leverages semantic gradients for high-quality candidate generation and a PPO Gate for robust Skill verification. Through score-based maintenance, Skill-Pro sustains compact, high-quality procedural memory.
Experimental results across in-domain, cross-task, and cross-agent scenarios demonstrate that Skill-Pro achieves superior reuse rates and significant gains with extreme memory compression. Visualized evolutionary trajectories and Skill distributions further reveal how Skill-Pro transparently accumulates, refines, and reuses procedural knowledge to facilitate long-term autonomy.

## One-Sentence Claim

Skill-Pro lets LLM agents convert episodic experience into reusable executable skills without updating model parameters.

## Problem

LLM agents often solve recurring situations from scratch, creating redundant reasoning, unstable behavior, and poor long-term experience reuse.

## Core Contribution

The paper introduces Skill-Pro, a procedural-memory framework built around a Skill-MDP and Non-Parametric PPO for generating, verifying, maintaining, and reusing skills.

## Method

Skill-Pro transforms passive episodic narratives into executable skills with activation, execution, and termination conditions. Non-Parametric PPO uses semantic gradients to generate candidate skills and a PPO Gate to verify them, while score-based maintenance keeps a compact procedural memory.

## Experiments and Evidence

The abstract reports superior reuse rates and significant gains across in-domain, cross-task, and cross-agent scenarios, with extreme memory compression and visualized skill evolution.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv is currently being deferred after repeated 429/503 errors. Details still need checking: skill syntax, verification metrics, failure recovery, cross-agent transfer protocol, and memory-compression tradeoffs.

## Deep Themes

- Agent autonomy depends on procedural memory, not just on-the-fly reasoning.
- Experience reuse can be non-parametric and executable.
- Skills need activation and termination conditions to become reliable tools.

## Subthemes

- LLM agents.
- Procedural memory.
- Skill-MDP.
- Non-parametric PPO.
- Experience reuse.
- Long-term autonomy.

## Connections to Other Papers

Connects to DR Tulu, TTT-Discover, Neural Thickets, skill neologisms, and tool-integrated agents through reusable adaptation and agent-process optimization.

## Notes for Cross-Paper Synthesis

Skill-Pro reinforces the memory-as-capability theme: agents need to accumulate reusable procedures from experience rather than repeatedly re-derive actions.
