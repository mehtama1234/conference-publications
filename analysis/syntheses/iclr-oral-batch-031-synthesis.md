# ICLR Oral Batch 031 Synthesis

## Papers Covered

- Global Resolution: Speculative Decoding with Optimal Multi-Draft Fusion
- Locality-aware Parallel Decoding for Efficient Autoregressive Image Generation
- P-GenRM: Personalized Generative Reward Model with Test-time User-based Scaling
- AutoEP: LLMs-driven Automation of Hyperparameter Evolution for Metaheuristic Algorithms
- MedAgentGym: A Scalable Agentic Training Environment for Code-centric Reasoning in Biomedicine

## Shared Thesis

This batch is about test-time and process-level optimization under constraints. Global Resolution preserves target distributions while making multi-draft speculative sampling tractable. LPD changes autoregressive image generation order to expose locality-based parallelism. P-GenRM personalizes reward scoring through user and prototype scaling. AutoEP couples LLM reasoning to live landscape diagnostics for zero-shot hyperparameter control. MedAgentGym provides executable biomedical environments where code-centric agents can be trained with verifiable feedback. Across the batch, stronger systems come from optimizing the procedure around the model, not only the model weights.

## Deep Themes

### Distribution-Preserving Acceleration

Global Resolution and LPD both accelerate generation while trying to preserve the intended output behavior. Global Resolution uses max-flow and polymatroid structure to collapse an exponential optimal-transport verification problem into a tractable convex form. LPD exposes safe parallelism in image-token generation by changing generation order and grouping nearby patches. The shared pattern is that latency reductions are framed as dependency-structure problems rather than approximate shortcuts alone.

### Test-Time Personalization and Scaling

P-GenRM extends reward modeling from population-average preference scoring toward user-specific evaluation. It derives adaptive personas and rubrics, then scales evaluation at both individual and prototype granularity. This fits a broader 2026 pattern: test-time computation is increasingly used to condition systems on users, tasks, or contexts instead of relying on one fixed post-training objective.

### LLMs as Grounded Algorithm Controllers

AutoEP uses LLM reasoning for dynamic hyperparameter evolution, but grounds the reasoning in online exploratory landscape analysis. The important subtheme is not simply "LLMs tune algorithms"; it is that LLM control becomes more credible when coupled to quantitative diagnostics from the running process. This links to broader agent and optimizer work where feedback channels determine whether reasoning helps or drifts.

### Executable Environments for Domain Agents

MedAgentGym makes biomedical data-science reasoning trainable and measurable by wrapping tasks in executable sandboxes with feedback, ground truth, and trajectory generation. The subtheme is domain-specific agent infrastructure: useful agents need environments that encode the real workflow, expose verifiable outcomes, and support offline and online improvement.

## Cross-Paper Pattern

The common pattern is controlled procedural adaptation. Global Resolution adapts verification across multiple drafts; LPD adapts generation order to locality; P-GenRM adapts reward criteria to a user or prototype; AutoEP adapts optimization parameters to landscape signals; MedAgentGym adapts biomedical agents through executable task feedback. The deeper theme is that many 2026 methods treat the surrounding process as a first-class optimization target.

## Subthemes to Track

- Convex and combinatorial structure in speculative decoding.
- Locality-aware parallel autoregressive generation.
- Personalized generative reward modeling.
- Quantitative diagnostics for LLM-driven algorithm control.
- Executable biomedical agent training environments.

## Confidence and Source Depth

These notes are based on abstracts and local metadata. Formal details, validation protocols, and benchmark settings should be upgraded when PDFs are available.
