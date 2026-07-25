# Near-Optimal Private Linear Regression via Iterative Hessian Mixing

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: IwP8LZzc97
- Authors: Omri Lev; Moshe Shenfeld; Vishwak Srinivasan; Katrina Ligett; Ashia C. Wilson
- Primary area: social_aspects->privacy
- Keywords: Differential Privacy; Sketching; Private Linear Regression;
- Source URL: https://openreview.net/forum?id=IwP8LZzc97
- PDF URL: https://openreview.net/pdf?id=IwP8LZzc97

## Abstract

We study differentially private ordinary least squares (DP-OLS) with bounded data $(X,Y)$ via sketching-based mechanisms. While Gaussian sketching approaches have been explored for DP-OLS (Sheffet, 2017), they are typically viewed as less competitive than the Adaptive Sufficient Statistics Perturbation (AdaSSP) method (Wang, 2018), which directly perturbs the sufficient statistics $(X^{\top}X, X^{\top}Y)$. This method was shown to be close to information-theoretically optimal, while also exhibiting strong empirical performance. In this work, we propose \emph{Iterative Hessian Mixing} (IHM), an algorithm that builds on Gaussian-sketching approaches to DP-OLS and is inspired by the Iterative Hessian Sketch (Pilanci & Wainwright, 2016). We prove that IHM is differentially private and provide utility guarantees in the form of excess empirical risk bounds. These bounds improve upon those of AdaSSP by removing a multiplicative factor that can be as large as the square root of the data dimension. The design of the IHM is based on new accuracy guarantees that we present for prior Gaussian sketching approaches for DP-OLS, which clarify when these methods are expected to perform well and how IHM circumvents their inherent limitations.
We also conduct a rigorous empirical evaluation on a large suite of datasets, demonstrating that IHM consistently outperforms prior baselines, including AdaSSP.

## One-Sentence Claim

Iterative Hessian Mixing improves differentially private ordinary least squares by using sketching-based updates with stronger excess-risk guarantees than AdaSSP.

## Problem

DP-OLS mechanisms must protect bounded data while preserving utility, but prior Gaussian sketching methods were viewed as weaker than sufficient-statistics perturbation and had unclear accuracy regimes.

## Core Contribution

The paper proposes IHM, proves differential privacy and excess empirical risk bounds, improves over AdaSSP by removing a potentially sqrt(d)-sized multiplicative factor, and clarifies when Gaussian sketching works.

## Method

IHM builds on Gaussian sketching and the Iterative Hessian Sketch idea, repeatedly mixing/sketching Hessian information to solve private least squares with provable privacy and utility.

## Experiments and Evidence

The abstract reports rigorous experiments over a large suite of datasets, with IHM consistently outperforming prior baselines including AdaSSP.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: privacy parameters, boundedness assumptions, condition-number dependence, dataset suite, runtime cost, and practical tuning relative to AdaSSP.

## Deep Themes

- Revisiting older mechanisms with sharper analysis can change practical rankings.
- Privacy utility depends on geometry of the optimization problem.
- Sketching can be both an efficiency and privacy tool when paired with iterative structure.

## Subthemes

- Differential privacy.
- Ordinary least squares.
- Gaussian sketching.
- Iterative Hessian Sketch.
- Excess empirical risk.
- Sufficient-statistics perturbation.

## Connections to Other Papers

Connects to privacy and theory papers through rigorous privacy-utility tradeoffs, and to efficiency papers that use sketching or low-rank structure to reduce cost without giving up guarantees.

## Notes for Cross-Paper Synthesis

IHM adds a classical-statistics anchor to the privacy theme: strong theory is still improving foundational ML primitives, not only frontier foundation-model workflows.
