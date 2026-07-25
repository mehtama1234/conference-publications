# Scaling Laws and Spectra of Shallow Neural Networks in the Feature Learning Regime

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: Q3yLIIkt7z
- Authors: Leonardo Defilippis; Yizhou Xu; Julius Girardin; Vittorio Erba; Emanuele Troiani; Lenka Zdeborová; Bruno Loureiro; Florent Krzakala
- Primary area: learning theory
- Keywords: Scaling laws; Neural networks; LASSO and matrix compressed sensing; Random matrix theory; Approximate message passing; High dimensional Statistics
- Source URL: https://openreview.net/forum?id=Q3yLIIkt7z
- PDF URL: https://openreview.net/pdf?id=Q3yLIIkt7z

## Abstract

Neural scaling laws underlie many of the recent advances in deep learning, yet their theoretical understanding remains largely confined to linear models. In this work, we present a systematic analysis of scaling laws for quadratic and diagonal neural networks in the feature learning regime. Leveraging connections with matrix compressed sensing and LASSO, we derive a detailed phase diagram for the scaling exponents of the excess risk as a function of sample complexity and weight decay. This analysis uncovers crossovers between distinct scaling regimes and plateau behaviors, mirroring phenomena widely reported in the empirical neural scaling literature. Furthermore, we establish a precise link between these regimes and the spectral properties of the trained network weights, which we characterize in detail. As a consequence, we provide a theoretical validation of recent empirical observations connecting the emergence of power-law tails in the weight spectrum with network generalization performance, yielding an interpretation from first principles.

## One-Sentence Claim

This paper derives feature-learning scaling laws for quadratic and diagonal neural networks and links excess-risk regimes to trained weight spectra.

## Problem

Empirical neural scaling laws are central to modern deep learning, but theoretical understanding is much stronger for linear models than for nonlinear feature-learning networks.

The field also observes spectral phenomena such as power-law tails in trained weights, but lacks first-principles explanations connecting those spectra to generalization scaling.

## Core Contribution

The paper analyzes scaling laws for quadratic and diagonal neural networks in the feature-learning regime.

It derives a phase diagram for excess-risk scaling exponents as functions of sample complexity and weight decay, identifies crossovers and plateaus, and connects these regimes to trained-weight spectral properties.

## Method

The analysis leverages connections to matrix compressed sensing, LASSO, random matrix theory, approximate message passing, and high-dimensional statistics.

These tools allow the authors to characterize how sample complexity and regularization shape learning regimes and spectra.

## Experiments and Evidence

The abstract emphasizes theoretical derivation rather than empirical benchmarking.

The results mirror empirical scaling-law phenomena, including crossovers between regimes and plateau behavior, and validate observed links between power-law spectral tails and generalization.

## Limits and Failure Modes

Quadratic and diagonal networks are still simplified relative to deep transformers. The relevance of derived exponents to large-scale models depends on whether the same mechanisms persist in deeper architectures and real data.

Because this note is abstract-only, details still need checking: model assumptions, exact phase diagram, AMP equations, risk definitions, spectral metrics, and any empirical validation.

## Deep Themes

- Scaling laws from feature learning: nonlinear models can be theoretically analyzed beyond linear-regime approximations.
- Spectra as generalization signatures: trained-weight eigenvalue distributions encode learning regimes.
- Regularization-controlled phase transitions: weight decay and sample complexity determine excess-risk scaling.
- Theory explaining empirical scaling: observed plateaus and power laws get a first-principles account.

## Subthemes

- Quadratic and diagonal networks.
- Matrix compressed sensing.
- Approximate message passing.
- Power-law weight spectra.

## Connections to Other Papers

This connects to Scaling Laws Origin, Train-before-Test, Muon/Beyond Muon, and DFM Bounds through attempts to explain empirical practice theoretically.

It also relates to optimizer and spectral-method papers because weight geometry becomes a measurable proxy for learning behavior.

## Notes for Cross-Paper Synthesis

This paper strengthens the theory-unifies-practice theme: empirical scaling and spectral heuristics are being connected to analyzable feature-learning regimes.
