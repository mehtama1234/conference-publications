# ICML 2026 Spotlight Batch 083 Synthesis

## Scope

This synthesis covers ICML 2026 spotlight notes 411-415:

- STAR-KV: Low-Rank KV Cache Compression via Soft Thresholding for Adaptive Rank Control
- Vision2Web: A Hierarchical Benchmark for Visual Website Development with Agent Verification
- PLAINTAIN: Plan-Answer Interleaved Reasoning
- From Poisoned to Aware: Fostering Backdoor Self-Awareness in LLMs
- OPUS: Towards Efficient and Principled Data Selection in Large Language Model Pre-training in Every Iteration

Source depth: abstract/metadata only for all five papers. ArXiv acquisition remains deferred after repeated rate-limit/service failures; these papers should be retried later from offset 410.

## Emerging Pattern 1: Intermediate State Is Becoming the Optimization Target

STAR-KV compresses KV cache states adaptively. PLAINTAIN changes the visible intermediate reasoning state. Backdoor self-awareness trains the model to articulate hidden trigger states. OPUS scores candidate data by optimizer-induced update state.

The common pattern is that ML systems are optimizing internal and intermediate objects, not only final outputs.

## Emerging Pattern 2: Agent Evaluation Is Moving Toward Executable Workflows

Vision2Web evaluates visual website development from static UI reproduction to full-stack long-horizon tasks, with GUI and VLM-based verification. This connects directly to RoTS, ThunderAgent, daVinci-Dev, and VenusBench-Mobile.

The benchmark direction is clear: agent claims increasingly need executable, workflow-aware verification rather than static examples.

## Emerging Pattern 3: Reasoning Interfaces Are Being Designed for Intervention

PLAINTAIN externalizes plans before full reasoning completes, reducing time-to-first-response and enabling early correction. Critique-GRPO and Weak-Strong Verification similarly use process signals to intervene before final failure.

This creates a user-facing process-control theme: the system should expose enough structure for feedback while preserving reasoning capacity.

## Emerging Pattern 4: Safety Work Is Learning to Inspect Hidden Failure Conditions

Backdoor self-awareness is the defensive counterpart to Rapid Poison. One paper attacks adaptive safety data pipelines; the other trains poisoned models to articulate triggers.

Both imply that hidden conditions in training or behavior must become explicit artifacts for safety governance.

## Emerging Pattern 5: Efficiency Is Becoming Adaptive and Geometry-Aware

STAR-KV adapts rank by attention head and block, then combines low-rank compression with quantization. OPUS scores data in the optimizer-induced update geometry. Both reject one-size-fits-all heuristics.

The broader theme is adaptive allocation: memory rank, bits, data tokens, and training updates are all resources to distribute where marginal utility is highest.

## Cross-Batch Links

- STAR-KV connects to CONTINUUM, ThunderAgent, WaterSIC, QAT Scaling, ReQAT, and MACKO-SpMV.
- Vision2Web connects to RoTS, ThunderAgent, daVinci-Dev, VenusBench-Mobile, and MADQA.
- PLAINTAIN connects to Critique-GRPO, Weak-Strong Verification, Monitoring Monitorability, and process-visible reasoning.
- Backdoor self-awareness connects to Rapid Poison, Monitoring Monitorability, and robustness/safety papers.
- OPUS connects to PRISM, Source Screening, VideoKR, daVinci-Dev, and training-data governance.

## Deep Theme Update

Batch 083 emphasizes adaptive control of hidden infrastructure: KV caches, website-development workflows, reasoning plans, backdoor triggers, and optimizer-induced data utility all become explicit surfaces for intervention.
