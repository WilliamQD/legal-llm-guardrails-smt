# Presentation: Formal Guardrails for Legal LLMs

Project context: Yale course final project | CPSC 4151 | Public-safe presentation derivative

This is a recruiter-readable version of the project presentation. It is structured like a short slide deck without publishing private course examples or raw model outputs.

## Slide 1: Motivation

LLMs can produce plausible legal explanations while missing hard statutory boundaries. In legal or compliance settings, the final verdict needs to be checked against rule logic, not only reviewed for fluency.

## Slide 2: Core Idea

Use a symbolic solver as the ground-truth layer:

- encode legal dependency rules as SMT constraints,
- generate solver-backed verdicts,
- fine-tune small models on legal examples,
- parse model answers into verdicts,
- compare model verdicts against the solver.

## Slide 3: System Components

| Layer | Role |
|---|---|
| SMT formalization | Encodes eligibility logic and produces `Yes`, `No`, or `Ambiguous` labels |
| LoRA adapters | Tests whether small adapted models learn rule-following behavior |
| Verdict parser | Converts generated text into normalized classifications |
| Evaluation summary | Reports correct/error/ambiguous outcomes and failure modes |

## Slide 4: Experiment

The experiment compared LoRA adapters trained with 10, 20, and 50 examples. Each adapter was evaluated against held-out SMT-checked legal scenarios.

## Slide 5: Headline Result

| Adapter | Correct | Error | Ambiguous |
|---|---:|---:|---:|
| 10 examples | 3 | 2 | 1 |
| 20 examples | 3 | 2 | 1 |
| 50 examples | 2 | 3 | 1 |

More examples did not automatically improve rule-following behavior.

## Slide 6: Failure Modes

The model often over-predicted dependency and struggled with:

- income thresholds,
- age and student-status cutoffs,
- support conditions,
- genuinely ambiguous fact patterns.

## Slide 7: Takeaway

Formal checking is useful because it catches confident rule violations. The point is not to replace legal judgment with an SMT solver, but to add a grounded evaluation layer around model output.
