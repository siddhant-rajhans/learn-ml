# 02 · Math from zero

← previous: [01-computer-literacy.md](01-computer-literacy.md) · next: [03-python-syntax-and-data.md](03-python-syntax-and-data.md)

You don't need to be a mathematician to do ML. You need to stop flinching when notation shows up.

This is the refresh. Arithmetic that creeps back into ML in weird ways (every time floats don't add up cleanly, every time someone says "learning rate of 0.001" and means something specific). Algebra you might have forgotten. The handful of symbols (Σ, Π, ∈, ∇) that look intimidating until someone tells you what they actually mean.

You're not learning to do proofs. You're learning to read.

---

## 2.1 · Arithmetic refresh

### Fractions

A fraction `a/b` means *a divided by b*. The number on top is the **numerator**, the bottom is the **denominator**.

```
1/2 = 0.5
3/4 = 0.75
1/3 = 0.333...
```

Rules you'll use:

- **Add fractions** with the same bottom: `1/4 + 2/4 = 3/4`. Different bottoms? Find a common denominator first: `1/2 + 1/3 = 3/6 + 2/6 = 5/6`.
- **Multiply fractions**: `(1/2) * (1/3) = 1/6`. Top times top, bottom times bottom.
- **Divide fractions**: flip the second, then multiply. `(1/2) / (1/3) = (1/2) * (3/1) = 3/2`.

In ML, you'll see fractions less than you'd think — most things become decimals. But probabilities are often written as fractions (`P(A | B) = 1/3`), and the gradient of a loss is the *ratio* of two changes, which is fundamentally a fraction.

### Decimals

`0.5` is the same as `1/2`. `0.333` is approximately `1/3`. Decimals are just fractions with a denominator that's a power of 10 (or close to it).

The position after the decimal point matters: `0.1` is one tenth, `0.01` is one hundredth, `0.001` is one thousandth. You'll see `learning_rate = 0.001` constantly — that's *very small steps*.

### Percents

`50%` means `50/100` means `0.5`. Three forms of the same number.

To convert: divide by 100 to get a decimal (`73% → 0.73`), multiply by 100 to go back (`0.04 → 4%`).

You'll see *"the model is 87% confident"* a lot. That's a probability dressed up as a percent.

### Negative numbers

Numbers less than zero. The rules:

- `+ + +` and `+ - −` give positive results.
- `− × −` gives a positive. `(-3) × (-4) = 12`.
- `− × +` gives a negative. `(-3) × 4 = -12`.

In ML: gradients can be positive or negative. *Negative gradient* means "the loss is going down as this weight goes up" — so to lower the loss, we *increase* the weight. We covered this in episodes 16 + 17 of the calculus series.

### Order of operations

`2 + 3 × 4` is **14**, not 20. Why? **PEMDAS** — the order in which operations get evaluated:

1. **P**arentheses first
2. **E**xponents
3. **M**ultiplication and **D**ivision (left to right)
4. **A**ddition and **S**ubtraction (left to right)

```
2 + 3 × 4       =  2 + 12       = 14
(2 + 3) × 4     =  5 × 4        = 20
2^3 + 1         =  8 + 1        = 9
2 × (3 + 4)^2   =  2 × 49       = 98
```

This applies in code too. Python evaluates `2 + 3 * 4` as `14`, exactly like the math.

**When in doubt, use parentheses.** Even when they're not strictly needed. Readability > cleverness.

### Scientific notation

When you see `1.5e6` in code or `1.5 × 10⁶` in math, both mean **1,500,000** — 1.5 with the decimal point moved 6 places to the right.

```
1e3   = 1000               (one thousand)
1e6   = 1,000,000          (one million)
1e9   = 1,000,000,000      (one billion)
1e-3  = 0.001              (one thousandth)
1e-6  = 0.000001           (one millionth)
```

Why this matters: ML deals in numbers like `learning_rate=1e-4` and `params=175e9`. Reading these without converting in your head saves time.

---

## 2.2 · Exponents and roots

### Exponents

`x^n` (or `x**n` in code) means *x multiplied by itself n times*.

```
2^3 = 2 × 2 × 2 = 8
5^2 = 25
10^0 = 1                  (any number to the 0 is 1)
3^1 = 3                   (any number to the 1 is itself)
2^(-1) = 1/2 = 0.5        (negative exponent = reciprocal)
4^(1/2) = √4 = 2          (fractional exponent = root)
```

Rules you'll actually use:

```
x^a × x^b  = x^(a+b)             (multiplying same base: add exponents)
x^a / x^b  = x^(a-b)             (dividing same base: subtract exponents)
(x^a)^b    = x^(a×b)             (power of a power: multiply exponents)
x^0        = 1                   (always, for any nonzero x)
```

### Square roots

`√4 = 2` because `2 × 2 = 4`. `√9 = 3`, `√16 = 4`, `√2 ≈ 1.414`.

In code: `import math; math.sqrt(2)`.

### The constant e

`e ≈ 2.71828...` is a special number that shows up everywhere in math and ML. You'll see `e^x` (often written `exp(x)`) in:

- The softmax activation: `softmax(z_i) = e^(z_i) / Σ e^(z_j)`
- The sigmoid: `σ(x) = 1 / (1 + e^(-x))`
- Continuous probability distributions: `P(x) = e^(...)` for many of them.

You don't need to compute `e^x` in your head — Python and any calculator does it. You need to *recognize* it.

---

## 2.3 · Logarithms

The logarithm is the inverse of an exponent. If `2^3 = 8`, then `log₂(8) = 3`. In English: *"log base 2 of 8 is 3"* — meaning *"to get 8, raise 2 to the 3rd power."*

```
log₂(8) = 3              because 2^3 = 8
log₁₀(1000) = 3          because 10^3 = 1000
log(1) = 0               for any base, log(1) = 0 (because anything^0 = 1)
```

Two bases you'll see constantly:

- `log₁₀(x)` — log base 10. Sometimes just written `log(x)`. Used for "orders of magnitude."
- `ln(x)` or `log(x)` (in PyTorch, NumPy) — **natural log**, base `e`. Used in loss functions, information theory, anywhere `e` shows up.

In ML papers, `log` almost always means `ln` (natural log). Get used to that convention.

Rules you'll meet:

```
log(a × b) = log(a) + log(b)         (multiplication becomes addition)
log(a / b) = log(a) - log(b)
log(a^n)   = n × log(a)
log(1)     = 0
log(0)     = -∞ (negative infinity — undefined, but it's the limit)
```

The first rule is why logs show up in loss functions. Multiplying many tiny probabilities (`0.001 × 0.002 × ...`) underflows to zero. Taking the log turns the product into a sum, which is numerically stable. *That's the whole reason cross-entropy uses log.*

---

## 2.4 · Variables, expressions, equations

### Variable (mathematical sense)

A letter that stands for a number. `x = 5` means *"the variable x has the value 5."*

In ML we use letters all the time: `W` for weight matrices, `b` for biases, `x` for input, `y` for output, `L` for loss, `η` for learning rate.

### Expression vs equation

- **Expression**: a formula that *evaluates to* a number. `2x + 3` is an expression. If `x = 5`, it evaluates to 13.
- **Equation**: two expressions with `=` between them. `2x + 3 = 13` is an equation. You can *solve* it for `x` (here, `x = 5`).

### Basic algebra moves

To solve `2x + 3 = 13`:

1. Subtract 3 from both sides: `2x = 10`.
2. Divide both sides by 2: `x = 5`.

The rule: whatever you do to one side, do to the other. The `=` is sacred.

### Functions

A **function** is a rule that takes an input and produces an output. Written as `f(x) = ...`:

```
f(x) = 2x + 3            "f takes x, doubles it, adds 3"
f(0) = 3
f(5) = 13
f(-2) = -1
```

You're already used to this from Python — `def f(x): return 2*x + 3`. The math notation is older but it's the same idea.

In ML, a neural network is one giant function. It takes an input (an image, a sentence) and produces an output (a label, a next token).

---

## 2.5 · The coordinate plane

Two perpendicular axes — `x` (horizontal) and `y` (vertical) — meeting at the **origin** `(0, 0)`. Every point on the plane has coordinates `(x, y)`.

```
        y
        |
        |     • (3, 4)
        |
        |
 ───────+─────── x
        |
        |
        |
```

When you plot a function `y = f(x)`, you put a dot at `(x, f(x))` for many values of x. The dots form a curve.

In ML, you'll see plots constantly: loss over training steps (x = step, y = loss), accuracy over epochs, the data scatter plot, the gradient descent path. They all live on this plane.

### Three curves to know by sight

```
y = x         linear              a straight line through the origin
y = x²        parabola            a U-shape
y = √x        square root         climbs fast at first, then flattens
y = 1/x       hyperbola           two branches, blowing up near 0
y = sin(x)    sine wave           a smooth oscillation
y = e^x       exponential         starts slow, then EXPLODES
y = log(x)    logarithm           climbs fast at first, then crawls
```

If you can mentally picture the *shape* of each one, you've absorbed 80% of what you need for ML intuition. The other 20% is calculus, which we covered in the YouTube series.

---

## 2.6 · Notation you'll see in ML

### Sums

`Σ` (capital sigma) means *"add these up."*

```
       n
       Σ  xᵢ     means    x₁ + x₂ + x₃ + ... + xₙ
      i=1
```

Read it as *"sum from i equals 1 to n of x sub i."* `i` is the **index** — it counts through the values.

In code: `sum(x[i] for i in range(n))` or just `sum(x)`.

You'll see Σ in:

- The dot product: `Σ xᵢyᵢ`.
- Mean: `(1/n) Σ xᵢ`.
- Loss functions: `L = Σ loss(predᵢ, trueᵢ)`.
- Softmax: `e^(zᵢ) / Σⱼ e^(zⱼ)`.

### Products

`Π` (capital pi) means *"multiply these together."*

```
       n
       Π  xᵢ     means    x₁ × x₂ × x₃ × ... × xₙ
      i=1
```

In code: there's no built-in product, but `math.prod(x)` works (Python 3.8+).

Less common than Σ in ML. The biggest place it shows up is in joint probabilities: `P(x₁, x₂, ..., xₙ) = Π P(xᵢ)` when the variables are independent. Which is why log-probabilities are common — turning that product into a sum.

### Set notation

A **set** is an unordered collection of unique items. Written `{a, b, c}`.

```
∈      "element of"           x ∈ A         "x is in A"
∉      "not element of"
⊂ or ⊆ "subset of"            A ⊂ B         "A is a subset of B"
∪      "union"                A ∪ B         "everything in A or B"
∩      "intersection"         A ∩ B         "everything in both A and B"
∅      "empty set"
|A|    "size of A"            |{1,2,3}| = 3
ℝ      the real numbers
ℕ      the natural numbers (0, 1, 2, 3, ...)
ℤ      the integers (... -2, -1, 0, 1, 2 ...)
```

You'll see `x ∈ ℝᵈ` constantly in ML. It means *"x is a real-valued vector with d entries."*

### Other symbols

```
≈      approximately equal       π ≈ 3.14
≪      "much less than"          1e-6 ≪ 1
≫      "much greater than"       1e9 ≫ 100
→      "approaches" or "maps to" x → ∞, f: ℝ → ℝ
∀      "for all"                 ∀x ∈ ℝ
∃      "there exists"            ∃x such that x² = 2
∇      "gradient" (nabla)        ∇L      — covered in Ep 16
∂      "partial derivative"      ∂L/∂w   — covered in Eps 14-18
```

You're not expected to write proofs with these. You're expected to skim a paper, see `∀x ∈ ℝᵈ`, and not panic.

---

## 2.7 · Intervals

The set of all numbers between two endpoints.

```
[a, b]    closed interval         includes both a and b
(a, b)    open interval           excludes both endpoints
[a, b)    half-open               includes a, excludes b
(-∞, ∞)   all real numbers
```

Square brackets *include* the endpoint, round brackets *exclude*. Same convention as Python's `range(a, b)` — which is the half-open interval `[a, b)`.

You'll see intervals in probability (`P(X ∈ [0, 1])`) and optimization (`lr ∈ (0, 1)`).

---

## 2.8 · A small toolkit you can lean on

Memorize the *shape* of these — not the values.

### Algebra rules
```
(a + b)² = a² + 2ab + b²
(a - b)² = a² - 2ab + b²
(a + b)(a - b) = a² - b²
a² - b² = (a + b)(a - b)
```

### Exponent rules
```
x^a × x^b = x^(a+b)
x^a / x^b = x^(a-b)
(x^a)^b   = x^(a×b)
x^0       = 1
x^(-a)    = 1 / x^a
```

### Log rules
```
log(ab)   = log(a) + log(b)
log(a/b)  = log(a) - log(b)
log(a^n)  = n × log(a)
log(1)    = 0
log(e^x)  = x          (when base is e)
e^(log x) = x          (when base is e)
```

### Constants
```
π ≈ 3.14159...
e ≈ 2.71828...
√2 ≈ 1.414
log(10) ≈ 2.303        (natural log of 10)
log(2) ≈ 0.693         (natural log of 2)
```

---

## 2.9 · Do these before moving on

Convert ten random percentages to decimals and fractions. Then convert ten random decimals back. Five minutes. Should be boring. Boring is the goal.

Compute these in your head (or on paper, but not in a calculator):
   - `2^10` = ?
   - `log₁₀(1000)` = ?
   - `(-3) × (-4)` = ?
   - `1/4 + 1/2` = ?
   - `1.5e3 + 250` = ?
   - In `2 + 3 × 4`, what's the answer?
   - If `f(x) = x² + 1`, what's `f(-2)`?

Answers in the dropdown below. Try first. If any of those was genuinely hard, slow down and re-read the relevant section.

Then go watch [3Blue1Brown — Essence of Calculus, episode 1](https://www.youtube.com/watch?v=WUvTyaaNkzM). Fifteen minutes. You don't have to understand all of it. You're checking whether the vocabulary in this chapter lets you follow along. If it does, you're set for the foundations track.

<details>
<summary>Answers</summary>

- `2^10` = **1024**
- `log₁₀(1000)` = **3**
- `(-3) × (-4)` = **12**
- `1/4 + 1/2` = `1/4 + 2/4` = **3/4** (or 0.75)
- `1.5e3 + 250` = `1500 + 250` = **1750**
- `2 + 3 × 4` = `2 + 12` = **14**
- `f(-2)` = `(-2)² + 1` = `4 + 1` = **5**
</details>

---

## Where to next

→ [03-python-syntax-and-data.md](03-python-syntax-and-data.md) — Python syntax, every built-in datatype, every operator.

Or jump back to the [pre-foundations index](README.md).

---

## Further reading

- [Khan Academy — Algebra 1](https://www.khanacademy.org/math/algebra) — the gold standard, free.
- [3Blue1Brown — Essence of Calculus](https://www.3blue1brown.com/topics/calculus) — for after foundations. Visual, intuitive.
- [The math companion to deep learning](https://github.com/jermwatt/machine_learning_refined) — an open-access book that re-derives all the math you need.
- [w3schools Math](https://www.w3schools.com/python/python_math.asp) — Python's `math` module reference. Not a math tutorial, but useful when you want to compute something.
