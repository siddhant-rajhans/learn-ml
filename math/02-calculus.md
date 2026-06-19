# 02 · Calculus

← previous: [01-linear-algebra.md](01-linear-algebra.md) · next: [03-probability.md](03-probability.md)

**Visual companions:** the 5-episode calculus series (eps 14–18) and the runnable [calculus-playground/](./calculus-playground/) — change a number, rerun, watch the math move.

Calculus is the math of change, and ML is one long optimization problem, so calculus is how models *learn*. Training is: measure how wrong you are, find which direction reduces the wrongness, step that way, repeat. The "which direction" is a gradient. The "how the error flows back through the layers" is the chain rule. That's the whole of backprop, and it's just calculus you already half-know, applied carefully.

This chapter pairs tightly with the video series — the videos build each idea visually; here you get the through-line, the ML payoff, and exercises. Watch the matching episode, run the matching playground script, then test yourself.

---

## 2.1 · The derivative is a slope

The derivative of `f` at a point is the **slope of the curve there** — the rate at which output changes as you nudge the input.

```
f'(x) = how fast f changes at x
      = slope of the tangent line
```

Three readings, same object: a slope, an instantaneous rate of change, and the best straight-line approximation to the curve near that point. That last one is the deepest — calculus is the art of approximating curvy things with flat things you can compute.

In ML, `f` is the loss and `x` is a parameter. The derivative answers: *if I nudge this weight up, does the loss go up or down, and how fast?* That single number is the entire training signal for one parameter.

> Episode 14 builds this from the tangent line. Run [`01_tangent_line.py`](./calculus-playground/01_tangent_line.py) and drag the point along the curve.

---

## 2.2 · The chain rule is backprop

Most functions in ML are functions of functions of functions — a deep network is `f(g(h(x)))` stacked dozens deep. The **chain rule** tells you the derivative of a composition:

```
d/dx f(g(x)) = f'(g(x)) · g'(x)
```

In words: **multiply the local slopes along the chain.** The error at the output flows backward, getting multiplied by each layer's local derivative on the way.

This *is* backpropagation. There's no extra magic. "Backprop" is the chain rule applied to a computational graph, with the multiplications organized so you reuse work instead of recomputing it. Once you see that, the mystery evaporates — and you also see why very deep chains cause **vanishing/exploding gradients**: multiply many small numbers and you get ~0; many large ones and you blow up.

> Episode 15. Run [`02_chain_rule.py`](./calculus-playground/02_chain_rule.py) to watch slopes multiply through a chain.

---

## 2.3 · Partial derivatives and the gradient

Real models have millions of parameters, not one. A **partial derivative** `∂f/∂wᵢ` is the slope in one parameter's direction, holding the rest fixed — "if I wiggle only this weight, how does the loss respond?"

Stack all the partials into a vector and you get the **gradient**:

```
∇f = [∂f/∂w₁, ∂f/∂w₂, ..., ∂f/∂wₙ]
```

The gradient is the single most important object in ML training, because of one fact: **it points in the direction of steepest increase.** So `−∇f` points downhill, toward lower loss. Every optimizer is a strategy for following `−∇f`.

> Episode 16. Run [`03_gradient_field.py`](./calculus-playground/03_gradient_field.py) to see gradient arrows over a surface.

---

## 2.4 · Gradient descent

Put 2.1–2.3 together and you get the algorithm that trains essentially everything:

```
repeat:
    w ← w − η · ∇L(w)
```

Stand on the loss surface, compute the downhill direction, take a step of size `η` (the learning rate), repeat until you stop improving. That's it. Linear regression, logistic regression, a 70-billion-parameter transformer — all trained by this loop.

The learning rate is the one knob that breaks everything when it's wrong: too big and you overshoot and diverge; too small and you crawl. The whole zoo of optimizers (Momentum, RMSprop, Adam) are smarter versions of this step — covered properly in [05-optimization.md](05-optimization.md).

> Episode 17. Run [`04_descent_tuner.py`](./calculus-playground/04_descent_tuner.py) and feel what the learning rate does — it's the fastest way to build intuition for it.

---

## 2.5 · Jacobian and Hessian

Two generalizations you'll meet in papers:

- **Jacobian** — when `f` takes a vector *and returns a vector*, the Jacobian is the matrix of all partial derivatives (every output's slope with respect to every input). A network layer's local derivative is a Jacobian; backprop multiplies Jacobians.
- **Hessian** — the matrix of *second* derivatives. It measures **curvature**: how the gradient itself changes. Its eigenvalues tell you whether you're in a bowl, on a saddle, or on a ridge — which is exactly why some directions of a loss landscape train fast and others stall.

You rarely compute a full Hessian (it's `n²` for `n` parameters — astronomical for big models), but you reason about it constantly. Second-order optimizers approximate it.

---

## 2.6 · Taylor series and automatic differentiation

**Taylor series** approximates any smooth function near a point using its derivatives:

```
f(x + Δ) ≈ f(x) + f'(x)Δ + ½ f''(x)Δ² + ...
```

This is the theoretical backbone of optimization: gradient descent is the first-order Taylor approximation (use the slope); Newton's method adds the second-order term (use the curvature). When a proof says "to first order," this is what it means.

**Automatic differentiation (autodiff)** is how PyTorch and JAX compute exact gradients of arbitrary code. It's not symbolic math and not finite-difference approximation — it's the chain rule applied mechanically to the computational graph as the code runs. Understanding 2.2 means you understand what `loss.backward()` actually does.

> Episode 18 (the finale) derives backprop in five lines. Run [`05_backprop_by_hand.py`](./calculus-playground/05_backprop_by_hand.py) to do it manually once — after that, you'll trust the framework because you know what it's doing.

---

## 2.7 · Do these before moving on

1. The loss has derivative `∂L/∂w = −3` at your current weight. Which way do you change `w` to reduce loss, and why?
2. State backprop in one sentence using the words "chain rule."
3. Your gradient is `∇L = [0, 0, 0]`. What does that mean about where you are?
4. A learning rate that's too large does what to training? Too small?
5. What does the Hessian measure that the gradient doesn't?
6. Why don't we compute the full Hessian for large neural networks?

<details>
<summary>Answers</summary>

1. **Increase `w`.** The update is `w ← w − η·(∂L/∂w) = w − η·(−3) = w + 3η`. Negative slope means loss falls as `w` rises, so step up. (This is the sign intuition from the video series.)
2. Backprop is the **chain rule** applied to the network's computational graph, multiplying local derivatives backward from the loss while reusing shared work.
3. You're at a **critical point** — a minimum, maximum, or saddle. The gradient gives no direction to move; training stalls there.
4. Too large: **overshoots the minimum, oscillates or diverges.** Too small: **converges very slowly** (and can get stuck in shallow regions).
5. **Curvature** — the second derivative, how fast the gradient itself is changing. The gradient is slope; the Hessian is how the slope bends.
6. It's an **`n×n` matrix for `n` parameters** — quadratic in model size, so for billions of parameters it's impossible to store or invert. We approximate it instead.
</details>

---

## Where to next

→ [03-probability.md](03-probability.md) — uncertainty, distributions, and Bayes.

Or back to the [math index](README.md).

---

## Further reading

- [3Blue1Brown — Essence of Calculus](https://www.3blue1brown.com/topics/calculus) — the intuition, beautifully.
- [Mathematics for Machine Learning](https://mml-book.github.io/) — Ch. 5 (Vector Calculus), free PDF.
- [The Matrix Calculus You Need For Deep Learning](https://explained.ai/matrix-calculus/) — Parr & Howard, bridges single-variable calculus to the vector/matrix derivatives ML actually uses.
- [Khan Academy — Multivariable Calculus](https://www.khanacademy.org/math/multivariable-calculus) — for the partial-derivative and gradient mechanics.
