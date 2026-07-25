# Common Corpus: The Largest Collection of Ethical Data for LLM Pre-Training

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: 0wSlFpMsGb
- Authors: Pierre-Carl Langlais; Pavel Chizhov; Catherine Arnett; Carlos Rosas Hinostroza; Mattia Nee; Eliot Krzysztof Jones; Irène Girard; David Mach; Anastasia Stasenko; Ivan P. Yamshchikov
- Primary area: datasets and benchmarks
- Keywords: dataset;pre-training;large language models;open data;open science;multilingual
- Source URL: https://openreview.net/forum?id=0wSlFpMsGb
- PDF URL: https://openreview.net/pdf?id=0wSlFpMsGb

## Abstract

Large Language Models (LLMs) are pre-trained on large data from different sources and domains. These data most often contain trillions of tokens with large portions of copyrighted or proprietary content, which hinders the usage of such models under AI legislation. This raises the need for truly open pre-training data that is compliant with the data security regulations. In this paper, we introduce Common Corpus, the largest open dataset for LLM pre-training. The data assembled in Common Corpus are either uncopyrighted or under permissible licenses and amount to about two trillion tokens. The dataset contains a wide variety of languages, ranging from the high-resource European languages to some low-resource languages rarely represented in pre-training datasets. In addition, it includes a large portion of code data. The diversity of data sources in terms of covered domains and time periods opens up the paths for both research and entrepreneurial needs in diverse areas of knowledge. In this paper, we present the detailed provenance of data assembling and the details of dataset filtering and curation. We train two small language models on Common Corpus and find that the resulting model performs comparably to other models of their size, indicating that our dataset is suitable for multilingual pretraining. Common Corpus represents a key contribution to the ecosystem for open science research on large language models.

## One-Sentence Claim

Common Corpus provides a two-trillion-token, permissively licensed multilingual pretraining corpus intended to make LLM development legally safer, more open, and suitable for both research and commercial use.

## Problem

LLM pretraining datasets often contain copyrighted, proprietary, or legally ambiguous material, which limits transparent research and creates deployment risk under emerging AI regulation. Open science also needs large-scale multilingual data that is not restricted to high-resource languages.

## Core Contribution

The paper introduces Common Corpus, a very large open pretraining dataset with documented provenance, filtering, curation, multilingual coverage, code content, and permissive licensing or uncopyrighted status.

## Method

The work is primarily dataset construction. It assembles data from diverse sources and time periods, filters and curates the corpus, documents provenance, and trains two small language models as suitability checks for multilingual pretraining.

## Experiments and Evidence

The abstract reports that small models trained on Common Corpus perform comparably to other models of similar size. Evidence to verify in the PDF: exact sources, license audit procedure, language distribution, filtering rules, contamination checks, benchmark set, and model-training details.

## Limits and Failure Modes

Potential limits include residual licensing uncertainty, uneven language/domain quality, filtering bias, benchmark contamination, and the fact that small-model validation may not fully predict performance at frontier scale.

## Deep Themes

- Data governance is becoming core ML infrastructure.
- Open data is framed as both a scientific and regulatory requirement.
- Dataset provenance and licensing are becoming part of model capability claims.

## Subthemes

- Ethical pretraining data.
- Multilingual LLM corpora.
- Open science infrastructure.
- Data provenance.
- Legal compliance for AI.

## Connections to Other Papers

Connects to synthetic/data-quality work, benchmark construction, model governance, and safety/privacy papers. It is a dataset-side counterpart to papers that focus on post-training alignment or model-level safety.

## Notes for Cross-Paper Synthesis

This is evidence for a major 2026 pattern: the data substrate is being treated as a first-class research artifact. The contribution is not a new architecture but an attempt to make large-model training reproducible, lawful, and multilingual.
