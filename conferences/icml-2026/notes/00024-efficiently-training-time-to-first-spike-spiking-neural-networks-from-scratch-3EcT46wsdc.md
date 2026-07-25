# Efficiently Training Time-to-First-Spike Spiking Neural Networks from Scratch

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 3EcT46wsdc
- Authors: Kaiwei Che; Zhengyu Ma; Yifan Huang; Peng Xue; Li Yuan; Wei Fang; Yonghong Tian
- Primary area: applications->neuroscience_cognitive_science
- Keywords: Spiking neural networks;Time-to-first-spike
- Source URL: https://openreview.net/forum?id=3EcT46wsdc
- PDF URL: https://openreview.net/pdf?id=3EcT46wsdc

## Abstract

Spiking Neural Networks (SNNs), with their event-driven and biologically inspired mechanisms, are well-suited for energy-efficient neuromorphic hardware. Neural coding, which is critical to SNNs, determines how information is represented via spikes. While Time-to-First-Spike (TTFS) coding uses a single spike per neuron to offer extreme sparsity and energy efficiency, it often suffers from unstable training and low accuracy due to its sparse firing.
To address these challenges, we propose a training framework that incorporates parameter initialization, training normalization, a temporal output decoder, and a re-evaluation of the pooling layer. 
The proposed parameter initialization and training normalization mitigate signal diminishing and gradient vanishing, which helps stabilize training. Our output decoder aggregates temporal spikes to encourage earlier firing, thereby reducing latency.
The re-evaluation of the pooling layer demonstrates that max-pooling violates single-spike constraints, which should be avoided, whereas average-pooling preserves them.
Experiments show that our framework stabilizes and accelerates training, reduces latency, and achieves state-of-the-art accuracy for step-by-step TTFS SNNs on MNIST ($99.48\%$), Fashion-MNIST ($92.90\%$), CIFAR10 ($90.56\%$), CIFAR100 ($70.27\%$) and DVS Gesture ($95.83\%$).

## One-Sentence Claim

ETTFS makes direct Time-to-First-Spike SNN training stable and low-latency through TTFS-specific initialization, normalization, temporal decoding, and average-pooling design.

## Problem

TTFS coding is extremely sparse because each neuron fires at most once, making it attractive for neuromorphic efficiency, but that same sparse firing causes unstable training, signal diminishing, gradient vanishing, low accuracy, and latency issues.

## Core Contribution

The paper proposes a practical framework for training TTFS SNNs from scratch, combining parameter initialization, training-time normalization, a temporal output decoder, and a pooling-layer correction.

## Method

ETTFS-init stabilizes layer-wise signal statistics under TTFS firing; weight normalization reduces distribution shift during training; the temporal weighting decoder encourages earlier output firing; and average-pooling replaces max-pooling because max-pooling violates single-spike constraints.

## Experiments and Evidence

The abstract reports state-of-the-art step-by-step TTFS SNN accuracy on MNIST, Fashion-MNIST, CIFAR10, CIFAR100, and DVS Gesture, along with reduced latency.

## Full-Text Upgrade

The full text distinguishes non-causal layer-by-layer TTFS propagation from causal step-by-step propagation. Step-by-step propagation is the neuromorphic-friendly target because spikes move forward each time step and avoid depth-dependent latency accumulation, but it is harder to train accurately. ETTFS is designed specifically for this causal low-latency regime.

The technical diagnosis is concrete: default Kaiming initialization can make TTFS signals diminish and gradients vanish; ETTFS-init regulates layer statistics, and weight normalization keeps them from drifting during training. The paper also shows why max-pooling is structurally incompatible with TTFS: selecting a maximum over a spatial window can violate the one-spike constraint, while average-pooling preserves it. Reported benchmarks include 99.48% MNIST, 92.90% Fashion-MNIST, about 90.56% CIFAR10, about 70.27% CIFAR100, and 95.83% DVS Gesture, with lower average inference time steps than a TQ-TTFS decoder.

## Limits and Failure Modes

Limits to watch: results focus on standard vision and neuromorphic gesture benchmarks; the method is specialized to TTFS coding assumptions; and its advantage on larger architectures or more diverse event-stream tasks still needs broader evidence.

## Deep Themes

- Efficiency comes from respecting the computational substrate.
- Sparse neural codes need training rules designed around their constraints.
- Neuromorphic learning is shifting from conversion pipelines toward direct training.

## Subthemes

- Spiking neural networks.
- Time-to-first-spike coding.
- Neuromorphic latency.
- Initialization and normalization.
- Temporal output decoding.
- Pooling constraints.

## Connections to Other Papers

Connects to LiftQuant, low-precision transformer training, and resource-constrained transformer training as another example of hardware-aware ML where algorithm design must fit operational constraints.

## Notes for Cross-Paper Synthesis

ETTFS adds to the efficiency theme by showing that hardware-efficient models often require rethinking basic training components, not only compressing a conventional network after the fact.
