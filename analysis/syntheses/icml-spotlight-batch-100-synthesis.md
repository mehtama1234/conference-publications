# ICML 2026 Spotlight Batch 100 Synthesis

Papers covered: 00496-00500.

## Batch Thesis

This batch is about aligning systems to the right objective under ambiguity, imbalance, or conflict. Alignment-guided score matching repairs text-image semantics without external rewards; NASH decomposes utility so Shapley data selection becomes informative; Bayesian hypergraphs reveal latent disease-risk pathways with uncertainty; DroneDINO routes detector capacity across heterogeneous drone sensing tasks; and RACO performs reward-free LLM alignment across conflicting objectives.

The common pattern is objective restructuring. Instead of accepting a blunt objective, each paper changes the optimization target so it better reflects the real decision: score-level alignment, componentwise data utility, pathway-level disease risk, modality-aware expert routing, or Pareto-aware preference updates.

## Cross-Paper Themes

### 1. Reward-Free Alignment Is Expanding

The diffusion alignment paper and RACO both avoid explicit reward models. One moves contrastive guidance into diffusion score matching; the other resolves conflicting preference gradients directly from pairwise data.

This reflects a broader skepticism about external rewards: when reward quality is uncertain or objectives conflict, aligning the native training objective may be cleaner.

### 2. Decomposition Makes Attribution and Selection Useful

NASH argues raw Data Shapley can fail because the target utility is not Shapley-informative. Decomposing utility into simpler components makes semivalue signals useful again.

The Bayesian hypergraph paper makes a similar structural move in medicine: instead of independent disease risks or black-box prediction, decompose risk into latent higher-order pathways.

### 3. Heterogeneity Requires Structured Routing

DroneDINO organizes experts into shared, task-specific, and dynamic groups to prevent dominant tasks from monopolizing capacity. This connects to ScaleMoE, WestWorld, FedARC, and embedding HMoE: heterogeneous domains need explicit mechanisms for both sharing and specialization.

### 4. Pareto and Tradeoff Thinking Are Becoming Central

RACO optimizes toward Pareto-critical points under user weights. MORetro* generates Pareto fronts for retrosynthesis. Fair OT exposes fairness-cost tradeoffs. The corpus increasingly treats single-objective optimization as an oversimplification.

## Deep Subthemes

### Score-Level Semantic Alignment

Text-image alignment can be injected into the diffusion denoising process rather than appended as a post-hoc reward. Counting accuracy becomes a concrete compositionality test.

### Shapley-Informative Utility Components

Data valuation becomes useful when utility is decomposed into components where semivalues carry stable signal. Nonlinear aggregation then selects better subsets.

### Bayesian Disease Pathways

Hyperedges represent latent disease subsets with shared risk factors, enabling overlapping pathways and calibrated uncertainty for rare outcomes.

### Heterogeneous Routed Detection

DroneDINO gives MoE experts semantic roles: shared across all inputs, exclusive to matching tasks, or dynamic per input. This counters data imbalance in unified drone detection.

### Conflict-Averse Preference Updates

RACO treats multi-objective alignment as gradient conflict resolution. Clipping and Pareto-critical convergence provide a geometry-aware alternative to reward-model scalarization.

## Common Pattern

The batch's shared lesson is that objective design is representation design. What the objective decomposes, routes, aligns, or constrains determines what the model can learn and what tradeoffs remain visible.
