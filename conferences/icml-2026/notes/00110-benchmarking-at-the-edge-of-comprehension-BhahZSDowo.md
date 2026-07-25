# Benchmarking at the Edge of Comprehension

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: BhahZSDowo
- Authors: Samuele Marro; Jialin Yu; Emanuele La Malfa; Oishi Deb; Jiawei Li; Yibo Yang; Ebey Abraham; Sunando Sengupta; Eric Sommerlade; Michael J. Wooldridge; Philip Torr
- Primary area: general_machine_learning->evaluation
- Keywords: benchmarking;llms;math;verification;weak-to-strong
- Source URL: https://openreview.net/forum?id=BhahZSDowo
- PDF URL: https://openreview.net/pdf?id=BhahZSDowo

## Abstract

As frontier Large Language Models (LLMs) increasingly saturate new benchmarks shortly after they are published, benchmarking itself is at a juncture: if frontier models keep improving, it will become increasingly hard for humans to generate discriminative tasks, provide accurate ground-truth answers, or evaluate complex solutions.
If benchmarking becomes infeasible, our ability to measure any progress in AI is at stake. We refer to this scenario as the *post-comprehension regime*.
In this work, we propose Critique-Resilient Benchmarking, an adversarial framework designed to compare models even when full human understanding is infeasible. 
Our technique relies on the notion of *critique-resilient correctness*: an answer is deemed correct if no adversary has convincingly proved otherwise.
Unlike standard benchmarking, humans serve as bounded verifiers and focus on localized claims, which preserves evaluation integrity beyond full comprehension of the task. 
Using an itemized bipartite Bradley-Terry model, we jointly rank LLMs by their ability to solve challenging tasks and to generate difficult yet solvable questions. 
We showcase the effectiveness of our method in the mathematical domain across eight frontier LLMs, showing that the resulting scores are stable and correlate with external capability measures. 
Our framework reformulates benchmarking as an adversarial generation-evaluation game in which humans serve as final adjudicators.

## One-Sentence Claim

Critique-Resilient Benchmarking compares frontier models in a post-comprehension regime by treating correctness as surviving adversarial critique rather than requiring full human solution understanding.

## Problem

As frontier models rapidly saturate benchmarks, humans may struggle to create discriminative tasks, know ground truth, or evaluate complex solutions, threatening progress measurement.

## Core Contribution

The paper proposes an adversarial benchmark framework where models generate and solve hard tasks, adversaries critique answers, and humans serve as bounded local verifiers.

## Method

It defines critique-resilient correctness: an answer is accepted if no adversary convincingly proves it wrong. An itemized bipartite Bradley-Terry model jointly ranks models by solving ability and question-generation difficulty.

## Experiments and Evidence

The abstract reports mathematical-domain evaluation across eight frontier LLMs, with stable scores that correlate with external capability measures.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: adversary strength, human adjudication protocol, collusion risks, itemized model specification, and transfer beyond math.

## Deep Themes

- Benchmarking may need to function beyond full human comprehension.
- Evaluation can become an adversarial generation-critique game.
- Humans can remain final adjudicators by verifying localized claims.

## Subthemes

- Post-comprehension benchmarking.
- Critique-resilient correctness.
- Weak-to-strong evaluation.
- Bradley-Terry ranking.
- Mathematical benchmarking.
- Bounded human verification.

## Connections to Other Papers

Connects to Jailbreak Foundry, CVE Factory, DR Tulu, and oracle-free evaluation papers through benchmarks as adversarial/evolving processes.

## Notes for Cross-Paper Synthesis

This paper adds a post-comprehension evaluation theme: model capability may outgrow static human-authored benchmarks, forcing evaluation into adversarial verification games.
