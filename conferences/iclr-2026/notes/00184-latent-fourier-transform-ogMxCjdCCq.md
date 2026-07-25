# Latent Fourier Transform

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: ogMxCjdCCq
- Authors: Mason Long Wang; Cheng-Zhi Anna Huang
- Primary area: applications to computer vision, audio, language, and other modalities
- Keywords: Music Generation;Signal Processing;Diffusion Models;Audio;Music;Audio Generation;Controllable Generation;Fourier Transform;Diffusion Autoencoders
- Source URL: https://openreview.net/forum?id=ogMxCjdCCq
- PDF URL: https://openreview.net/pdf?id=ogMxCjdCCq

## Abstract

We introduce the Latent Fourier Transform (LatentFT), a framework that provides novel frequency-domain controls for generative music models. LatentFT combines a diffusion autoencoder with a latent-space Fourier transform to separate musical patterns by timescale. By masking latents in the frequency domain during training, our method yields representations that can be manipulated coherently at inference. This allows us to generate musical variations and blends from reference examples while preserving characteristics at desired timescales, which are specified as frequencies in the latent space. LatentFT parallels the role of the equalizer in music production: while traditional equalizers operates on audible frequencies to shape timbre, LatentFT operates on latent-space frequencies to shape musical structure. Experiments and listening tests show that LatentFT improves condition adherence and quality compared to baselines. We also present a technique for hearing frequencies in the latent space in isolation, and show different musical attributes reside in different regions of the latent spectrum. Our results show how frequency-domain control in latent space provides an intuitive, continuous frequency axis for conditioning and blending, advancing us toward more interpretable and interactive generative music models.

## One-Sentence Claim

LatentFT gives generative music models frequency-domain controls in latent space, letting users manipulate musical structure across timescales rather than only audible timbre.

## Problem

Music generation needs controllable variation and blending across different structural timescales, but controls are often opaque or tied to surface audio features. Traditional equalizers shape audible frequency/timbre, not latent musical patterns such as motif, rhythm, or larger structure.

## Core Contribution

The paper introduces Latent Fourier Transform, combining a diffusion autoencoder with a Fourier transform over latent representations. Frequency-domain latent masking during training creates representations that can be coherently manipulated at inference.

## Method

LatentFT trains a diffusion autoencoder with latent-space frequency masking so different musical attributes organize across latent spectral regions. At inference, users mask, blend, or alter latent frequencies to preserve or vary musical characteristics at selected timescales. The paper also introduces a way to hear isolated latent frequencies.

## Experiments and Evidence

Experiments and listening tests reportedly show improved condition adherence and quality relative to baselines. The analysis shows that different musical attributes occupy different regions of the latent spectrum.

## Limits and Failure Modes

Latent frequency axes may not map cleanly to human-interpretable musical concepts across genres, tempos, or instrumentation. Listening tests can be subjective and dataset-dependent. Full-text review should check music datasets, user controls, evaluation design, ablations, and how latent-frequency isolation is rendered.

## Deep Themes

- Interpretable controls for generative music.
- Frequency-domain structure in latent spaces.
- Timescale-aware generation and blending.
- Diffusion autoencoders for controllable media.

## Subthemes

- Latent-space Fourier transform.
- Latent frequency masking.
- Musical variation preservation.
- Reference-based blending.
- Listening-test evaluation.

## Connections to Other Papers

Connects to SANA-Video, MotionStream, and image/video generation papers through controllable media generation, and to representation-geometry papers where latent axes become operational control surfaces.

## Notes for Cross-Paper Synthesis

LatentFT adds a clear example of interpretable control emerging from structured latent transforms. The broader pattern is turning representation geometry into a user-facing editing interface.
