# MrRoPE: Mixed-radix Rotary Position Embedding

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: 1J63FJYJKg
- Authors: Qingyuan Tian; Wenhong Zhu; Xiaoran Liu; Xiaofeng Wang; Rui Wang
- Primary area: generative models
- Keywords: transformers;nlp;llms;context window extension;attention;rotary embedding
- Source URL: https://openreview.net/forum?id=1J63FJYJKg
- PDF URL: https://openreview.net/pdf?id=1J63FJYJKg

## Abstract

Rotary Position Embedding (RoPE)-extension refers to modifying or generalizing the Rotary Position Embedding scheme to handle longer sequences than those encountered during pre-training. However, current extension strategies are highly diverse and lack a unified theoretical foundation. In this paper, we propose $\textbf{\textit{MrRoPE (Mixed-radix RoPE)}}$, a generalized encoding formulation based on a radix system conversion perspective, which elegantly unifies various RoPE-extension approaches as distinct radix conversion strategies. Based on this theory, we introduce two training-free extensions, $\textbf{\textit{MrRoPE-Uni}}$ and $\textbf{\textit{MrRoPE-Pro}}$, which leverage uniform and progressive radix conversion strategies, respectively, to achieve “train short, test long” generalization. Without fine-tuning, MrRoPE-Pro sustains over 85% recall in the 128K-context Needle-in-a-Haystack test and achieves more than double YaRN’s accuracy on Infinite-Bench retrieval and dialogue subsets. Theoretical analysis confirms that MrRoPE-Pro effectively raises the upper bound of RoPE's attainable encoding length, which further validates the reliability and utility of our theory and methodology.

## One-Sentence Claim

MrRoPE unifies RoPE context-extension methods as radix-conversion strategies and introduces training-free variants that substantially improve long-context generalization.

## Problem

LLMs need longer context windows than those seen during pretraining, but RoPE extension methods are fragmented and lack a shared theoretical explanation.

## Core Contribution

The paper reframes RoPE extension through mixed-radix encoding, deriving a unified theory and two training-free methods, MrRoPE-Uni and MrRoPE-Pro.

## Method

The method treats positional encoding extension as radix system conversion. MrRoPE-Uni uses uniform conversion, while MrRoPE-Pro uses progressive conversion to raise the attainable encoding-length upper bound without fine-tuning.

## Experiments and Evidence

The abstract reports more than 85% recall on 128K Needle-in-a-Haystack and more than double YaRN's accuracy on Infinite-Bench retrieval and dialogue subsets. Key checks for the PDF: baseline settings, context lengths, model families, degradation at shorter contexts, and computational overhead.

## Limits and Failure Modes

Possible limits include dependency on RoPE-based architectures, benchmark-specific gains, failures on tasks requiring dense reasoning over all context tokens, and unknown interaction with fine-tuning or retrieval augmentation.

## Deep Themes

- Long-context capability can be improved through encoding reinterpretation, not only model retraining.
- Test-time/generalization interventions increasingly target infrastructure around foundation models.
- Theory is used to unify a scattered engineering practice.

## Subthemes

- Context window extension.
- Positional encoding theory.
- Training-free adaptation.
- Retrieval and long-context evaluation.
- Transformer infrastructure.

## Connections to Other Papers

Connects to efficient adaptation, long-horizon reasoning, retrieval/memory, and evaluation papers. It should be compared with methods that extend context through retrieval, memory, compression, or training-time long-context data.

## Notes for Cross-Paper Synthesis

This paper is an example of a larger theme: frontier-model capability can be expanded by changing the computational interface around a pretrained model, avoiding the cost of full retraining.
