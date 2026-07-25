# LiftQuant: Continuous Bit-Width LLM via Dimensional Lifting and Projection

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 1GvXUhLIMP
- Authors: Liulu He; Xuan Ang Liu; Juntao Liu; Taolue Feng; Ting Lu; Chunsheng Gan; ZHIYV PENG; Yuan Du; Huanrui Yang; Yijiang Liu; Li Du
- Primary area: deep_learning->large_language_models
- Keywords: Large language models;quantization
- Source URL: https://openreview.net/forum?id=1GvXUhLIMP
- PDF URL: https://openreview.net/pdf?id=1GvXUhLIMP

## Abstract

Existing quantization methods are fundamentally limited by rigid, integer-based bit-widths (e.g., 2, 3-bit), resulting in a "deployment gap" where Large Language Models cannot be optimally fitted to specific memory budgets. To bridge this gap, we introduce LiftQuant, a novel framework that enables continuous bit-width control for true Pareto-optimal deployment.  The core innovation is a "lift-then-project" mechanism which approximates low-dimensional weight vectors by projecting a simple 1-bit lattice from a higher-dimensional ``lifted" space.  Crucially, the effective bit-width is determined simply by the ratio of the lifted dimension to the original dimension, which allows the bit-width to be tuned quasi-continuous as the dimension is a flexible structural parameter. This projection generates a structured yet non-uniform codebook, capturing the expressive power of Vector Quantization (VQ).  While beneficial over VQ, LiftQuant's decoding path relies solely on linear transformations and 1-bit uniform quantizers, retaining hardware-friendly nature.  This flexibility is transformative: LiftQuant enables a 70B LLM to be compressed to 2.4 bits to precisely fit a 24GB GPU, where its performance significantly surpasses state-of-the-art 2-bit models fitted on the same device.  Our code and ckpt is available at \url{https://github.com/Heliulu/LiftQuant}.

## One-Sentence Claim

LiftQuant enables quasi-continuous LLM bit-width control by lifting weights into a higher-dimensional 1-bit lattice and projecting back to structured non-uniform codebooks.

## Problem

Integer bit-width quantization creates a deployment gap: a model may not fit a specific memory budget optimally because available choices like 2-bit or 3-bit are too coarse.

## Core Contribution

The paper proposes LiftQuant, a lift-then-project quantization framework where effective bit-width is controlled by the ratio between lifted and original dimensions, enabling fine-grained memory-performance tradeoffs.

## Method

Low-dimensional weight vectors are approximated by projecting simple 1-bit lattice points from a higher-dimensional lifted space. The projection yields a structured non-uniform codebook with vector-quantization-like expressivity while decoding through linear transformations and 1-bit uniform quantizers.

## Experiments and Evidence

The abstract reports compressing a 70B LLM to 2.4 bits to fit a 24GB GPU, with performance significantly surpassing state-of-the-art 2-bit models under the same device constraint.

## Limits and Failure Modes

Full-text checks needed: calibration cost, hardware kernels, latency overhead, model families, task coverage, and how continuous bit-width interacts with activation quantization.

## Deep Themes

- Efficiency is becoming budget-continuous rather than discrete.
- Deployment constraints motivate new mathematical parameterizations.
- Quantization is shifting from fixed formats to flexible codebook geometry.

## Subthemes

- LLM quantization.
- Continuous bit-width control.
- Vector quantization.
- Hardware-friendly compression.
- Memory-budget fitting.

## Connections to Other Papers

Connects to low-precision flash attention, WASI, and other efficiency papers. It is a deployment-side counterpart to training-side efficiency methods.

## Notes for Cross-Paper Synthesis

LiftQuant strengthens the theme that efficient ML is about fitting exact operational constraints, not only reducing average cost.

## Full-Text Upgrade

Source used: `conferences/icml-2026/text/00014-liftquant-continuous-bit-width-llm-via-dimensional-lifting-and-projection-1GvXUhLIMP-arxiv.txt`.

Additional verified details:

- The motivating deployment example is Llama-3-70B on a 24GB GPU: 3-bit is too large, while 2-bit fits but wastes accuracy relative to the available memory budget.
- LiftQuant decouples quantization rate from coding format: the effective bit-width is the lifted dimension/original dimension ratio.
- The method learns a global projection matrix that defines the fractional bit-width and codebook geometry.
- The projected codebook is described as dense and Gaussian-like, giving vector-quantization expressivity while retaining a linear-transform plus 1-bit quantizer decoding path.
- The paper focuses strategically on the 2-to-3-bit regime, where rigid integer choices most visibly create deployment gaps.
- Transformation parameters add small overhead per parameter under the 1.6-to-3-bit settings according to the extracted text.

Refined limits:

- Practical gains depend on efficient nearest-neighbor/quantization search and fused decoding kernels.
- At higher bit-widths, simpler group-wise approaches may already be near-lossless, so LiftQuant's main value is the aggressive low-bit deployment regime.
