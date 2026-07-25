# T$^2$PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic Reinforcement Learning

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: aD1zjvdJN4
- Authors: Haixin Wang; Hejie Cui; Chenwei Zhang; Xin Liu; Shuowei Jin; Shijie Geng; Xinyang Zhang; Nasser Zalmout; Zhenyu Shi; Yizhou Sun
- Primary area: deep_learning->large_language_models
- Keywords: LLM Agent;Agentic RL
- Source URL: https://openreview.net/forum?id=aD1zjvdJN4
- PDF URL: https://openreview.net/pdf?id=aD1zjvdJN4

## Abstract

Recent progress in multi-turn reinforcement learning (RL) has significantly improved reasoning LLMs' performances on complex interactive tasks. 
Despite advances in stabilization techniques such as fine-grained credit assignment and trajectory filtering, instability remains pervasive and often leads to training collapse.
We argue that this instability stems from inefficient exploration in multi-turn settings, where policies continue to generate low-information actions that neither reduce uncertainty nor advance task progress.
To address this issue, we propose Token- and Turn-level Policy Optimization (T$^2$PO), an uncertainty-aware framework that explicitly controls exploration at fine-grained levels. At the token level, T$^2$PO monitors uncertainty dynamics and triggers a thinking intervention once  the marginal uncertainty change falls below a threshold. 
At the turn level, T$^2$PO identifies interactions with negligible exploration progress and dynamically resamples such turns to avoid wasted rollouts. 
We evaluate T$^2$PO in diverse environments, including WebShop, ALFWorld, and Search QA, demonstrating substantial gains in training stability and performance improvements with better exploration efficiency. Code is available at https://github.com/WillDreamer/T2PO.

## One-Sentence Claim

T2PO stabilizes multi-turn agentic RL by controlling exploration at token and turn levels based on uncertainty dynamics and exploration progress.

## Problem

Multi-turn RL improves reasoning agents on interactive tasks, but training remains unstable and can collapse. Existing stabilizers such as fine-grained credit assignment and trajectory filtering do not fully address inefficient exploration: agents keep producing low-information actions that neither reduce uncertainty nor advance progress.

The paper asks how to explicitly regulate exploration in multi-turn LLM-agent RL.

## Core Contribution

The paper proposes Token- and Turn-level Policy Optimization, an uncertainty-aware framework for exploration control. At token level, T2PO monitors uncertainty dynamics and triggers a thinking intervention when marginal uncertainty change falls below a threshold. At turn level, it detects interactions with negligible exploration progress and dynamically resamples those turns to avoid wasted rollouts.

The method improves training stability, performance, and exploration efficiency on WebShop, ALFWorld, and Search QA.

## Method

T2PO instruments the agent rollout with uncertainty measurements. When token generation stops reducing uncertainty, the framework intervenes to encourage additional thinking. When a turn contributes little exploration progress, the rollout is resampled so training focuses on more informative interactions.

This treats exploration as a measurable control process rather than an implicit byproduct of policy entropy.

## Experiments and Evidence

Evidence reported in the abstract:

- Evaluation on WebShop, ALFWorld, and Search QA.
- Improved multi-turn training stability.
- Better task performance.
- Better exploration efficiency.
- Token-level thinking intervention and turn-level dynamic resampling.
- Code release.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: uncertainty estimator, thresholds, RL algorithm, collapse diagnostics, and compute overhead from resampling.

## Limits and Failure Modes

- Uncertainty reduction may not always correlate with task progress.
- Thresholds could be environment- or model-specific.
- Resampling low-progress turns may reduce exposure to hard but necessary exploration.
- Extra monitoring and intervention can complicate agent training systems.

## Deep Themes

**Exploration must be progress-aware.** Token and turn decisions are judged by whether they reduce uncertainty or advance the task.

**Agentic RL needs runtime diagnostics.** Stability is improved by monitoring internal rollout quality.

**Thinking interventions are becoming control actions.** The model is prompted or guided to allocate cognition when uncertainty stagnates.

## Subthemes

- Multi-turn agentic RL.
- Token-level uncertainty dynamics.
- Turn-level exploration progress.
- Dynamic rollout resampling.
- Training-collapse prevention.

## Connections to Other Papers

Connects to R2VPO, PAVE, TG-RAG, Agent0-VL, and tau2-bench through process-controlled agent/RL systems. It also links to NAD because both use early internal signals to decide whether a reasoning trajectory is worth continuing.

## Notes for Cross-Paper Synthesis

T2PO extends the process-control theme into RL training: stable agent improvement requires measuring the information value of tokens and turns while the rollout is happening.
