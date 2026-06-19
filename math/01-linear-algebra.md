# 01 · Linear algebra

← back: [math README](README.md) · next: [02-calculus.md](02-calculus.md)

**Visual companions:** [What a vector actually is](https://siddhant-rajhans.github.io/ml-roadmap/vector.html) · [the 3D transformation engine](https://siddhant-rajhans.github.io/ml-roadmap/linear-algebra.html) · episodes 9–13 of the series.

Linear algebra is the language of data. Every dataset is a matrix, every embedding is a vector, every layer of a neural network is a matrix multiply. You don't need to compute an SVD by hand — NumPy does that. You need to *see* what these operations do to data, so that when a paper says "project onto the top-k singular directions," you picture it instead of panicking.

This chapter is a guided path, not a textbook. For each idea: the intuition, the ML payoff, and where to go deep. The deep part is mostly **3Blue1Brown's _Essence of Linear Algebra_** — watch it, it's the best thing ever made on this subject. Here we connect it to ML and give you problems to check yourself.

Assumes you're comfortable with the notation from [pre-foundations](../pre-foundations/02-math-zero.md) and [foundations](../foundations/01-math-refresh.md).

---

## 1.1 · Vectors are points and arrows and lists

A vector is three things at once, and fluency means switching between them without thinking:

- A **list of numbers**: `[2, 5, -1]`. This is how code sees it.
- A **point** in space: the location `(2, 5, -1)`.
- An **arrow** from the origin to that point: it has direction and length.

```
  list          point/arrow
 [3]                  •(3,2)
 [2]   ⇄            ↗
                  origin
```

In ML, a vector is how you represent *one thing*: one data point, one word embedding, one image flattened out. A 768-number vector is just a point in 768-dimensional space. You can't picture 768 dimensions, but every rule you learn in 2D and 3D still holds — that's the quiet miracle that makes this all work.

**Two operations define a vector space:** you can add vectors (tip to tail) and scale them (stretch/flip). That's it. Anything closed under those two operations is a vector space.

---

## 1.2 · Span, basis, independence

- **Span** — all the points you can reach by scaling and adding a set of vectors. One vector spans a line. Two non-parallel vectors span a plane.
- **Linearly independent** — none of the vectors is a combination of the others. No redundancy. Each one adds a new direction.
- **Basis** — a minimal set of independent vectors that spans the whole space. The coordinate axes are the obvious basis, but there are infinitely many.

Why it matters: **a basis is a coordinate system, and choosing a good one is half of ML.** PCA finds the basis where your data's variance lines up with the axes. An embedding *is* a learned basis where "meaning" becomes direction. When someone says "in the eigenbasis everything is diagonal," they mean: pick the right axes and a hard problem turns easy.

---

## 1.3 · Matrices are transformations

Here's the reframing that makes linear algebra click. A matrix isn't a grid of numbers — **it's a function that moves space.** Multiply a vector by a matrix and the vector lands somewhere new. The whole grid of space stretches, rotates, shears, or collapses, but lines stay lines and the origin stays put.

The columns of the matrix tell you exactly where the basis vectors land. That's the entire secret:

```
[2 0]   sends  x-axis → (2,0)   ... stretch x by 2
[0 3]   sends  y-axis → (0,3)   ... stretch y by 3
```

Play with [the transformation engine](https://siddhant-rajhans.github.io/ml-roadmap/linear-algebra.html) until this is physical — type a matrix, watch the point cloud move.

**Matrix multiplication is composition** — `AB` means "do B, then do A." That's why it isn't commutative: rotating then shearing ≠ shearing then rotating. And a neural network layer, `Wx + b`, is exactly this: transform the input by `W`, then shift by `b`.

---

## 1.4 · Inverse, rank, and collapse

The **inverse** `A⁻¹` undoes the transformation. But not every matrix has one — some transformations *destroy information* by squashing space into a lower dimension, and you can't un-squash.

- **Rank** — the number of dimensions the output still occupies. A 3×3 matrix of rank 2 has flattened 3D space onto a plane. Information was lost.
- **Null space** — the set of vectors that get sent to zero. A non-trivial null space means collapse, means no inverse.

This isn't abstract. **Low rank = redundancy = compressibility.** A low-rank weight matrix has fewer effective parameters; LoRA fine-tuning works precisely because the *update* to a giant weight matrix can be low-rank, so you train two tiny matrices instead of one huge one.

---

## 1.5 · The determinant

The determinant is one number that says how much a transformation **scales area (2D) or volume (3D)**.

```
det = 2   → areas double
det = 1   → area preserved (a pure rotation)
det = 0   → space collapsed to a lower dimension (no inverse!)
det < 0   → space got flipped (orientation reversed)
```

`det = 0` is the headline: it's the precise signal that a matrix is singular, rank-deficient, non-invertible — all the same fact wearing different names. (Episode 11 builds this from the area picture.)

---

## 1.6 · Eigenvectors and eigenvalues

Most vectors change direction when you apply a matrix. A few special ones don't — they only get stretched or squished, staying on their own line. Those are **eigenvectors**, and the stretch factor is the **eigenvalue**.

```
A v = λ v     "applying A to v just scales v by λ"
```

Eigenvectors are the transformation's *natural axes* — the directions it leaves alone. Find them and the transformation becomes pure stretching, no rotation to track.

The ML payoff is enormous:

- **PCA** is eigendecomposition of the covariance matrix. The top eigenvector is the direction of maximum variance — the single most informative axis in your data.
- **Spectral methods, PageRank, graph ML** all hinge on eigenvectors.
- The eigenvalues of the **Hessian** tell you the curvature of a loss landscape — why some directions train fast and others crawl.

(Episode 12.)

---

## 1.7 · SVD — the master decomposition

Eigendecomposition only works on square matrices. The **singular value decomposition** works on *any* matrix, and it's the most useful factorization in all of applied math:

```
A = U Σ Vᵀ
```

Read it geometrically, right to left: **every linear transformation is a rotation (Vᵀ), then a scaling along axes (Σ), then another rotation (U).** That's it. Any matrix, no matter how ugly, is just rotate–stretch–rotate.

The **singular values** in Σ (sorted big to small) measure how much each direction matters. Keep the top few and throw the rest away — that's low-rank approximation, and it powers:

- **Compression** (image, model) — most of a matrix's "energy" lives in a handful of singular values.
- **Recommender systems** — the classic Netflix-style latent-factor model is a truncated SVD.
- **PCA**, again — PCA is SVD of the centered data matrix.
- **Noise reduction** — small singular values are usually noise; drop them.

(Episode 13, the finale.) If you internalize one thing from this chapter, make it SVD = rotate, stretch, rotate.

---

## 1.8 · Do these before moving on

Try each, then check. NumPy is allowed for arithmetic — the point is whether you know *what to compute and why*.

1. A matrix has columns `(1, 0)` and `(1, 0)`. What's its rank, and does it have an inverse?
2. A 2D transformation has `det = 0`. What happened to space geometrically?
3. You run PCA and the top two eigenvalues are `[40, 38, 0.5, 0.3, ...]`. What does that tell you about reducing to 2 dimensions?
4. In `A = UΣVᵀ`, which part holds the "importance" of each direction, and how would you compress `A`?
5. Why is `AB ≠ BA` in general? Answer in terms of transformations.
6. A weight update in fine-tuning is low-rank. Why does that save parameters?

<details>
<summary>Answers</summary>

1. Both columns are the same direction, so **rank 1** (output is a line, not the plane). The columns are linearly dependent → **no inverse** (det = 0).
2. Space **collapsed onto a line (or a point)** — a whole dimension was flattened. The transformation is not invertible.
3. The first two directions hold almost all the variance (40 + 38 vs tiny rest), so **reducing to 2D loses almost nothing** — PCA to 2 components is well justified here.
4. **Σ** (the singular values) holds the importance. Compress by **keeping the top-k singular values/vectors and zeroing the rest** (truncated SVD).
5. Matrix multiplication is **function composition**, and order matters: "rotate then shear" lands somewhere different from "shear then rotate."
6. A low-rank matrix `ΔW = BA` factors a big `d×d` update into a `d×r` and `r×d` pair with `r ≪ d`, so you train `2dr` numbers instead of `d²`. That's LoRA.
</details>

---

## Where to next

→ [02-calculus.md](02-calculus.md) — derivatives, the chain rule, and how backprop falls out of them.

Or back to the [math index](README.md).

---

## Further reading

- [3Blue1Brown — Essence of Linear Algebra](https://www.3blue1brown.com/topics/linear-algebra) — watch the whole series. This is the canonical intuition.
- [Gilbert Strang — Linear Algebra (MIT 18.06)](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/) — the rigorous course, lectures free on OCW.
- [Mathematics for Machine Learning](https://mml-book.github.io/) — Part I, free PDF. ML-focused from the start.
- [immersive linear algebra](http://immersivemath.com/ila/) — a free book with fully interactive figures.
