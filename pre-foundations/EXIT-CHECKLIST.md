# Are you done with pre-foundations?

← back to [pre-foundations index](README.md)

No certificate. No quiz. Just an honest checklist.

Read each box. If you can do the thing without looking it up, check it. If you'd need to peek, leave it blank and go back to the chapter that covers it. Foundations gets harder if any of this isn't reflexive yet.

---

## Computer literacy (chapter 01)

- [ ] You can open a terminal on your machine without thinking about which app to open.
- [ ] You know what your current working directory is at any moment (you can run `pwd` and not be surprised).
- [ ] You can `cd` into a folder, `ls` to see what's there, `mkdir` a new folder, `touch` a new file (or your editor equivalent), and `rm` a file.
- [ ] You can run `python --version` and see what's installed.
- [ ] You can run `python script.py` from the terminal and have it actually find your script.
- [ ] You know the difference between an absolute and a relative path.
- [ ] You have VS Code (or another text editor) installed, with the integrated terminal working.
- [ ] You have a GitHub account.

---

## Math zero (chapter 02)

- [ ] You can compute `0.1 + 0.2` and know why the answer isn't exactly `0.3`.
- [ ] You can read `1.5e-6` and know it's "1.5 times ten to the negative six" — a very small number.
- [ ] You remember PEMDAS without looking it up — `2 + 3 × 4` is 14.
- [ ] You can read `log(x)` and `e^x` without panic.
- [ ] You can read `Σᵢ xᵢ` and know it means "sum of all the xᵢ values."
- [ ] You can read `x ∈ ℝᵈ` and know it means "x is a d-dimensional real-valued vector."
- [ ] You can sketch the shape of `y = x²`, `y = e^x`, `y = log(x)`, `y = 1/x` from memory.
- [ ] If `f(x) = 2x + 3`, you can compute `f(-2)` in your head.

---

## Python syntax & data (chapter 03)

- [ ] You can list Python's main built-in datatypes without looking them up (int, float, str, bool, list, tuple, set, dict, None).
- [ ] You know what `type(x)` does and what `isinstance(x, int)` does.
- [ ] You can convert between types: `int("42")`, `str(3.14)`, `list("abc")`, `bool([])`.
- [ ] You know that `=` is assignment and `==` is equality.
- [ ] You know what falsy values are: `None`, `0`, `0.0`, `""`, `[]`, `{}`, `set()`.
- [ ] You know the difference between `/` (always float) and `//` (integer division) and `%` (modulo).
- [ ] You can use f-strings: `f"x is {x:.2f}"`.
- [ ] You can read these errors and not panic: `SyntaxError`, `NameError`, `TypeError`, `ValueError`, `IndexError`, `KeyError`.

---

## Flow & collections (chapter 04)

- [ ] You can write `if` / `elif` / `else` and know that the colon and indentation matter.
- [ ] You can use `for` with `range()`, `enumerate()`, and `zip()`.
- [ ] You know when to use `while` vs `for`.
- [ ] You know `break`, `continue`, and what `pass` is for.
- [ ] You can pick the right container — given a problem, you know whether to reach for `list`, `tuple`, `set`, or `dict`.
- [ ] You can write a basic list comprehension: `[x * 2 for x in nums if x > 0]`.
- [ ] You know that copying a list takes `.copy()` or `list(other)` — that `b = a` doesn't copy.
- [ ] You can iterate a dict with `for key, value in d.items():`.

---

## Functions, modules, files (chapter 05)

- [ ] You can define a function with `def`, take parameters, return a value.
- [ ] You can give a parameter a default value.
- [ ] You know what `*args` and `**kwargs` mean when you see them.
- [ ] You can `import` a module and `from module import thing`.
- [ ] You can read code that uses `import numpy as np`.
- [ ] You can install a package: `pip install requests` (or `uv pip install`).
- [ ] You know what a virtual environment is and why it exists.
- [ ] You can open a file with `with open(...) as f:` — read or write.

---

## Everyday essentials (chapter 06)

- [ ] You can wrap risky code in `try / except SpecificError:`.
- [ ] You know what JSON looks like and how to read/write it with the `json` module.
- [ ] You know how to get the current time with `datetime.now()`.
- [ ] You know that `math.sqrt`, `math.log`, and `random.choice` exist (you don't have to memorize the full APIs).
- [ ] You recognize a regex (`r"\d+"`) and know it's a pattern, not garbage.
- [ ] You know how to read environment variables with `os.environ`.

---

## The honest "can you do this?" test

Without looking anything up, write a small Python program that:

1. Asks the user for a filename.
2. Reads that file line by line.
3. For each line, splits it into words.
4. Builds a dictionary: word → how many times that word appeared across the whole file.
5. Prints the top 10 most common words.
6. Handles the case where the file doesn't exist (gracefully — print an error and exit).

If you can write this in ~20 lines without help, **you're done with pre-foundations.** Every concept needed for it is in chapters 03 through 06.

If you can't, that's your study plan: go back to whichever step you got stuck on.

<details>
<summary>One working solution (peek only after you've tried)</summary>

```python
import sys

filename = input("Filename: ")

try:
    with open(filename) as f:
        text = f.read()
except FileNotFoundError:
    print(f"No file: {filename}")
    sys.exit(1)

counts = {}
for word in text.split():
    word = word.lower().strip(".,!?;:\"'()")
    if word:
        counts[word] = counts.get(word, 0) + 1

top = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)

for word, count in top[:10]:
    print(f"{count:4}  {word}")
```

Other solutions exist (using `collections.Counter`, regex for splitting, etc.). What matters is that the structure makes sense to you. If you can read the above and understand every line, you're set.
</details>

---

## What's next

You can go a few directions from here.

The path most people take: [`../foundations/`](../foundations/) for the math refresh (logs, trig, set notation), git fluency, and three small projects. Then [`../paths/`](../paths/) to pick a track — Literacy, Builder, or Researcher.

Or keep practicing in [`../prog/python-and-dsa/`](../prog/python-and-dsa/). 34 runnable lessons including the 15 Pre-foundations ones you've already seen. The other 19 walk through data structures, search algorithms with live animations, and a working k-NN classifier.

That's the whole curriculum from here. Pick something and start.
