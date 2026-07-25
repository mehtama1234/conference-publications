# Suppress and Diversify: Refining Robust Pathways for Corruption Robustness

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: Tam54Owz7G
- Authors: Jiangang Yang; Wenhui Shi; Xiaoran Xu; Wenyue Chong; Luqing Luo; Jing Xing; Jian Liu
- Primary area: deep_learning->robustness
- Keywords: model robustness; image corruptions
- Source URL: https://openreview.net/forum?id=Tam54Owz7G
- PDF URL: https://openreview.net/pdf?id=Tam54Owz7G

## Abstract

Model robustness against natural image corruptions is essential for safety-critical applications. While existing methods primarily focus on implicit representation learning, we provide the first systematic exploration of computational pathways to explicitly characterize internal robustness. We identify a progressive decay of robust features across network layers and establish a functional dependency between the prevalence of these features and model performance. To exploit these insights, we propose Suppress and Diversify (S\&D), a non-intrusive refinement approach that enhances robustness by dynamically selecting robust pathways and diversifying them through symmetry-preserving transformations. S\&D is architecture-agnostic, parameter-free, and incurs zero test-time overhead. Extensive evaluations across eight benchmarks demonstrate that S\&D consistently improves performance across multiple vision tasks, diverse backbones, and complex real-world scenarios, highlighting its broad efficacy and scalability.

## One-Sentence Claim

Corruption robustness can be improved by identifying decaying robust computational pathways inside networks, suppressing fragile pathways, and diversifying robust ones without changing architecture or adding test-time cost.

## Problem

Natural image corruptions threaten reliability in safety-critical vision systems. Many robustness methods improve representations implicitly, but they do not explicitly characterize which internal computational pathways carry robust features or how those pathways evolve across depth.

The paper asks whether robustness can be diagnosed and refined by intervening on internal pathways rather than relying only on external data augmentation or architectural changes.

## Core Contribution

The paper reports a systematic exploration of computational pathways for corruption robustness. It identifies progressive decay of robust features across layers and a functional dependency between robust-feature prevalence and model performance.

Based on this, it proposes Suppress and Diversify, or S&D, a non-intrusive refinement method that dynamically selects robust pathways and diversifies them via symmetry-preserving transformations. The method is described as architecture-agnostic, parameter-free, and zero-overhead at test time.

## Method

The method appears to first analyze internal pathways to determine which parts of the network preserve robust features. S&D then suppresses less robust pathways and diversifies selected robust pathways using transformations that preserve relevant symmetries.

Because the approach is parameter-free and non-intrusive, it likely operates as a training or refinement procedure rather than an added inference module.

## Experiments and Evidence

Evidence reported in the abstract:

- Systematic pathway analysis showing robust features decay progressively across network layers.
- Functional relation between robust-feature prevalence and performance.
- Eight robustness benchmarks.
- Improvements across multiple vision tasks, diverse backbones, and complex real-world scenarios.
- Zero test-time overhead and architecture-agnostic behavior.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: pathway definition, transformation family, benchmark names, corruption severities, and whether clean accuracy is preserved.

## Limits and Failure Modes

- "Robust pathway" needs formal definition; the abstract does not reveal whether it is causal or correlational.
- Parameter-free methods can be attractive but may hide sensitivity in pathway thresholds or preprocessing choices.
- Symmetry-preserving transformations may not cover corruptions that break assumed symmetries.
- Zero test-time overhead does not imply zero training/refinement cost.

## Deep Themes

**Robustness can be localized inside computation.** The paper treats robustness as something carried by internal pathways, not only as an aggregate test metric.

**Interventions should preserve useful symmetries.** Diversification is constrained so it does not destroy task-relevant invariances.

**No-overhead robustness is an important deployment target.** The method tries to improve reliability without making inference heavier.

## Subthemes

- Pathway-level robustness diagnostics.
- Progressive robust-feature decay across layers.
- Dynamic robust-pathway selection.
- Symmetry-preserving diversification.
- Architecture-agnostic refinement.

## Connections to Other Papers

Connects to Consistent Adversarial Attacks, DISCO, FeatJND, and DOUBT through robustness as separation of stable signal from brittle or spurious computation. It also links to interpretability-as-intervention work because internal-pathway identification becomes an actionable control point.

## Notes for Cross-Paper Synthesis

S&D adds to a pattern where robustness papers move inward: rather than only measuring failures at the output, they identify internal channels, features, pathways, or dependencies that should be suppressed, diversified, or regularized.
