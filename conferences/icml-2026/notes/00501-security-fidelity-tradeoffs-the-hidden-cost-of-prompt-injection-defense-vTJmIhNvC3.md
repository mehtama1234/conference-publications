# Security--Fidelity Tradeoffs: The Hidden Cost of Prompt Injection Defense

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: vTJmIhNvC3
- Authors: Mitchell Hermon; Rahul Gupta; Weitong Ruan; Ekraam Sabir; Haohan Wang
- Primary area: social_aspects->security
- Keywords: Prompt Injection;Fidelity;LLM;Evaluation;Security;Robustness
- Source URL: https://openreview.net/forum?id=vTJmIhNvC3
- PDF URL: https://openreview.net/pdf?id=vTJmIhNvC3

## Abstract

We identify a **security--fidelity tradeoff** in defending LLMs against indirect prompt injection: defenses resist injected instructions largely by
suppressing untrusted text, which corrupts tasks that must preserve it, such as translation and document editing. Attack-success metrics cannot see this, because a model that ignores an injection and one that faithfully processes it as data score identically. We introduce **SecFid**, a benchmark built so that *executing* an injection, *processing* it as data, and *ignoring* it produce distinguishable outputs. This makes fidelity measurable, and exposes a frontier: across 1,168 examples and 48 configurations, no model or defense
achieves both objectives. The highest-fidelity model reaches 96.5% fidelity at 47.8% security, while the most secure defenses invert this, at 99.3% security but only 71.0%--73.9% fidelity. Even defenses with identical security differ in how they earn it: some repair hijacks into faithful processing, others simply suppress benign content. A decision-theoretic analysis shows why no fixed choice can be right everywhere: the correct behavior is not a property of the defense but of the deployment, set by its relative cost of a hijack versus a dropped span. Security alone therefore measures only half of robustness, and reporting it without fidelity hides the price at which it was bought.

## One-Sentence Claim

Prompt-injection defenses trade security against fidelity because many defenses block attacks by suppressing untrusted text that benign tasks need to preserve.

## Problem

Indirect prompt injection defenses are usually judged by attack success: did the model follow the injected instruction or not? That metric misses a crucial distinction between faithfully processing untrusted text as data and ignoring it entirely.

This matters for tasks such as translation, summarization, and document editing, where the untrusted span is the object of work. A defense can appear secure while corrupting the task by dropping or suppressing the content the user wanted processed.

## Core Contribution

The paper identifies and measures a security-fidelity tradeoff. It introduces SecFid, a benchmark where executing an injection, processing it as data, and ignoring it produce distinguishable outputs.

The key contribution is to make fidelity a first-class robustness metric. The paper also gives a decision-theoretic framing showing that the right defense behavior depends on deployment-specific costs of hijack versus dropped content.

## Method

SecFid constructs examples where security and fidelity are separable. A model must refuse or neutralize injected instructions while still preserving benign untrusted content needed for the task.

The benchmark evaluates many model/defense configurations and plots a frontier between attack resistance and content preservation. Decision-theoretic analysis then explains why no fixed operating point is universally optimal.

## Experiments and Evidence

The abstract reports 1,168 examples and 48 configurations. No model or defense achieves both objectives. The highest-fidelity model reaches 96.5 percent fidelity but only 47.8 percent security, while the most secure defenses reach 99.3 percent security but only 71.0-73.9 percent fidelity.

It also finds defenses with identical security can differ in whether they repair hijacks into faithful processing or simply suppress benign content.

## Limits and Failure Modes

SecFid focuses on indirect prompt injection scenarios where untrusted text must often be preserved. Other security settings may prioritize isolation over fidelity, and the proper cost tradeoff is application-specific.

The benchmark measures a sharper distinction than attack success, but real deployments may include multi-step tool calls, retrieval pipelines, and policy constraints that add further fidelity/security dimensions.

## Deep Themes

- Robustness as frontier, not scalar: security alone hides fidelity loss.
- Untrusted text has dual status: it can be both attack vector and task data.
- Deployment-specific risk tradeoffs: correct behavior depends on the relative cost of hijacks and dropped spans.
- Evaluation by distinguishable outcomes: benchmarks must separate ignore, execute, and process-as-data cases.

## Subthemes

- Suppression is a common hidden defense mechanism.
- Translation and document editing expose fidelity costs clearly.
- Equal security scores can mask different mechanisms.
- Prompt-injection defense needs utility-preserving evaluation.

## Connections to Other Papers

This paper connects to MiniAppBench, PIPE, and performative-misalignment work through benchmark confounds: a high score can hide the mechanism that produced it. It also relates to conformal policy control and RACO because all treat safety as a tradeoff-sensitive objective.

It belongs in the robustness/safety cluster but sharpens the metric: secure behavior must preserve the intended task semantics.

## Notes for Cross-Paper Synthesis

The synthesis point is that safety metrics can be incomplete even when they look precise. If the benchmark cannot distinguish safe faithful processing from safe suppression, it rewards the wrong behavior.
