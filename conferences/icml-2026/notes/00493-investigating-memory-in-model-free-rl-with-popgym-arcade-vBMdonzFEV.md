# Investigating Memory in Model-Free RL with POPGym Arcade

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: vBMdonzFEV
- Authors: Zekang Wang; Zhe He; Borong Zhang; Edan Toledo; Steven Morad
- Primary area: reinforcement_learning
- Keywords: reinforcement learning;pomdp;memory;rnn
- Source URL: https://openreview.net/forum?id=vBMdonzFEV
- PDF URL: https://openreview.net/pdf?id=vBMdonzFEV

## Abstract

How should we analyze memory in deep RL? We introduce tools for analyzing policies under partial observability and revealing how agents use memory to make decisions. To utilize these tools, we present POPGym Arcade, a collection of Atari-inspired, hardware-accelerated environments sharing a single observation and action space. Each environment provides fully and partially observable variants, enabling counterfactual studies on observability. We find that controlled studies are necessary for fair comparisons and identify a pathology where value functions smear credit over irrelevant history. Using this pathology, we demonstrate how out-of-distribution scenarios can contaminate memory, perturbing the policy far into the future.

## One-Sentence Claim

POPGym Arcade provides controlled partially observable RL environments and analysis tools showing that value functions can smear credit over irrelevant history, causing memory contamination far into the future.

## Problem

Memory in model-free RL is hard to analyze because partial observability, recurrent policies, value estimation, and environment differences are often entangled. Standard benchmarks may not reveal whether an agent uses memory correctly or merely overfits temporal correlations.

The paper asks how to study memory under controlled observability changes and expose pathologies in how learned policies and value functions depend on history.

## Core Contribution

The paper introduces POPGym Arcade, a set of Atari-inspired hardware-accelerated environments sharing a common observation and action space. Each environment includes fully and partially observable variants, enabling counterfactual observability studies.

It also contributes tools for analyzing policies under partial observability and identifies a pathology where value functions smear credit over irrelevant history, allowing OOD scenarios to contaminate memory and perturb policy behavior far into the future.

## Method

POPGym Arcade controls interface variation by keeping observation and action spaces shared across environments while varying observability. Fully observable variants act as counterfactual baselines for partially observable versions.

The analysis tools inspect how policies use memory and how value estimates assign credit over histories. OOD perturbations are used to test whether irrelevant history persists in memory and affects later decisions.

## Experiments and Evidence

The abstract reports controlled studies showing the need for fair memory comparisons and demonstrating value-function credit smearing. It also shows that OOD scenarios can contaminate memory and perturb policies far into the future.

Full-paper reading should verify environment list, hardware acceleration, analyzed agent architectures, memory metrics, and the exact credit-smearing diagnostic.

## Limits and Failure Modes

Atari-inspired environments are controlled and useful, but may not capture all memory demands of robotics, language agents, or real-world POMDPs. Shared observation/action spaces improve comparison but may constrain environment diversity.

Memory contamination is a serious pathology, but mitigation strategies are not described in the abstract and need full-paper inspection.

## Deep Themes

- Memory as a measurable RL object: recurrent state should be audited, not assumed useful.
- Counterfactual observability: fully and partially observable variants isolate memory demand.
- Credit smearing over history: value functions can assign relevance to irrelevant past events.
- OOD memory contamination: transient anomalies can perturb policies long after they occur.

## Subthemes

- Hardware-accelerated environments support large controlled studies.
- Shared interfaces reduce benchmark confounds.
- Partial observability requires more than adding an RNN.
- Long-lived hidden state can be a liability.

## Connections to Other Papers

POPGym Arcade connects to CMRU, HSR, JitRL, and temporal graph memory explainability through memory and history. It also relates to PIPE and MiniAppBench because controlled environment variants expose hidden failure mechanisms.

It fits the broader agent diagnostics theme: interactive systems need tools that reveal internal state use over time.

## Notes for Cross-Paper Synthesis

The synthesis point is that memory is not automatically beneficial. Long-lived state can preserve useful context or contaminate future decisions, so memory must be evaluated counterfactually.
