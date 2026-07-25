# RAGEN-2: Reasoning Collapse in Agentic RL

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 01caH9oj7C
- Authors: Zihan Wang; Chi Gui; Xing Jin; Qineng Wang; Licheng Liu; Kangrui Wang; Shiqi Chen; Linjie Li; Zhengyuan Yang; Pingyue Zhang; Yiping Lu; Jiajun Wu; Li Fei-Fei; Lijuan Wang; Yejin Choi; Manling Li
- Primary area: deep_learning->foundation_models
- Keywords: multi-turn reinforcement learning;LLM agents;PPO;GRPO;reasoning collapse;mutual information;conditional entropy;information-theoretic diagnostics;reward-variance filtering
- Source URL: https://openreview.net/forum?id=01caH9oj7C
- PDF URL: https://openreview.net/pdf?id=01caH9oj7C

## Abstract

RL training of multi-turn LLM agents is unstable, and reasoning quality drives task performance. Entropy, the standard reasoning-stability monitor, only measures within-input diversity and misses whether reasoning depends on the input. We identify **template collapse**: stable entropy alongside input-agnostic boilerplate, invisible to entropy and existing metrics. We diagnose it via a **mutual-information (MI) proxy** that scores cross-input distinguishability online; across tasks, MI correlates with final performance far more strongly than entropy. We then explain collapse via a **signal-to-noise ratio (SNR)** mechanism: low within-input reward variance weakens task gradients, letting input-agnostic regularization dominate and erase cross-input differences. We mitigate this with **SNR-Aware Filtering**, prioritizing high-variance prompts each iteration. Across planning, math reasoning, web navigation, and code execution, the method consistently improves input dependence and task performance.

## One-Sentence Claim

RAGEN-2 identifies template collapse in multi-turn LLM-agent RL, diagnoses it with a mutual-information proxy, and mitigates it by filtering for high reward-variance prompts.

## Problem

RL training for multi-turn LLM agents is unstable, and standard entropy monitoring can miss a damaging failure mode where outputs remain superficially diverse but become input-agnostic boilerplate.

## Core Contribution

The paper introduces template collapse as a reasoning-specific RL failure mode, proposes an online mutual-information proxy for detecting whether reasoning depends on the input, explains collapse through a signal-to-noise mechanism, and proposes SNR-Aware Filtering.

## Method

The diagnostic measures cross-input distinguishability rather than only within-input entropy. The mitigation prioritizes prompts with higher within-input reward variance during RL iterations so task gradients remain strong enough to preserve input-dependent reasoning.

## Experiments and Evidence

The abstract reports that MI correlates with final performance more strongly than entropy across tasks, and that SNR-Aware Filtering improves input dependence and task performance across planning, math reasoning, web navigation, and code execution.

## Limits and Failure Modes

PDF checks needed: sensitivity of the MI proxy to generation sampling settings, whether reward-variance filtering biases task distributions, compatibility with different RL algorithms, and whether template collapse appears outside agentic/multi-turn settings.

## Deep Themes

- Agentic RL needs process diagnostics, not just final reward or entropy.
- Reasoning quality is being operationalized through input dependence.
- Training instability is linked to weak task signal versus regularization pressure.

## Subthemes

- LLM agents.
- Multi-turn reinforcement learning.
- Reasoning collapse.
- Mutual-information diagnostics.
- Reward-variance filtering.

## Connections to Other Papers

Connects to test-time/process evaluation, reasoning benchmarks, agent safety, and interpretability work that looks for internal or behavioral signals of meaningful reasoning rather than fluent output.

## Notes for Cross-Paper Synthesis

This paper gives strong evidence for a broader pattern: as LLM systems become interactive agents, the field needs diagnostics for whether behavior remains conditioned on the task context rather than collapsing into generic templates.
