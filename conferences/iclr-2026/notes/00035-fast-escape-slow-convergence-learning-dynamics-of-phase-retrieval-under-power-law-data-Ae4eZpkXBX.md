# Fast Escape, Slow Convergence: Learning Dynamics of Phase Retrieval under Power-Law Data

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: Ae4eZpkXBX
- Authors: Guillaume Braun; Bruno Loureiro; Minh Ha Quang; Masaaki Imaizumi
- Primary area: learning theory
- Keywords: scaling laws;gradient flow;power-law spectrum;phase retrieval;anisotropic data;learning dynamics
- Source URL: https://openreview.net/forum?id=Ae4eZpkXBX
- PDF URL: https://openreview.net/pdf?id=Ae4eZpkXBX

## Abstract

Scaling laws describe how learning performance improves with data, compute, or training time, and have become a central theme in modern deep learning. We study this phenomenon in a canonical nonlinear model: phase retrieval with anisotropic Gaussian inputs whose covariance spectrum follows a power law. Unlike the isotropic case, where dynamics collapse to a two-dimensional system, anisotropy yields a qualitatively new regime in which an infinite hierarchy of coupled equations governs the evolution of the summary statistics. We develop a tractable reduction that reveals a three-phase trajectory: (i) fast escape from low alignment, (ii) slow convergence of the summary statistics, and (iii) spectral-tail learning in low-variance directions. From this decomposition, we derive explicit scaling laws for the mean-squared error, showing how spectral decay dictates convergence times and error curves. Experiments confirm the predicted phases and exponents. These results provide the first rigorous characterization of scaling laws in nonlinear regression with anisotropic data, highlighting how anisotropy reshapes learning dynamics.

## One-Sentence Claim

Power-law anisotropy in phase retrieval creates three learning phases whose convergence rates and error curves are dictated by spectral decay.

## Problem

Scaling laws are central in deep learning, but rigorous characterizations in nonlinear models with anisotropic data are limited.

In isotropic phase retrieval, dynamics collapse to a low-dimensional system. With anisotropic Gaussian inputs and power-law covariance spectra, learning dynamics become much richer.

## Core Contribution

The paper develops a tractable reduction for phase retrieval with power-law anisotropic Gaussian data.

It reveals a three-phase trajectory: fast escape from low alignment, slow convergence of summary statistics, and spectral-tail learning in low-variance directions.

## Method

The analysis derives an infinite hierarchy of coupled equations for summary statistics under anisotropy, then reduces it to a tractable form.

From this decomposition, it derives explicit scaling laws for mean-squared error as a function of spectral decay, convergence time, and learning phase.

## Experiments and Evidence

The abstract reports experiments confirming predicted phases and exponents.

The theoretical contribution is described as the first rigorous characterization of scaling laws in nonlinear regression with anisotropic data.

## Limits and Failure Modes

Phase retrieval is a stylized nonlinear model; lessons may transfer qualitatively rather than directly to deep networks.

Because this note is abstract-only, details still need checking: exact covariance assumptions, gradient-flow setup, reduction method, exponent formulas, finite-sample experiments, and robustness beyond Gaussian inputs.

## Deep Themes

- Anisotropy reshapes learning dynamics: data spectrum controls convergence stages.
- Scaling laws beyond empirical fitting: exponents can be derived from model and data structure.
- Fast escape versus slow convergence: early progress can hide long tail learning.
- Low-variance directions matter: spectral tails can dominate final error and training time.

## Subthemes

- Phase retrieval.
- Power-law covariance spectra.
- Infinite hierarchy of summary statistics.
- Spectral-tail learning.

## Connections to Other Papers

This connects to ICML scaling-law papers, Gaussian single-index learning, alignment-sensitive spectral algorithms, and embedding collapse through theory of anisotropic representation learning.

It also relates to coverage theory because both aim to replace coarse loss narratives with sharper quantities predicting downstream behavior.

## Notes for Cross-Paper Synthesis

This paper adds a spectral-dynamics theme: learning can escape quickly while still spending most of its time fitting low-variance directions that determine final performance.
