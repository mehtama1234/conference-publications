# Rate or Fate? RLV$^{\varepsilon}$R: Reinforcement Learning with Verifiable Noisy Rewards

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: LwB2EacVT6
- Authors: Ali Rad; Khashayar Filom; Darioush Keivan; Peyman Mohajerin Esfahani; Ehsan Kamalinejad
- Primary area: deep_learning->large_language_models
- Keywords: LLM;Nosie in reward;RLVR;GRPO
- Source URL: https://openreview.net/forum?id=LwB2EacVT6
- PDF URL: https://openreview.net/pdf?id=LwB2EacVT6

## Abstract

Reinforcement learning with verifiable rewards (RLVR) trains a policy by verifying sampled completions and reinforcing higher-scoring outputs, but practical verifiers (e.g., incomplete unit tests or noisy judges) are prone to false positives and false negatives.
We ask when such noise merely slows learning and when it reverses it.
Modeling GRPO-style RLVR as a bandit over recurring \emph{reasoning modes}, we derive mean-field replicator-style (natural-selection) flow on the probability simplex. The dynamics decouples into within-correct-mode competition and a one-dimensional evolution for the mass on incorrect modes, whose drift is determined solely by Youden's index $J=\mathrm{TPR}-\mathrm{FPR}$. This yields a sharp phase transition: when $J>0$, the incorrect mass is driven toward extinction (learning); when $J=0$, the process is neutral; and when $J<0$, incorrect modes amplify until they dominate (anti-learning and collapse). In the learning regime $J>0$, noise primarily rescales convergence time (``rate, not fate''). Experiments on verifiable programming tasks under synthetic noise reproduce the predicted $J=0$ boundary. Beyond noise, the framework offers a general lens for analyzing RLVR stability, convergence, and algorithmic interventions.

## One-Sentence Claim

RLVR with noisy verifiers has a sharp phase transition controlled by Youden's index: positive verifier signal slows but preserves learning, while negative signal drives anti-learning collapse.

## Problem

Reinforcement learning with verifiable rewards depends on imperfect verifiers such as incomplete unit tests or noisy judges, but it is unclear when false positives/negatives merely slow optimization versus reverse it.

## Core Contribution

The paper models GRPO-style RLVR as a bandit over recurring reasoning modes and derives replicator-style dynamics showing that the mass on incorrect modes is governed solely by J = TPR - FPR.

## Method

The mean-field analysis decouples within-correct-mode competition from one-dimensional incorrect-mode mass evolution, yielding regimes where incorrect modes go extinct, drift neutrally, or amplify. Experiments inject synthetic verifier noise into programming tasks to test the predicted boundary.

## Experiments and Evidence

The abstract reports synthetic-noise programming experiments reproducing the J=0 boundary and supports the claim that in the J>0 regime noise changes convergence rate rather than final learning fate.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: reasoning-mode abstraction, GRPO assumptions, verifier-noise models, nonstationary policies, real noisy judge behavior, and interventions for J near or below zero.

## Deep Themes

- Alignment training stability depends on verifier signal quality.
- A single diagnostic statistic can separate learning from collapse.
- RL dynamics over reasoning modes can be understood through evolutionary flow.

## Subthemes

- RLVR.
- GRPO.
- Noisy rewards.
- Youden's index.
- Programming verification.
- Replicator dynamics.

## Connections to Other Papers

Connects to TRM, SOAR, and reward-modeling papers through process optimization under imperfect feedback. It also relates to tail-risk and safety papers because verifier errors can amplify undesirable behavior.

## Notes for Cross-Paper Synthesis

This paper adds a feedback-quality threshold theme: noisy supervision is not uniformly harmful; whether it changes rate or fate depends on the directionality of the verifier signal.
