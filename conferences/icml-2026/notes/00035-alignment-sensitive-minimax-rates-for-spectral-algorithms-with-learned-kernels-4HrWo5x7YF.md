# Alignment-Sensitive Minimax Rates for Spectral Algorithms with Learned Kernels

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 4HrWo5x7YF
- Authors: Dongming Huang; Zhifan Li; Yicheng Li; Qian Lin
- Primary area: theory->learning_theory
- Keywords: kernel regression;spectral algorithms;feature learning theory;minimax theory;over parameterized gradient flow
- Source URL: https://openreview.net/forum?id=4HrWo5x7YF
- PDF URL: https://openreview.net/pdf?id=4HrWo5x7YF

## Abstract

We study spectral algorithms in settings where kernels may arise from a learning procedure, and ask how the resulting spectral order affects risk. We introduce the effective span dimension (ESD), an alignment-sensitive complexity measure that depends jointly on the target signal, the spectral order induced by the kernel, and the noise level $\sigma^2$. The ESD is defined without requiring eigen-decay conditions or source conditions, and it captures how much of the target signal lies in the leading spectral span. We prove that, for sequence models whose ESD is at most $K$, the minimax excess risk scales as $\sigma^2 K$, and we extend the framework to linear models and RKHS regression. Furthermore, we analyze over-parameterized gradient flow in a fixed-eigenbasis spectral learning model and prove that it can reduce the ESD under certain conditions. Together with numerical experiments, these results connect adaptive feature learning with reductions in ESD and offer a novel perspective on generalization beyond traditional fixed-kernel theories.

## One-Sentence Claim

Effective span dimension explains how learned-kernel spectral alignment controls minimax risk, with excess risk scaling like noise variance times the aligned span size.

## Problem

Classical fixed-kernel theory relies on eigen-decay and source conditions, but learned kernels adapt their spectra during training, making traditional complexity measures poorly suited to explain generalization gains.

## Core Contribution

The paper introduces effective span dimension, an alignment-sensitive complexity measure depending on target signal, kernel-induced spectral order, and noise level, then proves minimax rates and analyzes when gradient flow can reduce ESD.

## Method

It develops sequence-model minimax theory for ESD-bounded signal classes, extends the framework to linear models and RKHS regression, and studies over-parameterized gradient flow in a fixed-eigenbasis spectral learning model.

## Experiments and Evidence

The abstract reports minimax excess risk scaling as sigma-squared times ESD, plus numerical experiments connecting adaptive feature learning to reductions in ESD.

## Full-Text Upgrade

The full text defines ESD as the number of leading spectral coordinates needed so that the remaining target tail is below a noise-calibrated threshold. This makes ESD sensitive to both the target's coefficient allocation and the kernel's spectral ordering, unlike complexity measures that only inspect eigenvalue decay.

The key theoretical message is that minimax risk over an ESD-bounded class scales linearly with the ESD quota and noise variance. The learned-kernel angle comes from showing that adaptive training can reshape spectral order or eigenvalues so the target lies in a smaller effective span. For evolving eigenfunctions, the framework remains meaningful through a time-dependent/pathwise eigensystem.

## Limits and Failure Modes

Limits to watch: the strongest adaptive-learning result is in a fixed-eigenbasis eigenvalue-learning model; extending sharp dynamics to learned eigenfunctions and full neural networks remains harder; and ESD is a population quantity that may require estimation in practice.

## Deep Themes

- Generalization depends on target-kernel alignment, not only kernel complexity.
- Feature learning can be understood as reducing the effective dimension of the target.
- Minimax theory is adapting to learned representations rather than assuming fixed features.

## Subthemes

- Effective span dimension.
- Learned kernels.
- Spectral algorithms.
- Minimax rates.
- Over-parameterized gradient flow.
- Signal-kernel alignment.

## Connections to Other Papers

Connects to Single-Head Attention in High Dimensions and Jacobian spectra through spectral explanations of generalization. It also links to DiReCT because both use eigenspace structure to reason about learning dynamics.

## Notes for Cross-Paper Synthesis

This paper adds a formal version of the alignment theme: representation learning helps when it reorders or reshapes spectra so the target occupies a smaller, noise-relevant span.
