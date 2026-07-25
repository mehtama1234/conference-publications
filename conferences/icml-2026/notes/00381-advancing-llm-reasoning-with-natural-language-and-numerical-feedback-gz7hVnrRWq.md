# Advancing LLM Reasoning with Natural Language and Numerical Feedback

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: gz7hVnrRWq
- Authors: Xiaoying Zhang; Yipeng Zhang; Hao Sun; Kaituo Feng; Chaochao Lu; Chao Yang; Helen M. Meng
- Primary area: reinforcement_learning
- Keywords: LLM reasoning;reinforcement learning;natural language feedback
- Source URL: https://openreview.net/forum?id=gz7hVnrRWq
- PDF URL: https://openreview.net/pdf?id=gz7hVnrRWq

## Abstract

Recent advances in reinforcement learning (RL) using numerical rewards have significantly enhanced the complex reasoning capabilities of large language models (LLMs). However, we identify three fundamental limitations of purely numerical feedback: performance plateaus, ineffective spontaneous self-reflection, and persistent failures. We show that plateaued RL models can successfully refine failed solutions when given natural language critiques. Motivated by this, we propose Critique-GRPO, an online RL framework that integrates both natural language and numerical feedback for policy optimization. This approach enables LLMs to learn simultaneously from initial responses and critique-guided refinements, effectively internalizing the exploration benefits of both stages. Extensive experiments show that Critique-GRPO outperforms all compared supervised and RL-based fine-tuning methods, achieving average Pass@1 improvements of approximately +15.0-21.6% on various Qwen models and +7.3% on Llama-3.2-3B-Instruct across eight challenging reasoning tasks. Notably, Critique-GRPO facilitates effective self-improvement through self-critiquing, achieving substantial gains over GRPO, e.g., a +16.7% Pass@1 improvement on AIME 2024. The code and models are released at: https://github.com/zhangxy-2019/critique-GRPO

## One-Sentence Claim

Critique-GRPO improves LLM reasoning by combining numerical rewards with natural-language critiques, letting models learn from both failed initial attempts and critique-guided refinements.

## Problem

RL with numerical rewards has improved reasoning, but purely numeric feedback hits plateaus, does not reliably induce spontaneous self-reflection, and leaves persistent failure modes unresolved. The abstract reports that plateaued RL models can improve failed solutions when given natural-language critiques.

The problem is that scalar rewards say whether an answer worked but often not why it failed or how to repair it.

## Core Contribution

The paper introduces Critique-GRPO, an online RL framework that integrates natural-language and numerical feedback during policy optimization. It trains on both initial responses and critique-guided refinements so the policy can internalize the exploration benefits of external critique.

The method also enables self-improvement through self-critiquing, suggesting that critique behavior can become part of the learned reasoning process.

## Method

Critique-GRPO extends GRPO by adding a critique/refinement stage. Initial responses receive numerical feedback, while failed or improvable attempts are paired with natural-language critique and refined solutions. The policy learns from both trajectories.

This creates a richer reward channel: numerical correctness anchors the objective, while textual critique supplies directional repair information.

## Experiments and Evidence

Evidence reported in the abstract:

- Eight challenging reasoning tasks.
- Average Pass@1 gains of about 15.0-21.6% on various Qwen models.
- Average Pass@1 gain of 7.3% on Llama-3.2-3B-Instruct.
- Self-critiquing improves over GRPO, including +16.7% Pass@1 on AIME 2024.
- Outperforms compared supervised and RL-based fine-tuning methods.
- Code and models released at the listed GitHub URL.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: critique source, self-critique training schedule, reward construction, and baseline tuning.

## Limits and Failure Modes

- Natural-language critiques can be wrong, vague, or reward-hacking-prone.
- Self-critiquing may reinforce model misconceptions if critique quality is not controlled.
- Gains may depend on reasoning domains where critique text is actionable.
- Online RL with critique stages can increase training complexity and data cost.

## Deep Themes

**Scalar rewards are not enough.** Reasoning models need feedback that identifies failure causes and repair paths.

**Critique is exploration guidance.** Natural-language critique helps models move from failed trajectories to better alternatives.

**Self-reflection must be trained, not assumed.** The paper treats self-critique as a learned capability produced by the feedback loop.

## Subthemes

- Natural-language feedback for RL.
- Critique-guided refinement.
- GRPO extension.
- Self-critiquing reasoning models.
- Numerical-plus-textual reward channels.

## Connections to Other Papers

Connects to RePO, Hista/Numca, PRISM, MoCA, Weak-Strong Verification, and T2PO. It shares the theme that post-training improves when feedback is more structured than final binary or scalar reward.

## Notes for Cross-Paper Synthesis

Critique-GRPO adds a language-native feedback pattern: textual critique can act as a bridge between sparse reward and process-level learning.
