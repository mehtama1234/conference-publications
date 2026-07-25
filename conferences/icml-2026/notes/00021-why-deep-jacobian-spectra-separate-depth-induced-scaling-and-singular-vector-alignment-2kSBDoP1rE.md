# Why Deep Jacobian Spectra Separate: Depth-Induced Scaling and Singular-Vector Alignment

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 2kSBDoP1rE
- Authors: Nathanaël Haas; François Gatine; Augustin M Cosse; Zied Bouraoui
- Primary area: deep_learning->theory
- Keywords: Implicit bias;Jacobian spectrum;Random matrix products;Lyapunov exponents
- Source URL: https://openreview.net/forum?id=2kSBDoP1rE
- PDF URL: https://openreview.net/pdf?id=2kSBDoP1rE

## Abstract

Understanding why gradient-based training in deep networks exhibits strong implicit bias remains challenging, in part because tractable singular-value dynamics are typically available only for balanced deep linear models. We propose an alternative route based on two theoretically grounded and empirically testable signatures of deep Jacobians: depth-induced exponential scaling of ordered singular values and strong spectral separation. Adopting a fixed-gates view of piecewise-linear networks, where Jacobians reduce to products of masked linear maps within a single activation region, we prove the existence of Lyapunov exponents governing the top singular values at initialization, give closed-form expressions in a tractable masked model, and quantify finite-depth corrections. We further show that sufficiently strong separation forces singular-vector alignment in matrix products, yielding an approximately shared singular basis for intermediate Jacobians. Together, these results motivate an approximation regime in which singular-value dynamics become effectively decoupled, mirroring classical balanced deep-linear analyses without requiring balancing. Experiments in fixed-gates settings validate the predicted scaling, alignment, and resulting dynamics, supporting a mechanistic account of emergent low-rank Jacobian structure as a driver of implicit bias.

## One-Sentence Claim

Deep Jacobian spectra separate because depth induces exponential singular-value scaling and that spectral separation drives singular-vector alignment, making singular dynamics approximately decoupled.

## Problem

Implicit bias in deep networks is difficult to explain beyond balanced deep linear settings, where singular-value dynamics are tractable. For nonlinear piecewise-linear networks, the question is why low-rank Jacobian structure and ordered spectral separation emerge during training.

## Core Contribution

The paper gives a fixed-gates account of deep Jacobians as products of masked linear maps, proves Lyapunov-exponent scaling for top singular values, and shows that sufficiently strong spectral separation forces singular-vector alignment across matrix products.

## Method

It analyzes Jacobians inside a fixed activation region, where the network reduces to a product of gated/masked linear maps. Random-matrix product theory supplies Lyapunov exponents and finite-depth corrections; alignment results then motivate a decoupled approximation for singular-value dynamics.

## Experiments and Evidence

Experiments in fixed-gates and masked-network settings validate predicted depth-induced scaling, singular-vector alignment, and the resulting structured evolution of Jacobian singular values.

## Full-Text Upgrade

The full text makes the proposed mechanism explicit: depth first creates separation among ordered singular values; strong separation then promotes alignment of dominant singular vectors across partial products; once those directions stabilize, singular-value dynamics resemble the decoupled equations of balanced deep-linear networks without requiring an explicit balancing assumption.

The theoretical chain is deliberately modular. The paper proves Lyapunov exponents for masked products at random initialization, including closed-form expressions in a tractable masked model and finite-depth corrections. It separately proves that spectral separation can force singular-vector alignment. The authors note these theorems are not simply chained as a single proof of all training dynamics, but together they define an approximation regime for fixed-gates Jacobian analysis.

## Limits and Failure Modes

The fixed-gates assumption controls the analysis but leaves open how well the mechanism persists when activation patterns change substantially during training. The experiments validate controlled Jacobian settings rather than proving a full account for arbitrary nonlinear network training.

## Deep Themes

- Implicit bias can emerge from depth-induced spectral geometry.
- Low-rank behavior may be a structural consequence of Jacobian products.
- Theory is moving from idealized balanced linear models toward locally nonlinear but analyzable regimes.

## Subthemes

- Jacobian spectra.
- Random matrix products.
- Lyapunov exponents.
- Singular-vector alignment.
- Fixed-gates networks.
- Low-rank implicit bias.

## Connections to Other Papers

Connects to DiReCT through Hessian/Jacobian spectral geometry as a guide to optimization behavior. It also links to theory papers that explain training dynamics through tractable structural approximations rather than purely empirical scaling.

## Notes for Cross-Paper Synthesis

This paper strengthens the theory-and-optimization theme: modern deep-learning theory is trying to identify intermediate regimes where nonlinear networks have enough structure to recover useful linear-model-style dynamics.
