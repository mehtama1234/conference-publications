# On The Surprising Effectiveness of a Single Global Merging in Decentralized Learning

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: zrFnwRHuQo
- Authors: Tongtian Zhu; Tianyu Zhang; Mingze Wang; Zhanpeng Zhou; Can Wang
- Primary area: optimization
- Keywords: Decentralized Learning;Model Merging
- Source URL: https://openreview.net/forum?id=zrFnwRHuQo
- PDF URL: https://openreview.net/pdf?id=zrFnwRHuQo

## Abstract

Decentralized learning provides a scalable alternative to parameter-server-based training, yet its performance is often hindered by limited peer-to-peer communication. 
In this paper, we study how communication should be scheduled over time to improve global generalization, including determining when and how frequently devices synchronize. 
Counterintuitive empirical results show that concentrating communication budgets in the later stages of decentralized training remarkably improves global generalization.
Surprisingly, we uncover that fully connected communication at the final step, implemented by a single global merging, can significant improve the generalization performance of decentralized learning under serve high data heterogeneity. 
Our theoretical contributions, which explains these phenomena, are first to establish that the globally merged model of decentralized SGD can match the convergence rate of parallel SGD.
Technically, we reinterpret part of the discrepancy among local models, which were previously considered as detrimental noise, as constructive components essential for matching this rate. 
This work provides promising results that  decentralized learning is able to generalize under high data heterogeneity and limited communication, while offering broad new avenues for model merging research. 
The code will be made publicly available.

## One-Sentence Claim

A single fully connected global merge at the end of decentralized training can substantially improve generalization under high data heterogeneity and match parallel-SGD convergence rates.

## Problem

Decentralized learning reduces dependence on a parameter server, but limited peer-to-peer communication can hurt global generalization, especially when local data distributions are highly heterogeneous. It is unclear when communication should occur and how much synchronization is needed.

## Core Contribution

The paper shows empirically and theoretically that concentrating communication late, even as a single final global merge, can improve decentralized learning. It proves that the globally merged model of decentralized SGD can match the convergence rate of parallel SGD and reinterprets some local-model discrepancy as constructive rather than purely harmful.

## Method

The study varies communication schedules over decentralized training, focusing on when devices synchronize and whether communication budgets should be spread across training or concentrated near the end. The theoretical analysis studies decentralized SGD with a final global model merge and decomposes local-model discrepancies to explain convergence behavior.

## Experiments and Evidence

The abstract reports counterintuitive empirical gains from concentrating communication in later stages and especially from a final fully connected global merge under severe data heterogeneity. Theoretical results explain how this merged model can match parallel-SGD convergence rates.

## Limits and Failure Modes

This note is abstract/metadata-only. Full-text review should inspect assumptions about network topology, data heterogeneity, optimizer, model class, local training length, and communication budget. A single final merge may fail if local models diverge into incompatible basins or if personalization is more important than global generalization.

## Deep Themes

- Communication scheduling in decentralized learning.
- Model merging as late-stage synchronization.
- Constructive local diversity.
- Generalization under data heterogeneity.

## Subthemes

- Decentralized SGD.
- Parallel-SGD convergence.
- Final global merging.
- Peer-to-peer communication limits.
- Heterogeneous local data.

## Connections to Other Papers

Connects to Polar Express through optimization primitives that change training efficiency, to federated/private data themes through distributed constraints, and to broader model-merging work where independently trained weights can combine into a better global model.

## Notes for Cross-Paper Synthesis

This paper adds a distributed-learning version of the corpus's resource-allocation theme: communication does not need to be frequent to be useful if scheduled at the right phase. Local disagreement can be an asset before it is merged.
