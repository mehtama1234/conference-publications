# Diffuse to Detect: Bi-Level Sample Rebalancing with Pseudo-Label Diffusion for Point-Supervised Infrared Small-Target Detection

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: RNn2wtNeoK
- Authors: Zhu Liu; Yuanhang Yao; Ping Qian; Zihang Chen; Risheng Liu
- Primary area: applications->computer_vision
- Keywords: Bi-Level Optimization;Sample Rebalancing;Pseudo-Label Diffusion;Small Target Detection
- Source URL: https://openreview.net/forum?id=RNn2wtNeoK
- PDF URL: https://openreview.net/pdf?id=RNn2wtNeoK

## Abstract

Point supervision has become a scalable solution to address dense annotation for infrared small target detection, but its performance is limited by two coupled bottlenecks: unstable pseudo-label evolution in cluttered, low-contrast infrared imagery and severe sample-distribution imbalance. In this paper, we present a more adaptive and stable framework to address these issues. Leveraging the intrinsic consistency between thermal radiation patterns and heat diffusion, we propose a physics-induced annotation strategy that expands single-point labels into reliable pseudo-masks. To further enhance supervision and alleviate sample imbalance, we develop a bi-level dual-update framework that jointly optimizes detector weights, sample weights, and diffusion parameters. A meta-classifier dynamically predicts sample-wise loss weights, while a differentiable diffusion module refines pseudo-labels with detection feedback, enabling adaptive interaction between training and hyperparameter optimization. Extensive experiments across multiple datasets demonstrate five-fold annotation acceleration, superior detection accuracy, and comparable performance with 30\% of the training data, validating the efficiency and practicality of our approach. Our code is available at https://github.com/yuanhang-yao/diffuse-to-detect.

## One-Sentence Claim

Diffuse to Detect improves point-supervised infrared small-target detection by expanding point labels into heat-diffusion pseudo-masks and jointly optimizing sample weights, diffusion parameters, and detector weights.

## Problem

Point supervision reduces dense annotation cost, but infrared small-target detection suffers unstable pseudo-labels in cluttered low-contrast scenes and severe sample-distribution imbalance.

## Core Contribution

The paper introduces a physics-induced annotation strategy plus a bi-level dual-update framework with a meta-classifier for sample weights and a differentiable diffusion module refined by detection feedback.

## Method

Single-point labels are expanded into pseudo-masks using thermal-radiation/heat-diffusion consistency. A bi-level optimization loop updates detector parameters, sample weights, and diffusion hyperparameters so pseudo-label refinement and sample rebalancing interact adaptively.

## Experiments and Evidence

The abstract reports five-fold annotation acceleration, better detection accuracy across multiple datasets, and comparable performance using 30% of the training data.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: infrared datasets, point-label protocol, diffusion physics assumptions, small-target metrics, meta-classifier stability, and robustness to non-thermal clutter.

## Deep Themes

- Weak supervision improves when pseudo-labels encode domain physics.
- Sample rebalancing and label refinement should be optimized jointly.
- Annotation efficiency is a deployment-critical dimension for vision systems.

## Subthemes

- Infrared small-target detection.
- Point supervision.
- Pseudo-label diffusion.
- Bi-level optimization.
- Sample rebalancing.
- Thermal radiation priors.

## Connections to Other Papers

Connects to PWC-Diff, CLEAR, and scientific/vision papers that use physical priors and weak supervision to reduce annotation or improve robustness.

## Notes for Cross-Paper Synthesis

This paper adds a weak-supervision physics theme: label expansion should follow the physical process governing the signal rather than generic smoothing.
