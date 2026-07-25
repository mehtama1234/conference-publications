# ICML 2026 Spotlight Batch 088 Synthesis

Papers covered: 00436-00440.

## Batch Thesis

This batch is about the dynamics behind scalable decision systems. Ambiguity-averse MDPs characterize when epistemic uncertainty remains compatible with Bellman recursion; ScaleMoE shows that RL scaling needs conditional expert capacity; reasoning-loop analysis explains why inference-time chains get stuck; stochastic Transformer theory shows initialization noise prevents simplistic token collapse; and MoE pruning compresses expert models at channel granularity.

The common point is that behavior emerges from dynamics and structure: risk measures shape solvability, expert routing shapes RL scale, learning errors shape reasoning loops, stochastic initialization shapes token geometry, and attribution coverage shapes deployable MoE compression.

## Cross-Paper Themes

### 1. Scaling Needs the Right Decomposition

ScaleMoE and MoE pruning make this explicit from opposite directions. ScaleMoE adds experts to improve continuous-control capacity; MoE pruning removes redundant channels inside experts while preserving coverage. Together they show that MoE is not just "more parameters" but a decomposition problem.

WestWorld from the previous batch also fits this pattern: it routes trajectory prediction by system and morphology. Across control and language models, useful scaling comes from conditional specialization.

### 2. Dynamics Explain Failures That Static Metrics Hide

The reasoning-loop paper studies why long reasoning traces repeat instead of progress. The stochastic Transformer paper studies how tokens move across depth when random initialization is treated properly. The ambiguity-averse MDP paper studies which risk objectives can be recursively optimized.

All three papers argue that static snapshots are inadequate. To understand reliability, one must model the update process: decoding steps, layers, Bellman recursions, or learning dynamics.

### 3. Uncertainty Is Both a Modeling Target and an Algorithmic Constraint

Ambiguity-averse MDPs formalize epistemic uncertainty through random transitions and risk measures. Reasoning loops arise partly because the model places probability mass on easy cyclic actions under uncertainty about hard progress actions. Stochastic Transformer clustering shows that random initialization noise can preserve representational diversity.

The batch suggests a nuanced view: uncertainty is not always something to suppress. Some uncertainty must be represented and optimized under; some stochasticity is beneficial; some learned uncertainty produces pathological loops.

### 4. Efficiency Work Is Becoming Fine-Grained

MoE pruning moves below expert-level decisions to channel-level coverage. ScaleMoE studies expert count and gating placement. DHSA from the prior batch predicts sparsity at chunk and token levels. STAR-KV uses adaptive rank and quantization.

The pattern is a move from coarse compression to semantically or attribution-informed resource allocation.

## Deep Subthemes

### Bellman Compatibility as an Expressivity Limit

Dynamic programming is powerful only for objectives that decompose correctly over time. The ambiguity-averse MDP paper gives a clean version of a broader theme: modeling choices have algorithmic consequences.

### Expert Routing as RL Scaling

ScaleMoE shows that actor-critic RL may scale through conditional expert specialization rather than monolithic width. This gives continuous control a scaling primitive closer to modern large-model practice.

### Degenerate Reasoning Attractors

Looping is a failure mode of the inference process, not merely bad formatting. The graph-task analysis highlights cyclic attractors caused by learned error probabilities and temporally correlated Transformer mistakes.

### Noise-Preserved Representation Diversity

The stochastic Transformer paper revises deterministic collapse stories. Initialization noise can prevent single-cluster collapse and create richer attractor geometry, suggesting that stochastic details matter for representation theory.

### Coverage-Preserving Compression

MoE pruning reframes compression as retaining important channel coverage across routed experts. This is a more surgical view of efficiency than dropping modules wholesale.

## Common Pattern

The deepest common pattern is that the relevant object is often not the final model but the induced process: Bellman recursion under risk, expert routing during control, token choice during reasoning, token movement through depth, or channel coverage under pruning. ICML 2026 is repeatedly asking which processes are stable, scalable, and compressible.
