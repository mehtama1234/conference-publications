# Towards the Explainability of Temporal Graph Networks via Memory Backtracking and Topological Attribution

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: sKAgLgpujy
- Authors: Yazheng Liu; Xi Zhang; Sihong Xie; Hui Xiong
- Primary area: social_aspects->accountability_transparency_and_interpretability
- Keywords: Temporal graph networks;memory backtracking tree;LRP;explanations
- Source URL: https://openreview.net/forum?id=sKAgLgpujy
- PDF URL: https://openreview.net/pdf?id=sKAgLgpujy

## Abstract

Temporal graphs are ubiquitous in real-world applications and Temporal Graph Networks (TGNs) have achieved superior predictive accuracy. 
Understanding which historical events drive 
model predictions can enhance trustworthiness of TGNs. Existing explanation methods overlook the memory module, the core component that records and updates node histories, leaving the influence of past events unexplored. To address this, we attribute TGNs predictions through the topology attribution tree and memory backtracking tree. The topology attribution tree captures the influence of neighbors and their memory vectors, then the memory backtracking tree quantifies how historical events shape node memory vectors. We apply the LRP in TGNs, 
ensuring that the total contribution of events equals the model’s logits. Finally, top-k selection may be unfaithful due to the nonlinear mapping from logits to probabilities, we design optimization objectives to identify the important events. Experiments on nine temporal graph datasets, spanning node property prediction, link prediction tasks and graph classification tasks, show that our method provides faithful explanations and outperforms state-of-the-art baselines. The code is available at https://github.com/yazhengliu/MemExplainer.

## One-Sentence Claim

Temporal Graph Network predictions can be explained faithfully by backtracking both topological neighbor influence and memory-module history, with relevance propagation conserving contribution to logits.

## Problem

Temporal Graph Networks achieve strong predictive performance on dynamic graph tasks, but their memory modules make explanations difficult. Existing explainers often focus on graph topology and overlook how historical events update node memory.

For temporal graphs, the key question is not only which neighbors matter now, but which past events shaped the memory vectors that drive current predictions.

## Core Contribution

The paper proposes explanations through two complementary structures: a topology attribution tree for neighbors and memory vectors, and a memory backtracking tree for historical events that shaped node memory.

It applies layer-wise relevance propagation to TGNs so event contributions sum to the model's logits. It also argues that naive top-k selection can be unfaithful because logits map nonlinearly to probabilities, motivating optimization objectives for selecting important events.

## Method

The topology attribution tree traces influence through current graph neighbors and their memory states. The memory backtracking tree recursively tracks how historical events updated those memory states.

LRP assigns relevance through these structures while conserving total contribution at the logit level. Important-event selection is framed through optimization objectives rather than simple top-k probability heuristics.

## Experiments and Evidence

The abstract reports experiments on nine temporal graph datasets covering node property prediction, link prediction, and graph classification. The method provides faithful explanations and outperforms state-of-the-art baselines.

Full-paper reading should verify faithfulness metrics, dataset list, TGN variants, runtime of memory backtracking, and whether explanations remain understandable for long event histories.

## Limits and Failure Modes

Memory backtracking can become large in long temporal histories, requiring pruning or approximation. Explanations may be faithful to the model's logits but still hard for users to interpret if many events interact.

LRP-based attributions depend on implementation choices and may behave differently across TGN architectures. Faithfulness to logits does not imply causal faithfulness to the real temporal process.

## Deep Themes

- Memory-aware explainability: temporal models require explanations of stored history, not just current structure.
- Conservation-based attribution: relevance is propagated so event contributions sum to logits.
- Topology plus chronology: graph explanations must combine neighbor influence and historical event influence.
- Faithful selection over nonlinear outputs: important event choice should respect logit/probability transformations.

## Subthemes

- Memory modules are central hidden state in TGNs.
- Historical events can influence predictions indirectly through node memory.
- Top-k attribution can be misleading under nonlinear probability maps.
- Temporal graph explainers need task-general validation.

## Connections to Other Papers

This paper connects to categorical ANOVA, Verified SHAP, and NS/IF attribution through exact or faithful explanation methods. It also relates to recurrent/long-horizon memory papers such as JitRL and CoEvol-NO because memory is treated as a causal carrier of past information.

It fits the broader interpretability-as-intervention theme by making hidden temporal state auditable.

## Notes for Cross-Paper Synthesis

The synthesis point is that explainability must follow the architecture's actual information pathways. For TGNs, the path runs through memory updates over time, so static graph explanations miss the main mechanism.
