# ICLR 2026 Oral Batch 010 Synthesis

## Papers

- Safety-Guided Flow: A Unified Framework for Negative Guidance in Safe Generation
- Pi-net: Optimizing hard-constrained neural networks with orthogonal projection layers
- Shoot First, Ask Questions Later? Building Rational Agents that Explore and Act Like People
- The Art of Scaling Reinforcement Learning Compute for LLMs
- FALCON: Few-step Accurate Likelihoods for Continuous Flows

## Source Depth

All five notes are abstract/metadata-only in the current local workspace. OpenReview remains the preferred source, and arXiv fallback should be retried for this ICLR oral range when access and rate limits clear.

## Shared Thesis

This batch is about making generation, optimization, agents, and scientific sampling respect the constraints of deployment. Safe flows need time-local guidance; constrained networks need feasible outputs; LM agents need resource-rational information seeking; LLM RL needs predictable compute scaling; and molecular flows need fast samples with accurate likelihoods.

The common pattern is disciplined control: guidance schedules, projection layers, Bayesian experimental design, scaling curves, and invertibility objectives all constrain flexible models so they become reliable tools.

## Subthemes

### Timed safety guidance

SGF argues that negative guidance in diffusion/flow models should be strong during a critical denoising window and decay elsewhere. Safety is a temporal control problem, not just a static penalty.

### Feasible-by-design neural optimization

Pi-net adds a projection layer so neural networks satisfy convex constraints by construction. This shifts constraint satisfaction from training loss to architecture.

### Resource-rational agents

Collaborative Battleship and Guess Who? show LM agents need explicit inference procedures for question asking and action selection. Bayesian experimental design can make weaker models act more rationally and cheaply.

### Predictive RL scaling

ScaleRL brings pretraining-style predictability to LLM RL. The key distinction is between recipe choices that alter compute efficiency and those that change the asymptotic ceiling.

### Likelihood-aware scientific flows

FALCON accelerates continuous flows for Boltzmann sampling while preserving likelihood accuracy for importance sampling. Scientific generation requires estimator correctness, not only sample fidelity.

## Cross-Batch Connections

SGF connects to GoodDiffusion, DivIn, RLR, DFM theory, and safe generation work through process-level control of diffusion/flow models.

Pi-net connects to control-barrier methods, conformal policy control, robust nonlinear systems, and safe optimization because feasibility is enforced structurally.

The rational-agent paper connects to Gaia2, GLANCE, MiniAppBench, and test-time scaling work through inference-time decision procedures.

ScaleRL connects to SGD RLVR, OpenThoughts, coverage theory, RAGEN-2, and Ctrl-R through LLM post-training scaling.

FALCON connects to RealUID, DFM theory, quotient-space diffusion, and molecular generative modeling through fast and correct scientific sampling.

## Emerging Pattern

The broader pattern is that flexible learned models become deployable when surrounded by principled controls: safety windows, projections, information-gain estimates, scaling laws, or likelihood guarantees.
