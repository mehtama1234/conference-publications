# DAVE: Distribution-Aware Attribution via ViT Gradient Decomposition

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: ykTMNA6Mbh
- Authors: Adam Wróbel; Siddhartha Gairola; Jacek Tabor; Bernt Schiele; Bartosz Michał Zieliński; Dawid Damian Rymarczyk
- Primary area: social_aspects->accountability_transparency_and_interpretability
- Keywords: attributions;dynamic linearity;interpretability;explainable ai (xai);vision transformers
- Source URL: https://openreview.net/forum?id=ykTMNA6Mbh
- PDF URL: https://openreview.net/pdf?id=ykTMNA6Mbh

## Abstract

Vision Transformers (ViTs) have become a dominant architecture in computer vision, yet producing stable and high-resolution attribution maps remains challenging. Architectural components such as patch embeddings and attention routing often introduce structured artifacts in pixel-level explanations, leading many existing methods to rely on coarse patch-level attributions. We introduce DAVE (Distribution-Aware Attribution via ViT Gradient Decomposition), a mathematically grounded attribution method for ViTs based on a structured decomposition of the input gradient. By exploiting architectural properties of ViTs, DAVE isolates locally equivariant and stable components of the effective input-output mapping while suppressing architecture-induced artifacts and instability. Consequently, DAVE produces robust, precise, and class-consistent attribution maps that highlight model-relevant visual features. Experimental results show that across supervised, self-supervised, and inherently interpretable ViTs, DAVE outperforms prior methods on localization, faithfulness, and user studies.

## One-Sentence Claim

DAVE produces stable high-resolution ViT attribution maps by decomposing input gradients to isolate locally equivariant components and suppress architecture-induced artifacts.

## Problem

Vision Transformers are strong vision models, but pixel-level explanations are often unstable or contaminated by structured artifacts from patch embeddings and attention routing.

Because of these artifacts, many attribution methods retreat to coarse patch-level explanations, losing the spatial precision users need for localization and inspection.

## Core Contribution

The paper introduces DAVE, Distribution-Aware Attribution via ViT Gradient Decomposition, a mathematically grounded method for ViT attribution.

The core contribution is a structured decomposition of the input gradient that exploits ViT architecture to keep stable locally equivariant components of the effective input-output mapping while suppressing artifacts.

## Method

DAVE decomposes the input gradient into components tied to architectural behavior. It isolates the parts of the gradient that behave stably and locally with respect to the input distribution.

By filtering out artifact-prone components, it produces high-resolution class-consistent attribution maps rather than coarse patch maps.

## Experiments and Evidence

The abstract reports that DAVE outperforms prior methods across supervised, self-supervised, and inherently interpretable ViTs.

Evaluation covers localization, faithfulness, and user studies, suggesting the maps are both quantitatively and qualitatively better aligned with model-relevant visual features.

## Limits and Failure Modes

Gradient decompositions can still reflect local sensitivity rather than causal necessity, and attribution quality may depend on ViT architecture details.

Because this note is abstract-only, details still need checking: decomposition formula, distribution assumptions, ViT variants, localization datasets, faithfulness metrics, user-study design, and robustness under distribution shift.

## Deep Themes

- Architecture-aware interpretability: explanations must account for model-specific artifact sources.
- High-resolution attribution: interpretability should recover pixel-level evidence without patch-grid artifacts.
- Distribution-aware gradients: stable explanations depend on how gradients behave over data, not only one input.
- Faithfulness versus visual appeal: attribution methods need quantitative and human-facing validation.

## Subthemes

- ViT gradient decomposition.
- Locally equivariant explanation components.
- Suppression of patch and attention artifacts.
- Class-consistent attribution maps.

## Connections to Other Papers

This connects to Information Flow, Assistant Axis, and temporal graph memory explanation through internal-pathway interpretability. It also relates to Motion Attribution for Video Generation in the next stub window because both attempt attribution in modern visual architectures.

It belongs in the interpretability-as-intervention cluster, but with a vision-specific architectural focus.

## Notes for Cross-Paper Synthesis

DAVE reinforces the idea that explanation methods must be matched to architecture. Generic gradients can be misleading when the model's routing and tokenization create structured artifacts.
