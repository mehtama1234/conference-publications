# ICML 2026 Spotlight Batch 045 Synthesis

## Scope

This synthesis covers ICML 2026 spotlight notes 221-225:

- Provably Convergent Actor-Critic for MARL through Risk-aversion
- Towards Sub-Second Molecular Docking as a Structural Primitive: A Quantized Consistency Diffusion Framework
- Jailbreak to Protect: Buffering and Reinforcing via Temporary Jailbreaking for Safe Fine-Tuning in Large Language Models
- $\tau^2$-Bench: Evaluating Conversational Agents in a Dual-Control Environment
- Updating Parametric Knowledge with Context Distillation Retains Post-Training Capabilities

Source depth: abstract/metadata only for all five papers. ArXiv acquisition remains deferred after repeated rate-limit/service failures; these papers should be retried later from offset 220.

## Emerging Pattern 1: Changing the Equilibrium Target Can Make MARL Learnable

The MARL paper uses risk-averse quantal response equilibria as a more regular solution concept for general-sum Markov games. This allows a single-timescale actor-critic method with global convergence and finite-sample guarantees.

This connects to NonZero and other multi-agent decision papers. The deeper pattern is that hard multi-agent learning problems may need different equilibrium notions, not only better optimizers.

## Emerging Pattern 2: Scientific Models Are Becoming Real-Time Agent Primitives

The molecular docking paper explicitly frames docking as a structural primitive for agent-centered drug discovery. Progressive consistency regularization and residual-safe quantization reduce diffusion co-folding to sub-second calls while preserving structural fidelity.

This extends Chamaileon, FIRE, and WLA/ERA5-Latent. AI-for-science work is moving from offline model quality to callable infrastructure that can sit inside automated research loops.

## Emerging Pattern 3: Safety Fine-Tuning Is Moving to Gradient-Level Control

Buffer-and-Reinforce uses temporary jailbreaking to saturate harmful safety-degrading gradients during user adaptation, then merges in a safety-reinforcing adapter. The defense is counterintuitive but fits the growing focus on internal update dynamics.

This connects to Robust Harmful Features, RLVepsR, GR-LoRA, and GEM. Safety is increasingly treated as a question of which gradients, heads, routes, or trajectories are allowed to control adaptation.

## Emerging Pattern 4: Conversational Agents Need Shared-World Evaluation

tau2-bench moves beyond single-control agent tests by letting both user and AI use tools in a dynamic environment. The performance drop in dual-control settings shows that guiding user action is a distinct capability from solving the task alone.

This connects to MEnvAgent and CE-Graph. Agent benchmarks are becoming more realistic by adding executable state, user simulation, compositional task generation, and error decomposition.

## Emerging Pattern 5: Knowledge Updates Must Preserve Post-Training Skills

DiSC updates parametric knowledge with split-context distillation while retaining instruction following, reasoning, and factual behavior. The core problem is not simply adding new facts, but doing so without erasing post-training capabilities.

This connects to MemoryBench, GR-LoRA, and Nevo-CRL. Continual learning for foundation models is becoming a maintenance problem: freshness, stability, and utility must be optimized together.

## Cross-Batch Links

- RQE actor-critic and NonZero both make multi-agent learning tractable through structure: equilibrium regularity in one case, interaction-guided search in the other.
- Sub-second docking, FIRE, WLA/ERA5-Latent, and TideGS all show scientific ML moving toward infrastructure primitives.
- Buffer-and-Reinforce, Robust Harmful Features, RLVepsR, and GR-LoRA all analyze adaptation at the level of internal signals and gradients.
- tau2-bench, MEnvAgent, CE-Graph, and MemoryBench all build benchmarks around executable or service-time process structure.
- DiSC, MemoryBench, GR-LoRA, and Nevo-CRL all address long-horizon retention under ongoing adaptation.

## Deep Theme Update

Batch 045 is about making advanced AI systems maintainable in active environments: multi-agent policies need learnable equilibria, scientific models need sub-second latency, fine-tuning needs safety buffers, agents need shared-world coordination tests, and LLMs need knowledge updates that preserve post-training skills. The common thread is not static capability, but reliable operation under repeated use and adaptation.
