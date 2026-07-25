# ICML 2026 Spotlight Batch 061 Synthesis

## Scope

This synthesis covers ICML 2026 spotlight notes 301-305:

- Learning to Execute Graph Algorithms Exactly with Graph Neural Networks
- On the Optimization Trajectory of DeepWalk Embeddings
- Lottery Prior: Randomized Neural Compression for Zero-Shot Inverse Problems
- Neural Feature Geometry Evolves as Discrete Ricci Flow
- Rethinking LLM Ensembling from the Perspective of Mixture Models

Source depth: abstract/metadata only for all five papers. ArXiv acquisition remains deferred after repeated rate-limit/service failures; these papers should be retried later from offset 300.

## Emerging Pattern 1: Exactness Comes From the Right Local Primitive

Exact GNN Algorithms reduces global graph algorithm execution to learning local node instructions, then iterating them as GNN updates. DeepWalk Trajectory similarly explains global cluster recovery through alignment with a low-rank spectral subspace during optimization.

Both papers show graph behavior becoming understandable when the right local or spectral primitive is isolated.

## Emerging Pattern 2: Optimization Paths Are Explanatory Objects

DeepWalk Trajectory analyzes what happens from random initialization, while Neural Ricci Flow tracks feature-graph geometry during training. These papers treat training dynamics as primary evidence, not just a route to a final model.

This connects to Diffract and PAVE, where adaptation and control behavior are understood through trajectories, fields, or subspaces.

## Emerging Pattern 3: Compact Priors Can Replace Large Learned Priors

Lottery Prior uses random lightweight networks and compression regularization for zero-shot inverse problems. It joins Brain Encoding Scale, FlashOptim, and SmoothSpike in challenging the assumption that larger or externally pretrained models are always necessary.

The shared condition is structure: compact methods work when the prior, representation, or compression objective matches the task.

## Emerging Pattern 4: Feature Geometry Has Dynamical Curvature

Neural Ricci Flow studies feature representations as geometric graphs evolving like discrete Ricci flow. Class separability appears with community structure, giving a geometry-level marker of learning.

This complements DIGL, language-symmetry geometry, and manifold-aware perturbations: geometry is not static representation decoration but an evolving mechanism.

## Emerging Pattern 5: Equivalent Sampling Can Be Much Cheaper

ME Ensemble samples the same ensemble distribution by choosing one model per token instead of evaluating all models. This is a probabilistic execution-order trick, similar in spirit to FlashSinkhorn's IO-aware reformulation.

## Cross-Batch Links

- Exact GNN Algorithms connects to Procedural Pretraining, WZ-LLM, ENGNN, DIGL, and graph algorithmic reasoning.
- DeepWalk Trajectory connects to DIGL, language-symmetry geometry, Diffract, and graph clustering papers through subspace emergence.
- Lottery Prior connects to Brain Encoding Scale, FlashOptim, Manifold Perturbations, and inverse/generative modeling papers through compact structured priors.
- Neural Ricci Flow connects to language-symmetry geometry, DIGL, ENGNN, and interpretability-as-geometry work.
- ME Ensemble connects to WeDLM, FlashSinkhorn, DLMR, TG-RAG, and token-routing papers through cheaper test-time execution.

## Deep Theme Update

Batch 061 is about making hidden structure explicit enough to exploit: graph algorithms reduce to local rules, DeepWalk dynamics align to spectral subspaces, inverse restoration uses compression priors, feature learning resembles curvature flow, and ensembling becomes a one-model-per-token mixture sampler.
