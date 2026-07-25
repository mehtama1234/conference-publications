# Triple-BERT: Do We Really Need MARL for Order Dispatch on Ride-Sharing Platforms?

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: symgW6FhA6
- Authors: Zijian Zhao; Sen Li
- Primary area: reinforcement learning
- Keywords: Reinforcement Learning;Order Dispatching;Ride Sharing
- Source URL: https://openreview.net/forum?id=symgW6FhA6
- PDF URL: https://openreview.net/pdf?id=symgW6FhA6

## Abstract

On-demand ride-sharing platforms, such as Uber and Lyft, face the intricate real-time challenge of bundling and matching passengers—each with distinct origins and destinations—to available vehicles, all while navigating significant system uncertainties. Due to the extensive observation space arising from the large number of drivers and orders, order dispatching, though fundamentally a centralized task, is often addressed using Multi-Agent Reinforcement Learning (MARL). However, independent MARL methods fail to capture global information and exhibit poor cooperation among workers, while Centralized Training Decentralized Execution (CTDE) MARL methods suffer from the curse of dimensionality. To overcome these challenges, we propose Triple-BERT, a centralized  Single Agent Reinforcement Learning (MARL) method designed specifically for large-scale order dispatching on ride-sharing platforms. Built on a variant TD3, our approach addresses the vast action space through an action decomposition strategy that breaks down the joint action probability into individual driver action probabilities. To handle the extensive observation space, we introduce a novel BERT-based network, where parameter reuse mitigates parameter growth as the number of drivers and orders increases, and the attention mechanism effectively captures the complex relationships among the large pool of driver and orders. We validate our method  using a real-world ride-hailing dataset from Manhattan. Triple-BERT achieves approximately an 11.95% improvement over current state-of-the-art methods, with a 4.26% increase in served orders and a 22.25% reduction in pickup times. Our code, trained model parameters, and processed data are publicly available at https://github.com/RS2002/Triple-BERT .

## One-Sentence Claim

Triple-BERT treats ride-sharing order dispatch as centralized single-agent RL with decomposed actions and BERT-style relational encoding, outperforming MARL approaches on a Manhattan ride-hailing dataset.

## Problem

Order dispatch is centralized in platform operation but has huge observation and action spaces due to many drivers and orders. Independent MARL misses global coordination, while CTDE-style MARL can suffer from dimensionality as system scale grows.

## Core Contribution

The paper proposes Triple-BERT, a centralized RL method based on a TD3 variant, action decomposition over individual driver decisions, and a BERT-based network with parameter reuse for scalable driver-order relation modeling.

## Method

Triple-BERT decomposes the joint dispatch action probability into per-driver action probabilities, reducing the action-space burden. A BERT-style attention network encodes relationships among large pools of drivers and orders while reusing parameters so model size does not grow directly with entity count.

## Experiments and Evidence

On a real-world Manhattan ride-hailing dataset, Triple-BERT reportedly improves over current state-of-the-art methods by about 11.95 percent, increases served orders by 4.26 percent, and reduces pickup times by 22.25 percent. Code, trained parameters, and processed data are public.

## Limits and Failure Modes

Ride-sharing benchmarks depend heavily on simulator fidelity, demand dynamics, constraints, and fairness/business objectives. A centralized policy may face latency or observability issues in live deployment. Full-text review should check simulator setup, baseline tuning, action decomposition assumptions, robustness to distribution shift, and operational constraints.

## Deep Themes

- Centralized RL for platform dispatch.
- Entity-relation modeling in large action spaces.
- Questioning MARL defaults.
- Scalable attention for operations research.

## Subthemes

- Action decomposition for dispatch.
- BERT-style driver-order encoding.
- TD3 variants for large-scale matching.
- Ride-hailing pickup-time reduction.
- Centralized decision-making under uncertainty.

## Connections to Other Papers

Connects to AIGB-Pearl and L2Seg through real-world decision optimization, to ranking-feedback and online-learning papers through platform control, and to hybrid solver papers where model structure handles large combinatorial spaces.

## Notes for Cross-Paper Synthesis

Triple-BERT reinforces that a problem's operational centralization should shape the learning formulation. MARL is not automatically appropriate just because many entities act in the environment.
