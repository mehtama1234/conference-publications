# Skip a Layer or Loop It? Learning Program-of-Layers in LLMs

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: pl10b6EQAN
- Authors: Ziyue Li; Yang Li; Tianyi Zhou
- Primary area: deep_learning->large_language_models
- Keywords: Efficient Architecture;LLMs
- Source URL: https://openreview.net/forum?id=pl10b6EQAN
- PDF URL: https://openreview.net/pdf?id=pl10b6EQAN

## Abstract

Large language models (LLMs) perform inference by following a fixed depth and order, non-recurrent execution of all layers. We reveal the wide existence of training-free, flexible, dynamic *program-of-layers (PoLar)*, where pretrained layers can be packed as modules and then skipped or looped to form a customized program for each input. For most inputs, substantially shorter program executions can achieve the same or better accuracy, while incorrect predictions of the original LLM can be corrected by alternative programs with fewer layers. These observations indicate that inference admits multiple valid latent computations beyond the standard forward pass. To efficiently achieve PoLar in practice, we propose a lightweight PoLar prediction network, which learns to generate execution programs that dynamically skip or repeat pretrained layers for each input. Experiments on mathematical reasoning benchmarks demonstrate that PoLar consistently improves accuracy over standard inference and prior dynamic-depth methods, often while executing fewer layers, and that these gains persist under out-of-distribution evaluation. Our results suggest that fixed-depth execution captures only a narrow subset of an LLM’s latent reasoning capacity.

## One-Sentence Claim

Pretrained LLM layers can be dynamically skipped or repeated as input-specific programs, often improving reasoning accuracy while executing fewer layers than the standard fixed-depth forward pass.

## Problem

LLMs normally run every layer once in a fixed order, regardless of input difficulty. This assumes the pretrained network has only one valid computation path, even though different tasks or examples may need different depths or repeated transformations.

The paper questions whether fixed-depth inference underuses latent reasoning capacity. If alternative layer programs can correct wrong predictions with fewer layers, then standard inference is only one narrow execution policy over a richer modular network.

## Core Contribution

The paper reveals the existence of training-free flexible programs of layers, where pretrained layers are treated as modules that can be skipped or looped. It then proposes a lightweight PoLar prediction network that generates input-specific execution programs.

The contribution is to make layer execution itself dynamic. Instead of changing weights, prompts, or decoding, PoLar changes the computation graph traversed by each input.

## Method

PoLar packs pretrained layers as reusable modules and allows a program to skip layers or repeat selected layers. A lightweight predictor learns to choose these programs per input, targeting accuracy improvements and reduced execution depth.

The approach is training-free with respect to the base LLM weights. The learned component is the program predictor, which controls layer order/depth without modifying the pretrained layer parameters.

## Experiments and Evidence

The abstract reports mathematical reasoning experiments where PoLar consistently improves accuracy over standard inference and prior dynamic-depth methods, often with fewer executed layers. Gains persist under out-of-distribution evaluation.

It also reports that many inputs can achieve same-or-better accuracy with shorter programs, and some original LLM errors are corrected by alternative programs. Full-paper reading should verify model sizes, program search space, predictor training cost, and latency/accuracy tradeoffs.

## Limits and Failure Modes

Dynamic layer programs can introduce routing errors and unpredictable behavior if the predictor selects an unsuitable loop/skip pattern. Repeating layers may also create stability issues or distribution shifts in hidden states, especially outside the training regime.

Operational gains depend on whether program prediction overhead and irregular execution patterns map efficiently to hardware. The method may be less attractive if dynamic control flow harms batching.

## Deep Themes

- Inference as programmable computation: pretrained layers can be scheduled, not merely executed in order.
- Latent capacity beyond weights: capability may be unlocked by changing execution paths.
- Dynamic depth for reasoning: different inputs need different computational budgets and transformations.
- Weight-frozen adaptation: execution policy changes without base-model finetuning.

## Subthemes

- Skipping layers is not only compression; it can improve accuracy.
- Looping layers creates recurrent computation inside a nominally feed-forward Transformer.
- OOD gains suggest dynamic programs may capture robust alternatives to standard inference.
- Hardware efficiency depends on managing irregular layer execution.

## Connections to Other Papers

PoLar connects to DHSA, TabSwift, STAR-KV, and JitRL through dynamic inference-time control. DHSA changes attention sparsity, TabSwift changes depth, JitRL changes logits, and PoLar changes layer execution programs.

It also relates to reasoning-loop work, but with an important contrast: repeated text loops are pathological, while repeated layer modules can be useful when controlled by an execution program.

## Notes for Cross-Paper Synthesis

PoLar is a strong example of the corpus-wide move from static models to programmable inference. The model's weights are only one artifact; the execution schedule becomes a new optimization surface.
