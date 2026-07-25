# Self-Distillation Enables Continual Learning

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: qA6FgH0nnZ
- Authors: Idan Shenfeld; Mehul Damani; Jonas Hübotter; Pulkit Agrawal
- Primary area: deep_learning->algorithms
- Keywords: continual learning;distillation;large language models
- Source URL: https://openreview.net/forum?id=qA6FgH0nnZ
- PDF URL: https://openreview.net/pdf?id=qA6FgH0nnZ

## Abstract

Continual learning, enabling models to acquire new skills and knowledge without degrading existing capabilities, remains a fundamental challenge for foundation models. While on-policy reinforcement learning can reduce forgetting, it requires explicit reward functions that are often unavailable. Learning from expert demonstrations, the primary alternative, is dominated by supervised fine-tuning (SFT), which is inherently off-policy. We introduce Self-Distillation Fine-Tuning (SDFT), a simple method that enables on-policy learning directly from demonstrations. SDFT leverages in-context learning by using a demonstration-conditioned model as its own teacher, generating on-policy training signals that preserve prior capabilities while acquiring new skills. Across skill learning and knowledge acquisition tasks, SDFT consistently outperforms SFT, achieving higher new-task accuracy while substantially reducing catastrophic forgetting. In sequential learning experiments, SDFT enables a single model to accumulate multiple skills over time without performance regression, establishing on-policy distillation as a practical path to continual learning from demonstrations.

## One-Sentence Claim

Self-Distillation Fine-Tuning converts demonstrations into on-policy training signals by using a demonstration-conditioned model as its own teacher, improving new-skill learning while reducing catastrophic forgetting.

## Problem

Continual learning for foundation models requires acquiring new skills or knowledge without degrading existing capabilities. Supervised fine-tuning from demonstrations is the standard practical method, but it is off-policy: it trains the model to imitate expert data rather than learn from the model's own induced behavior distribution.

On-policy RL can reduce forgetting, but it usually requires explicit reward functions, which are not available for many demonstration-based tasks. The paper targets the gap between demonstration learning and on-policy continual adaptation.

## Core Contribution

The paper introduces Self-Distillation Fine-Tuning, a simple method that uses in-context learning to make the model its own teacher. A demonstration-conditioned version of the model generates on-policy training signals, enabling learning from demonstrations while preserving prior capabilities.

The contribution is to turn demonstrations into an on-policy distillation source. This gives the benefits of policy-consistent learning without needing hand-designed rewards.

## Method

SDFT conditions the model on demonstrations and asks that conditioned model to generate target behavior. The base model is then trained on these self-generated, on-policy signals rather than directly imitating the original expert trajectories through ordinary SFT.

Because the teacher is the same model under demonstration conditioning, the training distribution is closer to the learner's own policy. This reduces the mismatch that can cause supervised fine-tuning to overwrite prior behavior.

## Experiments and Evidence

The abstract reports that SDFT consistently outperforms SFT across skill learning and knowledge acquisition tasks. It achieves higher new-task accuracy and substantially reduces catastrophic forgetting.

In sequential learning experiments, a single model accumulates multiple skills over time without performance regression. Full-paper reading should verify task suites, demonstration sizes, baseline tuning, forgetting metrics, and how self-generated targets are filtered.

## Limits and Failure Modes

Self-distillation can propagate the model's own mistakes if demonstration-conditioned outputs are wrong or overconfident. It may also preserve prior capabilities partly by being conservative, which could limit learning of genuinely novel behaviors.

The method's success likely depends on the base model's in-context ability. If the model cannot infer the target skill from demonstrations, the self-teacher will not produce useful on-policy targets.

## Deep Themes

- On-policy learning without rewards: demonstration-conditioned self-teaching approximates RL-like distribution matching.
- Continual learning through self-generated targets: the model adapts while reducing off-policy overwrite.
- In-context learning as a teacher mechanism: prompting supplies temporary skill acquisition that can be distilled.
- Forgetting as distribution mismatch: SDFT treats catastrophic forgetting as partly caused by SFT's off-policy nature.

## Subthemes

- Sequential skill accumulation is a stronger test than isolated finetuning.
- Demonstrations can guide policy improvement without explicit rewards.
- Self-distillation depends on teacher quality and calibration.
- Prior capability preservation is a first-class continual-learning metric.

## Connections to Other Papers

SDFT connects to JitRL and post-training policy-gradient theory: all study adaptation without simply applying ordinary SFT. JitRL adapts through memory/logits at test time, while SDFT adapts weights through on-policy self-distillation.

It also relates to BLL-Loss and outcome-over-realization training, since both critique naive token imitation as a misaligned objective for behavior acquisition.

## Notes for Cross-Paper Synthesis

The cross-paper pattern is that demonstrations are being reinterpreted. They are not just sequences to imitate; they can condition teachers, define outcomes, or induce policy updates that better match deployment behavior.
