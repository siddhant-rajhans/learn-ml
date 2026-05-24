# 06 · Everyday essentials

← previous: [05-functions-modules-files.md](05-functions-modules-files.md) · next: [EXIT-CHECKLIST.md](EXIT-CHECKLIST.md)

Six small things that aren't in the language tutorial but show up in week one of any real project.

When user input is bad and your program shouldn't crash, that's `try / except`. When you talk to an API the data comes back as JSON. When you compare dates or measure how long something took, that's `datetime` and `time`. When you want to find a pattern in a string, that's regex. When you have an API key that shouldn't be in your code, that's an environment variable. When `print()` isn't cutting it for debugging anymore, that's `logging`.

None of these need deep treatment. You just need to know they exist so you can reach for them.

---

## 6.1 · Exceptions — `try` / `except`

Some code can fail at runtime — a file doesn't exist, a network call times out, a user types text where you wanted a number. **Exceptions** are how Python signals these failures. **`try` / `except`** is how you handle them.

### The basic form

```python
try:
    x = int(input("Enter a number: "))
    print(f"Squared: {x ** 2}")
except ValueError:
    print("That wasn't a number.")
```

If `int(...)` raises `ValueError` (because the input wasn't a number), control jumps to the `except` block. If no exception happens, the `except` is skipped.

### Catching multiple types

```python
try:
    data = open("data.txt").read()
    value = int(data)
except FileNotFoundError:
    print("No file.")
except ValueError:
    print("File didn't contain a number.")
```

Or in one `except`:

```python
try:
    ...
except (FileNotFoundError, ValueError) as e:
    print(f"Something went wrong: {e}")
```

The `as e` binds the exception object to a name — useful for printing the message or logging.

### The exception types you'll meet

These are the same ones from chapter 3, but here's when you'd actually catch each:

| Exception | Catch it when |
|-----------|---------------|
| `ValueError` | Parsing user input — `int("abc")`, `float("not a number")`. |
| `KeyError` | Looking up a dict key that might not exist — *but* `dict.get(key, default)` is usually cleaner. |
| `IndexError` | Indexing into a list/string when the size isn't guaranteed. |
| `FileNotFoundError` | Opening a file that might not be there. |
| `PermissionError` | Writing to a file/folder you don't have access to. |
| `KeyboardInterrupt` | User hit Ctrl+C — catch this in long-running programs to clean up. |
| `ZeroDivisionError` | Division where the denominator might be 0. |
| `TimeoutError` | Network calls that took too long. |
| `Exception` | The catch-all "something went wrong." Use sparingly. |

### `else` and `finally`

```python
try:
    file = open("data.txt")
except FileNotFoundError:
    print("No file.")
else:
    # runs only if no exception was raised
    contents = file.read()
    file.close()
finally:
    # runs ALWAYS — exception or not
    print("Done trying.")
```

`finally` is for cleanup that has to happen no matter what. In modern code, the `with` statement (chapter 5) handles most of these cases automatically.

### Raising your own exceptions

If your code detects something is wrong, you raise:

```python
def withdraw(account, amount):
    if amount < 0:
        raise ValueError("Amount must be positive")
    if amount > account.balance:
        raise ValueError(f"Insufficient funds: balance is {account.balance}")
    account.balance -= amount
```

You can raise any built-in exception type. For your own custom errors, define a class:

```python
class InsufficientFunds(Exception):
    pass

raise InsufficientFunds("Not enough money")
```

### Don't catch what you don't handle

```python
# BAD — silently swallows every error, you'll never know why something broke
try:
    do_thing()
except:
    pass

# also BAD — catches things you didn't mean to (KeyboardInterrupt, MemoryError)
try:
    do_thing()
except Exception:
    pass
```

Be specific. Catch the exceptions you can actually do something about. Let the rest propagate up so you see them.

---

## 6.2 · JSON

**JSON** (JavaScript Object Notation) is a text format for structured data. It's how nearly every web API sends data, how config files are often stored, how you save dict-like data to disk.

JSON looks almost exactly like a Python dict/list literal:

```json
{
  "name": "Sid",
  "age": 30,
  "tags": ["ml", "python"],
  "active": true,
  "spouse": null
}
```

The differences from Python:
- `true` / `false` / `null` — lowercase. Python's `True` / `False` / `None` are capitalized.
- Keys must be in `"double quotes"`. Python dicts accept single or double.
- No trailing commas. (Python lets you have them; JSON doesn't.)

### Parsing JSON in Python

```python
import json

# JSON string → Python dict/list
text = '{"name": "Sid", "age": 30}'
data = json.loads(text)
print(data["name"])           # "Sid"
print(type(data))             # <class 'dict'>

# Python → JSON string
back_to_text = json.dumps(data)
print(back_to_text)
# '{"name": "Sid", "age": 30}'

# pretty-printed
print(json.dumps(data, indent=2))
```

### Reading from / writing to a file

```python
# write a dict to a JSON file
with open("config.json", "w") as f:
    json.dump(data, f, indent=2)

# read it back
with open("config.json") as f:
    data = json.load(f)
```

Note the difference: `json.dumps` / `json.loads` work with strings, `json.dump` / `json.load` work directly with files.

### What JSON can (and can't) hold

| JSON type | Python equivalent |
|-----------|-------------------|
| object `{}` | `dict` |
| array `[]` | `list` |
| string | `str` |
| number | `int` or `float` |
| `true` / `false` | `True` / `False` |
| `null` | `None` |

**JSON can't hold:** tuples (become lists on round-trip), sets, dates, custom objects, `inf` / `nan`. For those you need either custom encoders or a different format (pickle, msgpack).

---

## 6.3 · Dates and time

Three modules, related but different:

- `time` — Unix timestamps, sleep, simple time measurement.
- `datetime` — date and time as structured objects.
- `zoneinfo` — timezone handling (Python 3.9+).

### Quick stuff

```python
import time

time.time()                    # 1735000000.123 — seconds since 1970 (Unix timestamp)

# time how long something takes
start = time.time()
do_expensive_thing()
elapsed = time.time() - start
print(f"Took {elapsed:.2f} seconds")

time.sleep(2)                  # pause for 2 seconds
```

### `datetime` — the structured way

```python
from datetime import datetime, date, timedelta

now = datetime.now()           # current date and time
today = date.today()           # just date, no time

print(now)                     # 2026-05-18 14:23:01.123456
print(now.year, now.month, now.day, now.hour)

# create a specific datetime
birthday = datetime(2000, 1, 15, 10, 30)

# arithmetic with timedeltas
tomorrow = now + timedelta(days=1)
next_week = now + timedelta(weeks=1)
two_hours_ago = now - timedelta(hours=2)

# difference
delta = next_week - now
delta.days                     # 7
delta.total_seconds()          # 604800.0
```

### Formatting and parsing

```python
now = datetime.now()

# format a datetime to a string
now.strftime("%Y-%m-%d %H:%M")     # "2026-05-18 14:23"
now.strftime("%B %d, %Y")          # "May 18, 2026"

# parse a string into a datetime
dt = datetime.strptime("2026-05-18", "%Y-%m-%d")
```

Format codes you'll see most:

| Code | Meaning | Example |
|------|---------|---------|
| `%Y` | year, 4-digit | 2026 |
| `%m` | month, 2-digit | 05 |
| `%d` | day, 2-digit | 18 |
| `%H` | hour, 24-hour | 14 |
| `%M` | minute | 23 |
| `%S` | second | 01 |
| `%B` | month, full name | May |
| `%b` | month, short name | May |
| `%A` | weekday, full | Sunday |
| `%a` | weekday, short | Sun |

For ML you'll often see ISO 8601 dates: `2026-05-18T14:23:01Z`. Parse with `datetime.fromisoformat("2026-05-18T14:23:01")`.

### Timezones

⚠ The hardest part of dates. Python defaults to "naive" datetimes (no timezone). Be careful when comparing or storing.

```python
from datetime import datetime
from zoneinfo import ZoneInfo

now_utc = datetime.now(ZoneInfo("UTC"))
now_ny = datetime.now(ZoneInfo("America/New_York"))
now_tokyo = datetime.now(ZoneInfo("Asia/Tokyo"))

# convert between zones
ny_to_tokyo = now_ny.astimezone(ZoneInfo("Asia/Tokyo"))
```

Rule of thumb: store dates as UTC, display them in the user's local time. Saves grief.

---

## 6.4 · The `math` and `random` modules

Both built-in. You'll meet them constantly.

### `math` — every function you'd expect

```python
import math

math.pi                  # 3.141592653589793
math.e                   # 2.718281828459045
math.inf                 # infinity
math.nan                 # not-a-number

math.sqrt(16)            # 4.0
math.pow(2, 10)          # 1024.0 (same as 2 ** 10)
math.exp(1)              # e^1 ≈ 2.718
math.log(math.e)         # 1.0 (natural log)
math.log(100, 10)        # 2.0 (log base 10)
math.log2(8)             # 3.0
math.log10(1000)         # 3.0

math.sin(math.pi / 2)    # 1.0
math.cos(0)              # 1.0
math.tan(math.pi / 4)    # 1.0
math.degrees(math.pi)    # 180.0
math.radians(180)        # 3.14159...

math.floor(3.7)          # 3 (round down)
math.ceil(3.2)           # 4 (round up)
math.trunc(3.7)          # 3 (truncate, same as int())
round(3.5)               # 4 (built-in — banker's rounding)
round(3.14159, 2)        # 3.14

math.factorial(5)        # 120
math.gcd(12, 18)         # 6
math.isclose(0.1 + 0.2, 0.3)    # True — for float comparisons
```

You'll graduate from `math` to NumPy in the [`../prog/`](../prog/) track, but `math` is what's built in.

### `random` — random numbers

```python
import random

random.random()                    # float in [0.0, 1.0)
random.uniform(0, 10)              # float in [0, 10]
random.randint(1, 6)               # int in [1, 6] inclusive
random.randrange(0, 10, 2)         # 0, 2, 4, 6, or 8

random.choice([1, 2, 3, 4])        # one random pick
random.choices([1, 2, 3], k=5)     # 5 picks WITH replacement
random.sample([1, 2, 3, 4], k=2)   # 2 picks WITHOUT replacement
random.shuffle(my_list)            # shuffle in place

# reproducible randomness
random.seed(42)
print(random.random())             # same every time
```

⚠ `random` is fine for most things but NOT cryptographically secure. For passwords or tokens, use `secrets` (`secrets.token_hex(16)`).

⚠ For ML, use `numpy.random` or `torch.manual_seed` once you're in the prog/ track — they have proper RNG state for arrays/tensors.

---

## 6.5 · Regular expressions (regex) — intro

A **regex** is a tiny language for describing string patterns. *"Match any line that starts with a date."* *"Find every email address."* *"Replace every multiple of whitespace with a single space."*

The Python module is `re`. Pre-foundations is just the *what is this* level.

```python
import re

# Does the string match a pattern?
re.match(r"\d+", "123 hello")           # match object (truthy)
re.match(r"\d+", "hello 123")           # None — match looks at the START

# Find anywhere in the string
re.search(r"\d+", "hello 123 world")    # match for "123"

# Find ALL non-overlapping matches
re.findall(r"\d+", "a1 b22 c333")       # ["1", "22", "333"]

# Replace
re.sub(r"\d+", "N", "a1 b22 c333")      # "aN bN cN"

# Split on a pattern
re.split(r"\s+", "a  b   c d")          # ["a", "b", "c", "d"]
```

### The pattern characters

| Pattern | Means |
|---------|-------|
| `.` | any single character |
| `\d` | a digit (0–9) |
| `\w` | word character (letter, digit, underscore) |
| `\s` | whitespace (space, tab, newline) |
| `\D` `\W` `\S` | NOT digit / NOT word / NOT whitespace |
| `^` | start of the string (or line, with `re.MULTILINE`) |
| `$` | end of the string |
| `*` | zero or more of the previous thing |
| `+` | one or more |
| `?` | zero or one |
| `{n}` | exactly n |
| `{n,m}` | between n and m |
| `[abc]` | any of `a`, `b`, `c` |
| `[^abc]` | NOT a, b, c |
| `[a-z]` | range — any lowercase letter |
| `(stuff)` | a group — captures what matched |
| `|` | OR — `cat|dog` matches either |

### Useful regex you'll meet

```python
# email-like (NOT rigorous, but useful)
r"\w+@\w+\.\w+"

# date YYYY-MM-DD
r"\d{4}-\d{2}-\d{2}"

# whitespace-separated tokens
r"\S+"

# strip everything inside parentheses
re.sub(r"\(.*?\)", "", "Hello (world) again")    # "Hello  again"
```

⚠ The `r"..."` prefix is a **raw string** — backslashes are literal. Always use raw strings for regex.

For pre-foundations: recognize a regex, know `re.findall` and `re.sub` exist, know you can paste a regex into [regex101.com](https://regex101.com) to interactively debug. That's enough.

---

## 6.6 · Environment variables and command-line arguments

### Environment variables

Variables set in your shell that any program can read. Used for:
- API keys (don't hardcode them in your code!)
- Configuration that changes between dev / staging / production.
- Paths to data folders.

```python
import os

api_key = os.environ.get("OPENAI_API_KEY")          # None if not set
api_key = os.environ["OPENAI_API_KEY"]              # KeyError if not set
api_key = os.environ.get("OPENAI_API_KEY", "default")
```

Setting them in your shell:

```
# Mac / Linux
export OPENAI_API_KEY=sk-...

# Windows PowerShell
$env:OPENAI_API_KEY = "sk-..."
```

For local dev, the common convention is a `.env` file in your project root:

```
OPENAI_API_KEY=sk-...
DATABASE_URL=postgres://...
```

Load it with [`python-dotenv`](https://pypi.org/project/python-dotenv/):

```python
from dotenv import load_dotenv
load_dotenv()

# now os.environ knows about the .env values
api_key = os.environ.get("OPENAI_API_KEY")
```

⚠ **Never commit a `.env` file to git.** Add it to `.gitignore`.

### Command-line arguments

When you run `python script.py arg1 arg2`, the script can see `arg1` and `arg2`:

```python
import sys

print(sys.argv)
# ["script.py", "arg1", "arg2"]

# sys.argv[0] is always the script name
# sys.argv[1:] are the user's args
```

For real CLIs (lots of options, `--help`, etc.), use [`argparse`](https://docs.python.org/3/library/argparse.html) (built in) or [`click`](https://click.palletsprojects.com/) / [`typer`](https://typer.tiangolo.com/) (third-party, nicer).

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--lr", type=float, default=0.01)
parser.add_argument("--epochs", type=int, default=10)
parser.add_argument("data_path")
args = parser.parse_args()

print(args.lr, args.epochs, args.data_path)
```

Then `python train.py --lr 0.001 --epochs 50 data/train.csv` works.

---

## 6.7 · Logging — a step beyond `print`

`print` is fine for quick scripts. For anything you want to debug, monitor in production, or filter by severity, use the `logging` module:

```python
import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

log.debug("very detailed — usually hidden")
log.info("normal informational message")
log.warning("something to pay attention to")
log.error("something went wrong but we continued")
log.critical("something went badly wrong")
```

The output:

```
INFO:__main__:normal informational message
WARNING:__main__:something to pay attention to
...
```

Why bother over `print`?

1. You can set the level. In dev, see everything (`DEBUG`). In production, only warnings and up.
2. You can route messages to a file, the console, a remote logging service — all at once.
3. Stack traces from exceptions get logged automatically with `log.exception(...)`.
4. It plays nicely with ML frameworks (PyTorch, TensorFlow) that also log.

Pre-foundations: know it exists. The prog/ track teaches it properly.

---

## 6.8 · Practice — three things to do before moving on

1. **Make a script that handles bad input gracefully.** Write a program that asks the user for a number, computes the square root, and prints it. Handle: not a number, negative number, user hits Ctrl+C. Use `try` / `except` for each.

2. **Save and load a config.** Make a Python dict with your name, age, and a list of favorite languages. Save it to `config.json`. Then write a separate script that reads it back and prints each field on its own line. Verify the round-trip works.

3. **Time something.** Write code that creates a list of 1 million numbers, then measures (with `time.time()`) how long it takes to:
   - Iterate and sum with a for loop.
   - Sum with the built-in `sum()`.
   - Convert to a NumPy array (you'll need `pip install numpy`) and `.sum()`.

   You'll see why people use NumPy — usually 10–100× faster for the same work. Worth seeing once before you reach the [`../prog/`](../prog/) track.

---

## Where to next

→ [EXIT-CHECKLIST.md](EXIT-CHECKLIST.md) — the honest test. Are you done with pre-foundations?

Or jump back to the [pre-foundations index](README.md).

---

## Further reading

- [w3schools Python try / except](https://www.w3schools.com/python/python_try_except.asp).
- [w3schools Python JSON](https://www.w3schools.com/python/python_json.asp).
- [w3schools Python dates](https://www.w3schools.com/python/python_datetime.asp).
- [w3schools Python regex](https://www.w3schools.com/python/python_regex.asp).
- [regex101.com](https://regex101.com) — interactive regex testing, with explanations.
- [Python docs — `logging`](https://docs.python.org/3/howto/logging.html) — when you outgrow `print()`.
- [12factor.net — config](https://12factor.net/config) — why env vars are the right default for configuration.
