# ICML 2026 Spotlight Batch 004 Synthesis

Scope: ICML spotlight notes 16-20.

Source depth: full extracted arXiv text for BehaviorVLA, Rare Event Analysis of LLMs, DiReCT, and Beyond Log Likelihood; abstract/metadata only for Transformer Circuits Can Realize Clustering Algorithms because no confident local PDF match is available yet.

## Papers Covered

- From Abstraction to Instantiation: Learning Behavioral Representation for Vision-Language-Action Model.
- Rare Event Analysis of Large Language Models.
- Towards Efficient LLMs Annealing with Principled Sample Selection.
- Beyond Log Likelihood: Probability-Based Objectives for Supervised Fine-Tuning across the Model Capability Continuum.
- Transformer Circuits Can Realize Clustering Algorithms.

## Emerging Pattern 1: Representation Is Moving Up a Level of Abstraction

BehaviorVLA is not optimizing only an action head. It builds a long-horizon behavioral representation with causal Mamba streams, then uses phase-conditioned decoding to instantiate actions during execution. Transformer Circuits makes a parallel move in a different domain: standard transformer components are treated as an exact algorithmic substrate for Lloyd's k-means.

The common thread is abstraction with executable consequences. A representation is valuable when it constrains action, clustering, or computation in a way that remains operational, not merely descriptive.

## Emerging Pattern 2: Evaluation Is Turning Toward the Tail

Rare Event Analysis argues that deployment-scale LLM behavior cannot be summarized by typical samples. Rare behaviors need event definitions, probability estimates, error bars, and structural exploration. This is a deep evaluation shift: safety-relevant model behavior is treated as a statistical tail problem rather than a benchmark-average problem.

This connects directly to SandboxEscapeBench, CyberGym, Invisible Safety Threat, and Catch-22. The field is building tools for behaviors that are low-frequency, adversarial, hidden, or expensive to observe.

## Emerging Pattern 3: Training Rules Depend on Phase and Capability

DiReCT and Beyond Log Likelihood both reject fixed training recipes. DiReCT says the annealing phase has its own loss-geometry constraints, so sample selection should follow Hessian eigendirections. Beyond Log Likelihood says SFT objectives should depend on the base model's capability: strong models benefit from prior-leaning objectives, while weak models still need NLL's corrective pressure.

The deeper theme is conditional training. The right objective or data policy depends on where the model is in training and what the model already knows.

## Emerging Pattern 4: Data Is Becoming a Control Surface

DiReCT chooses data through per-sample gradient geometry. Beyond Log Likelihood downweights or thresholds low-probability tokens when they are likely to be noise for a strong model. BehaviorVLA shows that robot data efficiency improves when demonstrations are encoded as coherent behavioral trajectories rather than isolated action labels.

Across these papers, data is not passive fuel. It is filtered, weighted, structured, and temporally organized to steer optimization.

## Emerging Pattern 5: Classical Theory Is Being Reused as ML Infrastructure

Rare Event Analysis imports statistical mechanics and Monte Carlo tools. DiReCT imports spectral Hessian geometry. Transformer Circuits imports classical clustering algorithms into transformer circuit analysis. These are not cosmetic analogies; they produce concrete procedures, estimators, constraints, and architectural proofs.

This suggests a growing research style: use older mathematical machinery to make modern foundation-model behavior more measurable, controllable, and interpretable.

## Cross-Batch Links

- BehaviorVLA and MomaGraph form a strong embodied-AI pair: one structures behavioral policy execution over time, the other structures task-oriented scene understanding before planning.
- Rare Event Analysis links with Invisible Safety Threat, SandboxEscapeBench, CyberGym, and Catch-22 as a cluster around hard-to-see safety failures.
- DiReCT links with Difficult Examples Hurt Unsupervised Contrastive Learning and Common Corpus by treating data composition as a determinant of model behavior rather than background infrastructure.
- Beyond Log Likelihood links with Base Models Know How to Reason and DMPO: post-training should respect the base model's existing mechanisms and probability landscape.
- Transformer Circuits links with HATSolver and Base Models Know How to Reason as evidence that transformer behavior can be analyzed through algorithmic mechanisms, not only end-task accuracy.

## Subthemes to Track

- Long-horizon behavioral abstraction.
- Phase-conditioned robot policy execution.
- Rare-event probability estimation for LLMs.
- Tail-risk error analysis.
- Curvature-aware annealing.
- Capability-conditioned SFT objectives.
- Prior-leaning versus prior-averse updates.
- Transformer circuits as exact algorithms.
- Classical theory as foundation-model tooling.
