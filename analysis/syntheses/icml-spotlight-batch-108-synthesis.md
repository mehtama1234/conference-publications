# ICML 2026 Spotlight Batch 108 Synthesis

## Papers

- MSP: Probabilistically Consistent Multi-Scale Action Generation

## Source Depth

This note is abstract/metadata-only. arXiv acquisition remains deferred after repeated 429/503 failures across preceding exact-batch attempts. Full-paper details should be verified later from official PDFs or a high-confidence arXiv match.

## Shared Thesis

MSP extends the corpus's embodied-generation theme into robotic imitation learning. The central problem is not only generating plausible actions, but keeping coarse task intent and fine-grained control probabilistically consistent across temporal scales.

## Deep Theme

The paper reinforces a cross-scale consistency pattern already visible in long-horizon reasoning, dynamic graphs, video generation, and world simulation. Systems that operate over extended horizons need abstractions that compress long-range intent without losing the local information required for execution.

## Cross-Batch Connections

MSP connects to VectorWorld through long-horizon embodied simulation and action feasibility; to GLANCE through partially observed agent behavior; to Reverse Flow Matching and DFM theory through flow-based generative control; and to hierarchical RL work through multi-scale temporal abstraction.

## Emerging Pattern

The broader pattern is that hierarchy alone is insufficient. A useful hierarchy must maintain probabilistic agreement between levels so high-level plans, mid-level latent structure, and low-level actions do not drift apart.
