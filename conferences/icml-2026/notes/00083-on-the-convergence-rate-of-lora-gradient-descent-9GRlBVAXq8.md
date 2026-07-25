# On the Convergence Rate of LoRA Gradient Descent

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 9GRlBVAXq8
- Authors: Siqiao Mu; Diego Klabjan
- Primary area: theory->optimization
- Keywords: LoRA;low-rank training;low-rank finetuning;finetuning;gradient descent;parameter efficient finetuning;PEFT;optimization;convergence;convergence analysis
- Source URL: https://openreview.net/forum?id=9GRlBVAXq8
- PDF URL: https://openreview.net/pdf?id=9GRlBVAXq8

## Abstract

The low-rank adaptation (LoRA) algorithm for fine-tuning large models has grown popular in recent years due to its remarkable performance and low computational requirements. LoRA trains two "adapter" matrices that form a low-rank representation of the model parameters, thereby massively reducing the number of parameters that need to be updated at every step. Although LoRA is simple, its convergence is poorly understood due to the lack of Lipschitz smoothness, a key condition for classic convergence analyses. As a result, current theoretical results only consider asymptotic behavior or assume strong boundedness conditions which artificially enforce Lipschitz smoothness. In this work, we provide for the first time a non-asymptotic convergence analysis of the *original LoRA gradient descent* algorithm, which reflects widespread practice, without such assumptions. Our work relies on three key steps: i) reformulating the problem in terms of the outer product of the stacked adapter matrices, ii) a modified descent lemma for the "Lipschitz-like" reparametrized function, and iii) controlling the step size. With this approach, we prove that LoRA gradient descent converges to a stationary point at rate $O(\frac{1}{\log T})$, where $T$ is the number of iterations.

## One-Sentence Claim

Original LoRA gradient descent has a non-asymptotic convergence guarantee to stationary points at rate O(1/log T) without artificial boundedness assumptions.

## Problem

LoRA is widely used for parameter-efficient fine-tuning, but its original gradient-descent dynamics lack classic Lipschitz smoothness, making standard convergence analyses inapplicable.

## Core Contribution

The paper gives a non-asymptotic convergence analysis of practical LoRA gradient descent without imposing strong boundedness assumptions that artificially restore Lipschitz smoothness.

## Method

The analysis reformulates LoRA in terms of the outer product of stacked adapter matrices, proves a modified descent lemma for a Lipschitz-like reparameterized objective, and controls the step size.

## Experiments and Evidence

The abstract reports a theoretical convergence rate of O(1/log T) to a stationary point for T iterations.

## Limits and Failure Modes

ArXiv search failed with HTTP 429 for this batch, so this note is abstract-only. Details still need checking: assumptions on the base objective, step-size schedule, rank dependence, practical tightness of O(1/log T), and implications for stochastic training.

## Deep Themes

- Popular fine-tuning methods need theory for their actual parameterization.
- Reparameterization can break standard smoothness assumptions.
- PEFT theory is catching up to deployed practice.

## Subthemes

- LoRA.
- Gradient descent convergence.
- Low-rank adaptation.
- PEFT.
- Non-asymptotic analysis.
- Stationary-point convergence.

## Connections to Other Papers

Connects to Neural Thickets, Skill Neologisms, midtraining, and alignment/preference optimization papers through efficient adaptation of pretrained models. It also links to implementation-aware theory papers.

## Notes for Cross-Paper Synthesis

This paper adds a PEFT-theory theme: efficient adaptation methods are mature enough in practice that their exact optimization dynamics now matter theoretically.
