# Distribution Transformers: Fast Approximate Bayesian Inference With On-The-Fly Prior Adaptation

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: bMHwh8qAGc
- Authors: George Whittle; Juliusz Ziomek; Jacob Henry Rawling; Michael A Osborne
- Primary area: probabilistic_methods->bayesian_models_and_methods
- Keywords: Amortized Bayesian Inference;Bayesian Filtering;Sequential Inference;Prior Amortization
- Source URL: https://openreview.net/forum?id=bMHwh8qAGc
- PDF URL: https://openreview.net/pdf?id=bMHwh8qAGc

## Abstract

While Bayesian inference provides a principled framework for reasoning under uncertainty, its widespread adoption is limited by the intractability of exact posterior computation, necessitating the use of approximate inference. However, existing methods are often computationally expensive, or demand costly retraining when priors change, limiting their utility, particularly  in sequential inference problems such as real-time sensor fusion. To address these challenges, we introduce the Distribution Transformer---a novel architecture that can learn arbitrary distribution-to-distribution mappings. Our method can be trained to map a prior to the corresponding posterior, conditioned on some dataset---thus performing approximate Bayesian inference. Our novel architecture represents a prior distribution as a (universally-approximating) Gaussian Mixture Model (GMM), and transforms it into a GMM representation of the posterior. The components of the GMM attend to each other via self-attention, and to the datapoints via cross-attention. We demonstrate that Distribution Transformers both maintain flexibility to vary the prior, and significantly reduces computation times---from minutes to milliseconds---while achieving expected log-likelihood performance on par with or superior to existing approximate inference methods across tasks such as sequential inference, quantum system parameter inference, and Gaussian Process predictive posterior inference with hyperpriors.

## One-Sentence Claim

Distribution Transformers amortize Bayesian inference as prior-to-posterior GMM transformations, enabling millisecond approximate inference with on-the-fly prior changes.

## Problem

Bayesian inference is principled but often too expensive for exact posterior computation. Approximate methods can still be slow or require retraining when priors change, which is especially limiting in sequential settings such as real-time sensor fusion.

The paper asks how to amortize inference while preserving flexibility to vary the prior at deployment time.

## Core Contribution

The paper introduces the Distribution Transformer, an architecture that learns distribution-to-distribution mappings. It represents a prior as a universally approximating Gaussian mixture model and transforms it into a posterior GMM conditioned on data.

GMM components attend to each other with self-attention and attend to datapoints with cross-attention. The method reduces computation from minutes to milliseconds while matching or exceeding expected log-likelihood of existing approximate inference methods.

## Method

The model treats mixture components as tokens. Self-attention lets prior components exchange information, while cross-attention lets them condition on observations. The output is a transformed GMM representing the posterior.

Because the prior itself is an input distribution, changing the prior at inference time does not require retraining.

## Experiments and Evidence

Evidence reported in the abstract:

- Arbitrary distribution-to-distribution mapping architecture.
- Prior-to-posterior approximate Bayesian inference.
- GMM prior and posterior representations.
- Computation reduced from minutes to milliseconds.
- Sequential inference, quantum system parameter inference, and GP predictive posterior inference with hyperpriors.
- Expected log-likelihood on par with or better than existing approximate inference methods.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: GMM component counts, training distributions, posterior calibration, and sequential update behavior.

## Limits and Failure Modes

- GMM approximation quality may degrade for highly complex or constrained posteriors.
- Amortization can fail under prior/data distributions outside training support.
- Posterior calibration needs careful validation, not only log-likelihood.
- Component attention cost may grow with mixture size and dataset size.

## Deep Themes

**Inference can be learned as distribution transformation.** The model maps priors to posteriors directly.

**Priors should remain runtime inputs.** On-the-fly prior adaptation avoids retraining whenever beliefs change.

**Attention is used over distributions, not just sequences.** GMM components become tokens in a probabilistic computation.

## Subthemes

- Amortized Bayesian inference.
- Prior amortization.
- GMM-to-GMM posterior maps.
- Sequential inference.
- Attention over mixture components.

## Connections to Other Papers

Connects to BFTS, TRECA, ROCP, and Distributional IRL through uncertainty-aware decision systems. It also links to Flow Sampling because both learn fast approximations to expensive probabilistic computations.

## Notes for Cross-Paper Synthesis

Distribution Transformers add to the amortization theme: expensive inference can become a learned operator when distributions themselves are represented as structured inputs.
