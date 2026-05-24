# 03 · Python syntax and data

← previous: [02-math-zero.md](02-math-zero.md) · next: [04-flow-and-collections.md](04-flow-and-collections.md)

Every Python datatype, every Python operator, every common error, pinned in one place. Open this when you forget whether `/` or `//` is the one that drops the decimal. (`//`.)

This is the longest chapter in pre-foundations. It's also the one you'll come back to most.

---

## 3.1 · The 5 rules of Python syntax

Python has a smaller set of syntax rules than most languages. Five things you have to get right:

### Rule 1: Indentation IS the grammar

Most languages use `{ }` or `begin/end` to group code. Python uses **whitespace**.

```python
# CORRECT
if x > 0:
    print("positive")
    print("greater than zero")

# WRONG — IndentationError
if x > 0:
print("positive")

# WRONG — inconsistent indentation, IndentationError
if x > 0:
    print("positive")
      print("oops")
```

**Use 4 spaces per level.** Always. Tabs work but mixing tabs and spaces breaks Python in horrible ways. Every editor can be set to convert tab presses into 4 spaces — turn that on once and forget about it.

### Rule 2: Colons start blocks

Any line that opens a new block ends with a `:`. Then the next line is indented.

```python
if x > 0:                        # block follows
    print("positive")

for item in [1, 2, 3]:           # block follows
    print(item)

def greet(name):                 # block follows
    return f"Hello {name}"
```

Forget the colon and you get `SyntaxError: expected ':' ...`.

### Rule 3: Comments start with `#`

Everything after `#` on a line is ignored by Python. Use comments to explain *why*, not *what* (the code already says what).

```python
# good comment — explains intent
threshold = 0.5  # below this we predict "negative"

# bad comment — restates the code
x = x + 1  # increment x
```

For multi-line comments, just stack `#` lines. Python has triple-quoted strings (`"""..."""`) too, but those are technically string literals — used for *docstrings* (function/class documentation), not arbitrary comments.

### Rule 4: One statement per line (mostly)

```python
x = 5
y = 10
result = x + y
```

You *can* put multiple on one line with `;` (`x = 5; y = 10`), but don't. It's ugly.

If a line is genuinely too long, break it inside parentheses:

```python
# Python is happy with line breaks inside (), [], {}
result = (some_very_long_function_name(arg1, arg2)
          + another_function(arg3))
```

### Rule 5: Names are case-sensitive

`age` and `Age` and `AGE` are three different variables.

**Naming conventions** (PEP 8):
- `snake_case` for variables and functions: `my_variable`, `compute_loss`.
- `CamelCase` for classes: `Person`, `LinearRegression`.
- `UPPER_SNAKE_CASE` for constants: `MAX_ITERATIONS`, `PI`.

These aren't rules Python enforces — they're conventions everyone follows. Code that doesn't follow them looks weird to other programmers.

---

## 3.2 · Variables and assignment

A variable is a name that points at a value:

```python
x = 5
name = "Sid"
is_ready = True
```

The `=` is **assignment** (not equality). It says *"put this value into this name."*

Python is **dynamically typed** — you don't declare the type of a variable. The type is whatever value you put in. And the type can change:

```python
x = 5         # x is now an int
x = "hello"   # x is now a str
x = [1, 2, 3] # x is now a list
```

You can assign multiple variables at once:

```python
x, y = 1, 2          # x = 1, y = 2
a = b = c = 0        # all three are 0
```

### Valid variable names

- Must start with a letter or underscore: `name`, `_private`, `name2` — OK. `2name` — error.
- Can contain letters, digits, underscores. No spaces, no dashes, no other punctuation.
- Can't be a Python keyword (`if`, `for`, `def`, `class`, `return`, etc.). Your editor will color these blue.
- Case-sensitive.

```python
my_var = 1            # OK
_secret = 2           # OK (convention: leading underscore = "private")
my-var = 3            # SyntaxError — dashes aren't allowed
def = 4               # SyntaxError — def is a keyword
my var = 5            # SyntaxError — spaces aren't allowed
```

---

## 3.3 · The built-in datatypes

Python has a small set of built-in types. Here they all are.

### `int` — integers

Whole numbers, positive or negative. Unlimited size (Python doesn't have a max int — it'll happily compute `2**1000`).

```python
age = 30
year = 2026
huge = 10 ** 100             # 1 followed by 100 zeros, no problem
negative = -7
zero = 0
```

You can write ints in other bases:
```python
0b1010    # binary,    = 10
0o17      # octal,     = 15
0xff      # hex,       = 255
```

You can use `_` as a thousands separator for readability:
```python
million = 1_000_000          # same as 1000000
```

### `float` — floating-point numbers

Numbers with a decimal point. Used for *every* real-valued computation in ML.

```python
pi = 3.14159
gravity = 9.8
fraction = 0.5
tiny = 1e-10                  # scientific notation: 1 × 10⁻¹⁰
huge = 1.5e9                  # 1.5 billion
negative = -0.001
```

⚠ **Floats are not exact.** `0.1 + 0.2` is **not** `0.3`:

```python
>>> 0.1 + 0.2
0.30000000000000004
```

That's a 60-year-old quirk of how computers represent decimals in binary. It's not a Python bug. Live with it — when comparing floats for equality, use `math.isclose(a, b)` instead of `a == b`.

Special floats: `float('inf')` (positive infinity), `float('-inf')`, `float('nan')` (not-a-number — a placeholder for "undefined").

### `complex` — complex numbers

Numbers with a real and imaginary part. Used in signal processing, quantum, some physics ML.

```python
z = 2 + 3j         # j is the imaginary unit (not i, oddly)
z.real             # 2.0
z.imag             # 3.0
```

You'll see these rarely in mainstream ML. They're in the language for completeness.

### `str` — strings

Sequences of characters. Use single or double quotes — doesn't matter, but pick one and be consistent.

```python
name = "Sid"
also_name = 'Sid'              # identical
sentence = "Hello, world!"
empty = ""
```

For multi-line strings, use triple quotes:
```python
poem = """Roses are red
Violets are blue
Python is fun
And so are you"""
```

Strings can contain any Unicode character — emoji, math symbols, Chinese, whatever:
```python
emoji = "🚀"
math_sym = "∇L"
greeting = "你好"
```

**Strings are immutable.** You can't change a character in place:
```python
s = "hello"
s[0] = "H"        # TypeError: 'str' object does not support item assignment
s = "H" + s[1:]   # OK — but this creates a NEW string
```

We cover string operations and slicing in section 3.6.

### `bool` — booleans

Two values: `True` and `False`. **Capital first letter.**

```python
is_ready = True
is_done = False
```

`bool` is technically a subclass of `int` — `True == 1` and `False == 0`. You can do math with them:

```python
True + True       # 2
sum([True, False, True, True])    # 3
```

Useful for counting how many things in a list satisfy a condition.

### `NoneType` — `None`

Python's "nothing." Used to represent a missing value, an uninitialized variable, or a function that doesn't return anything.

```python
result = None
def greet():
    print("hi")
x = greet()       # x is None — greet() didn't return anything
```

Compare to `None` with `is`, never `==`:
```python
if result is None: ...        # good
if result == None: ...        # works but uses the wrong operator
```

### `list` — ordered, mutable sequence

Square brackets. The most-used container in Python.

```python
numbers = [1, 2, 3, 4, 5]
mixed = ["sid", 30, True, 3.14]      # any types, any mix
nested = [[1, 2], [3, 4]]            # lists in lists
empty = []
```

Lists are **mutable** — you can change them after creation:
```python
numbers.append(6)              # add to the end
numbers[0] = 99                # change an element
numbers.remove(3)              # remove the first occurrence of 3
```

Full coverage in [chapter 4](04-flow-and-collections.md).

### `tuple` — ordered, immutable sequence

Round brackets. Like a list, but you can't change it after creation.

```python
point = (3, 4)
rgb = (255, 0, 128)
empty = ()
single = (5,)                  # ⚠ trailing comma needed — (5) is just 5 in parens
```

Used for: data that shouldn't change (coordinates, colors, dict keys), returning multiple values from a function, fixed-size records.

### `set` — unordered, unique, mutable

Curly braces with values. No duplicates. No order.

```python
fruits = {"apple", "banana", "cherry"}
fruits.add("apple")            # already there — no effect
{1, 2, 2, 3, 3, 3}             # = {1, 2, 3} — duplicates removed
empty_set = set()              # ⚠ {} is an empty DICT, not set
```

Useful for: membership tests (very fast), removing duplicates, set operations (union, intersection).

### `frozenset` — unordered, unique, immutable

Like `set`, but you can't change it.

```python
frozen = frozenset([1, 2, 3])
```

Rare. Used when you need a set as a dictionary key (regular sets can't be keys because they're mutable).

### `dict` — key-value pairs

Curly braces with `key: value` pairs. The second most-used container after `list`.

```python
person = {"name": "Sid", "age": 30, "city": "Hoboken"}
person["name"]                 # "Sid"
person["job"] = "ML student"   # add a new key
empty = {}
```

Keys must be **hashable** (immutable) — strings, numbers, tuples work. Lists and dicts as keys: not allowed.

Full coverage in [chapter 4](04-flow-and-collections.md).

### `bytes` and `bytearray`

Raw binary data — what files actually store on disk before you decode them as text.

```python
b = b"hello"                   # bytes literal — prefix with b
b[0]                           # 104 (the byte value, not a character)
b.decode("utf-8")              # "hello" (now it's a regular string)
```

You'll meet `bytes` when reading files in binary mode (`open(file, 'rb')`), working with images, or downloading from a URL. Don't sweat it now.

### Recap table

| Type | Example | Mutable? | Used for |
|------|---------|----------|----------|
| `int` | `5` | n/a | whole numbers |
| `float` | `3.14` | n/a | real numbers (everything in ML) |
| `complex` | `2+3j` | n/a | rare in ML |
| `str` | `"hello"` | no | text |
| `bool` | `True` | n/a | true / false |
| `NoneType` | `None` | n/a | nothing / missing |
| `list` | `[1, 2, 3]` | yes | ordered, mutable sequence |
| `tuple` | `(1, 2, 3)` | no | ordered, fixed sequence |
| `set` | `{1, 2, 3}` | yes | unique, unordered |
| `frozenset` | `frozenset({1,2})` | no | unique, unordered, hashable |
| `dict` | `{"a": 1}` | yes | key → value lookup |
| `bytes` | `b"hello"` | no | raw binary data |
| `bytearray` | `bytearray(b"hi")` | yes | raw binary data, mutable |

---

## 3.4 · Checking types and casting

### `type()` — what is this?

```python
type(5)              # <class 'int'>
type(3.14)           # <class 'float'>
type("hi")           # <class 'str'>
type([1, 2])         # <class 'list'>
type(None)           # <class 'NoneType'>
```

### `isinstance()` — is this one of these types?

Better than `type(x) == int` because it handles subclasses correctly:

```python
isinstance(5, int)               # True
isinstance(5, (int, float))      # True — tuple = "any of these"
isinstance(True, int)            # True — bool is a subclass of int!
isinstance("hi", str)            # True
```

Use `isinstance` when you need to check a type. Use `type` mostly for debugging ("what *is* this thing?").

### Casting — converting between types

Python has built-in constructors that convert values:

```python
# to int
int(3.7)             # 3 — truncates toward zero, doesn't round
int(-3.7)            # -3
int("42")            # 42
int("3.14")          # ValueError — can't parse a float string as int
int(True)            # 1
int(False)           # 0

# to float
float(5)             # 5.0
float("3.14")        # 3.14
float("inf")         # inf
float(True)          # 1.0

# to str
str(5)               # "5"
str(3.14)            # "3.14"
str([1, 2, 3])       # "[1, 2, 3]"
str(None)            # "None"

# to bool
bool(0)              # False
bool(1)              # True
bool("")             # False — empty string is "falsy"
bool("hello")        # True — non-empty string is "truthy"
bool([])             # False — empty list
bool([0])            # True — non-empty list (even with 0 inside)
bool(None)           # False

# to list / tuple / set
list("abc")          # ['a', 'b', 'c']
list((1, 2, 3))      # [1, 2, 3]
tuple([1, 2, 3])     # (1, 2, 3)
set([1, 1, 2, 3])    # {1, 2, 3}

# to dict (needs a sequence of pairs)
dict([("a", 1), ("b", 2)])    # {"a": 1, "b": 2}
```

### Truthy and falsy

When you put a non-boolean value in a `bool()` or an `if` condition, Python decides if it's True-ish or False-ish:

**Falsy** (treated as False):
- `False`, `None`
- `0`, `0.0`, `0j`
- `""` (empty string)
- `[]`, `()`, `{}`, `set()` — any empty container

**Truthy** (treated as True):
- Everything else. Any non-zero number, non-empty string, non-empty container.

Why care? Because this works:

```python
if my_list:                    # True if list is non-empty
    print("has stuff")

name = input("Your name: ") or "anonymous"     # "anonymous" if input is empty
```

This is idiomatic Python — `if my_list` reads as *"if there's anything in my_list."*

---

## 3.5 · Operators

### Arithmetic operators

```python
a + b        # addition
a - b        # subtraction
a * b        # multiplication
a / b        # division — always returns a float
a // b       # integer division (floor) — drops the fractional part
a % b        # modulo — the remainder after division
a ** b       # exponentiation (a to the power b)
-a           # negation
```

The two that surprise people:

```python
7 / 2        # 3.5 — / always gives a float, even with integers
7 // 2       # 3 — floor division, drops the .5
-7 // 2      # -4 — rounds toward negative infinity, not toward zero
7 % 2        # 1 — remainder
2 ** 10      # 1024
```

`%` (modulo) is incredibly useful. `n % 2` is 0 for even, 1 for odd. `n % 60` "wraps" `n` into the range 0-59.

### Comparison operators

All return a bool.

```python
a == b       # equal
a != b       # not equal
a < b        # less than
a > b        # greater than
a <= b       # less than or equal
a >= b       # greater than or equal
```

Comparisons can be **chained** in Python:

```python
0 < x < 10                 # same as (0 < x) and (x < 10)
a == b == c                # all three are equal
```

This is a Python superpower — most languages don't allow this.

### Logical operators

```python
a and b      # True if both are truthy
a or b       # True if at least one is truthy
not a        # opposite of a's truthiness
```

`and` and `or` are **short-circuit** — they stop evaluating as soon as the answer is known:

```python
True or expensive_function()      # expensive_function never runs
False and expensive_function()    # never runs

# common idiom — use a default value if the first one is falsy
name = user_input or "anonymous"
```

⚠ Don't confuse `and`/`or`/`not` with `&`/`|`/`~` — the latter are bitwise (covered below).

### Assignment operators

```python
x = 5                # assign
x += 1               # same as x = x + 1
x -= 1               # x = x - 1
x *= 2               # x = x * 2
x /= 2               # x = x / 2
x //= 2              # x = x // 2
x %= 3               # x = x % 3
x **= 2              # x = x ** 2

# also works for strings, lists
s = "hello"
s += " world"        # "hello world"

nums = [1, 2]
nums += [3, 4]       # [1, 2, 3, 4]
```

### Identity operators

```python
a is b           # True if a and b are the SAME object in memory
a is not b
```

Use `is` for `None`, `True`, `False` — never for equality of other values:

```python
if x is None: ...               # ✓ correct
if x is True: ...               # ✓ correct (rare)
if name is "Sid": ...           # ✗ might work by coincidence, but use ==
```

The difference between `==` (equal values) and `is` (same object):
```python
a = [1, 2, 3]
b = [1, 2, 3]
a == b           # True — same values
a is b           # False — they're two different list objects
a is a           # True — same object as itself
```

### Membership operators

```python
x in collection         # True if x is in the list/tuple/set/dict/string
x not in collection
```

```python
"x" in "alex"                   # True (substring check)
3 in [1, 2, 3, 4]               # True
"name" in {"name": "Sid"}       # True (checks keys of a dict)
```

Constant-time for `set` and `dict`. Linear-time for `list` and `tuple` (it scans). When you find yourself doing many membership checks, convert to a set first.

### Bitwise operators

Operate on the binary representation of integers. You'll meet these less often, but they're real Python.

```python
a & b        # bitwise AND
a | b        # bitwise OR
a ^ b        # bitwise XOR
~a           # bitwise NOT (flip all bits)
a << n       # shift bits left by n positions (= multiply by 2^n)
a >> n       # shift bits right by n positions (= divide by 2^n)
```

In ML you'll mostly see these in:
- PyTorch / NumPy boolean masks: `mask & other_mask` (element-wise AND on arrays).
- Bit packing for efficient storage.

### Operator precedence

What gets computed first when you write `a + b * c`? Python's order:

1. `**` (power)
2. `+x -x ~x` (unary)
3. `* / // %`
4. `+ -`
5. `<< >>`
6. `&`
7. `^`
8. `|`
9. `== != < > <= >= is is not in not in`
10. `not`
11. `and`
12. `or`

**Don't memorize.** Just use parentheses when in doubt. `(a + b) * c` is always clearer than relying on precedence.

---

## 3.6 · Strings — the essentials

Strings show up everywhere. The core operations:

### Concatenation and repetition

```python
"hello" + " " + "world"          # "hello world"
"ha" * 3                         # "hahaha"
```

### Length

```python
len("hello")                     # 5
len("")                          # 0
```

### Indexing — zero-based

```python
s = "hello"
s[0]      # "h"
s[1]      # "e"
s[4]      # "o"
s[-1]     # "o" — negative indexing from the end
s[-2]     # "l"
s[100]    # IndexError — out of range
```

### Slicing — half-open intervals

`s[start:stop]` gives you characters from `start` (inclusive) to `stop` (exclusive):

```python
s = "hello"
s[1:4]      # "ell"     — indices 1, 2, 3
s[:3]       # "hel"     — from start
s[2:]       # "llo"     — to end
s[:]        # "hello"   — a full copy
s[::2]      # "hlo"     — every 2nd character
s[::-1]     # "olleh"   — reversed (the classic Python trick)
```

Same slicing rules apply to lists and tuples.

### Useful string methods

```python
s = "Hello World"

s.lower()                  # "hello world"
s.upper()                  # "HELLO WORLD"
s.title()                  # "Hello World"
s.strip()                  # removes whitespace from both ends
s.startswith("Hello")      # True
s.endswith("World")        # True
s.replace("World", "Sid")  # "Hello Sid"
s.split(" ")               # ["Hello", "World"]
" ".join(["a", "b", "c"])  # "a b c"
s.find("World")            # 6 — index where "World" starts, or -1 if not found
s.count("l")               # 3
```

`split` and `join` are the workhorses of text processing. Memorize them.

### String formatting — the f-string

There are 3 ways to interpolate values into a string. **Use f-strings.** They're the modern, readable default.

```python
name = "Sid"
age = 30

# 1. f-string (USE THIS)
f"Name: {name}, Age: {age}"          # "Name: Sid, Age: 30"
f"{age * 2}"                          # "60" — expressions work too
f"{age:>5}"                           # "   30" — right-aligned in 5 chars
f"{3.14159:.2f}"                      # "3.14" — 2 decimal places
f"{1234567:,}"                        # "1,234,567" — thousands separator

# 2. .format() — older, more verbose
"Name: {}, Age: {}".format(name, age)
"Name: {n}, Age: {a}".format(n=name, a=age)

# 3. % — really old, avoid in new code
"Name: %s, Age: %d" % (name, age)
```

F-string format spec cheat sheet (the bit after `:`):

```python
f"{x:.3f}"       # 3 decimal places — "3.142"
f"{x:.0f}"       # no decimals     — "3"
f"{x:5}"         # min width 5
f"{x:>5}"        # right-aligned
f"{x:<5}"        # left-aligned
f"{x:^5}"        # centered
f"{x:0>5}"       # zero-padded     — "00042"
f"{x:%}"         # percentage      — "50.000000%"
f"{x:.2%}"       # percentage 2dp  — "50.00%"
f"{x:e}"         # scientific      — "1.500000e+03"
f"{x:,}"         # thousands sep   — "1,000,000"
f"{x:b}"         # binary
f"{x:x}"         # hex
```

---

## 3.7 · `print()` and `input()`

### `print()`

Writes things to the terminal.

```python
print("hello")                        # hello
print("hello", "world")               # hello world      (space-separated)
print("a", "b", "c", sep="-")         # a-b-c            (custom separator)
print("no newline", end="")           # doesn't add a newline at the end
print(f"x = {x}")                     # with f-string
```

You can print any value — Python converts it to a string automatically:

```python
print(42)                             # 42
print([1, 2, 3])                      # [1, 2, 3]
print({"a": 1})                       # {'a': 1}
print(None)                           # None
```

### `input()`

Reads a line of text from the user.

```python
name = input("Your name: ")           # prompts, reads, stores in name
print(f"Hi {name}!")
```

⚠ **`input()` always returns a string.** Even if the user types `42`, you get `"42"`. To get a number, cast it:

```python
age = int(input("Your age: "))        # crashes if user types non-number
```

Wrap that in a `try/except` (chapter 6) when you want it to handle bad input gracefully.

---

## 3.8 · The errors you'll meet in week one

Reading the error tells you 90% of what you need. Here are the ones you'll see most:

| Error | What it means | Common cause |
|-------|---------------|--------------|
| `SyntaxError` | Python can't parse your code at all | Missing colon, unmatched bracket, typo in keyword |
| `IndentationError` | Indentation is wrong or inconsistent | Mixed tabs and spaces, missing indent after `:` |
| `NameError` | A name you used isn't defined | Typo in a variable name, used before assignment |
| `TypeError` | Operation doesn't fit the types | `"5" + 3` (can't add str + int), `len(5)` (int has no len) |
| `ValueError` | Right type, bad value | `int("hello")`, `math.sqrt(-1)` |
| `IndexError` | List/tuple index out of range | `my_list[100]` when list has 3 items |
| `KeyError` | Dict key doesn't exist | `my_dict["missing"]` |
| `ZeroDivisionError` | Divided by zero | `1 / 0` |
| `AttributeError` | Tried to access a method/attr that doesn't exist | `"hello".sort()` (strings don't sort) |
| `FileNotFoundError` | File path doesn't exist | Wrong path, wrong working directory |
| `ImportError` / `ModuleNotFoundError` | Couldn't import the module | Not installed, typo in the name |

Every error message also gives you a **traceback** — the chain of function calls that led to the crash. Read it bottom-up. The bottom line is the actual error; the lines above show you the path it took to get there.

---

## 3.9 · Practice — three things to do before moving on

1. **Open the python-and-dsa playground** ([`../prog/python-and-dsa/`](../prog/python-and-dsa/)) and do Lessons 1-4 (Hello World, Variables, Numbers & Math, Strings). About 30 minutes. You're applying everything in this chapter.

2. **In the REPL, type these and predict the output before pressing Enter.** Then check. Each one tests one concept from this chapter.

```python
type(3 / 2)
type(3 // 2)
"5" * 3
3 * "5"
bool("")
bool(" ")
[1, 2] + [3, 4]
[1, 2] * 2
0.1 + 0.2 == 0.3
list("hello")
"abc"[::-1]
f"{1/3:.2f}"
```

3. **Make every error happen at least once.** Open the REPL and deliberately trigger:
   - A `SyntaxError` (forget a colon)
   - A `TypeError` (try `"5" + 3`)
   - A `NameError` (use a variable you never defined)
   - A `ZeroDivisionError`
   - An `IndexError`

   You'll start seeing errors as data, not as failure.

<details>
<summary>Predicted outputs</summary>

```python
type(3 / 2)           # <class 'float'>           — / always gives float
type(3 // 2)          # <class 'int'>             — // gives int (when both are int)
"5" * 3               # "555"                     — string repetition
3 * "5"               # "555"                     — same, commutative
bool("")              # False                     — empty string is falsy
bool(" ")             # True                      — space is not empty
[1, 2] + [3, 4]       # [1, 2, 3, 4]              — list concatenation
[1, 2] * 2            # [1, 2, 1, 2]              — list repetition
0.1 + 0.2 == 0.3      # False                     — float precision
list("hello")         # ['h', 'e', 'l', 'l', 'o']
"abc"[::-1]           # "cba"                     — reverse via slice
f"{1/3:.2f}"          # "0.33"                    — 2 decimal places
```
</details>

---

## Where to next

→ [04-flow-and-collections.md](04-flow-and-collections.md) — if/else, loops, list / dict / set / tuple in depth.

Or jump back to the [pre-foundations index](README.md).

---

## Further reading

- [w3schools Python syntax](https://www.w3schools.com/python/python_syntax.asp) — same material, tighter.
- [w3schools Python datatypes](https://www.w3schools.com/python/python_datatypes.asp).
- [w3schools Python operators](https://www.w3schools.com/python/python_operators.asp).
- [Python docs — built-in types](https://docs.python.org/3/library/stdtypes.html) — the authoritative reference. Skim, don't read.
- [Python docs — string formatting mini-language](https://docs.python.org/3/library/string.html#format-specification-mini-language) — every f-string format spec.
