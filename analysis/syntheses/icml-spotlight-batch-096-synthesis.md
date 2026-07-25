# ICML 2026 Spotlight Batch 096 Synthesis

Papers covered: 00476-00480.

## Batch Thesis

This batch is about learning where the real control variable is. DAWN shows residual RL efficiency depends on critic anchoring and scale-sensitive value representations; insertion-based generation learns generation order rather than assuming left-to-right construction; fair OT constrains group-pair probabilities in the transport plan; WIRE injects graph structure through spectral rotations; and DecodeShare identifies causal decode-time subspaces rather than relying on prefill representations.

The shared idea is that performance improves when the method targets the right latent degree of freedom: residual value scale, insertion trajectory, matching probabilities, graph spectral position, or decode-time decision channel.

## Cross-Paper Themes

### 1. Inference and Learning Protocols Need Alignment

Insertion Process aligns training with adaptive insertion orders. DecodeShare aligns interpretability with the decode phase of KV-cached inference. DAWN aligns critic training with residual-policy refinement around a frozen base policy.

All three reject a default protocol: left-to-right generation, prefill-only analysis, or generic critic initialization. The method must match the actual way the system is used.

### 2. Safety and Fairness Become Constraints on the Optimization Object

Conformal Policy Control from the prior batch calibrates policy deviation; this batch's fair OT paper constrains group-pair matching probabilities directly inside transport. Both make social or safety requirements native to the optimizer rather than external metrics.

The result is a tradeoff-aware system: fairness or safety can be exact, penalized, or calibrated, but it is visible in the objective.

### 3. Domain Geometry Defines Transformer Adaptation

WIRE extends RoPE to graph Laplacian spectra, recovering grid RoPE as a special case and preserving linear-attention compatibility. DecodeShare identifies geometry inside LLM hidden states. ConFlux and temporal graph explainability make similar domain-specific adaptations.

The corpus pattern is clear: as Transformer ideas migrate across domains, positional and representation geometry must be rebuilt for each domain.

### 4. Latent Order and Latent Subspace Are Emerging Control Surfaces

Insertion order and decode-time shared subspaces are not visible in final outputs, but they strongly affect generation quality and decisions. This aligns with PoLar, LatentMAS, and Assistant Axis: dynamic computation and latent representation are now explicit optimization targets.

## Deep Subthemes

### Residual Critic Anchoring

Residual RL depends on critic knowledge near the base policy. Base-policy transitions provide a local value anchor, and normalization restores sensitivity to bounded corrections.

### Variable-Length Insertion Generation

Insertion Process models where, what, and when to insert. This supports domains where no canonical left-to-right order exists and termination is part of generation.

### Group-Fair Transport

Fairness can be specified as target matching probabilities between groups. Exact Sinkhorn, penalized OT, and learned fair costs provide different points on the cost-fairness frontier.

### Spectral Graph RoPE

WIRE uses graph Laplacian waves to rotate tokens. The method imports RoPE's success into graphs without losing compatibility with efficient linear attention.

### Decode-Time Shared Channels

DecodeShare shows that compact hidden subspaces can causally drive decisions during decoding, and that prefill-derived steering signals can be unreliable proxies.

## Common Pattern

The batch's deepest common pattern is protocol-specific structure. Whether improving a residual policy, generating a sequence, matching groups, encoding graph positions, or steering an LLM, the method works by identifying the hidden structure that the default pipeline ignores.
