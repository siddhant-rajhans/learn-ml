# Foundations — True Zero

> *"Stop being afraid of math notation. Stop being afraid of a terminal."*

This isn't a category in the main map. It's the **entry door** for anyone whose floor isn't yet high-school math + basic Python. Once you can answer "yes" to the skip checks below, you don't need this folder — head to [`math/`](../math/).

> **Newer to this than that?** If you've never opened a terminal, never written `print("hello")`, or it's been a decade since you saw `Σ` — start at [`../pre-foundations/`](../pre-foundations/) instead. Foundations assumes you have *that* layer already.

## Skip this folder if…

You can answer **all** of these without looking anything up:

- Compute $\frac{d}{dx}\left[e^{2x}\sin(x)\right]$ on paper.
- Read a CSV in Python, do a basic plot, and push to git in under 10 minutes.
- Solve a quadratic equation.
- Read $\log$ and $e^x$ expressions without breaking stride.
- `cd` into a directory and run a script.

If any of those is shaky, this folder.

## What you'll learn

```mermaid
flowchart LR
    A[Arithmetic Intuition] --> B[Algebra & Functions]
    B --> C[Trig & Geometry]
    B --> D[Logs & Exponents]
    A --> E[Sets & Logic]

    F[What's a Computer] --> G[Terminal Navigation]
    G --> H[Editor (VS Code)]
    H --> I[Git Basics]

    J[Python: Variables] --> K[Control Flow]
    K --> L[Functions & Scope]
    L --> M[Lists, Dicts, Tuples]
    M --> N[Three Mini Projects]
```

## What's here

Three chapters, one per track. Each is short explainers plus the best external resources plus exercises — read here, practice with the linked material, check yourself at the end.

| # | File | Track | Time |
|---|------|-------|------|
| 1 | [01-math-refresh.md](01-math-refresh.md) | Solving, the function zoo, light trig, counting for probability | 6–10 hrs |
| 2 | [02-coding-projects.md](02-coding-projects.md) | Three real programs that turn syntax into skill | 6–10 hrs |
| 3 | [03-dev-tools-and-git.md](03-dev-tools-and-git.md) | Terminal fluency, Git, GitHub, VS Code | 4–6 hrs |

> **On overlap with pre-foundations:** if you came up through [`../pre-foundations/`](../pre-foundations/), you already have basic arithmetic, the symbols, and Python syntax. Foundations doesn't repeat those — chapter 1 picks up at *using* the math, and chapter 2 jumps straight to building programs. Skim what you know, slow down where it's new.

## Time budget

6–10 weeks at ~10 hrs/week. Closer to 4 weeks if one of the three tracks (math, coding, tools) is already comfortable.

## Track 1 — Math refresh (4–6 weeks)

→ Chapter: [01-math-refresh.md](01-math-refresh.md)

- **Arithmetic intuition** — place value, fractions, percent, ratios. The boring kind that creeps back later as "why is my softmax giving NaN."
- **Algebra** — equations, inequalities, factoring.
- **Functions** — linear, quadratic, polynomial, rational. The mental model: input → black box → output.
- **Exponentials and logarithms** — *especially* logs. You'll see them in every loss function.
- **Trigonometry** — sin/cos/tan, unit circle. Light touch.
- **Sets, logic, basic combinatorics** — for probability later.

## Track 2 — Coding from zero (4 weeks)

→ Chapter: [02-coding-projects.md](02-coding-projects.md) (the syntax below is in [pre-foundations](../pre-foundations/); the chapter focuses on building with it)

- Install Python (use `uv` — modern, fast), VS Code, set up your terminal.
- Variables, types, expressions.
- Control flow (if/else, loops). When to use which loop.
- Functions and scope. Why functions exist.
- Lists, dicts, tuples, sets — the four containers; pick the right one.
- Reading and writing files.
- **3 mini projects** to consolidate:
  1. CLI calculator
  2. Todo list with file persistence
  3. Word counter (any text file, top-N words)

## Track 3 — Dev tools (1–2 weeks)

→ Chapter: [03-dev-tools-and-git.md](03-dev-tools-and-git.md)

- Terminal navigation (cd, ls, mkdir, mv, cp).
- Git basics (init, add, commit, push). Branches can wait.
- GitHub account → first repo.
- VS Code: the 10 keybindings worth learning.

## Companion video

See the [interactive roadmap](https://siddhant-rajhans.github.io/ml-roadmap/roadmap.html) → **Foundations** satellite node for the visual entry point. Companion episode(s) will be linked from the detail panel as they ship.

## Exit criteria

You move on to [`math/`](../math/) when:

- [ ] Solve a quadratic equation on paper.
- [ ] Read an exponent or log expression without breaking stride.
- [ ] Write a Python function that takes a list of dicts and returns a transformed list of dicts.
- [ ] Pushed at least one of the 3 mini projects to your own GitHub.
- [ ] `cd` and `ls` without thinking.

All checked? Welcome to the map.
