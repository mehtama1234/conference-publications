# A Unifying View of Variational Generative Wasserstein Flows

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: sJ7ngz2eQx
- Authors: Paul Caucheteux; Clément Bonet; Anna Korba
- Primary area: deep_learning->generative_models_and_autoencoders
- Keywords: Wasserstein gradient flows;Jordan–Kinderlehrer–Otto (JKO) scheme;generative adversarial networks
- Source URL: https://openreview.net/forum?id=sJ7ngz2eQx
- PDF URL: https://openreview.net/pdf?id=sJ7ngz2eQx

## Abstract

Many modern generative models can be viewed as minimizing divergences between probability distributions, yet they rely on different algorithmic and geometric principles. Wasserstein gradient flows provide a continuous-time formulation for optimizing over distributions, and can be approximated through their implicit discretization via the Jordan–Kinderlehrer–Otto (JKO) scheme. In this work, we present a unified theoretical framework for generative modeling based on Wasserstein gradient flows, which we refer to as Generative Wasserstein Flows (GWF). We show that a broad class of existing methods can be derived as instances of parametric JKO schemes for $f$-divergence objectives, and we establish equivalences between several recently proposed algorithms. We extend this framework beyond $f$-divergences to Integral Probability Metrics and squared Maximum Mean Discrepancy, deriving new JKO-based generative algorithms, and clarifying their connections with GANs. We study empirically the impact of the JKO regularization for a wide set of objectives. Finally, we analyze parametric Wasserstein flows, where the dynamics are restricted to distributions induced by parametrized maps.

## One-Sentence Claim

Generative Wasserstein Flows unify broad classes of generative models as parametric JKO schemes over distribution divergences, extending from f-divergences to IPMs and MMD.

## Problem

Modern generative models often optimize divergences between probability distributions, but they use different algorithmic and geometric principles. This makes it hard to compare methods or see when apparently different algorithms are equivalent.

Wasserstein gradient flows provide a continuous-time view of optimization over distributions, and the JKO scheme gives an implicit discretization. The paper asks whether this structure can unify existing and new generative algorithms.

## Core Contribution

The paper introduces Generative Wasserstein Flows, a theoretical framework for generative modeling based on Wasserstein gradient flows. It shows that many existing methods arise as parametric JKO schemes for f-divergence objectives and establishes equivalences among recent algorithms.

It extends the framework beyond f-divergences to Integral Probability Metrics and squared Maximum Mean Discrepancy, deriving new JKO-based generative algorithms and clarifying their connections to GANs.

## Method

The framework starts from distributional gradient flows in Wasserstein space and applies parametric JKO discretization, restricting dynamics to distributions induced by parameterized maps.

By choosing different divergence objectives, the same variational flow perspective recovers or generates different generative-model algorithms. The authors also study the role of JKO regularization empirically across objectives.

## Experiments and Evidence

The abstract reports theoretical derivations, equivalence results, new algorithms for IPM and MMD objectives, and empirical study of JKO regularization over a wide set of objectives.

Full-paper reading should verify which existing algorithms are recovered, assumptions behind parametric maps, empirical datasets, and how JKO regularization affects sample quality or training stability.

## Limits and Failure Modes

A unifying framework can clarify relationships without making all instances equally practical. Parametric restrictions may break properties of ideal Wasserstein flows, and JKO steps may be computationally difficult depending on objective and architecture.

Connections to GANs and MMD methods need careful interpretation because adversarial optimization, finite samples, and neural parameterization introduce approximation gaps.

## Deep Themes

- Generative modeling as distributional dynamics: training is a flow over probability measures.
- JKO schemes as algorithm templates: implicit variational steps unify disparate methods.
- Geometry of divergences: f-divergences, IPMs, and MMD fit into a shared transport view.
- Theory unifies engineering practice: algorithm equivalences expose hidden common structure.

## Subthemes

- Parametric Wasserstein flows restrict ideal distribution dynamics to neural maps.
- JKO regularization can affect stability and sample quality.
- GAN connections emerge through IPM-based flow formulations.
- Objective choice determines the geometry of generative training.

## Connections to Other Papers

This paper connects to XDLM and any-order GPT diffusion through generative-model alternatives and theoretical unification. It also connects to attention mean-field work because both use Wasserstein/gradient-flow ideas to analyze neural systems.

It fits the broader corpus theme of recasting fragmented methods as special cases of a common formalism, similar to ambiguity-averse MDPs and CoEvol-NO.

## Notes for Cross-Paper Synthesis

The synthesis point is that generative modeling is being reorganized around flow and geometry. Rather than treating GANs, diffusion, and variational methods as isolated families, papers are mapping their shared distributional dynamics.
