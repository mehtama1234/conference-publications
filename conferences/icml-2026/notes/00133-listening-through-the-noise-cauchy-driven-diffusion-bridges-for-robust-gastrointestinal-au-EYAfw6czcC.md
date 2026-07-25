# Listening Through the Noise: Cauchy-Driven Diffusion Bridges for Robust Gastrointestinal Auscultation and Clinical Benchmarking

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: EYAfw6czcC
- Authors: Dian Ding; Liren Dong; Yu Lu; Juntao Zhou; Ran Wang; Peng Li; Zhenyi Jia; Guangtao Xue
- Primary area: applications->health_medicine
- Keywords: Bowel Sound Analysis;Biomedical Signal Processing
- Source URL: https://openreview.net/forum?id=EYAfw6czcC
- PDF URL: https://openreview.net/pdf?id=EYAfw6czcC

## Abstract

Gastrointestinal (GI) motility assessment via bowel sounds (BS) offers a non-invasive alternative to resource-intensive clinical standards. However, the diagnostic utility of BS is often compromised by its spectral overlap with non-stationary speech interference. While generative models have advanced signal restoration, traditional Gaussian-based diffusion frameworks struggle with the impulsive, heavy-tailed nature of real-world clinical noise. In this paper, we propose a novel Cauchy-driven Diffusion Bridge framework to isolate high-fidelity bowel sounds from complex interference. Our contributions are three-fold: (1) We introduce ClinBS, a large-scale clinical dataset (over 25 hours) containing rare pathological transients verified by experts; (2) We mathematically formulate a Cauchy bridge driver, deriving closed-form expressions for the score and density to better model heavy-tailed perturbations; and (3) We implement an efficient sampling procedure via Gaussian scale-mixture reparameterization. Extensive experiments show our framework achieves state-of-the-art performance, outperforming baselines by 13.4%–49.8% across core metrics and elevating abnormal BS recognition accuracy to 88.01%. These results demonstrate the system's potential for robust clinical GI monitoring and diagnosis.

## One-Sentence Claim

Cauchy-driven diffusion bridges restore bowel sounds under heavy-tailed clinical noise, improving robust gastrointestinal auscultation and abnormal-sound recognition.

## Problem

GI motility assessment via bowel sounds is non-invasive, but clinical utility is limited by speech interference and heavy-tailed non-stationary noise that Gaussian diffusion models handle poorly.

## Core Contribution

The paper introduces ClinBS, a clinical bowel-sound dataset, and a Cauchy-driven diffusion bridge with closed-form score/density and efficient scale-mixture sampling.

## Method

It formulates a Cauchy bridge driver to model impulsive heavy-tailed perturbations and implements sampling through Gaussian scale-mixture reparameterization.

## Experiments and Evidence

The abstract reports over 25 hours of expert-verified clinical data, 13.4%-49.8% improvements across core metrics, and abnormal bowel-sound recognition accuracy of 88.01%.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: clinical cohort, noise conditions, annotation protocol, bridge comparison baselines, and diagnostic validation.

## Deep Themes

- Clinical audio restoration needs noise models matched to heavy-tailed real-world interference.
- Diffusion bridge methods are expanding into biomedical signal processing.
- Robust restoration can directly improve downstream diagnosis.

## Subthemes

- Gastrointestinal auscultation.
- Bowel sound analysis.
- Cauchy diffusion bridges.
- Heavy-tailed noise.
- Biomedical signal restoration.
- Clinical benchmarking.

## Connections to Other Papers

Connects to SleepLM, Control Consistency Losses, and healthcare time-series/audio papers through domain-specific foundation/sampling methods for clinical signals.

## Notes for Cross-Paper Synthesis

This paper adds a clinical-noise-modeling theme: robust medical AI often depends on matching the stochastic corruption process, not only scaling the model.
