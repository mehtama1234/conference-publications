# SpatioLM: Towards General Physical Spatial Intelligence in Vision-Language Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: CHavqrN1X9
- Authors: jing wu; Jianhua Wu; Jiayi Guan; Jiahong Chen; Jinghui Lu; Hangjun Ye; Bingzhao Gao; Long Chen
- Primary area: deep_learning->foundation_models
- Keywords: Vision-Language Models;Spatial intelligence
- Source URL: https://openreview.net/forum?id=CHavqrN1X9
- PDF URL: https://openreview.net/pdf?id=CHavqrN1X9

## Abstract

Vision-Language Models (VLMs) perform well on commonsense reasoning tasks but struggle with visual spatial reasoning. Most existing solutions introduce extra 3D prior inputs or external spatial encoders, which increase complexity and degrade the underlying VLMs' general-purpose capabilities after spatial fine-tuning. To this end, we propose a parameter-efficient \textit{\textbf{Spatio}-vision \textbf{L}anguage \textbf{M}odels (SpatioLM)}, that enhances spatial intelligence without extra 3D prior inputs or third-party spatial encoders. Concretely, we design a plug-and-play and non-invasive spatio-vision module that elicits the spatial knowledge inherent in VLMs. Furthermore, we innovatively leverage pseudo depth and camera information as supervision to guide the model in learning physically coherent representations. Extensive experiments show that SpatioLM achieves significant improvements in diverse tasks, including spatial perception and understanding while effectively limiting the degradation of general capabilities. Notably, the model achieves an impressive score of 71.6 on the VSI-Bench (the first model to surpass 70). In addition, it attains competitive performance when transferred to embodied manipulation tasks.

## One-Sentence Claim

SpatioLM improves VLM spatial reasoning with a plug-and-play spatio-vision module supervised by pseudo depth and camera information, without external 3D encoders.

## Problem

VLMs often struggle with physical spatial reasoning, and prior fixes add 3D priors or spatial encoders that increase complexity and can degrade general-purpose VLM ability.

## Core Contribution

The paper proposes a parameter-efficient, non-invasive spatial module that elicits latent spatial knowledge in VLMs and learns physically coherent representations from pseudo depth and camera supervision.

## Method

SpatioLM adds a plug-and-play spatio-vision module to a VLM and trains it with pseudo depth/camera signals rather than requiring extra 3D inputs or third-party spatial encoders.

## Experiments and Evidence

The abstract reports significant gains on spatial perception and understanding, limited degradation of general capabilities, a 71.6 score on VSI-Bench, and competitive transfer to embodied manipulation tasks.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: pseudo-depth source, camera-supervision quality, module architecture, embodied transfer tasks, and failure cases under ambiguous geometry.

## Deep Themes

- Spatial intelligence can be elicited with lightweight modules rather than heavy external 3D pipelines.
- VLMs need physically coherent representations for embodied transfer.
- Preserving general capability matters when specializing foundation models.

## Subthemes

- Vision-language models.
- Spatial reasoning.
- Pseudo depth.
- Camera supervision.
- Parameter-efficient adaptation.
- Embodied manipulation transfer.

## Connections to Other Papers

Connects to SAW-Bench, SVL, RoboMME, and spatial/embodied evaluation papers through physically grounded visual reasoning.

## Notes for Cross-Paper Synthesis

SpatioLM adds to the spatial-intelligence theme: models need internal physical geometry without losing broad VLM capabilities.
