# Towards Understanding Adam Convergence on Highly Degenerate Polynomials

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: uYWVGk1Qt0
- Authors: Zhiwei Bai; Jiajie Zhao; Zhangchen Zhou; Zhi-Qin John Xu; Yaoyu Zhang
- Primary area: theory->optimization
- Keywords: Adam;convergence;degeneration;adaptive gradient methods
- Source URL: https://openreview.net/forum?id=uYWVGk1Qt0
- PDF URL: https://openreview.net/pdf?id=uYWVGk1Qt0

## Abstract

Adam is a widely used optimization algorithm in deep learning, yet the specific class of objective functions where it exhibits inherent advantages remains underexplored. Unlike prior studies requiring external schedulers and $\beta_2$ near 1 for convergence, this work investigates the ``natural'' auto-convergence properties of Adam. We identify a class of highly degenerate polynomials where Adam converges automatically without additional schedulers. Specifically, we derive theoretical conditions for local asymptotic stability on degenerate polynomials and demonstrate strong alignment between theoretical bounds and experimental results. We prove that Adam achieves local linear convergence on these degenerate functions, significantly outperforming the sub-linear convergence of Gradient Descent and Momentum. This acceleration stems from a decoupling mechanism between the second moment $v_t$ and squared gradient $g_t^2$, which exponentially amplifies the effective learning rate. Finally, we characterize Adam's hyperparameter phase diagram, identifying three distinct behavioral regimes: stable convergence, spikes, and SignGD-like oscillation.

## One-Sentence Claim

Adam has a natural auto-convergence advantage on highly degenerate polynomials, achieving local linear convergence through second-moment/gradient decoupling that amplifies the effective learning rate.

## Problem

Adam is widely used, but the objective classes where its adaptive mechanism gives inherent advantages remain poorly characterized. Much convergence theory depends on external schedulers or beta2 choices near one, which does not explain Adam's natural behavior.

The paper focuses on highly degenerate polynomial objectives, where gradient descent and momentum can be slow and where adaptive normalization may change convergence qualitatively.

## Core Contribution

The paper identifies a class of highly degenerate polynomials where Adam converges automatically without additional schedulers. It derives theoretical conditions for local asymptotic stability and proves local linear convergence.

It explains the acceleration through a decoupling mechanism between the second moment v_t and squared gradient g_t^2, which exponentially amplifies effective learning rate. It also maps a hyperparameter phase diagram with stable convergence, spikes, and SignGD-like oscillation.

## Method

The analysis studies Adam dynamics near degenerate polynomial minima. By tracking how the adaptive second-moment accumulator evolves relative to squared gradients, the authors characterize regimes where Adam's normalized step grows effectively larger than GD's.

Local stability conditions define when this amplification yields convergence rather than spikes or oscillation. Experiments compare theoretical bounds with observed behavior.

## Experiments and Evidence

The abstract reports strong alignment between theoretical bounds and experiments, local linear convergence for Adam, and sublinear convergence for GD and momentum on the studied degenerate functions.

Full-paper reading should verify polynomial class definitions, hyperparameter assumptions, stability proofs, phase diagram parameters, and whether insights transfer to neural-network loss landscapes.

## Limits and Failure Modes

Highly degenerate polynomials are controlled objectives, not full deep-learning losses. The theory may explain a mechanism present in neural training without covering all interactions with stochastic gradients, weight decay, normalization, or scheduling.

The same amplification that accelerates convergence can lead to spikes or SignGD-like oscillation in other hyperparameter regimes, so the advantage is conditional.

## Deep Themes

- Adaptive optimization as geometry changer: Adam modifies effective learning rates in degenerate directions.
- Degeneracy as advantage regime: flat/high-order objectives can favor adaptive methods.
- Phase diagrams for optimizers: behavior should be mapped across hyperparameters, not summarized by one convergence theorem.
- Natural convergence without schedulers: some stability arises from Adam dynamics themselves.

## Subthemes

- v_t and g_t^2 decoupling drives acceleration.
- Local linear convergence contrasts with GD sublinear behavior.
- Spikes and SignGD-like oscillations mark failure regimes.
- Controlled polynomials isolate optimizer mechanisms.

## Connections to Other Papers

This paper connects to non-Euclidean edge-of-stability, NorMuon, and scaling-law origin work through optimization dynamics. It also relates to theory papers using simplified worlds to explain empirical deep-learning behavior.

It complements EoS diagnostics: both show optimizer behavior depends on dynamics and geometry that classical smoothness stories miss.

## Notes for Cross-Paper Synthesis

The synthesis point is that optimizer advantage is objective-class-specific. ICML theory papers are increasingly asking when popular training recipes are actually well matched to the local geometry.
