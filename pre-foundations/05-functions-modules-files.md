# 05 · Functions, modules, files

← previous: [04-flow-and-collections.md](04-flow-and-collections.md) · next: [06-everyday-essentials.md](06-everyday-essentials.md)

A program is a few functions calling each other.

A library is a file full of functions you can `import` into your program.

A real project has some files of your own functions, some libraries installed from PyPI into a virtual environment, and some files it reads from and writes to.

This chapter is those three things.

---

## 5.1 · Functions

A function is a named block of code that takes inputs and (usually) returns an output. The single most important building block of any program.

### The basic form

```python
def greet(name):
    return f"Hello, {name}"

print(greet("Sid"))         # Hello, Sid
print(greet("Alex"))        # Hello, Alex
```

Pieces:

- `def` — keyword that starts a function definition.
- `greet` — the function's name. Same naming rules as variables.
- `(name)` — the **parameters** (sometimes called arguments). Comma-separated.
- `:` — the colon that opens the function's body.
- Indented body — what the function does.
- `return` — what the function gives back to the caller. Optional — if you don't `return`, the function returns `None`.

### Multiple parameters

```python
def add(a, b):
    return a + b

result = add(3, 4)          # 7
```

### Default values

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}"

greet("Sid")                          # "Hello, Sid"
greet("Sid", greeting="Hi")           # "Hi, Sid"
greet("Sid", "Hi")                    # "Hi, Sid" (positional still works)
```

Parameters with defaults must come *after* parameters without:

```python
def f(a, b=2): ...        # OK
def f(a=1, b): ...        # SyntaxError
```

### Keyword arguments

When calling, you can pass arguments by name. Order doesn't matter:

```python
def make_user(name, age, city):
    return {"name": name, "age": age, "city": city}

# positional
make_user("Sid", 30, "Hoboken")

# keyword — clearer, especially for many args
make_user(name="Sid", age=30, city="Hoboken")

# mix — positional first, then keyword
make_user("Sid", age=30, city="Hoboken")
```

For functions with many parameters, keyword arguments are much more readable. PyTorch and most ML libraries use them extensively.

### Returning multiple values

```python
def stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

lo, hi, avg = stats([1, 2, 3, 4, 5])    # 1, 5, 3.0
```

Under the hood, you're returning a tuple and unpacking it on the way out. Both `return min, max, avg` and `return (min, max, avg)` do the same thing.

### `*args` and `**kwargs`

When you want a function to accept *any* number of arguments:

```python
def sum_all(*args):
    return sum(args)             # args is a tuple

sum_all(1, 2, 3)                 # 6
sum_all(1, 2, 3, 4, 5)           # 15
```

`*args` collects extra positional arguments into a tuple.

```python
def make_config(**kwargs):
    return kwargs                # kwargs is a dict

make_config(lr=0.01, epochs=100)
# {"lr": 0.01, "epochs": 100}
```

`**kwargs` collects extra keyword arguments into a dict.

You can combine them:

```python
def f(required, default=10, *args, **kwargs):
    ...
```

`*args` and `**kwargs` are common in ML library wrappers — a function that forwards extra args to some inner function without caring what they are.

### Scope

Variables defined inside a function are **local** — they only exist inside the function.

```python
def f():
    x = 5
    return x

f()                # 5
print(x)           # NameError — x is not defined outside f
```

Variables defined outside a function are **global** — accessible everywhere:

```python
PI = 3.14159

def area(r):
    return PI * r ** 2       # can READ PI

area(5)                       # 78.53975
```

But you can't *write* a global from inside a function unless you use the `global` keyword:

```python
counter = 0

def increment():
    counter += 1              # UnboundLocalError — Python thinks counter is local
```

The fix:

```python
counter = 0

def increment():
    global counter            # tell Python: "I mean the global counter"
    counter += 1
```

**Avoid `global` when you can.** Better to return a value and let the caller update.

```python
def increment(c):
    return c + 1

counter = increment(counter)
```

### Early return for cleaner code

Instead of nesting everything inside `if`s, return early when something is wrong:

```python
# nested — works but harder to read
def process(data):
    if data is not None:
        if len(data) > 0:
            # ... real work happens here, indented twice
            return result
        else:
            return None
    else:
        return None

# flat — early returns
def process(data):
    if data is None:
        return None
    if len(data) == 0:
        return None
    # ... real work happens here, no extra indentation
    return result
```

The flat version is easier to read. Use it.

---

## 5.2 · `lambda` — anonymous functions

A one-line, throwaway function:

```python
square = lambda x: x ** 2
square(5)                       # 25
```

Same as:

```python
def square(x):
    return x ** 2
```

Lambdas are for places where you need a quick function inline and naming it would be overkill:

```python
words = ["banana", "apple", "cherry"]

# sort by length
words.sort(key=lambda w: len(w))
# ["apple", "banana", "cherry"]

# filter to long words
long_words = list(filter(lambda w: len(w) > 5, words))
# ["banana", "cherry"]

# map to lengths
lengths = list(map(lambda w: len(w), words))
# [5, 6, 6]
```

⚠ Don't write multi-line lambdas. If you need more than one expression, use `def`. Lambdas are for one-liners.

---

## 5.3 · Type hints

Python is dynamically typed — but you can *annotate* what types you expect. The annotations don't enforce anything at runtime, but they help your editor, your reader, and tools like `mypy`.

```python
def greet(name: str) -> str:
    return f"Hello, {name}"

def add(a: int, b: int) -> int:
    return a + b

def find(items: list, target) -> int | None:
    for i, item in enumerate(items):
        if item == target:
            return i
    return None
```

Common annotations:

```python
def f(name: str,
      age: int,
      score: float,
      tags: list[str],
      config: dict[str, int],
      ready: bool = True) -> bool:
    ...
```

You'll see these constantly in serious Python codebases. Pre-foundations: just recognize them. You don't have to write them yet. The [`../prog/`](../prog/) track covers them properly.

---

## 5.4 · Docstrings

A string at the top of a function (or class, or module) that documents what it does:

```python
def normalize(values):
    """Scale values to the range [0, 1].

    Args:
        values: list of numbers.

    Returns:
        A new list where the smallest is 0 and the largest is 1.
    """
    lo = min(values)
    hi = max(values)
    return [(v - lo) / (hi - lo) for v in values]
```

Triple-quoted string, just inside the function body. Tools like `help(normalize)` will show this docstring. Editors will display it on hover. Every public function in a real codebase should have one.

---

## 5.5 · Modules and imports

A **module** is just a Python file. Any `.py` file is a module. You can import functions and variables from one file into another.

### Built-in modules

Python ships with a huge "standard library." A few you'll use early:

```python
import math
math.sqrt(16)                # 4.0
math.pi                      # 3.141592653589793
math.log(10)                 # 2.302585...

import random
random.randint(1, 10)        # random integer between 1 and 10
random.choice([1, 2, 3])     # random pick from a list
random.shuffle(my_list)      # shuffle a list in place

import json
data = json.loads('{"a": 1}')      # parse JSON string → dict
json.dumps(data)                    # dict → JSON string

import os
os.getcwd()                  # current directory
os.listdir(".")              # files in current directory

import sys
sys.argv                     # command-line arguments
sys.exit()                   # quit the program
```

### Import variants

```python
import math                          # import the whole module
math.sqrt(16)

from math import sqrt                # import just one thing
sqrt(16)

from math import sqrt, pi, log       # import several
sqrt(pi)

from math import *                   # import EVERYTHING (avoid — pollutes namespace)

import numpy as np                   # import with an alias
np.array([1, 2, 3])

from collections import Counter      # specific class from a module
```

The `as` syntax is conventional for some big libraries:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
```

Everyone writes these exact aliases. Don't invent your own.

### Your own modules

If you have two files in the same folder:

```
my-project/
├── helpers.py
└── main.py
```

Where `helpers.py` is:
```python
def greet(name):
    return f"Hello, {name}"
```

Then in `main.py`:
```python
from helpers import greet
print(greet("Sid"))
```

That's it. Any `.py` file is importable.

### `if __name__ == "__main__":`

A pattern you'll see often:

```python
# in a file called calc.py
def add(a, b):
    return a + b

if __name__ == "__main__":
    print(add(3, 4))
```

The `if` block runs only when you execute `python calc.py` directly. If you `import calc` from another file, the `if` block is skipped. Useful pattern: a file that's both an importable library and a runnable script.

---

## 5.6 · pip and virtual environments

### `pip` — Python's package installer

The Python standard library is big, but not infinite. For everything else — NumPy, PyTorch, Pandas, requests, etc. — there's the [Python Package Index (PyPI)](https://pypi.org/), and the tool to install from it is `pip`.

```
pip install numpy
pip install torch
pip install "pandas>=2.0"           # version constraint
pip install -r requirements.txt     # install everything in a file
pip uninstall numpy
pip list                            # what's installed
pip show numpy                      # info about a package
```

### Why virtual environments exist

The problem: if you `pip install numpy` *globally* on your system, *every* Python project on your machine uses that same numpy. Two projects that need different versions? You're stuck.

A **virtual environment** is a self-contained Python install for one project. Each project has its own packages, isolated.

### With `venv` (built-in)

```
# in your project folder
python -m venv .venv          # creates a .venv/ folder

# activate it
source .venv/bin/activate     # Mac / Linux
.venv\Scripts\activate         # Windows

# now pip installs into the venv, not globally
pip install numpy

# when done
deactivate
```

While the venv is active, your prompt usually shows `(.venv)` so you know.

### With `uv` (faster, modern)

```
uv venv                       # creates .venv
source .venv/bin/activate     # or .venv\Scripts\activate on Windows
uv pip install numpy
```

`uv` is 10–100× faster than `pip` and handles Python versions too. It's the modern default — if you're starting from zero, just use `uv`.

### `requirements.txt`

The convention for pinning a project's dependencies:

```
# requirements.txt
numpy>=1.24
pandas>=2.0
matplotlib>=3.7
torch>=2.0
```

Then anyone who clones the project runs:
```
pip install -r requirements.txt
```

You'll see one in [`../math/calculus-playground/`](../math/calculus-playground/).

---

## 5.7 · Files

### Opening, reading, closing

```python
# basic open / read / close
f = open("data.txt", "r")       # "r" = read mode (default)
contents = f.read()
f.close()
```

⚠ Forgetting `f.close()` is a real bug — the OS holds the file open. The fix: the `with` statement.

### The `with` statement (use this)

```python
with open("data.txt", "r") as f:
    contents = f.read()
# file is automatically closed here
```

Even if an error happens inside the `with` block, the file gets closed. Always prefer this form.

### Reading modes

```python
with open("data.txt") as f:
    text = f.read()                 # whole file as one string

with open("data.txt") as f:
    lines = f.readlines()           # list of lines (each includes \n)

with open("data.txt") as f:
    for line in f:                  # iterate line by line — memory-efficient for big files
        print(line.strip())         # strip removes the trailing newline
```

### Writing

```python
with open("output.txt", "w") as f:
    f.write("Hello\n")
    f.write("World\n")
```

Modes:
- `"r"` — read (default; fails if file doesn't exist).
- `"w"` — write (overwrites the file; creates it if missing).
- `"a"` — append (adds to the end; creates if missing).
- `"r+"` — read and write.
- `"rb"`, `"wb"` — read/write in binary mode (for non-text files: images, audio, etc.).

### Reading a CSV the simple way

Quick and dirty, no library needed:

```python
with open("data.csv") as f:
    header = f.readline().strip().split(",")
    rows = []
    for line in f:
        rows.append(line.strip().split(","))
```

The right way uses the built-in `csv` module:

```python
import csv

with open("data.csv") as f:
    reader = csv.DictReader(f)
    rows = list(reader)             # list of dicts, one per row
```

And the real-world way (once you're in the prog/ track) is `pandas`.

### Pathlib — the modern way to handle paths

Old way: messing with string paths and `os.path.join`. Modern way: `pathlib.Path`.

```python
from pathlib import Path

p = Path("data") / "raw" / "file.csv"     # OS-correct path
p.exists()                                # True / False
p.is_file()
p.read_text()                             # read whole file as string
p.write_text("new contents")
p.parent                                  # Path("data/raw")
p.name                                    # "file.csv"
p.stem                                    # "file"
p.suffix                                  # ".csv"

# iterate files in a directory
for path in Path("data").iterdir():
    print(path)

# only .csv files
for path in Path("data").glob("*.csv"):
    print(path)
```

`pathlib` is what you should reach for in 2025+ code.

---

## 5.8 · Practice — three things to do before moving on

1. **Open the python-and-dsa playground**, do Lesson 7 (Functions) if you haven't. Then write a function called `is_palindrome(s)` that returns True if a string reads the same forwards and backwards. Test it on `"racecar"`, `"hello"`, `""`.

2. **Make a real project folder.** From the terminal:
   ```
   mkdir my-first-project
   cd my-first-project
   uv venv                       # or python -m venv .venv
   source .venv/bin/activate     # .venv\Scripts\activate on Windows
   uv pip install requests       # or pip install requests
   ```
   Then create `main.py` with:
   ```python
   import requests
   r = requests.get("https://api.github.com")
   print(r.status_code)
   print(r.json()["current_user_url"])
   ```
   Run `python main.py`. You just installed a third-party package and made an API call.

3. **Read and write a file.** Create `notes.txt` with three lines. Write a script that reads it, prints each line numbered, and writes a new file `notes_uppercased.txt` with each line uppercased.

   Don't look at the solution — just do it. If you get stuck, the techniques are all in section 5.7.

---

## Where to next

→ [06-everyday-essentials.md](06-everyday-essentials.md) — exceptions, JSON, dates, math/random modules, regex, environment variables.

Or jump back to the [pre-foundations index](README.md).

---

## Further reading

- [w3schools Python functions](https://www.w3schools.com/python/python_functions.asp).
- [w3schools Python modules](https://www.w3schools.com/python/python_modules.asp).
- [w3schools Python files](https://www.w3schools.com/python/python_file_handling.asp).
- [Real Python — Python virtual environments](https://realpython.com/python-virtual-environments-a-primer/) — when you want the full story.
- [Python docs — `pathlib`](https://docs.python.org/3/library/pathlib.html) — the modern path API.
- [`uv` documentation](https://docs.astral.sh/uv/) — modern Python package and project manager.
