# Every Language Model Has a Forgery-Resistant Signature

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: vLFqOoMBol
- Authors: Matthew Finlayson; Xiang Ren; Swabha Swayamdipta
- Primary area: alignment, fairness, safety, privacy, and societal considerations
- Keywords: fingerprint;watermark;language model;signature;accountability;cryptography;forgery;security
- Source URL: https://openreview.net/forum?id=vLFqOoMBol
- PDF URL: https://openreview.net/pdf?id=vLFqOoMBol

## Abstract

The ubiquity of closed-weight language models with public-facing APIs has generated interest in forensic methods, both for extracting hidden model details (e.g., parameters) and identifying models by their outputs. One successful approach to these goals has been to exploit the geometric constraints imposed by the language model architecture and parameters. In this work, we show that a lesser-known geometric constraint—namely that language model outputs lie on the surface of a high-dimensional ellipse—functions as a signature for the model, which be used to identify which model an output came from. This ellipse signature has unique properties that distinguish it from existing model-output association methods like language model watermarks. In particular, the signature is hard to forge: without direct access to model parameters, it is practically infeasible to produce logprobs on the ellipse. Secondly, the signature is naturally occurring, since all language models have these elliptical constraints. Thirdly, the signature is self-contained, in that it is detectable without access to the model input or full weights. Finally, the signature is exceptionally redundant, as it is independently detectable in every single logprob output from the model. We evaluate a novel technique for extracting the ellipse on small models, and discuss the practical hurdles that make it infeasible for production-size models, making the signature hard to forge. Finally, we use ellipse signatures to propose a protocol for language model output verification, which is analogous to cryptographic symmetric-key message authentication systems.

## One-Sentence Claim

Language-model logprob outputs lie on a model-specific high-dimensional ellipse that can serve as a naturally occurring, self-contained, hard-to-forge signature for output verification.

## Problem

Closed-weight LLM APIs create forensic needs: identifying which model produced an output, proving provenance, and preventing forged attribution. Watermarks require model modification or prior embedding and can be removed or absent.

## Core Contribution

The paper identifies an elliptical geometric constraint in language-model outputs and frames it as a model-specific signature. It proposes using ellipse signatures for output verification analogous to symmetric-key message authentication.

## Method

The method analyzes the geometry imposed by model architecture and parameters on logprob outputs. It evaluates techniques for extracting the ellipse on small models and argues that extracting it for production-size models without parameter access is practically infeasible, making forgery difficult.

## Experiments and Evidence

The abstract reports evaluation of ellipse extraction on small models, discusses scaling hurdles for production-size models, and emphasizes four properties: hard to forge, naturally occurring, self-contained without inputs/full weights, and redundantly detectable in every logprob output.

## Limits and Failure Modes

Practical use may require access to logprobs, which many APIs restrict. The method's robustness to sampling, truncation, calibration, quantization, adapters, or logprob rounding needs inspection. Full-text review should check the ellipse derivation, extraction algorithms, verification protocol, false positives, and threat model.

## Deep Themes

- Natural model-output signatures.
- Geometry-based provenance.
- Forgery-resistant LLM verification.
- Cryptographic analogies for model accountability.

## Subthemes

- High-dimensional ellipse constraints.
- Logprob-output authentication.
- Self-contained signatures.
- Output provenance without watermarking.
- Practical hardness from production-scale extraction.

## Connections to Other Papers

Connects to semantically conditioned watermark fingerprints, watermarking tradeoff papers, and model-security/provenance work through ownership and output verification.

## Notes for Cross-Paper Synthesis

This paper complements watermarking by looking for signatures that already exist because of model geometry. Provenance may come from architecture-imposed constraints, not only explicit marking.
