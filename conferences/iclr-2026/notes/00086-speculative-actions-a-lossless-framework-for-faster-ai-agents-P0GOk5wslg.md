# Speculative Actions: A Lossless Framework for Faster AI Agents

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: P0GOk5wslg
- Authors: Naimeng Ye; Arnav Ahuja; Georgios Liargkovas; Yunan Lu; Kostis Kaffes; Tianyi Peng
- Primary area: infrastructure, software libraries, hardware, systems, etc.
- Keywords: AI Agents;Speculative Decoding;Parallel Execution;Agentic Serving;Agentic Simulation
- Source URL: https://openreview.net/forum?id=P0GOk5wslg
- PDF URL: https://openreview.net/pdf?id=P0GOk5wslg

## Abstract

AI agents have attracted growing interest across industry and academia, but in practice their execution can be slow. For example, letting two state-of-the-art agents play a game of chess may take hours. A key bottleneck is that agent behavior unfolds sequentially: each action requires an API call, and these calls can be time-consuming. Inspired by speculative execution in microprocessors and speculative decoding in LLM inference, we propose speculative actions—a lossless framework that predicts likely actions using faster models, enabling multiple API calls to be executed in parallel. We evaluate this framework across four agentic environments: gaming, e-commerce, web search, and operating systems. In all cases, speculative actions yield substantial acceleration, with potential speedups of up to 30%. Moreover, performance can be further improved through stronger guessing models and top-K action prediction, opening a promising path toward real world, efficient deployment of AI agents.

## One-Sentence Claim

Speculative Actions accelerates sequential AI agents by predicting likely next actions with faster models and executing multiple API calls in parallel while preserving lossless behavior.

## Problem

AI agents can be slow because their behavior unfolds as a serial chain of API calls. Each action depends on previous observations, so long-horizon tasks can take excessive wall-clock time.

This is a serving problem for agents: even if the policy is capable, deployment suffers when external calls, tool execution, and environment latency accumulate.

## Core Contribution

The paper proposes speculative actions, inspired by speculative execution and speculative decoding.

Fast guessing models predict likely actions, allowing multiple candidate API calls to execute in parallel. The framework is described as lossless, meaning acceleration does not change the final accepted agent behavior.

## Method

Speculative Actions runs likely future actions ahead of time. When the main agent reaches a decision point, precomputed action results can be accepted if they match the selected trajectory.

The framework can use stronger guessing models and top-K action prediction to increase the chance that speculative parallel work is useful.

## Experiments and Evidence

The abstract reports evaluations across four agentic environments: gaming, e-commerce, web search, and operating systems.

Speculative actions yield substantial acceleration, with possible speedups up to 30 percent. Performance improves with better guessing models and top-K action prediction.

## Limits and Failure Modes

Speculation wastes compute when guessed actions are wrong, and parallel API calls may be expensive or unsafe in real systems if actions have side effects. Losslessness likely depends on separating reversible or simulated calls from committed external actions.

Because this note is abstract-only, details still need checking: acceptance rule, side-effect handling, environment interfaces, speedup accounting, cost overhead, and whether speculation changes tool-rate limits.

## Deep Themes

- Agentic serving: tool-using agents need runtime systems, not only better policies.
- Lossless wall-clock acceleration: parallelism speeds sequential workflows without changing accepted behavior.
- Speculation as agent infrastructure: ideas from processors and LLM decoding transfer to multi-action agents.
- Prediction-quality dependent speedup: faster execution depends on forecasting the agent's next actions well enough.

## Subthemes

- Speculative execution.
- Parallel API calls.
- Agentic serving.
- Top-K action prediction.

## Connections to Other Papers

This connects to HSD, ThinKV, and TileLang through inference and serving acceleration.

It also connects to AgentFlow, SimuHome, WebDevJudge, and AstaBench because those agent systems expose the latency and side-effect constraints speculative actions targets.

## Notes for Cross-Paper Synthesis

Speculative Actions extends the efficiency theme from token generation to agent workflows: long-horizon tool use needs runtime parallelism as well as better reasoning.
