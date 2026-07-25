# ICML 2026 Spotlight Batch 084 Synthesis

## Scope

This synthesis covers ICML 2026 spotlight notes 416-420:

- Interpretable Functional Koopman Learning with Non-Markovian Closure for Spatiotemporal Systems
- LaST0: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model
- Fair Classification with Efficient and Post-hoc Controllable Fairness-Accuracy Trade-off
- DeCoDe: Decoupling Binding Position and Molecular Conformation in 3D Ligand Diffusion for Structure-Based Drug Design
- NorMuon: Making Muon more efficient and scalable

Source depth: abstract/metadata only for all five papers. ArXiv acquisition remains deferred after repeated rate-limit/service failures; these papers should be retried later from offset 415.

## Emerging Pattern 1: Reduced Representations Need the Missing Dynamics Back

MERLIN uses non-Markovian memory closure to compensate for information lost in low-dimensional Koopman representations. LaST0 uses latent spatio-temporal CoT to encode physical dynamics that language cannot express.

Both papers show that compression or abstraction works only if the omitted dynamics are handled explicitly.

## Emerging Pattern 2: Reasoning Format Should Match the Action Domain

PLAINTAIN made reasoning visible and early for human feedback. LaST0 keeps reasoning latent and low-frequency for robot control, where linguistic CoT would be too slow and lossy.

The cross-batch lesson is that "reasoning" is not one interface. It should be visible for user correction, latent for high-frequency embodiment, and formal for theorem solving.

## Emerging Pattern 3: Controllability Is a Deployment Requirement

The fair classification paper trains representations so post-processing can adjust fairness-accuracy tradeoffs after training. Fair Causal Bandits controls fairness online through causal constraints.

Together, they frame fairness as an operational control surface, not a single static constraint.

## Emerging Pattern 4: Generative Diffusion Benefits From Factorized Schedules

DeCoDe decouples ligand binding position and molecular conformation diffusion, mirroring MOG, KPE/KTS, and JustGRPO's broader message that generation trajectories should be structured rather than maximally unconstrained.

Physical design tasks need schedules aligned with domain factors.

## Emerging Pattern 5: Training Efficiency Is Update Geometry

NorMuon combines Muon's orthogonalized update geometry with neuron-wise adaptive normalization. OPUS selected data based on optimizer-induced update geometry. POET-X and QAT Scaling similarly shape training around mathematical structure.

The shared insight is that efficient training depends on controlling the geometry of parameter updates and their distribution across model components.

## Cross-Batch Links

- MERLIN connects to Walrus, LoRFS, ReViT, Generative Filtering, LASER, and Dirac-Frenkel-Onsager dynamics.
- LaST0 connects to EcoVLA, PACT, NeuronCtrl, MoCA, and PLAINTAIN.
- Post-hoc fair classification connects to Fair Causal Bandits, SCIQL, CreDRO, and fairness/robustness papers.
- DeCoDe connects to MOG, KPE/KTS, Tilt Matching, Weak Diffusion Priors, and protein/molecular generation work.
- NorMuon connects to OPUS, POET-X, QAT Scaling, WaterSIC, and LLM training-efficiency papers.

## Deep Theme Update

Batch 084 highlights matched abstractions: memory-closed Koopman states for PDEs, latent CoT for robotics, post-hoc fairness knobs for deployment, decoupled diffusion coordinates for drug design, and neuron-wise normalized updates for LLM optimization.
