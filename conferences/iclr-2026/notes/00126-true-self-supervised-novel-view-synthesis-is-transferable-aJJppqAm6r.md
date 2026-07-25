# True Self-Supervised Novel View Synthesis is Transferable

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: aJJppqAm6r
- Authors: Thomas Mitchel; Hyunwoo Ryu; Vincent Sitzmann
- Primary area: applications to computer vision, audio, language, and other modalities
- Keywords: Novel View Synthesis;Self-Supervised;Unsupervised;Representation Learning
- Source URL: https://openreview.net/forum?id=aJJppqAm6r
- PDF URL: https://openreview.net/pdf?id=aJJppqAm6r

## Abstract

In this paper, we identify that the key criterion for determining whether a model is truly capable of novel view synthesis (NVS) is transferability: Whether any pose representation extracted from one video sequence can be used to re-render the same camera trajectory in another. We analyze prior work on self-supervised NVS and find that their predicted poses do not transfer: The same set of poses lead
to different camera trajectories in different 3D scenes. Here, we present XFactor, the first geometry-free self-supervised model capable of true NVS. XFactor combines pair-wise pose estimation with a simple augmentation scheme of the inputs and outputs that jointly enables disentangling camera pose from scene content and facilitates geometric reasoning. Remarkably, we show that XFactor achieves transferability with unconstrained latent pose variables, without any 3D inductive biases or concepts from multi-view geometry — such as an explicit parameterization of poses as elements of SE(3). We introduce a new metric to quantify transferability, and through large-scale experiments, we demonstrate that XFactor significantly outperforms prior pose-free NVS transformers, and show that latent poses are highly correlated with real-world poses through probing experiments.

## One-Sentence Claim

XFactor makes self-supervised novel view synthesis transferable by learning latent poses that re-render camera trajectories across scenes without explicit 3D geometry or SE(3) pose parameterization.

## Problem

Prior self-supervised NVS methods can appear to synthesize new views but fail a stricter transferability test: pose representations extracted from one sequence do not produce the same camera trajectory in another scene.

This means the learned pose is entangled with scene content rather than representing reusable camera motion.

## Core Contribution

The paper proposes transferability as the key criterion for true self-supervised NVS and introduces XFactor.

XFactor combines pairwise pose estimation with input/output augmentation to disentangle camera pose from scene content while avoiding explicit multi-view geometry, SE(3), or 3D inductive biases.

## Method

XFactor learns unconstrained latent pose variables from video sequences. Pairwise pose estimation provides relative view structure, while a simple augmentation scheme forces pose and content factors to separate.

The model is evaluated by whether latent poses can transfer across scenes to reproduce the same camera trajectory.

## Experiments and Evidence

The abstract reports large-scale experiments showing XFactor significantly outperforms prior pose-free NVS transformers.

A new transferability metric quantifies whether poses transfer across scenes, and probing experiments show learned latent poses are highly correlated with real-world poses.

## Limits and Failure Modes

Geometry-free latent poses may still fail under unusual camera motion, dynamic scenes, or severe occlusion. Transferability metrics need to rule out shortcut correlations between scenes and motion patterns.

Because this note is abstract-only, details still need checking: augmentation design, transferability metric, datasets, baselines, probing protocol, and whether dynamic/nonrigid scenes are covered.

## Deep Themes

- Transferability as representation test: true NVS requires pose factors that move across scenes.
- Geometry-free spatial reasoning: explicit SE(3) is not always necessary if training constraints induce disentanglement.
- Latent pose disentanglement: camera motion and scene content must be separable.
- Metrics for hidden factors: transfer tests expose failures that reconstruction quality can hide.

## Subthemes

- Novel view synthesis.
- Self-supervised pose learning.
- Transferable latent poses.
- Geometry-free 3D representation.

## Connections to Other Papers

This connects to DepthLM, Generative Human Geometry Distribution, AnyUp, and geometry/vision representation papers.

It also relates to LLM DNA and latent-dynamics work because all use functional tests to validate whether hidden representations mean what they claim.

## Notes for Cross-Paper Synthesis

XFactor adds a representation-validity theme: a latent variable is meaningful only if it transfers under interventions that preserve the factor it claims to encode.
