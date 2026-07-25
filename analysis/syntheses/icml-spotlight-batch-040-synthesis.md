# ICML 2026 Spotlight Batch 040 Synthesis

## Scope

This synthesis covers ICML 2026 spotlight notes 196-200:

- Adaptive Policy Backbone via Shared Network
- VideoFlexTok: Flexible-Length Coarse-to-Fine Video Tokenization
- ECHO: Elastic Speculative Decoding with Sparse Gating for High-Concurrency Scenarios
- SWING: Unlocking Implicit Graph Representations for Graph Random Features
- Dynamic Stratified Contrastive Learning with Upstream Augmentation for MILP Branching

Source depth: abstract/metadata only for all five papers. ArXiv acquisition remains deferred after repeated rate-limit/service failures; these papers should be retried later from offset 195.

## Emerging Pattern 1: Adaptation Can Be Moved to Lightweight Interfaces

APB adapts only linear layers before and after a frozen policy backbone, yet reports performance competitive with standard RL and stronger OOD generalization. This resembles adapter-style thinking outside LLMs: constrain task-specific learning to a small interface around reusable structure.

This connects to LiME, SmartFed, CLEAR, and APB's RL neighbors. The broader pattern is that robustness may improve when the system is prevented from rewriting the whole policy or model.

## Emerging Pattern 2: Tokenization Is a Compute Allocation Policy

VideoFlexTok treats video tokens as a variable-length coarse-to-fine sequence rather than a fixed 3D grid. Early tokens capture semantics and motion, while later tokens add detail, allowing downstream generation to spend token budget according to content and task needs.

This links to long-context and multimodal representation papers. The corpus repeatedly shows that token structure sets the learning problem for the downstream model.

## Emerging Pattern 3: Production Inference Needs Load-Aware Algorithms

ECHO reframes speculative decoding for high-concurrency settings, where verification compute dominates. By managing a batch as a sparsely gated super-tree, it adapts depth and width under a serving budget.

This adds a deployment-systems layer to test-time scaling. The best inference procedure under single-request benchmarking may not be the best under industrial batch loads and kernel constraints.

## Emerging Pattern 4: Graph Computation Can Move Into Implicit Continuous Space

SWING avoids materializing implicit feature-defined graphs by performing walks in continuous embedding space, using random features, importance sampling, and a Gumbel-softmax mechanism.

This connects to Riemannian metric matching and other graph-free geometry papers. When graph structure is implicit in high-dimensional features, operating directly in that feature space can be more scalable than building the graph.

## Emerging Pattern 5: Learned Solvers Need Data Where Search Is Most Fragile

SC-MILP targets upstream branch-and-bound nodes, where decisions are high-leverage but samples are scarce. Dynamic stratified contrastive learning handles depth-dependent semantic variation, while augmentation generates equivalent and perturbed MILP instances.

This connects to decision-focused optimization and data-augmentation papers. It shows that solver learning benefits from shaping both representation and data distribution around compounding search decisions.

## Cross-Batch Links

- APB, LiME, SmartFed, and CLEAR all specialize fixed or shared cores with lightweight interfaces.
- VideoFlexTok, PoPE, and long-context sequence papers all show representation format strongly governs downstream compute and generalization.
- ECHO, Top-W, LiDAR, and compute-bounded RL all improve behavior through inference-time algorithms under explicit compute budgets.
- SWING, Riemannian metric matching, and graph-learning papers avoid expensive explicit structures by exploiting implicit geometry.
- SC-MILP, loss-aware OT-DRO, and graph-algorithm papers all put ML inside classical optimization pipelines while respecting solver structure.

## Deep Theme Update

Batch 040 emphasizes efficient control over where computation and adaptation happen: around a policy backbone, across video-token granularity, inside a speculative decoding schedule, within implicit graph feature space, or at upstream branch-and-bound nodes. The shared pattern is targeted resource allocation at the points where uniform processing would waste capacity or miss structure.
