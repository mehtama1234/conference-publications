# ICLR Oral Batch 038 Synthesis

## Papers Covered

- Learning to See Before Seeing: Demystifying LLM Visual Priors from Language Pre-training
- The Spacetime of Diffusion Models: An Information Geometry Perspective
- AdAEM: An Adaptively and Automated Extensible Evaluation Method of LLMs' Value Difference
- Scaling Atomistic Protein Binder Design with Generative Pretraining and Test-Time Compute
- mCLM: A Modular Chemical Language Model that Generates Functional and Makeable Molecules

## Shared Thesis

This batch is about hidden structure that becomes useful when exposed through the right representation or evaluation loop. Visual priors are latent in text-only LLM pretraining. Diffusion geometry becomes meaningful when represented as latent spacetime. LLM value differences become visible through adaptive question generation. Protein binders improve when a generative prior is refined with test-time compute. Molecule generation becomes actionable when the language is built from synthesis-compatible modules. Across the batch, progress comes from discovering and operationalizing latent priors.

## Deep Themes

### Pretraining Creates Latent Cross-Modal Priors

The visual-priors paper argues that text-only pretraining can produce transferable visual reasoning ability, especially from reasoning-centric corpora. This complicates the boundary between unimodal and multimodal learning: later visual alignment may activate capacities already formed in language pretraining.

### Geometry Depends on the State Representation

The diffusion spacetime paper shows that standard latent choices can make geometry degenerate or misleading. Adding noise scale/time to the latent state creates a nontrivial Fisher-Rao geometry and a principled edit distance. This fits the corpus-wide representation-geometry theme.

### Adaptive Evaluation for Moving Targets

AdAEM treats value evaluation as a co-evolving process. Instead of relying on fixed value questions, it probes model boundaries and generates more informative controversial prompts. This mirrors dynamic agent benchmarks and subjective alignment measures elsewhere in the corpus.

### Scientific Generation Needs Test-Time Objectives

Complexa and mCLM both emphasize that scientific generation must satisfy more than likelihood or visual plausibility. Binder design needs atomistic interfaces and test-time optimization; molecule generation needs functional properties and makeability. Both papers encode real-world constraints directly into the generation process.

## Cross-Paper Pattern

The common pattern is representation plus constraint. Text corpora encode visual priors, but they need decomposition. Diffusion latents need time/noise state to carry geometry. Value evaluation needs adaptive question constraints. Protein binders need a generative prior constrained by structural optimization. Molecules need tokens constrained by modular synthesis. Each paper asks what representation makes the hidden objective controllable.

## Subthemes to Track

- Visual priors from language pretraining.
- Diffusion latent spacetime geometry.
- Adaptive value-difference evaluation.
- Generative pretraining plus test-time protein design.
- Modular synthesis-compatible molecule language.

## Confidence and Source Depth

These notes are based on abstracts and local metadata. Formal details, validation protocols, and benchmark settings should be upgraded when PDFs are available.
