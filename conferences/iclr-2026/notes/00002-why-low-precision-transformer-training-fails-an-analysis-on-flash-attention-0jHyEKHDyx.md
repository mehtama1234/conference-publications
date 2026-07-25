# Why Low-Precision Transformer Training Fails: An Analysis on Flash Attention

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: 0jHyEKHDyx
- Authors: Haiquan Qiu; Quanming Yao
- Primary area: other topics in machine learning (i.e., none of the above)
- Keywords: low-precision training;transformer;attention
- Source URL: https://openreview.net/forum?id=0jHyEKHDyx
- PDF URL: https://openreview.net/pdf?id=0jHyEKHDyx

## Abstract

The pursuit of computational efficiency has driven the adoption of low-precision formats for training transformer models. However, this progress is often hindered by notorious training instabilities. This paper provides the first mechanistic explanation for a long-standing and unresolved failure case where training with flash attention in low-precision settings leads to catastrophic loss explosions. Our in-depth analysis reveals that the failure is not a random artifact but caused by two intertwined phenomena: the emergence of similar low-rank representations within the attention mechanism and the compounding effect of biased rounding errors inherent in low-precision arithmetic. We demonstrate how these factors create a vicious cycle of error accumulation that corrupts weight updates, ultimately derailing the training dynamics. To validate our findings, we introduce a minimal modification to the flash attention that mitigates the bias in rounding errors. This simple change stabilizes the training process, confirming our analysis and offering a practical solution to this persistent problem. Code is available at https://anonymous.4open.science/r/why-low-precision-training-fails.

## One-Sentence Claim

Low-precision transformer training with flash attention can fail because low-rank attention representations amplify biased rounding errors into catastrophic training instability, and a small rounding-bias mitigation stabilizes training.

## Problem

Low-precision training is essential for scaling transformers efficiently, but training can exhibit sudden loss explosions. The failure mode is known in practice but lacks a mechanistic account, making fixes ad hoc.

## Core Contribution

The paper gives a mechanistic explanation for a specific low-precision flash-attention failure mode and validates the explanation by introducing a minimal modification that reduces biased rounding errors.

## Method

The analysis traces training instability to two interacting causes: similar low-rank representations inside attention and biased rounding errors from low-precision arithmetic. The proposed intervention modifies flash attention to mitigate rounding bias.

## Experiments and Evidence

The abstract claims validation through a simple modification that stabilizes training, which is strong evidence if the PDF shows controlled ablations linking instability to representation rank and rounding bias. Key details to verify: formats tested, model scales, datasets, and whether the fix preserves speed.

## Limits and Failure Modes

Likely limits: the mechanism may be specific to certain low-precision formats, flash-attention implementations, architectures, or training regimes. The proposed fix may trade off throughput, numerical exactness, or hardware portability.

## Deep Themes

- Efficiency work is becoming mechanistic: failures are explained through training dynamics rather than treated as engineering quirks.
- Scaling depends on numerical systems choices, not only model architecture.
- Interpretability of optimization and hardware-level behavior is becoming part of ML research.

## Subthemes

- Low-precision training.
- Flash attention.
- Numerical instability.
- Error accumulation.
- Transformer training dynamics.

## Connections to Other Papers

Connects to the efficiency/compression cluster and to papers on transformer training under resource constraints. It pairs naturally with WASI because both target efficient transformer training, but at different layers: numerical kernels versus optimization subspaces.

## Notes for Cross-Paper Synthesis

This paper supports a common pattern: efficiency advances expose hidden assumptions in the training stack. When models are pushed into lower precision or smaller devices, numerical behavior becomes a first-order scientific object.

## Full-Text Upgrade

Source used: `conferences/iclr-2026/text/00002-why-low-precision-transformer-training-fails-an-analysis-on-flash-attention-0jHyEKHDyx-arxiv.txt`.

Additional verified details:

- The studied failure case is BF16 GPT-2 training with flash attention, where loss explosion originates in a specific early layer/head according to their debugging workflow.
- The paper narrows the source to the `PV` product in flash attention and the low-precision output term used in `delta = rowsum(dO * O)`.
- Two stabilization probes support this diagnosis: recomputing `PV` in FP32 during backward stabilizes training, and computing the attention output in FP32 during forward also restores stability.
- The mechanism depends on repeated or near-repeated maxima in a row of pre-softmax scores. Those maxima can create attention probabilities exactly equal to 1, which makes BF16 rounding bias systematic.
- Their proposed stabilized flash attention changes the row-wise softmax normalization constant only under repeated-maximum conditions, using a dynamic adjustment with beta in `[2, 8]`.
- The modification is mathematically equivalent to standard attention in exact arithmetic because it relies on softmax shift invariance, and it does not alter the backward pass.
- Validation includes GPT-2S pretraining for 600K steps in BF16 with AdamW and Muon optimizers, plus GPT-2M for 100K steps with AdamW.
- The discussion links attention sinks to numerical instability: sinks make probabilities of 1 more likely, which triggers the biased rounding pathway.

Refined limits:

- The authors state that the analysis focuses on a specific GPT-2 failure case.
- Generalization to other architectures, larger scales, and FP8 remains future work.
- The mitigation addresses the identified rounding error and may not cover unrelated numerical instability sources.
