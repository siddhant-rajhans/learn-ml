# Pre-Foundations — *True Zero*

> *"Before the foundation, the ground."*

This folder is for people whose floor isn't yet **"comfortable with a computer + remembers middle-school math."** Once you can answer the [exit checklist](EXIT-CHECKLIST.md) without help, you graduate to [`../foundations/`](../foundations/).

## Who this is for

If any of these describes you, **start here**:

- You've never opened a terminal.
- You're not sure what a "file path" actually is.
- The last time you did long division was a while ago, and you've never seen `Σ` or `∈` in writing.
- You've never written `print("hello")` in any language.
- You've heard the words "ML" and "Python" and want a calm, walked-through ramp instead of a course that throws you at NumPy in week one.

If those *don't* describe you — skip straight to [`../foundations/`](../foundations/) (math refresh + Python from scratch + git) or to your chosen [`../paths/`](../paths/) entry point.

## What's in here

| # | File | What it covers | Time |
|---|------|----------------|------|
| 1 | [01-computer-literacy.md](01-computer-literacy.md) | Files & folders & paths. The terminal. Installing Python. Editors. Browser dev tools. Keyboard literacy. | 3–5 hrs |
| 2 | [02-math-zero.md](02-math-zero.md) | Arithmetic that creeps back into ML. Fractions, decimals, percents, scientific notation. Order of operations. Negative numbers. Exponents. Basic algebra. Functions. Coordinate plane. Notation you'll meet later (Σ, Π, ∈, ⊂). | 5–8 hrs |
| 3 | [03-python-syntax-and-data.md](03-python-syntax-and-data.md) | Python syntax rules. Variables. **All** the built-in datatypes (int, float, complex, str, bool, list, tuple, set, dict, NoneType). Casting. **Every** operator category. `input()` / `print()`. String formatting. | 6–10 hrs |
| 4 | [04-flow-and-collections.md](04-flow-and-collections.md) | `if` / `elif` / `else`. `while` and `for`. `range`, `enumerate`, `zip`. `break` / `continue`. Lists, tuples, sets, dictionaries — operations + when to use which + comprehensions. | 6–10 hrs |
| 5 | [05-functions-modules-files.md](05-functions-modules-files.md) | `def`, parameters, `*args` / `**kwargs`, return. Scope. `lambda`. Modules. `import`. `pip install`. Virtual environments. Files — open / read / write / `with`. | 5–8 hrs |
| 6 | [06-everyday-essentials.md](06-everyday-essentials.md) | `try` / `except` and the common exceptions. JSON. Dates & time. `math` and `random` modules. Regex (intro). Environment variables. Command-line arguments. | 4–6 hrs |
| ✓ | [EXIT-CHECKLIST.md](EXIT-CHECKLIST.md) | The honest test. If you check every box, you're done with pre-foundations. | 1 hr to self-test |

**Total time:** 30–48 hours of focused work. About 4–6 weeks at 8 hrs/week. Faster if you've coded in *anything* before — even spreadsheet formulas count.

## How to use this folder

1. **Read in order.** Each file assumes the previous ones. The structure compounds.
2. **Type every code example.** Don't copy-paste. Typing forces you to notice the parentheses, colons, and indentation. The errors you make while typing are the curriculum.
3. **Use the playground.** [`../prog/python-and-dsa/`](../prog/python-and-dsa/) runs Python in your browser — no installs. The first chapter, **"Pre-foundations"**, has 15 runnable lessons that mirror these chapters one-for-one. Open it on a second tab while you read.
4. **Read w3schools alongside.** [w3schools Python tutorial](https://www.w3schools.com/python/) has a "Try It Yourself" editor for every concept. Tighter examples than this folder, no commentary. Use it as a reference card.
5. **Don't memorize — recognize.** You're building familiarity, not knowledge. The goal is *"I've seen this word, I know roughly what it does"* — not *"I can write it from memory."* The recall comes later, from doing the foundations and prog tracks.

## Why we made this

The original `foundations/` folder said *"6–10 weeks at 10 hrs/week, refresh math + Python + git."* That's correct for the median ML-curious adult who took some math in college and once installed something.

It's not correct for the person who literally just decided to learn ML and has never opened a code editor. They need the layer below — what's a `.py` file? Why does pressing Enter in a terminal do something different than pressing Enter in a text document? What does it mean when a tutorial says *"open a terminal and run `python script.py`"*? That layer is this folder.

We don't want to lose that audience. ML doesn't have a citizenship test — anyone who wants in should get in.

## What's NOT in here

These belong in `foundations/` or later, not pre-foundations:

- **Calculus, linear algebra, probability** — covered in [`../foundations/`](../foundations/) (refresh) and [`../math/`](../math/) (depth).
- **Object-oriented programming, decorators, generators** — covered in [`../prog/`](../prog/) (Python Mastery section).
- **NumPy / Pandas / PyTorch** — covered in [`../prog/`](../prog/).
- **Git in depth** — basics get a mention in 01-computer-literacy.md; the workflow is in [`../foundations/`](../foundations/).
- **Data structures + algorithms** — there's a runnable playground at [`../prog/python-and-dsa/`](../prog/python-and-dsa/). Pre-foundations only gives you the conceptual basics of lists/dicts/sets/tuples.

## After you finish

You'll be ready for [`../foundations/`](../foundations/) — which covers the math refresh you might still need (algebra fluency, logs/exponents, trig, sets/logic for probability), gets you fluent with git, and puts you through three small Python projects.

After foundations, you pick a [`../paths/`](../paths/) entry — Literacy, Builder, or Researcher — and start building.

Welcome. Take your time.
