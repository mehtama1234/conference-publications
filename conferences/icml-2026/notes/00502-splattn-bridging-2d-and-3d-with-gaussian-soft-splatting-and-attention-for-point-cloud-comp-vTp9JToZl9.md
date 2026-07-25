# SplAttN: Bridging 2D and 3D with Gaussian Soft Splatting and Attention for Point Cloud Completion

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: vTp9JToZl9
- Authors: Zhaoyang Li; Zhichao You; Tianrui Li
- Primary area: applications->computer_vision
- Keywords: Point Cloud Completion;Multimodal Learning;Gaussian Splatting;Differentiable Rendering;Cross-Modal Attention
- Source URL: https://openreview.net/forum?id=vTp9JToZl9
- PDF URL: https://openreview.net/pdf?id=vTp9JToZl9

## Abstract

Although multi-modal learning has advanced point cloud completion, the theoretical mechanisms remain unclear. Recent works attribute success to the connection between modalities, yet we identify that standard hard projection severs this connection: projecting a sparse point cloud onto the image plane yields an extremely sparse support, which hinders visual prior propagation, a failure mode we term Cross-Modal Entropy Collapse. To address this practical limitation, we propose SplAttN, which replaces hard projection with Differentiable Gaussian Splatting to produce a dense, continuous image-plane representation. By reformulating projection as continuous density estimation, SplAttN avoids collapsed sparse support, facilitates gradient flow, and improves cross-modal connection learnability. Extensive experiments show that SplAttN achieves state-of-the-art performance on PCN and ShapeNet-55/34. Crucially, we utilize the real-world KITTI benchmark as a stress test for multi-modal reliance. Counter-factual evaluation reveals that while baselines degenerate into unimodal template retrievers insensitive to visual removal, SplAttN maintains a robust dependency on visual cues, validating that our method establishes an effective cross-modal connection. Code is available at https://github.com/zay002/SplAttN.

## One-Sentence Claim

SplAttN fixes cross-modal entropy collapse in point-cloud completion by replacing sparse hard projection with differentiable Gaussian splatting that preserves dense 2D-3D visual connections.

## Problem

Multimodal point-cloud completion uses image priors to fill missing 3D structure, but hard projection from sparse point clouds to the image plane creates extremely sparse support. This breaks the pathway by which visual information should propagate into 3D completion.

The paper names this failure Cross-Modal Entropy Collapse: the apparent multimodal model can degenerate into a weakly connected or effectively unimodal system.

## Core Contribution

The paper proposes SplAttN, which reformulates projection as continuous density estimation via differentiable Gaussian splatting. This creates a dense image-plane representation that supports gradient flow and cross-modal attention.

The contribution is not only performance improvement but a diagnostic: counterfactual evaluation on KITTI shows whether completion actually depends on visual cues rather than using images as ignored side information.

## Method

SplAttN replaces hard point projection with soft Gaussian splats, spreading each projected 3D point over a continuous image-plane density. This avoids collapsed sparse supports and gives attention modules a learnable bridge between 2D visual features and 3D geometry.

Cross-modal attention then uses this dense splatted representation to propagate visual priors into point-cloud completion.

## Experiments and Evidence

The abstract reports state-of-the-art performance on PCN and ShapeNet-55/34. KITTI is used as a real-world stress test for multimodal reliance.

Counterfactual evaluation shows baselines can degrade into unimodal template retrievers insensitive to visual removal, while SplAttN maintains robust dependence on visual cues.

## Limits and Failure Modes

Gaussian splatting introduces kernel/scale choices that may affect fine geometry. Dense splats can blur small structures or create misleading visual support under calibration errors.

The method assumes useful image-point alignment. Severe sensor misalignment, occlusion, or domain shift may weaken the visual bridge.

## Deep Themes

- Cross-modal connection as measurable mechanism: multimodal performance should depend on the auxiliary modality.
- Soft projection for gradient flow: continuous density avoids sparse-support collapse.
- Counterfactual modality reliance: removing visual cues tests whether the model truly uses them.
- Geometry-aware multimodal fusion: projection operators shape what attention can learn.

## Subthemes

- Hard projection can sever 2D-3D information flow.
- Gaussian splatting bridges rendering and representation learning.
- Template retrieval is a hidden failure mode in point completion.
- Real-world KITTI stresses modality reliance beyond synthetic benchmarks.

## Connections to Other Papers

SplAttN connects to WIRE, ConFlux, and DroneDINO through domain-specific representation geometry. It also relates to concept binding and RFCMH because cross-modal systems must preserve meaningful connections rather than merely co-train modalities.

It fits the evaluation theme shared with PIPE and MiniAppBench: counterfactual tests reveal whether the intended mechanism is actually used.

## Notes for Cross-Paper Synthesis

The synthesis point is that multimodality must be causal, not decorative. Good benchmarks should test whether removing a modality changes behavior in the expected way.
