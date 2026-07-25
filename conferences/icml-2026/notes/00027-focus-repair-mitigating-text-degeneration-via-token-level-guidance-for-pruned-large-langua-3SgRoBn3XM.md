# FOCUS & RePAIR: Mitigating Text Degeneration via Token-Level Guidance For Pruned Large Language Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 3SgRoBn3XM
- Authors: Junyoung Lee; Sehyeon Park; Shinhyoung Jang; Seonha Ryu; Hojeong Kim; Hyunsei Lee; Il hong Suh; Yeseong Kim
- Primary area: deep_learning->large_language_models
- Keywords: Large Language model;Text Degnertaion;Pruning;Distillation
- Source URL: https://openreview.net/forum?id=3SgRoBn3XM
- PDF URL: https://openreview.net/pdf?id=3SgRoBn3XM

## Abstract

Pruning is a practical approach to compress large language models (LLMs), but it can amplify text degeneration, especially repetition loops, even when perplexity and task accuracy remain largely unchanged. In this work, we present a token-level analysis of this failure mode by viewing decoding as a dynamical process that enters and persists in a small set of recurrent contexts. Our analysis decomposes degeneration into loop entry risk and loop persistence, and shows that persistence is controlled by the escape mass assigned to plausible alternatives within the token sampling set.
Motivated by these findings, we propose two token-level guidance objectives for post-pruning fine-tuning. FOCUS reweights distillation toward high-confidence teacher regions to suppress leakage, while RePAIR uses onset-centered positive/negative continuation pairs with a margin loss to promote plausible alternatives and prevent early commitment to repetition loops. Experiments on open-ended continuation and instruction-based generation show that both methods consistently reduce repetition and improve generation quality.

## One-Sentence Claim

FOCUS and RePAIR reduce repetition degeneration in pruned LLMs by targeting token-level loop entry and loop persistence during post-pruning fine-tuning.

## Problem

Pruning can compress LLMs while leaving perplexity and task accuracy mostly intact, yet still worsen open-ended generation quality through repetition loops and text degeneration.

## Core Contribution

The paper decomposes pruned-model degeneration into loop entry risk and loop persistence, then proposes two token-level guidance objectives designed to suppress repetition without relying only on aggregate perplexity.

## Method

FOCUS reweights distillation toward high-confidence teacher regions to reduce leakage. RePAIR constructs onset-centered positive/negative continuation pairs and uses a margin loss to increase plausible alternatives before the model commits to a repetition loop.

## Experiments and Evidence

The abstract reports consistent repetition reduction and improved generation quality on open-ended continuation and instruction-based generation.

## Limits and Failure Modes

No confident local PDF/arXiv match yet, so details still need checking: pruning method coverage, decoding settings, repetition metrics, tradeoffs with factuality/instruction following, and whether token-level guidance generalizes across model families.

## Deep Themes

- Compression can preserve benchmark accuracy while damaging generation dynamics.
- Token-level probability mass matters for qualitative behavior.
- Post-compression repair needs behavioral diagnostics, not only loss recovery.

## Subthemes

- LLM pruning.
- Text degeneration.
- Repetition loops.
- Distillation.
- Token-level guidance.
- Open-ended generation quality.

## Connections to Other Papers

Connects to LiftQuant and low-precision training papers as a compression/deployment risk paper. It also connects to Rare Event Analysis: low average degradation can hide problematic generation trajectories.

## Notes for Cross-Paper Synthesis

This paper adds a useful deployment theme: model compression should be evaluated as a dynamical behavior change, not only as a parameter-count or perplexity change.
