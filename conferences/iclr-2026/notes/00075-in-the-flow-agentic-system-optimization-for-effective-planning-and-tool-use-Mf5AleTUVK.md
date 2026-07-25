# In-The-Flow Agentic System Optimization for Effective Planning and Tool Use

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: Mf5AleTUVK
- Authors: Zhuofeng Li; Haoxiang Zhang; Seungju Han; Sheng Liu; Jianwen Xie; Yu Zhang; Yejin Choi; James Zou; Pan Lu
- Primary area: applications to computer vision, audio, language, and other modalities
- Keywords: Reinforcement Learning;Large Language Models;Agentic Systems;Tool Use;Planning;On-policy Optimization;Sparse Rewards
- Source URL: https://openreview.net/forum?id=Mf5AleTUVK
- PDF URL: https://openreview.net/pdf?id=Mf5AleTUVK

## Abstract

Outcome-driven reinforcement learning has advanced reasoning in large language models (LLMs), but prevailing tool-augmented approaches train a single, monolithic policy that interleaves thoughts and tool calls under full context; this scales poorly with long horizons and diverse tools and generalizes weakly to new scenarios. Agentic systems offer a promising alternative by decomposing work across specialized modules, yet most remain training-free or rely on offline training decoupled from the live dynamics of multi-turn interaction. We introduce AgentFlow, a trainable, *in-the-flow* agentic framework that coordinates four modules (planner, executor, verifier, generator) through an evolving memory and directly optimizes its planner inside the multi-turn loop. To train on-policy in live environments, we propose *Flow-based Group Refined Policy Optimization* (Flow-GRPO), which tackles long-horizon, sparse-reward credit assignment by converting multi-turn optimization into a sequence of tractable single-turn policy updates. It broadcasts a single, verifiable trajectory-level outcome to every turn to align local planner decisions with global success and stabilizes learning with group-normalized advantages. Across ten benchmarks, AgentFlow with a 7B-scale backbone outperforms top-performing baselines with average accuracy gains of 14.9% on search, 14.0% on agentic, 14.5% on mathematical, and 4.1% on scientific tasks, even surpassing larger proprietary models like GPT-4o. Further analyses confirm the benefits of in-the-flow optimization, showing improved planning, enhanced tool-calling reliability, and positive scaling with model size and reasoning turns. Codebase is available at https://anonymous.4open.science/r/agentflow.

## One-Sentence Claim

AgentFlow trains a modular planner-executor-verifier-generator agent inside live multi-turn tool-use loops using Flow-GRPO for long-horizon sparse-reward credit assignment.

## Problem

Outcome-driven RL has improved LLM reasoning, but many tool-augmented methods train one monolithic policy that mixes thoughts and tool calls in full context.

That setup scales poorly to long horizons and diverse tools. Modular agentic systems are promising, but often remain training-free or are trained offline away from live multi-turn interaction dynamics.

## Core Contribution

The paper introduces AgentFlow, an in-the-flow trainable agentic system with four coordinated modules: planner, executor, verifier, and generator.

It also proposes Flow-based Group Refined Policy Optimization, which directly optimizes the planner during live multi-turn interaction.

## Method

AgentFlow coordinates its modules through evolving memory. The planner is optimized on-policy while the system interacts with live environments.

Flow-GRPO converts sparse trajectory-level rewards into tractable single-turn policy updates by broadcasting the final verifiable outcome to each turn and stabilizing learning with group-normalized advantages.

## Experiments and Evidence

The abstract reports results across ten benchmarks.

Using a 7B-scale backbone, AgentFlow outperforms top baselines with average gains of 14.9 percent on search, 14.0 percent on agentic tasks, 14.5 percent on mathematics, and 4.1 percent on scientific tasks, even surpassing GPT-4o in the reported setting. Analyses show improved planning, better tool-calling reliability, and positive scaling with model size and reasoning turns.

## Limits and Failure Modes

Broadcasting trajectory-level outcome rewards to every turn may credit local decisions too broadly when success depends on only a few key steps. Modular systems also introduce interface and memory-design choices that can become hidden sources of performance.

Because this note is abstract-only, details still need checking: module prompts/models, benchmark list, exact reward signals, live environment setup, Flow-GRPO derivation, and ablations separating planner learning from system design.

## Deep Themes

- On-policy agent optimization: agent systems are trained inside their actual interaction loop.
- Modular tool-use architecture: planning, execution, verification, and generation are separated into coordinated roles.
- Long-horizon sparse-reward credit assignment: final outcomes are converted into local planner updates.
- Tool reliability as a trainable behavior: agent performance depends on learning when and how to call tools.

## Subthemes

- AgentFlow.
- Planner-executor-verifier-generator architecture.
- Flow-GRPO.
- Live multi-turn optimization.

## Connections to Other Papers

This connects to AstaBench, SimuHome, MC-Search, Q-RAG, Gaia2, and WebDevJudge through the move from static answer evaluation to tool-using, process-aware agent systems.

It also relates to LongWriter-Zero because both use RL objectives to induce long-horizon behaviors from LLMs.

## Notes for Cross-Paper Synthesis

AgentFlow crystallizes a major agentic-systems pattern: long-horizon tool use needs optimization inside the workflow, not just prompting or offline imitation.
