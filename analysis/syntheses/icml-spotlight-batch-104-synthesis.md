# ICML 2026 Spotlight Batch 104 Synthesis

## Papers

- PanoWorld-X: Generating Explorable Panoramic Worlds via Sphere-Aware Video Diffusion
- Delving into Muon and Beyond: Deep Analysis and Extensions
- Joint Learning in the Gaussian Single Index Model
- EntroKV: Entropy-Guided Dynamic Budget Allocation for KV-Cache Compression
- On the Sharp Input-Output Analysis of Nonlinear Systems under Adversarial Attacks

## Source Depth

All five notes are abstract/metadata-only. arXiv acquisition remains deferred after repeated 429/503 failures across preceding exact-batch attempts. Full-paper details should be verified when official PDFs or reliable arXiv matches become accessible.

## Shared Thesis

This batch is about matching methods to the structure of the underlying object: panoramic worlds need spherical geometry, optimizers need spectral update geometry, single-index learning needs low-dimensional Gaussian structure, long-context serving needs entropy-sensitive cache budgets, and nonlinear system identification needs adversarial sparsity assumptions.

The shared pattern is structure-aware control. Each paper gains either capability or theory by replacing a generic assumption with a sharper one: sphere rather than plane, spectral family rather than isolated optimizer, projection-plus-link rather than arbitrary high-dimensional regression, dynamic rather than uniform cache budgets, and sparse attacks rather than benign disturbances.

## Subthemes

### Geometry-aware world generation

PanoWorld-X argues that immersive 360-degree worlds cannot be treated as ordinary 2D videos. Panoramic representation, Plucker-style 3D motion guidance, and sphere-aware attention align the model's computation with the topology of the scene.

### Spectral optimizer understanding

The Muon analysis places orthogonalized updates inside a U Sigma^p V^T family. This changes the question from whether Muon is better than Adam to when spectral normalization stabilizes updates and when RMS-normalized adaptivity already provides the benefit.

### Tractable representation learning

The Gaussian single-index paper studies a narrow but fundamental representation-learning problem: jointly learn a projection and a scalar nonlinear function. The role of Gaussian regularity and information exponent gives a precise handle on nonconvex convergence.

### Entropy-guided serving memory

EntroKV uses attention entropy as a runtime proxy for compression sensitivity. This extends the corpus's resource-adaptive theme from compute routing to cache memory: not every attention head deserves the same retention budget.

### Sparse-adversary system identification

The nonlinear-system analysis shows that strong full-history adversaries can be handled if attack times are sufficiently sparse. Robustness is not free; it is possible under a quantitative condition on adversarial frequency.

## Cross-Batch Connections

PanoWorld-X connects to SplAttN and EgoTactile through geometry-aware multimodal inference, and to Beyond Language Modeling through world-modeling-oriented pretraining.

Muon connects to Adam degeneracy, SlaClip, and spectral theory papers by turning optimizer behavior into analyzable update geometry.

The Gaussian single-index paper connects to causal representation learning and alignment-sensitive spectral algorithms through provable recovery of structured low-dimensional representations.

EntroKV connects to FFCC, IO-aware GNNs, LiftQuant, and EcoVLA through the theme of adaptive resource allocation. It also links to Information Flow because both use internal model statistics to identify information-critical pathways.

The adversarial nonlinear-systems paper connects to robust contextual optimization, conformal policy control, and LAMP through dynamical-system reliability under uncertainty.

## Emerging Pattern

The larger pattern is that general-purpose modeling becomes more reliable when the system's geometry, spectrum, memory, or adversarial regime is made explicit. Generic flexibility gives way to targeted structure.
