# Publication Audit

This repository is a curated, no-data public portfolio version of the original course final project.

## Published

- Polished recruiter/interviewer-facing README.
- Rewritten method, results, privacy, and contribution notes.
- Public-safe Python utilities for verdict parsing, dataset schema validation, SMT subprocess execution, and Markdown result summaries.
- Synthetic unit tests that do not expose private course cases or datasets.

## Excluded

- Training datasets.
- Evaluation datasets.
- Instructor-provided held-out cases.
- SMT case files containing official fact patterns.
- Raw model generations.
- Adapter checkpoints and model files.
- Course submission metadata, student identifiers, grading language, and private instructions.

## Rationale

The goal is to demonstrate the project design and engineering quality without publishing course-private or potentially restricted content. The public repo therefore favors clean code, documentation, and aggregate result summaries over reproducibility from raw artifacts.
