# ICML 2026 Spotlight Batch 005 Synthesis

Scope: ICML spotlight notes 21-25.

Source depth: full extracted arXiv text for Why Deep Jacobian Spectra Separate, h1, and ETTFS; abstract/metadata only for Robust Contextual Optimization with Missing Covariates and Language Generation in the Limit because no confident local PDF match is available yet.

## Papers Covered

- Why Deep Jacobian Spectra Separate: Depth-Induced Scaling and Singular-Vector Alignment.
- Robust Contextual Optimization with Missing Covariates.
- h1: Bootstrapping LLMs to Reason over Longer Horizons via Reinforcement Learning.
- Efficiently Training Time-to-First-Spike Spiking Neural Networks from Scratch.
- Language Generation in the Limit: Complexity Barriers and Implications for Learning.

## Emerging Pattern 1: Feasibility Is Replacing Possibility as the Theoretical Target

Why Deep Jacobian Spectra Separate and Language Generation in the Limit both ask whether high-level theoretical claims survive when made operational. The Jacobian paper looks for an analyzable approximation regime where nonlinear-network spectra behave like decoupled deep-linear dynamics. The language-generation paper argues that computable generation in the limit can still be infeasible once sample complexity is considered.

The shared move is from existence to usable mechanisms. It is no longer enough to say that learning or generation can happen; the field wants to know when the path is tractable.

## Emerging Pattern 2: Training Signal Must Be Preserved Across Depth, Horizon, or Sparsity

h1, ETTFS, and the Jacobian-spectra paper all study forms of signal degradation. h1 addresses reward sparsity over long reasoning horizons. ETTFS addresses signal diminishing and gradient vanishing under single-spike coding. The Jacobian paper studies spectral separation and alignment in deep products.

The common pattern is that scale creates structured signal problems: deeper networks, longer dependency chains, and sparser event codes each need mechanisms that keep useful gradients or update directions alive.

## Emerging Pattern 3: Robustness Starts at the Observation Process

Robust Contextual Optimization with Missing Covariates argues that missing features should be modeled directly in the decision problem rather than patched with imputation. This connects to LIMSSR's incomplete multimodal observations and to rare-event evaluation: real systems are not fed clean, complete, typical data.

The deeper theme is observation-aware modeling. Robustness depends on representing what was not observed, why it may be missing, and how that uncertainty should affect downstream choices.

## Emerging Pattern 4: Curricula and Constraints Are Becoming Core Design Objects

h1 uses a stagewise horizon curriculum to make outcome-only RL viable. ETTFS constrains architecture choices around single-spike coding, including rejecting max-pooling. DiReCT from the previous batch constrains sample selection through Hessian eigendirections.

Across these papers, the "method" is often a constraint system or training schedule. The model architecture matters, but the decisive design is how learning is staged, filtered, or restricted.

## Emerging Pattern 5: Hardware and Formal Structure Push Against Generic Deep Learning Recipes

ETTFS shows that neuromorphic efficiency requires TTFS-specific initialization, normalization, decoding, and pooling. Language Generation in the Limit shows that formal language classes can impose sample-complexity barriers independent of generic generative optimism. Robust Contextual Optimization shows that decision pipelines fail when real covariate structures violate full-observation assumptions.

These papers share a pragmatic lesson: generic recipes fail when the substrate has hard structure, whether that substrate is hardware, formal language, or missing-data decision systems.

## Cross-Batch Links

- Why Deep Jacobian Spectra Separate links with DiReCT through spectral geometry as a way to understand optimization.
- Robust Contextual Optimization links with LIMSSR through missing-data modeling and with deployment-focused robustness papers through partial-observation assumptions.
- h1 links with Base Models Know How to Reason, The Tell-Tale Norm, DMPO, and RAGEN-2 as another reasoning-RL paper focused on when training signal actually changes model behavior.
- ETTFS links with LiftQuant, low-precision transformer training, and resource-constrained transformer training as hardware-aware ML design.
- Language Generation in the Limit links with Transformer Circuits and HATSolver in the algorithmic/theory cluster, but contributes a negative feasibility lens.

## Subthemes to Track

- Depth-induced spectral separation.
- Singular-vector alignment.
- Missing-covariate robust optimization.
- Observation-aware decision-making.
- Long-horizon reasoning curricula.
- Outcome-only RL sample complexity.
- Time-to-first-spike direct training.
- Neuromorphic latency constraints.
- Computability versus feasible generation.
- Formal-language sample-complexity barriers.
