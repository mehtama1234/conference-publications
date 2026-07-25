# A Regret Minimization Framework on Preference Learning in Large Language Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: genVnYBAV7
- Authors: Suhwan Kim; Taehyun Cho; Geon-Hyeong Kim; Yu Jin Kim; Youngsoo Jang; Moontae Lee; Jungwoo Lee
- Primary area: reinforcement_learning->deep_rl
- Keywords: RLHF;regret minimization
- Source URL: https://openreview.net/forum?id=genVnYBAV7
- PDF URL: https://openreview.net/pdf?id=genVnYBAV7

## Abstract

Reinforcement learning with verifiable rewards (RLVR) has enabled progress on reasoning-intensive tasks by relying on task-specific verifiers that provide automated correctness signals. However, many realistic language tasks are difficult to equip with reliable verifiers, motivating a growing reliance on reinforcement learning from human feedback (RLHF). 
In this setting, we argue that a closer examination of how human feedback should be interpreted is essential.
We introduce Regret-based Preference Optimization (RePO), which reframes RLHF through *regret minimization* rather than reward maximization. 
Human preferences are often shaped by *prospective* anticipation of outcomes and *counterfactual* comparisons to alternative behaviors, rather than by immediate, outcome-independent utility. 
RePO captures this structure by modeling preferences as behavior-conditioned assessments of relative suboptimality.
Within a KL-regularized reinforcement learning framework, RePO admits a closed-form policy update compatible with direct preference optimization. 
Experiments on mathematical reasoning benchmarks and human-annotated preference datasets demonstrate consistent performance gains, indicating that regret-based preference learning is an effective and human-aligned approach for training large language models.

## One-Sentence Claim

RePO reframes RLHF as regret minimization, modeling human preferences as behavior-conditioned judgments of relative suboptimality rather than direct reward observations.

## Problem

RLVR works when task-specific verifiers can provide reliable correctness signals, but many language tasks lack such verifiers. RLHF fills that gap, yet ordinary reward-maximization interpretations of human preference can miss how humans actually judge alternatives.

The paper argues that preferences often include prospective and counterfactual reasoning: annotators compare what happened with what could have happened, not just assign an outcome-independent utility.

## Core Contribution

The contribution is Regret-based Preference Optimization, a preference-learning framework that treats human feedback as assessments of relative regret or suboptimality. Instead of learning a static reward and maximizing it, RePO models preferences as conditioned on behavior and counterfactual alternatives.

Within KL-regularized RL, this framing yields a closed-form policy update compatible with direct preference optimization.

## Method

RePO embeds regret minimization into preference optimization. Human preferences are modeled as signals about how far a behavior falls short relative to alternatives under anticipated outcomes.

The closed-form update fits into DPO-style training, suggesting that the method can be implemented without a full online RL loop while retaining a regret-theoretic interpretation.

## Experiments and Evidence

Evidence reported in the abstract:

- Mathematical reasoning benchmarks.
- Human-annotated preference datasets.
- Consistent performance gains over preference-learning baselines.
- Closed-form KL-regularized policy update compatible with DPO.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: regret model form, baselines, preference datasets, and whether gains hold outside reasoning tasks.

## Limits and Failure Modes

- Human regret judgments may be noisy or inconsistent across annotators.
- Counterfactual preference modeling depends on which alternatives are presented or sampled.
- Closed-form updates can still optimize biased feedback if preference data are skewed.
- Regret framing may be less natural for open-ended taste or style preferences.

## Deep Themes

**Preferences are comparative processes.** The paper treats human feedback as counterfactual evaluation, not scalar reward measurement.

**Alignment objectives are becoming more behavioral.** RePO models how annotators judge decisions, not only what they choose.

**DPO-style simplicity can coexist with richer semantics.** The method keeps direct optimization while changing the preference interpretation.

## Subthemes

- Regret-based preference optimization.
- Counterfactual human feedback.
- KL-regularized policy updates.
- RLHF without verifiable rewards.
- DPO-compatible regret learning.

## Connections to Other Papers

Connects to Hista/Numca, Weak-Strong Verification, MoCA, Tilt Matching, and T2PO. It adds another form of process-aware alignment: preferences evaluate relative suboptimality rather than just final reward.

## Notes for Cross-Paper Synthesis

RePO strengthens the alignment theme that feedback must be modeled structurally. Whether the signal is human preference, verifier output, or state value, naive scalarization can lose what makes the signal meaningful.
