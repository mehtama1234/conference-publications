# Multimodal Aligned Semantic Knowledge for Unpaired Image-text Matching

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: d3CISVVO6v
- Authors: Laiguo Yin; Yixin Zhang; YUQING SUN; Lizhen Cui
- Primary area: applications to computer vision, audio, language, and other modalities
- Keywords: Unpaired Image-text Matching;Out-of-Distribution Word;Multimodal Aligned Semantic Knowledge;Prototype
- Source URL: https://openreview.net/forum?id=d3CISVVO6v
- PDF URL: https://openreview.net/pdf?id=d3CISVVO6v

## Abstract

While existing approaches address unpaired image-text matching by constructing cross-modal aligned knowledge, they often fail to identify semantically corresponding visual representations for Out-of-Distribution (OOD) words. Moreover, the distributional variance of visual representations associated with different words varies significantly, which negatively impacts matching accuracy. To address these issues, we propose a novel method namely Multimodal Aligned Semantic Knowledge (MASK), which leverages word embeddings as bridges to associate words with their corresponding prototypes, thereby enabling semantic knowledge alignment between the image and text modalities. For OOD words, the representative prototypes are constructed by leveraging the semantic relationships encoded in word embeddings. Beyond that, we introduce a prototype consistency contrastive loss to structurally regularize the feature space, effectively mitigating the adverse effects of variance. Experimental results on the Flickr30K and MSCOCO datasets demonstrate that MASK achieves superior performance in unpaired matching.

## One-Sentence Claim

MASK improves unpaired image-text matching by using word embeddings to construct visual prototypes for in-distribution and OOD words, with contrastive prototype consistency to control variance.

## Problem

Unpaired image-text matching needs aligned semantic knowledge across modalities without paired supervision.

Existing methods struggle with OOD words and with varying visual-representation variance across words, which hurts matching accuracy.

## Core Contribution

The paper proposes Multimodal Aligned Semantic Knowledge.

MASK uses word embeddings as bridges from words to corresponding visual prototypes, including constructing representative prototypes for OOD words from semantic relationships in the embedding space.

## Method

MASK aligns image and text modalities through prototype associations derived from word embeddings.

A prototype consistency contrastive loss regularizes the feature space so visual representations tied to different words remain structurally coherent despite variance differences.

## Experiments and Evidence

The abstract reports experiments on Flickr30K and MSCOCO.

MASK achieves superior performance for unpaired image-text matching.

## Limits and Failure Modes

Word embeddings may encode biased or incomplete semantic relationships, especially for rare or visually ambiguous OOD words. Prototype construction may fail for words without stable visual referents.

Because this note is abstract-only, details still need checking: prototype construction, OOD split, embedding source, contrastive loss, baselines, and retrieval/matching metrics.

## Deep Themes

- Semantic bridges for unpaired alignment: text embeddings provide structure when paired image-text data is absent.
- OOD word grounding: prototypes can extend visual matching beyond seen vocabulary.
- Variance-aware representation regularization: different concepts have different visual spread.
- Prototype-based multimodal knowledge: cross-modal alignment is organized around semantic anchors.

## Subthemes

- Unpaired image-text matching.
- Out-of-distribution words.
- Visual prototypes.
- Prototype consistency contrastive loss.

## Connections to Other Papers

This connects to WAVE, MF-GIA, CorreGen, and multimodal representation alignment papers.

It also relates to CLIP/DINO feature work and AnyUp because all concern reusable representation spaces.

## Notes for Cross-Paper Synthesis

MASK adds a cross-modal alignment theme: when direct pairs are missing, semantic prototypes can act as anchors for modality matching.
