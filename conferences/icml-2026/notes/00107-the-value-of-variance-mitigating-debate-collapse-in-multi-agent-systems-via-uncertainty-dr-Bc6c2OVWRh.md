# The Value of Variance: Mitigating Debate Collapse in Multi-Agent Systems via Uncertainty-Driven Policy Optimization

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: Bc6c2OVWRh
- Authors: Luoxi Tang; Yuqiao Meng; Joseph Costa; Yingxue Zhang; Muchao Ye; Zhaohan Xi
- Primary area: reinforcement_learning->multiagent
- Keywords: Multi-agent systems;Large Language Models (LLMs);Reasoning;Uncertainty estimation;Multi-agent debate;Calibration;Consensus / disagreement
- Source URL: https://openreview.net/forum?id=Bc6c2OVWRh
- PDF URL: https://openreview.net/pdf?id=Bc6c2OVWRh

## Abstract

Multi-agent debate (MAD) systems improve LLM reasoning through iterative deliberation, but remain vulnerable to debate collapse, a failure type where final agent decisions are compromised on erroneous reasoning. Existing methods lack principled mechanisms to detect or prevent such failures. To address this gap, we first propose a hierarchical metric that quantifies behavioral uncertainty at three levels: intra-agent (individual reasoning uncertainty), inter-agent (interactive uncertainty), and system-level (output uncertainty). Empirical analysis across several benchmarks reveals that our proposed uncertainty quantification reliably indicates system failures, which demonstrates the validity of using them as diagnostic metrics to indicate the system failure. Subsequently, we propose a mitigation strategy by formulating an uncertainty-driven policy optimization to penalize self-contradiction, peer conflict, and low-confidence outputs in a dynamic debating environment. Experiments demonstrate that our proposed uncertainty-driven mitigation reliably calibrates the multi-agent system by consistently improving decision accuracy while reducing system disagreement.

## One-Sentence Claim

Uncertainty at intra-agent, inter-agent, and system levels can diagnose and mitigate debate collapse in multi-agent LLM debate systems.

## Problem

Multi-agent debate can improve reasoning but may collapse when agents converge on erroneous reasoning, and existing systems lack principled failure diagnostics or prevention mechanisms.

## Core Contribution

The paper proposes hierarchical behavioral uncertainty metrics and an uncertainty-driven policy optimization method that penalizes self-contradiction, peer conflict, and low-confidence outputs.

## Method

It quantifies uncertainty across individual reasoning, interactive disagreement, and final system output, then uses these signals as policy-optimization penalties in dynamic debate environments.

## Experiments and Evidence

The abstract reports that uncertainty metrics reliably indicate system failures across benchmarks and that mitigation improves decision accuracy while reducing system disagreement.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: uncertainty estimators, debate protocols, benchmark diversity, calibration measures, and whether reducing disagreement can suppress useful dissent.

## Deep Themes

- Disagreement can be diagnostic signal rather than noise.
- Multi-agent systems need calibration at multiple interaction levels.
- Debate quality depends on maintaining useful variance while avoiding collapse.

## Subthemes

- Multi-agent debate.
- Debate collapse.
- Uncertainty estimation.
- Calibration.
- Policy optimization.
- Consensus and disagreement.

## Connections to Other Papers

Connects to MASPOB, OMAC, ParetoPO, non-cooperative LM safety games, and debate/value-of-variance papers through multi-agent process diagnostics.

## Notes for Cross-Paper Synthesis

This paper adds an uncertainty-as-control theme: variance across agents can reveal and correct collective reasoning failures.
