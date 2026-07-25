# CausalGame: Benchmarking Causal Thinking of LLM Agents in Games

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: WNqIX3IFZU
- Authors: Zhenhao Chen; Yongqiang Chen; Chenxi Liu; Junchi Yu; Xiangchen Song; Zijian Li; Jialin Li; Philip Torr; Bo Han; Kun Zhang
- Primary area: deep_learning->large_language_models
- Keywords: LLM Agent;Interactive Benchmark;causality
- Source URL: https://openreview.net/forum?id=WNqIX3IFZU
- PDF URL: https://openreview.net/pdf?id=WNqIX3IFZU

## Abstract

Recently, it has received growing attention in building AI Scientist agents with Large Language Models (LLMs). Since scientific discovery fundamentally relies on uncovering causal relationships from observations, the capability of causal thinking that distinguish causation from correlation and hidden biases, is essential to LLM agents. Despite a number of existing benchmarks for AI scientists, they do not explicitly incorporate challenges from hidden confounders, selection bias, and noisy measurements that widely exist in real-world scientific discovery. To this end, we present CausalGame, a benchmark that evaluates the causal thinking capabilities of LLM agents through interactive games. More specifically, we ask LLM agents to actively design experimental protocols, collect observation data and derive a final solution with an explanation report. To emulate realistic scientific discovery challenges, we design 14 game settings with the incorporation of selection bias, noisy measurements, and hidden confounders. The results with 29 frontier LLM agents show that they consistently fail to reason about and recover the underlying causal relationships required to solve the games. CausalGame provides a controlled testbed for evaluating causal thinking of AI Scientist agents. The project is available at causalgame.github.io .

## One-Sentence Claim

CausalGame shows that frontier LLM agents fail controlled interactive games requiring causal discovery under confounding, selection bias, and noisy measurements.

## Problem

AI scientist agents need to uncover causal relationships from observations, but many existing benchmarks do not explicitly test hidden confounding, selection bias, or noisy measurements. These are core obstacles in real scientific discovery.

The paper asks whether LLM agents can actively design experiments, collect data, infer causal structure, and explain conclusions under controlled but realistic causal challenges.

## Core Contribution

The paper introduces CausalGame, an interactive benchmark for causal thinking in LLM agents. Agents must design experimental protocols, collect observational data, and produce a final solution with an explanation report.

The benchmark includes 14 game settings with selection bias, noisy measurements, and hidden confounders. Evaluation of 29 frontier LLM agents shows consistent failure to recover required causal relationships.

## Method

CausalGame wraps causal-discovery tasks as interactive games. Instead of giving a static dataset, it lets agents choose experiments and gather observations, then tests whether they distinguish causation from correlation under deliberately introduced biases.

The game format measures scientific process: experimental design, data collection, causal inference, and explanation.

## Experiments and Evidence

Evidence reported in the abstract:

- 14 interactive causal game settings.
- Explicit hidden confounders, selection bias, and noisy measurements.
- Evaluation of 29 frontier LLM agents.
- Agents consistently fail to reason about and recover underlying causal relationships.
- Public project site.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: game mechanics, agent scaffolds, scoring rubric, model identities, and whether tool use or repeated trials were allowed.

## Limits and Failure Modes

- Game abstractions may not capture all forms of scientific causal reasoning.
- Poor performance could reflect interaction protocol limitations as well as causal reasoning limits.
- Frontier-agent evaluations can become stale quickly as models change.
- The benchmark must guard against memorization if public tasks are exposed.

## Deep Themes

**Scientific agents need causal process tests.** Static QA is insufficient for evaluating experimental reasoning.

**Interactivity exposes planning failures.** Agents must decide what data to collect, not only interpret provided evidence.

**Current LLM agents struggle with hidden bias.** Confounding, selection effects, and noise remain hard even for frontier systems.

## Subthemes

- Interactive causal discovery benchmarks.
- Experiment-design evaluation.
- Hidden confounders and selection bias.
- AI scientist agents.
- Explanation reports as process evidence.

## Connections to Other Papers

Connects to HypoSpace, TerminalTraj, tau2-bench, and TG-RAG through process-oriented agent evaluation. It also links to DISCO and TRECA because all center causal reasoning under biased or uncertain observations.

## Notes for Cross-Paper Synthesis

CausalGame reinforces that agent evaluation is moving from answer correctness to scientific workflow competence: choose interventions, gather evidence, account for bias, and justify the causal claim.
