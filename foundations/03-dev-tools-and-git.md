# 03 · Dev tools and Git

← previous: [02-coding-projects.md](02-coding-projects.md) · next: [foundations README](README.md) → then [`../math/`](../math/)

Pre-foundations showed you what a terminal *is* and got Python installed. This chapter makes you fluent: moving around the terminal without thinking, and using Git to save your work, undo mistakes, and put your three projects on the internet.

This is the least glamorous chapter and the one that pays off daily forever. Every ML job, every open-source repo, every "clone this and run it" assumes you have this. You'll use Git more than you use calculus.

By the end, projects from chapter 2 will be live on your own GitHub.

---

## 3.1 · Terminal, for real this time

A terminal is a text box that runs commands in a folder. The "current folder" is everything — commands act where you're standing.

The core moves. These work on Mac and Linux as-is; on Windows, PowerShell understands `cd`, `ls`, `mkdir`, `cp`, `mv`, `rm` too (they're aliases), so the same vocabulary carries:

```
pwd                 print working directory — "where am I?"
ls                  list what's in this folder
ls -la              list everything, including hidden files, with detail
cd projects         change directory into "projects"
cd ..               go up one level
cd ~                go to your home folder
mkdir ml            make a new folder called "ml"
touch notes.txt     create an empty file   (PowerShell: ni notes.txt)
cp a.py b.py        copy a.py to b.py
mv old.py new.py    move/rename
rm junk.txt         delete a file          (no undo — be sure)
```

Three habits that separate comfortable from flailing:

- **Tab completion.** Type the first few letters of a name and hit `Tab`. The terminal finishes it. This isn't a shortcut, it's how everyone actually types — and it stops typos in long paths.
- **Up arrow** re-runs your last command. Hit it a few times to walk back through history.
- **`Ctrl+C`** cancels whatever's running and gives you the prompt back. Your escape hatch.

You don't need to memorize a hundred commands. These ten plus tab-completion cover ninety percent of real use. The rest you look up the day you need them.

---

## 3.2 · Git: the mental model

Git is a **time machine for a folder.** It saves snapshots of your project, each one labeled, so you can see what changed, undo anything, and never lose work to a bad edit.

The vocabulary, in the order you'll use it:

- **Repository (repo)** — a folder Git is tracking.
- **Commit** — one saved snapshot, with a message describing it.
- **Staging** — the waiting room. You pick which changes go into the next commit.
- **Remote** — a copy living elsewhere, usually GitHub.

Here's the whole everyday loop. Inside your project folder:

```
git init                       turn this folder into a repo  (once, ever)
git status                     what's changed? what's staged?
git add calc.py                stage one file
git add .                      stage everything changed
git commit -m "Add calculator" save a snapshot with a message
git log --oneline              see your history, one line each
```

The rhythm is **edit → `add` → `commit`**, over and over. Each commit is a save point you can return to. `git status` is your most-used command — run it constantly, it tells you exactly where you are.

Write commit messages a human can read. `"Add divide-by-zero guard"` tells future-you what happened. `"stuff"` and `"fix"` tell you nothing. You'll thank yourself in a month.

### The one file everyone forgets: `.gitignore`

Some things should never be committed — virtual environments, secret keys, huge data files, editor clutter. List them in a file called `.gitignore` and Git pretends they don't exist:

```
.venv/
__pycache__/
*.pyc
.env
.DS_Store
```

Make this file before your first commit. Committing a `.venv` folder or an API key is a rite-of-passage mistake. Skip the rite.

---

## 3.3 · GitHub: put it on the internet

Git runs on your machine. **GitHub** is the website that hosts a copy so others (and future employers) can see it, and so you have a backup.

One-time setup:

1. Make a free account at [github.com](https://github.com).
2. Create a new **empty** repository (no README, no `.gitignore` — you already have your files locally). Call it `python-projects`.
3. GitHub shows you the commands. They look like this:

```
git remote add origin https://github.com/YOUR-NAME/python-projects.git
git branch -M main
git push -u origin main
```

`remote add origin` tells your local repo where the GitHub copy lives. `push` uploads your commits. The `-u origin main` part wires them together so that next time you can just type `git push`.

From then on, the loop gains one step: **edit → `add` → `commit` → `push`.** Push whenever you want the GitHub copy caught up.

> **Authentication note:** GitHub no longer takes your password on the command line. The smoothest path is the [GitHub CLI](https://cli.github.com/) — install it, run `gh auth login`, and it handles the rest. Or set up an SSH key ([GitHub's guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)). Five minutes of setup, never think about it again.

Do this now with your three projects from chapter 2. Having real code on GitHub is the single most useful thing in this whole folder — it's your portfolio's first brick.

---

## 3.4 · Branches, lightly

A **branch** is a parallel copy where you can try something risky without touching your working version.

```
git checkout -b experiment    create a branch and switch to it
...edit, add, commit...        work freely
git checkout main             switch back — your experiment vanishes from view
git merge experiment          fold the experiment's commits into main
```

If the experiment was a dead end, you just stay on `main` and delete the branch. Nothing lost.

You don't need branches for solo projects yet. But the moment you collaborate, or contribute to an open-source repo, this is the workflow: branch, change, open a **pull request** (a "please merge my branch" proposal) on GitHub. Know it exists; you'll learn it deeply the first time you use it for real.

---

## 3.5 · VS Code: ten keybindings

You'll live in your editor. Learning a handful of keys turns it from a fancy notepad into a power tool. (Mac uses `Cmd`; Windows and Linux use `Ctrl`.)

```
Cmd/Ctrl + P            quick-open any file by typing its name
Cmd/Ctrl + Shift + P    command palette — every command, searchable
Cmd/Ctrl + /            comment / uncomment the current line
Cmd/Ctrl + D            select the next copy of the word (multi-cursor magic)
Cmd/Ctrl + F            find in this file
Cmd/Ctrl + S            save
Alt + ↑ / ↓             move the current line up or down
Cmd/Ctrl + `            open / close the built-in terminal
F2                      rename a variable everywhere at once
Cmd/Ctrl + B            toggle the sidebar for more screen
```

The two that change your life first: **`Cmd/Ctrl+P`** (jump to any file instantly, stop hunting in the sidebar) and **`Cmd/Ctrl+`` `** (terminal and editor in one window, no alt-tabbing).

Install the **Python extension** from Microsoft while you're here. It adds error squiggles, autocomplete, and a run button. For data work later, add the **Jupyter** extension too.

---

## Do these before moving on

You're ready for [`../math/`](../math/) and the rest of the map when you can, without notes:

- [ ] `cd` into a folder and `ls` its contents, using tab-completion.
- [ ] Take a fresh folder from `git init` to a first commit.
- [ ] Explain the difference between `add` and `commit` in one sentence each.
- [ ] Have your three chapter-2 projects pushed to a public GitHub repo.
- [ ] Write a commit message that would make sense to a stranger.
- [ ] Open a file in VS Code with `Cmd/Ctrl+P` instead of the mouse.

Last box checked? That's the foundations track done. Everything above this — `math/`, `prog/`, `classical/` — assumes exactly these reflexes and nothing more.

---

## Where to next

This is the end of foundations. Two doors:

→ [`../math/`](../math/) — calculus, linear algebra, probability. The real curriculum starts here. (The [YouTube calculus series](https://siddhant-rajhans.github.io/ml-roadmap/) is the companion.)

→ [`../prog/`](../prog/) — if you'd rather build coding muscle first: object-oriented Python, NumPy, Pandas, and the [python-and-dsa playground](../prog/python-and-dsa/).

Either is a fine next step. Check the [paths](../paths/) folder if you want a guided order.

---

## Further reading

- [Pro Git book](https://git-scm.com/book/en/v2) — free, official, the definitive reference. Read chapters 1–3.
- [Oh My Git!](https://ohmygit.org/) — a free game that teaches Git visually. Genuinely fun.
- [GitHub Skills](https://skills.github.com/) — short hands-on courses run inside real repos.
- [MIT's Missing Semester](https://missing.csail.mit.edu/) — the terminal, shell, and tooling class no CS degree teaches. Worth every hour.
- [VS Code keyboard shortcuts (PDF)](https://code.visualstudio.com/docs/getstarted/keybindings) — the full printable cheat sheet.
