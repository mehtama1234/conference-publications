# Consolidated Theme Writeup

Scope: current local analysis of ICML 2026 Spotlight notes, ICLR 2026 Oral notes, and the first ICLR 2026 Poster batches.

Source depth: mixed. Some notes use arXiv-extracted paper text, but many ICLR notes are based on OpenReview/Paper Copilot metadata and abstracts because OpenReview PDF access was blocked from this environment and arXiv fallback was conservative. Treat this as a strong theme map and synthesis draft, not as a final full-paper literature review.

## Executive Thesis

The strongest pattern across the 2026 ICML/ICLR corpus is that machine learning research is shifting from single-model prediction toward engineered reasoning systems. The model is still central, but many of the most repeated ideas live around it: test-time compute allocation, verification loops, tool calls, retrieval, richer reward models, structured intermediate states, domain-specific benchmarks, data curation, and deployment-aware efficiency.

In other words, capability is increasingly produced by the whole process: what data the model sees, what representation it uses internally, how inference is scheduled, how outputs are checked, and what constraints are imposed by deployment. The papers are less often saying "scale the model and it works"; they are saying "shape the context, reward, benchmark, representation, or inference procedure so the model can use its capacity correctly."

## 1. Inference Is Becoming an Adaptive Process

A major cross-corpus theme is that inference is no longer treated as one forward pass. Papers repeatedly introduce search, refinement, verification, branching, adaptive decoding, tool calls, and confidence-based scheduling.

This appears in reasoning and tool-use work such as THOR, which optimizes mathematical reasoning at both final-answer and intermediate tool-call levels. It appears in diffusion-language work such as AdaBlock-dLLM, which changes block size during decoding based on confidence dynamics rather than using a fixed semi-autoregressive schedule. It appears in agent work such as T3, which preserves informative prefixes and truncates weak trajectory tails. It also appears in self-refinement and planning papers where models decide when and how to revise.

The deeper point is that compute is becoming a controllable test-time resource. The important question is not simply whether a model can answer, but how it spends computation: which branches to explore, which tool calls to trust, when to stop, when to revise, and how to trade speed against quality.

## 2. Evaluation Has Become a Research Object

Evaluation is one of the densest themes in the corpus. Many papers build benchmarks not as afterthoughts but as the core contribution. These benchmarks test abilities that conventional accuracy misses: verifiable proof, spatial mental modeling, closed-loop world-model usefulness, grounded image flaws, intent reasoning in misinformation, physical realism, agent security, and deep information synthesis.

VERINA is a clean example: it separates code correctness from specification correctness and proof success, revealing that current LLMs can often write code but rarely complete formal proof obligations. RedTeamCUA evaluates computer-use agents in hybrid web-OS environments where malicious content can be embedded in the environment. WoW! tests world models by whether they improve embodied task success, not whether their videos merely look good. ImageDoctor gives localized, multi-aspect diagnostics for text-to-image outputs rather than a single scalar.

The field seems to be responding to a measurement crisis. Model outputs are fluent enough that shallow metrics are no longer trusted. The emerging answer is evaluation that is executable, adversarial, grounded, process-aware, and domain-specific.

## 3. Intermediate States Are Becoming the Main Object of Control

A repeated pattern is that papers make intermediate states meaningful: reasoning traces, partial solutions, visual plans, cognitive maps, retrieved definitions, tool-call outputs, diffusion states, or local model discrepancies.

NEXCO makes masked diffusion states into feasible partial solutions for combinatorial optimization. Visual Planning uses image sequences as plans rather than text-only chains. MindCube-style spatial mental modeling asks VLMs to construct cognitive maps of unseen space. CRAMF retrieves exact formal definitions so autoformalization is grounded before generation. Global merging in decentralized learning reinterprets local-model discrepancies as partly constructive rather than merely noisy.

The common move is to stop treating the path to the output as hidden plumbing. The path becomes trainable, inspectable, rewardable, and sometimes the real contribution.

## 4. Data Is a Control Surface, Not Just Fuel

Another strong pattern is data as intervention. The corpus contains many papers on synthetic data, dataset filtering, data sufficiency, curated benchmarks, preference data, domain-specific corpora, and compositionally dense examples.

COMPACT shows that visual instruction tuning can use far fewer samples if each example combines multiple atomic visual capabilities. CauKer generates causally coherent synthetic time series for pretraining and reports cleaner scaling behavior than irregular real-world datasets. CALIPER decides when enough post-drift data has accumulated for retraining. WIMHF uses sparse autoencoder features to diagnose and clean preference datasets. Common Corpus frames legally usable, open pretraining data as research infrastructure.

The deeper theme is that data quality, provenance, and structure are now first-class levers of model behavior. More data still matters, but the papers repeatedly show that the relevant question is "what kind of data, selected by what principle, for which capability?"

## 5. Scaling Laws Are Being Refined, Not Abandoned

Scaling remains central, but the scaling story is becoming more conditional. ATLAS extends scaling laws to multilingual transfer, deriving language-pair transfer matrices and compute crossover points. The multi-epoch scaling paper defines an effective data reuse rate, showing when repeating a dataset is equivalent to fresh data and when gains plateau. Intrinsic Entropy argues that longer context helps only when it reduces irreducible uncertainty enough to justify the added context.

These papers push against naive monotonic intuitions. Longer context is not always better. More languages are not automatically better. Repeated epochs are not always wasteful, but their value depends on dataset size and distribution. Larger models do not remove the need to allocate data, compute, and context carefully.

The emerging scaling law is adaptive: scale has to be conditioned on language transfer, data reuse, context informativeness, and deployment cost.

## 6. Domain-Native Representations Are Replacing Generic Ones

Many papers argue that the right representation should match the task domain. EmotionThinker grounds speech emotion reasoning in prosody. OrbEvo predicts electronic wavefunction coefficients and density-matrix interactions for TDDFT. DA3 uses depth rays as a unified geometry target. SI-VAE uses point-process likelihoods to model spatial organization in microscopy images. `cadrille` outputs executable CAD code rather than a generic 3D artifact.

The pattern is strongest in scientific, spatial, formal, and multimodal domains. Generic text or image embeddings are often too weak because they erase the structure that matters: physical symmetries, acoustic cues, formal definitions, geometry, molecular makeability, or executable constraints.

The corpus suggests a mature view of foundation models: they are powerful substrates, but high-quality systems often need domain-native interfaces around them.

## 7. Rewards Are Becoming Hybrid, Dense, and Trust-Aware

Reward design is a recurring pressure point. Sparse verifiers are reliable but brittle; dense learned rewards are informative but easier to exploit. Several papers try to combine these signals.

HERO mixes verifier correctness with reward-model nuance using stratified normalization and variance-aware weighting. ImageDoctor turns localized image flaws into dense reward for text-to-image alignment. EmotionThinker introduces trust-aware reasoning rewards that check whether explanations align with outcomes. MNPO generalizes preference optimization into multiplayer Nash settings to capture non-transitive and heterogeneous human preferences.

The larger pattern is that reward is becoming structured. Instead of one scalar preference model, papers use verifier groups, local heatmaps, rationale quality, trust weights, population games, and tool feedback. Alignment is moving toward richer supervision that preserves correctness while giving useful gradients.

## 8. Safety, Robustness, Privacy, and Provenance Are Converging

The safety-related papers are not isolated. They share tools with evaluation, interpretability, data governance, and deployment systems.

RedTeamCUA and PLAGUE study adversarial multi-step behavior in agents and LLMs. Differentially Private Domain Discovery asks what can be surfaced from an unknown domain under privacy constraints. Gaussian certified unlearning reframes deletion guarantees through high-dimensional hypothesis testing. Ellipse signatures and semantic watermark fingerprints treat model provenance as a structural verification problem. Persistent homology analyzes adversarial influence through latent-space topology.

The repeated point is that deployment creates coupled risks. Privacy, safety, robustness, hallucination, provenance, and adversarial behavior all require audits and constraints over processes, not just final outputs.

## 9. Efficiency Is a Capability Enabler

Efficiency papers are not merely about reducing cost. They make new behavior feasible: longer inference, real-time interaction, large-context operation, on-device learning, and larger evaluation loops.

Polar Express revisits matrix sign computation for the Muon optimizer under GPU and `bfloat16` constraints. PGM removes mask-token overhead in masked generation. MotionStream enables fixed-context interactive video generation. MetaEmbed lets users choose retrieval quality/cost by selecting how many meta-token vectors to use. Layer-pruning work shows that simple pruning plus targeted fine-tuning can outperform more elaborate heuristics. TiTok makes LoRA adaptation more transferable through token-level diagnostics.

The deeper theme is that engineering constraints now shape method design. Memory, latency, quantization, serving cost, and training throughput are not secondary; they define what capabilities can be deployed or even evaluated.

## 10. Scientific ML Is Becoming a Stress Test for General ML

Scientific and physical-domain papers recur across protein design, PDEs, quantum dynamics, chemistry, biology, climate, microscopy, and physical-video benchmarks. These domains demand things generic benchmarks often do not: conservation, symmetry, uncertainty, makeability, measurement realism, and sim-to-real transfer.

RealPDEBench pairs real measurements with simulations to expose deployment gaps. OrbEvo builds symmetry-aware wavefunction dynamics. Complexa and mCLM encode atomistic or synthesis constraints. PhyWorldBench tests whether video models obey physical principles. HierAFold exploits protein-complex modularity to scale structural prediction.

Scientific ML appears to be serving as a forcing function. It pushes models toward grounded representations, uncertainty-aware evaluation, and constraints that cannot be satisfied by surface fluency.

## Cross-Cutting Pattern: From Bigger Models to Better Systems

The clearest common pattern is a shift from model size as the primary story to system structure as the primary story. Strong papers often ask:

- What intermediate representation should the model use?
- What evidence is sufficient before acting?
- What should be retrieved, verified, or executed?
- How should test-time compute be allocated?
- What reward signal preserves correctness while giving useful gradients?
- What benchmark actually measures the intended capability?
- What data structure induces the desired behavior?
- What deployment constraint changes the algorithm?

This does not mean scale is unimportant. It means scale is becoming conditional. The best-performing systems are often those that know how to spend scale: through data curation, adaptive inference, domain-native representations, structured rewards, verification, and efficient infrastructure.

## Practical Takeaways

1. Treat inference as a policy, not a fixed call.
2. Evaluate processes and artifacts, not only final answers.
3. Make intermediate states meaningful and inspectable.
4. Use data curation as an explicit capability intervention.
5. Prefer domain-native representations where the task has structure.
6. Combine sparse correctness signals with dense diagnostic feedback.
7. Treat deployment constraints as part of the research problem.
8. Separate abstract-derived hypotheses from full-paper-confirmed claims.

## Confidence

High confidence in the existence of these recurring themes, because they are supported by a large theme index and many batch syntheses. Medium confidence in specific causal claims for abstract-only papers. The next improvement would be to upgrade the most important abstract-only notes with full PDFs when OpenReview or arXiv access is available, then revise this synthesis around the strongest full-text evidence.
