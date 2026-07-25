# WestWorld: A Knowledge-Encoded Scalable Trajectory World Model for Diverse Robotic Systems

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: ncRRCG4BfP
- Authors: Yuchen Wang; Jiangtao Kong; Sizhe Wei; Xiaochang Li; Haohong Lin; Hongjue Zhao; Tianyi Zhou; Lu Gan; Huajie Shao
- Primary area: applications->robotics
- Keywords: Trajectory World Model;Knowledge-Encoded Robotics Learning;Mixture-of-Experts
- Source URL: https://openreview.net/forum?id=ncRRCG4BfP
- PDF URL: https://openreview.net/pdf?id=ncRRCG4BfP

## Abstract

Trajectory world models play a crucial role in robotic dynamics learning, planning, and control. While recent works have explored trajectory world models for diverse robotic systems, they struggle to scale to a large number of distinct system dynamics and overlook domain knowledge of physical structures. To address these limitations, we introduce *WestWorld*, a kno**W**ledge-**E**ncoded **S**calable **T**rajectory **World** model for diverse robotic systems. To tackle the scalability challenge, we propose a novel system-aware Mixture-of-Experts (Sys-MoE) that dynamically combines and routes specialized experts for different robotic systems via a learnable system embedding. To further enhance zero-shot generalization, we incorporate domain knowledge of robot physical structures by introducing a structural embedding that aligns trajectory representations with morphological information. After pretraining on 89 complex environments spanning diverse morphologies across both simulation and real-world settings, *WestWorld* achieves significant improvements over competitive baselines in zero- and few-shot trajectory prediction. Additionally, it shows strong scalability across a wide range of robotic environments and significantly improves performance on downstream model-based control for different robots. Finally, we deploy our model on a real-world Unitree Go1, where it demonstrates stable locomotion performance. The code is available at https://github.com/511205787/WestWorld.

## One-Sentence Claim

WestWorld scales trajectory world modeling across diverse robots by routing through system-aware experts and embedding physical morphology into trajectory representations.

## Problem

Trajectory world models are useful for robotic prediction, planning, and control, but diverse robot morphologies and dynamics make scaling difficult. A model trained for one robot or narrow family often fails to generalize when bodies, actuators, contacts, and motion regimes change.

The paper identifies two missing ingredients in prior work: scalable specialization across many systems and explicit use of physical-structure knowledge. Without those, a large trajectory model risks learning a flat mixture of dynamics that is neither specialized enough for individual robots nor structured enough to transfer zero-shot.

## Core Contribution

The contribution is a knowledge-encoded scalable trajectory world model. WestWorld combines a system-aware Mixture-of-Experts with structural embeddings that align trajectory representations to robot morphology.

The deeper contribution is to treat robot diversity as a routing and representation problem. The model does not merely expand capacity; it learns how to select and combine dynamics experts based on system identity and physical structure.

## Method

WestWorld uses a learnable system embedding to dynamically route through specialized experts in a Sys-MoE. This creates capacity that can be reused across robots while still allowing system-specific dynamics modeling.

It also incorporates structural embeddings derived from robot physical morphology. These embeddings inject domain knowledge into trajectory representations, supporting zero-shot and few-shot transfer when the model encounters new or underrepresented robotic systems.

## Experiments and Evidence

The abstract reports pretraining on 89 complex environments spanning diverse morphologies across simulation and real-world settings. WestWorld improves zero-shot and few-shot trajectory prediction, scales across robotic environments, improves downstream model-based control, and is deployed on a real Unitree Go1 with stable locomotion.

This is a broad empirical claim spanning prediction, control, scalability, and real-world deployment. Full-paper verification should inspect environment diversity, ablations for Sys-MoE and structural embeddings, and how real-world stability was measured.

## Limits and Failure Modes

The model likely depends on the quality and granularity of the morphology encoding. If structural embeddings omit relevant physical properties, routing may select experts that are plausible but dynamically wrong.

Mixture-of-experts models can also suffer from expert collapse, brittle routing under distribution shift, and hidden capacity imbalance. For robotics, sim-to-real gaps and safety constraints remain important even if trajectory prediction improves.

## Deep Themes

- Embodied scaling through morphology: physical structure becomes an input to model routing and generalization.
- World models as reusable infrastructure: trajectory prediction supports downstream control rather than standing alone.
- Conditional specialization: scalable robotics models need both shared capacity and system-specific experts.
- Real-world validation as a credibility filter: deployment on Unitree Go1 strengthens the claim beyond simulation-only evaluation.

## Subthemes

- System embeddings make robot identity computationally actionable.
- Structural embeddings align learned representations with morphology.
- Zero-shot robotic transfer requires knowing what kind of body the model is predicting.
- Model-based control benefits when the learned dynamics model is scalable across environments.

## Connections to Other Papers

WestWorld connects to LaST0 through embodied prediction and control, but LaST0 emphasizes latent reasoning for vision-language-action policies while WestWorld focuses on trajectory dynamics. It also relates to MERLIN and Excited Pfaffians as scientific/physical modeling papers that use structured representations to generalize across systems.

It sits near OPUS and NorMuon in the broader scaling theme: specialization and routing are used to make more capability fit within practical compute.

## Notes for Cross-Paper Synthesis

WestWorld reinforces the pattern that physical-domain foundation models need domain structure. In robotics, scaling is not just more environments; it is morphology-aware routing over heterogeneous dynamics.
