# FIN 4414 — Fintech Capstone (Public Demo Repo)

This is a public companion repository for **FIN 4414**, a fintech capstone course. The
course is roughly half topic-oriented instruction (with graded assessments) and half
independent empirical research, culminating in a thesis-style paper with accompanying
replication code.

This repo is **not** a place for student submissions — all official course
submissions (papers, assessments, and links to student repos) are handled through
the course's Canvas site, per university policy. This repo exists to:

- Illustrate a sensible repo structure and workflow for an empirical finance research
  project — the same structure students are expected to use for their own thesis
  replication repos.
- Demonstrate how a tool like [Claude Code](https://claude.com/claude-code) can be used
  to manage code production, documentation, and repo hygiene throughout a research
  project.
- Host example notebooks and scripts referenced during the topic-oriented portion
  of the course.

Graded, in-class assessment materials are **not** included here, even though they're
part of the topic-oriented portion of the course — those stay in Canvas rather than
a public repo.

Student thesis repos should be **private** (e.g., via GitHub Classroom, with the
instructor added as a collaborator), not public — see the note on data below for why
that matters. Students submit a link to their repo (and their paper) through Canvas;
the repo itself is never the system of record for the submission.

## Repo structure

```
data/          Small example datasets used in notebooks and scripts. See
               "A note on data" below — most data is intentionally NOT tracked here.
html/          Static HTML exports of the notebooks in notebooks/, for quick viewing
               without running Jupyter. Regenerated from the notebooks, not
               hand-edited. Currently committed by hand after each notebook
               change; may move to a script/CI step that regenerates these
               automatically instead of tracking them in git.
notebooks/     Jupyter notebooks (Python and/or R) covering course topics.
notes/         Weekly conceptual notes (Markdown) for the topic-oriented portion
               of the course, cross-referencing the notebooks where relevant.
python/        Reusable Python modules/utilities shared across notebooks and scripts.
```

## A note on data

Empirical finance research draws on data with very different rules about
redistribution, and this repo is meant to model good practice around that:

- **Public-domain sources** (e.g., FRED — the Federal Reserve's economic data
  service) can be committed to the repo when the file is small. A handful of small
  example FRED extracts may be tracked here for convenience.
- **Freely available market data** (e.g., daily closing prices for publicly traded
  ETFs, retrieved from Yahoo Finance) can also be committed when the extract is
  small. This isn't "public domain" in the same formal sense as FRED, but a small,
  illustrative extract of daily closing prices carries no redistribution
  restriction the way a WRDS pull does.
- **Larger datasets**, even from public sources, are intentionally left **untracked**
  to keep the repo lean — this is itself a practice worth learning: keep raw/large
  data out of version control and instead version the code that generates or
  downloads it.
- **Licensed data** (e.g., pulled from WRDS — CRSP, Compustat, etc.) is **never**
  committed, regardless of file size. Redistribution of WRDS-sourced data is
  generally prohibited under the license terms your institution holds, independent
  of how small or processed the extract is. Instead, this repo versions the *code*
  used to pull that data (e.g., a script using the `wrds` Python package), so the
  pull is reproducible by anyone with their own authorized WRDS access — without
  ever redistributing the data itself.

See `.gitignore` for how this is enforced in practice.

### Files currently tracked in `data/`

- `uso_etf_daily.csv` — daily closing prices for USO (the United States Oil
  Fund, an ETF designed to track the spot price of WTI crude oil), August 2020
  through the present. Retrieved from Yahoo Finance. Used by
  `notebooks/Security_Returns_Properties.ipynb`.
- `spy_etf_daily.csv` — daily closing prices for SPY (the SPDR S&P 500 ETF
  Trust), August 2020 through the present. Retrieved from Yahoo Finance. Used
  by `notebooks/Security_Returns_Properties.ipynb`.

## License

Code in this repository is released under the MIT License (see `LICENSE`) unless
noted otherwise. This does not apply to any data files, which retain the license
terms of their original source.
