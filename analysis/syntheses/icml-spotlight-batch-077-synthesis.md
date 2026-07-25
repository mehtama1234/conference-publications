# ICML 2026 Spotlight Batch 077 Synthesis

## Scope

This synthesis covers ICML 2026 spotlight notes 381-385:

- Advancing LLM Reasoning with Natural Language and Numerical Feedback
- Efficient Parallel Samplers for Recurrent-Depth Models and Their Connection to Diffusion Language Models
- Learning Randomized Reductions
- CONTINUUM: Restoring the Contiguous Tensor Abstraction Efficiently for Dynamic AI Workloads via Hardware Virtualization
- Beyond Theorem Proving: Formulation, Framework and Benchmark for Formal Problem-Solving

Source depth: abstract/metadata only for all five papers. ArXiv acquisition remains deferred after repeated rate-limit/service failures; these papers should be retried later from offset 380.

## Emerging Pattern 1: Feedback Is Becoming Multimodal and Process-Directed

Critique-GRPO combines numerical rewards with natural-language critiques so models learn from both failed initial responses and critique-guided refinements. RePO from the previous batch reframed preferences as regret-like counterfactual judgments.

The shared move is to make feedback describe a repair direction or comparative structure, not only success/failure.

## Emerging Pattern 2: Inference Computation Is Being Rescheduled, Not Just Scaled

The recurrent-depth sampler uses diffusion forcing to decode new tokens while refining latent states in parallel. This preserves recurrent depth but expands the token frontier updated per serial step.

This connects to KPE/KTS, BlitzRank, NAD, and other test-time scaling papers: better inference comes from scheduling computation around the structure of the task.

## Emerging Pattern 3: LLM Agents Are Proposal Engines Inside Verified Pipelines

Agentic Bitween uses LLM agents to propose query functions for randomized self-reduction discovery, while Formal Problem-Solving uses Lean obligations to verify constructed answers. In both cases, the model's role is not final authority; it proposes objects that a symbolic or formal layer checks.

This is a strong pattern for reliable automation: search with neural flexibility, certify with formal structure.

## Emerging Pattern 4: Infrastructure Abstractions Can Be Capability Bottlenecks

CONTINUUM argues that software-defined paging exposes fragmentation complexity and breaks the contiguous tensor abstraction. Its tensor virtualization layer reduces mapping latency and makes dynamic memory behavior easier to express.

This batch therefore links algorithmic capability to systems interface design: some future LLM algorithms may be blocked by memory abstractions, not only by model quality.

## Emerging Pattern 5: Formalization Moves From Verification to Construction

FPS shifts from checking known propositions to constructing unknown answers with proof obligations. This parallels Learning Randomized Reductions, where the system discovers reductions rather than only verifying supplied ones.

The broader direction is constructive reliability: models must synthesize the object and supply or pass a correctness check.

## Cross-Batch Links

- Critique-GRPO connects to RePO, Hista/Numca, PRISM, MoCA, and T2PO.
- Recurrent-depth parallel sampling connects to KPE/KTS, Distribution Transformers, Incremental BPE, NAD, and BlitzRank.
- Learning Randomized Reductions connects to Formal Problem-Solving, daVinci-Dev, 2-SAT Robustness, and finite-test certification.
- CONTINUUM connects to MACKO-SpMV, FlashSketch, POET-X, Incremental BPE, and other systems-efficiency work.
- Formal Problem-Solving connects to Weak-Strong Verification, Finite Test Certification, RePO/Critique-GRPO, and formal reasoning benchmarks.

## Deep Theme Update

Batch 077 emphasizes reliable construction under constraints: reasoning models need richer critique, recurrent models need better parallel schedules, agentic discovery needs formal verification, dynamic workloads need memory virtualization, and mathematical solvers need proof-carrying answers.
