# ICML 2026 Spotlight Batch 050 Synthesis

## Scope

This synthesis covers ICML 2026 spotlight notes 246-250:

- AdLift: Lifting Adversarial Perturbations to Safeguard 3D Gaussian Splatting Assets Against Instruction-Driven Editing
- Diffuse to Detect: Bi-Level Sample Rebalancing with Pseudo-Label Diffusion for Point-Supervised Infrared Small-Target Detection
- TD3B: Transition-Directed Discrete Diffusion for Allosteric Binder Generation
- Beyond Global Alignment: Fine-Grained Motion-Language Retrieval via Pyramidal Shapley-Taylor Learning
- Just Noticeable Difference Modeling for Deep Visual Features

Source depth: abstract/metadata only for all five papers. ArXiv acquisition remains deferred after repeated rate-limit/service failures; these papers should be retried later from offset 245.

## Emerging Pattern 1: Protection Moves Into the Representation

AdLift protects 3DGS assets by lifting bounded 2D adversarial perturbations into safeguard Gaussians. Protection is no longer only a watermark or image-space perturbation; it is embedded in the 3D neural asset itself so it can generalize across views.

This connects to TideGS, GEM, and DGS-Net. As generative and editable visual representations become assets, robustness and rights management need to operate at the representation level.

## Emerging Pattern 2: Weak Supervision Works Better With Physics

Diffuse to Detect expands point annotations into pseudo-masks using heat-diffusion structure, then jointly optimizes labels, sample weights, and detector parameters. It treats label generation as a physical and optimization problem rather than a generic weak-label heuristic.

This links to PWC-Diff and other physical-prior papers. Domain physics repeatedly improves learning when labels are sparse, noisy, or expensive.

## Emerging Pattern 3: Molecular Generation Needs Functional Directionality

TD3B targets allosteric binders that bias biological state transitions as agonists or antagonists. This goes beyond static affinity or equilibrium conformation matching.

This connects to Chamaileon and sub-second docking. Scientific generation is shifting toward functional constraints: what the molecule does to a system over time matters as much as where it binds.

## Emerging Pattern 4: Cross-Modal Alignment Is Becoming Fine-Grained and Hierarchical

PST motion-language retrieval decomposes motion into joints and temporal segments, then aligns those local structures with text tokens. This replaces global sequence-text matching with a pyramidal interaction model.

This connects to Table-GLS, 3ViewSense, XR-1, and VGS. Multimodal systems increasingly need intermediate structures that match the compositional structure of the domain.

## Emerging Pattern 5: Efficiency Needs Task-Aligned Tolerance Maps

FeatJND extends just-noticeable-difference thinking into deep feature space. Its key practical use is dynamic quantization: allocate noise/precision where downstream tasks can tolerate it.

This connects to WBMM, ECHO, and systems-efficiency papers. Efficient computation is becoming more selective: reduce cost where the task is insensitive, preserve precision where errors matter.

## Cross-Batch Links

- AdLift, GEM, FlowGuard, and DGS-Net all protect or verify generated visual content by intervening below the final rendered output.
- Diffuse to Detect, PWC-Diff, Modified SINNs, and Lagrangian Action use physical structure to stabilize learning under difficult observations.
- TD3B, Chamaileon, and sub-second docking move biomolecular generation toward function- and agent-oriented scientific workflows.
- PST, Table-GLS, 3ViewSense, and causal route gating all replace global multimodal alignment with structured local correspondences.
- FeatJND, WBMM, ECHO, and TideGS all show efficiency gains from knowing which computations or perturbations matter.

## Deep Theme Update

Batch 050 emphasizes task-specific tolerances and controls: protect the 3D representation, diffuse point labels according to thermal physics, generate molecules for transition direction, align motion at joint and segment granularity, and quantize visual features according to downstream tolerance. The common pattern is that effective systems know where precision, protection, or alignment is actually needed.
