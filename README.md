# Research Compendium

*A living series of scholarly reviews, technical notes, and curated references in theoretical and experimental physics.*

[Review catalog](CATALOG.md) · [Editorial policy](EDITORIAL.md) · [Roadmap](ROADMAP.md) · [Bibliography](bibliography/README.md)

## Principle

**A paper is an argument, not a pile of citations.** Each review starts with a sharply defined question, establishes notation and admissible evidence, distinguishes measurement from inference, exposes assumptions, and makes unresolved questions explicit. The documents are versioned, independently compilable, and linked to a shared bibliography.

The main areas are nuclear reactions, few-body scattering, interaction constraints, and particle correlations. The scope can grow without changing the basic structure.

## Start here / 快速开始

Requirements: TeX Live with `latexmk` and `biber`, plus GNU Make and Python 3.

```bash
make list
make tt-scattering         # reviews/tt-scattering/main.pdf
make femtoscopy            # reviews/femtoscopy/main.pdf
make all                   # automatically build all review directories
make new TOPIC=effective-range TITLE="Effective-range theory"
```

TeX sources are the source of truth; PDFs are generated outputs and are not committed. Every LaTeX-changing push to `main` and pull request triggers GitHub Actions PDF builds, and compiled PDFs are attached as downloadable workflow artifacts.

### Local GitHub setup (first time only)

With an authenticated GitHub CLI, creation and push take one command:

```bash
gh repo create tianbaiting/research-compendium --private --source=. --remote=origin --push
```

Alternatively, create an **empty private** repository named `research-compendium` in your GitHub account (do not initialize with a README, license, or `.gitignore`). From this directory:

```bash
git remote add origin git@github.com:tianbaiting/research-compendium.git
git push -u origin main
```

Use an HTTPS remote instead if SSH keys are not configured.

## Architecture

```text
research-compendium/
├── CATALOG.md                     # review index and maturity status
├── EDITORIAL.md                   # evidence and citation standards
├── ROADMAP.md                      # research agenda
├── bibliography/
│   ├── references.bib             # shared, audited BibLaTeX metadata
│   └── README.md                  # provenance and reuse policy
├── tex/
│   ├── preamble.tex               # uniform typesetting
│   └── macros.tex                 # notation / mathematical operators
├── notes/                         # short research derivations
├── reviews/
│   ├── tt-scattering/             # evolving t–t interaction review
│   │   ├── main.tex
│   │   └── sections/
│   └── femtoscopy/                # source–interaction inference
│       ├── main.tex
│       └── sections/
├── templates/review/              # compilable new-review template
├── scripts/new_review.py          # create a review with one command
├── .github/workflows/latex.yml   # CI build and PDF artifacts
└── Makefile
```

## Review lifecycle

`outline` → `working` → `reviewed` → `stable` (and back to `working` when substantive new evidence arises). A status describes editorial maturity, **not** peer review or correctness. Each review should maintain a dated changelog, definitions, an evidence table, a systematic-uncertainty discussion, and an explicit list of unresolved questions.

## Reference and copyright policy

This is **not a mirror of publisher PDFs**. Store DOI/arXiv/publisher links and original notes here. Only redistribute full-text files when the license explicitly permits it. Bibliographic metadata should be checked against an authoritative source and should not be synthesized from memory. See [bibliography/README.md](bibliography/README.md).

## How to contribute

Commit small, traceable changes; use stable citation keys; record the origin of numerical claims and digitized data. Propose new topics in `ROADMAP.md` and implement them with `make new` (new reviews are discovered automatically). Do not add a physical claim without a traceable reference or clear derivation.
