# Towards Sub-Second Molecular Docking as a Structural Primitive: A Quantized Consistency Diffusion Framework

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: NyPHOtsJfE
- Authors: Kexin Zhang; Weichen Qin; Yue Teng; Jiale Yu; Yuanyuan Ma; Jinyu Lin; Liping Sun; Jie Zheng; Jingyi Yu
- Primary area: applications->chemistry_physics_and_earth_sciences
- Keywords: Molecular Docking;Diffusion Models;Consistency Regularization;Quantized Residual Learning;Scientific Digital Infrastructure
- Source URL: https://openreview.net/forum?id=NyPHOtsJfE
- PDF URL: https://openreview.net/pdf?id=NyPHOtsJfE

## Abstract

Agent-centered scientific discovery is turning scientific models into always-on computational infrastructure.
In this paradigm, AI agents coordinate tools, interpret feedback, and drive high-frequency research loops, requiring domain models that are both accurate and callable in real time.
Molecular docking exposes this bottleneck: it provides essential structural feedback for drug discovery, yet current high-fidelity docking and co-folding models remain limited by iterative generative refinement and heavy computation.
We present a compute-efficient co-folding framework that turns molecular docking into a sub-second structural primitive.
Because docking methods operate under different levels of structural prior, we report accuracy under information-level-matched protocols, comparing blind settings with blind generative methods and interface-informed settings with surface- or interface-informed baselines.
Our framework combines two ideas.
First, Progressive Consistency Regularization (PCR) compresses diffusion dynamics into reliable few-step inference through reconstruction-anchored consistency tuning.
Second, Residual-Safe Quantization preserves high-fidelity residual streams and geometry-sensitive operations in BF16 while quantizing selected compute-intensive linear transformations.
Our model achieves state-of-the-art docking accuracy under the matched interface-informed protocol, reports blind docking performance separately under the matched blind protocol, and generates five conformations for a representative 256-token complex in 0.17 seconds on a single NVIDIA H20 GPU, delivering a $>300\times$ speedup over AlphaFold3 under the benchmarked setting.
Together, these results move molecular docking from an offline generative simulator toward a real-time structural primitive for agent-centered drug discovery.

## One-Sentence Claim

The paper turns molecular docking into a sub-second structural primitive by compressing diffusion co-folding with consistency regularization and residual-safe quantization.

## Problem

Agent-centered drug discovery needs accurate structural feedback callable in real time, but high-fidelity docking and co-folding models remain too slow because of iterative generative refinement and heavy computation.

## Core Contribution

The paper introduces a quantized consistency diffusion framework with Progressive Consistency Regularization and Residual-Safe Quantization, evaluated under information-level-matched docking protocols.

## Method

PCR compresses diffusion dynamics into reliable few-step inference with reconstruction-anchored consistency tuning. Residual-Safe Quantization keeps high-fidelity residual streams and geometry-sensitive operations in BF16 while quantizing selected expensive linear transformations.

## Experiments and Evidence

The abstract reports state-of-the-art docking accuracy under matched interface-informed protocols, separate blind-protocol reporting, and five conformations for a representative 256-token complex in 0.17 seconds on one NVIDIA H20 GPU, more than 300x faster than AlphaFold3 under the benchmarked setting.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: dataset/protocol definitions, fairness of AlphaFold3 comparison, blind versus interface-informed accuracy, quantization error, hardware dependency, and wet-lab relevance.

## Deep Themes

- Scientific models are becoming real-time tools inside agent loops.
- Consistency compression can turn iterative diffusion into callable infrastructure.
- Quantization must preserve geometry-sensitive residual computations.

## Subthemes

- Molecular docking.
- Diffusion co-folding.
- Consistency regularization.
- Quantized residual learning.
- Drug discovery agents.
- Structural primitives.

## Connections to Other Papers

Connects to Chamaileon, FIRE, PWC-Diff, and AI-for-science infrastructure papers through scientific generative modeling under latency and fidelity constraints.

## Notes for Cross-Paper Synthesis

This paper adds a latency-critical science theme: for agents to use scientific models in high-frequency loops, accuracy alone is insufficient; the model must be fast enough to become a primitive operation.
