# Just-In-Time Reinforcement Learning: Continual Learning in LLM Agents Without Gradient Updates

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: pLvye0zHUC
- Authors: Yibo Li; Zijie Lin; Ailin Deng; Xuan Zhang; Yufei He; Shuo Ji; Tri Cao; Bryan Hooi
- Primary area: deep_learning->large_language_models
- Keywords: LLM;agents
- Source URL: https://openreview.net/forum?id=pLvye0zHUC
- PDF URL: https://openreview.net/pdf?id=pLvye0zHUC

## Abstract

While Large Language Model (LLM) agents excel at general tasks, they inherently struggle with continual adaptation due to the frozen weights after deployment. Conventional reinforcement learning (RL) offers a solution but incurs prohibitive computational costs and the risk of catastrophic forgetting. 
    We introduce Just-In-Time Reinforcement Learning (JitRL), a training-free framework that enables test-time policy optimization without any gradient updates. 
    JitRL maintains a dynamic, non-parametric memory of experiences and retrieves relevant trajectories to estimate action advantages on-the-fly. 
    These estimates are then used to directly modulate the LLM's output logits. 
    We theoretically prove that this additive update rule is the exact closed-form solution to the KL-constrained policy optimization objective. 
    Extensive experiments on WebArena and Jericho demonstrate that JitRL establishes a new state-of-the-art among training-free methods. 
    Crucially, JitRL outperforms the performance of computationally expensive fine-tuning methods (e.g., WebRL) while reducing monetary costs by over 30 times, offering a scalable path for continual learning agents. The code is available at https://github.com/liushiliushi/JitRL.

## One-Sentence Claim

JitRL enables deployed LLM agents to adapt continually without gradient updates by retrieving past trajectories, estimating action advantages at test time, and applying the resulting closed-form KL-constrained logit update.

## Problem

LLM agents are usually deployed with frozen weights, so they struggle to adapt continually from new experience. Conventional RL fine-tuning can adapt policies, but it is computationally expensive and risks catastrophic forgetting.

The problem is to get the benefits of reinforcement learning for agents after deployment without running gradient-based updates, retraining, or expensive fine-tuning loops.

## Core Contribution

JitRL contributes a training-free framework for test-time policy optimization. It keeps a dynamic non-parametric memory of experiences, retrieves relevant trajectories, estimates action advantages on the fly, and directly modulates the LLM's output logits.

The paper also provides a theoretical justification: the additive logit update is the exact closed-form solution to a KL-constrained policy optimization objective. This gives the method a stronger grounding than heuristic memory prompting alone.

## Method

At inference time, the agent stores and retrieves trajectories similar to the current context. Retrieved outcomes are used to estimate advantages for candidate actions, and these advantage estimates are added to the model's logits under a KL-constrained policy-update view.

Because the base model weights remain frozen, the method avoids gradient costs and catastrophic parameter forgetting. Adaptation is moved into memory retrieval and logit-level policy modulation.

## Experiments and Evidence

The abstract reports experiments on WebArena and Jericho, where JitRL reaches a new state of the art among training-free methods. It also reports outperforming computationally expensive fine-tuning methods such as WebRL while reducing monetary costs by over 30x.

Full-paper reading should inspect trajectory memory size, retrieval design, online evaluation protocol, comparison fairness against fine-tuning, and how advantage estimates handle noisy or sparse rewards.

## Limits and Failure Modes

JitRL depends on retrieving relevant prior trajectories. If the memory is sparse, stale, adversarial, or mismatched to the current task, logit modulation can bias the agent toward bad actions.

Non-parametric memory also creates governance issues: privacy, deletion, deduplication, and reward hacking can become part of the deployed system. Since the method adapts at test time, evaluation must account for stateful behavior across episodes.

## Deep Themes

- Test-time RL without gradients: policy improvement is moved from parameter updates to logit updates.
- Memory as continual-learning substrate: experience storage replaces weight plasticity.
- KL-constrained control of LLM outputs: advantage estimates become direct probability-shaping signals.
- Cost-aware agent adaptation: reducing fine-tuning cost is part of the method's value proposition.

## Subthemes

- Retrieved trajectories act as local policy-improvement evidence.
- Frozen-weight agents can still be stateful through memory.
- Closed-form policy updates give theoretical grounding to logit steering.
- Web and text-game agents are natural testbeds for continual adaptation.

## Connections to Other Papers

JitRL connects to MAP, Vision2Web, and PLAINTAIN through agent workflow improvement. It also relates to post-training policy-gradient theory: both use KL-constrained policy optimization ideas, but JitRL avoids gradient updates through retrieval-conditioned logit modulation.

It also links to exact RL unlearning because persistent trajectory memory raises deletion and governance questions for adaptive agents.

## Notes for Cross-Paper Synthesis

JitRL strengthens a theme of inference-time adaptation. The model is fixed, but the policy is not: memory, retrieval, and logit steering create a lightweight RL layer around the LLM.
