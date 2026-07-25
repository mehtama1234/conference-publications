# What You Think is What You See: Driving Exploration in VLM Agents via Visual-Linguistic Curiosity

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: zWStW3hrfW
- Authors: Haoxi Li; Qinglin Hou; Jianfei Ma; Jinxiang Lai; Tao Han; Sikai Bai; Jingcai Guo; Jie ZHANG; Song Guo
- Primary area: reinforcement_learning->deep_rl
- Keywords: Curiosity Driven VLM Agentic RL Training
- Source URL: https://openreview.net/forum?id=zWStW3hrfW
- PDF URL: https://openreview.net/pdf?id=zWStW3hrfW

## Abstract

To navigate partially observable visual environments, recent VLM agents increasingly internalize world modeling capabilities directly into their policies via explicit CoT reasoning with reinforcement learning (RL). However, mere passive exploitation of reasoning on visited states is insufficient for sparse-reward agentic tasks, as it lacks the epistemic drive to actively uncover the *known unknown* required for robust generalization. We ask: *Can VLM agents actively find signals that challenge and update their internal world model through curiosity-driven exploration?* In this work, we propose **GLANCE**, a unified framework that bridges reasoning and exploration by grounding the agent's linguistic world model into the stable visual representations of an evolving target network. Crucially, **GLANCE** leverages the discrepancy between linguistic prediction and visual reality as an intrinsic curiosity signal within reinforcement learning, steering the agent to actively explore areas where its internal model is uncertain. Extensive experiments across a series of agentic tasks show the effectiveness of **GLANCE**, and demonstrate that aligning *what the agent thinks* with *what the agent sees* is key to solving complex or sparse agentic tasks.

## One-Sentence Claim

GLANCE drives VLM-agent exploration by turning mismatch between linguistic world-model predictions and visual reality into an intrinsic curiosity reward.

## Problem

VLM agents in partially observable visual environments increasingly use CoT reasoning and RL to internalize world models. But passive exploitation of visited states is not enough for sparse-reward tasks.

The agent needs an epistemic drive to seek observations that challenge and update its internal world model, especially the known unknowns required for generalization.

## Core Contribution

The paper proposes GLANCE, a framework that connects reasoning and exploration by grounding the agent's linguistic world model in stable visual representations from an evolving target network.

Its central contribution is a visual-linguistic curiosity signal: discrepancy between what the agent predicts linguistically and what it sees visually becomes intrinsic reward.

## Method

GLANCE compares linguistic predictions from the agent's internal world model with visual representations from a target network. Discrepancy signals uncertainty or model mismatch.

During RL, this discrepancy steers exploration toward states where the agent's internal model is incomplete or wrong, encouraging active world-model improvement.

## Experiments and Evidence

The abstract reports extensive experiments across a series of agentic tasks showing GLANCE's effectiveness.

It emphasizes that aligning what the agent thinks with what it sees is key for complex or sparse-reward tasks.

## Limits and Failure Modes

Curiosity rewards can be distracted by noisy, irrelevant, or visually surprising but task-useless states. The linguistic-visual discrepancy must distinguish productive uncertainty from perceptual noise.

Because this note is abstract-only, details still need checking: task suite, VLM architecture, target-network update rule, discrepancy metric, reward weighting, and whether curiosity causes unsafe or inefficient exploration.

## Deep Themes

- Curiosity from cross-modal prediction error: exploration is driven by mismatch between language beliefs and visual evidence.
- World-model repair: agents should seek observations that update internal models.
- Partially observable agentic RL: reasoning alone is insufficient without epistemic exploration.
- Stable visual grounding: target networks can anchor linguistic speculation.

## Subthemes

- Visual-linguistic curiosity.
- Sparse-reward VLM agents.
- CoT-grounded world models.
- Known-unknown exploration.

## Connections to Other Papers

This connects to L2T, VectorWorld, and Beyond Language Modeling through world-model formation. It also relates to POPGym and linear recurrent memory because partial observability requires active information gathering.

It links to Ctrl-R and RAGEN-2 through RL-shaped reasoning, but focuses on exploration rather than reasoning trajectory diversity or collapse.

## Notes for Cross-Paper Synthesis

GLANCE adds active epistemic control to the agent theme: robust agents must not only reason over observations, but choose observations that expose their own uncertainty.
