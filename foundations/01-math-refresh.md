# 01 · Math refresh

← back: [foundations README](README.md) · next: [02-coding-projects.md](02-coding-projects.md)

Pre-foundations taught you to *read* math notation without flinching. This chapter teaches you to *use* it.

The difference matters. Reading `f(x) = x² + 1` and knowing it's a function is one skill. Solving `x² + 1 = 5`, knowing the graph is a U-shape that sits one unit off the floor, and recognizing the same parabola when it shows up as a loss curve — that's the skill ML actually leans on.

If you haven't done [pre-foundations 02-math-zero](../pre-foundations/02-math-zero.md), do that first. It covers fractions, exponents, logs, the symbols (Σ, Π, ∈, ∇), and basic function notation. I won't re-explain those here. This is the layer on top: solving, the function zoo, a little trig, and the counting you need before probability.

Nothing here needs proofs. You're building the working math of a practitioner, not a mathematician.

---

## 1.1 · Solving equations

You met equations in pre-foundations: two expressions with `=` between them. Solving means isolating the unknown. One rule, used over and over: **whatever you do to one side, do to the other.**

```
3x - 7 = 11
3x = 18          add 7 to both sides
x = 6            divide both sides by 3
```

Two unknowns need two equations. This is a **system**, and you solve it by substitution or elimination:

```
y = 2x + 1
y = -x + 7

2x + 1 = -x + 7        substitute the first into the second
3x = 6
x = 2,  y = 5          back-substitute
```

That `(2, 5)` is where two lines cross. Hold onto that picture — half of classical ML is "find where these things meet" or "find where this is smallest."

In ML you rarely solve by hand. But you solve `∂L/∂w = 0` conceptually every time you train: gradient descent is just *numerically* hunting for where the slope is zero, because you can't always solve it on paper.

---

## 1.2 · Inequalities

Same moves as equations, with one trap: **multiply or divide by a negative, and the inequality flips.**

```
-2x < 6
x > -3           divide by -2, flip < to >
```

Inequalities describe regions, not points. `x ≥ 0` is "the right half of the number line." You'll see them everywhere a model has a constraint:

- A probability lives in `0 ≤ p ≤ 1`.
- A ReLU activation is `max(0, x)` — it outputs `x` when `x > 0`, else `0`.
- A learning rate is `η > 0`, and in practice `η ≪ 1`.

The notation `≤` and `≥` (less/greater than or equal) carries the boundary; `<` and `>` exclude it. Same closed-vs-open idea as the intervals from pre-foundations.

---

## 1.3 · Factoring and the quadratic

**Factoring** means rewriting a sum as a product. It's reverse multiplication.

```
x² - 5x + 6 = (x - 2)(x - 3)
```

To check, expand it back: `(x-2)(x-3) = x² - 3x - 2x + 6 = x² - 5x + 6`. The trick: find two numbers that multiply to the last term (`+6`) and add to the middle one (`-5`). Here, `-2` and `-3`.

Why bother? A product is zero only when one of its factors is zero. So `(x-2)(x-3) = 0` means `x = 2` or `x = 3`. Factoring turns a curve-crossing problem into two trivial ones.

When factoring is ugly, the **quadratic formula** always works for `ax² + bx + c = 0`:

```
        -b ± √(b² - 4ac)
  x  =  ──────────────────
              2a
```

The piece under the root, `b² - 4ac`, is the **discriminant**. It tells you the story before you finish:

```
b² - 4ac > 0    two real solutions    (parabola crosses the x-axis twice)
b² - 4ac = 0    one solution          (parabola just kisses the axis)
b² - 4ac < 0    no real solutions     (parabola floats above or below)
```

You won't run the quadratic formula during training. But the *shape* it describes — a parabola with a single lowest point — is the picture of a well-behaved loss function. Convex. One bottom. Gradient descent's favorite case.

---

## 1.4 · The function zoo

Pre-foundations introduced `f(x)`. Here's the cast of characters you'll meet again and again. For each, learn the **shape** and **where it lives in ML** — not the algebra.

### Linear — `f(x) = mx + b`

A straight line. `m` is the slope (rise over run), `b` is where it crosses the y-axis.

```
 y
 |        /
 |      /
 |    /          slope m = steepness
 |  /            intercept b = height at x=0
 +────────── x
```

This *is* linear regression with one feature. The entire ep19–23 YouTube series is about finding the best `m` and `b`. A neuron before its activation is `w·x + b` — the same line, just with `x` as a vector.

### Quadratic — `f(x) = ax² + bx + c`

A parabola. Opens up if `a > 0`, down if `a < 0`. One turning point (the **vertex**).

```
 y                    y
 |   \      /         |  ───╮    ╭───
 |    \    /          |      \  /
 |     \__/           |       \/
 +────────── x        +────────── x
   a > 0 (a bowl)       a < 0 (a hill)
```

The bowl is the mental model for a loss surface. Lowest point = best parameters. The whole game of training is rolling down to that vertex.

### Polynomial — `f(x) = aₙxⁿ + ... + a₁x + a₀`

Higher powers, more wiggles. A degree-`n` polynomial can turn up to `n-1` times. Degree 3 (cubic) has an S-ish bend; higher degrees get wavy.

These show up as a cautionary tale: fit a high-degree polynomial to a few points and it'll snake through every one of them perfectly — then predict garbage between them. That's **overfitting**, drawn in one picture.

### Rational — `f(x) = 1/x` and friends

A ratio of polynomials. The defining feature is **asymptotes** — places the curve races toward but never touches.

```
 y
 |  |
 |  |
 |   \___
 +────────── x
    blows up near x=0
```

Rational functions are why you guard against divide-by-zero. `1/x` near `x=0` is the reason you'll write `x + 1e-8` in denominators to keep things finite.

### Exponential and logarithm — `f(x) = eˣ` and `f(x) = ln(x)`

You met these in pre-foundations. Worth restating as shapes, because they're mirror images across the line `y = x`:

```
 eˣ : starts flat near 0, then EXPLODES upward
 ln : EXPLODES upward near 0, then crawls almost flat
```

`eˣ` is inside softmax and sigmoid. `ln` is inside every log-loss / cross-entropy. They're inverses, which is exactly why "take the log of the exponential" cancels and keeps the math stable.

If you can sketch these seven shapes from memory — line, bowl, wiggle, asymptote, explosion, crawl — you've got the visual vocabulary for most of ML intuition.

---

## 1.5 · Trigonometry, lightly

You need a little trig, not a semester of it.

`sin`, `cos`, and `tan` relate an angle to ratios of a right triangle's sides. The cleanest way to hold them is the **unit circle** — a circle of radius 1 centered at the origin. A point on it at angle `θ` is exactly `(cos θ, sin θ)`.

```
        (0,1)
          |
 (-1,0) ──+── (1,0)      a point at angle θ is (cos θ, sin θ)
          |
        (0,-1)
```

The one identity worth memorizing falls straight out of that picture (it's the Pythagorean theorem on the circle):

```
sin²θ + cos²θ = 1
```

Where this shows up in ML:

- **Rotations.** Spinning a vector by angle `θ` is multiplying by a matrix built from `sin` and `cos`. The ep12–13 linear-algebra material leans on this.
- **Periodicity.** `sin` and `cos` repeat forever, so they're used to encode position in transformers (the famous sinusoidal positional encodings) and any signal that cycles.
- **Similarity.** Cosine similarity — how aligned two vectors are — is literally the `cos` of the angle between them. `1` means same direction, `0` means perpendicular, `-1` means opposite.

That's enough. If you ever need more, it's a lookup, not a memory test.

---

## 1.6 · Sets, logic, and counting

Pre-foundations gave you set *notation* (∈, ∪, ∩). Here's the reasoning you build on it, because probability is right around the corner and probability is just counting done carefully.

### Logic

Three operators, the same ones you'll write in code as `and`, `or`, `not`:

```
A AND B    true only when both are true
A OR  B    true when at least one is true
NOT A      flips true/false
```

The one rule that surprises people, **De Morgan's law** — useful when you simplify conditions:

```
NOT (A AND B)  =  (NOT A) OR  (NOT B)
NOT (A OR  B)  =  (NOT A) AND (NOT B)
```

"It's not the case that both happened" is the same as "at least one didn't." You'll feel this every time you untangle a gnarly `if` statement.

### Counting

Before probability you need to count outcomes. Two ideas cover most of it.

**Permutations** — arrangements where order matters. How many ways to order `r` things out of `n`:

```
        n!
P(n,r) = ──────        n! means n × (n-1) × ... × 1
       (n-r)!
```

**Combinations** — selections where order does *not* matter. How many ways to choose `r` things out of `n`:

```
        n!
C(n,r) = ──────────       also written  (n choose r)
        r!(n-r)!
```

The difference in one sentence: picking a 3-person committee is a combination (order doesn't matter); picking gold-silver-bronze is a permutation (order does).

Why it matters: probability of an event is (favorable outcomes) / (total outcomes), and both halves are counting problems. Combinations also appear directly in the binomial distribution, which is the foundation under a lot of classification math.

---

## 1.7 · Do these before moving on

Don't peek. Try each, then check.

1. Solve `5x - 3 = 2x + 9`.
2. Solve and flip correctly: `-3x ≥ 12`.
3. Factor `x² - 7x + 12`, then give both solutions of `x² - 7x + 12 = 0`.
4. Use the discriminant: how many real solutions does `x² + x + 1 = 0` have?
5. You're at angle `θ` on the unit circle and `cos θ = 0.6`. What is `sin θ`? (positive case)
6. How many ways to choose a 2-person team from 5 people? (combination)
7. Rewrite without the outer NOT: `NOT (rainy AND cold)`.

<details>
<summary>Answers</summary>

1. `5x - 3 = 2x + 9` → `3x = 12` → **x = 4**.
2. `-3x ≥ 12` → divide by -3 and flip → **x ≤ -4**.
3. `(x - 3)(x - 4)`, so **x = 3 or x = 4**.
4. Discriminant `= 1² - 4·1·1 = -3 < 0` → **no real solutions** (the parabola floats above the x-axis).
5. `sin²θ = 1 - 0.6² = 1 - 0.36 = 0.64`, so **sin θ = 0.8**.
6. `C(5,2) = 5! / (2!·3!) = 10` → **10 teams**.
7. **`(NOT rainy) OR (NOT cold)`** — by De Morgan.
</details>

If two or more of those fought back, re-read the matching section before continuing. This is the math you'll stand on for the rest of the map.

---

## Where to next

→ [02-coding-projects.md](02-coding-projects.md) — turn the Python from pre-foundations into three real programs.

Or jump back to the [foundations index](README.md).

---

## Further reading

- [Khan Academy — Algebra & Precalculus](https://www.khanacademy.org/math/algebra2) — free, thorough, the standard refresh.
- [Paul's Online Math Notes](https://tutorial.math.lamar.edu/) — concise, no-nonsense algebra and precalc, great as a reference.
- [3Blue1Brown — Essence of Linear Algebra](https://www.3blue1brown.com/topics/linear-algebra) — for after this, when the function shapes become transformations.
- [Seeing Theory](https://seeing-theory.brown.edu/) — a visual intro to probability, for when the counting here turns into chance.
