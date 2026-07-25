# LoongRL: Reinforcement Learning for Advanced Reasoning over Long Contexts

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: o29E01Q6bv
- Authors: Siyuan Wang; Gaokai Zhang; Li Lyna Zhang; Ning Shang; Fan Yang; Dongyao Chen; Mao Yang
- Primary area: foundation or frontier models, including LLMs
- Keywords: Long Context Reasoning;Reinforcement Learning
- Source URL: https://openreview.net/forum?id=o29E01Q6bv
- PDF URL: https://openreview.net/pdf?id=o29E01Q6bv

## Abstract

Reasoning over long contexts is essential for large language models. While reinforcement learning (RL) enhances short-context reasoning by inducing "Aha" moments in chain-of-thought, the advanced thinking patterns required for long-context reasoning  remain largely unexplored, and high-difficulty RL data are scarce. In this paper, we introduce LoongRL, a data-driven RL method for advanced long-context reasoning. Central to LoongRL is KeyChain,  a synthesis approach that transforms short multi-hop QA into high-difficulty long-context tasks by inserting UUID chains that hide the true question among large collections of distracting documents. Solving these tasks requires the model to trace the correct chain step-by-step, identify the true question,   retrieve relevant facts and reason over them to answer correctly. 
RL training on KeyChain data induces an emergent plan–retrieve–reason–recheck reasoning pattern that generalizes far beyond training length. Models trained at 16K effectively solve 128K tasks without prohibitive full-length RL rollout costs. On Qwen2.5-7B and 14B, LoongRL substantially improves long-context multi-hop QA accuracy by +23.5% and +21.1% absolute gains. The  resulting LoongRL-14B reaches a score of 74.2, rivaling much larger frontier models such as o3-mini (74.5) and DeepSeek-R1 (74.9). It  also improves long-context retrieval, passes all 128K needle-in-a-haystack stress tests, and preserves short-context reasoning capabilities.

## One-Sentence Claim

LoongRL trains long-context reasoning behavior with synthetic KeyChain tasks, inducing plan-retrieve-reason-recheck patterns that generalize from 16K training to 128K evaluation.

## Problem

RLVR improves short-context reasoning, but long-context reasoning requires different behaviors: locating hidden relevant chains, resisting distractors, retrieving facts, and rechecking answers over very large contexts. High-difficulty long-context RL data are scarce, and full-length rollouts are expensive.

## Core Contribution

The paper introduces LoongRL and KeyChain, a data synthesis method that turns short multi-hop QA into high-difficulty long-context tasks using UUID chains and distractor documents. It shows that RL on these tasks can teach advanced long-context reasoning patterns without prohibitive full-length rollout costs.

## Method

KeyChain hides the true question in a chain of UUID-linked documents mixed with distractors. During RL training, the model must trace the chain, identify the question, retrieve relevant facts, reason over them, and recheck. Training at 16K context is designed to generalize to much longer contexts.

## Experiments and Evidence

On Qwen2.5-7B and 14B, LoongRL reportedly improves long-context multi-hop QA by +23.5 and +21.1 absolute points. LoongRL-14B reaches 74.2, near o3-mini at 74.5 and DeepSeek-R1 at 74.9, passes all 128K needle-in-a-haystack stress tests, improves long-context retrieval, and preserves short-context reasoning.

## Limits and Failure Modes

UUID chains may simplify or distort the structure of natural long-context tasks. Models could learn artificial chain-following strategies that transfer unevenly to real documents. Full-text review should check benchmark diversity, rollout lengths, reward design, distractor construction, leakage, and whether plan-retrieve-reason-recheck is measured directly or inferred.

## Deep Themes

- RL for long-context reasoning processes.
- Synthetic curriculum construction for scarce hard tasks.
- Retrieval and reasoning as coupled long-context skills.
- Length generalization without full-length rollout.

## Subthemes

- KeyChain task synthesis.
- UUID-chain tracing.
- Plan-retrieve-reason-recheck behavior.
- 16K-to-128K extrapolation.
- Long-context multi-hop QA.

## Connections to Other Papers

Connects to MemAgent, In-Place TTT, Revela, and long-context SSM tool-use papers through context extrapolation, and to DECS through RL over reasoning process rather than only final-answer correctness.

## Notes for Cross-Paper Synthesis

LoongRL reinforces that long-context capability is a trained behavior, not just a longer window. The key unit is the interaction between data synthesis, RL signal, retrieval, and verification.
