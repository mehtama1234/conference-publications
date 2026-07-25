# Hyperparameter Trajectory Inference with Conditional Lagrangian Optimal Transport

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: P5B97gZwRb
- Authors: Harry Amad; Mihaela van der Schaar
- Primary area: other topics in machine learning (i.e., none of the above)
- Keywords: hyperparameter;optimal transport;trajectory inference;manifold learning;interpolation
- Source URL: https://openreview.net/forum?id=P5B97gZwRb
- PDF URL: https://openreview.net/pdf?id=P5B97gZwRb

## Abstract

Neural networks (NNs) often have critical behavioural trade-offs that are set at design time with hyperparameters—such as reward weighting in reinforcement learning or quantile targets in regression. 
Post-deployment, however, user preferences can evolve, making initially optimal settings undesirable, necessitating expensive retraining. 
To circumvent this, we introduce the task of Hyperparameter Trajectory Inference (HTI), to learn, from observed data, how a NN's conditional output distribution changes as a function of its hyperparameters, such that a surrogate model can approximate the NN at unobserved hyperparameter settings. 
HTI requires extending existing trajectory inference approaches to incorporate conditions, posing key challenges to ensure meaningful inferred conditional probability paths. 
We propose an approach grounded in conditional Lagrangian optimal transport theory, jointly learning the Lagrangian function governing hyperparameter-induced dynamics along with the associated optimal transport maps and geodesics, which form the surrogate model.
We incorporate inductive biases based on the manifold hypothesis and least-action principles into the learned Lagrangian, improving surrogate model feasibility.
We empirically demonstrate that our approach reconstructs NN behaviour across hyperparameter spectrums better than other alternatives, enabling effective inference-time adaptation of NNs.

## One-Sentence Claim

Hyperparameter Trajectory Inference learns conditional optimal-transport paths that approximate how a neural network's output distribution changes across hyperparameter settings, enabling inference-time adaptation without retraining.

## Problem

Neural network behavior is often set by design-time hyperparameters such as reward weights or quantile targets. After deployment, user preferences or operating requirements can change, making the original hyperparameter choice suboptimal.

Retraining models for every new setting is expensive. The challenge is to infer the behavioral path across hyperparameters from observed data and approximate unobserved settings.

## Core Contribution

The paper introduces Hyperparameter Trajectory Inference and proposes a method based on conditional Lagrangian optimal transport.

It jointly learns a Lagrangian governing hyperparameter-induced dynamics, optimal transport maps, and geodesics that form a surrogate model over hyperparameter settings.

## Method

The approach extends trajectory inference to conditional probability paths. It learns how the conditional output distribution moves as hyperparameters vary.

Inductive biases from the manifold hypothesis and least-action principles are incorporated into the learned Lagrangian, making inferred trajectories more feasible and structured.

## Experiments and Evidence

The abstract reports empirical reconstruction of neural-network behavior across hyperparameter spectra.

The proposed method performs better than alternatives and enables effective inference-time adaptation of neural networks.

## Limits and Failure Modes

The surrogate may fail when hyperparameter changes cause discontinuous behavior, new failure modes, or representation shifts not covered by observed settings. Learning transport maps may also be expensive for high-dimensional outputs.

Because this note is abstract-only, details still need checking: observed hyperparameter grids, output-distribution representation, OT objective, baselines, adaptation tasks, and uncertainty calibration.

## Deep Themes

- Post-deployment adaptability: models should respond to changed preferences without full retraining.
- Hyperparameters as trajectories: design knobs induce paths through output-distribution space.
- Optimal transport for model behavior: transport geometry models how predictions change under conditions.
- Least-action inductive bias: physical-style principles regularize learned behavioral surrogates.

## Subthemes

- Hyperparameter trajectory inference.
- Conditional Lagrangian optimal transport.
- Inference-time adaptation.
- Manifold and least-action priors.

## Connections to Other Papers

This connects to Wasserstein GPCA and other optimal-transport geometry papers.

It also relates to SafeDPO, p-less sampling, and Train-before-Test because all examine how model behavior changes under adaptation, objectives, or control parameters.

## Notes for Cross-Paper Synthesis

HTI adds an adaptation theme: instead of retraining for every preference shift, learn the geometry of how behavior moves under hyperparameter changes.
