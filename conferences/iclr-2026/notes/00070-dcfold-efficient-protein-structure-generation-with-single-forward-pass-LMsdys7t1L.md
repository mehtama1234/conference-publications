# DCFold: Efficient Protein Structure Generation with Single Forward Pass

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: LMsdys7t1L
- Authors: Zhe Zhang; Yuanning Feng; Yuxuan Song; Keyue Qiu; Hao Zhou; Wei-Ying Ma
- Primary area: applications to physical sciences (physics, chemistry, biology, etc.)
- Keywords: consistency model;protein structure generation
- Source URL: https://openreview.net/forum?id=LMsdys7t1L
- PDF URL: https://openreview.net/pdf?id=LMsdys7t1L

## Abstract

AlphaFold3 introduces a diffusion-based architecture that elevates protein structure prediction to all-atom resolution with improved accuracy. This state-of-the-art performance has established AlphaFold3 as a foundation model for diverse generation and design tasks. However, its iterative design substantially increases inference time, limiting practical deployment in downstream settings such as virtual screening and protein design. We propose DCFold, a single-step generative model that attains AlphaFold3-level accuracy. Our Dual Consistency training framework, which incorporates a novel Temporal Geodesic Matching (TGM) scheduler, enables DCFold to achieve a 15× acceleration in inference while maintaining predictive fidelity. We validate its effectiveness across both structure prediction and binder design benchmarks.

## One-Sentence Claim

DCFold distills diffusion-style protein structure generation into a single-forward-pass consistency model while maintaining AlphaFold3-level accuracy.

## Problem

AlphaFold3-style diffusion models achieve strong all-atom protein structure prediction, but iterative sampling increases inference time.

That latency limits downstream workflows such as virtual screening and protein design, where many candidate structures may need to be generated or evaluated.

## Core Contribution

The paper proposes DCFold, a single-step generative model for efficient protein structure generation.

Its Dual Consistency training framework and Temporal Geodesic Matching scheduler are designed to preserve predictive fidelity while removing iterative inference.

## Method

DCFold uses consistency training to map inputs to high-quality structures in one forward pass. Dual Consistency appears to constrain the generation process so single-step outputs remain aligned with the iterative diffusion target.

Temporal Geodesic Matching shapes the training schedule along protein-structure trajectories, likely respecting geometric structure in the all-atom output space.

## Experiments and Evidence

The abstract reports AlphaFold3-level accuracy with 15x inference acceleration.

The paper validates DCFold on both structure prediction and binder design benchmarks, suggesting the speedup is useful for both predictive and generative protein workflows.

## Limits and Failure Modes

Single-step generation may lose calibration, diversity, or uncertainty signals that iterative diffusion provides. Protein design workflows may also need more than structure accuracy, including binding energetics, specificity, and wet-lab validity.

Because this note is abstract-only, details still need checking: input types, training targets, consistency losses, TGM definition, benchmark datasets, AlphaFold3 comparison protocol, and binder-design evaluation.

## Deep Themes

- Single-pass scientific generation: expensive iterative models are being compressed into deployable inference procedures.
- Consistency models for structure: diffusion-quality outputs can sometimes be approximated by direct generation.
- Geometry-aware training schedules: protein structure generation needs objectives that respect spatial trajectory structure.
- Throughput as scientific capability: faster structure generation changes what screening and design loops are practical.

## Subthemes

- Protein structure generation.
- Dual Consistency training.
- Temporal Geodesic Matching.
- Binder design acceleration.

## Connections to Other Papers

This connects to diffusion and flow acceleration work such as DFM Bounds and DivIn, but in a scientific-domain setting where inference speed has direct downstream value.

It also relates to TileLang, Mamba-3, and InfoTok through the larger pattern of converting expensive model families into efficient deployable systems.

## Notes for Cross-Paper Synthesis

DCFold adds a scientific-computing version of the efficiency theme: acceleration is not just serving optimization, but can expand the feasible search space for protein design.
