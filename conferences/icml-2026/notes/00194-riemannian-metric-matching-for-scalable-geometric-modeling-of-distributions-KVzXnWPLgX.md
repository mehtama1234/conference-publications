# Riemannian Metric Matching for Scalable Geometric Modeling of Distributions

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: KVzXnWPLgX
- Authors: Jacob Bamberger; Adam Gosztolai; Pierre Vandergheynst; Michael M. Bronstein; Iolo Jones
- Primary area: deep_learning->selfsupervised_learning
- Keywords: diffusion geometry;manifold hypothesis;geometric data analysis;Riemannian geometry;denoising
- Source URL: https://openreview.net/forum?id=KVzXnWPLgX
- PDF URL: https://openreview.net/pdf?id=KVzXnWPLgX

## Abstract

High-dimensional datasets often concentrate near low-dimensional structures, but estimating their geometry from samples typically relies on graphs and kernels that scale poorly with dataset size and dimension.
We propose **Riemannian metric matching**: a denoising probabilistic framework for learning the Riemannian geometry of data using neural networks.
Specifically, we learn the *carré du champ* operator, which, using diffusion geometry, gives us access to the Riemannian geometry toolkit for downstream machine learning and statistical tasks.
Our key observation is that the carré du champ operator can be formulated as a conditional expectation over random perturbations of the data,
which can be exploited for sample-wise training and constant cost, amortized inference without explicit kernel construction.
Empirically, metric matching rivals or improves the accuracy of $k$-NN-based diffusion geometry estimators, while enabling amortized inference that is up to $400\times$ faster, and supports graph-free geometric analysis on high-dimensional images where nearest neighbors break down.

## One-Sentence Claim

Riemannian metric matching learns data-manifold geometry with neural denoising, enabling graph-free amortized diffusion-geometry analysis in high dimensions.

## Problem

Estimating low-dimensional geometry in high-dimensional data usually relies on graphs or kernels that scale poorly and can fail when nearest neighbors become unreliable.

## Core Contribution

The paper formulates the carré du champ operator as a conditional expectation over random perturbations, allowing sample-wise training and constant-cost amortized inference of Riemannian geometry.

## Method

A denoising probabilistic framework trains neural networks to estimate the carré du champ operator, which provides access to Riemannian geometric tools without explicit kernel or k-NN graph construction.

## Experiments and Evidence

The abstract reports matching or improving k-NN diffusion-geometry estimator accuracy, up to 400x faster amortized inference, and graph-free geometric analysis on high-dimensional images where nearest-neighbor methods break down.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: perturbation distribution, geometry metrics, image datasets, manifold assumptions, robustness to noise, and downstream tasks using the learned metric.

## Deep Themes

- Neural denoising as scalable geometric estimation.
- Manifold hypothesis tools can be amortized instead of graph-built.
- Riemannian structure becomes a reusable representation for downstream analysis.

## Subthemes

- Diffusion geometry.
- Riemannian metric learning.
- Carré du champ operator.
- Denoising.
- Graph-free geometry.
- High-dimensional images.

## Connections to Other Papers

Connects to GFG, FlatLand, Top-W, and representation-geometry papers where learned geometry is used for modeling, routing, or verification.

## Notes for Cross-Paper Synthesis

Riemannian metric matching deepens the geometry theme by making data geometry itself a learned amortized object rather than a computationally expensive graph preprocessing step.
