# Method Summary

The project evaluated whether an LLM can follow rule-based legal dependency logic when its answers are checked against a symbolic formalization.

## Formal Ground Truth

The dependency rules were encoded as SMT constraints. Each legal scenario was translated into facts about age, relationship, residence, support, income, citizenship, and joint-return status. The solver produced one of three verdicts:

- `Yes`: the individual satisfies the dependency rule.
- `No`: the individual does not satisfy the dependency rule.
- `Ambiguous`: the available facts are insufficient to force one answer.

## Model Adaptation

Small language models were adapted with LoRA on preference-style examples. Each example used:

- a legal fact pattern as the prompt,
- a rule-consistent `chosen` answer,
- a plausible but incorrect or incomplete `rejected` answer.

The ablation compared adapters trained on 10, 20, and 50 examples.

## Evaluation

Model outputs were parsed into normalized verdicts and compared against SMT labels. This made the evaluation stricter than ordinary text similarity: a fluent answer only counted as correct if the final legal verdict matched the solver result.

The public code keeps the reusable parts of that evaluation workflow:

- verdict parsing,
- schema checks for private preference records,
- solver subprocess handling,
- summary table generation.
