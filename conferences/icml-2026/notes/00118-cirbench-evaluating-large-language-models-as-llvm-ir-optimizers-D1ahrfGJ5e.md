# CIRBench: Evaluating Large Language Models as LLVM IR Optimizers

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: D1ahrfGJ5e
- Authors: Zi Yang; Haifeng Ding; Fei Liu; Yingying Cheng; Han Cheng; Zhilei Chai; Haojie Zhou
- Primary area: general_machine_learning->evaluation
- Keywords: LLVM IR;LLMs;compiler optimization;program transformation;benchmarking
- Source URL: https://openreview.net/forum?id=D1ahrfGJ5e
- PDF URL: https://openreview.net/pdf?id=D1ahrfGJ5e

## Abstract

Large language models are beginning to introduce a new paradigm for compilation: instead of only assisting at the source level, they can operate directly on **intermediate representations (IRs)**, the compiler’s internal code representation, Early studies suggest that LLM-guided optimization can sometimes rival traditional compiler optimizations on selected programs, but evidence remains fragmented.
Yet the community still lacks a rigorous IR-level benchmark that tests whether a model not only understands IR but can rewrite it under compiler-grade semantic constraints with meaningful performance impact.
We present **CIRBench**, a benchmark of 800 curated IR instances spanning four compiler-oriented tracks: Analysis infers IR properties, Repair fixes invalid IR, Refactor applies a single semantics-preserving compiler optimization, and Transform performs performance-oriented rewrites, together mirroring core optimization responsibilities in modern compilers.
CIRBench combines verifier, equivalence checking, and end-to-end performance measurement into a unified, layered correctness-aware evaluation of LLMs on IR.
On six mainstream LLMs, CIRBench shows that current models fail on many IR analysis and rewriting instances and on median underperform the compiler baseline, but we also observe a maximum speedup of $4.96\times$ over -O3.
These findings highlight both the opportunities and the remaining challenges of using LLMs inside optimizing compilers.

## One-Sentence Claim

CIRBench evaluates whether LLMs can analyze, repair, refactor, and transform LLVM IR under compiler-grade correctness and performance constraints.

## Problem

LLM compiler-optimization evidence is fragmented, and there is no rigorous IR-level benchmark for semantic correctness and performance impact.

## Core Contribution

The paper introduces an 800-instance benchmark across four compiler tracks with verifier, equivalence checking, and end-to-end performance measurement.

## Method

CIRBench covers Analysis, Repair, Refactor, and Transform tasks, mirroring compiler responsibilities from property inference to performance-oriented rewrites. It layers correctness checks and runtime measurement to evaluate both semantic validity and optimization value.

## Experiments and Evidence

The abstract reports that six mainstream LLMs fail many analysis and rewriting instances and underperform compiler baselines on median, while still occasionally achieving up to 4.96x speedup over -O3.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: IR instance selection, equivalence checker soundness, performance measurement noise, prompt protocol, and compiler baseline configuration.

## Deep Themes

- Code intelligence is moving inside compiler intermediate representations.
- Correctness-aware evaluation is essential for program transformation.
- LLMs may find rare optimizations while still lacking reliable compiler competence.

## Subthemes

- LLVM IR.
- Compiler optimization.
- Program transformation.
- Equivalence checking.
- LLM code evaluation.
- Performance benchmarking.

## Connections to Other Papers

Connects to DRPBench, CVE-Factory, CyberGym, and software-agent tasks through executable code benchmarks with formal or runtime checks.

## Notes for Cross-Paper Synthesis

CIRBench adds an IR-level code-intelligence theme: useful code agents must handle internal compiler representations, not only source text.
