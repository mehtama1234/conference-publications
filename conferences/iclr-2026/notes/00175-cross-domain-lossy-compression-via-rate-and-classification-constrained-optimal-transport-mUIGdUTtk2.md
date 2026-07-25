# Cross-Domain Lossy Compression via Rate- and Classification-Constrained Optimal Transport

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: mUIGdUTtk2
- Authors: Nam Nguyen; Thinh Nguyen; Bella Bose
- Primary area: applications to computer vision, audio, language, and other modalities
- Keywords: Lossy Compression;Image Compression;Image Restoration;Image Inpainting;Optimal Transport;Multi-task Learning;Rate-Distortion-Perception Tradeoff;Rate-Distortion-Classification Tradeoff;Deep Learning;Unsupervised Learning
- Source URL: https://openreview.net/forum?id=mUIGdUTtk2
- PDF URL: https://openreview.net/pdf?id=mUIGdUTtk2

## Abstract

We study cross-domain lossy compression, where the encoder observes a degraded source while the decoder reconstructs samples from a distinct target distribution. The problem is formulated as constrained optimal transport with two constraints on compression rate and classification loss. With shared common randomness, the one-shot setting reduces to a deterministic transport plan, and we derive closed-form distortion-rate-classification (DRC) and rate-distortion-classification (RDC) tradeoffs for Bernoulli sources under Hamming distortion. In the asymptotic regime, we establish analytic DRC/RDC expressions for Gaussian models under mean-squared error. The framework is further extended to incorporate perception divergences (Kullback-Leibler and squared Wasserstein), yielding closed-form distortion-rate-perception-classification (DRPC) functions. To validate the theory, we develop deep end-to-end compression models for super-resolution (MNIST), denoising (SVHN, CIFAR-10, ImageNet, KODAK), and inpainting (SVHN) problems, demonstrating the consistency between the theoretical results and empirical performance.

## One-Sentence Claim

The paper formulates cross-domain lossy compression as constrained optimal transport, deriving rate-distortion-classification and perception-aware tradeoffs and validating them with deep compression models.

## Problem

Classical lossy compression usually reconstructs the same source distribution, but restoration settings such as denoising, inpainting, and super-resolution require decoding from a different target distribution. Compression must balance bit rate, distortion, perceptual quality, and downstream classification utility.

## Core Contribution

The paper gives an optimal-transport framework for cross-domain lossy compression with rate and classification constraints, derives closed-form tradeoffs for Bernoulli and Gaussian models, extends them with perception divergences, and builds end-to-end deep models to test the theory.

## Method

The framework treats encoder observations from a degraded source and decoder outputs in a target domain as a constrained transport problem. In one-shot settings with shared common randomness, the transport reduces to a deterministic plan. The analysis derives DRC/RDC and DRPC functions under Hamming and MSE settings, then trains neural compression systems for image restoration tasks.

## Experiments and Evidence

The abstract reports empirical validation on super-resolution for MNIST, denoising for SVHN, CIFAR-10, ImageNet, and KODAK, and inpainting for SVHN. The observed deep-model behavior is said to match the theoretical tradeoffs.

## Limits and Failure Modes

Closed-form theory may rely on idealized Bernoulli/Gaussian assumptions and shared common randomness. Classification constraints depend on the chosen classifier and may not capture semantic utility broadly. Full-text review should check rate models, perception divergences, neural architectures, whether target distributions are genuinely distinct, and how empirical tradeoff curves are measured.

## Deep Themes

- Optimal transport for compression and restoration.
- Multi-objective rate-distortion-utility tradeoffs.
- Cross-domain reconstruction.
- Theory-to-deep-model validation.

## Subthemes

- Distortion-rate-classification functions.
- Rate-distortion-perception-classification tradeoffs.
- Shared randomness and deterministic transport.
- Restoration as target-domain compression.
- Classification-constrained image compression.

## Connections to Other Papers

Connects to Global Resolution through optimal transport as a tractable systems tool, to image restoration and generative modeling papers through perception/distortion tradeoffs, and to data-efficient compression themes in representation learning.

## Notes for Cross-Paper Synthesis

This paper gives a formal version of a common applied tension: compressed outputs must be small, faithful, perceptually plausible, and useful for downstream decisions. Optimal transport supplies a language for balancing those requirements.
