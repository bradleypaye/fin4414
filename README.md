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
- Host example notebooks, scripts, and assessment materials referenced during the
  topic-oriented portion of the course.

Student thesis repos should be **private** (e.g., via GitHub Classroom, with the
instructor added as a collaborator), not public — see the note on data below for why
that matters. Students submit a link to their repo (and their paper) through Canvas;
the repo itself is never the system of record for the submission.

## Repo structure

```
assessments/   Example quizzes, coding exercises, and rubrics used in the
               topic-oriented portion of the course.
data/          Small example datasets used in notebooks and scripts. See
               "A note on data" below — most data is intentionally NOT tracked here.
notebooks/     Jupyter notebooks (Python and/or R) covering course topics.
python/        Reusable Python modules/utilities shared across notebooks and scripts.
```

## A note on data

Empirical finance research draws on data with very different rules about
redistribution, and this repo is meant to model good practice around that:

- **Public-domain sources** (e.g., FRED — the Federal Reserve's economic data
  service) can be committed to the repo when the file is small. A handful of small
  example FRED extracts may be tracked here for convenience.
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

## License

Code in this repository is released under the MIT License (see `LICENSE`) unless
noted otherwise. This does not apply to any data files, which retain the license
terms of their original source.
