# On the Wasserstein Geodesic Principal Component Analysis of probability measures

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: OJupg4mDjS
- Authors: Nina Vesseron; Elsa Cazelles; Alice Le Brigant; Klein
- Primary area: unsupervised, self-supervised, semi-supervised, and supervised representation learning
- Keywords: wasserstein PCA;optimal transport;deep learning
- Source URL: https://openreview.net/forum?id=OJupg4mDjS
- PDF URL: https://openreview.net/pdf?id=OJupg4mDjS

## Abstract

This paper focuses on Geodesic Principal Component Analysis (GPCA) on a collection of probability distributions using the Otto-Wasserstein geometry. The goal is to identify geodesic curves in the space of probability measures that best capture the modes of variation of the underlying dataset. We first address the case of a collection of Gaussian distributions, and show how to lift the computations in the space of invertible linear maps. For the more general setting of absolutely continuous probability measures, we leverage a novel approach to parameterizing geodesics in Wasserstein space with neural networks. Finally, we compare to classical tangent PCA through various examples and provide illustrations on real-world datasets.

## One-Sentence Claim

This paper develops Wasserstein geodesic PCA methods for probability measures, including Gaussian lifting to invertible maps and neural parameterizations for general absolutely continuous distributions.

## Problem

Classical PCA assumes linear structure in Euclidean vector spaces, but datasets of probability distributions live on nonlinear spaces where variation should respect distributional geometry.

Tangent-space PCA can approximate local variation, but may miss global geodesic modes in Otto-Wasserstein geometry.

## Core Contribution

The paper studies Geodesic PCA over probability measures under Otto-Wasserstein geometry.

It gives a computational treatment for Gaussian distributions by lifting to invertible linear maps and introduces neural-network parameterizations for geodesics among general absolutely continuous measures.

## Method

For Gaussian collections, the method transfers Wasserstein-geodesic computations into a space of invertible linear maps, where structure is easier to manipulate.

For general absolutely continuous distributions, it parameterizes Wasserstein geodesics with neural networks and compares the resulting GPCA curves against classical tangent PCA.

## Experiments and Evidence

The abstract reports comparisons with tangent PCA on several examples and illustrations on real-world datasets.

The evidence appears focused on whether Wasserstein geodesic curves better capture modes of distributional variation than local tangent approximations.

## Limits and Failure Modes

Neural geodesic parameterizations may be difficult to optimize and may depend on regularity assumptions for probability measures. Global geodesic PCA can also be computationally more expensive than tangent methods.

Because this note is abstract-only, details still need checking: objective formulation, constraints guaranteeing valid geodesics, Gaussian lifting derivation, real datasets, metrics, and scalability.

## Deep Themes

- Geometry of distributions: probability measures require representation methods that respect transport structure.
- Nonlinear PCA beyond tangent approximations: principal variation can be modeled as geodesic curves.
- Neural optimal transport parameterization: deep networks approximate geometric objects in measure space.
- Structured unsupervised learning: representation learning is guided by mathematical geometry rather than generic embeddings.

## Subthemes

- Wasserstein GPCA.
- Otto geometry.
- Invertible linear-map lifting.
- Neural geodesic parameterization.

## Connections to Other Papers

This connects to optimal-transport and representation-geometry papers, including hyperparameter trajectory inference and quotient-space diffusion.

It also relates to SFA because both combine probabilistic structure with modern neural parameterizations.

## Notes for Cross-Paper Synthesis

Wasserstein GPCA reinforces a theory-to-representation theme: better latent summaries often require respecting the geometry of the object being represented.
