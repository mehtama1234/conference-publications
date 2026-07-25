# Seeing Through the Brain: New Insights from Decoding Visual Stimuli with fMRI

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: 88ZLp7xYxw
- Authors: Zheng Huang; Enpei Zhang; Weikang Qiu; Yinghao Cai; Carl Yang; Elynn Chen; Xiang Zhang; Rex Ying; Dawei Zhou; Yujun Yan
- Primary area: applications to neuroscience & cognitive science
- Keywords: Neuroscience;Functional Magnetic Resonance Imaging;Image reconstruction;Reconstruction
- Source URL: https://openreview.net/forum?id=88ZLp7xYxw
- PDF URL: https://openreview.net/pdf?id=88ZLp7xYxw

## Abstract

Understanding how the brain encodes visual information is a central challenge in neuroscience and machine learning. A promising approach is to reconstruct visual stimuli—essentially images—from functional Magnetic Resonance Imaging (fMRI) signals. This involves two stages: transforming fMRI signals into a latent space and then using a pre-trained generative model to reconstruct images. The reconstruction quality depends on how similar the latent space is to the structure of neural activity and how well the generative model produces images from that space. Yet, it remains unclear which type of latent space best supports this transformation and how it should be organized to represent visual stimuli effectively.

We present two key findings. First, fMRI signals are more similar to the text space of a language model than to either a vision-based space or a joint text–image space. Second, text representations and the generative model should be adapted to capture the compositional nature of visual stimuli, including objects, their detailed attributes, and relationships. Building on these insights, we propose PRISM, a model that Projects fMRI sIgnals into a Structured text space as an interMediate representation for visual stimuli reconstruction. It includes an object-centric diffusion module that generates images by composing individual objects to reduce object detection errors, and an attribute–relationship search module that automatically identifies key attributes and relationships that best align with the neural activity.

Extensive experiments on real-world datasets demonstrate that our framework outperforms existing methods, achieving up to an 8% reduction in perceptual loss. These results highlight the importance of using structured text as the intermediate space to bridge fMRI signals and image reconstruction.

## One-Sentence Claim

PRISM improves fMRI-to-image reconstruction by projecting brain signals into structured text representations that capture objects, attributes, and relationships before image generation.

## Problem

Reconstructing viewed images from fMRI requires mapping neural signals into a latent space that a generative model can use. It is unclear which latent space best matches neural activity and visual-stimulus structure.

The challenge is to bridge noisy brain signals and image generation while preserving compositional visual content.

## Core Contribution

The paper reports that fMRI signals are more similar to language-model text space than to vision-only or joint text-image spaces.

Building on this, it proposes PRISM: Projecting fMRI signals into a Structured text space as an intermediate representation. PRISM adds object-centric diffusion and attribute-relationship search to support compositional reconstruction.

## Method

PRISM maps fMRI signals into structured text representations describing objects, attributes, and relationships. An attribute-relationship search module identifies the semantic details most aligned with neural activity.

An object-centric diffusion module then composes individual objects into reconstructed images, reducing object detection errors relative to less structured generation.

## Experiments and Evidence

The abstract reports extensive real-world dataset experiments and up to an 8 percent reduction in perceptual loss compared with existing methods.

The key empirical finding is that structured text is a better intermediate bridge between fMRI and visual reconstruction than vision or joint text-image latent spaces.

## Limits and Failure Modes

Structured text may omit low-level visual details such as texture, spatial precision, or style, and fMRI signals are noisy and subject-specific.

Because this note is abstract-only, details still need checking: fMRI datasets, subject splits, latent-space similarity measure, text-structure format, diffusion backbone, perceptual metric, and generalization across subjects.

## Deep Themes

- Text as neural-visual bridge: language representations may align surprisingly well with brain encodings of visual scenes.
- Compositional reconstruction: objects, attributes, and relations help structure generative decoding.
- Neuroscience meets foundation models: pretrained generative models become tools for probing brain representation.
- Latent-space choice matters: reconstruction quality depends on matching neural geometry to model geometry.

## Subthemes

- fMRI image reconstruction.
- Structured text intermediate space.
- Object-centric diffusion.
- Attribute-relationship search.

## Connections to Other Papers

This connects to Mind-Omni, BioX-Bridge, and neuroscience/biomedical multimodal transfer papers through cross-modal latent alignment.

It also relates to MetaphorVU and concept binding because structured semantic representations mediate between raw perception and higher-level meaning.

## Notes for Cross-Paper Synthesis

PRISM adds a cross-modal representation insight: language-like structured semantics can serve as a bridge even when neither input nor output is text.
