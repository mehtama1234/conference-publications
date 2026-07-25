# DRPBench: Evaluating LLMs in Concurrent Code Comprehension via Fine-Grained Data Race Prediction

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 6249M0mKR2
- Authors: Yuqi Guo; Siwei Wei; Yan Cai
- Primary area: general_machine_learning->evaluation
- Keywords: LLM benchmarking;Evaluation;Data race prediction
- Source URL: https://openreview.net/forum?id=6249M0mKR2
- PDF URL: https://openreview.net/pdf?id=6249M0mKR2

## Abstract

Large Language Models (LLMs) have demonstrated sophisticated comprehension of sequential code, yet their capacity for reasoning about concurrent programs remains largely unquantified. We introduce DRPBench, a benchmark designed to evaluate the concurrent code comprehension of LLMs by measuring their data race prediction performance. To address the challenge of runtime non-determinism for evaluation on concurrent programs, we frame the evaluation as a fine-grained static prediction task using 1,003 programs from the SV-COMP suite, featuring 557 manually annotated data races with precise variable- and line-level granularity. Our evaluation of 15 state-of-the-art LLMs—spanning standard, reasoning, and agentic variants—reveals that DRPBench effectively differentiates concurrent code comprehension capabilities of LLMs. While the top-performing model (Gemini 3 with test-time reasoning) achieves an F1 score of 74.89%, most models struggle significantly (scoring less than 60%), with Llama 3 70B achieving only 8.80%. Beyond benchmarking, we characterize two primary failure modes: (1) shared-variable distraction, where multiple variable appearances degrade comprehension accuracy, and (2) synchronization-logic myopia, the inability to interpret non-standard synchronization implementations. Our findings provide a diagnostic roadmap for enhancing concurrent code comprehension of LLMs in future development.

## One-Sentence Claim

DRPBench exposes a gap in LLM code understanding by evaluating fine-grained static data-race prediction in concurrent programs.

## Problem

LLMs are increasingly strong on sequential code tasks, but their ability to reason about concurrency, nondeterminism, shared variables, and synchronization remains undermeasured.

## Core Contribution

The paper introduces DRPBench, a benchmark of 1,003 SV-COMP concurrent programs with 557 manually annotated data races at variable- and line-level granularity.

## Method

Instead of executing nondeterministic concurrent programs, DRPBench frames evaluation as static fine-grained prediction: models must identify whether and where data races occur, enabling reproducible scoring across LLMs.

## Experiments and Evidence

The abstract reports evaluation of 15 standard, reasoning, and agentic LLM variants. Gemini 3 with test-time reasoning reaches 74.89% F1, most models score below 60%, and Llama 3 70B reaches only 8.80%.

## Limits and Failure Modes

ArXiv searches for this batch hit HTTP 429, so no local PDF is available yet. Details still need checking: annotation protocol, prompt formats, model list, static-analysis baselines, and how line/variable granularity is scored.

## Deep Themes

- Code comprehension benchmarks are moving from syntax/sequential tasks toward concurrency semantics.
- Static evaluation can avoid runtime nondeterminism while preserving fine-grained diagnostic value.
- Test-time reasoning helps but does not solve synchronization understanding.

## Subthemes

- Concurrent code comprehension.
- Data race prediction.
- SV-COMP.
- Static program reasoning.
- Shared-variable distraction.
- Synchronization-logic myopia.

## Connections to Other Papers

Connects to CyberGym and SandboxEscapeBench as code/security-adjacent evaluations where execution environments and program semantics matter. It also links to HATSolver and transformer-circuit work through algorithmic reasoning.

## Notes for Cross-Paper Synthesis

DRPBench adds a software-engineering evaluation theme: LLM code ability must be tested on semantic hazards such as concurrency, not only generation or repair of sequential programs.
