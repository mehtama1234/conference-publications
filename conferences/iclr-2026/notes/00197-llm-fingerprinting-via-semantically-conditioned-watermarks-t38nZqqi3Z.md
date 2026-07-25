# LLM Fingerprinting via Semantically Conditioned Watermarks

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: t38nZqqi3Z
- Authors: Thibaud Gloaguen; Robin Staab; Nikola Jovanović; Martin Vechev
- Primary area: alignment, fairness, safety, privacy, and societal considerations
- Keywords: LLM;Watermarks;Fingerprinting
- Source URL: https://openreview.net/forum?id=t38nZqqi3Z
- PDF URL: https://openreview.net/pdf?id=t38nZqqi3Z

## Abstract

Most LLM fingerprinting methods teach the model to respond to a few fixed queries with predefined atypical responses (keys). This memorization often does not survive common deployment steps such as finetuning or quantization, and such keys can be easily detected and filtered from LLM responses, ultimately breaking the fingerprint. To overcome these limitations we introduce *LLM fingerprinting via semantically conditioned watermarks*, replacing fixed query sets with a broad semantic domain, and replacing brittle atypical keys with a statistical watermarking signal diffused throughout each response. After teaching the model to watermark its responses only to prompts from a predetermined domain e.g., French language, the model owner can use queries from that domain to reliably detect the fingerprint and verify ownership. As we confirm in our thorough experimental evaluation, our fingerprint is both stealthy and robust to all common deployment scenarios.

## One-Sentence Claim

Semantically conditioned watermarks make LLM fingerprints more robust and stealthy by spreading a statistical signal across responses to prompts from a broad semantic domain instead of relying on fixed trigger queries.

## Problem

Fixed-query fingerprinting trains models to emit atypical key responses, but those keys can be detected, filtered, or destroyed by finetuning and quantization. Model owners need ownership verification that survives common deployment transformations without obvious trigger artifacts.

## Core Contribution

The paper introduces LLM fingerprinting via semantically conditioned watermarks: a model is trained to watermark responses only within a chosen semantic domain, letting owners query that domain and statistically detect the fingerprint.

## Method

Instead of memorizing predefined query-response pairs, the model learns a watermarking behavior conditioned on a broad semantic domain, such as a language domain. The watermark signal is diffused through generated responses and later detected statistically across owner-chosen prompts from that domain.

## Experiments and Evidence

The abstract reports thorough experiments showing the fingerprint is stealthy and robust across common deployment scenarios, including finetuning and quantization.

## Limits and Failure Modes

Semantic-domain triggers may affect user-facing behavior in that domain, and statistical detection must balance false positives with robustness. Attackers could target the domain if discovered. Full-text review should check watermark strength, detection power, ownership claims, domain choices, adaptive removal attacks, and utility impact.

## Deep Themes

- Robust model ownership verification.
- Semantic-domain conditioned watermarking.
- Statistical rather than memorized fingerprints.
- Deployment-resilient LLM provenance.

## Subthemes

- Stealthy fingerprint signals.
- Fine-tuning and quantization robustness.
- Broad semantic trigger domains.
- Watermark detection statistics.
- Model theft and provenance.

## Connections to Other Papers

Connects to watermarking tradeoff papers, LLM privacy/security benchmarks, and governance work where model provenance, ownership, and deployment robustness matter.

## Notes for Cross-Paper Synthesis

This paper turns fingerprinting from a brittle memorization trick into a distributional behavior over a semantic domain. It fits the broader move toward statistical, robust provenance signals.
