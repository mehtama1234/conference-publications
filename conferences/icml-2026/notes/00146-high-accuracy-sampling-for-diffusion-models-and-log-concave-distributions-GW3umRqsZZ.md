# High-Accuracy Sampling for Diffusion Models and Log-Concave Distributions

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: GW3umRqsZZ
- Authors: Fan Chen; Sinho Chewi; Constantinos Costis Daskalakis; Alexander Rakhlin
- Primary area: theory->learning_theory
- Keywords: diffusion models;sampling;log-concave sampling;query complexity
- Source URL: https://openreview.net/forum?id=GW3umRqsZZ
- PDF URL: https://openreview.net/pdf?id=GW3umRqsZZ

## Abstract

We present algorithms for diffusion model sampling which obtain $\delta$-error in $\mathrm{polylog}(1/\delta)$ steps, given access to $\widetilde O(\delta)$-accurate score estimates in $L^2$. This is an exponential improvement over all previous results. Specifically, under minimal data assumptions, the complexity is $\widetilde O(d\mathrm{polylog}(1/\delta))$ where $d$ is the dimension of the data; under a non-uniform $L$-Lipschitz condition, the complexity is $\widetilde O(\sqrt{dL}\mathrm{polylog}(1/\delta))$; and if the data distribution has intrinsic dimension $d_\star$, then the complexity reduces to $\widetilde O(d_\star\mathrm{polylog}(1/\delta))$. Our approach also yields the first $\mathrm{polylog}(1/\delta)$ complexity sampler for general log-concave distributions using only gradient evaluations.

## One-Sentence Claim

New diffusion and log-concave samplers achieve delta-error in polylog(1/delta) steps under suitable score or gradient access, exponentially improving prior high-accuracy rates.

## Problem

High-accuracy sampling for diffusion models and log-concave distributions can require many steps as target error shrinks, making rigorous small-error sampling expensive.

## Core Contribution

The paper gives algorithms with polylogarithmic dependence on inverse accuracy for diffusion model sampling and the first such sampler for general log-concave distributions using only gradient evaluations.

## Method

The algorithms assume access to approximately accurate score estimates in L2 for diffusion sampling and derive complexity bounds under minimal data assumptions, non-uniform Lipschitz conditions, and intrinsic-dimension structure.

## Experiments and Evidence

The abstract states theoretical complexity bounds: roughly O(d polylog(1/delta)), O(sqrt(dL) polylog(1/delta)) under non-uniform L-Lipschitz conditions, and O(d_star polylog(1/delta)) under intrinsic dimension d_star.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: score-accuracy assumptions, constants hidden by tilde notation, implementability, and empirical behavior.

## Deep Themes

- Sampling theory is pushing toward high-accuracy regimes with logarithmic error dependence.
- Intrinsic dimension can govern sampling complexity.
- Diffusion and log-concave sampling share algorithmic tools.

## Subthemes

- Diffusion sampling.
- Log-concave distributions.
- Query complexity.
- Score estimation.
- Intrinsic dimension.
- High-accuracy theory.

## Connections to Other Papers

Connects to Reinforced SMC, Rex, Control Consistency Losses, and scientific sampling papers through sampling as core ML infrastructure.

## Notes for Cross-Paper Synthesis

This paper sharpens the sampler-infrastructure theme with a theory result: the asymptotic accuracy dependence of sampling can change qualitatively.
