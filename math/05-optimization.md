# 05 · Optimization

← previous: [04-information-theory.md](04-information-theory.md) · next: [math README](README.md) → then [`../prog/`](../prog/) or [`../classical/`](../classical/)

[Calculus](02-calculus.md) gave you the gradient and the basic descent step. Optimization is everything around that step: which direction to *really* go, how big a step to take, how to escape bad spots, and what "converged" even means. This is where training stops being a formula and becomes a craft — the difference between a model that trains in an hour and one that never trains at all is usually an optimization choice.

Pairs with episode 17 (gradient descent). Run [`04_descent_tuner.py`](./calculus-playground/04_descent_tuner.py) alongside this — feeling the learning rate misbehave is worth more than reading about it.

---

## 5.1 · Convex vs non-convex

A **convex** loss is bowl-shaped: one bottom, and downhill always leads to it. Gradient descent is *guaranteed* to find the global minimum. Linear and logistic regression are convex — that's why they just work.

A **non-convex** loss is a mountain range: many valleys, ridges, and saddle points. Neural networks are wildly non-convex, so in principle gradient descent could get stuck in a bad local minimum.

```
convex                 non-convex
  \      /             \  /\    /\  /
   \    /               \/  \  /  \/
    \__/                      \/
 one global min        many minima + saddles
```

The surprise of deep learning: **it works anyway.** In very high dimensions, most critical points are saddles rather than bad minima, the many minima tend to be about equally good, and noise from stochastic updates helps escape the bad spots. We gave up the convex guarantee and got something that works empirically — nobody fully knows why, and that's an honest open question.

---

## 5.2 · SGD — stochastic gradient descent

Computing the gradient over the *entire* dataset for every step is too slow. **SGD** estimates it from a small random **minibatch** instead:

```
w ← w − η · ∇L_batch(w)
```

Each step is noisy (it's an estimate), but it's thousands of times cheaper, so you take vastly more steps. The noise is a feature, not just a bug: it jostles the optimizer out of sharp, bad minima and tends to find flatter ones that generalize better. Batch size is a real knob — bigger is smoother and more parallel, smaller is noisier and sometimes generalizes better.

---

## 5.3 · The optimizer zoo

Plain SGD struggles when the loss surface is steeper in some directions than others — it zig-zags. The famous optimizers each fix a piece of that. You don't memorize the formulas; you know what each *adds*:

| Optimizer | What it adds | Intuition |
|---|---|---|
| **SGD** | the baseline | step downhill, one noisy batch at a time |
| **Momentum** | a velocity term | a ball rolling downhill — builds speed in consistent directions, damps zig-zag |
| **AdaGrad** | per-parameter rates | rare features get bigger steps; decays over time |
| **RMSprop** | a moving average of squared grads | fixes AdaGrad's "step size dies" problem |
| **Adam** | momentum **+** RMSprop | the default. Adaptive per-parameter steps with momentum |

**Adam is the one you reach for by default** — it combines a velocity term (momentum) with per-parameter learning rates (RMSprop), so it's forgiving about the initial learning rate and handles messy gradients well. SGD with momentum sometimes generalizes slightly better and is still common for vision. When in doubt: Adam.

> The notebooks switch from hand-rolled SGD to Adam for exactly these reasons — un-normalized features make plain SGD crawl, and Adam's per-parameter scaling absorbs that.

---

## 5.4 · Learning rate schedules

The learning rate is the single most important hyperparameter, and the best value *changes during training*: big steps early to make progress, small steps late to settle precisely. A **schedule** varies `η` over time:

- **Warmup** — start tiny and ramp up, so early noisy gradients don't blow things up. Standard for transformers.
- **Decay** — step, exponential, or cosine. Shrink `η` as you approach the minimum.
- **Cosine annealing** — a smooth decay to near-zero; the current default for most large models.

A good schedule routinely beats a fixed rate. It's the cheapest "free" accuracy in practice.

---

## 5.5 · Second-order methods

Gradient descent uses only the slope (first derivative). **Second-order methods** also use curvature (the Hessian, from [calculus](02-calculus.md)):

- **Newton's method** — jumps using curvature; converges in very few steps near a minimum, but needs the Hessian inverse (`n²`–`n³` cost). Impossible at neural-net scale.
- **L-BFGS** — approximates the curvature from recent gradients without forming the Hessian. Excellent for small/medium convex problems (classical ML, not deep nets).

For big models the Hessian is too expensive, so first-order adaptive methods (Adam) win on cost even though each step is "dumber." Knowing *why* — `n²` curvature vs `n` gradient — is the point.

---

## 5.6 · Constrained optimization, briefly

Sometimes you minimize subject to a **constraint** ("weights must sum to 1," "stay within a budget"). **Lagrange multipliers** turn a constrained problem into an unconstrained one by folding the constraint into the objective with a penalty term; the **KKT conditions** generalize this to inequality constraints. This is the machinery behind **support vector machines** (maximize the margin subject to classifying correctly) and the formal version of regularization. You'll meet it properly in [classical/](../classical/); for now, know that "constrained min" has a standard, gradient-friendly reformulation.

---

## 5.7 · Do these before moving on

1. Why is gradient descent guaranteed to find the best answer for logistic regression but not for a neural network?
2. What does SGD compute the gradient over instead of the full dataset, and what's the upside?
3. In one phrase each: what does **momentum** add, and what does **Adam** combine?
4. Why does the noise in SGD sometimes *help*?
5. Name one reason a learning-rate schedule beats a fixed learning rate.
6. Why don't we use Newton's method to train large neural networks?

<details>
<summary>Answers</summary>

1. Logistic regression's loss is **convex** (one global minimum, downhill always reaches it); a neural network's loss is **non-convex** (many minima and saddles), so no global guarantee.
2. A small random **minibatch**. Upside: each step is far **cheaper**, so you take many more steps in the same time (and the noise aids generalization).
3. Momentum adds a **velocity term** (a rolling ball that damps zig-zag); Adam combines **momentum + per-parameter adaptive rates** (RMSprop).
4. It **jostles the optimizer out of sharp/bad minima and saddle points**, often landing in flatter minima that generalize better.
5. **Big steps early** make fast progress while **small steps late** settle precisely (warmup avoids early blow-ups; decay avoids bouncing around the minimum).
6. Newton's method needs the **Hessian** (and its inverse) — an `n×n` matrix for `n` parameters, which is `n²`–`n³` cost. At billions of parameters it's infeasible, so we use first-order adaptive methods.
</details>

---

## Where to next

You've finished the math track. From here:

→ [`../prog/`](../prog/) — write code that uses all of this (NumPy, then the playground).
→ [`../classical/`](../classical/) — the simplest place to watch these ideas do real work (linear models, SVMs, trees).

Or revisit the [math index](README.md).

---

## Further reading

- [3Blue1Brown — Gradient descent, how neural networks learn](https://www.youtube.com/watch?v=IHZwWFHWa-w) — the visual anchor.
- [Sebastian Ruder — An overview of gradient descent optimization algorithms](https://www.ruder.io/optimizing-gradient-descent/) — the clearest written tour of the optimizer zoo.
- [distill.pub — Why Momentum Really Works](https://distill.pub/2017/momentum/) — interactive, gorgeous, deep.
- [Boyd & Vandenberghe — Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/) — the reference for the convex/constrained theory, free PDF.
