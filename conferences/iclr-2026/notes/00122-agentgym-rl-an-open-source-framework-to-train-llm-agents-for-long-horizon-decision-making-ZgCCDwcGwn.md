# AgentGym-RL: An Open-Source Framework to Train LLM Agents for Long-Horizon Decision Making via Multi-Turn RL

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: ZgCCDwcGwn
- Authors: Zhiheng Xi; Jixuan Huang; Chenyang Liao; Baodai Huang; Jiaqi Liu; Honglin Guo; yajie yang; Rui Zheng; Junjie Ye; Jiazheng Zhang; Wenxiang Chen; Wei He; Yiwen Ding; Guanyu Li; Zehui Chen; Zhengyin Du; Xuesong Yao; Yufei Xu; Jiecao Chen; Tao Gui; Zuxuan Wu; Qi Zhang; Xuanjing Huang; Yu-Gang Jiang
- Primary area: applications to computer vision, audio, language, and other modalities
- Keywords: large language model;LLM-based agent;decision-making
- Source URL: https://openreview.net/forum?id=ZgCCDwcGwn
- PDF URL: https://openreview.net/pdf?id=ZgCCDwcGwn

## Abstract

Training LLM agents for complex multi-turn decision-making tasks requires extensive exploration within their environment, with reinforcement learning (RL) as a natural way. However, the open-source community currently lacks a unified RL framework capable of training agents from scratch across diverse and realistic environments. To bridge this gap, we introduce AgentGym-RL, a modular and decoupled framework specifically designed for RL-based agent in multi-turn decision-making tasks. It offers high flexibility and extensibility, supports mainstream RL algorithms, and spans a broad range of real-world scenarios. To effectively train agents for challenging tasks, we argue that they are required to expand external interactions with the environment, rather than relying solely on internal reasoning. Nevertheless, training agents for long-horizon interaction with vanilla methods often faces challenges like training instability. To this end, we propose ScalingInter-RL, a staged training approach for stable long-horizon RL training. It starts with short-horizon interaction to establish foundational policies and progressively expands them to encourage deeper exploration. Extensive experiments show that agents trained with our method achieve performance on par with—or even surpass—commercial counterparts like OpenAI o3 and Gemini-2.5-Pro across 27 tasks in diverse environments. We share key insights and will release the full framework, including code and datasets, to empower the community in building the next generation of intelligent agents.

## One-Sentence Claim

AgentGym-RL provides a modular open-source framework for training LLM agents with multi-turn RL, using staged interaction scaling to stabilize long-horizon decision making.

## Problem

Training LLM agents for realistic multi-turn tasks requires extensive environment exploration. The open-source ecosystem lacks a unified RL framework that trains agents from scratch across diverse environments.

Vanilla long-horizon RL can be unstable, especially when agents must rely on external interactions rather than internal reasoning alone.

## Core Contribution

The paper introduces AgentGym-RL, a modular and decoupled framework for RL-based agent training in multi-turn decision-making tasks.

It also proposes ScalingInter-RL, a staged training approach that starts with short-horizon interactions and progressively expands toward deeper exploration.

## Method

AgentGym-RL supports mainstream RL algorithms and diverse real-world scenarios.

ScalingInter-RL builds foundational policies on shorter interactions before increasing interaction horizon, reducing instability while encouraging agents to explore the environment more extensively.

## Experiments and Evidence

The abstract reports experiments across 27 tasks in diverse environments.

Agents trained with the framework perform on par with or surpass commercial systems such as OpenAI o3 and Gemini-2.5-Pro in the reported settings.

## Limits and Failure Modes

Framework comparisons can be sensitive to environment selection, backbone models, reward design, and tool access. Long-horizon RL may still overfit to benchmark environments.

Because this note is abstract-only, details still need checking: task suite, algorithms supported, reward definitions, staged schedule, baselines, model backbones, and compute cost.

## Deep Themes

- Open-source agent RL infrastructure: agent training needs shared frameworks, not only isolated benchmarks.
- External interaction scaling: agents improve by expanding environment contact, not only by longer hidden reasoning.
- Curriculum for interaction horizon: staged horizon growth stabilizes long-horizon RL.
- Decoupled modular training: framework design matters for reproducible agent research.

## Subthemes

- Multi-turn RL.
- Long-horizon decision making.
- ScalingInter-RL.
- Agent training framework.

## Connections to Other Papers

This connects to AgentFlow, SimuHome, AstaBench, SwingArena, and weak-to-strong monitoring through agent training and evaluation.

It also relates to multi-turn conversation failure work because both emphasize interaction dynamics over single-turn aptitude.

## Notes for Cross-Paper Synthesis

AgentGym-RL adds an infrastructure theme: scalable agent progress needs standardized training loops that expose agents to external environments over increasing horizons.
