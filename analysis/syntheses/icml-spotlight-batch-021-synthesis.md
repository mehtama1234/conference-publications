# ICML 2026 Spotlight Batch 021 Synthesis

## Scope

This synthesis covers ICML 2026 spotlight notes 101-105:

- Geometric and Stochastic Analysis of Discontinuities in Sparse Mixture-of-Experts
- Nash Equilibria in Games with Playerwise Concave Coupling Constraints: Existence and Computation
- Train for Truth, Keep the Skills: Binary Retrieval-Augmented Reward Mitigates Hallucinations
- Concept Removal Guidance: Evidence-Calibrated Negative Guidance for Safe Diffusion Sampling
- Jailbreak Foundry: From Papers to Runnable Attacks for Reproducible Benchmarking

Source depth: abstract/metadata only for all five papers. ArXiv acquisition remains deferred after repeated rate-limit/service failures; these papers should be retried later from offset 100.

## Emerging Pattern 1: Scalable Architectures Need Boundary Analysis

The sparse MoE paper shows that top-k routing, the mechanism that makes conditional computation efficient, also makes the model discontinuous. The paper's geometric and stochastic analysis asks where these discontinuity surfaces live, which ones are likely to be encountered under perturbation, and how local smoothing can repair the highest-risk boundaries.

This links to TetraJet-v2, SSO, and other training-stability papers. The recurring pattern is that scale-enabling tricks create new failure surfaces: routing discontinuities, outliers, oscillations, load imbalance, or quantization artifacts. These surfaces need their own theory and mitigation.

## Emerging Pattern 2: Game-Theoretic ML Is Moving Toward Real Constraints

The Nash-equilibrium paper studies games with shared coupling constraints and proves existence under playerwise concavity. For potential games, it gives a log-barrier gradient method with convergence to approximate constrained equilibria.

This connects to ParetoPO, non-cooperative LM safety games, debate-collapse work, and multi-agent optimization. The field is not only invoking game theory metaphorically; it is rebuilding equilibrium and learning tools for constrained strategic systems.

## Emerging Pattern 3: Factuality Rewards Are Being Designed Around Incentives

Binary RAR uses retrieved evidence but deliberately makes the reward binary: no contradictions gets 1, anything else gets 0. The key motivation is incentive design. Continuous factuality rewards can be hacked by saying less or becoming generic; a binary contradiction check is meant to reduce hallucinations without changing the distribution of error-free responses.

This links to DR Tulu, RGR-GRPO, and RLHF reward-hacking papers. The deeper theme is reward shape as behavioral control. More granular reward is not always better if it creates the wrong optimization pressure.

## Emerging Pattern 4: Diffusion Safety Is Becoming Evidence-Adaptive

Concept Removal Guidance adjusts negative guidance based on evidence from the denoising trajectory itself. Instead of a fixed suppression weight or prompt-similarity heuristic, it estimates unwanted concept presence from noise predictions and applies a constrained update to hit a target threshold with minimal perturbation.

This continues the inference-time safety thread from Divide-and-Denoise and watermark/safety papers. The key subtheme is calibrated intervention: safety controls should respond to what the model is actually generating, not just to the initial text prompt.

## Emerging Pattern 5: Security Evaluation Wants Executable Living Benchmarks

Jailbreak Foundry turns papers into runnable attacks and evaluates them in a shared harness. The system-level contribution is important: attack benchmarks drift because code, prompts, judges, and datasets differ. JBF tries to make the benchmark executable, reusable, and continuously extensible.

This connects to CyberGym, CVE Factory, DRPBench, and other executable evaluation efforts. Benchmarks are becoming software systems, not static datasets.

## Cross-Batch Links

- SMoE discontinuities, low-precision training, and floating-point theory all expose hidden numerical or geometric implementation issues.
- Constrained Nash equilibria, ParetoPO, and multi-agent debate work use game-theoretic tools under deployment constraints.
- Binary RAR, RGR-GRPO, DR Tulu, and reward-hacking mitigation papers treat reward design as incentive engineering.
- Concept Removal Guidance and Divide-and-Denoise both control diffusion sampling through adaptive inference-time mechanisms.
- Jailbreak Foundry, CyberGym, and Copyright-Bench make evaluation executable and workflow-realistic.

## Deep Theme Update

Batch 021 emphasizes that mature ML systems require infrastructure around the model: routing-boundary smoothing, constrained equilibrium computation, reward designs that resist hacking, generation-time safety controllers, and living security harnesses. The model's raw capability is not the whole system. The surrounding mathematical and software machinery increasingly determines whether the capability is reliable.
