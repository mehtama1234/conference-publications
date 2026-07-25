# SAW-Bench: Learning Situated Awareness in the Real World

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 8lwrYjv6r7
- Authors: Chuhan Li; Rilyn R. Han; Joy Hsu; Yongyuan Liang; Rajiv Dhawan; Jiajun Wu; Ming-Hsuan Yang; Xin Eric Wang
- Primary area: applications->computer_vision
- Keywords: Evaluation;Multimodal Foundation Models;Spatial Intelligence
- Source URL: https://openreview.net/forum?id=8lwrYjv6r7
- PDF URL: https://openreview.net/pdf?id=8lwrYjv6r7

## Abstract

A core aspect of human perception is *situated awareness*, the ability to relate ourselves to the surrounding physical environment and reason over possible actions in context. However, most existing benchmarks for multimodal foundation models (MFMs) emphasize **environment-centric** spatial relations (relations among objects in a scene), while largely overlooking **observer-centric** relationships that require reasoning relative to agent's viewpoint, pose, and motion. To bridge this gap, we introduce SAW-Bench (**S**ituated **A**wareness in the Real **W**orld), a novel benchmark for evaluating egocentric situated awareness using real-world videos. SAW-Bench comprises 786 self-recorded videos captured with Ray-Ban Meta (Gen 2) smart glasses spanning diverse indoor and outdoor environments, and over 2071 *human-annotated* question-answer pairs. It probes a model’s observer–environment understanding with *six* different awareness tasks. Our comprehensive evaluation reveals a human-model performance gap of 37.66%, even with the best-performing MFM, Gemini 3 Flash. Beyond this gap, our in-depth analysis uncovers several notable findings; for example, while models can exploit partial geometric cues in egocentric videos, they often fail to infer a coherent camera geometry, leading to systematic spatial reasoning errors. We position SAW-Bench as a benchmark for situated spatial intelligence, moving beyond passive observation to understanding physically grounded, observer-centric dynamics.

## One-Sentence Claim

SAW-Bench evaluates whether multimodal foundation models can reason from an egocentric observer's viewpoint about real-world spatial situations and possible actions.

## Problem

Most multimodal benchmarks focus on object-to-object spatial relations, leaving observer-centric awareness of pose, viewpoint, motion, and action context under-measured.

## Core Contribution

The paper introduces SAW-Bench, a real-world egocentric video benchmark with human-annotated question-answer pairs spanning six situated-awareness tasks.

## Method

SAW-Bench uses 786 self-recorded Ray-Ban Meta smart-glasses videos from diverse indoor and outdoor environments, paired with 2,071 human-annotated QA items probing observer-environment understanding.

## Experiments and Evidence

The abstract reports a 37.66% human-model performance gap even for Gemini 3 Flash, and identifies systematic failures in coherent camera-geometry inference despite partial use of geometric cues.

## Limits and Failure Modes

ArXiv search failed with HTTP 429 for this batch, so this note is abstract-only. Details still need checking: the six task definitions, annotation protocol, model set, video length distribution, and whether egocentric device bias affects generality.

## Deep Themes

- Spatial intelligence needs observer-centric evaluation.
- Egocentric video benchmarks expose failures hidden by static scene understanding.
- Embodied awareness requires coherent camera geometry, not just object recognition.

## Subthemes

- Situated awareness.
- Egocentric video.
- Observer-centric spatial reasoning.
- Multimodal foundation model evaluation.
- Camera geometry.
- Real-world action context.

## Connections to Other Papers

Connects to RoboMME, EcoVLA, SCALE, and robot-evaluation papers through physically grounded perception/action reasoning. It also links to UniPercept as a benchmark that names an under-measured perceptual capability.

## Notes for Cross-Paper Synthesis

SAW-Bench adds a benchmark theme around embodied viewpoint: models may parse scenes but still fail to understand where the observer is and what actions are possible from that pose.
