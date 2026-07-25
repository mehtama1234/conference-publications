# Scaling Real-World Robot Policy Evaluation via Discrete Diffusion World Model

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 93uNlQ1Qp0
- Authors: Yaxuan Li; Junjie Wen; Zhongyi Zhou; Yefei Chen; Chaomin Shen; Yaxin Peng; Yichen Zhu
- Primary area: applications->robotics
- Keywords: World Model;evaluation;VLA
- Source URL: https://openreview.net/forum?id=93uNlQ1Qp0
- PDF URL: https://openreview.net/pdf?id=93uNlQ1Qp0

## Abstract

Evaluating generalist robot manipulation policies is costly and difficult to scale in the real world. While emerging world models (e.g., WorldEval, Ctrl-World) offer a promising alternative, the reliability of such evaluation remains a critical bottleneck. 
Specifically, their visual predictions can undermine policy assessment by "self-correcting" failures into false positives or yielding artifacts under out-of-distribution controls.
Even with failure-enriched data, current architectures struggle to capture action-causal dynamics, as they typically treat actions as passive conditions rather than causal drivers.
To address this, we propose dWorldEval, an action-centric discrete-diffusion world model that maps visual observations, language instructions, and action chunks into a shared unified token space and denoises them with a single self-attention backbone where actions function as first-class tokens. 
To realize reliable policy-world interaction, dWorldEval introduces a sparse keyframe memory that anchors global scene state while preserving fine-grained multi-view interaction cues, and leverages Progress-as-text to jointly generate future observations and success indicators.
Extensive experiments on LIBERO, RoboTwin, and real-robot tasks demonstrate that dWorldEval significantly outperforms video diffusion baselines in action controllability, stabilizes long-horizon multi-view rollouts, enabling accurate policy ranking via automatic success estimation.

## One-Sentence Claim

dWorldEval scales robot policy evaluation by using an action-centric discrete-diffusion world model whose action tokens drive future visual and success predictions.

## Problem

Real-world robot evaluation is expensive, while existing world-model evaluators can self-correct failures into false positives or produce artifacts under out-of-distribution controls because they treat actions as passive conditions.

## Core Contribution

The paper proposes dWorldEval, a unified token-space discrete-diffusion world model for observations, language, and action chunks, with sparse keyframe memory and progress-as-text success prediction.

## Method

dWorldEval maps visual observations, instructions, and action chunks into shared tokens processed by one self-attention denoising backbone. Actions are first-class tokens, sparse keyframes anchor global scene state, and Progress-as-text jointly generates future observations and success indicators.

## Experiments and Evidence

The abstract reports experiments on LIBERO, RoboTwin, and real-robot tasks showing stronger action controllability, more stable long-horizon multi-view rollouts, and accurate automatic policy ranking.

## Limits and Failure Modes

ArXiv search failed with HTTP 429 for this batch, so this note is abstract-only. Details still need checking: world-model calibration, policy-ranking correlation, OOD action handling, failure false-positive rates, and real-robot scale.

## Deep Themes

- Robot policy evaluation is becoming a learned simulation problem.
- Action causality must be explicit in world models used for evaluation.
- Success prediction and visual rollout need to be coupled for reliable policy ranking.

## Subthemes

- Robot world models.
- Discrete diffusion.
- Action-centric tokens.
- Policy evaluation.
- Sparse keyframe memory.
- Progress-as-text.

## Connections to Other Papers

Connects to RoboMME, SAW-Bench, SCALE, and EcoVLA through scalable embodied evaluation and control. It also links to generative-model papers through diffusion as a simulation/evaluation substrate.

## Notes for Cross-Paper Synthesis

dWorldEval adds an evaluation-infrastructure theme: as robot policies become expensive to test, learned world models become part of the benchmark stack.
