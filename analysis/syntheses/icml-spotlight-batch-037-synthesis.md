# ICML 2026 Spotlight Batch 037 Synthesis

## Scope

This synthesis covers ICML 2026 spotlight notes 181-185:

- How RL Unlocks the Aha Moment in Geometric Interleaved Reasoning
- Decomposed On-Policy Distillation for Vision-Language Reasoning: Steering Gradients for Visual Grounding
- NonZero: Interaction-Guided Exploration for Multi-Agent Monte Carlo Tree Search
- Keeping a Secret Requires a Good Memory: Unconditional Streaming Lower-Bounds for Differentially Private Algorithms
- Mixture of Concept Bottleneck Experts

Source depth: abstract/metadata only for all five papers. ArXiv acquisition remains deferred after repeated rate-limit/service failures; these papers should be retried later from offset 180.

## Emerging Pattern 1: Superficial Trace Matching Is Not Functional Alignment

Faire shows that SFT on interleaved plot-solution data can harm geometric reasoning because the model learns the visible trace format without internalizing the causal role of plots. RL constraints are used to make plotting function as an action that supports deduction.

This connects directly to TRM, CE-Graph, LALP, and SOAR. The reasoning cluster keeps converging on the same lesson: intermediate traces matter only when they are causally tied to better problem solving.

## Emerging Pattern 2: Multimodal Training Objectives Need Decomposition

VGS decomposes VLM distillation into language-prior and visual-grounding components and finds their gradients nearly orthogonal. The method then steers updates toward the visual subspace because grounding is treated as the bottleneck.

This mirrors AGREE's attribute-gradient conflict and FlowGuard's multimodal information decomposition. The broader pattern is that multimodal objectives hide separable subproblems, and training improves when those subproblems are made explicit.

## Emerging Pattern 3: Coordination Search Needs Interaction Signals

NonZero attacks multi-agent MCTS branching by proposing local deviations guided by single-agent gains and pairwise mixed differences. The important idea is that some coordinated improvements are invisible if each agent is evaluated alone.

This connects to compute-bounded RL and other test-time control papers. It adds a multi-agent version of efficient search: spend compute on candidate interactions likely to matter, not on exhaustive joint-action enumeration.

## Emerging Pattern 4: Privacy Has Fundamental Memory Costs

The streaming lower-bound paper proves unconditional space lower bounds for user-level DP algorithms and an exponential separation from non-private streaming estimators for distinct elements.

This complements IHM's algorithmic improvements for private regression. Together, the privacy papers map both sides of the frontier: better algorithms can reduce overhead in some settings, but lower bounds identify costs that cannot be optimized away.

## Emerging Pattern 5: Interpretability Needs Flexible Modular Explanations

M-CBE generalizes concept bottleneck models by allowing multiple concept-to-task expert expressions and variable functional forms, including symbolic regression with user-specified operators.

This connects to SSMoE and AGREE through expert/pathway decomposition, but with a user-facing interpretability aim. A single global concept rule may be too rigid; multiple simple expressions can better preserve both accuracy and legibility.

## Cross-Batch Links

- Faire, TRM, CE-Graph, LALP, and SOAR all evaluate or optimize reasoning as a functional process rather than a surface transcript.
- VGS, AGREE, and FlowGuard all decompose multimodal or subjective objectives into components that can be separately measured or steered.
- NonZero and compute-bounded RL treat inference/search budget as a controllable source of capability.
- The streaming lower-bound paper and IHM jointly define privacy's algorithmic frontier: achievable utility improvements versus unavoidable resource costs.
- M-CBE, SSMoE, and FlatLand all use mixtures or modular components to handle heterogeneity without collapsing into one global function.

## Deep Theme Update

Batch 037 is about replacing superficial alignment with functional structure. A plot must causally aid a proof, a distillation gradient must strengthen visual grounding, a search proposal must expose interaction, a privacy algorithm must respect memory lower bounds, and an explanation must adapt its functional form to the user and task.
