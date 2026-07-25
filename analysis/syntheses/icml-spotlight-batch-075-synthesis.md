# ICML 2026 Spotlight Batch 075 Synthesis

## Scope

This synthesis covers ICML 2026 spotlight notes 371-375:

- ReViT: Rotational-equivariant Vision Transformers for Neural PDE Solvers
- Asymmetric Perturbation in Solving Bilinear Saddle-Point Optimization
- One Intervention per Component is Enough: Towards Identifiability in Linear Stochastic Dynamics from Steady State
- On the Expressive Power of Permutation-Equivariant Weight-Space Networks
- Stable Deep Reinforcement Learning via Isotropic Gaussian Representations

Source depth: abstract/metadata only for all five papers. ArXiv acquisition remains deferred after repeated rate-limit/service failures; these papers should be retried later from offset 370.

## Emerging Pattern 1: Symmetry Is Becoming a Design Constraint Across Domains

ReViT enforces rotational equivariance for PDE fields. Weight-space networks enforce permutation equivariance over neural parameters. Symmetry ICL Dynamics and OENN/CENN from earlier batches use equivariance to make computation identifiable or universal.

The cross-paper theme is that symmetry is not decoration; it is a way to reduce sample complexity, improve generalization, and make learned computation compatible with the domain.

## Emerging Pattern 2: Dynamics Can Be Stabilized Without Changing the Target

Asymmetric perturbation changes one player's payoff to obtain linear last-iterate convergence while preserving an original-game equilibrium. Isotropic Gaussian regularization changes representation geometry to stabilize RL under non-stationary targets without replacing the RL objective.

Both papers modify the path of learning, not the desired endpoint.

## Emerging Pattern 3: Minimal Evidence Can Identify Complex Systems When Structure Is Right

The OU identifiability paper shows that one intervention per strongly connected component can recover linear stochastic dynamics from steady-state snapshots. This connects to finite-test certification, source screening, and weak-strong verification: structured evidence can substitute for exhaustive observation.

The important condition is placement. One intervention is enough only when it is placed according to the component graph.

## Emerging Pattern 4: Representation Geometry Is a Control Surface

ReViT uses canonical bases before attention. Weight-space networks operate on parameter tensors under permutation symmetries. Isotropic Gaussian RL shapes hidden-state distributions to prevent collapse and neuron dormancy.

The shared idea is that learning behavior is controlled by the geometry of the representation space, not only by loss functions.

## Emerging Pattern 5: Scientific and Sequential Domains Prefer Structure Over Generic Scale

PDE solvers, game optimization, causal dynamics, and RL stability all benefit from explicit mathematical structure. This batch strongly reinforces the theory-unifies-practice theme seen in LoRFS, Modern Conservation Laws, Jacobi Spectral Reconstruction, and Constrained Transformers.

## Cross-Batch Links

- ReViT connects to LoRFS, Dirac-Frenkel-Onsager dynamics, OENN/CENN, and Modern Conservation Laws.
- Asymmetric Perturbation connects to Mean-Expansion Q-Learning, Constrained Transformers, and optimization-dynamics papers.
- OU identifiability connects to Source Screening, Finite Test Certification, Noisy Sample Compression, and causal discovery themes.
- Weight-space expressivity connects to OENN/CENN, Context-Parameter Equivalence, Symmetry ICL Dynamics, and model-as-data themes.
- Isotropic Gaussian RL connects to Hista/Numca, Mean-Expansion Q-Learning, Fisher Memory Dynamics, and representation-shaping papers.

## Deep Theme Update

Batch 075 is a compact statement of the current corpus's strongest structural theme: equivariance, perturbation geometry, graph interventions, parameter-space symmetries, and isotropic embeddings all show that the right constraints make learning more stable, identifiable, and generalizable.
