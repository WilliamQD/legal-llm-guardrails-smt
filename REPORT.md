# Report: Formal Guardrails for Legal LLMs

Project context: Yale course final project | CPSC 4151 | Public-safe report derivative

This report summarizes the original final write-up in a public-safe format. It preserves the technical argument, methods, and results while omitting private identifiers, instructor-provided scenarios, raw model generations, and training/evaluation data.

## Abstract

Large language models can produce fluent legal explanations while missing hard rule boundaries. This project tested a guardrail pattern for that problem: represent legal dependency rules in an SMT-checkable form, use the solver as ground truth, adapt small language models with LoRA, and evaluate generated verdicts against solver-derived labels rather than text similarity.

The central result was not that more examples automatically improved legal reasoning. Adapters trained on 10 and 20 examples tied on the held-out set, while the 50-example adapter performed slightly worse. The important lesson was that formal checking exposed confident but rule-inconsistent answers that would be easy to miss in ordinary qualitative review.

## Problem

Legal and compliance workflows need more than fluent answers. A model can sound certain while overlooking an income threshold, age cutoff, student-status condition, support test, or ambiguity in the facts. The project therefore treated the legal verdict as a formal object that can be checked.

The task focused on dependency-rule scenarios under 26 U.S.C. 152(a)-(d). Each scenario was classified as:

- `Yes`: the facts force dependency eligibility.
- `No`: the facts rule out eligibility.
- `Ambiguous`: the available facts do not force either answer.

## Method

The pipeline had three stages.

1. **Formalization:** legal facts were translated into SMT constraints over age, relationship, residence, income, support, citizenship, and joint-return conditions.
2. **Model adaptation:** LoRA adapters were trained on small preference-style legal examples. The project compared 10-example, 20-example, and 50-example settings.
3. **Evaluation:** model outputs were parsed into normalized verdicts and compared against SMT labels on held-out scenarios.

The key design choice was to evaluate the final legal classification, not the polish of the explanation. This made the evaluation strict: a persuasive answer still counted as wrong if the verdict disagreed with the solver.

## Results

| Adapter | Correct | Error | Ambiguous |
|---|---:|---:|---:|
| 10 examples | 3 | 2 | 1 |
| 20 examples | 3 | 2 | 1 |
| 50 examples | 2 | 3 | 1 |

The 10-example and 20-example adapters performed identically on the held-out cases. The 50-example adapter flipped one previously correct case while still missing the hard negative cases.

## Error Analysis

The most consistent failure mode was over-predicting dependency. Models tended to answer `Yes` even when the formalization ruled out eligibility because of gross-income thresholds, age or student cutoffs, or support conditions.

Ambiguity was also difficult. In unresolved fact patterns, models often forced a determinate answer instead of recognizing that the available facts were insufficient.

## Discussion

The result argues for formal evaluation as a guardrail around legal LLM workflows. The solver does not make the model legally competent by itself, but it gives the system a clear external standard for whether the final verdict respects encoded rule logic.

The strongest engineering takeaway is that legal LLM evaluation should separate fluent explanation from rule-consistent classification. Without that separation, confident wrong answers can look acceptable.

## Public-Safe Scope

This public derivative omits:

- private course identifiers,
- instructor-provided or private held-out cases,
- training datasets,
- raw model generations,
- local/HPC paths,
- exact private prompts.

The repository includes reusable evaluation code patterns and rewritten documentation suitable for public portfolio review.
