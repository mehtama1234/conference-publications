# Do LLMs Signal When They’re Right? Evidence from Neuron Agreement

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: ZVRgcQq4D2
- Authors: Kang Chen; Yaoning Wang; Kai Xiong; Zhuoka Feng; Yu Minshen; Wenhe Sun; Haotian Chen; Yixin Cao
- Primary area: general_machine_learning->evaluation
- Keywords: Neuron-Agreement Decoding (NAD); Neuron activation patterns; Unsupervised answer selection; Chain-of-thought ensembling; Token efficiency
- Source URL: https://openreview.net/forum?id=ZVRgcQq4D2
- PDF URL: https://openreview.net/pdf?id=ZVRgcQq4D2

## Abstract

Large language models (LLMs) commonly boost reasoning via sample-evaluate-ensemble decoders (e.g., majority voting), achieving label free gains without ground truth. However, prevailing strategies score candidates using only external outputs such as token probabilities, entropies, or self evaluations, and these signals can be poorly calibrated after post training. We instead analyze internal behavior based on neuron activations and uncover three findings: (1) external signals are low dimensional projections of richer internal dynamics; (2) correct responses activate substantially fewer unique neurons than incorrect ones throughout generation; and (3) activations from correct responses exhibit stronger cross sample agreement, whereas incorrect ones diverge. Motivated by these observations, we propose Neuron Agreement Decoding (NAD), an unsupervised best of N method that selects candidates using activation sparsity and cross sample neuron agreement, operating solely on internal signals and without requiring comparable textual outputs. NAD enables early correctness prediction within the first 32 generated tokens and supports aggressive early stopping. Across math and science benchmarks with verifiable answers, NAD matches majority voting; on open ended coding benchmarks where majority voting is inapplicable, NAD consistently outperforms Avg@64. By pruning unpromising trajectories early, NAD reduces token usage by 99% with minimal loss in generation quality, showing that internal signals provide reliable, scalable, and efficient guidance for label free ensemble decoding.

## One-Sentence Claim

Correct LLM reasoning samples exhibit sparser and more cross-sample-consistent neuron activations, enabling unsupervised candidate selection and early stopping via Neuron Agreement Decoding.

## Problem

Sample-evaluate-ensemble decoding improves reasoning without labels, but common selection signals such as token probabilities, entropy, or self-evaluation can be poorly calibrated after post-training. Majority voting works only when outputs are comparable and can be clustered into repeated answers.

The paper asks whether internal activation dynamics provide a richer correctness signal than external text or probability summaries.

## Core Contribution

The paper finds that correct responses activate fewer unique neurons than incorrect ones and show stronger cross-sample neuron agreement throughout generation, while incorrect samples diverge. It proposes Neuron Agreement Decoding, an unsupervised best-of-N method using activation sparsity and cross-sample agreement.

NAD can predict correctness within the first 32 generated tokens, supports aggressive early stopping, matches majority voting on verifiable math/science tasks, works on open-ended coding where majority voting is inapplicable, and reduces token usage by 99 percent with minimal quality loss.

## Method

NAD collects internal neuron activation patterns across sampled generations. It scores candidates by how sparse their activations are and how much they agree with other samples' activation patterns, then selects or continues trajectories based on these internal signals.

Early stopping prunes trajectories whose activation behavior looks unlikely to converge to a correct response.

## Experiments and Evidence

Evidence reported in the abstract:

- Internal activation analysis showing external signals are low-dimensional projections of richer dynamics.
- Correct responses activate fewer unique neurons.
- Correct responses have stronger cross-sample neuron agreement.
- Early correctness prediction within 32 generated tokens.
- Matches majority voting on math and science benchmarks with verifiable answers.
- Outperforms Avg@64 on open-ended coding benchmarks.
- 99 percent token reduction through early pruning.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: model families, neuron definition, activation storage cost, benchmark list, and whether activation access is practical for API-only systems.

## Limits and Failure Modes

- NAD requires internal activations, which may not be available in closed model APIs.
- Activation sparsity-correctness relations may vary by architecture, layer, post-training recipe, or task.
- Early stopping could discard creative but correct long-horizon solutions.
- The method may be sensitive to sample diversity and decoding temperature.

## Deep Themes

**Correctness can be internally signaled before final answers.** Neuron agreement gives a process-level confidence measure.

**Efficiency comes from pruning bad reasoning trajectories early.** The method saves tokens by detecting divergence inside generation.

**Internal diagnostics can replace textual self-evaluation.** NAD avoids relying on models to verbally judge themselves.

## Subthemes

- Neuron Agreement Decoding.
- Activation sparsity as correctness signal.
- Cross-sample internal agreement.
- Label-free best-of-N selection.
- Token-efficient reasoning ensembles.

## Connections to Other Papers

Connects to Neuron-Basis Circuits, MDA, AI Engram, and interpretability-as-intervention papers through internal-unit diagnostics. It also links to BrokenMath, CausalGame, WZ-LLM, and reasoning evaluation papers because it targets correctness selection in multi-sample reasoning.

## Notes for Cross-Paper Synthesis

NAD adds a major process-diagnostics theme: reasoning systems may expose useful confidence signals in their internal dynamics even when external self-reports are unreliable.
