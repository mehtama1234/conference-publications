# Rex: A Family of Reversible Exponential (Stochastic) Runge-Kutta Solvers

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 7pQIzVNctu
- Authors: Zander W. Blasingame; Chen Liu
- Primary area: applications->chemistry_physics_and_earth_sciences
- Keywords: numerical methods;neural differential equations;stochastic processes;stochastic differential equations;runge-kutta methods;diffusion models
- Source URL: https://openreview.net/forum?id=7pQIzVNctu
- PDF URL: https://openreview.net/pdf?id=7pQIzVNctu

## Abstract

Deep generative models based on neural differential equations have become state-of-the-art for many generation tasks.
These models rely on ODE/SDE solvers that integrate from a prior distribution to the data distribution; in many applications it is also highly desirable to integrate in the inverse direction.
Standard solvers, however, accumulate discretization errors that prohibit *exact inversion*, an inaccuracy that is unacceptable in precision-critical applications.
Existing inversion methods suffer from poor stability and low order of convergence, and are strictly limited to the ODE setting.
In this work, we propose *Rex*, a family of reversible exponential (stochastic) Runge-Kutta solvers obtained by applying Lawson methods to convert any explicit (stochastic) Runge-Kutta scheme into an algebraically reversible one for both diffusion ODEs *and* SDEs.
Beyond a rigorous theoretical analysis---establishing arbitrary-order convergence and a non-zero region of linear stability---we empirically demonstrate that *Rex* achieves near-machine-precision reconstruction and improves Boltzmann sampling with flow models as well as image generation and editing with diffusion models.

## One-Sentence Claim

Rex converts explicit ODE/SDE Runge-Kutta schemes into algebraically reversible exponential solvers, enabling near-exact inversion for diffusion models and related generative systems.

## Problem

Diffusion and neural differential equation models often need inverse integration, but standard solvers accumulate discretization error, while prior reversible methods can be unstable, low-order, or limited to ODEs.

## Core Contribution

The paper introduces Rex, a family of reversible exponential stochastic Runge-Kutta solvers for both diffusion ODEs and SDEs, with arbitrary-order convergence and nonzero linear-stability regions.

## Method

Rex applies Lawson/exponential-integrator transformations to a base explicit Runge-Kutta or stochastic Runge-Kutta scheme, builds a Princeps scheme, then constructs an algebraically reversible solver through a McCallum-Foster-style reversible method.

## Experiments and Evidence

The abstract reports near-machine-precision reconstruction and improvements for Boltzmann sampling with flow models, image generation, and image editing with diffusion models.

## Full-Text Upgrade

The full text emphasizes that Rex is not one solver but a recipe that can produce reversible versions of popular diffusion solvers, including DDIM and DPM-Solver-style schemes. It handles both probability-flow ODEs and reverse-time SDEs, making it broader than prior ODE-only exact-inversion work.

The theoretical results show that Rex inherits the order of the base explicit RK/SRK scheme and, through the McCallum-Foster construction, retains a nonzero linear-stability region. Empirically, Rex(Euler) achieves orders-of-magnitude lower inversion error on real images, supports exact-inversion editing workflows, and enables more accurate likelihood-based Boltzmann sampling.

## Limits and Failure Modes

Limits to watch: algebraic reversibility can still be affected by finite-precision arithmetic; solver benefits depend on diffusion schedule and base scheme; and higher-order/stochastic variants may add implementation complexity.

## Deep Themes

- Generative models increasingly depend on numerical-solver properties.
- Exact inversion is becoming important for editing, likelihoods, and scientific sampling.
- Classical numerical analysis can directly improve modern diffusion-model workflows.

## Subthemes

- Reversible solvers.
- Exponential Runge-Kutta.
- Diffusion ODEs and SDEs.
- Exact inversion.
- Image editing.
- Boltzmann sampling.

## Connections to Other Papers

Connects to IRNO, Frozen-PINN, physical dynamical solvers, and constrained diffusion papers through numerical-methods-as-ML-infrastructure. It also links to Autoregressive Boltzmann Generators through equilibrium sampling.

## Notes for Cross-Paper Synthesis

Rex strengthens the solver-infrastructure theme: as generative models become tools for editing and scientific inference, numerical reversibility and stability are first-class ML capabilities.
