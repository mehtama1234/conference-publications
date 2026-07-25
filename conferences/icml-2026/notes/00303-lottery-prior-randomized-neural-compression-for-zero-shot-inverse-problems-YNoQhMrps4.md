# Lottery Prior: Randomized Neural Compression for Zero-Shot Inverse Problems

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: YNoQhMrps4
- Authors: Haotian Wu; Di You; Pier Luigi Dragotti; Deniz Gunduz
- Primary area: applications->computer_vision
- Keywords: Neural compression;Implicit codec;Zero-shot learning;Inverse problem
- Source URL: https://openreview.net/forum?id=YNoQhMrps4
- PDF URL: https://openreview.net/pdf?id=YNoQhMrps4

## Abstract

We study zero-shot inverse problems, where a clean signal is recovered from a single degraded observation without external training data. Contrary to the common belief that such problems require highly complex models, we show that a lightweight neural network, when combined with entropy and complexity regularization in a compression-based formulation, is sufficient for high-quality restoration. We propose Lottery Prior, a compression-based inverse solver that leverages architectural priors from random networks and induces a family of implicit priors through randomness, enabling ensemble-based refinement. We further derive non-asymptotic error bounds for compression-based maximum-likelihood inverse solvers, revealing how rate–distortion constraints act as implicit regularizers. Experiments on denoising, noisy super-resolution, and inpainting demonstrate that our method achieves state-of-the-art with significantly fewer effective parameters. Project page: https://eedavidwu.github.io/LotteryPrior/

## One-Sentence Claim

Lottery Prior solves zero-shot inverse problems with lightweight random-network compression priors, using entropy and complexity regularization rather than large external training sets.

## Problem

Zero-shot inverse problems recover a clean signal from one degraded observation without external training data. Common intuition suggests high-quality restoration requires complex learned priors or pretrained models, which may be unavailable or mismatched.

The paper asks whether lightweight random neural networks plus compression principles can provide enough prior structure for restoration.

## Core Contribution

The paper introduces Lottery Prior, a compression-based inverse solver that uses architectural priors from random networks and randomness-induced ensembles of implicit priors. It combines entropy and complexity regularization in a neural compression formulation.

The theory derives non-asymptotic error bounds for compression-based maximum-likelihood inverse solvers, showing how rate-distortion constraints serve as implicit regularizers.

## Method

Lottery Prior treats restoration as finding a compact neural representation of the signal consistent with the degraded observation. Random lightweight networks provide a family of implicit codec priors; ensemble refinement exploits variation across random draws.

Rate-distortion and entropy/complexity penalties prevent the solution from fitting degradation noise too freely.

## Experiments and Evidence

Evidence reported in the abstract:

- Non-asymptotic error bounds for compression-based maximum-likelihood inverse solvers.
- Experiments on denoising, noisy super-resolution, and inpainting.
- State-of-the-art restoration with significantly fewer effective parameters.
- Ensemble-based refinement from randomized priors.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: degradation models, network architectures, runtime, ensemble size, and comparison to pretrained diffusion priors.

## Limits and Failure Modes

- Zero-shot optimization may be slower per image than feed-forward restoration.
- Random-network priors may fail on highly semantic degradations requiring learned world knowledge.
- Compression regularization depends on rate and complexity hyperparameters.
- Single-observation inverse problems remain ill-posed under severe degradation.

## Deep Themes

**Compression acts as a prior.** The method uses rate-distortion structure to regularize inverse recovery.

**Randomness can define a useful prior family.** Random architectures supply implicit biases without external data.

**Small models can solve structured inverse problems.** The result pushes against default reliance on huge pretrained restorers.

## Subthemes

- Zero-shot inverse problems.
- Neural compression priors.
- Random-network ensembles.
- Rate-distortion regularization.
- Denoising, super-resolution, and inpainting.

## Connections to Other Papers

Connects to Brain Encoding Scale, FlashOptim, SmoothSpike, and efficiency papers through compactness as capability. It also links to manifold-aware perturbations and diffusion-sampling theory through inverse/generative problem structure.

## Notes for Cross-Paper Synthesis

Lottery Prior adds to the "small but structured" theme: constraints from compression and architecture can substitute for large external datasets in some inverse problems.
