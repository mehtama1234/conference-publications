# LiveMoments: Reselected Key Photo Restoration in Live Photos via Reference-guided Diffusion

## Metadata

- Conference: iclr-2026
- Status: Poster
- OpenReview ID: 02mgFnnfqG
- Authors: Clara Xue; Zizheng Yan; Zhenning Shi; Yuhang Yu; Jingyu Zhuang; Qi Zhang; Jinwei Chen; Qingnan Fan
- Primary area: applications to computer vision, audio, language, and other modalities
- Keywords: Live Photo;Reference-based Image Restoration;Conditional Image Generation;Motion Alignment
- Source URL: https://openreview.net/forum?id=02mgFnnfqG
- PDF URL: https://openreview.net/pdf?id=02mgFnnfqG

## Abstract

Live Photo captures both a high-quality key photo and a short video clip to preserve the precious dynamics around the captured moment. 
While users may choose alternative frames as the key photo to capture better expressions or timing, these frames often exhibit noticeable quality degradation, as the photo capture ISP pipeline delivers significantly higher image quality than the video pipeline. This quality gap highlights the need for dedicated restoration techniques to enhance the reselected key photo. To this end, we propose LiveMoments, a reference-guided image restoration framework tailored for the reselected key photo in Live Photos. Our method employs a two-branch neural network: a reference branch that extracts structural and textural information from the original high-quality key photo, and a main branch that restores the reselected frame using the guidance provided by the reference branch. Furthermore, we introduce a unified Motion Alignment module that incorporates motion guidance for spatial alignment at both the latent and image levels. Experiments on real and synthetic Live Photos demonstrate that LiveMoments significantly improves perceptual quality and fidelity over existing solutions, especially in scenes with fast motion or complex structures.

## One-Sentence Claim

LiveMoments restores lower-quality reselected Live Photo frames by using the original high-quality key photo as a reference and aligning motion at latent and image levels.

## Problem

Live Photos contain a high-quality key photo and lower-quality video frames. When users reselect a better-timed video frame as the key photo, the new frame can suffer from video-pipeline quality degradation, especially with fast motion or complex structure.

## Core Contribution

The paper contributes a reference-guided image restoration framework tailored to reselected Live Photo key frames. It uses a two-branch network and a unified Motion Alignment module to transfer structural and textural guidance from the original high-quality photo.

## Method

LiveMoments has a reference branch that extracts structure and texture from the original key photo and a main branch that restores the selected video frame. Motion Alignment provides spatial alignment at both latent and image levels so reference details can guide restoration despite temporal movement.

## Experiments and Evidence

The abstract reports experiments on real and synthetic Live Photos, showing improved perceptual quality and fidelity over existing solutions, particularly for fast motion and complex scenes.

## Limits and Failure Modes

This note is abstract/metadata-only. Full-text review should inspect dataset realism, motion magnitude, temporal alignment errors, reference-frame mismatch, artifact rates, and whether restoration hallucinates details not present in the selected frame. User-perceived quality may trade off with faithfulness to the chosen moment.

## Deep Themes

- Reference-guided diffusion restoration.
- Consumer-media quality gap correction.
- Motion-aware spatial alignment.
- Real/synthetic data pairing for restoration.

## Subthemes

- Live Photos.
- Reselected key frames.
- Two-branch restoration.
- Latent and image-level alignment.
- Perceptual fidelity.

## Connections to Other Papers

Connects to MotionStream through motion-conditioned generation, to DA3 through geometric/spatial consistency, and to ImageDoctor through the need for localized image-quality diagnostics.

## Notes for Cross-Paper Synthesis

LiveMoments fits the corpus pattern of using a better reference signal rather than asking the model to invent quality from scratch. The restoration problem is solved as alignment plus guided reconstruction, not generic enhancement.
