# ICML 2026 Spotlight Batch 018 Synthesis

## Scope

This synthesis covers ICML 2026 spotlight notes 86-90:

- PhenoBrain: Phenotype-Conditioned Long-Range Communication for Multi-Modal Brain Network Analysis
- S3GNN: Efficient Global Mixing and Local Message Passing for Long-Range Graph Learning
- Skill-Pro: Learning Reusable Skills from Experience via Non-Parametric PPO for LLM Agents
- Towards Pareto-Optimal Tool-Integrated Agents with Pareto Ranking Policy Optimization
- CAT-Q: Cost-efficient and Accurate Ternary Quantization for LLMs

Source depth: abstract/metadata only for all five papers. ArXiv acquisition was deferred in this turn after repeated 429/503 failures across the previous three exact-batch attempts; these papers should be retried later from offset 85.

## Emerging Pattern 1: Graph Learning Is Becoming Context-Conditioned and Long-Range

PhenoBrain and S3GNN both address long-range communication, but in different domains. PhenoBrain argues that phenotype information should condition how brain networks communicate, because the same connectome pattern may carry different clinical meaning under different subject contexts. S3GNN tackles oversquashing in long-range graph learning by mixing global spectral information with local message passing under more practical assumptions.

Together they extend a graph-learning theme already visible in HyperDepth and spectral/geometry papers: graph models need to preserve structure across distance, hierarchy, and context. The key subtheme is not just "better message passing"; it is selective communication shaped by the semantics of the domain.

## Emerging Pattern 2: Agent Memory Is Becoming Executable

Skill-Pro turns episodic narratives into executable skills with activation, execution, and termination conditions. That is more concrete than storing summaries of past experience. A stored skill must know when it applies, what to do, and when to stop.

This links to RoboMME's robotic memory taxonomy, DR Tulu's evolving rubrics, and test-time discovery systems. Across the agent papers, memory is becoming operational: reusable procedures, rubrics, tool trajectories, and learned skills are treated as durable artifacts that guide future behavior.

## Emerging Pattern 3: Agent Alignment Is Multi-Objective

ParetoPO argues that tool-integrated agents should not optimize only task accuracy. Tool-use efficiency is also a deployment objective, and scalar reward weights can hide important tradeoffs. Pareto-ranking policy optimization instead promotes nondominated trajectories and uses Pareto progress to adapt training.

This expands the alignment theme beyond harmlessness or preference matching. For deployed agents, alignment also means respecting cost, latency, tool budget, and other operational constraints. The natural target is a frontier, not a single scalar optimum.

## Emerging Pattern 4: Compression Is Moving Toward Post-Training Conversion at Extreme Scale

CAT-Q targets ternary LLM quantization without expensive quantization-aware training. Its combination of learnable modulation and softened ternarization is positioned as a small-calibration, post-training route to compress models from 1.7B up to 235B parameters.

This connects to TetraJet-v2, LiftQuant, OmniFit, TACO, and EcoVLA. The shared direction is aggressive efficiency work that preserves enough capability to make deployment realistic. CAT-Q specifically emphasizes the cost of the compression process itself: compression is less useful if it requires massive retraining.

## Emerging Pattern 5: The Batch Repeats a Division-of-Labor Motif

Each paper splits a system into roles:

- PhenoBrain separates phenotype-conditioned routing from prediction.
- S3GNN separates global spectral mixing from local message passing.
- Skill-Pro separates episodic experience from executable procedural memory.
- ParetoPO separates competing objectives and uses Pareto structure to coordinate them.
- CAT-Q separates modulation of pretrained weights from the ternarization transition.

This division-of-labor pattern has appeared repeatedly in ICML 2026: hybrid sequence layers, shared-spine FL, nested multimodal learning, cloud-edge video reasoning, and runtime pruning all use structure to avoid forcing one mechanism to solve every constraint.

## Cross-Batch Links

- PhenoBrain, S3GNN, HyperDepth, and LOES show spectral/geometric structure becoming central to graph and representation learning.
- Skill-Pro, DR Tulu, TTT-Discover, and Neural Thickets treat adaptation as a reusable or searchable process around a pretrained model.
- ParetoPO, Copyright-Bench, and Pressure Reveals Character expand agent evaluation to deployment tradeoffs and pressure-sensitive behavior.
- CAT-Q, TetraJet-v2, LiftQuant, and floating-point theory build the low-precision/implementation-aware cluster.

## Deep Theme Update

Batch 018 reinforces a cross-corpus idea: practical ML systems increasingly require structured control surfaces. Graphs need conditioned routing, agents need executable memories and Pareto objectives, and LLM deployment needs post-training numerical conversion. The work is not just making models larger or smaller; it is giving systems explicit handles for context, memory, objectives, and representation cost.
