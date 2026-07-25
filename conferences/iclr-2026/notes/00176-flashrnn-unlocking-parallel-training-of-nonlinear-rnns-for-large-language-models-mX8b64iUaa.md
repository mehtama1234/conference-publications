# FlashRNN: Unlocking Parallel Training of Nonlinear RNNs for Large Language Models

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: mX8b64iUaa
- Authors: Federico Danieli; Pau Rodriguez; Miguel Sarabia; Xavier Suau; Luca Zappella
- Primary area: foundation or frontier models, including LLMs
- Keywords: RNN;Mamba;SSM;Transformers;Parallelization;Parallel scan;Nonlinear
- Source URL: https://openreview.net/forum?id=mX8b64iUaa
- PDF URL: https://openreview.net/pdf?id=mX8b64iUaa

## Abstract

Recurrent Neural Networks (RNNs) laid the foundation for sequence modeling, but their intrinsic sequential nature restricts parallel computation, creating a fundamental barrier to scaling. This has led to the dominance of parallelizable architectures like Transformers and, more recently, State Space Models (SSMs). While SSMs achieve efficient parallelization through structured linear recurrences, this linearity constraint limits their expressive power and precludes modeling complex, nonlinear sequence-wise dependencies.
To address this, we present FlashRNN, a framework that breaks the sequence-parallelization barrier for nonlinear RNNs. Building on prior work, we cast the sequence of nonlinear recurrence relationships as a single system of equations, which we solve in parallel using Newton's iterations combined with custom parallel reductions. Our implementation achieves speedups of up to $665\times$ over na\"ive sequential application, allowing training nonlinear RNNs at unprecedented scales. To showcase this, we apply FlashRNN to adaptations of LSTM and GRU architectures, successfully training models of 7B parameters that attain perplexity comparable to similarly-sized Transformers and Mamba2 architectures.
To accelerate research in efficient sequence modeling, we release the FlashRNN codebase as an open-source framework for automatic training-parallelization of nonlinear RNNs, enabling researchers and practitioners to explore new nonlinear RNN models at scale.

## One-Sentence Claim

FlashRNN parallelizes nonlinear RNN training by solving the full recurrence system with Newton iterations and custom reductions, enabling 7B-parameter nonlinear recurrent language models.

## Problem

RNNs have strong sequence-modeling appeal but are hard to scale because recurrence is inherently sequential. SSMs regain parallelism through linear recurrences, but that linearity constrains expressiveness and limits nonlinear sequence dependencies.

## Core Contribution

The paper introduces FlashRNN, a framework for automatic training parallelization of nonlinear RNNs. It formulates nonlinear recurrent updates as a system of equations and solves them in parallel, making large LSTM/GRU-style language models feasible.

## Method

FlashRNN casts a sequence of nonlinear recurrence relationships as one coupled system. It applies Newton iterations and custom parallel reductions to solve that system across time steps, rather than unrolling it sequentially. The approach is applied to nonlinear adaptations of LSTM and GRU architectures.

## Experiments and Evidence

The abstract reports speedups up to 665x over naive sequential recurrence and successful training of 7B-parameter nonlinear RNNs with perplexity comparable to similarly sized Transformers and Mamba2 models. The authors also release an open-source framework.

## Limits and Failure Modes

Newton-style parallel solving may add memory pressure, convergence sensitivity, or numerical instability for some nonlinear recurrences. The comparison depends on hardware kernels, sequence lengths, and model recipes. Full-text review should check solver convergence, approximation error, scaling curves, wall-clock training cost, and downstream evaluation beyond perplexity.

## Deep Themes

- Parallelizing sequential computation.
- Nonlinear recurrence as scalable language-model architecture.
- Solver-based sequence model training.
- Revisiting RNNs under modern systems constraints.

## Subthemes

- Newton iterations for recurrence solving.
- Custom parallel reductions.
- LSTM/GRU scaling to billions of parameters.
- Expressiveness beyond linear SSMs.
- Efficient sequence modeling alternatives to Transformers.

## Connections to Other Papers

Connects to Mamba ICL theory, In-Place TTT, and SSM length-generalization papers through efficient sequence architectures, and to numerical/systems papers where algorithmic reformulation unlocks hardware parallelism.

## Notes for Cross-Paper Synthesis

FlashRNN fits the larger theme of removing architectural bottlenecks by changing the computation graph. It argues that RNN sequentiality is not a fixed barrier if recurrence can be solved as a parallel system.
