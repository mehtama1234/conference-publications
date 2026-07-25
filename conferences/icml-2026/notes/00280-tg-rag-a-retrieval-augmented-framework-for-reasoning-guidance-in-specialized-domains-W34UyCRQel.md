# TG-RAG: A Retrieval-Augmented Framework for Reasoning Guidance in Specialized Domains

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: W34UyCRQel
- Authors: Liang Su; Mingyang Zhang; Yun Xiong; Tengfei LIU; Siwei Zhang; Xi Chen; Li Sun
- Primary area: applications->language_speech_and_dialog
- Keywords: Large Reasoning Model;Retrieval-Augmented Generation;Controllable Generation
- Source URL: https://openreview.net/forum?id=W34UyCRQel
- PDF URL: https://openreview.net/pdf?id=W34UyCRQel

## Abstract

Enhancing Large Reasoning Models (LRMs) for specialized domains remains a critical challenge. While recent industrial frameworks attempt to encapsulate Standard Operating Procedures into modular "skills" for dynamic retrieval, utilizing them via context engineering often proves insufficient for complex workflows, leading to "Cognitive Drift." To mitigate this, we propose $\textbf{Thought Guidance-Retrieval Augmented Generation (TG-RAG)}$, a Retrieval-Augmented framework that effectively steers the generation process without relying solely on the model's self-correction. Built upon an Expert Procedure Graph (EPG) that formalizes unstructured SOPs, the framework uniquely employs a dynamic $\textbf{``Interrupt-Retrieve-Generate" (IRG)}$ mechanism to actively inject step-specific directives into the model's reasoning process. Extensive evaluations show that TG-RAG achieves competitive performance, demonstrating advantages in specialized domains by ensuring faithful adherence to domain SOPs. Code is available at https://github.com/V1ncent-S/Thought-Guidance.

## One-Sentence Claim

TG-RAG reduces cognitive drift in specialized-domain reasoning by converting SOPs into expert procedure graphs and injecting step-specific guidance through interrupt-retrieve-generate control.

## Problem

Large reasoning models struggle in specialized domains where workflows must follow standard operating procedures. Recent systems try to retrieve modular skills or context snippets, but context engineering alone can fail on complex workflows, letting the model drift away from required procedures.

The paper calls this failure cognitive drift and asks how retrieval can steer the reasoning process itself rather than merely provide background information.

## Core Contribution

The paper proposes Thought Guidance-Retrieval Augmented Generation, a RAG framework built around an Expert Procedure Graph that formalizes unstructured SOPs. Its Interrupt-Retrieve-Generate mechanism dynamically injects step-specific directives into the model's reasoning process.

The contribution is a procedural-control layer for domain reasoning: retrieve the right procedural node at the right moment and actively steer generation.

## Method

TG-RAG first converts SOPs into an Expert Procedure Graph. During generation, the system interrupts the model's reasoning trajectory, retrieves the relevant procedure guidance, and resumes generation with step-specific directives.

This differs from passive RAG because retrieval is tied to reasoning stages, not only to initial query context.

## Experiments and Evidence

Evidence reported in the abstract:

- Extensive evaluations in specialized domains.
- Competitive performance versus baselines.
- Advantages in faithful adherence to domain SOPs.
- Code release.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: specialized domains, EPG construction method, interrupt policy, adherence metrics, and comparison against tool/agent frameworks.

## Limits and Failure Modes

- SOPs may be incomplete, contradictory, outdated, or hard to graph automatically.
- Frequent interruptions can increase latency and fragment reasoning if poorly timed.
- Procedure adherence does not guarantee factual correctness or optimal action.
- The method depends on detecting the model's current reasoning stage reliably.

## Deep Themes

**Retrieval is becoming process control.** TG-RAG retrieves procedural guidance during reasoning, not just documents before answering.

**Specialized reasoning needs externalized workflow structure.** Expert Procedure Graphs make domain procedures explicit and machine-addressable.

**Cognitive drift is a systems failure.** The problem is not only model knowledge but maintaining procedural alignment across multi-step generation.

## Subthemes

- Expert Procedure Graphs.
- Interrupt-Retrieve-Generate control.
- SOP adherence in LRMs.
- Dynamic reasoning guidance.
- Specialized-domain RAG.

## Connections to Other Papers

Connects to tau2-bench, TerminalTraj, Scientific Annotation BC, and DLMR because all model reasoning as a controlled process over steps, tools, or memories. It also links to WETR as a training-free steering method for frozen models.

## Notes for Cross-Paper Synthesis

TG-RAG contributes to the process-control theme: reliable reasoning requires mechanisms that keep the model aligned to procedural state, not just larger contexts or better self-correction.
