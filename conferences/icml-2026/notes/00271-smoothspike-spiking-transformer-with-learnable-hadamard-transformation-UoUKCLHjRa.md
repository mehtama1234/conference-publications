# SmoothSpike: Spiking Transformer with Learnable Hadamard Transformation

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: UoUKCLHjRa
- Authors: Zijian Zhou; Wenjie Wei; Yu Liang; Jialin Li; Ammar Belatreche; Honglin Cao; Shuai Wang; Malu Zhang; Yang Yang; Haizhou Li
- Primary area: applications->neuroscience_cognitive_science
- Keywords: Spiking Neural Network;Spiking Transformers
- Source URL: https://openreview.net/forum?id=UoUKCLHjRa
- PDF URL: https://openreview.net/pdf?id=UoUKCLHjRa

## Abstract

Spiking Neural Networks (SNNs) have attracted growing attention due to their sparse spike-based communication and inherent temporal dynamics. However, their discrete information representation fundamentally limits expressiveness, resulting in a notable performance gap relative to Artificial Neural Networks (ANNs) on language modeling tasks. In this paper, we reveal that this gap is fundamentally rooted in a spike saturation-induced information homogenization problem: within a bounded time window, distinct high-amplitude inputs converge to identical spike counts, compressing neural representations and impairing fine-grained semantic discrimination across layers.  To address this, we propose SmoothSpike, which applies a randomized Hadamard transformation to smooth pre-activation inputs and theoretically proves that it bounds the maximum input to $\mathcal{O}(\sqrt{\frac{\log n}{n}})$  with high probability. To further improve adaptability across varying input distributions, we extend the fixed transformation within SmoothSpike to a learnable orthogonal matrix updated via Newton-Schulz iterations, which can be fused into model weights at inference with no additional overhead. Experiments on the GLUE benchmark show that SmoothSpike effectively reduces information homogenization, yielding an 8.2\% average improvement over the Spikingformer baseline without compromising the efficiency inherent to spike-driven computation. These results advance the prospects for energy-efficient and high-performance language modeling on edge devices. Code is available at https://github.com/CayleyZ/SmoothSpike.

## One-Sentence Claim

SmoothSpike reduces spike-saturation information homogenization in spiking Transformers by smoothing pre-activations with fixed or learnable orthogonal Hadamard-style transformations.

## Problem

Spiking neural networks promise sparse communication and energy-efficient temporal computation, but their discrete spike counts limit expressiveness on language tasks. Within bounded time windows, high-amplitude inputs can collapse to identical spike counts, erasing fine-grained semantic differences as representations propagate through layers.

The paper identifies this as spike saturation-induced information homogenization, a root cause of the performance gap between spiking Transformers and conventional ANNs.

## Core Contribution

The paper proposes SmoothSpike, which applies randomized Hadamard transformations to smooth pre-activation inputs before spiking. It proves a high-probability bound on the maximum transformed input, reducing saturation risk.

It further replaces the fixed transform with a learnable orthogonal matrix updated by Newton-Schulz iterations. The learned transform can be fused into model weights at inference, preserving spike-computation efficiency with no additional runtime overhead.

## Method

SmoothSpike spreads large coordinate amplitudes across dimensions through an orthogonal transformation. This prevents individual channels from saturating spike counts and making different inputs indistinguishable.

The learnable variant adapts the smoothing transform to input distributions while maintaining orthogonality. Weight fusion means the transformation affects training and learned representations without adding a separate inference module.

## Experiments and Evidence

Evidence reported in the abstract:

- Theoretical maximum-input bound of order O(sqrt(log n / n)) with high probability after randomized Hadamard smoothing.
- Learnable orthogonal transform trained with Newton-Schulz iterations.
- GLUE benchmark evaluation.
- 8.2 percent average improvement over the Spikingformer baseline.
- No compromise to spike-driven inference efficiency because the transform can be fused.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: model sizes, timestep windows, energy measurements, GLUE task breakdown, and fusion implementation.

## Limits and Failure Modes

- The approach addresses saturation-induced homogenization but may not solve all expressivity limits of spiking language models.
- Orthogonal smoothing may interact with sparsity and temporal coding in task-dependent ways.
- GLUE improvements may not transfer to long-context or generative language modeling.
- Newton-Schulz learning stability and hardware friendliness need full-paper inspection.

## Deep Themes

**Information bottlenecks can be geometric.** The failure mode is not only discreteness but coordinate concentration before discrete spike counting.

**Efficiency-preserving transforms matter.** SmoothSpike improves expressivity while preserving inference-time spiking advantages through weight fusion.

**Orthogonal mixing recurs as a control primitive.** Like OCE and ENGNN, the paper uses orthogonal structure to change representations without destroying useful geometry.

## Subthemes

- Spike saturation and information homogenization.
- Randomized Hadamard smoothing.
- Learnable orthogonal transforms.
- Newton-Schulz orthogonal updates.
- Edge-efficient language modeling.

## Connections to Other Papers

Connects to WBMM, WeDLM, FeatJND, and other efficiency papers that preserve deployment practicality. It also links to OCE, ENGNN, and PRISM through geometry-preserving transformations over internal representations.

## Notes for Cross-Paper Synthesis

SmoothSpike adds a hardware-aware representation theme: efficient model families often fail through specific information bottlenecks, and the fix is to alter internal geometry without adding inference cost.
