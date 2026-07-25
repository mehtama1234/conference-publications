# FALCON: Few-step Accurate Likelihoods for Continuous Flows

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: FbssShlI4N
- Authors: Danyal Rehman; Tara Akhound-Sadegh; Artem Gazizov; Yoshua Bengio; Alexander Tong
- Primary area: applications to physical sciences (physics, chemistry, biology, etc.)
- Keywords: Generative Models;Flow Matching;Boltzmann Generators;AI for Science
- Source URL: https://openreview.net/forum?id=FbssShlI4N
- PDF URL: https://openreview.net/pdf?id=FbssShlI4N

## Abstract

Scalable sampling of molecular states in thermodynamic equilibrium is a long-standing challenge in statistical physics. Boltzmann Generators tackle this problem by pairing a generative model, capable of exact likelihood computation, with importance sampling to obtain consistent samples under the target distribution. Current Boltzmann Generators primarily use continuous normalizing flows (CNFs) trained with flow matching for efficient training of powerful models. However, likelihood calculation for these models is extremely costly, requiring thousands of function evaluations per sample, severely limiting their adoption. In this work, we propose Few-step Accurate Likelihoods for Continuous Flows (FALCON), a method which allows for few-step sampling with a likelihood accurate enough for importance sampling applications by introducing a hybrid training objective that encourages invertibility. We show FALCON outperforms state-of-the-art normalizing flow models for molecular Boltzmann sampling and is \emph{two orders of magnitude faster} than the equivalently performing CNF model.

## One-Sentence Claim

FALCON makes continuous-flow Boltzmann generators practical by producing few-step samples with likelihoods accurate enough for importance sampling.

## Problem

Boltzmann generators need exact or accurate likelihoods for importance sampling in thermodynamic equilibrium sampling. Continuous normalizing flows trained with flow matching can be powerful, but likelihood computation is extremely expensive.

Thousands of function evaluations per sample make CNF likelihoods a bottleneck for molecular Boltzmann sampling.

## Core Contribution

The paper proposes FALCON, Few-step Accurate Likelihoods for Continuous Flows.

It introduces a hybrid training objective that encourages invertibility, enabling few-step sampling while preserving likelihood accuracy sufficient for importance sampling.

## Method

FALCON modifies continuous-flow training with an invertibility-oriented hybrid objective. The goal is to retain the expressivity and training benefits of flow matching while allowing efficient likelihood computation.

The generated samples can then be used in importance sampling for target Boltzmann distributions.

## Experiments and Evidence

The abstract reports that FALCON outperforms state-of-the-art normalizing flow models for molecular Boltzmann sampling.

It is two orders of magnitude faster than an equivalently performing CNF model.

## Limits and Failure Modes

Likelihood accuracy must be sufficient for importance sampling; small errors could bias equilibrium estimates. The method may depend on molecular system complexity and invertibility tradeoffs.

Because this note is abstract-only, details still need checking: molecular benchmarks, likelihood-error metrics, objective terms, number of steps, effective sample size, and comparison against other fast flow methods.

## Deep Themes

- Generative models for statistical physics: sampling quality must be paired with likelihood correctness.
- Few-step flows with usable likelihoods: speed and importance weights must coexist.
- Invertibility as deployment constraint: scientific sampling requires more than visually plausible samples.
- Flow matching for equilibrium sampling: generative modeling becomes an inference engine for physical systems.

## Subthemes

- Boltzmann generators.
- Continuous normalizing flows.
- Importance sampling likelihoods.
- Molecular equilibrium sampling.

## Connections to Other Papers

This connects to RealUID, Diffusion Flow Matching theory, Reverse Flow Matching, and scientific generative modeling papers.

It also relates to quotient-space diffusion and molecular/protein generation work because physical distributions impose constraints beyond sample appearance.

## Notes for Cross-Paper Synthesis

FALCON adds a scientific-likelihood theme: in physics-facing generation, fast samples are not enough; likelihoods must remain accurate enough for downstream estimators.
