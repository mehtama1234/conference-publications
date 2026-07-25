# DR Tulu: Reinforcement Learning with Evolving Rubrics for Deep Research

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 97NEP1pyS3
- Authors: Rulin Shao; Akari Asai; Shannon Zejiang Shen; Hamish Ivison; Varsha Kishore; Jingming Zhuo; Xinran Zhao; Molly Park; Samuel G. Finlayson; David Sontag; Tyler Murray; Sewon Min; Pradeep Dasigi; Luca Soldaini; Faeze Brahman; Wen-tau Yih; Tongshuang Wu; Luke Zettlemoyer; Yoon Kim; Hannaneh Hajishirzi; Pang Wei Koh
- Primary area: deep_learning->large_language_models
- Keywords: deep research agent;reinforcement learning;rubric rewards;llm;search agent
- Source URL: https://openreview.net/forum?id=97NEP1pyS3
- PDF URL: https://openreview.net/pdf?id=97NEP1pyS3

## Abstract

Deep research agents perform multi-step research to produce long-form, well-attributed answers. However, most open deep research agents are trained on easily verifiable short-form QA tasks via reinforcement learning with verifiable rewards, which does not extend to realistic long-form tasks. We address this with Reinforcement Learning with Evolving Rubrics (RLER), where rubrics are constructed and maintained to co-evolve with the policy model during training. This allows the rubrics to incorporate newly explored information from search and contrasting model responses, enabling better fact checking and more discriminative on-policy feedback. Using RLER, we develop Deep Research Tulu (DR Tulu-8B), the first fully open model that is directly trained for open-ended, long-form deep research. Across four long-form deep research benchmarks in science, healthcare, and general domains, DR Tulu-8B substantially outperforms existing open deep research agents (by 15.6% over Tongyi DR on average) and matches or exceeds proprietary deep research agents (by 0.7% over OpenAI DR on average), while being significantly smaller and cheaper per query (1000x cheaper than OpenAI DR per query).

## One-Sentence Claim

DR Tulu trains an open deep-research agent with reinforcement learning from evolving rubrics that co-adapt with the policy during long-form search-based tasks.

## Problem

Open research agents are often trained with verifiable rewards on short-form QA, which does not transfer well to open-ended long-form answers requiring search, attribution, and synthesis.

## Core Contribution

The paper proposes Reinforcement Learning with Evolving Rubrics and uses it to train DR Tulu-8B, described as the first fully open model directly trained for long-form deep research.

## Method

RLER constructs and maintains rubrics during policy training. The rubrics incorporate newly explored search information and contrasting model responses, making on-policy feedback more discriminative and better suited to fact checking.

## Experiments and Evidence

The abstract reports results on four long-form deep-research benchmarks in science, healthcare, and general domains. DR Tulu-8B outperforms open deep-research agents by 15.6% over Tongyi DR on average, slightly exceeds OpenAI DR by 0.7% on average, and is reported as 1000x cheaper per query.

## Limits and Failure Modes

ArXiv search failed with HTTP 429 for this batch, so this note is abstract-only. Details still need checking: rubric generation safeguards, benchmark overlap, attribution quality scoring, healthcare-domain risk controls, and cost assumptions.

## Deep Themes

- Long-form agent training needs evaluators that evolve with policy capability.
- Rubrics can act as dynamic reward models for open-ended research.
- Open agents can be specialized for deep research through task-specific RL infrastructure.

## Subthemes

- Deep research agents.
- Reinforcement learning with rubrics.
- Search-based long-form QA.
- Fact checking.
- On-policy feedback.
- Open model agents.

## Connections to Other Papers

Connects to Reward and Guidance through Rubrics, Skill-Pro, Pareto tool-integrated agents, Copyright-Bench, and DRPBench through process-aware agent evaluation and training.

## Notes for Cross-Paper Synthesis

DR Tulu reinforces the rubric-as-infrastructure theme: for complex agent tasks, the evaluator must track what the agent discovers, not just compare to static answer keys.
