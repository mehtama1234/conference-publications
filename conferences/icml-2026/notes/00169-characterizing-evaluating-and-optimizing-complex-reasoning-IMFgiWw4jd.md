# Characterizing, Evaluating, and Optimizing Complex Reasoning

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: IMFgiWw4jd
- Authors: Haoran Zhang; Yafu Li; Zhi Wang; Zhilin Wang; Shunkai Zhang; Xiaoye Qu; Yu Cheng
- Primary area: deep_learning->large_language_models
- Keywords: Large Reasoning Models;Complex Reasoning;Reasoning Trace Modeling
- Source URL: https://openreview.net/forum?id=IMFgiWw4jd
- PDF URL: https://openreview.net/pdf?id=IMFgiWw4jd

## Abstract

Large Reasoning Models (LRMs) increasingly rely on reasoning traces with complex internal structures. However, existing work lacks a unified answer to three fundamental questions: 
(1) what defines high-quality reasoning, 
(2) how to reliably evaluate long, implicitly structured reasoning traces, and 
(3) how to use such evaluation signals for reasoning optimization.
To address these challenges, we provide a unified perspective. (1) We introduce the ME$^2$ principle to characterize reasoning quality along macro- and micro-level concerning efficiency and effectiveness. (2) Built on this principle, we model reasoning traces as directed acyclic graphs (DAGs) and develop a DAG-based pairwise evaluation method, capturing complex reasoning structures. (3) Based on this method, we construct the TRM-Preference dataset and train a Thinking Reward Model (TRM) to evaluate reasoning quality at scale.
Experiments show that thinking rewards serve as an effective optimization signal. At test time, selecting better reasoning leads to better outcomes (up to 19.3\% gain), and during RL training, thinking rewards enhance reasoning and performance (up to 3.9\% gain) across diverse tasks. Code and data are available at https://github.com/Simplified-Reasoning/TRM.

## One-Sentence Claim

The paper models reasoning traces as DAGs and trains a Thinking Reward Model to evaluate and optimize complex reasoning quality at test time and during RL.

## Problem

Large reasoning models produce long, structured traces, but the field lacks a unified definition of quality, reliable trace evaluation, and scalable optimization signals for reasoning processes.

## Core Contribution

The paper introduces the ME2 principle for macro/micro efficiency and effectiveness, a DAG-based pairwise reasoning-trace evaluator, the TRM-Preference dataset, and a Thinking Reward Model.

## Method

Reasoning traces are represented as directed acyclic graphs to capture implicit structure. Pairwise evaluations built on ME2 produce preference data, which trains TRM to score reasoning quality and provide rewards for selection or RL optimization.

## Experiments and Evidence

The abstract reports that selecting higher-reward reasoning at test time improves outcomes by up to 19.3%, and using thinking rewards during RL improves reasoning and task performance by up to 3.9% across diverse tasks.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: DAG extraction method, annotation process, task suite, reward hacking risks, trace-length bias, and whether pairwise preferences generalize across domains.

## Deep Themes

- Process-level supervision for reasoning models.
- Structured trace representations as evaluation objects.
- Efficiency and effectiveness jointly define reasoning quality.

## Subthemes

- Large reasoning models.
- Reasoning trace modeling.
- Reward models.
- Pairwise preference data.
- Test-time selection.
- RL optimization.

## Connections to Other Papers

Connects to LALP, SOAR, CE-Graph, and other agent/reasoning papers that supervise intermediate reasoning processes rather than final answers alone.

## Notes for Cross-Paper Synthesis

This paper strengthens a major reasoning-process theme: the unit of optimization is shifting from answer correctness to structured trajectories with measurable local and global quality.
