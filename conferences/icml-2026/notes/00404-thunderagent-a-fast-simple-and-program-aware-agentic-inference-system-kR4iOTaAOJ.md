# ThunderAgent: A Fast, Simple, and Program-Aware Agentic Inference System

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: kR4iOTaAOJ
- Authors: Hao Kang; Ziyang li; Weili Xu; Xinyu Yang; Yinfang Chen; Junxiong Wang; Beidi Chen; Tushar Krishna; Chenfeng Xu; Simran Arora
- Primary area: deep_learning->large_language_models
- Keywords: LLM Agent;machine learning system;Scheduler;efficient machine learning;LLM reinforcement learning
- Source URL: https://openreview.net/forum?id=kR4iOTaAOJ
- PDF URL: https://openreview.net/pdf?id=kR4iOTaAOJ

## Abstract

Large language models (LLMs) are now used to power complex multi-turn agentic workflows. Existing systems run agentic inference by loosely assembling isolated components: an LLM inference engine (e.g., vLLM) and a tool orchestrator (e.g., Kubernetes). Although agentic workflows involve multiple LLM and tool requests, these systems schedule and allocate resources separately on a per-request basis, without end-to-end knowledge of the workflow. This leads to sub-optimal management of KV cache and tool execution environments. To address the challenges, we propose **ThunderAgent**, a fast, simple, and program-aware agentic inference system. We first abstract agentic workflows as ***LLM Programs***, enabling a unified view of heterogeneous resources, including KV caches, system states, and external tool assets such as disk memory and network ports. Built upon this abstraction, ThunderAgent introduces a program-aware scheduler and a tool resource manager designed to maximize KV cache hit rates, mitigate memory imbalances, and enable asynchronous environment preparation. Evaluations across coding, routing, and scientific discovery agents demonstrate that ThunderAgent achieves **1.5-3.6×** throughput improvements in serving, **1.8-3.9×** in RL rollout, and up to **4.2×** disk memory savings compared to state-of-the-art inference systems. To facilitate reproducibility and support future development, we open-source the system implementations of ThunderAgent at: https://github.com/ThunderAgent-org/ThunderAgent

## One-Sentence Claim

ThunderAgent speeds multi-turn agentic inference by treating workflows as LLM Programs and scheduling KV cache, tool environments, and external assets with end-to-end program awareness.

## Problem

Agentic workflows involve multiple LLM calls and tool invocations, but current serving systems often stitch together separate inference engines and tool orchestrators. They schedule per request, without understanding the whole workflow.

This loses opportunities to reuse KV cache, balance memory, and prepare tool environments asynchronously.

## Core Contribution

ThunderAgent introduces the LLM Program abstraction, giving the system a unified view of heterogeneous resources: KV caches, system states, disk memory, network ports, and other tool assets.

Built on that abstraction, it adds a program-aware scheduler and tool resource manager to improve cache hit rates, reduce memory imbalance, and prepare environments asynchronously.

## Method

The system represents an agent workflow as a program with known or discoverable dependencies between LLM and tool steps. The scheduler uses this structure to coordinate LLM serving and tool resources, rather than treating each request independently.

The tool manager handles external assets such as disk and ports as first-class schedulable resources alongside GPU/KV memory.

## Experiments and Evidence

Evidence reported in the abstract:

- Evaluations across coding, routing, and scientific discovery agents.
- 1.5-3.6x throughput improvements in serving.
- 1.8-3.9x throughput improvements in RL rollout.
- Up to 4.2x disk memory savings.
- Improved KV cache hit rates, memory balance, and asynchronous environment preparation.
- Open-source system implementation at the listed GitHub URL.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: workload definitions, baseline systems, scheduler overhead, and failure isolation.

## Limits and Failure Modes

- Program-aware scheduling may require workflow structure that not all agents expose cleanly.
- Tool environments can be unpredictable or stateful in ways that complicate scheduling.
- Gains may vary with workload mix, cache reuse patterns, and tool latency.
- System complexity can make debugging harder than request-level orchestration.

## Deep Themes

**Agent workflows need program-level systems.** Per-request serving misses structure across multi-step workflows.

**Tools are resources, not side effects.** Disk, ports, environments, and state must be scheduled alongside model inference.

**Serving and RL rollout share infrastructure needs.** Agent training and deployment both benefit from end-to-end workflow awareness.

## Subthemes

- Program-aware agent serving.
- LLM Program abstraction.
- KV cache scheduling.
- Tool resource management.
- RL rollout throughput.

## Connections to Other Papers

Connects to CONTINUUM, daVinci-Dev, RoTS, Agent0-VL, and BlitzRank. It expands the systems-infrastructure theme from tensor memory to whole agent workflows.

## Notes for Cross-Paper Synthesis

ThunderAgent reinforces that agent capability depends on runtime systems: complex workflows need schedulers that understand the program, not only the next prompt.
