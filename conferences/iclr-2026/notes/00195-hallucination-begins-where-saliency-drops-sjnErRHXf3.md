# Hallucination Begins Where Saliency Drops

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: sjnErRHXf3
- Authors: Xiaofeng Zhang; Yuanchao Zhu; Chaochen Gu; Xiaosong Yuan; Qiyan Zhao; Jiawei Cao; Feilong Tang; Sinan Fan; Yaomin Shen; Chen Shen; Hao Tang
- Primary area: foundation or frontier models, including LLMs
- Keywords: LVLMs-Saliency; Saliency-Guided Rejection Sampling;  Local Coherence Reinforcement; Hallucination
- Source URL: https://openreview.net/forum?id=sjnErRHXf3
- PDF URL: https://openreview.net/pdf?id=sjnErRHXf3

## Abstract

Recent studies have investigated attention dynamics in large vision language models (LVLMs), yet existing methods remain limited in reliably distinguishing hallucinated from correct outputs — primarily because they rely solely on forward-pass attention, ignoring gradient-based signals that reveal how token influence propagates through the model. To bridge this gap, we introduce \textbf{LVLMs-Saliency}, an \textit{gradient-aware diagnostic tool} that quantifies the grounding strength of each output token by fusing attention weights with their gradients. Through analysis, we identify a decisive pattern: \textit{Hallucinations occur when prior output tokens shows low saliency to the next token prediction}, indicating a failure of contextual memory. Building on this insight, we propose a dual-mechanism inference-time framework: (1) Saliency-Guided Rejection Sampling (SGRS), which dynamically filters candidate tokens during decoding by rejecting those with saliency below a context-adaptive threshold, thereby preventing coherence-breaking tokens from entering the sequence; and (2) Local Coherence Reinforcement (LocoRE), a lightweight plug-and-play module that strengthens attention from the current token to its most recent outputs, actively counteracting the “forgetting” behavior identified by LVLMs-Saliency. Experimental results demonstrate that our method significantly reduces hallucinations across multiple LVLMs, offering a robust and interpretable solution to improve model reliability.

## One-Sentence Claim

LVLM hallucinations correlate with drops in gradient-aware token saliency, and saliency-guided decoding plus local coherence reinforcement can reduce hallucinated outputs.

## Problem

Attention-only analyses of LVLM hallucination may miss how token influence propagates through the model. Without a reliable diagnostic signal, inference-time interventions cannot easily distinguish grounded continuations from coherence-breaking hallucinated tokens.

## Core Contribution

The paper introduces LVLMs-Saliency, a gradient-aware diagnostic combining attention weights and gradients to quantify output-token grounding strength. It identifies low saliency from prior outputs as a hallucination pattern and proposes SGRS plus LocoRE to intervene during inference.

## Method

LVLMs-Saliency fuses forward attention with gradient information for each output token. Saliency-Guided Rejection Sampling filters candidate tokens whose saliency falls below a context-adaptive threshold, while Local Coherence Reinforcement strengthens attention from the current token to recent outputs to counteract contextual forgetting.

## Experiments and Evidence

The abstract reports significant hallucination reductions across multiple LVLMs, with the method positioned as robust and interpretable. The key analytical evidence is the observed link between low prior-token saliency and hallucination onset.

## Limits and Failure Modes

Gradient-aware saliency can be expensive and may not capture semantic grounding in all architectures. Rejecting low-saliency tokens may reduce diversity or overemphasize local coherence at the expense of global image grounding. Full-text review should check hallucination benchmarks, latency overhead, threshold tuning, model coverage, and whether saliency is causal or merely correlated.

## Deep Themes

- Gradient-aware diagnostics for LVLM reliability.
- Hallucination as contextual memory failure.
- Inference-time rejection and reinforcement.
- Interpretable decoding interventions.

## Subthemes

- Attention-gradient saliency fusion.
- Saliency-Guided Rejection Sampling.
- Local Coherence Reinforcement.
- Context-adaptive thresholds.
- LVLM grounding strength.

## Connections to Other Papers

Connects to visual symbolic mechanisms, Veritas, and hallucination/safety papers through mechanistic diagnostics, and to speculative/Prophet-style decoding work through inference-time token filtering.

## Notes for Cross-Paper Synthesis

This paper fits a broader interpretability-as-control pattern: diagnostics become useful when they drive an inference-time intervention, not only a post-hoc explanation.
