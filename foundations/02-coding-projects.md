# 02 · Coding projects

← previous: [01-math-refresh.md](01-math-refresh.md) · next: [03-dev-tools-and-git.md](03-dev-tools-and-git.md)

Pre-foundations taught you the pieces: variables, types, `if`/`else`, loops, functions, lists and dicts, reading and writing files. This chapter makes you *build* with them.

There's a gap between "I understand a `for` loop" and "I can write a working program." The only bridge is writing working programs. So that's the whole chapter: three small projects, each one a complete thing you run from the terminal. No new syntax — if something here is unfamiliar, it's in [pre-foundations 03–05](../pre-foundations/03-python-syntax-and-data.md).

**Type every line yourself.** Don't copy-paste. Run it, watch it break, fix it. The bugs you create are the lesson. By the end you'll have three programs on your own GitHub (chapter 3 shows you how to put them there).

Each project starts minimal and grows. Get v1 running before you touch v2.

---

## Project 1 — CLI calculator

**The goal:** type `3 + 4`, get `7`. Keep going until you quit.

### v1 — one calculation

Start dead simple. Make a file `calc.py`:

```python
a = float(input("First number: "))
op = input("Operator (+ - * /): ")
b = float(input("Second number: "))

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
else:
    print("Unknown operator")
```

Run it: `python calc.py`. It works once, then exits. `float()` is doing quiet work here — turning the typed text `"3"` into the number `3.0` so the math works.

### v2 — loop until quit, survive bad input

A real tool doesn't die after one use, and doesn't crash when you fat-finger something.

```python
while True:
    raw = input("calc> ").strip()
    if raw in ("q", "quit", "exit"):
        break

    try:
        a_text, op, b_text = raw.split()
        a, b = float(a_text), float(b_text)
    except ValueError:
        print("Type it like:  3 + 4")
        continue

    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        if b == 0:
            print("Can't divide by zero.")
        else:
            print(a / b)
    else:
        print(f"Unknown operator: {op}")
```

Two new ideas earning their place. `raw.split()` breaks `"3 + 4"` into the list `["3", "+", "4"]`, which unpacks into three names at once. And `try`/`except` catches the crash when someone types `"hello"` — instead of a red traceback, they get a polite nudge. That `except ValueError` is the difference between a script and a tool.

### Stretch goals

- Replace the `if`/`elif` ladder with a dict that maps operators to functions:
  ```python
  import operator
  OPS = {"+": operator.add, "-": operator.sub,
         "*": operator.mul, "/": operator.truediv}
  ```
  Now the whole thing is `if op in OPS: print(OPS[op](a, b))`. This is **dispatch by dictionary**, and it's everywhere in real code — including how ML frameworks pick an optimizer or activation from a string name like `"adam"` or `"relu"`.
- Add `**` for powers and `%` for remainder.
- Keep a running history list and print it on `history`.

---

## Project 2 — Todo list that remembers

**The goal:** add tasks, list them, check them off — and have them still be there tomorrow. That last part means writing to a file.

This is the project that teaches **persistence**: data that outlives the program run. Every dataset you'll ever load is this same idea at scale.

### The whole thing

We'll store tasks as a list and save it to a JSON file. JSON is just text that looks like Python lists and dicts, which makes it the easiest format to save structured data. Make `todo.py`:

```python
import json
from pathlib import Path

TODO_FILE = Path("todos.json")

def load():
    if TODO_FILE.exists():
        return json.loads(TODO_FILE.read_text())
    return []

def save(todos):
    TODO_FILE.write_text(json.dumps(todos, indent=2))

def main():
    todos = load()
    print("Commands: list | add <task> | done <n> | quit")

    while True:
        cmd = input("todo> ").strip()

        if cmd == "list":
            if not todos:
                print("  (nothing yet)")
            for i, task in enumerate(todos):
                print(f"  {i}. {task}")

        elif cmd.startswith("add "):
            todos.append(cmd[4:])
            save(todos)
            print(f"  added: {cmd[4:]}")

        elif cmd.startswith("done "):
            idx = int(cmd[5:])
            removed = todos.pop(idx)
            save(todos)
            print(f"  done: {removed}")

        elif cmd in ("q", "quit"):
            break

        else:
            print("  Commands: list | add <task> | done <n> | quit")

if __name__ == "__main__":
    main()
```

Run it, add a couple tasks, quit, run it again. They're still there. That's the payoff — `load()` reads the file back on startup, `save()` writes it after every change.

A few things worth noticing:

- `Path("todos.json")` from `pathlib` is the modern way to handle files. `.exists()`, `.read_text()`, `.write_text()` are cleaner than the old `open()` dance.
- `json.dumps` turns your list into text; `json.loads` turns text back into a list. The `s` is for "string."
- `enumerate(todos)` hands you the index and the item together, so you can number the list.
- `if __name__ == "__main__":` means "only run `main()` when this file is run directly, not when it's imported." You'll see this guard at the bottom of nearly every Python script.

### Stretch goals

- It crashes on `done 99` or `done abc`. Wrap the index logic in `try`/`except (ValueError, IndexError)` and print a friendly message. (You did this pattern in project 1.)
- Add a `clear` command that empties the list.
- Store each task as a dict `{"text": ..., "done": False}` instead of a string, and a `check <n>` command that flips `done` without deleting. Now `list` can show `[x]` or `[ ]`. This is your first taste of modeling data as records — the shape every row in a dataset takes.

---

## Project 3 — Word counter

**The goal:** point it at any text file and get the most common words. This is the one that points straight at machine learning.

### The whole thing

Make `wordcount.py`:

```python
import sys
from pathlib import Path
from collections import Counter

def count_words(path, top_n=10):
    text = Path(path).read_text(encoding="utf-8").lower()
    words = text.split()

    # strip punctuation clinging to each word
    cleaned = [w.strip(".,!?;:\"'()[]{}") for w in words]
    cleaned = [w for w in cleaned if w]   # drop anything left empty

    counts = Counter(cleaned)
    return counts.most_common(top_n)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python wordcount.py <file> [top_n]")
        sys.exit(1)

    path = sys.argv[1]
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 10

    for word, count in count_words(path, n):
        print(f"{count:5d}  {word}")
```

Run it on any text file you have: `python wordcount.py somebook.txt 15`. (No text file handy? Run it on one of your own `.py` files — the results are funny.)

New pieces:

- `sys.argv` is the list of words you typed after `python`. `sys.argv[0]` is the script name, `sys.argv[1]` is the first argument. This is how every command-line tool — including every ML training script — reads its options.
- `Counter` from `collections` counts things for you. Feed it a list, it hands back a dict of item → count, and `.most_common(n)` sorts and slices in one call. Doing this by hand is a good exercise; reaching for `Counter` is what you'll actually do.
- `f"{count:5d}"` pads the number to 5 spaces so the columns line up. Small touch, big readability.

### Why this one matters

You just built the seed of natural language processing. Counting word frequencies is the first step in:

- **Bag-of-words** — representing a document as its word counts. One of the oldest text-classification features.
- **Building a vocabulary** — the set of words a model knows, ranked by frequency, is exactly `Counter.most_common()`.
- **Tokenization** — splitting text into pieces is `text.split()` grown up.

When you later load a dataset and a tutorial says "build the vocab," you'll recognize it. You wrote it here.

### Stretch goals

- Add a **stopword** filter: skip common words like `the`, `a`, `and`, `of` so the interesting words rise to the top. Keep a `set` of stopwords and `if w not in STOP`.
- Count two-word phrases (bigrams) instead of single words: `zip(cleaned, cleaned[1:])`.
- Make it read from standard input so you can pipe into it: `cat file.txt | python wordcount.py`.

---

## Do these before moving on

You're done with this chapter when:

- [ ] All three programs run without crashing on normal input.
- [ ] The calculator survives garbage input without a traceback.
- [ ] The todo list still has your tasks after you quit and restart.
- [ ] The word counter runs on a real text file and the top words make sense.
- [ ] You can explain, out loud, what `try`/`except`, `json.dumps`, and `sys.argv` each do.

If any program only "works" because you copied it — delete it and rewrite it from a blank file. You'll know you've got it when you can.

---

## Where to next

→ [03-dev-tools-and-git.md](03-dev-tools-and-git.md) — the terminal, Git, and getting these three projects onto your own GitHub.

Or jump back to the [foundations index](README.md).

---

## Further reading

- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) — free online, project-driven, perfect at this level.
- [Python docs — `pathlib`](https://docs.python.org/3/library/pathlib.html) and [`collections.Counter`](https://docs.python.org/3/library/collections.html#collections.Counter) — the two modules these projects lean on.
- [Real Python — Command-Line Interfaces](https://realpython.com/command-line-interfaces-python-argparse/) — when your `sys.argv` parsing outgrows itself, `argparse` is next.
- [w3schools Python](https://www.w3schools.com/python/) — the tighter reference, with a "Try It" button on every page.
