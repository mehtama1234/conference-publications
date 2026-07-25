# ICLR Oral Batch 035 Synthesis

## Papers Covered

- Optimistic Task Inference for Behavior Foundation Models
- Discount Model Search for Quality Diversity Optimization in High-Dimensional Measure Spaces
- Causal Structure Learning in Hawkes Processes with Complex Latent Confounder Networks
- Mean Flow Policy with Instantaneous Velocity Constraint for One-step Action Generation
- Cross-Domain Lossy Compression via Rate- and Classification-Constrained Optimal Transport

## Shared Thesis

This batch is about decision-making when the relevant objective, measure, cause, action distribution, or target domain is not directly available in simple supervised form. OpTI-BFM actively infers reward tasks through test-time interaction. DMS learns a continuous exploration signal for high-dimensional quality-diversity measures. The Hawkes paper recovers causal structure despite latent subprocesses. MFP compresses expressive flow policies into one-step action generation. Cross-domain compression uses optimal transport to balance rate, distortion, perception, and classification when source and target domains differ. The common thread is optimizing under missing or transformed signals.

## Deep Themes

### Test-Time Inference as Data Collection

OpTI-BFM shows that zero-shot RL is not automatically data-efficient. A behavior foundation model still needs to infer the reward task, and optimism provides a principled way to collect the most useful interactions. This aligns with broader test-time adaptation work where small amounts of targeted interaction replace broad offline labeling.

### Continuous Surrogates for High-Dimensional Search

DMS addresses a representational failure in quality-diversity optimization: histograms cannot preserve useful distinctions in high-dimensional measure spaces. A learned discount model becomes a smoother search guide. The larger subtheme is that exploration pressure itself often needs a learned representation.

### Latent Causes in Temporal Systems

The Hawkes causal-discovery paper focuses on the hidden structure behind event streams. By connecting continuous-time events to limiting discrete-time causal models, it provides identifiability conditions and an iterative algorithm for discovering latent subprocesses. This adds temporal causal discovery to the corpus's larger hidden-variable theme.

### One-Step Generative Control

MFP targets the deployment side of expressive generative policies. Flow policies are useful because they represent rich action distributions, but multi-step sampling can be too slow. Modeling mean velocity with an instantaneous velocity constraint is a way to keep expressiveness while making action selection fast.

### Multi-Objective Information Tradeoffs

The cross-domain compression paper formalizes restoration-like compression as optimal transport between degraded source and target distributions. The key idea is that compression quality is not just distortion: classification utility and perceptual plausibility are explicit constraints in the tradeoff.

## Cross-Paper Pattern

The shared pattern is replacing unavailable direct supervision with structured proxy signals. Reward uncertainty guides OpTI-BFM interaction. A continuous discount model guides DMS exploration. Path-based identifiability guides latent Hawkes discovery. An instantaneous velocity constraint guides one-step flow policies. Rate, classification, and perception constraints guide cross-domain transport. Each paper turns a hard-to-observe objective into a more structured optimization signal.

## Subthemes to Track

- Optimistic task inference for BFMs.
- High-dimensional quality-diversity search.
- Latent-confounder causal discovery in Hawkes processes.
- One-step mean-flow policies.
- Rate-distortion-perception-classification optimal transport.

## Confidence and Source Depth

These notes are based on abstracts and local metadata. Formal details, validation protocols, and benchmark settings should be upgraded when PDFs are available.
