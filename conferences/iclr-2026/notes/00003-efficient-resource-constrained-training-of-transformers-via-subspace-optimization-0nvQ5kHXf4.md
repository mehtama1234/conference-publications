# Efficient Resource-Constrained Training of Transformers via Subspace Optimization

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: 0nvQ5kHXf4
- Authors: Le-Trung Nguyen; Enzo Tartaglione; Van-Tam Nguyen
- Primary area: optimization
- Keywords: Deep Learning;Computer Vision;Compression;Low rank
- Source URL: https://openreview.net/forum?id=0nvQ5kHXf4
- PDF URL: https://openreview.net/pdf?id=0nvQ5kHXf4

## Abstract

As AI increasingly shapes daily life, energy consumption and data privacy have become pressing concerns. On-device learning trains models directly on edge devices, cutting energy consumption and safeguarding data privacy. However, the expanding scale of modern neural networks creates a major obstacle for on-device training. Although prior work has concentrated on compact convolutional architectures, we instead apply subspace-based training to transformer models. Motivated by the idea that a model's essential information lies in a fixed subspace, we introduce Weight-Activation Subspace Iteration (WASI), a method that mitigates the memory bottleneck of backpropagation and boosts inference efficiency in transformer models by restricting training to this subspace. Our results demonstrate that WASI maintains accuracy comparable to vanilla training while reducing memory usage by up to $62\times$ and computational cost (FLOPs) by up to $2\times$. On a Raspberry Pi 5, WASI achieves roughly $1.4\times$ faster training and inference than vanilla training. The code is available at https://github.com/Le-TrungNguyen/ICLR2026-WASI.git.

## One-Sentence Claim

Transformer training can be made practical on resource-constrained devices by restricting optimization to a learned weight-activation subspace while retaining accuracy close to full training.

## Problem

On-device learning can reduce energy use and protect privacy, but modern transformer training exceeds the memory and compute budgets of edge devices. Existing compact-training work has focused more on convolutional architectures than transformers.

## Core Contribution

The paper introduces Weight-Activation Subspace Iteration (WASI), a subspace-based transformer training method that reduces the memory bottleneck of backpropagation and improves efficiency.

## Method

WASI assumes the model's essential trainable information lies in a fixed subspace and restricts training to that subspace across weights and activations. This reduces memory usage during backpropagation and lowers compute for transformer training/inference.

## Experiments and Evidence

The abstract reports accuracy comparable to vanilla training, memory reduction up to 62x, FLOP reduction up to 2x, and about 1.4x faster training and inference on Raspberry Pi 5. The PDF should be checked for model families, task breadth, how the subspace is chosen, and wall-clock measurement methodology.

## Limits and Failure Modes

Likely limits: performance may depend on how well a task/model fits the fixed subspace assumption; gains may vary by hardware; the approach may be weaker for large distribution shifts, full fine-tuning needs, or tasks requiring substantial representation change.

## Deep Themes

- Efficiency as a deployment enabler, not merely a cost reduction.
- Privacy and energy constraints pushing training closer to the edge.
- Subspace assumptions as a recurring way to make large models trainable under constraints.

## Subthemes

- On-device learning.
- Transformer compression.
- Low-rank/subspace optimization.
- Memory-efficient backpropagation.
- Edge deployment.

## Connections to Other Papers

Connects to low-precision transformer training, pruning, quantization, LoRA/adapters, and privacy-preserving learning. It should be compared with other efficient adaptation papers to determine whether 2026 favors subspace restriction, modular adapters, sparsity, or numerical compression.

## Notes for Cross-Paper Synthesis

This paper reinforces the pattern that deployment constraints are reshaping core ML methods. The theme is not just smaller models; it is local, private, energy-aware adaptation of foundation-model-style architectures.
