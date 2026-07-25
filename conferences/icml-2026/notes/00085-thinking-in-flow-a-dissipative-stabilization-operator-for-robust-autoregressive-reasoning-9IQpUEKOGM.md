# Thinking in Flow: A Dissipative Stabilization Operator for Robust Autoregressive Reasoning

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 9IQpUEKOGM
- Authors: Yujie Huang; Wenwu He; Zhuo-Xu Cui
- Primary area: deep_learning->robustness
- Keywords: Large Language Models;Chain-of-Thought;Neural ODEs;Dissipative Stabilization
- Source URL: https://openreview.net/forum?id=9IQpUEKOGM
- PDF URL: https://openreview.net/pdf?id=9IQpUEKOGM

## Abstract

Chain-of-Thought (CoT) prompting enables multi-step reasoning in large language models, yet long-horizon generation remains brittle under distribution shift and context interference: irrelevant cues persist, small deviations compound into inference drift, and late-stage corrections can destabilize the trajectory. We recast autoregressive decoding as a perturbed long-horizon dynamical system and introduce an *inference-time stabilization operator* that targets *trajectory-level* reliability rather than token-level fluency. Specifically, we propose *ODE-guided language models*, which augment a base Transformer with a persistent continuous-time *thought state* whose dynamics are explicitly designed to be dissipative, enabling stable evidence accumulation with controlled forgetting. Instantiating this framework, *Thinking in Flow* (TiF) equips the model with a lightweight Neural ODE controller and injects its output through post-norm residual updates to achieve numerically stable, low-intrusion steering. A demand--supply (uncertainty--capacity) gate determines *when* intervention is warranted, while a direction gate determines *how* to steer in representation space, yielding selective, do-no-harm corrections instead of persistent bias. We establish well-posedness, dissipativity, and incremental stability of the controlled thought dynamics, implying bounded interventions over arbitrarily long contexts, and empirically demonstrate improved robustness to distractions and semantic perturbations, while matching or improving accuracy on mathematical reasoning benchmarks across both the Llama and Qwen model families; we further observe gains on non-mathematical BBH reasoning tasks when training TiF on Llama.

## One-Sentence Claim

Thinking in Flow stabilizes long-horizon autoregressive reasoning with an inference-time Neural ODE thought state designed for dissipative, selective representation steering.

## Problem

Chain-of-thought generation is brittle under distribution shift and context interference: irrelevant cues persist, small deviations compound, and late corrections can destabilize the reasoning trajectory.

## Core Contribution

The paper recasts autoregressive decoding as a perturbed long-horizon dynamical system and introduces ODE-guided language models with a dissipative stabilization operator.

## Method

TiF adds a persistent continuous-time thought state controlled by a lightweight Neural ODE. Its output is injected through post-norm residual updates, with a demand-supply gate deciding when intervention is needed and a direction gate deciding how to steer representation space.

## Experiments and Evidence

The abstract reports well-posedness, dissipativity, and incremental stability guarantees, plus improved robustness to distractions and semantic perturbations while matching or improving mathematical reasoning accuracy across Llama and Qwen families. It also reports gains on non-mathematical BBH tasks after training on Llama.

## Limits and Failure Modes

ArXiv search failed with HTTP 429 for this batch, so this note is abstract-only. Details still need checking: controller training data, inference overhead, gate calibration, benchmark coverage, and whether stabilization suppresses creative but valid reasoning paths.

## Deep Themes

- Reasoning can be modeled as a dynamical trajectory requiring stabilization.
- Inference-time control can target trajectory reliability rather than token fluency.
- Controlled forgetting may be as important as evidence accumulation in long contexts.

## Subthemes

- Chain-of-thought robustness.
- Neural ODE controllers.
- Dissipative stabilization.
- Inference-time steering.
- Long-horizon reasoning.
- Context interference.

## Connections to Other Papers

Connects to Rex, IRNO, and other numerical/dynamical-systems papers through continuous-time control ideas. It also links to test-time scaling and robustness papers through inference-time intervention.

## Notes for Cross-Paper Synthesis

TiF strengthens the dynamical-systems view of reasoning: robust generation is treated as stabilizing a trajectory, not merely choosing the next token.
