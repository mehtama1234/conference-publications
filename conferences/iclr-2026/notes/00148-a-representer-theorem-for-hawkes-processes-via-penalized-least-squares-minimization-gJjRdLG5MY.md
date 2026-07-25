# A Representer Theorem for Hawkes Processes via Penalized Least Squares Minimization

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: gJjRdLG5MY
- Authors: Hideaki Kim; Tomoharu Iwata
- Primary area: learning theory
- Keywords: Hawkes processes;kernel methods;representer theorem;point processes;least squares loss
- Source URL: https://openreview.net/forum?id=gJjRdLG5MY
- PDF URL: https://openreview.net/pdf?id=gJjRdLG5MY

## Abstract

The representer theorem is a cornerstone of kernel methods, which aim to estimate latent functions in reproducing kernel Hilbert spaces (RKHSs) in a nonparametric manner. Its significance lies in converting inherently infinite-dimensional optimization problems into finite-dimensional ones over dual coefficients, thereby enabling practical and computationally tractable algorithms. In this paper, we address the problem of estimating the latent triggering kernels--functions that encode the interaction structure between events--for linear multivariate Hawkes processes based on observed event sequences within an RKHS framework. We show that, under the principle of penalized least squares minimization, a novel form of representer theorem emerges: a family of transformed kernels can be defined via a system of simultaneous integral equations, and the optimal estimator of each triggering kernel is expressed as a linear combination of these transformed kernels evaluated at the data points. Remarkably, the dual coefficients are all analytically fixed to unity, obviating the need to solve a costly optimization problem to obtain the dual coefficients. This leads to a highly efficient estimator capable of handling large-scale data more effectively than conventional nonparametric approaches. Empirical evaluations on synthetic datasets reveal that the proposed method attains competitive predictive accuracy while substantially improving computational efficiency over existing state-of-the-art kernel method-based estimators.

## One-Sentence Claim

This paper derives a representer theorem for multivariate Hawkes triggering kernels under penalized least squares, yielding efficient finite-dimensional estimators with analytically fixed dual coefficients.

## Problem

Hawkes processes model event interactions through latent triggering kernels, but nonparametric RKHS estimation is infinite-dimensional and computationally costly.

Existing kernel methods may require expensive optimization over dual coefficients for large event-sequence datasets.

## Core Contribution

The paper establishes a novel representer theorem for linear multivariate Hawkes processes.

It defines transformed kernels through simultaneous integral equations and shows optimal triggering-kernel estimators are linear combinations of these transformed kernels evaluated at data points, with all dual coefficients fixed to one.

## Method

The method uses penalized least squares in an RKHS framework.

The theorem converts the infinite-dimensional functional estimation problem into a finite-dimensional estimator, while avoiding coefficient optimization because the coefficients are analytically determined.

## Experiments and Evidence

The abstract reports empirical evaluations on synthetic datasets.

The proposed estimator achieves competitive predictive accuracy and substantially better computational efficiency than existing state-of-the-art kernel-based estimators.

## Limits and Failure Modes

Synthetic datasets may not capture real point-process complexities such as nonstationarity, marks, censoring, inhibition, or exogenous covariates.

Because this note is abstract-only, details still need checking: integral-equation system, RKHS assumptions, stability conditions, multivariate scaling, synthetic setups, and runtime comparisons.

## Deep Themes

- Classical kernel theory for temporal events: representer theorems remain useful for modern scalable estimation.
- Infinite-to-finite reduction: tractability comes from structural form, not approximation alone.
- Interaction-kernel estimation: Hawkes processes expose causal-like event influence through triggering functions.
- Analytic coefficient simplification: fixed dual weights remove a costly optimization layer.

## Subthemes

- Hawkes processes.
- RKHS.
- Penalized least squares.
- Transformed kernels.

## Connections to Other Papers

This connects to theory/optimization papers, causal temporal-process work, and point-process modeling.

It also relates to Koopman and dynamical-systems representation papers because all model temporal dependence through structured operators or kernels.

## Notes for Cross-Paper Synthesis

This paper adds a classical-theory efficiency theme: exact representer structure can make nonparametric temporal modeling scalable.
