# Editorial and Reproducibility Policy

## I. Evidence, not accumulation

A review should distinguish: **primary observation** (measured counts/observables), **data reduction** (acceptance, calibration, fit), **phenomenological extraction** (model-dependent parameter), and **theoretical prediction** (Hamiltonian, solver, regulator, approximation). A review may disagree with a paper; the reason must be technical and checkable.

## II. Minimum review anatomy

1. **Problem statement:** observable, energy domain, symmetries, channels, and why the question matters.
2. **Conventions:** frames, momentum definitions, normalizations, boundary conditions, signs, units, and channel labels.
3. **Evidence register:** bibliographic reference, experiment, observable, cuts and acceptance, published numerical result, and extraction method.
4. **Theory comparison:** interaction model, parameter space, two- or three-body dynamics, long-range forces, numerical convergence.
5. **Inference ledger:** what is *measured*, what is *fit*, what is *assumed*, and what can genuinely be bounded.
6. **Open questions:** prioritized measurements and calculations that could change the conclusion.
7. **Change history:** date, conceptual change, citation/figure change, and reason.

## III. Claim taxonomy

Annotate uncertain passages in source comments with `% EVIDENCE: needed`, `% CHECK: convention`, `% TODO: digitization`, or `% DERIVATION: ...`. Never fill a missing reference with an approximate or guessed citation. Avoid giving a precise scattering length or effective range without specifying Coulomb convention and fit domain.

## IV. Figures and data

- Figures must have their origin, author/permission, transform steps, and digitization uncertainty documented.
- Generated plots should come from an executable script with recorded units and input provenance.
- Raw experimental data and publisher PDFs normally live outside the public Git repository.
- Never confuse a citation to an experimental study with independent verification of its derived parameters.

## V. LaTeX and bibliography

- Prefer clear definitions and explicit equations over decorative prose.
- Use `\label`, `\cref`, `\cite`, `\doi`/`\url`, and `\printbibliography` so the final PDF has functional navigation.
- Central `bibliography/references.bib` is authoritative. Keys are stable; document title/DOI corrections in commits.
- Compile every active review in CI. The template must compile too.

## VI. Publishing

Default to **private** while source material and author permissions are audited. To publish, review every added asset for copyright, unpublished collaboration results, personal notes, and confidential data. The absence of a LICENSE is intentional until publication terms are chosen.
