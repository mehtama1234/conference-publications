# daVinci-Dev: Agent-native Mid-training for Software Engineering

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: a86luANykT
- Authors: Ji Zeng; Dayuan Fu; Tiantian Mi; Zhuang Yumin; Yaxing Huang; Xuefeng Li; Lyumanshan Ye; Muhang Xie; Qishuo Hua; Zhen Huang; Mohan Jiang; Hanning Wang; Jifan Lin; Yang Xiao; Jie Sun; Yunze Wu; Pengfei Liu
- Primary area: deep_learning->large_language_models
- Keywords: Mid-training;Software Engineering;Agent-native Mid-training;Large Language Models
- Source URL: https://openreview.net/forum?id=a86luANykT
- PDF URL: https://openreview.net/pdf?id=a86luANykT

## Abstract

While the emerging field of agentic software engineering has spurred extensive research into post-training, this paradigm alone does not fully address the distribution mismatch between traditional static pre-training and dynamic deployment environments. In this paper, we instead investigate agentic mid-training as a scalable complementary approach.
Central to our approach is *agent-native data* comprising two complementary components: *contextually-native trajectories* that preserve the complete information flow an agent experiences, offering broad coverage and diversity; and *environmentally-native trajectories* whose observations stem from actual tool invocations and test executions, providing interaction authenticity.
On `SWE-Bench Verified`, our recipe outperforms the previous open software engineering mid-training recipe `Kimi-Dev` under two post-training settings with the same base model and agentic scaffold, while using fewer than half mid-training tokens (73.1B).
Furthermore, our 32B and 72B models achieve state-of-the-art resolution rates of **56.1\%** and **58.5\%** among open agentic recipes using agentic scaffolds, despite starting from non-coder `Qwen2.5` base models.
We also observe performance gains on general code generation and scientific benchmarks.
We open-source a significant portion of our datasets, recipes, and model checkpoints to facilitate further research.

## One-Sentence Claim

daVinci-Dev shows that agent-native mid-training on contextually and environmentally native trajectories can substantially improve open software-engineering agents before post-training.

## Problem

Agentic software engineering is usually improved through post-training, but static pretraining data differs from dynamic deployment environments where agents inspect files, use tools, run tests, and revise code. This distribution mismatch limits what post-training alone can fix.

The paper asks whether mid-training on agent-native trajectories can provide a scalable bridge between generic pretraining and agentic deployment.

## Core Contribution

The paper introduces an agentic mid-training recipe built on two trajectory types:

- Contextually-native trajectories preserve the full information flow experienced by an agent, giving broad coverage and diversity.
- Environmentally-native trajectories come from actual tool invocations and test executions, giving authentic interaction evidence.

Using fewer than half the mid-training tokens of Kimi-Dev, the recipe improves SWE-Bench Verified under the same base model and scaffold. Its 32B and 72B models reach 56.1 percent and 58.5 percent resolution rates among open agentic recipes from non-coder Qwen2.5 bases.

## Method

The method curates and trains on trajectories that resemble software-agent deployment rather than static code text alone. Contextually-native data records the observations and context flow needed to make decisions. Environmentally-native data grounds actions in real tool and test outputs.

Mid-training happens before post-training, shaping the base model toward agentic software workflows.

## Experiments and Evidence

Evidence reported in the abstract:

- SWE-Bench Verified comparisons against Kimi-Dev under two post-training settings.
- Fewer than half the mid-training tokens, 73.1B.
- 32B model reaches 56.1 percent resolution rate.
- 72B model reaches 58.5 percent resolution rate.
- Gains on general code generation and scientific benchmarks.
- Open-sourced datasets, recipes, and checkpoints in significant part.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: data construction, scaffolds, contamination controls, post-training recipes, and exact benchmark protocol.

## Limits and Failure Modes

- Agent-native data may be expensive to collect and verify.
- SWE-Bench performance is scaffold-sensitive.
- Tool trajectories can encode brittle environment assumptions.
- Open-sourcing only part of the recipe may limit reproducibility.

## Deep Themes

**Agent capability needs native process data.** Static code corpora do not capture tool use, tests, and iterative debugging.

**Mid-training is a major control point.** The recipe improves downstream post-training by changing the model before alignment.

**Environment authenticity matters.** Real tool outputs and test executions provide supervision that synthetic static examples cannot.

## Subthemes

- Agent-native mid-training.
- Contextually-native trajectories.
- Environmentally-native trajectories.
- SWE-Bench Verified.
- Software-engineering tool use.

## Connections to Other Papers

Connects to TerminalTraj, TG-RAG, Scientific Annotation BC, and Procedural Pretraining through process/trajectory data. It also links to Pre/Mid/RL Reasoning because both show mid-training can be as important as RL post-training.

## Notes for Cross-Paper Synthesis

daVinci-Dev reinforces the long-running data theme: for agents, the unit of training data is not a document but a situated trajectory with observations, actions, and consequences.
