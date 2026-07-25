# On the Origin of Neural Scaling Laws: from Random Graphs to Natural Language

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: mu17VSX8q9
- Authors: Maissam Barkeshli; Alberto Alfarano; Andrey Gromov
- Primary area: deep_learning
- Keywords: Neural scaling laws;Language modeling;Compute-optimal training
- Source URL: https://openreview.net/forum?id=mu17VSX8q9
- PDF URL: https://openreview.net/pdf?id=mu17VSX8q9

## Abstract

Scaling laws have played a major role in modern AI, providing predictive power over how model performance will improve with increasing resources. This has spurred intense interest in their origin, with a common suggestion being that they arise from power laws already present in the data. Here we study scaling laws for transformers trained to predict random walks on graphs with tunable complexity. We show that this simplified setting already yields scaling laws even in the absence of power laws in the data correlations. We further consider dialing down the complexity of language by training on sequences sampled from increasingly simplified generative language models, from 4,2,1-layer transformer language models down to language bigrams, revealing a monotonic evolution of the scaling exponents. Our results also include scaling laws obtained from training on random walks on random graphs drawn from Erdös-Renyi and scale-free Barabási-Albert ensembles. Finally, we revisit scaling laws for language modeling, demonstrating that several essential results can be reproduced using 2 layer transformers with context length of 100, demonstrate an alternative method for obtaining compute optimal curves, and provide preliminary evidence that maximal update parameterization may be more parameter efficient than standard parameterization.

## One-Sentence Claim

Scaling laws can arise from transformer learning dynamics even when the data lacks power-law correlations, as shown by controlled random-graph and simplified-language experiments.

## Problem

Neural scaling laws are central to modern model planning, but their origin remains disputed. A common explanation is that scaling laws reflect power-law structure already present in natural data. If true, scaling behavior would be mostly a property of the dataset; if false, it may emerge from model architecture, optimization, and task complexity more generally.

The challenge is to build settings simple enough to control data complexity while still rich enough to reproduce scaling behavior. Natural language alone is too entangled to isolate causal factors.

## Core Contribution

The paper contributes controlled experiments showing scaling laws in transformers trained on random walks over graphs, including settings without power-law data correlations. It then gradually simplifies language generation from multi-layer transformer language models down to bigrams, observing monotonic changes in scaling exponents.

The deeper contribution is a bridge between toy complexity-controlled processes and natural language scaling. It argues that scaling laws do not require power-law data statistics as their primitive cause; they can emerge from how transformer learners approximate structured sequence processes.

## Method

The authors train transformers to predict random walks on graph ensembles with tunable complexity, including Erdos-Renyi and Barabasi-Albert random graphs. These graph processes provide a way to vary structural complexity and correlation properties while measuring loss scaling with model/data/compute.

They also train on sequences produced by increasingly simplified generative language models, from 4-, 2-, and 1-layer transformer language models down to language bigrams. This creates a ladder from naturalistic language-like structure to much simpler sequence statistics, letting the scaling exponent evolve under controlled simplification.

## Experiments and Evidence

The abstract reports that graph random-walk prediction yields scaling laws even without power-law correlations in the data. It also reports monotonic evolution of scaling exponents as language sources are simplified, plus reproduction of key language-model scaling results using small 2-layer transformers with context length 100.

The paper further offers an alternative way to obtain compute-optimal curves and preliminary evidence that maximal update parameterization may be more parameter-efficient than standard parameterization. Full-paper reading is needed to evaluate the exact exponent-fitting methodology and robustness checks.

## Limits and Failure Modes

Controlled synthetic settings clarify mechanisms but may omit important aspects of real language, such as semantic compositionality, long-context dependencies, multimodal grounding, and heterogeneous data mixtures. Showing that scaling laws can arise without data power laws does not prove that natural-language scaling is independent of real data statistics.

The mup parameterization result is described as preliminary in the abstract, so it should be treated as suggestive until the full experiments and confidence intervals are inspected.

## Deep Themes

- Theory through controllable worlds: simplified graph and language generators are used to isolate mechanisms behind large-scale empirical laws.
- Scaling laws as emergent learner-data interaction: exponents reflect task complexity, architecture, and optimization, not just raw corpus statistics.
- Compute planning from small models: small controlled transformers can reproduce qualitative scaling phenomena.
- Parameterization as scaling infrastructure: maximal update parameterization appears as a possible lever for more efficient scaling.

## Subthemes

- Random-walk prediction becomes a laboratory for studying sequence-model scaling.
- Simplified language models create a continuum between toy processes and natural text.
- Power laws in observed data are not necessary for power-law-like learning curves.
- Compute-optimal training curves can be studied with cheaper controlled experiments.

## Connections to Other Papers

This paper connects to NorMuon, OPUS, and other efficiency papers because all ask how to extract better capability from a fixed compute budget. It also relates to theoretical papers that explain empirical practice: instead of proposing a new benchmark or model, it studies why a planning rule used across frontier-model training may work.

It sits beside CV relative instability and FTRL lower-bound work as a caution that empirical regularities need mechanistic explanation before they become reliable engineering doctrine.

## Notes for Cross-Paper Synthesis

The cross-paper pattern is "make the large-scale law small enough to interrogate." ICML 2026 contains many attempts to turn frontier-model heuristics into controlled mechanisms, whether for scaling, optimization, data selection, or attribution.
