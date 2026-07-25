# Catch-22: On the Fundamental Tradeoff Between Detectability and Robustness in LLM Watermarking

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 097IlaUfQY
- Authors: Kuheli Pratihar; Debdeep Mukhopadhyay
- Primary area: social_aspects->robustness
- Keywords: Watermarking;LLM;Undetectability;Information Leakage;Robustness
- Source URL: https://openreview.net/forum?id=097IlaUfQY
- PDF URL: https://openreview.net/pdf?id=097IlaUfQY

## Abstract

Large language models generate text by sampling tokens at random, a process now widely used for inference-time watermarking that verifies AI-generated content. We present an information-theoretic framework that captures the trade-off between robustness to text edits and detectability by observers who lack the watermark key or a keyless detector. The bounds we derive hold regardless of computational power, and what a keyless detector can actually achieve depends on what it can observe about the model and its outputs. At the heart of the analysis is an additive, Kullback-Leibler (KL) information measure that quantifies how well a hypothesis test can distinguish watermarked from unwatermarked text while the watermark remains stealthy. The measure remains zero for distribution-preserving schemes and increases with text length for token-level and sentence-level probability-modifying schemes. When edits are modeled as noise, the KL measure shrinks quadratically with the edit rate for token-level schemes and with an induced semantic flip rate for sentence-level schemes. This shrinkage exposes an unavoidable trilemma among robustness, stealth, and reliable verification. Guided by these limits, we propose a hybrid watermarking strategy that selects the Pareto-optimal scheme among distribution-preserving, semantic-level, and token-level methods based on the expected editing regime at deployment. Experiments on Llama-2-7B and Mistral-7B under paraphrasing attacks corroborate these theoretical predictions and confirm that the hybrid strategy lies near the Pareto frontier across the edit regimes we evaluate.

## One-Sentence Claim

LLM watermarking faces an information-theoretic trilemma: schemes cannot simultaneously maximize robustness to edits, stealth from keyless observers, and reliable verification.

## Problem

Inference-time watermarking aims to verify AI-generated text, but robust watermark signals can leak detectable information, while stealthy distribution-preserving schemes may be fragile under edits.

## Core Contribution

The paper develops an information-theoretic framework for the detectability-robustness tradeoff and proposes a hybrid watermarking strategy that chooses among distribution-preserving, semantic-level, and token-level schemes based on the expected editing regime.

## Method

The analysis uses an additive KL information measure to quantify how distinguishable watermarked text is from unwatermarked text under a hypothesis-testing view, then studies how edit noise reduces that measure for token-level and sentence-level schemes.

## Experiments and Evidence

The abstract reports experiments on Llama-2-7B and Mistral-7B under paraphrasing attacks, where the hybrid strategy lies near the Pareto frontier across evaluated edit regimes.

## Limits and Failure Modes

No arXiv/PDF match is currently local for this note. Checks needed: assumptions behind the edit-noise model, whether paraphrasing attacks cover realistic adversaries, and how detector observability assumptions affect the bounds.

## Deep Themes

- Safety mechanisms have unavoidable information-theoretic tradeoffs.
- Verification can conflict with stealth and robustness.
- Deployment regime should choose the watermarking method, not a universal default.

## Subthemes

- LLM watermarking.
- Detectability versus robustness.
- Information leakage.
- Keyless detection.
- Paraphrasing attacks.

## Connections to Other Papers

Connects to certified unlearning through hypothesis-testing style safety definitions, and to broader robustness/security papers where verification mechanisms create their own attack surfaces.

## Notes for Cross-Paper Synthesis

This adds a safety-pattern variant: some safety tools are constrained by fundamental tradeoffs, not just imperfect algorithms. The correct contribution may be characterizing the Pareto frontier rather than claiming one method dominates.
