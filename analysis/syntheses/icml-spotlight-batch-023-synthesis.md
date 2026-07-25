# ICML 2026 Spotlight Batch 023 Synthesis

## Scope

This synthesis covers ICML 2026 spotlight notes 111-115:

- CVE-Factory: Scaling Expert-Level Agentic Tasks for Code Security Vulnerability
- Safety Alignment of LMs via Non-cooperative Games
- Shared Semantics, Divergent Mechanisms: Unsupervised Feature Discovery by Aligning Semantics and Mechanisms
- SpatioLM: Towards General Physical Spatial Intelligence in Vision-Language Models
- OSM+: Billion-Level Open Street Map Dataset for City-wide Experiments

Source depth: abstract/metadata only for all five papers. ArXiv acquisition remains deferred after repeated rate-limit/service failures; these papers should be retried later from offset 110.

## Emerging Pattern 1: Security Evaluation Is Becoming Environment Generation

CVE-Factory automates the transformation of sparse CVE metadata into executable vulnerability tasks. This is the same living-benchmark impulse seen in Jailbreak Foundry, but applied to code security environments rather than prompt attacks. The downstream result is not only a benchmark, LiveCVEBench, but also a large pool of training environments.

The pattern is clear: security progress needs runnable worlds. Static descriptions are not enough for evaluating and improving agents that operate through terminals, repositories, and exploit chains.

## Emerging Pattern 2: Safety Alignment Is Becoming Co-Evolutionary

AdvGame frames safety alignment as a non-zero-sum game between an attacker LM and defender LM trained jointly online. This contrasts with sequential adversarial training, where attack discovery and defense updates happen in separate phases.

This links to constrained Nash equilibria, ParetoPO, and debate-collapse mitigation. Safety and alignment are increasingly modeled as strategic processes between adaptive agents, not one-directional fine-tuning.

## Emerging Pattern 3: Interpretability Is Moving from Targets to Distributions

Shared Semantics, Divergent Mechanisms argues that target-conditioned circuit analysis can hide heterogeneity in the continuation distribution. Its unsupervised feature discovery clusters continuations by both semantic embeddings and mechanistic attribution signatures.

This extends SVD interpretability, activation oracles, and feature-discovery work. The important subtheme is distribution-level auditing: a model's internal mechanisms may differ across plausible continuations even when the prompt is fixed.

## Emerging Pattern 4: Physical Spatial Intelligence Is Becoming a VLM Specialization

SpatioLM aims to improve spatial reasoning without external 3D encoders or extra 3D priors. It adds a plug-and-play spatial module and uses pseudo depth and camera signals to guide physically coherent representations.

This connects to SAW-Bench, SVL, RoboMME, and dWorldEval. The embodied/spatial cluster is increasingly focused on physical coherence: camera geometry, egocentric pose, 3D representations, and transfer to manipulation.

## Emerging Pattern 5: Dataset Infrastructure Is Scaling to World Graphs

OSM+ processes worldwide OpenStreetMap into a billion-vertex road-network graph with query tools and downstream traffic/policy benchmarks. This is dataset work as infrastructure, not just benchmark curation.

This links to S3GNN, long-range graph learning, and traffic/time-series papers. The challenge is no longer only whether a graph model works on citation networks or small road graphs; it is whether graph learning can operate at city and world scale.

## Cross-Batch Links

- CVE-Factory, Jailbreak Foundry, CyberGym, and DRPBench all turn evaluation into executable software artifacts.
- AdvGame, constrained Nash equilibria, ParetoPO, and multi-agent debate work use game structures to model strategic learning systems.
- Shared Semantics, SVD interpretability, LOES, and activation-oracle work broaden interpretability beyond output behavior.
- SpatioLM, SAW-Bench, SVL, and RoboMME form a strong physical-spatial intelligence cluster.
- OSM+, S3GNN, and time-series/geospatial papers make scale and topology central to real-world graph ML.

## Deep Theme Update

Batch 023 is about operational substrates: executable security environments, attacker-defender games, continuation-distribution audits, physical spatial modules, and world-scale road graphs. Each paper gives a model something more realistic to operate on: a runnable vulnerability, an adaptive opponent, a distribution of possible mechanisms, a physical geometry signal, or a billion-node city graph.
