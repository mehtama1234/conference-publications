# ICML 2026 Spotlight Batch 085 Synthesis

## Scope

This synthesis covers ICML 2026 spotlight notes 421-425:

- mHC: Manifold-Constrained Hyper-Connections
- On the Accuracy of Newton Step and Influence Function Data Attributions
- Causal Modeling of Selection in Evolution
- Don't Force the Fit: Bounded Log-Likelihood Loss for Enhanced Reasoning in Large Language Models
- Measuring Agents in Production

Source depth: abstract/metadata only for all five papers. ArXiv acquisition remains deferred after repeated rate-limit/service failures; these papers should be retried later from offset 420.

## Emerging Pattern 1: Stability Often Comes From Preserving the Right Local Invariant

mHC restores the identity mapping property inside widened Hyper-Connections. Newton-step attribution replaces global assumptions with local curvature around the first Newton step. Both papers argue that the useful guarantee is local and structural, not generic.

This continues a strong ICML theme: scalable methods work when hidden invariants are protected.

## Emerging Pattern 2: Data Governance Needs Better Counterfactual Approximation

Influence functions and Newton steps approximate what happens if points are removed. OPUS estimates which data produce useful optimizer-shaped updates. Source Screening selects source subsets. These papers treat training data as an intervention surface.

The key distinction in this batch is accuracy: attribution approximations need local guarantees before being trusted for unlearning, valuation, or debugging.

## Emerging Pattern 3: Causal Modeling Must Match the Generating Process

Evolutionary selection is not static selection; repeated reproduction creates a different causal structure. This links to DiCoLa, Unpaired Causal IV, and Fair Causal Bandits, all of which show that causal assumptions must match how data were produced.

The broader causal theme is process-specific modeling.

## Emerging Pattern 4: Objective Design Should Avoid Overfitting Surface Realizations

BLL-Loss argues that SFT should not force low-probability reasoning tokens that encode stylistic or realization-specific variation. This connects to RePO, DPO Unchained, and Identity Bridge: task-aligned objectives often require changing how data are interpreted.

For reasoning, exact token imitation can be the wrong target.

## Emerging Pattern 5: Production Agents Are Simpler and More Human-Governed Than Research Narratives

MAP finds production agents are mostly short-horizon, prompt-based, and human-evaluated. This contextualizes Vision2Web, RoTS, ThunderAgent, and MADQA: long-horizon autonomy is still hard, and reliability is handled through systems and oversight.

## Cross-Batch Links

- mHC connects to NorMuon, Constrained Transformers, POET-X, and architecture-stability work.
- Newton-step attribution connects to OPUS, Source Screening, unlearning, and data valuation themes.
- Evolutionary selection connects to DiCoLa, Unpaired Causal IV, OU Identifiability, and causal fairness.
- BLL-Loss connects to RePO, Critique-GRPO, PRISM, DPO Unchained, and Identity Bridge.
- MAP connects to ThunderAgent, Vision2Web, RoTS, MADQA, VenusBench-Mobile, and production-agent measurement.

## Deep Theme Update

Batch 085 closes this stub window with a practical warning: stable architectures, accurate attributions, valid causal assumptions, aligned objectives, and realistic agent measurement all depend on modeling the actual process rather than relying on convenient abstractions.
