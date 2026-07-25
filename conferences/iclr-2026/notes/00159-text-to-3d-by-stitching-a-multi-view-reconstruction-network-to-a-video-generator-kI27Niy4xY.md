# Text-to-3D by Stitching a Multi-view Reconstruction Network to a Video Generator

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: kI27Niy4xY
- Authors: Hyojun Go; Dominik Narnhofer; Goutam Bhat; Prune Truong; Federico Tombari; Konrad Schindler
- Primary area: generative models
- Keywords: Text-to-3D generation;Video Diffusion Model;3D Gaussian Splatting;Generation
- Source URL: https://openreview.net/forum?id=kI27Niy4xY
- PDF URL: https://openreview.net/pdf?id=kI27Niy4xY

## Abstract

The rapid progress of large, pretrained models for both visual content generation and 3D reconstruction opens up new possibilities for text-to-3D generation. Intuitively, one could obtain a formidable 3D scene generator if one were able to combine the power of a modern latent text-to-video model as "generator" with the geometric abilities of a recent (feedforward) 3D reconstruction system as "decoder". We introduce **VIST3A**, a general framework that does just that, addressing two main challenges. First, the two components must be joined in a way that preserves the rich knowledge encoded in their weights. We revisit *model stitching*, i.e., we identify the layer in the 3D decoder that best matches the latent representation produced by the text-to-video generator and stitch the two parts together. That operation requires only a small dataset and no labels. Second, the text-to-video generator must be aligned with the stitched 3D decoder, to ensure that the generated latents are decodable into consistent, perceptually convincing 3D scene geometry. To that end, we adapt *direct reward finetuning*, a popular technique for human preference alignment. We evaluate the proposed VIST3A approach with different video generators and 3D reconstruction models. All tested pairings markedly improve over prior text-to-3D models that output Gaussian splats. Moreover, by choosing a suitable 3D base model, VIST3A also enables high-quality text-to-pointmap generation.

## One-Sentence Claim

VIST3A stitches a latent text-to-video generator to a feedforward multi-view 3D reconstruction decoder, then reward-finetunes the generator so video latents decode into consistent text-conditioned 3D geometry.

## Problem

Text-to-3D generation wants both rich semantic generation and accurate 3D geometry. Pretrained video generators know visual dynamics and appearance, while 3D reconstruction networks know multi-view geometry, but naively combining them can break latent compatibility and produce undecodable or inconsistent 3D scenes.

## Core Contribution

The paper proposes VIST3A, a model-stitching framework that identifies a compatible layer between a video generator and a 3D decoder using a small unlabeled dataset, then aligns the video generator to the stitched decoder with direct reward finetuning.

## Method

VIST3A treats the latent text-to-video model as the generator and the feedforward 3D reconstruction system as the decoder. It searches for the decoder layer whose representation best matches the generator latent, stitches the components while preserving pretrained weights, and applies reward finetuning so generated latents become decodable into perceptually convincing 3D Gaussian splats or pointmaps.

## Experiments and Evidence

The abstract reports evaluations across different video generators and 3D reconstruction models. All tested pairings markedly improve over prior Gaussian-splat text-to-3D methods, and suitable 3D base models enable high-quality text-to-pointmap generation.

## Limits and Failure Modes

Stitching quality may depend on latent compatibility, decoder choice, small-dataset coverage, and reward-model alignment. Video priors can still encode inconsistent views, and reward finetuning may trade diversity for decodability. Full-text review should check stitching-layer selection, reward definition, dataset size, 3D metrics, prompt diversity, and failure cases for thin structures or unusual viewpoints.

## Deep Themes

- Composing pretrained generative and geometric models.
- Model stitching as a low-data multimodal bridge.
- Reward finetuning for 3D decodability.
- Text-to-3D through video and reconstruction priors.

## Subthemes

- Latent compatibility between generators and decoders.
- Feedforward 3D reconstruction as a generative decoder.
- Direct reward finetuning beyond human preference alignment.
- Gaussian splat and pointmap generation.
- Reuse of pretrained foundation components.

## Connections to Other Papers

Connects to FlashWorld, quotient-space diffusion, RoSE, and other 3D/geometry papers through structured generative modeling, and to VLM/critic-based 3D generation work through alignment signals that make generated representations geometrically usable.

## Notes for Cross-Paper Synthesis

VIST3A shows a recurring architecture pattern: instead of training a complete generative system from scratch, stitch together pretrained modules and add a narrow alignment procedure at the interface where their representations meet.
