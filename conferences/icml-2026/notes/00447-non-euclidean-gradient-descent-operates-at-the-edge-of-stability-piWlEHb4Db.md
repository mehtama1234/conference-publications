# Non-Euclidean Gradient Descent Operates at the Edge of Stability

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: piWlEHb4Db
- Authors: Rustem Islamov; Michael Crawshaw; Jeremy Cohen; Robert M. Gower
- Primary area: optimization
- Keywords: edge of stability;optimization;deep learning
- Source URL: https://openreview.net/forum?id=piWlEHb4Db
- PDF URL: https://openreview.net/pdf?id=piWlEHb4Db

## Abstract

The Edge of Stability (EoS) is a phenomenon where the sharpness (largest eigenvalue) of the Hessian approaches and then hovers near the stability threshold $2/\eta$ during gradient descent (GD) with step size $\eta$. Despite (apparently) violating classical smoothness assumptions, EoS has been widely observed in deep learning, but its theoretical foundations remain incomplete. We provide an interpretation of EoS through the lens of Directional Smoothness [Mishkin et al., 2024]. This interpretation naturally extends to non-Euclidean norms, which we use to define generalized sharpness under an arbitrary norm.  Our generalized sharpness measure includes previously studied vanilla GD and preconditioned GD as special cases, as well as methods for which EoS has not been studied, such as  $\ell_{\infty}$-descent, Block CD, Spectral GD, and their normalized versions. Through experiments on neural networks, we show that non-Euclidean GD with our generalized sharpness also exhibits progressive sharpening followed by oscillations around or above the threshold $2/\eta$. Practically, our framework provides a geometry-aware spectral diagnostic that can be applied across a broad class of non-Euclidean gradient methods.

## One-Sentence Claim

Edge-of-stability behavior extends beyond Euclidean gradient descent: non-Euclidean gradient methods exhibit geometry-specific sharpness growth and oscillation near the same 2/eta stability threshold.

## Problem

Deep networks trained with gradient descent often operate at the edge of stability, where Hessian sharpness approaches and hovers near the classical stability threshold. This seems to violate smoothness-based optimization intuitions, and existing explanations are incomplete.

Most EoS analysis is tied to Euclidean GD or specific preconditioned variants. The open question is whether EoS is a broader property of gradient-like methods under different geometries.

## Core Contribution

The paper interprets EoS through directional smoothness and extends the idea to arbitrary non-Euclidean norms. This yields a generalized sharpness measure that covers vanilla GD, preconditioned GD, l_infinity descent, block coordinate descent, spectral GD, and normalized variants.

The contribution is a geometry-aware diagnostic for optimization dynamics: sharpness should be measured relative to the update geometry, not only through the Euclidean Hessian spectrum.

## Method

The framework defines generalized sharpness under arbitrary norms using directional smoothness. The stability threshold remains expressed as 2/eta, but the relevant curvature quantity changes with the geometry of the descent method.

The authors then examine non-Euclidean GD variants experimentally on neural networks, tracking whether generalized sharpness progressively increases and oscillates around or above the threshold.

## Experiments and Evidence

The abstract reports neural-network experiments showing progressive sharpening followed by oscillations around or above 2/eta across non-Euclidean methods. The included methods span l_infinity descent, block coordinate descent, spectral GD, preconditioned GD, and normalized versions.

Full-paper reading should inspect architectures, datasets, step-size regimes, exact generalized sharpness computation, and whether the diagnostic predicts optimization outcomes rather than only describing them.

## Limits and Failure Modes

The framework is diagnostic rather than necessarily prescriptive: observing edge-of-stability behavior may not immediately tell practitioners how to choose step sizes or norms. Generalized sharpness estimation may also be expensive or approximate in large models.

EoS behavior can depend on architecture, normalization, batch size, optimizer details, and loss landscape. Extending the theory to adaptive optimizers and modern LLM training remains a further step.

## Deep Themes

- Optimization geometry matters: stability should be measured in the norm used by the update rule.
- EoS as a broad training phenomenon: sharpness-threshold dynamics are not limited to vanilla GD.
- Directional smoothness as explanatory bridge: local curvature along update directions explains apparent smoothness violations.
- Diagnostics over folklore: the paper turns an observed phenomenon into a geometry-aware measurement tool.

## Subthemes

- Non-Euclidean norms induce different sharpness notions.
- Normalized methods can also operate near stability boundaries.
- Progressive sharpening appears robust across update geometries.
- Spectral diagnostics need to match the optimizer, not just the model.

## Connections to Other Papers

This paper connects to NorMuon, scaling-law origin work, and stochastic Transformer theory through the study of training dynamics and parameterization. It also relates to FTRL lower-bound and CV instability papers as another example of theory explaining when intuitive optimization claims fail.

Its geometry-aware diagnostic complements efficiency work: optimizers are not only faster or slower; they define the curvature regime in which models train.

## Notes for Cross-Paper Synthesis

The synthesis theme is that optimization phenomena are geometry-dependent. Several ICML papers are moving from scalar metrics toward diagnostics matched to the actual algorithmic process.
