# Jailbreak Foundry: From Papers to Runnable Attacks for Reproducible Benchmarking

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: BSi2mfMDsx
- Authors: Zhicheng Fang; Jingjie Zheng; Chenxu Fu; Wei Xu
- Primary area: social_aspects->safety
- Keywords: large language models;jailbreaks;benchmark;evaluations
- Source URL: https://openreview.net/forum?id=BSi2mfMDsx
- PDF URL: https://openreview.net/pdf?id=BSi2mfMDsx

## Abstract

Jailbreak techniques for large language models (LLMs) evolve faster than benchmarks, making robustness estimates stale and difficult to compare across papers due to drift in datasets, harnesses, and judging protocols. We introduce **JAILBREAK FOUNDRY (JBF)**, a system that addresses this gap via a multi-agent workflow to translate jailbreak papers into executable modules for immediate evaluation within a unified harness. JBF features three core components: (i) *JBF-LIB* for shared contracts and reusable utilities; (ii) *JBF-FORGE* for the multi-agent paper-to-module translation; and (iii) *JBF-EVAL* for standardizing evaluations. Across 30 reproduced attacks, JBF achieves high fidelity with a mean (reproduced$-$reported) attack success rate (ASR) deviation of $+0.26$ percentage points. By leveraging shared infrastructure, JBF reduces attack-specific implementation code by nearly half relative to original repositories and achieves an 82.5% mean reused-code ratio. This system enables a standardized AdvBench evaluation of all 30 attacks across 10 victim models using a consistent GPT-4o judge. By automating both attack integration and standardized evaluation, JBF offers a scalable solution for creating living benchmarks that keep pace with the rapidly shifting security landscape.

## One-Sentence Claim

Jailbreak Foundry converts jailbreak papers into runnable attack modules inside a unified evaluation harness, enabling reproducible and living LLM robustness benchmarks.

## Problem

Jailbreak methods evolve quickly, while benchmark comparisons become stale and inconsistent because attacks, datasets, harnesses, and judging protocols drift across papers.

## Core Contribution

The paper introduces JBF, a system with shared attack libraries, multi-agent paper-to-module translation, and standardized evaluation across attacks and victim models.

## Method

JBF-LIB provides shared contracts and utilities, JBF-FORGE translates papers into executable attack modules through a multi-agent workflow, and JBF-EVAL standardizes evaluations in a common harness.

## Experiments and Evidence

The abstract reports reproduction of 30 attacks with mean reproduced-minus-reported ASR deviation of +0.26 percentage points, nearly half the attack-specific code of original repositories, 82.5% mean reused-code ratio, and standardized AdvBench evaluation across 10 victim models using a GPT-4o judge.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: paper-to-code validation, judge reliability, attack licensing/ethics, coverage of multimodal attacks, and maintenance burden.

## Deep Themes

- Security benchmarks need executable, reproducible attack infrastructure.
- Living benchmarks can keep pace with rapidly changing jailbreak methods.
- Multi-agent coding workflows can operationalize research papers into standardized modules.

## Subthemes

- Jailbreak benchmarking.
- Reproducible attacks.
- Multi-agent paper-to-code translation.
- Unified evaluation harness.
- AdvBench.
- LLM safety.

## Connections to Other Papers

Connects to CyberGym, Copyright-Bench, DRPBench, and safety evaluation papers through executable benchmark infrastructure. It also links to agentic coding/security workflows.

## Notes for Cross-Paper Synthesis

JBF adds a living-benchmark theme: safety evaluation must be continuously executable and reproducible, not just a static leaderboard.
