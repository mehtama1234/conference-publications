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
- `math-paper-object-index.html`: created as a paper-first lookup layer with 112 entries across 30 mathematical object groups, linking named papers to their core object, short first-principles read, and relevant deep page.

Balance-pass progress:

- `math-concepts.html`: added a route-finder section that tells readers which atlas layer to use when starting from a paper name, theme, mathematical object, or big-picture question.
- `math-coverage-matrix.html`: created as a working audit page showing per-lane paper-level depth, object coverage, cross-paper links, assumptions/failure-boundary coverage, and next expansion targets.
- `math-theorem-to-deployment.html`: created as a theory transfer page with 14 bridge cards separating mathematical, statistical, and system-level assumptions for guarantees and deployment claims.
- `math-verifier-gaming.html`: created as a cross-lane synthesis page connecting verifier gaming, reward hacking, measurement-channel drift, adaptive pressure, certificate mismatch, and aggregation failure across the seven lanes.
- `math-icml-iclr-differences.html`: created as a conference-difference synthesis page explaining ICML and ICLR through mathematical habits: ICML tends to expose control variables, while ICLR tends to build system forms where behavior can be observed.
- `math-agents-reasoning.html`: added a focused chain connecting reasoning collapse, tool-call cost, executable verification, and verifier gaming across RAGEN-2, ParetoPO, CyberGym, and TRACE Effort.
- `math-agents-reasoning.html`: added a paper-specific formula/evidence box section for RAGEN-2, The Tell-Tale Norm, h1, Verifying Chain-of-Thought, ParetoPO, Skill-Pro, CyberGym, and OMAC, stating the compact mathematical condition and evidence check for each.
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
- `math-paper-object-index.html`: added theory/optimization theorem-to-evidence examples for adaptive optimizer geometry, curvature-aware data movement, low-rank adaptation, trust-region policy movement, spectral alignment, Jacobian and BBP signal recovery, low-rank logit subspaces, architecture-as-algorithm claims, expressivity versus learnability, finite test certification, watermark detection frontiers, and finite-precision guarantees.
- `math-paper-object-index.html`: added data/systems evidence examples for optimizer-time data value, midtraining distribution bridges, sequential marginal contribution, optimizer-shaped selection, governed corpora, market incentives, multilingual transfer matrices, memorization/missingness/synthetic coverage, long-context memory schedules, cache sufficiency, speculative agent execution, tensor-layout semantics, precision maps, quantization error dynamics, pruning loops, and conditional-computation preservation.
- `math-paper-object-index.html`: added molecule-design evidence examples for molecular identity under quotient geometry, coarse-to-fine protein hierarchy, fold consistency, contextual binder distributions, factorized binding/conformation variables, density-tracked equilibrium sampling, rare-mode estimation, Best-of-N selection, building-block constrained generation, reaction-aware synthesis, retrosynthesis Pareto fronts, structure-sensitive benchmarks, and the identity-feasibility-route-selection chain.
- `math-paper-object-index.html`: added agents/reasoning evidence examples for trace-input dependence, inspectable reasoning trajectory distributions, horizon curricula, hidden-state recursion signals, dependency-graph verification, trace-effort sensitivity, shared user-agent-tool state, executable skills, tool-use Pareto frontiers, cybersecurity execution certificates, terminal/tool trajectory state, cache value, collaboration graphs, value of information, latent roles, and strategic mechanism response.
- `math-paper-object-index.html`: added evaluation/safety evidence examples for Fisher-information item selection, factored benchmark quality, finite-sample ranking confidence, domain-specific judges, human-agent-oracle decomposition, causal dependence on visual and multimodal evidence, expert event grammars, embodied evaluation functionals, rare-event tail probability, CVaR trajectory credit, decision-shaped uncertainty sets, adaptive jailbreak pressure, feasible boundary geometry, noisy verifier training dynamics, unlearning indistinguishability, RL policy deletion, memorization capacity, privacy-noise geometry, watermark detection frontiers, value-intensity profiles, cross-modal reward state, helpfulness-safety frontiers, welfare mechanisms, fairness couplings, and truthful data valuation.
- `math-verifier-gaming.html`: added six cross-lane failure chains showing when a score, reward, judge, verifier, certificate, or aggregation rule stops identifying the real target: proxy objective gap, process shortcut, instrument drift, adaptive pressure, certificate mismatch, and aggregation failure.
- `math-icml-iclr-differences.html`: added eight object-level comparison sections across reasoning, agents, safety, generation, data, systems, theory, and measurement, pairing ICML control-surface examples with ICLR system-form examples and explaining why each habit works mathematically.
- `math-evaluation-safety.html`: added a paper-specific formula/evidence box section for ATLAS, FRABench/UFEval, Micro-Benchmarking Reliability, Rare Event Analysis/Tail Risks, CSPO/SecFid/SandboxEscapeBench, RLVepsR/Weak-Strong Verification, Gaussian Certified Unlearning, Catch-22/Watermarking, VALUEFLOW/SafeDPO, and Omni-Reward/VISUALSWAP/FlowGuard, stating the compact mathematical condition and evidence check for each.
- `math-theory-optimization.html`: added a paper-specific formula/evidence box section for Adam Degeneracy, DiReCT, LoRA theory, Alignment-Sensitive Minimax Rates, Single-Head Attention, Transformer Circuits, Language Generation in the Limit, FTRL lower bounds, Fair Optimal Transport, Mamba Markov ICL, Finite Test Certification, and Certified Unlearning/Privacy Bounds, tying each method to its mathematical object, working condition, and evidence check.
- `math-physical-generative.html`: added a paper-specific formula/evidence box section for Depth Anything 3, Stable Video Infinity, FlashWorld/VectorWorld, Safety-Guided Flow, DMPO, Quotient-Space Diffusion, Protein Autoregressive Modeling, DeCoDe/Chamaileon/Complexa, IRNO, HDFlow, MAPF via MMOT/Schrodinger Bridges, Mind-Omni/PRISM, and TEDBench/MiAE/FLIP2/RealPDEBench, tying physical and generative models to coordinates, trajectories, quotient spaces, transport paths, fixed points, latent human signals, and structure-sensitive benchmarks.
- `math-data-systems.html`: added a paper-specific formula/evidence box section for LR Decay, Midtraining Bridges/PRISM, BLL-Loss/LALP/OpenThoughts, Sequential Data Values/NASH, OPUS/DiReCT/HOBIT, LIMSSR/robust missing-covariate optimization, Common Corpus/Hubble/memorization capacity, DHSA/TileLang/einx, ThinKV/STAR-KV/EntroKV, ThunderAgent/speculative actions/ADP, LiftQuant/TetraJet/quantized diffusion, FOCUS/RePAIR, RAIN-Merging/FlexRank/LoRA, and Continual VLA/Skill Neologisms/GEPA/DTO-KD, tying data and systems papers to time-indexed gradients, marginal utility, missingness sets, cache sufficiency, compression error dynamics, and constrained adaptation.
- `math-multimodal-embodied.html`: added a paper-specific formula/evidence box section for MoCA/VGS/Causal Route Gating, VISUALSWAP/MINT, DOUBT/LIMSSR, FlashVID/InfoTok/VideoFlexTok, OmniFit/LST/COMPACT/LiME, MetaEmbed/TACO, LatentLM/UALM/NextStep-1, EditVerse/VIST3A/TideGS/RadioGS, VibeVoice/TTSDS2/Hibiki-Zero/WAVE, EmotionThinker/EEmo-Logic/Active Mind Avatars/MetaphorVU, PRISM/Mind-Omni/SleepLM/BioX-Bridge, SAW-Bench/RoboMME/MomaGraph/EgoTactile, HDFlow/PACT/JoSE/RodriNet/BehaviorVLA, VideoKR/Visual Attribution Streaming/DLMR/WETR/AGREE, and OmniVerifier/FlowGuard/DAVE/VC-STaR/HALO, tying multimodal and embodied work to causal route credit, token sufficiency, native media state, physiological latents, feasible action transitions, provenance-aware memory, and grounded verifiers.
- `math-causality-scientific.html`: added a paper-specific formula/evidence box section for Local Covariate Selection, TRECA/Fair Causal Bandits, Unpaired Causal IV, Structure Learning CI/DiCoLa, Distributional Equivalence, BRCD/production agent studies, CausalGame, Latent Hawkes/OU Identifiability/Power-Law Discovery, Neural Effect Search, HypoSpace/Bitween/Consequence-Based Utility, RefineStat/MedAgentGym/PaperBench/WZ-LLM/VERINA, DISCO/Fair Posthoc Control/missing-covariate robustness/Accuracy Auctions, and MINT/Causal Route Gating/Divergent Interventions/Activation Oracles, tying causal and scientific papers to identification targets, equivalence classes, intervention ranking, temporal mechanism assumptions, rejectable hypotheses, executable artifacts, policy constraints, and on-manifold latent interventions.
- `math-formula-gap-audit.html`: created a cross-page formula gap audit with 18 compact first-principles boxes for underrepresented named papers and paper groups across reasoning mechanisms, tool-use cost, expert/domain measurement, legal and incentive-constrained governance, artifact-native judging, multilingual token transfer, synthetic coverage repair, hardware-aware conditional computation, rare-mode sampling, molecule-route feasibility, spatial state consistency, architecture expressivity, spectral visibility, strategic equilibrium, finite arithmetic, memory correspondence, multimodal attribution, and checkable scientific artifacts.
- `math-paper-template.html`: created a reusable first-principles paper-entry protocol with nine required slots: big-picture problem, state space, mathematical object, preserved quantity, allowed movement, why the method works, formula condition, evidence check, and cross-paper role. The page also adds worked forms for agents, evaluation, safety, data/systems, physical/generative modeling, theory/optimization, and causality/multimodal claims.
- `math-paper-exemplars.html`: created and expanded a full-depth worked-exemplar layer applying the nine-slot protocol to RAGEN-2, ATLAS, Rare Event Analysis/Tail Risks, Midtraining Bridges, Quotient-Space Diffusion, Alignment-Sensitive Minimax Rates, Distributional Equivalence, Steer Like The LLM, RLVepsR, DiReCT, ReaSyn/MORetro*, Error Propagation in Quantized Diffusion Models, VISUALSWAP/MINT, Skill-Pro, ParetoPO, WebDevJudge/PaperBench/VERINA, ThinKV/STAR-KV/EntroKV, CSPO/SafeDPO/SecFid, LiftQuant/TetraJet/QAT Scaling, Safety-Guided Flow/DMPO, IRNO/RealPDEBench, Local Covariate Selection/TRECA, Neural Effect Search/HypoSpace, Mind-Omni/PRISM, and HDFlow/PACT/BehaviorVLA, showing how each paper's problem, state space, mathematical object, invariant, allowed movement, working condition, evidence check, failure boundary, and cross-paper role connect into the atlas.
- `math-object-deep-dives.html`: created an object-first deep-dive layer explaining ten recurring mathematical objects across papers: sufficient state, measurement channel, feasible set, transport path, spectrum, tail event, game/mechanism, identified set, latent interface, and certificate. Each object now has a first-principles problem statement, formula condition, why-it-works account, paper examples, evidence check, and failure boundary.
- `math-theme-subtheme-map.html`: created a theme-first map across seven lanes and 29 subthemes. Each subtheme now states the big-picture problem, mathematical object, approach family, representative papers, and cross-theme connection, bridging lane pages, object deep dives, paper exemplars, and cross-paper synthesis.
- `math-proof-sketches.html`: created an argument-first layer with 12 reusable first-principles proof sketches: invariance, feasibility, sufficiency, measurement, tail sampling, spectral visibility, update geometry, transport, identification, verification, mechanisms, and latent interfaces. Each sketch states the assumption, mathematical move, compact condition, why it works, representative papers, and where the argument breaks.
- `math-equation-glossary.html`: created a notation-first layer decoding 14 recurring formula forms across the atlas: constrained objective, state transition, sufficient statistic, measurement channel, tail probability, transport path, spectral gap, update geometry, low-rank movement, quotient space, identified claim, verifier, game/mechanism, and tradeoff frontier. Each form now has a plain read, paper families, why-it-works explanation, and evidence check.
- `math-paper-proof-audit.html`: created a paper-family claim-check layer with 24 rows mapping representative paper groups to proof sketches, required assumptions, supporting evidence, and failure modes. This connects named papers back to the reusable mathematical arguments and makes future card expansion auditable.

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
- `math-failure-mode-atlas.html`: created a cross-theme failure-mode layer with 18 rows mapping proxy drift, false invariance, missing sufficient state, bad feasible sets, tail blindness, spectral mirage, wrong update geometry, transport support miss, identification overclaim, verifier mismatch, strategic response gaps, entangled latent interfaces, tradeoff hiding, finite-sample overconfidence, finite-machine mismatch, artifact decomposition error, modality credit failure, and plasticity timing miss to broken assumptions, symptoms, evidence checks, and repair directions.
- `math-approach-patterns.html`: created a method-first layer with 20 reusable approach patterns, including state lifting, measurement-channel construction, feasible-set movement, distribution redesign, update geometry, quotienting, transport paths, tail estimation, spectral signal recovery, identification, mechanisms, latent control, dependency-aware artifact checking, compression, tradeoff frontiers, certificates, curricula, modality credit, native structure, and uncertainty reporting. Each pattern states the problem, approach, compact mathematical condition, why it works, and representative paper families.
- `math-paper-method-matrix.html`: created a paper-to-method bridge with 36 representative rows across reasoning, agents, evaluation, safety, data, systems, generation, science, theory, causality, multimodal, and embodied work. Each row maps a named paper or family to its mathematical object, approach pattern, why-it-works argument, assumption to audit, failure mode, and neighboring papers.
- `math-big-picture-problems.html`: created a problem-first synthesis layer with 12 underlying mathematical problems: reasoning trace validity, agent resource allocation, measurement under optimization, tail and boundary safety, data timing, compression fidelity, generative transport, native scientific representation, theoretical control quantities, causal identification, multimodal credit assignment, and theorem-to-deployment transfer. Each problem states the object, approaches, representative papers, why the approaches work, failure checks, and cross-page reading paths.
- `math-subtheme-proof-obligations.html`: created a subtheme-level proof-obligation ledger with 29 rows across reasoning, agents, evaluation, safety, data, systems, generation, science, theory, causality, multimodal, and embodied work. Each row states the mathematical object, approach move, proof obligation, evidence check, and next paper family to deepen.
- `math-evidence-check-atlas.html`: created an evidence-first layer with 24 concrete checks, including trace-input dependence, latent locality, horizon dependency, tool-value frontiers, skill reuse validity, verifier scope, benchmark rank uncertainty, proxy pressure, tail coverage, boundary audits, unlearning distinguishability, phase ablations, data marginal contribution, missingness stress, cache sufficiency, compression behavior drift, hardware traces, transport support, invariance boundaries, structure feasibility, spectral alignment, curvature energy, identified-set reports, and modality interventions. Each check names the object observed, representative paper families, weak substitutes to reject, and failure modes exposed.
- `math-paper-deepening-backlog.html`: created a prioritized paper-deepening backlog with 40 paper families across four priority bands. Each row states why the family matters, the object to explain, the approach to unpack, evidence needed, failure boundary, and cross-theme connections, so future iterations can select paper families for full nine-slot treatment systematically.
- `math-paper-exemplars.html`: expanded from 13 to 17 full-depth exemplars by adding Skill-Pro, ParetoPO, WebDevJudge/PaperBench/VERINA, and ThinKV/STAR-KV/EntroKV. These additions cover reusable agent skills, tool-use cost frontiers, native artifact verification, and context compression as sufficient-state selection.
- `math-paper-exemplars.html`: expanded from 17 to 21 full-depth exemplars by adding CSPO/SafeDPO/SecFid, LiftQuant/TetraJet/QAT Scaling, Safety-Guided Flow/DMPO, and IRNO/RealPDEBench. These additions cover safety as constrained movement, low-bit deployment as finite-machine approximation, reward and safety as distribution transport, and physical surrogates as stable operators.
- `math-paper-exemplars.html`: expanded from 21 to 25 full-depth exemplars by adding Local Covariate Selection/TRECA, Neural Effect Search/HypoSpace, Mind-Omni/PRISM, and HDFlow/PACT/BehaviorVLA. These additions cover local causal adjustment, validated hypothesis search, physiological latent interfaces, and embodied action feasibility.

## Completion Standard

The long-term goal is not complete until a reader can start from any major paper or theme and understand:

- what mathematical problem the paper is actually solving
- why the proposed method should help
- what assumptions make it work
- what failure remains outside the method
- which other papers are solving the same mathematical object in another setting
