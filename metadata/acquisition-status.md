# Acquisition Status

Last updated: 2026-07-20.

## Metadata

- ICLR 2026 public metadata records: 19,814.
- ICLR 2026 accepted-publication records: 5,343.
- ICML 2026 public metadata records: 6,341.
- ICML 2026 accepted-publication records: 6,341.

Primary metadata source currently used: Paper Copilot public GitHub data.

Preferred official source: OpenReview and, for final ICML proceedings, PMLR when available.

## PDF Acquisition

OpenReview PDF and API endpoints have returned challenge/403 responses from this environment, so the project uses `scripts/fetch_arxiv_pdfs.py` as a conservative fallback for high-confidence title matches.

Downloaded PDFs:

- ICLR 2026: 15 arXiv PDFs.
- ICML 2026: 48 arXiv PDFs.

Extracted text files:

- ICLR 2026: 15.
- ICML 2026: 48.

## Known Constraints

- ArXiv API returned HTTP 429 for every ICML spotlight paper in the 46-50 batch, so those five notes are currently abstract/metadata-only and should be retried later from offset 45.
- ArXiv API returned HTTP 429 during the first ICML spotlight probe after two successful downloads. A later slower resume downloaded six additional PDFs before being manually interrupted during the post-download sleep.
- No confident arXiv match was found for `Catch-22: On the Fundamental Tradeoff Between Detectability and Robustness in LLM Watermarking` in the first spotlight batch.
- No confident arXiv match was found for `Spherical Watermark: Encryption-Free, Lossless Watermarking for Diffusion Models` in ICLR oral papers 9-13.
- No confident arXiv match was found for `HATSolver: Learning Groebner Bases with Hierarchical Attention Transformers` in ICLR oral papers 14-18.
- ArXiv acquisition was deferred for ICLR oral papers 19-23 after repeated OpenReview access limits and arXiv fallback constraints, so these five notes are currently abstract/metadata-only and should be retried later from offset 18.
- ArXiv acquisition was deferred for ICLR oral papers 24-25 after repeated OpenReview access limits and arXiv fallback constraints, so these two notes are currently abstract/metadata-only and should be retried later from offset 23.
- ArXiv acquisition was deferred for ICLR oral papers 26-30 after repeated OpenReview access limits and arXiv fallback constraints, so these five notes are currently abstract/metadata-only and should be retried later from offset 25.
- ArXiv acquisition was deferred for ICLR oral papers 31-35 after repeated OpenReview access limits and arXiv fallback constraints, so these five notes are currently abstract/metadata-only and should be retried later from offset 30.
- ArXiv acquisition was deferred for ICLR oral papers 36-40 after repeated OpenReview access limits and arXiv fallback constraints, so these five notes are currently abstract/metadata-only and should be retried later from offset 35.
- ArXiv acquisition was deferred for ICLR oral papers 41-45 after repeated OpenReview access limits and arXiv fallback constraints, so these five notes are currently abstract/metadata-only and should be retried later from offset 40.
- ArXiv acquisition was deferred for ICLR oral papers 46-50 after repeated OpenReview access limits and arXiv fallback constraints, so these five notes are currently abstract/metadata-only and should be retried later from offset 45.
- ArXiv acquisition was deferred for ICLR oral papers 51-55 after repeated OpenReview access limits and arXiv fallback constraints, so these five notes are currently abstract/metadata-only and should be retried later from offset 50.
- ArXiv acquisition was deferred for ICLR oral papers 56-60 after repeated OpenReview access limits and arXiv fallback constraints, so these five notes are currently abstract/metadata-only and should be retried later from offset 55.
- ArXiv acquisition was deferred for ICLR oral papers 61-65 after repeated OpenReview access limits and arXiv fallback constraints, so these five notes are currently abstract/metadata-only and should be retried later from offset 60.
- ArXiv acquisition was deferred for ICLR oral papers 66-70 after repeated OpenReview access limits and arXiv fallback constraints, so these five notes are currently abstract/metadata-only and should be retried later from offset 65.
- ArXiv acquisition was deferred for ICLR oral papers 71-75 after repeated OpenReview access limits and arXiv fallback constraints, so these five notes are currently abstract/metadata-only and should be retried later from offset 70.
- ArXiv acquisition was deferred for ICLR oral papers 76-80 after repeated OpenReview access limits and arXiv fallback constraints, so these five notes are currently abstract/metadata-only and should be retried later from offset 75.
- ArXiv acquisition was deferred for ICLR oral papers 81-85 after repeated OpenReview access limits and arXiv fallback constraints, so these five notes are currently abstract/metadata-only and should be retried later from offset 80.
- ArXiv acquisition was deferred for ICLR oral papers 86-90 after repeated OpenReview access limits and arXiv fallback constraints, so these five notes are currently abstract/metadata-only and should be retried later from offset 85.
- ArXiv acquisition was deferred for ICLR oral papers 91-95 after repeated OpenReview access limits and arXiv fallback constraints, so these five notes are currently abstract/metadata-only and should be retried later from offset 90.
- ArXiv acquisition was deferred for ICLR oral papers 96-100 after repeated OpenReview access limits and arXiv fallback constraints, so these five notes are currently abstract/metadata-only and should be retried later from offset 95.
- ArXiv acquisition was deferred for ICLR oral papers 101-105 after repeated OpenReview access limits and arXiv fallback constraints, so these five notes are currently abstract/metadata-only and should be retried later from offset 100.
- ArXiv acquisition was deferred for ICLR oral papers 106-110 after repeated OpenReview access limits and arXiv fallback constraints, so these five notes are currently abstract/metadata-only and should be retried later from offset 105.
- ArXiv acquisition was deferred for ICLR oral papers 111-115 after repeated OpenReview access limits and arXiv fallback constraints, so these five notes are currently abstract/metadata-only and should be retried later from offset 110.
- ArXiv acquisition was deferred for ICLR oral papers 116-120 after repeated OpenReview access limits and arXiv fallback constraints, so these five notes are currently abstract/metadata-only and should be retried later from offset 115.
- ArXiv acquisition was deferred for ICLR oral papers 121-125 after repeated OpenReview access limits and arXiv fallback constraints, so these five notes are currently abstract/metadata-only and should be retried later from offset 120.
- ArXiv acquisition was deferred for ICLR oral papers 126-130 after repeated OpenReview access limits and arXiv fallback constraints, so these five notes are currently abstract/metadata-only and should be retried later from offset 125.
- ArXiv acquisition was deferred for ICLR oral papers 131-135 after repeated OpenReview access limits and arXiv fallback constraints, so these five notes are currently abstract/metadata-only and should be retried later from offset 130.
- ArXiv acquisition was deferred for ICLR oral papers 136-140 after repeated OpenReview access limits and arXiv fallback constraints, so these five notes are currently abstract/metadata-only and should be retried later from offset 135.
- ArXiv acquisition was deferred for ICLR oral papers 141-145 after repeated OpenReview access limits and arXiv fallback constraints, so these five notes are currently abstract/metadata-only and should be retried later from offset 140.
- ArXiv acquisition was deferred for ICLR oral papers 146-150 after repeated OpenReview access limits and arXiv fallback constraints, so these five notes are currently abstract/metadata-only and should be retried later from offset 145.
- ArXiv acquisition was deferred for ICLR oral papers 151-155 after repeated OpenReview access limits and arXiv fallback constraints, so these five notes are currently abstract/metadata-only and should be retried later from offset 150.
- ArXiv acquisition was deferred for ICLR oral papers 156-160 after repeated OpenReview access limits and arXiv fallback constraints, so these five notes are currently abstract/metadata-only and should be retried later from offset 155.
- ArXiv acquisition was deferred for ICLR oral papers 161-165 after repeated OpenReview access limits and arXiv fallback constraints, so these five notes are currently abstract/metadata-only and should be retried later from offset 160.
- ArXiv acquisition was deferred for ICLR oral papers 166-170 after repeated OpenReview access limits and arXiv fallback constraints, so these five notes are currently abstract/metadata-only and should be retried later from offset 165.
- ArXiv acquisition was deferred for ICLR oral papers 171-175 after repeated OpenReview access limits and arXiv fallback constraints, so these five notes are currently abstract/metadata-only and should be retried later from offset 170.
- ArXiv acquisition was deferred for ICLR oral papers 176-180 after repeated OpenReview access limits and arXiv fallback constraints, so these five notes are currently abstract/metadata-only and should be retried later from offset 175.
- ArXiv acquisition was deferred for ICLR oral papers 181-185 after repeated OpenReview access limits and arXiv fallback constraints, so these five notes are currently abstract/metadata-only and should be retried later from offset 180.
- ArXiv acquisition was deferred for ICLR oral papers 186-190 after repeated OpenReview access limits and arXiv fallback constraints, so these five notes are currently abstract/metadata-only and should be retried later from offset 185.
- ArXiv acquisition was deferred for ICLR oral papers 191-195 after repeated OpenReview access limits and arXiv fallback constraints, so these five notes are currently abstract/metadata-only and should be retried later from offset 190.
- ArXiv acquisition was deferred for ICLR oral papers 196-200 after repeated OpenReview access limits and arXiv fallback constraints, so these five notes are currently abstract/metadata-only and should be retried later from offset 195.
- ArXiv acquisition was deferred for ICLR oral papers 201-205 after repeated OpenReview access limits and arXiv fallback constraints, so these five notes are currently abstract/metadata-only and should be retried later from offset 200.
- ArXiv acquisition was deferred for ICLR oral papers 206-210 after repeated OpenReview access limits and arXiv fallback constraints, so these five notes are currently abstract/metadata-only and should be retried later from offset 205.
- ArXiv acquisition was deferred for ICLR oral papers 211-215 after repeated OpenReview access limits and arXiv fallback constraints, so these five notes are currently abstract/metadata-only and should be retried later from offset 210.
- ArXiv acquisition was deferred for ICLR oral papers 216-220 after repeated OpenReview access limits and arXiv fallback constraints, so these five notes are currently abstract/metadata-only and should be retried later from offset 215.
- ArXiv acquisition was deferred for ICLR oral papers 221-223 after repeated OpenReview access limits and arXiv fallback constraints, so these three notes are currently abstract/metadata-only and should be retried later from offset 220.
- The first 25 ICLR poster note stubs were created with `poster-` filename prefixes to avoid visual collision with existing oral note numbering.
- ArXiv acquisition was deferred for ICLR poster papers 1-5 after repeated OpenReview access limits and arXiv fallback constraints, so these five notes are currently abstract/metadata-only and should be retried later from poster offset 0.
- ArXiv acquisition was deferred for ICLR poster papers 6-10 after repeated OpenReview access limits and arXiv fallback constraints, so these five notes are currently abstract/metadata-only and should be retried later from poster offset 5.
- ArXiv acquisition was deferred for ICLR poster papers 11-15 after repeated OpenReview access limits and arXiv fallback constraints, so these five notes are currently abstract/metadata-only and should be retried later from poster offset 10.
- ArXiv acquisition was deferred for ICLR poster papers 16-20 after repeated OpenReview access limits and arXiv fallback constraints, so these five notes are currently abstract/metadata-only and should be retried later from poster offset 15.
- No confident arXiv match was found for `Transformer Circuits Can Realize Clustering Algorithms` in ICML spotlight papers 16-20.
- No confident arXiv match was found for `Robust Contextual Optimization with Missing Covariates` in ICML spotlight papers 21-25.
- No confident arXiv match was found for `Language Generation in the Limit: Complexity Barriers and Implications for Learning` in ICML spotlight papers 21-25.
- No confident arXiv match was found for `FOCUS & RePAIR: Mitigating Text Degeneration via Token-Level Guidance For Pruned Large Language Models` in ICML spotlight papers 26-30.
- No confident arXiv match was found for `SlaClip: Gradient Norm Slacks can be Indicator for Adaptive Clipping in DP-SGD` in ICML spotlight papers 31-35.
- No confident arXiv match was found for `Error Propagation Mechanisms and Compensation Strategies for Quantized Diffusion Models` in ICML spotlight papers 36-40.
- No confident arXiv match was found for `What Preferences Can—and Cannot—Predict in Multi-Agent Online Learning` in ICML spotlight papers 41-45.
- No confident arXiv match was found for `Ranking Time Series using a Time Warping Ideal Point Model` in ICML spotlight papers 41-45.
- No confident arXiv match was found for `On the Identifiability of Poisson Branching Structural Causal Model Under Latent Confounding` in ICML spotlight papers 51-55.
- No confident arXiv match was found for `Conditional Equivalence of DPO and RLHF: Assumptions, Failure Modes, and Provable Alignment` in ICML spotlight papers 56-60.
- No confident arXiv match was found for `EcoVLA: Environment-Aware Adaptive Pruning with Interleaved Inference Orchestration for Vision-Language-Action Models` in ICML spotlight papers 61-65.
- No confident arXiv match was found for `SVD as a Fast Interpretability Method for Transformers` in ICML spotlight papers 61-65.
- No confident arXiv match was found for `Copyright-Bench: Agentic Evaluation of Copyright Law Compliance` in ICML spotlight papers 61-65.
- No confident arXiv match was found for `Towards Hierarchy–Uniformity Equilibrium: Recovering Semantic Depth in Hypergraph Contrastive Learning` in ICML spotlight papers 66-70.
- No confident arXiv match was found for `On Minimum Depth and Width of Floating-Point Neural Networks for Representing Floating-Point Functions` in ICML spotlight papers 66-70.
- ArXiv API returned HTTP 429/503 errors for every ICML spotlight paper in the 71-75 batch, so those five notes are currently abstract/metadata-only and should be retried later from offset 70.
- ArXiv API returned HTTP 429/503 errors for every ICML spotlight paper in the 76-80 batch, so those five notes are currently abstract/metadata-only and should be retried later from offset 75.
- ArXiv API returned HTTP 429 errors for every ICML spotlight paper in the 81-85 batch, so those five notes are currently abstract/metadata-only and should be retried later from offset 80.
- ArXiv acquisition was deferred for ICML spotlight papers 86-90 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 85.
- ArXiv acquisition was deferred for ICML spotlight papers 91-95 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 90.
- ArXiv acquisition was deferred for ICML spotlight papers 96-100 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 95.
- ArXiv acquisition was deferred for ICML spotlight papers 101-105 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 100.
- ArXiv acquisition was deferred for ICML spotlight papers 106-110 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 105.
- ArXiv acquisition was deferred for ICML spotlight papers 111-115 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 110.
- ArXiv acquisition was deferred for ICML spotlight papers 116-120 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 115.
- ArXiv acquisition was deferred for ICML spotlight papers 121-125 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 120.
- ArXiv acquisition was deferred for ICML spotlight papers 126-130 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 125.
- ArXiv acquisition was deferred for ICML spotlight papers 131-135 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 130.
- ArXiv acquisition was deferred for ICML spotlight papers 136-140 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 135.
- ArXiv acquisition was deferred for ICML spotlight papers 141-145 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 140.
- ArXiv acquisition was deferred for ICML spotlight papers 146-150 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 145.
- ArXiv acquisition was deferred for ICML spotlight papers 151-155 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 150.
- ArXiv acquisition was deferred for ICML spotlight papers 156-160 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 155.
- ArXiv acquisition was deferred for ICML spotlight papers 161-165 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 160.
- ArXiv acquisition was deferred for ICML spotlight papers 166-170 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 165.
- ArXiv acquisition was deferred for ICML spotlight papers 171-175 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 170.
- ArXiv acquisition was deferred for ICML spotlight papers 176-180 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 175.
- ArXiv acquisition was deferred for ICML spotlight papers 181-185 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 180.
- ArXiv acquisition was deferred for ICML spotlight papers 186-190 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 185.
- ArXiv acquisition was deferred for ICML spotlight papers 191-195 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 190.
- ArXiv acquisition was deferred for ICML spotlight papers 196-200 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 195.
- ArXiv acquisition was deferred for ICML spotlight papers 201-205 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 200.
- ArXiv acquisition was deferred for ICML spotlight papers 206-210 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 205.
- ArXiv acquisition was deferred for ICML spotlight papers 211-215 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 210.
- ArXiv acquisition was deferred for ICML spotlight papers 216-220 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 215.
- ArXiv acquisition was deferred for ICML spotlight papers 221-225 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 220.
- ArXiv acquisition was deferred for ICML spotlight papers 226-230 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 225.
- ArXiv acquisition was deferred for ICML spotlight papers 231-235 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 230.
- ArXiv acquisition was deferred for ICML spotlight papers 236-240 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 235.
- ArXiv acquisition was deferred for ICML spotlight papers 241-245 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 240.
- ArXiv acquisition was deferred for ICML spotlight papers 246-250 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 245.
- ArXiv acquisition was deferred for ICML spotlight papers 251-255 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 250.
- ArXiv acquisition was deferred for ICML spotlight papers 256-260 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 255.
- ArXiv acquisition was deferred for ICML spotlight papers 261-265 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 260.
- ArXiv acquisition was deferred for ICML spotlight papers 266-270 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 265.
- ArXiv acquisition was deferred for ICML spotlight papers 271-275 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 270.
- ArXiv acquisition was deferred for ICML spotlight papers 276-280 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 275.
- ArXiv acquisition was deferred for ICML spotlight papers 281-285 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 280.
- ArXiv acquisition was deferred for ICML spotlight papers 286-290 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 285.
- ArXiv acquisition was deferred for ICML spotlight papers 291-295 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 290.
- ArXiv acquisition was deferred for ICML spotlight papers 296-300 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 295.
- ArXiv acquisition was deferred for ICML spotlight papers 301-305 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 300.
- ArXiv acquisition was deferred for ICML spotlight papers 306-310 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 305.
- ArXiv acquisition was deferred for ICML spotlight papers 311-315 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 310.
- ArXiv acquisition was deferred for ICML spotlight papers 316-320 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 315.
- ArXiv acquisition was deferred for ICML spotlight papers 321-325 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 320.
- ArXiv acquisition was deferred for ICML spotlight papers 326-330 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 325.
- ArXiv acquisition was deferred for ICML spotlight papers 331-335 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 330.
- ArXiv acquisition was deferred for ICML spotlight papers 336-340 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 335.
- ArXiv acquisition was deferred for ICML spotlight papers 341-345 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 340.
- ArXiv acquisition was deferred for ICML spotlight papers 346-350 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 345.
- ArXiv acquisition was deferred for ICML spotlight papers 351-355 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 350.
- ArXiv acquisition was deferred for ICML spotlight papers 356-360 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 355.
- ArXiv acquisition was deferred for ICML spotlight papers 361-365 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 360.
- ArXiv acquisition was deferred for ICML spotlight papers 366-370 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 365.
- ArXiv acquisition was deferred for ICML spotlight papers 371-375 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 370.
- ArXiv acquisition was deferred for ICML spotlight papers 376-380 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 375.
- ArXiv acquisition was deferred for ICML spotlight papers 381-385 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 380.
- ArXiv acquisition was deferred for ICML spotlight papers 386-390 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 385.
- ArXiv acquisition was deferred for ICML spotlight papers 391-395 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 390.
- ArXiv acquisition was deferred for ICML spotlight papers 396-400 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 395.
- ArXiv acquisition was deferred for ICML spotlight papers 401-405 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 400.
- ArXiv acquisition was deferred for ICML spotlight papers 406-410 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 405.
- ArXiv acquisition was deferred for ICML spotlight papers 411-415 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 410.
- ArXiv acquisition was deferred for ICML spotlight papers 416-420 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 415.
- ArXiv acquisition was deferred for ICML spotlight papers 421-425 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 420.
- ArXiv acquisition was deferred for ICML spotlight papers 426-430 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 425.
- ArXiv acquisition was deferred for ICML spotlight papers 431-435 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 430.
- ArXiv acquisition was deferred for ICML spotlight papers 436-440 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 435.
- ArXiv acquisition was deferred for ICML spotlight papers 441-445 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 440.
- ArXiv acquisition was deferred for ICML spotlight papers 446-450 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 445.
- ArXiv acquisition was deferred for ICML spotlight papers 451-455 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 450.
- ArXiv acquisition was deferred for ICML spotlight papers 456-460 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 455.
- ArXiv acquisition was deferred for ICML spotlight papers 461-465 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 460.
- ArXiv acquisition was deferred for ICML spotlight papers 466-470 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 465.
- ArXiv acquisition was deferred for ICML spotlight papers 471-475 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 470.
- ArXiv acquisition was deferred for ICML spotlight papers 476-480 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 475.
- ArXiv acquisition was deferred for ICML spotlight papers 481-485 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 480.
- ArXiv acquisition was deferred for ICML spotlight papers 486-490 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 485.
- ArXiv acquisition was deferred for ICML spotlight papers 491-495 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 490.
- ArXiv acquisition was deferred for ICML spotlight papers 496-500 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 495.
- ArXiv acquisition was deferred for ICML spotlight papers 501-505 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 500.
- ArXiv acquisition was deferred for ICML spotlight papers 506-510 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 505.
- ArXiv acquisition was deferred for ICML spotlight papers 511-515 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 510.
- ArXiv acquisition was deferred for ICML spotlight papers 516-520 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 515.
- ArXiv acquisition was deferred for ICML spotlight papers 521-525 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 520.
- ArXiv acquisition was deferred for ICML spotlight papers 526-530 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 525.
- ArXiv acquisition was deferred for ICML spotlight papers 531-535 after repeated 429/503 failures across preceding exact-batch attempts, so those five notes are currently abstract/metadata-only and should be retried later from offset 530.
- ArXiv acquisition was deferred for ICML spotlight paper 536 after repeated 429/503 failures across preceding exact-batch attempts, so this note is currently abstract/metadata-only and should be retried later from offset 535.
- ArXiv PDFs are not official conference PDFs; each downloaded file has a `.arxiv.json` sidecar recording the matched arXiv entry and conference metadata.
- Full-paper note upgrades should cite whether they used arXiv-extracted text or only conference metadata/abstracts.

## Resumable Commands

```bash
python3 scripts/fetch_openreview.py --conference iclr-2026
python3 scripts/fetch_openreview.py --conference icml-2026
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Oral --offset 18 --limit 25 --sleep 8
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Oral --offset 18 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Oral --offset 23 --limit 2 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Oral --offset 25 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Oral --offset 30 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Oral --offset 35 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Oral --offset 40 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Oral --offset 45 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Oral --offset 50 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Oral --offset 55 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Oral --offset 60 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Oral --offset 65 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Oral --offset 70 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Oral --offset 75 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Oral --offset 80 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Oral --offset 85 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Oral --offset 90 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Oral --offset 95 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Oral --offset 100 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Oral --offset 105 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Oral --offset 110 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Oral --offset 115 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Oral --offset 120 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Oral --offset 125 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Oral --offset 130 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Oral --offset 135 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Oral --offset 140 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Oral --offset 145 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Oral --offset 150 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Oral --offset 155 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Oral --offset 160 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Oral --offset 165 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Oral --offset 170 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Oral --offset 175 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Oral --offset 180 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Oral --offset 185 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Oral --offset 190 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Oral --offset 195 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Oral --offset 200 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Oral --offset 205 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Oral --offset 210 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Oral --offset 215 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Oral --offset 220 --limit 3 --sleep 20
python3 scripts/create_note_stubs.py --conference iclr-2026 --status Oral --offset 223 --limit 25
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 45 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 70 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 75 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 80 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 85 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 90 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 95 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 100 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 105 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 110 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 115 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 120 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 125 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 130 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 135 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 140 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 145 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 150 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 155 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 160 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 165 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 170 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 175 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 180 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 185 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 190 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 195 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 200 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 205 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 210 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 215 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 220 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 225 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 230 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 235 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 240 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 245 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 250 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 255 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 260 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 265 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 270 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 275 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 280 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 285 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 290 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 295 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 300 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 305 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 310 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 315 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 320 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 325 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 330 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 335 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 340 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 345 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 350 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 355 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 360 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 365 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 370 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 375 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 380 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 385 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 390 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 395 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 400 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 405 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 410 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 415 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 420 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 425 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 430 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 435 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 440 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 445 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 450 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 455 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 460 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 465 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 470 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 475 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 480 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 485 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 490 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 495 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 500 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 505 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 510 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 515 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 520 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 525 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 530 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference icml-2026 --status Spotlight --offset 535 --limit 1 --sleep 20
python3 scripts/create_note_stubs.py --conference icml-2026 --status Spotlight --offset 536 --limit 25
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Poster --offset 0 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Poster --offset 5 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Poster --offset 10 --limit 5 --sleep 20
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Poster --offset 15 --limit 5 --sleep 20
python3 scripts/create_note_stubs.py --conference iclr-2026 --status Poster --offset 25 --limit 25 --filename-prefix poster-
.venv/bin/python scripts/extract_pdf_text.py --conference iclr-2026
.venv/bin/python scripts/extract_pdf_text.py --conference icml-2026
python3 scripts/progress_report.py
```
