# Reward and Guidance through Rubrics: Promoting Exploration to Improve Multi-Domain Reasoning

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: AfqsNFzJcs
- Authors: Baolong Bi; Shenghua Liu; Yiwei Wang; Siqian Tong; Lingrui Mei; Yuyao Ge; Yilong Xu; Jiafeng Guo; Xueqi Cheng
- Primary area: reinforcement_learning->policy_search
- Keywords: Reinforcement Learning;Large Language Models
- Source URL: https://openreview.net/forum?id=AfqsNFzJcs
- PDF URL: https://openreview.net/pdf?id=AfqsNFzJcs

## Abstract

Recent advances in reinforcement learning (RL) have significantly improved the complex reasoning capabilities of large language models (LLMs).
Despite these successes, existing methods mainly focus on single-domain RL (e.g., mathematics) with verifiable rewards (RLVR), and their reliance on purely online RL frameworks restricts the exploration space, thereby limiting reasoning performance.
In this paper, we address these limitations by leveraging rubrics to provide both fine-grained reward signals and offline guidance.
We propose $\textbf{RGR-GRPO}$ (Reward and Guidance through Rubrics), a rubric-driven RL framework for multi-domain reasoning. 
RGR-GRPO enables LLMs to receive dense and informative rewards while exploring a larger solution space during GRPO training.
Extensive experiments across 14 benchmarks spanning multiple domains demonstrate that RGR-GRPO consistently outperforms RL methods that rely solely on alternative reward schemes or offline guidance.
Compared with verifiable online RL baseline, RGR-GRPO achieves average improvements of +7.0%, +5.4%, +8.4%, and +6.6% on mathematics, physics, chemistry, and general reasoning tasks, respectively.
Notably, RGR-GRPO maintains stable entropy fluctuations during off-policy training and achieves superior pass@k performance, reflecting sustained exploration and effective breakthrough beyond existing performance bottlenecks.

## One-Sentence Claim

RGR-GRPO uses rubrics as both dense rewards and offline guidance to improve multi-domain LLM reasoning beyond purely verifiable online RL.

## Problem

LLM reasoning RL often focuses on single-domain verifiable tasks such as math, while purely online RL constrains exploration and limits performance in broader reasoning domains.

## Core Contribution

The paper proposes Reward and Guidance through Rubrics, a rubric-driven GRPO framework for multi-domain reasoning that combines informative reward signals with broader exploration guidance.

## Method

RGR-GRPO supplies dense rubric-based rewards and offline guidance during GRPO training, expanding the solution space explored while retaining reinforcement learning updates.

## Experiments and Evidence

The abstract reports consistent gains across 14 benchmarks, including average improvements over verifiable online RL of +7.0% math, +5.4% physics, +8.4% chemistry, and +6.6% general reasoning, plus stable entropy fluctuations and stronger pass@k.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition is deferred after repeated rate-limit failures. Details still need checking: rubric construction, reward hacking defenses, off-policy data source, domain balance, and pass@k evaluation setup.

## Deep Themes

- Rubrics can expand RL beyond binary verifiable rewards.
- Exploration quality matters for reasoning breakthroughs.
- Multi-domain reasoning needs dense process-aware supervision.

## Subthemes

- GRPO.
- Rubric rewards.
- Offline guidance.
- Multi-domain reasoning.
- Exploration.
- Pass@k.

## Connections to Other Papers

Connects to DR Tulu, MASPOB, ParetoPO, and alignment/evaluation papers through rubrics as training infrastructure for complex agent and reasoning behavior.

## Notes for Cross-Paper Synthesis

RGR-GRPO deepens the rubric theme: rubrics are not only evaluators; they are exploration guides for reasoning RL.
