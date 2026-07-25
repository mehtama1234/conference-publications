# Asymptotic Optimality of the High-Dimensional Gaussian Mechanism and Improved Low-Dimensional Mechanisms for Differential Privacy

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 82Wosp2Iu1
- Authors: Yu Wei; Alexander Bienstock; Antigoni Polychroniadou
- Primary area: social_aspects->privacy
- Keywords: Differential Privacy;Gaussian Mechanism;Spherical Generalized Gamma Mechanism
- Source URL: https://openreview.net/forum?id=82Wosp2Iu1
- PDF URL: https://openreview.net/pdf?id=82Wosp2Iu1

## Abstract

The additive noise mechanism is a foundational tool for differential privacy (DP) of $T$-dimensional real-valued vector queries. The Gaussian mechanism, utilizing Gaussian noise, is the mostly widely used such mechanism, due to its simplicity and strong privacy guarantees. In this work, we provide justification for this choice, showing that as the dimension $T\to\infty$, no additive-noise mechanism can asymptotically improve on the Gaussian mechanism's privacy--utility tradeoff for the strong privacy settings typically used. We also develop a new family of **Spherical Generalized Gamma** DP mechanisms, which contains both the Gaussian mechanism and the recently studied $\ell_2$ mechanism (Joseph \emph{et al.}, ICML 2025). We identify members of this family that outperform both the Gaussian and $\ell_2$ mechanisms in certain low-dimensional settings, and show tight composition of all mechanisms in this family, answering an open question of Joseph \emph{et al.}~regarding the $\ell_2$ mechanism.

## One-Sentence Claim

The Gaussian mechanism is asymptotically optimal for high-dimensional additive-noise differential privacy, while Spherical Generalized Gamma mechanisms can improve low-dimensional privacy-utility tradeoffs.

## Problem

Gaussian noise is widely used for vector-query DP, but its optimality is not obvious, and recent non-Gaussian mechanisms suggest it may be suboptimal in some regimes.

## Core Contribution

The paper proves that no additive-noise mechanism asymptotically beats Gaussian noise in strong high-dimensional privacy settings, introduces a Spherical Generalized Gamma family, and gives tight composition for that family.

## Method

It studies spherically symmetric additive mechanisms by decomposing noise into radial and directional components, reducing privacy analysis to a radial integration problem. It compares mechanisms under fixed mean-squared error and privacy level using the optimal delta/privacy profile.

## Experiments and Evidence

The abstract reports high-dimensional asymptotic optimality for Gaussian noise and identifies Spherical Generalized Gamma mechanisms that outperform both Gaussian and l2 mechanisms in certain low-dimensional settings.

## Full-Text Upgrade

The full text frames the main result as a high-privacy, high-dimensional limit: for vector queries in R^T as T grows, Gaussian noise attains the limiting worst-case optimal delta at the same MSE budget. The proof route uses spherical symmetry and concentrates attention on the radial distribution, showing that non-Gaussian additive mechanisms cannot improve the asymptotic privacy-utility tradeoff in the target regime.

The low-dimensional part is not an afterthought. The Spherical Generalized Gamma family contains Gaussian and l2-style mechanisms but also includes shapes whose radial distributions give better tradeoffs for some finite dimensions and privacy parameters. The paper also answers a composition question for this family through tight privacy-profile composition.

## Limits and Failure Modes

Limits to watch: the optimality claim is asymptotic and focused on strong privacy regimes; finite-dimensional and low-privacy regimes can still favor non-Gaussian mechanisms; and implementation requires choosing the SGG parameters for the actual dimension/privacy budget.

## Deep Themes

- Classical baselines can be both asymptotically justified and locally improvable.
- Privacy mechanisms have dimension-dependent regimes.
- Better DP utility may come from matching noise geometry to the operating scale.

## Subthemes

- Differential privacy.
- Gaussian mechanism.
- Additive noise.
- Spherical Generalized Gamma mechanisms.
- Privacy-profile composition.
- High-dimensional asymptotics.

## Connections to Other Papers

Connects to DP-SGD clipping and privacy papers through a shared focus on the real privacy-utility frontier. It also links to theory papers that distinguish asymptotic guarantees from finite-regime engineering choices.

## Notes for Cross-Paper Synthesis

This paper adds a regime-awareness theme: a dominant standard method may be optimal in one limit but not in the practical low-dimensional corner that a deployment actually occupies.
