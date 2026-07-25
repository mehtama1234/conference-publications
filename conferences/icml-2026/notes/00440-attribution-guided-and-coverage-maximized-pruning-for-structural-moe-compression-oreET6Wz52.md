# Attribution-Guided and Coverage-Maximized Pruning for Structural MoE Compression

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: oreET6Wz52
- Authors: Yifu Ding; jiacheng wang; Ge Yang; Yongcheng Jing; Jinyang Guo; Xianglong Liu; Dacheng Tao
- Primary area: deep_learning->large_language_models
- Keywords: Mixture-of-Experts (MoE);Structured Pruning;First-Order Approximation;Hardware-Aware Alignment
- Source URL: https://openreview.net/forum?id=oreET6Wz52
- PDF URL: https://openreview.net/pdf?id=oreET6Wz52

## Abstract

Mixture-of-Experts (MoE) models scale compute efficiently, yet they remain expensive to deploy due to substantial memory footprint and inference overhead. Prior methods mainly operate at the expert level, either removing whole experts or ranking experts by importance. However, such expert-wise decisions are too coarse to identify redundancy, and often misallocate pruning budgets and limits compression. This issue worsens in large MoEs with dynamic routing and heterogeneous experts. To alleviate this dilemma, we for the first time observe that information in MoE experts is highly concentrated in a few channels, leaving substantial redundancy even in "high importance" experts. Accordingly, we propose a structural pruning framework tailored for MoEs, reforming the prune-ratio objective to maximizing channel-score coverage via an efficient attribution-based approximation. Experiments on DeepSeek and Qwen MoEs retain accuracy under 50\% or 25\% pruning joinly with 4-bit quantization, reducing the memory footprint of Qwen3-30B-A3B by 5.27$\times$, and outperforming state-of-the-art baselines under diverse benchmarks.

## One-Sentence Claim

MoE models can be compressed more effectively by pruning redundant expert channels with attribution-guided coverage maximization rather than dropping whole experts.

## Problem

Mixture-of-Experts models improve compute scaling, but deployment remains costly because expert weights create large memory footprints and inference overhead. Existing compression methods often make coarse expert-level decisions: remove entire experts or rank experts by global importance.

That granularity is too blunt for large MoEs with heterogeneous experts and dynamic routing. Even important experts can contain redundant channels, so expert-wise pruning may preserve unneeded parameters while deleting useful specialized capacity elsewhere.

## Core Contribution

The paper observes that information within MoE experts is concentrated in a small number of channels. It proposes a structural MoE pruning framework that reformulates pruning as channel-score coverage maximization using an efficient attribution-based approximation.

The contribution is to move compression from expert selection to within-expert structural pruning. This allows the method to preserve useful expert coverage while removing redundant channels, and to combine pruning with low-bit quantization.

## Method

The method estimates channel importance through a first-order attribution approximation, then allocates pruning ratios to maximize coverage of high-scoring channels across the MoE. Rather than assigning a uniform or expert-level budget, it adapts pruning to the distribution of informative channels.

The framework is hardware-aware, aligning structural pruning choices with deployable dimensions, and is evaluated jointly with 4-bit quantization. This is important because theoretical sparsity does not automatically translate into memory or latency gains.

## Experiments and Evidence

The abstract reports experiments on DeepSeek and Qwen MoE models. The method retains accuracy under 50 percent or 25 percent pruning combined with 4-bit quantization, reduces the memory footprint of Qwen3-30B-A3B by 5.27x, and outperforms state-of-the-art baselines across diverse benchmarks.

Full-paper reading should verify exact benchmark set, latency results, calibration data requirements, expert/channel utilization analysis, and whether accuracy retention differs across reasoning, coding, and knowledge tasks.

## Limits and Failure Modes

Attribution approximations can be brittle when calibration data is narrow or when expert routing changes after pruning. Channel-level pruning may also interact unexpectedly with quantization, activation outliers, and hardware kernels.

The method compresses existing MoEs but does not remove the need for careful deployment validation. Sparse or pruned structures must still map to efficient kernels; otherwise memory savings may not yield proportional runtime improvements.

## Deep Themes

- Fine-grained MoE compression: redundancy exists inside experts, not only between experts.
- Attribution as deployment tooling: interpretability-style scores guide structural model surgery.
- Coverage-preserving pruning: compression should preserve the diversity of useful expert channels.
- Compression plus quantization: practical efficiency comes from combining structural and numeric reductions.

## Subthemes

- Expert importance is too coarse for large heterogeneous MoEs.
- Channel concentration creates large pruning opportunities.
- Hardware-aware alignment is necessary for real gains.
- Dynamic routing complicates static compression decisions.

## Connections to Other Papers

This paper pairs naturally with ScaleMoE: one uses experts to scale RL capacity, while the other compresses expert models for deployment. It also connects to STAR-KV, DHSA, NorMuon, and OPUS as part of the efficiency-as-capability theme.

The attribution angle links it to NS/IF attribution and interpretability-as-intervention papers, though here attribution is used for model compression rather than explanation to humans.

## Notes for Cross-Paper Synthesis

The synthesis point is that MoE is becoming a general scaling primitive, but it creates a second-order optimization problem: how to route, specialize, prune, and deploy experts without losing the diversity that made them valuable.
