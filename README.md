# Formal Guardrails for Legal LLMs

SMT-checked evaluation pipeline for testing whether LoRA-adapted language models follow rule-based legal dependency logic.

![Python](https://img.shields.io/badge/Python-evaluation-blue)
![SMT](https://img.shields.io/badge/SMT-rule_checking-purple)
![LoRA](https://img.shields.io/badge/LoRA-adapter_eval-orange)
![Public safe](https://img.shields.io/badge/Public--safe-no_data-green)

Project context: Yale course final project | CPSC 4151 | Curated public showcase

This portfolio repo is a curated, no-data version of the final project. It is designed to show the engineering and evaluation approach without publishing private course materials, instructor-provided cases, raw model outputs, or training/evaluation datasets.

**Read the deliverables:** [Report](REPORT.md) | [Presentation](PRESENTATION.md)

## At a Glance

<table>
  <tr>
    <td><strong>Problem</strong><br>Legal LLMs can sound confident while violating formal rule logic.</td>
    <td><strong>Approach</strong><br>Use SMT verdicts as ground truth, then score model outputs against solver-checked labels.</td>
    <td><strong>Signal</strong><br>More examples did not automatically improve borderline rule reasoning.</td>
  </tr>
</table>

## Overview

Large language models can produce confident legal answers even when the underlying rule logic is wrong. This project explored a guardrail pattern for that problem: use a symbolic solver as the source of truth, then compare model behavior against solver-checked verdicts.

The original project formalized dependency rules under 26 U.S.C. 152(a)-(d), generated preference-style training data, fine-tuned small language models with LoRA, and evaluated their outputs against SMT-derived labels on held-out legal scenarios.

## Why This Matters

Legal and compliance workflows are risky places to rely on fluent text alone. A useful AI system needs a way to separate plausible language from rule-consistent reasoning. This project demonstrates one version of that pattern:

- encode rule logic in a formal system,
- use the solver to produce ground-truth verdicts,
- fine-tune models on structured legal examples,
- parse model outputs into stable verdict classes,
- compare model answers against the solver rather than against vibes.

## My Contribution

I built the project pipeline end to end for the course deliverable:

- formalized dependency-rule scenarios with SMT constraints,
- constructed preference-style examples for LoRA supervised fine-tuning,
- trained small/medium/large data ablations,
- wrote evaluation code to parse model outputs and compare them with SMT verdicts,
- summarized model failure patterns and wrote the final analysis.

## Technical Approach

The project used three layers.

1. **Formal layer:** SMT constraints represented eligibility rules and produced `Yes`, `No`, or `Ambiguous` verdicts.
2. **Modeling layer:** TinyLlama adapters were trained with LoRA on preference-formatted legal examples.
3. **Evaluation layer:** model generations were parsed into verdicts and compared against solver outputs.

The public code in this repo focuses on the reusable evaluation layer and public-safe interfaces. The private datasets and official held-out cases are intentionally omitted.

## Headline Results

The final evaluation compared three LoRA adapters trained on 10, 20, and 50 examples against six held-out SMT-checked legal scenarios.

| Adapter | Correct | Error | Ambiguous |
|---|---:|---:|---:|
| 10 examples | 3 | 2 | 1 |
| 20 examples | 3 | 2 | 1 |
| 50 examples | 2 | 3 | 1 |

The main finding was not "more data always helps." The larger adapter did not improve the difficult borderline cases and over-predicted dependency on examples involving income, support, age, and student-status cutoffs. The strongest lesson was that formal evaluation exposed failure modes that sounded legally confident but were rule-inconsistent.

## Repository Structure

```text
REPORT.md          # public-safe report derivative
PRESENTATION.md    # public-safe presentation derivative
src/guardrail_eval/
  verdicts.py       # parse model verdicts and score against SMT labels
  schema.py         # validate private preference datasets without publishing them
  smt_interface.py  # run local Z3/SMT files and normalize solver status
  summary.py        # produce Markdown summary tables
tests/
  test_guardrail_eval.py
docs/
  methods.md
  results_summary.md
  privacy.md
  contribution_note.md
data/
  README.md         # explains why no datasets are published
```

## Run the Public Checks

The public test suite uses synthetic strings only.

```bash
python -m pytest tests
```

The original training stack used PyTorch, Hugging Face Transformers, PEFT, Accelerate, and BitsAndBytes on an HPC/GPU environment. Those heavyweight training artifacts are not required for this showcase repo.

## Data and Privacy

No training datasets, held-out instructor cases, model generations, or official course materials are published here. The public files are limited to rewritten documentation and reusable code patterns that can be inspected without exposing private data.

See [docs/privacy.md](docs/privacy.md) for details.

## Skills Demonstrated

- LLM evaluation and guardrail design
- Formal methods / SMT-based rule checking
- LoRA fine-tuning workflow design
- Python evaluation tooling
- Dataset schema validation
- Error analysis for rule-based reasoning
- Public-safe technical documentation
