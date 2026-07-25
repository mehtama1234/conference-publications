# ICML 2026 Spotlight Batch 017 Synthesis

## Scope

This synthesis covers ICML 2026 spotlight notes 81-85:

- Learning to Discover at Test Time
- DR Tulu: Reinforcement Learning with Evolving Rubrics for Deep Research
- On the Convergence Rate of LoRA Gradient Descent
- Think in Cloud, Look at Edges: Semantic-Driven Query Decomposition for Efficient Video Reasoning
- Thinking in Flow: A Dissipative Stabilization Operator for Robust Autoregressive Reasoning

Source depth: abstract/metadata only for all five papers. ArXiv search returned HTTP 429 responses for this batch and should be retried later.

## Emerging Pattern 1: Test-Time Scaling Is Becoming Test-Time Learning

TTT-Discover moves beyond frozen-model search. It performs reinforcement learning during the test-time attempt itself, optimizing for one exceptional solution to the current scientific or engineering problem. That is a sharper objective than average-task improvement: the model does not need to generalize broadly from the episode; it needs to discover something valuable in that episode.

This connects to Neural Thickets, Skill-Pro, Pareto tool agents, and broader test-time scaling work. The common direction is that inference is becoming an adaptive process with state, feedback, and sometimes parameter updates.

## Emerging Pattern 2: Evaluators Are Becoming Dynamic Training Partners

DR Tulu's evolving rubrics address a hard problem in deep research: long-form, attributed, search-based answers do not reduce cleanly to short verifiable rewards. RLER lets rubrics co-evolve with policy behavior by incorporating newly explored search information and contrasting model responses.

This extends the rubric and benchmark line visible in Copyright-Bench, UniPercept, DRPBench, and Reward and Guidance through Rubrics. The evaluator is no longer a static scoring rule; for open-ended agent work, it becomes part of the training process.

## Emerging Pattern 3: PEFT Practice Is Forcing Exact Optimization Theory

The LoRA convergence paper studies original LoRA gradient descent without replacing it with a smoother toy version. Its key claim is a non-asymptotic convergence rate despite the lack of standard Lipschitz smoothness, using a reparameterized outer-product view and step-size control.

This links to floating-point expressivity, size-sensitive matroid oracles, and low-precision training: theory is being rebuilt around the method people actually use. The subtheme is practice-faithful theory.

## Emerging Pattern 4: Efficient Video Reasoning Needs Logical Evidence Plans

SCOPE identifies Semantic Submergence: flat semantic-vector filtering can preserve dominant visual content while losing subtle cues needed for multi-step reasoning. Its solution is to let a cloud LMM decompose the query into a DAG observation plan, then have edge devices retrieve evidence according to logical necessity.

This connects to OmniFit and TACO as semantics-aware compression. The efficient system keeps less input, but it chooses what to keep by task structure rather than raw similarity or uniform token budgets.

## Emerging Pattern 5: Reasoning Is Being Treated as a Controlled Dynamical System

Thinking in Flow recasts autoregressive chain-of-thought as a long-horizon trajectory that can drift under perturbations. It adds a dissipative Neural ODE thought state and selective gates to stabilize representation evolution during inference.

This links to Rex, IRNO, and broader numerical-methods-as-ML-infrastructure papers. The same mathematical language of stability, trajectories, and controlled dynamics is spreading from physical systems and diffusion solvers into language-model reasoning.

## Cross-Batch Links

- TTT-Discover, Neural Thickets, Skill Neologisms, and LoRA convergence all probe the adaptation geometry around pretrained models.
- DR Tulu and Copyright-Bench both show that realistic agent evaluation needs task-process structure, not just answer matching.
- SCOPE, OmniFit, and TACO all compress context by preserving semantically necessary information.
- Thinking in Flow, Rex, and IRNO all treat model behavior as a dynamical process whose stability matters.
- LoRA convergence and floating-point expressivity reinforce the practice-faithful theory cluster.

## Deep Theme Update

Batch 017 makes one theme especially clear: modern ML systems are being optimized at the level of process, not just prediction. Discovery is a training process at test time. Deep research is a rubric-evolution process. LoRA is an optimization process with nonstandard geometry. Video reasoning is a cloud-edge evidence-planning process. Chain-of-thought is a controlled dynamical process.

The deeper pattern is process-aware ML: the papers study the trajectory by which outputs are produced, not only the final output distribution.
