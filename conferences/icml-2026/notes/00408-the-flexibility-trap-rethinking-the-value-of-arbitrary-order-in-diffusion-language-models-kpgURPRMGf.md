# The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: kpgURPRMGf
- Authors: Zanlin Ni; Shenzhi Wang; Yang Yue; Tianyu Yu; Weilin Zhao; Yeguo Hua; Tianyi Chen; Jun Song; Cheng Yu; Bo Zheng; Gao Huang
- Primary area: deep_learning->large_language_models
- Keywords: Diffusion Language Models;Reasoning;Reinforcement Learning;Large Language Models
- Source URL: https://openreview.net/forum?id=kpgURPRMGf
- PDF URL: https://openreview.net/pdf?id=kpgURPRMGf

## Abstract

Diffusion Large Language Models (dLLMs) break the rigid left-to-right constraint of traditional LLMs, enabling token generation in arbitrary orders. Intuitively, this flexibility implies a solution space that strictly supersets the fixed autoregressive trajectory, theoretically unlocking superior reasoning potential. However, in this paper, we find that for general reasoning tasks (e.g., mathematics and coding), arbitrary order generation may in fact limit the reasoning potential of dLLMs.
We observe that dLLMs tend to exploit this order flexibility to bypass high-uncertainty tokens that are crucial for exploration, which can lead to a premature collapse of solution coverage.
This observation motivates a rethink of RL approaches for dLLMs, where considerable complexities, such as handling combinatorial trajectories and intractable likelihoods, are often devoted to preserving this flexibility.
We show that effective reasoning can be elicited by simply forgoing arbitrary order and applying standard Group Relative Policy Optimization (GRPO) instead.
Our approach, JustGRPO, is minimalist yet surprisingly effective (e.g., 89.1\% accuracy on GSM8K) while fully retaining the parallel decoding ability of dLLMs. Code: https://github.com/LeapLabTHU/JustGRPO.

## One-Sentence Claim

For reasoning tasks, arbitrary-order diffusion language generation can hurt exploration by skipping high-uncertainty tokens, while standard GRPO with constrained order can perform better.

## Problem

Diffusion language models can generate tokens in arbitrary order, seemingly expanding the solution space beyond left-to-right autoregression. Many RL methods for dLLMs preserve this flexibility despite combinatorial trajectories and difficult likelihoods.

The paper asks whether arbitrary-order flexibility actually helps reasoning tasks such as math and coding.

## Core Contribution

The paper identifies a flexibility trap: dLLMs can exploit arbitrary order to bypass high-uncertainty tokens that are crucial for exploration, leading to premature collapse of solution coverage.

It proposes JustGRPO, a minimalist approach that forgoes arbitrary order and applies standard Group Relative Policy Optimization while retaining parallel decoding. The abstract reports 89.1% accuracy on GSM8K.

## Method

JustGRPO constrains the generation/training setup enough to avoid arbitrary-order trajectory complications, then applies standard GRPO to elicit reasoning. The method keeps dLLM parallel decoding but abandons the premise that order flexibility should be preserved for RL.

The analysis compares solution coverage and exploration behavior under arbitrary-order versus constrained-order generation.

## Experiments and Evidence

Evidence reported in the abstract:

- Observation that dLLMs bypass high-uncertainty tokens under arbitrary order.
- Premature collapse of solution coverage.
- JustGRPO applies standard GRPO while forgoing arbitrary order.
- 89.1% accuracy on GSM8K.
- Retains parallel decoding ability.
- Code released at the listed GitHub URL.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: dLLM model, tasks, ordering constraint, likelihood handling, and baselines.

## Limits and Failure Modes

- Arbitrary order may still help non-reasoning tasks such as infilling or editing.
- GSM8K accuracy alone is not enough to establish broad reasoning superiority.
- Constraining order could reduce diversity or controllability in some settings.
- The mechanism of uncertainty skipping needs fuller empirical characterization.

## Deep Themes

**Flexibility can undermine exploration.** More generation orders can let the model avoid hard decisions.

**Reasoning may need committed trajectories.** Hard tokens often carry the informative branching structure.

**Simpler RL can beat preserving theoretical generality.** JustGRPO favors practical training dynamics over maximal trajectory flexibility.

## Subthemes

- Diffusion language models.
- Arbitrary-order generation.
- GRPO for reasoning.
- Solution coverage collapse.
- Parallel decoding without order flexibility.

## Connections to Other Papers

Connects to Recurrent Diffusion Sampler, Critique-GRPO, Entropy Control, KPE/KTS, and test-time scaling papers. It is a useful counterpoint: not every expanded inference space improves reasoning.

## Notes for Cross-Paper Synthesis

This paper adds a constraint-as-capability theme: limiting a model's freedom can improve reasoning when freedom lets it avoid important uncertainty.
