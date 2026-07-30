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
- multimodal and embodied AI: first expansion complete

Each entry should include problem, object, approach, why it works, and connection.

Pass 3 first-expansion sweep is complete across the listed theme families.

Next targets:

1. Per-paper child page split if `math-concepts.html` becomes too dense for readable navigation.
2. Second-pass per-paper detail for the densest lanes: agents/reasoning, physical/generative, and theory/optimization.
3. Cross-paper synthesis chains for modality credit assignment, state control, sample-path control, and identification boundaries.

Recent Pass 3 additions:

- Data and systems now has a theme expansion covering curriculum timing, data value, missingness and provenance, serving as information movement, compression as function preservation, adaptation, continual updates, and optimizer geometry.
- Physical and generative modeling now has a theme expansion covering spatial grounding, coherent worlds and video, diffusion/flow/energy sampling, chemistry and proteins, PDEs and scientific operators, embodied action, and human/multimodal signals.
- Theory and optimization now has a theme expansion covering optimizer dynamics, spectra and representation geometry, architecture as computation, scaling and learnability limits, games and mechanisms, sampling and transport, deployment-constrained guarantees, and constraints inside models.
- Causality and scientific discovery now has a theme expansion covering local effects, CI-test structure learning, Bayesian root cause under graph uncertainty, temporal and stochastic mechanisms, scientific hypothesis search, executable scientific workflows, counterfactual constraints, and identification boundaries.
- Multimodal and embodied AI now has a theme expansion covering coordinate state, world-model transitions, action geometry, modality credit assignment, token information bottlenecks, unified generation, non-text human signals, and outcome-level evaluation.

### Pass 4: Per-paper coverage

Status: in progress.

Add enough paper cards that the page covers the major named examples from each lane, while keeping the page readable. If it becomes too long, split into child pages by lane:

- `math-agents-reasoning.html`: created with second-pass paper-level detail for 40 papers
- `math-physical-generative.html`: created with second-pass paper-level detail for 43 paper-level cards
- `math-theory-optimization.html`: created with second-pass paper-level detail for 42 papers
- `math-evaluation-safety.html`: created with second-pass paper-level detail for 42 papers
- `math-data-systems.html`: created with second-pass paper-level detail for 48 paper-level cards

Next Pass 4 targets:

1. Cross-paper synthesis chains for state control, sample-path control, feasible-set design, measurement economics, and identification boundaries.
2. Optional follow-up child pages for any remaining over-dense lanes after the first child-page sweep.
3. A final balance pass to remove overlap among parent atlas cards and child-page links now that the cross-paper chains and paper-first index are stronger.

Optional child-page progress:

- `math-causality-scientific.html`: created with 31 paper-level cards across local effects, graph evidence, root-cause diagnosis, temporal mechanisms, hypothesis search, executable workflows, counterfactual policy, and latent interventions.
- `math-multimodal-embodied.html`: created with 54 paper-level cards across modality credit assignment, token bottlenecks, unified generation, non-text human signals, embodied action, memory and world state, grounded verification, and latent interfaces.
- `math-paper-object-index.html`: created as a paper-first lookup layer with 96 entries across 16 mathematical object groups, linking named papers to their core object, short first-principles read, and relevant deep page.

Balance-pass progress:

- `math-concepts.html`: added a route-finder section that tells readers which atlas layer to use when starting from a paper name, theme, mathematical object, or big-picture question.
- `math-coverage-matrix.html`: created as a working audit page showing per-lane paper-level depth, object coverage, cross-paper links, assumptions/failure-boundary coverage, and next expansion targets.
- `math-theorem-to-deployment.html`: created as a theory transfer page with 14 bridge cards separating mathematical, statistical, and system-level assumptions for guarantees and deployment claims.
- `math-agents-reasoning.html`: added a focused chain connecting reasoning collapse, tool-call cost, executable verification, and verifier gaming across RAGEN-2, ParetoPO, CyberGym, and TRACE Effort.
- `math-physical-generative.html`: added a focused native-state chain connecting quotient geometry, field/PDE operators, and embodied action across Quotient-Space Diffusion, TideGS/RadioGS, IRNO, HDFlow, MomaGraph, EgoTactile, JoSE, and RodriNet.
- `math-physical-generative.html`: added a focused grounded-world-model chain connecting action-conditioned transition state, vector world representation, control consistency, and verifier projections across FlashWorld, VectorWorld, dWorldEval, OmniVerifier, and VideoKR.
- `math-physical-generative.html`: added a focused tail-sensitive sampling chain connecting rare-mode estimation, safety boundaries, heavy-tailed corruption, tractable density, and Best-of-N selection across SRMC, Safety-Guided Flow, Cauchy-Driven Diffusion Bridges, FALCON, and FIDIA.
- `math-multimodal-embodied.html`: added a focused measurement-channel chain connecting fMRI, speech prosody, tactile contact, missing modalities, clinical labels, and video knowledge across Mind-Omni, PRISM, Hibiki-Zero, EgoTactile, LIMSSR, Seizure-Semiology-Suite, and VideoKR.
- `math-multimodal-embodied.html`: added a focused evidence-route intervention chain connecting route credit, visual counterfactuals, hidden-state patching, streaming attribution, and routed memory across MoCA, VGS, VISUALSWAP, Causal Route Gating, MINT, Visual Attribution Streaming, and DLMR.
- `math-multimodal-embodied.html`: added a focused token-sufficiency chain connecting spatiotemporal merging, information-value token allocation, modality context budgets, online filtering, low-dimensional adaptation, and structure-preserving embeddings across FlashVID, InfoTok, VideoFlexTok, OmniFit, LST, COMPACT, LiME, MetaEmbed, and TACO.
- `math-multimodal-embodied.html`: added a focused embodied-constraint chain connecting embodied evaluation, affordance graphs, tactile contact, hierarchical action, constrained policy updates, action manifolds, kinematics, reusable behavior, simulated practice, and self-control across SAW-Bench, MomaGraph, RoboMME, HDFlow, EgoTactile, PACT, JoSE, RodriNet, BehaviorVLA, DreamDojo, and SCALE.
- `math-multimodal-embodied.html`: added a focused unified-generation chain connecting iterative editing, shared latent protocols, native speech state, world and view consistency, field coordinates, and artifact-level reward/verification across NextStep-1, EditVerse, LatentLM, UALM, VibeVoice, TTSDS2, FlashWorld, VIST3A, TideGS/RadioGS, Omni-Reward, UniPercept, and MetamerGen.
- `math-multimodal-embodied.html`: added a focused memory-provenance chain connecting video event state, streaming visual attribution, routed observation/reasoning memory, cross-modal hallucination repair, and weak-label reliability across VideoKR, Visual Attribution Streaming, DLMR, RFCMH, WETR, and AGREE.
- `math-assumptions-failure-boundaries.html`: added paper-specific multimodal boundary rows for measurement channels, evidence-route interventions, token sufficiency, embodied constraints, memory provenance, and unified-generation interfaces.
- `math-assumptions-failure-boundaries.html`: added paper-specific physical/generative boundary rows for quotient identity, molecule-design feasibility, tail-sensitive sampling, guided probability paths, scientific field bases, action-conditioned world models, and native verifier projections.
- `math-assumptions-failure-boundaries.html`: added paper-specific theory/optimization boundary rows translating theorem assumptions into evidence checks for optimizer geometry, low-rank adaptation, spectra, expressivity, finite tests, unlearning/privacy, watermarking, and finite arithmetic.
- `math-agents-reasoning.html`: added a focused multi-agent mechanism chain connecting disagreement as information, collaboration graph search, value of information, latent roles, cost frontiers, strategic response, and aggregation across Value of Variance, OMAC, Rational Agents, MASPOB/LatentMAS, ParetoPO, Accuracy Auctions, and AdvGame.
- `math-assumptions-failure-boundaries.html`: added paper-specific evaluation/safety boundary rows separating measurement validity, domain observation channels, tail-pressure safety, adaptive boundary pressure, executable certificates, distinguishability tests, and governance aggregation rules.
- `math-evaluation-safety.html`: added focused measurement-validity and tail-pressure safety chains connecting benchmark instruments, domain judges, finite-sample ranking, rare-event estimation, adaptive attacks, feasible boundaries, and verifier-noise training dynamics.
- `math-assumptions-failure-boundaries.html`: added paper-specific data/systems boundary rows for training-time plasticity, conditional data value, provenance and incentives, missingness and synthetic coverage, serving-state preservation, compression error, and adaptation subspaces.
- `math-data-systems.html`: added focused training-path value and serving-state preservation chains connecting data timing, marginal utility, update geometry, reasoning-trace supervision, memory layouts, KV retention, agent workflow state, and compression dynamics.
- `math-assumptions-failure-boundaries.html`: added paper-specific causality/scientific-discovery boundary rows for local effect identification, graph equivalence, root-cause posterior diagnosis, temporal mechanisms, rejectable hypothesis search, executable scientific workflows, and latent intervention validity.
- `math-causality-scientific.html`: added focused identification-boundary and executable-hypothesis chains connecting local causal certificates, graph equivalence, root-cause intervention ranking, temporal mechanism recovery, randomized effect search, hypothesis-space coverage, scientific workflow execution, and proof/artifact checking.
- `math-paper-object-index.html`: added causal-identification and scientific-hypothesis evidence examples that state what observation, intervention, stress test, execution trace, or checker output would make each mathematical object credible.
- `math-paper-object-index.html`: added multimodal evidence-route and multimodal state/token/embodiment evidence examples for modality credit, counterfactual visual grounding, internal fusion intervention, brain/tactile measurement channels, shared latent protocols, field bases, video token sufficiency, provenance-routed memory, affordance graphs, hierarchical action, artifact verification, and expert event labels.

### Pass 5: Cross-paper synthesis

Status: in progress.

Add chain sections that show how groups of papers form one argument:

- reasoning traces as information channels
- benchmarks as measurement instruments
- safety as boundary and tail modeling
- generation as sampling in native structure
- compression as function-preserving approximation
- training as movement through geometry
- data as distribution design
- causality as intervention-aware representation
- multimodal fusion as modality credit assignment
- context compression as sufficient-state selection
- scientific claims as testable hypotheses
- assumptions and remaining failures as explicit mathematical boundaries

Current Pass 5 artifact:

- `math-cross-paper-synthesis.html`: expanded to 18 first-principles cross-paper chains covering state control, measurement instruments, distribution design, feasible sets, transport paths, update geometry, function-preserving approximation, certificates, mechanisms, identification boundaries, modality credit, bottlenecks, grounded verification, latent interfaces, tail pressure, spectra, curriculum paths, and testable hypotheses.
- `math-assumptions-failure-boundaries.html`: created with 16 cross-lane boundary cards explaining the assumptions under which each mathematical object helps and the failure that remains outside those assumptions.

## Completion Standard

The long-term goal is not complete until a reader can start from any major paper or theme and understand:

- what mathematical problem the paper is actually solving
- why the proposed method should help
- what assumptions make it work
- what failure remains outside the method
- which other papers are solving the same mathematical object in another setting
