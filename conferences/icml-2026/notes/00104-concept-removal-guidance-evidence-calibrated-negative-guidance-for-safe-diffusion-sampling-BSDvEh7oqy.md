# Concept Removal Guidance: Evidence-Calibrated Negative Guidance for Safe Diffusion Sampling

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: BSDvEh7oqy
- Authors: Yoonseok Choi; Chaeyoung Oh; Hyunjun Choi; Seokin Seo; Kee-Eung Kim
- Primary area: applications->computer_vision
- Keywords: Diffusion Models;Safety;Computer Vision;Privacy
- Source URL: https://openreview.net/forum?id=BSDvEh7oqy
- PDF URL: https://openreview.net/pdf?id=BSDvEh7oqy

## Abstract

Text-to-image diffusion models remain vulnerable to adversarial prompts that elicit disallowed content, motivating reliable inference-time controls. A popular approach is negative guidance, which subtracts a negative prompt direction with a fixed weight. However, it often forces a safety–fidelity trade-off, causing artifacts or prompt drift when over-applied and failing under attacks when under-applied. Dynamic variants reweight guidance using posterior-odds signals, which can be brittle for open-vocabulary compositional prompts, while lightweight similarity-based methods ignore the evolving image evidence along the denoising trajectory. We introduce Concept Removal Guidance (CRG), a training-free method that estimates unwanted-concept presence at each diffusion step from the model's noise predictions, and adaptively calibrates negative guidance via a closed-form constrained update enforcing a target presence threshold while minimally perturbing the conditional trajectory. Across red-teaming benchmarks, CRG reduces attack success rates while preserving benign fidelity, and extends to additional suppression targets such as artist style and violence without fine-tuning or external classifiers.

## One-Sentence Claim

Concept Removal Guidance adaptively calibrates negative diffusion guidance from denoising evidence to suppress unwanted concepts while minimally perturbing benign generation.

## Problem

Fixed negative guidance creates a safety-fidelity tradeoff: too much guidance causes artifacts or prompt drift, while too little fails under adversarial prompts.

## Core Contribution

The paper introduces CRG, a training-free inference-time method that estimates unwanted concept presence at each denoising step and solves a constrained update to enforce a target threshold.

## Method

CRG uses the model's noise predictions as evolving evidence of unwanted concept presence, then adaptively sets negative guidance through a closed-form constrained update that minimally alters the conditional denoising trajectory.

## Experiments and Evidence

The abstract reports reduced attack success on red-teaming benchmarks while preserving benign fidelity, and extension to suppression targets such as artist style and violence without fine-tuning or external classifiers.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: concept-presence estimator, thresholds, adversarial prompt set, benign fidelity metrics, and false-positive suppression.

## Deep Themes

- Diffusion safety can be controlled at inference time through evidence-calibrated guidance.
- Safety-fidelity tradeoffs improve when intervention strength follows the denoising trajectory.
- Open-vocabulary safety controls need internal evidence, not only prompt similarity.

## Subthemes

- Safe diffusion sampling.
- Negative guidance.
- Concept removal.
- Red-teaming.
- Training-free safety.
- Privacy/style suppression.

## Connections to Other Papers

Connects to Divide-and-Denoise, Spherical Watermark, diffusion safety/benchmark papers, and jailbreak/security evaluation through inference-time safeguards.

## Notes for Cross-Paper Synthesis

CRG strengthens the inference-time safety theme: model internals during generation can calibrate intervention more precisely than static prompt-level controls.
