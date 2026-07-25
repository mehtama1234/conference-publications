# Breaking the Reversal Curse in Autoregressive Language Models via Identity Bridge

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: kKUrbW8xJ3
- Authors: Xutao Ma; Yixiao Huang; Hanlin Zhu; Somayeh Sojoudi
- Primary area: theory->learning_theory
- Keywords: reversal curse;implicit bias;transformer
- Source URL: https://openreview.net/forum?id=kKUrbW8xJ3
- PDF URL: https://openreview.net/pdf?id=kKUrbW8xJ3

## Abstract

Autoregressive large language models (LLMs) have achieved remarkable success in many complex tasks, yet they can still fail in very simple logical reasoning such as the "reversal curse" --- when trained on forward knowledge data of the form "$A \rightarrow B$" (e.g., Alice's husband is Bob), the model is unable to deduce the reversal knowledge "$B \leftarrow A$" (e.g., Bob's wife is Alice) during test. Extensive prior research suggests that this failure is an inherent, fundamental limit of autoregressive causal LLMs, indicating that these models tend to memorize factual-level knowledge rather than capture higher-level rules. In this paper, we challenge this view by showing that this seemingly fundamental limit can be mitigated by slightly tweaking the training data with a simple regularization data recipe called the Identity Bridge of the form "$A \to A$" (e.g., The name of Alice is Alice). Theoretically, we prove that under this recipe, even a one-layer transformer can break the reversal curse by analyzing the implicit bias of gradient descent. Empirically, we show that a 1B pretrained language model finetuned with the proposed data recipe achieves a 50\% success rate on reversal tasks, in stark contrast to a near-zero success rate when trained solely on forward-knowledge data. Our work provides a novel theoretical foundation for the reversal curse and offers a principled, low-cost path to encouraging LLMs to learn higher-level rules from data.

## One-Sentence Claim

Adding simple identity-bridge examples such as A -> A can make autoregressive Transformers learn reversible relational rules rather than only memorizing forward facts.

## Problem

Autoregressive LLMs often exhibit the reversal curse: training on A -> B facts does not make them infer B -> A queries. This has been viewed as a fundamental limitation of causal language modeling and evidence that models memorize facts instead of abstract relations.

The paper asks whether a small data-recipe change can alter the implicit bias of training enough to support reversal.

## Core Contribution

The contribution is the Identity Bridge data recipe, which adds examples of the form A -> A. The paper theoretically proves that, under this recipe, even a one-layer Transformer can break the reversal curse by changing the implicit bias of gradient descent.

Empirically, a 1B pretrained language model finetuned with identity bridges reaches 50% success on reversal tasks, compared with near-zero success from forward-only training.

## Method

The method augments factual training data with identity examples that explicitly connect entities to themselves. These examples provide a bridge in representation space or attention behavior that lets forward relations be reused for reverse queries.

The theoretical analysis studies gradient-descent implicit bias in a one-layer Transformer to explain why the bridge encourages rule-level learning.

## Experiments and Evidence

Evidence reported in the abstract:

- Theoretical proof for a one-layer Transformer under the identity-bridge recipe.
- Implicit-bias analysis of gradient descent.
- 1B pretrained language model finetuning experiment.
- 50% success on reversal tasks with identity bridges.
- Near-zero success with forward-knowledge-only data.
- Low-cost data augmentation recipe.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: reversal dataset, bridge ratio, generality across relation types, and whether performance scales above 50%.

## Limits and Failure Modes

- Identity bridges may not handle complex many-to-many or asymmetric relations.
- 50% success is a major improvement but not full rule mastery.
- The one-layer proof may not directly characterize large pretrained models.
- Data recipes can create artifacts if identity examples are overrepresented.

## Deep Themes

**Data can shape implicit rules.** A tiny augmentation changes whether the model learns relation structure.

**Memorization failures may not be architectural absolutes.** The reversal curse can be mitigated without abandoning autoregressive training.

**Identity anchors support relational transfer.** Self-links help connect entity representations across query directions.

## Subthemes

- Reversal curse.
- Identity Bridge data augmentation.
- Transformer implicit bias.
- Rule learning versus factual memorization.
- Low-cost relational generalization.

## Connections to Other Papers

Connects to Context-Parameter Equivalence, Symmetry ICL Dynamics, 2-SAT Robustness, and PRISM. It also relates to data-design papers showing that small dataset structure can change reasoning behavior.

## Notes for Cross-Paper Synthesis

Identity Bridge adds a data-mechanism lesson: some reasoning failures may be fixed by examples that expose the intended invariance, not merely by scaling model or data volume.
