# InfoNCE Induces Gaussian Distribution

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: BlSH7gNQSq
- Authors: Roy Betser; Eyal Gofer; Meir Yossef Levi; Guy Gilboa
- Primary area: learning theory
- Keywords: Contrastive learning;Gaussian distribution;InfoNCE
- Source URL: https://openreview.net/forum?id=BlSH7gNQSq
- PDF URL: https://openreview.net/pdf?id=BlSH7gNQSq

## Abstract

Contrastive learning has been at the bedrock of unsupervised learning in recent years, allowing training with massive
unlabeled data for both task-specific and general (foundation) models.
A prototypical loss in contrastive training is InfoNCE and its variants. In this paper we show that the embedding of the features
which emerge from InfoNCE training can be well approximated by
a multivariate Gaussian distribution. We justify this claim by
taking two approaches. First, we show that under certain  alignment and concentration assumptions, finite projections of a high dimensional representation approach multivariate Gaussian distribution, as the representation dimensions approach infinity.
Next, under less strict assumptions, we show that adding a small regularization term (which vanishes asymptotically) that promotes low feature norm and high feature entropy, we reach similar asymptotic results. 
We demonstrate experimentally, in a synthetic setting, CIFAR-10 and on pretrained foundation models, that the features indeed follow almost precise 
Gaussian distribution. One can use the Gaussian model to easily derive analytic expressions in the representation space and to obtain very useful measures, such as likelihood, data entropy and mutual information. Hence, we expect such theoretical grounding to be very
useful in various applications involving contrastive learning.

## One-Sentence Claim

InfoNCE-trained high-dimensional representations are well approximated by multivariate Gaussian distributions, enabling analytic measures such as likelihood, entropy, and mutual information.

## Problem

Contrastive learning with InfoNCE is central to unsupervised and foundation-model training, but the distributional geometry of learned feature embeddings is not fully understood.

Without a tractable distributional model, it is harder to derive analytic quantities in representation space.

## Core Contribution

The paper argues theoretically and empirically that features emerging from InfoNCE training approach multivariate Gaussian distributions.

It gives two routes: one under alignment and concentration assumptions, and one under weaker assumptions with a vanishing regularizer encouraging low feature norm and high entropy.

## Method

The first theoretical approach studies finite projections of high-dimensional representations as dimensionality grows, proving Gaussian convergence under alignment and concentration assumptions.

The second adds a small asymptotically vanishing regularization term that promotes low norm and high entropy, reaching similar Gaussianity under less strict conditions.

## Experiments and Evidence

The abstract reports experiments in synthetic settings, CIFAR-10, and pretrained foundation models showing features follow an almost precise Gaussian distribution.

It also notes that the Gaussian model yields analytic expressions for likelihood, data entropy, and mutual information.

## Limits and Failure Modes

Gaussian approximation may be weaker for multimodal, clustered, or highly anisotropic representations, especially before normalization or under supervised contrastive variants.

Because this note is abstract-only, details still need checking: exact assumptions, regularizer form, goodness-of-fit tests, foundation models evaluated, and whether class-conditional structure remains Gaussian.

## Deep Themes

- Distributional geometry of representation learning: contrastive embeddings may have simple asymptotic form.
- Gaussianity as analytic bridge: likelihood, entropy, and mutual information become tractable.
- High-dimensional projection behavior: feature distributions simplify as dimension grows.
- Regularization-induced geometry: small norm/entropy terms can shape asymptotic representation distributions.

## Subthemes

- InfoNCE theory.
- Multivariate Gaussian embeddings.
- Alignment and concentration assumptions.
- Entropy and mutual-information estimation.

## Connections to Other Papers

This connects to embedding collapse, Gaussian single-index learning, and phase-retrieval dynamics through representation geometry under high-dimensional assumptions.

It also relates to contrastive difficult-example theory, offering a distributional lens on the features produced by contrastive objectives.

## Notes for Cross-Paper Synthesis

This paper adds a probabilistic-representation theme: self-supervised objectives may induce simple latent distributions that make downstream analysis possible.
