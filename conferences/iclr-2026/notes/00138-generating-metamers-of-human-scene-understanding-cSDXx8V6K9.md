# Generating metamers of human scene understanding

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: cSDXx8V6K9
- Authors: Ritik Raina; Abe Leite; Alexandros Graikos; Seoyoung Ahn; Dimitris Samaras; Greg Zelinsky
- Primary area: applications to neuroscience & cognitive science
- Keywords: human scene understanding;generative modeling
- Source URL: https://openreview.net/forum?id=cSDXx8V6K9
- PDF URL: https://openreview.net/pdf?id=cSDXx8V6K9

## Abstract

Human vision combines low-resolution “gist” information from the visual periphery with sparse but high-resolution information from fixated locations to construct a coherent understanding of a visual scene. In this paper, we introduce MetamerGen, a tool for generating scenes that are aligned with latent human scene representations. MetamerGen is a latent diffusion model that combines peripherally obtained scene gist information with information obtained from scene-viewing fixations to generate image metamers for what humans understand after viewing a scene. Generating images from both high and low resolution (i.e. “foveated”) inputs constitutes a novel image-to-image synthesis problem, which we tackle by introducing a dual-stream representation of the foveated scenes consisting of DINOv2 tokens that fuse detailed features from fixated areas with peripherally degraded features capturing scene context. To evaluate the perceptual alignment of MetamerGen generated images to latent human scene representations, we conducted a same-different behavioral experiment where participants were asked for a “same” or “different” response between the generated and the original image. With that, we identify scene generations that are indeed metamers for the latent scene representations formed by the viewers. MetamerGen is a powerful tool for understanding scene understanding. Our proof-of-concept analyses uncovered specific features at multiple levels of visual processing that contributed to human judgments. While it can generate metamers even conditioned on random fixations, we find that high-level semantic alignment most strongly predicts metamerism when the generated scenes are conditioned on viewers’ own fixated regions.

## One-Sentence Claim

MetamerGen generates images aligned with latent human scene representations by combining peripheral gist and fixation-specific detail in a foveated latent diffusion model.

## Problem

Human scene understanding integrates low-resolution peripheral context with sparse high-resolution information from fixations.

Standard image generation does not directly model this foveated perceptual process or produce images that are equivalent under a viewer's latent scene representation.

## Core Contribution

The paper introduces MetamerGen, a latent diffusion tool for generating scene metamers.

It formulates image-to-image synthesis from foveated inputs and evaluates whether generated scenes match human latent representations through behavioral same-different judgments.

## Method

MetamerGen uses a dual-stream representation of foveated scenes based on DINOv2 tokens.

One stream captures detailed features from fixated regions, while the other captures degraded peripheral scene gist. The latent diffusion model generates candidate metamers from this combined representation.

## Experiments and Evidence

The abstract reports same-different behavioral experiments with human participants.

Some generated images are identified as metamers of viewers' latent scene representations. Analyses find features at multiple visual-processing levels contributing to judgments, and high-level semantic alignment is strongest when conditioning on viewers' own fixations.

## Limits and Failure Modes

Metamer judgments may depend on display time, task framing, participant variability, and fixation measurement quality. DINOv2 features may not fully match human visual representations.

Because this note is abstract-only, details still need checking: behavioral protocol, fixation acquisition, generation setup, participant count, metamer criteria, and statistical analyses.

## Deep Themes

- Human-aligned generative probes: generated images become tools for studying perception.
- Foveated representation: scene understanding combines peripheral gist with fixation detail.
- Behavioral validation of latent representations: human judgments test whether generated samples match internal percepts.
- Cognitive science meets diffusion: generative models operationalize hypotheses about visual processing.

## Subthemes

- Scene metamers.
- Foveated image synthesis.
- DINOv2 token streams.
- Same-different behavioral evaluation.

## Connections to Other Papers

This connects to DepthLM, DAVE, AnyUp, and visual representation papers.

It also relates to Energy-Based Transformers and representation diagnostics because generative models are used to probe latent understanding.

## Notes for Cross-Paper Synthesis

MetamerGen adds a cognitive-evaluation theme: generative models can test alignment with human representations, not only generate visually plausible images.
