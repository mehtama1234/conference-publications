# Holi-Spatial: Evolving Video Streams into Holistic 3D Spatial Intelligence

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: UGAP2F6FfV
- Authors: Yuanyuan Gao; Hao Li; Yifei Liu; Xinhao Ji; Yuning Gong; Yuanjun Liao; Fangfu Liu; Manyuan Zhang; Yuchen Yang; Dan Xu; Xue Yang; Huaxi Huang; Hongjie Zhang; Ziwei Liu; Xiao Sun; Dingwen Zhang; Zhihang Zhong
- Primary area: deep_learning->foundation_models
- Keywords: 3D Spatial Intelligence
- Source URL: https://openreview.net/forum?id=UGAP2F6FfV
- PDF URL: https://openreview.net/pdf?id=UGAP2F6FfV

## Abstract

The pursuit of spatial intelligence fundamentally relies on access to large-scale, fine-grained 3D data. However, existing approaches predominantly construct spatial understanding benchmarks by generating question–answer (QA) pairs from a limited number of manually annotated datasets, rather than systematically annotating new large-scale 3D scenes from raw web data. As a result, their scalability is severely constrained, and model performance is further hindered by domain gaps inherent in these narrowly curated datasets.
In this work, we propose \textbf{Holi-Spatial}, the first fully automated, large-scale, spatially-aware multimodal dataset, constructed from raw video inputs without human intervention, using the proposed data curation pipeline. Holi-Spatial supports multi-level spatial supervision, ranging from geometrically accurate 3D Gaussian Splatting (3DGS) reconstructions with rendered depth maps to object-level and relational semantic annotations, together with corresponding spatial Question–Answer (QA) pairs.
Following a principled and systematic pipeline, we further construct \textbf{Holi-Spatial-4M}, the first large-scale, high-quality 3D semantic dataset, containing 12K optimized 3DGS scenes, 1.3M 2D masks, 320K 3D bounding boxes, 320K instance captions, 1.2M 3D grounding instances, and 1.2M spatial QA pairs spanning diverse geometric, relational, and semantic reasoning tasks.
Holi-Spatial demonstrates exceptional performance in data curation quality, significantly outperforming existing feed-forward and per-scene optimized methods on datasets such as ScanNet, ScanNet++, and DL3DV. Furthermore, fine-tuning Vision-Language Models (VLMs) on spatial reasoning tasks using this dataset has also led to substantial improvements in model performance.

## One-Sentence Claim

Holi-Spatial turns raw web videos into a large automated 3D spatial-intelligence dataset with 3DGS reconstructions, geometry, semantics, grounding, and spatial QA supervision.

## Problem

Spatial intelligence requires large, fine-grained 3D data, but current benchmarks often derive QA pairs from a small number of manually annotated datasets. This limits scale, creates domain gaps, and underrepresents the diversity of raw web video.

The paper asks whether spatial reasoning supervision can be generated automatically from raw video streams at the scale needed for multimodal foundation models.

## Core Contribution

The paper introduces Holi-Spatial, an automated pipeline for constructing spatially aware multimodal data from raw video without human intervention. It supports multiple supervision levels: 3D Gaussian Splatting reconstructions, rendered depth maps, object-level semantic annotations, relational annotations, grounding instances, and spatial QA pairs.

The resulting Holi-Spatial-4M dataset includes 12K optimized 3DGS scenes, 1.3M 2D masks, 320K 3D bounding boxes, 320K instance captions, 1.2M 3D grounding instances, and 1.2M spatial QA pairs.

## Method

The method is a curation pipeline rather than a single model. It starts from raw video, reconstructs 3D scenes as 3DGS assets, renders or extracts geometry such as depth, annotates objects and relations, and derives grounding and QA supervision for spatial reasoning tasks.

The key engineering contribution is chaining reconstruction, geometry extraction, semantic annotation, and QA generation into a fully automated large-scale data factory.

## Experiments and Evidence

Evidence reported in the abstract:

- Dataset scale: 12K 3DGS scenes and millions of masks, captions, grounding instances, and QA pairs.
- Curation-quality comparisons against feed-forward and per-scene optimized methods.
- Evaluation on ScanNet, ScanNet++, and DL3DV.
- Fine-tuning VLMs on Holi-Spatial spatial reasoning tasks improves model performance.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: video source filtering, reconstruction failure rates, annotation validation, QA generation prompts, and licensing/privacy constraints.

## Limits and Failure Modes

- Fully automated curation can scale errors as well as data; quality filters are crucial.
- Web videos may contain biases, privacy-sensitive scenes, or inconsistent camera motion.
- 3DGS reconstructions can fail under dynamic objects, poor texture, reflective surfaces, or sparse views.
- Spatial QA improvements may depend on overlap between generated supervision and evaluation tasks.

## Deep Themes

**Dataset construction is becoming model-building infrastructure.** Holi-Spatial is not just a benchmark; it is a pipeline for producing supervision at foundation-model scale.

**3D spatial intelligence needs layered supervision.** Geometry, objects, relations, grounding, and language QA are combined rather than treated separately.

**Raw web video is a latent 3D corpus.** The paper treats video streams as recoverable spatial scenes, not only 2D temporal data.

## Subthemes

- Automated 3DGS scene reconstruction.
- Multi-level spatial supervision.
- 3D grounding and spatial QA generation.
- Domain-gap reduction through raw web video.
- Dataset scale as spatial-reasoning capability driver.

## Connections to Other Papers

Connects to AdLift and 3DGS-related papers, DLMR and multimodal reasoning, Table-GLS through structured evidence generation, and TerminalTraj/HypoSpace through large automatically validated data resources. It also links to data-governance themes because automated curation quality becomes central to downstream model capability.

## Notes for Cross-Paper Synthesis

Holi-Spatial is a strong example of the corpus-wide shift from hand-built benchmarks to scalable data factories. The common question is no longer only "how does the model reason," but "what pipeline produces the structured world evidence it can learn from?"
