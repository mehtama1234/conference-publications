# Vision2Web: A Hierarchical Benchmark for Visual Website Development with Agent Verification

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: lJpXXwhRRF
- Authors: Zehai He; Wenyi Hong; Zhen Yang; Ziyang Pan; Mingdao Liu; Xiaotao Gu; Jie Tang
- Primary area: general_machine_learning->evaluation
- Keywords: Autonomous Coding Agents;Multimodal Agent Evaluation;Hierarchical Benchmarks;End-to-End Software Development;Workflow-based Verification
- Source URL: https://openreview.net/forum?id=lJpXXwhRRF
- PDF URL: https://openreview.net/pdf?id=lJpXXwhRRF

## Abstract

Recent advances in large language models have improved the capabilities of coding agents, yet systematic evaluation of complex, end-to-end website development remains limited. To address this gap, we introduce Vision2Web, a hierarchical benchmark for visual website development, spanning from static UI-to-code generation, interactive multi-page frontend reproduction, to long-horizon full-stack website development. The benchmark is constructed from real-world websites and comprises a total of 193 tasks across 16 categories, with 918 prototype images and 1,255 test cases. To support flexible, thorough and reliable evaluation, we propose workflow-based agent verification paradigm based on two complementary components: a GUI agent verifier and a VLM-based judge. We evaluate multiple visual language models instantiated under different coding-agent frameworks, revealing substantial performance gaps at all task levels, with state-of-the-art models still struggling on full-stack development.

## One-Sentence Claim

Vision2Web evaluates visual coding agents across a hierarchy from static UI reproduction to long-horizon full-stack website development, using workflow-based agent verification.

## Problem

Coding agents are improving, but evaluation of complex visual website development remains shallow. Static screenshot-to-code tasks do not capture interactive pages, multi-page flows, or full-stack development with tests and user workflows.

The paper asks how to evaluate end-to-end website-building agents in a way that is realistic, hierarchical, and verifiable.

## Core Contribution

The contribution is Vision2Web, a hierarchical benchmark built from real-world websites. It spans static UI-to-code generation, interactive multi-page frontend reproduction, and long-horizon full-stack website development.

The benchmark includes 193 tasks across 16 categories, 918 prototype images, and 1,255 test cases. It also proposes workflow-based agent verification using a GUI agent verifier and a VLM-based judge.

## Method

Tasks are organized by complexity level, allowing models to be evaluated from local visual reproduction through full-stack workflows. The verification pipeline combines executable GUI interaction checks with visual-language judging for aspects that require perception or layout assessment.

Multiple visual language models are instantiated under different coding-agent frameworks to compare both model and agent scaffolding effects.

## Experiments and Evidence

Evidence reported in the abstract:

- 193 tasks across 16 categories.
- 918 prototype images.
- 1,255 test cases.
- Hierarchy from static UI-to-code to full-stack website development.
- GUI agent verifier plus VLM-based judge.
- Evaluation of multiple VLMs under different coding-agent frameworks.
- Substantial performance gaps at all levels.
- State-of-the-art models still struggle on full-stack development.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: website source selection, verifier reliability, judge calibration, and task leakage controls.

## Limits and Failure Modes

- VLM judges can be inconsistent or insensitive to functional defects.
- Real-world website tasks may involve licenses, assets, or dependencies that affect reproducibility.
- Full-stack evaluation can be brittle due to environment setup.
- Agent framework differences may confound pure model comparisons.

## Deep Themes

**Coding-agent evaluation is becoming workflow-based.** Real development needs interaction and verification, not only code generation.

**Visual fidelity and functional correctness must be checked together.** Website tasks span layout, interaction, and backend behavior.

**Benchmarks need hierarchies.** Difficulty levels reveal where agents fail as task scope expands.

## Subthemes

- Visual website development.
- Hierarchical coding-agent benchmark.
- GUI agent verification.
- VLM-based judging.
- Full-stack agent evaluation.

## Connections to Other Papers

Connects to RoTS, ThunderAgent, daVinci-Dev, VenusBench-Mobile, and MADQA. It reinforces the process-oriented agent evaluation theme.

## Notes for Cross-Paper Synthesis

Vision2Web adds a web-development-specific evaluation layer: agent progress should be measured across increasing workflow depth, with verification tied to real interactions.
