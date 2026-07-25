# ICML 2026 Spotlight Batch 038 Synthesis

## Scope

This synthesis covers ICML 2026 spotlight notes 186-190:

- Estimating Tail Risks in Language Model Output Distributions
- FIRE: Multi-Fidelity Regression with Distribution-Conditioned In-Context Learning Using Tabular Foundation Models
- Loss-Aware Distributionally Robust Optimization via Trainable Optimal Transport Ambiguity Sets
- The Power of Power Law: Asymmetry Enables Compositional Reasoning
- TideGS: Scalable Training of Over One Billion 3D Gaussian Splatting Primitives via Out-of-Core Optimization

Source depth: abstract/metadata only for all five papers. ArXiv acquisition remains deferred after repeated rate-limit/service failures; these papers should be retried later from offset 185.

## Emerging Pattern 1: Safety Evaluation Is Becoming Tail-Aware

The LLM tail-risk paper estimates the probability of harmful outputs for a given input by importance sampling from unsafe proposal models. The key deployment point is that billion-query systems need probabilities of rare bad completions, not only red-team prompt success rates.

This connects to FlowGuard, Copyright-Bench, and other safety evaluation papers. The shared movement is toward distributional risk estimation that captures rare but consequential behaviors.

## Emerging Pattern 2: Foundation Models Are Being Reused as In-Context Inference Engines

FIRE uses tabular foundation models for training-free multi-fidelity regression, conditioning high-fidelity correction on low-fidelity posterior predictive summaries. This turns a pretrained TFM into a Bayesian surrogate without retraining.

This links to SSMoE, SmartFed, and Top-W. A recurring theme is fixed-model leverage: if the right interface is supplied, pretrained systems can be repurposed for new inference or adaptation regimes.

## Emerging Pattern 3: Robustness Should Be Shaped by the Downstream Loss

Loss-aware OT-DRO learns ambiguity sets end to end rather than designing uncertainty sets before optimization. The claimed benefit is less conservative decisions while preserving distributional robustness.

This connects to data valuation and decision-focused learning papers. The corpus repeatedly argues that uncertainty, robustness, and selection mechanisms should be optimized for the decision they support, not specified generically.

## Emerging Pattern 4: Natural Imbalance Can Be a Useful Curriculum

The power-law paper challenges the instinct to uniformize long-tail data. It argues that power-law asymmetry lets models first learn frequent compositions, which then become stepping stones for rare compositional skills.

This links to Real-World Unsupervised Models and SOAR. Natural data distribution and curriculum design are both becoming explanations for why certain capabilities emerge.

## Emerging Pattern 5: Spatial Scale Depends on Systems-Aware Sparsity

TideGS scales 3D Gaussian Splatting to over one billion primitives by exploiting sparse camera-conditioned visibility and moving parameters across SSD, CPU, and GPU as a working set. This is not just hardware engineering; it changes the feasible representation scale.

This connects to VGGT-Motion, XR-1, and 3ViewSense. Spatial intelligence depends on geometry, but also on memory hierarchy and dataflow when scenes become large.

## Cross-Batch Links

- Tail-risk estimation, ATLAS, Prescriptive Scaling, and MemoryBench all make evaluation more targeted to deployment realities.
- FIRE, SSMoE, and SmartFed all reuse fixed pretrained structure rather than retraining from scratch.
- Loss-aware OT-DRO and data-valuation papers make selection/uncertainty mechanisms downstream-objective-aware.
- Power-law compositional reasoning and Real-World Unsupervised Models both argue that natural data distributions are useful inductive biases.
- TideGS, VGGT-Motion, XR-1, and 3ViewSense build the spatial/embodied stack from systems scaling up through geometric reasoning and action.

## Deep Theme Update

Batch 038 emphasizes that practical ML progress often comes from respecting the real shape of the problem: rare safety failures, imbalanced fidelity levels, loss-specific uncertainty, power-law data, and sparse spatial working sets. The common pattern is to exploit structure in the operating distribution rather than flatten it into a generic training or evaluation procedure.
