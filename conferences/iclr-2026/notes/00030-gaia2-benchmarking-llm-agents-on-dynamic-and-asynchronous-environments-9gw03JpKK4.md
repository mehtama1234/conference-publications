# Gaia2: Benchmarking LLM Agents on Dynamic and Asynchronous Environments

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: 9gw03JpKK4
- Authors: Romain Froger; Pierre Andrews; Matteo Bettini; Amar Budhiraja; Ricardo Silveira Cabral; Virginie Do; Emilien Garreau; Jean-Baptiste Gaya; Hugo Laurençon; Maxime Lecanu; Kunal Malkan; Dheeraj Mekala; Pierre Menard; Gerard Moreno-Torres Bertran; Ulyana Piterbarg; Mikhail Plekhanov; Mathieu Rita; Andrey Rusakov; Vladislav Vorotilov; Mengjue Wang; Ian Yu; Amine Benhalloum; Grégoire Mialon; Thomas Scialom
- Primary area: datasets and benchmarks
- Keywords: benchmark;agents;rlvr;multi-agent systems;reasoning;large language models;evaluation;framework
- Source URL: https://openreview.net/forum?id=9gw03JpKK4
- PDF URL: https://openreview.net/pdf?id=9gw03JpKK4

## Abstract

We introduce **Gaia2**, a benchmark for evaluating large language model agents in realistic, asynchronous environments. Unlike prior static or synchronous evaluations, Gaia2 introduces scenarios where environments evolve independently of agent actions, requiring agents to operate under temporal constraints, adapt to noisy and dynamic events, resolve ambiguity, and collaborate with other agents. Each scenario is paired with a write-action verifier, enabling fine-grained, action-level evaluation and making Gaia2 directly usable for reinforcement learning from verifiable rewards. Our evaluation of state-of-the-art proprietary and open-source models shows that no model dominates across capabilities: GPT-5 (high) reaches the strongest overall score of 42% pass@1 but fails on time-sensitive tasks, Claude-4 Sonnet trades accuracy and speed for cost, Kimi-K2 leads among open-source models with 21% pass@1. These results highlight fundamental trade-offs between reasoning, efficiency, robustness, and expose challenges in closing the “sim2real” gap. Gaia2 is built on a consumer environment with the open-source **Agents Research Environments** platform and designed to be easy to extend. By releasing Gaia2 alongside the foundational ARE framework, we aim to provide the community with a flexible infrastructure for developing, benchmarking, and training the next generation of practical agent systems.

## One-Sentence Claim

Gaia2 benchmarks LLM agents in dynamic asynchronous environments where time, noise, ambiguity, and multi-agent collaboration expose capability tradeoffs hidden by static evaluations.

## Problem

Many agent benchmarks are static or synchronous: the environment waits for the agent and changes only in response to explicit actions. Realistic environments evolve independently and impose temporal constraints.

The problem is to evaluate agents under noisy dynamic events, ambiguity, time-sensitive decisions, and collaboration demands.

## Core Contribution

The paper introduces Gaia2, a benchmark and infrastructure for evaluating LLM agents in realistic asynchronous environments.

Each scenario includes a write-action verifier, enabling fine-grained action-level evaluation and direct use for reinforcement learning from verifiable rewards.

## Method

Gaia2 scenarios run in environments that evolve independently of agent actions. Agents must adapt to asynchronous events and collaborate with other agents while satisfying task-specific verifiers.

The benchmark is built on the open-source Agents Research Environments platform and is designed to be extendable.

## Experiments and Evidence

The abstract reports evaluation of proprietary and open-source models. GPT-5 high has the strongest overall score at 42 percent pass@1 but fails on time-sensitive tasks. Claude-4 Sonnet trades accuracy and speed for cost. Kimi-K2 leads open-source models with 21 percent pass@1.

No model dominates across capabilities, revealing tradeoffs among reasoning, efficiency, and robustness.

## Limits and Failure Modes

Benchmark conclusions depend on scenario design, verifier quality, and the realism of the asynchronous environment. Agent performance can be sensitive to tool interfaces and cost budgets.

Because this note is abstract-only, details still need checking: task taxonomy, number of scenarios, verifier implementation, timing model, multi-agent protocol, cost accounting, and sim-to-real validation.

## Deep Themes

- Dynamic agent evaluation: real environments change while agents think.
- Action-level verifiability: write-action verifiers make agent behavior trainable with RLVR.
- Capability tradeoff surfaces: reasoning, speed, robustness, and cost cannot be collapsed into one score.
- Sim-to-real gap for agents: benchmark environments must approximate practical deployment dynamics.

## Subthemes

- Asynchronous environments.
- Temporal constraints.
- Multi-agent collaboration.
- Agents Research Environments infrastructure.

## Connections to Other Papers

This connects to MiniAppBench, CyberGym, CounselBench, and Copyright-Bench through realistic evaluation. It also connects to GLANCE, Ctrl-R, and RLVR optimizer work because action-level verifiers can become training signals.

It belongs in the agent-infrastructure cluster: reliable agents need dynamic evaluation surfaces, not only static tasks.

## Notes for Cross-Paper Synthesis

Gaia2 reinforces the deployment-realism theme: agent benchmarks need independent environment dynamics, time pressure, and verifiable actions to reveal practical failures.
