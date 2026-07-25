# BIRD-INTERACT: Re-imagining Text-to-SQL Evaluation via Lens of Dynamic Interactions

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: nHrYBGujps
- Authors: Nan Huo; Xiaohan Xu; Jinyang Li; Per Jacobsson; Shipei Lin; Bowen Qin; Binyuan Hui; Xiaolong Li; Ge Qu; Shuzheng Si; Linheng Han; Edward Alexander; Xintong Zhu; Rui Qin; Ruihan Yu; Yiyao Jin; Feige Zhou; Weihao Zhong; Yun Chen; Hongyu Liu; Chenhao Ma; Fatma Ozcan; Yannis Papakonstantinou; Reynold Cheng
- Primary area: datasets and benchmarks
- Keywords: Interactive;Text-to-SQL;LLM;Code Generation
- Source URL: https://openreview.net/forum?id=nHrYBGujps
- PDF URL: https://openreview.net/pdf?id=nHrYBGujps

## Abstract

Large language models (LLMs) have demonstrated remarkable performance on single-turn text-to-SQL tasks, but real-world database applications predominantly require multi-turn interactions to handle ambiguous queries, execution errors, and evolving user requirements. Existing multi-turn benchmarks fall short of capturing this complexity, either by treating conversation histories as static context or by limiting evaluation to narrow, read-only (SELECT-ONLY) operations, thereby failing to reflect the challenges encountered in production-grade database assistant. In this work, we introduce BIRD-INTERACT, a benchmark that restores this missing realism through: (1) a ***comprehensive interaction environment*** that couples each database with a hierarchical knowledge base, metadata files, and a function-driven user simulator, enabling models to solicit clarifications, retrieve knowledge, and recover from execution errors without human supervision; (2) two ***evaluation settings*** reflecting real-world interaction settings which contain a pre-defined conversational protocol (c-Interact) and a more open-ended agentic setting (a-Interact) in which the model autonomously decides when to query the user simulator or explore the DB environment; (3) a ***challenging task suite*** that covers the full CRUD spectrum for both business-intelligence and operational use cases, guarded by executable test cases. Each task features ambiguous and follow-up sub-tasks, requiring LLMs to engage in dynamic interaction. The suite is organized into two sets: a full set (**BIRD-INTERACT-FULL**) of 600 tasks which unfold up to **11,796** dynamic interactions for a comprehensive overview of performance and a lite set (**BIRD-INTERACT-LITE**) of 300 tasks, with simplified databases for detailed behavioral analysis of interactions, and fast development of methods. Our empirical results highlight the difficulty of BIRD-INTERACT: the most recent flagship model GPT-5 completes only **8.67%** of tasks in the c-Interact setting and **17.00%** in the a-Interact setting on the full task suite. Further analysis via memory grafting and Interaction Test-time Scaling (ITS), validate the importance of effective interaction for achieving success in complex, dynamic text-to-SQL tasks.

## One-Sentence Claim

BIRD-INTERACT evaluates text-to-SQL agents in dynamic multi-turn database environments with clarification, retrieval, error recovery, CRUD operations, and executable tests, exposing large gaps in current flagship models.

## Problem

Single-turn text-to-SQL benchmarks miss production realities: user requests are ambiguous, requirements evolve, SQL execution can fail, and database assistants must sometimes ask clarifying questions or inspect metadata. Existing multi-turn benchmarks often treat history as static context or restrict tasks to SELECT-only queries.

## Core Contribution

The paper introduces BIRD-INTERACT, a benchmark with database environments, hierarchical knowledge bases, metadata, a function-driven user simulator, two interaction settings, full CRUD task coverage, and executable test cases. It includes full and lite task suites for comprehensive evaluation and fast behavioral analysis.

## Method

BIRD-INTERACT couples each database with supporting knowledge and a user simulator. In c-Interact, models follow a predefined conversational protocol. In a-Interact, agents decide when to query the simulator or explore the DB environment. Tasks include ambiguous and follow-up subtasks, and correctness is checked with executable tests.

## Experiments and Evidence

The full benchmark has 600 tasks and up to 11,796 dynamic interactions; the lite suite has 300 tasks. The abstract reports GPT-5 completing only 8.67 percent of tasks in c-Interact and 17.00 percent in a-Interact on the full suite, with memory grafting and Interaction Test-time Scaling analyses showing the importance of interaction quality.

## Limits and Failure Modes

Simulator behavior and executable tests define what counts as successful interaction, so realism depends on user-simulator fidelity and task design. CRUD evaluation can raise safety concerns if actions mutate state. Full-text review should check database domains, test-case coverage, simulator prompts/functions, error handling, and whether scores separate SQL ability from agent orchestration.

## Deep Themes

- Dynamic executable evaluation for database agents.
- Interaction quality as a text-to-SQL bottleneck.
- Agentic clarification and environment exploration.
- Production-grade CRUD evaluation.

## Subthemes

- Function-driven user simulators.
- c-Interact versus a-Interact settings.
- Hierarchical DB knowledge bases.
- Execution-error recovery.
- Interaction test-time scaling.

## Connections to Other Papers

Connects to OpenApps, Gaia2, CyberGym, and MedAgentGym through executable agent benchmarks, to SQL/code-generation papers through tool-use evaluation, and to memory/process papers through multi-turn interaction control.

## Notes for Cross-Paper Synthesis

BIRD-INTERACT reinforces a major benchmark trend: static answer accuracy is insufficient for agents. Realistic evaluation increasingly requires dynamic environments, executable tests, and analysis of the interaction policy itself.
