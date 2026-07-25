# Scalable Option Learning in High-Throughput Environments

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: p2RPRTPPMO
- Authors: Mikael Henaff; Scott Fujimoto; Michael Matthews; Michael Rabbat
- Primary area: reinforcement_learning->deep_rl
- Keywords: hierarchical reinforcement;long horizon;scale
- Source URL: https://openreview.net/forum?id=p2RPRTPPMO
- PDF URL: https://openreview.net/pdf?id=p2RPRTPPMO

## Abstract

Hierarchical reinforcement learning (RL) has the potential to enable effective decision-making over long timescales. Existing approaches, while promising, have yet to realize the benefits of large-scale training. In this work, we identify and solve several key challenges in scaling online hierarchical RL to high-throughput environments. We propose Scalable Option Learning (SOL), a highly scalable hierarchical policy gradient algorithm which achieves a ~35x higher throughput compared to existing hierarchical methods. To demonstrate SOL's performance and scalability, we train hierarchical agents using 30 billion frames of experience on the complex game of NetHack, significantly surpassing flat agents and demonstrating positive scaling trends. We also validate SOL on MiniHack and Mujoco environments, showcasing its general applicability.

## One-Sentence Claim

Scalable Option Learning makes hierarchical RL practical at very high throughput, enabling option-based agents to scale to 30 billion NetHack frames and outperform flat policies.

## Problem

Hierarchical RL promises long-horizon decision-making through temporally extended options, but many methods have not benefited from modern high-throughput training. Option discovery and hierarchical policy optimization can introduce overhead that prevents scaling to billions of frames.

This is especially limiting for complex environments like NetHack, where long-term abstraction should help but only if the algorithm can process enough experience efficiently.

## Core Contribution

The paper identifies and addresses scaling bottlenecks in online hierarchical RL, proposing Scalable Option Learning, a hierarchical policy-gradient algorithm with roughly 35x higher throughput than existing hierarchical methods.

The contribution is to show positive scaling for learned options in high-throughput environments. Rather than presenting hierarchy as a sample-efficiency trick at small scale, SOL demonstrates hierarchy under large-scale training budgets.

## Method

SOL is a scalable hierarchical policy-gradient method for option learning. The abstract does not detail its internal optimization, but the emphasis is on removing throughput bottlenecks that have prevented online hierarchical RL from matching flat-agent training scale.

The method is evaluated across environments with different properties: NetHack for complex long-horizon decision-making, MiniHack for controlled variants, and MuJoCo for continuous-control generality.

## Experiments and Evidence

The strongest reported evidence is training hierarchical agents with 30 billion frames on NetHack, significantly surpassing flat agents and showing positive scaling trends. SOL also achieves about 35x higher throughput than existing hierarchical methods and is validated on MiniHack and MuJoCo.

Full-paper reading should inspect option definitions, comparison baselines, throughput measurement, compute budget, scaling curves, and whether hierarchy improves exploration, credit assignment, or policy reuse.

## Limits and Failure Modes

The method may depend on environments where temporally extended options match the task structure. Hierarchy can hurt if options become too coarse, collapse to flat behavior, or constrain adaptation in tasks requiring fine-grained control.

High-throughput success also raises reproducibility concerns: 30 billion frames is a large budget, so the practical value depends on the infrastructure required and whether smaller-scale regimes still benefit.

## Deep Themes

- Hierarchy as long-horizon scaling: options become useful when the algorithm can train at modern throughput.
- Systems bottlenecks in RL algorithms: algorithmic ideas fail if they cannot consume enough experience.
- Positive scaling in online RL: SOL argues hierarchical methods can improve with massive data rather than plateau.
- Temporal abstraction for exploration and control: options provide a structure for extended decision-making.

## Subthemes

- NetHack is a stress test for long-horizon hierarchical agents.
- Throughput is an algorithmic property, not only an implementation detail.
- Flat-agent baselines define whether hierarchy adds real value.
- Cross-domain validation matters because option learning can overfit environment structure.

## Connections to Other Papers

SOL connects to ScaleMoE and WestWorld through scalable RL/control systems. ScaleMoE scales network capacity; SOL scales temporal abstraction and training throughput; WestWorld scales dynamics prediction across robots.

It also connects to LongCoT and reasoning-loop work at the abstract level: both study long-horizon processes where local competence is insufficient without process-level structure.

## Notes for Cross-Paper Synthesis

SOL adds a temporal abstraction axis to the corpus's scaling story. In RL, scale is not just model size or data; it is also whether the algorithm can represent and optimize long-duration behaviors at high throughput.
