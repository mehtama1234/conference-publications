# A Call to Lagrangian Action: Learning Population Mechanics from Temporal Snapshots

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: MjPv4kRu3H
- Authors: Vincent Guan; Lazar Atanackovic; Kirill Neklyudov
- Primary area: applications->chemistry_physics_and_earth_sciences
- Keywords: Population dynamics;trajectory inference;single-cell;gradient flows;flow matching
- Source URL: https://openreview.net/forum?id=MjPv4kRu3H
- PDF URL: https://openreview.net/pdf?id=MjPv4kRu3H

## Abstract

The population dynamics of molecules, cells, and organisms are governed by a number of unknown internal and external forces. In the last decade, population dynamics have predominately been modeled with Wasserstein gradient flows. However, since gradient flows minimize free energy, they fail to capture important dynamical properties, such as periodicity. In this work, we propose a change in perspective by considering population dynamics that minimize Wasserstein Lagrangian action, rather than free energy. As our main theoretical contributions, we derive the Hamiltonian equations of motion from the principle of least population-level action and we show that these mechanics encompass classical mechanics, quantum mechanics, and gradient flows. We further leverage the Hamiltonian perspective to propose an algorithm that learns the population mechanics from observed marginals, without specifying the Lagrangian. We demonstrate that by directly learning the population mechanics, our method forecasts and interpolates unseen marginals without a reference process, and outperforms gradient flow and flow matching methods across a wide range of real and simulated experiments.

## One-Sentence Claim

The paper models population dynamics by minimizing Wasserstein Lagrangian action instead of free energy, enabling learned mechanics that capture periodic and Hamiltonian behavior from temporal snapshots.

## Problem

Population dynamics for molecules, cells, and organisms are often modeled as Wasserstein gradient flows, but free-energy minimization cannot capture important dynamics such as periodicity.

## Core Contribution

The paper derives population-level Hamiltonian equations from least Lagrangian action, shows this framework encompasses classical mechanics, quantum mechanics, and gradient flows, and proposes an algorithm for learning mechanics from observed marginals without specifying the Lagrangian.

## Method

The method shifts from free-energy minimization to population-level action minimization, uses the Hamiltonian perspective to infer forces/mechanics from temporal marginal snapshots, and forecasts/interpolates unseen marginals without a reference process.

## Experiments and Evidence

The abstract reports improved forecasting and interpolation over gradient-flow and flow-matching methods across a wide range of real and simulated experiments.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: assumptions behind Lagrangian recovery, datasets, marginal observation noise, periodic-system benchmarks, identifiability, and computational cost versus flow matching.

## Deep Themes

- Scientific dynamics may need action principles rather than dissipative gradient-flow assumptions.
- Population-level mechanics can unify physical and biological temporal modeling.
- Learning from marginals requires structural principles to recover unseen trajectories.

## Subthemes

- Population dynamics.
- Wasserstein Lagrangian action.
- Hamiltonian mechanics.
- Single-cell trajectory inference.
- Flow matching.
- Temporal snapshots.

## Connections to Other Papers

Connects to CoCLD, SDEVI, GFG, and Modified SINNs through scientific temporal dynamics and explicit physical/mathematical priors.

## Notes for Cross-Paper Synthesis

This paper strengthens the AI-for-science theme: the right governing principle, such as action minimization, can matter more than using a generic learned flow.
