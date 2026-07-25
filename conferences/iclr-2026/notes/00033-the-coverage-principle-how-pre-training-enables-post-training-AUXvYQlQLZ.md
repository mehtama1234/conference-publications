# The Coverage Principle: How Pre-Training Enables Post-Training

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: AUXvYQlQLZ
- Authors: Fan Chen; Audrey Huang; Noah Golowich; Sadhika Malladi; Adam Block; Jordan T. Ash; Akshay Krishnamurthy; Dylan J Foster
- Primary area: learning theory
- Keywords: language models;reinforcement learning;test-time scaling;statistical learning theory
- Source URL: https://openreview.net/forum?id=AUXvYQlQLZ
- PDF URL: https://openreview.net/pdf?id=AUXvYQlQLZ

## Abstract

Language models demonstrate remarkable abilities when pre-trained on large text corpora and fine-tuned for specific tasks, but how and why pre-training shapes the success of the final model remains poorly understood. Notably, although pre-training success is often quantified by cross entropy loss, cross entropy can be poorly predictive of downstream performance. Instead, we provide a theoretical perspective on this relationship through the lens of coverage, which quantifies the probability mass the pre-trained model places on high-quality responses and which is necessary and sufficient for post-training and test-time scaling methods like Best-of-N to succeed. Our main results develop an understanding of the coverage principle, a phenomenon whereby next-token prediction implicitly optimizes toward a model with good coverage. In particular, we uncover a mechanism that explains the power of coverage in predicting downstream performance: coverage generalizes faster than cross entropy, avoiding spurious dependence on problem dependent parameters such as the sequence length. We also study practical algorithmic interventions with provable benefits for improving coverage, including (i) model/checkpoint selection procedures, (ii) gradient normalization schemes, and (iii) test-time decoding strategies.

## One-Sentence Claim

Pretraining enables post-training when it gives the model coverage: enough probability mass on high-quality responses for selection, RL, or test-time scaling to find them.

## Problem

Pretraining success is often measured by cross-entropy loss, but cross entropy can poorly predict downstream performance after fine-tuning or test-time scaling.

The problem is to identify a theoretical quantity that explains when pretraining makes later post-training methods effective.

## Core Contribution

The paper introduces the coverage principle. Coverage measures the probability mass a pretrained model assigns to high-quality responses.

It shows coverage is necessary and sufficient for methods like Best-of-N to succeed, and argues that next-token prediction implicitly optimizes toward good coverage.

## Method

The theory analyzes how coverage generalizes compared with cross entropy. Coverage avoids spurious dependence on problem-specific parameters such as sequence length and generalizes faster.

The paper also studies interventions with provable benefits: model/checkpoint selection, gradient normalization, and test-time decoding strategies.

## Experiments and Evidence

The abstract is mainly theoretical but identifies practical algorithmic interventions derived from the coverage lens.

The key evidence is a statistical-learning argument that coverage better predicts downstream post-training and test-time scaling success than cross entropy.

## Limits and Failure Modes

Coverage depends on defining high-quality responses, which can be task-specific and hard to observe. Best-of-N-style sufficiency may not directly capture interactive or safety-constrained tasks.

Because this note is abstract-only, details still need checking: formal coverage definition, assumptions, intervention algorithms, empirical validation, and extension to RLHF/RLVR beyond Best-of-N.

## Deep Themes

- Pretraining as support construction: later training succeeds only if good responses are already reachable.
- Cross entropy is not enough: likelihood can miss downstream selection potential.
- Test-time scaling as coverage exploitation: sampling helps when quality mass exists.
- Theory-guided model selection: checkpoints should be chosen for coverage, not only loss.

## Subthemes

- Best-of-N success conditions.
- Coverage generalization.
- Gradient normalization for coverage.
- Decoding strategies.

## Connections to Other Papers

This connects to PonderLM-2, OpenThoughts, Ctrl-R, H1, and ASAG through reasoning and test-time compute.

It also relates to accessible sequence bounds: both ask what outputs are reachable, though coverage focuses on probability mass over high-quality outputs rather than architectural accessibility.

## Notes for Cross-Paper Synthesis

Coverage is a major bridge concept: pretraining does not directly solve tasks, but it creates the distributional support that post-training and inference-time search exploit.
