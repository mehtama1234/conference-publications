# FIDIA: Function-Informed Sequence Design via Inference-Aligned Policy Optimization

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: pvbJsa0ia0
- Authors: Minghan Li; Fengji Li; Yilin Tao; Yue Deng
- Primary area: applications->chemistry_physics_and_earth_sciences
- Keywords: Protein Inverse Folding; Best-of-N Inference Alignment; Gradient Estimation
- Source URL: https://openreview.net/forum?id=pvbJsa0ia0
- PDF URL: https://openreview.net/pdf?id=pvbJsa0ia0

## Abstract

Computational protein design typically employs a sequential workflow of structure generation followed by sequence (re)design. While structure generators can be explicitly conditioned on functional objectives, inverse folding models are constrained by their function-agnostic nature and sequence-structure degeneracy. More critically, the associated training objectives do not account for the *Best-of-N* (BoN) inference protocol, resulting in a fundamental training-inference misalignment. Here, we propose FIDIA, a reinforcement learning framework that enables **F**unction-**I**nformed sequence **D**esign via **I**nference-**A**ligned policy optimization. Specifically, FIDIA integrates functional constraints into composite rewards and explicitly optimize the induced policy under BoN toward high-fitness sequence regions. We achieve this via a grounded gradient estimator that directly maximizes the expected maximum reward. FIDIA consistently outperforms both standard and RL-optimized baselines in success rate and precision on a general motif scaffolding benchmark. Further experiments on realworld cases including vaccine and affinity-enhancing enzyme design validate FIDIA’s efficacy in complex therapeutic and biocatalytic contexts.

## One-Sentence Claim

FIDIA aligns protein inverse-folding training with Best-of-N inference by optimizing sequence policies directly toward high-fitness candidates under functional constraints.

## Problem

Protein design workflows often generate structures first and then redesign sequences. Structure generators can be conditioned on functional objectives, but inverse-folding models are typically function-agnostic and face sequence-structure degeneracy: many sequences can fit a structure, not all equally functional.

There is also a training-inference mismatch. If deployment uses Best-of-N selection to choose the highest-scoring candidate, then standard training objectives that optimize average likelihood or independent sequence quality do not directly optimize the selected maximum.

## Core Contribution

FIDIA contributes a reinforcement-learning framework for function-informed sequence design that explicitly optimizes the policy induced by Best-of-N inference. It integrates functional constraints into composite rewards and drives generation toward high-fitness sequence regions.

The key technical contribution is a grounded gradient estimator for directly maximizing expected maximum reward, aligning the optimization objective with how candidates are selected at inference time.

## Method

FIDIA treats the inverse-folding model as a policy over sequences and defines composite rewards that include functional constraints. Instead of optimizing only single-sample behavior, it optimizes for the expected best reward among N generated candidates.

The grounded gradient estimator supplies a tractable policy-optimization signal for this Best-of-N objective. This shifts training from fitting plausible sequences to producing candidate sets likely to contain high-fitness sequences.

## Experiments and Evidence

The abstract reports that FIDIA outperforms standard and RL-optimized baselines in success rate and precision on a general motif scaffolding benchmark. It also validates on real-world cases including vaccine design and affinity-enhancing enzyme design.

Full-paper reading should verify reward construction, oracle/function evaluator quality, N values, baseline tuning, wet-lab versus computational validation, and whether optimization sacrifices diversity or developability.

## Limits and Failure Modes

Function-informed RL depends on reward fidelity. If functional constraints are approximated poorly, the policy can exploit the reward while generating sequences that fail in real biological contexts.

Best-of-N optimization may reduce diversity or create overconfident concentration around reward-model artifacts. Protein design also needs constraints beyond target function, including stability, immunogenicity, manufacturability, and off-target behavior.

## Deep Themes

- Inference-aligned training: optimize the distribution used by Best-of-N selection, not an average-sample surrogate.
- Function-aware inverse folding: sequence redesign becomes conditional on downstream utility.
- Candidate-set optimization: success depends on the best generated sample, not only per-sample likelihood.
- RL for scientific design: policy optimization is used to steer generative models toward high-fitness regions.

## Subthemes

- Sequence-structure degeneracy requires functional disambiguation.
- Composite rewards encode multiple biological objectives.
- Motif scaffolding is a useful benchmark for function-preserving design.
- Real-world therapeutic and biocatalytic cases test whether benchmark gains transfer.

## Connections to Other Papers

FIDIA connects to PAR, DeCoDe, and Excited Pfaffians through scientific-domain generation. It also relates to BLL-Loss and post-training theory through training-inference alignment: the objective should match the selection/evaluation process used at deployment.

It also sits near OPUS and data-selection work because both emphasize choosing or generating data points with high downstream utility rather than maximizing generic likelihood.

## Notes for Cross-Paper Synthesis

FIDIA adds an important scientific-design pattern: when inference uses selection over candidates, training should optimize the selected candidate distribution. This principle appears across reasoning, protein design, and generation.
