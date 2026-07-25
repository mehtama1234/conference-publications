# SimuHome: A Temporal- and Environment-Aware Benchmark for Smart Home LLM Agents

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: LCS1WsGvha
- Authors: Gyuhyeon Seo; Jungwoo Yang; Junseong Pyo; Nalim Kim; Jonggeun Lee; Yohan Jo
- Primary area: datasets and benchmarks
- Keywords: smart home;simulator;language model;language agent;benchmark
- Source URL: https://openreview.net/forum?id=LCS1WsGvha
- PDF URL: https://openreview.net/pdf?id=LCS1WsGvha

## Abstract

Large Language Model (LLM) agents excel at multi-step, tool-augmented tasks. However, smart homes introduce distinct challenges, requiring agents to handle latent user intents, temporal dependencies, device constraints, scheduling, and more.
The main bottlenecks for developing smart home agents with such capabilities include the lack of a realistic simulation environment where agents can interact with devices and observe the results, as well as a challenging benchmark to evaluate them.
To address this, we introduce $\textbf{SimuHome}$, a time-accelerated home environment that simulates smart devices, supports API calls, and reflects changes in environmental variables.
By building the simulator on the Matter protocol, the global industry standard for smart home communication, SimuHome provides a high-fidelity environment, and agents validated in SimuHome can be deployed on real Matter-compliant devices with minimal adaptation.
We provide a challenging benchmark of 600 episodes across twelve user query types that require the aforementioned capabilities.
Our evaluation of 16 agents under a unified ReAct framework reveals distinct capabilities and limitations across models. Models under 7B parameters exhibited negligible performance across all query types. Even GPT-4.1, the best-performing standard model, struggled with implicit intent inference, state verification, and particularly temporal scheduling. While reasoning models such as GPT-5.1 consistently outperformed standard models on every query type, they required over three times the average inference time, which can be prohibitive for real-time smart home applications. This highlights a critical trade-off between task performance and real-world practicality. We will release our code and dataset upon publication of the paper.

## One-Sentence Claim

SimuHome benchmarks smart-home LLM agents in a time-accelerated Matter-based simulator that tests temporal reasoning, device constraints, implicit intent inference, and real-time practicality.

## Problem

Smart-home agents face constraints that generic tool-use benchmarks often miss: latent user intent, temporal dependencies, device state changes, scheduling, environmental variables, and real-world protocol constraints.

The field lacks a realistic interactive simulator where agents can issue device API calls, observe resulting state changes, and be evaluated on behavior that transfers toward real smart-home deployments.

## Core Contribution

The paper introduces SimuHome, a time-accelerated smart-home simulation environment built on the Matter protocol.

It also provides a benchmark with 600 episodes across twelve user-query types and evaluates 16 agents under a unified ReAct framework.

## Method

SimuHome simulates smart devices, API calls, environmental variables, and temporal progression. By grounding the simulator in Matter, it aims to make policies and agent interfaces closer to real device ecosystems.

The benchmark episodes probe user-intent inference, temporal scheduling, state verification, and device constraints under a common ReAct interaction loop.

## Experiments and Evidence

The abstract reports evaluation of 16 agents.

Models below 7B parameters show negligible performance. GPT-4.1 is the best standard model but struggles with implicit intent, state verification, and especially temporal scheduling. Reasoning models such as GPT-5.1 perform better across all query types but require more than three times the average inference time.

## Limits and Failure Modes

Simulation fidelity is crucial: a Matter-based simulator improves realism, but real homes include noisy sensors, user ambiguity, device failures, security constraints, and heterogeneous vendor behavior.

Because this note is abstract-only, details still need checking: twelve query types, scoring, environment dynamics, exact agent prompts/tools, latency measurements, and whether real-device validation is included.

## Deep Themes

- Situated agent evaluation: agents are judged inside changing environments, not static text tasks.
- Temporal and stateful reasoning: smart-home control depends on future scheduling and verification after action.
- Standards-aligned simulation: Matter provides a bridge from benchmark API calls to deployable device interactions.
- Capability-latency tradeoff: stronger reasoning models may be too slow for real-time home automation.

## Subthemes

- Smart-home simulator.
- Matter protocol.
- ReAct agents.
- Temporal scheduling and state verification.

## Connections to Other Papers

This connects to MC-Search, Gaia2, WebDevJudge, ASTABench, and In the Flow through agent evaluation that measures process and environmental interaction.

It also relates to GLANCE and robotics benchmarks because all require agents to update beliefs from observations rather than solve isolated prompts.

## Notes for Cross-Paper Synthesis

SimuHome strengthens the embodied-agent benchmark theme: practical agents must trade reasoning quality against latency while operating under real API and environment constraints.
