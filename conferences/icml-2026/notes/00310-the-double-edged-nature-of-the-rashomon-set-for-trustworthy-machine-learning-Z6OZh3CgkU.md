# The Double-Edged Nature of the Rashomon Set for Trustworthy Machine Learning

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: Z6OZh3CgkU
- Authors: Ethan Hsu; Harry Chen; Chudi Zhong; Lesia Semenova
- Primary area: social_aspects->accountability_transparency_and_interpretability
- Keywords: Trustworthy ML;Rashomon Effect;Interpretable Model
- Source URL: https://openreview.net/forum?id=Z6OZh3CgkU
- PDF URL: https://openreview.net/pdf?id=Z6OZh3CgkU

## Abstract

Real-world machine learning (ML) pipelines rarely produce a single model; instead, they produce a Rashomon set of many near-optimal ones. We show that this multiplicity reshapes key aspects of trustworthiness. At the individual-model level, sparse interpretable models tend to preserve privacy but are fragile to adversarial attacks. In contrast, the diversity within a large Rashomon set enables reactive robustness: even when an attack compromises one model, a practitioner can switch to a different near-optimal model that remains accurate, without retraining.  However, the same diversity increases information leakage, as disclosing more near-optimal models provides an attacker with progressively richer views of the training data. This produces a robustness–privacy trade-off governed by diversity, which we analyze theoretically and empirically. Beyond this trade-off, Rashomon sets are stable under small distribution shifts, so a set computed once remains valid under such shifts without re-computation. Our results highlight the dual role of Rashomon sets as both a resource and a risk for trustworthy ML.

## One-Sentence Claim

Rashomon sets improve reactive robustness by offering alternative near-optimal models, but their diversity also increases training-data leakage and creates a robustness-privacy tradeoff.

## Problem

ML pipelines often produce many near-optimal models rather than one uniquely best model. This Rashomon multiplicity is usually viewed as helpful for interpretability or model choice, but its trustworthiness implications are more complex.

The paper asks how the size and diversity of a Rashomon set affect privacy, adversarial robustness, and stability under distribution shift.

## Core Contribution

The paper shows a double-edged effect. At the individual-model level, sparse interpretable models tend to preserve privacy but are fragile to adversarial attacks. At the set level, diversity enables reactive robustness: if one model is attacked, a practitioner can switch to another near-optimal model without retraining.

However, revealing more models from a diverse Rashomon set leaks more information about the training data. The paper analyzes this robustness-privacy tradeoff theoretically and empirically, and finds Rashomon sets can remain stable under small distribution shifts.

## Method

The method treats the Rashomon set itself as the object of trust analysis. It measures or bounds individual model privacy/robustness, then studies how model diversity changes leakage and the ability to switch after attack.

Distribution-shift stability is analyzed by asking whether a set computed once remains near-optimal after small shifts.

## Experiments and Evidence

Evidence reported in the abstract:

- Theoretical and empirical analysis of diversity-governed robustness/privacy tradeoffs.
- Individual sparse interpretable models preserve privacy but are adversarially fragile.
- Large Rashomon sets enable reactive robustness through switching.
- Disclosing more near-optimal models increases information leakage.
- Rashomon sets remain stable under small distribution shifts.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: privacy metric, attack model, model classes, diversity measure, and shift assumptions.

## Limits and Failure Modes

- Reactive robustness assumes practitioners can detect attack and switch appropriately.
- Publishing many models can leak data; keeping them private may reduce transparency.
- Stability under small shifts may fail under targeted or structural shifts.
- Sparse interpretable models vary widely in privacy and robustness depending on feature design.

## Deep Themes

**Multiplicity is both resource and risk.** Many near-optimal models provide options but expose more information.

**Trustworthiness tradeoffs move from model to set.** Robustness, privacy, and interpretability depend on the ensemble of available models, not only one selected model.

**Diversity governs security properties.** The same diversity that enables switching also reveals richer views of training data.

## Subthemes

- Rashomon-set diversity.
- Reactive robustness.
- Privacy leakage from model disclosure.
- Sparse interpretable model fragility.
- Stability under small distribution shifts.

## Connections to Other Papers

Connects to Falling Trees and Rashomon-set learning, TRECA/ROCP high-stakes decision systems, and privacy papers such as PRISM and IHM. It also links to ME Ensemble because both treat sets of models as operational objects, though with different trust and efficiency goals.

## Notes for Cross-Paper Synthesis

This paper adds an important governance warning: providing more acceptable models can improve resilience but also expands the information surface exposed to attackers.
