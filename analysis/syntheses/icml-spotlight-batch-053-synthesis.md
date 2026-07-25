# ICML 2026 Spotlight Batch 053 Synthesis

## Scope

This synthesis covers ICML 2026 spotlight notes 261-265:

- A Distributional View for Visual Mechanistic Interpretability: KL-Minimal Soft-Constraint Principle
- Suppress and Diversify: Refining Robust Pathways for Corruption Robustness
- Neural Concept Verifier: Scaling Prover-Verifier Games via Concept Encodings
- Holi-Spatial: Evolving Video Streams into Holistic 3D Spatial Intelligence
- Manifold-Aware Perturbations for Constrained Generative Modeling

Source depth: abstract/metadata only for all five papers. ArXiv acquisition remains deferred after repeated rate-limit/service failures; these papers should be retried later from offset 260.

## Emerging Pattern 1: Interpretability Is Becoming a Constrained Inference Problem

KL-Minimal Visual MI frames feature visualization as posterior sampling under a natural-image prior and feature-activation constraints. Neural Concept Verifier routes image decisions through selected concept encodings and a verifier.

Both papers move beyond displaying explanations toward specifying an evidence-generating process with constraints: naturalness plus activation in one case, selected concepts plus verifier sufficiency in the other.

## Emerging Pattern 2: Robustness Is Moving Inside the Network

Suppress and Diversify studies internal computational pathways and finds robust-feature decay across layers. It then refines robustness by selecting and diversifying pathways while preserving symmetries.

This connects to DISCO, DOUBT, and Consistent Adversarial Attacks: robustness is increasingly treated as a property of internal dependencies, pathways, and evidence channels, not just a test-set number.

## Emerging Pattern 3: Scalable Supervision Pipelines Are Becoming Core Contributions

Holi-Spatial is primarily a data factory. It turns raw videos into 3DGS scenes, masks, 3D boxes, captions, grounding instances, and spatial QA at multi-million annotation scale.

This aligns with TerminalTraj, HypoSpace, and other corpus-building papers. Dataset construction is being treated as an algorithmic contribution because the supervision pipeline defines what future models can learn.

## Emerging Pattern 4: Geometry-Aware Smoothing Bridges Theory and Practice

Manifold-Aware Perturbations addresses singular equality-constrained data by making a constraint-aware distributional modification. The goal is to preserve manifold geometry while giving diffusion models and flows an ambient-dimensional training distribution.

This echoes ENGNN, RECM, PRISM, and Flowers: the intrinsic structure matters, but practical learning often needs a carefully designed ambient representation.

## Emerging Pattern 5: Explanation, Robustness, and Data Are Converging

Across the batch, the same design pattern appears in different forms: define the allowed evidence or distribution, then force the model or dataset to respect it. Visual MI constrains samples, S&D constrains robust pathways, NCV constrains decision evidence, Holi-Spatial constrains supervision generation, and manifold perturbations constrain noise around scientific data.

## Cross-Batch Links

- KL-Minimal Visual MI connects to Neuron-Basis Circuits, MDA, AI Engram, and DISCO through structured interpretability objectives.
- S&D connects to Consistent Adversarial Attacks, FeatJND, DOUBT, and DISCO through robust signal separation.
- NCV connects to Table-GLS, DLMR, SVGT, and value/module routing through constrained intermediate evidence.
- Holi-Spatial connects to AdLift, DLMR, TerminalTraj, and dataset-governance papers through large-scale structured supervision.
- Manifold Perturbations connects to Flowers, WLA/ERA5-Latent, TD3B, ENGNN, and RECM through intrinsic-geometry-aware model design.

## Deep Theme Update

Batch 053 emphasizes constrained evidence and constrained distributions. The papers do not merely ask models to perform better; they define the intermediate object that should carry meaning: a feature-conditioned image distribution, a robust pathway, a concept proof, a spatially reconstructed scene, or a manifold-aware perturbed distribution.
