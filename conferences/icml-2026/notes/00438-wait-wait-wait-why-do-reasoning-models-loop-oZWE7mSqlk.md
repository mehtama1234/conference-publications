# Wait, Wait, Wait... Why Do Reasoning Models Loop?

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: oZWE7mSqlk
- Authors: Charilaos Pipis; Shivam Garg; Vasilis Kontonis; Vaishnavi Shrivastava; Akshay Krishnamurthy; Dimitris Papailiopoulos
- Primary area: deep_learning->large_language_models
- Keywords: reasoning models;looping;llms;inference-time compute;learning theory
- Source URL: https://openreview.net/forum?id=oZWE7mSqlk
- PDF URL: https://openreview.net/pdf?id=oZWE7mSqlk

## Abstract

Reasoning models (e.g., DeepSeek-R1) generate long chains of thought to solve harder problems, but they often loop, repeating the same text at low temperatures or with greedy decoding. We study why this happens and what role temperature plays. With open reasoning models, we find that looping is common at low temperature. Larger models tend to loop less, and distilled students loop significantly even when their teachers rarely do. This points to mismatches between the training distribution and the learned model, which we refer to as errors in learning, as a key cause. To understand how such errors cause loops, we introduce a synthetic graph reasoning task and demonstrate two mechanisms. First, risk aversion caused by hardness of learning: when the correct progress-making action is hard to learn but an easy cyclic action is available, the model puts relatively more probability on the cyclic action and gets stuck. Second, even when there is no hardness, Transformers show an inductive bias toward temporally correlated errors, so the same few actions keep being chosen and loops appear. Higher temperature reduces looping by promoting exploration, but it does not fix the errors in learning, so generations remain much longer than necessary at high temperature; in this sense, temperature is a stopgap rather than a holistic solution. We end with a discussion of training-time interventions aimed at directly reducing errors in learning.

## One-Sentence Claim

Reasoning-model loops arise from learned errors and Transformer error correlations: low temperature exposes cyclic actions, while higher temperature only masks the problem by forcing exploration.

## Problem

Reasoning models often generate long chains of thought, but they can enter repetitive loops, especially under greedy or low-temperature decoding. This is more than an annoyance: loops waste inference-time compute and signal that the model's internal search process is not reliably making progress.

The practical question is why models choose cyclic continuations when progress-making actions exist, and whether decoding temperature fixes the underlying issue or merely changes surface behavior.

## Core Contribution

The paper combines empirical study of open reasoning models with a synthetic graph reasoning task to identify mechanisms behind looping. It argues that errors in learning, meaning mismatches between the training distribution and learned model, are a key cause.

It identifies two mechanisms: risk aversion under hard-to-learn progress actions, where easy cyclic actions receive too much probability, and Transformer inductive bias toward temporally correlated errors, where repeated action choices reinforce loops even without hardness.

## Method

Empirically, the authors examine looping behavior across open reasoning models, temperatures, model sizes, and distilled student models. The observation that distilled students loop more than teachers points toward learned-distribution mismatch rather than inherent task necessity.

The synthetic graph reasoning task provides a controlled environment where correct progress actions and cyclic actions can be separated. It allows the authors to demonstrate both hardness-induced risk aversion and temporally correlated errors under Transformer dynamics.

## Experiments and Evidence

The abstract reports that low-temperature looping is common, larger models loop less, and distilled students can loop substantially even when teachers rarely do. Higher temperature reduces looping through exploration but leaves generations longer than necessary, indicating it is a workaround rather than a cure.

The controlled graph task supplies mechanistic evidence for why loops appear. Full-paper reading should inspect model list, loop definitions, temperature sweeps, synthetic-task construction, and proposed training-time interventions.

## Limits and Failure Modes

Looping likely varies by prompt type, model family, training recipe, and decoding implementation. A loop detector may also confuse legitimate repeated verification with pathological repetition unless carefully defined.

The synthetic mechanisms are persuasive as explanations but may not cover all real reasoning loops, such as loops caused by tool feedback, prompt contradictions, safety policies, or reward hacking during RL.

## Deep Themes

- Inference-time compute pathology: longer thinking can become cyclic rather than useful.
- Decoding as symptom management: temperature changes exploration but not learned errors.
- Distillation can amplify reasoning defects: students may inherit behavior distributions imperfectly.
- Synthetic tasks as mechanism probes: controlled graph worlds reveal failure causes hidden in natural tasks.

## Subthemes

- Low-temperature decoding exposes high-probability cyclic attractors.
- Easy wrong actions can dominate hard correct actions.
- Transformers may correlate errors over time rather than independently recover.
- Training-time interventions are needed when decoding cannot repair the learned distribution.

## Connections to Other Papers

This paper connects to LongCoT, PLAINTAIN, RAGEN-style reasoning-collapse work, and post-training support-barrier theory. All study extended reasoning failure modes, but this paper focuses specifically on self-repetition under inference-time search.

It also relates to scaling-law origin work because both use synthetic controlled processes to explain large-model behavior. The shared methodological theme is to isolate mechanisms in a simple world, then interpret observed frontier-model behavior through them.

## Notes for Cross-Paper Synthesis

The synthesis point is that more inference-time tokens are not automatically more reasoning. The corpus increasingly distinguishes productive process length from degenerate process length, and asks training to fix the distributional cause rather than relying on decoding knobs.
