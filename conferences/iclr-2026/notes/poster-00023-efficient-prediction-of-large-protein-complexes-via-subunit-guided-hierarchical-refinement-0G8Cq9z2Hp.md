# Efficient Prediction of Large Protein Complexes via Subunit-Guided Hierarchical Refinement

## Metadata

- Conference: iclr-2026
- Status: Poster
- OpenReview ID: 0G8Cq9z2Hp
- Authors: Chixiang Lu; Yunhua Zhong; Shikang Liang; Xiaojuan Qi; Haibo Jiang
- Primary area: applications to physical sciences (physics, chemistry, biology, etc.)
- Keywords: Protein complex structure prediction;AlphaFold3;complex modularity
- Source URL: https://openreview.net/forum?id=0G8Cq9z2Hp
- PDF URL: https://openreview.net/pdf?id=0G8Cq9z2Hp

## Abstract

State-of-the-art protein structure predictors have revolutionized structural biology, yet quadratic memory growth with token length makes end-to-end inference impractical for large complexes beyond a few thousand tokens. We introduce \textsc{HierAFold}, a hierarchical pipeline that exploits the modularity of large complexes via PAE-guided (Predicted Aligned Error) subunit decomposition, targeted interface-aware refinement, and confidence-weighted assembly. PAE maps localize rigid intra-chain segments and sparse inter-chain interfaces, enabling joint refinement of likely interacting subunits to capture multi-body cooperativity without increasing memory. \textsc{HierAFold} matches AlphaFold3 accuracy, raises success rates from 49.9\% (CombFold) to 73.1\% on recent PDB set. While for large complexes, it cuts peak memory by $\sim$25\,GB on a 4{,}000-token target ($\sim$40\%), successfully models complexes with over $5{,}000$ tokens that are out-of-memory for AlphaFold3, and raises success rates by two-fold compared with CombFold.

## One-Sentence Claim

TODO

## Problem

TODO

## Core Contribution

TODO

## Method

TODO

## Experiments and Evidence

TODO

## Limits and Failure Modes

TODO

## Deep Themes

TODO

## Subthemes

TODO

## Connections to Other Papers

TODO

## Notes for Cross-Paper Synthesis

TODO
