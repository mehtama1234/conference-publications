# Hista and Numca: Estimate State Value Effectively for Large Language Model Reinforcement Learning

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: ff4b0ELdU0
- Authors: Zizhe Chen; Jiqian Dong; Yizhou Tian; Garry YANG; Yongqiang Chen; Zhitang Chen; James Cheng
- Primary area: deep_learning->large_language_models
- Keywords: Reinforcement Learning;Large Language Model;State Value Estimation
- Source URL: https://openreview.net/forum?id=ff4b0ELdU0
- PDF URL: https://openreview.net/pdf?id=ff4b0ELdU0

## Abstract

Reinforcement learning (RL) refines large language models (LLMs) by directly optimizing model behavior through reward signals. While accurate state value estimation is critical for stable training in classical RL, it remains an underexplored challenge in LLM post‑training. In this work, we introduce the State Value Estimation Benchmark (SVEB) to assess state estimation within existing RL frameworks and show that critics in standard approaches like PPO collapse to a coarse group‑average baseline. To address this, we propose two techniques: \textit{Numca}, which leverages numerical spans as gradable milestones for state value estimation, and \textit{Hista}, a framework that uses LLM's hidden states as representation to weighted average disjoint rollouts and their return. Extensive experiments demonstrate that both methods yield more accurate state value estimates and enhance training performance across different RL algorithms and model sizes without incurring significant computational overhead. Code available at \url{https://github.com/VOXXXX1874/Hista}.

## One-Sentence Claim

Hista and Numca improve LLM reinforcement learning by giving state-value estimators finer intermediate signal than the coarse group-average critics used by standard PPO-style training.

## Problem

Stable RL depends on accurate state-value estimation, but LLM post-training often treats value estimation as a secondary detail. The paper argues that standard critics in approaches such as PPO collapse to coarse group-average baselines, leaving little useful token- or state-level guidance.

The core problem is that language trajectories are long, sparse-reward, and semantically structured, so classical value heads may not learn meaningful intermediate values.

## Core Contribution

The paper introduces the State Value Estimation Benchmark (SVEB) to evaluate value estimation in LLM RL. It then proposes two techniques: Numca, which uses numerical spans as gradable milestones, and Hista, which uses hidden-state representations to weighted-average disjoint rollouts and returns.

Both methods improve value-estimate accuracy and downstream RL training across algorithms and model sizes without major computational overhead.

## Method

Numca exploits numerical spans as intermediate, gradable anchors for state value estimation. This is especially relevant for math and reasoning tasks where partial numerical progress can be assessed before the final answer.

Hista represents states using the LLM's hidden states and estimates value by weighting disjoint rollouts according to representational similarity and observed returns. This turns hidden-state geometry into a value-estimation prior.

## Experiments and Evidence

Evidence reported in the abstract:

- SVEB benchmark for state value estimation in LLM RL.
- Diagnosis that standard PPO critics collapse to coarse group-average baselines.
- Numca and Hista produce more accurate state value estimates.
- Training performance improves across different RL algorithms and model sizes.
- No significant computational overhead.
- Code release at the listed GitHub URL.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: SVEB construction, tasks, value metrics, RL algorithms, and overhead.

## Limits and Failure Modes

- Numca depends on tasks with numerical spans or similarly gradable milestones.
- Hista's hidden-state similarity may be misleading when semantically different states are representationally close.
- Value-estimation improvements may not transfer to open-ended reward settings.
- Better critics can optimize flawed rewards more aggressively if reward design is weak.

## Deep Themes

**LLM RL needs process values, not only final rewards.** Intermediate state value is a missing training signal in many post-training pipelines.

**Hidden states become credit-assignment geometry.** Hista uses the model's own representations to share return information across rollouts.

**Benchmarks are moving inside the training loop.** SVEB evaluates a component that is normally hidden behind final reward curves.

## Subthemes

- State value estimation for LLM RL.
- PPO critic collapse.
- Numerical-span milestones.
- Hidden-state rollout averaging.
- Process-level credit assignment.

## Connections to Other Papers

Connects to T2PO, UDM-GRPO, MoCA, Weak-Strong Verification, and NAD. It shares the broader theme of using internal or intermediate process signals to control long reasoning trajectories.

## Notes for Cross-Paper Synthesis

Hista/Numca adds a reinforcement-learning version of the process-localization theme: stronger post-training may require knowing how good a partial reasoning state is, not merely whether the final answer got reward.
