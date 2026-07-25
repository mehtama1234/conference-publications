# ICML 2026 Spotlight Batch 010 Synthesis

Scope: ICML spotlight notes 46-50.

Source depth: abstracts/metadata only for all five papers. The arXiv API returned HTTP 429 for each paper in this batch, so these notes should be prioritized for later full-text upgrades.

## Papers Covered

- DRPBench: Evaluating LLMs in Concurrent Code Comprehension via Fine-Grained Data Race Prediction.
- OMAC: A Holistic Optimization Framework for LLM-Based Multi-Agent Collaboration.
- Efficient Diffusion Models under Nonconvex Equality and Inequality constraints via Landing.
- Surgery: Mitigating Harmful Fine-Tuning for Large Language Models via Attention Sink.
- dnaHNet: A Scalable and Hierarchical Foundation Model for Genomic Sequence Learning.

## Emerging Pattern 1: Evaluation Is Moving Into Harder Semantic Regimes

DRPBench targets data-race prediction in concurrent programs, where runtime nondeterminism and synchronization semantics make ordinary code-comprehension benchmarks insufficient. It evaluates variable- and line-level static predictions rather than generic code generation.

This connects with CyberGym, SandboxEscapeBench, and HATSolver: the field is increasingly testing models on structured procedural understanding where shallow pattern matching breaks.

## Emerging Pattern 2: Agent Systems Need Architecture Search, Not Only Prompt Craft

OMAC frames LLM multi-agent collaboration as a holistic optimization problem over both agent functionality and collaboration structure. This is a natural progression from hand-built agent systems toward systematic search over roles, communication, and coordination.

The deeper theme is that multi-agent systems have an architecture of interaction. Optimizing only the individual prompts or models misses the system-level behavior produced by communication topology.

## Emerging Pattern 3: Feasibility Constraints Are Becoming Native to Generative Modeling

Efficient Diffusion via Landing targets nonconvex equality and inequality constraints throughout diffusion sampling. Like quotient-space diffusion, latent spherical flow policies, and constrained robot planners, it treats feasibility as part of the generative process rather than a post-hoc filter.

This matters most for science, robotics, molecules, and safety-critical design, where invalid samples can be useless even if they are visually or statistically plausible.

## Emerging Pattern 4: Harmful Fine-Tuning Requires Mechanistic Defenses

Surgery responds to the same threat surface as Trojan-Speak and Invisible Safety Threat: fine-tuning can change safety behavior. Its proposed defense acts during fine-tuning by regularizing attention-sink divergence, suggesting that internal attention dynamics may separate harmful pattern learning from benign adaptation.

The common pattern is moving safety from surface classifiers into model-internal diagnostics and training-time constraints.

## Emerging Pattern 5: Scientific Tokenization Is Domain-Specific Compression

dnaHNet addresses the mismatch between NLP tokenization and genomic structure by dynamically chunking raw nucleotides into latent tokens. This connects to Mind-Omni's brain tokens and other scientific foundation models: tokenization is no longer a generic preprocessing step, but a learned scientific abstraction.

For long biological sequences, the key tradeoff is preserving meaningful motifs while reducing the cost of long-context modeling.

## Cross-Batch Links

- DRPBench links with CyberGym, SandboxEscapeBench, and code/security benchmarks through executable or semantically grounded software evaluation.
- OMAC links with Unsupervised Partner Design and multi-agent game-dynamics work through interaction-level optimization.
- Efficient Diffusion via Landing links with quotient-space diffusion, HDFlow, and latent spherical flow policy through constraint-aware generation.
- Surgery links with Trojan-Speak and Invisible Safety Threat as a defense-side response to harmful or malicious fine-tuning.
- dnaHNet links with Mind-Omni, Protein Autoregressive Modeling, BioX-Bridge, and MrRoPE through scientific tokenization and long-context efficiency.

## Subthemes to Track

- Concurrent-code data-race prediction.
- Static evaluation for nondeterministic programs.
- Multi-agent collaboration optimization.
- Agent role and topology search.
- Projection-free constrained diffusion.
- Nonconvex feasible-set sampling.
- Attention-sink safety signals.
- Fine-tuning-stage safety regularization.
- Tokenizer-free genomic modeling.
- Adaptive latent chunking for long biological sequences.
