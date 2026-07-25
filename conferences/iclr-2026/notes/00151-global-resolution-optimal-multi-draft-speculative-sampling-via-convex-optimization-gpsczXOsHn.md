# Global Resolution: Optimal Multi-Draft Speculative Sampling via Convex Optimization

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: gpsczXOsHn
- Authors: Rahul Krishna Thomas; Arka Pal
- Primary area: probabilistic methods (Bayesian methods, variational inference, sampling, UQ, etc.)
- Keywords: LLMs;Inference;Optimal Transport;Speculative Decoding
- Source URL: https://openreview.net/forum?id=gpsczXOsHn
- PDF URL: https://openreview.net/pdf?id=gpsczXOsHn

## Abstract

Speculative sampling reduces the latency of autoregressive decoding for target model LLMs without sacrificing inference quality, by using a cheap draft model to suggest a candidate token and a verification criterion to accept or resample this token. To improve acceptance and decoding efficiency, recent work has explored the multi-draft extension, where at each step $n$ draft tokens are generated, and the verification criterion is a distribution conditioned on these. When this criterion maximizes the probability of accepting some draft token, it is called the optimal transport (OT). However, finding the OT is difficult, as it is the solution of a linear program (OTLP) in over $V^n$ variables, with $V$ being the vocabulary size. Two recent theoretical works have reframed the OTLP in terms of importance sampling or subset selection. In this work, we prove that these formulations are equivalent to an exponentially large relaxed OTLP, so it remains infeasible to solve. Then, we reverse engineer subset selection to formulate the OTLP as a max-flow problem. With a novel application of polymatroid theory, we reduce the exponentially large OTLP to a convex optimization problem in at most $V$ variables. This allows us to devise an algorithm for optimal $n$-draft speculative sampling when the $n$ tokens are chosen i.i.d. from a single draft model, which can be tuned to arbitrary accuracy. Finally, we measure acceptance rates and algorithm runtimes for various $n$ and top-$k$ draft sampling settings. Our findings give the first multi-draft algorithm with 90\% acceptance and under 100 ms of overhead per generated token with negligible deviation from the target model distribution.

## One-Sentence Claim

Global Resolution reduces optimal multi-draft speculative sampling from an exponential optimal-transport problem to a tractable convex optimization problem, enabling high-acceptance distribution-preserving decoding.

## Problem

Speculative sampling speeds autoregressive decoding by using draft tokens and target-model verification, but multi-draft variants require an optimal acceptance/resampling criterion.

The optimal transport formulation maximizes acceptance probability but naively requires solving a linear program over more than vocabulary-size-to-the-number-of-drafts variables, making it infeasible.

## Core Contribution

The paper proves recent importance-sampling and subset-selection formulations remain equivalent to an exponentially large relaxed OT problem.

It then reformulates optimal multi-draft verification through max-flow and polymatroid theory, reducing the problem to convex optimization in at most vocabulary-size variables.

## Method

The method reverse-engineers subset selection into a max-flow formulation and uses polymatroid structure to collapse the exponential OTLP.

The resulting algorithm computes an approximately optimal n-draft speculative sampling rule when draft tokens are sampled i.i.d. from one draft model, with tunable accuracy.

## Experiments and Evidence

The abstract reports acceptance-rate and runtime measurements across n and top-k draft sampling settings.

The method reaches 90 percent acceptance with under 100 ms overhead per generated token and negligible deviation from the target distribution.

## Limits and Failure Modes

The stated algorithm assumes i.i.d. draft tokens from a single draft model; correlated drafts, multiple draft models, or structured draft proposals may need extensions. Overhead may also be too high for small target models.

Because this note is abstract-only, details still need checking: convex program form, approximation guarantees, vocabulary/top-k handling, distribution-deviation metric, and end-to-end latency.

## Deep Themes

- Distribution-preserving acceleration: speculative decoding remains useful only if target-model law is preserved.
- Convex relaxation of exponential verification: mathematical structure turns infeasible OT into practical inference control.
- Multi-draft acceptance optimization: more proposals require globally optimal acceptance rules rather than local heuristics.
- Polymatroid theory in LLM inference: classical combinatorial optimization enters decoding algorithms.

## Subthemes

- Multi-draft speculative sampling.
- Optimal transport verification.
- Max-flow and polymatroids.
- Convex optimization for decoding.

## Connections to Other Papers

This connects to HSD, Prophet, Speculative Actions, ThinKV, and p-less sampling through test-time inference acceleration.

It also relates to HTI and Wasserstein/OT papers through optimal-transport structure used for practical model behavior control.

## Notes for Cross-Paper Synthesis

Global Resolution adds to the lossless-inference theme: 2026 decoding work increasingly uses exact optimization structure to preserve model distributions while reducing latency.
