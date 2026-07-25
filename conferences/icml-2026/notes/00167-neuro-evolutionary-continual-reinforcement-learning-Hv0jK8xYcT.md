# Neuro-evolutionary Continual Reinforcement Learning

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: Hv0jK8xYcT
- Authors: Pengyi Li; Hongyao Tang; Yifu Yuan; YAN ZHENG; Xin Xu; Jianye HAO
- Primary area: deep_learning->algorithms
- Keywords: Continual Reinforcement Learning
- Source URL: https://openreview.net/forum?id=Hv0jK8xYcT
- PDF URL: https://openreview.net/pdf?id=Hv0jK8xYcT

## Abstract

Deploying robots in open-ended real-world environments demands continual learning capabilities to adapt to an ever-expanding range of tasks. This requires retaining previously acquired skills without forgetting while effectively leveraging prior knowledge to learn new ones. Inspired by neuroscience, we propose **N**euro-**e**volutionary **C**ontinual **R**einforcement **L**earning (**Nevo-CRL**). Nevo-CRL maintains a fixed-capacity monolithic policy network, solving tasks by optimizing inter-layer connectivity and neuron parameters.
For each new task, Nevo-CRL constructs a mask population to selectively activate the outputs of each hidden layer, thereby forming a task-specific policy population. Upon completing each task, the best-performing mask is stored, and its activated neurons are frozen to prevent catastrophic forgetting. To facilitate knowledge transfer, Nevo-CRL reuses neurons from acquired skills based on semantic similarity between tasks, while dynamically allocating additional neurons for task-specific adaptation.
In the learning process, Nevo-CRL iteratively adjusts masks via importance-guided crossover to optimize the policy network connectivity. To improve neuron utilization, we prune low-activity connections to recycle neurons. Experiments demonstrate that Nevo-CRL achieves state-of-the-art performance among continual RL methods.
The code is available at [https://github.com/yeshenpy/Nevo-CRL](https://github.com/yeshenpy/Nevo-CRL).

## One-Sentence Claim

Nevo-CRL uses task-specific evolved activation masks over a fixed-capacity policy network to support continual RL without catastrophic forgetting.

## Problem

Robots in open-ended environments must learn new tasks while retaining old skills, but continual RL methods struggle to balance transfer, plasticity, and fixed resource capacity.

## Core Contribution

The paper introduces a neuro-evolutionary continual RL method that stores best-performing task masks, freezes activated neurons for retention, reuses semantically related skills, and recycles low-activity capacity.

## Method

For each task, Nevo-CRL constructs a population of masks that selectively activate hidden-layer outputs, then optimizes connectivity through importance-guided crossover. After learning, it stores the best mask, freezes the corresponding neurons, reuses neurons based on task semantic similarity, and prunes low-activity connections to recycle neurons.

## Experiments and Evidence

The abstract reports state-of-the-art performance among continual RL methods.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: task suite, semantic-similarity source, mask population size, scalability to long task sequences, capacity exhaustion behavior, and robot-realism of benchmarks.

## Deep Themes

- Continual learning as dynamic allocation of fixed neural capacity.
- Skill retention through structural freezing and mask reuse.
- Evolutionary search as a connectivity optimizer for RL policies.

## Subthemes

- Continual reinforcement learning.
- Catastrophic forgetting.
- Mask populations.
- Skill transfer.
- Capacity recycling.
- Robotics adaptation.

## Connections to Other Papers

Connects to Posterior Behavioral Cloning and compute-bounded RL through policy adaptability, and to anti-collapse/modularity papers through selective reuse of internal capacity.

## Notes for Cross-Paper Synthesis

Nevo-CRL adds a continual-learning version of the corpus's preservation theme: the system protects prior capabilities by allocating and freezing structure rather than repeatedly overwriting a shared policy.
