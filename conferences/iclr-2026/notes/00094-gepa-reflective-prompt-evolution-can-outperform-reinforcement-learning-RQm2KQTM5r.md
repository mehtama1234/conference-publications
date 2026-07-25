# GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: RQm2KQTM5r
- Authors: Lakshya A Agrawal; Shangyin Tan; Dilara Soylu; Noah Ziems; Rishi Khare; Krista Opsahl-Ong; Arnav Singhvi; Herumb Shandilya; Michael J Ryan; Meng Jiang; Christopher Potts; Koushik Sen; Alex Dimakis; Ion Stoica; Dan Klein; Matei Zaharia; Omar Khattab
- Primary area: foundation or frontier models, including LLMs
- Keywords: prompt optimization;natural language;reflection;large language models;agent design;agent discovery;code optimization;compound AI systems;genetic;language based learning;evolutionary algorithms
- Source URL: https://openreview.net/forum?id=RQm2KQTM5r
- PDF URL: https://openreview.net/pdf?id=RQm2KQTM5r

## Abstract

Large language models (LLMs) are increasingly adapted to downstream tasks via reinforcement learning (RL) methods like Group Relative Policy Optimization (GRPO), which often require thousands of rollouts to learn new tasks. We argue that the interpretable nature of language often provides a much richer learning medium for LLMs, compared to policy gradients derived from sparse, scalar rewards. To test this, we introduce GEPA (Genetic-Pareto), a prompt optimizer that thoroughly incorporates natural language reflection to learn high-level rules from trial and error.
    Given any AI system containing one or more LLM prompts, GEPA samples trajectories (e.g., reasoning, tool calls, and tool outputs) and reflects on them in natural language to diagnose problems, propose and test prompt updates, and combine complementary lessons from the Pareto frontier of its own attempts. As a result of GEPA's design, it can often turn even just a few rollouts into a large quality gain.
    Across four tasks, GEPA outperforms GRPO by 6% on average and by up to 20%, while using up to 35x fewer rollouts. GEPA also outperforms the leading prompt optimizer, MIPROv2, by over 10% (e.g., +10% accuracy on AIME-2025).

## One-Sentence Claim

GEPA uses natural-language reflection and Pareto-based prompt evolution to improve LLM systems with far fewer rollouts than reinforcement learning methods such as GRPO.

## Problem

LLM systems are often adapted with RL methods that require thousands of rollouts and learn from sparse scalar rewards.

For prompt-based compound AI systems, language itself may provide richer diagnostic information than policy gradients: trajectories can be inspected, failure causes named, and rules updated directly.

## Core Contribution

The paper introduces GEPA, Genetic-Pareto prompt optimization.

GEPA samples system trajectories, reflects on failures and successes in natural language, proposes prompt updates, tests them, and combines complementary lessons from the Pareto frontier of attempts.

## Method

Given one or more LLM prompts in an AI system, GEPA runs trials that include reasoning, tool calls, and tool outputs.

It then uses natural-language reflection to derive high-level rules, evolves prompt variants, and selects or combines candidates based on Pareto tradeoffs across performance dimensions.

## Experiments and Evidence

The abstract reports results across four tasks.

GEPA outperforms GRPO by 6 percent on average and up to 20 percent while using up to 35x fewer rollouts. It also beats MIPROv2 by more than 10 percent, including a 10 percent gain on AIME-2025.

## Limits and Failure Modes

Prompt evolution may be less effective when failures are not verbally diagnosable, when the system needs new model weights, or when prompts become brittle to distribution shift.

Because this note is abstract-only, details still need checking: tasks, Pareto objectives, reflection prompts, rollout budget, comparison fairness to GRPO, and whether improvements persist across hidden tests.

## Deep Themes

- Language as learning medium: reflection can encode reusable rules more efficiently than scalar rewards.
- Prompt optimization for compound systems: adaptation targets the system's instruction layer, not model parameters.
- Pareto-guided search: multiple prompt qualities are balanced instead of collapsed to one reward.
- Sample-efficient system improvement: few trajectories can produce large gains when error analysis is explicit.

## Subthemes

- Reflective prompt evolution.
- Genetic-Pareto search.
- Natural-language diagnostics.
- Rollout efficiency.

## Connections to Other Papers

This connects to AgentFlow, LongWriter-Zero, SafeDPO, and Train-before-Test through alternative adaptation routes.

It also relates to prompt/program optimization papers and agent benchmarks where system-level prompts control tool use and reasoning behavior.

## Notes for Cross-Paper Synthesis

GEPA adds a counterpoint to RL-heavy adaptation: for language-mediated systems, structured reflection can be a more data-efficient optimizer than gradient-based policy updates.
