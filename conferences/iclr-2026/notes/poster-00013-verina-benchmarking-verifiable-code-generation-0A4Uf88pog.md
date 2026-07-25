# VERINA: Benchmarking Verifiable Code Generation

## Metadata

- Conference: iclr-2026
- Status: Poster
- OpenReview ID: 0A4Uf88pog
- Authors: Zhe Ye; Zhengxu Yan; Jingxuan He; Timothe Kasriel; Kaiyu Yang; Dawn Song
- Primary area: neurosymbolic & hybrid AI systems (physics-informed, logic & formal reasoning, etc.)
- Keywords: code generation;formal verification;verifiable code generation;AI for math;theorem proving;AI for code
- Source URL: https://openreview.net/forum?id=0A4Uf88pog
- PDF URL: https://openreview.net/pdf?id=0A4Uf88pog

## Abstract

Large language models (LLMs) are increasingly integrated in software development, but ensuring correctness in LLM-generated code remains challenging and often requires costly manual review. Verifiable code generation---jointly generating code, specifications, and proofs of code-specification alignment---offers a promising path to address this limitation and further unleash LLMs' benefits in coding. Yet, there exists a significant gap in evaluation: current benchmarks often focus on only individual components rather than providing a holistic evaluation framework of all tasks. In this paper, we introduce VERINA (Verifiable Code Generation Arena), a high-quality benchmark enabling a comprehensive and modular evaluation of code, specification, and proof generation as well as their compositions. VERINA consists of 189 manually curated coding tasks in Lean, with detailed problem descriptions, reference implementations, formal specifications, and extensive test suites. Our extensive evaluation of state-of-the-art LLMs reveals significant challenges in verifiable code generation, especially in proof generation, underscoring the need for improving LLM-based theorem provers in verification domains.
The best model, OpenAI o3, achieves a 72.6% code correctness rate, 52.3% for specification soundness and completeness, and a mere 4.9% proof success rate (based on one trial per task).
We hope VERINA will catalyze progress in verifiable code generation by providing a rigorous and comprehensive benchmark.

## One-Sentence Claim

VERINA benchmarks verifiable code generation as the joint production of code, formal specifications, and proofs, revealing proof generation as the largest bottleneck for current LLMs.

## Problem

LLM-generated code is increasingly used in software development, but correctness remains hard to guarantee without manual review. Existing benchmarks often evaluate code, specs, or proofs separately rather than testing the full verifiable-code pipeline.

## Core Contribution

The paper introduces VERINA, a manually curated Lean benchmark with 189 coding tasks, detailed problem descriptions, reference implementations, formal specifications, and extensive test suites. It supports modular and compositional evaluation of code generation, specification generation, proof generation, and their combinations.

## Method

VERINA frames verifiable code generation as generating artifacts that align: executable code, specifications, and proofs of code-spec conformance. The benchmark evaluates state-of-the-art LLMs on each component and on composed verification tasks in Lean.

## Experiments and Evidence

The abstract reports that OpenAI o3 achieves 72.6% code correctness, 52.3% specification soundness/completeness, and only 4.9% proof success in one trial per task. This indicates that current models can often write code but rarely complete formal proof obligations.

## Limits and Failure Modes

This note is abstract/metadata-only. Full-text review should inspect task diversity, Lean version, proof-checking setup, one-trial versus sampling results, and whether reference specs bias the evaluation. Small curated benchmarks can be rigorous but may not cover broader software domains.

## Deep Themes

- Verifiable code generation.
- Holistic code-spec-proof evaluation.
- Formal verification bottlenecks for LLMs.
- Lean-based software correctness benchmarks.

## Subthemes

- VERINA.
- Specification soundness and completeness.
- Proof success rate.
- Reference implementations.
- Modular benchmark design.

## Connections to Other Papers

Connects to CRAMF through Lean/Mathlib grounding, to THOR through tool-integrated reasoning, and to provable NAM explanations through formal guarantees as a way to move from plausible outputs to certified artifacts.

## Notes for Cross-Paper Synthesis

VERINA is a sharp measurement paper: it separates seeming coding competence from proof-backed correctness. The cross-corpus theme is that reliable AI systems require evaluation of the whole artifact chain, not only final natural-language or code outputs.
