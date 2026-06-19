# 04 · Information theory

← previous: [03-probability.md](03-probability.md) · next: [05-optimization.md](05-optimization.md)

Information theory is short but it pays off immediately: it's the reason cross-entropy is *the* classification loss, what KL divergence measures when a VAE or a diffusion model minimizes it, and why "bits" is a unit of surprise. This is the smallest chapter with the highest ratio of "oh, *that's* what that loss function is" per page.

It builds straight on [probability](03-probability.md). One prerequisite reflex: logs turn products into sums, and `log(1/p) = −log(p)`.

---

## 4.1 · Information is surprise

The information content of an event is how *surprised* you should be by it:

```
I(x) = −log p(x)     =  log(1 / p(x))
```

A certain event (`p = 1`) carries zero information — no surprise, you knew it. A rare event (`p` tiny) carries a lot. This single definition drives everything else, and it's why it's a *negative* log: rare things have small `p`, large `−log p`, high surprise.

**Bits vs nats** is just the log base. `log₂` gives **bits** (the natural unit for "how many yes/no questions"); `ln` gives **nats**. ML uses nats because `ln` differentiates cleanly. Same quantity, different ruler.

---

## 4.2 · Entropy

**Entropy** is the *average* surprise of a distribution — the expected information content:

```
H(p) = −Σ p(x) log p(x)
```

It measures uncertainty. A fair coin has maximum entropy (you learn the most from the flip); a two-headed coin has zero (the outcome tells you nothing). High entropy = unpredictable = informative when resolved.

Intuition that sticks: entropy is the *theoretical minimum* average number of bits to encode samples from `p`. Predictable distributions compress well; uniform ones don't. That's the link between "uncertainty" and "compression" — they're the same number.

---

## 4.3 · Cross-entropy — the loss, explained

Now the payoff. **Cross-entropy** measures the average surprise when you encode data from the *true* distribution `p` using your *model's* distribution `q`:

```
H(p, q) = −Σ p(x) log q(x)
```

If your model `q` is perfect (`q = p`), cross-entropy bottoms out at the true entropy. If your model is wrong, you pay a surprise penalty. **So minimizing cross-entropy = making your model's predicted distribution match reality.** That's exactly what you want from training.

For classification, the true distribution is one-hot (the right label has probability 1), and the sum collapses to a single term:

```
loss = −log q(correct class)
```

That's it — that's the cross-entropy / log loss from the logistic-regression and classification series. Confident and right → tiny loss. Confident and wrong → huge loss. The whole behavior of the loss falls out of "−log of the probability you assigned to the truth."

---

## 4.4 · KL divergence

**KL divergence** measures how far one distribution is from another — the *extra* surprise from using `q` when the truth is `p`:

```
KL(p ‖ q) = Σ p(x) log( p(x) / q(x) )  =  H(p, q) − H(p)
```

Read that second form: **cross-entropy = entropy + KL divergence.** Since the true entropy `H(p)` is a constant you can't change, *minimizing cross-entropy is identical to minimizing KL divergence.* Training a classifier is pulling your model's distribution toward the data's.

Two things to remember:
- KL is **always ≥ 0**, and `= 0` only when the distributions match exactly.
- KL is **not symmetric**: `KL(p‖q) ≠ KL(q‖p)`. The two directions penalize different mistakes, which is a real modeling choice (it's why VAEs and some RL methods pick one direction deliberately).

KL is the objective (or part of it) in **VAEs** (keep the latent close to a prior), **diffusion models**, **variational inference**, and **distillation** (match a student to a teacher).

---

## 4.5 · Mutual information, and the rest

**Mutual information** `I(X; Y)` measures how much knowing one variable tells you about another — shared information, zero when independent. It shows up in feature selection, representation learning (InfoNCE, contrastive objectives), and analyses of what a network "knows."

The remaining syllabus terms, briefly: **channel capacity** (max reliable information rate — Shannon's original problem), **rate-distortion** (the tradeoff between compression and fidelity — the lens behind lossy compression and some generative models), and the **MDL principle** ("the best model is the one that compresses the data most," a formal Occam's razor). Know the names; reach for them when a paper does.

---

## 4.6 · Do these before moving on

1. Which carries more information: an event with `p = 0.99` or one with `p = 0.01`? Why?
2. A fair coin vs a coin that's heads 90% of the time — which has higher entropy?
3. Write the cross-entropy loss for a single correctly-labeled classification example.
4. Cross-entropy equals entropy plus what? And why does that mean minimizing cross-entropy minimizes KL?
5. Is `KL(p‖q)` the same as `KL(q‖p)`?
6. Your model assigns probability `0.1` to the true class. Is the loss large or small? What if it assigned `0.95`?

<details>
<summary>Answers</summary>

1. The **`p = 0.01`** event — rarer means more surprising, and `I = −log p` is larger for small `p`.
2. The **fair coin** (`H = 1 bit`, maximum for two outcomes). The 90/10 coin is more predictable, so lower entropy.
3. `loss = −log q(correct class)` — negative log of the probability the model gave the true label.
4. Cross-entropy = **entropy `H(p)` + `KL(p‖q)`**. Since `H(p)` is fixed by the data, minimizing cross-entropy can only reduce the **KL** term — pulling `q` toward `p`.
5. **No** — KL divergence is not symmetric in general.
6. `−log(0.1) ≈ 2.30` — **large** loss. `−log(0.95) ≈ 0.05` — **small** loss. Confidence in the truth is rewarded.
</details>

---

## Where to next

→ [05-optimization.md](05-optimization.md) — how the gradients actually get followed: SGD, momentum, Adam, and why they differ.

Or back to the [math index](README.md).

---

## Further reading

- [3Blue1Brown — But what is entropy / Wordle solver](https://www.youtube.com/watch?v=v68zYyaEmEA) — information as the optimal-guessing quantity, made visual.
- [Christopher Olah — Visual Information Theory](https://colah.github.io/posts/2015-09-Visual-Information-Theory/) — the clearest visual treatment of entropy, cross-entropy, and KL anywhere.
- [Mathematics for Machine Learning](https://mml-book.github.io/) and, for depth, Cover & Thomas, *Elements of Information Theory*.
