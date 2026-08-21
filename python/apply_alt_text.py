"""Patch <img alt="..."> attributes into an nbconvert HTML export.

nbconvert's default "lab" HTML template never emits an `alt` attribute for
image/png outputs, so every plot in a notebook export ends up with the
generic placeholder "No description has been provided for this image" --
a WCAG 1.1.1 (Level A) failure. This script fixes that after the fact,
without changing which nbconvert template is used.

Alt text is sourced from `cell.metadata["alt"]` on each *code* cell that
produces a plot -- see the "Accessibility" section of
.claude/skills/fin-notebook-structure/SKILL.md for how that metadata should
be set and written. Every code cell producing an image/png output must carry
one; the script fails loudly if any is missing, or if the number of <img>
tags in the HTML doesn't match the number of images found in the notebook
(e.g. because a cell produces more than one figure).

Usage:
    python python/apply_alt_text.py notebooks/Foo.ipynb html/Foo.html
"""
import json
import sys

from bs4 import BeautifulSoup


def image_alt_texts(nb_path):
    """Return the alt text for every image/png output in the notebook, in
    the same top-to-bottom order nbconvert renders them in."""
    nb = json.load(open(nb_path, encoding="utf-8"))
    alts = []
    for cell in nb["cells"]:
        if cell["cell_type"] != "code":
            continue
        n_images = sum(
            1
            for o in cell.get("outputs", [])
            if o.get("output_type") in ("display_data", "execute_result")
            and "image/png" in o.get("data", {})
        )
        if n_images == 0:
            continue
        alt = cell.get("metadata", {}).get("alt")
        if not alt:
            src_preview = "".join(cell["source"])[:60].replace("\n", " ")
            raise SystemExit(
                f"{nb_path}: code cell producing an image has no "
                f"metadata['alt']: {src_preview!r}..."
            )
        alts.extend([alt] * n_images)
    return alts


def apply_alt_text(nb_path, html_path):
    alts = image_alt_texts(nb_path)
    soup = BeautifulSoup(open(html_path, encoding="utf-8").read(), "html.parser")
    imgs = soup.select("img")
    if len(imgs) != len(alts):
        raise SystemExit(
            f"{html_path}: found {len(imgs)} <img> tag(s) but {len(alts)} "
            f"alt text(s) from {nb_path} -- check for non-plot images, or "
            f"a cell producing more than one figure."
        )
    for img, alt in zip(imgs, alts):
        img["alt"] = alt
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(str(soup))
    print(f"Patched {len(imgs)} image alt text(s) in {html_path}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("usage: python apply_alt_text.py <notebook.ipynb> <export.html>")
    apply_alt_text(sys.argv[1], sys.argv[2])
