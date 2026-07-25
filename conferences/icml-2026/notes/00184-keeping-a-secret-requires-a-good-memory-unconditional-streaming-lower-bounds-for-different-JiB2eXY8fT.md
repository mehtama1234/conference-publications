# Keeping a Secret Requires a Good Memory: Unconditional Streaming Lower-Bounds for Differentially Private Algorithms

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: JiB2eXY8fT
- Authors: Alessandro Epasto; Xin Lyu; Pasin Manurangsi
- Primary area: social_aspects->privacy
- Keywords: Lower bounds;Differential privacy;Space complexity;Communication Complexity;Streaming Algorithms
- Source URL: https://openreview.net/forum?id=JiB2eXY8fT
- PDF URL: https://openreview.net/pdf?id=JiB2eXY8fT

## Abstract

We study the computational cost of differential privacy in terms of memory efficiency. Specifically, we establish for the first time an unconditional space lower bound for user-level differential privacy by introducing a novel proof technique based on a multi-player communication game. We apply our framework, as an example, to the fundamental problem of estimating the number of distinct elements in a stream: we prove that any private algorithm requires almost $\widetilde{\Omega}(T^{1/3})$ space (where $T$ denotes the length of the stream) to achieve certain error rates in a promise variant of the problem, resolving an open problem in the literature (by Jain et al. 2023 and Cummings et al. 2025) and establishes the first exponential separation between the space complexity of private algorithms and their non-private $\widetilde{O}(1)$ counterparts for a natural statistical estimation task. Furthermore, we show that this communication-theoretic technique generalizes to broad classes of problems, yielding lower bounds for private medians, quantiles, and max-select.

## One-Sentence Claim

The paper proves unconditional space lower bounds for user-level differentially private streaming algorithms, showing privacy can require substantially more memory than non-private estimation.

## Problem

The memory cost of differential privacy in streaming algorithms was not well understood, especially for unconditional lower bounds separating private and non-private space complexity.

## Core Contribution

The paper introduces a multi-player communication-game technique and uses it to prove nearly Omega-tilde(T^(1/3)) space lower bounds for private distinct-elements estimation, plus broader bounds for medians, quantiles, and max-select.

## Method

The proof reduces private streaming estimation to a novel multi-player communication game, deriving unconditional memory lower bounds for user-level DP algorithms under specified promise/error conditions.

## Experiments and Evidence

The abstract is theoretical. It claims resolution of open problems from Jain et al. 2023 and Cummings et al. 2025 and an exponential separation from non-private Omega-tilde(1)-space counterparts for a natural statistical estimation task.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: exact privacy model, promise variant, error regime, constants/log factors, whether lower bounds match algorithms, and applicability beyond the listed streaming problems.

## Deep Themes

- Privacy can impose unavoidable resource costs.
- Memory lower bounds expose limits of streaming private analytics.
- Communication complexity remains a powerful tool for ML privacy theory.

## Subthemes

- Differential privacy.
- Streaming algorithms.
- Space complexity.
- Distinct elements.
- Communication complexity.
- User-level privacy.

## Connections to Other Papers

Connects to IHM and privacy-utility papers by showing the other side of the tradeoff: some private computation costs are fundamental rather than algorithmic inefficiencies.

## Notes for Cross-Paper Synthesis

This paper adds a hard-limit privacy theme: efficiency claims in private learning need to be interpreted against lower bounds that show when resource overhead is unavoidable.
