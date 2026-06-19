# 03 · Probability & Bayesian thinking

← previous: [02-calculus.md](02-calculus.md) · next: [04-information-theory.md](04-information-theory.md)

Machine learning is applied probability wearing an engineering hat. A model doesn't output "cat" — it outputs a *distribution* over labels and you read off the most probable one. Training a model is finding the parameters that make your data most probable. Every loss function you've met is a probability statement in disguise. Get comfortable here and a dozen ML ideas stop being separate facts and become one idea.

There's no episode for this yet, so this chapter leans harder on curated resources — the standout is **Brown's [Seeing Theory](https://seeing-theory.brown.edu/)**, a visual probability course; skim it alongside this. Here you get the ML-focused through-line and exercises.

---

## 3.1 · The rules, fast

Probability assigns numbers in `[0, 1]` to events. Three rules generate everything:

```
0 ≤ P(A) ≤ 1                          probabilities live in [0,1]
P(A or B) = P(A) + P(B) − P(A and B)  the inclusion rule
P(A and B) = P(A) · P(B | A)          the chain rule
```

The one to internalize is **conditional probability**, `P(A | B)` — "probability of A *given that* B happened." It's the whole game: a classifier computes `P(label | input)`. A language model computes `P(next token | everything so far)`. Generation is just sampling from a conditional, one step at a time.

**Independence** is when `P(A | B) = P(A)` — knowing B tells you nothing about A. The "naive" in Naive Bayes is assuming features are independent. It's usually false and often works anyway.

---

## 3.2 · Random variables and distributions

A **random variable** attaches numbers to random outcomes. A **distribution** says how probable each value is. The ones worth knowing on sight:

| Distribution | Shape / use | Where it shows up in ML |
|---|---|---|
| **Bernoulli** | one coin flip, prob `p` | binary classification output |
| **Categorical** | one roll of a `k`-sided die | multiclass output (softmax) |
| **Gaussian (normal)** | the bell curve | noise, initialization, latent spaces, "errors" |
| **Uniform** | flat, all equal | dropout masks, random init ranges |

The **Gaussian** earns special status — it's everywhere because of the central limit theorem (3.5), it's the maximum-entropy distribution for a given variance, and its math is uniquely clean. Weight init, VAE latents, diffusion noise, the assumption behind mean-squared error — all Gaussian.

Discrete distributions have a **probability mass function** (PMF); continuous ones have a **probability density** (PDF) that integrates to 1. The mean (`expected value`, `E[X]`) is the average you'd get over infinite samples; the **variance** is how spread out it is.

---

## 3.3 · Bayes' theorem, deeply

Bayes' theorem flips a conditional around, and it's the most important equation in this chapter:

```
              P(data | hypothesis) · P(hypothesis)
P(hyp | data) = ─────────────────────────────────────
                          P(data)
```

Name the pieces, because you'll hear them constantly:

- **Prior** `P(hyp)` — what you believed before seeing data.
- **Likelihood** `P(data | hyp)` — how well the hypothesis explains the data.
- **Posterior** `P(hyp | data)` — your updated belief after.

The Bayesian worldview: **start with a belief, see evidence, update.** That loop is spam filters, medical diagnosis, A/B testing, and the philosophical backbone of half of ML. The famous "the test is 99% accurate but a positive result still probably means you're healthy" puzzle is just Bayes with a small prior — work that example until it stops being surprising.

---

## 3.4 · MLE and MAP — where loss functions come from

This is the section that pays for the whole chapter. **Maximum likelihood estimation (MLE)** picks the parameters that make the observed data most probable:

```
θ* = argmax  P(data | θ)
```

Maximizing a product of probabilities is numerically nasty, so we maximize its **log** instead (logs turn products into sums — see [pre-foundations](../pre-foundations/02-math-zero.md)), and since optimizers minimize, we flip the sign. The result:

> **Minimizing negative log-likelihood = MLE.** And:
> - Gaussian likelihood → **mean-squared error**. (MSE *is* MLE under Gaussian noise.)
> - Bernoulli/categorical likelihood → **cross-entropy / log loss**.

So MSE and cross-entropy aren't arbitrary choices someone picked because they "worked." They're what MLE *forces* on you once you assume a noise model. That's why the logistic-regression series uses log loss — it's the negative log-likelihood of a Bernoulli.

**MAP** (maximum a posteriori) adds a prior: `argmax P(data|θ)·P(θ)`. The prior term turns out to be exactly **regularization** — an L2 prior is weight decay, an L1 prior is Lasso. Regularization is just MLE with a belief about what good weights look like.

---

## 3.5 · Central limit theorem

Add up lots of independent random things and the sum looks Gaussian — *no matter what the individual things looked like.*

That's the **central limit theorem**, and it's why the bell curve is inescapable: measurement noise, averaged gradients over a minibatch, the distribution of a sum of features — all drift toward Gaussian. It's the license behind "assume the errors are normal," and the reason the Gaussian is the default when you don't know better.

---

## 3.6 · The rest, in one breath

You'll meet these later; know what they're *for* now:

- **Exponential family** — a unifying form (Gaussian, Bernoulli, Poisson, ...) that makes the math of generalized linear models clean.
- **Markov chains** — "the next state depends only on the current one." The backbone of MCMC, and the mental model for autoregressive generation.
- **MCMC / variational inference** — two ways to approximate posteriors that are too hard to compute exactly. VI in particular powers VAEs.
- **Concentration inequalities** (Hoeffding, Chebyshev) — guarantees that sample averages stay close to true means. The theory behind why a test set tells you anything.

---

## 3.7 · Do these before moving on

1. A classifier outputs `P(spam | email) = 0.8`. In one sentence, what kind of probability is that?
2. Why do we maximize *log*-likelihood instead of likelihood directly?
3. MSE is the maximum-likelihood loss under what assumption about the noise?
4. L2 regularization corresponds to adding what, in the MAP view?
5. A disease affects 1 in 1000. A test is 99% accurate. You test positive. Roughly, is it more likely you have the disease or not? (Reason with Bayes; no exact number needed.)
6. Why does the Gaussian show up even when the underlying things aren't Gaussian?

<details>
<summary>Answers</summary>

1. A **conditional probability** — the probability of "spam" *given* this particular email.
2. The **log turns the product of many probabilities into a sum**, which avoids numerical underflow and is far easier to differentiate. The argmax is unchanged because log is monotonic.
3. **Gaussian (normally distributed) noise.** MSE is the negative log-likelihood of a Gaussian.
4. A **Gaussian prior on the weights** (centered at 0). That prior's log is the `−λ‖w‖²` term — weight decay.
5. **More likely you do NOT have it.** With a 0.1% prior, the false positives (≈1% of the 999 healthy people ≈ 10) vastly outnumber the true positives (≈1 sick person), so a positive is most often a false alarm. Small prior wins.
6. The **central limit theorem**: sums/averages of many independent contributions converge to a Gaussian regardless of the individual distributions.
</details>

---

## Where to next

→ [04-information-theory.md](04-information-theory.md) — entropy, KL divergence, and why cross-entropy is the right loss.

Or back to the [math index](README.md).

---

## Further reading

- [Seeing Theory](https://seeing-theory.brown.edu/) — Brown's visual, interactive probability course. Start here.
- [3Blue1Brown — Bayes' theorem](https://www.youtube.com/watch?v=HZGCoVF3YvM) and [the binomial / "probabilities of probabilities"](https://www.youtube.com/watch?v=8idr1WZ1A7Q) videos.
- [Mathematics for Machine Learning](https://mml-book.github.io/) — Ch. 6 (Probability & Distributions), free PDF.
- [StatQuest](https://www.youtube.com/c/joshstarmer) — Josh Starmer explains every stats concept slowly and clearly. Great when one idea won't stick.
