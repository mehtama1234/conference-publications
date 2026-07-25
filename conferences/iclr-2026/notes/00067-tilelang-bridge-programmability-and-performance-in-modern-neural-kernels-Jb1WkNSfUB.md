# TileLang: Bridge Programmability and Performance in Modern Neural Kernels

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: Jb1WkNSfUB
- Authors: Lei Wang; Yu Cheng; Yining Shi; Zhiwen Mo; Zhengju Tang; Wenhao Xie; Tong Wu; Lingxiao Ma; Yuqing Xia; Jilong Xue; Fan Yang; Zhi Yang
- Primary area: infrastructure, software libraries, hardware, systems, etc.
- Keywords: compiler; AI; programming model
- Source URL: https://openreview.net/forum?id=Jb1WkNSfUB
- PDF URL: https://openreview.net/pdf?id=Jb1WkNSfUB

## Abstract

Modern AI algorithms increasingly adopt fused kernels for performance, but implementing them remains complex due to the lack of fine-grained control in existing compilers like Triton. We introduce TileLang, a controllable programming system for fused neural kernels. TileLang provides explicit tile-level primitives for memory placement, data movement, and parallel scheduling. To guide developers in hardware-aware programming, the TileLang introduces two key techniques: tile inference which models tile programs as fused graphs and automatically deduces tile configuration from partial annotations; and tile recommendation that suggests efficient tile configurations based on hardware profiles and heuristics. TileLang makes it easy to express a wide range of fused attention kernels in under 80 lines of Python code, reducing code size by up to 90% compared to manual implementations. Evaluations show that TileLang achieves up to 5x speedup over Triton on NVIDIA H100 and up to 6 on AMD GPUs, demonstrating its ability to bridge programmability and performance.

## One-Sentence Claim

TileLang bridges high-level programmability and hardware performance for fused neural kernels through explicit tile-level primitives plus automatic tile inference and recommendation.

## Problem

Modern AI systems rely heavily on fused kernels, especially for attention and other memory-bound operators. Hand-written kernels are fast but hard to maintain, while compiler systems such as Triton may not expose enough fine-grained control for newer fused patterns.

The bottleneck is developer productivity under hardware pressure: researchers need kernels that are easy to write, portable across accelerator families, and still close to manual performance.

## Core Contribution

The paper introduces TileLang, a programming system for fused neural kernels with explicit primitives for memory placement, data movement, and parallel scheduling.

Two key support mechanisms make the system practical: tile inference, which treats tile programs as fused graphs and infers configurations from partial annotations, and tile recommendation, which suggests efficient configurations using hardware profiles and heuristics.

## Method

TileLang exposes tile-level control in Python while automating parts of configuration search. Developers specify computation and selected tile constraints; the system infers missing tiling choices and recommends hardware-aware schedules.

This keeps the programming model closer to fused kernel intent than low-level manual code while preserving enough control to target GPUs effectively.

## Experiments and Evidence

The abstract reports that TileLang can express many fused attention kernels in under 80 lines of Python.

It reduces code size by up to 90 percent compared with manual implementations and achieves up to 5x speedup over Triton on NVIDIA H100 and up to 6x speedup on AMD GPUs.

## Limits and Failure Modes

The performance gains may depend on kernel family, hardware generation, and quality of the recommendation heuristics. More explicit control can also increase the burden on users who lack kernel expertise.

Because this note is abstract-only, details still need checking: supported operators, compilation backend, AMD/NVIDIA portability limits, benchmark baselines, autotuning cost, and how tile inference handles irregular kernels.

## Deep Themes

- Programmable performance: AI infrastructure needs systems that expose hardware control without forcing full manual kernel engineering.
- Tile as an abstraction boundary: explicit tiling becomes the level where memory, parallelism, and scheduling are coordinated.
- Compiler assistance for experts: automation helps fill partial annotations rather than hiding the full performance model.
- Cross-vendor acceleration: kernel systems increasingly need to cover multiple GPU ecosystems.

## Subthemes

- Fused attention kernels.
- Tile inference.
- Hardware-aware tile recommendation.
- Python DSL for neural kernels.

## Connections to Other Papers

This connects to Mamba-3, FlashVID, EntroKV, ThinkV, and InfoTok through the infrastructure layer of efficient AI: algorithmic wins matter only if they map well to hardware.

It also complements systems papers that treat serving and training efficiency as capability enablers rather than deployment afterthoughts.

## Notes for Cross-Paper Synthesis

TileLang strengthens the systems theme: 2026 efficiency work is as much about programmable kernels and memory movement as it is about model architecture.
