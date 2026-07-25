# Monitoring Monitorability

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: b82fgbMVpz
- Authors: Melody Y. Guan; Miles Wang; Micah Carroll; Zehao Dou; Annie Y. Wei; Marcus Williams; Benjamin Arnav; Joost Huizinga; Ian D Kivlichan; Amelia Glaese; Jakub Pachocki; Bowen Baker
- Primary area: social_aspects->safety
- Keywords: monitorability;chain-of-thought;scalable oversight;weak-to-strong monitoring;evaluation suite;test-time compute;compute scaling;pretraining scaling;auditing
- Source URL: https://openreview.net/forum?id=b82fgbMVpz
- PDF URL: https://openreview.net/pdf?id=b82fgbMVpz

## Abstract

Safe deployment of increasingly capable AI agents may require visibility into how they make decisions. Chain-of-thought (CoT) monitoring can detect misbehavior in today’s reasoning models, but this “monitorability” may be fragile under different training procedures, data sources, or continued system scaling. We propose three evaluation archetypes (intervention, process, and outcome-property), a new monitorability metric, and a broad evaluation suite. We show CoT monitoring outperforms action-only monitoring in practical settings, and that frontier models are generally—but not perfectly—monitorable. We study scaling trends with pre-training model size and inference-time compute, finding longer CoTs are typically more monitorable. We find that, for a fixed capability level, using a smaller model at higher reasoning effort can yield higher monitorability, at greater inference compute cost. We further find that increasing a weak monitor’s test-time compute when monitoring a strong agent improves monitorability, and giving the monitor access to the CoT both boosts monitorability and steepens the compute–to-monitorability scaling trend. Finally, we show monitorability can be improved by asking follow-up questions and giving the follow-up CoT to the monitor.

## One-Sentence Claim

CoT monitorability is measurable but fragile: reasoning traces improve oversight, longer CoTs are often easier to monitor, and monitor compute can compensate for weaker monitors.

## Problem

Safe deployment of capable agents may require visibility into decision processes. Chain-of-thought monitoring can detect some misbehavior today, but it is unclear how robust this monitorability is across training procedures, data sources, model scaling, and inference-time compute.

The paper asks how to measure monitorability and how it scales with agent and monitor properties.

## Core Contribution

The paper proposes three evaluation archetypes, intervention, process, and outcome-property, plus a new monitorability metric and a broad evaluation suite.

It finds CoT monitoring outperforms action-only monitoring, frontier models are generally but imperfectly monitorable, longer CoTs tend to be more monitorable, smaller models with higher reasoning effort can be more monitorable at fixed capability, and increasing a weak monitor's test-time compute improves monitoring of strong agents. Follow-up questions and follow-up CoTs also improve monitorability.

## Method

The method constructs evaluation settings that test whether monitors can detect relevant properties from agent behavior and reasoning traces. It varies what evidence the monitor sees, model scale, reasoning effort, and monitor test-time compute.

The monitorability metric quantifies how visible the decision process is to an oversight system.

## Experiments and Evidence

Evidence reported in the abstract:

- Three evaluation archetypes: intervention, process, and outcome-property.
- New monitorability metric and broad evaluation suite.
- CoT monitoring outperforms action-only monitoring.
- Frontier models are generally but not perfectly monitorable.
- Longer CoTs are typically more monitorable.
- Smaller model with higher reasoning effort can have higher monitorability at fixed capability.
- More monitor test-time compute improves weak-to-strong monitoring.
- Follow-up questions and follow-up CoT improve monitoring.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: tasks, models, monitor architectures, CoT faithfulness assumptions, and metric definitions.

## Limits and Failure Modes

- CoT may be unfaithful or strategically obfuscated by future agents.
- Longer CoTs cost more inference compute and may leak sensitive reasoning.
- Monitorability metrics may not capture rare catastrophic failures.
- Training to appear monitorable could create Goodhart effects.

## Deep Themes

**Oversight is a scaling object.** Monitorability changes with model size, reasoning effort, and monitor compute.

**Reasoning traces are useful but not guaranteed.** CoT improves monitoring today while remaining a fragile safety substrate.

**Weak monitors can be strengthened with compute and interaction.** Follow-up questions and test-time compute are active oversight levers.

## Subthemes

- Chain-of-thought monitoring.
- Weak-to-strong monitoring.
- Monitorability metric.
- Test-time compute for oversight.
- Follow-up CoT interrogation.

## Connections to Other Papers

Connects to NAD, BrokenMath, CausalGame, Agent0-VL, TG-RAG, and tau2-bench through process-level evaluation and oversight. It also links to safety governance papers because it asks when internal reasoning is auditable.

## Notes for Cross-Paper Synthesis

Monitoring Monitorability adds a central safety axis: capability is not enough; systems must remain legible to oversight as they scale and as reasoning effort changes.
