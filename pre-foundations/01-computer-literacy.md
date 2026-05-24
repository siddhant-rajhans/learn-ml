# 01 · Computer literacy

> *"Almost every tutorial assumes you know what a 'file path' is. This file explains it."*

← [back to pre-foundations](README.md) · next: [02-math-zero.md](02-math-zero.md)

---

## What you'll know by the end

- What a file, folder, path, and extension actually are.
- What a terminal is and the ~12 commands you'll use forever.
- How to install Python and run a script.
- How to use a text editor like a tool, not a Word doc.
- What the browser's "developer tools" are and why you'd ever open them.
- A small vocabulary of words that show up everywhere: process, RAM, encoding, URL.

---

## 1.1 · Files, folders, paths

Your computer stores everything in **files**. A file has:

- A **name** — `homework.docx`, `vacation.jpg`, `train.py`.
- An **extension** — the bit after the dot. Tells you what's inside. `.txt` = plain text, `.py` = Python source, `.jpg` = photo, `.csv` = spreadsheet-shaped data. The extension is just a hint; renaming a `.jpg` to `.py` doesn't make it Python.
- **Contents** — anywhere from 0 bytes (empty) to gigabytes.

Files live in **folders** (aka *directories*). Folders can contain other folders. The whole thing is a tree.

A **path** is the address of a file. Two flavors:

```
absolute path:  C:\Users\sid\projects\learn-ml\README.md       (Windows)
absolute path:  /Users/sid/projects/learn-ml/README.md         (Mac / Linux)
relative path:  projects/learn-ml/README.md                    (from your home folder)
relative path:  ./README.md                                    (from the current folder; . means "here")
relative path:  ../README.md                                   (from one folder up; .. means "parent")
```

Three rules:

1. Windows uses `\` (backslash) as the separator. Mac and Linux use `/` (forward slash). Most modern tools accept both — but if a script breaks on Windows, this is one place to check.
2. Spaces in paths are a real pain. `My Projects/learn ml/script.py` will confuse the terminal. When you can, name folders `my-projects` or `my_projects` or `myProjects`. Pick one style and stick with it.
3. The path is *case-sensitive* on Mac/Linux. `README.md` and `readme.md` are different files. On Windows they're treated as the same file.

### A useful mental picture

When a tutorial says *"open a terminal in the project folder and run `python script.py`"*, what's actually happening:

1. The terminal has a notion of a **current working directory** — *which folder am I standing in?*
2. `python script.py` says *"find the file `script.py` in the current directory and feed it to the Python interpreter."*
3. If the file isn't in your current directory, Python prints `python: can't open file 'script.py': [Errno 2] No such file or directory`. The error isn't lying — the file genuinely isn't where Python looked.

This is the most common newbie source of confusion. **The terminal is somewhere.** Where you are matters.

---

## 1.2 · The terminal

The terminal (aka *shell*, *command line*, *console*) is a text interface to your computer. You type commands, it does things.

### Opening one

- **Mac:** ⌘ + Space → type `Terminal` → Enter. Or use [iTerm2](https://iterm2.com).
- **Windows:** Win key → type `Terminal` → Enter. (Use *Windows Terminal*, not the older `cmd.exe`.) Or install [Git Bash](https://git-scm.com/downloads) for a Mac-like experience.
- **Linux:** ctrl + alt + T usually works. Otherwise look for "Terminal" in your apps.

When it opens, you see a **prompt** — something like `sid@laptop:~$ ` or `PS C:\Users\sid>`. The `~` (tilde) means *your home folder*.

### The commands you'll actually use

| Command | What it does | Example |
|---------|--------------|---------|
| `pwd` | "print working directory" — where am I right now? | `pwd` |
| `ls` | list files in the current folder | `ls` or `ls -la` (with details) |
| `cd` | "change directory" — move to a different folder | `cd projects` or `cd ..` (up one) or `cd ~` (home) |
| `mkdir` | make a new folder | `mkdir my-project` |
| `touch` | make a new empty file (Mac/Linux) | `touch script.py` |
| `cp` | copy a file | `cp script.py backup.py` |
| `mv` | move or rename a file | `mv script.py main.py` |
| `rm` | delete a file (**no undo, no trash**) | `rm temp.txt` |
| `cat` | print a file's contents to the screen | `cat README.md` |
| `clear` | wipe the screen | `clear` |
| `python --version` | check Python is installed and what version | `python --version` |
| `python script.py` | run a Python script | `python script.py` |

**On Windows**, the same commands exist but some are slightly different. In PowerShell: `pwd` works, `ls` works (it's aliased to `Get-ChildItem`), `cd` works, `mkdir` works. `touch` doesn't exist — use `New-Item -ItemType File script.py` or just create the file in your editor.

### The tab key is your friend

In the terminal, **press tab to autocomplete**. Type `cd proj` then tab — if there's only one folder starting with `proj`, the terminal completes it for you. If there are several, tab twice shows you the options. Use this constantly. It prevents typos.

### Up-arrow

Press the ↑ arrow in the terminal — it brings back the previous command. Press it again — the one before that. This is how everybody navigates their command history.

### When something goes wrong

Read the error message. Terminal errors are surprisingly readable when you're not panicked.

```
$ python scrpit.py
python: can't open file 'scrpit.py': [Errno 2] No such file or directory
```

That's saying *"I looked for a file named `scrpit.py` and didn't find one."* You typed it wrong. Fix the typo. (Use tab-complete next time.)

---

## 1.3 · Installing Python

Python is a programming language. To run Python code, you need the Python *interpreter* installed on your machine.

### Easy mode — Mac/Linux

Most Macs and Linuxes ship with some Python. Check:

```
python3 --version
```

If you see something like `Python 3.11.5`, you're done.

If not, install [Python from python.org](https://www.python.org/downloads/) (download the latest, follow the installer). Then check again.

### Easy mode — Windows

Install Python from [python.org](https://www.python.org/downloads/). **Critically: during installation, check the box that says "Add Python to PATH."** Without it, the terminal won't find Python.

Then check:

```
python --version
```

### Modern mode (recommended) — uv

[`uv`](https://docs.astral.sh/uv/) is a faster, cleaner way to manage Python and packages. Install it once, then you never need to touch the system Python again.

```
# Mac / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Then to install a Python version:

```
uv python install 3.12
```

You'll see why this matters in chapter 5 (virtual environments). For now: knowing `uv` exists is enough.

### Running your first Python script

Make a folder somewhere:

```
mkdir hello-python
cd hello-python
```

Open your text editor and create a file called `hello.py` with this in it:

```python
print("Hello from Python")
```

Save. Back to the terminal:

```
python hello.py
```

You should see `Hello from Python`. **You're a programmer now.** Everything from here is more of the same.

---

## 1.4 · The Python REPL

Type `python` (no script name) in the terminal and you get the **REPL** — Read-Eval-Print Loop. It's an interactive Python session where you can type code one line at a time and see results immediately.

```
$ python
Python 3.12.0 (...)
>>> 2 + 2
4
>>> name = "Sid"
>>> print(f"Hello {name}")
Hello Sid
>>> exit()
```

The `>>> ` is the REPL's prompt. Type any Python expression, hit Enter, get the answer. `exit()` (or ctrl+D on Mac/Linux, ctrl+Z then Enter on Windows) leaves the REPL.

The REPL is your best friend when you're learning. *"Does this string method exist?"* — open the REPL, try it.

---

## 1.5 · Text editors

A **text editor** is software for writing plain-text files (`.py`, `.md`, `.csv`, `.json`, etc.). Word and Google Docs are NOT text editors — they save in a special format with bold and italic and fonts. Code files have to be pure text.

### Pick one

- **[VS Code](https://code.visualstudio.com/)** — free, popular, works on every OS. Has good Python support out of the box. This is the default we recommend.
- **[Cursor](https://www.cursor.com/)** — VS Code with built-in AI. Same interface, drops in.
- **[PyCharm Community](https://www.jetbrains.com/pycharm/download/)** — heavier, more "IDE-like." Free for personal use.

Install VS Code. Open it. Use **File → Open Folder** to open your `hello-python` folder. Notice the file tree on the left — that's your folder's contents.

### The 8 keyboard shortcuts worth memorizing

Same on all editors. These save weeks of your life over a few years.

| Shortcut | What it does |
|----------|--------------|
| ⌘/Ctrl + S | save the current file |
| ⌘/Ctrl + P | quick-open any file by name (start typing) |
| ⌘/Ctrl + F | find in current file |
| ⌘/Ctrl + Shift + F | find across the entire folder |
| ⌘/Ctrl + / | comment / uncomment the current line |
| ⌘/Ctrl + D | select next occurrence (great for renaming) |
| Tab / Shift+Tab | indent / unindent the selected lines |
| ⌘/Ctrl + ` (backtick) | toggle the integrated terminal |

That last one is huge. VS Code has a terminal built into the window. Cmd+backtick opens it, in the folder you're already working in. No window-switching.

---

## 1.6 · A small vocabulary of words that show up everywhere

These appear in tutorials with no explanation. Knowing what they mean removes mystery:

- **OS** — operating system. macOS, Windows, Linux, iOS, Android. The big software that runs the small software.
- **CLI** — command-line interface. Text-only programs you control by typing.
- **GUI** — graphical user interface. The one with buttons and icons.
- **Process** — a running program. When you run `python script.py`, a Python *process* is created, it does its work, then exits.
- **RAM** — your computer's short-term memory. Fast, small, gone when you turn the machine off. When your model "doesn't fit in memory," this is what's full.
- **Disk** (or *storage*) — your computer's long-term memory. Slow, big, permanent. When you "save a file," it goes to disk.
- **CPU** — the chip that does generic computation. Every laptop has one.
- **GPU** — a different chip that does parallel matrix math super fast. The reason ML models train at all in reasonable time.
- **URL** — the address of something on the internet. `https://example.com/page.html` is a URL.
- **HTTP / HTTPS** — the protocol for fetching web pages. The S is for secure (encrypted). When you load a URL, your browser makes an HTTP request.
- **API** — application programming interface. A way for one program to talk to another. Most modern APIs are HTTP — your code sends a request to a URL, the server sends back data (usually JSON).
- **JSON** — a text format for structured data. Looks like Python dicts with double quotes everywhere. We cover it in chapter 6.
- **UTF-8** — the standard way to encode text into bytes. *Always* save your files as UTF-8 (most editors default to this). Whenever you see a weird `'utf-8' codec can't decode` error, this is what's involved.
- **Open source** — code anyone can read and modify, usually on GitHub. Python is open source. PyTorch is open source. Most ML tooling is open source.
- **PR** (pull request) — a proposed change to an open-source project. You fork the repo, make changes, open a PR, the maintainers review and merge or reject.
- **Repo** (repository) — a project tracked in git. The thing you `git clone`.
- **Bash / zsh / PowerShell** — different shells (terminal programs). Their commands are mostly the same; small differences. You don't need to care which you have right now.

---

## 1.7 · Browser dev tools

Open your web browser. Press **F12** (or right-click anything on a page → "Inspect"). A panel opens.

This is the **browser dev tools**. Three tabs you'll actually use:

- **Elements** — the HTML / CSS of the current page. Click any element to see its underlying code.
- **Console** — a JavaScript REPL. Type `2 + 2`, press Enter, get `4`. This is where errors from broken websites show up.
- **Network** — every request the page is making. If a website is loading slowly or a button isn't working, this tab tells you which request is failing.

Why does this matter for ML? Because eventually you'll deploy a model behind a web interface, or fetch data from an API in a notebook, or debug why a chart isn't rendering. The dev tools are how you see what's actually happening in a browser.

Open them on this page right now. Click "Console". Type `console.log("hi")`. Hit Enter. You just wrote your first line of JavaScript.

---

## 1.8 · Git, the 30-second intro

**Git** is version control. It tracks every change to every file in a project, lets you go back to any past state, lets multiple people work on the same project without overwriting each other.

**GitHub** is a website that hosts git repositories. (There's also GitLab, Bitbucket, etc. — GitHub is the default for open-source.)

You only need 4 commands to start:

```
git clone <url>            # download a project from GitHub
git status                 # what changed since last commit?
git add <file>             # stage a file for the next commit
git commit -m "message"    # save staged changes as a commit
git push                   # upload commits to GitHub
```

We don't go deeper here — [`../foundations/`](../foundations/) has a full git track. For now, knowing these 4 commands exist is enough.

To make a GitHub account: go to [github.com](https://github.com), click Sign Up, follow the steps. Free.

---

## 1.9 · Practice — the 3 things to do before moving on

1. **Make a folder, make a file, run a Python script.** Don't proceed until you can do all three from the terminal without referencing this file. The muscle memory matters.

2. **Open the REPL and play for 10 minutes.** Type `2 + 2`. Type `"hello" * 5`. Type `[1, 2, 3] + [4, 5, 6]`. Be curious. Try things that *shouldn't* work and see what error you get. The errors are how you learn what the rules are.

3. **Open the python-and-dsa playground** at [`../prog/python-and-dsa/`](../prog/python-and-dsa/). It runs Python in your browser — no installs. Do Lesson 1 (Hello World) and Lesson 2 (Variables). 10 minutes total. You're now a Python programmer.

---

## Where to next

→ [02-math-zero.md](02-math-zero.md) — math fluency basics for the ML you're about to meet.

Or jump back to the [pre-foundations index](README.md).

---

## Further reading

- [w3schools Python intro](https://www.w3schools.com/python/python_intro.asp) — short, clean, has the "Try It" button.
- [w3schools Python install / get started](https://www.w3schools.com/python/python_getstarted.asp).
- [The Missing Semester of Your CS Education](https://missing.csail.mit.edu/) — the canonical "things every programmer is assumed to know but nobody teaches you." MIT, free. Spend a weekend on this eventually.
