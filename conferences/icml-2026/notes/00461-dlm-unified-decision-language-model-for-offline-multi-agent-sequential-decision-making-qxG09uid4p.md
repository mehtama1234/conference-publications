# DLM: Unified Decision Language Model for Offline Multi-Agent Sequential Decision Making

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: qxG09uid4p
- Authors: Zhuohui Zhang; Bin Cheng; Bin He
- Primary area: reinforcement_learning->multiagent
- Keywords: Decision Language Model;Offline Multi-Agent Reinforcement Learning;Large Language Models
- Source URL: https://openreview.net/forum?id=qxG09uid4p
- PDF URL: https://openreview.net/pdf?id=qxG09uid4p

## Abstract

Building scalable and reusable multi-agent decision policies from offline datasets remains a challenge in offline multi-agent reinforcement learning (MARL), as existing methods often rely on fixed observation formats and action spaces that limit generalization. In contrast, large language models (LLMs) offer a flexible modeling interface that can naturally accommodate heterogeneous observations and actions. Motivated by this, we propose the Decision Language Model (DLM), which formulates multi-agent decision making as a dialogue-style sequence prediction problem under the centralized training with decentralized execution paradigm. DLM is trained in two stages: a supervised fine-tuning phase, which leverages dialogue-style datasets for centralized training with inter-agent context and generates executable actions from offline trajectories, followed by a group relative policy optimization phase to enhance robustness to out-of-distribution actions through lightweight reward functions. Experiments on multiple benchmarks show that a unified DLM outperforms strong offline MARL baselines and LLM-based conversational decision-making methods, while demonstrating strong zero-shot generalization to unseen scenarios across tasks.

## One-Sentence Claim

DLM turns offline multi-agent sequential decision making into dialogue-style sequence prediction, enabling one reusable language-model policy to handle heterogeneous observations/actions and generalize zero-shot across tasks.

## Problem

Offline multi-agent RL often depends on fixed observation formats and action spaces. That makes learned policies brittle when tasks, agents, communication formats, or executable actions vary across environments.

LLMs offer a flexible interface for heterogeneous information, but converting multi-agent trajectories into reliable executable decisions requires more than conversational prompting. The model must learn centralized context while supporting decentralized execution.

## Core Contribution

The paper proposes Decision Language Model, a unified framework that represents multi-agent decision making as dialogue-style sequence prediction under centralized training with decentralized execution.

DLM combines supervised fine-tuning on dialogue-style trajectory data with group relative policy optimization using lightweight rewards to improve robustness to out-of-distribution actions. The contribution is to bridge offline MARL and LLM sequence modeling in one reusable policy interface.

## Method

In the first stage, DLM uses supervised fine-tuning on offline trajectories converted into dialogue-style data, where inter-agent context is available during centralized training and the model learns to emit executable actions.

In the second stage, GRPO improves robustness to OOD actions through lightweight reward functions. The deployment setting follows decentralized execution, so each agent must act from its available context despite training benefiting from centralized information.

## Experiments and Evidence

The abstract reports experiments across multiple benchmarks where a unified DLM outperforms strong offline MARL baselines and LLM-based conversational decision-making methods. It also demonstrates strong zero-shot generalization to unseen scenarios across tasks.

Full-paper reading should verify benchmark diversity, action serialization, reward design for GRPO, decentralized-execution protocol, and whether the method handles continuous or only discrete action spaces.

## Limits and Failure Modes

Language serialization can hide task-specific assumptions. If observations or actions are poorly represented as text, the LLM interface may introduce ambiguity or invalid actions.

Offline MARL is also vulnerable to dataset coverage limits, coordination failures, and distribution shift. GRPO with lightweight rewards can improve robustness but may not solve severe extrapolation beyond offline trajectories.

## Deep Themes

- Decision making as language modeling: heterogeneous multi-agent trajectories are converted into a common dialogue interface.
- Centralized training, decentralized execution for LLM policies: language models absorb shared context but must act locally.
- Offline RL plus post-training: SFT supplies behavior cloning, while GRPO improves action robustness.
- Reusable policy interfaces: LLMs become adapters across observation and action schemas.

## Subthemes

- Dialogue formatting is an alignment layer for multi-agent trajectories.
- Zero-shot task transfer is the central payoff of unification.
- Lightweight rewards make RL refinement feasible after SFT.
- Executable action generation is stricter than natural-language planning.

## Connections to Other Papers

DLM connects to JitRL, SOL, ScaleMoE, and WestWorld as another route to scalable decision-making. JitRL adapts agents at test time; DLM trains a reusable offline MARL language policy; SOL scales temporal hierarchy.

It also relates to MiniAppBench and Vision2Web through the shift from text output to executable artifacts or actions.

## Notes for Cross-Paper Synthesis

DLM strengthens the theme that language is becoming an interoperability layer for decision systems. The risk is that linguistic flexibility must still compile into valid, robust actions.
