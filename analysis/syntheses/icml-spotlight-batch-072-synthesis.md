# ICML 2026 Spotlight Batch 072 Synthesis

## Scope

This synthesis covers ICML 2026 spotlight notes 356-360:

- Real-Time Visual Attribution Streaming in Thinking Model
- VideoKR: Towards Knowledge- and Reasoning-Intensive Video Understanding
- POET-X: Memory-efficient LLM Training by Scaling Orthogonal Transformation
- WaterSIC: Information-Theoretically (Near) Optimal Linear Layer Quantization
- Symmetry Reveals Layerwise Dynamics: How Transformers Perform In-Context Classification

Source depth: abstract/metadata only for all five papers. ArXiv acquisition remains deferred after repeated rate-limit/service failures; these papers should be retried later from offset 355.

## Emerging Pattern 1: Multimodal Reasoning Needs Both Better Data and Better Process Visibility

Real-Time Visual Attribution streams grounding evidence while a thinking model reasons. VideoKR builds a large human-in-the-loop corpus and expert benchmark for knowledge-intensive video understanding.

Together, they show two complementary routes to robust multimodal reasoning: create training data that demands deeper capabilities, then expose whether the model's reasoning is actually grounded in visual evidence.

## Emerging Pattern 2: Efficiency Work Is Moving From Heuristics to Structural Guarantees

POET-X uses orthogonal-equivalence training to preserve stability while reducing training memory and compute. WaterSIC uses information-theoretic rate allocation to quantize linear layers near the optimal limit.

Both papers are efficiency papers, but neither is merely a faster implementation. They encode mathematical structure, spectral preservation or rate-distortion allocation, into systems mechanisms.

## Emerging Pattern 3: Interpretability Benefits From the Right Constraints

Visual Attribution learns a fast estimator for causal region effects. Symmetry Reveals Layerwise Dynamics imposes permutation equivariance to make Transformer in-context classification identifiable.

The shared lesson is that interpretability often requires restricting or instrumenting the system so the relevant causal or algorithmic variables become visible.

## Emerging Pattern 4: Data, Hardware, and Theory Are Co-Optimized

VideoKR treats data as the bottleneck for video reasoning. POET-X treats optimizer memory as the bottleneck for billion-parameter training. WaterSIC treats bit allocation as the bottleneck for low-precision deployment. Symmetry work treats redundant degrees of freedom as the bottleneck for mechanistic understanding.

The batch shows mature ML engineering becoming bottleneck-specific: progress depends on identifying the scarce resource, then designing the objective around it.

## Emerging Pattern 5: Process-Level Evidence Is Becoming User-Facing

Attribution streaming turns grounding into something users can observe during generation. VideoKR-Eval tries to prevent models from passing through textual shortcuts. Symmetry-based analysis extracts an internal update rule rather than treating in-context learning as a black box.

This links evaluation, interpretability, and trust into one process-evidence theme.

## Cross-Batch Links

- Real-Time Visual Attribution connects to MoCA, Agent0-VL, Monitoring Monitorability, and NAD.
- VideoKR connects to MADQA, VenusBench-Mobile, Agent0-VL, and multimodal data curation.
- POET-X connects to ReQAT, WaterSIC, MACKO-SpMV, EMP, and Incremental BPE.
- WaterSIC connects to ReQAT, POET-X, MACKO-SpMV, and FlashSketch.
- Symmetry Reveals Layerwise Dynamics connects to Context-Parameter Equivalence, Constrained Transformers, Modern Conservation Laws, OENN/CENN, and Fisher Memory Dynamics.

## Deep Theme Update

Batch 072 strengthens three major cross-corpus themes: multimodal models need grounded process evidence, efficiency gains increasingly come from mathematically structured allocation, and interpretability often emerges when symmetries or causal targets make the hidden computation identifiable.
