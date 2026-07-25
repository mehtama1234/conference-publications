# dnaHNet: A Scalable and Hierarchical Foundation Model for Genomic Sequence Learning

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 6pN2KNCspk
- Authors: Arnav Shah; Junzhe Li; Parsa Idehpour; Adibvafa Fallahpour; Brandon Wang; Sukjun Hwang; BO WANG; Patrick D Hsu; Hani Goodarzi; Albert Gu
- Primary area: applications->everything_else
- Keywords: Genomic foundation models;Scaling laws;Variant effect prediction;Gene Essentiality
- Source URL: https://openreview.net/forum?id=6pN2KNCspk
- PDF URL: https://openreview.net/pdf?id=6pN2KNCspk

## Abstract

Genomic foundation models have the potential to decode DNA syntax, yet face a fundamental tradeoff. Standard subword tokenizers fragment biologically meaningful motifs such as codons and regulatory elements, while nucleotide-level models preserve biological coherence but incur prohibitive computational costs for long contexts. We introduce dnaHNet, a state-of-the-art tokenizer-free autoregressive model that segments and models genomic sequences end to end. Using a differentiable dynamic chunking mechanism, dnaHNet compresses raw nucleotides into latent tokens adaptively, balancing compression with predictive accuracy. Pretrained on prokaryotic genomes, dnaHNet outperforms leading architectures including StripedHyena2 in scaling and efficiency. This recursive chunking yields quadratic FLOP reductions, enabling $>3 \times$ inference speedup over Transformers. On zero-shot tasks, dnaHNet achieves superior performance in predicting protein variant fitness and gene essentiality, while automatically discovering hierarchical biological structures without supervision. These results establish dnaHNet as a scalable, interpretable framework for next-generation genomic modeling.

## One-Sentence Claim

dnaHNet uses differentiable dynamic chunking to build a tokenizer-free hierarchical genomic foundation model that preserves biological motifs while reducing long-context cost.

## Problem

Genomic models face a tokenization tradeoff: subword tokenizers can fragment biologically meaningful motifs, while nucleotide-level modeling preserves structure but becomes too expensive for long sequences.

## Core Contribution

The paper introduces dnaHNet, a tokenizer-free autoregressive genomic model that adaptively compresses raw nucleotides into latent tokens through recursive differentiable chunking.

## Method

The model segments genomic sequences end to end, forming hierarchical latent chunks that balance compression and predictive accuracy without fixed subword tokenization.

## Experiments and Evidence

The abstract reports pretraining on prokaryotic genomes, better scaling and efficiency than leading architectures such as StripedHyena2, over 3x inference speedup over Transformers, and strong zero-shot variant-fitness and gene-essentiality prediction.

## Limits and Failure Modes

ArXiv searches for this batch hit HTTP 429, so no local PDF is available yet. Details still need checking: chunking objective, context lengths, pretraining corpus composition, downstream task splits, and interpretability evidence for discovered biological hierarchy.

## Deep Themes

- Scientific foundation models need tokenization that respects domain structure.
- Adaptive compression can preserve biological syntax while enabling long-context scaling.
- Hierarchical latent structure can support both efficiency and interpretability.

## Subthemes

- Genomic foundation models.
- Tokenizer-free sequence modeling.
- Dynamic chunking.
- Variant effect prediction.
- Gene essentiality.
- Biological hierarchy discovery.

## Connections to Other Papers

Connects to Mind-Omni, Protein Autoregressive Modeling, BioX-Bridge, and other scientific foundation-model papers. It also links to MrRoPE and long-context work through sequence-length efficiency.

## Notes for Cross-Paper Synthesis

dnaHNet strengthens the scientific-tokenization theme: effective foundation models for biology may need adaptive domain-native units rather than imported NLP tokenization assumptions.
