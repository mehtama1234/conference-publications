# MASPOB: Bandit-Based Prompt Optimization for Multi-Agent Systems with Graph Neural Networks

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: A5venxSvpw
- Authors: Zhi Hong; Qian Zhang; Jiahang Sun; Zhiwei Shang; Mingze Kong; Xiangyi Wang; Yao Shu; Zhongxiang Dai
- Primary area: deep_learning->large_language_models
- Keywords: Large Language Models;Multi-Agent System
- Source URL: https://openreview.net/forum?id=A5venxSvpw
- PDF URL: https://openreview.net/pdf?id=A5venxSvpw

## Abstract

Large Language Models (LLMs) have achieved substantial success in real-world applications, particularly as the cognitive backbone of Multi-Agent Systems (MAS) for orchestrating complex workflows. Since many deployments preclude workflow modifications while MAS performance is highly prompt-sensitive, prompt optimization becomes a critical strategy for improvement. However, real-world prompt optimization for MAS is impeded by three key challenges: (1) the need of sample efficiency due to prohibitive evaluation costs, (2) topology-induced coupling among prompts, and (3) the combinatorial explosion of the search space. To address these challenges, we introduce **MASPOB** (**M**ulti-**A**gent **S**ystem **P**rompt **O**ptimization via **B**andits), a novel sample-efficient framework based on bandits. By leveraging Upper Confidence Bound (UCB) to quantify uncertainty, the bandit framework balances exploration and exploitation, maximizing gains within a strictly limited budget. To handle topology-induced coupling, MASPOB integrates Graph Neural Networks (GNNs) to capture structural priors, learning topology-aware representations of prompt semantics. Furthermore, it employs coordinate ascent to decompose the optimization into univariate sub-problems, reducing search complexity from exponential to linear. Extensive experiments across diverse benchmarks demonstrate that MASPOB achieves state-of-the-art performance, consistently outperforming existing baselines. Our code is available at <https://github.com/HZ1008/MASPOB>.

## One-Sentence Claim

MASPOB optimizes prompts in fixed multi-agent workflows using bandits, graph neural networks, and coordinate ascent for sample-efficient topology-aware search.

## Problem

Multi-agent system performance is prompt-sensitive, but real deployments may forbid workflow changes and make prompt evaluation expensive; agent topology also couples prompt effects.

## Core Contribution

The paper introduces Multi-Agent System Prompt Optimization via Bandits, a sample-efficient framework that handles topology-induced coupling and combinatorial prompt search.

## Method

MASPOB uses UCB bandits to balance exploration and exploitation, GNNs to encode workflow topology and prompt semantics, and coordinate ascent to reduce prompt optimization from exponential combinatorial search to linear univariate subproblems.

## Experiments and Evidence

The abstract reports state-of-the-art performance across diverse benchmarks, consistently outperforming existing baselines.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition is deferred after repeated rate-limit failures. Details still need checking: benchmark workflows, prompt candidate generation, evaluation budgets, GNN architecture, and robustness to topology changes.

## Deep Themes

- Multi-agent systems need optimization over prompts even when workflow topology is fixed.
- Agent graphs create coupled prompt effects.
- Sample efficiency matters because evaluating agent workflows is expensive.

## Subthemes

- Multi-agent systems.
- Prompt optimization.
- Bandits.
- Graph neural networks.
- Coordinate ascent.
- Workflow topology.

## Connections to Other Papers

Connects to OMAC, ParetoPO, DR Tulu, and tool-integrated agent work through optimization of agent processes under evaluation-cost constraints.

## Notes for Cross-Paper Synthesis

MASPOB adds a topology-aware agent-optimization theme: prompts are not independent strings when agents interact through a workflow graph.
