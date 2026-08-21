---
name: fin-notebook-structure
description: Structural template and authoring conventions for FIN4414 teaching notebooks in notebooks/. Use when creating a new course notebook, or reviewing/restructuring an existing one, to keep it consistent with Security_Returns_Properties.ipynb and Equity_Premium_Inference.ipynb.
---

# FIN4414 notebook structure

This course's notebooks (`notebooks/*.ipynb`) follow a shared template, established by
`Security_Returns_Properties.ipynb` and `Equity_Premium_Inference.ipynb` and applied to
`CAPM_BivariateRegression.ipynb`. New notebooks should follow it from the start; existing
notebooks that predate it should be brought into line when touched.

## Section order

1. **`# Title`** (H1, one per notebook) — a short paragraph or two on what the notebook
   covers and how it connects to prior notebooks/notes in the course (name them explicitly,
   e.g. "This draws on `notes/week01_...md` and `SampleMeanSimulation.ipynb`"). End with:

   `*Acknowledgment*: This notebook was produced with the assistance of AI. I remain responsible for the content and any errors.`

2. **`## Learning Objectives`** — "By the end of this notebook, you should be able to:"
   followed by a numbered list, each item starting with an action verb (Define, Explain,
   Derive, Compute, Estimate, Apply, Interpret, Simulate, ...). Aim for one item per major
   concept/skill in the notebook, roughly in the order they appear. If the notebook has an
   optional/advanced appendix, give it its own final objective prefixed `(Optional, ...)`.

3. **`## Instructions to Run`** — bold-labeled bullets covering:
   - **Data**: what file(s) or live data source are needed. If a local CSV: name it, say
     it's already in `data/` (small, redistributable extracts only), and note the
     boilerplate that non-redistributable data (e.g. licensed WRDS data) instead gets
     posted to the course Canvas site under Data. If pulled live (e.g. via
     `pandas_datareader`): say so explicitly and flag that an internet connection is
     required.
   - **If your data lives somewhere else**: which `pd.read_csv(...)` call(s) to edit,
     assuming the notebook lives in `notebooks/` and `data/` is a sibling folder.
   - **Package dependencies**: list them, note they're standard Anaconda packages except
     any that aren't, and give the `pip install ...` fallback.

4. **Motivating hook** — before diving into theory/derivations, ground the notebook in a
   concrete example or dataset (a real market event, a real anomaly) that motivates why the
   reader should care about the machinery that follows.

5. **Core content** — theory, derivations, and application, organized under `##`/`###`
   headers as needed. No fixed template here; follow the material.

6. **`## Takeaways`** — a short, bulleted synthesis of what the notebook actually showed
   (not a re-statement of the learning objectives), plus a closing pointer to where this
   connects in the next notebook/topic (a bolded lead-in like **Why this matters.** or
   **Where this goes next.** works well). This is the last required section of the main
   body — anything after it is appendix material.

7. **`## Additional Technical Material`** (only if there is any) — an appendix of proofs,
   derivations, or extensions that go beyond the notebook's core narrative or its listed
   prerequisites. Open with a one-line scope statement (e.g. "This appendix collects the
   technical details that were stated without proof in the main text above"). Use `###`
   subsections for each appendix item — the appendix header itself is the only `##` in
   this section. Anything that assumes background the course hasn't covered yet (e.g.
   matrix/vector algebra) needs an explicit, bolded warning saying so and that it's safe to
   skip — don't just label it "(Optional)" in the heading and leave it at that.

## Calibrating technical level

The audience is undergraduates who have had undergraduate probability/statistics and some
calculus and linear algebra — but treat linear algebra especially as a soft prerequisite,
not something to lean on by default. Write "Core content" (and any appendix) with this in
mind:

- **Lead with intuition, not notation.** Before a formula or proof, give the one- or
  two-sentence plain-English version of what it says and why it should be true, so the
  formal statement lands as confirming something the reader already half-expects rather
  than introducing it cold. (E.g. the McDonald's/diversification paragraph that motivates
  beta before the CAPM math in `CAPM_BivariateRegression.ipynb`, or the "what does this
  statement even mean?" gloss that follows the GRS formula.)
- **Don't skip steps in a derivation just because they're routine to us.** If a step is a
  few lines of algebra a student could follow — why a cross term vanishes when summed, why
  a substitution is valid, why a particular expectation is zero — show the few lines rather
  than jumping over them. "It can be shown that..." is for results that are genuinely out
  of scope, not a shortcut around a derivation step that's merely tedious.
- **Define, then immediately restate in plain language.** Whenever a new object shows up
  (a conditional expectation, a covariance matrix, a test statistic), give the formal
  definition and then a plain-words restatement tied to the running example, before moving
  on.
- **Verify results via simulation where practical, not proof alone.** This is already the
  pattern in `Equity_Premium_Inference.ipynb` (derive a result, then simulate to confirm it
  numerically) — simulation-based intuition lands better with this audience than a purely
  analytical argument, and it also catches derivation mistakes.
- **Matrix/vector notation belongs in the appendix, not the main narrative**, per the
  `## Additional Technical Material` guidance above — don't let a derivation quietly
  introduce it in the core content.

## Other conventions

- No stray trailing empty cells — clean these up before considering a notebook done.
- Before finalizing a notebook (and after any data refresh), do a clean **Restart Kernel &
  Run All**. This repo has had real drift where prose cited specific alpha/t-stat/CI
  numbers that were correct for an earlier data pull but silently went stale after the
  underlying data (or date range) changed — a full linear re-run makes it obvious that the
  narrative needs a matching pass, and catches non-monotonic execution counts left over
  from out-of-order editing.
- Prefer explaining a computed number's magnitude in prose loosely ("around half the
  portfolios", "on the order of several percentage points") over hardcoding many precise
  values that will drift out of sync with re-run output; where precise values are worth
  citing, re-derive/copy them from the actual latest output rather than typing from memory.
