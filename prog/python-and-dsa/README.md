# Python & DSA · Practice Playground

> Type, run, see — no setup, no signup.
> Real Python in your browser. Real algorithms, animated.

A self-contained learning playground that runs entirely in your browser. Clone the repo, open one HTML file, start coding. No installs, no terminals, no configs.

## What's inside

- **Python in the browser** via [Skulpt](https://skulpt.org) — a pure-JavaScript Python interpreter. ~500 KB, vendored locally, zero CDN dependency.
- **A real code editor** (Ace) with syntax highlighting, auto-indent, and `Cmd/Ctrl + Enter` to run.
- **40 lessons across 9 chapters** — from the true-zero pre-foundations (datatypes, casting, operators, comprehensions) through a k-NN classifier on iris, then on to animated sorting, recursion, and graph traversal. Each ~3–12 minutes.
- **Live algorithm visualizations.** Binary vs linear search; bubble vs quick sort (bars sized by value, every comparison and swap lit up); the recursion call stack growing and unwinding; BFS vs DFS exploring a graph with a live queue/stack panel. Every algorithm drives its own animation from the Python you actually run.
- **A canvas-based `plt`** shim for plotting — scatter, line, bar, all rendered inline.
- **A pure-Python `np`** shim so `import np` works for arrays, broadcasting, and the operations you'll meet again in real NumPy.
- **A vendored `iris.csv`** so `open('iris.csv')` works inside the playground for the dataset / classifier lessons.
- **Progress tracking** in `localStorage` — your completion state persists across sessions.

## How to use

### Online (anyone)

> https://siddhant-rajhans.github.io/learn-ml/prog/python-and-dsa/

### Locally (recommended for practice)

```bash
git clone https://github.com/siddhant-rajhans/learn-ml.git
cd learn-ml/prog/python-and-dsa
python server.py
# then open http://localhost:8000
```

`server.py` is a tiny dependency-free HTTP server. Skulpt, Ace, and every asset live inside `vendor/`, so the playground works fully offline after the first clone — no CDN, no internet, no install dance, no `pip` anything.

## Curriculum

40 lessons across 9 chapters. Each one self-contained — open it, hit Run, edit, run again.

### Pre-foundations *(new)*

Runnable companions to the markdown chapters in [`../../pre-foundations/`](../../pre-foundations/). For people with no Python background — the layer below "Foundations."

0. **Welcome** — the rhythm of run, change, run again
1. **Variables, formally** — names, assignment, reassignment, swap
2. **The datatype zoo** — int / float / str / bool / list / tuple / set / dict / None side by side, with `type()`
3. **Truthy & falsy** — what counts as True in an `if` (and what doesn't)
4. **Casting between types** — `int()`, `float()`, `str()`, `list()`, `set()` for dedup
5. **Math operators with surprises** — `/` always returns float, `//` floors toward -∞, `**` is right-associative
6. **Comparisons & logical operators** — chained comparisons, short-circuit `and` / `or`
7. **Strings — indexing & slicing** — `s[0]`, `s[-1]`, `s[::-1]`, `.split()`, `.join()`
8. **f-strings** — width, alignment, decimals, padding, percent, thousands separator
9. **Lists** — append/pop/sort + the "b = a doesn't copy" gotcha
10. **List comprehensions** — `[x**2 for x in range(10) if x % 2 == 0]`
11. **Dictionaries** — `.get(key, default)`, `.items()`, the counter pattern
12. **try / except** — catching `ValueError`, `KeyError`, `ZeroDivisionError`
13. **A 20-line program that uses everything** — word frequency counter, the EXIT-CHECKLIST graduation exercise
14. **You're ready** — what to do next

### Foundations

1. **Hello, World** — `print`, comments, your first program
2. **Variables** — names, types, your first vector
3. **Numbers & Math** — operators, plus a tiny dot product
4. **Strings** — quotes, concatenation, f-strings, slicing
5. **If / else** — a confidence score becomes a classifier label
6. **Loops** — `for` over `range`, plus your first `mean`
7. **Functions** — `def`, parameters, return values. ReLU and `dot_product` as your first ML functions.

### Data structures

8. **Lists** — a row of pixel brightnesses
9. **Dictionaries** — word → embedding lookup

### Algorithms (with live visualizations)

10. **Binary search** — divide and conquer, two checks to find 23 in a sorted list of 16
11. **Linear search** — the naive baseline, marching one position at a time. Same 16 numbers, shuffled. Fifteen checks. Visual contrast with binary.

### Python idioms

12. **Tuples** — shape tuples, unpacking, immutability
13. **List & dict comprehensions** — the pythonic ML idiom
14. **enumerate & zip** — the training-loop pattern

### Real ML

15. **NumPy** — `array`, broadcasting, `shape`, `sum / mean / max`, `dot`, `zeros / ones / arange` (via teaching shim)
16. **Load a dataset** — parse the vendored `iris.csv` with `open()` + comprehensions
17. **When things break** — `try / except`, specific exception types, the per-row pattern for surviving messy CSVs
18. **Plotting** — `scatter`, `plot`, `bar` rendered to canvas (via teaching shim)
19. **Your first classifier** — k-NN on iris, ~95% accuracy, ~30 lines of plain Python

### Sorting (animated)

20. **Bubble sort** — O(n²) compare-and-swap; the biggest value bubbles to the end each pass
21. **Quick sort** — O(n log n) divide-and-conquer with a live gold pivot and partitions

### Recursion (call-stack viz)

22. **Recursion — the call stack** — factorial; frames push down to the base case, then unwind
23. **Recursion that branches** — fibonacci; the stack pulses, and the repeated work motivates memoization

### Graphs (animated traversal)

24. **Breadth-first search** — a FIFO queue explores ring by ring (the reason BFS finds shortest paths)
25. **Depth-first search** — a LIFO stack dives deep first; same graph, a completely different journey

## Keyboard shortcuts

| Shortcut | What it does |
|---|---|
| `Cmd / Ctrl + Enter` | Run the current code |
| `J` / `K` | Next / previous lesson |
| `Cmd / Ctrl + .` | Reset code to starter |
| `?` | Show all shortcuts |

## A note on the shims

Running real Python in the browser used to mean downloading ~10 MB of compiled CPython (Pyodide) on every visit. Skulpt is 500 KB and starts instantly — but the trade-off is that the heavyweight scientific libraries (NumPy, Pandas, Matplotlib) don't exist in Skulpt by default.

To preserve the muscle memory beginners actually need, the playground ships two small teaching modules:

- A pure-Python **`np`** that mirrors the NumPy API for `array`, `shape`, `sum`, `mean`, `max`, `dot`, `zeros`, `ones`, `arange`, and element-wise math / broadcasting on 1-D and 2-D arrays.
- A canvas-based **`plt`** that mirrors Matplotlib for `figure`, `title`, `xlabel`, `ylabel`, `plot`, `scatter`, `bar`, `legend`, `show`.

Lessons that use the shims flag it at the top. Your code transfers unmodified to real NumPy / Matplotlib the moment you `pip install` them.

## What's coming

Tracked in [issues](https://github.com/siddhant-rajhans/learn-ml/issues). The short list:

- Merge sort and heap sort — animated, alongside the existing bubble & quick
- Dynamic programming — memoized Fibonacci, then the classic DP grid
- Classes (`nn.Module` shape), exception handling, file-I/O patterns
- Exercise sets per chapter with hint reveals + solution checks
- Per-chapter cheat sheets

## Why this exists

This is the **`prog/python` corner** of [learn-ml](https://github.com/siddhant-rajhans/learn-ml) — the curriculum companion to [The Map](https://siddhant-rajhans.github.io/ml-roadmap/) and the [Siddhant Rajhans](https://siddhant-rajhans.github.io/) YouTube channel.

Most "learn Python" sites assume you can install Python, configure a terminal, and survive your first error message. Most beginners can't, yet — and shouldn't have to before they've felt the joy of typing `print("hi")` and seeing it work. This is the playground that meets them where they are.

## License

[MIT](../../LICENSE) — fork, embed, teach with it, ship it inside your bootcamp. Attribution appreciated, not required.
