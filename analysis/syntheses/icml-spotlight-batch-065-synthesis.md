# ICML 2026 Spotlight Batch 065 Synthesis

## Scope

This synthesis covers ICML 2026 spotlight notes 321-325:

- T2PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic Reinforcement Learning
- A Dirac-Frenkel-Onsager Principle: Instantaneous Residual Minimization with Gauge Momentum for Nonlinear Parametrizations of PDE Solutions
- Is Your LLM Overcharging You? Tokenization, Transparency, and Incentives
- Foundations of Equivariant Deep Learning: Unifying Graph and Sheaf Neural Networks
- ReQAT: Achieving Full-Precision Reasoning Accuracy with 4-bit Floating-Point Quantization-Aware Training

Source depth: abstract/metadata only for all five papers. ArXiv acquisition remains deferred after repeated rate-limit/service failures; these papers should be retried later from offset 320.

## Emerging Pattern 1: Fine-Grained Control Prevents Collapse

T2PO controls agent exploration at token and turn levels, intervening when uncertainty stops changing or turns stop making progress. ReQAT protects low-entropy symbolic tokens where quantization noise causes reasoning cascades.

Both papers identify specific fragile points inside a long process and add controls exactly there rather than applying broad regularization.

## Emerging Pattern 2: Gauge Freedom Is a Practical Stabilizer

Dirac-Frenkel-Onsager dynamics interpret parameter non-uniqueness as gauge freedom and inject momentum only along nullspace directions. This preserves residual minimization while improving conditioning.

This connects to PRISM and OCE: non-identifiability is dangerous if ignored but useful when controlled through geometry-preserving directions.

## Emerging Pattern 3: Tokens Are Economic and Computational Objects

Token Overcharging treats token counts as a billing mechanism with strategic incentives. Incremental BPE treated tokenization as streaming infrastructure. ReQAT treats low-entropy tokens as the failure locus of FP4 reasoning.

Across the corpus, tokens are no longer just model inputs. They are units of latency, cost, trust, and numerical fragility.

## Emerging Pattern 4: Symmetry Theory Is Moving Beyond Groups

OENN/CENN unifies graph and sheaf neural networks and extends equivariance to categorical, non-invertible, compositional symmetries. This broadens the geometric-learning toolkit beyond standard group actions and graph message passing.

## Emerging Pattern 5: Reasoning Efficiency Must Preserve Exact Commitments

ReQAT shows low-bit inference can work for reasoning if training focuses on precise symbolic positions and KV-cache transformations. This matches NAD's finding that correctness signals appear early in internal activations: efficient reasoning depends on preserving the right internal events.

## Cross-Batch Links

- T2PO connects to R2VPO, PAVE, Agent0-VL, TG-RAG, NAD, and tau2-bench through process-controlled agent learning.
- Dirac-Frenkel-Onsager connects to Flowers, NeuronCtrl, PRISM, OCE, and scientific PDE/operator papers through gauge-aware dynamics.
- Token Overcharging connects to Incremental BPE, Data Market Pricing, Bayesian Truthful Valuation, and ML governance/economics.
- OENN/CENN connects to ENGNN, RECM, DIGL, Neural Ricci Flow, and language-symmetry geometry through generalized equivariance.
- ReQAT connects to FlashOptim, SmoothSpike, Brain Encoding Scale, Incremental BPE, and NAD through efficient reasoning-preserving infrastructure.

## Deep Theme Update

Batch 065 is about controlling the exact failure points of modern systems: exploration stalls in agent RL, nullspace ambiguity in PDE parameter dynamics, token-count incentives in billing, missing generality in equivariant theory, and low-entropy token errors in quantized reasoning.
