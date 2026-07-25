# Overparametrization bends the landscape: BBP transitions at initialization in simple Neural Networks

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: xDLE5n3x9Y
- Authors: Brandon Livio Annesi; Dario Bocchi; Chiara Cammarota
- Primary area: learning theory
- Keywords: Overparametrization;Loss landscapes;Signal recovery;High-dimensional learning
- Source URL: https://openreview.net/forum?id=xDLE5n3x9Y
- PDF URL: https://openreview.net/pdf?id=xDLE5n3x9Y

## Abstract

High-dimensional non-convex loss landscapes play a central role in the theory of Machine Learning. Gaining insight into how these landscapes interact with gradient-based optimization methods, even in relatively simple models, can shed light on this enigmatic feature of neural networks. In this work, we will focus on a prototypical simple learning problem, which generalizes the Phase Retrieval inference problem by allowing the exploration of overparametrized settings. Using techniques from field theory, we analyze the spectrum of the Hessian at initialization and identify a Baik–Ben Arous–Péché (BBP) transition in the amount of data that separates regimes where the initialization is informative or uninformative about a planted signal of a teacher-student setup. Crucially, we demonstrate how overparameterization can "bend" the loss landscape, shifting the transition point, even reaching the information-theoretic weak-recovery threshold in the large overparameterization limit, while also altering its qualitative nature.
 We distinguish between continuous and discontinuous BBP transitions and support our analytical predictions with simulations, examining how they compare to the finite-N behavior. In the case of discontinuous BBP transitions strong finite-N corrections allow the retrieval of information at a signal-to-noise ratio (SNR) smaller than the predicted BBP transition. In these cases we provide estimates for a new lower SNR threshold that marks the point at which initialization becomes entirely uninformative.

## One-Sentence Claim

The paper analyzes how overparameterization changes Hessian spectra at initialization, shifting BBP transitions and making simple neural-network landscapes informative at lower data or signal levels.

## Problem

High-dimensional nonconvex loss landscapes remain hard to understand, even in simple neural models. A key question is when initialization already contains recoverable information about a planted signal and how overparameterization changes that threshold.

## Core Contribution

The contribution is an analytical account of BBP transitions at initialization in an overparameterized generalization of phase retrieval. It shows that overparameterization can bend the loss landscape, shift transition points, approach the weak-recovery threshold in the large-overparameterization limit, and change whether transitions are continuous or discontinuous.

## Method

The paper uses field-theoretic techniques to analyze the Hessian spectrum at initialization in a teacher-student signal-recovery setup. It identifies data and signal-to-noise regimes where Hessian outliers reveal information about the planted signal, then studies how those regimes vary with overparameterization.

## Experiments and Evidence

The abstract reports simulations supporting the analytical predictions and comparing them to finite-N behavior. It also reports strong finite-N corrections in discontinuous transition regimes, where information can be retrieved below the predicted BBP transition, plus estimates for a lower SNR threshold where initialization becomes entirely uninformative.

## Limits and Failure Modes

This note is abstract/metadata-only. Full-text review should check the exact neural architecture, teacher-student assumptions, high-dimensional limits, finite-size corrections, and relationship to practical gradient descent. Results in simple phase-retrieval-like models may illuminate but not directly characterize large deep networks.

## Deep Themes

- Loss-landscape spectral theory.
- Overparameterization as geometric deformation.
- Initialization informativeness.
- Phase transitions in signal recovery.

## Subthemes

- BBP transitions.
- Hessian spectrum.
- Phase retrieval.
- Teacher-student models.
- Weak-recovery threshold.

## Connections to Other Papers

Connects to Track-and-Stop Theory through finite-regime guarantees, to representation-geometry papers through spectral/topological structure, and to Capacity Manipulation through internal resource geometry shaping what information can be represented or recovered.

## Notes for Cross-Paper Synthesis

This paper gives a theoretical foundation for a recurring empirical theme: model size changes the geometry of learning, not just the amount of capacity. Overparameterization can move phase transitions and alter what information is visible before training begins.
