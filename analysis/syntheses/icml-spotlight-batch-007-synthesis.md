# ICML 2026 Spotlight Batch 007 Synthesis

Scope: ICML spotlight notes 31-35.

Source depth: full extracted arXiv text for Single-Head Attention in High Dimensions, CSPO, Linear Causal Representation Learning, and Alignment-Sensitive Minimax Rates; abstract/metadata only for SlaClip because no confident local PDF match is available yet.

## Papers Covered

- Single-Head Attention in High Dimensions: A Theory of Generalization, Weights Spectra, and Scaling Laws.
- CSPO: Constraint-Sensitive Policy Optimization for Safe Reinforcement Learning.
- SlaClip: Gradient Norm Slacks can be Indicator for Adaptive Clipping in DP-SGD.
- Linear Causal Representation Learning by Topological Ordering, Pruning, and Disentanglement.
- Alignment-Sensitive Minimax Rates for Spectral Algorithms with Learned Kernels.

## Emerging Pattern 1: Spectra Are Becoming a Unifying Language for Generalization

Single-Head Attention in High Dimensions and Alignment-Sensitive Minimax Rates both use spectral structure to explain when learned models generalize. The attention paper treats learned query-key spectra as a diagnostic of recovered target modes versus noisy finite-sample bulk. The minimax paper defines effective span dimension as a noise-calibrated measure of how well target signal aligns with a kernel's leading spectral span.

Together with the Jacobian-spectra and DiReCT papers, this suggests a strong field-level movement: learned spectra are not only artifacts to visualize, but objects that define sample complexity, optimization direction, and emergent scaling.

## Emerging Pattern 2: Adaptation Is Valuable When It Reuses Existing Signals

SlaClip adapts DP-SGD clipping from slack information already produced by standard clipping. CSPO adapts safe-RL updates from local constraint sensitivity already available in first-order constraint information. Alignment-Sensitive Minimax Rates frames feature learning as adapting spectral order so target signal occupies a smaller effective span.

The deeper commonality is low-overhead adaptation: use signals the training or optimization process already exposes, rather than adding separate expensive probes.

## Emerging Pattern 3: Safety Is About Recovery Trajectories, Not Only Satisfaction

CSPO explicitly evaluates time to safety, reward preservation during recovery, and violation frequency. This complements Pressure Reveals Character and Rare Event Analysis: behavior near the boundary matters. A system that eventually satisfies a constraint but oscillates through unsafe regions is not equivalent to one that recovers smoothly.

This is a useful cross-domain safety theme. LLM alignment, safe RL, and privacy-preserving training all need process-level diagnostics, not only final metrics.

## Emerging Pattern 4: Identifiability Is Moving From Interventions to Heterogeneity

Linear Causal Representation Learning tries to recover latent causal features without the strongest single-node intervention assumptions. It uses environment heterogeneity to infer topological ordering, prune causal effects, and disentangle features up to an equivalence class.

This connects to missing-data and multimodal papers: modern datasets are heterogeneous in ways that can either break assumptions or provide structure. The research move is to turn heterogeneity into an identifiability resource.

## Emerging Pattern 5: Theory Is Becoming More Architecture-Specific and Still Solvable

The attention-spectra paper does not analyze a generic black-box neural net; it builds a solvable high-dimensional attention model. The minimax paper does not rely on generic VC-style complexity; it defines a spectral target-kernel alignment quantity. CSPO uses the geometry of constraint boundaries rather than generic penalty tuning.

These papers share a pragmatic theoretical style: simplify enough to solve, but keep the simplification close to the mechanism that matters in current systems.

## Cross-Batch Links

- Single-Head Attention links with Why Deep Jacobian Spectra Separate, DiReCT, and Alignment-Sensitive Minimax Rates as a spectral-generalization cluster.
- CSPO links with Rare Event Analysis, Pressure Reveals Character, and SandboxEscapeBench through process-sensitive safety evaluation.
- SlaClip links with Gaussian certified unlearning and privacy papers through formal privacy constraints that still need practical utility.
- Linear CRL links with Base Models Know How to Reason and visual-symbolic mechanisms as interpretability work, but adds causal identifiability.
- Alignment-Sensitive Minimax Rates links with feature-learning and kernel-theory papers by reframing representation learning as reducing noise-relevant effective dimension.

## Subthemes to Track

- Attention spectral outliers.
- Sequential spectral recovery.
- Effective span dimension.
- Signal-kernel alignment.
- Safe-RL recovery metrics.
- Constraint-boundary geometry.
- DP-SGD adaptive clipping.
- Privacy-budget-neutral adaptation.
- Environment heterogeneity for causal identifiability.
- Latent causal features for model interpretability.
