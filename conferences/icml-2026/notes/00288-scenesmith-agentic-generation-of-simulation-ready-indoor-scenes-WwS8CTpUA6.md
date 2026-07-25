# SceneSmith: Agentic Generation of Simulation-Ready Indoor Scenes

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: WwS8CTpUA6
- Authors: Nicholas Pfaff; Thomas Cohn; Sergey Zakharov; Rick Cory; Russ Tedrake
- Primary area: applications->robotics
- Keywords: Indoor Scene Synthesis;LLM Agents;Robotics Simulation
- Source URL: https://openreview.net/forum?id=WwS8CTpUA6
- PDF URL: https://openreview.net/pdf?id=WwS8CTpUA6

## Abstract

Simulation has become a key tool for training and evaluating home robots at scale, yet existing environments fail to capture the diversity and physical complexity of real indoor spaces. Current scene synthesis methods produce sparsely furnished rooms that lack the dense clutter, articulated furniture, and physical properties essential for robotic manipulation. We introduce SceneSmith, a hierarchical agentic framework that generates simulation-ready indoor environments from natural language prompts. SceneSmith constructs scenes through successive stages—from architectural layout to furniture placement to small object population—each implemented as an interaction among VLM agents: designer, critic, and orchestrator. The framework tightly integrates asset generation through text-to-3D synthesis for static objects, dataset retrieval for articulated objects, and physical property estimation. SceneSmith generates 3-6x more objects than prior methods, with $<$2\% inter-object collisions and 96\% of objects remaining stable under physics simulation. In a user study with 205 participants, it achieves 92\% average realism and 91\% average prompt faithfulness win rates against baselines. We further demonstrate that these environments can be used in an end-to-end pipeline for automatic robot policy evaluation.

## One-Sentence Claim

SceneSmith uses hierarchical VLM-agent collaboration to generate dense, physically stable, simulation-ready indoor scenes for robot training and evaluation.

## Problem

Home-robot simulation needs environments that reflect real indoor diversity and physical complexity. Existing scene synthesis methods often produce sparse rooms that lack clutter, articulated furniture, and physical properties needed for manipulation.

The paper asks how to generate indoor scenes from language prompts that are not just visually plausible but ready for physics simulation and robot policy evaluation.

## Core Contribution

The paper introduces SceneSmith, a hierarchical agentic framework that builds scenes through stages: architectural layout, furniture placement, and small-object population. Each stage is handled by interacting VLM agents: designer, critic, and orchestrator.

The framework integrates text-to-3D asset generation for static objects, dataset retrieval for articulated objects, and physical property estimation. Generated scenes contain 3-6x more objects than prior methods, with low collisions and high physics stability.

## Method

SceneSmith decomposes indoor scene generation into staged decisions. VLM agents propose, critique, and coordinate scene elements, while asset pipelines supply static and articulated objects. Physical property estimation and simulation checks ensure generated scenes can be used by robot policies.

This makes scene generation an agentic design-and-validation workflow rather than pure geometry synthesis.

## Experiments and Evidence

Evidence reported in the abstract:

- 3-6x more objects than prior methods.
- Less than 2 percent inter-object collisions.
- 96 percent of objects remain stable under physics simulation.
- User study with 205 participants.
- 92 percent average realism and 91 percent prompt-faithfulness win rates against baselines.
- End-to-end pipeline for automatic robot policy evaluation.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: simulator, asset sources, prompts, collision/stability metrics, and robot-policy evaluation setup.

## Limits and Failure Modes

- VLM-generated scenes can inherit biases or unrealistic assumptions about households.
- Asset retrieval/generation quality may limit physical realism.
- Stability checks may not capture all manipulation-relevant dynamics.
- User-study realism does not necessarily imply task diversity for robot learning.

## Deep Themes

**Simulation data needs physical validity, not just visual plausibility.** SceneSmith measures collisions and stability because robots must act in the scene.

**Agentic pipelines can structure synthetic data generation.** Designer, critic, and orchestrator roles decompose a complex generation problem.

**Robotics evaluation is becoming environment-scale.** The scene generator itself becomes part of the policy-evaluation infrastructure.

## Subthemes

- Hierarchical indoor scene synthesis.
- VLM designer/critic/orchestrator agents.
- Text-to-3D and articulated asset retrieval.
- Physics-stability validation.
- Automatic robot policy evaluation.

## Connections to Other Papers

Connects to Holi-Spatial, RelaxFlow, AdLift, Latent Action Supervision, and continual VLA learning through 3D/robotics data generation and evaluation. It also links to PhotoAgent through agentic visual generation with feedback and critique.

## Notes for Cross-Paper Synthesis

SceneSmith extends the dataset-factory theme into simulation: generated data is valuable only if it is physically actionable and can support downstream policy testing.
