# ICML 2026 Spotlight Batch 079 Synthesis

## Scope

This synthesis covers ICML 2026 spotlight notes 391-395:

- Training-Free Bayesian Filtering with Generative Emulators
- Sharp Inequalities between Total Variation and Hellinger Distances for Gaussian Mixtures
- DPO Unchained: Your Training Algorithm is Secretly Disentangled in Human Choice Theory
- A Fully First-Order Layer for Differentiable Optimization
- Protein Fold Classification at Scale: Benchmarking and Pretraining

Source depth: abstract/metadata only for all five papers. ArXiv acquisition remains deferred after repeated rate-limit/service failures; these papers should be retried later from offset 390.

## Emerging Pattern 1: Learned Models Are Becoming Reusable Inference Machinery

Training-free Bayesian filtering uses diffusion-based dynamical emulators to implement particle-filter variants without extra training. DiScoFormer from the previous batches learns reusable density and score operators.

The pattern is that generative or Transformer models are being repurposed as components of inference algorithms, not just predictors or samplers.

## Emerging Pattern 2: Statistical Distance Geometry Still Matters

The Gaussian-mixture paper proves sharp TV-to-Hellinger inequalities, enabling entropic characterizations and robust-estimation consequences. This sits underneath many empirical uncertainty claims: distance choice determines learnability, robustness, and regret.

The broader corpus repeatedly uses distribution geometry, from CreDRO and Distribution Transformers to noisy sample compression and DiScoFormer.

## Emerging Pattern 3: Alignment Losses Need Normative Audits

DPO Unchained treats DPO and its extensions as choices inside a broad human-choice-theory framework. RePO similarly argues that preference feedback should be interpreted as regret-like and counterfactual.

Together, these papers move RLHF analysis away from "which loss works?" toward "what model of human judgment does this loss encode?"

## Emerging Pattern 4: Structured Solvers Need Cheap Differentiation

FFOLayer attacks the sensitivity bottleneck in differentiable optimization by replacing Hessian-heavy implicit differentiation with near-constant first-order hypergradients.

This connects to a broader structure-inside-model theme: optimization layers, constraints, and solvers become practical only when their gradients are computationally manageable.

## Emerging Pattern 5: Scientific Benchmarks Need Both Scale and Non-Redundancy

TEDBench targets protein fold classification with large-scale non-redundant structure data, while MiAE uses SE(3)-invariant masked autoencoding for scalable representation learning.

This mirrors the scientific-ML theme seen in ReViT and LoRFS: domain geometry and benchmark hygiene are as important as model size.

## Cross-Batch Links

- Bayesian filtering with generative emulators connects to DiScoFormer, Distribution Transformers, LASER, NeuronCtrl, and RMT diffusion theory.
- Gaussian-mixture inequalities connect to Noisy Sample Compression, CreDRO, robust distribution learning, and empirical Bayes themes.
- DPO Unchained connects to RePO, Critique-GRPO, PRISM, and Weak-Strong Verification.
- FFOLayer connects to Asymmetric Perturbation, Constrained Transformers, FlowOptimizer, and differentiable solver work.
- TEDBench/MiAE connects to ReViT, LoRFS, NeuronCtrl, and scientific benchmark/data curation papers.

## Deep Theme Update

Batch 079 emphasizes foundations beneath practical systems: reusable generative inference, sharp statistical metrics, normative preference theory, first-order differentiable solvers, and non-redundant scientific benchmarks all make downstream ML claims more defensible.
