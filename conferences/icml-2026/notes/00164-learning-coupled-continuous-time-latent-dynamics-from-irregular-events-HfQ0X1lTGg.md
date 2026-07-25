# Learning Coupled Continuous-Time Latent Dynamics from Irregular Events

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: HfQ0X1lTGg
- Authors: Jiankai Zuo; Yang Zhang; Yu Zhang; Jiarui Liang; Yaying Zhang
- Primary area: deep_learning->sequential_models_time_series
- Keywords: Continuous-Time Latent Dynamics;Coupled Dynamical Systems;Neural Ordinary Differential Equations;Diffusion Probabilistic Models;Irregularly Sampled Event Sequences;Latent Interpolation;Temporal Sparsity
- Source URL: https://openreview.net/forum?id=HfQ0X1lTGg
- PDF URL: https://openreview.net/pdf?id=HfQ0X1lTGg

## Abstract

Modeling dynamic dependencies from irregularly sampled event sequences is a fundamental challenge in modern machine learning. In many real-world systems, individual-level states evolve continuously over time while being simultaneously influenced by population-level dynamics. However, existing methods typically model these processes in isolation or rely on discrete-time approximations that fail to capture long-range temporal irregularities and sparse observations. This paper studies the problem of learning coupled continuous-time latent dynamics from irregular events, where individual event sequences and global distributional processes evolve asynchronously and interact over time. We propose a Coupled Continuous-Time Latent Dynamics (CoCLD) framework that jointly models individual latent dynamics and population-level distributional shifts, and aligns them in a continuous-time latent space. CoCLD integrates a Diffusion-based Latent Interpolator with neural ordinary differential equations, enabling principled interpolation, generation, and alignment of latent states across arbitrary time points. We show that the proposed coupling mechanism yields a consistent estimator of continuous-time latent dynamics under sparse and irregular observations. Empirical evaluations show CoCLD effectively captures dynamic dependencies and generalizes across tasks like next-event prediction, mobility trajectory generation, and sequential behavior modeling, indicating that learning coupled continuous-time latent dynamics is a powerful paradigm for irregular event sequence modeling.

## One-Sentence Claim

CoCLD models irregular event sequences by coupling individual continuous-time latent dynamics with asynchronous population-level distributional shifts.

## Problem

Real-world event sequences are sparse and irregular, and existing models often separate individual trajectories from population dynamics or approximate time with discrete steps that miss long-range temporal irregularity.

## Core Contribution

The paper proposes a coupled continuous-time latent-dynamics framework that aligns individual and population processes in a shared continuous-time latent space and provides consistency theory under sparse observations.

## Method

CoCLD combines neural ODEs with a diffusion-based latent interpolator to interpolate, generate, and align latent states at arbitrary time points while modeling interactions between individual event sequences and global distributional processes.

## Experiments and Evidence

The abstract reports empirical gains on next-event prediction, mobility trajectory generation, and sequential behavior modeling, indicating better capture of dynamic dependencies under irregular sampling.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: consistency assumptions, interpolation objective, diffusion architecture, computational cost over long sequences, datasets, and robustness to missing-not-at-random events.

## Deep Themes

- Continuous time as a more faithful substrate for real-world sequence modeling.
- Coupling individual and population dynamics rather than treating them independently.
- Generative interpolation as a bridge across sparse observations.

## Subthemes

- Irregular event sequences.
- Neural ODEs.
- Diffusion latent interpolation.
- Temporal sparsity.
- Population distribution shifts.
- Mobility and behavior modeling.

## Connections to Other Papers

Connects to time-series modeling and long-context papers through temporal extrapolation, and to diffusion/sampling papers through generative latent-state reconstruction.

## Notes for Cross-Paper Synthesis

CoCLD extends the corpus's structure-aware modeling theme into time: the right abstraction is not a fixed discrete sequence but interacting continuous processes observed sparsely and asynchronously.
