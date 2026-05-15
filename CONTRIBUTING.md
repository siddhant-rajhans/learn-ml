# Contributing

Thanks for considering a contribution. A few ground rules to keep the curriculum coherent.

## What we welcome

- **Clarifications and typo fixes.** Open a PR directly.
- **New worked exercises** with solutions. Open an issue first to coordinate.
- **Notebook improvements** — clearer narrative, better visuals, faster execution.
- **Translations.** Open an issue with your target language; we'll set up a `translations/<lang>/` branch.
- **Bug reports** on notebooks (especially Colab compatibility regressions).

## What's out of scope

- **Restructuring the curriculum order.** The phase order is opinionated; debates belong in an issue, not a PR.
- **Adding new specializations to Phase 5** without prior discussion. Phase 5 is the easiest place to bloat.
- **Marketing changes** (logos, taglines, repo descriptions).

## PR checklist

- [ ] One concern per PR. Don't bundle a typo fix with a new exercise.
- [ ] If you touched a notebook, it runs top-to-bottom on a fresh kernel.
- [ ] If you added an exercise, you also added the solution.
- [ ] Your changes preserve the visual-first philosophy — if you're replacing a diagram with prose, expect pushback.

## Style

- **Math notation:** LaTeX in markdown. Inline `$...$`, display `$$...$$`. Avoid plain-text math.
- **Code:** Python 3.11+. Type hints encouraged in library code, not required in notebooks.
- **Plots:** matplotlib for static, Plotly for interactive. Three.js / R3F visuals belong in [ml-visuals](https://github.com/siddhant-rajhans/ml-visuals), not here.
- **Notebooks:** every notebook starts with a "Why this notebook exists" cell and ends with "What you should be able to do now."

## Code of conduct

Be kind. Bad-faith arguments, dunking on beginners, or condescending corrections will get the PR closed without discussion.
