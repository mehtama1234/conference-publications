# Understanding VLMs Spatial Mental Modeling Capability from Limited Views

## Metadata

- Conference: iclr-2026
- Status: Poster
- OpenReview ID: 0FhrtdKLtD
- Authors: Qineng Wang; Baiqiao Yin; Pingyue Zhang; Jianshu Zhang; Kangrui Wang; Zihan Wang; Jieyu Zhang; Keshigeyan Chandrasegaran; Han Liu; Ranjay Krishna; Saining Xie; Jiajun Wu; Li Fei-Fei; Manling Li
- Primary area: foundation or frontier models, including LLMs
- Keywords: Vision Language Models;VLMs;Multi Modal Language Models;Spatial Intelligence;Spatial Reasoning
- Source URL: https://openreview.net/forum?id=0FhrtdKLtD
- PDF URL: https://openreview.net/pdf?id=0FhrtdKLtD

## Abstract

Can Vision Language Models (VLMs) imagine the full scene from just a few views, like humans do? Humans form spatial mental models, internal representations of unseen space, to reason about layout, perspective, and motion. Our new MindCube benchmark with 21,154 questions across 3,268 images exposes this critical gap, where existing VLMs exhibit near-random performance. Using MindCube, we systematically evaluate how well VLMs build robust spatial mental models through representing positions (cognitive mapping), orientations (perspective-taking), and dynamics (mental simulation for "what-if" movements). We then explore three approaches to help VLMs approximate spatial mental models, including unseen intermediate views, natural language reasoning chains, and cognitive maps. The significant improvement comes from a synergistic approach, "map-then-reason", that jointly trains the model to first generate a cognitive map and then reason upon it. By training models to reason over these internal maps, we boosted accuracy from 37.8% to 60.8% (+23.0%). Adding reinforcement learning pushed performance even further to 70.7% (+32.9%). Our key insight is that such scaffolding of spatial mental models, actively constructing and utilizing internal structured spatial representations with flexible reasoning processes, significantly improves understanding of unobservable space.

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
