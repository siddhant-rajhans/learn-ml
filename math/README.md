# Math — Foundations

> *"The language everything else is written in. Skipping this is like trying to read without knowing the alphabet — you can fake it for a while, then it catches up to you."*

**Total time:** ~14–21 weeks (3–5 months at 10 hrs/week)
**Visual companion:** [The Map → Foundations](https://siddhant-rajhans.github.io/ml-roadmap/roadmap.html)

## What this unlocks

Backprop becomes the chain rule. Embeddings become vectors in space. Loss functions stop being magic and become information-theoretic objects. Every architecture in this curriculum derives its existence from these five topics.

## Topics

### Linear Algebra · 3–4 weeks
*Understand how embeddings work, why PCA reduces dimensions, what a neural network weight matrix actually does to data.*

- Vectors & vector spaces
- Basis, span, linear independence
- Matrix operations & inverses
- Rank, null space, column space
- Determinants
- Eigendecomposition
- Singular Value Decomposition (SVD)
- Tensors — intro
- PCA as eigendecomposition

> Interactive: [Linear Algebra — 3D Transformation Engine](https://siddhant-rajhans.github.io/ml-roadmap/linear-algebra.html)
> Episode: [What a Vector Actually Is](https://siddhant-rajhans.github.io/ml-roadmap/vector.html)

### Calculus & Analysis · 3–4 weeks
*Derive backpropagation from scratch. Understand why gradient descent works. Read any ML paper with confidence.*

- Functions, limits, continuity
- Derivatives & chain rule
- Partial derivatives
- Gradients & directional derivatives
- Jacobian & Hessian matrices
- Taylor series
- Multivariable integration
- Automatic differentiation — theory

### Probability & Bayesian Thinking · 4–6 weeks
*The Bayesian lens changes how you see everything.*

- Probability axioms & rules
- Random variables & distributions
- Bayes' theorem — deeply
- MLE, MAP & posterior
- Exponential family distributions
- Central limit theorem
- Markov chains
- MCMC & variational inference (intro)
- Concentration inequalities

### Information Theory · 2 weeks
*Understand why cross-entropy is the right loss. What KL divergence measures. How VAEs and diffusion models minimize information-theoretic quantities.*

- Entropy & self-information
- KL divergence
- Mutual information
- Cross-entropy & log-loss
- Channel capacity
- Bits vs nats
- Rate-distortion theory
- MDL principle

### Optimization Theory · 2–3 weeks
*Why Adam beats SGD in some settings. How to derive learning rate schedules. Why non-convex loss landscapes are still tractable.*

- Convex vs non-convex landscapes
- Gradient descent — convergence theory
- SGD, Momentum, AdaGrad, RMSprop, Adam
- Second-order methods (Newton, L-BFGS)
- Learning rate schedules
- Constrained optimization
- Lagrange multipliers & KKT conditions
- Variational methods

## Recommended external resources

- 3Blue1Brown — *Essence of Linear Algebra*, *Essence of Calculus*
- Strang — *Introduction to Linear Algebra* (MIT OCW 18.06)
- Mathematics for Machine Learning — Deisenroth, Faisal, Ong
- Boyd & Vandenberghe — *Convex Optimization*

## Where to go next

If math is mostly solid, parallel-track **[prog/](../prog/)** (you'll write code that uses these ideas) and **[classical/](../classical/)** (the simplest place to see them in action). If you came here straight from Phase 0, do math fully before classical.
