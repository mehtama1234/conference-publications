# OpenApps: Simulating Environment Variations to Measure UI Agent Reliability

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: cj1MAx7lKs
- Authors: Karen Ullrich; Jingtong Su; Claudia Shi; Arjun Subramonian; Amir Bar; Ivan Evtimov; Nikolaos Tsilivis; Randall Balestriero; Julia Kempe; Mark Ibrahim
- Primary area: datasets and benchmarks
- Keywords: reinforcement learning;agents;envrionment;reliability
- Source URL: https://openreview.net/forum?id=cj1MAx7lKs
- PDF URL: https://openreview.net/pdf?id=cj1MAx7lKs

## Abstract

Reliability is key to realizing the promise of autonomous UI-agents, multimodal agents that directly interact with the apps humans use, as users must be able to trust an agent to complete a given task. Current evaluations rely on fixed environments---often clones of existing apps--- which are limited in that they can only shed light on whether or how often an agent can complete a task within a specific environment. When deployed however, agents are likely to encounter variations in app design and content that can affect an agent’s ability to complete a task. To address this blind spot of measuring agent reliability across app variations, we develop OpenApps, a light-weight open-source ecosystem with six apps (messenger, calendar, maps, etc.) that are configurable in appearance and content. OpenApps requires just a single CPU to run, enabling easy generation and deployment of thousands of versions of each app. Specifically, we run more than 10,000 independent evaluations to study reliability across seven leading multimodal agents. We find that while standard reliability within a fixed app is relatively stable, reliability can vary drastically when measured across app variations. Task success rates for many agents can fluctuate by more than 50\% across app variations. For example, Kimi-VL-3B's average success across all tasks fluctuates from 63\% to just 4\% across app versions. We also find agent behaviors such as looping or hallucinating actions can differ drastically depending on the environment configuration. These initial findings highlight the importance of measuring reliability along this new dimension of app variations.

## One-Sentence Claim

OpenApps measures UI-agent reliability across configurable app variations, showing fixed-environment success can hide large robustness failures under changed design and content.

## Problem

UI agents interact with real apps whose appearance and content vary. Current evaluations often use fixed app clones, measuring whether an agent can complete tasks in one environment rather than across realistic variations.

Deployment reliability depends on whether task success survives changes in UI design, content, layout, and configuration.

## Core Contribution

The paper introduces OpenApps, a lightweight open-source ecosystem of six configurable apps such as messenger, calendar, and maps.

It enables generation and deployment of thousands of app versions on a single CPU, allowing reliability evaluation across environment variation.

## Method

OpenApps varies app appearance and content while preserving task semantics.

The authors run more than 10,000 independent evaluations across seven leading multimodal agents to compare fixed-app reliability with reliability under variations.

## Experiments and Evidence

The abstract reports that standard reliability in a fixed app can appear stable while success under variations fluctuates drastically.

Many agents vary by more than 50 percent across app versions. Kimi-VL-3B drops from 63 percent to 4 percent average success across versions, and behaviors such as looping or hallucinated actions vary by configuration.

## Limits and Failure Modes

Simulated apps may not capture all real-world web/app complexity, authentication flows, latency, accessibility layers, or user-specific data. Variation dimensions also need to be representative rather than arbitrary.

Because this note is abstract-only, details still need checking: six apps, task set, variation generator, agent list, UI instrumentation, metrics, and failure taxonomies.

## Deep Themes

- Environment-variation reliability: agent success must be measured over distributions of interfaces.
- Fixed benchmark overconfidence: one app clone can hide brittle perception and action policies.
- Lightweight simulation for scale: many environment variants expose robustness patterns.
- UI grounding failures: looping and hallucinated actions depend on visual/layout configuration.

## Subthemes

- UI agents.
- Configurable app simulation.
- Multimodal agent reliability.
- Environment variation.

## Connections to Other Papers

This connects to SimuHome, AgentGym-RL, AstaBench, SwingArena, and weak-to-strong monitoring.

It also relates to multi-turn conversation failures because both reveal reliability drops that single fixed evaluations miss.

## Notes for Cross-Paper Synthesis

OpenApps strengthens the agent-evaluation theme: deployed reliability is a distributional property over environment variants, not a single success rate.
