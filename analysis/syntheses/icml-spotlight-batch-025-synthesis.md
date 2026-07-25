# ICML 2026 Spotlight Batch 025 Synthesis

## Scope

This synthesis covers ICML 2026 spotlight notes 121-125:

- Reinforced Sequential Monte Carlo for Amortised Sampling
- Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers
- Are VLMs Seeing or Just Saying? Uncovering the Illusion of Visual Re-examination
- Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling
- Judging What We Cannot Solve: A Consequence-Based Approach for Oracle-Free Evaluation of Research-Level Math

Source depth: abstract/metadata only for all five papers. ArXiv acquisition remains deferred after repeated rate-limit/service failures; these papers should be retried later from offset 120.

## Emerging Pattern 1: Sampling Is Becoming Hybrid Learned-Classical Infrastructure

Reinforced SMC links maximum-entropy RL-trained neural samplers with sequential Monte Carlo. Learned policies become proposal kernels, value functions become twist functions, and SMC samples become off-policy training data.

This connects to Rex, Autoregressive Boltzmann Generators, and scientific sampling papers. The pattern is that high-quality sampling is increasingly a hybrid system: learned amortization plus classical correction, tempering, replay, or importance weighting.

## Emerging Pattern 2: Interpretability Is Becoming Queryable

Activation Oracles turn activations into inputs for LLMs that answer natural-language questions. The striking claim is that these systems can recover fine-tuned information, including hidden propensities, even when it is not present in the prompt text.

This extends SVD interpretability, distribution-level feature discovery, and activation-oracle-style auditing. The model internals are becoming something another model can interrogate, not just something an analyst visualizes.

## Emerging Pattern 3: Multimodal Reasoning Text Can Be Performative

VISUALSWAP tests whether VLMs that say they are re-checking an image actually increase visual grounding. The answer in the abstract is mostly no: self-generated reflective statements do not raise visual-token attention, while explicit user instructions do.

This connects to SAW-Bench, SpatioLM, UniPercept, and visual grounding benchmarks. The broader lesson is that chain-of-thought language can create an illusion of process. Evaluation needs to verify whether the claimed process is causally active.

## Emerging Pattern 4: Reward Models Need Interpretable Latent Structure

BNRM attacks reward hacking through Bayesian non-negative latent factors. The paper's design separates instance-specific reward factors from sparse global debiasing factors, making reward learning both uncertainty-aware and more interpretable.

This links to Binary RAR, RGR-GRPO, RLHF regularization theory, and DPO/RLHF equivalence. Across the alignment papers, reward design is moving away from opaque scalar preference scores and toward structured, uncertainty-aware, incentive-conscious models.

## Emerging Pattern 5: Evaluation Can Use Consequences When Direct Answers Are Unavailable

Consequence-Based Utility evaluates research-level math solutions by using them as exemplars for related verifiable questions. If a candidate solution contains real method-level insight, it should improve downstream solving in a neighborhood of tasks.

This connects to post-comprehension benchmarking and critique-resilient evaluation. The shared challenge is how to judge model outputs when ground truth is scarce, expensive, or beyond ordinary human comprehension. Consequences provide an indirect but testable signal.

## Cross-Batch Links

- Reinforced SMC, Rex, and Boltzmann generation papers make sampling/solver infrastructure central to scientific ML.
- Activation Oracles, Shared Semantics, SVD interpretability, and LOES show interpretability becoming scalable and queryable.
- VISUALSWAP, SAW-Bench, SpatioLM, and UniPercept test whether multimodal models are grounded in the perceptual evidence they claim to use.
- BNRM, Binary RAR, and RGR-GRPO all focus on reward shaping that avoids pathological incentives.
- Consequence-Based Utility, Benchmarking at the Edge of Comprehension, and oracle-free evaluation reframe correctness as adversarial, consequential, or indirectly verifiable.

## Deep Theme Update

Batch 025 is about indirect evidence. SMC particles provide evidence for better sampler training. Activation questions provide evidence about hidden model state. Image swaps provide evidence about whether visual attention is actually used. Non-negative reward factors provide evidence about reward biases. Related math problems provide evidence about a solution's method-level validity. The corpus is increasingly rich in methods that infer what cannot be observed directly.
