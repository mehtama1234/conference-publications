# Recovering Policy-Induced Errors: Benchmarking and Trajectory Synthesis for Robust GUI Agents

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: iJwDylm93H
- Authors: Tianpeng Bu; Xin Liu; Qihua Chen; Hao Jiang; Shurui Li; hongtao duan; Lu Jiang; lulu hu; Bin Yang; Minying Zhang
- Primary area: applications->everything_else
- Keywords: Robust GUI Agent;Visual Language Model;Computer Use Agent;Error Recovery of GUI Agents
- Source URL: https://openreview.net/forum?id=iJwDylm93H
- PDF URL: https://openreview.net/pdf?id=iJwDylm93H

## Abstract

While GUI agents have advanced rapidly, they often lack the robustness to recover from their own errors, hindering real-world deployment. To bridge this gap at both the evaluation and data levels, we introduce GUI-RobustEval and propose Robustness-driven Trajectory Synthesis. GUI-RobustEval contains 1,216 executable test cases that systematically measure error recovery capabilities across a broad and realistic spectrum of error modes. At the data level, RoTS is a scalable synthesis framework that creates 800k high-quality data via a tree-based pipeline that proactively discovers diverse error modes and synthesizes corresponding recovery steps. Our two models, RoTS-7B and RoTS-32B, fine-tuned on our dataset, both demonstrate significant gains on GUI-RobustEval and traditional GUI benchmarks. Notably, RoTS-32B achieves state-of-the-art performance on OSWorld, with a 47.4% success rate and a 33.8% All-Pass@4 score, suggesting that improved long-horizon error recovery ability contributes to both robustness and overall performance. Our code is available at https://github.com/AlibabaResearch/RoTS

## One-Sentence Claim

GUI-RobustEval and RoTS target GUI agents' ability to recover from their own policy-induced errors, showing that synthesized recovery trajectories improve both robustness and general GUI performance.

## Problem

GUI agents can complete some tasks but often fail after making their own mistakes. Real-world computer-use agents need long-horizon recovery: recognizing that an action went wrong, undoing or compensating, and continuing toward the goal.

The paper addresses this at both evaluation and data levels because ordinary GUI benchmarks may not isolate error recovery.

## Core Contribution

The paper introduces GUI-RobustEval, a benchmark with 1,216 executable test cases covering diverse error modes, and Robustness-driven Trajectory Synthesis, a scalable tree-based pipeline that discovers error modes and synthesizes recovery steps.

RoTS creates 800k high-quality training trajectories. Fine-tuned RoTS-7B and RoTS-32B models improve on GUI-RobustEval and traditional GUI benchmarks, with RoTS-32B reaching state-of-the-art OSWorld performance.

## Method

GUI-RobustEval systematically injects or exposes policy-induced error scenarios in executable GUI tasks. RoTS uses a tree-based synthesis process to branch into diverse failure modes and generate corresponding recovery trajectories.

Training on these trajectories teaches the agent not only the ideal path but how to re-enter a productive state after mistakes.

## Experiments and Evidence

Evidence reported in the abstract:

- GUI-RobustEval with 1,216 executable test cases.
- RoTS synthesis of 800k high-quality recovery data.
- RoTS-7B and RoTS-32B both improve on GUI-RobustEval and traditional GUI benchmarks.
- RoTS-32B achieves 47.4% success on OSWorld.
- RoTS-32B achieves 33.8% All-Pass@4 on OSWorld.
- Long-horizon error recovery improves robustness and overall performance.
- Code release at the listed GitHub URL.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: error taxonomy, synthesis validation, base models, and benchmark overlap controls.

## Limits and Failure Modes

- Synthetic recovery trajectories may not cover rare real-world UI failures.
- Agents can overfit to benchmark-style error modes.
- Executable GUI evaluation depends on environment stability and reproducibility.
- Recovery may require memory and causal diagnosis, not just local corrective actions.

## Deep Themes

**Robust agents need recovery data.** Training only on successful trajectories leaves agents brittle after mistakes.

**Evaluation should include self-induced failures.** Real deployment depends on what the agent does after it causes trouble.

**Trajectory synthesis can target failure modes.** RoTS proactively constructs the negative space missing from ordinary demonstrations.

## Subthemes

- GUI error recovery.
- Policy-induced failures.
- Executable robustness benchmark.
- Tree-based trajectory synthesis.
- Long-horizon computer-use agents.

## Connections to Other Papers

Connects to VenusBench-Mobile, MADQA, daVinci-Dev, Agent0-VL, and Monitoring Monitorability. It shares the agent-process theme: success depends on trajectory management, not just final-answer accuracy.

## Notes for Cross-Paper Synthesis

RoTS strengthens the agent robustness theme by making recovery a first-class training target and benchmark dimension.
