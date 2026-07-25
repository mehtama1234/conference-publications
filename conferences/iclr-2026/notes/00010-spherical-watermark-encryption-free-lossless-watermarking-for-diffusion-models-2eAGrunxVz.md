# Spherical Watermark: Encryption-Free, Lossless Watermarking for Diffusion Models

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: 2eAGrunxVz
- Authors: Xiaoxiao Hu; Jiaqi Jin; Sheng Li; Wanli Peng; Xinpeng Zhang; Zhenxing Qian
- Primary area: alignment, fairness, safety, privacy, and societal considerations
- Keywords: AIGC Watermarking; Diffusion Models;
- Source URL: https://openreview.net/forum?id=2eAGrunxVz
- PDF URL: https://openreview.net/pdf?id=2eAGrunxVz

## Abstract

Diffusion models have revolutionized image synthesis but raise concerns around content provenance and authenticity. Digital watermarking offers a means of tracing generated media, yet traditional schemes often introduce distributional shifts and degrade visual quality. Recent lossless methods embed watermark bits directly into the latent Gaussian prior without modifying model weights, but still require per-image key storage or heavy cryptographic overhead. In this paper, we introduce Spherical Watermark, an encryption‐free and lossless watermarking framework that integrates seamlessly with diffusion architectures. First, our binary embedding module mixes repeated watermark bits with random padding to form a high-entropy code. Second, the spherical mapping module projects this code onto the unit sphere, applies an orthogonal rotation, and scales by a chi-square-distributed radius to recover exact multivariate Gaussian noise. We theoretically prove that the watermarked noise distribution preserves the target prior up to third-order moments, and empirically demonstrate that it is statistically indistinguishable from a standard multivariate normal distribution. Adopting Stable Diffusion, extensive experiments confirm that Spherical Watermark consistently preserves high visual fidelity while simultaneously improving traceability, computational efficiency, and robustness under attacks, thereby outperforming both lossy and lossless approaches.

## One-Sentence Claim

Spherical Watermark embeds traceable bits into diffusion-model latent Gaussian noise while preserving the prior distribution closely enough to remain lossless, efficient, and robust.

## Problem

Diffusion-generated media needs provenance and authenticity mechanisms, but watermarking can degrade image quality, shift the sampling distribution, or require per-image keys and cryptographic overhead.

## Core Contribution

The paper proposes an encryption-free lossless diffusion watermarking framework that maps encoded watermark bits onto a spherical Gaussian construction, preserving the model's latent prior while improving traceability and robustness.

## Method

The method mixes repeated watermark bits with random padding into a high-entropy code, maps it to the unit sphere through an orthogonal rotation, and scales it with a chi-square-distributed radius to recover multivariate Gaussian noise.

## Experiments and Evidence

The abstract claims preservation of the target prior up to third-order moments, empirical statistical indistinguishability from standard Gaussian noise, and Stable Diffusion experiments showing strong fidelity, traceability, efficiency, and robustness under attacks.

## Limits and Failure Modes

No confident arXiv/PDF match is local yet. Checks needed: threat model, image-editing attack coverage, payload capacity, detection false positives, and whether third-order moment preservation is enough for all diffusion models.

## Deep Themes

- Provenance tools for generative media are becoming distribution-preserving.
- Safety mechanisms are being embedded into model sampling processes.
- Watermarking research is balancing traceability, robustness, and indistinguishability.

## Subthemes

- Diffusion watermarking.
- Lossless latent watermarking.
- Gaussian prior preservation.
- Content provenance.
- Attack robustness.

## Connections to Other Papers

Connects directly to ICML Catch-22 on watermarking tradeoffs. Together they suggest watermark design must manage detectability, robustness, fidelity, and distribution leakage.

## Notes for Cross-Paper Synthesis

This paper provides the diffusion-media counterpart to LLM watermarking: provenance is becoming a statistical distribution-design problem, not just a signature overlay.
