# Is Data Shapley Not Better than Random in Data Selection? Ask NASH

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: vMsrm8UGGC
- Authors: Xiao Tian; Jue Fan; Rachael Hwee Ling Sim; Wang Zixuan; Nancy F. Chen; Bryan Kian Hsiang Low
- Primary area: social_aspects->accountability_transparency_and_interpretability
- Keywords: Data Shapley;data selection;data valuation;semivalues;Shapley value
- Source URL: https://openreview.net/forum?id=vMsrm8UGGC
- PDF URL: https://openreview.net/pdf?id=vMsrm8UGGC

## Abstract

Data selection studies the problem of identifying high-quality subsets of training data. While some existing works have considered selecting the subset of data with top-$m$ Data Shapley or other semivalues as they account for the interaction among every subset of data, other works argue that Data Shapley can sometimes perform ineffectively in practice and select subsets that are *no better than random*. This raises the questions: **(I)** *Are there certain "Shapley-informative" settings where Data Shapley consistently works well?* **(II)** *Can we strategically utilize these settings to select high-quality subsets consistently and efficiently?*
In this paper, we propose a novel data selection framework, **NASH** (Non-linear Aggregation of SHapley-informative components), which **(I)** decomposes the target utility function (e.g., validation accuracy) into simpler, Shapley-informative component functions, and selects data by optimizing an objective that **(II)** aggregates these components non-linearly. We demonstrate that NASH substantially boosts the effectiveness of Shapley/semivalue-based data selection with minimal additional runtime cost.

## One-Sentence Claim

NASH improves Shapley/semivalue data selection by decomposing target utility into Shapley-informative components and nonlinearly aggregating them before subset selection.

## Problem

Data Shapley values are appealing because they account for data interactions across subsets, but practical data selection results are mixed. Some studies find Shapley-based selection no better than random.

The paper asks when Shapley values are informative and how to exploit those settings efficiently. A single target utility such as validation accuracy may be too complex or noisy for raw Data Shapley to rank examples reliably.

## Core Contribution

The paper proposes NASH, Non-linear Aggregation of SHapley-informative components. It decomposes the target utility into simpler component functions where Shapley or semivalue estimates are more informative.

Then it selects data by optimizing a nonlinear aggregation of those components, substantially improving semivalue-based data selection with minimal extra runtime cost.

## Method

NASH first identifies or constructs component utility functions that better satisfy conditions under which Shapley rankings correlate with useful data contributions. Each component can be valued separately.

The component valuations are then combined through a nonlinear objective for subset selection, allowing interactions among components to shape the final selected set more robustly than a single global Shapley score.

## Experiments and Evidence

The abstract reports substantial boosts in Shapley/semivalue-based data selection effectiveness with minimal additional runtime. It frames results around resolving cases where Data Shapley appears no better than random.

Full-paper reading should verify datasets, model families, component definitions, runtime overhead, comparison to random and other data-selection baselines, and sensitivity to component choice.

## Limits and Failure Modes

NASH depends on finding useful Shapley-informative components. If decomposition is poorly chosen, nonlinear aggregation may add complexity without improving selection.

Shapley estimation can still be expensive or noisy for large datasets, and component utility functions may encode implicit task assumptions.

## Deep Themes

- Data valuation through decomposition: global utility is broken into more informative components.
- Semivalue repair rather than rejection: Shapley can work when applied to the right utility structure.
- Nonlinear aggregation for subset quality: selection should combine component evidence rather than rank by one scalar.
- Efficient data curation: improved selection must not erase gains through large runtime overhead.

## Subthemes

- Shapley informativeness is setting-dependent.
- Validation accuracy may be too blunt as a utility function.
- Component-level valuation exposes distinct training-data roles.
- Random-selection parity is a diagnostic of utility misspecification.

## Connections to Other Papers

NASH connects to OPUS, NS/IF attribution, and local redundancy through data valuation and training utility estimation. It also relates to categorical ANOVA and SHAP work because all refine attribution under better structural assumptions.

It fits the broader data-governance theme: selecting data requires matching the valuation method to the downstream utility.

## Notes for Cross-Paper Synthesis

The synthesis point is that attribution methods fail when the target utility is poorly factorized. Decomposition can make valuation signals actionable again.
