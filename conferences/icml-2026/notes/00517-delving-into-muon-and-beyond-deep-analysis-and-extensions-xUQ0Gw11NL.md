# Delving into Muon and Beyond: Deep Analysis and Extensions

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: xUQ0Gw11NL
- Authors: Xianbiao Qi; Marco Chen; Jiaquan Ye; Yelin He; Rong Xiao
- Primary area: theory->deep_learning
- Keywords: Muon; Optimizer;Adam
- Source URL: https://openreview.net/forum?id=xUQ0Gw11NL
- PDF URL: https://openreview.net/pdf?id=xUQ0Gw11NL

## Abstract

The Muon optimizer has recently attracted considerable attention for its strong empirical performance and use of orthogonalized updates on matrix-shaped parameters, yet its underlying mechanisms and relationship to adaptive optimizers such as Adam remain insufficiently understood.
In this work, we aim to address these questions through a unified spectral perspective. Specifically, we view Muon as the \( p = 0 \) endpoint of a family of spectral transformations of the form \( \boldsymbol{U} \boldsymbol{\Sigma}^{p} \boldsymbol{V}^{\top} \), and consider additional variants with \( p = \frac{1}{2} \), \( p = \frac{1}{4} \), and \( p = 1 \). These transformations are applied to both first-moment updates, as in momentum SGD, and to root-mean-square (RMS) normalized gradient updates as in Adam. To enable efficient computation, we develop a coupled Newton iteration that avoids explicit singular value decomposition. Across controlled experiments, we find that RMS-normalized updates yield more stable optimization than first-moment updates. Moreover, while spectral compression provides strong stabilization benefits under first-moment updates, the Muon update (\( p = 0 \)) does not consistently outperform Adam. These results suggest that Muon is best understood as an effective form of spectral normalization, but not a universally superior optimization method. Our code is available at \url{https://github.com/Ocram7/BeyondMuon}.

## One-Sentence Claim

Muon is best understood as a spectral normalization endpoint for matrix updates, not as a universally superior optimizer to Adam.

## Problem

Muon has gained attention because orthogonalized matrix-shaped updates perform well empirically, but the mechanism behind those gains and their relationship to Adam-like adaptive updates remain unclear.

The problem is to separate what Muon contributes spectrally from what RMS normalization and other optimizer components already provide.

## Core Contribution

The paper gives a unified spectral perspective: Muon is the p = 0 endpoint of update transformations of the form U Sigma^p V^T, with variants at p = 1/2, p = 1/4, and p = 1.

It applies these transformations to both first-moment updates and RMS-normalized gradient updates, and develops a coupled Newton iteration to avoid explicit SVD.

## Method

The method analyzes optimizer updates through singular-value transformations. Spectral compression changes how update energy is distributed across matrix directions.

A coupled Newton iteration approximates the needed spectral transforms efficiently. Controlled experiments compare first-moment and RMS-normalized variants across p values.

## Experiments and Evidence

The abstract reports that RMS-normalized updates are more stable than first-moment updates. Spectral compression gives strong stabilization benefits for first-moment updates, but Muon p = 0 does not consistently outperform Adam.

This supports the interpretation that Muon is an effective spectral normalization method rather than a universal replacement for adaptive optimizers.

## Limits and Failure Modes

The conclusions may depend on model classes, parameter shapes, training scale, and hyperparameter tuning. Spectral transformations for matrix parameters may not transfer cleanly to all tensor layouts.

Because this note is abstract-only, details still need checking: benchmark tasks, optimizer hyperparameters, coupled Newton convergence, overhead, stability metrics, and behavior at large language-model scale.

## Deep Themes

- Optimizers as update geometry: spectral transformations reshape learning directions.
- Normalization versus adaptivity: Muon-like gains may come from stabilizing update spectra rather than replacing Adam.
- Endpoint analysis: placing a method in a parameterized family reveals when it helps.
- Efficient spectral computation: practical optimizer research depends on avoiding expensive decompositions.

## Subthemes

- U Sigma^p V^T update families.
- Orthogonalized matrix updates.
- RMS-normalized spectral variants.
- Coupled Newton iteration.

## Connections to Other Papers

This connects to Adam degeneracy, SlaClip, and optimization phase-diagram work through efforts to explain optimizer behavior beyond empirical recipes.

It also relates to spectral informed neural networks and alignment-sensitive spectral algorithms because singular geometry is used as the explanatory axis.

## Notes for Cross-Paper Synthesis

This paper contributes to a recurring theory-practice pattern: popular training tricks become more useful when mapped into a broader family that reveals their actual mechanism.
