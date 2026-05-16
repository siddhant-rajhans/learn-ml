# Python & DSA — Recording Script

> Tone: calm, direct, like a senior dev explaining to a curious friend. No filler. No hype.

---

## OPEN (30s)

Python is the language of ML. You don't need to master it — you need to be comfortable enough that the code doesn't slow down your thinking. That's what this is for. Ten lessons. Run everything yourself. Let's go.

---

## FOUNDATIONS

### 01 — Hello, World.
Every program you'll ever write starts with this idea — give the computer something to say.
`print()` is Python talking back to you. Whatever you put inside the brackets, it shows below.
Hit Run. Change the message. Run it again. That loop — write, run, see — is how you learn to code.

### 02 — Variables.
Variables are names for values. You're not storing the number 25 — you're calling it `age`.
Three things to notice: integers, floats, booleans. No type declarations, Python figures it out.
`type()` tells you what something is. Use it whenever you're not sure.

### 03 — Numbers & math.
`+  -  *  /` — that's 90% of it. Two extras worth knowing:
`//` is floor division — drops the decimal. `%` is modulo — gives you the remainder.
Modulo is everywhere in DSA. You'll see it in hashing, in cyclic problems, in binary search.

### 04 — Strings.
Text. Single quotes, double quotes — same thing.
Three operations: concatenate with `+`, repeat with `*`, slice with `[start:end]`.
f-strings are the clean way to mix variables into sentences. Write one. Run it.

### 05 — If, else.
Decision making. `if condition:` — if true, run this block. `else:` — otherwise, run that one.
Indentation is not optional in Python. The indent IS the block. Two spaces or four, pick one, be consistent.
`elif` chains multiple conditions. Keep them ordered — Python stops at the first true one.

### 06 — Loops.
`for item in collection:` — for each thing, do something.
`range(n)` gives you 0 through n-1. `range(2, 10, 2)` gives you evens.
`while condition:` keeps running until the condition is false. Every infinite loop you've accidentally written started here.

### 07 — Functions.
`def name(parameters):` — you're defining a reusable block.
`return` sends a value back. Without it, Python returns `None`.
Functions are how you stop repeating yourself. Any code you write more than twice belongs in a function.

---

## DATA STRUCTURES

### 08 — Lists.
Ordered. Mutable. Zero-indexed.
`append()` adds to the end. `pop()` removes from the end. Slicing gives you a sub-list.
Lists are your default container for sequences. Most DSA problems start with a list.

### 09 — Dictionaries.
Key-value pairs. Lookup in O(1) — constant time, no matter how big the dictionary.
`dict[key]` gets a value. `dict[key] = value` sets one. `.get(key, default)` avoids KeyError.
When you see "count occurrences" or "cache a result" — reach for a dict.

---

## ALGORITHMS

### 10 — Binary Search.
The problem: find a value in a sorted list. The naive way — check every element — is O(n).
Binary search cuts the search space in half every step. That's O(log n). On a million items, that's 20 comparisons instead of a million.
Watch the animation. `lo` and `hi` close in. `mid` is always the halfway point. Every ML search, every database index — this idea underneath.

---

## CLOSE (20s)

That's the foundation. Not everything — the foundation. Variables, control flow, functions, two data structures, one algorithm that shows up everywhere.
Next: we take this into the math that ML actually runs on. Linear algebra, visualized.

---

*[cut to next video / end screen]*
