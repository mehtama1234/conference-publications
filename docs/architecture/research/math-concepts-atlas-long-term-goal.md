# Math Concepts Atlas Long-Term Goal

## Objective

Build the conference math layer into a first-principles atlas over ICML / ICLR 2026 papers. The page should explain, for each theme, subtheme, and representative paper:

- the big-picture problem being solved
- the mathematical object the paper defines
- why that object makes the approach work
- what failure mode the approach avoids
- how the paper connects to other papers that use the same object in a different domain

The tone should stay conceptual and precise. Avoid generic claims such as "better robustness", "improved efficiency", or "novel framework" unless the text says what is being measured, constrained, optimized, or preserved.

## Working Principle

Every paper entry should answer this chain:

1. What is the state space?
2. What information must be preserved?
3. What variation should not matter?
4. What constraints define valid behavior?
5. What uncertainty remains after observation?
6. What update, sampler, verifier, or representation is used?
7. Why does that choice improve the mathematical problem rather than only changing the implementation?

## Iteration Plan

### Pass 1: Existing dense atlas

Status: complete.

The current `math-concepts.html` has concept lenses, per-paper cards, cross-theme mechanisms, paper chains, and a dense mechanism atlas.

### Pass 2: Object grammar

Status: complete.

Add a section that makes the recurring mathematical objects explicit:

- state transition
- feasible set
- quotient space
- latent variable
- verifier
- ambiguity set
- tail event
- tradeoff frontier
- spectrum
- game / mechanism
- trajectory
- sample path

Each object should be tied to multiple papers and explained in plain language.

### Pass 3: Theme-by-theme expansion

Status: in progress.

Expand each theme family into 10-15 richer entries:

- agents and reasoning: first expansion complete
- evaluation and diagnostics: first expansion complete
- safety and governance: first expansion complete through the evaluation/safety lane
- data and systems: first expansion complete
- physical and generative modeling: first expansion complete
- theory and optimization: first expansion complete
- causality and scientific discovery: first expansion complete
- multimodal and embodied AI

Each entry should include problem, object, approach, why it works, and connection.

Next Pass 3 targets:

1. Multimodal and embodied AI: modality credit assignment, geometry, memory routing, action constraints, tactile/contact evidence, human-signal structure.
2. Per-paper child page split if `math-concepts.html` becomes too dense for readable navigation.
3. Second-pass per-paper detail for the densest lanes: agents/reasoning, physical/generative, and theory/optimization.

Recent Pass 3 additions:

- Data and systems now has a theme expansion covering curriculum timing, data value, missingness and provenance, serving as information movement, compression as function preservation, adaptation, continual updates, and optimizer geometry.
- Physical and generative modeling now has a theme expansion covering spatial grounding, coherent worlds and video, diffusion/flow/energy sampling, chemistry and proteins, PDEs and scientific operators, embodied action, and human/multimodal signals.
- Theory and optimization now has a theme expansion covering optimizer dynamics, spectra and representation geometry, architecture as computation, scaling and learnability limits, games and mechanisms, sampling and transport, deployment-constrained guarantees, and constraints inside models.
- Causality and scientific discovery now has a theme expansion covering local effects, CI-test structure learning, Bayesian root cause under graph uncertainty, temporal and stochastic mechanisms, scientific hypothesis search, executable scientific workflows, counterfactual constraints, and identification boundaries.

### Pass 4: Per-paper coverage

Add enough paper cards that the page covers the major named examples from each lane, while keeping the page readable. If it becomes too long, split into child pages by lane:

- `math-agents-reasoning.html`
- `math-evaluation-safety.html`
- `math-data-systems.html`
- `math-physical-generative.html`
- `math-theory-optimization.html`

### Pass 5: Cross-paper synthesis

Add chain sections that show how groups of papers form one argument:

- reasoning traces as information channels
- benchmarks as measurement instruments
- safety as boundary and tail modeling
- generation as sampling in native structure
- compression as function-preserving approximation
- training as movement through geometry
- data as distribution design
- causality as intervention-aware representation

## Completion Standard

The long-term goal is not complete until a reader can start from any major paper or theme and understand:

- what mathematical problem the paper is actually solving
- why the proposed method should help
- what assumptions make it work
- what failure remains outside the method
- which other papers are solving the same mathematical object in another setting
