# Equilibrium Pricing in Oligopolistic Data Markets

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: TAqejOfEAJ
- Authors: Bhaskar Ray Chaudhury; Jugal Garg; Eklavya Sharma; Jiaxin Song
- Primary area: theory->game_theory
- Keywords: data markets;equilibrium
- Source URL: https://openreview.net/forum?id=TAqejOfEAJ
- PDF URL: https://openreview.net/pdf?id=TAqejOfEAJ

## Abstract

We study equilibrium pricing in oligopolistic data markets with budget-constrained buyers (e.g., ML companies purchasing data to improve model accuracy) and strategic data sellers. Sellers compete by setting prices for their datasets, giving rise to a pricing game whose pure Nash equilibria correspond to equilibrium prices. While equilibrium prices are guaranteed for rivalrous goods via competitive equilibrium, we show that the non-rivalry of data fundamentally alters this picture: an exact Nash equilibrium need not exist, and in fact no 1.364-approximate equilibrium exists under uniform pricing. We therefore investigate relaxed equilibrium notions. Allowing sellers to use beyond-uniform pricing—specifically, piecewise-linear convex pricing functions—guarantees approximate stability within a constant factor: there exists a pricing profile in which no seller can improve revenue by a factor of two by deviating to any uniform price (a 2-approximate Nash equilibrium). Finally, our simulations demonstrate fast convergence and empirical approximation guarantees that outperform the worst-case bound of 2.

## One-Sentence Claim

Data non-rivalry breaks classical equilibrium-pricing guarantees, but richer seller pricing functions can recover constant-factor approximate stability in oligopolistic data markets.

## Problem

Data marketplaces are not ordinary goods markets: one buyer's use of a dataset does not consume it, sellers can sell to many buyers, and ML buyers often face budget constraints while valuing data through downstream performance gains. The paper asks whether strategic sellers can settle into stable prices when they compete to sell datasets to budget-constrained buyers.

The central difficulty is that competitive-equilibrium intuitions for rivalrous goods do not transfer cleanly. In data markets, a seller's revenue response to price changes can be discontinuous or non-convex because the same dataset can be bought by multiple buyers, combined with other datasets, and valued under budget constraints.

## Core Contribution

The paper gives a negative-to-positive equilibrium story:

- Under uniform pricing, exact pure Nash equilibria may not exist.
- More strongly, the paper shows no 1.364-approximate equilibrium exists under uniform pricing in the studied setting.
- If sellers can use beyond-uniform pricing, specifically piecewise-linear convex pricing functions, the market admits a 2-approximate Nash equilibrium against unilateral deviations to uniform prices.
- Simulations suggest convergence and approximation quality can be better than the worst-case factor.

## Method

The method is primarily game-theoretic. The authors model sellers as strategic price setters and buyers as budget-constrained data purchasers. Seller utilities are revenues, and stability is measured by whether any seller can improve revenue by deviating.

The constructive side replaces one-price-per-dataset uniform pricing with richer convex price schedules. This increases the expressive power of market mechanisms enough to smooth the strategic landscape and obtain approximate stability.

## Experiments and Evidence

Evidence comes from theoretical impossibility and existence results, plus simulation:

- Non-existence of exact Nash equilibria under uniform pricing.
- Lower bound ruling out 1.364-approximate equilibrium under uniform pricing.
- Existence of a 2-approximate Nash equilibrium with piecewise-linear convex pricing profiles.
- Simulations showing fast convergence and empirical approximation factors below the 2 worst-case guarantee.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: formal valuation model, budget assumptions, exact approximation definition, simulation scale, and whether deviations are restricted only to uniform prices.

## Limits and Failure Modes

- The positive guarantee is approximate, not exact.
- The abstract says the constructed profile blocks improvements by a factor of two against deviations to uniform prices; stronger deviation classes may require different analysis.
- Practical data markets may include exclusivity, privacy limits, data quality uncertainty, licensing terms, and strategic buyers, none of which are visible from the abstract.
- The results may depend sharply on the assumed buyer valuation and budget model.

## Deep Themes

**Non-rival goods require new market primitives.** Data's reusable nature changes the equilibrium landscape enough that standard pricing concepts can fail.

**Mechanism expressivity stabilizes strategic systems.** Uniform prices are too rigid; piecewise-linear convex pricing functions act like a richer control surface that restores approximate stability.

**ML data economics is becoming formal infrastructure.** Data is treated not just as a training ingredient but as an allocable, priceable resource with strategic supply-side behavior.

## Subthemes

- Approximate equilibrium as the realistic stability target.
- Seller-side strategic behavior in ML data supply.
- Budget constraints as a central source of market coupling.
- Pricing-function design as a computational mechanism, not just an economic detail.

## Connections to Other Papers

Connects to data governance and curation papers such as MTS Difficulty, HOBIT, Sequential Data Values, and FAC Synthesis, but from a market-design angle rather than an optimization-pipeline angle. It also links to theory papers on equilibrium learning and bounded-rational solution concepts, including RQE Actor-Critic, where exact classical equilibria are replaced by more tractable relaxed targets.

## Notes for Cross-Paper Synthesis

This paper adds a data-market layer to the broader 2026 theme that "data quality" is no longer just a static dataset property. Across the corpus, data is selected, valued, bought, reweighted, audited, distilled, and governed through mechanisms that must themselves be stable.
