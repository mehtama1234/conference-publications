# Joint-Space Empowerment as a Theory of Dexterous Motor Coordination

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: qI2eHwfNfh
- Authors: James Heald; Vittorio Caggiano; Vikash Kumar; Maneesh Sahani
- Primary area: reinforcement_learning
- Keywords: Empowerment;Mutual Information;Muscle Synergies;Biomechanics;Action Manifolds
- Source URL: https://openreview.net/forum?id=qI2eHwfNfh
- PDF URL: https://openreview.net/pdf?id=qI2eHwfNfh

## Abstract

Searching for effective policies is notoriously challenging in high-dimensional musculoskeletal systems, where multiple muscles actuate individual joints. Although this redundancy complicates naive policy search, it also implies that effective control can be captured by a low-dimensional action manifold. To identify such a manifold, we introduce Joint-Space Empowerment (JoSE), a novel information-theoretic objective that quantifies how much control an agent has over its mechanical degrees-of-freedom. We frame manifold discovery as an optimal precoding problem—where a state-dependent precoder maps low-dimensional latent actions to high-dimensional muscle commands—and derive the optimal precoder in closed form under control-affine Gaussian dynamics. We show that manipulation policies learned on this manifold display significantly enhanced dexterity, sample efficiency, and improved generalization. These results present optimal precoding as a general information-theoretic paradigm for coordinating high-dimensional actuators to control low-dimensional features.

## One-Sentence Claim

Joint-Space Empowerment discovers low-dimensional action manifolds for high-dimensional musculoskeletal control by maximizing information-theoretic control over mechanical degrees of freedom.

## Problem

High-dimensional musculoskeletal systems are difficult for policy search because many muscles redundantly actuate individual joints. This redundancy makes naive action spaces large and poorly conditioned, but it also suggests that effective control may lie on a lower-dimensional manifold.

The challenge is to identify a control manifold that preserves dexterity while reducing the search burden. A good manifold should coordinate muscles according to the mechanical degrees of freedom that matter for behavior.

## Core Contribution

The paper introduces Joint-Space Empowerment, an information-theoretic objective measuring how much control an agent has over its mechanical degrees of freedom. It frames manifold discovery as an optimal precoding problem from low-dimensional latent actions to high-dimensional muscle commands.

Under control-affine Gaussian dynamics, the authors derive the optimal state-dependent precoder in closed form. This gives a principled basis for learning manipulation policies on the discovered manifold.

## Method

JoSE defines empowerment in joint space through mutual information between latent actions and controllable mechanical outcomes. A state-dependent precoder maps low-dimensional action coordinates into high-dimensional actuator commands.

The closed-form solution under control-affine Gaussian assumptions identifies the precoder that maximizes controllability over target degrees of freedom. Policies are then trained on the resulting action manifold rather than the full muscle-command space.

## Experiments and Evidence

The abstract reports that manipulation policies learned on the JoSE manifold show enhanced dexterity, improved sample efficiency, and better generalization. This supports the claim that information-theoretic action manifolds can coordinate high-dimensional actuators effectively.

Full-paper reading should verify the musculoskeletal environments, baseline action parameterizations, dimensionality reduction comparisons, and whether the closed-form assumptions hold approximately in the tested tasks.

## Limits and Failure Modes

The closed-form result depends on control-affine Gaussian dynamics. Real biomechanical systems can be nonlinear, contact-rich, delayed, and noisy in ways that violate those assumptions.

A low-dimensional manifold can also exclude useful actions if empowerment is defined too narrowly. Dexterity gains depend on choosing mechanical degrees of freedom and latent dimension that match the task.

## Deep Themes

- Information-theoretic motor abstraction: empowerment discovers action coordinates by controllability.
- Redundancy as structure: many muscles are not merely a curse but evidence of lower-dimensional synergies.
- Precoding for embodied control: action manifolds can be derived as mappings from latent commands to actuators.
- Biomechanics-aware RL: policy search improves when the action space respects body mechanics.

## Subthemes

- Mutual information links motor control and representation learning.
- Muscle synergies become computational objects.
- State-dependent action manifolds can adapt to posture and dynamics.
- Sample efficiency improves when search avoids irrelevant actuator dimensions.

## Connections to Other Papers

JoSE connects to WestWorld and ScaleMoE through embodied control scaling. WestWorld models morphology-conditioned dynamics; ScaleMoE scales actor-critic capacity; JoSE changes the action space itself through information-theoretic coordination.

It also relates to representation-geometry papers because the key object is a useful low-dimensional manifold embedded in a high-dimensional system.

## Notes for Cross-Paper Synthesis

JoSE adds an action-space version of the corpus's structured-representation theme. For embodied systems, the right abstraction may be neither more model capacity nor more data, but a manifold that matches biomechanical controllability.
