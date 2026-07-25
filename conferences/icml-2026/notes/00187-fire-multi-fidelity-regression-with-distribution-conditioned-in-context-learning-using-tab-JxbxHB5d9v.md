# FIRE: Multi-Fidelity Regression with Distribution-Conditioned In-Context Learning Using Tabular Foundation Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: JxbxHB5d9v
- Authors: Rosen Ting-Ying Yu; Nicholas Sung; Faez Ahmed
- Primary area: applications
- Keywords: Multi-Fidelity;Multi-Fidelity Regression;Tabular Foundation Models
- Source URL: https://openreview.net/forum?id=JxbxHB5d9v
- PDF URL: https://openreview.net/pdf?id=JxbxHB5d9v

## Abstract

Multi-fidelity (MF) regression often operates in regimes of extreme data imbalance, where the commonly-used Gaussian-process surrogates struggle with cubic scaling costs and overfit to sparse high-fidelity observations, limiting efficiency and generalization in real-world applications. We introduce FIRE, a training-free MF framework that couples tabular foundation models (TFMs) to perform zero-shot in-context Bayesian inference via a high-fidelity correction model conditioned on the low-fidelity model's posterior predictive distributions. This cross-fidelity information transfer via distributional summaries captures heteroscedastic errors, enabling robust residual learning without model retraining. Across 31 benchmark problems spanning synthetic functions and real-world tasks (e.g., DrivAerNet, LCBench), FIRE delivers a stronger performance–time trade-off than seven state-of-the-art GP-based or deep learning MF regression methods, ranking highest in accuracy and uncertainty quantification with runtime advantages. Limitations include context window constraints and dependence on the quality of the pre-trained TFMs. Code & data can be found here: https://github.com/rosenyu304/FIRE.

## One-Sentence Claim

FIRE performs training-free multi-fidelity regression by using tabular foundation models for in-context Bayesian correction conditioned on low-fidelity posterior predictive distributions.

## Problem

Multi-fidelity regression often has severe imbalance between abundant low-fidelity and sparse high-fidelity data, while Gaussian-process surrogates can overfit high-fidelity observations and scale cubically.

## Core Contribution

The paper introduces a zero-shot, training-free framework that transfers cross-fidelity information through distributional summaries, capturing heteroscedastic residual errors without retraining.

## Method

FIRE couples tabular foundation models: a low-fidelity model produces posterior predictive distributions, and a high-fidelity correction model conditions on those distributional summaries for in-context Bayesian residual learning.

## Experiments and Evidence

The abstract reports results on 31 synthetic and real-world benchmarks, including DrivAerNet and LCBench, where FIRE has the best accuracy and uncertainty-quantification rankings plus runtime advantages over seven GP-based or deep learning multi-fidelity methods.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: tabular foundation models used, context-window limits, high/low-fidelity split design, uncertainty calibration, and sensitivity to pretrained TFM quality.

## Deep Themes

- Foundation models as training-free Bayesian surrogates for structured tabular tasks.
- Distributional summaries are reusable interfaces between fidelity levels.
- In-context learning can replace bespoke retraining in data-scarce scientific workflows.

## Subthemes

- Multi-fidelity regression.
- Tabular foundation models.
- In-context Bayesian inference.
- Heteroscedastic residual learning.
- Uncertainty quantification.
- Training-free transfer.

## Connections to Other Papers

Connects to AI-for-science and evaluation papers through surrogate modeling under data scarcity. It also parallels SSMoE and SmartFed by extracting new behavior from fixed pretrained components.

## Notes for Cross-Paper Synthesis

FIRE adds a tabular/scientific example of training-free adaptation: pretrained foundation models can be used as conditional inference engines when the right distributional interface is supplied.
