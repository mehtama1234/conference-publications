# From movement to cognitive maps: recurrent neural networks reveal how locomotor development shapes hippocampal spatial coding

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: 8bM7MkxJee
- Authors: Marco P Abrate; Laurenz Muessig; Joshua P Bassett; Hui Min Tan; Francesca Cacucci; Thomas Joseph Wills; Caswell Barry
- Primary area: applications to neuroscience & cognitive science
- Keywords: recurrent neural network;spatial representations;hippocampus;development;locomotion;rats
- Source URL: https://openreview.net/forum?id=8bM7MkxJee
- PDF URL: https://openreview.net/pdf?id=8bM7MkxJee

## Abstract

The hippocampus contains neurons whose firing correlates with an animal's location and orientation in space. Collectively, these neurons are held to support a cognitive map of the environment, enabling the recall of and navigation to specific locations. Although recent studies have characterised the timelines of spatial neuron development, no unifying mechanistic model has yet been proposed. Moreover, the processes driving the emergence of spatial representations in the hippocampus remain unclear (Tan et al., 2017). Here, we combine computational analysis of postnatal locomotor development with a recurrent neural network (RNN) model of hippocampal function to demonstrate how changes in movement statistics -- and the resulting sensory experiences -- shape the formation of spatial tuning. First, we identify distinct developmental stages in rat locomotion during open-field exploration using published experimental data. Then, we train shallow RNNs to predict upcoming visual stimuli from concurrent visual and vestibular inputs, exposing them to trajectories that reflect progressively maturing locomotor patterns. Our findings reveal that these changing movement statistics drive the sequential emergence of spatially tuned units, mirroring the developmental timeline observed in rats. The models generate testable predictions about how spatial tuning properties mature -- predictions we confirm through analysis of hippocampal recordings. Critically, we demonstrate that replicating the specific statistics of developmental locomotion -- rather than merely accelerating sensory change -- is essential for the emergence of an allocentric spatial representation. These results establish a mechanistic link between embodied sensorimotor experience and the ontogeny of hippocampal spatial neurons, with significant implications for neurodevelopmental research and predictive models of navigational brain circuits.

## One-Sentence Claim

Developmental locomotor statistics can drive the sequential emergence of hippocampal-like spatial representations in RNNs trained on visual and vestibular prediction.

## Problem

The hippocampus develops spatially tuned neurons that support cognitive maps, but the mechanisms driving their emergence remain unclear. Prior work characterizes developmental timelines but does not provide a unifying computational model.

The central question is how embodied movement and sensory experience shape the formation of allocentric spatial coding.

## Core Contribution

The paper links postnatal locomotor development to hippocampal spatial representation formation using shallow recurrent neural networks.

It shows that RNNs exposed to progressively maturing locomotor trajectories develop spatially tuned units in a sequence that mirrors rat hippocampal development, and that specific developmental movement statistics are necessary for allocentric representations.

## Method

The authors analyze published rat locomotion data to identify developmental stages during open-field exploration. They then train shallow RNNs to predict upcoming visual stimuli from concurrent visual and vestibular inputs.

The RNNs are exposed to trajectories matching progressively mature locomotor patterns. The resulting units are analyzed for spatial tuning and compared against hippocampal recordings.

## Experiments and Evidence

The abstract reports that changing movement statistics drive sequential emergence of spatially tuned units, matching observed developmental timelines in rats.

The model generates predictions about maturation of spatial tuning properties, which the authors confirm through analysis of hippocampal recordings. Replicating developmental locomotion statistics is essential; merely accelerating sensory change is insufficient.

## Limits and Failure Modes

The model is shallow and predictive, so it may abstract away biological details such as neuromodulation, plasticity rules, multisensory development, and anatomical constraints.

Because this note is abstract-only, details still need checking: locomotor dataset, RNN architecture, sensory encoding, spatial-cell metrics, hippocampal recording analysis, and causal tests of movement statistics.

## Deep Themes

- Embodied development: representational structure emerges from changing action statistics.
- Sensorimotor prediction as cognitive-map formation: predicting visual futures from vestibular cues can induce spatial coding.
- Developmental curriculum: the order and distribution of experience matters, not just total sensory change.
- Neuroscience-model feedback: RNNs generate testable predictions for biological recordings.

## Subthemes

- Hippocampal spatial tuning.
- Rat locomotor development.
- Visual-vestibular recurrent prediction.
- Allocentric representation emergence.

## Connections to Other Papers

This connects to PRISM, BioX-Bridge, and Mind-Omni through neuroscience-inspired multimodal representation learning.

It also relates to GLANCE, VectorWorld, and L2T because all treat world modeling as grounded in embodied interaction rather than passive prediction alone.

## Notes for Cross-Paper Synthesis

This paper adds a developmental embodiment theme: the statistics of movement can determine what internal maps a learner discovers.
