# 04 · Flow and collections

← previous: [03-python-syntax-and-data.md](03-python-syntax-and-data.md) · next: [05-functions-modules-files.md](05-functions-modules-files.md)

This is where Python starts feeling like Python.

`if`, `else`, `while`, `for`. Lists, tuples, sets, dictionaries. List comprehensions, which are the thing Python programmers like to show off about. By the end you can write programs that loop over data and make decisions about it. Most programs are that.

Picking a container is a habit you build. Lists most of the time. Dicts more than you'd think. Tuples for fixed-shape things. Sets when you need to dedupe or check "is this in there?" fast. That's the heuristic. The rest is detail.

---

## 4.1 · if / elif / else

Branching is choosing one path based on a condition.

```python
x = 5

if x > 0:
    print("positive")
elif x < 0:
    print("negative")
else:
    print("zero")
```

The flow:

1. Python checks `x > 0`. If True, run that block and skip the rest.
2. Otherwise, check `x < 0`. If True, run that block.
3. Otherwise (`else`), run the else block.

You can have any number of `elif` branches, or none. `else` is optional.

### Conditions can be any expression

If it evaluates to something truthy, the branch runs:

```python
name = input("Your name: ")
if name:                   # truthy if not empty
    print(f"Hi {name}")
else:
    print("No name given")

if my_list:                # truthy if non-empty
    print(f"First item: {my_list[0]}")
```

### Combining conditions

```python
if x > 0 and x < 100:
    print("in range")

# better — Python lets you chain comparisons
if 0 < x < 100:
    print("in range")

if x < 0 or x > 100:
    print("out of range")

if not is_ready:
    print("not ready")
```

### Nested vs flat

```python
# nested — works, but harder to read
if x > 0:
    if x < 10:
        print("small positive")

# flatter — easier to read
if x > 0 and x < 10:
    print("small positive")

# even better — chained comparison
if 0 < x < 10:
    print("small positive")
```

**Flat beats nested.** A common refactor: flip an `if` to an early return so the rest of the function isn't indented inside it. We'll see this in chapter 5.

### The ternary expression

A compact one-line if/else, when you just need a value:

```python
status = "adult" if age >= 18 else "minor"
sign = "+" if x >= 0 else "-"
result = compute() if data else default
```

Read it as *"X if condition else Y."* Use sparingly — it's nice for short cases, gets unreadable fast for long expressions.

---

## 4.2 · `while` loops

A `while` runs as long as a condition is true.

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

**The condition must eventually become false** — or you have an infinite loop. (Ctrl+C in the terminal kills it.)

Use `while` when:
- You don't know in advance how many times to loop.
- You're polling something (keep going until the user types "quit").
- You're searching until a condition is met.

Don't use `while` when you have a fixed sequence to iterate over — use `for`.

```python
# good while — unknown number of iterations
while True:
    user_input = input("> ")
    if user_input == "quit":
        break
    process(user_input)
```

---

## 4.3 · `for` loops

A `for` iterates over a sequence — list, tuple, string, dict, file, anything iterable.

```python
for item in [10, 20, 30]:
    print(item)
# prints 10, 20, 30

for char in "hello":
    print(char)
# prints h, e, l, l, o

for line in open("data.txt"):
    process(line)
# iterates lines of a file
```

This is the workhorse loop in Python. You'll use it ten times more than `while`.

### `range()` — counting

`range(stop)` gives you `0, 1, 2, ..., stop-1`. `range(start, stop)` and `range(start, stop, step)` are the other variants.

```python
for i in range(5):
    print(i)
# 0, 1, 2, 3, 4

for i in range(2, 8):
    print(i)
# 2, 3, 4, 5, 6, 7

for i in range(0, 20, 5):
    print(i)
# 0, 5, 10, 15

for i in range(10, 0, -1):
    print(i)
# 10, 9, 8, ..., 1
```

`range` is **half-open** — includes `start`, excludes `stop`. Same convention as slicing. `range(5)` has 5 elements, indices 0 to 4. This is what people mean by "0-indexed."

### `enumerate()` — both index and value

When you need to know *where* you are in a loop:

```python
fruits = ["apple", "banana", "cherry"]

for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
# 0: apple
# 1: banana
# 2: cherry
```

Better than `for i in range(len(fruits)): ... fruits[i]` — more Pythonic, doesn't break if the list is something other than a list.

### `zip()` — iterate over two (or more) things together

```python
names = ["Alice", "Bob", "Carol"]
ages = [30, 25, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age}")
# Alice is 30
# Bob is 25
# Carol is 35
```

`zip` stops at the shorter sequence. To go to the longer, `itertools.zip_longest`.

### `break`, `continue`, and the loop `else`

```python
# break — leave the loop immediately
for x in [1, 2, 3, 4, 5]:
    if x == 3:
        break
    print(x)
# 1, 2

# continue — skip to the next iteration
for x in [1, 2, 3, 4, 5]:
    if x % 2 == 0:
        continue
    print(x)
# 1, 3, 5

# else on a loop — runs if the loop completed WITHOUT break
for x in [1, 2, 3]:
    if x == 99:
        break
else:
    print("never found 99")
# never found 99
```

The `else` on loops is rarely used and surprises people. Don't worry about it — just recognize it.

### `pass` — explicit do-nothing

```python
if x > 0:
    pass    # TODO: handle the positive case later
else:
    print("not positive")
```

Useful as a placeholder so the syntax is valid while you stub out code.

---

## 4.4 · Lists in depth

A list is an ordered, mutable sequence. Square brackets.

```python
nums = [10, 20, 30, 40]
mixed = [1, "hello", True, [1, 2]]      # any types, including nested lists
empty = []
```

### Indexing and slicing

Same rules as strings (covered in chapter 3):

```python
nums[0]         # 10
nums[-1]        # 40
nums[1:3]       # [20, 30]
nums[:2]        # [10, 20]
nums[::-1]      # [40, 30, 20, 10]
```

### Modifying

Lists are mutable — you can change them in place:

```python
nums = [10, 20, 30]

nums[0] = 99                 # [99, 20, 30] — replace one item
nums.append(40)              # [99, 20, 30, 40] — add to end
nums.extend([50, 60])        # [99, 20, 30, 40, 50, 60] — add many
nums.insert(0, 5)            # [5, 99, 20, 30, ...] — insert at index
nums.pop()                   # returns 60, list is now [5, 99, 20, 30, 40, 50]
nums.pop(0)                  # returns 5, removes from index 0
nums.remove(99)              # removes first occurrence of 99
nums.clear()                 # []
```

### Sorting

```python
nums = [3, 1, 4, 1, 5, 9, 2, 6]

nums.sort()                  # sorts IN PLACE, returns None
                             # nums is now [1, 1, 2, 3, 4, 5, 6, 9]

# OR — make a sorted copy without changing the original
sorted_nums = sorted(nums)

# reverse order
nums.sort(reverse=True)

# sort by a key
words = ["banana", "apple", "cherry"]
words.sort(key=len)          # by length: ["apple", "banana", "cherry"]
```

### Searching and counting

```python
nums = [10, 20, 30, 20, 40]

len(nums)                    # 5
30 in nums                   # True
nums.index(20)               # 1 — first index of 20
nums.count(20)               # 2 — how many 20s
min(nums)                    # 10
max(nums)                    # 40
sum(nums)                    # 120
```

### Copying — the gotcha

```python
a = [1, 2, 3]
b = a                        # b is the SAME LIST as a (just another name)
b.append(4)
print(a)                     # [1, 2, 3, 4] — a changed!

# to make a real copy:
b = a.copy()                 # or list(a), or a[:]
b.append(4)
print(a)                     # [1, 2, 3] — unchanged
```

This bites everyone once. The rule: assignment doesn't copy. To copy, you have to be explicit.

### List comprehensions

The most distinctive Python feature. A compact way to build a list from another iterable.

```python
# old way — works but verbose
squares = []
for x in range(10):
    squares.append(x ** 2)

# list comprehension — same result
squares = [x ** 2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

With a filter:

```python
evens = [x for x in range(20) if x % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# both a transformation and a filter
even_squares = [x ** 2 for x in range(20) if x % 2 == 0]
```

Comprehensions exist for dicts and sets too:

```python
squares_dict = {x: x ** 2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

unique_first_letters = {word[0] for word in ["apple", "banana", "avocado"]}
# {'a', 'b'}
```

Use comprehensions when the logic is simple — one line. If you need nested ifs or complex transformations, write a regular for loop. Readability over cleverness.

---

## 4.5 · Tuples in depth

Like a list, but immutable.

```python
point = (3, 4)
rgb = (255, 128, 0)
single = (5,)         # trailing comma needed — (5) is just 5 in parens
empty = ()
```

Many tuple operations are the same as lists (indexing, slicing, `len`, `in`, `count`, `index`). What you *can't* do is modify them:

```python
point = (3, 4)
point[0] = 5         # TypeError — tuples are immutable
```

### Why use tuples?

1. **Signal that a sequence is fixed.** Coordinates `(x, y)`, RGB `(r, g, b)`, a date `(year, month, day)`.
2. **Multiple return values.** A common Python pattern:
   ```python
   def min_max(nums):
       return min(nums), max(nums)        # returns a tuple

   lo, hi = min_max([3, 1, 4, 1, 5])      # unpacking — lo = 1, hi = 5
   ```
3. **Dict keys.** Tuples are hashable (because immutable), so they can be dict keys. Lists can't.
   ```python
   distances = {("New York", "LA"): 2451, ("NY", "Chicago"): 711}
   ```
4. **Faster and smaller than lists.** Marginal, but real for large datasets.

### Unpacking

You can unpack a tuple (or list) into multiple variables:

```python
point = (3, 4)
x, y = point                         # x = 3, y = 4

a, b, c = [1, 2, 3]                 # works for lists too

# Swap variables — no temp needed
a, b = b, a

# *rest captures the leftover
first, *rest = [1, 2, 3, 4, 5]      # first = 1, rest = [2, 3, 4, 5]
*init, last = [1, 2, 3, 4, 5]       # init = [1, 2, 3, 4], last = 5
first, *middle, last = [1, 2, 3, 4, 5]   # first=1, middle=[2,3,4], last=5
```

---

## 4.6 · Sets in depth

Unordered, unique, mutable. Curly braces with values:

```python
nums = {1, 2, 3, 4}
empty = set()         # NOT {} — that's an empty dict

# from a list
unique = set([1, 1, 2, 2, 3])    # {1, 2, 3}
```

### Operations

```python
nums = {1, 2, 3}

nums.add(4)                   # {1, 2, 3, 4}
nums.add(2)                   # no effect — already there
nums.remove(3)                # {1, 2, 4} — KeyError if not present
nums.discard(99)              # no error if not present
nums.pop()                    # removes arbitrary element (sets are unordered)
3 in nums                     # True / False — VERY FAST (~O(1))
len(nums)
```

### Set operations (mathematical)

```python
a = {1, 2, 3}
b = {3, 4, 5}

a | b           # union           {1, 2, 3, 4, 5}
a & b           # intersection    {3}
a - b           # difference      {1, 2}     (in a but not in b)
a ^ b           # symmetric diff  {1, 2, 4, 5}  (in either, not both)

a.issubset(b)               # False
a.issuperset({1, 2})        # True
a.isdisjoint({99, 100})     # True
```

### When to use a set

1. **Fast membership checks.** `x in my_set` is O(1) — instant, regardless of size. `x in my_list` is O(n) — scans through.
2. **Removing duplicates.** `unique = set(my_list)` then back to list if order matters: `unique = list(set(my_list))` (but order is lost).
3. **Set math.** Comparing two collections — what's shared, what's different.

```python
visitors_jan = {"alice", "bob", "carol"}
visitors_feb = {"bob", "dave"}

returning = visitors_jan & visitors_feb       # {"bob"}
new_in_feb = visitors_feb - visitors_jan      # {"dave"}
all_visitors = visitors_jan | visitors_feb    # {"alice", "bob", "carol", "dave"}
```

---

## 4.7 · Dictionaries in depth

The most-used Python container after `list`. Key-value pairs. Curly braces with `:`.

```python
person = {"name": "Sid", "age": 30, "city": "Hoboken"}
empty = {}
```

### Lookup, insert, delete

```python
person["name"]            # "Sid"
person["age"] = 31        # update existing key
person["job"] = "ML"      # add new key
del person["city"]        # delete a key

"name" in person          # True
"missing" in person       # False

person["missing"]         # KeyError
person.get("missing")     # None — no error
person.get("missing", "default")  # "default" if not present
```

### Iterating

By default, iterating a dict gives you the keys:

```python
person = {"name": "Sid", "age": 30}

for key in person:
    print(key)                # "name", "age"

for key in person.keys():     # explicit version of the same
    print(key)

for value in person.values():
    print(value)              # "Sid", 30

for key, value in person.items():
    print(f"{key}: {value}")  # "name: Sid", "age: 30"
```

`.items()` is the one you'll use most.

### Useful methods

```python
person.keys()                 # dict_keys(['name', 'age'])
person.values()               # dict_values(['Sid', 30])
person.items()                # dict_items([('name', 'Sid'), ('age', 30)])
person.update({"age": 31, "city": "Hoboken"})    # bulk update / merge
person.pop("age")             # returns 30, removes the key
person.clear()                # empty the dict
len(person)                   # number of keys
```

### Dict keys must be hashable

Immutable types (str, int, float, tuple of hashables, frozenset) — yes. Lists, sets, dicts — no.

```python
d = {(1, 2): "point a", "name": "sid"}    # OK — tuple key
d = {[1, 2]: "oops"}                       # TypeError — list isn't hashable
```

Values can be anything — no restrictions.

### Nested dicts

The natural shape of structured data:

```python
config = {
    "model": {
        "type": "resnet",
        "layers": 50,
    },
    "optimizer": {
        "name": "adam",
        "lr": 0.001,
    },
}

config["model"]["layers"]              # 50
config["optimizer"]["lr"] = 0.0001     # change a nested value
```

This is essentially JSON (covered in chapter 6).

### Dict comprehensions

```python
squares = {x: x ** 2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# invert a dict
person = {"name": "Sid", "age": 30}
inverted = {v: k for k, v in person.items()}
# {"Sid": "name", 30: "age"}

# filter
big = {k: v for k, v in numbers.items() if v > 10}
```

---

## 4.8 · The four containers — when to use which

| Container | Ordered | Mutable | Allows duplicates | Lookup speed | When |
|-----------|---------|---------|-------------------|--------------|------|
| `list` | ✓ | ✓ | ✓ | O(n) to find | A sequence of things you'll iterate or modify. The default. |
| `tuple` | ✓ | ✗ | ✓ | O(n) to find | A fixed sequence — coordinates, records, multiple return values. |
| `set` | ✗ | ✓ | ✗ | O(1) to check membership | Unique items, fast membership tests, set math. |
| `dict` | ✓ (insertion order, Python 3.7+) | ✓ | keys ✗, values ✓ | O(1) to look up | Looking things up by a key. |

**Default heuristic:**
- A bunch of things in order? `list`.
- A pair / fixed record / things that shouldn't change? `tuple`.
- Just need to know "is X in this collection"? `set`.
- Mapping one thing to another? `dict`.

---

## 4.9 · The `match` statement (Python 3.10+)

A switch-like construct for pattern matching:

```python
def describe(point):
    match point:
        case (0, 0):
            return "origin"
        case (x, 0):
            return f"on x-axis at {x}"
        case (0, y):
            return f"on y-axis at {y}"
        case (x, y):
            return f"point at ({x}, {y})"
        case _:
            return "not a point"
```

`_` is the catch-all. You can match against literals, tuples, lists, dicts, types, and more.

Use sparingly — for many cases a chain of `if/elif` is clearer. `match` shines when you're destructuring nested data (parsing JSON, AST nodes, etc.).

---

## 4.10 · Practice — four things to do before moving on

1. **Open the python-and-dsa playground** and do Lessons 5-8 (If/else, Loops, Functions, Lists). About 45 minutes.

2. **Write a histogram.** Given a list like `["apple", "banana", "apple", "cherry", "banana", "apple"]`, build a dict that counts each word. Try it with a regular for-loop first, then with `dict.get(key, 0) + 1`, then look up `collections.Counter` (the cheating way).

3. **Convert these forms back and forth.** Take a list of names. Make a set of unique names. Make a dict mapping each name to its length. Iterate, sort, slice. Twenty minutes of playing with the four containers does more than reading them.

4. **Predict the output:**

```python
# A
nums = [1, 2, 3]
copy_a = nums
copy_b = nums.copy()
nums.append(4)
print(copy_a, copy_b)

# B
words = ["apple", "banana", "cherry"]
result = [w.upper() for w in words if "a" in w]
print(result)

# C
person = {"a": 1, "b": 2}
person["c"] = 3
for key in person:
    print(key, end=" ")

# D
s = {1, 2, 3}
s.add(2)
s.add(4)
print(sorted(s))
```

<details>
<summary>Answers</summary>

A. `[1, 2, 3, 4] [1, 2, 3]` — `copy_a` is the same list as `nums`, `copy_b` is a real copy.

B. `['APPLE', 'BANANA']` — "cherry" has no "a", gets filtered out; the rest uppercase.

C. `a b c ` — dicts preserve insertion order since Python 3.7.

D. `[1, 2, 3, 4]` — `add(2)` does nothing (already there), `add(4)` works. `sorted()` returns a list.
</details>

---

## Where to next

→ [05-functions-modules-files.md](05-functions-modules-files.md) — functions, modules, files, the rest of the toolkit.

Or jump back to the [pre-foundations index](README.md).

---

## Further reading

- [w3schools Python conditions](https://www.w3schools.com/python/python_conditions.asp)
- [w3schools Python loops](https://www.w3schools.com/python/python_for_loops.asp)
- [w3schools Python lists / tuples / sets / dictionaries](https://www.w3schools.com/python/python_lists.asp) — one page per container.
- [Python docs — `collections`](https://docs.python.org/3/library/collections.html) — when you outgrow the built-in containers, this is where you go. `Counter`, `defaultdict`, `deque`, `OrderedDict`, `namedtuple`.
