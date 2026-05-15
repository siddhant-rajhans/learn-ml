# Python & DSA · Practice Playground

> Type, run, see — no setup, no signup.
> Real Python in your browser. Real algorithms, animated.

A self-contained learning playground that runs entirely in your browser. Clone the repo, open one HTML file, start coding. No installs, no terminals, no configs.

## What's inside

- **Real Python** via [Pyodide](https://pyodide.org) — CPython compiled to WebAssembly. NumPy, Pandas, and most of the scientific stack work.
- **A code editor** (Ace) with syntax highlighting, auto-indent, and `Cmd/Ctrl + Enter` to run.
- **A curriculum** of bite-sized lessons — from `print("Hello")` to binary search — each ~3–8 minutes.
- **Live algorithm visualizations**. When you run binary search, you *watch* the search narrow. Sort algorithms animate their swaps. DSA stops being a wall of code.
- **Progress tracking** in `localStorage` — your completion state persists across sessions.

## How to use

### Online (anyone)

Browse to the GitHub Pages URL once it's live:

> https://siddhant-rajhans.github.io/learn-ml/prog/python-and-dsa/

### Locally (recommended for practice)

```bash
git clone https://github.com/siddhant-rajhans/learn-ml.git
cd learn-ml/prog/python-and-dsa
python server.py
# then open http://localhost:8000
```

That's it. `server.py` is a tiny script (no dependencies) that sends the right cross-origin headers so Pyodide can use SharedArrayBuffer for the fast load path — meaningfully snappier than a plain `python -m http.server`.

On first load, Pyodide downloads ~10 MB of WASM Python from CDN. After that your browser caches it; subsequent loads are instant.

If the load hangs for more than a minute, the page shows an actionable error pointing you back here — usually means the CDN is unreachable or you opened the file directly without a server.

## Curriculum

10 lessons to start. More land over time.

### Foundations
1. **Hello, World** — print, comments, your first program
2. **Variables** — names, assignment, types
3. **Numbers & Math** — `+ - * / // % **`, the math you'll actually use
4. **Strings** — quotes, concatenation, f-strings
5. **If / else** — making decisions
6. **Loops** — `for` over `range`, over lists
7. **Functions** — `def`, parameters, return values

### Data structures
8. **Lists** — create, index, slice, append
9. **Dictionaries** — key–value, lookups, iteration

### Algorithms (with live visualizations)
10. **Binary search** — divide and conquer, watch the search space shrink

## Keyboard shortcuts

| Shortcut | What it does |
|---|---|
| `Cmd / Ctrl + Enter` | Run the current code |
| `J` / `K` | Next / previous lesson |
| `Cmd / Ctrl + .` | Reset code to starter |
| `?` | Show all shortcuts |

## What's coming

These ship as the channel publishes more episodes. Tracked in [issues](https://github.com/siddhant-rajhans/learn-ml/issues):

- More foundations: sets, tuples, comprehensions, recursion, classes
- More DSA: linear search, bubble sort, merge sort, quick sort, BFS, DFS, dynamic programming
- More visualizations: every algorithm becomes animated
- Exercise sets — guided problems with hint reveals + solution checks
- Cheat sheets — one-page reference per chapter

## Why this exists

This is the **`prog/python` corner** of [learn-ml](https://github.com/siddhant-rajhans/learn-ml) — the curriculum companion to [The Map](https://siddhant-rajhans.github.io/ml-roadmap/) and the Siddhant Rajhans YouTube channel(s).

Most "learn Python" sites assume you can install Python, configure a terminal, and survive your first error message. Most beginners can't, yet — and shouldn't have to before they've felt the joy of typing `print("hi")` and seeing it work. This is the playground that meets them where they are.

## License

[MIT](../../LICENSE) — fork, embed, teach with it, ship it inside your bootcamp. Attribution appreciated, not required.
