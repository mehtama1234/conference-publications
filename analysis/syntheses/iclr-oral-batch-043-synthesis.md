# ICLR Oral Batch 043 Synthesis

## Papers Covered

- Extending Sequence Length is Not All You Need: Effective Integration of Multimodal Signals for Gene Expression Prediction
- Multiplayer Nash Preference Optimization
- CauKer: Classification Time Series Foundation Models Can Be Pretrained on Synthetic Data
- Overparametrization bends the landscape: BBP transitions at initialization in simple Neural Networks
- RealPDEBench: A Benchmark for Complex Physical Systems with Real-World Data

## Shared Thesis

This batch is about replacing naive scale with structured evidence. Prism argues that longer DNA context is weaker than confounding-aware multimodal regulatory integration. MNPO replaces scalar or two-player preference optimization with a multiplayer equilibrium view. CauKer uses causally coherent synthetic time series to make pretraining scalable and predictable. The BBP-transition paper analyzes how overparameterization changes the geometry of signal recovery. RealPDEBench insists that scientific ML be evaluated on paired real measurements and simulations. Across the batch, the move is from "more" to "better structured": better signals, better preference games, better synthetic generators, better theory, and better benchmarks.

## Deep Themes

### Scale Needs Structure

Prism and the intrinsic-entropy context work from the prior batch both reject simple context expansion as a default answer. Prism shows long DNA sequences can harm gene-expression prediction if multimodal epigenomic signals are not integrated correctly. CauKer and RealPDEBench make a parallel point for scientific and temporal data: scaling pretraining is useful when the data-generation or evaluation structure is meaningful.

### Synthetic and Simulated Data as Controlled Infrastructure

CauKer and RealPDEBench form a productive tension. CauKer shows synthetic data can produce clear scaling laws for time-series foundation models. RealPDEBench shows simulation-only validation misses discrepancies visible in real measurements. Together they suggest that synthetic and simulated data are best treated as controlled infrastructure, not as a replacement for real-world grounding.

### Optimization Geometry and Preference Geometry

MNPO and the BBP-transition paper both study geometry, but at different levels. MNPO studies the geometry of preference competition across a population of policies. The BBP paper studies the spectral geometry of initialization and signal recovery. Both show that richer structure changes what can be optimized or recovered.

## Cross-Paper Pattern

The common pattern is structured correction. Prism corrects multimodal confounding. MNPO corrects single-opponent preference bias. CauKer corrects irregular real-data scaling with causal synthetic generation. The BBP analysis corrects flat intuitions about overparameterization by showing phase-transition shifts. RealPDEBench corrects simulation-only evaluation with paired real-world measurements. Each paper adds a missing structural layer that makes learning behavior more interpretable or deployable.

## Subthemes to Track

- Confounding-aware multimodal genomics.
- Multiplayer preference optimization.
- Causally coherent synthetic time-series generation.
- BBP transitions and Hessian spectra at initialization.
- Real-world PDE benchmarks with paired simulations.
- Sim-to-real gaps in scientific ML.

## Confidence and Source Depth

These notes are based on abstracts and local metadata. Full-paper upgrades should check causal assumptions, equilibrium derivations, synthetic generator details, finite-size theory, benchmark composition, and metric definitions.
