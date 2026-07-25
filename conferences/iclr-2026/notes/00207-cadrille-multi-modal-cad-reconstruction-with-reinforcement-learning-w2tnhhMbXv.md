# cadrille: Multi-modal CAD Reconstruction with Reinforcement Learning

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: w2tnhhMbXv
- Authors: Maksim Kolodiazhnyi; Denis Tarasov; Dmitrii Zhemchuzhnikov; Alexander Nikulin; Ilya Zisman; Anna Vorontsova; Anton Konushin; Vladislav Kurenkov; Danila Rukhovich
- Primary area: applications to computer vision, audio, language, and other modalities
- Keywords: CAD;3D reconstruction;LLM;VLM;point cloud;DPO;GRPO
- Source URL: https://openreview.net/forum?id=w2tnhhMbXv
- PDF URL: https://openreview.net/pdf?id=w2tnhhMbXv

## Abstract

Computer-Aided Design (CAD) plays a central role in engineering and manufacturing, making it possible to create precise and editable 3D models. Using a variety of sensor or user-provided data as inputs for CAD reconstruction can democratize access to design applications. However, most existing methods focus on a single input modality: point clouds, images, or texts, which limits their generalizability and robustness, while few multimodal approaches struggle to deliver competitive quality. Leveraging advances in vision-language models (VLM), we propose $\texttt{cadrille}$, a multimodal CAD reconstruction model that takes inputs of three modalities and outputs executable Python code for CAD reconstruction. Inspired by large language model (LLM) training paradigm, we adopt a two-stage pipeline: supervised fine-tuning (SFT) on large-scale procedurally generated data, followed by reinforcement learning (RL) fine-tuning using online feedback, obtained programatically. In the DeepCAD benchmark, our SFT model outperforms existing single-modal approaches in all three input modalities simultaneously. More importantly, after RL fine-tuning, $\texttt{cadrille}$ sets new state-of-the-art in as many as 10 benchmarks across three modalities and four datasets, including a real-world one.

## One-Sentence Claim

`cadrille` reconstructs editable CAD models from point clouds, images, or text by generating executable Python CAD code and improving it with programmatic-feedback reinforcement learning.

## Problem

CAD reconstruction matters because engineering models need to be precise, editable, and compatible with downstream design workflows. Existing methods are usually tied to one modality, so they do not generalize well when users supply different kinds of input, and existing multimodal systems have not matched strong single-modal quality.

## Core Contribution

The paper contributes a multimodal CAD reconstruction model that accepts three input modalities and emits executable Python reconstruction code. It combines large-scale procedurally generated supervised data with online reinforcement learning feedback, and reports state-of-the-art results across many benchmarks, modalities, and datasets.

## Method

The method follows a two-stage LLM-style training pipeline. First, supervised fine-tuning trains the model on large-scale procedurally generated CAD data. Second, reinforcement learning fine-tunes outputs using programmatically obtained online feedback. The keyword metadata indicates use of VLM/LLM components and preference/RL methods such as DPO and GRPO.

## Experiments and Evidence

The abstract reports that the SFT model outperforms existing single-modal methods on DeepCAD across point-cloud, image, and text inputs simultaneously. After RL fine-tuning, `cadrille` reaches new state of the art on 10 benchmarks across three modalities and four datasets, including a real-world dataset.

## Limits and Failure Modes

This note is abstract/metadata-only. Full-text review should inspect the programmatic reward definition, execution sandbox, geometric validity checks, benchmark coverage, and failure modes for ambiguous or incomplete inputs. CAD code generation can also fail through syntactically valid but semantically wrong programs, overfitting to procedural generators, or brittle handling of real industrial geometry.

## Deep Themes

- Multimodal reconstruction into editable programs.
- Reinforcement learning with executable feedback.
- Procedural data as a bridge to real design tasks.
- Code as a structured output interface for geometry.

## Subthemes

- CAD reconstruction.
- Point-cloud, image, and text conditioning.
- VLM-to-code generation.
- Programmatic online feedback.
- SFT followed by RL fine-tuning.

## Connections to Other Papers

Connects to Visual Planning through non-textual reasoning over spatial structure, to EmotionThinker through GRPO-style post-training for modality-specific reasoning, and to Complexa/mCLM through scientific or engineering generation where validity is constrained by external structure rather than language plausibility.

## Notes for Cross-Paper Synthesis

This paper shows a recurring 2026 pattern: frontier-model methods are being adapted to domains where outputs must be executable, editable, or physically meaningful. The important shift is from generating plausible artifacts to generating artifacts that can be checked and improved by domain-specific feedback loops.
