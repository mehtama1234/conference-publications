# ICML 2026 Spotlight Batch 073 Synthesis

## Scope

This synthesis covers ICML 2026 spotlight notes 361-365:

- Minimax Optimal Strategy for Delayed Observations in Online Reinforcement Learning
- Provable Bounds for the Learnability of Sample-Compressible Families from Noisy Samples
- End-to-End Autoregressive Image Generation with 1D Semantic Tokenizer
- Scaling Law for Quantization-Aware Training
- Correcting Split Selection in Online Decision Trees via Anytime-Valid Inference

Source depth: abstract/metadata only for all five papers. ArXiv acquisition remains deferred after repeated rate-limit/service failures; these papers should be retried later from offset 360.

## Emerging Pattern 1: Statistical Guarantees Must Match the Real Observation Process

Delayed-observation RL changes what an agent knows when it acts. Anytime-valid online trees correct the mismatch between fixed-sample guarantees and adaptive stopping. Noisy sample-compressible learning asks when compressed distribution structure remains recoverable after perturbation.

Across these papers, the central issue is not a new model architecture but the validity of learning when feedback is delayed, adaptively gathered, or corrupted.

## Emerging Pattern 2: Compression and Quantization Are Becoming Allocation Problems

QAT scaling laws model quantization error over model size, token count, and group size. WaterSIC from the previous batch allocates rates across columns based on activation covariance. POET-X uses structural reparameterization to reduce training memory.

This batch extends the efficiency theme: the scarce resource may be bits, memory, training tokens, or statistical confidence, and the solution is to allocate it where marginal damage is lowest.

## Emerging Pattern 3: Latent Interfaces Shape Generative Quality

The 1D semantic tokenizer paper collapses the tokenizer-generator boundary so generation quality supervises token formation. This links to quantization work because both tokenizers and quantizers define compressed internal interfaces.

The common pattern is interface alignment: representation bottlenecks should be optimized for the downstream computation they serve, not only for local reconstruction or compression metrics.

## Emerging Pattern 4: Bigger Data Can Create New Compression Error

The QAT scaling law reports that quantization error can rise with more training tokens, and weight error can eventually exceed activation error. That is a useful counterpoint to simple scale optimism: more data and larger models can change which approximation error dominates.

The result connects with WaterSIC and EMP by showing that compression policy must adapt as model and data scale move.

## Emerging Pattern 5: Adaptivity Is a Source of Both Power and Invalidity

Delayed RL, anytime-valid trees, and weak-strong verification all use adaptive decisions. But adaptivity breaks naive guarantees unless the analysis explicitly includes it.

This is a deep cross-corpus theme: many modern ML systems are loops, not one-shot predictors, so their evidence model must be sequential.

## Cross-Batch Links

- Delayed-observation RL connects to T2PO, Mean-Expansion Q-Learning, Distributional IRL, and online inference-control papers.
- Sample-compressible noisy learning connects to Source Screening, CreDRO, GFD-EMVC, and Finite Test Certification.
- End-to-end image tokenization connects to MOG, KPE/KTS, Tilt Matching, and representation-bottleneck work.
- QAT scaling connects to WaterSIC, ReQAT, MACKO-SpMV, EMP, and POET-X.
- Anytime-valid online trees connect to Weak-Strong Verification, Finite Test Certification, Token Overcharging, and delayed-feedback learning.

## Deep Theme Update

Batch 073 shows a strong statistical-systems pattern: when learning becomes delayed, compressed, noisy, quantized, or adaptively stopped, classical assumptions quietly fail. The papers repair those failures by aligning guarantees with the actual information path.
