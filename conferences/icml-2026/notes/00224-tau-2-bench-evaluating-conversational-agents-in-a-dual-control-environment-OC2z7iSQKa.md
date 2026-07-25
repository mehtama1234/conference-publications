# $\tau^2$-Bench: Evaluating Conversational Agents in a Dual-Control Environment

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: OC2z7iSQKa
- Authors: Victor Barres; Honghua Dong; Soham Ray; Xujie Si; Karthik R Narasimhan
- Primary area: applications
- Keywords: Benchmark;Evaluation;Dual Control;Conversational AI Agents;User Simulation
- Source URL: https://openreview.net/forum?id=OC2z7iSQKa
- PDF URL: https://openreview.net/pdf?id=OC2z7iSQKa

## Abstract

Existing benchmarks for conversational AI agents simulate _single-control_ environments, where only the AI agent can use tools to interact with the world, while the user remains a passive information provider. This differs from real-world scenarios like technical support, where users need to actively participate in modifying the state of the (shared) world. In order to address this gap, we introduce $\tau^2$-bench, with four key contributions:

(1) A novel Telecom dual-control domain modeled as a Dec-POMDP, where both agent and user make use of tools to act in a shared, dynamic environment that tests both agent coordination and communication;
(2) A compositional task generator that programmatically creates diverse, verifiable tasks from atomic components, ensuring domain coverage and controlled complexity;
(3) A reliable user simulator tightly coupled with the environment, whose behavior is constrained by tools and observable states, improving simulation fidelity;
(4) Fine-grained analysis of agent performance through multiple ablations including separating errors arising from reasoning vs communication/coordination.

In particular, our experiments show significant performance drops when agents shift from no-user to dual-control, highlighting the challenges of guiding users. Overall, $\tau^2$-bench provides a controlled testbed for agents that must both reason effectively and guide user actions. Code, data, and leaderboard are available at https://taubench.com/.

## One-Sentence Claim

tau2-bench evaluates conversational agents in dual-control environments where both user and AI can act with tools in a shared dynamic world.

## Problem

Most conversational-agent benchmarks use single-control environments where only the AI acts and the user passively supplies information, unlike real support settings where users must also modify world state.

## Core Contribution

The paper introduces a Telecom Dec-POMDP dual-control domain, a compositional verifiable task generator, a tool-constrained user simulator, and fine-grained analysis separating reasoning from communication/coordination errors.

## Method

tau2-bench programmatically builds tasks from atomic components, couples a user simulator to environment tools and observable state, and tests whether agents can reason while guiding user actions in a shared environment.

## Experiments and Evidence

The abstract reports significant performance drops when agents move from no-user to dual-control settings, exposing the difficulty of guiding active users.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: task generator coverage, user-simulator fidelity, telecom-domain realism, Dec-POMDP specification, leaderboard baselines, and transfer beyond support-like domains.

## Deep Themes

- Agent evaluation must model active users, not passive query providers.
- Coordination and communication failures differ from reasoning failures.
- Verifiable simulated environments can test shared-world tool use.

## Subthemes

- Conversational agents.
- Dual control.
- User simulation.
- Dec-POMDP.
- Tool use.
- Verifiable task generation.

## Connections to Other Papers

Connects to MEnvAgent, CE-Graph, MemoryBench, and agent workflow evaluation papers through executable/verifiable environments and process diagnostics.

## Notes for Cross-Paper Synthesis

tau2-bench adds a human-in-the-loop environment theme: real agents must coordinate with users who can also act, so benchmark worlds need shared control dynamics.
