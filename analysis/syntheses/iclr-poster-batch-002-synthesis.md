# ICLR Poster Batch 002 Synthesis

## Papers Covered

- When to Retrain after Drift: A Data-Only Test of Post-Drift Data Size Sufficiency
- PLAGUE: Plug-and-play Framework for Lifelong Adaptive Generation of Multi-turn Exploits
- Orbital Transformers for Predicting Wavefunctions in Time-Dependent Density Functional Theory
- COMPACT: COMPositional Atomic-to-Complex Visual Capability Tuning
- Native Adaptive Solution Expansion for Diffusion-based Combinatorial Optimization

## Shared Thesis

This batch is about making intermediate processes informative. CALIPER decides when post-drift data is sufficient for retraining. PLAGUE decomposes multi-turn attacks into phases that optimize context over time. OrbEvo learns wavefunction evolution as a structured transition operator. COMPACT packs multiple visual capabilities into each instruction-tuning example. NEXCO makes combinatorial diffusion states into feasible partial solutions. Across the batch, progress comes from treating the path between start and finish as the object to model, test, or optimize.

## Deep Themes

### Adaptive Progression Under Constraints

CALIPER and NEXCO both ask when to move forward. CALIPER moves from drift detection to retraining only when post-drift evidence is sufficient. NEXCO expands partial solutions through confidence and feasibility projection. Both replace fixed schedules with data- or instance-adaptive progression.

### Long-Horizon Process Vulnerability and Control

PLAGUE shows that attack success in LLMs depends on multi-turn context shaping, not just one-shot prompts. OrbEvo faces a benign but related long-horizon problem: autoregressive rollout error in quantum dynamics. In both cases, the system's intermediate state history controls final behavior.

### Capability Density in Data and Representations

COMPACT compresses visual instruction tuning by making each example compositionally rich. OrbEvo uses physically structured wavefunction and density-matrix representations. NEXCO makes intermediate diffusion states semantically meaningful. These papers all increase the density of useful information per training sample or inference step.

## Cross-Paper Pattern

The cross-paper pattern is structured intermediates. Post-drift windows, attack contexts, wavefunction states, visual questions, and partial combinatorial solutions are not incidental artifacts; they are where the method exerts control. This matches the broader 2026 corpus shift toward process-level supervision, diagnostics, and decoding.

## Subthemes to Track

- Post-drift data sufficiency.
- Multi-turn jailbreak planning.
- Equivariant quantum dynamics prediction.
- Compositional visual instruction tuning.
- Native diffusion decoding for constrained optimization.
- Intermediate states as controllable evidence.

## Confidence and Source Depth

These notes are based on abstracts and local metadata. Full-paper upgrades should inspect theoretical assumptions, attack protocols, TDDFT datasets, synthetic question generation, solver benchmarks, and source-code availability.
