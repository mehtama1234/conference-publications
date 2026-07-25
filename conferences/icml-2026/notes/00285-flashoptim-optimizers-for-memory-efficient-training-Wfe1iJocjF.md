# FlashOptim: Optimizers for Memory-Efficient Training

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: Wfe1iJocjF
- Authors: Jose Javier Gonzalez Ortiz; Abhay Gupta; Christopher Rinard; Davis Blalock
- Primary area: deep_learning->everything_else
- Keywords: optimization;large scale training;compression;quantization;systems
- Source URL: https://openreview.net/forum?id=Wfe1iJocjF
- PDF URL: https://openreview.net/pdf?id=Wfe1iJocjF

## Abstract

Standard mixed-precision training of neural networks requires many bytes of accelerator memory for each model parameter. These bytes reflect not just the parameter itself, but also its gradient and one or more optimizer state variables. With each of these values typically requiring 4 bytes, training even a 7 billion parameter model can be impractical for researchers with less than 100\,GiB of accelerator memory. 

We introduce FlashOptim, a suite of optimizations that reduces per-parameter memory by over 50% while preserving model quality and API compatibility. Our approach introduces two key techniques. First, we improve master weight splitting by finding and exploiting a tight bound on its quantization error. Second, we design companding functions that greatly reduce the error in 8-bit optimizer state quantization. Together with 16-bit gradients, these techniques reduce AdamW memory from 16 bytes to 7 bytes per parameter, or 5 bytes with gradient release. They also cut model checkpoint sizes by more than half. 

Experiments with FlashOptim applied to SGD, AdamW, and Lion show no measurable quality degradation across a collection of standard vision and language benchmarks, including Llama-3.1-8B finetuning.

## One-Sentence Claim

FlashOptim reduces optimizer-state memory by over 50 percent through bounded master-weight splitting and companded 8-bit optimizer states while preserving API compatibility and model quality.

## Problem

Mixed-precision neural network training consumes substantial accelerator memory per parameter: parameter, gradient, and optimizer states often require about 16 bytes per parameter for AdamW. This makes even 7B-parameter training difficult for researchers without very large-memory accelerators.

The paper targets memory as the bottleneck limiting access to large-scale fine-tuning and training.

## Core Contribution

The paper introduces FlashOptim, a suite of optimizer memory reductions that keeps APIs compatible. Its two central techniques are:

- Improved master weight splitting using a tight bound on quantization error.
- Companding functions that reduce error in 8-bit optimizer state quantization.

Together with 16-bit gradients, FlashOptim reduces AdamW memory from 16 bytes to 7 bytes per parameter, or 5 bytes with gradient release, and cuts checkpoint sizes by more than half.

## Method

FlashOptim compresses the memory-heavy components of optimizers rather than changing the model architecture. Master weights are split more carefully under a quantization-error bound, and optimizer states are quantized with companding so limited 8-bit resolution is allocated where it matters most.

The methods are applied to SGD, AdamW, and Lion while preserving standard optimizer interfaces.

## Experiments and Evidence

Evidence reported in the abstract:

- More than 50 percent per-parameter memory reduction.
- AdamW reduced from 16 bytes to 7 bytes, or 5 bytes with gradient release.
- Checkpoint sizes cut by more than half.
- Experiments on SGD, AdamW, and Lion.
- No measurable quality degradation across standard vision and language benchmarks.
- Includes Llama-3.1-8B finetuning.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: benchmark list, training lengths, throughput impact, optimizer-state error analysis, and compatibility with distributed training.

## Limits and Failure Modes

- Memory savings may trade off with extra computation or kernel complexity.
- No measurable degradation on tested benchmarks does not guarantee stability for all training regimes.
- Quantized optimizer states can fail under unusual gradient distributions.
- Distributed optimizer sharding and mixed hardware support need full details.

## Deep Themes

**Memory is a first-class training bottleneck.** Reducing bytes per parameter changes who can fine-tune large models.

**Compression needs error geometry, not just fewer bits.** Tight bounds and companding make quantization usable for optimizer states.

**API compatibility accelerates adoption.** Systems methods matter more when they drop into existing training code.

## Subthemes

- Low-memory optimizer states.
- Master weight splitting.
- 8-bit companded optimizer quantization.
- Gradient release.
- Smaller checkpoints for large-model training.

## Connections to Other Papers

Connects to FlashSinkhorn, WBMM, WeDLM, SmoothSpike, and FeatJND through efficiency as capability enabler. It also links to PRISM and LoRA/privacy work because low-dimensional or compressed updates are becoming central to practical adaptation.

## Notes for Cross-Paper Synthesis

FlashOptim adds to the access theme: algorithmic capability is partly determined by memory format and optimizer state representation, not just model architecture or data.
