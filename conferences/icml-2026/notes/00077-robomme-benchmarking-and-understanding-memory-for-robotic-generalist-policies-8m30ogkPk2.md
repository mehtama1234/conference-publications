# RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 8m30ogkPk2
- Authors: Yinpei Dai; Hongze Fu; Jayjun Lee; Yuejiang Liu; Haoran Zhang; Jianing Yang; Chelsea Finn; Nima Fazeli; Joyce Chai
- Primary area: applications->robotics
- Keywords: Robot Manipulation;Benchmark;Memory-Augmented Policy;Vision-Language-Action Models
- Source URL: https://openreview.net/forum?id=8m30ogkPk2
- PDF URL: https://openreview.net/pdf?id=8m30ogkPk2

## Abstract

Memory is critical for long-horizon and history-dependent robotic manipulation. Such tasks often involve counting repeated actions or manipulating objects that become temporarily occluded. Recent vision-language-action (VLA) models have begun to incorporate memory mechanisms; however, their evaluations remain confined to narrow, non-standardized settings. This limits systematic understanding, comparison, and progress measurement.  To address these challenges, we introduce **RoboMME**: a large-scale standardized benchmark for evaluating and advancing VLA models in long-horizon, history-dependent scenarios. Our benchmark comprises 16 manipulation tasks constructed under a carefully designed taxonomy that evaluates *temporal*, *spatial*, *object*, and *procedural* memory. We further develop a suite of 14 memory-augmented VLA variants built on the $\pi_{0.5}$ backbone to systematically explore different memory representations across multiple integration strategies. We show that the effectiveness of memory representations is highly task-dependent, with each design offering distinct advantages and limitations across different tasks.  Videos and code can be found at https://robomme.github.io

## One-Sentence Claim

RoboMME benchmarks how memory mechanisms affect VLA robot policies on long-horizon, history-dependent manipulation tasks.

## Problem

Robotic manipulation often depends on past actions, occluded objects, and procedures, but memory-augmented VLA policies are evaluated in narrow and non-standardized settings.

## Core Contribution

The paper introduces RoboMME, a standardized benchmark with a memory taxonomy, and evaluates 14 memory-augmented VLA variants built on the pi_0.5 backbone.

## Method

RoboMME defines 16 manipulation tasks covering temporal, spatial, object, and procedural memory. The accompanying model suite varies memory representations and integration strategies to compare how designs behave across task types.

## Experiments and Evidence

The abstract reports that memory representation effectiveness is highly task-dependent, with each design showing distinct advantages and limitations.

## Limits and Failure Modes

ArXiv search failed with HTTP 429 for this batch, so this note is abstract-only. Details still need checking: task construction, memory-module implementations, evaluation metrics, real/sim split, and statistical reliability of policy comparisons.

## Deep Themes

- Robotic generalist policies need memory taxonomies, not just aggregate success rates.
- Long-horizon manipulation exposes temporal, spatial, object, and procedural memory gaps.
- Memory mechanisms are task-dependent control surfaces.

## Subthemes

- VLA models.
- Robotic memory.
- Long-horizon manipulation.
- History-dependent tasks.
- Memory-augmented policies.
- Benchmark standardization.

## Connections to Other Papers

Connects to SAW-Bench, dWorldEval, SCALE, EcoVLA, and BehaviorVLA through embodied evaluation. It also links to hybrid memory-role work through the question of which mechanism should carry which history.

## Notes for Cross-Paper Synthesis

RoboMME strengthens the embodied-memory theme: progress in robotic generalists depends on identifying the kind of memory a task requires.
