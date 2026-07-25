# Online Conformal Prediction via Universal Portfolio Algorithms

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: EKmiOtjZjI
- Authors: Tuo Liu; Edgar Dobriban; Francesco Orabona
- Primary area: theory->online_learning_and_bandits
- Keywords: Conformal prediction;online learning;universal portfolio
- Source URL: https://openreview.net/forum?id=EKmiOtjZjI
- PDF URL: https://openreview.net/pdf?id=EKmiOtjZjI

## Abstract

Online conformal prediction (OCP) seeks prediction intervals that achieve long-run $1-\alpha$ coverage for arbitrary (possibly adversarial) data streams, while remaining as informative as possible. Existing OCP methods often require manual learning-rate tuning to work well, and may also require algorithm-specific analyses. Here, we develop a general regret-to-coverage theory for interval-valued OCP based on the $(1-\alpha)$-pinball loss. Our first contribution is to identify *linearized regret* as a key notion, showing that controlling it implies coverage bounds for any online algorithm. This relies on a black-box reduction that depends only on the Fenchel conjugate of an upper bound on the linearized regret. Building on this theory, we propose UP-OCP, a parameter-free method for OCP, via a reduction to a two-asset portfolio selection problem, leveraging universal portfolio algorithms. We show strong finite-time bounds on the miscoverage of UP-OCP, even for polynomially growing predictions. Extensive experiments support that UP-OCP delivers consistently better size/coverage trade-offs than prior online conformal baselines.

## One-Sentence Claim

UP-OCP uses universal portfolio algorithms to obtain parameter-free online conformal prediction with finite-time coverage guarantees and strong size/coverage tradeoffs.

## Problem

Online conformal prediction must maintain long-run coverage on arbitrary streams while keeping intervals informative, but existing methods often need manual learning-rate tuning and custom analyses.

## Core Contribution

The paper develops a general regret-to-coverage theory based on linearized regret for the pinball loss, then reduces OCP to two-asset portfolio selection.

## Method

It shows that controlling linearized regret implies coverage bounds through a black-box reduction using the Fenchel conjugate of a regret upper bound. UP-OCP applies universal portfolio algorithms to adapt without tuning.

## Experiments and Evidence

The abstract reports finite-time miscoverage bounds even for polynomially growing predictions and experiments showing consistently better size/coverage tradeoffs than prior OCP baselines.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: interval construction, adversarial-stream assumptions, computational overhead, and empirical domains.

## Deep Themes

- Calibration guarantees can be derived from online-learning regret.
- Parameter-free uncertainty methods are valuable for deployment streams.
- Portfolio algorithms can serve as generic adaptation machinery beyond finance.

## Subthemes

- Online conformal prediction.
- Universal portfolios.
- Linearized regret.
- Pinball loss.
- Finite-time coverage.
- Adaptive intervals.

## Connections to Other Papers

Connects to robustness/certification papers, uncertainty-driven debate, and online learning theory through reliable uncertainty under distribution shift.

## Notes for Cross-Paper Synthesis

UP-OCP adds a calibration-under-streaming theme: adaptive guarantees can be built from generic regret machinery rather than hand-tuned update rules.
