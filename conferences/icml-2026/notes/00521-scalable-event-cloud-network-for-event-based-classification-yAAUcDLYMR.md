# Scalable Event Cloud Network for Event-based Classification

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: yAAUcDLYMR
- Authors: Hongwei Ren; Fei Ma; Xiaopeng LIN; Yuetong Fang; Hongxiang Huang; Yue Zhou; Yulong Huang; Haotian FU; Ziyi Yang; Youxin Jiang; Xiangqian Wu; Bojun Cheng
- Primary area: applications->computer_vision
- Keywords: Event Camera;Event Cloud;Classification
- Source URL: https://openreview.net/forum?id=yAAUcDLYMR
- PDF URL: https://openreview.net/pdf?id=yAAUcDLYMR

## Abstract

Event cameras are biologically inspired sensors garnering significant attention from both industry and academia. Mainstream methods favor frame and voxel representations, which reach a satisfactory performance while introducing time-consuming transformations, bulky models, and sacrificing fine-grained temporal information. Alternatively, Point Cloud representation demonstrates promise in addressing the mentioned weaknesses, but it has limited scalability in abstracting features of higher spatial resolution and longer temporal sequence events.  In this paper, we propose a Scalable Network named SECNet to leverage Event Cloud representation. SECNet integrates polarity at the structural level by innovating the Event-based Group and Sampling module rather than only at the input level. To accommodate the surge in the number of events, SECNet embraces feature extraction in the frequency domain via the Fourier transform. This approach not only substantially extinguishes the explosion of Multiply Accumulate Operations but also effectively abstracts spatio-temporal features. We conducted extensive experiments on ten event-based datasets, and substantiate the scalability, effectiveness, and efficiency of SECNet. Our code will be available at: https://github.com/rhwxmx/SECNet_ICML.

## One-Sentence Claim

SECNet scales event-camera classification by operating on event-cloud representations with structural polarity integration and frequency-domain feature extraction.

## Problem

Event-camera methods often convert asynchronous events into frames or voxels. These representations can perform well but add transformation cost, require bulky models, and discard fine-grained temporal information.

Point-cloud-style event representations preserve event structure but struggle to scale to higher spatial resolution and longer temporal sequences.

## Core Contribution

The paper proposes SECNet, a scalable event-cloud network for event-based classification.

Its main contributions are an Event-based Group and Sampling module that integrates polarity structurally, and Fourier-domain feature extraction that reduces multiply-accumulate growth while abstracting spatiotemporal features.

## Method

SECNet treats events as an event cloud rather than converting them into dense frames or voxels. Polarity is incorporated into grouping and sampling, not merely appended as an input feature.

For large event counts, SECNet uses Fourier transform-based feature extraction to control computational explosion and capture spatiotemporal patterns efficiently.

## Experiments and Evidence

The abstract reports extensive experiments on ten event-based datasets and claims scalability, effectiveness, and efficiency.

It also frames the method as a response to both bulky frame/voxel pipelines and non-scalable point-cloud alternatives.

## Limits and Failure Modes

Frequency-domain abstraction may lose localized temporal details if not carefully designed, and event-cloud methods may be sensitive to sensor noise, event rate, and motion statistics.

Because this note is abstract-only, details still need checking: dataset list, event sampling strategy, Fourier feature implementation, model size, latency, comparisons against voxel/frame baselines, and robustness to high-noise event streams.

## Deep Themes

- Sensor-native representation: event cameras need models that preserve asynchronous temporal structure.
- Frequency-domain scalability: transform methods can reduce computation while preserving useful spatiotemporal signal.
- Structural polarity integration: polarity is part of event geometry, not just an input channel.
- Efficient perception beyond RGB: specialized sensors require specialized architectures.

## Subthemes

- Event-cloud classification.
- Event-based grouping and sampling.
- Fourier feature extraction.
- Long temporal sequence scalability.

## Connections to Other Papers

This connects to EgoTactile and DroneDINO through specialized multimodal or nonstandard sensor modeling.

It also links to IO-aware GNN kernels and EntroKV because all target scalability by changing how data structure is represented and processed.

## Notes for Cross-Paper Synthesis

SECNet adds to the representation-efficiency theme: using a sensor-native representation can avoid expensive conversions and preserve the signal that dense abstractions discard.
